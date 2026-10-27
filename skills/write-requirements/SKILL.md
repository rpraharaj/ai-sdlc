---
name: write-requirements
description: >
  Turn an approved PRD into testable functional requirements with traces
  and acceptance. Use when the user asks for requirements, a BRD, a
  functional spec, or /write-requirements. Do not write product code.
  Do not invent Must vs Should.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2.0"
  stage: "20-shape"
---

# Write requirements

Capture the **testable contract**. This is not a PRD (`write-prd`), not a technical design (`write-design`), and not a ticket list (`write-dev-tasks`).

Do not implement. Do not invent users, SLAs, or priority.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Why / who / success still open | `write-prd` |
| No PRD and the ask is a pitch | `write-opportunity` |
| Current vs future process | `map-process` |
| Measurable quality targets only | `write-nfr` |
| How we will build it | `write-design` |
| Tickets | `write-dev-tasks` |
| One small already-clear change | `shape-work` |

If there is no PRD (or the user cannot point at one), **stop**. Name `write-prd`. Do not write requirements from a conversation alone unless the user explicitly waives that and you record the waiver in the doc.

## Required inputs

- Path to the PRD (or the explicit waiver above)
- `AGENTS.md`; `context/glossary.md` and `context/systems-of-record.md` if they exist
- Human approval evidence for the PRD revision, or an explicit prerequisite waiver, following `context/decision-rights.md`. Missing, stale, or unassigned approval → **stop** even when a PRD file exists. An `accepted` label alone is insufficient.

## Human decisions (do not invent)

- Must vs Should vs Later
- Who in the business is accountable for each Must
- Legal / compliance wording

## Procedure

1. Read `AGENTS.md` if present. Read `context/glossary.md` and `context/systems-of-record.md` if present.
2. Read the PRD and verify the authorized human's approval or waiver for this revision. If decision rights or the signer cannot be established, stop. List its goals and Must/Should if it has them. Do not add goals the PRD does not have.
3. Find the home: first existing `docs/requirements/`, a path `AGENTS.md` names, or offer to create `docs/requirements/`.
4. Name: `docs/requirements/YYYY-MM-DD-<slug>.md`.
5. Open [references/requirements-template.md](references/requirements-template.md). Copy every heading. Write `n/a` when unused.
6. Each requirement:
   - id `R-…`
   - traces to a **PRD goal** (or a named PRD section)
   - acceptance that a stranger can check (command, UI observation, or API response)
   - priority only if the user or the PRD already set it; otherwise `unassigned` and stop for Must vs Should
7. Systems named must appear in `context/systems-of-record.md` or be marked `not in systems-of-record`.
8. No database-table design, framework choice, or folder layout (that is `write-design`). The requirements template's evidence tables are required. No secrets.

## Output

- Path: `docs/requirements/YYYY-MM-DD-<slug>.md`
- Template: `references/requirements-template.md`

## Quality bar

- [ ] PRD path is named at the top, or an explicit waiver is named
- [ ] The PRD revision has authorized human approval evidence, or a recorded prerequisite waiver; the agent did not grant approval
- [ ] Every Must traces to a PRD goal
- [ ] Every Must has a yes/no acceptance check
- [ ] At least one acceptance check would fail today
- [ ] Priority is not invented (`unassigned` or taken from the PRD/user)
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Count of Must / Should / unassigned
3. Next skill: `map-process`, `write-nfr`, `write-architecture` (new boundaries), or `write-design`
