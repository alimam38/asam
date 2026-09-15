# Skills Scout — 2026-09-15

_Scan window: 2026-09-13 → 09-15. SerpAPI recency layer used (3/3 calls: GitHub qdr:d, lane-scoped qdr:d, Google News). GitHub sweep via Composio. Deduped against seen-index through 2026-09-14._

## Official / Tier 1

- **Claude for Financial Advisors** — Anthropic launched (Sep 14) a Claude Cowork **plugin** bundling 8 advisor workflows (prospect intake, pre-meeting prep, post-meeting notes/follow-up, portfolio rebalance review, estate & tax brief, alternative-investments brief, advisor onboarding, **compliance & AI policy**) on top of a new partner-connector wave: Addepar, BlackRock Advisor Center (plugin surfaced yesterday — now clear why), Schwab, Envestnet (Tamarac/MoneyGuide), iCapital, Orion, SS&C Black Diamond, Wealthbox, Wealth.com, Vanguard, Zocks — plus existing M365/Salesforce/DocuSign/Box/FactSet/S&P/Morningstar. Enterprise-only, with audit logs pitched as the recordkeeping/compliance answer; license credit offer through Sep 30. Repo: `anthropics/claude-for-financial-advisors` (points at the `financial-services` marketplace). **Why it matters (Meridia/Hypomone + Plumbline):** this is the clearest template yet for your exact play — a regulated-vertical Cowork plugin whose value is workflows + governed connectors + audit trail. The skill list is worth reverse-engineering for Hypomone member/lending workflows, and "Enterprise + audit logs = compliance posture" is the pattern Plumbline can cite for FERPA-adjacent buyers. Trust: Anthropic-verified. — claude.com/blog/claude-for-financial-advisors · github.com/anthropics/claude-for-financial-advisors
- **Anthropic Threat Intelligence report, September 2026** [backfilled, Sep 10] — "Detecting and countering misuse of AI": state-linked espionage/weapons-research abuse cases, plus industrial-scale **distillation attacks** — Anthropic says seven China-based labs (incl. Moonshot, DeepSeek) secretly routed user requests through Claude to train their models. **Why it matters (Aegis / governance lane):** the report is a live catalog of agent-misuse and detection patterns (the flip side of governance-not-guardrails), and the distillation section is relevant context for any IP-sensitive corpus work (Meridia). Trust: Anthropic-verified; heavy press corroboration (Reuters, CNBC, Bloomberg). — anthropic.com/threat-intelligence-report-september-2026
- **Quiet-window notes:** No Claude or Claude Code release since v2.1.270 (Sep 12) — releasebot shows Sep 14's only entry is the Financial Advisors launch. `anthropics/skills` has no commits since Sep 13; both official plugin marketplaces show only routine version bumps this window (the one real add, BlackRock Advisor Center, was surfaced yesterday).

## Fintech / Meridia–Hypomone

- Covered by the Financial Advisors item above — nothing else genuinely new this window (Aave DeFi MCP and Futurum market-intel logged yesterday as off-lane; today's lending/CDFI sweep returned no new tooling).

## Education / Recess (K-12)

- Searched (web + GitHub sweep): **nothing new this window.** Only previously-logged items resurfaced (canvas-mcp, k12-teacher-skills, education-agent-skills). Two education-adjacent micro-skills went to the skipped log (studyos-builder, ocw-to-study).

## Governance / Aegis

- Threat report above is the item. Otherwise no new governance/audit tooling — this window's governance chatter (AAIF "MCP Is Growing Up") is spec-stewardship commentary, logged as an increment.

## MCP / dev tooling / Postgres / Populi

- **Nothing surfaced.** Postgres and Populi/SIS lanes turned up only known items. Ops note for the sources file: `topic:mcp-server created:<48h` on GitHub is now **~100% genpark twin-org spam** (307 results, all filtered) — the 09-03 caution has become total; created-recent topic sweeps for MCP servers are effectively dead until the flood clears.
