---
name: refactor-safely
description: >
  Behavior-preserving cleanup — lock behavior with tests, refactor
  mechanically, re-run the same tests. Use when the user asks to
  refactor, clean up, simplify, or restructure without changing
  behavior.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3.0"
  stage: "40-build"
---

# Refactor safely

Change structure, not behavior. If they also want new behavior, stop and send that part to `shape-work` / `implement-change`.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| New behavior in the same ask | split — this skill is structure only |
| Tests are red before you start | `debug` |
| Delete-list only | `lean-review` first |

## Required inputs

- Named unit (files, package, endpoint)
- `AGENTS.md` Test command

## Human decisions (do not invent)

- Mixing a feature into the refactor (do not)

## Procedure

1. Pin behavior with existing tests. If coverage is too thin, add characterization tests via `write-tests` first. Run them — that green run is the baseline. If they are red, this is `debug`.
2. List mechanical steps. Climb `engineering-bar` Minimum path. No new framework, cache, or feature flags. Never delete trust-boundary checks to look smaller.
3. One cluster of moves, then re-run the same tests. Stay in the named unit plus callers.
4. Re-run characterization tests, then repo **Test** / **Lint** / **Typecheck** if known. If a conditional’s meaning changed, revert that part.

## Output

- Path: the structural diff
- Template: [references/refactor-report.md](references/refactor-report.md)

## Quality bar

- [ ] Baseline tests were green before the moves
- [ ] Same tests green after
- [ ] Diff is structural
- [ ] No mixed feature work

## Done

Fill the report. Next: `ready-to-merge` if they want it shipped.
