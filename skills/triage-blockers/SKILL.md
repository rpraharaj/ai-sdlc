---
name: triage-blockers
description: >
  Cluster blockers, name an owner, and escalate per decision-rights.
  Use when the user asks to triage blockers, stand-up blockers, or
  /triage-blockers. Do not invent owners. Update RAID rather than a
  second list.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2.0"
  stage: "70-govern"
---

# Triage blockers

Cluster and escalate. This is not `update-raid` (that writes the log) and not `assess-change`.

Do not keep a second blocker database. Prefer RAID ids.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Add a risk with evidence | `update-raid` |
| Scope/date change | `assess-change` |
| Weekly page | `write-status` after this |

## Required inputs

- Open issues/dependencies from `docs/govern/raid.md` and/or stand-up notes the user provides
- `context/decision-rights.md`

If RAID is missing and the user has no list, **stop** and offer `update-raid`.

## Human decisions (do not invent)

- Owner if not on the RAID row
- Escalate vs wait

## Procedure

1. Read `AGENTS.md` if present. Read RAID and decision-rights.
2. Cluster open issues/dependencies by theme (same system, same team).
3. Find the home: `docs/govern/blockers-YYYY-MM-DD.md` **and** tell the user to persist owners on RAID via `update-raid`.
4. Open [references/blockers-template.md](references/blockers-template.md). Copy every heading. Write `n/a` when unused.
5. Each cluster: RAID ids, owner (from RAID or `unassigned`), escalate to (from decision-rights) or `none`.

## Output

- Path: `docs/govern/blockers-YYYY-MM-DD.md`
- Template: `references/blockers-template.md`

## Quality bar

- [ ] Every cluster cites RAID ids or a user-named source
- [ ] No invented owner
- [ ] Escalate targets come from decision-rights or `none`
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Cluster count
3. Next skill: `update-raid` then `write-status`
