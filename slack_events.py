"""Authenticated Slack Events API handshake and event dispatch."""

import hashlib
import hmac
import json
import time

from flask import jsonify, request


def register_slack_events(app, signing_secret, handle_event=None):
    @app.post('/slack/events')
    def slack_events():
        secret = signing_secret()
        if not secret:
            return jsonify(error='Slack signing secret is not configured'), 503

        body = request.get_data()
        timestamp = request.headers.get('X-Slack-Request-Timestamp', '')
        try:
            fresh = abs(time.time() - int(timestamp)) <= 300
        except ValueError:
            fresh = False

        expected = 'v0=' + hmac.new(
            secret.encode(),
            b'v0:' + timestamp.encode() + b':' + body,
            hashlib.sha256,
        ).hexdigest()
        signature = request.headers.get('X-Slack-Signature', '')
        if not fresh or not hmac.compare_digest(expected, signature):
            return jsonify(error='Invalid Slack signature'), 403

        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify(error='Expected a JSON object'), 400

        if payload.get('type') == 'url_verification':
            challenge = payload.get('challenge')
            if not isinstance(challenge, str) or not challenge:
                return jsonify(error='Missing challenge'), 400
            return jsonify(challenge=challenge)

        if payload.get('type') == 'event_callback' and handle_event:
            try:
                handle_event(payload)
            except Exception as exc:
                print(json.dumps({
                    'event': 'slack_event_queue_error',
                    'error_type': type(exc).__name__,
                }), flush=True)
                return jsonify(error='Queue temporarily unavailable'), 503

        return '', 200
