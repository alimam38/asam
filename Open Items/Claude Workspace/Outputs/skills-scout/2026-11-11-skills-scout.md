# Skills Scout — 2026-11-11

_Window: Nov 10–11, 2026. Sources: claude.com / TechCrunch / Data Studios (Tier 1–2), GitHub search (repos created ≥ Nov 9), SerpAPI last-24h (3 calls). No new Claude Code release since 2.1.319 (seen 11-07)._

**Headline:** Anthropic shipped an office suite on Nov 10: Sheets, Whiteboards, Claude Data, Meetings, and interactive connectors. Several of these overlap tools you already run (Read.ai ledger sweep, hand-built dashboards, the Plumbline overlay), so they need a decision.

## Official / Tier 1

1. **Claude Sheets + Claude Whiteboards (beta) and Claude Data (GA, formerly Claude Dashboards)** — new artifact types, on every paid plan (Pro/Max/Ultra/Team/Enterprise). Sheets: multi-tab, editable, capped at 100k cells, no pivot tables or macros. Data: dashboards and visual analyses wired to connected sources. Team plans get it automatically; Enterprise admins enable it, and a **default changes on Nov 19**. Press reports Claude now routes chat, Cowork and artifacts inside one workspace.
   - *Why it matters:* **Plumbline** — Claude Data is a direct reference (or substitute) for the exec-dashboard layer; test it against Populi/QBO before you hand-build more. **Talbot/Turner finance** — Sheets could hold the receivables trackers. **Hypomone** — Whiteboards suit the Charter intake flow mapping. The 100k-cell cap and the lack of pivots matter for month-end.
   - *Trust:* Tier 1 ([claude.com article](https://claude.com/resources/articles/more-ways-to-work-with-claude-sheets-whiteboards-and-interactive-connectors)); plan and limit details from [Data Studios](https://www.datastudios.org/post/claude-sheets-whiteboards-beta-claude-data-generally-available-paid-plans) (Tier 2).

2. **Claude Meetings (beta: Team + Enterprise; Google Meet first)** — Claude joins the call, drafts the plan being discussed, maps timelines on a Whiteboard, answers questions in the meeting chat, and pulls figures from connected apps.
   - *Why it matters:* Overlaps your **readai-ledger-sweep / Turner Commitments Ledger** pipeline. Decide whether Meetings replaces or feeds Read.ai. **FERPA / consent**: Turner student matters and Shadow Rock (Recess) calls need a recording and consent policy before you turn it on. Not on Pro/Max yet.
   - *Trust:* Tier 1 announcement via [TechCrunch](https://techcrunch.com/2026/11/10/anthropic-launches-claude-meetings-to-turn-workplace-discussions-into-plans-and-tasks/) (Tier 2).

3. **Interactive connectors upgrade** — opens a connected tool's full UI inside Claude, beside the conversation (launch partners Adobe, Atlassian, Box). Anthropic cites 9,000+ MCP connectors.
   - *Why it matters:* This is the **MCP Apps / UI-in-chat** pattern. It's the most credible delivery surface for a **Plumbline** or **Aegis** approval UI, with no separate web app. Worth a spike before more front-end work.
   - *Trust:* Tier 1 ([@claudeai](https://x.com/claudeai/status/2120206375137484875), claude.com article above).

## Aegis — governance / approvals

4. **agentisend/agent-email-guard** — "blast-radius control" for agents that send email: budgets, a rate ceiling, loop detection, a kill switch and **approval holds** (Node/Python/PHP/Go). Created ~Nov 9.
   - *Why it matters:* A concrete, reusable control pattern for Aegis governance-alert approvals, and for any Turner/Talbot automation that emails residents.
   - *Trust:* Tier 4, new and low-star; read the code before adopting. [repo](https://github.com/agentisend/agent-email-guard)

## Meridia / NAS-Postgres

5. **timescale/memory-engine** — agentic memory on Postgres, run as an MCP server (10 tools to create, search and manage memories; all data stays in Postgres).
   - *Why it matters:* Fits the **Meridia** NAS/Postgres stack and the **Hypomone** event/ledger spine. A possible self-hosted memory layer for the corpus agents.
   - *Trust:* Tier 2 (Timescale/Tiger Data, same vendor as pg-aiguide, seen 07-02). [repo](https://github.com/timescale/memory-engine)

## Grants / nonprofit data (KSW, Turner development)

6. **vianido/ai** — MCP server plus skills over Vianido's public record of US nonprofits, for Claude and other MCP clients. Created Nov 4; first seen today.
   - *Why it matters:* A possible free complement to the Candid connector (paid tiers) for funder and peer research, e.g. the KSW PG-2 grant and Turner development work.
   - *Trust:* Tier 4; check data provenance against IRS BMF and 990 data. [repo](https://github.com/vianido/ai)

7. **Digital-Tax-LLC/990tax-mcp** — free IRS nonprofit lookup and **Form 990-N filing** over MCP. Created Nov 3.
   - *Why it matters:* Lookup is useful for grant research. Filing is a regulated action: treat it as read-only unless a human files.
   - *Trust:* Tier 4, install with caution; it touches IRS filings. [repo](https://github.com/Digital-Tax-LLC/990tax-mcp)

## Claude Code workflow

8. **TheDecipherist/claude-packs** — rules, checks, **hooks** and skills that hold Claude Code to what a senior engineer would accept, and stop repetition before it's written.
   - *Why it matters:* Follows the "CLAUDE.md is a request; hooks are enforced" note (11-08). A source of hook recipes for the asam repo.
   - *Trust:* Tier 4. [repo](https://github.com/TheDecipherist/claude-packs)

## Lanes searched with nothing new
- **Recess / K-12:** no new teacher/FERPA/COPPA skills or MCPs in the window (Portuguese course-brand skills logged as skipped).
- **Hypomone / lending:** no new items; Blend, Bud and Carrington were already surfaced.
- **Populi / SIS:** nothing new.
- **Claude Code releases:** still 2.1.319.

_SerpAPI: available (3/3 calls used, qdr:d)._
