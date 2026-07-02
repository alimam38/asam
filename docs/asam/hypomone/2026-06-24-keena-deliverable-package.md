# The Keena Package — Deliverable Index

**For:** Keena Pierre (Prep Capital) · **From:** Aliman Neal / Eden Intelligence Group · **Assembled:** 2026-06-24
**Status:** Delivery-ready. One operational choice remains (Charter hosting endpoint — see §Deploy).

This is the complete package referenced in the cover note — finished and assembled. It is built around
the thing Keena specifically asked for: **fresh, first-party data.** The Charter is not research *about* a
future build; it *is* the build — a live instrument that generates new, owned, consented founding-cohort
data from day one. Nothing here retrofits a pre-existing book.

---

## What to send, in order

1. **Cover Note** — `2026-05-28-keena-cover-note-v1.md` *(the framing; adjust voice/length before sending)*
2. **Architecture Overview** — `../../meridia/2026-05-24-eig-meridia-architecture-overview.md` *(EIG/Meridia, AIA at a non-confidential level, the engagement frame)*
3. **Market Read v1** — `2026-06-01-market-read-v1.md` *(the federally-sourced national picture, source-tiered T1/T2/T3)*
4. **Georgia & Atlanta Addendum v2** — `2026-06-01-market-read-addendum-georgia-atlanta-v2.md` *(the metro layer; DTI-as-denial-mechanism is the spine; Atlanta Fed credit-card signal is the local pulse)*
5. **The Charter — live instrument** — `2026-06-24-the-charter-live.html` *(the fresh-data centerpiece; host it, send the link)*

**Do NOT send:** the Naming & Architecture document or any interior-grammar material (Zakhar, Shema,
Aletheia, Aegis, Solera, the Reserved). That is the internal catechism. Keena gets the institution's name,
the one-line thesis, the sourced market case, and the live Charter — the deeper architecture earns its
disclosure later. (See the canon, §11: *internal cosmology vs. the outward story*.)

---

## The Charter — what it is and why it's the deliverable

A 5-section, 19-question, phone-first instrument (**Recognition → Experience → How you operate →
Membership → The Charter**) that:
- **Generates fresh, owned, first-party data** — citable primary evidence that the federally-documented
  misbanking condition is present *in this specific cohort, with names attached*. (The Market Read carries
  the national claim; the Charter carries the cohort claim — kept separate, per the methodology.)
- **Converts respondents into charter members** of the founding cohort (Q16–Q17).
- **Propagates through the right network** via a per-respondent referral/share link (Q18, `?ref=` tracking).
- **Stays compliant by design** — interest and experience, never an offer of credit; explicit, optional,
  consented contact capture (Q19). This guards the founder's NMLS standing.
- **Produces the institutional-sales line** (for Hypomone Financial Network Partners): Q8 + Q9 + Q10 + Q11
  together → *"a segment moving [X] in volume, using [Y] products, paying [Z] reliably, whose institutions
  don't recognize the relationship."*

**Verified:** all 19 questions render, sections build, the conditional participation question reveals on a
"Yes," the "choose up to 3" cap holds, and submit shows the closing screen and saves an owned copy of the
response. Tested headless; open it in any browser to see it live.

---

## Deploy + own the data (the one remaining choice)

The Charter is self-contained HTML — host it anywhere (your NAS, Netlify, a static host) and send the link.
Data ownership is built in two ways:

1. **Collection endpoint (recommended).** Open the file and set one line near the top of the script:
   `const SUBMIT_ENDPOINT = ""` → your own endpoint (a NAS API route, Formspree, or a Google Apps Script
   webhook). Each submission `POST`s as JSON to *you*. This is the self-hosted answer to the Charter's open
   "self-hosted vs. Typeform" question — fast standup, data fully yours, no vendor lock.
2. **Local owned copy (always on).** Every response is also saved to the device and downloadable as JSON,
   so nothing is ever trapped in a third party — consistent with the no-central-honeypot posture.

Until an endpoint is set, the form works and captures locally; set the endpoint when you pick the host.

---

## The ask to Keena (per the cover note)

Small and honest, one conversation in:
1. **Read the materials** and tell us where the thesis is weakest, where the data overstates, where the
   architecture is missing something visible from her vantage.
2. **If it holds for her — consider being among the first to sign The Charter.** She and her husband sit in
   the segment; she offered to champion responses. The honest version of that is to be a charter member,
   not only a referrer.

No capital introductions requested at this stage. That comes later, at her pace.

---

## Provenance

The substantive spine for this package is the canon: `../../../specs/meridia/2026-06-24-Meridia-Canonical-Architecture-and-Strategy-v1.md`.
Source drafts (Charter v2, Market Read v1, Addendum v2, Architecture Overview, cover note) live in
`docs/asam/hypomone/` and `docs/meridia/` and were assessed delivery-ready on 2026-06-24; the Charter was
upgraded from spec to a live, tested instrument.
