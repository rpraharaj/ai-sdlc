---
name: fix-ci
description: >
  Make a failing pipeline check green by reproducing it locally and
  fixing the cause. Use when CI failed, a required check is red, or the
  user pastes a failing job log. Do not skip, delete, or weaken the
  failing test to get green.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3"
  stage: "60-release"
---

# Fix CI

Green the **same check** that failed. This is `debug` aimed at a pipeline job.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Review pipeline design | `review-pipeline` |
| Local failure with a repro | `debug` |
| Passes locally, failed in CI, and you cannot compare env | stop — do not guess |

## Required inputs

- Check/job name, command the job ran, error text
- `AGENTS.md`

If you cannot name the command, **stop**.

## Human decisions (do not invent)

- Disabling the job (forbidden)

## Procedure

1. Identify the check from the log or workflow file.
2. Reproduce locally with the same command or the closest AGENTS.md Test/Lint/Typecheck/Build.
3. Fix the cause via `debug`. Forbidden: delete/skip/weaken the test, `continue-on-error`, `--no-verify` as the solution.
4. Re-run the same local command. It must pass. Run neighboring checks if cheap.

## Output

- Path: reply
- Template: [references/fix-ci-report.md](references/fix-ci-report.md)

## Quality bar

- [ ] Same command is green locally
- [ ] Job still enabled
- [ ] Assertions still strict

## Done

Fill the report. Push only if they asked.
