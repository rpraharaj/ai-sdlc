---
name: implement-change
description: >
  Implement a scoped change in this repository using existing patterns.
  Use when the user wants a feature, bug fix, or code change applied and
  the ask is already shaped or is a clear small change. Do not claim
  done without command output.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3"
  stage: "40-build"
---

# Implement change

Apply the smallest change that satisfies the request. Do not orchestrate other agents unless the user asked.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Empty tree / no app | `start-project` |
| Vague ask, several product decisions | `shape-work` first |
| Production incident | `incident-triage` |
| Known failure, find the cause | `debug` |

A clear small change (one behavior, likely files obvious) does not need a shape document.

## Required inputs

- A shaped task or a clear small change
- `AGENTS.md` commands

## Human decisions (do not invent)

- Adding a new dependency when a lower rung would do (say why if you add one)
- Waiving an engineering-bar fail

## Procedure

1. Read `AGENTS.md`. Use its commands.
2. If the workspace has no product (only bootstrap files), **stop** and run `start-project`.
3. If the request is vague, run `shape-work` and stop unless they already told you to implement the result.
4. Load `../engineering-bar/SKILL.md`. Climb Minimum path. Search this repo for an existing helper first.
5. Bug fix: find every caller; fix the shared cause once.
6. Touch only files the request and its tests need. No drive-by refactors. Do not edit generated paths in `AGENTS.md`.
7. Prove: focused test, then **Test**, then **Lint** / **Typecheck** if known. Never claim pass without this session’s output. Missing tests → `write-tests`. UI → `verify-ui`.
8. Walk the diff against `engineering-bar`. Fix fails or get an explicit waiver.

## Output

- Path: the product diff
- Template: [references/implement-report.md](references/implement-report.md)

## Quality bar

- [ ] Acceptance checks pass or were not specified
- [ ] Commands run are listed with exit status
- [ ] No secrets
- [ ] Engineering-bar fails are fixed or waived

## Done

Fill the report template. Do not commit unless asked. Next: `write-tests` / `verify-ui` / `ready-to-merge`.
