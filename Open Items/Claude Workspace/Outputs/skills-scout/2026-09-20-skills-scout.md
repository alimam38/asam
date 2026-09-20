# Skills Scout — 2026-09-20

Scan window: 2026-09-18 → 2026-09-20 (last digest 09-19). SerpAPI used: 3 calls (24h GitHub sweep, Google News, weekly edu/fintech MCP). Trust tiers per skills-scout-sources.md.

## Official / Tier 1

- **anthropics/k12-teacher-skills** — official Anthropic repo of Agent Skills + eval rubrics for K-12 teachers, co-developed with Learning Commons (★520, Apache-2.0; created Jul 2026 — backfilled, never surfaced). Direct Recess-lane material: standards-aligned teacher workflows, plus the eval rubrics show how Anthropic grades pedagogy skills — and it pairs with the Learning Commons Knowledge Graph connector already in this workspace. Trust: Anthropic-verified. github.com/anthropics/k12-teacher-skills
- **Claude Code v2.1.275 + v2.1.278** (Sep 17–19) — v2.1.275 adds syncing of skills/plugins from your claude.ai account into terminal sessions (`syncClaudeAiSkills` / `syncClaudeAiPlugins`) plus `/plugin install --marketplace`; v2.1.278 makes auto mode default to a server-side classifier for API/Enterprise users (no classifier overhead charges; new `/status` row). v2.1.276–277 (AGENTS.md support) surfaced 09-19. Trust: Tier 1. code.claude.com/docs/en/changelog
- **Official plugin marketplace** — only Wingspan (#6258) and incident.io (#6252) merged since 09-18, both surfaced yesterday; #6257 was partner-metadata only. anthropics/skills and claude-plugins-community: no commits since 09-18. Nothing new.

## Agent infrastructure (cross-lane: Aegis governance · skill routing · Hypomone intake)

- **Jev — TypeSafe AI's "System One" decision model + a 72-hour ecosystem explosion** — launched Sep 15: a non-LLM frontier model for fast typed decisions inside software — schema-constrained outputs (type errors/hallucination impossible by construction, per vendor), calibrated confidence on every answer, 70–500ms latency, $0.042/M input tokens. The ecosystem that erupted in three days is the story: jev-review (★177, local-first MCP continuous code review), kerpopule/hermes-jev-skills (★144, Jev-powered model routing / memory / skill selection), jkudish/jev-mcp (★137) and itsmostafa/typesafe-mcp (★126) MCP connectors, kbhuw/jev-sift (★46, batch text classification), Ying-Kai-Liao/jev-browser (★34, LLM plans / Jev decides), tacticocc/Jevbridge (★25, ACP+MCP adapter), kraayenjon/awesome-jev (★41), plus skill-routers (lomeshdutta/skill-router) and decision-design skills (24601/Augustus, harrymunro/decision-first). Why it matters: typed decisions + calibrated confidence + deterministic, audit-friendly judgments is precisely the Aegis governance-not-guardrails shape (approval gates, routing, screening); ms-latency cheap classification also fits Hypomone intake/screening and Recess prerequisite routing. Trust: TypeSafe official = Tier 2 new vendor — verify the "cannot hallucinate" claim yourself; ecosystem repos are day-old Tier 3/4 — read before install. typesafe.ai/blog/introducing-system-one-models-and-jev
- **kitze/skillbox** (★207, Sep 17) — self-hosted, versioned skills library for AI agents: MCP interface, scoped clients, optional Jev recommendations. Known indie author (Kitze). The own-your-skill-registry pattern fits how this workspace already runs its lane registry. Tier 3. github.com/kitze/skillbox
- **nahid-sparktales/agent-dispatcher** (★26, Sep 19) — capability-aware Claude Code dispatcher: 27 specialist roles, composable skills, MCP/tool routing, verification workflows. Overlaps previously-surfaced orchestrators; the verification-workflow wiring is the interesting part. Tier 4. github.com/nahid-sparktales/agent-dispatcher
- **friday-memory/friday** (★47) — open-source persistent cognitive memory layer for coding agents (Cursor/Claude/Copilot). Crowded field (claude-mem, memsearch, agent-memory all previously surfaced); watch, don't adopt. Tier 4. github.com/friday-memory/friday

## Aegis — governance / audit

- **elsechord/CyberGuard** (★48, Sep 17) — evidence-driven autonomous SOC team on AgentTeams: hash-bound approvals, HMAC audit chain, rollback, reproducible attack scenarios. The SOC use case isn't yours, but hash-bound approval + tamper-evident audit chain are directly liftable Aegis primitives. Tier 4 — pattern read, not install. github.com/elsechord/CyberGuard
- **Smarsh "AskSmarsh" AI + MCP server** (~Sep 16) — financial-services compliance-archive vendor ships a policy-enforced MCP bridge into its comms archive. Another regulated-industry-MCP proof point for the agentic-banking file. Tier 2 press (ffnews.com).

## Meridia / Hypomone — fintech & lending

- Quiet window beyond the Jev intake/screening angle and Smarsh above. Plaid MCP (recirculating via an mcpmarket listing) was surfaced 08-17. Searched lending / CRA / Plaid / community-lending MCP: nothing new.
- **Apideck MCP server** — one MCP server, 200+ SaaS connectors across accounting, CRM, HRIS, file storage. The aggregator-MCP pattern is relevant to Plumbline's QBO+Populi+Gusto integration surface (one governed connector vs. many) — but it puts a vendor in your data path; evaluate trust before use. Tier 2 vendor. apideck.com/mcp-server

## Recess — K-12 education

- **anthropics/k12-teacher-skills** (see Official / Tier 1) is the headline for this lane.
- **Caution — hirotomasato/yowes** (★83, Sep 19) — MCP server that generates "realistic teacher documents (ID cards, licenses, letters) for 13 countries." Fraud-shaped tooling trending in the education keyword space; awareness only, do not install. Tier 4.

## Plumbline / product, design & GTM

- **op7418/guizang-product-video-skill** (★185, Sep 18) — 归藏's skill for making software-update promo videos from your real product components and design language (storyboards, original music, SFX, render; Claude Code + Codex). Known, credible Chinese AI curator; strongest new GTM-craft skill this window. Tier 3. github.com/op7418/guizang-product-video-skill
- **INSANE0777/Awwards-mcp** (★36, Sep 18) — design-inspiration MCP: search award-winning websites with real screenshots from inside the agent. Fits the Claude Design / UI-mockup open item. Tier 4. github.com/INSANE0777/Awwards-mcp
- **Raja0sama/vibex** (day-old) — ERD, C4, API and lifecycle architecture diagrams + checkable docs generated from Prisma/OpenAPI/GraphQL, one self-contained HTML file. Spec-artifact fit for Plumbline/Hypomone schema work. Tier 4, unproven. github.com/Raja0sama/vibex
- **sowadalmughni/ai-codebase-audit + vibe-debt-scanner** (Sep 20) — audits AI-generated codebases for six production failure modes (disconnected schema, missing RLS, exposed secrets, broken auth, unwired integrations, N+1) and scores tech debt with PR-gate verdicts (PASS/WARN/BLOCK). Timely hygiene for AI-built Plumbline/Hypomone code. Tier 4, day-zero. github.com/sowadalmughni

## Quiet lanes

- Populi / SIS-LMS: nothing new. Postgres/NAS/Docker: nothing new (Jev-adjacent tooling aside). Grants / KSW: nothing new this window.
