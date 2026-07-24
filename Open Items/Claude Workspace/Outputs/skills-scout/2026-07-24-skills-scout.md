# Skills Scout — 2026-07-24

Quiet Tier 1 day (only a Claude voice-mode model upgrade, out of category). Today's five are high-traction ecosystem tools that hit the last-24h search index and were not yet in the seen index. SerpAPI used: 3/3 calls (24h-scoped GitHub + news + community queries).

## 1. nexu-io/open-design — open-source Claude Design alternative
- **What:** Local-first desktop app where your coding agent (Claude Code, Codex, Cursor, 20+ CLIs via BYOK) is the design engine: prototypes, landing pages, dashboards, slides — real files with HTML/PDF/PPTX/MP4 export. ~81k★, Apache-2.0, pushed today.
- **Why it matters:** Directly on open item #5 (Claude Design / UI mockups / interactive prototypes). A repo-native, exportable way to iterate Plumbline dashboard mockups without leaving the agent workflow.
- **Trust:** Tier 3 — community org with massive traction (and 600+ open issues); vet before installing. https://github.com/nexu-io/open-design

## 2. EveryInc/compound-engineering-plugin — lessons that compound into your agent
- **What:** Every's official plugin (Claude Code/Codex/Cursor): plan → work → review loops where each task's lessons are written back into your agent's context and skills, so the system gets better with every unit of work. 23.4k★, MIT, active today.
- **Why it matters:** This is your "agentic context setup, not one-shot prompts" doctrine turned into an installable workflow — a strong pattern for the Plumbline build loop and for how the Claude Workspace repo itself accretes context.
- **Trust:** Tier 2/3 — known company (Every), official repo. https://github.com/EveryInc/compound-engineering-plugin

## 3. mksglu/context-mode — context-window optimization layer
- **What:** Sandboxes tool output (claims ~98% context reduction), persists session memory, and enforces routing across 17 agent platforms via MCP + hooks. 19.3k★, pushed Jul 23.
- **Why it matters:** Token economics for long Cowork/Code sessions — the practical complement to Anthropic's context-engineering doctrine (surfaced 06-30).
- **Trust:** Tier 3/4 — single author with large traction; non-OSI "Other" license — read it before adopting. https://github.com/mksglu/context-mode

## 4. Yeachan-Heo/oh-my-claudecode — teams-first multi-agent orchestration
- **What:** The highest-traction community harness (38k★, MIT) for running teams of Claude Code agents with parallel execution; active this week.
- **Why it matters:** Multi-agent orchestration surfaced as a concept 06-22 (Code with Claude); this is the concrete, widely-adopted way people are actually doing it — relevant when Plumbline work outgrows single-session Claude Code.
- **Trust:** Tier 3 — community, very high adoption. https://github.com/Yeachan-Heo/oh-my-claudecode

## 5. vercel-labs/agent-browser — browser automation CLI for agents
- **What:** Vercel Labs' Rust CLI that gives AI agents a scriptable browser (39k★, Apache-2.0, active; agent-browser.dev).
- **Why it matters:** Agent-driven UI testing of Plumbline prototypes/dashboards from inside Claude Code, and a workaround for JS-heavy sources (e.g. the X/Twitter caveat in your sources file).
- **Trust:** Tier 2 — Vercel official lab. https://github.com/vercel-labs/agent-browser

---
_Deduped against seen-index (Finn-loop, handoff-skill, enterprise-prd-toolkit, openhub, Grill-Me/HN repost, Claude Security plugin coverage all dropped as repeats). Near-misses logged in skipped-log._
