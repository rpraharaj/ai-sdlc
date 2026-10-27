---
name: write-status
description: >
  Write a one-page program or project status from RAID, git, and CI.
  Use when the user asks for a status report, RAG, weekly update, or
  /write-status. Do not invent progress or a green rating.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2.0"
  stage: "70-govern"
---

# Write status

Produce **one page a steerco can send**. This is not RAID maintenance (`update-raid`), not a change request (`assess-change`), and not release notes (`ship-notes`).

Do not invent progress. Every factual line cites RAID, git, CI, or a named artifact.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Add or close a risk | `update-raid` first |
| Scope/date/design change | `assess-change` |
| Decisions-asked paper for steerco | `draft-steerco` |
| What shipped in a tag | `ship-notes` |

## Required inputs

- `docs/govern/raid.md` if it exists (if missing, run or offer `update-raid` first — status may still list “RAID missing”)
- Evidence from git and from the test/CI command in `AGENTS.md` when those exist
- `context/decision-rights.md` if decisions are being asked

If the user wants “make it green,” **stop**. RAG is a human decision.

## Human decisions (do not invent)

- Overall RAG (red / amber / green)
- Which decisions they will actually ask this week

## Procedure

1. Read `AGENTS.md` if present. Read `context/decision-rights.md` if present.
2. Read `docs/govern/raid.md`. Summarize open items by id — do not rewrite RAID here.
3. Collect evidence:
   - git: what merged in the window the user named (or say you did not look)
   - CI / tests: read the existing result for the named revision, or request execution by `verifier`; coordinator does not run tests. Cite the command, revision, and result, or `(unknown)` / “not run”. Old results are not evidence for a newer revision.
4. Find the home: `docs/govern/status-YYYY-MM-DD.md` (new file per date).
5. Open [references/status-template.md](references/status-template.md). Copy every heading. Write `n/a` when unused.
6. Each highlight, slip, and decision-needed line cites an id or a command result.
7. Leave **RAG** as `unassigned — need human` unless the user set it.
8. No secrets. No “on track” without a cited fact.

## Output

- Path: `docs/govern/status-YYYY-MM-DD.md`
- Template: `references/status-template.md`

## Quality bar

- [ ] Every progress or slip line cites RAID, git, CI, or an artifact path
- [ ] RAG is user-set or `unassigned — need human`
- [ ] Open RAID counts match the RAID file you read, or RAID is marked missing
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Open RAID counts + whether RAG is assigned
3. Next skill: `assess-change` for items that need a decision; `draft-steerco` if they need a pack
