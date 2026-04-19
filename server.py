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
import re
import threading
import time

import anthropic
import requests
from flask import Flask, jsonify, request

# ─── Config ───────────────────────────────────────────────────────────────────

SERVER_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR   = SERVER_DIR  # KB files live alongside server.py in the repo root
KB_FILES   = ['kb-refunds.md', 'kb-b2c.md', 'kb-b2b.md', 'kb-general.md', 'kb-operations.md']
MODEL      = 'claude-sonnet-4-6'
SEPARATOR  = '\n\n' + ('=' * 80) + '\n\n'

SLACK_SIGNING_SECRET = os.environ.get('SLACK_SIGNING_SECRET', '')
SLACK_BOT_TOKEN      = os.environ.get('SLACK_BOT_TOKEN', '')
SUPPORT_CHANNEL_ID   = os.environ.get('SUPPORT_CHANNEL_ID', '')
RELEASE_CHANNEL_ID   = os.environ.get('RELEASE_CHANNEL_ID', '')

# Notion integration — external articles auto-publish, announcements saved as drafts
NOTION_API_KEY                  = os.environ.get('NOTION_API_KEY', '')
NOTION_CLIENT_ID                = os.environ.get('NOTION_CLIENT_ID', '')
NOTION_CLIENT_SECRET            = os.environ.get('NOTION_CLIENT_SECRET', '')
NOTION_REDIRECT_URI             = os.environ.get('NOTION_REDIRECT_URI', '')
NOTION_RELEASE_NOTES_PAGE_ID    = os.environ.get('NOTION_RELEASE_NOTES_PAGE_ID', '33d3f4388bf9815bb637d368e5395fcf')
NOTION_ANNOUNCEMENTS_PAGE_ID    = os.environ.get('NOTION_ANNOUNCEMENTS_PAGE_ID', '33d3f4388bf9819e947dcb53ba684810')
NOTION_VERSION = '2022-06-28'

kb_lock = threading.Lock()

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


def build_system_prompt(kb_content: str) -> str:
    return f"""You are a CS support assistant for Sauce.
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

{kb_content}"""


KB_CONTENT = load_kb()
print(f'\nKB loaded — {len(KB_CONTENT):,} characters\n')

SYSTEM_PROMPT = build_system_prompt(KB_CONTENT)

# ─── Claude ───────────────────────────────────────────────────────────────────

claude = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env automatically


STRUCTURED_QUERY_PROMPT = SYSTEM_PROMPT + """

IMPORTANT — when responding, also include a metadata block at the very end
of your response using this exact format:

===METADATA===
entry_id: [The entry ID you cited, e.g. GEN-1, B2C-3, OPS-5, 14. Use "none" if no entry applies]
entry_title: [The full title of the cited entry, or "N/A"]
kb_file: [The source file: kb-general.md, kb-b2c.md, kb-b2b.md, kb-operations.md, or kb-refunds.md. Use "none" if no entry applies]
approval_required: [yes/no based on the entry, or "unknown"]
recommended_action: [One-line summary of the recommended next step for the agent]
"""


def query_claude(question: str) -> str:
    for attempt in range(3):
        try:
            msg = claude.messages.create(
                model=MODEL,
                max_tokens=1024,
                system=SYSTEM_PROMPT,
                messages=[{'role': 'user', 'content': question}],
            )
            return msg.content[0].text
        except anthropic.APIStatusError as e:
            if e.status_code == 529 and attempt < 2:
                time.sleep(2 ** attempt)  # 1s, 2s
                continue
            raise


def query_claude_structured(question: str) -> str:
    """Like query_claude but with metadata block appended."""
    for attempt in range(3):
        try:
            msg = claude.messages.create(
                model=MODEL,
                max_tokens=1280,
                system=STRUCTURED_QUERY_PROMPT,
                messages=[{'role': 'user', 'content': question}],
            )
            return msg.content[0].text
        except anthropic.APIStatusError as e:
            if e.status_code == 529 and attempt < 2:
                time.sleep(2 ** attempt)
                continue
            raise


def parse_query_metadata(response_text: str) -> dict:
    """Extract metadata block from a structured query response."""
    result = {'answer': response_text, 'metadata': {}}
    tag = '===METADATA==='
    if tag in response_text:
        idx = response_text.index(tag)
        result['answer'] = response_text[:idx].strip()
        meta_text = response_text[idx + len(tag):].strip()
        for line in meta_text.splitlines():
            if ':' in line:
                key, _, val = line.partition(':')
                result['metadata'][key.strip()] = val.strip()
    return result


def query_claude_workflow(system_prompt: str, user_message: str) -> str:
    """Call Claude for workflow generation tasks (higher token limit)."""
    for attempt in range(3):
        try:
            msg = claude.messages.create(
                model=MODEL,
                max_tokens=4096,
                system=system_prompt,
                messages=[{'role': 'user', 'content': user_message}],
            )
            return msg.content[0].text
        except anthropic.APIStatusError as e:
            if e.status_code == 529 and attempt < 2:
                time.sleep(2 ** attempt)
                continue
            raise


# ─── KB management helpers ───────────────────────────────────────────────────

def get_next_entry_id(kb_filename: str) -> str:
    """Determine the next sequential entry ID for a given KB file."""
    filepath = os.path.join(DOCS_DIR, kb_filename)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return 'GEN-1'

    prefix_map = {
        'kb-general.md': 'GEN-',
        'kb-b2c.md': 'B2C-',
        'kb-b2b.md': 'B2B-',
        'kb-operations.md': 'OPS-',
        'kb-refunds.md': '',
    }
    prefix = prefix_map.get(kb_filename, 'GEN-')

    if prefix:
        pattern = rf'## Entry {re.escape(prefix)}(\d+)'
    else:
        pattern = r'## Entry (\d+)'

    numbers = [int(m) for m in re.findall(pattern, content)]
    next_num = max(numbers, default=0) + 1
    return f'{prefix}{next_num}'


def update_entry_count(filepath: str):
    """Update the Entry count: N header in a KB file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    actual_count = len(re.findall(r'^## Entry ', content, re.MULTILINE))
    content = re.sub(r'Entry count: \d+', f'Entry count: {actual_count}', content, count=1)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def append_kb_entry(kb_filename: str, entry_markdown: str):
    """Append a new KB entry to disk and update in-memory KB (thread-safe)."""
    global KB_CONTENT, SYSTEM_PROMPT
    with kb_lock:
        filepath = os.path.join(DOCS_DIR, kb_filename)
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write('\n\n---\n\n' + entry_markdown.strip() + '\n')
        update_entry_count(filepath)
        KB_CONTENT = load_kb()
        SYSTEM_PROMPT = build_system_prompt(KB_CONTENT)


# ─── Notion helpers ──────────────────────────────────────────────────────────

def _parse_inline_md(text: str) -> list:
    """Convert a line of markdown to Notion rich_text blocks (bold + plain)."""
    rich = []
    for part in re.split(r'(\*\*[^*]+\*\*)', text):
        if part.startswith('**') and part.endswith('**'):
            rich.append({'type': 'text', 'text': {'content': part[2:-2]},
                         'annotations': {'bold': True}})
        elif part:
            rich.append({'type': 'text', 'text': {'content': part}})
    return rich or [{'type': 'text', 'text': {'content': text}}]


def _md_to_notion_blocks(md: str) -> list:
    """Convert markdown text to a list of Notion block objects."""
    blocks = []
    for line in md.splitlines():
        s = line.rstrip()
        if not s:
            continue
        if s == '---':
            blocks.append({'object': 'block', 'type': 'divider', 'divider': {}})
        elif s.startswith('### '):
            blocks.append({'object': 'block', 'type': 'heading_3',
                            'heading_3': {'rich_text': _parse_inline_md(s[4:])}})
        elif s.startswith('## '):
            blocks.append({'object': 'block', 'type': 'heading_2',
                            'heading_2': {'rich_text': _parse_inline_md(s[3:])}})
        elif s.startswith('# '):
            blocks.append({'object': 'block', 'type': 'heading_1',
                            'heading_1': {'rich_text': _parse_inline_md(s[2:])}})
        elif s.startswith('- ') or s.startswith('\u2022 '):
            blocks.append({'object': 'block', 'type': 'bulleted_list_item',
                            'bulleted_list_item': {'rich_text': _parse_inline_md(s[2:])}})
        elif s.startswith('> '):
            blocks.append({'object': 'block', 'type': 'quote',
                            'quote': {'rich_text': _parse_inline_md(s[2:])}})
        else:
            blocks.append({'object': 'block', 'type': 'paragraph',
                            'paragraph': {'rich_text': _parse_inline_md(s)}})
    return blocks


def _notion_headers() -> dict:
    return {
        'Authorization': f'Bearer {NOTION_API_KEY}',
        'Notion-Version': NOTION_VERSION,
        'Content-Type': 'application/json',
    }


def publish_article_to_notion(title: str, article_md: str) -> dict:
    """Create a child page under the Product Release Notes page."""
    if not NOTION_API_KEY:
        return {'ok': False, 'error': 'NOTION_API_KEY not set'}
    blocks = _md_to_notion_blocks(article_md)
    resp = requests.post(
        'https://api.notion.com/v1/pages',
        headers=_notion_headers(),
        json={
            'parent': {'type': 'page_id', 'page_id': NOTION_RELEASE_NOTES_PAGE_ID},
            'properties': {'title': {'title': [{'type': 'text', 'text': {'content': title}}]}},
            'children': blocks[:100],  # Notion API limit
        },
        timeout=15,
    )
    data = resp.json()
    return {'ok': resp.status_code == 200, 'url': data.get('url'), 'error': data.get('message')}


def save_announcement_draft_to_notion(title: str, announcement_text: str) -> dict:
    """Save a Slack announcement as a draft child page under Pending Announcements.
    Slack's API does not support creating drafts programmatically, so drafts
    are stored here for manual review and copy-paste to Slack."""
    if not NOTION_API_KEY:
        return {'ok': False, 'error': 'NOTION_API_KEY not set'}
    blocks = _md_to_notion_blocks(announcement_text)
    resp = requests.post(
        'https://api.notion.com/v1/pages',
        headers=_notion_headers(),
        json={
            'parent': {'type': 'page_id', 'page_id': NOTION_ANNOUNCEMENTS_PAGE_ID},
            'properties': {'title': {'title': [{'type': 'text', 'text': {'content': f'DRAFT: {title}'}}]}},
            'children': blocks[:100],
        },
        timeout=15,
    )
    data = resp.json()
    return {'ok': resp.status_code == 200, 'url': data.get('url'), 'error': data.get('message')}


# ─── Slack helpers ───────────────────────────────────────────────────────────

def post_to_slack_channel(channel_id: str, text: str) -> dict:
    """Post a message to a Slack channel using chat.postMessage."""
    resp = requests.post(
        'https://slack.com/api/chat.postMessage',
        headers={'Authorization': f'Bearer {SLACK_BOT_TOKEN}'},
        json={'channel': channel_id, 'text': text},
        timeout=10,
    )
    return resp.json()


def parse_workflow_response(response_text: str) -> dict:
    """Parse Claude's delimited workflow response into named sections."""
    parts = {}
    markers = ['EXTERNAL_ARTICLE', 'KB_ENTRY', 'ANNOUNCEMENT', 'TARGET_KB_FILE']
    for key in markers:
        tag = f'==={key}==='
        if tag not in response_text:
            continue
        start = response_text.index(tag) + len(tag)
        # Find the next delimiter or end of string
        next_positions = []
        for other in markers:
            other_tag = f'==={other}==='
            try:
                pos = response_text.index(other_tag, start)
                next_positions.append(pos)
            except ValueError:
                pass
        end = min(next_positions) if next_positions else len(response_text)
        parts[key] = response_text[start:end].strip()
    return parts


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


# ─── Workflow prompt templates ───────────────────────────────────────────────

RELEASE_SYSTEM_PROMPT = """\
You are a technical writer for Sauce, a restaurant online ordering platform.
You will receive product release information and must generate THREE outputs
plus a target KB file selection.

Respond with EXACTLY the following structure, using these exact delimiters:

===EXTERNAL_ARTICLE===
[Customer-facing knowledge article in markdown. Professional tone.
Explain what changed, how it affects users, and any action required.
Include sections: Overview, What's New, How It Works, FAQ if applicable.]

===KB_ENTRY===
[Internal KB entry for the CS team in this EXACT format:]

## Entry {ENTRY_ID}: [Short Title]

**Title:** [Full descriptive title]
**Issue Type:** [e.g. Product Update, New Feature, Process Change]
**Situation:** [When a CS agent would need to reference this]
**Resolution:**
[Step-by-step guidance for CS agents handling questions about this release]

**Exceptions:** [Edge cases or limitations]
**Approval Required:** [Yes/No]
**Last Updated:** {TODAY} — added via product release workflow

===ANNOUNCEMENT===
[Slack announcement for the support team. Use Slack mrkdwn formatting.
Include: what changed, impact on support workflows, key talking points.
Keep it concise and scannable with bullet points.]

===TARGET_KB_FILE===
[ONLY one of: kb-general.md, kb-b2c.md, kb-b2b.md, kb-operations.md, kb-refunds.md]
Choose based on which category this release most closely affects.
"""

KB_UPDATE_SYSTEM_PROMPT = """\
You are a technical writer for Sauce, a restaurant online ordering platform.
You will receive information about a knowledge base update and must generate
TWO outputs plus a target KB file selection.

Respond with EXACTLY the following structure, using these exact delimiters:

===KB_ENTRY===
[Internal KB entry for the CS team in this EXACT format:]

## Entry {ENTRY_ID}: [Short Title]

**Title:** [Full descriptive title]
**Issue Type:** [e.g. Policies & Rules, Order Issues, Restaurant Relations]
**Situation:** [When a CS agent would need this]
**Resolution:**
[Step-by-step guidance]

**Exceptions:** [Edge cases]
**Approval Required:** [Yes/No]
**Last Updated:** {TODAY} — added via KB update workflow

===ANNOUNCEMENT===
[Slack announcement for the support team. Use Slack mrkdwn formatting.
Brief summary of what was added/changed in the KB and why.
Keep it concise with bullet points.]

===TARGET_KB_FILE===
[ONLY one of: kb-general.md, kb-b2c.md, kb-b2b.md, kb-operations.md, kb-refunds.md]
Choose based on which category this update most closely affects.
"""


def build_release_user_message(release_text: str) -> str:
    """Build the user message for the full release workflow."""
    today = time.strftime('%Y-%m-%d')
    ids = {f: get_next_entry_id(f) for f in KB_FILES}
    id_lines = '\n'.join(f'  - {f}: {eid}' for f, eid in ids.items())
    return (
        f'Product release information:\n\n{release_text}\n\n'
        f'Today\'s date: {today}\n'
        f'Available entry IDs per KB file:\n{id_lines}\n\n'
        f'Use the entry ID that corresponds to the TARGET_KB_FILE you select.'
    )


def build_update_user_message(update_text: str) -> str:
    """Build the user message for the KB-update workflow."""
    today = time.strftime('%Y-%m-%d')
    ids = {f: get_next_entry_id(f) for f in KB_FILES}
    id_lines = '\n'.join(f'  - {f}: {eid}' for f, eid in ids.items())
    return (
        f'Knowledge base update information:\n\n{update_text}\n\n'
        f'Today\'s date: {today}\n'
        f'Available entry IDs per KB file:\n{id_lines}\n\n'
        f'Use the entry ID that corresponds to the TARGET_KB_FILE you select.'
    )


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
    """Direct POST endpoint for testing and external integrations.
    Body: {"question": "your question"}
    Returns structured response with answer + metadata (entry_id, kb_file, etc.)
    """
    data = request.get_json(silent=True) or {}
    question = data.get('question', '').strip()
    if not question:
        return jsonify({'ok': False, 'error': 'question is required'}), 400
    try:
        raw = query_claude_structured(question)
        parsed = parse_query_metadata(raw)
        return jsonify({
            'ok': True,
            'answer': parsed['answer'],
            'entry_id': parsed['metadata'].get('entry_id'),
            'entry_title': parsed['metadata'].get('entry_title'),
            'kb_file': parsed['metadata'].get('kb_file'),
            'approval_required': parsed['metadata'].get('approval_required'),
            'recommended_action': parsed['metadata'].get('recommended_action'),
        })
    except Exception as e:
        return jsonify({'ok': False, 'error': str(e)}), 500


@app.route('/test/release', methods=['POST'])
def test_release():
    """Direct test endpoint for the release workflow (no Slack auth).
    Body: {"text": "your release info", "commit": false}
    - commit=false (default): dry run — returns JSON only, no KB write
    - commit=true: writes KB entry to disk, returns JSON, no Slack posting
    """
    data = request.get_json(silent=True) or {}
    release_text = data.get('text', '').strip()
    commit = bool(data.get('commit', False))
    if not release_text:
        return jsonify({'ok': False, 'error': 'text is required'}), 400
    try:
        response = query_claude_workflow(
            RELEASE_SYSTEM_PROMPT,
            build_release_user_message(release_text),
        )
        parts = parse_workflow_response(response)
        target_file = parts.get('TARGET_KB_FILE', 'kb-general.md').strip()
        if target_file not in KB_FILES:
            target_file = 'kb-general.md'
        if commit and parts.get('KB_ENTRY'):
            append_kb_entry(target_file, parts['KB_ENTRY'])
        return jsonify({
            'ok': True,
            'committed': commit,
            'target_kb_file': target_file,
            'external_article': parts.get('EXTERNAL_ARTICLE'),
            'kb_entry': parts.get('KB_ENTRY'),
            'announcement': parts.get('ANNOUNCEMENT'),
        })
    except Exception as e:
        return jsonify({'ok': False, 'error': str(e)}), 500


@app.route('/test/kb-update', methods=['POST'])
def test_kb_update():
    """Direct test endpoint for the KB update workflow (no Slack auth).
    Body: {"text": "your update info", "commit": false}
    - commit=false (default): dry run — returns JSON only, no KB write
    - commit=true: writes KB entry to disk, returns JSON, no Slack posting
    """
    data = request.get_json(silent=True) or {}
    update_text = data.get('text', '').strip()
    commit = bool(data.get('commit', False))
    if not update_text:
        return jsonify({'ok': False, 'error': 'text is required'}), 400
    try:
        response = query_claude_workflow(
            KB_UPDATE_SYSTEM_PROMPT,
            build_update_user_message(update_text),
        )
        parts = parse_workflow_response(response)
        target_file = parts.get('TARGET_KB_FILE', 'kb-general.md').strip()
        if target_file not in KB_FILES:
            target_file = 'kb-general.md'
        if commit and parts.get('KB_ENTRY'):
            append_kb_entry(target_file, parts['KB_ENTRY'])
        return jsonify({
            'ok': True,
            'committed': commit,
            'target_kb_file': target_file,
            'kb_entry': parts.get('KB_ENTRY'),
            'announcement': parts.get('ANNOUNCEMENT'),
        })
    except Exception as e:
        return jsonify({'ok': False, 'error': str(e)}), 500


@app.route('/slack/release', methods=['POST'])
def slack_release():
    """Full product release workflow: external article + KB entry + announcement + confirmation."""
    raw_body = request.get_data(as_text=True)
    if not verify_slack(raw_body, dict(request.headers)):
        return jsonify({'error': 'Invalid Slack signature'}), 403

    if not SLACK_BOT_TOKEN:
        return jsonify({
            'response_type': 'ephemeral',
            'text': ':x: SLACK_BOT_TOKEN is not configured. Contact the bot admin.',
        })

    release_text = request.form.get('text', '').strip()
    response_url = request.form.get('response_url', '')
    user_name    = request.form.get('user_name', 'agent')

    if not release_text:
        return jsonify({
            'response_type': 'ephemeral',
            'text': (
                '*Usage:* `/release <product release details>`\n'
                '*Example:* `/release New feature: customers can now schedule '
                'orders up to 14 days in advance (previously 7). Affects all '
                'B2C ordering flows.`'
            ),
        })

    def release_async():
        try:
            # Step 1: Generate all content via Claude
            response = query_claude_workflow(
                RELEASE_SYSTEM_PROMPT,
                build_release_user_message(release_text),
            )
            parts = parse_workflow_response(response)

            if not parts.get('KB_ENTRY') or not parts.get('ANNOUNCEMENT'):
                raise ValueError('Claude response missing required sections')

            target_file = parts.get('TARGET_KB_FILE', 'kb-general.md').strip()
            if target_file not in KB_FILES:
                target_file = 'kb-general.md'

            # Step 2: Append KB entry to disk + memory
            append_kb_entry(target_file, parts['KB_ENTRY'])

            # Step 3: Publish external article to Notion Product Release Notes
            notion_url = None
            if parts.get('EXTERNAL_ARTICLE'):
                notion_result = publish_article_to_notion(
                    f'Release: {release_text[:80]}',
                    parts['EXTERNAL_ARTICLE'],
                )
                notion_url = notion_result.get('url')

            # Step 4: Save announcement draft to Notion (Slack API does not support
            # creating drafts programmatically — saved here for manual review + posting)
            draft_url = None
            draft_result = save_announcement_draft_to_notion(
                release_text[:80],
                parts['ANNOUNCEMENT'],
            )
            draft_url = draft_result.get('url')

            # Step 5: Post confirmation to release channel
            notion_line = f'• External article: {notion_url}' if notion_url else '• External article: Notion not configured'
            draft_line  = f'• Announcement draft: {draft_url}' if draft_url else '• Announcement draft: Notion not configured'
            confirmation = (
                f':white_check_mark: *Release processed by {user_name}*\n\n'
                f'*KB entry added to:* `{target_file}`\n'
                f'{notion_line}\n'
                f'{draft_line}\n\n'
                f'_Review the announcement draft in Notion before posting to the support team._'
            )
            if RELEASE_CHANNEL_ID:
                post_to_slack_channel(RELEASE_CHANNEL_ID, confirmation)

            # Step 6: Confirm back to the invoking user
            requests.post(response_url, json={
                'response_type': 'ephemeral',
                'text': (
                    f':white_check_mark: Release workflow complete.\n'
                    f'• KB updated in `{target_file}`\n'
                    f'• External article published to Notion\n'
                    f'• Announcement saved as draft in Notion — review before posting'
                ),
            }, timeout=10)

        except Exception as e:
            requests.post(response_url, json={
                'response_type': 'ephemeral',
                'text': f':x: Release workflow failed: {e}',
            }, timeout=10)

    threading.Thread(target=release_async, daemon=True).start()

    return jsonify({
        'response_type': 'ephemeral',
        'text': ':hourglass_flowing_sand: Processing release — generating KB entry, external article, and support announcement…',
    })


@app.route('/slack/kb-update', methods=['POST'])
def slack_kb_update():
    """Shorter workflow: KB entry + support announcement only."""
    raw_body = request.get_data(as_text=True)
    if not verify_slack(raw_body, dict(request.headers)):
        return jsonify({'error': 'Invalid Slack signature'}), 403

    if not SLACK_BOT_TOKEN:
        return jsonify({
            'response_type': 'ephemeral',
            'text': ':x: SLACK_BOT_TOKEN is not configured. Contact the bot admin.',
        })

    update_text  = request.form.get('text', '').strip()
    response_url = request.form.get('response_url', '')
    user_name    = request.form.get('user_name', 'agent')

    if not update_text:
        return jsonify({
            'response_type': 'ephemeral',
            'text': (
                '*Usage:* `/kb-update <knowledge update details>`\n'
                '*Example:* `/kb-update New policy: all refund requests over '
                '$200 now require manager approval before submitting to ePayments.`'
            ),
        })

    def update_async():
        try:
            # Step 1: Generate KB entry + announcement via Claude
            response = query_claude_workflow(
                KB_UPDATE_SYSTEM_PROMPT,
                build_update_user_message(update_text),
            )
            parts = parse_workflow_response(response)

            if not parts.get('KB_ENTRY') or not parts.get('ANNOUNCEMENT'):
                raise ValueError('Claude response missing required sections')

            target_file = parts.get('TARGET_KB_FILE', 'kb-general.md').strip()
            if target_file not in KB_FILES:
                target_file = 'kb-general.md'

            # Step 2: Append KB entry
            append_kb_entry(target_file, parts['KB_ENTRY'])

            # Step 3: Save announcement draft to Notion for review before posting
            draft_url = None
            draft_result = save_announcement_draft_to_notion(
                update_text[:80],
                parts['ANNOUNCEMENT'],
            )
            draft_url = draft_result.get('url')

            # Step 4: Confirm back to the invoking user
            draft_line = f'• Announcement draft: {draft_url}' if draft_url else '• Announcement draft: Notion not configured'
            requests.post(response_url, json={
                'response_type': 'ephemeral',
                'text': (
                    f':white_check_mark: KB update complete.\n'
                    f'• KB updated in `{target_file}`\n'
                    f'{draft_line}\n'
                    f'_Review the announcement draft in Notion before posting to the support team._'
                ),
            }, timeout=10)

        except Exception as e:
            requests.post(response_url, json={
                'response_type': 'ephemeral',
                'text': f':x: KB update workflow failed: {e}',
            }, timeout=10)

    threading.Thread(target=update_async, daemon=True).start()

    return jsonify({
        'response_type': 'ephemeral',
        'text': ':hourglass_flowing_sand: Processing KB update — generating entry and support announcement…',
    })


@app.route('/notion/setup', methods=['GET'])
def notion_setup():
    """Step 1: Redirect to Notion OAuth authorization page.
    Visit this URL once to authorize the integration and get your NOTION_API_KEY.
    """
    if not NOTION_CLIENT_ID or not NOTION_REDIRECT_URI:
        return (
            '<h2>Notion OAuth not configured</h2>'
            '<p>Set NOTION_CLIENT_ID and NOTION_REDIRECT_URI on Railway first.</p>'
        ), 400
    from urllib.parse import urlencode
    params = urlencode({
        'client_id': NOTION_CLIENT_ID,
        'response_type': 'code',
        'owner': 'user',
        'redirect_uri': NOTION_REDIRECT_URI,
    })
    auth_url = f'https://api.notion.com/v1/oauth/authorize?{params}'
    return f'<meta http-equiv="refresh" content="0;url={auth_url}"><a href="{auth_url}">Click here if not redirected</a>'


@app.route('/notion/oauth/callback', methods=['GET'])
def notion_oauth_callback():
    """Step 2: Notion redirects here after authorization.
    Exchanges the code for an access token and displays it to copy into Railway.
    """
    import base64
    code  = request.args.get('code')
    error = request.args.get('error')

    if error:
        return f'<h2>Authorization denied</h2><p>{error}</p>', 400
    if not code:
        return '<h2>No code returned from Notion</h2>', 400

    credentials = base64.b64encode(
        f'{NOTION_CLIENT_ID}:{NOTION_CLIENT_SECRET}'.encode()
    ).decode()

    resp = requests.post(
        'https://api.notion.com/v1/oauth/token',
        headers={
            'Authorization': f'Basic {credentials}',
            'Content-Type': 'application/json',
        },
        json={
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': NOTION_REDIRECT_URI,
        },
        timeout=15,
    )
    data = resp.json()

    if resp.status_code != 200:
        return f'<h2>Token exchange failed</h2><pre>{data}</pre>', 400

    token = data.get('access_token', '')
    workspace = data.get('workspace_name', '')
    return f'''
    <h2>Notion authorization successful</h2>
    <p>Workspace: <strong>{workspace}</strong></p>
    <p>Copy this token and add it to Railway as <code>NOTION_API_KEY</code>:</p>
    <textarea rows="3" cols="80" onclick="this.select()">{token}</textarea>
    <p><strong>Done.</strong> Once added to Railway and redeployed, the integration is live.
    You will not need to do this again — Notion tokens do not expire.</p>
    '''


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
        'slack_bot_token_set': bool(SLACK_BOT_TOKEN),
        'support_channel_id': SUPPORT_CHANNEL_ID or None,
        'release_channel_id': RELEASE_CHANNEL_ID or None,
        'notion_api_key_set': bool(NOTION_API_KEY),
        'notion_release_notes_page_id': NOTION_RELEASE_NOTES_PAGE_ID,
        'notion_announcements_page_id': NOTION_ANNOUNCEMENTS_PAGE_ID,
        'env_keys': [k for k in os.environ if 'ANTHROPIC' in k or 'API' in k],
    })


# ─── Start ────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print('WARNING: ANTHROPIC_API_KEY not set — Claude calls will fail\n')
    port = int(os.environ.get('PORT', 5000))
    print(f'Sauce KB server running on http://localhost:{port}\n')
    app.run(host='0.0.0.0', port=port)
