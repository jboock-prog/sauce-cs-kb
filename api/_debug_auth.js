'use strict';

// TEMPORARY diagnostic endpoint — reports lengths/match only, never the value.
// Remove after debugging the ADMIN_PASSWORD mismatch.
module.exports = async (req, res) => {
  const env = process.env.ADMIN_PASSWORD;
  const hdr = req.headers['x-admin-password'];
  const envStr = typeof env === 'string' ? env : null;
  const hdrStr = typeof hdr === 'string' ? hdr : null;
  res.json({
    envPresent: !!envStr && envStr.length > 0,
    envLen: envStr === null ? null : envStr.length,
    headerPresent: !!hdrStr && hdrStr.length > 0,
    headerLen: hdrStr === null ? null : hdrStr.length,
    exactMatch: envStr !== null && hdrStr !== null && envStr === hdrStr,
    trimmedMatch: envStr !== null && hdrStr !== null && envStr.trim() === hdrStr.trim(),
  });
};
