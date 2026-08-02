# Skills Scout — 2026-08-02

_Weekend scan (window Jul 31 – Aug 2). SerpAPI: used, 3/3 calls (24h GitHub scope, Google News, Reddit/HN)._

**Official layer: quiet.** No Claude Code release since v2.1.219 (surfaced 07-26); whats-new still ends at Week 29; anthropics/claude-plugins-official shows only version bumps since Jul 30 (no new plugin adds); anthropics/skills has no new commits. All four items today are community-layer (Tier 4) — verify before install.

## 1. impeccable-lite — single-file design-judgment skill
- github.com/ilindaniel/impeccable-lite (created Aug 1; ~61★ day-one)
- One SKILL.md distilling Paul Bakaus's "Impeccable" design plugin — typography, color, layout, motion, accessibility judgment — with the commands/hooks machinery stripped out; install-path table for 16+ agent platforms.
- Why it matters: directly serves the Claude Design / UI-mockup focus (open item #5) and Plumbline dashboard UI; also the cleanest example yet of the "one-file skill" packaging pattern.
- Trust: Tier 4 (unknown packager), but the upstream author is known; small enough to audit the whole file before install.

## 2. Skill-Sentinel — behavioral (runtime) scanner for Claude skills
- github.com/handcraftedbygod/Skill-Sentinel (Jul 31; active pushes through Aug 2)
- Sandboxes and traces what a skill actually *does* (files, network, shell) instead of trusting its description — the trust lane's step from static scanning (malskanner 07-22, StepSecurity inventory 07-31) to dynamic analysis.
- Why it matters: you install a steady stream of Tier 3/4 skills; a behavioral second opinion is the missing piece of the curation pipeline.
- Trust: Tier 4, day-one, unvetted — audit the auditor first.

## 3. humanizer-cli — AI-text detection checks in the terminal
- github.com/0xwilliamortiz/humanizer-cli (Aug 1; ~141★/16 forks in a day)
- 33 heuristics for spotting AI-written text, with before/after examples and a draft checker; zero dependencies. Same author as ratchet (surfaced 08-01) — second big day-one repo in a week from this "measure the agent" author.
- Why it matters: a QA pass on GTM/donor/board copy before it ships; the author's measurement arc (rule-compliance → text tells) is worth tracking.
- Trust: Tier 4; day-one star velocity may be amplified — judge the checklist on its merits.

## 4. db-mcp — self-hosted read-only database gateway for agents
- github.com/mdadul/db-mcp (Aug 1)
- A self-hosted MCP gateway giving coding agents read-only access to your databases — a safety posture the gateway lane (MCPJungle 06-27, warden 07-31 skipped) hasn't centered.
- Why it matters: fits the Postgres/NAS/Docker stack and the Plumbline pattern — agents that can query but never mutate tenant data. Even if this repo doesn't mature, keep it as a design reference.
- Trust: Tier 4, day-one, ~1★ — pattern over pedigree today.

---
_Near-misses logged to skipped-log (7): verified-skills directory, evidence-to-skill, talivia analytics agent, dbt-governed AI analyst, skills-manager toggle, Anthropic agent-misuse disclosure (out of category), ASSISTments education connector (outside window)._
