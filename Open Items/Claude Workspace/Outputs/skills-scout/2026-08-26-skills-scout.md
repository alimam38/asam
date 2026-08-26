# Skills Scout — 2026-08-26

Window: last ~24–48h (deduped against seen index through 2026-08-25). SerpAPI used (3/3 budget: 2× qdr:d GitHub-scoped, 1× Google News). Official repos checked directly via GitHub API; venture STATUS files consulted for relevance.

## Official / Tier 1

- **Claude Code v2.1.243–246** (Aug 24–26) — the meaty release after the quiet 240/241. v2.1.243: `/usage` **Loops breakdown** (per-loop tokens/runs — directly useful for auditing this scout and your other scheduled loops), `modelPicker` + org `modelPricing` settings, `promptCacheTtl`/`subagentPromptCacheTtl`, keyless Console sign-in, `managed` markers on org-managed connectors in `/mcp`//`plugins`, zstd-compressed binary (~75MB vs 340MB) + big memory/startup improvements. v2.1.246: Auto-mode classifier rules tab in `/permissions`, `/cd` now switches settings/hooks/MCP/skills immediately, subagents stopped at maxTurns return output marked partial with a SendMessage continuation hint, and a pile of plugin/skill loading fixes (BOM, `skills/*/SKILL.md` discovery, doubled plugin prefixes). Trust: Anthropic-verified (official changelog).
- **Official skill/plugin repos quiet**: no new commits to anthropics/skills or claude-plugins-community since Aug 25; claude-plugins-official's only change was the NetSuite refresh already surfaced yesterday. Trust: Anthropic-verified.

## Governance, verification & audit (Aegis lane)

- **systempromptio/awesome-ai-agent-governance** — curated list of tools/standards for governing AI agents in production: policy enforcement, audit trails, EU AI Act compliance, MCP + Claude Code security. ★30, maintained since April, pushed yesterday. The closest thing yet to a reading map for the Aegis governance-alert/approval thesis. Trust: known directory (curated by vendor systemprompt.io — Tier 3, check items individually).
- **Morningstar202604/AgentSeed** — anti-hallucination guardrails for coding agents: hybrid Skill + MCP server (6 tools) that verifies code before it's marked done; works across Claude Code/Cursor/Copilot. Fits the verification-loop lane you track for Aegis-style gates. ★8 day-one. Trust: unknown author, install-with-caution (Tier 4).
- **bharat-goel/cobra-skill** — a Goodhart's-law probe: finds the cheapest way a measure can be satisfied *without* achieving its goal, and ships with the eval that measured it. Small (★2) but philosophically on the nose for "governance-not-guardrails" (Meridia patent #3) and gate design. Trust: unknown author (Tier 4); read the SKILL.md, don't just install.

## MCP & agent infrastructure

- **apify/mcpc** — universal CLI client for MCP: persistent sessions, stdio/HTTP, OAuth 2.1, tasks, JSON output for code-mode, proxy for AI sandboxes. ★755, Apache-2.0, actively maintained by Apify. Best-in-class debug/driver tool if you build the Populi or Hypomone MCP servers — pairs with simonw/mcp-explorer (seen 07-29) and the 2026-07-28 stateless spec. Trust: known vendor (Tier 2).
- **bitwarden/ai-plugins** — Bitwarden's official AI plugin marketplace (★137, pushed today). Secrets/credential hygiene inside agent workflows from a security-first vendor — relevant to how you handle keys across NAS/Docker/scheduled runs (cf. the .env-fetch pattern this scout itself uses). Trust: known vendor (Tier 2).

## Skill curation & supply chain

- **nks0614/harnessay** — local-only, zero-dependency: profiles Claude Code context cost, discovers repeated workflows, and regression-tests your skills. Sits at the intersection of `/doctor` (07-13) and the skillbench wave (07-22) but with workflow discovery added. ★3 day-one. Trust: unknown author (Tier 4).
- **⚠ topic:claude-skill spam flood widening** — the GitHub topic is now heavily polluted with keyword-stuffed "2026" repos showing identical suspicious star counts (~115★ each on throwaway accounts), beyond the alphaparkinc farm logged 08-21. Practical rule: distrust topic-page star counts entirely; verify author history + commit dates before installing anything found via topic search. Trust: scout observation from today's topic sweep (Tier 4 signal).

## Product / GTM

- **coreyhaines31/marketingskills** — ★45,700 (not a typo), MIT, actively maintained (pushed Aug 24): CRO, copywriting, SEO, analytics, and growth-engineering skills for Claude Code by Corey Haines (Swipe Files/Conversion Factory). Somehow never surfaced here despite being one of the largest skill repos in existence — the strongest single GTM asset for the Plumbline/MIG go-to-market work. Trust: known author, huge community adoption (Tier 3, verify individual skills before use).

## Design & visual (open item #5 — Claude Design)

- **ConnorRX56/presentation-delivery-skills** — "one sentence in, polished editable PPTX out"; claims reverse-engineered frontend patterns behind Claude Design and Fable for visual design. Day-one ★7. Interesting as a study object for how Claude Design's output patterns transfer to skills. Trust: unknown author (Tier 4).
- **parthjshah95/visual-planning-skills** — tool-agnostic trio: visual-explainer, visual-plan, challenge-plan — single-file interactive HTML explainers and browser-reviewed plans. Matches your "HTML is the new Markdown" + plan-review patterns. ★3. Trust: unknown author (Tier 4).

## Craft wave (brief)

- **Anti-overengineering skill wave** — two same-day entries: alvindemesadev/boring-engineering (turns KISS/YAGNI/DRY into a decision system) and coopersimson96/midwit (every piece of complexity must name the failure it prevents, or it's cut). Useful discipline for the Plumbline/Hypomone build sessions where scope creep is the enemy. Both day-one ★6–7. Trust: unknown authors (Tier 4).

## Lanes searched, nothing new

- **Education / K-12 (Recess)**: searches returned only already-surfaced items (k12-teacher-skills, ASSISTments, GarethManning). Nothing new in window.
- **Fintech / lending (Meridia, Hypomone)**: only off-focus press in window (Longbridge equities skill, HoneyBook SMB CRM — logged). No new Plaid/CRA/lending-infra tooling.
- **Populi / SIS**: nothing new.
- **Postgres**: only neondatabase/postgres-skills, a companion repo to the Neon agent-skills already surfaced 07-29 — logged, not repeated.
