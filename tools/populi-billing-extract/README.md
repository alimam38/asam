# Populi billing extract

Pulls Populi's posted financial transactions for a date range, expands each to its ledger
entries, and aggregates **net credit-to-income by account × month** — the *Populi side* of
the Populi → QuickBooks reconciliation. Output mirrors the QBO
`Turner-FY26-Revenue-Reconciliation` workbook so the two reconcile **by account name**
(Populi and QBO account numbers diverged after the QB restructuring).

The default date range is the full fiscal year (2025-07-01 .. 2026-06-30), so a plain run
produces all of FY26.

## One-time setup

The script needs your Populi API key (the same `sk_…` the Populi connector uses). Put it in a
local `.env` once so you never type it again:

```
cd tools/populi-billing-extract
cp .env.example .env            # PowerShell: Copy-Item .env.example .env
# open .env and paste your key into POPULI_API_KEY
pip install -r requirements.txt
```

`.env` is gitignored — the real key never leaves your machine or enters the repo.

## Run in Claude Code (recommended)

Open the `asam` repo in Claude Code and ask it to run the extract, e.g.
*"run the Populi FY26 billing extract."* Claude Code reads the key from `.env`, runs the
script, and reports the output path — nothing is typed at a prompt. This is the durable home
for the tool: same repo, version-controlled, re-runnable every close.

## Run from a terminal (no setup beyond the key)

The script auto-loads `.env`, so once it's filled in:

```
python extract.py
```

Or, without a `.env`, pass the key inline for a single run (PowerShell):

```powershell
$env:POPULI_API_KEY = "your sk_… key"
$env:POPULI_SCHOOL  = "turnerseminary"
python extract.py
```

Optional env: `POPULI_FY_START`, `POPULI_FY_END`, `OUT`.

It pulls the chart of accounts, every posted transaction in the range (~860 for a full year),
and each transaction's ledger entries (~one API call per transaction; it backs off
automatically on HTTP 429). A full run is a few minutes and prints progress.

## Where the output goes

Output lands as `populi-revenue-by-account.xlsx` in this folder. **Move it into the Dropbox
finance lane** next to `Turner-FY26-Revenue-Reconciliation.xlsx` — it's live client financials,
and it's gitignored so it never lands in the repo. Then diff the two **by account name**.

## How it reconciles to QBO

- Diff by **account name** against the QBO revenue workbook.
- **Housing (resolved 2026-06-21):** Populi account `41064-01 Auxiliary Enterprise Revenue -
  Housing Rentals` now matches QBO on both number and name, so housing lines tie directly.
- Expect housing / Spelman / CORT revenue to be **larger in QBO than Populi** — much of it is
  billed/booked directly in QBO, not through Populi student billing. The variance is the point.

## Notes

- Revenue = net credit to income accounts; customer **payments** (which credit A/R) are excluded
  automatically. Scholarship/contra accounts are included so gross-vs-aid is visible.
- Validated against live July 2025 data (2026-06-21): the 6 income-crediting transactions netted
  to $300 of application fees; the 17 customer payments correctly contributed $0.
- Read-only against Populi; writes only the local `.xlsx`.
- Verified API path: `GET /transactions?posted_date_start=&posted_date_end=` then
  `GET /transactions/{id}` with `expand=["ledger_entries"]`; `GET /accounts` for the name map.
