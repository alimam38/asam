# Skills Scout — 2026-09-07

_Window: Sep 5–7 (since the 09-06 run) + verified backfills. SerpAPI recency layer used (3 calls: 24h GitHub scope, 24h web, Google News). Weekend window — official channels quiet; the signal is in skill/MCP security-and-infra tooling plus two heavily-starred backfills. Trust tiers per skills-scout-sources.md._

## Official / Tier 1
- **Official channels quiet this window.** No new plugins or skills landed in anthropics/claude-plugins-official, anthropics/skills, or claude-plugins-community Sep 5–7. Sep 4 evening was a ~30-plugin version-bump sweep (cloudflare, neon, mongodb, azure, aws-core, atlassian, resend, firecrawl, qdrant, posthog, dataverse…) — maintenance, not new capability. Claude Code v2.1.263 (Sep 6) is bug-fixes-only and was already logged on the 09-06 run. Trust: Anthropic-verified (commit logs + changelog).

## Skill & MCP security / governance / infra (Claude-Dev · Aegis · Meridia infra)
- **cisco-ai-defense/skill-scanner** (★2.5k, actively maintained; backfill — Jan 2026, never surfaced) — Cisco AI Defense's official security scanner for Agent Skills. The biggest-name vendor yet in the skill supply-chain security lineage (SkillSpector 07-28, malskanner 07-22, assay 08-04); candidate for a pre-install vetting step in the hub. Trust: Tier 2 — major vendor, still review before wiring into anything.
- **ToolHive (stacklok/toolhive)** — enterprise-grade open-source platform for running MCP servers securely: containerized isolation, secrets management, curated registry, Kubernetes operator; fresh coverage Sep 7 (Help Net Security). Direct fit for the NAS/Docker + governed-MCP posture (Meridia Postgres MCPs; Aegis-style control plane). Trust: Tier 2 — established Stacklok project; the coverage is new, the project isn't.
- **okf-memory/okf-agent-memory** (★421 in 2 days; new Sep 5) — Git-native persistent memory for coding agents: pure Go, zero external databases, embedded MCP server, BM25 search, progressive disclosure; claims "Google OKF v0.2" compliance and ~80% token savings. Memory-layer lane (claude-mem 07-13, memsearch 07-25, lemmalog 08-31). Trust: Tier 4 — brand-new org and the "Google OKF" standard claim is unverified; vet hard before adopting.
- **alchaincyf/huashu-mac-use** (★157 day-one; Sep 6) — Agent Skill for macOS computer use: drives native Mac apps that have no API, background reads, non-intrusive writes, per-step evidence capture. Lands the same weekend as Anthropic's background computer use (seen 09-06) — the community layer on top of it. macOS-only, so pattern-watch for Ali's Windows fleet rather than install. Trust: Tier 3/4 — known CN AI author (花叔); verify.
- **wbso-ai/omarchy-plugin-security-skill** (★62; Sep 6) — field guide + skill distilling the security pitfalls that block plugins on the Omarchy marketplace, from 5,000+ maintainer reviews. Useful reviewer-side checklist for anything shipped to a marketplace. Trust: Tier 4.
- **Skill-management tooling wave (Sep 5–6)** — **Routed** (bshea-1, ★16: universal local router for Agent Skills across coding environments), **agent-skiller** (lattebbrook, ★29: open-source visual step-by-step skill builder), **agent-plugins** (dmgrok, ★18 but Jan-created: quality-validated skill discovery). SKILL.md-authoring/curation lane. Trust: Tier 4 — small and new; watch traction.
- **shinpr/sub-agents-skills** (★83; active, Jan 2026) — cross-LLM sub-agent orchestration as Agent Skills: route tasks to Codex, Grok, GLM, Kimi, Cursor, Gemini, OpenCode from one session. Adjacent to the council lane (outside-model panels) — a skills-native alternative to council.py's provider layer. Trust: Tier 4.
- **AWS: "MCP went stateless — is your MCP server deployment well-architected?"** (Sep 1, AWS Architecture Blog) — prescriptive deployment guidance for stateless 2026-07-28-spec MCP servers (load balancing, scaling, auth). Reference doc for self-hosted MCP on the NAS. Trust: Tier 2.

## Document & output production (Cowork · Turner)
- **hugohe3/ppt-master** (★52.7k on GitHub; backfill — Dec 2025, pushed today) — turns documents or topics into native PowerPoint decks: real shapes, transitions, animations, data-backed charts (not images-pasted-on-slides). If legitimate, the strongest PPTX generator surfaced to date — an upgrade path over consulting-pptx-skill (09-03) for Turner board/report decks. Trust: Tier 3 flagged — unknown author with a very high star count; check for star inflation (08-26 caution) before install.
- **imbad0202/academic-research-skills** (★46.7k on GitHub; backfill — Feb 2026, active) — research → write → review → revise → finalize pipeline skills for Claude Code. Relevant to research-heavy deliverables and the queued PBD-OS documentation work. Same star-inflation flag. Trust: Tier 3/4 — vet before use.
- **conorbronsdon/avoid-ai-writing** (★4.2k; backfill — Mar 2026) — the standalone upstream of the de-AI-writing wave already tracked (dripips/plain-prose merged it, seen 09-05): audits and rewrites content to strip AI writing patterns; works across agents. Trust: Tier 3 — known author.

## Education / K-12 (Recess)
- **Alchemist-Jo/textbook-anything** (★20; Sep 5) — agent skill for STEM textbooks: research prerequisites, write clear explanations, build connected exercises. The prerequisite-mapping method rhymes with Recess's math-gap / prerequisite-routing work (5th-grade analysis) — worth reading for method even though it targets university level. Trust: Tier 4.
- Claude-for-Teachers / K-12 outlets: nothing new since the 08-30 schools-and-districts launch.

## Fintech / lending (Meridia · Hypomone)
- **DocuSign opens its MCP server to every AI agent** (Sep 5) — agreement/e-signature workflows callable from any MCP client; relevant to membership/lending paperwork flows (Charter intake → signed agreements) when Hypomone reaches that gate. Trust: Tier 2 press (Yahoo Finance).
- Otherwise quiet: no new Plaid/CRA/CDFI-relevant skill or MCP motion Sep 5–7.

## Quiet lanes
- Populi/SIS-LMS, Postgres/NAS ops, grants & nonprofit pricing, governance-news beyond the items above: searched, nothing new this window.
