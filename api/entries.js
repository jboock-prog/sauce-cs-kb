'use strict';

const {
  stripInternal,
  loadKbFile,
  getOctokit, getOctokitConfig,
} = require('./_kb');

const KB_FILES = [
  'kb-refunds.md', 'kb-b2c.md', 'kb-b2b.md',
  'kb-general.md', 'kb-operations.md',
];

async function readOne(octokit, cfg, filename) {
  try {
    const { header, entries } = await loadKbFile(octokit, cfg, filename);
    return { filename, header, entries: entries.map(stripInternal), error: null };
  } catch (e) {
    console.error(`Failed to load ${filename}:`, e.message);
    const error = e.status === 404 ? 'File not found'
                : e.status === 401 || e.status === 403 ? 'Auth failure'
                : 'Load failed';
    return { filename, header: '', entries: [], error };
  }
}

module.exports = async (req, res) => {
  if (req.method !== 'GET') {
    return res.status(405).json({ ok: false, error: 'Method not allowed' });
  }

  let cfg, octokit;
  try {
    cfg = getOctokitConfig();
    octokit = getOctokit();
  } catch (e) {
    return res.status(500).json({ ok: false, error: e.message });
  }

  const results = await Promise.all(
    KB_FILES.map(filename => readOne(octokit, cfg, filename))
  );

  const ok = results.every(r => !r.error);
  res.json({ ok, files: results });
};
