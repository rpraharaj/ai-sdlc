---
name: prioritize-backlog
description: >
  Rank backlog items from written evidence only, and list what you
  rejected. Use when the user asks to prioritize, rank a backlog, apply
  RICE or WSJF, or /prioritize-backlog. Do not invent scores. Do not
  write product code.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2"
  stage: "10-discover"
---

# Prioritize backlog

Produce an **ordered list plus rejects**, scored only from artifacts you can open. This is not a PRD (`write-prd`) and not a status report.

Do not invent reach, impact, confidence, or job size.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Problem not written down | `write-opportunity` / `write-prd` |
| Raw interviews | `synthesize-discovery` first |
| Scope change to a committed plan | `assess-change` |
| Tickets for an agreed how | `write-dev-tasks` |

## Required inputs

- Two or more candidate items, each with a path (opportunity, PRD, synthesis insight, requirement)
- The scoring fields the user wants, or default: reach / impact / confidence / effort **only if those numbers exist in the artifacts or the user supplies them**

If an item has no artifact, drop it to **unscored** — do not guess.

## Human decisions (do not invent)

- Final rank if scores tie
- What “now” vs “later” means for this increment

## Procedure

1. Read `AGENTS.md` if present. Read `context/glossary.md` if present.
2. Read each named artifact. Copy numbers only if they appear there or the user typed them this session.
3. Find the home: `docs/discover/backlog-YYYY-MM-DD.md` (or the existing discover home).
4. Open [references/backlog-template.md](references/backlog-template.md). Copy every heading. Write `n/a` when unused.
5. Score only rows with complete inputs. Missing input → `unscored` + reason.
6. **Rejected** is required: items out of evidence, duplicates, or user-dropped.
7. Do not write tracker tickets unless the user asked and a tracker CLI already exists. Even then, link to this file.

## Output

- Path: `docs/discover/backlog-YYYY-MM-DD.md`
- Template: `references/backlog-template.md`

## Quality bar

- [ ] Every ranked row cites an artifact path
- [ ] No invented score field
- [ ] Rejected or unscored list is non-empty or explicitly `none`
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Ranked count / unscored count / rejected count
3. Next skill: `write-prd` or `write-dev-tasks` for item 1 — or stop — need user
