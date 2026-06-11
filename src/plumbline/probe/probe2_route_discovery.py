"""Plumbline probe pass 2 - API2 route discovery for KPI-critical objects.
Same rules: read-only, structure/types only, values never recorded, token redacted."""
import json, sys, urllib.request, urllib.error

ENV = r"C:\Users\alima\Dropbox\Claude\.env"
BASE = "https://turnerseminary.populiweb.com/api2"
token = next(l.split("=",1)[1].strip() for l in open(ENV, encoding="utf-8") if l.startswith("Primary_Token="))

def js(obj, d=0):
    if d > 3: return "..."
    if isinstance(obj, dict): return {k: js(v, d+1) for k, v in obj.items()}
    if isinstance(obj, list): return {"_len": len(obj), "_first": js(obj[0], d+1) if obj else None}
    return type(obj).__name__

CANDIDATES = ["people", "persons", "students", "enrollments", "courseofferings",
              "courses", "admissions/applications", "applications", "admissions/leads",
              "leads", "inquiries", "departments", "academicyears", "aid/awards",
              "financialaid/awards", "tags", "customfields/person", "events"]

out = {}
for path in CANDIDATES:
    req = urllib.request.Request(f"{BASE}/{path}", headers={
        "Authorization": f"Bearer {token}", "Accept": "application/json",
        "User-Agent": "plumbline-probe/0.2"})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            body = json.loads(r.read().decode("utf-8", "replace"))
            n = body.get("results", body.get("count"))
            out[path] = {"http": r.status, "results": n, "structure": js(body)}
    except urllib.error.HTTPError as e:
        try: msg = json.loads(e.read().decode())[ "type"]
        except Exception: msg = "?"
        out[path] = {"http": e.code, "type": msg}
    except Exception as e:
        out[path] = {"error": str(e).replace(token, "[TOKEN]")}

rep = json.dumps(out, indent=1).replace(token, "[TOKEN]")
open(sys.argv[1], "w", encoding="utf-8").write(rep)
print("ok")
