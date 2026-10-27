---
name: map-dependencies
description: >
  Map team × system × date dependencies from process, contracts, and
  RAID. Use when the user asks for a dependency map, cross-team
  dependencies, or /map-dependencies. Do not invent dates or teams.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2.0"
  stage: "70-govern"
---

# Map dependencies

One picture of **who waits on whom**. This is not RAID (`update-raid` still holds status) and not architecture.

Do not invent dates or teams.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Payload between systems | `write-integration-contract` |
| Process steps | `map-process` |
| Open risk/issue rows | `update-raid` |

## Required inputs

- At least one of: process map, contracts, RAID dependencies
- `context/systems-of-record.md` if it exists

If none of those exist, **stop**.

## Human decisions (do not invent)

- Needed-by dates that are not already on RAID or a plan

## Procedure

1. Read `AGENTS.md` if present. Read process map, contracts, RAID, systems-of-record.
2. Find the home: `docs/govern/dependencies.md` (one file, update in place).
3. Open [references/dependencies-template.md](references/dependencies-template.md). Copy every heading. Write `n/a` when unused.
4. Each edge: from team/system, to team/system, what (contract or RAID id), needed-by (sourced or `unknown`).
5. Flag missing contracts as `gap`.

## Output

- Path: `docs/govern/dependencies.md`
- Template: `references/dependencies-template.md`

## Quality bar

- [ ] Every edge cites process, contract, or RAID
- [ ] Dates are sourced or `unknown`
- [ ] Systems match systems-of-record or are marked `not in systems-of-record`
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Edge count + gap count
3. Next skill: `write-integration-contract` for gaps; `update-raid` for dates
