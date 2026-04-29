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
  const { filename, raw_id: rawId } = body;
  if (!filename || !rawId) {
    return res.status(400).json({ ok: false, error: 'filename and raw_id required' });
  }

  try {
    const { header, entries, sha } = await loadKbFile(octokit, cfg, filename);

    const filtered = entries.filter(e => e.raw_id !== rawId);
    if (filtered.length === entries.length) {
      return res.status(404).json({ ok: false, error: `Entry ${rawId} not found` });
    }

    await commitKbFile(octokit, cfg, {
      filename, header, entries: filtered, sha,
      message: `Admin: delete entry ${rawId} from ${filename}`,
    });

    res.json({ ok: true });
  } catch (e) {
    console.error(`delete ${filename} failed:`, e.message);
    const { status, msg } = mapWriteError(e, 'Delete');
    res.status(status).json({ ok: false, error: msg });
  }
};
