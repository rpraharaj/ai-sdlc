---
name: write-nfr
description: >
  Write measurable non-functional requirements or mark them unknown.
  Use when the user asks for NFRs, SLOs, quality attributes, performance
  or security targets, or /write-nfr. Do not invent numbers. Do not write
  product code.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.1.0"
  stage: "30-design"
---

# Write NFR

Record **quality attributes as numbers or as unknown**. This is not a PRD, not architecture, and not a test plan.

Do not implement. Do not invent SLOs, SLAs, or baselines.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Functional behavior | `write-requirements` |
| Durable system shape | `write-architecture` |
| How this initiative is built | `write-design` |
| What we will and will not automate | `write-test-strategy` |
| PII classification of a change | `classify-data` |

## Required inputs

- A PRD and/or requirements path, **or** an architecture doc for an existing system
- `AGENTS.md`; `context/environments.md` if it exists

If the user says “it must be fast/secure/scalable” with no number and no existing baseline, write `unknown` and stop for a human target. Do not pick industry-typical numbers.

## Human decisions (do not invent)

- Any numeric target that is not already in the repo, the PRD, or a signed architecture doc
- What happens if a target is missed (error budget / reject traffic / unknown)

## Procedure

1. Read `AGENTS.md` if present. Read `context/environments.md` if present.
2. Read the named PRD, requirements, and architecture. Collect quality attributes they already state.
3. Find the home: first existing `docs/nfr/`, or offer to create it. Name: `docs/nfr/<slug>.md`.
4. Open [references/nfr-template.md](references/nfr-template.md). Copy every heading. Write `n/a` when unused.
5. For each category in the template: either a number **with its source** (path or “user-set”), or `unknown`.
6. Do not specify implementation (caches, vendors, instance sizes). That is `write-design`.
7. Point at environments by the names in `context/environments.md`. Do not invent prod URLs.

## Output

- Path: `docs/nfr/<slug>.md`
- Template: `references/nfr-template.md`

## Quality bar

- [ ] Every numeric target names a source or is `unknown`
- [ ] No invented baseline
- [ ] No implementation or vendor choice presented as an NFR
- [ ] Unused headings are `n/a`
- [ ] At least one row is a real target or an explicit `unknown` the human must set

## Done

1. Path
2. How many targets vs unknowns
3. Next skill: `write-design`, `write-test-strategy`, or stop — need user for unknowns that block
