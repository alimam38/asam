# STATUS — Hypomone (Meridia member platform)

**State:** 🟡 Promoted to active build (focus, 2026-08-02) — first build commit not yet landed
**Last reviewed:** 2026-08-03 (sweep — 08-02 focus promotion noted; no build artifacts yet)

## Where things live in this repo
- Spec: `specs/hypomone/spec-v1.md`
- Working docs: `docs/asam/hypomone/` (Charter v2, market reads, naming & architecture, founding-member survey, Keena cover note)
- Duplicate drafts also in `Open Items/Hypomone/` — candidates for cleanup (single home)

## Current state
- MVP scope locked: membership platform first, lending step 2/3; The Charter as structured intake; governance gate enforcing reflective-only clarity-loop output in code; event/ledger-as-spine PostgreSQL on NAS/Docker.
- Model policy: Claude primary, Gemini secondary, OpenAI excluded by configuration.
- Capital pathway: Keena Pierre (Prep Capital / Erez Capital), offered active participation. Andre status still uncertain (confirmed 2026-07-02).

## Open decisions
1. Build start date relative to Plumbline (which owns the August deadline).
2. Consolidate `Open Items/Hypomone/` into `docs/asam/hypomone/` — keep one home.

## Next action
- First build commit against `specs/hypomone/spec-v1.md` (Gate-1 Charter build) — or an explicit sequencing call vs. Plumbline (open decision #1).

## 2026-07-15 — Build-input sourcing reviewed (fork sweep)
Ali forked ~54 fintech/lending repos on 2026-07-14. Reviewed against `specs/hypomone/spec-v1.md`.
**Correction to first read:** most of that sweep (credit-repair, loan-origination, underwriting,
core-banking, ledger) serves **Gate 3+ — Hypomone Capital, the regulated lending institution** —
which is Gate-0-blocked on legal/licensing (spec §10, item 1). It is **not** input to the actual
Gate-1 build, which is **The Charter** (compliance-safe intake instrument, §4).

**Shortlist for the Gate-1 Charter build** (§9: self-hosted, owned, exportable, phone-first):
- **supabase** (starred) — Postgres + auth + instant API + export → covers the data model
  (`respondent` / `charter_response` / `charter_member` / `referral` / `consent`, §6) and the
  "exportable & owned, never vendor-locked" rule. Strongest candidate for the self-hosted path.
- **coolify** (starred) — self-hostable PaaS on the NAS/Docker → deployment target; keeps standup
  under the §9 one-week bar that decides self-hosted vs. Typeform.
- Phone-first form UI from the design-layer forks (`typeui` / `uilayouts`).

**Parked (correctly) until §10 item 1 counsel review** — the Gate-3+ lending stack:
`core-banking-prototype-laravel`, `formancehq/ledger`, `multi-agent-loan-origination`, and the
underwriting/credit forks. Real assets, wrong gate for now.

## 2026-08-02 — Promoted to active build in current-focus (sweep note)
Ali promoted Hypomone to **active build** in `Open Items/Claude Workspace/Context/current-focus.md`
(commit `49e2b35c`, "focus v3: promote Hypomone to active build"). As of the 2026-08-03 sweep
**no build artifacts have landed** — nothing changed under `src/`, `specs/hypomone/`, or
`docs/asam/hypomone/` since the 2026-07-15 fork-sweep note — so the state emoji stays 🟡 until the
first build commit. Open decision #1 (build start relative to Plumbline) is now live rather than
hypothetical: both ventures are queued for the same build capacity and Plumbline's "before August"
target has arrived with no build code on either side. (sweep-reconciled 2026-08-03)
