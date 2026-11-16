# Skills Scout — 2026-11-16

_Window: Nov 14–16 (quiet weekend). Sources: SerpAPI (3/3 calls: site:github qdr:d, venture-lane MCP qdr:d, Google News Anthropic), web search, GitHub repo search (created ≥ Nov 14), anthropics/claude-code CHANGELOG. Deduped against seen-index + skipped-log._

## Official / Tier 1
- Nothing new. Claude Code CHANGELOG still tops out at **2.1.325** (seen 11-14); no Anthropic newsroom posts since Claude for Manufacturing (Nov 12, seen) and Fable/Mythos 5.2 (Nov 9, seen).

## Aegis — governance, approvals, audit
- **Google "Esmeralda" — governed multi-agent platform blueprint** (google.github.io/esmeralda). Open-source reference for running ADK/A2A agents + MCP tool servers in production: zero-trust layers (workloads, governance, identity, security), Agent Gateway + Registry, central outbound policy, per-team chargeback, Terraform. Walk-through scenario is **mortgage underwriting**. *Why:* the most complete public "governance-not-guardrails" style reference architecture to compare against Aegis's layering and Hypomone's lending step 2/3; GCP-specific, so mine patterns, not code. *Trust:* Tier 2 (Google LLC-authored GitHub Pages; launch date unverified, surfaced by SerpAPI qdr:d).
- **Arcade × Mastra "Agent Action Governance" template** (mastra.ai/templates/agent-action-governance-with-arcade). A Loan Desk MCP server + Mastra agent where every tool call passes per-user policy hooks: role-checked loan approvals, sensitive-field filtering, hard limit blocking, and **human approval requests via Slack**. *Why:* a runnable lending-flavored approval-gate pattern — directly comparable to Aegis's governance-alert approvals (PR #8) and a candidate pattern for Hypomone's member/lending actions. *Trust:* Tier 2 (Mastra official template; Arcade is a known vendor — note it's their product demo).
- **VentureBeat: "One compromised MCP server can trick an AI agent into misusing tools you already trust"** (venturebeat.com/orchestration/…, ~Nov 15). Cross-server tool-misuse attack framing; argues identity governance, not deployment speed, is the real MCP project. *Why:* threat-model input for Aegis and for Hypomone's connector surface (Plaid/QBO). Reading, not tooling. *Trust:* Tier 2 (trade press).

## Claude Design / UI prototyping
- **diego3g/craft — design skills for AI agents** (github.com/diego3g/craft, MIT, 61★, created Nov 15). `/craft-setup` writes a design brief; `/craft` designs screens with every state (loading/empty/error) from your design system, explores options, critiques; works with Paper, Figma or plain HTML. *Why:* open item #5 (UI mockups/prototypes) — a brief-first, state-complete workflow that could feed Plumbline dashboard screens and pair with Claude Design. Compare against existing frontend-design skill before adopting. *Trust:* Tier 3/4 (known author — Rocketseat founder — but day-one repo; install-with-caution, read SKILL.md first).

## Lanes searched, nothing new
- Hypomone / Meridia fintech data (FRED/FDIC/HMDA, Plaid, CDFI/credit-union MCP): only re-surfacings (Narmi, Nymbus — already seen/older).
- Recess / K-12 (Claude for Teachers, COPPA, tutoring MCPs): nothing new since 11-13.
- Populi / SIS-LMS, Postgres/NAS, grants/KSW: nothing new.

## Ask
Pick any to adopt/trial: (1) clone Arcade×Mastra approval template as an Aegis/Hypomone spike, (2) read Esmeralda governance layer for Aegis disposition session, (3) trial `craft` against a Plumbline screen.
