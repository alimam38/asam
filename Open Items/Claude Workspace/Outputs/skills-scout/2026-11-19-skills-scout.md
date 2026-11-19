# Skills Scout — 2026-11-19

_Scan window: Nov 18–19 (plus one unseen Tier 1 backfill). SerpAPI used (3/3 calls: site:github 24h, Anthropic 24h, Google News MCP×lending/K-12/governance). Official repos checked via GitHub API (claude-plugins-official, skills, knowledge-work-plugins, financial-services)._

## Official / Tier 1

1. **Claude Code 2.1.328 (Nov 19)** — Tier 1 release. What matters for you:
   - `"onFailure": "block"` for `mcp_tool` hooks: a governance hook that errors now **fails closed** instead of letting the action through. **Aegis** lane: this is the fail-closed approval pattern you want for governance-alert gates.
   - `deniedMcpServers` entries (`claude.ai <name>`) now also apply in **cloud and self-hosted runner sessions** — one deny list covers scheduled cloud runs like this scout.
   - `/code-review` now reports only bugs + CLAUDE.md violations, tags each finding Important / Pre-existing / Nit, ends with a suggested fix; `/simplify` takes the cleanup role. Useful for **Aegis PR review** and Plumbline.
   - Fixes: saving a scheduled task could erase the project's other saved tasks if the tasks file was unreadable; a typo'd task got deleted on next save (**scheduled tasks** lane). Auto mode extended to Opus/Sonnet 4.6 on Bedrock/Vertex/Foundry; many Code Mode and self-hosted-runner improvements.
   - Trust: Anthropic-verified — https://code.claude.com/docs/en/changelog

2. **Claude-issued plugin auto-connect (beta, Team/Enterprise; Nov 3) [backfill — not previously surfaced]** — when an org member signs in, Claude can connect workplace plugins automatically if the plugin's MCP server trusts Claude as an issuer. 14 at launch: Amplitude, Apollo, Atlassian, Datadog, **Dropbox**, Figma, Granola, HubSpot, Linear, Mixpanel, **Notion**, PagerDuty, Semrush, **Supabase**. Why it matters: it's the admin side of the connector setup Ali does by hand, and a reference for how **Plumbline / Hypomone** MCP servers could later accept Claude-issued auth instead of a per-user OAuth flow. Plan-gated: Ali's org would need Team/Enterprise.
   - Trust: Anthropic-verified (support article) + press — https://support.claude.com/en/articles/15537633-auto-connect-your-organization-s-apps-to-claude · https://runtimewire.com/article/claude-auto-connects-workplace-plugins-enterprise-login

3. **Infobip Message — verified Claude connector (~Nov 17)** — sends SMS / RCS / MMS / Viber from Claude through one connector (there's also an Infobip Documentation connector). **Hypomone** lane: member notices (dues, application status, loan reminders) to misbanked operators who may not use email much. Before using it: consent/TCPA rules, and the member ledger should stay the record of what was sent.
   - Trust: Claude Marketplace listing (Anthropic-verified directory) + vendor press — https://claude.com/marketplace/connectors/infobip-message · https://martechedge.com/news/infobip-brings-global-messaging-capabilities-to-anthropics-claude-ai

## Hypomone / Meridia — Postgres & data

4. **DanielFreitasDev/pgharbor (created Nov 17, MIT, ★0)** — a Postgres MCP server, **read-only by default**, that **asks a human before touching production or making changes**, and doesn't treat a read-only transaction as enough protection. Supports PG 9.6–19, Python 3.11+. Why it matters: it fits the **Hypomone event/ledger Postgres on the NAS** and Meridia's integra-core — agents could explore the schema without write access to the ledger. Compare it with Postgres MCP Pro (seen 06-20) before adopting.
   - Trust: Tier 4, a new single-author repo with CI → install with caution, and read the code before pointing it at real data — https://github.com/DanielFreitasDev/pgharbor

## Aegis — governance / audit

5. **VishnuChivukula/bastion-agent-governance (created Nov 16, Apache-2.0, ★0)** — reference runtime governance plane: a policy-enforcing MCP gateway, **argument-bound human approvals**, a kill switch, a tamper-evident audit log, an exported evidence pack, and red-team eval suites; replay demo needs no API key. Why it matters: an **Aegis** pattern library, especially argument-bound approvals (the approval covers the exact arguments, not just the tool name) and the evidence pack. Pair it with today's fail-closed hook (item 1).
   - Trust: Tier 4, self-labelled "reference implementation; not production" → mine for patterns, don't deploy — https://github.com/VishnuChivukula/bastion-agent-governance

## Lanes searched, nothing new
- **Recess / K-12:** nothing new in the window (McGraw Hill × Claude for Teachers and the AFT/UFT terms were already seen).
- **Populi / SIS:** nothing.
- **Fintech MCP (lending/credit-union/CDFI):** nothing new in 24–48h (Blend/nCino/Nymbus/Omni-53 already seen).
- **Grants / KSW:** nothing.
- **Official plugin/skills repos:** only version bumps (see skipped log).

## Your call (single ask)
Pick any to adopt: **(1)** set `onFailure: block` on Aegis/governance MCP hooks · **(3)** trial Infobip for Hypomone member notices · **(4)** test pgharbor read-only against a NAS Postgres copy · **(5)** mine Bastion's argument-bound approvals for Aegis.
