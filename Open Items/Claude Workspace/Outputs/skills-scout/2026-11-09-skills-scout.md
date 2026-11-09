# Skills Scout — 2026-11-09

_Window: Nov 7–9 (weekend → quiet official day). Method: built-in web search + Firecrawl reads of Tier 1 pages + GitHub API (official-repo commits since Nov 7; repo search `created:>=2026-11-06/07` across all focus lanes) + SerpAPI 3/3 calls (tbs=qdr:d, site:github.com skills/MCP + Anthropic news). Deduped against seen-index (588 lines) and skipped-log. Trust tiers per skills-scout-sources.md._

## Official / Tier 1
- **No new official releases since the Nov 6–8 items already surfaced.** Checked: Claude Code latest is still v2.1.319 (Nov 6); support.claude.com release notes newest entry is Nov 6 (project spend tags — seen); releasebot shows nothing Nov 7–9; `anthropics/skills` and `anthropics/claude-plugins-official` have no commits since Nov 7; `knowledge-work-plugins` only a security-guidance 2.0.18 version bump (logged as increment). _Trust: Anthropic-verified sources, checked directly._

## Claude Cowork / Code — skill & plugin hygiene
1. **MBotirjonDev/skillset-lint** — lints Agent Skills one by one *and as a set*: spec compliance, trigger quality, broken paths, risky scripts, and **overlapping skills**. Why it matters: your skill list has several near-identical triggers (the 47/48/50/f5 prompt-rewriters, skill-forge vs skill-creator vs skill-distiller, docs vs docx); set-level overlap detection is the piece agent-lint (seen 11-06) didn't do. Good candidate to run once against your exported skills before the next curation pass. _Trust: Tier 4 — new repo (Nov 8, ★1); read the scripts before running; run on a copy._ https://github.com/MBotirjonDev/skillset-lint
2. **avivgerz-hue/vibe-shield** — 60-rule static security scanner shipped as an MCP server + skill, including a **skill-poisoning auditor** for SKILL.md/plugin content. Why it matters: complements skillwall (seen 11-07) — skillwall pins/diffs, this inspects contents; relevant to your skill/plugin curation lane and to any third-party skills pulled into Plumbline/Hypomone repos. _Trust: Tier 4 install-with-caution — ★24 in 2 days and the same author launched `unslop` the same day; verify the rules yourself, don't grant it write access._ https://github.com/avivgerz-hue/vibe-shield
3. **tailucanh/offload-mcp-server** — lets the main coding agent hand heavy reading (big files, logs, docs) to a second agent and read back only the answer. Why it matters: context-hygiene pattern for long Cowork/Code sessions like this scout (large seen-index/skipped-log files) and Plumbline's Populi API dumps; same idea as subagent delegation but tool-shaped. _Trust: Tier 4 (Nov 8, ★17)._ https://github.com/tailucanh/offload-mcp-server
4. **assassin808/learn-from-lessons** — skill/tool that turns your corrections into durable lessons the agent re-reads (Claude Code, Codex, MCP). Why it matters: overlaps your Writing Profile / preferences loop; worth a look only as a pattern for per-repo "lessons.md" in asam. _Trust: Tier 4 (Nov 9, ★14)._ https://github.com/assassin808/learn-from-lessons

## Recess / K-12 (FERPA)
5. **psd401/psd401-prr** — a school district's own (Peninsula SD 401, WA) open-source public-records-request manager with a **RCW 42.56 + FERPA compliance engine** (Django/DRF + React), replacing NextRequest. Why it matters: rare district-authored FERPA redaction/exemption logic you can read as a reference model for Recess's FERPA discipline and Shadow Rock admin ops (records requests are a real front-office burden). _Trust: Tier 4 — ★0, but org name matches a real district; WA-statute specific, so treat as pattern not drop-in._ https://github.com/psd401/psd401-prr
6. **greebrit32-lgtm/privacy-portfolio** — worked edtech vendor review (FERPA, COPPA, Texas law, SDPC NDPA), PIA/data map, and incident tabletop. Why it matters: ready-made checklist shape for vetting tools before they touch Shadow Rock student data (and for Claude for Teachers rollout questions). _Trust: Tier 4 — individual portfolio; templates only, verify legal claims._ https://github.com/greebrit32-lgtm/privacy-portfolio

## Lanes searched, nothing new
- **Meridia / Hypomone (fintech, lending, FDIC/HMDA/CU, Plaid):** only re-surfaced older launches (Comply MCP = Apr 2026, Blend/Nymbus/Agentic Banking Directory = seen) — logged.
- **Aegis (governance/approvals/audit):** new repos were increments of patterns already seen (SreAgentHarness 11-08, zhiheng 11-08).
- **Plumbline / Populi / Postgres:** no new Populi tooling; new Postgres MCPs are thin read-only increments (observe-mcp already surfaced).
- **Claude Design / scheduled tasks / live artifacts, KSW (grants/music), WayPoint:** nothing new in window.

## Your call (single ask)
Pick any to adopt/trial: **(1) skillset-lint** (one-time audit of your skill set — highest value), (2) vibe-shield, (3) offload-mcp, (5) psd401-prr as Recess FERPA reference. Default if no answer: none installed.

_Notes: SerpAPI available (3/3 used). The Neuron Nov 9 digest page could not be fetched (blocked). This run had no access to your computer — cloud only._
