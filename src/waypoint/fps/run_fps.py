"""Run the FPS GPS engine on a realistic misbanked borrower and render the report."""

from dataclasses import asdict
from datetime import datetime, timezone
import json, os
from fps_gps_engine import (
    Borrower, Property, SubjectLoan, Goal,
    compute_position, vet_product, explain, build_route, append_event,
    PRODUCT_CATALOG, STANDARD_SET_VERSION, METHOD_VERSION,
)

OUT = "/mnt/user-data/outputs"
os.makedirs(OUT, exist_ok=True)
LEDGER = os.path.join(OUT, "ledger.jsonl")

# --- A realistic borrower the conventional DTI box misreads --------------- #
borrower = Borrower(
    borrower_id="BR-10428",
    name="M. Okafor",
    reported_taxable_monthly=3500,           # what a DTI test counts
    schedule_c_net_annual=42000,
    depreciation_addback_annual=18000,
    one_time_writeoffs_annual=6000,
    documented_distributions_annual=36000,
    liquid_reserves=18000,
    credit_score=688,
    tradelines=3,
    monthly_deposits_12mo=[7000,6000,8000,9500,11000,12500,11500,10000,8500,7500,7000,9500],
    properties=[
        Property("Rental A", 360000, 220000, 1500, 2300),
        Property("Rental B", 280000, 164000, 1100, 1700),
    ],
)
subject = SubjectLoan("Subject duplex", 300000, 225000, 2150, 3150)
goal = Goal("Acquire the duplex now, scale to 5 doors, and become conventionally bankable in 24 months.",
            target_doors=5, target_months=24, wants_conventional_bankability=True)

pos = compute_position(borrower, subject, clean_pl_cycles=0)
matches = [vet_product(p, pos) for p in PRODUCT_CATALOG]
reading = explain(pos)
route = build_route(pos, goal)

# --- Write the immutable assurance event ---------------------------------- #
event = append_event(
    LEDGER, borrower.borrower_id,
    inputs={"borrower": asdict(borrower), "subject": asdict(subject)},
    output={"position": asdict(pos),
            "matches": [{"product_id": m.product_id, "qualifies_now": m.qualifies_now} for m in matches]},
)

# --- Console proof -------------------------------------------------------- #
print("POSITION (the read):")
print(f"  DTI sees           ${pos.dti_qualifying_monthly:,.0f}/mo")
print(f"  True cash flow     ${pos.true_monthly_cashflow:,.0f}/mo  ({pos.cashflow_understatement_x}x understated)")
print(f"  Subject DSCR       {pos.subject_dscr}")
print(f"  Reserves           {pos.reserves_months} months")
print(f"  Portfolio LTV      {pos.portfolio_ltv}%   (${pos.equity_available:,.0f} equity available)")
print(f"  Credit / tradelines {pos.credit_score} / {pos.tradelines}")
print("\nVEHICLES:")
for m in matches:
    tag = "QUALIFIES NOW" if m.qualifies_now else "unlocks along route"
    print(f"  [{tag:>20}] {m.name}")
print(f"\nLEDGER event hash: {event['this_hash'][:24]}...  (standard set {STANDARD_SET_VERSION})")

# --------------------------------------------------------------------------- #
# CUSTOMER-FACING GPS REPORT
# --------------------------------------------------------------------------- #

CSS = """
:root{
  --ink:#20231f; --paper:#f4f0e6; --card:#fffdf7; --gold:#946218; --goldsoft:#efe2c4;
  --teal:#0f6e56; --tealsoft:#d8ece4; --clay:#9c4327; --claysoft:#f0ddd2;
  --muted:#6c6a60; --line:rgba(32,35,31,.13);
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--paper);color:var(--ink);font-family:'Newsreader',Georgia,serif;
  font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased;padding:48px 20px 80px}
.wrap{max-width:880px;margin:0 auto}
.kick{font-family:'Fraunces',serif;font-size:13px;letter-spacing:.22em;text-transform:uppercase;
  color:var(--gold);font-weight:600}
h1{font-family:'Fraunces',serif;font-weight:600;font-size:42px;line-height:1.08;margin:10px 0 6px;letter-spacing:-.01em}
h2{font-family:'Fraunces',serif;font-weight:600;font-size:25px;margin:0 0 18px;letter-spacing:-.01em}
.sub{color:var(--muted);font-size:16px}
.rule{height:1px;background:var(--line);margin:40px 0}
section{margin-top:44px}
.tiles{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.tile{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px 18px 16px}
.tile .lab{font-size:12.5px;letter-spacing:.07em;text-transform:uppercase;color:var(--muted)}
.tile .val{font-family:'Fraunces',serif;font-size:30px;font-weight:600;margin-top:6px;line-height:1}
.tile .note{font-size:14px;color:var(--muted);margin-top:6px}
.misread{background:var(--goldsoft);border-radius:14px;padding:22px 24px;display:flex;gap:26px;
  align-items:center;flex-wrap:wrap;border:1px solid rgba(148,98,24,.25)}
.misread .big{font-family:'Fraunces',serif;font-size:34px;font-weight:600;color:var(--gold)}
.misread .txt{flex:1;min-width:240px;font-size:16px}
.dest{background:var(--ink);color:#f4f0e6;border-radius:14px;padding:24px 26px}
.dest .kick{color:#e7c98a}
.dest p{font-family:'Fraunces',serif;font-size:22px;line-height:1.3;margin-top:8px}
.leg{display:grid;grid-template-columns:120px 1fr;gap:18px;padding:18px 0;border-top:1px solid var(--line)}
.leg:first-child{border-top:none}
.leg .when{font-family:'Fraunces',serif;font-weight:600;color:var(--gold);font-size:16px}
.leg .ms{font-size:16.5px}
.leg .unlock{color:var(--muted);font-size:15px;margin-top:4px}
.cols{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.col h3{font-family:'Fraunces',serif;font-size:17px;margin-bottom:10px}
.col.s h3{color:var(--teal)} .col.w h3{color:var(--clay)} .col.o h3{color:var(--gold)}
.col li{list-style:none;font-size:15px;line-height:1.5;margin-bottom:12px;padding-left:16px;position:relative}
.col li:before{content:"";position:absolute;left:0;top:9px;width:6px;height:6px;border-radius:50%}
.col.s li:before{background:var(--teal)} .col.w li:before{background:var(--clay)} .col.o li:before{background:var(--gold)}
.grouplab{font-family:'Fraunces',serif;font-size:14px;letter-spacing:.04em;color:var(--muted);
  text-transform:uppercase;margin:22px 0 12px}
.prod{background:var(--card);border:1px solid var(--line);border-radius:13px;padding:20px 22px;margin-bottom:14px}
.prod.now{border-left:4px solid var(--teal)}
.prod.later{border-left:4px solid var(--gold)}
.prod .top{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap}
.prod .name{font-family:'Fraunces',serif;font-size:19px;font-weight:600}
.badge{font-size:12px;letter-spacing:.06em;text-transform:uppercase;padding:4px 10px;border-radius:20px;white-space:nowrap}
.badge.now{background:var(--tealsoft);color:var(--teal)}
.badge.later{background:var(--goldsoft);color:var(--gold)}
.prod .purpose{color:var(--muted);font-size:15px;margin:6px 0 14px}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{font-size:13px;padding:5px 11px;border-radius:8px;border:1px solid var(--line);
  display:inline-flex;gap:7px;align-items:center}
.chip.pass{background:var(--tealsoft);border-color:rgba(15,110,86,.25)}
.chip.gap{background:var(--claysoft);border-color:rgba(156,67,39,.28)}
.chip .mk{font-weight:600}
.chip.pass .mk{color:var(--teal)} .chip.gap .mk{color:var(--clay)}
.assure{background:var(--card);border:1px dashed rgba(148,98,24,.4);border-radius:13px;padding:20px 22px;margin-top:14px}
.assure .lab{font-family:'Fraunces',serif;font-size:13px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold)}
.assure code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:13px;background:rgba(32,35,31,.05);
  padding:2px 6px;border-radius:5px;word-break:break-all}
.assure .row{display:flex;justify-content:space-between;gap:14px;font-size:14px;padding:7px 0;border-top:1px solid var(--line)}
.assure .row:first-of-type{border-top:none;margin-top:10px}
.assure .k{color:var(--muted)}
@media(max-width:680px){.tiles,.cols{grid-template-columns:1fr}h1{font-size:33px}.leg{grid-template-columns:1fr}}
"""

def chip(c):
    optxt = "≥" if c.op == "gte" else "≤"
    unit = c.unit
    have = f"{c.have:g}{unit}" if unit not in ("$",) else f"${c.have:,.0f}"
    need = f"{c.threshold:g}{unit}" if unit not in ("$",) else f"${c.threshold:,.0f}"
    mk = "meets" if c.passed else "gap"
    cls = "pass" if c.passed else "gap"
    return (f'<span class="chip {cls}"><span class="mk">{mk}</span> '
            f'{c.label}: {have} (needs {optxt} {need})</span>')

def prod_card(m):
    cls = "now" if m.qualifies_now else "later"
    badge = ('<span class="badge now">Available now</span>' if m.qualifies_now
             else '<span class="badge later">On the route</span>')
    chips = "".join(chip(c) for c in m.checks)
    unlock = f'<div style="color:var(--gold);font-size:14px;margin-top:12px">{m.unlock_note}</div>' if not m.qualifies_now else ""
    return (f'<div class="prod {cls}"><div class="top"><span class="name">{m.name}</span>{badge}</div>'
            f'<div class="purpose">{m.purpose}</div><div class="chips">{chips}</div>{unlock}</div>')

def li(items): return "".join(f"<li>{x}</li>" for x in items)

now_cards = "".join(prod_card(m) for m in matches if m.qualifies_now)
later_cards = "".join(prod_card(m) for m in matches if not m.qualifies_now)
legs_html = "".join(
    f'<div class="leg"><div class="when">{l.window}</div>'
    f'<div><div class="ms">{l.milestone}</div><div class="unlock">{l.unlocks}</div></div></div>'
    for l in route)
date_str = datetime.now(timezone.utc).strftime("%B %d, %Y")

HTML = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Financial GPS — {borrower.name}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Newsreader:opsz,wght@6..72,400;6..72,500&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body><div class="wrap">

<div class="kick">Financial Positioning System</div>
<h1>Your financial GPS</h1>
<div class="sub">Prepared for {borrower.name} &middot; {date_str} &middot; a true, complete read of where you are and how to get where you're going</div>

<section>
<h2>Where you are today</h2>
<div class="tiles">
  <div class="tile"><div class="lab">True monthly cash flow</div><div class="val">${pos.true_monthly_cashflow:,.0f}</div><div class="note">sustainable, after seasonality</div></div>
  <div class="tile"><div class="lab">Subject property DSCR</div><div class="val">{pos.subject_dscr}</div><div class="note">earns ${pos.subject_dscr} per $1 of payment</div></div>
  <div class="tile"><div class="lab">Equity available</div><div class="val">${pos.equity_available:,.0f}</div><div class="note">portfolio LTV {pos.portfolio_ltv:.0f}%</div></div>
  <div class="tile"><div class="lab">Reserves</div><div class="val">{pos.reserves_months} mo</div><div class="note">target is 6 months</div></div>
  <div class="tile"><div class="lab">Credit</div><div class="val">{pos.credit_score}</div><div class="note">{pos.tradelines} tradelines &middot; target 720 / 5</div></div>
  <div class="tile"><div class="lab">Income variability</div><div class="val">{pos.income_volatility_cov:.0%}</div><div class="note">seasonal, explainable</div></div>
</div>
</section>

<section>
<div class="misread">
  <div class="big">{pos.cashflow_understatement_x}&times;</div>
  <div class="txt">A conventional debt-to-income test counts only <b>${pos.dti_qualifying_monthly:,.0f}/mo</b> of your income. Read completely &mdash; depreciation added back, distributions and net rents counted &mdash; your sustainable cash flow is <b>${pos.true_monthly_cashflow:,.0f}/mo</b>. The income is real; the standard test simply doesn't see it.</div>
</div>
</section>

<section>
<div class="dest"><div class="kick">Where you're going</div><p>{goal.headline}</p></div>
</section>

<section>
<h2>Your route</h2>
{legs_html}
</section>

<div class="rule"></div>

<section>
<h2>The honest read</h2>
<div class="cols">
  <div class="col s"><h3>Strengths</h3><ul>{li(reading['strengths'])}</ul></div>
  <div class="col w"><h3>Watch points</h3><ul>{li(reading['weaknesses'])}</ul></div>
  <div class="col o"><h3>Opportunities</h3><ul>{li(reading['opportunities'])}</ul></div>
</div>
</section>

<section>
<h2>Your vehicles</h2>
<div class="grouplab">Available to you now</div>
{now_cards}
<div class="grouplab">Unlocks as you move down the route</div>
{later_cards}
</section>

<section>
<div class="assure">
  <div class="lab">Assurance &middot; vetted against standards</div>
  <p style="font-size:15px;margin-top:8px">Both you and every product above were measured against one published standard set. This read is recorded, timestamped, and reproducible &mdash; the same inputs and standard version always produce this same result, so a lender or funder can independently verify it.</p>
  <div class="row"><span class="k">Standard set</span><span>{STANDARD_SET_VERSION}</span></div>
  <div class="row"><span class="k">Read method</span><span>{METHOD_VERSION}</span></div>
  <div class="row"><span class="k">Recorded (UTC)</span><span>{event['timestamp']}</span></div>
  <div class="row"><span class="k">Ledger entry</span><code>{event['this_hash']}</code></div>
</div>
</section>

</div></body></html>"""

with open(os.path.join(OUT, "financial_gps_report.html"), "w") as f:
    f.write(HTML)
print(f"\nWrote {OUT}/financial_gps_report.html  ({len(HTML):,} bytes)")
