"""Plumbline - Populi API probe (read-only).

Discovers which Populi API generation the token drives and inventories
reference data and taxonomies WITHOUT persisting student detail.

Pull directions (and nothing else):
  1. Auth discovery: legacy XML API (/api/index.php, task-based) vs API2 (/api2/, bearer).
  2. Reference data: academic terms, programs, degrees, campuses.
  3. Taxonomies: custom fields, application/funnel-related option sets.
  4. Aggregates: record counts only. Any sampled record reports FIELD NAMES ONLY.

Secrets: token is read from a local .env (never committed, never printed).
Output: markdown report with structure only - all values masked.

Usage:
  python populi_probe.py --env "C:\\path\\to\\.env" --subdomain turner --out report.md
"""
import argparse
import json
import sys
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET

TIMEOUT = 25

LEGACY_TASKS = [
    "getAcademicTerms", "getTerms", "getCurrentAcademicTerm",
    "getDegrees", "getPrograms", "getEducationLevels", "getCampuses",
    "getCustomFields", "getApplicationTemplates", "getLeadSources",
    "getApplicationFieldOptions", "getCountries",
]

API2_GETS = [
    "terms", "academicterms", "programs", "degrees", "campuses",
    "customfields", "applicationtemplates",
]


def load_token(env_path: str) -> str:
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("Primary_Token="):
                return line.split("=", 1)[1].strip()
    raise SystemExit("Primary_Token not found in .env")


def redact(text: str, token: str) -> str:
    return text.replace(token, "[TOKEN]") if token else text


def xml_structure(root: ET.Element, max_children: int = 3) -> dict:
    """Return tag structure and counts; never element text (values masked)."""
    children = list(root)
    out = {"tag": root.tag, "attr_names": sorted(root.attrib.keys()), "child_count": len(children)}
    seen = {}
    for c in children:
        if c.tag not in seen and len(seen) < max_children:
            seen[c.tag] = xml_structure(c, max_children)
    out["child_tags"] = {t: seen[t] for t in seen}
    return out


def json_structure(obj, depth=0):
    if depth > 3:
        return "..."
    if isinstance(obj, dict):
        return {k: json_structure(v, depth + 1) for k, v in obj.items()}
    if isinstance(obj, list):
        return {"_list_len": len(obj), "_first": json_structure(obj[0], depth + 1) if obj else None}
    return type(obj).__name__  # value masked, type only


def call_legacy(base: str, token: str, task: str):
    data = urllib.parse.urlencode({"access_key": token, "task": task}).encode()
    req = urllib.request.Request(base + "/api/index.php", data=data,
                                 headers={"User-Agent": "plumbline-probe/0.1"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            body = r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        return {"task": task, "http": e.code, "result": "http-error",
                "detail": redact(body[:300], token)}
    except Exception as e:
        return {"task": task, "result": "exception", "detail": redact(str(e), token)}
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        return {"task": task, "result": "non-xml", "detail": redact(body[:200], token)}
    err = root.find(".//code")
    if root.tag == "error" or err is not None:
        code = (err.text if err is not None else "?")
        msg = root.findtext(".//message", default="")
        return {"task": task, "result": "api-error", "code": code, "message": msg[:200]}
    return {"task": task, "result": "ok", "structure": xml_structure(root)}


def call_api2(base: str, token: str, path: str):
    req = urllib.request.Request(f"{base}/api2/{path}",
                                 headers={"Authorization": f"Bearer {token}",
                                          "Accept": "application/json",
                                          "User-Agent": "plumbline-probe/0.1"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            body = r.read().decode("utf-8", "replace")
            code = r.status
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        return {"path": path, "http": e.code, "result": "http-error",
                "detail": redact(body[:300], token)}
    except Exception as e:
        return {"path": path, "result": "exception", "detail": redact(str(e), token)}
    try:
        return {"path": path, "http": code, "result": "ok",
                "structure": json_structure(json.loads(body))}
    except json.JSONDecodeError:
        return {"path": path, "http": code, "result": "non-json",
                "detail": redact(body[:200], token)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--env", required=True)
    ap.add_argument("--subdomain", default="turnerseminary")
    ap.add_argument("--out", default="populi-probe-report.md")
    args = ap.parse_args()

    token = load_token(args.env)
    base = f"https://{args.subdomain}.populiweb.com"
    lines = [f"# Populi probe report - {args.subdomain}.populiweb.com", ""]

    lines.append("## Legacy API (/api/index.php)\n")
    auth_ok = None
    for task in LEGACY_TASKS:
        res = call_legacy(base, token, task)
        lines.append(f"### task={task}\n```json\n{json.dumps(res, indent=1)[:2500]}\n```")
        if res.get("result") == "ok":
            auth_ok = "legacy"
        if res.get("result") == "api-error" and "AUTH" in str(res.get("code", "")).upper():
            lines.append("(auth rejected - stopping legacy sweep)")
            break

    lines.append("\n## API2 (/api2/, bearer)\n")
    for path in API2_GETS:
        res = call_api2(base, token, path)
        lines.append(f"### GET /api2/{path}\n```json\n{json.dumps(res, indent=1)[:2500]}\n```")
        if res.get("result") == "ok" and auth_ok is None:
            auth_ok = "api2"

    lines.append(f"\n## Verdict\n\nWorking auth path: **{auth_ok or 'none - see errors above'}**\n")
    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"report written: {args.out}; auth path: {auth_ok}")


if __name__ == "__main__":
    main()
