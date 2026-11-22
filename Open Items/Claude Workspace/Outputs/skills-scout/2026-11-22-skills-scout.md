# Skills Scout — 2026-11-22

_Window: Nov 20–22, 2026. Deduped against the seen index (686 lines). SerpAPI: 3 of 3 calls used (1 Google News hit; two `qdr:d` site:github queries came back empty). GitHub search ran via Composio (repos created on or after Nov 20)._

**Quiet day.** Nothing new from Anthropic, and no new releases in the fintech or K-12 lanes. There are four small community finds below, all **Tier 4 (unknown author, install with caution)**.

## Official / Tier 1
- No new official items. Claude Code is still on **2.1.330** (surfaced 11-21). `claude-plugins-official` had one increment (theme-examples sound, #7191). `anthropics/skills`, `knowledge-work-plugins` and `claude-plugins-community` had no commits since Nov 21.

## Claude Code / skills / Claude Design lane
1. **Artesiana/bridge-anything** — an agent skill that builds a REST, MCP or CLI bridge to software that has no API (MIT, ★46, created Nov 20). *Why it matters:* Turner/Talbot back-office tools without an API (Plumbline overlay, Talbot ops) could get an MCP surface without hand-writing a server. It overlaps with computer use (surfaced 11-21) but gives a reusable bridge instead of a screen-driving session. *Trust:* Tier 4. Read the generated code before pointing it at anything with student or financial data. — github.com/Artesiana/bridge-anything
2. **pritamux/gridlines** — an agent skill for an "alignment pass": it draws guide lines down an interface and finds every element that misses its line (MIT, ★135 in ~1 day, created Nov 21). *Why it matters:* a cheap QA step for Claude Design and UI mockups (open item #5) and Plumbline dashboards. It pairs with diego3g/craft (11-16). *Trust:* Tier 4, but it gained traction quickly. — github.com/pritamux/gridlines
3. **VinVirtual/skill-ci** — a GitHub Action and CLI that check Claude Code skill repos: SKILL.md lint, secrets scan, script safety, media bloat (MIT, 0★, created Nov 22). *Why it matters:* it could run as CI on the asam repo's `.claude/skills/` and on skill-forge output. It complements skillaudit (11-21), which scans for injection, while this one checks hygiene. *Trust:* Tier 4 and brand new. Pin a commit before adopting. — github.com/VinVirtual/skill-ci

## Education / K-12 (Recess)
4. **ibl.ai PowerSchool SIS and Infinite Campus MCP server and agent skill** — connector pages for the two dominant K-12 SIS platforms, plus an MCP architecture guide for K-12. *Why it matters:* these are the SIS systems a district like Shadow Rock's likely runs, so this is the reference pattern if Recess ever reads SIS data. FERPA/COPPA review would be required. *Trust:* Tier 4 vendor pages, undated (first seen today). ibl.ai's higher-ed MCP guide was logged 06-22. — ibl.ai/developer/connectors/powerschool-sis · ibl.ai/developer/connectors/infinite-campus · ibl.ai/solutions/k-12/mcp-guide

## Lanes searched, nothing new in window
- **Fintech/lending (Meridia/Hypomone):** nothing new since Lendflow and Built (11-20). Older bank MCPs (Narmi/Grasshopper, Nymbus) are already in the index.
- **Governance/audit (Aegis):** only duplicates of the Bastion and SidClaw patterns (logged as skipped).
- **Populi / Postgres / NAS:** no new Populi tooling. Small Postgres/SQLite/CSV MCPs are logged as skipped.
- **Grants / KSW:** nothing.

## Ask
Pick any to adopt or trial: **bridge-anything** (Turner tools without APIs), **gridlines** (Claude Design QA), **skill-ci** (asam repo CI). The ibl.ai SIS connector is reference-only until the Recess pilot plan exists.
