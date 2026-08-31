# STATUS — Infrastructure (NAS platform)

**State:** 🟢 Live (local) — ⚠ cloud access path down since 2026-07-23
**Last reviewed:** 2026-08-31 (sweep)

## Where things live in this repo
- `infra/meridia/` — Dockerfile, docker-compose.yml, NAS deployment guides, EIG-CORPUS-2026-001 deployment guide, env template
- Nightly cloud connectivity snapshots: `Open Items/Claude Workspace/Outputs/meridia-core/`

## Current state
- Synology DS925+ live: PostgreSQL, Docker, 24 backend endpoints, Index8 frontend. Hosts corpus schema and will host the Hypomone event/ledger spine.
- ⚠ **Cloud → NAS access path still failing — 30 failed nightly runs spanning 2026-07-23 → 2026-08-31, all `websocket: bad handshake`** (17 through 08-17 per the prior count, plus 13 dated snapshots 08-18 → 08-31; the job produced no snapshot on 08-29 and was dark 08-11 → 08-16 and 08-05 → 08-07 earlier). The nightly cadence has otherwise been steady at ≈12:40 UTC since 08-18. No DB data has been read since the nightly job began. (sweep-reconciled 2026-08-31)
- **Diagnosis (revised again by the 08-23 → 08-31 snapshots): the service token is valid; the fault is NAS-side.** Every snapshot since 08-23 runs a differential probe against `db.meridiahq.com`: HTTPS **without** the service token → `403` (Access enforcing), **with** the token → `502` from `server: cloudflare`. Access is therefore accepting the token; the 502 is the Cloudflare edge reporting **no healthy tunnel connector** to hand the request to — i.e. the `cloudflared` connector on the NAS is down, not registered for the `db.meridiahq.com` public hostname, or its route to `192.168.0.160:5433` is misconfigured (consistent with cloudflared in Docker without host networking, or the container stopped). This **supersedes the 2026-08-04/08-09 "Access service token / policy" read** and re-aligns with the original 2026-07-26 "no healthy tunnel origin / connector down" read. History of reads: 07-26 connector-down (502) → 08-04/08-09 Access token/policy → 08-23+ token valid, connector-down. Adjudicate at the fix.

## Open decisions
- None — the operational action (pending since 2026-07-27) is now pointed at the NAS side first: (1) On the NAS: confirm the cloudflared tunnel connector container/service is running and connected — Zero Trust → Networks → Tunnels shows a HEALTHY connector, and `db.meridiahq.com` → `tcp://192.168.0.160:5433` is in the tunnel's public-hostname routes; restart the container if stopped; confirm it can reach `192.168.0.160:5433` from inside its network namespace. (2) Only if the connector is healthy: re-check Cloudflare Zero Trust → Access → Service Auth (token unexpired, Client ID matches Dropbox `/Claude/.env`, `db.meridiahq.com` Access app has a Service Auth policy including it).

## Next action
- Restart/verify the NAS-side cloudflared connector (per the 08-23 → 08-31 snapshots the token is not the problem); the next nightly snapshot verifies the fix. While in the scheduler, note that the weekly sweep skipped 08-24 and meridia-core skipped 08-29. Worth doing before the next Hypomone or corpus session, both of which need this path.
