---
name: write-tests
description: >
  Add tests for a change using this repository's runner and style, at
  public seams, with independent expected values. Use when the user
  asks for tests or coverage, after an implementation, for a regression
  check, or for a red-green loop.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3"
  stage: "40-build"
---

# Write tests

Match **this** repository. Do not introduce a new test framework or folder layout.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Test strategy / what not to automate | `write-test-strategy` |
| Scripted case list | `write-test-plan` |
| Find why a test is red | `debug` |
| Behavior-preserving cleanup | `refactor-safely` |

Red-green: one failing test at a confirmed seam, then only enough code to pass. Do not write a bulk suite then implement.

## Required inputs

- The change or behavior to pin
- `AGENTS.md` **Test** command, or a runner from the manifest / existing tests

If you cannot find a runner or any existing test, say so. Ask before generating a new harness.

## Human decisions (do not invent)

- Creating a new harness when none exists

## Procedure

1. Read `AGENTS.md` Test command. Open 2–3 existing tests nearest the change. Copy naming, location, fixtures.
2. Name the **seam** (public boundary a caller already uses) in one line. Prefer an existing seam.
3. Smallest set that would have failed before the change: happy, edge, error if the change handles failure.
4. Do not add tautologies, private-method tests, or “does not throw” only. Expected values are independent literals or spec examples.
5. Put tests next to existing ones of the same kind. Run the focused file, then repo **Test** if known. Keep output.

## Output

- Path: test files next to existing tests
- Template: [references/tests-report.md](references/tests-report.md)

## Quality bar

- [ ] Seam named
- [ ] Runner is this repo’s
- [ ] Command output recorded (or unverified)
- [ ] No new framework

## Done

Fill the report. Do not commit unless asked.
