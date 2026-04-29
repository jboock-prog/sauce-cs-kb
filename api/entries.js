'use strict';

const { Octokit } = require('@octokit/rest');
const { parseKbFile, stripInternal } = require('./_kb');

const KB_FILES = [
  'kb-refunds.md', 'kb-b2c.md', 'kb-b2b.md',
  'kb-general.md', 'kb-operations.md',
];

module.exports = async (req, res) => {
  if (req.method !== 'GET') {
    return res.status(405).json({ ok: false, error: 'Method not allowed' });
  }

  const octokit = new Octokit({ auth: process.env.GITHUB_TOKEN });
  const results = [];

  for (const filename of KB_FILES) {
    const fileObj = { filename };
    try {
      const { data } = await octokit.rest.repos.getContent({
        owner: process.env.GITHUB_OWNER,
        repo: process.env.GITHUB_REPO,
        path: filename,
        ref: process.env.GITHUB_BRANCH,
      });
      const content = Buffer.from(data.content, 'base64').toString('utf-8');
      const { header, entries } = parseKbFile(content);
      fileObj.header = header;
      fileObj.entries = entries.map(stripInternal);
      fileObj.error = null;
    } catch (e) {
      fileObj.header = '';
      fileObj.entries = [];
      fileObj.error = e.message;
    }
    results.push(fileObj);
  }

  res.json({ ok: true, files: results });
};
