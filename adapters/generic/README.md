# Any other client

1. Ensure the product repo has `AGENTS.md` (see `templates/consuming-AGENTS.md`).
2. Install skills at `.agents/skills/` ([INSTALL.md](../../INSTALL.md)).
3. If the client has its own instruction filename, add a **one-line pointer** to `./AGENTS.md` — same text as `adapters/claude/CLAUDE.md`.
4. If it has its own skills directory, symlink to `.agents/skills/<name>`.

Do not paste a skill body into the vendor folder.
