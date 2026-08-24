# Skills Scout — 2026-08-24

Scan window: ~Aug 23–24 (since yesterday's digest). Method: SerpAPI (3/3 date-restricted calls: last-24h GitHub sweep, Google News, venture-lane sweep) + built-in web search + GitHub API (new-repo search, Tier 1 repo commit logs). Quiet weekend overall — one platform incident, one large backfill find, thin community churn.

## Official / Tier 1

- **Claude platform outage, Aug 24 (resolved)** — elevated errors across Claude models/products for roughly 3+ hours early this morning UTC; Anthropic reported normal operations restored by ~10:30 UTC. Why it matters: anything scheduled this morning — Cowork scheduled tasks, Managed Agents crons — may have failed or degraded silently; worth re-running anything time-sensitive from today. Trust: Tier 1 origin (Anthropic status) via broad press (PCMag, Mashable, Android Authority).
- **Tier 1 repos and changelog quiet** — anthropics/skills: no commits since the 08-22 claude-api SDK item. claude-plugins-official: version bumps only plus Claude Security v0.10.2 (increment of the 08-22 Mythos/Claude Security item). claude-plugins-community: no commits. Claude Code v2.1.240–241 shipped with changelog text of "bug fixes and reliability improvements" only. Trust: Tier 1, checked directly.

## Design & documents (Plumbline / venture collateral)

- **tw93/Kami — print-grade document design system (plugin + skill + MCP renderer)** [backfilled] — ~10k★. "Good content deserves good paper": eight opinionated templates (résumé, one-pager, letter, portfolio, slides, equity report, changelog) under a strict unified design system (parchment background, ink-blue accents, serif type), shipped as a Claude Code plugin, a Claude Desktop skill, and an MCP server so any agent can use it as a rendering engine; auto-triggers from natural requests. Why it matters: board-facing one-pagers and decks for Plumbline/Turner plus venture collateral (WayPoint one-pagers, Hypomone Charter docs) without hand-designing each document; same author as Waza (surfaced 07-25). Established since at least July (v1.10) but never crossed the scout's feeds until a docs refresh today — logged as backfill. Trust: Tier 3 — known author, large traction; review template output before sending to external audiences.

## Claude Code / agentic dev

- **PiLastDigit/Code-With-Claude** — 88★ day one; full transcripts of all 19 Code w/ Claude 2026 (San Francisco) talks, machine-transcribed (Deepgram Nova-3) with per-talk summaries. Why it matters: the conference's agentic-context/skills/orchestration content in searchable text — useful corpus for the Claude/Cowork lane (the 06-22 recap items came from secondhand writeups). Trust: Tier 4 — unofficial machine transcripts; verify wording against video before quoting.
- **aiopshwang verification-skill trio** — `evidence-first-problem-solving`, `verify-regression-tests`, `ship-mobile-app` (8★ each, day one, single author; Claude Code + Codex). Standout: verify-regression-tests checks that a regression test actually fails on the intended bug and passes with the fix — catching "false greens" from mocks, gates, fallbacks, and fixtures. Why it matters: clean addition to the verification-loop pattern library (Aegis-adjacent QA discipline). Trust: Tier 4 — brand-new, unknown author; read the SKILL.md before installing.

## Recess / K-12
Searched (SerpAPI lane sweep + web): nothing new beyond items already surfaced (k12-teacher-skills 08-09, DeepTutor 08-18). One teacher-facing explainer blog logged to skipped.

## Meridia–Hypomone / fintech-lending
Searched: nothing new. Blend's lending MCP resurfaced in press but was surfaced 08-04; an unverified banking-MCP vendor directory logged to skipped.

## Aegis / governance
Nothing new beyond the promptfoo/JFrog/Cloudflare governance items surfaced 08-19/08-21.

## Populi / Postgres / NAS
Nothing new. The only "Postgres tuning skill" hit in the last-24h sweep was part of the genpark SEO-farm flood (avoid; pattern logged 08-21/22).

---
11 items logged to the skipped log (increments, spam-pattern continuations, low-signal churn, and two install-with-caution security flags: Wbrowser and tikeytaka).
