#!/usr/bin/env python3
"""
GitHub MCP connector - token-based (no OAuth).

A small Model Context Protocol (stdio) server that exposes the GitHub REST API for
repository and file operations, focused on publishing/migrating a local working tree
into a (private) GitHub repository in clean commits.

Why this exists: the hosted GitHub MCP requires an interactive OAuth flow that some
clients can't complete automatically. This connector uses a Personal Access Token
from the environment instead - the same pattern as the Talbot Hall Populi connector.

Auth (verified against api.github.com):
  - Header:  Authorization: Bearer <token>
  - Accept:  application/vnd.github+json
  - Version: X-GitHub-Api-Version: 2022-11-28
  - Base:    https://api.github.com

Bulk push uses the Git Data API (blobs -> tree -> commit -> update ref) so many files
land in ONE commit instead of one-commit-per-file.

SECURITY: the token is read ONLY from the environment variable GITHUB_TOKEN. Never
hard-code it and never paste it into a chat. See README.md.
"""
import base64
import os
import time
from typing import Any, Optional

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("github")

TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()
API = os.environ.get("GITHUB_API_URL", "https://api.github.com").strip().rstrip("/")
TIMEOUT = float(os.environ.get("GITHUB_TIMEOUT", "30"))


def _headers() -> dict[str, str]:
    return {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "asam-github-mcp",
    }


def _req(method: str, path: str, body: Optional[dict] = None,
         params: Optional[dict] = None, max_retries: int = 3) -> dict[str, Any]:
    """Authenticated GitHub call. Returns parsed JSON, or {'error': ...}."""
    if not TOKEN:
        return {"error": "GITHUB_TOKEN is not set (see README.md)."}
    url = path if path.startswith("http") else f"{API}/{path.lstrip('/')}"
    attempt = 0
    while True:
        attempt += 1
        try:
            with httpx.Client(timeout=TIMEOUT) as client:
                resp = client.request(method.upper(), url, headers=_headers(),
                                      json=(body if body is not None else None),
                                      params=params)
        except httpx.RequestError as e:
            return {"error": f"Network error calling {url}: {e}"}
        # Secondary rate limit / abuse: back off and retry.
        if resp.status_code in (403, 429) and "rate limit" in resp.text.lower() and attempt <= max_retries:
            ra = resp.headers.get("retry-after", "")
            time.sleep(min(60, int(ra) if ra.isdigit() else 5 * attempt))
            continue
        if resp.status_code == 204:
            return {"ok": True}
        try:
            data = resp.json()
        except Exception:
            data = {"raw": resp.text[:500]}
        if resp.status_code >= 400:
            msg = data.get("message") if isinstance(data, dict) else str(data)[:300]
            hint = ""
            if resp.status_code == 401:
                hint = " - token missing/expired or wrong scopes."
            elif resp.status_code == 404:
                hint = " - not found, or the token can't see it (check repo + scopes)."
            elif resp.status_code == 422:
                hint = " - validation failed (e.g. repo name already exists)."
            return {"error": f"HTTP {resp.status_code}: {msg}{hint}", "details": data}
        return data


def _whoami() -> Optional[str]:
    u = _req("GET", "user")
    return None if "error" in u else u.get("login")


# --------------------------------------------------------------------------- #
# Diagnostics
# --------------------------------------------------------------------------- #
@mcp.tool()
def github_check_config() -> dict:
    """Verify the token works and report the authenticated account. Read-only."""
    if not TOKEN:
        return {"ok": False, "detail": "GITHUB_TOKEN is not set (see README.md)."}
    u = _req("GET", "user")
    if "error" in u:
        return {"ok": False, "detail": u["error"]}
    return {"ok": True, "login": u.get("login"), "name": u.get("name"),
            "api": API, "token_present": True}


@mcp.tool()
def github_request(method: str, path: str, body: Optional[dict] = None,
                   params: Optional[dict] = None) -> dict:
    """Generic GitHub REST call - escape hatch for any endpoint not wrapped below.
    method: GET/POST/PUT/PATCH/DELETE. path: route after the host
    (e.g. 'repos/OWNER/REPO'). body/params: JSON dicts."""
    return _req(method, path, body, params)


@mcp.tool()
def github_get_user() -> dict:
    """Get the authenticated user (GET /user). Read-only."""
    return _req("GET", "user")


# --------------------------------------------------------------------------- #
# Repositories
# --------------------------------------------------------------------------- #
@mcp.tool()
def github_list_repos(per_page: int = 50, page: int = 1,
                      visibility: str = "all", affiliation: str = "owner") -> dict:
    """List repositories for the authenticated user (GET /user/repos). Read-only."""
    return _req("GET", "user/repos",
                params={"per_page": per_page, "page": page,
                        "visibility": visibility, "affiliation": affiliation})


@mcp.tool()
def github_get_repo(owner: str, repo: str) -> dict:
    """Get one repository (GET /repos/{owner}/{repo}). Read-only."""
    return _req("GET", f"repos/{owner}/{repo}")


@mcp.tool()
def github_create_repo(name: str, private: bool = True,
                       description: Optional[str] = None,
                       auto_init: bool = True,
                       default_branch: str = "main") -> dict:
    """Create a repository on the authenticated account (POST /user/repos). WRITE.
    Defaults to PRIVATE with an initial commit (auto_init=True) so it has a base
    branch ready for github_push_files. Requires a token with repo-creation rights."""
    body: dict[str, Any] = {"name": name, "private": private, "auto_init": auto_init}
    if description:
        body["description"] = description
    res = _req("POST", "user/repos", body)
    if "error" not in res and default_branch and res.get("default_branch") != default_branch:
        # best-effort rename of the default branch
        owner = res.get("owner", {}).get("login")
        _req("POST", f"repos/{owner}/{name}/branches/{res.get('default_branch')}/rename",
             {"new_name": default_branch})
        res = _req("GET", f"repos/{owner}/{name}")
    return res


# --------------------------------------------------------------------------- #
# Files
# --------------------------------------------------------------------------- #
@mcp.tool()
def github_get_file(owner: str, repo: str, path: str, ref: Optional[str] = None) -> dict:
    """Get a file's metadata + content (GET /repos/{owner}/{repo}/contents/{path}).
    Read-only. Use the returned 'sha' when updating an existing file via put_file."""
    return _req("GET", f"repos/{owner}/{repo}/contents/{path.lstrip('/')}",
                params={"ref": ref} if ref else None)


@mcp.tool()
def github_put_file(owner: str, repo: str, path: str, message: str,
                    content_text: Optional[str] = None,
                    content_base64: Optional[str] = None,
                    branch: Optional[str] = None,
                    sha: Optional[str] = None) -> dict:
    """Create or update a SINGLE file (PUT /repos/{owner}/{repo}/contents/{path}). WRITE.
    Provide content_text (UTF-8) or content_base64. To update an existing file, pass its
    current 'sha' (from github_get_file). For many files, prefer github_push_files."""
    if content_base64 is None:
        if content_text is None:
            return {"error": "Provide content_text or content_base64."}
        content_base64 = base64.b64encode(content_text.encode("utf-8")).decode("ascii")
    body: dict[str, Any] = {"message": message, "content": content_base64}
    if branch:
        body["branch"] = branch
    if sha:
        body["sha"] = sha
    return _req("PUT", f"repos/{owner}/{repo}/contents/{path.lstrip('/')}", body)


def _to_b64(entry: dict, base_dir: Optional[str]) -> tuple[Optional[str], Optional[str], Optional[str]]:
    """Return (repo_path, b64content, error)."""
    repo_path = entry.get("path") or entry.get("local_path")
    if not repo_path:
        return None, None, "each file needs a 'path'"
    repo_path = repo_path.replace("\\", "/").lstrip("/")
    if entry.get("content_base64") is not None:
        return repo_path, entry["content_base64"], None
    if entry.get("content_text") is not None:
        return repo_path, base64.b64encode(entry["content_text"].encode("utf-8")).decode("ascii"), None
    local = entry.get("local_path") or entry.get("path")
    if base_dir and not os.path.isabs(local):
        local = os.path.join(base_dir, local)
    try:
        with open(local, "rb") as fh:
            return repo_path, base64.b64encode(fh.read()).decode("ascii"), None
    except Exception as e:
        return repo_path, None, f"could not read {local}: {e}"


@mcp.tool()
def github_push_files(repo: str, message: str, files: list[dict],
                      owner: Optional[str] = None, branch: str = "main",
                      base_dir: Optional[str] = None) -> dict:
    """Push MANY files as ONE commit via the Git Data API. WRITE.
    files: list of {path, ...} where each item supplies content via one of:
      - local_path (read from disk; relative paths resolve against base_dir), or
      - content_text (UTF-8), or
      - content_base64.
    'path' is the path inside the repo. owner defaults to the authenticated user.
    The branch must already exist (create the repo with auto_init=True)."""
    if not owner:
        owner = _whoami()
        if not owner:
            return {"error": "Could not resolve owner; pass owner= explicitly."}
    if not files:
        return {"error": "No files provided."}

    ref = _req("GET", f"repos/{owner}/{repo}/git/ref/heads/{branch}")
    if "error" in ref:
        return {"error": f"Branch '{branch}' not found ({ref['error']}). "
                         f"Create the repo with auto_init=True first."}
    base_commit_sha = ref["object"]["sha"]
    base_commit = _req("GET", f"repos/{owner}/{repo}/git/commits/{base_commit_sha}")
    if "error" in base_commit:
        return base_commit
    base_tree_sha = base_commit["tree"]["sha"]

    tree_items: list[dict] = []
    pushed: list[str] = []
    for entry in files:
        rpath, b64, err = _to_b64(entry, base_dir)
        if err:
            return {"error": err}
        blob = _req("POST", f"repos/{owner}/{repo}/git/blobs",
                    {"content": b64, "encoding": "base64"})
        if "error" in blob:
            return {"error": f"blob failed for {rpath}: {blob['error']}"}
        tree_items.append({"path": rpath, "mode": "100644", "type": "blob", "sha": blob["sha"]})
        pushed.append(rpath)

    tree = _req("POST", f"repos/{owner}/{repo}/git/trees",
                {"base_tree": base_tree_sha, "tree": tree_items})
    if "error" in tree:
        return tree
    commit = _req("POST", f"repos/{owner}/{repo}/git/commits",
                  {"message": message, "tree": tree["sha"], "parents": [base_commit_sha]})
    if "error" in commit:
        return commit
    upd = _req("PATCH", f"repos/{owner}/{repo}/git/refs/heads/{branch}",
               {"sha": commit["sha"]})
    if "error" in upd:
        return upd
    return {"ok": True, "commit": commit["sha"], "files_pushed": len(pushed),
            "paths": pushed,
            "commit_url": f"https://github.com/{owner}/{repo}/commit/{commit['sha']}"}


@mcp.tool()
def github_create_branch(owner: str, repo: str, new_branch: str,
                         from_branch: str = "main") -> dict:
    """Create a new branch from an existing one. WRITE."""
    ref = _req("GET", f"repos/{owner}/{repo}/git/ref/heads/{from_branch}")
    if "error" in ref:
        return ref
    return _req("POST", f"repos/{owner}/{repo}/git/refs",
                {"ref": f"refs/heads/{new_branch}", "sha": ref["object"]["sha"]})


if __name__ == "__main__":
    mcp.run()
