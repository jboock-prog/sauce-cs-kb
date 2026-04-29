const { describe, it, before } = require('node:test');
const assert = require('node:assert/strict');
const {
  parseEntry, parseKbFile,
  serializeEntry, serializeKbFile,
  stripInternal, nextEntryId,
} = require('./_kb');

const SAMPLE_ENTRY_TEXT = `## Entry 5: Test Refund

**Title:** Test Refund
**Issue Type:** Refunds & Credits
**Situation:** Customer requests refund.
**Resolution:**
Step 1: Verify order.
Step 2: Process refund.
**Exceptions:** None
**Approval Required:** No
**Last Updated:** 2026-01-15 — source`;

const SAMPLE_FILE = `# KB Refunds

Entry count: 1

---

${SAMPLE_ENTRY_TEXT}`;

describe('parseEntry', () => {
  it('parses raw_id and heading', () => {
    const e = parseEntry(SAMPLE_ENTRY_TEXT);
    assert.equal(e.raw_id, '5');
    assert.equal(e._heading, 'Test Refund');
  });

  it('parses inline fields', () => {
    const e = parseEntry(SAMPLE_ENTRY_TEXT);
    assert.equal(e.title, 'Test Refund');
    assert.equal(e.issue_type, 'Refunds & Credits');
    assert.equal(e.situation, 'Customer requests refund.');
    assert.equal(e.approval_required, 'No');
  });

  it('parses multiline resolution', () => {
    const e = parseEntry(SAMPLE_ENTRY_TEXT);
    assert.ok(e.resolution.includes('Step 1'));
    assert.ok(e.resolution.includes('Step 2'));
  });

  it('records inline flags correctly', () => {
    const e = parseEntry(SAMPLE_ENTRY_TEXT);
    assert.equal(e._inline.situation, true);
    assert.equal(e._inline.resolution, false);
  });

  it('returns null for non-entry text', () => {
    assert.equal(parseEntry('# Not an entry'), null);
  });

  it('stores _raw verbatim', () => {
    const e = parseEntry(SAMPLE_ENTRY_TEXT);
    assert.equal(e._raw, SAMPLE_ENTRY_TEXT);
  });
});

describe('parseKbFile', () => {
  it('splits header and entries', () => {
    const { header, entries } = parseKbFile(SAMPLE_FILE);
    assert.ok(header.includes('# KB Refunds'));
    assert.equal(entries.length, 1);
    assert.equal(entries[0].raw_id, '5');
  });
});

describe('serializeEntry', () => {
  it('returns _raw verbatim when present', () => {
    const e = parseEntry(SAMPLE_ENTRY_TEXT);
    assert.equal(serializeEntry(e), SAMPLE_ENTRY_TEXT);
  });

  it('reconstructs when _raw is absent', () => {
    const e = parseEntry(SAMPLE_ENTRY_TEXT);
    delete e._raw;
    const out = serializeEntry(e);
    assert.ok(out.startsWith('## Entry 5: Test Refund'));
    assert.ok(out.includes('**Title:** Test Refund'));
    assert.ok(out.includes('**Resolution:**\nStep 1'));
  });
});

describe('serializeKbFile', () => {
  it('updates entry count in header', () => {
    const { header, entries } = parseKbFile(SAMPLE_FILE);
    entries.forEach(e => delete e._raw);
    const out = serializeKbFile(header, entries);
    assert.ok(out.includes('Entry count: 1'));
  });

  it('round-trips without mutation when _raw present', () => {
    const { header, entries } = parseKbFile(SAMPLE_FILE);
    const out = serializeKbFile(header, entries);
    assert.equal(out.trim(), SAMPLE_FILE.trim());
  });
});

describe('stripInternal', () => {
  it('removes _ prefixed keys', () => {
    const e = parseEntry(SAMPLE_ENTRY_TEXT);
    const stripped = stripInternal(e);
    assert.ok(!('_raw' in stripped));
    assert.ok(!('_heading' in stripped));
    assert.ok(!('_inline' in stripped));
    assert.equal(stripped.raw_id, '5');
  });
});

describe('nextEntryId', () => {
  it('returns 1 for empty list', () => {
    assert.equal(nextEntryId([]), '1');
  });

  it('increments the highest numeric id', () => {
    const entries = [{ raw_id: '3' }, { raw_id: '7' }, { raw_id: '2' }];
    assert.equal(nextEntryId(entries), '8');
  });

  it('preserves prefix', () => {
    const entries = [{ raw_id: 'B2B-4' }, { raw_id: 'B2B-9' }];
    assert.equal(nextEntryId(entries), 'B2B-10');
  });
});
