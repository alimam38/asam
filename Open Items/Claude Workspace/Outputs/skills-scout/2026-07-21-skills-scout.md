# Skills Scout — 2026-07-21

Scan window: roughly the last 1–2 days (last run was 2026-07-20, a weekly reconciliation).
Deduped against seen-index.md. Yield was thin for a genuinely fresh 1-2 day window — most
churn was repeat coverage of things already in the index (Cowork web/mobile, Claude Design
overhaul, agent teams, dynamic workflows). The five below are the items that cleared both
the freshness bar and the focus filter.

## Items

### 1. Artifacts can now call your MCP connectors for live data + actions
- **What:** Per Claude Code's Week 29 digest (Jul 13–17), a published Artifact can pull live
  data and take actions through **each viewer's own MCP connectors** when they open the page —
  plus public sharing links, editor roles on Team/Enterprise, and artifacts created directly
  from Claude Tag sessions.
- **Why relevant:** "Scheduled tasks & live artifacts" is a named focus domain. This is the
  capability that turns a static artifact into a live dashboard view backed by a viewer's own
  connectors (Populi, QBO, etc.) — worth testing for a Plumbline-style live status page. Builds
  on the base Artifacts feature already logged 2026-07-13; this is the new incremental piece,
  not a repeat.
- **Source:** https://code.claude.com/docs/en/whats-new (Week 29, "v2.1.207–v2.1.212")
- **Trust:** Tier 1 — Anthropic-verified, official weekly dev digest.

### 2. New Relic plugin — official Claude Code plugins marketplace
- **What:** Merged 2026-07-20 into `anthropics/claude-plugins-official`. Adds observability
  skills: APM performance investigation, cloud cost analysis, Kubernetes debugging, NRQL query
  writing, and alert response, via New Relic's remote MCP connector.
- **Why relevant:** Plugin-curation focus, and a ready-made observability toolkit once
  Plumbline is live in production for Turner (or if NAS/Docker ops end up on New Relic).
  Moderate fit today, worth knowing it exists.
- **Source:** https://github.com/anthropics/claude-plugins-official/pull/4282 (source repo:
  github.com/newrelic/claude-code-plugin)
- **Trust:** Tier 1 — official plugin directory, Anthropic-merged.

### 3. Kinetic Gain Protocol Suite MCP server (mcp-kinetic-gain)
- **What:** A single MCP server unifying ~12 open AI-governance disclosure specs (Agent Cards,
  AI Evidence, MCP Tool Cards, Prompt Provenance, plus an EdTech trio: AI Tutor Cards, Student
  AI Disclosure, Classroom AI AUP) into ~75 callable tools, incl. `tutor_card_coppa_check` and
  `disclosure_aup_check`. Latest tagged release v0.9.0 (2026-07-05).
- **Why relevant:** Directly on the FERPA-aware Populi/SIS-LMS focus (education disclosure +
  compliance auditing tools), and structurally adjacent to Recess's own AI-governance
  spine — worth a skim as prior art/competitive landscape, not as something to install as-is.
- **Source:** https://github.com/mizcausevic-dev/mcp-kinetic-gain
- **Trust:** Tier 4 — single author, **0 stars/forks**, unvetted. Read before running; don't
  point it at real student data.

### 4. claude-skill-github-actions — GitHub Actions troubleshooting skill
- **What:** A Claude Code skill that detects repos with Actions enabled, fetches workflow runs
  via `gh` CLI by commit/branch, downloads and pattern-matches logs, and produces an actionable
  CI/CD failure summary.
- **Why relevant:** Squarely in the "GitHub workflow" focus lane — a narrower, more
  purpose-built alternative to the broader git-workflow-skill already logged 2026-06-30.
- **Source:** https://github.com/steeef/claude-skill-github-actions
- **Trust:** Tier 4 — single author, 1 star, early-stage; test on a throwaway repo first.

### 5. US-law-mcp — federal compliance-statute lookup MCP server
- **What:** MCP server exposing 130 curated US federal statutes/regs (46,646 provisions) incl.
  full FERPA and COPPA coverage plus HIPAA, SOX, GLBA, CCPA/CPRA, FISMA — sourced from eCFR/US
  Code with daily freshness checks. Actively updated within the last 1–2 weeks.
- **Why relevant:** A quick-reference tool for the FERPA-aware side of Populi/Talbot Hall work
  and for Recess's compliance/governance angle — look things up instead of trusting memory.
- **Source:** https://github.com/kaerez/US-law-mcp
- **Trust:** Tier 4 — single author, 1 star; treat as a pointer to primary sources, not a legal
  authority itself.

## Skipped (logged to skipped-log.md)
- Claude Code Week 29 minor bundle (screen reader mode, `/fork`, auto mode GA on third-party
  clouds) — accessibility/UX items below the daily-five bar.
- "Reflect" / Monthly Recap dashboard — usage-reflection feature, not an installable
  skill/plugin/MCP.
- Nonprofit fund-accounting MCP server (PulseMCP) — real listing exists but couldn't pin an
  exact name/author/URL with confidence in this pass; revisit with a direct PulseMCP query.
- Claude Design "brand consistency" self-correction — actually a June 17 2026 feature, already
  covered by the design-system-imports item logged 2026-06-27/06-30; not new.
- General MCP/skill directory churn (PulseMCP, GitHub topic pages, claudemarketplaces.com) —
  high volume, low per-item signal this pass.
