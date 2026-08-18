---
name: write-docs
description: >
  Write or update documentation that matches this repository — README,
  API docs, or runbooks — from the code that exists. Use when the user
  asks for docs, README, API reference, or a runbook. Do not invent
  features the code does not have.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3"
  stage: "40-build"
---

# Write docs

Document **what the code does**. This is not `record-decision` and not `ship-notes`.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Why we chose X | `record-decision` |
| What shipped | `ship-notes` |
| PRD | `write-prd` |
| Architecture | `write-architecture` |
| Tech spec | `write-design` |
| Tickets | `write-dev-tasks` |
| Operational diagnose/mitigate | `write-runbook` if that is the artifact |

## Required inputs

- The code and existing docs you will touch
- `AGENTS.md`

## Human decisions (do not invent)

- Switching the repo to a new doc system (do not)

## Procedure

1. Read `AGENTS.md`. Pick the home that already exists (README, `docs/`, OpenAPI, runbooks).
2. Follow heading level and tone of the nearest existing doc.
3. Commands come from `AGENTS.md` or a file you opened. Never invent `npm test`.
4. Public behavior comes from handlers, types, and tests. Mark unknowns. No secrets.
5. Open [references/docs-notes.md](references/docs-notes.md) only if you need the kind table expanded. Prefer the smallest file that answers the ask.

## Output

- Path: existing README / docs home
- Template: `references/docs-notes.md`

## Quality bar

- [ ] No invented APIs, flags, or metrics
- [ ] Commands are evidenced
- [ ] Secrets absent

## Done

1. Kind and path
2. What you documented
3. What you left out (and which skill owns it)
