#!/usr/bin/env python3
"""
Sync KB markdown files to Confluence.
Each KB file becomes a parent page; each entry becomes a child page.

Usage:
    python sync_to_confluence.py

Required environment variables (or edit CONFIG below):
    CONFLUENCE_URL       e.g. https://yourcompany.atlassian.net
    CONFLUENCE_EMAIL     your Atlassian account email
    CONFLUENCE_API_TOKEN your Atlassian API token
    CONFLUENCE_SPACE_KEY e.g. CS or ~yourname for a personal space
"""

import os
import re
import sys
import json
import requests
from requests.auth import HTTPBasicAuth

# ── Config ────────────────────────────────────────────────────────────────────

CONFIG = {
    "url":        os.environ.get("CONFLUENCE_URL", "").rstrip("/"),
    "email":      os.environ.get("CONFLUENCE_EMAIL", ""),
    "api_token":  os.environ.get("CONFLUENCE_API_TOKEN", ""),
    "space_key":  os.environ.get("CONFLUENCE_SPACE_KEY", ""),
    # Optional: page ID of an existing parent page to nest everything under.
    # Leave empty to create top-level pages in the space.
    "root_page_id": os.environ.get("CONFLUENCE_ROOT_PAGE_ID", ""),
}

KB_FILES = [
    ("kb-general.md",     "KB: General Requests"),
    ("kb-b2c.md",         "KB: B2C Order Modifications"),
    ("kb-b2b.md",         "KB: B2B"),
    ("kb-operations.md",  "KB: Operations"),
    ("kb-refunds.md",     "KB: Refunds"),
]

# ── Confluence API helpers ────────────────────────────────────────────────────

def api(method, path, **kwargs):
    url = f"{CONFIG['url']}/wiki/rest/api{path}"
    auth = HTTPBasicAuth(CONFIG["email"], CONFIG["api_token"])
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    resp = getattr(requests, method)(url, auth=auth, headers=headers, **kwargs)
    if not resp.ok:
        print(f"  ERROR {resp.status_code}: {resp.text[:300]}")
        resp.raise_for_status()
    return resp.json() if resp.text else {}


def get_page_by_title(title, space_key):
    results = api("get", "/content", params={
        "title": title,
        "spaceKey": space_key,
        "expand": "version",
    }).get("results", [])
    return results[0] if results else None


def create_page(title, body_html, space_key, parent_id=None):
    payload = {
        "type": "page",
        "title": title,
        "space": {"key": space_key},
        "body": {"storage": {"value": body_html, "representation": "storage"}},
    }
    if parent_id:
        payload["ancestors"] = [{"id": parent_id}]
    return api("post", "/content", json=payload)


def update_page(page_id, title, body_html, current_version):
    payload = {
        "type": "page",
        "title": title,
        "version": {"number": current_version + 1},
        "body": {"storage": {"value": body_html, "representation": "storage"}},
    }
    return api("put", f"/content/{page_id}", json=payload)


def upsert_page(title, body_html, space_key, parent_id=None):
    existing = get_page_by_title(title, space_key)
    if existing:
        page_id = existing["id"]
        version = existing["version"]["number"]
        update_page(page_id, title, body_html, version)
        print(f"    updated  → {title}")
        return page_id
    else:
        result = create_page(title, body_html, space_key, parent_id)
        print(f"    created  → {title}")
        return result["id"]

# ── Markdown → Confluence storage format ─────────────────────────────────────

def md_to_confluence(text):
    """Convert a subset of markdown to Confluence storage format (XHTML)."""
    lines = text.split("\n")
    out = []
    in_list = False

    for line in lines:
        # Headings
        if line.startswith("### "):
            if in_list: out.append("</ul>"); in_list = False
            out.append(f"<h3>{escape(line[4:])}</h3>")
        elif line.startswith("## "):
            if in_list: out.append("</ul>"); in_list = False
            out.append(f"<h2>{escape(line[3:])}</h2>")
        elif line.startswith("# "):
            if in_list: out.append("</ul>"); in_list = False
            out.append(f"<h1>{escape(line[2:])}</h1>")
        # Bullet list
        elif line.startswith("- "):
            if not in_list: out.append("<ul>"); in_list = True
            out.append(f"<li>{inline_fmt(line[2:])}</li>")
        elif re.match(r"^\d+\. ", line):
            if in_list: out.append("</ul>"); in_list = False
            # numbered lists — wrap lazily as paragraphs for simplicity
            out.append(f"<p>{inline_fmt(line)}</p>")
        # Horizontal rule
        elif line.strip() == "---":
            if in_list: out.append("</ul>"); in_list = False
            out.append("<hr/>")
        # Empty line
        elif line.strip() == "":
            if in_list: out.append("</ul>"); in_list = False
            out.append("<p></p>")
        else:
            if in_list: out.append("</ul>"); in_list = False
            out.append(f"<p>{inline_fmt(line)}</p>")

    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline_fmt(s):
    # Bold: **text**
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    # Italic: *text* or _text_
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    s = re.sub(r"_(.+?)_", r"<em>\1</em>", s)
    # Inline code: `text`
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    # Escape remaining HTML special chars (after formatting)
    # Only escape in text nodes, not inside tags we just added
    def escape_outside_tags(m):
        return m.group(0).replace("&", "&amp;") if not m.group(0).startswith("<") else m.group(0)
    return s

# ── KB file parsing ───────────────────────────────────────────────────────────

def parse_entries(filepath):
    """Return list of (entry_id, title, raw_markdown) tuples."""
    with open(filepath) as f:
        content = f.read()

    # Split on entry headings: ## Entry XXX-N: Title
    pattern = r"(## Entry [A-Z0-9]+-\d+: .+)"
    parts = re.split(pattern, content)

    # parts[0] is the file header; then alternating heading / body
    file_header = parts[0]
    entries = []
    for i in range(1, len(parts), 2):
        heading = parts[i]
        body = parts[i + 1] if i + 1 < len(parts) else ""
        full = (heading + body).strip()

        # Extract entry ID and title from heading
        m = re.match(r"## Entry ([A-Z0-9]+-\d+): (.+)", heading)
        if m:
            entry_id = m.group(1)
            entry_title = m.group(2).strip()
            entries.append((entry_id, entry_title, full))

    return file_header, entries

# ── Index page builder ────────────────────────────────────────────────────────

def build_index_html(kb_title, entries):
    rows = ""
    for entry_id, entry_title, _ in entries:
        rows += f"<tr><td><strong>{escape(entry_id)}</strong></td><td>{escape(entry_title)}</td></tr>\n"
    return f"""
<h1>{escape(kb_title)}</h1>
<p>Auto-synced from the <strong>sauce-cs-kb</strong> repository. Edit the source markdown files — do not edit these pages directly.</p>
<table>
  <tbody>
    <tr><th>Entry ID</th><th>Title</th></tr>
    {rows}
  </tbody>
</table>
"""

# ── Main ──────────────────────────────────────────────────────────────────────

def validate_config():
    missing = [k for k in ("url", "email", "api_token", "space_key") if not CONFIG[k]]
    if missing:
        print("Missing required config / environment variables:")
        for k in missing:
            print(f"  CONFLUENCE_{k.upper()}")
        print("\nSet them as environment variables or edit CONFIG in this script.")
        sys.exit(1)


def main():
    validate_config()
    space = CONFIG["space_key"]
    root_id = CONFIG["root_page_id"] or None

    print(f"Syncing to Confluence space: {space}")
    print(f"Target: {CONFIG['url']}\n")

    for filename, kb_title in KB_FILES:
        filepath = os.path.join(os.path.dirname(__file__), filename)
        if not os.path.exists(filepath):
            print(f"Skipping {filename} (not found)")
            continue

        print(f"Processing {filename} → '{kb_title}'")
        file_header, entries = parse_entries(filepath)

        # Create/update the parent page for this KB file
        index_html = build_index_html(kb_title, entries)
        parent_id = upsert_page(kb_title, index_html, space, root_id)

        # Create/update a child page per entry
        for entry_id, entry_title, entry_md in entries:
            page_title = f"{entry_id}: {entry_title}"
            body_html = md_to_confluence(entry_md)
            upsert_page(page_title, body_html, space, parent_id)

        print()

    print("Done.")


if __name__ == "__main__":
    main()
