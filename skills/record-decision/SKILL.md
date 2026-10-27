---
name: record-decision
description: >
  Capture a sticky technical decision as a one-page ADR — context,
  options, choice, consequences. Use when the user asks to record a
  decision, write an ADR, or lock a library, shape, or approach. Do not
  start a full design document.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.4.0"
  stage: "30-design"
---

# Record decision

Write a **short** ADR. This is not `write-design`, not `write-architecture`, and not `write-prd`.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| README / API / runbook | `write-docs` |
| What / why | `write-prd` |
| Durable system shape | `write-architecture` |
| How this initiative is built | `write-design` |
| Local rename / one-line fix | stop — no ADR |

Write when the choice is expensive to reverse. If the decision is not made, list options and **ask**. Do not pick when options trade product risk.

## Required inputs

- The choice (or the options) and why it came up
- `AGENTS.md`

## Human decisions (do not invent)

- Which option wins when they trade product risk

## Procedure

1. Read `AGENTS.md`. Link files/symbols you actually opened.
2. Find the home: first `docs/adr/`, `doc/adr/`, `adr/`, `docs/decisions/`, or a path `AGENTS.md` names. Number like existing ADRs; else `0001-<slug>.md`.
3. Open [references/adr-template.md](references/adr-template.md). Copy every heading. Write `n/a` when unused.
4. Options include “do nothing.” At least two. Decision is one option. If the user already chose, quote them.
   Keep status `proposed` until the authorized human decision and exact artifact revision are evidenced in the approval home named by `context/decision-rights.md`. Missing evidence → stop before claiming the choice is accepted. `this session` may describe an author, never the human decider. Changed options or consequences require affected approval again.
5. No secrets.

## Output

- Path: `docs/adr/NNNN-<slug>.md`
- Template: `references/adr-template.md`

## Quality bar

- [ ] At least two options including do-nothing or keep-current
- [ ] Decision is one option
- [ ] Consequences include what you give up and when to revisit
- [ ] Unused headings are `n/a`
- [ ] Accepted status has revision-bound human approval evidence; otherwise the decision remains proposed

## Done

1. Path or full text
2. Decision in one sentence
3. Next: `data-change` / `implement-change` / `write-docs` / `write-design` or stop
