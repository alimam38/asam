# Skills Scout — 2026-06-20

Quick morning scan. Sources worked down by tier (official → community). Seen-index
was empty (first run), so nothing was dropped as a repeat. Caveat: most platform
items below come from **this week's official changelog (week of June 19)** — web
search can't pin exact publish days, so read "fresh" as current-week, not literally
yesterday. (UTC clock read 06-21; using your local date 06-20.)

## Items

### 1. Enterprise-managed MCP connectors (via identity provider, Okta first)
- **What:** Admins provision MCP connectors org-wide through the IdP; users get
  zero-touch connector access on first login, with authorization centralized across
  Claude chat, Claude Code, and Cowork (Team/Enterprise beta).
- **Why it's relevant:** Squarely in your MCP-connectors + Cowork/Code focus. For
  Plumbline (multi-tenant SaaS, Turner = tenant #1), IdP-provisioned connectors are
  the clean way to hand each institution its connectors without per-user setup.
- **Source:** https://support.claude.com/en/articles/12138966-release-notes
  (also via https://releasebot.io/updates/anthropic/claude)
- **Trust:** Tier 1 — Anthropic-verified.

### 2. Claude Developer Platform — new code-exec / web-search / web-fetch tool versions
- **What:** New tool versions expose the 90-sec per-cell limit for long-running code
  and add `response_inclusion` to trim consumed result blocks in agentic loops — no
  beta header required.
- **Why it's relevant:** You care about agentic context setup (not one-shot prompts)
  and building agents/MCP. `response_inclusion` is a context-budget lever for long
  Cowork/Code runs — the kind this very scout is.
- **Source:** https://releasebot.io/updates/anthropic (confirm on https://docs.claude.com)
- **Trust:** Tier 1 — Anthropic-verified.

### 3. Org-wide skill provisioning from the admin console
- **What:** Team/Enterprise admins can upload a zipped skill folder under Organization
  settings and have it on-by-default for every user across web chat, the Desktop chat
  tab, and Cowork — skills are no longer per-user / per-repo.
- **Why it's relevant:** Directly in your SKILL.md-authoring + skill/plugin-curation
  domain. If MIG/Turner standardizes skills (this scout, Plumbline ops skills), this
  is the distribution path. (Freshness: reported as a June 2026 change — confirm exact
  date before relying on it.)
- **Source:** https://support.claude.com/en/articles/12138966-release-notes
- **Trust:** Tier 1 — Anthropic-verified.

### 4. MCP-PostgreSQL-Ops (call518) — Postgres DBA MCP server
- **What:** 30+ tools for performance analysis, bloat detection, lock/deadlock
  monitoring, autovacuum and schema inspection; no extensions required; PG 12-18.
- **Why it's relevant:** Hits your NAS / Docker / PostgreSQL domain — useful for
  self-hosted Plumbline/Turner Postgres on the NAS; read-only DBA introspection pairs
  well with an agentic workflow.
- **Source:** https://github.com/call518/MCP-PostgreSQL-Ops
- **Trust:** Tier 3 — community GitHub → install-with-caution; vet read-only scoping
  and credentials before pointing at prod. Freshness not confirmed as last-1-2-days;
  surfaced because it's on-topic and not previously seen.

## Skipped (for transparency)
- Git MCP server (official, ~Jun 2) and Postgres MCP servers (pgEdge GA Apr 3,
  YawLabs Jun 6) — relevant but outside the 1-2 day window.
- Claude Design updates (canvas editing, Claude Code sync) — fresh + Tier 1 but
  tangential to your stated focus.

---

## Second pass (re-run, same day)

_First pass above leaned on this week's platform changelog. This supplement adds 5
actually-installable skills / MCP servers / plugins from the directories and GitHub,
none repeating the seen-index. Seen-index is still small, so these lean foundational
over bleeding-edge — the call the task says to make while we're early. (And: this pass
re-surfaces Claude Design as a real pick, since it's your open item #5, not a tangent.)_

### 1. anthropics/knowledge-work-plugins — open-source Cowork plugin repo
- **What:** Anthropic's public repo of role-based Cowork plugins (each bundles skills,
  connectors, slash commands, sub-agents), installable/forkable; ships a
  `cowork-plugin-management` plugin with a `create-cowork-plugin` skill.
- **Why it's relevant:** Two focus domains at once — Cowork agentic setup and
  SKILL.md/plugin curation. `create-cowork-plugin` is the cleanest reference for
  packaging your Plumbline/Talbot workflows into a real plugin instead of loose skills.
- **Source:** https://github.com/anthropics/knowledge-work-plugins
- **Trust:** Tier 1 — Anthropic-verified.
- **Freshness:** Actively-maintained repo; no single publish date to pin — foundational.

### 2. Claude Design (Anthropic Labs) — prompt-to-prototype mockups & decks
- **What:** Labs tool (research preview, Opus-class) turning a description into mockups,
  interactive prototypes, slides, one-pagers; learns a design system from your
  codebase/design files so later projects reuse your colors and components.
- **Why it's relevant:** Literally your open item #5 ("when to use it"). Useful rule from
  the coverage: reach for it for first-draft prototypes, pitch decks, quick landing pages,
  and PM → Claude Code feature-flow hand-off; keep Figma for pixel-perfect production UI.
  Good fit for exploring the Plumbline dashboard before committing to build.
- **Source:** https://www.anthropic.com/news/claude-design-anthropic-labs
- **Trust:** Tier 1 — Anthropic-verified.
- **Freshness:** Launched earlier in 2026 (≈April), not new-this-week — surfaced because
  it answers a standing open item (and the first pass undersold it as "tangential").

### 3. Postgres MCP Pro (crystaldba/postgres-mcp) — DB tuning MCP server
- **What:** Open-source Postgres MCP server with configurable read/write plus real DBA
  muscle — index tuning (hypopg simulation + Anytime algorithm), EXPLAIN-plan review,
  and health checks (bloat, cache, vacuum, replication lag).
- **Why it's relevant:** Postgres + MCP + embedded-analytics in one. Distinct from the
  call518 MCP-PostgreSQL-Ops already in your seen-index: that one is ops/observability-
  leaning; this one is performance/index-tuning-leaning. Useful for Plumbline's Postgres
  layer (Populi/QBO/Gusto data) when an agent needs to both query and *tune*.
- **Source:** https://github.com/crystaldba/postgres-mcp
- **Trust:** Tier 2/3 — known directory/author (PulseMCP, mcpservers.org); install-and-
  review and scope credentials before pointing at prod.
- **Freshness:** Established, actively-maintained; can't pin to a recent date — foundational.

### 4. dbt Semantic Layer MCP server — governed metrics over MCP
- **What:** MCP server that lets Claude query dbt Semantic Layer metrics in natural
  language, so numbers come from governed metric definitions instead of agent-improvised
  SQL.
- **Why it's relevant:** On your "semantic layers / embedded analytics" domain. If
  Plumbline ever needs trustworthy, consistent KPIs across tenants, semantic-layer + MCP
  is the pattern (Gartner has warned MCP-without-a-semantic-layer agentic analytics tends
  to fail). Worth grokking the architecture even before adopting dbt specifically.
- **Source:** https://www.getdbt.com/blog/dbt-mcp-server-conversational-analytics
  (community impl: https://github.com/TommyBez/dbt-semantic-layer-mcp-server)
- **Trust:** Tier 2 — known directory/author (dbt Labs reputable; the community server is
  a separate, verify-before-trust build).
- **Freshness:** dbt MCP + semantic-layer tooling matured across late-2025/2026; no single
  dated drop.

### 5. skill-creator — now with evals & benchmarking
- **What:** Official skill-creator gained a test/measure/refine loop: writes an eval set,
  splits train/held-out, scores your SKILL.md description's trigger rate, proposes improved
  descriptions, re-tests — returns an HTML report and a best_description.
- **Why it's relevant:** Squarely on your SKILL.md-authoring focus. You already have
  skill-creator available; the news is the rigor layer — handy for tightening the
  `description:` on your own skills (like this scout) so they trigger reliably as models
  change.
- **Source:** https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills
- **Trust:** Tier 1 — Anthropic-verified.
- **Freshness:** A 2026 update; couldn't pin the exact publish date from the scan — saying
  so plainly.

_Second-pass skipped (logged to skipped-log.md): Claude Code dynamic workflows / `ultracode`;
pgEdge Postgres MCP (GA, deduped against Postgres MCP Pro); Open Semantic Interchange v1.0 spec._
