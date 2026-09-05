# Skills Scout — 2026-09-05

Scan window: Sep 3–5 (last ~48h), deduped against seen index through 2026-09-04. SerpAPI used (3/3 budget; the Google News call errored, degraded to built-in search for news). Quiet-ish day: no new adds to the official plugin marketplace (Sep 4 was a mass version-bump wave), no fresh K-12 or lending items. The real motion: Claude Code point releases and two standards/governance repos worth knowing.

## Official / Tier 1

1. **Claude Code v2.1.260–261 (Sep 3–4)** — v2.1.261 adds **`/skill-doctor`**: shows which loaded skills go unused and what they cost in context, so you can prune — a direct fit for your skill-curation lane (pairs with July's `/doctor` context audit). Also: `/diff` side panel showing uncommitted changes live as Claude edits (v260), likely prompt-cache-miss causes surfaced in `/cost`, `bashOutputMaxChars`/`taskOutputMaxChars` settings (up to 128K inline tool output), an "Organization policy" diagnostic line in `/status`, and `/reload-plugins` + text `/advisor` in headless/desktop sessions. Trust: Anthropic-verified (code.claude.com changelog).
2. **`ant apply` — agent infrastructure as code (ant CLI 1.30.0, Sep 3)** — manage Managed Agents, environments, skills, memory stores, and deployments declaratively, with lockfile support. Matters for the Aegis lane (governed, reproducible, auditable agent estates) and for pinning any future Plumbline/Hypomone agent setup as reviewable config rather than console clicks. Trust: Anthropic-verified (platform release notes via releasebot).
3. **frontend-design skill rewrite (anthropics/skills #1713, Sep 3)** — the official skill was updated specifically to avoid generic design defaults. Matters anywhere you generate UI: Plumbline dashboard mockups, Claude Design work (open item #5). Worth refreshing if you carry a copy. Trust: Anthropic-verified.

## MCP ecosystem / standards

4. **modelcontextprotocol/ext-skills — "Skills Over MCP" Working Group** — official MCP-org repo exploring skills discovery and distribution through MCP primitives (an MCP server advertising/serving skills, not just tools); active spec followups, pushed Sep 4, 211★. This is the standards home for the pattern Microsoft demoed in .NET (surfaced 08-03) and likely where skills-vs-tools packaging lands post the stateless spec. Watch-level, not install-level. Trust: MCP org / Linux Foundation (Tier 1/2).

## Aegis — governance / audit

5. **microsoft/agent-governance-toolkit** [backfilled — created Mar 2026, actively maintained, pushed Sep 4; 6.2k★] — policy enforcement, zero-trust agent identity, execution sandboxing, and reliability engineering for autonomous agents, with audit-and-compliance tutorials; claims coverage of all 10 OWASP Agentic Top 10 risks. Strong comparable for Aegis's governance-alert/approval architecture — worth a read for patterns even if you build your own. Trust: Microsoft official (Tier 2).

## Product / GTM (Plumbline · Hypomone)

6. **Daqi029/saas-onboarding-diagnosis** — agent skill for diagnosing SaaS onboarding, activation, "aha moment," and time-to-value (21★ in ~2 days). On-lane for Plumbline's tenant-onboarding design and any GTM gate review. Trust: unknown author — read before use, low blast radius (analysis-only skill) (Tier 4).

## Postgres / data (Meridia · Hypomone)

7. **greenstevester/archlens-postgres** — Claude Code skill that documents a PostgreSQL schema and reviews its design in one run (new Aug 31, ~0★). Cheap to try against the Hypomone event/ledger schema or integra-core before a design pass. Trust: unknown author, install-with-caution (Tier 4).

## Writing / comms

8. **dripips/plain-prose** — de-AI-patterns prose skill for EN/RU/DE that merges the stop-slop and avoid-ai-writing lineages and adds a zero-dependency checker; 66★ in ~2 days, the current leader of the de-AI-writing wave (follows sepia 08-29, humanizer-cli 08-02). Trust: unknown author, text-only skill (Tier 4).

## Lane checks — searched, nothing new

- **Recess / K-12**: nothing new past Claude for Teachers district Enterprise (seen 08-30); education sweeps only re-surfaced known items (canvas-mcp, k12-teacher-skills).
- **Meridia / Hypomone fintech-lending**: no new MCP/skills beyond seen (Blend, Plaid MCP early access, nCino, agentic-banking directory all previously surfaced).
- **Populi / SIS-LMS**: no new servers; brightspace-mcp (seen 09-04) remains the latest SIS pattern.
- **Official plugin marketplace**: no new plugins Sep 3–5 — only the nightly bump wave (cap raised 30→60/night, logged as increment).
