---
name: cut-release
description: >
  Cut a version and run this repository's existing release or deploy
  path. Use when the user asks to release, deploy, tag, publish, or
  ship to production. Do not invent a pipeline. Do not publish unless
  asked. Do not spend money or change cloud accounts.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3"
  stage: "60-release"
---

# Cut release

Publish **this version** using machinery this repo already has. `ship-notes` writes the notes; this skill runs the release.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Notes only | `ship-notes` |
| Rollback of what just shipped | `plan-rollback` / `revert-change` |
| No release path in the repo | print human commands and stop |

## Required inputs

- User asked to publish / deploy / tag
- `git` and `AGENTS.md`
- Detected path: documented Release/Deploy command, existing Makefile/manifest/CI releaser, or host CLI this repo already uses

If you cannot find a path, **stop**. Do not guess `npm publish`.

## Human decisions (do not invent)

- Publish, tag, push, spend money (stop if a command would bill)

## Procedure

1. Detect the existing path from README, Makefile, manifest, CI, tags.
2. Preconditions: secret-scan clean; say if `ready-to-merge` was not run.
3. `ship-notes` if the changelog is stale and this repo keeps one.
4. Version bump only if they asked or the existing script does it.
5. Run the detected command. Tag only if they asked or the script tags. Do not `--force` a tag.
6. Do not change billing, plans, or accounts.

## Output

- Path: reply
- Template: [references/release-report.md](references/release-report.md)

## Quality bar

- [ ] Command is from this repo
- [ ] Published only if asked
- [ ] No invented pipeline
- [ ] No account/billing change

## Done

Fill the report. Next: `handoff` or stop.
