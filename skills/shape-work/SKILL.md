---
name: shape-work
description: >
  Turn a vague request into a scoped task with in/out of scope and
  yes/no acceptance. Use when the user says shape this, scope this,
  stress-test the plan, or pastes a rough ask. Do not write product
  code. Do not start the first slice unless they asked to implement too.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3"
  stage: "20-shape"
---

# Shape work

Turn the ask into a task another session can implement without guessing. Do not edit product code.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Stack trace / “broken” | `debug` (shape the repro; do not skip it) |
| Production down / wrong data in prod | `incident-triage` |
| Empty tree / no app | `start-project` |
| What / why for users | `write-prd` |
| Durable system shape | `write-architecture` |
| How this initiative is built | `write-design` |
| Ticket list | `write-dev-tasks` |
| How does this code work | `explain-code` — no fake task |
| README / API / runbook only | `write-docs` |
| Pure question | Answer; no fake task |

If kind is incident or greenfield, **stop** and run that skill. If the workspace is only README / LICENSE / `.gitignore` / `AGENTS.md`, treat as greenfield.

If **kind is change**, several decisions are open, and they asked to think it through, prefer `write-prd` or `write-design` over a one-shot shape.

## Required inputs

- The user’s ask
- `AGENTS.md` if present. If the change is more than a few lines and the repo is unmapped, run `explore-codebase` or say knowledge is incomplete.

## Human decisions (do not invent)

- Product forks (who it is for, contradicting goals)
- Whether a smaller reuse option is enough

## Procedure

1. Read `AGENTS.md`. Skim only the files needed to name a real approach.
2. Decide the kind (table above). Ask at most a few **blocking** questions. Non-blocking go in the doc.
3. Large ambiguous **change**: decision pass — frontier questions with recommended answers; wait; do not invent lookup-able facts.
4. Write the document from [references/shaped-work-template.md](references/shaped-work-template.md). Every acceptance check is yes/no. No “works well.”
5. Save a file only if the user asked or the repo already keeps shapes (`docs/tasks/`). Otherwise print it.

## Output

- Path: reply, or `docs/tasks/<slug>-slice.md`
- Template: `references/shaped-work-template.md`

## Quality bar

- [ ] Out of scope is non-empty unless the ask is tiny
- [ ] At least one acceptance check would fail today (change/defect)
- [ ] First slice is smaller than the whole goal when there is more than one risk
- [ ] Likely files are real paths or you say you could not find them

## Done

1. The shaped work
2. Next skill — do not implement unless they said shape **and** implement and slice 1 is fully specified
