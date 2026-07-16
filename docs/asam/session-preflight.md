# ASAM — Session Preflight (environment / capabilities manifest)

Last updated: 2026-07-16. Purpose: document what capabilities the environment needs so **any
session can activate what's missing** without rediscovering it — the environment half of the
Recess "context persistence" fix (pairs with `session-handoff.md`, which holds *work* state).

**Defaults chosen (override anytime):** curated "what's needed," not everything on (leaner, cheaper,
smaller attack surface); secrets live in env vars / the OS credential manager — this file records
their **names and location only, never values.**

## How to use at session start
1. Skim this file + `session-handoff.md`.
2. Run `/plugin` and `/mcp` to see live install/auth status.
3. Activate anything missing per the tables below.

## Plugins (installed — user scope; marketplaces: `claude-plugins-official`, `gitkraken`)
To restore on a fresh machine: `/plugin marketplace add <marketplace>` then `/plugin install <name>@<marketplace>`.

| Plugin | Purpose | Needed for |
|---|---|---|
| `desktop-commander` | local shell/files, persistent processes | general |
| `brightdata-plugin` | web scraping/search MCP (replaces WebFetch/WebSearch) | research, competitive scans |
| `cloudflare` (api/bindings/builds/observability) | Workers, D1, R2, KV, logs | future deploy (NAS alt / edge) |
| `dropbox` | Dropbox file ops MCP | Meridia Cataloger ingestion (B1) |
| `canva` | design gen/export MCP | design layer / agency deliverables |
| `adobe-for-creativity` | Adobe/Firefly MCP | design layer (optional) |
| `runway-api` | video/image gen | KSW / media (optional) |
| `mcp-server-dev`, `claude-code-setup` | build MCP servers; configure Claude Code | tooling |
| `gitkraken-hooks` | git hooks | git workflow |

## Connectors (MCP) — activation + auth
Connectors ship **inside** the plugins above (no standalone `mcpServers` entries). Verify live status with `/mcp`.

| Connector | Auth type | How to activate | Status (verify via /mcp) |
|---|---|---|---|
| `desktop-commander` | none | works out of the box | active |
| `cloudflare-*` | OAuth | `/mcp` → authorize | activate when deploying |
| `dropbox` | OAuth | `/mcp` → authorize | activate for Cataloger |
| `canva` | OAuth | `/mcp` → authorize | activate for design |
| `adobe-for-creativity` | OAuth | `/mcp` → authorize | **needs auth** (non-interactive sessions cannot) |
| `brightdata` | API key | set `BRIGHTDATA_API_KEY`; groups via `&groups=` / `GROUPS=` (see plugin skill) | key required |
| `runway-api` | API key | set Runway API key | key required |
| **LinkedIn** | — | **not configured in this environment.** Add via `/mcp` / `mcpServers` (it currently exists only in Claude Desktop) | absent |

> Non-interactive sessions (cron/headless) cannot run OAuth — authorize connectors once in an
> interactive session; the token then persists.

## Skills in `.claude/skills/` (project — version-controlled, auto-load)
| Skill | What it does |
|---|---|
| `recess-competitive-reverse-engineer` | competitor → Recess comparison + ASG node (Component 06 outward) |
| `roast` | 5-angle adversarial panel → GO/RESHAPE/KILL + cheapest 48h test |
| `dossier` | decision-grade entity diligence (hypothesis-tested) → .docx |
| `capture` | brain-dump → four-section actionable system |

**To add more:** full collection via `/plugin marketplace add alimam38/claude-skills` → `/plugin install`
(brings 345 skills — noisy; cherry-pick). Or sparse-copy a single skill folder into `.claude/skills/`
(how `capture`/`roast`/`dossier` were installed). Candidates on request: `patent` (→ B4 patents),
`arquiteto-de-empresa` (OKF "company-as-code" — heavier, ships Python tools).

## Secrets (names + location only — NEVER values, even in a private repo)
| Secret | Location | Verified |
|---|---|---|
| GitHub token (`x-access-token`) | Windows Credential Manager (git + `gh`) | ✅ working |
| `BRIGHTDATA_API_KEY` | env var | set when using Bright Data |
| Runway API key | env var / `/mcp` config | set when using Runway |
| Connector OAuth tokens | managed by `/mcp` (OS keyring) | per-connector |

## Permissions (`.claude/settings.json`)
Allow-list covers git, common Bash, WebSearch/WebFetch, Edit/Write, `date`, `mkdir`, `curl`,
`WebFetch(domain:southatlantadistrict-ame.org)`. Broaden via `/permissions` as new tools recur.

## Preflight checklist
- [ ] Repo is **private** (sensitive Meridia/Recess/Turner IP). Confirm: `gh repo view alimam38/asam --json visibility`.
- [ ] `/plugin` shows the plugins above installed.
- [ ] `/mcp` shows the connectors you need for *this* session authorized.
- [ ] `.claude/skills/` holds the four skills above.
- [ ] For Recess-adjacent work: load `specs/recess/2026-05-24-recess-framework-package-2026.md` + the governance spine first (CL-004/007).
