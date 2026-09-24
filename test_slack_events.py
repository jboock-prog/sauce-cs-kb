import hashlib
import hmac
import json
import os
import time
import unittest

from flask import Flask

from slack_events import register_slack_events


class SlackEventsTests(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        self.secret = 'test-secret'
        register_slack_events(app, lambda: self.secret)
        self.client = app.test_client()

    def post(self, payload, age=0, signed=True):
        body = json.dumps(payload)
        timestamp = str(int(time.time()) - age)
        signature = 'v0=' + hmac.new(
            b'test-secret',
            f'v0:{timestamp}:{body}'.encode(),
            hashlib.sha256,
        ).hexdigest()
        return self.client.post(
            '/slack/events',
            data=body,
            content_type='application/json',
            headers={
                'X-Slack-Request-Timestamp': timestamp,
                'X-Slack-Signature': signature if signed else 'invalid',
            },
        )

    def test_verification(self):
        response = self.post({'type': 'url_verification', 'challenge': 'challenge-test'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'challenge': 'challenge-test'})

    def test_invalid_and_stale_signatures(self):
        self.assertEqual(self.post({}, signed=False).status_code, 403)
        self.assertEqual(self.post({}, age=600).status_code, 403)

    def test_bad_payloads_and_missing_configuration(self):
        self.assertEqual(self.post([]).status_code, 400)
        self.assertEqual(self.post({'type': 'url_verification'}).status_code, 400)
        self.secret = ''
        self.assertEqual(self.post({}).status_code, 503)

    def test_events_acknowledged(self):
        self.assertEqual(
            self.post({'type': 'event_callback', 'event_id': 'test'}).status_code,
            200,
        )


class ProductionRouteWiringTests(unittest.TestCase):
    def test_server_app_registers_slack_events(self):
        os.environ.setdefault('ANTHROPIC_API_KEY', 'test-key')
        import server

        previous_secret = server.SLACK_SIGNING_SECRET
        server.SLACK_SIGNING_SECRET = 'test-secret'
        try:
            body = json.dumps({'type': 'url_verification', 'challenge': 'wired'})
            timestamp = str(int(time.time()))
            signature = 'v0=' + hmac.new(
                b'test-secret',
                f'v0:{timestamp}:{body}'.encode(),
                hashlib.sha256,
            ).hexdigest()
            response = server.app.test_client().post(
                '/slack/events',
                data=body,
                content_type='application/json',
                headers={
                    'X-Slack-Request-Timestamp': timestamp,
                    'X-Slack-Signature': signature,
                },
            )
        finally:
            server.SLACK_SIGNING_SECRET = previous_secret

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'challenge': 'wired'})


if __name__ == '__main__':
    unittest.main()
