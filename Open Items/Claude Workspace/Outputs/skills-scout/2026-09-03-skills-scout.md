# Skills Scout — 2026-09-03

Window: since the 2026-09-01 run (Sep 1–3). Sources per skills-scout-sources.md; deduped against seen-index.md.

## Official / Tier 1

- **Claude Fable 5.1 + Claude Mythos 5.1 (Sep 1)** — new flagship models: 1M-token context, 128k max output, adaptive thinking; Developer Platform cuts cache-read pricing 75% (to $0.25/MTok) with new beta controls for tool use and system messages; press coverage claims up to ~45% lower agent running costs, plus an EU-AI-Act watermark **detection API in private preview**. Day-one GA on GitHub Copilot and AWS Bedrock. *Why it matters:* this re-prices every lane you run — scheduled tasks, Managed Agents, Plumbline/Hypomone build sessions — and the cache-read cut directly favors long-context agentic work; worth re-baselining model choices in your routines. Trust: Anthropic official + broad Tier-1/2 press (anthropic.com, venturebeat, the-decoder, AWS/GitHub blogs).
- **Claude Code v2.1.257–258 (Sep 1–2)** — Fable 5.1 becomes default model; `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` env var for consistent subagent models; containment escape rules for auto mode; one-time prompt before first file read outside working directories; 80+ stability fixes. v2.1.258 fixes **remote/scheduled session failures** ("user messages must have non-empty content") — directly relevant to your scheduled-task fleet. Trust: Tier 1 (code.claude.com changelog).
- **Commerce agent blueprint + Claude Code plugin (Sep 2)** — reference shopping and merchant agents with guardrails for retail/travel/telecom/ticketing platforms. *Why:* the guardrailed reference-agent pattern is a governance template (Aegis lane) and a GTM read on how Anthropic packages vertical agents (WayPoint-relevant); merchant-side agents brush the Hypomone/commerce-adjacent space. Trust: Tier 1 (Anthropic launch, via releasebot).
- **Enterprise Frontier Safeguards (Sep 1)** — zero-data-retention plus misuse-detection safeguards running in customer-controlled cloud infrastructure. *Why:* the compliance posture story for FERPA-adjacent work (Plumbline/Recess) and any future regulated-lending motion (Hypomone Gate 3). Trust: Tier 1.
- **claude-api skill refresh in anthropics/skills (#1704, Sep 1)** — updated for Fable 5.1/Mythos 5.1, Managed Agents self-hosted memory stores + web tool domain settings, and cost-optimize guidance. If you carry a mirror of this skill, refresh it. Trust: Tier 1.
- **Official plugin marketplace:** no new plugin adds this window — one metadata cleanup (newrelic/nvidia-skills entries, #5738) and ~46 routine version bumps (box, figma, databricks, carta, unity, etc.). Trust: Tier 1 repo observation.

## Claude / Cowork / skills ecosystem (Tier 2–4)

- **SpecterOps/skills** — a skills marketplace from SpecterOps (known offensive/defensive-security firm). Security-authored skills with a real org behind them; also a signal that security vendors now curate their own skill marketplaces. Lane: skill curation + Aegis/security. Trust: Tier 2/3 (known vendor; verify per-skill). github.com/SpecterOps/skills
- **Junhan2/oh-my-fable** (~35★ d1) — Fable 5.1 prompting guide packaged as Claude Code skills (KO/EN/ZH); claims quality gains on Opus/Sonnet 5 too. Timely companion to the 5.1 release for tuning your prompts/skills to the new default model. Lane: Claude Code/Cowork practice. Trust: Tier 4 — unknown author, install-with-caution. github.com/Junhan2/oh-my-fable
- **korya/askl** — deterministic linter for agent skills and plugins (Agent Skills spec, Claude Code, Codex compliance) as CLI + GitHub Action. Complements agnix (surfaced 08-27) with CI-friendly determinism; candidate for the asam repo's skill hygiene. Lane: SKILL.md authoring/curation. Trust: Tier 4, new + tiny. github.com/korya/askl
- **gozen3ji/consulting-pptx-skill** (~134★ in a day) — consulting-grade PPTX generation skill: slide conventions + 38-type SlideSpec + generation pipeline + machine checks. Japanese-language but the SlideSpec/machine-check architecture is directly reusable for Turner/board-deck work. Lane: docs/decks. Trust: Tier 4 (fast-rising, unverified; JP docs). github.com/gozen3ji/consulting-pptx-skill
- **atlassian/atlassian-mcp-server now ships a skills/ directory** — the official-vendor "MCP server + paired skills" pattern continues (Figma did this 08-28). Watch-pattern for Populi: this is the shape a populi-mcp + skills bundle should take. Trust: Tier 2 (official Atlassian).
- **Caution — "genpark-*" skill flood:** alphaparkinc mass-published ~60 templated skills in 3 days (uniform ~8★ each, incl. several "Anthropic Merchant" riders on the Sep 2 commerce launch). Same star-inflation shape as the 08-26 topic-spam caution; treat the publisher as low-trust. Trust: Tier 4 signal (GitHub sweep observation).

## Governance / audit (Aegis)

- **MCP context-injection transparency audit** — an audit of what MCP servers actually put into agent context found context injection across 19 servers, including at least one active prompt injection. Concrete ammunition for governed-MCP patterns (tool-output sandboxing, gateway policy checks) and for vetting connectors before install. Trust: Tier 4 (digitalapplied.com write-up, echoed by aigovernance.com — verify server list before citing). digitalapplied.com/blog/mcp-server-context-injection-transparency-audit
- **CVE-2026-84810 (claude-skill-antivirus)** — Rapid7 vulnerability entry for a community Claude skill that fails to analyze executable files. Notable less for the bug than the precedent: **community skills are now drawing CVEs** — skill supply-chain governance is formalizing. Trust: Tier 4 (Rapid7 DB entry; skill itself unvetted). rapid7.com/db/vulnerabilities/cve-2026-84810

## Meridia / Hypomone (fintech & data)

- **ondata/ckan-mcp-server** — MCP server for querying CKAN open-data portals (the platform behind many gov data portals). Complements the FRED/FDIC/HMDA/census loaders in integra-core with an agent-native path into public datasets. Trust: Tier 3/4 (ondata is a known Italian open-data collective; small repo). github.com/ondata/ckan-mcp-server
- Otherwise quiet: no new Plaid/lending-infra MCP motion this window beyond items already in the seen index.

## Recess / K-12
- Searched (news + GitHub): nothing new this window — the Claude for Teachers / free K-12 Enterprise wave was fully surfaced 07-14→08-30; new edu repos were region-specific (logged, not surfaced).

## Populi / Postgres / NAS
- Searched: nothing new this window beyond routine bumps; no new Postgres/SIS MCP entrants worth surfacing.

---
*SerpAPI used: 3/3 budgeted calls (24h-scoped Google ×2 + Google News). Seen-index checked; 16 true non-fits/increments logged to skipped-log.md.*
