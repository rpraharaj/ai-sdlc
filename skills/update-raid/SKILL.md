---
name: update-raid
description: >
  Update the RAID log — risks, assumptions, issues, dependencies — from
  evidence. Use when the user asks to update RAID, add a risk, refresh
  assumptions, or /update-raid. Do not invent severity or green status.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.1.0"
  stage: "70-govern"
---

# Update RAID

Keep **one** RAID file honest. This is not a steerco deck (`draft-steerco`), not a weekly status (`write-status`), and not a change request (`assess-change`).

Do not invent risks, owners, or dates. Do not delete an open item without a human.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| One-page RAG for this week | `write-status` (read this RAID) |
| Scope/date/design change impact | `assess-change` |
| Steerco paper | `draft-steerco` |
| Cross-team contract map | `map-dependencies` |

## Required inputs

- Existing `docs/govern/raid.md` if it exists (create from the template if not)
- Evidence: named artifact, ticket id, git fact, or CI result
- `context/decision-rights.md` if it exists (for escalation)

If the user says “add a risk that we might be late” with no evidence, record it as an **assumption** or stop and ask what would tell us it is true.

## Human decisions (do not invent)

- Severity and owner
- Closing an item
- Date commitments

## Procedure

1. Read `AGENTS.md` if present. Read `context/decision-rights.md` if present.
2. Read `docs/govern/raid.md` if it exists. If not, offer to create `docs/govern/` and start from [references/raid-template.md](references/raid-template.md).
3. Open the template only to **keep every heading**. Do not drop columns.
4. Add or update only items with a source. Source = path, ticket id, or “user: <name>”.
5. Do not change owner, severity, or status to closed unless the user said so.
6. Dependencies name the other team or system from `context/systems-of-record.md` when possible.
7. After edits, `write-status` may run — do not write status inside this file beyond the item list.

## Output

- Path: `docs/govern/raid.md` (one file, updated in place)
- Template: `references/raid-template.md`

## Quality bar

- [ ] Every new or changed row has a source
- [ ] No closed item without a human
- [ ] No invented date or owner (`unassigned` is allowed)
- [ ] Headings from the template remain
- [ ] Secrets are absent

## Done

1. Path
2. Counts: open risks / assumptions / issues / dependencies
3. Next skill: `write-status` or `assess-change` if an item is a scope change
