# Skills Scout — 2026-08-20

Daily scan, window Aug 18–20. SerpAPI used (2 of 3 budget: 24h GitHub sweep + Google News). Quiet day: zero new commits in anthropics/skills, marketplace version-churn only, no Claude Code release after v2.1.235. Two items surfaced.

## Official / Tier 1

- **Gmail connector gains write actions — send, reply, forward (Aug 18; press wave Aug 19).** Claude's Gmail connector moves beyond read-only: on paid plans it can now send, reply to, and forward email. Default is per-action approval; users can opt into send-without-confirmation, and Team/Enterprise owners control whether members may do so. Why it matters: you use the Gmail connector daily — check your approval settings before unattended runs — and this is the approval-gating/governed-writes pattern Aegis studies, shipping as a production default (scoped writes + human gate + admin policy). Trust: Tier 1 origin (Anthropic support docs), relayed via 9to5Google/PCMag/Mashable — https://9to5google.com/2026/08/18/claude-can-now-send-emails-in-gmail-even-without-your-approval/

## Skills & agent-craft (Claude Code / Cowork lane)

- **Spielewoy/autoprompt-skill (~404★ in 3 days).** Coding-agent skill claiming a 45% cut in failures on agentic coding tasks by tightening the prompt/plan before execution; fastest-traction new skill this week. Why it matters: SKILL.md-craft/curation lane — if the method holds up it's a candidate pattern for Plumbline/Hypomone build sessions. Trust: Tier 3/4 community repo; benchmark claim unverified — read the method before installing. https://github.com/Spielewoy/autoprompt-skill

## Lane checks — searched, nothing new to surface

- **Recess / K-12:** only recycled Claude-for-Teachers press (seen 08-09); no new edtech skills/MCP servers.
- **Meridia / Hypomone (fintech/lending):** Plaid's August product-update press is an increment of the Plaid MCP early-access item (seen 08-17); nothing new on Blend/CRA/CDFI angles.
- **Populi / SIS + Postgres:** nothing new (evergreen Postgres-MCP content only).
- **Aegis (governance/audit):** no new tooling beyond the Gmail approval-gating item above; kubernetes-sigs MCP lifecycle operator logged as off-stack.
- **Anthropic repos:** anthropics/skills — no commits since Aug 19; claude-plugins-official — ~30 version bumps Aug 19, no new vendors (first-seen names carbone-skill / duende-skills are pre-existing plugins).
- **KSW (grants/music-ed):** nothing new.
