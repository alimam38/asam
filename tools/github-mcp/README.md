# GitHub MCP connector (token-based)

A small MCP server that lets Claude work with GitHub through a **Personal Access Token**
instead of the hosted OAuth connector. Built to create a private repo and publish a local
working tree in clean commits — the same pattern as the Talbot Hall Populi connector.

## 🔐 Security first

- Your token is a **secret**. It is read **only** from the environment variable `GITHUB_TOKEN`.
  **Never paste it into a chat** and never put it in this file or any document.
- Use it, then you can delete/rotate it anytime in GitHub → Settings → Developer settings.

## 1. Create a token

GitHub → **Settings → Developer settings → Personal access tokens**.

Simplest (classic): **Tokens (classic) → Generate new token (classic)**, check the **`repo`**
scope (this allows creating a repo and pushing files). Set a short expiration. Copy the
`ghp_…` value.

*(Fine-grained alternative: a fine-grained token scoped to your account with **Administration:
Read and write** — to create repos — and **Contents: Read and write** — to push files.)*

## 2. Install dependencies

Same two packages the Populi connector uses (you likely already have them):
```
pip install -r requirements.txt
```

## 3. Connect it to Claude

Add a `github` entry to your Claude Desktop config
(Settings ▸ Developer ▸ Edit Config), alongside your existing `populi` server:

```json
{
  "mcpServers": {
    "github": {
      "command": "python",
      "args": ["C:\\Users\\alima\\Products\\asam\\tools\\github-mcp\\github_mcp.py"],
      "env": { "GITHUB_TOKEN": "ghp_your_token_here" }
    }
  }
}
```

Restart Claude. The `github_*` tools will appear, and the migration can run.

## Tools

- Diagnostics: `github_check_config`, `github_request` (generic escape hatch), `github_get_user`
- Repos: `github_list_repos`, `github_get_repo`, `github_create_repo` (private + auto_init)
- Files: `github_get_file`, `github_put_file` (single), `github_push_files` (many files → one
  commit via the Git Data API), `github_verify_files` (confirm GitHub matches local files),
  `github_create_branch`

## Reliability & connection issues

Lessons from real incidents (a flaky connection failing pushes outright, and a
2026-07-02 push that landed 7 files truncated mid-sentence — caught 11 days later
by the weekly sweep):

**Connection handling.** The server keeps one shared HTTP client (connections are
reused instead of a fresh TLS handshake per request), transparently retries failed
connection attempts, and backs off + retries on GitHub 5xx responses and both
primary and secondary rate limits. A read that dies mid-response is retried only
for GET — a write may already have been applied. Timeout defaults to 60s
(override with `GITHUB_TIMEOUT`).

**Truncation guard.** Content that travels *through the chat* (`content_text`)
can be silently cut off; the API will happily commit the fragment. Three defenses:

1. Prefer `local_path` in `github_push_files` — content is read from disk on the
   machine running the server and never passes through the chat.
2. Pass `expected_bytes` (the source file's size) with any `content_text` /
   `content_base64` push — the server refuses to commit if the size doesn't match.
3. After pushing, run `github_verify_files` with the same paths — it compares git
   blob SHAs so any truncated or corrupted upload is reported immediately, not
   discovered weeks later.

If calls fail with `GITHUB_TOKEN is not set` or HTTP 401, start with
`github_check_config`: it confirms the token is present, valid, and which account
it authenticates as.

## Note on field names

Paths and verbs are verified against the GitHub REST API (api.github.com, version
2022-11-28). `github_push_files` reads files from disk on the machine running this server,
so it can publish a whole working tree (text and binary) without sending contents through
the chat.
