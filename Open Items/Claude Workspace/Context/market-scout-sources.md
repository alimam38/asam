# Market scout — sources (tunable)

_Draft created 2026-07-13; migrated from Dropbox to the repo 2026-07-13. GitHub queries run
through an authenticated GitHub connector when available (Composio in Cowork, GitHub MCP in
Claude Code cloud sessions), otherwise web search; HN via the public Algolia API; X via one
API attempt then web fallback._

## GitHub (authenticated search when available; sort=updated or created, last ~4 days for Tue run / ~4 days for Fri run)
- topic:ai-agents · topic:llm-agents · topic:agent-framework
- topic:mcp · topic:mcp-server (marketplace-level movers; the skills scout handles per-item vetting)
- "agent memory" OR "agent orchestration" in:description created:>{lookback}
- Release radar (check recent releases/commits): anthropics/* · modelcontextprotocol/* · vercel-labs/skills

## Discussion layer
- HN Algolia API (bash curl): https://hn.algolia.com/api/v1/search_by_date?query=X&tags=story&numericFilters=created_at_i>{epoch}
  queries: "claude", "mcp", "ai agent", "llm"
- Anthropic news & engineering: anthropic.com/news · anthropic.com/engineering · release notes/changelogs

## X / Twitter
- Queries: "claude code" OR "cowork", "MCP server", "agent framework" (min engagement; skip retweets)
- NOTE: X API currently has no credits (402) — one cheap attempt max, then WebSearch fallback; label "X via fallback".

## Cadence note
Tue run covers Sat–Mon; Fri run covers Tue–Thu. Seen-index dedups across runs.
