# Skills Scout — 2026-07-22

Scan window: Jul 20–22. Anthropic official news was the big signal this pass; registries/HN were quiet, so items 2–5 come from a fresh-repo GitHub sweep (young, low-star — treat accordingly).

## 1. "Record a skill" in Claude Cowork — teach a skill by screen recording
- **What:** New Cowork feature (launched Jul 21, Pro/Max/Team): record yourself doing a task (with voice-over), and Claude converts the recording into a reusable skill — extracting semantic intent rather than replaying clicks, and suggesting API connectors over brittle UI automation.
- **Why it matters:** Direct hit on your SKILL.md-authoring + Cowork focus. This is a second authoring path alongside skill-forge/skill-creator: record Talbot/Populi admin workflows (Campus Life updates, month-end steps) once, get a rerunnable skill. Worth testing against a hand-written SKILL.md for quality.
- **Trust:** Tier 1 (Anthropic-official launch; covered by the-decoder, Android Authority, Dataconomy Jul 21–22).
- **Link:** the-decoder.com/claude-cowork-learns-new-skills-through-screen-recordings-and-voice-over-explanations/

## 2. malskanner — prompt-injection scanner for repos/skills before your agent trusts them
- **What:** `npx malskanner <repo>` scans a repository for hidden prompt-injection; ships as CLI, MCP server, and GitHub Action (Octolabo, created Jul 21, ★4). Claims zero false positives.
- **Why it matters:** You install Tier 3/4 skills and plugins from this very digest — this is the missing pre-install vetting step, and it slots into your GitHub workflow as an Action. Complements /doctor context-audit (07-13) on the safety side.
- **Trust:** Tier 4 — brand-new, unknown author, unaudited claims; ironically, vet the vetter before wiring it in.
- **Link:** github.com/Octolabo/malskanner

## 3. skillbench + skill-receipts — the "prove your skill works" wave
- **What:** Two independent day-old repos with the same thesis: skills should ship with benchmarks. currenjin/skillbench runs a weekly public-log benchmark of agent skills against a no-skill baseline; sjh9714/skill-receipts publishes skills only if they beat baseline AND placebo, and publishes the rejects.
- **Why it matters:** For your skill/plugin curation this is the evaluation discipline the official skill-creator evals (surfaced 06-20) pointed at, now appearing community-side. The baseline-vs-placebo framing is a useful bar for your own skill-forge output — does the skill actually change results?
- **Trust:** Tier 4 — both created Jul 22, ★0; watch the pattern more than the repos.
- **Links:** github.com/currenjin/skillbench · github.com/sjh9714/skill-receipts

## 4. symaira-brain — portable agent-context layer behind one MCP gateway
- **What:** Multiplexes a secrets vault, persistent memory, and skills behind a single MCP gateway so the same context follows you across coding harnesses (Claude Code, Cursor, etc.). Created Jul 21, ★1.
- **Why it matters:** Squarely your "agentic context setup, not one-shot prompts" lane — an architecture sketch for context that outlives a session/tool, adjacent to claude-mem (07-13) and subagent memory (06-28) but cross-harness and secrets-aware.
- **Trust:** Tier 4 — day-old, unvetted; a vault behind an MCP gateway is exactly where you want a security review first. Read as reference architecture, don't feed it credentials.
- **Link:** github.com/danieljustus/symaira-brain

## 5. claude-oss-skills — resource-efficient OSS-development runbooks
- **What:** Practical Claude Code runbooks covering plan → implement → debug → review → release for clean open-source development (olgaiv39, created Jul 21, ★8 in a day — notable early traction for this window).
- **Why it matters:** Maps to your GitHub-workflow domain and to shipping Plumbline with discipline; "resource-efficient" runbooks also align with keeping agent sessions cheap. Lighter-weight alternative to the big SDLC bundles (addyosmani 07-06).
- **Trust:** Tier 3/4 — individual author, but readable runbooks you can audit before adopting.
- **Link:** github.com/olgaiv39/claude-oss-skills

---
_Near-misses went to skipped-log (Claude Code 2.1.212–217 security-hardening bundle, multimodels-mcp, aiskillstore marketplace, homespun, TipRanks MCP)._
