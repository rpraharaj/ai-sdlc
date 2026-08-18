---
name: write-opportunity
description: >
  Write a 1-2 page opportunity brief — problem, evidence, bets, non-goals,
  and the ask. Use when the user wants an opportunity brief, a pitch, a
  problem statement, or /write-opportunity. Do not write a PRD, requirements,
  or product code.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.1"
  stage: "10-discover"
---

# Write opportunity

Capture **whether this is worth a PRD**. This is not a PRD (`write-prd`), not requirements (`write-requirements`), and not a status update (`write-status`).

Do not implement. Do not invent users, market size, or competitors.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Why / who / success are already agreed | `write-prd` |
| Interview notes to distill | `synthesize-discovery` first, then this (or skip this if a PRD is the next artifact) |
| One-line bug or tiny change | `shape-work` |
| How we will build it | `write-design` |
| Status / RAG | `write-status` |

If the ask is already a committed initiative with success checks, say so and offer `write-prd`.

## Required inputs

- A problem the user can point at (ticket, incident, quote, metric this program already has, or a written complaint)
- `AGENTS.md` if present; `context/glossary.md` and `context/systems-of-record.md` if they exist

If there is **no** evidence — only a solution idea — stop and ask for the hurt. Do not invent the hurt.

## Human decisions (do not invent)

- Whether the program will spend discovery or PRD time on this
- Who the audience is, if not already in context
- Any numeric target that is not already measured

## Procedure

1. Read `AGENTS.md` if present. Read `context/` files it points at. Use terms as the glossary defines them.
2. Find the home: first existing `docs/discover/`, a path `AGENTS.md` names, or offer to create `docs/discover/`.
3. Name the file like existing briefs. If none, `docs/discover/YYYY-MM-DD-<slug>.md`.
4. Open [references/opportunity-template.md](references/opportunity-template.md). Copy every heading. Write `n/a` when unused. Do not add sections.
5. Fill only from the user and files you read:
   - **Problem** is a hurt, not a feature.
   - **Evidence** names sources (path, ticket id, quote). No source → `unknown`, not a story.
   - **Bets** are optional ways to respond, not a design.
   - **Non-goals** is non-empty.
   - **Ask** is the next human decision (fund a PRD, run discovery, drop it).
6. No secrets. No invented vendors or SLOs.

## Output

- Path: `docs/discover/YYYY-MM-DD-<slug>.md` (or the existing discover home)
- Template: `references/opportunity-template.md`

## Quality bar

- [ ] Problem can be read without guessing the solution
- [ ] At least one evidence line names a real source, or is explicitly `unknown`
- [ ] Non-goals is non-empty
- [ ] Ask names a next skill or a human stop
- [ ] Unused headings are `n/a`, not deleted

## Done

1. Path or the full text in the reply
2. The problem in one sentence
3. Next skill: usually `synthesize-discovery` if evidence is raw, else `write-prd`, else stop — need user
