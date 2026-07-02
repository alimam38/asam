# Skills Scout — 2026-06-21 (corrected run)

Note: the prior scheduled run produced output but couldn't **save** it — the `asam` repo
wasn't a connected folder, so the digest had nowhere to land. That's now fixed (folder
connected). This run applies the updated rules: Claude Design is in-focus, and the recency
rule is loosened so foundational items promoted from yesterday's skip list can surface.
Deduped against the 4 items already in seen-index. Freshness caveat still applies — web
search can't pin exact publish dates, so "fresh" means current-week.

## Items

### 1. Claude Design — recent updates (canvas editing, Claude Code sync)
- **What:** New canvas-editing controls plus sync between Claude Design and Claude Code.
- **Why relevant:** Now an explicit focus (#5 — understanding Claude Design and when to use it).
  The Code sync is the bridge from a Design mockup to a real build — directly useful for the
  Plumbline UI.
- **Source:** https://support.claude.com/en/articles/12138966-release-notes
- **Trust:** Tier 1 — Anthropic-verified. Promoted from yesterday's skip now that Design is in-focus.

### 2. Git MCP server (official)
- **What:** An MCP server exposing git operations (status, diff, commit, branch) to agentic sessions.
- **Why relevant:** Your GitHub lane (#8) — and a clean answer to the commit friction we hit this
  session. Lets an agent do git through a defined tool instead of raw shell against a Dropbox `.git`.
- **Source:** official MCP servers — https://github.com/modelcontextprotocol/servers (confirm exact repo)
- **Trust:** Tier 1/2 — official/known. Promoted from skip under the loosened recency rule
  (foundational outweighs strictly-fresh).

### 3. Postgres MCP servers — pgEdge & YawLabs
- **What:** MCP servers for PostgreSQL introspection/ops (query, schema, health checks), self-hostable.
- **Why relevant:** Your NAS / Docker / Postgres lane — for a self-hosted Plumbline/Turner database.
  Pairs with the call518 DBA server surfaced yesterday.
- **Source:** via PulseMCP / Glama (pgEdge MCP; YawLabs Postgres MCP) — confirm exact repos.
- **Trust:** Tier 2/3 — known/community → install-with-caution; vet read-only scoping and credentials
  before pointing at prod.

## Skipped (logged to skipped-log.md)
- General MCP directory churn (Glama / mcp.so daily new entries) — high volume, low per-item signal.
- Minor Claude Code changelog items — below the bar for a daily five.
