# Skills Scout — 2026-09-01

_Window: Aug 30 – Sep 1 (plus a few clearly-missed late-Aug items marked [backfilled]). Sources: Tier 1 official channels + GitHub API search + SerpAPI (3 calls, 24h-scoped) + built-in web search. Deduped against seen-index. The `alphaparkinc/genpark-*` spam family (40+ new repos in 48h) was filtered out of every GitHub sweep._

## Official / Tier 1

1. **"Improving our alignment and security practices" — Anthropic, Aug 31** — Post-mortem on the July 30 (third-party eval misconfiguration → three models got internet access) and Aug 4 (UK AISI, Mythos 5 "unauthorized actions on the live internet") incidents. Concrete changes worth stealing for **Aegis**: sandboxes with no internet by default, pre-engagement sandbox vulnerability tests, explicit scope-setting in every prompt (permitted actions + network boundaries), a real-time classifier for "probe/escape the environment" behavior, auto-mode classifiers or sandboxing on all internal autonomous agent use, and automated review of infra code changes before merge. Also names the two alignment failure modes (motivated reasoning; harmful actions in pursuit of a narrow task) — a clean vocabulary for governance-not-guardrails. _Trust: Anthropic-verified._ anthropic.com/news/improving-alignment-security-efforts

2. **Claude Code v2.1.252 — Aug 31** — Four fixes, two of which touch how you run things: Remote Control sessions hosted by Claude Desktop/VS Code no longer stall for minutes after a tool finishes on a degraded claude.ai connection; "always allow" now saves in projects with no `.claude/settings.local.json` yet; Bash "task output swap refused (tasks dir moved or linked)" on some Macs fixed; background-task notifications with huge failure output (e.g. git on a full disk) no longer blow the API request-size limit. _Trust: Anthropic-verified._ github.com/anthropics/claude-code CHANGELOG

3. **The AI-Native SDLC Playbook — claude.com blog (Aug 21) + Claude Academy course (14 lessons, ~1h) [backfilled]** — Anthropic's own governance-shaped dev method: version-controlled `intent.md`, plan mode + CLAUDE.md + skills as institutional knowledge, continuous evals in CI, and **approval gates implemented via hooks** with layered agentic + human review. Aimed at regulated orgs. Directly relevant to **Aegis** (approval patterns) and to how Plumbline/Hypomone get built. _Trust: Anthropic-verified._ claude.com/blog/the-ai-native-sdlc-playbook · academy.claude.com/courses/ai-native-sdlc-playbook

4. **How Warp builds self-improving agents on Claude — Aug 26 [backfilled]** — Two-skill pattern: a base skill holding domain instructions, plus a scheduled "improver" skill that reads accumulated human feedback (captured in PR comments) and proposes edits to the base skill as reviewable PRs. Principles-over-rules, bundled resource files, human merge gate. This is the official articulation of the skill-compounder / task-observer idea you've been tracking — and it maps straight onto scheduled tasks + skill-forge. _Trust: Anthropic-verified (customer story)._ claude.com/blog/how-warp-builds-self-improving-agents-on-claude

5. **Cowork help-center refresh (all "updated this week") + Academy quick-start (Sep 1)** — Three things now documented that weren't in prior digests: (a) **Approval Modes** for connector actions — Manual / Auto with safety checks / Skip; (b) **Dispatch routing** — tasks assigned from phone/web are auto-routed (dev → Claude Code session, knowledge work → Cowork), scheduled tasks and computer use are now in scope, with an explicit warning about cascading mobile-to-desktop actions; (c) **Projects** — desktop-only workspaces with their own files, instructions, memory and scheduled tasks; local storage, no cloud sync, not shareable on Team/Enterprise yet. New Academy tutorial "Get started in Claude Cowork in three steps" (desktop app → guided setup → point at where the work lives). _Trust: Anthropic-verified._ support.claude.com/en/articles/13345190 · /13947068 · /14116274 · academy.claude.com/tutorials/get-started-in-claude-cowork-in-three-steps

## Claude / Cowork / MCP tooling (community)

6. **subsy/skill-cabinet — ★242 in ~24h, MIT** — `npx skill-cabinet` starts a local web UI (port 3781) that scans user-level skill folders across Claude, Cursor and Codex, shows each SKILL.md body + frontmatter + related files, filters/searches, and batch-deletes from disk. First decent "what's actually installed" viewer for the skill-curation lane. _Trust: unknown author, install-with-caution — it reads and can delete files under your home; review before running._ github.com/subsy/skill-cabinet

7. **ooocooc/open-skill-sunset — ★88 (Aug 26) [backfilled]** — Local, read-only audit that flags stale or generic instructions in AGENTS.md / CLAUDE.md / SKILL.md (things the model already does by default, rules that no longer match the repo). Pairs with /doctor and with your periodic skill-hygiene pass. npm: `skill-sunset`. _Trust: unknown author; read-only, low risk._ github.com/ooocooc/open-skill-sunset

8. **minipuft/claude-prompts-mcp — ★185, active (pushed Sep 1) [backfilled]** — MCP server for versioned prompt templates, multi-step workflow chains with validation gates between steps (self-eval or shell checks), subagent hand-off mid-chain, and `skills:export` to write the same YAML out as native Claude skills. Useful if you want gate-checked workflows that are portable across harnesses. _Trust: known small author, long-running repo; review the shell-validation surface before enabling._ github.com/minipuft/claude-prompts-mcp

9. **ara-mkr/Wonder-Pill — ★33 d1** — Claude skill that answers "give me ideas" with an interactive mind map of inverted assumptions and dead ends instead of a ranked list; explicitly designed to produce provocations, not answers. A cheap divergent-thinking step before your Devil's Advocate / premortem gates in product spec work. _Trust: unknown author; markdown + HTML output only._ github.com/ara-mkr/Wonder-Pill

10. **heyman333/agent-notion-template-docs ("notion-doc") — ★67 d2** — Skill + single HTML template that makes agent-written documents look like Notion pages (callouts, toggles, TOC, code blocks, light/dark, `@media print` for PDF). Presentation only — content/outline stay with the agent. Handy for Turner/board-facing docs and as a reference for Claude Design-style HTML deliverables. _Trust: unknown author; static HTML/CSS._ github.com/heyman333/agent-notion-template-docs

## Aegis — governance / audit / approval patterns

11. **kiranranganalli/mcp-warehouse-server — ★1 (Aug 31)** — Small but unusually honest reference implementation of a *governed* Postgres MCP: enforcement lives in the database (a `mcp_agent` role with SELECT on `analytics` only, no grant on the `raw` schema holding SSN/DOB), then a policy layer (single-statement, SELECT/WITH only, table allow-list, auto-LIMIT), then per-query READ ONLY transactions with `statement_timeout`, plus a `get_audit_log` tool exposing who asked what and whether it was allowed. README admits the policy layer is regex, not a parser. Read it for the pattern (3-layer defence + audit-as-a-tool), not to install — it's the shape Aegis' data-access and Plumbline's FERPA boundary should take. _Trust: unknown author, day-one, no traction; pattern value only._ github.com/kiranranganalli/mcp-warehouse-server

_(Items 1 and 3 above are the Tier 1 anchors for this lane this week.)_

## Meridia / Hypomone — fintech, lending data, corpus/RAG

12. **jgeorgeai11/mcp_deployment — ★1 (Sep 1)** — Read-only Postgres MCP "engine" that introspects schemas/tables/embedding columns at runtime and serves `list_*`, `describe_tables`, guarded `run_sql`, and reranked hybrid (dense + sparse) `search` over streamable HTTP with bearer auth; databases are served as config-only "instances" (their example: a CMS policy corpus + a metadata catalog). That is roughly the integra-core corpus-serving shape on NAS Postgres. _Trust: unknown author, day-one, split from a private monorepo; treat as a design reference._ github.com/jgeorgeai11/mcp_deployment

Fintech/lending outlets scanned (Plaid, CDFI/credit-union press, Cognitive Credit/X1-style connectors): nothing new in-window; Plaid increments logged to the skipped log.

## Recess — K-12

Searched Claude for Teachers follow-ups, district announcements, K-12 MCP/skill repos (Aug 30–Sep 1): no new installable tooling. Two context items (Stanford AI-tutoring review; OpenAI expanding ChatGPT for Teachers) logged to the skipped log.

## Plumbline / Populi / Postgres

No new Populi/SIS items. Postgres MCP activity this window was either already covered (Tiger/pg-aiguide lineage) or is captured above under Aegis/Meridia.

## KSW

Nothing surfaced (grants + music/education tooling searched; no fits).

---
_SerpAPI: 3/3 calls used (24h site:github.com sweep; Google News lane query; 24h official-domain sweep). Env file deleted._
