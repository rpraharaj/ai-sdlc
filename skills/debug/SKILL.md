---
name: debug
description: >
  Diagnose a failure with a tight red loop first, then hypothesise, fix
  the shared cause, and prove it. Use when something is broken, a test
  fails, a bug is reported, or the user asks to debug or find the root
  cause. Do not shotgun-edit.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3.0"
  stage: "40-build"
---

# Debug

Find the cause of a known failure. Do not start a feature while debugging. Do not theorise without a command that can go red on **this** bug.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Live prod impact | `incident-triage` first |
| No expected/actual | `triage-defect` then return |
| Add tests after the cause is known | `write-tests` |

## Required inputs

- Expected, actual, and a repro command or the shortest UI/API steps
- Or captured production evidence from `incident-triage`

If you have neither a repro nor that evidence, **stop**.

## Human decisions (do not invent)

- Destructive data repairs

## Procedure

1. Read `AGENTS.md`. Redact secrets (`<REDACTED>`).
2. Pin expected / actual / repro. Write them down.
3. Build a **tight red loop** — one command you have already run that asserts the user’s symptom. Tests at a public seam first. If you cannot build a loop, list what you tried and stop.
4. Confirm it is the user’s failure. Minimise inputs until every leftover piece is load-bearing.
5. Write 3–5 falsifiable hypotheses, then test **one** at a time. Cap: five failed hypotheses → stop and report.
6. Fix the shared cause (every caller). Do not delete the failing test. Load `engineering-bar`. Prefer a failing test at the seam **before** the fix (`write-tests`).
7. Re-run the original loop. Remove tagged debug logs. Run focused tests and repo **Test** if cheap.

## Output

- Path: reply (and a file only if asked)
- Template: [references/debug-report.md](references/debug-report.md)

## Quality bar

- [ ] Red-loop command and output exist
- [ ] Root cause names a file/symbol
- [ ] Tagged debug logs are gone
- [ ] Original loop is green or you stopped honestly

## Done

Fill the report. Next: `write-tests` / `ready-to-merge`.
