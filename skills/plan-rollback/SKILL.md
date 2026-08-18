---
name: plan-rollback
description: >
  Write a rollback plan that starts with one spoken sentence plus steps.
  Use when the user asks for a rollback plan, backout, or /plan-rollback.
  Do not invent environments. Do not perform the rollback.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2"
  stage: "60-release"
---

# Plan rollback

Make rollback something a human can **say and do**. This is not `cut-release` and not `incident-triage`.

Do not perform the rollback. Do not invent environments.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Cut the release | `cut-release` after this exists |
| Incident in progress | `incident-triage` then this if rollback is the mitigate |
| Diagnose steps | `write-runbook` |

## Required inputs

- What would be rolled back (tag, flag, migration slice)
- `context/environments.md` and `context/decision-rights.md`

If there is no named artifact to undo, **stop**.

## Human decisions (do not invent)

- Who may run production rollback
- Data rollback vs forward-fix when contract already contracted (default: say if data rollback is impossible)

## Procedure

1. Read `AGENTS.md` if present. Read environments and decision-rights.
2. Find the home: `docs/ops/rollback-<slug>.md`.
3. Open [references/rollback-template.md](references/rollback-template.md). Copy every heading. Write `n/a` when unused.
4. First line of the plan is one spoken sentence (“revert tag X”, “turn flag off”, “redeploy previous image”).
5. Steps use commands this repo already has, or `unknown`.
6. Agents do not run production steps.

## Output

- Path: `docs/ops/rollback-<slug>.md`
- Template: `references/rollback-template.md`

## Quality bar

- [ ] One spoken sentence exists
- [ ] Environment names come from context or `unknown`
- [ ] No unattended prod by an agent
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Spoken sentence
3. Next skill: human go/no-go then `cut-release`; or `incident` workflow
