# Skills Scout — 2026-08-27

_Scan window: last 1–2 days (since 2026-08-26 digest). SerpAPI recency layer used (3/3 calls). Lanes searched: Claude/Cowork/Claude Code, MCP, skills infra, K-12/Recess, fintech/Meridia/Hypomone, governance/Aegis, Populi/Postgres._

## Official / Tier 1

- **Unified memory across Claude chat + Cowork** (Aug 25) — Memory is now shared between claude.ai chat and Cowork sessions, with viewable/editable memory topics, an optional sensitive-topics setting, and opt-out. Why it matters: directly changes how your Cowork jobs and chat sessions carry context — worth reviewing what memory now holds across your lanes (FERPA/client caution: check the sensitive-topics setting). Trust: Anthropic-verified (Tier 1; via TechCrunch/Engadget/ZDNet + releasebot).
- **Cowork gets its own built-in browser** (Aug 26–27) — Cowork now runs an isolated browser inside the desktop app; the Chrome extension is no longer required, and it doesn't touch your tabs, bookmarks, or passwords. Why it matters: browser automation from Cowork without Chrome coupling — relevant to Populi/QBO web workflows the API doesn't cover. Distinct from the Aug-17 "Cowork in Chrome side panel" item. Trust: Anthropic-verified (Tier 1 origin; the-decoder/thenewstack/digitaltrends).
- **Claude in Chrome GA on all paid plans** (Aug 26) — autonomous browser actions with prompt-injection defenses and "verified actions" for reading/typing/clicking/forms. Why it matters: pairs with the above; the injection-defense framing is Aegis-relevant precedent for governed agent actions. Trust: Anthropic-verified (Tier 1; releasebot).
- **Salesforce puts its CRM inside Claude ("Claudeforce", expanded partnership)** (Aug 26) — Salesforce CRM operable entirely from Claude; Benioff framing it as the answer to the "SaaSpocalypse." Why it matters: the strongest signal yet for the vertical-SaaS-inside-Claude GTM pattern you're tracking for Plumbline (Populi-overlay-as-agent-surface). Trust: Tier 1/2 (VentureBeat/CNBC press on an official partnership).
- **Compliance API session endpoints out of beta + Admin API in `ant` CLI/SDKs** (Aug 26) — the Cowork/Claude Code session compliance endpoints (surfaced as Enterprise beta on 08-17) are now GA, and the Admin API landed in the official CLI and SDKs. Why it matters: audit-trail/governance surface for agent sessions — Aegis pattern material. Trust: Anthropic-verified (Tier 1; releasebot).

## Dev tooling / skills & plugin infrastructure (Plumbline, skill-curation domains)

- **microsoft/power-platform-skills** — Microsoft-official plugin marketplace for Claude Code + GitHub Copilot covering Power Platform dev (skills, agents, commands; 773★, pushed today). Why it matters: another top-tier vendor shipping a whole plugin *marketplace*, not just a skills repo — the vendor-marketplace pattern keeps compounding. Trust: Tier 2 (Microsoft official; distinct from microsoft/skills seen 08-17).
- **alibaba/open-code-review** — Alibaba-official hybrid code-review tool (deterministic pipelines + LLM agent, line-level comments, NPE/thread-safety/XSS/SQLi rulesets; Anthropic-compatible; 21.5k★). Why it matters: battle-tested review harness you could bolt onto Plumbline/Aegis CI; the deterministic-core + agent pattern echoes your governance thesis. Trust: Tier 2 (Alibaba official).
- **agent-sh/agnix** — linter + LSP for AI-agent config: validates CLAUDE.md, AGENTS.md, SKILL.md, hooks, and MCP configs, with IDE plugins (396★, active). Why it matters: first proper lint toolchain for the SKILL.md authoring lane; complements skill-doctor/SkillSpector already in your index. Trust: Tier 3 (known-author OSS; not new-born but newly surfaced).
- **netresearch/context7-skill** — Context7 documentation lookup as a lightweight REST-wrapper *skill*, explicitly avoiding MCP context overhead. Why it matters: you run Context7 as an MCP today; the skill-instead-of-MCP pattern cuts context cost — same thesis as your /doctor context audits. Trust: Tier 3 (netresearch, consistent skill publisher; 56★).
- **LinklyAI/best-skills** — daily-updated Top-100 agent-skills rankings (installs/growth/social buzz aggregated from skills.sh, ClawHub, GitHub, X; open CSV). Why it matters: could become a standing input to this scout — machine-readable cross-directory rankings. Trust: Tier 3/4 (new org, 60★ — verify methodology before trusting rankings).
- **akto-api-security/akto** — established API-security platform (1.5k★, since 2023) repositioned to secure AI agents, MCPs, and Agent Skills org-wide. Why it matters: the agent-skill supply-chain security category is consolidating into real products — Aegis-adjacent. Trust: Tier 2/3 (established OSS vendor; repositioning is marketing-led).
- **gviiisen/repo-context-ledger** — Agent Skill for cross-window context continuation and agent handoffs, storing verifiable feature notes/change records in Git (104★). Why it matters: agentic-context-setup lane; Git-as-ledger echoes your repo-as-memory pattern for scheduled jobs. Trust: Tier 4 (single author, bilingual docs — review before install).
- **s0xDk/refactoring-ui-skill** — the concrete design rules from *Refactoring UI* (spacing/type/color/shadow scales, hierarchy) as a Claude Code skill (122★ day one). Why it matters: direct fit for Plumbline dashboard UI polish and your Claude Design domain. Trust: Tier 4 (day-one repo; book-derivative content — IP posture unverified).
- **leopard627/fire-your-seo-agency** — self-serve SEO/AEO/GEO/LLMO audit-and-optimize skill ("fire your SEO agency"; 135★/41 forks day one). Why it matters: GTM lane — AI-search optimization for venture sites without an agency retainer. Trust: Tier 4 (day-one Korean-market repo, fast stars — treat star velocity skeptically per the 08-26 star-inflation caution).

## Meridia / Hypomone (fintech, corpus/RAG)

- **Dictation354/paper-fetch-skill** — DOI/URL/title in → structured agent-ready markdown full text out; ships as CLI + MCP + skill (239★). Why it matters: corpus-ingestion tooling for the AIA corpus/RAG pipeline. Trust: Tier 3/4 (traction but unknown author).
- **atukunare/wiki-knowledge-agent** — turns chat-pasted text/links into a verified, translated, searchable wiki KB with RAG retrieval, local-first (14★, day one). Why it matters: lightweight pattern for The Charter/corpus intake → queryable knowledge. Trust: Tier 4 (day-one, unverified).
- No new lending/CRA/Plaid-specific MCP items in the window beyond already-indexed nCino/ATTOM/Agentic Banking Directory; two unverified banking-MCP vendor pages logged to skipped.

## Recess / K-12 education

- Nothing new in the window — no fresh K-12/edtech skill or MCP items in the last 48h (Claude for Teachers coverage circulating is the July launch, already indexed 08-09).

## Aegis / governance & audit

- Covered above by Compliance API GA, Claude in Chrome verified-actions, akto, and alibaba/open-code-review's deterministic-core pattern; no additional standalone governance items in the window.

## Populi / Postgres / NAS

- Nothing new — neondatabase/postgres-skills and a Tiger MCP comparison piece both logged to skipped as increments of already-seen items.
