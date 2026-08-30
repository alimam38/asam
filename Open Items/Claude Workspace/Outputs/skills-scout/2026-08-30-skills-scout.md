# Skills Scout — 2026-08-30

Scan window: Aug 28–30 (since the 08-29 run). Method: SerpAPI (3/3 calls: last-24h GitHub sweep, Google News, lane-scoped week query) + built-in web search + GitHub API (topic searches created:>2026-08-28; anthropics repo commits). Deduped against seen-index through 2026-08-29.

## Official / Tier 1

- **Claude for Teachers — free Enterprise for U.S. K-12 schools & districts** (Aug 28) — Anthropic expanded July's individual-educator offering into a free Enterprise tier for verified schools/districts: SSO, role-based access controls, domain claiming, a school/district-level K-12 Terms + Data Processing Agreement (student data not used for training), teaching skills mapped to academic standards in all 50 states, two new skills co-developed with Learning Commons, and a pilot evaluation in Detroit Public Schools this fall. Free for orgs that sign up by June 30, 2027. **Why it matters (Recess):** this is the FERPA-shaped, admin-managed distribution channel Recess would compete with/ride on — and the Shadow Rock pilot could enroll the school directly for free. Worth an admin sign-up conversation with your wife's school this week. Trust: Anthropic-verified — claude.com/blog/claude-for-teachers-now-available-for-schools-and-districts
- **Quiet Tier-1 weekend otherwise:** no Claude Code release Aug 29–30 (latest remains v2.1.251, surfaced 08-29); no new commits in anthropics/skills; claude-plugins-official's only recent merge was scandit-sdk (#5634, already surfaced 08-29).

## Claude Code / Cowork / agent tooling

- **Vuk97/forward-implementation-first** — day-one skill (25★ in hours) that stops coding agents from stalling real work on their own bookkeeping: hashes, lockfiles, receipts, certification markers, progress metadata. Distinct from the anti-overengineering wave (08-26): this targets process ritual, not code complexity. Cheap to try in Cowork/Claude Code sessions. Trust: unknown author, install-with-caution (Tier 4) — github.com/Vuk97/forward-implementation-first
- **K-Dense-AI/scientific-agent-skills + Mimeograph** — 38k★ "AI Scientist" skills library (165 validated skills) whose org also pins **Mimeograph**: "turn an expert into a SKILL.md or AGENTS.md." Newly active (pushed Aug 29), never surfaced here. **Why it matters:** biggest skills library yet unseen by this scout, and Mimeograph is the most credible entry in the expert→skill distillation wave (video-to-skill 07-31, book-to-skill 08-17) — relevant to your skill-forge/skill-distiller practice. Trust: high-traction known org, verify per-skill (Tier 2/3) — github.com/K-Dense-AI/scientific-agent-skills
- **southleft/design-systems-mcp** — 203★ MCP server acting as a design-systems assistant (components, tokens, patterns) with an explicit agent-facing design-system layer via AGENTS.md/SKILL.md/DESIGN.md. **Why it matters:** direct input to the Claude Design lane (open item #5) — a pattern for making Plumbline/WayPoint UI work design-system-aware rather than one-shot. Not new (2025) but active and never indexed here. Trust: known small studio (Tier 3) — github.com/southleft/design-systems-mcp

## Meridia / Hypomone (fintech, corpus & data infra)

- **jztan/pdf-mcp** — 124★, pushed Aug 30. MCP server for working through large PDFs and whole folders of them without overflowing context: hybrid semantic + keyword search, page-level reads, table/image extraction. **Why it matters:** clean fit for the Meridia corpus/RAG pipeline (regulatory PDFs, FDIC/HMDA docs) and Turner board-package workflows; complements Token Saver (07-30), which compresses cost rather than doing retrieval. Trust: individual author, months of history, active (Tier 3/4) — github.com/jztan/pdf-mcp
- Lending/fintech otherwise quiet: nothing new past Blend Autopilot (08-04), nCino Mortgage MCP (08-22), Plaid MCP early access (08-17).

## Aegis (governance / audit)

- **Collibra MCP Server** — enterprise data-governance vendor now shipping an MCP server that brings its governance/catalog layer (policies, lineage, data contracts) to any agent, Claude included. **Why it matters:** another datapoint that "governance-as-MCP-layer" is becoming a product category — validating the Aegis governed-core thesis and worth a look at their approval/audit surface design. Trust: established vendor, marketing page — verify capability claims (Tier 2) — collibra.com/products/mcp-server

## Lanes searched, nothing new

- Populi / SIS-LMS: nothing beyond populi-mcp (07-02) and Canvas MCP (06-26).
- Postgres / NAS / Docker: nothing beyond pg-aiguide (07-02), supabase/agent-skills (07-31), Neon (07-29).
- KSW (grants / music education): nothing.

## Notes

- SerpAPI: available and used (3/3 budget).
- GitHub topic:claude-skill continues to carry keyword-stuffed spam (flagged 08-26); today's sweep filtered several zero-star throwaways silently only where they were spam-pattern, everything borderline went to the skipped log.
