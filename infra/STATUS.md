# STATUS — Infrastructure (NAS platform)

**State:** 🟢 Live (local) — ⚠ cloud access path down since 2026-07-23
**Last reviewed:** 2026-07-27 (sweep)

## Where things live in this repo
- `infra/meridia/` — Dockerfile, docker-compose.yml, NAS deployment guides, EIG-CORPUS-2026-001 deployment guide, env template
- Nightly cloud connectivity snapshots: `Open Items/Claude Workspace/Outputs/meridia-core/`

## Current state
- Synology DS925+ live: PostgreSQL, Docker, 24 backend endpoints, Index8 frontend. Hosts corpus schema and will host the Hypomone event/ledger spine.
- ⚠ **Cloud → NAS access path failing.** The nightly meridia-core snapshot job (cloud sandbox → `cloudflared access tcp db.meridiahq.com` → NAS Postgres) has failed 4 consecutive runs (2026-07-23 → 07-26) with `websocket: bad handshake`; no DB data has been read since the job began. The 2026-07-26 run narrowed the cause: an edge probe with service-token headers returned **HTTP 502, not 403** — DNS resolves and the edge answers, so the token is not being rejected; there is **no healthy tunnel origin** behind `db.meridiahq.com`. Most likely the cloudflared connector on the NAS is down or disconnected. (sweep-reconciled 2026-07-27)

## Open decisions
- None — but one operational action is pending: on the NAS, confirm the cloudflared connector container/service is running and connected (`cloudflared tunnel info`, or Zero Trust dashboard → Tunnels → connector status).

## Next action
- Restart/reconnect the NAS-side cloudflared connector; the next nightly snapshot (12:40 UTC) verifies the fix.
