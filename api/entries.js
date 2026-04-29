'use strict';

const { parseKbFile, stripInternal, getOctokit, getOctokitConfig } = require('./_kb');

const KB_FILES = [
  'kb-refunds.md', 'kb-b2c.md', 'kb-b2b.md',
  'kb-general.md', 'kb-operations.md',
];

async function loadFile(octokit, cfg, filename) {
  const fileObj = { filename };
  try {
    const { data } = await octokit.rest.repos.getContent({
      owner: cfg.owner,
      repo: cfg.repo,
      path: filename,
      ref: cfg.branch,
    });
    if (data.type !== 'file') {
      throw new Error('Path is not a file');
    }
    const content = Buffer.from(data.content, 'base64').toString('utf-8');
    const { header, entries } = parseKbFile(content);
    fileObj.header = header;
    fileObj.entries = entries.map(stripInternal);
    fileObj.error = null;
  } catch (e) {
    console.error(`Failed to load ${filename}:`, e.message);
    fileObj.header = '';
    fileObj.entries = [];
    fileObj.error = e.status === 404 ? 'File not found'
                  : e.status === 401 || e.status === 403 ? 'Auth failure'
                  : 'Load failed';
  }
  return fileObj;
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
    KB_FILES.map(filename => loadFile(octokit, cfg, filename))
  );

  const ok = results.every(r => !r.error);
  res.json({ ok, files: results });
};
