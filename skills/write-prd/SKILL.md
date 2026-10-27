---
name: write-prd
description: >
  Write a product requirements document — problem, audience, goals,
  non-goals, and testable success. Use when the user asks for a PRD,
  product spec, requirements of what to build, or /write-prd. Do not
  write product code. Do not PRD a one-line bug.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.4.0"
  stage: "20-shape"
---

# Write PRD

Capture **what** to build and **why**. This is not `write-design`, not `write-architecture`, and not `shape-work`.

Do not implement. Do not invent users, metrics, or legal constraints.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| One-line bug or tiny change | `shape-work` or `implement-change` |
| How we will build an agreed product | `write-design` |
| System boundaries | `write-architecture` |
| Testable functional contract | `write-requirements` |
| Tickets from an existing PRD | `write-dev-tasks` |
| Pitch / problem not yet a PRD | `write-opportunity` |

If the ask is already tiny (one behavior, success is obvious), say so and offer `shape-work`.

## Required inputs

- A problem the user can point at, or an accepted opportunity brief
- `AGENTS.md`; `context/glossary.md` if present

## Human decisions (do not invent)

- Who it is for, if not in context
- Success numbers that are not already measured
- Must vs later

## Procedure

1. Read `AGENTS.md` if present. Skim the product enough to avoid inventing a second app.
2. Find the home: first existing `docs/prd/`, `docs/product/`, a path `AGENTS.md` names, or offer to create `docs/prd/`.
3. Name: `docs/prd/YYYY-MM-DD-<slug>.md`.
4. Open [references/prd-template.md](references/prd-template.md). Copy every heading. Write `n/a` when unused.
5. Problem is a hurt, not a solution. Non-goals is non-empty. Success checks are yes/no and at least one fails today. Do not invent a baseline.
6. Must / Should / Later — do not dump a wishlist into Must. Journeys cover happy, empty, and error when user-facing.
7. No secrets. Unknowns stay unknown.
8. Leave status `draft` or `review` until the authorized human signs problem and success. Record source revision and approval evidence using the home in `context/decision-rights.md`; an agent must not promote its own draft to accepted. If scope or success changes, invalidate affected downstream approval and verification.

## Output

- Path: `docs/prd/YYYY-MM-DD-<slug>.md`
- Template: `references/prd-template.md`

## Quality bar

- [ ] A stranger can tell shipped vs not from Success
- [ ] Non-goals is non-empty
- [ ] Requirements do not specify tables, frameworks, or folder layout
- [ ] Unused headings are `n/a`
- [ ] Next names a real skill
- [ ] Accepted status is backed by human approval evidence for this revision

## Done

1. Path or the full text in the reply
2. The problem in one sentence
3. Next skill: `write-requirements`, `write-architecture`, `write-design`, or `shape-work`
