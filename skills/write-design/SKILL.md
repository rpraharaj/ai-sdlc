---
name: write-design
description: >
  Write a technical design for one initiative — approach, contracts,
  failure, security, and delivery slices. Use when the user asks for a
  technical design, tech spec, or how we will build this. Do not write
  product code. Do not design a one-line bug.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.4.0"
  stage: "30-design"
---

# Write design

Describe **how this initiative** will be built in **this** repository. This is not a PRD, not `write-architecture`, and not `write-dev-tasks`.

Do not implement. Do not start coding “just the first slice.”

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Why / success still open | `write-prd` |
| New system boundaries / greenfield shape | `write-architecture` |
| One sticky library/store choice | `record-decision` |
| One small already-clear change | `shape-work` |
| Break an existing design into tickets | `write-dev-tasks` |

If product why is unknown, **stop** and run `write-prd`. If slice 1 is the whole goal, offer `shape-work`.

## Required inputs

- PRD and/or architecture if they exist
- Applicable requirements, contracts, and NFR paths with source revisions. For an initiative with Must requirements, missing requirements or approval evidence → stop and name `write-requirements`; a small clear slice may use `shape-work` with an explicit reason.
- `AGENTS.md`. Skim entry points and an existing pattern.

## Human decisions (do not invent)

- Product forks, compatibility, environment
- Breaking contract changes

## Procedure

1. Read `AGENTS.md`, applicable requirements/contracts/NFRs, and the named PRD/architecture. Check prerequisite approvals or explicit waivers against `context/decision-rights.md`; do not design from an unapproved or stale baseline.
2. Find the home: first existing `docs/design/`, `docs/designs/`, `docs/specs/`, or a path `AGENTS.md` names. Name: `docs/design/YYYY-MM-DD-<slug>.md`.
3. Open [references/design-template.md](references/design-template.md). Copy every heading. Write `n/a` when unused.
4. Approach names real files, types, or layers — or says none exist. Data/contracts stay expand-then-contract. Config is names only, never secret values. Delivery is ordered slices; do not write full tickets (`write-dev-tasks`).
5. Load `engineering-bar` (`../engineering-bar/SKILL.md`). Check Minimum path, Failure, Data, Security, UI. Do not paste the bar.
6. Map every applicable Must id to an approach/design slice, contract, and verification plan. A trace is artifact path + local id, qualified by source revision; do not renumber upstream ids. Uncovered Must items are blocking questions, not silent omissions. Keep design status draft until the authorized human's approval evidence exists.

## Output

- Path: `docs/design/YYYY-MM-DD-<slug>.md`
- Template: `references/design-template.md`

## Quality bar

- [ ] An engineer could start slice 1 without guessing the approach
- [ ] Alternatives include a smaller option (reuse / stdlib / native)
- [ ] At least one Delivery slice is smaller than the whole initiative
- [ ] Unused headings are `n/a`
- [ ] Every applicable Must is covered or explicitly blocked; input revisions and prerequisite approval evidence are named

## Done

1. Path
2. Chosen approach in a few sentences
3. Slice 1 and the next skill (`write-dev-tasks` or `shape-work`)
