# Skills Scout — 2026-08-25

_Method note: SerpAPI available (3/3 calls used: GitHub last-24h sweep, Google News, weekly lane sweep). Deduped against seen index through 2026-08-24. Quiet day at Tier 1: no Anthropic release-notes entries for Aug 23–25, no commits to anthropics/skills since Aug 22, and Claude Code's latest remains v2.1.239 (surfaced 08-23)._

## Official / Tier 1

- **NetSuite plugin refresh — netsuite-ai-companion + netsuite-finance-analyst** (anthropics/claude-plugins-official #5600, Aug 25). netsuite-suitecloud repointed to a new home, plus two new plugins: an end-user AI companion and a **finance-analyst** agent. Why it matters (Plumbline): a first-party ERP "finance analyst" plugin is the closest official analogue yet to the Populi+QBO+Gusto executive-overlay Plumbline is building — worth skimming its skill structure for finance-analysis patterns (month-end, variance narration, report framing). Trust: Anthropic-verified marketplace; Oracle/NetSuite-authored.
- **Unity official plugin** (#5595, Aug 24) — Unity Technologies partner listing added to the official marketplace. Off the direct stack, but the vendor-ships-a-Claude-plugin GTM wave continues (Adobe 07-26, PayPal/Shippo 07-28, Carta 07-30, GitKraken 07-31) — the pattern itself stays relevant to WayPoint/product GTM thinking. A **qodo** entry also picked up author metadata (#5598); not verified as newly added today. Trust: Anthropic-verified marketplace; vendor-authored.

## Claude / Cowork / skills-ops

- **ContextLab/claude-skill-compounder** — a hook that continually prompts Claude to spin session insights and discoveries off into new skills (automated skill extraction). Direct hit on the SKILL.md-authoring/curation lane: this is the "extraction pass" (sessions → durable skills) turned into an always-on mechanism. Day-one, tiny (★1). Trust: Tier 4 install-with-caution — ContextLab is a known academic lab (Dartmouth), but read the hook before enabling; it runs every turn and adds context cost.
- **Vishal-Kundar/spawn-guard** — Claude Code skill + PreToolUse hook that hard-blocks subagents spawning with the wrong model, effort, or output style. Small (★2 day-one) but on-lane for **Aegis**: enforcement-not-suggestion governance applied to agent fleets — the same "governed spawn/approval" pattern Aegis expresses at app level, here as a 50-line hook. Trust: Tier 4 — treat as a pattern to copy more than a dependency.

## Education / K-12 (Recess)

Searched (FERPA/K-12/tutoring MCP + edu press): nothing new — results were all previously surfaced items (k12-teacher-skills 08-09, Claude Academy 08-18, DeepTutor 08-18, canvas-mcp 06-26).

## Fintech / lending (Meridia / Hypomone)

Nothing new — lending-MCP results (Blend Autopilot, nCino Mortgage, Plaid MCP, agentic-banking directory) are all already in the seen index (08-04 → 08-23). The NetSuite finance-analyst plugin above is the day's most relevant finance item.

## Governance / audit (Aegis)

spawn-guard (above). The Aug 25 "Anthropic enterprise-managed MCP auth" security-press wave (CyberSecurityNews et al.) is a recycle of the June 18 MCP Enterprise-Managed Authorization spec extension (Okta XAA / ID-JAG) surfaced 06-20 — logged, not resurfaced.

## Populi / SIS · Postgres / NAS

Nothing new this run.
