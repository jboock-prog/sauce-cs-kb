#!/usr/bin/env python3
"""
build.py — Sauce CS Knowledge Base builder
Reads KB markdown files, injects content into index.html, writes index.built.html
"""

import json
import os
import re

DOCS_DIR = os.path.join(os.path.dirname(__file__), '..')
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'index.html')
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), 'index.built.html')
PLACEHOLDER = 'KB_CONTENT_PLACEHOLDER'

KB_FILES = [
    'kb-refunds.md',
    'kb-b2c.md',
    'kb-b2b.md',
    'kb-general.md',
    'kb-operations.md',
]

SEPARATOR = '\n\n' + ('=' * 80) + '\n\n'


def main():
    # Read and concatenate KB files
    sections = []
    for filename in KB_FILES:
        filepath = os.path.join(DOCS_DIR, filename)
        if not os.path.exists(filepath):
            print(f'WARNING: {filename} not found at {filepath} — skipping')
            continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        sections.append(f'# FILE: {filename}\n\n{content}')
        print(f'  Loaded {filename}')

    if not sections:
        print('ERROR: No KB files loaded. Check that the repo root contains the KB markdown files.')
        return

    kb_content = SEPARATOR.join(sections)

    # Count entries (lines starting with ## Entry)
    entry_count = len(re.findall(r'^## Entry ', kb_content, re.MULTILINE))

    # Read index.html template
    if not os.path.exists(TEMPLATE_PATH):
        print(f'ERROR: index.html not found at {TEMPLATE_PATH}')
        return

    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = f.read()

    if PLACEHOLDER not in template:
        print(f'ERROR: {PLACEHOLDER} not found in index.html')
        return

    # Replace placeholder with JSON-escaped KB content
    # json.dumps produces a valid JS string literal (with surrounding quotes)
    kb_json = json.dumps(kb_content)
    output = template.replace(PLACEHOLDER, kb_json)

    # Write output
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f'\nBuilt successfully. {entry_count} KB entries loaded.')
    print(f'Output: {OUTPUT_PATH}')


if __name__ == '__main__':
    main()
