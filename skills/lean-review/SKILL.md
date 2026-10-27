---
name: lean-review
description: >
  Review a diff or repo for unnecessary complexity only — delete-list of
  reinvented stdlib, unneeded deps, speculative abstractions. Use when
  the user asks what to delete, whether this is over-engineered, a
  simplify review, or a bloat audit. Do not edit product code.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3.0"
  stage: "50-verify"
---

# Lean review

Hunt **complexity that does not need to exist**. Not correctness (`review-change`), security, or performance.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Bugs / bar failures | `review-change` |
| Apply the cuts | `refactor-safely` / `implement-change` |

## Required inputs

- Current diff, or the whole tree if they said “audit”
- `engineering-bar` Minimum path + Never cut

If the target is empty, **stop**.

## Human decisions (do not invent)

- Applying cuts (not this skill)

## Procedure

1. Collect the diff or scan the tree (skip `node_modules`, `.git`, vendored/build).
2. One line per finding: `<file>:<line>: <tag> <what to cut>. <what replaces it>.`
3. Tags: `delete` | `stdlib` | `native` | `yagni` | `shrink`. See [references/tags.md](references/tags.md).
4. Do not flag trust-boundary validation, the focused test for new logic, or correctness/security/perf bugs (name the other skill).
5. Rank biggest cut first. End with `net: -<N> lines`. Nothing to cut: `Lean already.`

## Output

- Path: reply
- Template: `references/tags.md`

## Quality bar

- [ ] Product code not edited
- [ ] Tags from the table only
- [ ] Never-cut items absent from the list

## Done

The delete-list or `Lean already.`
