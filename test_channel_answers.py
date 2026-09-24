import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from channel_answers import ChannelAnswers


class ChannelTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.ask = Mock(return_value='Answer citing GEN-1')
        self.worker = ChannelAnswers(
            str(Path(self.temp.name) / 'events.sqlite3'),
            'C_TARGET',
            'test',
            self.ask,
        )

    def tearDown(self):
        self.temp.cleanup()

    def event(self, **changes):
        event = {
            'type': 'message',
            'channel': 'C_TARGET',
            'ts': '123.456',
            'user': 'U1',
            'text': 'How do I help?',
        }
        event.update(changes)
        return {'event': event}

    def test_channel_bot_thread_and_subtype_filters(self):
        for event in [
            self.event(channel='C_OTHER'),
            self.event(bot_id='B1'),
            self.event(subtype='message_changed'),
            self.event(thread_ts='100.000'),
            self.event(text=''),
            self.event(user=''),
        ]:
            self.worker.accept(event)
        self.assertFalse(self.worker.process_one())
        self.ask.assert_not_called()

    def test_dedup_restart_and_thread_delivery(self):
        self.worker.accept(self.event())
        self.worker.accept(self.event(type='app_mention'))
        self.worker = ChannelAnswers(self.worker.path, 'C_TARGET', 'test', self.ask)
        with patch(
            'channel_answers.requests.post',
            return_value=Mock(ok=True, json=lambda: {'ok': True}),
        ) as post:
            self.assertTrue(self.worker.process_one())
            self.assertFalse(self.worker.process_one())
            self.assertEqual(post.call_count, 1)
            self.assertEqual(post.call_args.kwargs['json']['thread_ts'], '123.456')
            self.assertEqual(post.call_args.kwargs['json']['channel'], 'C_TARGET')

        self.worker.accept(self.event())
        self.assertFalse(self.worker.process_one())

    def test_no_reply_for_non_question_and_ambiguous_delivery_not_reposted(self):
        self.ask.return_value = '__NO_REPLY__'
        self.worker.accept(self.event(text='Thanks'))
        with patch('channel_answers.requests.post') as post:
            self.worker.process_one()
            post.assert_not_called()

        self.ask.return_value = 'Answer'
        self.worker.accept(self.event(ts='124.000'))
        with patch('channel_answers.requests.post', side_effect=TimeoutError):
            self.worker.process_one()

        restarted = ChannelAnswers(self.worker.path, 'C_TARGET', 'test', self.ask)
        self.assertFalse(restarted.process_one())
        with restarted.db() as db:
            state = db.execute(
                "SELECT state FROM channel_questions WHERE ts='124.000'"
            ).fetchone()[0]
        self.assertEqual(state, 'delivery_unknown')


if __name__ == '__main__':
    unittest.main()
