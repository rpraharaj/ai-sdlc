# AGENTS.md

This repository is the **source** of a portable AI SDLC pack.

## Do

- Edit `docs/` when the operating model changes. Keep one home per fact.
- Edit `skills/<name>/` using `docs/reference/skill-standard.md`. Frontmatter: spec fields only.
- Edit `agents/`, `playbooks/`, `workflows/` using the matching standard under `docs/reference/`.
- Stay vendor-neutral. See `docs/reference/portability.md`.
- After edits, run `python3 scripts/check-pack.py`.

## Do not

- Do not add vendor-only frontmatter, vendor tool names, or orchestration DSLs to `skills/`, `context/`, `templates/`, `agents/`, `playbooks/`, or `workflows/`.
- Do not invent SLOs, users, or a live program’s systems of record in templates.
- Do not commit secrets.
- Do not put procedure steps in `adapters/`. Pointers only.

## Commands

- **Install:** n/a for this repo. Consuming repos follow `INSTALL.md`.
- **Run:** n/a
- **Test:** `python3 scripts/check-pack.py`
- **Lint / Typecheck / Build:** none

## Layout

- `context/` — templates for a consuming program’s always-on facts
- `skills/` — full standalone catalog (program + core engineering)
- `agents/` — nine permission profiles + optional personas
- `playbooks/` — one page per role
- `workflows/` — Markdown sequences with human gates
- `templates/consuming-AGENTS.md` — starter `AGENTS.md` for a product repo
- `adapters/` — client pointers to `AGENTS.md` and `.agents/skills/`
- `evals/` — fixtures + static cases (`scripts/check-evals.py`)
- `docs/` — PRD, architecture, design, reference
- `scripts/check-pack.py` — pack validator (includes evals)
