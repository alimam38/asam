# Plumbline — QBO Financials mapping & findings (Turner)

Date: 2026-06-20. Source: live QuickBooks Online (read-only) for **Turner Theological Seminary, Inc**
(NAICS 611310), plus the Turner R-14 / CFI workbooks in `docs/clients/turner/financial-analysis/`.
The QBO connector is already authenticated to Turner — no new credentials needed.

## Live now (President's View → Financial position panel)
From the QBO Balance Sheet `summary` on each open (as of the run date): cash on hand, A/R (GL),
working capital, current ratio. Plus an annual **Financial responsibility** trend (R-14, CFI) from
audited financials — not live.

## KPI → account mapping (verified against the live P&L; pull was calendar-YTD 2026-01-01..2026-06-20)

Revenue:
| KPI input | Account(s) — amount (cal-YTD) |
|---|---|
| Gross tuition | 40003-01 Tuition – Graduate $353,400 (= 40003.1-01 MDiv); 40004-01 Continuing Ed $300 |
| Fees | 40006-01 Comprehensive Fees $24,095 |
| Institutional aid (contra) | 40007-01 Institutional Aid ≈ −$353,650 (incl. 40008.5-01 Rufus Lee −$64,350) |
| Net tuition & fees | 40002-01 Tuition and Fees, Net $24,145 |
| Auxiliary / housing | 41060-01 Auxiliary Enterprise Revenue (group $657,443): 41064-01 Housing Rentals $83,800; 41061 Facility Rentals $11,000; 41062/41063 Housing Deposits; 41065 Amenities $0; 41066 Noncompliance $402,725 (see flag); 41069 Furniture Lease/CORT $154,992; 41070 Product Sales $480 |
| Restricted scholarship revenue | 42020-02 group $6,288: 42035-02 Book; 42038-02 Academic & Leadership |

Balance sheet (as of 2026-06-20):
- Cash **$12,804.15** (bank accounts incl. Talbot Hall 7082 $1,200, PNFP Main $9,408).
- A/R **$591,052.16** — Students $54,066.30, Facility Rentals $11,063.50, Housing Rentals $801.36, uncategorized A/R control $525,121.
- Current liabilities $1,145,233.34 incl. a **$982,663 PNFP line of credit** booked under Credit Cards.
- Working capital **−$541,352**; current ratio **0.53**; debt-to-equity 0.80. Equity $1,430,704 (net assets $330,110 with-donor-restriction, $359,805 without).

Expenses (cal-YTD): total **$804,747.85**; net income **$155,963.15** (income $960,711 − expenses).
Largest line: 50000 Salaries & Wages $356,431.60 (~44%). NOTE: the saved P&L snapshot truncated at
100 rows — non-payroll expense detail needs a re-pull.

## Financial responsibility (annual, from audited workbooks)
- **DOE R-14 composite** (Primary Reserve 40% ×10; Equity 40% ×6; Net Income 20% scaled; band −1..3): FY2024 **1.67** → FY2025 **0.63** (governing auditor figure; earlier client draft 0.55). Both "Acceptable".
- **CFI** (Salluzzo/KPMG-Prager, no-debt; Primary Reserve ×0.55÷0.133, Net-Income ×0.15÷0.007, Return-on-Net-Assets ×0.30÷0.02; Viability blank — no LT debt): FY2023 22.64 → FY2024 **1.39** → FY2025 **−5.42**.
- NOTE: the spec's "CFI and its four ratios" is really **three** active ratios (Viability N/A with no debt) — update the definitions registry.

## What didn't work / what's not clear (needs Aliman / Controller)
1. **A/R aging ≠ GL.** QBO A/R Aging total = $1,660,833 (97.9% "overdue"; 1–30 bucket $1,503,696) vs balance-sheet A/R $591,052 — a $1.07M gap. Aging is held off the dashboard until reconciled.
2. **Net tuition / discount rate.** Net tuition & fees $24,145 against ~$377,795 gross implies a ~93% discount — implausible at face value. Pull is calendar-YTD, not fiscal (FY ends Jun 30), and depends on how institutional aid (40007-01) is booked. Needs a fiscal-year pull + Controller confirmation before display.
3. **Budget vs. actuals.** The QBO connector exposes no budget endpoint. The approved FY26 budget lives in a PDF (`Facilities/02 Financial Management/Budget & P&L`). Comparison needs that parsed or a budget feed.
4. **Housing GL crosswalk.** Populi room plans were posted to "40005-01 Auxiliary Enterprise Revenue", but QBO's housing-rental account is **41064-01** (parent 41060-01). 40005-01 does not appear in QBO's revenue accounts — confirm the crosswalk so Populi housing ties to QBO.
5. **41066-01 "Housing Rentals – Noncompliance" = $402,725 YTD** — outsized vs $83,800 actual housing rentals; likely a catch-all / posting to review.
6. **QBO P&L tool quirk.** Top-level totalIncome/totalExpenses/netIncome return 0; real figures live in the report rows (grossProfit holds total income). Plumbline reads the rows, not the scalars.

## Phasing
- Live now: cash, A/R (GL), working capital, current ratio; R-14/CFI trend (annual).
- Phase 1: fiscal-year P&L pull → net tuition, discount rate, days-cash, expense ratios; A/R aging after reconciliation; budget feed; continuous CFI from mapped inputs; Gusto payroll.

## 2026-06-21 — fiscal-year P&L update (FY26-to-date, 2025-07-01 → 2026-06-20)

Re-pulled the P&L on Turner's fiscal year (ends June 30) to settle the calendar-YTD flags.

**Net tuition & discount rate — the ~93% was REAL** (≈ **90%** on the fiscal year; it's the actual model, not an artifact).
- Gross tuition & fees ≈ **$840,765** — Graduate/MDiv $708,380; Continuing Ed $82,307 (CIT $49,832, LLMV $14,175, CWJ $18,000); Comprehensive fees $50,028 (Technology $25,200, Admin $12,600, etc.).
- Institutional aid (40007-01) = **−$753,800** — President's ELEV8 Scholarship (MDiv) −$597,400; Rufus Lee Memorial −$111,150; President's Global ELEV8 (CIT/Other) −$45,250.
- **Net tuition & fees (40002-01) = $87,140 → discount rate ≈ 90%** (753,800 ÷ 840,765), driven by the President's ELEV8 Scholarship. Tuition is almost entirely scholarshipped — a real, headline institutional metric; belongs on the President's view, clearly labeled.

**Auxiliary is the dominant revenue (~$1.90M fiscal-YTD); housing rentals (41064-01) = $1,246,954.** The $83,800 seen earlier was only the Jan–Jun slice. Total income (gross profit) = $2,538,561 fiscal-YTD. Auxiliary is inflated by pass-throughs (CORT furniture lease 41069 = $228,366 in/out).

**Housing GL crosswalk — confirmed broken.** Populi room plans post to "40005-01 Auxiliary Enterprise Revenue", but in QBO **40005-01 = "Tuition – Special Programs"** (a tuition account; $50 fiscal-YTD). Housing belongs in **41064-01**. The Populi GL code must be corrected to 41064-01 or housing will mis-post to a tuition line.

**Days-cash still needs the Controller's call.** Cash is genuinely tight ($12,804; working capital −$541K), but a clean "days cash on hand" needs operating expense NET of pass-throughs (CORT furniture, housing re-bills); on gross expense it would understate liquidity. Define the opex basis and it can be computed.

**Open for the Controller:**
1. Operating-expense basis for days-cash (net of CORT/housing pass-throughs?).
2. 41066-01 "Housing Rentals – Noncompliance" $402,725 — real, or a posting to review?
3. Fix the Populi housing GL: 40005-01 (a QBO *tuition* account) → 41064-01.
