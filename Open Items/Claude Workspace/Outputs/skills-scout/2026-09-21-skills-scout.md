# Skills Scout — 2026-09-21 (Sunday)

Window: since the 09-20 scan (~24h, weekend). Official channels are quiet — no new commits in `claude-plugins-official` since the 09-19 adds, none in `anthropics/skills` since 09-17, and Claude Code is still at v2.1.278 — so today's signal is almost entirely community GitHub. 11 items surfaced. The TypeSafe/Jev wrapper flood (8+ new repos overnight) is logged as an increment, not re-surfaced.

## Official / Tier 1
- **Anthropic Institute: "Measurements for understanding the pace of AI development inside frontier labs"** — published this morning (09-21). Measurement framework behind the widely covered stat that Claude led ~26% of Anthropic's own R&D tasks in August. Why it matters: the best available baseline for how far agentic delegation — the bet under every one of your lanes — has actually gotten inside the frontier lab itself. Trust: Anthropic-verified. — anthropic.com/institute/measuring-pace-of-ai-development
- Otherwise quiet: plugin directory, skills repo, and Claude Code changelog all unchanged since items surfaced 09-19/09-20.

## Claude / Cowork / skills-ops
- **BuilderIO/skills** (★4.3k, pushed through the weekend) — Builder.io's vendor "skills for agents" collection, including `webmcp` for driving sites via MCP. A real vendor shipping agent-native web tooling as installable skills. Trust: Tier 2, known vendor. — github.com/BuilderIO/skills
- **initializ/forge** (★218, active this weekend) — open-source **runtime** for the Agent Skills standard: run skills next to a service, in your environment, on your infra. Directly relevant to the NAS/Docker self-hosting lane and to Aegis-style governed execution. Trust: Tier 3, known org, verify before prod. — github.com/initializ/forge
- **Berserk-hub150/skillhawk** (★63) — zero-dependency security scanner for Agent Skills / SKILL.md / MCP configs ("catch dangerous skills before they catch you"). Pairs with skillmd-lint (surfaced 09-19) as a vetting toolchain for your template-vetting workflow. Trust: Tier 4 — scan the scanner first. — github.com/Berserk-hub150/skillhawk
- **alifurkangokce/driftlint** (★56) — finds the claims in your CLAUDE.md / AGENTS.md / skills that the code no longer supports; zero-config, no API key. Timely now that Claude Code reads AGENTS.md (v2.1.277, surfaced 09-19). Trust: Tier 4. — github.com/alifurkangokce/driftlint
- **jtapes/claude-bus** (★3, day-old) — message-bus skill for Claude Code agents: file inboxes per project/subagent, background wake-ups, cron schedules, local web UI. Early, but it is the exact shape of your task-fleet / scheduled-tasks pattern. Trust: Tier 4, day-old — read the code. — github.com/jtapes/claude-bus
- **cochinescu/decent-skills** (★7, day-old) — blind multi-model code review: Codex, Gemini, Grok and Claude review the same packet **without repo access**. Same intent as your council skill; the blind-packet mechanic is worth stealing. Trust: Tier 4, day-old. — github.com/cochinescu/decent-skills

## Design / GTM
- **latent-spaces/brag** (★6.4k) — `/brag` skill: turns a just-built project into a short, shareable launch video (music, motion, share copy) in one command. GTM lane — launch/demo collateral for Plumbline and Hypomone milestones. Trust: Tier 3, high traction, author org less known. — github.com/latent-spaces/brag
- **zubair-trabzada/geo-seo-claude** (★10.8k / 1.6k forks — ⚑ repo funnels to a paid Skool community; star inflation plausible) — GEO-first "AI search optimization" skill: citability scoring, AI-crawler analysis, schema markup, PDF reports. Note: the scout previously judged SEO not lane-critical (jev-seo, 09-20), but this is the category's breakout repo — worth one look for the GTM/discoverability toolkit, then decide. Trust: Tier 3/4, flagged. — github.com/zubair-trabzada/geo-seo-claude
- **gongnyang/awesome-html-scrolline-deck** (★21, day-old) — "Scrolline Deck": scroll-driven cinematic HTML presentations (scrollytelling decks) as a Claude Code skill, 12 scene techniques. Claude Design / deck-artifact lane. Trust: Tier 4, day-old. — github.com/gongnyang/awesome-html-scrolline-deck

## Education / K-12 (Recess)
- **changshenhan/bb-mcp** (day-old, ⚑ caution) — headless Blackboard LMS MCP server (built against CUHK's instance): courseware download, assignment inspection/submission, announcements, fully headless credential auth. Not usable as-is, but a live worked example of the LMS-MCP pattern you'd want for Populi/SIS work — and a caution study in credential handling. Trust: Tier 4, single-institution scope. — github.com/changshenhan/bb-mcp
- Lane otherwise quiet: no new K-12/teacher-AI tooling in window (coverage still recycling the July Claude-for-Teachers launch).

## Fintech / lending (Meridia · Hypomone)
- Lane searched, nothing new in window. The fintech-MCP hits that came back (Nymbus core-banking MCP, Bud Financial) were already surfaced 09-09 / 08-29.

## Governance / audit (Aegis)
- Nothing new in window beyond skillhawk and forge above (both carry governance texture). systempromptio/awesome-ai-agent-governance already surfaced 08-26.

---
*Method: SerpAPI 3/3 budget spent (24h GitHub sweep, Google News, 24h Reddit — the Reddit query returned noise); official repos checked via GitHub API (commit-level); GitHub created:>2026-09-19 and pushed:>2026-09-20 searches; all candidates deduped against the seen index by name and URL.*
