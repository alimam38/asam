# Skills Scout — 2026-09-04

Window: since the 2026-09-03 run (Sep 3–4, ~24h). Sources per skills-scout-sources.md; deduped against seen-index.md.

## Official / Tier 1

- **Claude Code v2.1.259 (Sep 3)** — introduces **managed MCP servers** (centrally-administered MCP config), headless permission controls, GitLab merge-request recognition, JSON plugin validation, faster startup, and broad fixes for concurrency, resume, permissions, and **remote/scheduled sessions**. *Why it matters:* managed MCP + headless permissions is the admin/governance shape of MCP arriving in the CLI itself (Aegis-pattern relevant), and the remote-session stability fixes bear directly on your scheduled-task fleet — third stability pass in a week. Trust: Tier 1 (code.claude.com changelog, via releasebot).
- **Sep 3 platform outage (~13:41 UTC onward)** — elevated errors across Mythos 5.1/5, Fable 5.1/5, and Opus 5/4.8/4.6; Anthropic identified the cause and remediated through the morning ET. *Why:* second multi-model outage in ~10 days (Aug 24 logged previously) — morning scheduled runs on Sep 3 may have degraded; worth a glance at that day's task outputs. Trust: Tier 1 origin (status.anthropic.com via BleepingComputer).
- **"Use artifacts in Claude Cowork" help article (support.claude.com/articles/14729249, updated in the last 24h)** — official documentation for artifacts inside Cowork, which pairs with the artifacts-in-Claude-Code beta (surfaced 07-13) and your live-artifacts domain. *Caveat:* the article body couldn't be fetched from this sandbox (support.claude.com fetch gate) — item is from the search index only; open it directly for the details. Trust: Tier 1, partially verified.
- **Skill & plugin scanning "get started" doc refresh (support.claude.com/articles/15927065, updated in the last 24h)** — the scanning feature surfaced 08-08 as Enterprise beta now has a refreshed getting-started article; possible availability broadening. Same fetch caveat as above. Trust: Tier 1, partially verified.
- **Official plugin marketplace:** no new plugin adds this window — only routine version bumps (carta ×3, salesforce-development, convex, jfrog, figma, logfire, growthbook, etc.). anthropics/skills: one minor update (frontend-design tweaked to avoid generic design defaults, #1713 — logged as increment). Trust: Tier 1 repo observation.

## Claude Code / dev tooling (Tier 2–4)

- **aws/agent-toolkit-for-aws** (~2.5k★) — AWS's official consolidated toolkit of MCP servers, skills, *and* plugins for agents building on AWS, active daily. Distinct from awslabs/agent-plugins (surfaced 08-17); this is the canonical umbrella repo. *Why:* the strongest example yet of the vendor pattern converging on "MCP + skills + plugins in one toolkit" — reference shape for a future Populi/Meridia bundle, and practically useful if any NAS/cloud workload touches AWS. Trust: Tier 2 (official AWS). github.com/aws/agent-toolkit-for-aws
- **Agents365-ai/drawio-skill** (~9k★) — text/real-sources → maintainable .drawio architecture models: a diagram IR, incremental sync that preserves manual layout, multi-view projection (C4/UML/ERD/BPMN), **architecture-as-test with a CI action**, what-if queries, and a built-in MCP server. *Why:* directly usable for Plumbline/Hypomone/Aegis architecture docs that must stay current with code; the architecture-as-test idea is a governance pattern in itself. Trust: Tier 3 (high traction, org author; vet before CI install). github.com/Agents365-ai/drawio-skill
- **michaelshimeles/skills** (~586★, active this window) — agent skills + an AGENTS.md workflow template: isolate work in git worktrees, build to a service layer, prove with evidence, ship with before/after proof and review loops. *Why:* a compact, opinionated dev-methodology pack in the superpowers/addyosmani vein; the evidence-gated shipping loop matches your verification-loop habit. Lane: Claude Code practice. Trust: Tier 3/4 (known dev-educator author). github.com/michaelshimeles/skills

## Governance / security (Aegis + MCP ops)

- **Wiz: active attacks on exposed LiteLLM deployments and MCP servers (Sep 2)** — in-the-wild exploitation targeting AI infrastructure, including internet-exposed MCP servers. *Why:* you run self-hosted Postgres/Docker on a NAS with MCP ambitions — reinforces outbound-only patterns (MCP Tunnels, surfaced 06-28) and never exposing MCP endpoints directly. Trust: Tier 2 press (eSecurityPlanet on Wiz research). esecurityplanet.com/news/news-litellm-mcp-server-attacks
- **Grafana patches critical SSRF affecting Grafana MCP servers (Sep 3)** — fix shipped; Grafana's MCP server was surfaced 08-18. *Why:* if Grafana MCP is anywhere in your observability stack, patch; also another data point that vendor MCP servers are now in the vulnerability-disclosure cycle. Trust: Tier 2 press (SC World). scworld.com/news/grafana-fixes-critical-ssrf-flaw-affecting-grafana-mcp-servers

## Recess / K-12 & SIS-LMS

- **RohanMuppa/brightspace-mcp-server** (39★, npm `brightspace-mcp-server`) — MCP server for D2L Brightspace: grades, due dates, assignments, announcements, rosters, syllabus, course content; works against any school instance from any MCP client. *Why:* small, but the cleanest recent example of a student/LMS-facing MCP built on a SIS-LMS vendor API — a near-direct template for the populi-mcp shape (surfaced 07-02), and FERPA questions apply identically. Trust: Tier 4 (solo student author; read the auth flow before any real-school use). github.com/RohanMuppa/brightspace-mcp-server
- Otherwise quiet: no new Claude-in-education moves in this 24h window (last wave fully surfaced through 08-30).

## Product / GTM

- **sergebulaev/linkedin-skills** (~841★) — 11 Claude Code/Codex skills for LinkedIn: human-sounding posts, comments, feed analysis, publishing cadence. *Why:* narrow but real GTM tooling for the founder-distribution motion (Meridia/WayPoint external comms once patents unblock); pairs with the de-AI writing skills already surfaced (sepia 08-29). Trust: Tier 3/4 (established author, MIT-licensed; review before posting as yourself). github.com/sergebulaev/linkedin-skills

## Meridia / Hypomone (fintech & lending data)
- Searched (Plaid/CDFI/CRA/lending + MCP news, GitHub): nothing new this 24h window beyond items already in the seen index.

## Populi / Postgres / NAS
- Searched: nothing new this window — Postgres MCP landscape unchanged (pgEdge/crystaldba/pg-aiguide all previously surfaced).

## KSW / grants
- Searched: nothing new this window.

---
*SerpAPI used: 3/3 budgeted calls (24h-scoped site:github.com + official-domains queries, plus Google News). Support-article fetches blocked by sandbox provenance gate (noted inline). Seen-index checked; true non-fits/increments logged to skipped-log.md.*
