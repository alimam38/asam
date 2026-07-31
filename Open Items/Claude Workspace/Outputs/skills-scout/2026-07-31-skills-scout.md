# Skills Scout — 2026-07-31

Scan window: last 1–2 days (Jul 29–31). Focus filter: Plumbline (Populi/QBO/Gusto/Postgres), agentic setup, skill authoring/curation, GitHub workflow. SerpAPI used (3 calls: 24h GitHub sweep, Google News, general). No new Tier-1 Anthropic releases in the window (Claude/Claude Code release feeds last updated Jul 24/28).

## 1. supabase/agent-skills — official Supabase Agent Skills (incl. Postgres Best Practices)
- **What**: Supabase's official skills repo, pushed within the last day; headline skill is "Postgres Best Practices" (schema design, RLS, query patterns for AI agents), plus Supabase-platform skills. Also documented at supabase.com/docs/guides/ai-tools/ai-skills.
- **Why it matters**: Directly on your Postgres lane for Plumbline — an official, maintained Postgres-practices skill even if you never touch Supabase's platform; complements pg-aiguide (07-02) and neondatabase/agent-skills (07-29).
- **Trust**: Tier 2 — official vendor repo. https://github.com/supabase/agent-skills

## 2. GitKraken official Claude plugin (Claude marketplace, Jul 30)
- **What**: GitKraken shipped an official plugin in the Claude marketplace — no CLI install; wraps its MCP server so agents get repo/codebase-aware Git tooling with lower token usage.
- **Why it matters**: GitHub-workflow lane; a marketplace-install Git layer for Cowork/Claude Code sessions like this repo-driven job. Also another data point in the vertical-vendor-ships-a-plugin GTM pattern (Carta, 07-30).
- **Trust**: Tier 2 — official vendor, marketplace-listed. https://www.gitkraken.com/blog/gitkraken-claude-code

## 3. GitHub Copilot code review: Agent Skills + MCP now GA (Jul 29)
- **What**: GitHub made agent skills and MCP support generally available in Copilot code review — custom skills and MCP servers now steer PR review on the GitHub side.
- **Why it matters**: The Agent Skills standard keeps crossing ecosystems (Google 07-06, Copilot now GA): skills you author once (skill-forge) can shape GitHub-native PR review on the asam/Plumbline repos, independent of Claude sessions.
- **Trust**: Tier 1/2 — official GitHub changelog. https://github.blog/changelog/2026-07-29-copilot-code-review-agent-skills-and-mcp-now-generally-available/

## 4. Lum1104/video-to-skill — turn videos/courses into evidence-grounded Agent Skills
- **What**: New (Jul 30) tool that converts videos and course material into evidence-grounded SKILL.md packages for Claude Code/Codex.
- **Why it matters**: OSS counterpart to Cowork's "Record a skill" (surfaced 07-22), aimed at your skill-authoring lane — could distill Populi/QBO training material into skills. Day-one repo (~14★), sandbox it first.
- **Trust**: Tier 4 — unknown author, install-with-caution. https://github.com/Lum1104/video-to-skill

## 5. StepSecurity Dev Machine Guard now inventories agent skills on dev machines (Jul 29)
- **What**: StepSecurity's endpoint tool now inventories which AI agent skills are installed across developer machines — supply-chain visibility for the skill layer.
- **Why it matters**: Skill-curation lane: joins the skill-security wave (malskanner 07-22, SkillSpector 07-28) but at the fleet/inventory level rather than repo-scan level — the "what's actually installed" audit question you'd want before trusting Tier 3/4 skills.
- **Trust**: Tier 2 — known security vendor; product announcement. https://www.stepsecurity.io/blog/dev-machine-guard-now-inventories-ai-agent-skills-on-developer-machines

---
_Dedup notes: Microsoft azure-skills/dotnet-skills official wave, Black-cat red-team skill (★130 day-one), warden MCP router, quickbooks-mcp (community), product-deep-research → skipped-log with reasons._
