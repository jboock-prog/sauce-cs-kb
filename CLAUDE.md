# Sauce CS KB — Project Context

## What This Is
A Slack bot that serves as a CS (Customer Support) knowledge base for Sauce, a restaurant online ordering platform. Deployed on Railway, powered by Claude via the Anthropic SDK.

## Architecture
- **Single file server**: `server.py` (Flask)
- **KB files**: 5 markdown files (`kb-general.md`, `kb-b2c.md`, `kb-b2b.md`, `kb-operations.md`, `kb-refunds.md`)
- **Deployment**: Railway (Dockerfile + Procfile + nixpacks.toml)
- **Model**: `claude-sonnet-4-6`
- **Dependencies**: flask, anthropic, requests (see `requirements.txt`)

## Endpoints
| Route | Method | Purpose |
|---|---|---|
| `/slack/command` | POST | `/kb` slash command — query the KB |
| `/slack/release` | POST | `/release` slash command — full product release workflow |
| `/slack/kb-update` | POST | `/kb-update` slash command — shorter KB update + announcement |
| `/query` | POST | Query KB — returns structured JSON with answer + metadata (no Slack auth) |
| `/test/release` | POST | Test release workflow — returns JSON (no Slack auth) |
| `/test/kb-update` | POST | Test KB update workflow — returns JSON (no Slack auth) |
| `/health` | GET | Railway health check |

## Environment Variables
| Variable | Status | Purpose |
|---|---|---|
| `ANTHROPIC_API_KEY` | Existing | Claude API access |
| `SLACK_SIGNING_SECRET` | Existing | Slack request verification |
| `SLACK_BOT_TOKEN` | **NEW — needs setup** | Bot OAuth token (`xoxb-...`) for `chat.postMessage` |
| `SUPPORT_CHANNEL_ID` | **NEW — needs setup** | Channel ID for support team announcements |
| `RELEASE_CHANNEL_ID` | **NEW — needs setup** | Channel ID for release confirmations |

## KB Entry Format
Each KB file uses this structure:
```
## Entry PREFIX-N: Short Title

**Title:** Full title
**Issue Type:** Category
**Situation:** When this applies
**Resolution:** Steps...
**Exceptions:** Edge cases
**Approval Required:** Yes/No
**Last Updated:** Date — note
```
Prefixes: `GEN-`, `B2C-`, `B2B-`, `OPS-`, numeric (refunds)

## Recent Work: Product Release Workflows (branch: claude/product-release-workflow-2387o)

### What Was Built (DONE)
- `/slack/release` endpoint — full product release workflow:
  1. Accepts release info via Slack slash command
  2. Claude generates: external knowledge article, KB entry, support announcement
  3. Auto-detects target KB file (Claude picks from the 5 files)
  4. Appends KB entry to disk + refreshes in-memory KB
  5. Posts announcement to support team channel
  6. Posts confirmation + external article to release channel
- `/slack/kb-update` endpoint — shorter workflow (KB entry + announcement only)
- Utility functions: `get_next_entry_id()`, `append_kb_entry()`, `update_entry_count()`, `post_to_slack_channel()`, `parse_workflow_response()`, `query_claude_workflow()`
- Refactored `SYSTEM_PROMPT` into `build_system_prompt()` for dynamic rebuilds
- Thread-safe KB updates via `kb_lock`
- Updated `/health` endpoint with new config checks

### What Still Needs To Be Done (MANUAL STEPS)
1. **Slack App Configuration** (api.slack.com → your app):
   - Add slash command `/release` → `https://<railway-domain>/slack/release`
   - Add slash command `/kb-update` → `https://<railway-domain>/slack/kb-update`
   - Add `chat:write` OAuth scope to bot token
   - Reinstall app to workspace after scope change
2. **Railway Environment Variables**:
   - Set `SLACK_BOT_TOKEN` (from Slack OAuth & Permissions page)
   - Set `SUPPORT_CHANNEL_ID` (right-click channel in Slack → Copy link → extract ID)
   - Set `RELEASE_CHANNEL_ID` (same method)
3. **Invite the bot** to both the support and release channels
4. **Deploy** — push/redeploy on Railway to pick up the new code

### Design Decisions
- Single Claude call per workflow (generates all outputs at once) for consistency + lower latency
- Delimiter-based output parsing (`===SECTION===` markers) — more reliable than JSON
- No new dependencies — `requests` handles Slack Web API calls
- Ephemeral disk on Railway — KB file changes persist until redeploy; team should periodically commit accumulated entries to git
- Auto-detect target KB file via Claude (falls back to `kb-general.md`)
