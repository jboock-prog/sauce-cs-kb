"""Single-worker durable queue for replies in the configured Slack channel."""

import json
import os
import re
import sqlite3
import threading
from contextlib import contextmanager
from pathlib import Path

import requests


class ChannelAnswers:
    def __init__(self, path, channel, token, ask):
        self.path = path
        self.channel = channel
        self.token = token
        self.ask = ask
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with self.db() as db:
            db.execute('''CREATE TABLE IF NOT EXISTS channel_questions (
                id TEXT PRIMARY KEY, channel TEXT, ts TEXT, user TEXT, question TEXT,
                answer TEXT, state TEXT NOT NULL)''')
            # Generation is safe to repeat. An interrupted POST is ambiguous: do not repost.
            db.execute("UPDATE channel_questions SET state='pending' WHERE state='generating'")
            db.execute("UPDATE channel_questions SET state='delivery_unknown' WHERE state='posting'")

    @contextmanager
    def db(self):
        db = sqlite3.connect(self.path, timeout=0.5)
        try:
            with db:
                yield db
        finally:
            db.close()

    def accept(self, payload):
        event = payload.get('event')
        if not isinstance(event, dict):
            return
        if (
            event.get('channel') != self.channel
            or event.get('type') not in ('message', 'app_mention')
            or event.get('bot_id')
            or event.get('app_id')
            or event.get('subtype')
            or not event.get('user')
            or not event.get('ts')
            or (event.get('thread_ts') and event['thread_ts'] != event['ts'])
        ):
            return

        text = event.get('text', '').strip()
        if not text:
            return

        # Both app_mention and message events can describe the same message.
        key = self.channel + ':' + event['ts']
        with self.db() as db:
            db.execute(
                'INSERT OR IGNORE INTO channel_questions VALUES (?,?,?,?,?,?,?)',
                (key, self.channel, event['ts'], event['user'], text, '', 'pending'),
            )

    def process_one(self):
        with self.db() as db:
            row = db.execute(
                "SELECT id,channel,ts,user,question,answer,state "
                "FROM channel_questions WHERE state IN ('pending','ready') "
                "ORDER BY ts LIMIT 1"
            ).fetchone()
            if not row:
                return False
            key, channel, ts, user, question, answer, state = row
            if state == 'pending':
                db.execute("UPDATE channel_questions SET state='generating' WHERE id=?", (key,))

        if state == 'pending':
            try:
                answer = self.ask(
                    'The following is a new human post in the KB help channel. '
                    'If it is not a question or a request for help (for example a greeting, '
                    'thanks, or announcement), respond with exactly __NO_REPLY__. '
                    'Otherwise answer the question using the KB and cite the relevant entry titles. '
                    'Do not claim to have performed actions.\n\nChannel post:\n' + question,
                    route='/slack/events',
                    user_name=user,
                    metadata={
                        'slack_user_id': user,
                        'slack_channel_id': channel,
                        'message_ts': ts,
                    },
                )
                next_state = 'skipped' if answer.strip() == '__NO_REPLY__' else 'ready'
                with self.db() as db:
                    db.execute(
                        'UPDATE channel_questions SET answer=?,state=? WHERE id=?',
                        (answer, next_state, key),
                    )
                if next_state == 'skipped':
                    return True
            except Exception as exc:
                self.finish(key, 'query_failed', type(exc).__name__)
                return True

        with self.db() as db:
            db.execute("UPDATE channel_questions SET state='posting' WHERE id=?", (key,))

        try:
            # Suppress generated @channel/@here and user mentions in public replies.
            answer = re.sub(r'<!(?:channel|here|everyone)>', '[mention omitted]', answer)
            answer = re.sub(r'<@[A-Z0-9]+>', '[user]', answer)
            response = requests.post(
                'https://slack.com/api/chat.postMessage',
                headers={'Authorization': 'Bearer ' + self.token},
                json={
                    'channel': channel,
                    'thread_ts': ts,
                    'text': answer,
                    'unfurl_links': False,
                    'unfurl_media': False,
                    'parse': 'none',
                },
                timeout=15,
            )
            result = response.json()
            self.finish(
                key,
                'delivered' if response.ok and result.get('ok') else 'delivery_failed',
                result.get('error'),
            )
        except Exception as exc:
            self.finish(key, 'delivery_unknown', type(exc).__name__)
        return True

    def finish(self, key, state, error=None):
        with self.db() as db:
            db.execute('UPDATE channel_questions SET state=? WHERE id=?', (state, key))
        print(json.dumps({
            'event': 'kb_channel_answer',
            'message_id': key,
            'status': state,
            'error_type': error,
        }), flush=True)

    def start(self):
        def run():
            while True:
                try:
                    if self.process_one():
                        continue
                except Exception as exc:
                    print(json.dumps({
                        'event': 'kb_channel_worker_error',
                        'error_type': type(exc).__name__,
                    }), flush=True)
                threading.Event().wait(1)

        threading.Thread(target=run, name='kb-channel-answers', daemon=True).start()


def configure_channel_answers(ask):
    channel = os.environ.get('KB_AUTO_REPLY_CHANNEL_ID', '')
    token = os.environ.get('SLACK_BOT_TOKEN', '')
    if not channel or not token:
        return None

    worker = ChannelAnswers(
        os.environ.get('KB_EVENTS_DB', '/data/slack-events.sqlite3'),
        channel,
        token,
        ask,
    )
    worker.start()
    return worker.accept
