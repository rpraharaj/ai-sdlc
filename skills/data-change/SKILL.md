---
name: data-change
description: >
  Plan and apply a schema, API, or data migration using
  expand-then-contract. Use when adding or changing columns, indexes,
  events, protobuf or OpenAPI shapes, or backfills. Do not expand and
  contract in the same change.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3.0"
  stage: "40-build"
---

# Data change

Change stored or published shape **without breaking current readers**. For a multi-slice plan, `plan-data-migration` orders the slices; this skill applies **one** step.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Ordered expand/dual-write/contract plan | `plan-data-migration` first |
| Examples only | `write-api-examples` |
| No migrator in the repo and they need one | stop — do not invent a framework |

## Required inputs

- Current and desired shape (or the current `plan-data-migration` slice)
- `AGENTS.md`

## Human decisions (do not invent)

- Running a destructive migration against shared/prod
- Combining expand and contract (forbidden)

## Procedure

1. Detect how this repo migrates from existing folders. Do not add a new migrator.
2. Classify: **expand** | **backfill** | **contract**. Default to expand. Rename/drop is three later changes, not one.
3. Write the plan from [references/data-change-plan.md](references/data-change-plan.md). Destructive contract with expand is a fail. Unbounded backfill without batches is a fail.
4. Apply **only** the current step. Match existing migration naming. Load `engineering-bar`. Prove with this repo’s tests plus the verification check in the plan.

## Output

- Path: reply plan + migration files
- Template: `references/data-change-plan.md`

## Quality bar

- [ ] Step is one of expand / backfill / contract
- [ ] Expand and contract are not in the same change
- [ ] Rollback sentence exists
- [ ] Commands run are recorded

## Done

1. Plan + step executed
2. Files added
3. What a later change must do
