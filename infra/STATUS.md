# STATUS — Infrastructure (NAS platform)

**State:** 🟢 Live (local) — ⚠ cloud access path down since 2026-07-23
**Last reviewed:** 2026-08-10 (sweep)

## Where things live in this repo
- `infra/meridia/` — Dockerfile, docker-compose.yml, NAS deployment guides, EIG-CORPUS-2026-001 deployment guide, env template
- Nightly cloud connectivity snapshots: `Open Items/Claude Workspace/Outputs/meridia-core/`

## Current state
- Synology DS925+ live: PostgreSQL, Docker, 24 backend endpoints, Index8 frontend. Hosts corpus schema and will host the Hypomone event/ledger spine.
- ⚠ **Cloud → NAS access path still failing — 15 failed nightly runs spanning 2026-07-23 → 2026-08-09, all `websocket: bad handshake`.** The snapshot job has no runs for 2026-08-05 → 08-07 (all scheduled jobs were dark 08-06/08-07), so the true streak may be longer. No DB data has been read since the nightly job began.
- **Diagnosis revised by the 2026-08-04 and 2026-08-09 snapshots:** DNS resolves to the Cloudflare edge and the handshake is rejected **at the Cloudflare Access/edge layer before reaching the NAS** — pointing at the **service token** (expired, revoked, or not included in the Access policy) or the `db.meridiahq.com` Access app config, **not NAS-side routing**. This supersedes the 2026-07-26 "no healthy tunnel origin / connector down" read (edge probe returned 502); the two reads should be adjudicated when the fix is attempted. (sweep-reconciled 2026-08-10)

## Open decisions
- None — but the operational action (pending since 2026-07-27) is now two-sided: (1) Cloudflare Zero Trust → Access → Service Auth: confirm the service token exists, is unexpired, and its Client ID matches Dropbox `/Claude/.env`; confirm the `db.meridiahq.com` Access application has a Service Auth policy that includes this token; confirm the hostname is still routed to the tunnel. (2) On the NAS: confirm the cloudflared connector container/service is running and connected (`cloudflared tunnel info`, or Zero Trust dashboard → Tunnels → connector status).

## Next action
- Check the Access service token/policy first (per the latest snapshots), then the NAS-side connector; the next nightly snapshot (≈12:40 UTC) verifies the fix. Worth doing before the next Hypomone or corpus session, both of which need this path.
