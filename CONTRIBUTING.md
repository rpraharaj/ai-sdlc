# Contributing

PRs and issues are welcome. This pack is procedures other programs will run — change it the way the pack itself demands: evidence first, one home per fact, no vendor lock-in.

## Before you write a new skill

1. Read [docs/how-to-use.md](docs/how-to-use.md) and [docs/reference/catalog.md](docs/reference/catalog.md).
2. Check that an existing skill does not already produce that artifact. Two roles running the same steps is **one** skill.
3. Job-title agents (`pm-agent`, `ba-helper`) will be rejected.

## How to change a skill

Follow [docs/reference/skill-standard.md](docs/reference/skill-standard.md) and [docs/reference/portability.md](docs/reference/portability.md).

A skill PR should include:

1. **Why the current procedure failed** — a real trace (wrong output, a refuse that should have fired, a missing handoff). Not “would be nicer.”
2. The template or quality bar that now differs, if it does.
3. `metadata.version` bumped on that skill when the procedure or template changes.

Rules that will get a PR sent back:

- Vendor tool names or vendor-only frontmatter in `skills/` (those belong in `adapters/` as **pointers**, never a second `SKILL.md` body)
- Restating the glossary or Definition of Done inside a skill
- Invented users, SLOs, or “typical” numbers in templates
- Expand and contract of an artifact template in the same change
- More than one unrelated skill in the same PR

## Adapters and docs

- **Adapters:** one-line pointers to `AGENTS.md` / `.agents/skills/`. Deleting the adapter directory must lose no procedure text.
- **Playbooks / workflows:** indexes and sequences only. They name skills that already exist.
- **Context templates:** headings and empty tables. Do not fill them with a fictional live program (evals fixtures are the place for that).

## Check

From the repo root:

```sh
python3 scripts/check-pack.py
```

It must exit 0. It includes static evals and the disposable-copy validator/installer regression suite (`scripts/test-check-pack.py`). New validator rules need both valid inputs and rejected mutations at the CLI boundary. CI runs the same command. That is the mechanical bar. Reviewers still apply the skill standard and portability denylist by reading the diff.

## Pull request

- One concern per PR (one skill, one adapter, or one doc topic).
- Describe the trace: what you ran, what was wrong, what is different now.
- Do not commit secrets.

Pack ownership and versioning: [docs/reference/governance.md](docs/reference/governance.md).

## Issues

Useful issues name the skill, the artifact, and what the agent did that the quality bar forbids. “Add a PM agent” is not useful.
