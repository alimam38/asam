# Skills Scout — 2026-09-12

Window: since the 2026-09-10 digest (no 09-11 run), so ~Sept 10–12. SerpAPI used (3 date-restricted calls) + built-in search + GitHub API. Sources per `skills-scout-sources.md`; trust tier noted per item.

## Official / Tier 1

- **Claude Code v2.1.268–269 (Sep 10–11) — `claude plugin eval` lands.** Run a plugin's eval suite against Claude Code and get scored, reproducible results (JSON + HTML report), with a new docs page (code.claude.com/docs/en/plugin-evals). Also: `/output-style [name]` switching incl. headless/remote sessions; `bashEditDiffEnabled` (diffs of files a Bash command changed); `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` (raise Workflow fan-out to 256); gateway pricing parity in `/cost`; plugin-archive permission hardening; Slack scheduled routines can now reply in an existing thread instead of always posting top-level; Cowork local sessions with approvals skipped now refuse artifact reads outside session folders. Why it matters: `plugin eval` closes the loop with `/skill-doctor` and skill-creator evals — your skill/plugin curation lane gets a real regression harness; the Slack routine threading and Workflow concurrency touch your scheduled-task fleet directly. Trust: Anthropic-verified (changelog).
- **Smart Reports (Beta) — Claude App (Sep 10).** Analyzes how a team uses Claude and reports on work done, cost, session friction, and which repeated patterns are worth packaging as shared skills. Why: that last clause is your skill-curation flywheel made official — usage → candidate skills; relevant to Cowork ops and (later) tenant-facing Plumbline analytics framing. Trust: Anthropic-verified (release notes via releasebot.io/updates/anthropic).
- **Managed Agents `auto` permission policies + `ant beta:sessions connect` (Sep 10, Developer Platform).** Server-side evaluation of tool calls against permission policies, and terminal attach to live sessions for real-time monitoring/approval; the official claude-api skill was updated same day (anthropics/skills #1750). Why: this is the governance-not-guardrails/approval-gate pattern (Aegis lane) shipping as first-party infrastructure — worth reading before building custom approval plumbing. Trust: Anthropic-verified.

## Skills & plugin ecosystem

- **cathrynlavery/diagram-design — 38 editorial diagram types as an Agent Skill** (self-contained HTML + inline SVG, explicitly anti-"Mermaid slop"; ~38.7k★, 2.4k forks) [backfilled — Apr 2026, surfaced now via fresh activity]. Has spawned a real fork ecosystem (AWS-branded variant, a WCAG-AA/brand-token agency fork). Why: your deliverables lean hard on self-contained HTML/SVG diagrams (archify surfaced 08-31 is the workflow cousin); this is the editorial/diagram-type vocabulary side. Star counts unvetted (inflation pattern seen before), but the fork ecosystem is genuine. Trust: Tier 3 community — review SKILL.md before install.
- **Kin Lane (API Evangelist), "Agent Skills: New Value, New Problems" (Sep 10).** Analysis piece: skills sprawl is coming, rhyming with MCP-server sprawl — discovery, governance, and versioning problems named early. Why: exactly the curation problem this scout exists for, and useful framing for the Aegis governance lane. Trust: Tier 3 — known independent API analyst; commentary, not code.

## Fintech / lending — Meridia & Hypomone

- **Lendscape MCP server for asset/equipment finance** [backfilled — June 2026]. Commercial-lending platform (receivables/asset finance) exposing live lender data to AI assistants (Anthropic/OpenAI/Microsoft) with policy validation before any action executes; servicing, collections, portfolio-management workflows. Why: another regulated-lender MCP precedent with a compliance gate in the loop — joins Blend Autopilot, Nymbus, and Bud in your Gate-3+ pattern file for Hypomone Capital. Trust: Tier 2 — vendor press (Finextra/Equipment Finance News); no public repo sighted.
- **FirstTouch human-approval outreach MCP (Sep 10 post).** Agent proposes every outbound send; a person approves; everything logged to CRM. Why: small, but it's the propose→approve→audit-trail pattern (Aegis) applied to GTM outreach — relevant shape for founding-member outreach when Hypomone's Charter goes live. Trust: Tier 4 — vendor blog, unverified product.

## Governance / audit — Aegis

- **Oracle Integration MCP Gateway (announced ~Sep 10).** One governed path for enterprise agents to reach MCP servers instead of direct per-server access — centralized authz, audit, and control. Why: the MCP-gateway governance pattern keeps institutionalizing (joins lunar.dev, ToolHive, Collibra in the seen index); good comparable for Aegis's governed-core positioning. Trust: Tier 2 — official Oracle blog; enterprise-stack specific.

## Education / K-12 — Recess

- **"Best MCP Servers for Education and L&D (2026)" — minicoursegenerator.com (Sep 11).** Claims to have verified every education MCP server it lists and catalogs learning-activity Agent Skills types. Why: a fresh discovery sweep for the Recess lane cheaper than doing it yourself — mine it, don't trust it. Trust: Tier 4 — vendor roundup (they sell a course generator); verify every item independently.
- No new official Claude-education motion since Beneficial Deployments (surfaced 09-08); Claude for Teachers items circulating this week are July coverage.

## Lane checks with nothing new

- **Populi / SIS**: nothing new (populi-mcp surfaced 07-02 remains the only direct connector).
- **Postgres**: nothing new in-window; pgEdge "GA" stories circulating are April news, pgEdge already surfaced 06-21.
- **MCP spec/registry**: no in-window announcements; next spec target (Dec 15) unchanged from the 08-31 watch item.
- **Vendor skills-repo wave**: continues (LambdaTest, API7, Epic Games bumps) — logged to skipped-log as off-lane; the wave itself was surfaced 07-30.

---
*SerpAPI: 3/3 budget calls used (site:github.com 2-day sweep, Anthropic/Claude news 2-day, governance/education 2-day). Seen-index dedup applied (vercel-labs/skills, firebase/agent-skills, resend-skills, tech-leads-club, Blend, Nymbus, Bud, openbankingtracker, populi-mcp, yuna78/html-to-pptx all already surfaced).*
