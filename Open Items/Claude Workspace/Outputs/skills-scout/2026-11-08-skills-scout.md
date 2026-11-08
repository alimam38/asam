# Skills Scout — 2026-11-08 (Sun)

_Window: Nov 6 to Nov 8 (weekend run, so a light day). Sources: Tier 1 repos (anthropics/skills, claude-plugins-official, claude-code CHANGELOG), Anthropic news, GitHub repo search for repos created since 11-06, built-in web search, SerpAPI (3 calls: `site:github.com` SKILL.md/MCP qdr:d, Google News "Anthropic Claude" qdr:d, venture-lane MCP qdr:d, which returned 0)._
_Deduped against seen-index (name + URL). 7 items surfaced; non-fits logged in skipped-log._

## Official / Tier 1

1. **Office skills moved to the Apache 2.0 license** (anthropics/skills PR #2146, Nov 6). The `docx`, `pdf`, `pptx` and `xlsx` skills now use the same Apache 2.0 license as most of the repo. Before this they were source-available but not openly licensed.
   - **Why it matters:** these four skills sit underneath much of your Turner and Plumbline output: turner-brand, print-preflight, the receivables reports, and board memos. Apache 2.0 means you can fork and modify them, and ship derived versions inside a product. For example, a Plumbline report generator could be built on the xlsx/docx skills without license ambiguity. This affects the **Plumbline** GTM SaaS and **Turner ops**.
   - **Trust:** Anthropic-verified (Tier 1). Keep the NOTICE/LICENSE files when you fork. https://github.com/anthropics/skills/pull/2146
   - _Checked, nothing new:_ Claude Code is still on 2.1.319 (surfaced 11-07). claude-plugins-official added only the Xcode and champion-kit plugins (both already seen) plus infrastructure bumps.

## Aegis — governance / approvals / audit

2. **Yu-Peng-Tu/zhiheng-enterprise-agent** (created Nov 6). An auditable enterprise knowledge-and-workflow agent: RAG, human approval gates, idempotent execution, and event logging.
   - **Why it matters:** it matches Aegis's governance-alert approval recording (PR #8): an approval gate followed by an idempotent action and an audit record. Worth comparing as a reference design before the Aegis disposition session.
   - **Trust:** unknown / install-with-caution (Tier 4, new, ~0 stars). Read it, don't run it. https://github.com/Yu-Peng-Tu/zhiheng-enterprise-agent
3. **rainyZhou2/SreAgentHarness** (created Nov 6). A self-hosted, multi-tenant agent harness with risk-gated tool approvals and durable, resumable runs.
   - **Why it matters:** "risk-gated approvals" means tiering tool calls by risk before they reach a human. That pattern fits both Aegis and Hypomone's governance gate. Its multi-tenant design is also a reference for Plumbline (Turner = tenant #1).
   - **Trust:** Tier 4, new. https://github.com/rainyZhou2/SreAgentHarness
4. **dockndevai/mcp-github-enterprise** (created Nov 6). A safe-by-default MCP server for GitHub Enterprise covering orgs, repos, teams, rulesets, security alerts and Actions, with writes gated behind explicit opt-in.
   - **Why it matters:** this is the GitHub-workflow lane. Your scheduled jobs write to `asam` through broad Composio GitHub scopes, and this shows a read-default / write-opt-in posture you could copy.
   - **Trust:** Tier 4, new, unproven. https://github.com/dockndevai/mcp-github-enterprise

## Recess — K-12

5. **morrowdock/marty** (created Nov 6). An "AI teacher" built on the MartyGraphics engine. It exposes MCP tools and runs a plan → author → check → repair loop for generating lessons.
   - **Why it matters:** the check-and-repair step is the useful part. It is the generate-then-verify pattern that Recess's prerequisite-routing and math-gap outputs need before any teacher at Shadow Rock sees them.
   - **Trust:** Tier 4 (1 star). Pattern reference only. Check that no student data is involved before trying it.  https://github.com/morrowdock/marty

## Meridia / Hypomone — fintech and lending

6. **Carrington Labs MCP server** (compliant credit models in AI lending workflows). **Launch date not verified and likely older**, but it is not in the seen-index. The server exposes Carrington's cash-flow underwriting models (Cashflow Score) to agents through MCP, with compliance framing.
   - **Why it matters:** cash-flow underwriting is how you lend to misbanked operators without a thin-file credit score, which is **Hypomone lending step 2/3**. It is also a comparable product for the Meridia Trust Index IP; review it before the patents are drafted.
   - **Trust:** vendor press release via FF News (Tier 2/4). Verify the launch date and terms. https://ffnews.com/newsarticle/fintech/carrington-labs-launches-first-mcp-server-bringing-compliant-credit-models-into-ai-lending-workflows/

## Claude Code / Cowork practice

7. **"CLAUDE.md rules are requests; hooks are enforced"** (FourWeekMBA, Nov 8). A commentary piece arguing that instructions in CLAUDE.md or a skill are advisory to the model, while hooks are deterministic. It matches Anthropic's own docs.
   - **Why it matters:** your governance-not-guardrails thesis and the Aegis/Hypomone "gate in code" decision rest on this distinction. Anything that must never happen (for example, no FERPA data leaving Recess, or no Populi writes) belongs in a hook or permission rule, not in prose. The 11-06 privacy mod (already seen) is Anthropic doing exactly that.
   - **Trust:** Tier 4 commentary. The principle itself is Tier 1 (hooks docs). https://fourweekmba.com/ai-anthropic-claude-md-rules-are-requests-hooks-are-enforced/

## Lanes searched, nothing new
- Populi / SIS / FERPA: nothing new in the window (existing whitegloveai K-12 and higher-ed skill packs are already known).
- Postgres / NAS / Docker MCP, QuickBooks MCP, grants/nonprofit MCP: no new repos since 11-05.
- KSW (grants + music/education tooling): nothing.

## Ask
Pick any to adopt or trial. My suggestion: **#1** (fork the Office skills into a Plumbline/Turner report kit now that the license allows it), and read **#2 and #3** before the Aegis disposition session.
