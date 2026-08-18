---
name: write-architecture
description: >
  Write a system architecture document — boundaries, data, control flow,
  and quality attributes. Use when the user asks for architecture,
  system design of the durable shape, or /write-architecture. Do not
  write product code. Do not architecture a local rename.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3"
  stage: "30-design"
---

# Write architecture

Describe the **durable shape**. This is not a PRD, not `write-design`, and not `record-decision`.

Do not implement. Do not invent services, stores, or SLOs this product does not have.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| What / why for users | `write-prd` |
| How this feature will be built | `write-design` |
| One sticky choice | `record-decision` |
| One implementable slice | `shape-work` |
| Local rename | stop — no architecture doc |
| Review an existing architecture file | `review-architecture` |

If the ask is a single feature inside a settled system, say so and offer `write-design`.

## Required inputs

- `AGENTS.md`. If the repo is unmapped, run `explore-codebase` or say the picture is incomplete.
- Existing apps/packages you can name, or an explicit greenfield

## Human decisions (do not invent)

- Quality targets not already in the repo or set by the user
- Irreversible vendor/store picks (draft options; `record-decision` after they choose)

## Procedure

1. Read `AGENTS.md`. Map current apps, packages, stores from the tree.
2. Find the home: first existing `docs/architecture/`, `docs/arch/`, `architecture/`, or a path `AGENTS.md` names. Name: `docs/architecture/<area>.md`.
3. Open [references/architecture-template.md](references/architecture-template.md). Copy every heading. Write `n/a` when unused.
4. Boundaries are things that can fail or deploy apart. Quality attributes use numbers this repo has or user-set targets — else `unknown` / `n/a`. Alternatives include keep-current when a system exists.
5. Point sticky choices at `record-decision`.

## Output

- Path: `docs/architecture/<area>.md`
- Template: `references/architecture-template.md`

## Quality bar

- [ ] A new engineer could name where a request enters and where data lives
- [ ] Proposed shape is smaller than a platform rewrite unless asked
- [ ] Unused sections are `n/a`
- [ ] No secrets, no invented vendors

## Done

1. Path or full text
2. Proposed shape in a few sentences
3. Which ADRs should follow (or none)
