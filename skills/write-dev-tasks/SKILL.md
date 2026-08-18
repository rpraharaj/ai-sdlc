---
name: write-dev-tasks
description: >
  Break a PRD or technical design into ordered tasks with yes/no
  acceptance. Use when the user asks for tickets, a task breakdown,
  detailed dev tasks, or a work plan. Do not write product code. Do not
  invent a backlog for a one-file change.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3"
  stage: "20-shape"
---

# Write dev tasks

Turn an agreed **what/how** into ordered slices. This is not a PRD, not a design, and not `shape-work`.

Do not implement. Do not open tracker issues unless the user asked and a tracker CLI this repo already uses works.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Product why still open | `write-prd` |
| How still open | `write-design` |
| Exactly one small slice | `shape-work` |
| Start coding | `implement-change` |

If there is only one small task, **stop** and run `shape-work`.

## Required inputs

- PRD and/or design the user pointed at
- `AGENTS.md`

If none exists and the work is large, **stop** and offer `write-prd` or `write-design`.

## Human decisions (do not invent)

- Opening tracker issues
- Parallelism that shares a contract

## Procedure

1. Read `AGENTS.md` and the named PRD/design.
2. Find the home: first existing `docs/tasks/`, `docs/dev/`, a path `AGENTS.md` names, or a sibling of the design. Name: `docs/tasks/<slug>.md`.
3. Open [references/dev-tasks-template.md](references/dev-tasks-template.md). Copy every heading. Write `n/a` when unused.
4. Each task: one kind, one next skill, yes/no acceptance, real likely files or “could not find”, traces to PRD/design. No drive-by world refactor inside a feature task.
5. Order is dependency-real (expand before readers). Parallel only with no shared contract.

## Output

- Path: `docs/tasks/<slug>.md`
- Template: `references/dev-tasks-template.md`

## Quality bar

- [ ] Task 1 is the smallest slice that proves the approach
- [ ] Later tasks do not assume code Task 1 has not shipped
- [ ] Batch done would fail today
- [ ] Count is as small as the risks require

## Done

1. Path
2. Task count and first title
3. Next skill for Task 1: `shape-work` or `implement-change`
