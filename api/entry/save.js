'use strict';

const {
  loadKbFile, commitKbFile, mapWriteError,
  getOctokit, getOctokitConfig,
  readBody,
} = require('../_kb');

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    return res.status(405).json({ ok: false, error: 'Method not allowed' });
  }

  let cfg, octokit;
  try {
    cfg = getOctokitConfig();
    octokit = getOctokit();
  } catch (e) {
    return res.status(500).json({ ok: false, error: e.message });
  }

  const body = await readBody(req);
  const { filename, entry: entryData } = body;
  if (!filename || !entryData) {
    return res.status(400).json({ ok: false, error: 'filename and entry required' });
  }

  try {
    const { header, entries, sha } = await loadKbFile(octokit, cfg, filename);

    const rawId = entryData.raw_id;
    const idx = entries.findIndex(e => e.raw_id === rawId);
    if (idx === -1) {
      return res.status(404).json({ ok: false, error: `Entry ${rawId} not found in ${filename}` });
    }

    const oldEntry = entries[idx];
    delete entryData._raw;
    if (!entryData._heading) {
      entryData._heading = entryData.title || oldEntry._heading || '';
    }
    if (!entryData._inline) {
      entryData._inline = oldEntry._inline || {};
    }
    const oldExtraByLabel = Object.fromEntries(
      (oldEntry.extra_fields || []).map(ef => [ef.label, ef])
    );
    for (const ef of (entryData.extra_fields || [])) {
      if (!('_inline' in ef)) {
        const oldEf = oldExtraByLabel[ef.label];
        if (oldEf) ef._inline = oldEf._inline;
      }
    }
    entries[idx] = entryData;

    await commitKbFile(octokit, cfg, {
      filename, header, entries, sha,
      message: `Admin: update entry ${rawId} in ${filename}`,
    });

    res.json({ ok: true });
  } catch (e) {
    console.error(`save ${filename} failed:`, e.message);
    const { status, msg } = mapWriteError(e, 'Save');
    res.status(status).json({ ok: false, error: msg });
  }
};
