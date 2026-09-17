# Skills Scout — 2026-09-17

Window: 2026-09-15 → 09-17. SerpAPI used (3/3 budget: 24h GitHub sweep, Google News, education/lending week scan — third query returned empty). Deduped against seen-index (last digest 2026-09-16, which already covered Claude for Financial Advisors, Salesforce plugin, Small Business rebuild, API compaction, CC 2.1.271–273).

## Official / Tier 1

**1. Cowork is being folded into one unified Claude; Claude Docs + Claude Slides launched** — announced 09-16. Claude now decides per-task which capabilities to use inside normal chat; Docs = collaborative document creation/editing in-conversation; Slides = editable decks, presentable directly or exported PPTX/PDF; Claude Design stays standalone but its capabilities surface from chat too. Rollout: Pro/Max first (web/desktop/mobile, over coming weeks), Team/Free later; Enterprise gets 30+ days notice. Anthropic says chats, projects, artifacts, connectors and skills all carry over. Why it matters: the entire hub (MASTER.md boot, lane registry, scheduled tasks like this scout, Dropbox bridge) is Cowork-shaped — schedule a migration check that scheduled tasks, connectors, and the desktop folder bridge survive the merge; Slides' PPTX export is directly useful for Turner decks. Trust: Tier 1 announcement, multi-outlet corroborated (VentureBeat, Unite.AI, Pulse2).

**2. Intuit QuickBooks plugin added to the official directory** (`intuit-quickbooks`, #6189, 09-16). Why: Plumbline's spine is Populi + QBO + Gusto, and Turner month-end runs on QBO — evaluate against the Meridian QuickBooks connector already connected in the stack. Trust: Tier 1 directory listing; vendor plugin — check OAuth scopes before pointing it at live Turner books.

**3. Claude Code v2.1.274** (09-17): visible memory-critical warnings with recovery steps; MCP fixes (http+SSE 4xx connect, streamable-HTTP tool calls no longer time out at ~5 min, prompts/resources refresh on listChanged, 403s now name missing scopes); self-healing corrupted transcripts (no more endless tool_use_id retry loops); `/goal` survives compaction; VSCode continues steps after window reload; clearer code-review findings. Also new envs incl. `CLAUDE_CODE_MCP_STARTUP_WAIT_MS`. The MCP timeout/startup fixes matter for long connector calls in scheduled runs like this one. Trust: Tier 1 changelog.

**4. Regulated-finance plugin wave continues**: Zocks Advisor Intelligence (#6188, 09-16) and Chronograph GP + LP plugins (#6199, 09-17, private-equity fund analytics) landed right behind Claude for Financial Advisors. Why: Meridia/Hypomone lane — the pattern worth copying is regulated-finance workflows shipped as skills + connectors with audit logging; Chronograph's GP/LP split is a fund-reporting structure worth noting for Meridia IP work. Trust: Tier 1 listings; vendor plugins.

**5. GTM/product-analytics adds**: Clay (#6191), Leadfeeder (#6198), and a 5-plugin Pendo suite (#6190), all 09-16/17. GTM lane — relevant when Plumbline goes to market. Trust: Tier 1 listings.

## Fintech / Meridia–Hypomone
Nothing new beyond the Tier 1 items above. The "Claude Money" press wave (BleepingComputer 09-17, Android Authority — Claude analyzing bank/financial data, iOS launch prep) is an increment of the 09-16 seen item — logged, still unreleased.

## Dev tooling / agentic infra (community)
- **temporalio/skill-temporal-developer** — Temporal's own skill, packaged as a plugin for Claude Code (and other agents). Durable-execution workflow patterns; relevant if Hypomone's event/ledger spine or Aegis background jobs ever need durable orchestration. Trust: Tier 2 (vendor-official repo).
- **cytostack/openwolf** — portable project memory across Claude/Codex/OpenCode, reconciled from transcripts and session records. Agentic-context lane; overlaps GitLoom/agent-memory (already surfaced) — the differentiator is cross-agent reconciliation. Trust: Tier 4 — install-with-caution.
- **callstackincubator/agent-skills** — Callstack's (known React Native shop) skills collection: SKILL.md + references/ per skill, plugin manifests as install units. Clean authoring reference for skill-forge work. Trust: Tier 3 (known author).

## K-12 / Recess
Searched (FERPA / SIS / K-12 / tutoring / Populi terms, incl. a SerpAPI week-scoped query): nothing new in the window.

## Governance / Aegis
Nothing new beyond the already-surfaced Managed Agents auto-permission policies and Smart Reports; v2.1.274's clearer code-review findings is the only minor increment.

## Populi / Postgres / NAS
Populi: nothing. Postgres: pgEdge MCP Server GA (incl. pgEdge Cloud) is an increment of the 06-21 seen item — logged to the skipped log.
