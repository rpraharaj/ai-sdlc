---
name: diff-environments
description: >
  Diff declared environments against what you can observe. Use when the
  user asks for environment drift, env diff, config drift, or
  /diff-environments. Do not invent production values. Do not change
  any environment.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2"
  stage: "60-release"
---

# Diff environments

Compare **declared vs observed**. This is not a deploy and not `plan-rollback`.

Do not invent prod values. Do not change an environment.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| How promotion works | fill `context/environments.md` |
| Spoken rollback | `plan-rollback` |
| Pipeline jobs | `review-pipeline` |

## Required inputs

- `context/environments.md` (if missing, stop and say to fill it)
- Whatever config or status you can actually read (files, user paste). Do not guess live prod.

## Human decisions (do not invent)

- Whether a drift is allowed

## Procedure

1. Read `AGENTS.md` if present. Read `context/environments.md`.
2. Read observable config only (repo files, user-provided output). Mark anything you did not see as `not observed`.
3. Find the home: `docs/ops/env-diff-YYYY-MM-DD.md`.
4. Open [references/env-diff-template.md](references/env-diff-template.md). Copy every heading. Write `n/a` when unused.
5. No secret values in the table — names of vars only.

## Output

- Path: `docs/ops/env-diff-YYYY-MM-DD.md`
- Template: `references/env-diff-template.md`

## Quality bar

- [ ] `environments.md` was read or the skill stopped
- [ ] Unseen values are `not observed`, not invented
- [ ] No secret values
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Drift count + not-observed count
3. Next skill: human; then `implement-change` if they want config alignment
