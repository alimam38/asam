# Skills Scout — 2026-08-18

Scan window: since the 2026-08-17 digest (~24h). SerpAPI recency layer used (3/3 budget). Sources and trust tiers per skills-scout-sources.md.

## Official / Tier 1

1. **Two new official skills in anthropics/skills (Aug 17)** — `discernment-nudge` (opt-in; appends 2–3 targeted follow-up questions after substantive answers so the user checks key facts before acting on them) and `claude-academy-guide` (recommends matching Claude Academy courses when you ask how to use Claude or a Claude product). Why: discernment-nudge is a lightweight verification-posture pattern worth studying for Aegis-style "governance not guardrails" UX; academy-guide is the routing layer for the Academy (next item). Trust: Anthropic-verified (Tier 1). — github.com/anthropics/skills (PRs #1553, #1554)

2. **Claude Academy (academy.claude.com)** — official course platform (e.g. "Claude 101"), now cross-referenced by an official skill — a signal Anthropic is pushing it as the canonical learning path. Why: ready-made onboarding material for Plumbline tenant staff (Turner) and the Recess "Claude in education" watch; also personal Cowork/Code upskilling. Trust: Tier 1 (official site, live); exact launch date/catalog newness unverified.

3. **Official changelog quiet** — no Claude or Claude Code release-notes entries Aug 16–18 (latest remains v2.1.233, Aug 15). Official plugin marketplace: version bumps only (carta, stripe, neon, wix, jfrog, databricks…), no new vendors.

## Claude / Cowork / agent tooling

4. **yetone/cumora** — "where agent teams gather": cross-platform team chat where AI agents are first-class teammates, with cloud or bring-your-own Claude Code / Codex brains. ~2.1k★ and 220 forks within 24h of creation (Aug 17); author maintains avante.nvim. Why: strongest signal yet on the chat-room-as-agent-orchestration-surface pattern — adjacent to the Cowork SendMessage / fleet-session mechanics your scheduled jobs already use. Trust: known author but day-one repo (Tier 3) — sandbox before giving it credentials. — github.com/yetone/cumora

5. **Grafana gcx + MCP server GA** (InfoQ, Aug 17) — Grafana's agent-facing CLI and MCP server for telemetry-driven agent development reached GA. Why: NAS/Docker/Postgres ops lane — a governed way for agents to read metrics/dashboards if Grafana joins the Synology stack; also a reference implementation for telemetry-aware agents. Trust: Tier 2 (major vendor, GA). — infoq.com/news/2026/08/grafana-mcp-server-telemetry

## Recess / K-12 & education

6. **HKUDS/DeepTutor** [backfill — created Dec 2025, active this week] — agent-native "lifelong personalized tutoring" workspace: tutoring, problem solving, quiz generation, research, visualization, and mastery practice in one loop; ~36k★, from the HKU Data Science lab (LightRAG authors). Why: the closest large OSS analog to Recess's tutoring / math-gap / prerequisite-routing concepts — worth reading its mastery-practice and quiz-generation design even if never deployed. Trust: reputable academic lab (Tier 3); not FERPA/COPPA-scoped out of the box. — github.com/HKUDS/DeepTutor

Otherwise the K-12 lane turned up nothing new in-window (Claude for Teachers / k12-teacher-skills surfaced 08-09).

## Meridia / Hypomone (fintech & lending data)

7. Lane searched (Plaid / lending / CDFI / community-bank × MCP/skills, last 24h) — nothing new beyond Plaid MCP early access (surfaced 08-17). In-window fintech MCP press was off-stack (MongoDB Atlas managed MCP; D&B on watsonx) — logged, not surfaced.

## Aegis (governance / audit)

8. Nothing new in-window; nearest item is discernment-nudge (item 1) as a verification-posture pattern. (ICML counterfactual-trace-audit paper was logged 08-17.)

Populi/SIS lane: nothing new (populi-mcp unchanged since 07-02). Grants/KSW lane: nothing in-window; a federal-contracting Agent Plugins pack was logged as adjacent-not-fit.

---
SerpAPI: available, 3/3 calls spent. Non-fits and increments → skipped-log.md.
