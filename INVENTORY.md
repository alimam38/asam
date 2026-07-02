# Master Initiative Inventory — v0.3 (asam edition)
Date: 2026-07-02 (baseline corrected with Ali, 2026-07-02) · Owner: Ali · Status legend: 🟢 active · 🟡 paused/pending decision · 🔴 blocked · ⚪ proposed, not started · 🔍 needs a review session

> Purpose: single file listing everything in flight, one line of truth each. This is the root index of the **asam** repo. Each initiative has a `STATUS.md` in its home directory (map below); a weekly sweep job (`Open Items/Claude Workspace/SWEEP.md`) keeps both layers honest. Items marked **[?]** need your correction or confirmation — my picture has a recency bias and may be stale.

---

## A. Turner Theological Seminary (institutional role)

| # | Initiative | Status | Current state / next action |
|---|-----------|--------|------------------------------|
| A1 | **Plumbline** (Populi + QuickBooks analytics) | 🟢 | OAuth credentials secured; five-layer architecture locked (Integration / Normalization / Metrics / Presentation / Auth), TypeScript/Next.js. Target: one source of truth before August for SACSCOC/TRACS/ATS. Confirmed 2026-07-02: **no build code yet — prototypes/probes only.** Next: first build session against `specs/plumbline/spec-v2.md`; decide then how much of the president-view prototype carries over. |
| A2 | **Talbot Hall — Populi Campus Life build** | 🟡 | Cowork session **ran partially** (confirmed 2026-07-02). Dependency chain (room inventory → term assignments → rate binding → semester invoice → cohort flag) incomplete. Next: audit Populi to establish exactly which steps are done, then finish the chain. |
| A3 | **Talbot Hall — replacement housing tracker (Excel)** | 🟡 | Seven-sheet governed workbook delivered and in use, but **needs revision** (confirmed 2026-07-02; scope of revision TBD). |
| A4 | **FY-end QuickBooks review / three-way reconciliation** | 🟡 | QB vs. bank vs. Givelify/Authorize.net; unapplied-transaction diagnosis **paused** as of 2026-07-02. Next: pick a resume date or hand off. |
| A5 | **Grant management & proposal assembly system** | 🟡 | Designed with Kindora + Granted connectors in scope; not built. |
| A6 | Shipped one-offs (SACSCOC press companion, GEMA/HS FPC application, bridge-loan pro forma, move-in reservation form, apparel line concept) | ✅ | Delivered. Candidates for the sunset/transfer/keep classification below. |

## B. Eden Intelligence Group / Meridia (product & IP)

| # | Initiative | Status | Current state / next action |
|---|-----------|--------|------------------------------|
| B1 | **AIA methodology + corpus** (EIG-CORPUS-2026-001) | 🟡 | Schema built on NAS PostgreSQL; **Cataloger pipeline ready but Dropbox ingestion never run.** This is the second unclosed cataloging thread. |
| B2 | **Hypomone** (Meridia member platform) | 🟡 | MVP scope locked: membership first, lending step 2/3; The Charter intake; governance gate in code; event/ledger PostgreSQL spine. Capital pathway: Keena Pierre; Andre still uncertain. **No movement since scope lock** (confirmed 2026-07-02). Next: sequence the first build milestone. |
| B3 | **WayPoint product suite** (Core, Crown's Eye, Integra, Crown, Edge) | 🟡 | Proof cases of the methodology. Hard gate: nothing external before relevant provisional patent files. |
| B4 | **Provisional patents ×3** (FPS, Trust Index, governance-not-guardrails) | 🔴 | **None filed** (confirmed 2026-07-02). Gates all external product motion. |
| B5 | **Recess** (Crown's Eye education, Shadow Rock pilot) | 🟡 | Shared Cowork environment configured; FERPA + conflict-of-interest governance flagged as live constraints. |
| B6 | **AI integration consulting agency + white-label platform** | ⚪ | NEW (this thread). Decision made: consult-while-building; retain reusable IP contractually. Sequencing: Anthropic Academy → one live Tier 2–3 client deployment → partner network application. |

## C. Infrastructure & meta-work

| # | Initiative | Status | Current state / next action |
|---|-----------|--------|------------------------------|
| C1 | **Consolidation layer (Option A: repo + scheduled librarian agent)** | ⚪ | Proposed. This file is its first artifact. Next: create repo, one directory per initiative above, STATUS.md each, recurring sweep agent. |
| C2 | **Dev-machine preflight / repo scaffolding / gate system** | 🟡 | Preflight → scaffold → spec pattern established; Cowork HQ queued as "station five." Gate ledger **unreconciled** — Ali unsure which gates have closed (2026-07-02); Cowork-Master hub created partly to fix this. Next: one pass through `GATES.md` marking each gate closed/open with evidence. |
| C3 | **Skill library** (/48, /f5, skill-forge, verified-roster, Daily Skills Scout, catalog triage job) | 🟢 | Operational. Triage cadence: on model release + monthly. |
| C4 | **NAS platform** (Synology DS925+, PostgreSQL, Docker, 24 endpoints, Index8 frontend) | 🟢 | Live. Hosts corpus + Hypomone spine. |
| C5 | **Turner sunset/transfer/keep decommission** | ⚪ | Decision made in principle (this thread): controlled decommission with written notice; some items retained privately as portfolio proof cases. Next: classify every A-item above. |

## D. Personal / financial context items

| # | Item | Status |
|---|------|--------|
| D1 | GA unclaimed property claim (~$18K) | 🔴 **Not yet filed** (confirmed 2026-07-02). Next: file the claim. |
| D2 | Cloud credits (~$600K potential) | 🔍 Origin unclear to Ali (2026-07-02) — needs a review to reconstruct what this referred to before keeping it on the list. |
| D3 | Certifications track (Anthropic Academy, optional AWS AI Practitioner) | ⚪ Not started |

---

## Open decisions (the short list that unblocks the most)

1. **Run the Dropbox corpus ingestion or fold it into C1?** The Cataloger has sat ready for months — either run it or explicitly park it so it stops being ambient debt.
2. **A-item classification (C5):** keep / transfer / retire, with dates, for every Turner deliverable.
3. **First consulting client** for B6 — who is the discounted reference deployment?
4. **Patent filing order** — B4 gates everything external.
5. **Disposition review session (queued 2026-07-02):** three initiatives need a worked-through, recorded outcome rather than a one-line answer — **Aegis** (live vs. absorbed into Meridia/integra-core