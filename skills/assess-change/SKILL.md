---
name: assess-change
description: >
  Assess impact of a scope, date, or design change against current
  artifacts. Use when the user asks for a change request, impact
  assessment, re-plan, or /assess-change. Do not accept the change.
  Do not invent capacity or dates.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.1.0"
  stage: "70-govern"
---

# Assess change

Show **what breaks if we say yes**. This is not status (`write-status`), not RAID (`update-raid` — update RAID after the human decides), and not a new PRD.

Do not implement. Do not treat the change as accepted.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| New problem, no current plan | `write-opportunity` / `write-prd` |
| Weekly RAG | `write-status` |
| Add a risk without a proposed change | `update-raid` |
| Technical design of the new shape | `write-design` after a human accepts |

## Required inputs

- The proposed change in one paragraph (from the user)
- The current baseline: PRD and/or plan and/or RAID — at least one path
- `context/decision-rights.md` (who may accept)

If there is no baseline artifact, **stop**. You cannot assess impact against a blank.

## Human decisions (do not invent)

- Accept, accept-with-conditions, or reject
- New date or budget
- Must vs Should if scope moves

## Procedure

1. Read `AGENTS.md` if present. Read `context/decision-rights.md` if present.
2. Read the baseline artifacts the user named (PRD, requirements, plan, RAID, contracts).
3. Find the home: `docs/govern/change-YYYY-MM-DD-<slug>.md`.
4. Open [references/change-template.md](references/change-template.md). Copy every heading. Write `n/a` when unused.
5. List impacts only where you can name a file or RAID id:
   - scope (requirements that move)
   - date (only if a date already exists — do not invent a new one)
   - contracts / NFR / UAT
   - teams (from process map or systems-of-record)
6. Options: at least **accept as asked**, **smaller alternative**, **reject**. Recommendation is allowed; **decision stays `unassigned`**.
7. After the human decides, next is `update-raid` and, if accepted, the skill that updates the moved artifact (`write-requirements`, `write-prd`, …).

## Output

- Path: `docs/govern/change-YYYY-MM-DD-<slug>.md`
- Template: `references/change-template.md`

## Quality bar

- [ ] Baseline paths are named
- [ ] Every impact cites a file or RAID id
- [ ] Three options exist, including reject
- [ ] Decision is `unassigned` unless the user already decided
- [ ] No invented date or headcount
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Impact count
3. Next: human decision, then `update-raid` and the skill for the moved artifact
