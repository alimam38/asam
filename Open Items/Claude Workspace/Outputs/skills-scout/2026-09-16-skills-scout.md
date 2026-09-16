# Skills Scout — 2026-09-16

Window: since the 09-15 run (~24–48h). SerpAPI 3/3 calls used (GitHub qdr:d, Google News, Reddit qdr:d). All items checked against the seen index.

## Official / Tier 1

- **Salesforce in Claude plugin (beta) — public launch.** The 37-skill sales plugin (accounts, opportunities, pipeline inside Claude) moved from pilot (seen 08-30) to public beta on 09-15. Why: the current best template for what Plumbline wants to be — a vertical system-of-record surfaced through Claude as plugin = skills + connectors + subagents; worth reading its structure before Plumbline GTM decisions. Trust: Tier 1 (Anthropic; Forbes/unite.ai coverage).
- **Claude for Small Business rebuilt — 43 workflows, 27 integrations** (Shopify, Salesforce, Stripe; "starter pack" sales push citing 900K plugin installs, 09-15). Directory confirms a restructure: new plugin added (#6145) and the old `small-business` plugin removed (#6151) the same day. Why: the QBO/month-end workflows overlap Talbot Hall finance ops (old version logged 06-22 for exactly this), and the packaging is another GTM reference for Plumbline. Trust: Tier 1 — anthropic.com/news/claude-for-small-business · Forbes 09-15.
- **Messages API: on-demand conversation compaction (beta, 09-14).** Developer-triggered summarize-while-preserving-recent-turns for long agent conversations. Why: directly useful for Hypomone/Aegis backend agents and any long-running loop you build on the API. Trust: Tier 1 (platform changelog).
- **Informatica plugin added to the official directory** (`informatica-for-claude-platform`, #6152, merged 09-16 02:15 UTC). Why: mild — enterprise data-integration/ETL vendor joining the wave; signal for Meridia's integra-core data-platform lane that data-infra vendors now ship official plugins. Trust: Tier 1 directory.
- **Housekeeping:** Claude Code 2.1.271–273 (fast mode for remote sessions; MCP disconnect/reliability fixes) plus a ~25-plugin version-bump wave in claude-plugins-official on 09-15 (Stripe, Netlify, Databricks, BigQuery, Carta, Sourcegraph, Sentry…). Churn only — nothing new to adopt. anthropics/skills: no commits since 09-13.

## Governance / audit patterns (Aegis)

- **AlchemyInCode/plumloom-autoeval-oss** (★27, created 09-14) — open-source CLI + MCP server for evaluating AI applications and *gating releases on reliability evidence*. Why: closest thing this window to Aegis's governance-not-guardrails pattern (evidence-backed approval before ship); also usable as an eval harness for Plumbline/Hypomone agents. Trust: Tier 4 unknown author — read before install.
- **renker-industries/custos** (created 09-16) — guardrail plugin that refuses to let a session end on a "done/correct/secure" claim unless an executed check backs it. Why: proof-based completion is the same audit-trail philosophy as Aegis PR #8's approval recording. Trust: Tier 4, day-one, ★0 — pattern worth reading even if never installed.
- **wtfsayo/agent-plugin-secret-guard** (created 09-16) — credential-leak prevention via PreToolUse/PostToolUse hooks; works across Claude Code, Codex, Cursor, Devin, opencode. Why: cheap hardening for a multi-agent fleet; hook-based governance pattern. Trust: Tier 4.
- **"Evidence Graph"** (r/ClaudeCode, 09-15/16) — OSS enforcement layer claiming every SKILL.md instruction "100% enforced, 20+ checks." Why: skill-compliance enforcement is an Aegis-adjacent gap (skills are advisory today). Trust: Tier 4, Reddit-sourced, repo not yet verified — treat as a lead. reddit.com/r/ClaudeCode/comments/1whqjzq

## Fintech / lending (Meridia · Hypomone)

- **"Claude Money" in preparation** (TestingCatalog, 09-14) — product assets pointing to an Anthropic personal-finance Claude offering. Why: an official consumer-finance surface would sit adjacent to Hypomone's member-facing money features and set precedent for financial-data handling in Claude — watch. Trust: Tier 2 press, pre-release, unconfirmed by Anthropic.
- **PCI Pal MCP server** [backfill, 09-10] — PCI-DSS-compliant payment capture exposed to AI agents via MCP. Why: agentic-payments infrastructure precedent for Hypomone member/lending flows; with Nymbus core-banking MCP (logged 09-09), the compliant-fintech-MCP wave is real. Trust: Tier 2 vendor press.

## Education / K-12 (Recess)

- **sugarforever/math-coach** (created 09-15) — agent skill that turns AI math help into actual tutoring: diagnoses what the learner already knows, teaches the theorem/notation behind every answer, adapts to the gap. Why: this is precisely Recess's math-gap-analysis / prerequisite-routing concept shipped as a skill — read its SKILL.md diagnosis flow. Author is a known AI-education content creator. Trust: Tier 3/4 known author, ★0 day-one.
- Otherwise quiet: no new Claude-in-education moves this window (Claude for Teachers items all previously surfaced).

## Cowork / Claude Code ops

- **nchuguevskiy/tattoo** (created 09-16) — plugin that snapshots the session before /compact and restores it verbatim after ("Claude forgets on every /compact"). Why: compaction context-loss is a live pain in long Cowork/Code sessions; pairs neatly with the new compaction API above. Trust: Tier 4, day-one.
- **GitLoomHQ/gitloom-plugins** (created 09-16) — long-term agent memory backed by a real git repository, packaged as a Claude Code/Codex plugin. Why: git-repo-as-memory is literally the asam-repo pattern this scout runs on — worth a skim for convergent design. Trust: Tier 4, day-one.

## Lanes searched, nothing new

- Populi/SIS, Postgres/NAS, grants, WayPoint/patents, KSW (grants + music/education): no relevant items this window.
- MCP registries: topic:mcp-server created-recent still poisoned by genpark spam (per 09-15 note); keyword search used instead — nothing above the bar beyond items logged.
