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
  version: "0.4.0"
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
- Exact release revision and target environment
- `context/definition-of-done.md`, `context/decision-rights.md`, and `context/environments.md`; stop if the applicable policy or deploy authority is unknown
- A Ready record, executed regression results, notes, rollback plan, and human go/no-go evidence for the exact release revision and environment (or explicit authorized waivers for applicable checks)

If you cannot find a path, **stop**. Do not guess `npm publish`.

## Human decisions (do not invent)

- Publish, tag, push, spend money (stop if a command would bill)

## Procedure

1. Detect the existing path from README, Makefile, manifest, CI, tags.
2. Apply the same gates for standalone invocation and `release-train`: secret-scan clean; Ready evidence current; required regression items actually passed; coverage gaps resolved or explicitly waived; notes cover the range; rollback is documented and authorized humans signed go/no-go. Read approval and waiver evidence from the home named in `context/decision-rights.md`. Missing, failed, stale, unknown, or not-run prerequisites → **stop**. A request to publish is not evidence of every required signer's approval. A docs-only or tag-only release may mark a prerequisite `n/a` only with a policy-backed reason.
3. `ship-notes` if the changelog is stale and this repo keeps one.
4. Version bump only if they asked or the existing script does it.
5. Inspect what the detected command does before running it, including automatic production promotion or remote publication. Run only the authorized path in the permitted environment. If decision rights reserve production deployment for a human, print the reviewed command and hand off; do not execute a command that reaches production. Tag only if they asked or the approved script tags. Do not `--force` a tag. If the release command changes version files, verify the resulting revision and refresh affected checks and approvals before publication; do not approve a different revision silently. If preparation and publication cannot be separated enough to verify the required revision, stop and hand off to the authorized human rather than bypassing the gate.
6. Do not change billing, plans, or accounts.

## Output

- Path: reply
- Template: [references/release-report.md](references/release-report.md)

## Quality bar

- [ ] Command is from this repo
- [ ] Published only if asked
- [ ] No invented pipeline
- [ ] No account/billing change
- [ ] Required gates passed or have authorized waivers for the exact release revision and environment
- [ ] Production execution follows decision rights even when this skill is invoked alone

## Done

Fill the report. Next: `handoff` or stop.
