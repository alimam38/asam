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
  commit via the Git Data API), `github_create_branch`

## Note on field names

Paths and verbs are verified against the GitHub REST API (api.github.com, version
2022-11-28). `github_push_files` reads files from disk on the machine running this server,
so it can publish a whole working tree (text and binary) without sending contents through
the chat.
