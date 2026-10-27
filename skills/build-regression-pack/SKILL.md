---
name: build-regression-pack
description: >
  Name the tests that must run for this release train, from evidence.
  Use when the user asks for a regression pack, release test set, or
  /build-regression-pack. Do not invent tests that do not exist. Do not
  claim they passed unless this session ran them.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3.0"
  stage: "50-verify"
---

# Build regression pack

List **what must run** for this train. This is not `write-tests` and not `ready-to-merge` for a single diff.

Do not invent tests. Do not claim pass without command output.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| New cases for a feature | `write-test-plan` / `write-tests` |
| One change merge-ready | `ready-to-merge` |
| UAT | `plan-uat` |

## Required inputs

- Release range or train name
- Existing tests in the repo and/or `docs/qa/plan-*.md`
- `AGENTS.md` test command

## Human decisions (do not invent)

- What may be skipped this train (waiver)

## Procedure

1. Read `AGENTS.md` if present. List test commands it records.
2. Read the commit range or the user-named features. Map to existing test files or plan ids.
3. Find the home: `docs/qa/regression-<slug>.md`.
4. Open [references/regression-template.md](references/regression-template.md). Copy every heading. Write `n/a` when unused.
5. Each item: how to run (from `AGENTS.md` or a real file path), why it is in (feature / risk). Missing coverage → `gap`, not a fake test name.
6. Result column stays `not run` unless this session ran the command.
7. When asked to execute the existing list, use a separate verifier handoff: run every required item against the exact release revision in the recorded environment and attach output and exit status. Missing, failed, unknown, or not-run items and uncovered risks block release unless the authorized human records a waiver using `context/decision-rights.md`. A completed test list alone is not release evidence.

## Output

- Path: `docs/qa/regression-<slug>.md`
- Template: `references/regression-template.md`

## Quality bar

- [ ] Every run item is a real path or `AGENTS.md` command
- [ ] Gaps are listed, not papered over
- [ ] No pass without this session’s output
- [ ] Release handoff distinguishes the planned list from executed results and names the exact revision
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Item count + gap count
3. Next skill: run via `verifier`; `write-tests` for gaps; `cut-release` after go/no-go
