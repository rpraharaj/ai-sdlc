---
name: plan-data-migration
description: >
  Plan expand-then-contract data migration slices. Use when the user
  asks for a migration plan, expand/contract, dual-write plan, or
  /plan-data-migration. Do not expand and contract in the same change.
  Do not run the migration.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2"
  stage: "40-build"
---

# Plan data migration

Order the **safe slices**. This is not `data-change` (that applies one slice) and not `write-integration-contract`.

Do not implement. Do not put expand and contract in one slice.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| The contract/shape itself | `write-integration-contract` |
| Apply one expand or one contract | `data-change` |
| Examples only | `write-api-examples` |

## Required inputs

- Current shape and desired shape (design, contract, or schema path)
- `AGENTS.md`

If you cannot name the current stored shape, **stop**.

## Human decisions (do not invent)

- Downtime window (default: none — expand/contract online)
- Backfill ownership

## Procedure

1. Read `AGENTS.md` if present. Read the current schema/contract and the desired one.
2. Find the home: `docs/data/migration-<slug>.md`.
3. Open [references/migration-template.md](references/migration-template.md). Copy every heading. Write `n/a` when unused.
4. Slices in order: expand (add) → dual-write/read if needed → backfill → switch readers → contract (remove). Each slice separately reviewable.
5. Each slice names the later `data-change` (or sibling skill) and a rollback sentence.
6. No secret values.

## Output

- Path: `docs/data/migration-<slug>.md`
- Template: `references/migration-template.md`

## Quality bar

- [ ] Current and desired shapes are named
- [ ] Expand and contract are different slices
- [ ] Each slice has a rollback sentence
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Slice count
3. Next skill: `data-change` on slice 1
