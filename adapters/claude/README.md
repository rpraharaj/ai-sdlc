# Claude Code

Copy [CLAUDE.md](CLAUDE.md) to the product repo root as `CLAUDE.md` only if that client will not read `AGENTS.md`. Prefer a symlink:

```sh
ln -s AGENTS.md <product-repo>/CLAUDE.md
```

If you must keep a separate file, use the pointer in `CLAUDE.md` — do not paste skill procedures.

Skills: this client often also scans `.claude/skills/`. Symlink to `.agents/skills/<name>` if discovery misses the shared path. Do not copy `SKILL.md` bodies.
