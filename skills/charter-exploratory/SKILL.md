---
name: charter-exploratory
description: >
  Write time-boxed exploratory test charters from named risks. Use when
  the user asks for exploratory testing, charters, session-based test
  management, or /charter-exploratory. Do not invent risks. Do not
  declare pass without a charter log.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2.0"
  stage: "50-verify"
---

# Charter exploratory

Give testers a **mission and a clock**. This is not a case list (`write-test-plan`) and not `write-tests`.

Do not invent risks. Do not mark the charter passed until a log exists.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Scripted cases | `write-test-plan` |
| Strategy / layers | `write-test-strategy` |
| Defect write-up | `triage-defect` after the session |

## Required inputs

- Risks from `write-test-strategy` or the user (named)
- A time box per charter from the user (or `unknown — need human`)

## Human decisions (do not invent)

- Duration
- Whether the session found a ship blocker

## Procedure

1. Read `AGENTS.md` if present. Read the test strategy risks.
2. Find the home: `docs/qa/charter-<slug>.md`.
3. Open [references/charter-template.md](references/charter-template.md). Copy every heading. Write `n/a` when unused.
4. One charter per focused risk. Include: mission, time box, what to avoid, notes area for the session log.
5. If writing after a session, fill the log from what the tester said. Do not invent bugs.

## Output

- Path: `docs/qa/charter-<slug>.md`
- Template: `references/charter-template.md`

## Quality bar

- [ ] Each charter traces to a named risk
- [ ] Time box is user-set or `unknown — need human`
- [ ] Result is `not run` unless a log is present
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Charter count
3. Next skill: run the session, then `triage-defect` as needed
