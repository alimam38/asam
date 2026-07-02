# STATUS — Meridia / Eden Intelligence Group (AIA methodology, corpus, IP)

**State:** 🟡 Infrastructure live; ingestion and patents stalled
**Last reviewed:** 2026-07-02

## Where things live in this repo
- Strategy & mandates: `docs/meridia/` (system mandate v1, architecture overview, 90-day calendar EIG-CAL-2026-001)
- Reports: `docs/meridia/reports/` (MCR-2026-001, signal reports, cognitive state)
- Research: `docs/meridia/research/` (TAM, competitive landscape, data feeds)
- Corpus schema: `specs/meridia/EIG-CORPUS-2026-001_AIA_Corpus_Schema.sql`
- Cataloger: `src/meridia/services/aia_cataloger.py`
- Platform code: `src/meridia/integra-core/` (FastAPI app, trust_index.py, FRED/FDIC/HMDA/census loaders)
- NAS deployment: `infra/meridia/` (Dockerfile, docker-compose, deployment guides)
- Company docs: `docs/company/` (Meridia Holdings LLC formation, operating agreement)

## Current state
- NAS (Synology DS925+) live with PostgreSQL; corpus schema built; Cataloger pipeline ready.
- **Dropbox ingestion never run** — the oldest unclosed thread. Years of architecture docs waiting.
- Provisional patents ×3 (FPS, Trust Index, governance-not-guardrails): planned, **none filed** 🔴. Gates all external product motion.

## Open decisions
1. Run the Dropbox corpus ingestion, or explicitly park it (stop carrying it as ambient debt).
2. Patent filing order — this gates WayPoint and everything external.

## Next action
- Decide #1. If run: schedule one Cowork session against `aia_cataloger.py` + the deployment guide. If park: mark parked here with a revisit date.
