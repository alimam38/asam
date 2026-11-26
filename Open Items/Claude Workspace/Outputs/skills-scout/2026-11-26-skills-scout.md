# Skills Scout — 2026-11-26

_Run: scheduled, cloud-only. Window: last 24–48h (US Thanksgiving — light news day). SerpAPI used (3/3 calls: 2× `qdr:d` web, 1× Google News). Venture depth judged from current-focus.md summaries; STATUS.md files not re-read this run._

## Official / Tier 1
- Nothing new from Anthropic in the last 24h beyond items already surfaced 11-24/11-25 (Plugins page, Skills over MCP beta, Claude Ship, Artifacts desktop apps). Anthropic news/engineering, claude.com/blog and support release notes checked.

## Standing lanes — MCP / connectors / governance
1. **Google Workspace official MCP servers (Gmail, Drive, Calendar, etc.)** — Google's own remote MCP endpoints with a setup guide that names Claude as a supported client (OAuth consent screen, per-product endpoints, prompt-injection warnings). **Why it matters:** first-party, governed alternative to the community/Composio Gmail paths in your stack; relevant to every lane that touches mail/Drive (Talbot ops, Plumbline, Hypomone intake). A community short claims Google is pushing agents to MCP-only Workspace access from 1 Feb 2027 — **unverified, treat as rumor** until Google confirms. **Trust:** Tier 2 (Google official docs) — developers.google.com/workspace/guides/configure-mcp-servers · developers.google.com/workspace/gmail/api/guides/configure-mcp-server
2. **Microsoft Agent 365 — admin governance for plugins, skills and MCP servers** — M365 admin center flows to upload/allow/block plugins and skills, approve MCP-server registrations, and block individual tools inside a server (blocking stops governed use but doesn't revoke direct access). **Why it matters:** Aegis lane — a concrete enterprise reference model for approval/registration/tool-level allow-lists, and the Microsoft counterpart to Claude's unified Plugins page. [backfill: doc dated Nov 6, updated Nov 16] **Trust:** Tier 2 (Microsoft Learn) — learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-plugins-skills-mcp-servers
3. **Duco MCP server (GA)** — post-trade reconciliation vendor exposes break investigation and exception workflows to any MCP agent; agents propose fixes, prompt a human for the decision, and every action is audit-logged inside existing permissions. **Why it matters:** Aegis (human-decision gate + audit log pattern, in production) and Meridia/Hypomone (ledger reconciliation as an agent workflow). Not a tool you'd adopt — a pattern to copy. **Trust:** Tier 2 (vendor + trade press) — du.co/duco-mcp-server-brings-agentic-operations-for-post-trade-into-production · finadium.com/duco-touts-mcp-server-for-audited-agentic-ai-operations-in-post-trade
4. **MCP reference servers: proposal to bundle Agent Skills (git server first)** — open issue proposing a self-contained `skills/mcp-server-git/SKILL.md` (standard frontmatter) shipped with the reference git server, teaching agents how to use it. **Why it matters:** the official MCP project adopting the Skills-over-MCP pattern Anthropic launched 11-24 — a template for how your own MCP servers (Plumbline/Populi, Meridia data) should ship usage skills. Proposal only. **Trust:** Tier 2 (official MCP org, open issue) — github.com/modelcontextprotocol/servers/issues/5659

## Venture lanes
- **Recess / K-12:** searched (SerpAPI + web) — nothing new in window.
- **Meridia / Hypomone (fintech, lending data):** nothing new beyond Duco above; financial-news/filings MCPs seen were duplicative of existing connectors (logged to skipped).
- **Populi / SIS, KSW, grants:** nothing new in window.

---
**Ask:** pick any to adopt or prototype — top candidate: **Google Workspace official MCP** (test Gmail/Drive endpoints against your current Gmail connector; verify the Feb-2027 claim first).
