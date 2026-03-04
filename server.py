#!/usr/bin/env python3
"""
server.py — Sauce CS KB Slack Bot Server
Receives /kb slash commands from Slack, queries Claude with KB context, returns answers.

Usage:
  Local:  python server.py
  Deploy: push to Railway with requirements.txt + Procfile

Environment variables required:
  ANTHROPIC_API_KEY     — your Anthropic API key
  SLACK_SIGNING_SECRET  — from your Slack app's Basic Information page
"""

import hashlib
import hmac
import os
import threading
import time

import anthropic
import requests
from flask import Flask, jsonify, request

# ─── Config ───────────────────────────────────────────────────────────────────

SERVER_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR   = SERVER_DIR  # KB files live alongside server.py in the repo root
KB_FILES   = ['kb-refunds.md', 'kb-b2c.md', 'kb-b2b.md', 'kb-general.md', 'kb-operations.md']
MODEL      = 'claude-haiku-4-5-20251001'
SEPARATOR  = '\n\n' + ('=' * 80) + '\n\n'

SLACK_SIGNING_SECRET = os.environ.get('SLACK_SIGNING_SECRET', '')

# ─── Load KB at startup ───────────────────────────────────────────────────────

def load_kb():
    sections = []
    for filename in KB_FILES:
        filepath = os.path.join(DOCS_DIR, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read().strip()
            sections.append(f'# FILE: {filename}\n\n{content}')
            print(f'  Loaded {filename}')
        except FileNotFoundError:
            print(f'  WARNING: {filename} not found — skipping')
    return SEPARATOR.join(sections)


KB_CONTENT = load_kb()
print(f'\nKB loaded — {len(KB_CONTENT):,} characters\n')

SYSTEM_PROMPT = f"""You are a CS support assistant for Sauce.
Below is the complete Sauce CS Knowledge Base.
When an agent asks a question, find the most relevant KB entry and give a direct, actionable answer.
Always cite the entry title you are drawing from.
If no entry applies, say so clearly and suggest escalating to a team lead.

Format every response for Slack using mrkdwn:
- Use *bold* for section headers and key terms
- Use bullet points ( • ) for lists
- Use numbered steps for procedures
- Separate sections with a blank line
- Keep responses concise and scannable

{KB_CONTENT}"""

# ─── Claude ───────────────────────────────────────────────────────────────────

claude = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env automatically


def query_claude(question: str) -> str:
    msg = claude.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{'role': 'user', 'content': question}],
    )
    return msg.content[0].text


# ─── Slack signature verification ─────────────────────────────────────────────

def verify_slack(raw_body: str, headers: dict) -> bool:
    """Return True if the request is a genuine Slack webhook."""
    if not SLACK_SIGNING_SECRET:
        print('  WARNING: SLACK_SIGNING_SECRET not set — skipping verification')
        return True

    timestamp = headers.get('X-Slack-Request-Timestamp', '')
    try:
        if abs(time.time() - int(timestamp)) > 300:   # replay attack window
            return False
    except ValueError:
        return False

    sig_basestring = f'v0:{timestamp}:{raw_body}'
    expected = 'v0=' + hmac.new(
        SLACK_SIGNING_SECRET.encode(),
        sig_basestring.encode(),
        hashlib.sha256,
    ).hexdigest()

    return hmac.compare_digest(expected, headers.get('X-Slack-Signature', ''))


# ─── Flask app ────────────────────────────────────────────────────────────────

app = Flask(__name__)


@app.route('/slack/command', methods=['POST'])
def slack_command():
    # Cache raw body BEFORE accessing request.form (required for sig verification)
    raw_body = request.get_data(as_text=True)

    if not verify_slack(raw_body, dict(request.headers)):
        return jsonify({'error': 'Invalid Slack signature'}), 403

    question    = request.form.get('text', '').strip()
    response_url = request.form.get('response_url', '')
    user_name   = request.form.get('user_name', 'agent')

    # Empty query — show usage hint
    if not question:
        return jsonify({
            'response_type': 'ephemeral',
            'text': (
                '*Usage:* `/kb your question here`\n'
                '*Example:* `/kb what do I do if a customer\'s order never arrived?`'
            ),
        })

    # Respond immediately (Slack requires < 3 seconds)
    # Then call Claude in the background and post the answer via response_url
    def answer_async():
        try:
            answer = query_claude(question)
        except Exception as e:
            answer = f'Something went wrong querying the KB: {e}'

        requests.post(response_url, json={
            'response_type': 'ephemeral',
            'text': answer,
        }, timeout=10)

    threading.Thread(target=answer_async, daemon=True).start()

    return jsonify({
        'response_type': 'ephemeral',
        'text': f'Searching the KB for: _{question}_…',
    })


@app.route('/query', methods=['POST'])
def query():
    """Direct POST endpoint for testing without Slack.
    Body: {"question": "your question"}
    """
    data = request.get_json(silent=True) or {}
    question = data.get('question', '').strip()
    if not question:
        return jsonify({'ok': False, 'error': 'question is required'}), 400
    try:
        answer = query_claude(question)
        return jsonify({'ok': True, 'answer': answer})
    except Exception as e:
        return jsonify({'ok': False, 'error': str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    """Simple health check for Railway uptime monitoring."""
    key = os.environ.get('ANTHROPIC_API_KEY', '')
    return jsonify({
        'ok': True,
        'kb_chars': len(KB_CONTENT),
        'model': MODEL,
        'api_key_set': bool(key),
        'api_key_prefix': key[:10] if key else None,
        'env_keys': [k for k in os.environ if 'ANTHROPIC' in k or 'API' in k],
    })


# ─── Start ────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print('WARNING: ANTHROPIC_API_KEY not set — Claude calls will fail\n')
    port = int(os.environ.get('PORT', 5000))
    print(f'Sauce KB server running on http://localhost:{port}\n')
    app.run(host='0.0.0.0', port=port)
