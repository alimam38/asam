# Skills Scout — 2026-08-22

Window: Aug 21–22 (since yesterday's scout). SerpAPI used (3/3 calls: 24h claude-tooling sweep — empty return, Google News Anthropic, week-scoped lane query). Sources per skills-scout-sources.md; GitHub sweep via Composio repo search (created:>2026-08-20).

## Official / Tier 1

- **Claude Mythos 5 opened to defenders — Claude Security expansion + $35M Defender Advantage Fund** (Aug 21). Anthropic is putting its frontier security model behind Claude Security, partner integrations (Palo Alto Unit 42 announced same day), and a fund for open-source security patching. Why it matters: the security lane you inherit (skill/plugin scanning, vuln patching) just got a dedicated frontier model + money behind it — raises the bar for what "scanned" means for anything you install, and is the strongest Aegis-adjacent signal this week. Trust: Anthropic-verified (via releasebot/marktechpost/Palo Alto blog).
- **Computer use GA on the Claude Platform — multi-action turns + browser use** (Aug 20, part of the "build production agents" wave with Skills API + Files API GA surfaced yesterday). Computer use graduating from preview to GA with browser control matters for Plumbline/Populi work where no API exists for a workflow — an agent can now drive the web UI as a supported, GA capability. Trust: Anthropic-verified.
- **Claude Code v2.1.238** (Aug 21): new prompt settings, **hardened MCP and plugin security**, more reliable Remote Control messaging, long-session memory-leak fixes. The MCP/plugin security hardening continues the Aug 8 Enterprise-scanning thread — worth a changelog read before your next plugin install. Trust: Anthropic-verified (changelog via releasebot).
- **claude-api skill: Python SDK 0.x → 1.x upgrade guide** (anthropics/skills #1623, Aug 21). New `upgrade` subcommand that walks a project from anthropic-python 0.x to 1.x (httpx2 layer, Python 3.10 floor, removed deprecations). Why it matters: confirms SDK 1.x is the current target — Hypomone/Aegis backend code calling the API should migrate with this skill rather than by hand. Trust: Anthropic-verified.
- **eli5 plugin landed in anthropics/claude-plugins-community** (Aug 21, authored by Anthropic's Thariq Shihipar): plain-language explanations rendered as HTML artifacts. Small, but note the pattern echo below — and a possible Recess classroom-explainer primitive. Trust: Tier 1 marketplace infra, community plugin.

## Meridia / Hypomone — fintech & lending data

- **nCino Mortgage MCP** (Aug 7, caught late). The banking-platform vendor shipped an MCP server so AI agents can work inside mortgage-lending workflows on nCino. Why it matters: the clearest "lender-platform-ships-MCP" precedent yet for Hypomone's lending step 2/3 — same pattern as Blend Autopilot (seen 08-04) but from the dominant community-bank/CU core-adjacent vendor. Trust: known fintech press (fintech.global); verify against nCino's own docs before relying.
- **ATTOM property-data MCP server + specialized agents** (~Aug 18, HousingWire). Property/real-estate data giant exposes its data platform to agents via MCP. Why it matters: property-level data joins the FRED/FDIC/HMDA stack for Meridia's CRA/community-lending analytics — worth a look at coverage/pricing. Trust: Tier 2 press; vendor claims unverified.
- **Consensus official MCP server** (Consensus-NLP/consensus-mcp, new Aug 21, 16★). Search 220M+ peer-reviewed papers from Claude/any MCP client. Why it matters: evidence retrieval for the AIA corpus and for Recess education-research grounding, from the vendor itself. Trust: official vendor repo (Tier 2); new repo, low stars — sane to pin/review before daily use.
- **Revio Insight MCP** ("your bank's AI agent, everywhere"). Bank-facing MCP product page surfaced in this week's lane sweep. Logged here rather than trusted: marketing page, no public repo found. Trust: unknown vendor (Tier 4) — install-with-caution, verify before any contact with real data.

## Aegis — governance & approval patterns

- **Cairn** (Nouman-Amjad/Cairn, new Aug 21, 5★). Agentic incident-analysis copilot built around MCP tool servers, a cost-aware model router, and an **approval-gated write path**. Why it matters: independent implementation of exactly the governance-alert-approvals pattern Aegis uses — worth skimming the approval-gate design even if you never run it. Trust: unknown author, day-one repo (Tier 4) — read, don't install.

## Cross-cutting community

- **Plain-language output wave**: Leutenegger/claudish-to-english (Claude Code plugin rewriting assistant messages into plain language on screen only, local-model default, fail-open — **579★ day one**, known author from book-to-skill 08-17) and adnanakil/nobuzz (/debuzz skill, 144★). Together with Anthropic's own eli5 the same day, "de-jargon the agent" is suddenly a lane. Why it matters: readable-output patterns transfer directly to Plumbline exec dashboards and Recess teacher/parent-facing text. Trust: Tier 3 known-author / Tier 4 — claudish-to-english proxies output through another model; review before use on sensitive content.

## Lanes searched, nothing new

- **Recess / K-12**: no new education skills/MCP items this window (Claude for Teachers press continues to recycle; already covered).
- **Populi / Postgres**: no new servers; pgEdge Postgres MCP hit GA incl. pgEdge Cloud — increment of the 06-21 item, details in skipped log.

## Skipped (logged with reasons)

Version churn (Claude Security v0.10.2), Academy increments (blog + academy-coach plugin), pgEdge GA, Plaid model/press increments, Salesforce agent-skills page, Anthropic IPO + watermark press waves, book-to-skill and memory-lane increments, genpark spam continuation, and the daily repo-churn roll-up — all in skipped-log.md.
