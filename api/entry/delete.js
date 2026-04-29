'use strict';

const {
  parseKbFile, serializeKbFile,
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
    const { data } = await octokit.rest.repos.getContent({
      owner: cfg.owner, repo: cfg.repo, path: filename, ref: cfg.branch,
    });
    if (data.type !== 'file') throw new Error('Path is not a file');

    const content = Buffer.from(data.content, 'base64').toString('utf-8');
    const { header, entries } = parseKbFile(content);

    const originalLen = entries.length;
    const filtered = entries.filter(e => e.raw_id !== rawId);
    if (filtered.length === originalLen) {
      return res.status(404).json({ ok: false, error: `Entry ${rawId} not found` });
    }

    const newContent = serializeKbFile(header, filtered);
    await octokit.rest.repos.createOrUpdateFileContents({
      owner: cfg.owner, repo: cfg.repo, path: filename, branch: cfg.branch,
      message: `Admin: delete entry ${rawId} from ${filename}`,
      content: Buffer.from(newContent, 'utf-8').toString('base64'),
      sha: data.sha,
    });

    res.json({ ok: true });
  } catch (e) {
    console.error(`delete ${filename} failed:`, e.message);
    const msg = e.status === 401 || e.status === 403 ? 'Auth failure'
              : e.status === 404 ? 'Not found'
              : e.status === 409 ? 'Conflict — file changed since read'
              : 'Delete failed';
    res.status(500).json({ ok: false, error: msg });
  }
};
