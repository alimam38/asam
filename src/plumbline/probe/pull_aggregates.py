"""Plumbline demo pull - aggregates only, for the 2026-06-12 Turner meeting.
Reads record-level data in memory, persists ONLY aggregate counts keyed by
term/program/status ids. No names, no PII fields requested or stored."""
import json, sys, urllib.request, urllib.error
from collections import Counter

ENV = r"C:\Users\alima\Dropbox\Claude\.env"
BASE = "https://turnerseminary.populiweb.com/api2"
token = next(l.split("=",1)[1].strip() for l in open(ENV, encoding="utf-8") if l.startswith("Primary_Token="))

def get(path, page=None):
    body = json.dumps({"page": page}).encode() if page else None
    req = urllib.request.Request(f"{BASE}/{path}", data=body, method="GET",
        headers={"Authorization": f"Bearer {token}", "Accept": "application/json",
                 "Content-Type": "application/json", "User-Agent": "plumbline-demo/0.1"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8", "replace"))

def all_rows(path, cap=60):
    import time
    rows, seen, page = [], set(), 1
    while page <= cap:
        d = get(path, page)
        for rec in d.get("data", []):
            rid = rec.get("id")
            if rid not in seen:
                seen.add(rid); rows.append(rec)
        if not d.get("has_more"): break
        page += 1
        time.sleep(0.6)  # be polite per Populi rate guidance
    return rows

out = {}

terms = all_rows("academicterms")
out["terms"] = {t["id"]: {"name": t.get("display_name") or t.get("name"),
                          "start": t.get("start_date"), "end": t.get("end_date")} for t in terms}
programs = all_rows("programs")
out["programs"] = {p["id"]: p.get("name") for p in programs}

inq = all_rows("inquiries")
out["inquiries"] = {"total": len(inq),
    "by_term": Counter(str(i.get("academic_term_id")) for i in inq),
    "by_status": Counter(str(i.get("status")) for i in inq)}

leads = all_rows("leads")
out["leads"] = {"total": len(leads),
    "by_term": Counter(str(l.get("academic_term_id")) for l in leads),
    "by_status": Counter(str(l.get("status")) for l in leads),
    "active": sum(1 for l in leads if l.get("active"))}

apps = all_rows("applications")
def app_status(a):
    for k in ("status", "decision", "final_decision"):
        if a.get(k) is not None: return f"{k}:{a.get(k)}"
    if a.get("withdrawn_at"): return "withdrawn"
    if a.get("submitted_at"): return "submitted"
    if a.get("started_on"): return "started"
    return "unknown"
out["applications"] = {"total": len(apps),
    "by_term": Counter(str(a.get("academic_term_id")) for a in apps),
    "by_status": Counter(app_status(a) for a in apps),
    "by_program": Counter(str(a.get("program_id")) for a in apps),
    "field_names": sorted(apps[0].keys()) if apps else []}

enr = all_rows("enrollments")
keys = sorted(enr[0].keys()) if enr else []
out["enrollments"] = {"total": len(enr), "field_names": keys}
for f in ("academic_term_id", "term_id", "status", "program_id", "enrolled_credits", "exit_reason"):
    if enr and f in enr[0]:
        out["enrollments"]["by_" + f] = Counter(str(e.get(f)) for e in enr)
# people: status mix only
ppl = all_rows("people")
out["people"] = {"total": len(ppl), "by_status": Counter(str(p.get("status")) for p in ppl)}

json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), indent=1, default=dict)
print("written", sys.argv[1])
