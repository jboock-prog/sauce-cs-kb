'use strict';

const KNOWN_FIELDS = new Set([
  'Title', 'Issue Type', 'Situation', 'Resolution', 'Exceptions',
  'Approval Required', 'Last Updated',
  'Critical Rule', 'Ticket documentation', 'Reference',
]);

const STANDARD_MAP = {
  'Title': 'title',
  'Issue Type': 'issue_type',
  'Situation': 'situation',
  'Resolution': 'resolution',
  'Exceptions': 'exceptions',
  'Approval Required': 'approval_required',
  'Last Updated': 'last_updated',
};

function parseEntry(text) {
  const lines = text.split('\n');
  const headingMatch = lines[0].match(/^## Entry (.+?): (.+)$/);
  if (!headingMatch) return null;

  const fieldPositions = [];
  for (let i = 0; i < lines.length; i++) {
    const m = lines[i].match(/^\*\*([^*\n]+):\*\*(.*)$/);
    if (m && KNOWN_FIELDS.has(m[1])) {
      fieldPositions.push([i, m[1], m[2].trim()]);
    }
  }

  const entry = {
    raw_id: headingMatch[1],
    _raw: text,
    _heading: headingMatch[2],
    _inline: {},
    extra_fields: [],
  };

  for (let idx = 0; idx < fieldPositions.length; idx++) {
    const [lineI, label, inlineVal] = fieldPositions[idx];
    const wasInline = inlineVal !== '';
    const inlineKey = STANDARD_MAP[label] || label;
    entry._inline[inlineKey] = wasInline;

    let value;
    if (wasInline) {
      value = inlineVal;
    } else {
      const nextLineI = idx + 1 < fieldPositions.length
        ? fieldPositions[idx + 1][0]
        : lines.length;
      const valueLines = lines.slice(lineI + 1, nextLineI);
      while (valueLines.length && !valueLines[valueLines.length - 1].trim()) {
        valueLines.pop();
      }
      value = valueLines.join('\n');
    }

    if (STANDARD_MAP[label]) {
      entry[STANDARD_MAP[label]] = value;
    } else {
      entry.extra_fields.push({ label, value, _inline: wasInline });
    }
  }

  return entry;
}

function parseKbFile(content) {
  const rawParts = content.split('\n\n---\n\n');
  const header = rawParts[0].trimEnd();

  const assembled = [];
  for (const part of rawParts.slice(1)) {
    if (part.trim().startsWith('## Entry ')) {
      assembled.push(part);
    } else if (assembled.length) {
      assembled[assembled.length - 1] += '\n\n---\n\n' + part;
    }
  }

  const entries = [];
  for (const chunk of assembled) {
    const parsed = parseEntry(chunk.trim());
    if (parsed) entries.push(parsed);
  }

  return { header, entries };
}

function serializeEntry(e) {
  if (e._raw !== undefined) return e._raw;

  const inlineMap = e._inline || {};
  const parts = [];

  function addField(label, value, stdKey) {
    const key = stdKey || label;
    const wasInline = key in inlineMap ? inlineMap[key] : !String(value).includes('\n');
    if (wasInline) {
      parts.push(`**${label}:** ${value}`);
    } else {
      parts.push(`**${label}:**\n${value}`);
      parts.push('');
    }
  }

  const heading = e._heading || e.title || '';
  parts.push(`## Entry ${e.raw_id}: ${heading}`);
  parts.push('');

  addField('Title',             e.title || '',            'title');
  addField('Issue Type',        e.issue_type || '',       'issue_type');
  addField('Situation',         e.situation || '',        'situation');
  addField('Resolution',        e.resolution || '',       'resolution');
  addField('Exceptions',        e.exceptions || '',       'exceptions');
  addField('Approval Required', e.approval_required || '','approval_required');

  for (const ef of (e.extra_fields || [])) {
    const efInline = '_inline' in ef ? ef._inline : !String(ef.value || '').includes('\n');
    if (efInline) {
      parts.push(`**${ef.label}:** ${ef.value}`);
    } else {
      parts.push(`**${ef.label}:**\n${ef.value}`);
      parts.push('');
    }
  }

  addField('Last Updated', e.last_updated || '', 'last_updated');
  return parts.join('\n');
}

function serializeKbFile(header, entries) {
  const updatedHeader = header.replace(
    /^Entry count: \d+/m,
    `Entry count: ${entries.length}`
  );
  const parts = [updatedHeader, ...entries.map(serializeEntry)];
  return parts.join('\n\n---\n\n') + '\n';
}

function stripInternal(entry) {
  const result = Object.fromEntries(
    Object.entries(entry).filter(([k]) => !k.startsWith('_'))
  );
  result.extra_fields = (entry.extra_fields || []).map(ef =>
    Object.fromEntries(Object.entries(ef).filter(([k]) => !k.startsWith('_')))
  );
  return result;
}

function nextEntryId(entries) {
  if (!entries.length) return '1';
  const nums = [];
  let prefix = '';
  for (const e of entries) {
    // Diverges from Python admin_server.py to handle alphanumeric prefixes (e.g. "B2B-").
    // The Python version (regex /^([A-Z]+-)?(\d+)[a-z]?$/) is being deprecated by this
    // Vercel migration — admin_server.py will not be used in production.
    const m = e.raw_id.match(/^((?:[A-Z0-9]+-)+)?(\d+)[a-z]?$/);
    if (m) {
      prefix = m[1] || '';
      nums.push(parseInt(m[2], 10));
    }
  }
  if (nums.length) return prefix + String(Math.max(...nums) + 1);
  return entries[entries.length - 1].raw_id + '_new';
}

function readBody(req) {
  return new Promise((resolve, reject) => {
    let body = '';
    req.on('data', chunk => (body += chunk));
    req.on('end', () => {
      try { resolve(JSON.parse(body)); } catch { resolve({}); }
    });
    req.on('error', reject);
  });
}

function getOctokitConfig() {
  const required = ['GITHUB_TOKEN', 'GITHUB_OWNER', 'GITHUB_REPO', 'GITHUB_BRANCH'];
  const missing = required.filter(k => !process.env[k]);
  if (missing.length) {
    throw new Error(`Missing env vars: ${missing.join(', ')}`);
  }
  return {
    owner: process.env.GITHUB_OWNER,
    repo: process.env.GITHUB_REPO,
    branch: process.env.GITHUB_BRANCH,
    token: process.env.GITHUB_TOKEN,
  };
}

let _octokitInstance = null;
function getOctokit() {
  if (!_octokitInstance) {
    const { Octokit } = require('@octokit/rest');
    const cfg = getOctokitConfig();
    _octokitInstance = new Octokit({ auth: cfg.token });
  }
  return _octokitInstance;
}

module.exports = {
  parseEntry, parseKbFile,
  serializeEntry, serializeKbFile,
  stripInternal, nextEntryId,
  readBody,
  getOctokit, getOctokitConfig,
};
