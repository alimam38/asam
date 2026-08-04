# Skills Scout — 2026-08-04

Scan window: last 1–2 days (Aug 2–4). SerpAPI recency layer used (3 calls: 24h GitHub sweep, 24h lane sweep, Google News). Sources per skills-scout-sources.md; deduped against seen-index through 2026-08-03.

## Official / Tier 1

- **Claude Code v2.1.221 (Aug 4)** — today's release is a security/hygiene bundle: sandbox credential **masking** (`mode: "mask"` — sandboxed commands see a sentinel, the proxy substitutes the real value on egress), a fixed zsh `[[ ]]` permission-check **bypass**, `claude plugin validate` warnings for names Claude Desktop's managed-marketplace sync would reject, a new **`prompt-audit`** subcommand in the claude-api skill (flags prompts/tool descriptions written for older models), and a Focus view for hiding tool chatter. Why it matters: credential masking + the permission-bypass fix land directly on your agentic-setup and install-with-caution posture; `prompt-audit` is useful after the Opus 5 default switch. Trust: Anthropic-verified — code.claude.com/docs/en/changelog.
- **Official plugin marketplace: no new vendors this window** — last ~24h of anthropics/claude-plugins-official is version bumps only (datarobot, aws-agents, huggingface, bigquery-data-analytics, amplitude, figma, logrocket, neon, render, sentry). Quiet window after the July vendor wave. Trust: Anthropic-verified (repo commits).

## Governance / audit / approvals (Aegis)

- **Smitner-Studio/facet** — github.com/Smitner-Studio/facet (new Aug 3, ~3★). Renders agent-written Markdown as a live local page and sends the human's click back to the agent as **typed data** — i.e., human-in-the-loop approval gates for coding agents. Why it matters: this is the exact interaction shape of Aegis's governance-alert approvals (PR #8) — worth reading even if you never install it. Trust: Tier 4, day-one, unvetted — read the code first.
- **LLMSecurity/awesome-agent-skills-security** — github.com/LLMSecurity/awesome-agent-skills-security (active last 24h). Curated catalog of agent-skill supply-chain security: malicious instructions embedded in SKILL.md, plus an MCP server/CLI for **governed agent/skill/tool access with policy checks**. Why it matters: doubles as an Aegis governance reference and as ammunition for this scout's own install-with-caution tiering. Trust: Tier 4 community catalog — verify per item.

## Skill / plugin curation & evaluation

- **metahub-ai/assay** — github.com/metahub-ai/assay (new Aug 3, ~3★). Open, reproducible framework for **evaluating AI artifacts across types** — skills, MCP servers, agents, and plugins — reads what's inside them and optionally runs them in a sandbox. Why it matters: the vetting wave (malskanner 07-22, SkillSpector 07-28, Skill-Sentinel 08-02) has been one-artifact-type-at-a-time; this is the first one-framework-for-all-four entrant, which is the shape a curation pipeline actually needs. Trust: Tier 4, day-one — watch traction before adopting.

## Claude Design / HTML artifacts (open item #5)

- **plannotator/effective-html** — github.com/plannotator/effective-html (active last 24h). Focused agent skills for building useful, **self-contained HTML artifacts** — from low-fidelity wireframes to working interactive prototypes. Why it matters: directly on the "HTML is the new Markdown" thesis (seen 06-29) and your open item #5 (UI mockups / interactive prototypes without leaving Claude); also relevant to Hypomone's phone-first Charter form mockups. Trust: Tier 3/4 community — small repo, inspect before use.

## Fintech / lending (Meridia · Hypomone) — backfill

- **Blend "Autopilot" MCP Server** — nationalmortgageprofessional.com (May 2026; backfill — never surfaced, found via this window's lending-lane sweep). Blend (major mortgage-lending platform) opened its loan workflows to **lender-owned AI agents** via MCP: credit pulls, pricing checks, compliance verification, with audit trails and required authorization for sensitive actions. Why it matters: a production reference architecture for exactly the Hypomone Gate-3+ lending pattern — agents acting inside a regulated lending workflow behind approval gates — and evidence the "bring your own agent to the lending platform" model is real. Not input to the Gate-1 Charter build. Trust: Tier 2 vendor-official, press-carried; off-window, marked backfill.

## Lanes searched, nothing new to surface

- **Education / K-12 (Recess):** window sweep returned only already-seen items (ASSISTments connector logged 08-02, Claude for Teachers, GarethManning library) and off-fit churn (Qualy study-abroad payments, logged 08-03). Nothing new.
- **Populi / SIS / Postgres / semantic layer:** only the neon marketplace version bump (Neon skills surfaced 07-29); no new Populi or Postgres tooling in window.
- **Cowork / scheduled tasks / MCP spec:** no new official announcements in the Aug 2–4 window; post-spec (07-28) churn only.

---
*SerpAPI: used (3/3 calls). Increments and true non-fits from this window are in skipped-log.md (14 entries).*
