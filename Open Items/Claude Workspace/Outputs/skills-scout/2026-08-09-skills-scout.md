# Skills Scout — 2026-08-09

_Scan window: since the 08-08 digest (≈Aug 7–9). Method: SerpAPI recency layer (3/3 calls — 24h site:github.com sweep, 24h news, weekly venture-lane query) + GitHub API search (repos created ≥08-07; anthropics repo commits) + Tier 1 changelogs + built-in web search. Trust notes per skills-scout-sources.md._

## Official / Tier 1

1. **anthropics/k12-teacher-skills — official K-12 teacher Agent Skills + eval framework** — github.com/anthropics/k12-teacher-skills. Anthropic + Learning Commons co-developed repo behind Claude for Teachers: `k12-lesson-planning` (standards-aligned, curriculum-aware lesson plans) and `k12-lesson-differentiation` (tiered below/at/above-proficiency adaptations), packaged as an installable plugin (`claude plugin marketplace add ./k12-teacher-skills/plugin`) plus a Python evals framework. **Why (Recess):** this is Anthropic's own reference architecture for teacher-facing skills — standards alignment + differentiation is exactly the math-gap / prerequisite-routing shape, and the bundled eval harness is reusable for Recess skill QA. Trust: Tier 1, Anthropic-verified (Apache-2.0, ★57).

2. **Managed Agents August launch wave — budgets, GitHub-loaded skills, geo control** (Aug 5–7). The claude-api skill in anthropics/skills was refreshed Aug 7 (#1532) to mirror it: session/deployment `budget` objects (minor-unit cents) with `budget_reached` pause semantics and change/remove-to-resume, `session.usage` events, multi-agent shared caps; platform notes add GitHub-loaded skills into Managed Agents sessions, advisor support, and geo control. **Why:** cost-governance primitives for exactly the unattended scheduled-agent pattern this scout runs on; GitHub-loaded skills matches your repo-as-memory setup; budget/pause semantics are an Aegis-grade governance pattern worth stealing. Trust: Tier 1 (anthropics/skills commit + releasebot platform notes).

3. **New official marketplace plugins (Aug 7): airwallex-dev + salesforce-development** — anthropics/claude-plugins-official #5051/#5050. Airwallex (global payments / treasury infra) shipping an official dev plugin continues the fintech-vendor plugin wave (QuickBooks 07-03, Carta 07-30, Stripe/Gentkey 08-05) — worth a look at the Hypomone payments perimeter; salesforce-development is off-stack. Trust: Tier 1 marketplace listing / Tier 2 vendors.

## Ecosystem & standards — skill/plugin curation lane

4. **"Agent Plugins 1.0" — OpenAI, Microsoft, Google, Amazon, Vercel ship a portable agent-plugin standard** (~Aug 7–8) — vercel.com/blog/introducing-agent-plugins. One open format for agent plugins (skills + MCP + config bundles) portable across agent runtimes, shipped as 1.0 while the standards body was still debating — the cross-vendor counterpart to Anthropic's plugin format and the agentskills.io spec. **Why:** directly hits your skill/plugin curation lane — portability of the skill library you're accumulating, and a fork-risk watch item (does Claude Code/Cowork add import/compat?). Trust: Tier 2 (official vendor blogs; the crypto-aggregator echo coverage is noise — ignore it).

## Fintech / lending — Meridia · Hypomone

5. **Fifth Third "Newline" MCP Server + governed Skills layer** [backfilled — Apr 13, 2026 press; surfaced by this week's lane sweep] — ir.53.com. A regulated bank's embedded-finance platform (payments, cards, deposits) exposing an MCP server extended with a Skills layer that "standardizes how AI models use tools and workflows" under governance oversight. **Why:** proof pattern for Meridia/Hypomone — a chartered FI shipping agent-native surfaces with explicit governance framing; also an Aegis governance-pattern datapoint (skills as the governed interface, not raw tools). Pairs with Blend Autopilot (backfilled 08-04) and Plaid×Sierra (08-08). Trust: Tier 2 (official IR release).

## Education / K-12 — Recess

_(Item 1 above is the headline this run.)_

6. **meleantonio/assessment-cycle** — skills-only workflow for assessment design → rubric calibration → marking → feedback, targeting Claude Code and ChatGPT desktop (created Aug 7). **Why (Recess):** teacher-workflow shape useful for Shadow Rock assessment ops; complements the lesson-planning skills in item 1. Trust: Tier 4 — unknown author, ★3 day-one; read the skills before use.

## Claude Code / Cowork ops

7. **ray-amjad/peer-sessions** — a Claude Code skill for running a fleet of sessions on one machine and wiring them together with SendMessage (created Aug 7, ★10). **Why:** first community harness on top of cross-session messaging (surfaced 08-08) — relevant to juggling Plumbline + Hypomone build sessions. Trust: Tier 4 — day-one repo; install-with-caution.

8. **LunkiBR/ship-it** — pre-ship checklist skill that catches commonly-forgotten UX/product details before a screen or feature ships (created Aug 9, ★14). **Why:** lightweight ship-gate for Plumbline dashboard screens; pairs with the verification-loops lane (07-23). Trust: Tier 4 — brand-new; read SKILL.md before trusting.

## Lanes searched, nothing new
- **Populi / SIS / semantic layer:** nothing new in window — official marketplace showed version bumps only (fastly, hyperframes, wix, sentry, neon, stripe, carta, auth0, exa, langfuse…).
- **Governance/audit (Aegis):** no new installables beyond the budget/pause semantics (item 2) and Newline's governed-skills framing (item 5).
- **Grants/nonprofit and NAS/Docker/Postgres:** only pgEdge NL-agent repo churn (see skipped log).

_SerpAPI: used (3/3 budget). Dropbox key fetch OK; temp env file deleted._
