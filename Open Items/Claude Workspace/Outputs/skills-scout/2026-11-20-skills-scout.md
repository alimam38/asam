# Skills Scout — 2026-11-20

_Window: Nov 19–20 (last ~24–36h). Sources: Tier 1 repos/changelog, GitHub search (Composio), web search, SerpAPI 3/3 (qdr:d GitHub, 24h Google News, 24h lending/education/governance MCP). Deduped against seen-index (671 lines) and skipped-log._

## Official / Tier 1

1. **Claude Code 2.1.329** — the trust dialog now says *where* a folder's hooks are declared; Claude Desktop warns when managed-settings hooks fail to load; `/tasks` now lists scheduled tasks, `/loop` wakeups, goals and forks (x stops one); `/mcp` shows a "Server message" row with the JSON-RPC error when a remote HTTP MCP server refuses; `/status` names marketplaces that get no auto-update; PDFs/images/.docx/.xlsx/.pptx sent by MCP servers as octet-stream no longer saved as `.bin`; Claude is now told when a connected MCP server's tools failed to load (instead of assuming zero tools); `claude mcp login` handles retired client registrations (410); `~/.claude.json` reset-to-defaults fix.
   - **Why it matters:** Cowork/Code + scheduled-tasks lane — `/tasks` visibility for routines like this scout; MCP refusal diagnostics and the octet-stream fix directly help Populi/Dropbox-style connectors returning documents (Plumbline, Talbot reports). Hook-origin warning is an Aegis-style governance pattern worth copying.
   - **Trust:** Anthropic-verified — [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) / [releases](https://github.com/anthropics/claude-code/releases).

_Official plugin/skills repos Nov 19–20: increments only (code-modernization, theme-examples, datadog bump) — logged to skipped._

## Plumbline — embedded analytics / semantic layer

2. **metabase/agent-skills** (vendor-official, MIT, ~60★; "Learn Metabase" skill v2 + marketplace links merged Nov 18–19) — Agent Skills for Metabase built for Claude Code; optionally uses your own data via the Metabase MCP server.
   - **Why it matters:** Metabase is a credible self-hosted dashboard layer over Postgres — a candidate (or benchmark) for Plumbline's executive-dashboard surface and for Meridia's integra-core Postgres on the NAS. Skills show how a BI vendor packages "teach the agent our semantic model."
   - **Trust:** Known directory/author (vendor-official, Tier 2) — [github.com/metabase/agent-skills](https://github.com/metabase/agent-skills).

## Skill authoring / curation (cross-lane)

3. **google/skills** (Google official, Apache-2.0, ~24k★; active Nov 18–19) — Google's Agent Skills repo, installable as a Claude Code plugin marketplace. New this window: `agent-platform-agent-registry` (Google Cloud Agent Registry), three Spanner Graph skills, four Cloud CI/CD skills, BigQuery migration exporter; and a `gemini-api` skill rewrite that cut its context footprint (272 lines) and fixed SDK bugs causing agent verification loops.
   - **Why it matters:** (a) skill-forge reference — a big vendor publicly trimming a skill's token footprint is a concrete authoring lesson; (b) Agent Registry skill = registry/approval pattern relevant to Aegis; (c) first time the repo itself is surfaced here (only an Aug press item on its oversight was logged).
   - **Trust:** Known directory/author (vendor-official, not Anthropic; Tier 2) — [github.com/google/skills](https://github.com/google/skills).

4. **aiwithremy/session-skill-audit** (created Nov 18, ~8★, **no license**) — a Claude skill that traces what actually caused each mistake in a session and fixes your skills, "deleting as often as adding."
   - **Why it matters:** fits Ali's skill curation loop (skill-forge, skill-distiller, ~70 installed skills) — a pruning-first audit is the missing half. Read for the method; don't install verbatim.
   - **Trust:** Unknown/community → install-with-caution (Tier 4; no license = reuse rights unclear) — [github.com/aiwithremy/session-skill-audit](https://github.com/aiwithremy/session-skill-audit).

## Meridia / Hypomone — lending & fintech MCP

5. **Lendflow expands SBA MCP connectors** (Nov 19–20) — Lendflow's MCP now carries SBA-specific lender profiles, credit criteria and processing instructions, expanded document management and new checkout requirements, usable from Claude/ChatGPT/Grok to move SBA applications forward.
   - **Why it matters:** reference design for how an embedded-lending platform exposes underwriting context through MCP — useful for Hypomone Gate 3+ (lending, **still parked behind §10 counsel review**) and Meridia's CDFI/SBA market reads. Read-only interest for now.
   - **Trust:** Known vendor blog (Tier 2) — [lendflow.com post](https://www.lendflow.com/post/expanded-sba-lending-capabilities-through-lendflows-ai-connectors).

6. **Built Technologies "November Release for Lenders": Built MCP + Draw Agent Overview** (~Nov 19) — brings construction loans into Copilot, Claude and ChatGPT, plus a new compliance report and faster title searches.
   - **Why it matters:** another lender-side MCP datapoint (after Blend Autopilot, Carrington, Omni-53) — the pattern of loan-servicing systems going MCP-native strengthens the Meridia thesis on AI-readable lending data. Details beyond the release snippet unverified (page is JS-rendered).
   - **Trust:** Vendor blog (Tier 2), snippet-level only — [getbuilt.com/blog/november-release-lenders](https://getbuilt.com/blog/november-release-lenders/).

## Lanes searched, nothing new
- **Recess / K-12:** no new Claude-for-Teachers or classroom MCP items in window (prior AFT/UFT + McGraw Hill already logged).
- **Populi / SIS-LMS, FERPA:** nothing.
- **Aegis governance:** only weak duplicates of the Bastion/SidClaw pattern (logged to skipped).
- **Postgres / NAS / Docker:** one 0★ read-only Postgres MCP (skipped; pgharbor remains the pick).
- **KSW (grants/music):** nothing.

## Ask
Ali: pick any to adopt — suggested: (2) evaluate Metabase as Plumbline/Meridia dashboard layer; (4) borrow the session-audit method into skill-forge.
