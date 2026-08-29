# Skills Scout — 2026-08-29

_Scan window: Aug 27–29 (last run 2026-08-28). SerpAPI: used (3/3 budget — 24h GitHub sweep, Google News, lane query). Sources per skills-scout-sources.md; deduped against seen-index. anthropics/skills and official marketplace checked via GitHub API._

## Official / Tier 1

1. **Claude Code v2.1.251** — Security-focused release: fixes a symlink-replacement vuln (unauthorized file access) and path-traversal in marketplace plugins **and the Workflow tool**; adds `PreModelSwitch`/`PostModelSwitch` hooks, a spend-limit bar + prompt-cache visibility in `/cost`, and fixes hourly prompt-cache misses in long-running sessions. Why it matters: you run scheduled/long-lived Cowork+Claude Code sessions and install third-party plugins — patch-now class, and the new hooks matter for any model-policy enforcement (Hypomone's Claude-primary policy). Trust: Tier 1 (official changelog; summarized via Qiita carrier — verify in changelog before relying on exact flag names).
2. **Official plugin marketplace adds (Aug 28): scandit-sdk + activecampaign** — Scandit's 86-skill SDK-integration plugin was *promoted from the community marketplace to official* (#5634); ActiveCampaign marketing-automation plugin added (#5641); Carta plugins bumped. Neither is on your stack, but the community→official promotion path is now demonstrably real — a GTM precedent for any future Plumbline/WayPoint plugin. Trust: Tier 1 registry; plugin code is third-party.
3. **anthropics/skills: quiet** — no commits since Aug 27.

## Claude/Cowork tooling & skill curation

4. **rebelytics/one-skill-to-rule-them-all ("task-observer")** — Meta-skill that watches your work sessions (autonomous or human-led), captures patterns/corrections/judgment calls, and turns them into skill improvements and new-skill candidates for review; ~2.1k★, active (pushed Aug 28), CC BY 4.0, Python. Why: directly serves your SKILL.md-authoring/curation lane and the os-architect extraction pattern; more mature than claude-skill-compounder (seen 08-25). Trust: Tier 3 — known project with real traction; review before letting it watch sensitive (FERPA) sessions.
5. **Nanako0129/sepia — traction promotion** — Logged to skipped 08-28 at 38★; ~550★/26 forks a day later. De-AI writing skill (StoryScope-based): narrative-architecture repair for fiction, venue-matched rules for professional prose. Why: fastest-moving skill of the week; relevant to voice/writing outputs across ventures. Trust: Tier 4 — unknown author, big-claim academic basis; read SKILL.md before install.
6. **mintlify/mintlify-claude-plugin** — Official Mintlify plugin for Claude Code *and Cowork* (docs authoring against Mintlify sites); first-party but tiny (7★), pushed Aug 27. Why: docs/product-spec tooling for Plumbline/Hypomone if you adopt Mintlify; complements mintlify/index (seen 08-08). Trust: Tier 2 — official vendor repo, low adoption so far.

## Meridia / Hypomone — fintech & lending data

7. **Bud Financial MCP server** *[backfill — launched ~Oct 2025, never surfaced]* — Banking-data-enrichment vendor exposing bank-grade transaction intelligence (categorization, income/affordability signals) to AI agents via MCP. Why: exactly the transaction-intelligence layer a membership-lending MVP would otherwise build; also extends the agentic-banking watchlist (Agentic Banking Directory 08-23, nCino 08-22, Plaid MCP 08-17). Trust: Tier 2 vendor press — commercial API, not hands-on evaluated; UK-origin vendor, check US data coverage.

## Lanes searched, nothing new

- **Recess / K-12**: only re-circulation of Claude for Teachers (seen); one ★1 study-skills repo logged to skipped.
- **Aegis / governance & audit**: nothing beyond systempromptio list (seen 08-26); Anthropic's automated-alignment-research post logged to skipped as research-not-tooling.
- **Populi / Postgres / SIS**: no new servers or skills; pgEdge/crystaldba/pg-aiguide all previously seen.
- **Grants/nonprofit**: no new programs; "Beneficial Deployments" page is the existing Anthropic team, not a new launch.
