'use strict';

const {
  loadKbFile, commitKbFile, mapWriteError, nextEntryId,
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
    octokit = await getOctokit();
  } catch (e) {
    return res.status(500).json({ ok: false, error: e.message });
  }

  const body = await readBody(req);
  const { filename, entry: entryData = {} } = body;
  if (!filename) {
    return res.status(400).json({ ok: false, error: 'filename required' });
  }

  try {
    const { header, entries, sha } = await loadKbFile(octokit, cfg, filename);
    entryData.raw_id = nextEntryId(entries);
    entries.push(entryData);

    await commitKbFile(octokit, cfg, {
      filename, header, entries, sha,
      message: `Admin: add entry ${entryData.raw_id} to ${filename}`,
    });

    res.json({ ok: true, raw_id: entryData.raw_id });
  } catch (e) {
    console.error(`new-entry ${filename} failed:`, e.message);
    const { status, msg } = mapWriteError(e, 'Create');
    res.status(status).json({ ok: false, error: msg });
  }
};
