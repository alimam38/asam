# STATUS — Infrastructure (NAS platform)

**State:** 🟢 Live (local) — ⚠ cloud access path down since 2026-07-23
**Last reviewed:** 2026-08-03 (sweep)

## Where things live in this repo
- `infra/meridia/` — Dockerfile, docker-compose.yml, NAS deployment guides, EIG-CORPUS-2026-001 deployment guide, env template
- Nightly cloud connectivity snapshots: `Open Items/Claude Workspace/Outputs/meridia-core/`

## Current state
- Synology DS925+ live: PostgreSQL, Docker, 24 backend endpoints, Index8 frontend. Hosts corpus schema and will host the Hypomone event/ledger spine.
- ⚠ **Cloud → NAS access path still failing — 11 consecutive nightly runs (2026-07-23 → 2026-08-02), all `websocket: bad handshake`.** The 2026-07-26 diagnosis stands: an edge probe with service-token headers returns HTTP 502 (not 403), so DNS resolves and the token is accepted, but there is **no healthy tunnel origin** behind `db.meridiahq.com` — the NAS-side cloudflared connector is most likely down or disconnected. The restart/reconnect action flagged by the 2026-07-27 sweep has not yet been done (or has not worked); no DB data has been read since the nightly job began. (sweep-reconciled 2026-08-03)

## Open decisions
- None — but the operational action from 2026-07-27 is still pending: on the NAS, confirm the cloudflared connector container/service is running and connected (`cloudflared tunnel info`, or Zero Trust dashboard → Tunnels → connector status).

## Next action
- Restart/reconnect the NAS-side cloudflared connector; the next nightly snapshot (≈12:40 UTC) verifies the fix. Now 11 nights failed — worth doing before the next Hypomone or corpus session, both of which need this path.
