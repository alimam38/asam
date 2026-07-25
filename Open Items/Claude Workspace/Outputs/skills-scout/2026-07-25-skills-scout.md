# Skills Scout — 2026-07-25 (Sat)

_Window: last 1–2 days. SerpAPI recency layer used (3/3 date-restricted queries). Deduped against seen-index through 2026-07-24._

1. **Cowork "SharedRoot" VM-escape flaw (CVE-2026-46331)** — Accomplish AI disclosed that agents inside Cowork's macOS Linux VM could escape the sandbox: the host filesystem was mounted read-write at `/mnt/.virtiofs-root`, letting an agent read/write files far outside connected folders. Per the report, Anthropic closed it "as informative" without a fix; current Cowork defaults to cloud execution, but **local (on-your-computer) runs remain exposed**. *Why it matters:* you run Cowork desktop near FERPA-adjacent files — prefer cloud execution and connect minimal folders until this is hardened. *Trust:* security press (The Hacker News, Jul 23) — single source; verify against Anthropic advisories before acting.
   https://thehackernews.com/2026/07/claude-cowork-flaw-could-let-ai-agent.html

2. **tw93/Waza — engineering-habit skills (6.6k★)** — "Engineering habits you already know, turned into skills Claude can run": a disciplined-practice skill pack in the superpowers vein, MIT, pushed daily (incl. today). *Why:* skill curation + agentic context setup; established OSS author (tw93 of Pake). *Trust:* Tier 3 — known author, high traction.
   https://github.com/tw93/Waza

3. **zilliztech/memsearch — vendor-official persistent memory layer (2.4k★)** — unified cross-agent memory for Claude Code/Codex backed by Markdown + Milvus (hybrid semantic search, progressive disclosure), shipped as a Claude Code plugin + skills. *Why:* self-hostable agent memory on your own Docker infra — vendor-backed alternative to claude-mem (surfaced 07-13). *Trust:* Tier 2/3 — official Zilliz org repo.
   https://github.com/zilliztech/memsearch

4. **Figma official guide: build a design-system skill for Claude Code** (Jul 20) — Figma's resource-library walkthrough for authoring a SKILL.md that teaches Claude your design system (tokens, components, conventions) so generated UI matches it. *Why:* SKILL.md authoring craft + open item #5 (UI mockups/prototypes with Claude Design). *Trust:* Tier 2 — official vendor guide.
   https://www.figma.com/resource-library/how-to-create-a-skill-in-claude-code/

5. **puppyum/umlib-mcp — university-library paper access MCP** (new Jul 25) — lets Claude Code/Desktop read papers through your own institution's library access (EZproxy + open access). *Why:* seminary research workflows via Turner's library subscriptions instead of paywalled dead-ends. *Trust:* Tier 4 — day-old, 2★, handles library credentials → install-with-caution; read the proxy config before use.
   https://github.com/puppyum/umlib-mcp

---
_Near-misses logged to skipped-log (Opus 5 launch = out of category; MCP 2026-07-28 spec RC published — final lands Monday, re-check any MCP server builds; vercel-labs/agent-skills; iOS Simulator support; m-fyi install-count directories; ideate; agent-graph-mcp)._
