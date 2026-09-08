# Skills Scout — 2026-09-08

_Window: ~24–48h since the 09-07 run. SerpAPI used (3/3 budget: 24h GitHub sweep, Google News, lane sweep). Anthropic had a quiet weekend: no releases Sep 6–7 beyond the bug-fix-only Claude Code v2.1.263 (already logged), and anthropics/skills, claude-plugins-official, and claude-plugins-community all show zero commits since Sep 6._

## Official / Tier 1

- **Anthropic "Beneficial Deployments" education site** — Anthropic stood up a dedicated site for its Beneficial Deployments initiative with education as a headline focus: free/discounted Claude + technical support for qualifying orgs; Claude for Teachers, a Teach For All "AI Literacy and Creator Collective" across 63 countries, AI-tutoring research (explicitly flagging cognitive-offloading/skill-erosion concerns), and higher-ed work (WGU, tutor-style learning mode). **Recess lane** — this is the program surface where Anthropic subsidizes education deployments; worth checking eligibility for Recess/Shadow Rock and even Turner. Trust: Tier 1 program (reported via edtechinnovationhub.com, Sep 1; verify details on anthropic.com before acting).
- **MCP docs: "Build with Agent Skills" page** — modelcontextprotocol.io now carries an official page routing MCP server development *through Agent Skills*: install the `mcp-server-dev` plugin (build-mcp-server / build-mcp-app / build-mcpb), let the skill interrogate your use case (what it connects to, who uses it, action-surface size, auth), then it scaffolds one of four deployment paths — remote Streamable HTTP (default), MCP apps (chat widgets), MCPB bundles (local server + runtime in one installable), or plain stdio. **mcp-builder/Populi lane** — this is the current official recipe for any populi-mcp-style build. Trust: Tier 1/2 (official MCP docs; plugin itself seen 07-13).

## Skill & MCP tooling (Claude / Cowork lane)

- **contentful/skill-kit** — TypeScript SDK for building agent skills as *typed state machines*: define steps, validate outputs, compile to self-contained executables. A serious counterpoint to markdown-only SKILL.md authoring — deterministic step control with schema-validated outputs. Official Contentful org repo with docs site; ★66, pushed yesterday (repo dates to Apr 2026 — backfill; surfaced now on a 24h SerpAPI hit). **skill-forge/authoring lane.** Trust: Tier 2 (known vendor org).
- **Graphify-Labs/graphify** [backfilled, Apr 2026] — `/graphify` skill for Claude Code/Cursor/Codex: turns a codebase *plus docs, SQL schemas, configs, and PDFs* into a queryable knowledge graph via local deterministic AST parsing. **Meridia corpus/RAG + dev lane** (schema-aware graph over integra-core-style repos is exactly the shape). Trust: Tier 3 — claims ★115k, star inflation unvetted (per the 08-26 caution); vet before install.
- **OthmanAdi/planning-with-files** [backfilled, Jan 2026] — persistent file-based planning for coding agents: crash-proof markdown plans, session recovery after /clear and compaction, per-turn re-grounding. Complements the OS-file/lane-memory pattern already in use. **Claude Code workflow lane.** Trust: Tier 3 — ★26.7k unvetted; concept is sound regardless of stars.
- **goolamabbas/portable-llm-council** — model-neutral skill that pressure-tests business/technical decisions with five AI perspectives, blind peer review, and a synthesized recommendation. Direct overlap with the council-v2 skill — worth a template-vetting pass for extractable structure (blind review step is the novel bit). ★3 day-one. Trust: Tier 4 (unknown author, tiny; read before running).

## Meridia / Hypomone (fintech & lending)

- **noskillish/bankmcp** — self-hosted, read-only MCP server for *your own* bank accounts via open banking (Enable Banking / PSD2). MIT, TypeScript, ★66 + 9 forks in ~day one, has a docs site. EU rails only, so not directly usable for US members — but as a **Hypomone pattern reference** it's clean: consent-scoped, read-only, self-hosted member-account access over MCP is precisely the membership-platform shape. Trust: Tier 4 (new solo author; treat as design reference, not an install).

## Aegis (governance / skill supply chain)

- **ibl.ai — "Shadow Agents: The Skill Supply Chain Nobody Reviews"** — new post (≤24h) from the education-AI vendor arguing for pre-deployment scanning of agent skills as a supply-chain control. Bridges two lanes: Aegis governance (joins the scanning wave — SkillSpector 07-28, Cisco skill-scanner 09-07, malskanner 07-22) and Recess (an education vendor making the FERPA-adjacent case). Trust: Tier 4 — headline/snippet verified only; body could not be fetched this run, so treat claims as unread.

## Lanes searched, nothing new

- Populi/SIS-LMS, Postgres/NAS/Docker, grants & nonprofit pricing, Plaid/CRA news: nothing new in window (Plaid hits all resolved to items seen 08-17 or older).
