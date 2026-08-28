# Skills Scout — 2026-08-28

_Scan window: ~48h (Aug 26–28 UTC). SerpAPI recency layer used (3/3 budget: GitHub last-24h, official outlets last-24h, venture-lane last-24h). Sources per Context/skills-scout-sources.md; relevance per Context/current-focus.md (v3) + venture STATUS files._

## Official / Tier 1

- **Claude Code v2.1.247–250 bundle** (Aug 26–28) — v2.1.247: `SendFeedback` tool (Claude drafts feedback reports for `/feedback`), `/claude-api cost-optimize` (profiles a project's API spend + cost levers), Sonnet 5 auto-compact widened to its full 1M context. v2.1.248: **`--restricted` mode** (`CLAUDE_CODE_RESTRICTED=1`) — strips command/code-exec tools and WebFetch, confines file tools to the working dir, refuses `bypassPermissions`, ignores settings files; plus per-agent prompt-cache TTL frontmatter, `/loop` dynamic + autonomous modes now always available, cross-session messaging on Bedrock/Vertex/Foundry, Workflow tool prompt cut ~5.7k→1k tokens. v2.1.250: fixes. **Why it matters:** daily driver across every lane, and `--restricted` is the day's real governance story — a first-party locked-down runtime primitive directly relevant to Aegis approval/governance patterns and FERPA-constrained Plumbline/Recess sessions. Trust: Anthropic-verified (code.claude.com changelog).
- **Model Hardware Standard (MHS) — research preview** (Aug 27) — new Anthropic standard letting agents safely operate physical lab/manufacturing instruments in parallel, sitting alongside MCP and the command line. **Why:** MCP-lane ecosystem news — Anthropic extending the standards family beyond MCP; no direct venture pull today, but standards moves shape connector strategy. Trust: Anthropic-verified (anthropic.com/news; Bloomberg coverage same day).
- **Claude Team plan for scientists** (support article, ~Aug 27) — discounted Claude Team subscription for academic and non-profit research groups and labs. **Why:** grants & nonprofit/education pricing-programs lane (Turner-adjacent; education/nonprofit pricing watch). Trust: Anthropic-verified origin (support.claude.com), but full article was not fetchable this run — verify terms before acting.
- **Official plugin marketplace, Aug 27–28:** one new vendor add — activecampaign (marketing automation; logged to skipped as off-stack). Otherwise only Carta version bumps. `anthropics/skills`: no commits since Aug 26. Trust: Anthropic-verified.

## Claude / Cowork / dev-tooling lanes (Tier 2–4)

- **figma/mcp-server-guide — Figma's official MCP guide + agent skills** (new `figma-implement-motion` skill + motion-lint-rules pushed within the last day) — official Figma repo pairing its MCP server with skills that teach agents to implement motion/animation from Figma designs. **Why:** Claude Design / UI-mockup lane (open item #5) — design→code with vendor-authored guidance. Trust: Tier 2 (vendor-official; verify skill contents before install).
- **damejan80/tokentab** (~212★ day one, Aug 27) — CLI that reads Claude Code / Codex / Gemini CLI session logs and computes cost by model, project, and day. **Why:** extends the per-skill/MCP usage-attribution thread (06-26, /usage 08-26) to cross-tool cost accounting — useful for multi-venture spend tracking. Trust: Tier 3/4 (community, strong day-one traction; it reads local session logs — review before running).

## Product / GTM lane

- **ToolMonsters/hand-raisers** (19★ day one, Aug 27; known author — handoff-skill, surfaced 07-23) — skill that finds people who publicly asked for what you sell this week, qualifies each ask, checks competition, and drafts replies; runs on Bright Data. **Why:** MIG GTM / Plumbline demand-gen experiments. Trust: Tier 4 (install-with-caution; needs a Bright Data account and does live scraping).

## Lanes searched — nothing new in window

- **K-12 / Recess:** only July "Claude for Teachers" press recycles; no new installable tooling. (One SLED-gov intel vendor logged to skipped.)
- **Fintech / lending (Meridia · Hypomone):** nothing beyond already-seen Plaid MCP early access and agentic-banking directory; press recycles only.
- **Populi / SIS + Postgres:** quiet — nothing beyond the already-surfaced supabase / neon / pg-aiguide family.
- **Governance / audit (Aegis):** no new third-party tooling; `--restricted` (item 1) is the governance item of the day.

## Notes

- Spam caution continues: fake "Claude AI Free Unlimited" / "Claude Jailbreak" download repos appeared Aug 27 — malware-pattern, never install (logged).
