# Skills Scout — 2026-07-23

_Scan window: last 1–2 days. Trust tiers per Context/skills-scout-sources.md. SerpAPI recency layer: active (3/3 budget used)._

1. **Claude Security plugin (beta)** — `/plugin install claude-security@claude-plugins-official` (Tier 1 — Anthropic-verified; launched Jul 22).
   What: official multi-agent vulnerability scanner inside Claude Code — six-phase pipeline (inventory → threat model → research across injection/auth/memory-safety/crypto → sweep → 3-lens adversarial panel → max-effort re-review), 2-of-3 quorum on findings, full-repo or diff/PR scans, auto patch generation in scratch clones. Paid plan + CC ≥2.1.154. Docs: code.claude.com/docs/en/claude-security.
   Why: a pre-launch and per-PR security gate for Plumbline (FERPA-aware SaaS) and your GitHub workflow — and a reference implementation of adversarial-verification skill orchestration.

2. **"Building verification loops in Claude Code with skills"** — claude.com/blog/building-verification-loops-in-claude-code-with-skills (Tier 1; Jul 22).
   What: doctrine post on encoding manual checks as skills so Claude closes its own feedback loop — four deployment patterns (standalone, embedded, chained, PR-wide), built-in `/verify`, skill-creator integration, rubrics in Managed Agents.
   Why: directly upgrades your SKILL.md authoring practice (skill-forge) — the "verify" half of skill design that most libraries skip.

3. **finna/Finn-loop** — github.com/finna/Finn-loop (Tier 3/4 — community; unusual day-one traction ~125★/12 forks; created Jul 22).
   What: a 3-skill "AI software factory" for Claude Code — spec → build → review; humans merge.
   Why: mirrors your gate-driven product development (spec→build→review); day-old repo from an unknown org — vet before adopting.

4. **ToolMonsters/handoff-skill** — github.com/ToolMonsters/handoff-skill (Tier 4 — unknown author, ~25★, created Jul 22; install-with-caution).
   What: turns the current conversation into a complete handoff document so any LLM or later session picks up exactly where you left off.
   Why: agentic context setup + Cowork cross-session/device continuity; complements claude-mem (seen 07-13) with an explicit, portable artifact.

5. **fsbtactic-code/marketing-brain-skill** — github.com/fsbtactic-code/marketing-brain-skill (Tier 4 — unknown author, 3★, created Jul 22; install-with-caution).
   What: portable marketing "second brain" for Claude Code/Codex/Agent Skills — 502 curated sources spanning strategy, SMM, content, growth, CRO, buyer psychology.
   Why: the GTM lane of your focus (MIG GTM for Plumbline) — a content/growth reference skill rather than another PM library.

---
Method: SerpAPI 3/3 (qdr:d GitHub sweep, Google News, official-outlet sweep) + built-in web search + GitHub repo search (created:>2026-07-20). Deduped against seen-index — e.g. Cowork "Record a skill", malskanner, and olgaiv39/claude-oss-skills were already surfaced 07-22. Near-misses logged to skipped-log.
