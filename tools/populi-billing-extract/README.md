# Populi billing extract

Pulls Populi's posted financial transactions for a date range, expands each to its ledger
entries, and aggregates **net credit-to-income by account × month** — the *Populi side* of
the Populi → QuickBooks reconciliation. Output mirrors the QBO
`Turner-FY26-Revenue-Reconciliation` workbook so the two reconcile **by account name**
(Populi and QBO account numbers diverged after the QB restructuring).

## Run

Same token/env as the `populi-connector` (the key lives only in your environment, never in code):

```
pip install httpx openpyxl
POPULI_API_KEY=sk_xxx POPULI_SCHOOL=turnerseminary python extract.py
```

Optional env: `POPULI_FY_START` (default `2025-07-01`), `POPULI_FY_END` (default `2026-06-30`),
`OUT` (default `populi-revenue-by-account.xlsx`).

It pulls the chart of accounts, every posted transaction in the range, and each transaction's
ledger entries (~one API call per transaction — a few hundred for a full year; it backs off
automatically on HTTP 429). Then it writes one sheet: revenue accounts (income + scholarship/
contra) × month + FY total.

## How it reconciles to QBO

- Diff by **account name** against the QBO revenue workbook.
- **Housing:** Populi credits acct `40005-01 Auxiliary Enterprise Revenue` — rename its *name*
  in Populi to match QBO `41064-01 Auxiliary Enterprise Revenue - Housing Rentals`.
- Expect housing / Spelman / CORT revenue to be **larger in QBO than Populi** — much of it is
  billed/booked directly in QBO, not through Populi student billing. The variance is the point.

## Notes

- Revenue = net credit to income accounts; customer **payments** (which credit A/R) are excluded
  automatically. Scholarship/contra accounts are included so gross-vs-aid is visible.
- Read-only against Populi; writes only the local `.xlsx`.
- Verified API path (2026-06-21): `GET /transactions?posted_date_start=&posted_date_end=` then
  `GET /transactions/{id}` with `expand=["ledger_entries"]`; `GET /accounts` for the name map.
