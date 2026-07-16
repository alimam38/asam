# STATUS — Hypomone (Meridia member platform)

**State:** 🟡 MVP scope locked; awaiting build start
**Last reviewed:** 2026-07-02

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
- Confirmed 2026-07-02: **no movement since scope lock.**

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