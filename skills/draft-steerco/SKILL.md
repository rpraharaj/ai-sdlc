---
name: draft-steerco
description: >
  Draft a steerco pack from status, RAID, and change assessments only.
  Use when the user asks for a steerco deck, steering brief, or
  /draft-steerco. Do not add facts that are not in those files. Do not
  invent RAG.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2"
  stage: "70-govern"
---

# Draft steerco

Decisions asked, options, recommendation — **no new facts**. This is not `write-status` and not `assess-change`.

Do not invent RAG or progress.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Weekly one-pager | `write-status` |
| Impact of a change | `assess-change` first |
| RAID update | `update-raid` |

## Required inputs

- Latest `docs/govern/status-*.md`
- `docs/govern/raid.md`
- Any open `docs/govern/change-*.md`

If status is missing, **stop** and run `write-status` first.

## Human decisions (do not invent)

- RAG they will present
- Which recommendation they adopt

## Procedure

1. Read `AGENTS.md` if present. Read status, RAID, and open change assessments. Nothing else becomes a fact.
2. Find the home: `docs/govern/steerco-YYYY-MM-DD.md`.
3. Open [references/steerco-template.md](references/steerco-template.md). Copy every heading. Write `n/a` when unused.
4. Each decision asked cites a change file or RAID id. Options include reject.
5. RAG stays `unassigned` unless the status already has a human-set RAG — then copy it and cite status.

## Output

- Path: `docs/govern/steerco-YYYY-MM-DD.md`
- Template: `references/steerco-template.md`

## Quality bar

- [ ] Status path is named
- [ ] Every fact cites status, RAID, or a change file
- [ ] No new metric or date
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Decisions-asked count
3. Next: human sends it; then `update-raid` if they decided
