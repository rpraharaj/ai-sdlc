---
name: plan-uat
description: >
  Plan user acceptance testing — scope, data, scripts, and exit criteria.
  Use when the user asks for a UAT plan, acceptance scripts, business
  test pack, or /plan-uat. Do not invent sign-off. Do not write product code.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.1"
  stage: "50-verify"
---

# Plan UAT

Give the business a **pack they can run and sign**. This is not a test strategy (`write-test-strategy`), not automated tests (`write-tests`), and not go-live (`cut-release`).

Do not implement. Do not invent exit criteria or signers.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Layers and what we will not automate | `write-test-strategy` |
| Automated cases | `write-tests` or `write-test-plan` |
| Process as-is / to-be | `map-process` first |
| Production release | `cut-release` after UAT exit is signed |

## Required inputs

- Requirements path (Must items)
- Process map if the change crosses teams (`map-process`)
- `context/decision-rights.md` and `context/environments.md` if they exist

If Must requirements do not exist, **stop** and name `write-requirements`. Do not write UAT against a slide deck.

## Human decisions (do not invent)

- Who signs UAT (`decision-rights` or the user)
- Exit criteria if not already on the PRD success checks
- Whether production-like data may be used (default: no live personal data)

## Procedure

1. Read `AGENTS.md` if present. Read `context/decision-rights.md` and `context/environments.md` if present.
2. Read requirements (Must) and the process map. Each UAT script traces to a Must id.
3. Find the home: first existing `docs/qa/`, or offer to create it. Name: `docs/qa/uat-<slug>.md`.
4. Open [references/uat-template.md](references/uat-template.md). Copy every heading. Write `n/a` when unused.
5. Scripts: actor, steps, data (synthetic), expected. Happy, empty, and deny/error when the requirement has those journeys.
6. Environment must be a name from `environments.md` or `unknown`.
7. Data: synthetic only unless a human explicitly allows otherwise. Never put live personal data or secrets in the pack.
8. Exit: reuse PRD success checks when they exist. Otherwise `unknown — need human`.

## Output

- Path: `docs/qa/uat-<slug>.md`
- Template: `references/uat-template.md`

## Quality bar

- [ ] Every script traces to a Must requirement id
- [ ] Signer is named from decision-rights or marked `unassigned — need human`
- [ ] Exit criteria are PRD success checks or `unknown — need human`
- [ ] Data is synthetic or an explicit human waiver
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Script count
3. Next skill: wait for human sign-off, then `cut-release` / `ship-notes` as the program uses them
