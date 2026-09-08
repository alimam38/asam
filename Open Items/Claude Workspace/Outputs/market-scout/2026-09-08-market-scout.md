# Market scout — 2026-09-08 (Tue run, covers Sat Sep 5 – Mon Sep 7)

_Sources this run: GitHub topic searches (Composio, authenticated), HN Algolia, SerpAPI (4/6 calls: Google News + 2× X site-search + 1× 24h news), vercel-labs/skills release radar, Claude Code CHANGELOG. Readwise Reader: no new saves since Sep 4 — skipped. Note: yesterday's run (Sep 7) already covered the Fable 5.1 launch wave, so this digest is the residue after that filter — a lighter weekend, ranked accordingly._

## Ranked picks

### 1. trailofbits/coop — isolated VM environments for running Claude Code and Codex
**Link:** https://github.com/trailofbits/coop · [HN thread](https://news.ycombinator.com/item?id=49593842) (~61 pts Sep 7)
Trail of Bits (a serious security shop, not a star-farmer) shipped an open tool that runs each coding-agent session inside its own disposable VM instead of on your host. Same problem Docker Sandboxes (seen 08-12) attacks, but VM-grade isolation and agent-CLI-aware out of the box.
**Why it matters to Ali:** you run scheduled agents against real credentials (Populi, QuickBooks, Meridia DB) from a NAS/Docker stack. This is the current best-practice answer to "what if a skill or MCP server goes hostile" — and it's from a vendor whose threat model you can trust.

### 2. OKF (Open Knowledge Format) ecosystem wave — a standard forming around agent memory/knowledge
**Links:** [okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory) (478★ in 3 days; surfaced yesterday, now accelerating) · [Albertchamberlain/Awesome-OKF](https://github.com/Albertchamberlain/Awesome-OKF) (new curated catalog, 102★ in 1 day)
The "Google OKF v0.2" spec for git-native agent knowledge is sprouting an ecosystem — implementations, awesome-lists, MCP bridges — the same repo-plus-satellites pattern the DeepSeek Harness wave showed in August. Watch whether it's real adoption or wave-riding; the lead implementation (Go, BM25, progressive disclosure, 80% token-bloat claim) at least has a real artifact.
**Why it matters to Ali:** your whole hub design (OS files, seen indexes, repo-as-memory) is hand-rolled OKF. If a standard wins here, aligning your file formats to it later gets you free tooling; worth tracking, not yet adopting.

### 3. dhishwasher/Girder — semantic code graph + impact analysis as one static Rust MCP binary
**Link:** https://github.com/dhishwasher/Girder · via GitHub topic search + [HN](https://news.ycombinator.com/item?id=49602848)
Gives coding agents "exactly the code they need instead of whole files": code graph, impact analysis, MCP server, single binary. Same token-economy thesis as Spotify's Portal (seen 09-07) but self-hostable and tiny. Brand new, low stars — artifact looks real, judge after a week.
**Why it matters to Ali:** context-token spend is your recurring complaint across scheduled runs; a drop-in MCP that scopes retrieval per query is a cheap experiment on the asam/Plumbline codebases.

### 4. Skills supply chain gets scarier — and gets its first fix
**Links:** grith.ai, ["An agent skill can hand a stranger your shell — hours after you installed it"](https://grith.ai/blog/skill-md-permissions-manifest) ([HN](https://news.ycombinator.com/item?id=49597166)) · [vercel-labs/skills v1.5.24](https://github.com/vercel-labs/skills/releases/tag/v1.5.24) (Sep 6)
The grith.ai piece demonstrates a skill that mutates after install (fetch-at-runtime), arguing SKILL.md needs a permissions manifest. Two days later the main skills CLI shipped commit-SHA-pinned installs — exactly the mitigation. Pairs with the FakeGit/malicious-MCP thread this scout has tracked since July.
**Why it matters to Ali:** you install third-party skills routinely (template-vetting lane exists for this reason). Concrete action: pin external skills to a SHA when installing, and re-vet anything that fetches remote content at runtime.

### 5. hsandhu/mobilecode — opencode fork that builds and previews iOS/Android apps
**Link:** https://github.com/hsandhu/mobilecode (216★ since Sep 5)
An agent harness specialized for mobile: scaffolds, builds, and previews real iOS/Android projects. Alongside NoMac.app (iOS CI/CD for agents, Show HN same weekend), mobile is emerging as the next agent-harness niche.
**Why it matters to Ali:** if Plumbline ever needs a mobile companion (student/parent-facing views), the agent tooling to build one without a mobile team is arriving; a note-for-later, not a now.

## Worth a session this week

**trailofbits/coop (pick 1).** One session: run it on the NAS or a spare box, put one real scheduled job (e.g. sosmon) inside a Coop VM, and compare friction vs. your current Docker setup. You get a concrete answer on whether VM-isolating credentialed agent jobs is practical for your fleet — the highest-value 90 minutes on this list given how much authority your scheduled tasks carry.

## Also noted (one-liners)

- [noskillish/bankmcp](https://github.com/noskillish/bankmcp) — self-hosted, read-only open-banking MCP (Enable Banking, EU-centric); the "AI reads your bank" pattern arriving; US coverage limited.
- [Stormix/transcripts-mcp](https://github.com/Stormix/transcripts-mcp) — search your local Claude Code/Cursor/Codex session transcripts over MCP; cheap institutional memory for past sessions.
- [OpenAI reinstates the 5-hour usage limit for Plus/Business](https://news.ycombinator.com/item?id=49600233) (Tell HN, ~125 pts) — the usage-limits tightening trend is now industry-wide, not just Anthropic (pairs with the limits chatter noted 09-07).
- [dbreunig on Fable 5.1's system-prompt changes](https://www.dbreunig.com/2026/09/07/what-we-can-learn-from-claude-s-fable-5-1-system-prompt.html) — best short read on what actually changed under the hood of the model you're running.
- [fidetolabs/qanat](https://github.com/fidetolabs/qanat) — agent-native DAG workflow engine for building/backtesting trading alphas; the "agent-native workflow engine" shape applied to a vertical, same pattern to expect in higher-ed ops.
- Star-farming watch: the `Alpha-Park`/`alphaparkinc` "genpark-*-skill" flood (~40 near-identical repos, duplicated across two orgs, uniform 8★) — pattern-matched and excluded.

_Seen-index updated; next run Fri (covers Tue–Thu)._
