# Gemini CLI

No procedure file. Point the client at `AGENTS.md` if it is not the default context file.

Example merge into `<product-repo>/.gemini/settings.json` (see current Gemini docs if the key moved):

```json
{
  "context": {
    "fileName": "AGENTS.md"
  }
}
```

Skills: use `.agents/skills/` when the client scans it. Otherwise symlink from the client’s skills directory to that path. Do not rewrite `SKILL.md`.
