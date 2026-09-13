# Skills Scout — 2026-09-13

Window: since the 2026-09-12 digest (~24–36h). SerpAPI: used (3/3 budget — GitHub qdr:d, lanes qdr:d, Google News). Layers: SerpAPI + built-in web search + GitHub API (topic searches created:>2026-09-10; commit logs on anthropics/skills and claude-plugins-official).

## Official / Tier 1

- **Claude Code v2.1.270** (Sep 12) — single-fix release: read-only git commands in Bash no longer trigger unexpected permission prompts after extended sessions. No action needed; v2.1.268–269 (plugin evals etc.) were covered yesterday. _Trust: Tier 1 (via releasebot mirror of official changelog)._
- **Quiet window at Anthropic's repos** — checked directly via GitHub API: no new commits to `anthropics/skills` since the 09-11 refresh, and `claude-plugins-official` shows only routine version bumps (workos, mongodb, huggingface-skills, resend, unreal-engine, ~30 more on Sep 11) — **no new marketplace adds** in window. _Trust: Tier 1, observed directly._

## Ops / watch

- **Windows 11 September update breaks WSL → breaks Claude Cowork on Windows** (Sep 12) — XDA and Windows Latest report the September cumulative update breaks WSL, taking Cowork's Windows local mode down with it; Microsoft has acknowledged the update is breaking multiple features. If any machine in your fleet runs Cowork on Windows, hold/defer the September update until patched. _Trust: Tier 2 press; not independently verified._

## Skill ecosystem — curation & supply chain (Cowork / skill-forge lane)

- **aiskillstore/marketplace** — new skills marketplace whose pitch is that **every submission is automatically security-scanned before listing** (Agent Skills spec compliance + license required). Continues the supply-chain formalization thread (Cisco skill-scanner, NVIDIA-Verified Skills, malskanner). Same window also surfaced **skills.pub**, another new marketplace/index. _Trust: Tier 3/4 — new orgs, scanning depth unproven; verify before installing anything from either._
- **agenticskills.io "methodology" page** — directory positioning itself as a neutral auditor: install-independent skill-quality metrics (explicitly noting they *can't* see installs, unlike Anthropic) plus an **MCP audit framework with results published on every server page**. Useful comparison point for your own curation/template-vetting practice. _Trust: Tier 4 — unverified project; treat the audits as claims._

## Dev tooling — NAS / Docker / Postgres lane

- **netresearch/docker-development-skill** — Agent Skill for Docker image development: Dockerfile best practices, CI testing, compose orchestration. Repeat known author (netresearch: git-workflow-skill, context7-skill, skill-repo-skill). Direct fit for the Synology/Docker/Postgres ops behind Meridia/Hypomone. _Trust: Tier 3 — known community author, read before adopting._

## Governance & legal-ops (Aegis pattern-watch / Turner institutional ops)

- **kevanwee legal-automation suite** (4 repos, Sep 11–12, one author): **citecheck** (audit every legal citation in a draft — deterministic extraction, prove the authority exists, then verify it supports the proposition), **chronology** (litigation chronologies as data: mandatory pincites, provenance-preserving merges, date-conflict detection), **oblig-register** (executed contract → dated obligations register with validated schema, deadline traces, .ics export), **playbook-as-code** (contract-negotiation playbooks as an open schema + clause locator + redline changeset + Claude review skill). Why it matters: the *deterministic-verification + provenance* pattern is exactly the Aegis governance/audit doctrine applied to legal text, and oblig-register is plausibly usable as-is for Turner contract/covenant tracking. _Trust: Tier 4 — day-one repos, single author, ~1★ each; read code before use._

## Design (Claude Design / frontend lane)

- **systemonster/slop-check** — a 12-question "ship gate" for catching AI-generated design slop before shipping, distilled from ~2,600 Awwwards Site-of-the-Day winners. Cheap add alongside your impeccable-lite / frontend-design judgment stack. _Trust: Tier 4 — new repo, but it's a checklist skill (low blast radius)._

## Product / GTM

- **AgriciDaniel wave** (promoted from 09-12 skipped log on traction): **youtube-scout** now ~32★/6 forks in 2 days (topic in → ranked YouTube research workbook out via Data API v3: views/engagement/momentum/breakout ranking) plus new **claude-seo** (universal SEO skill: industry detection, full-site crawl via Firecrawl MCP). Content/GTM research tooling. _Trust: Tier 4 — fast-shipping single author; API keys required, review scripts._

## Lanes searched — nothing new

- **Education / K-12 (Recess):** nothing new in window; searches only resurfaced already-seen items (canvas-mcp, ibl.ai guide) and SEO roundups (logged as increments).
- **Fintech / lending (Meridia/Hypomone):** nothing new; only already-seen Blend / Nymbus / Agentic Banking Directory resurfaced.
- **Populi / SIS:** nothing new.
- **HN:** Algolia API unreachable this run; no in-window skill/MCP stories surfaced via available search.
