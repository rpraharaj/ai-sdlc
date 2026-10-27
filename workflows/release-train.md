# release-train

Ship a named range with notes, a rollback, and a human go/no-go.

## When to use

A release (or hotfix) is about to be cut.

## When not to use

The work is not merge-ready. A live incident — use `incident` first.

## Inputs

- Commit range or tag
- Current Ready evidence for the release revision; the workflow will execute the release regression list before go/no-go
- `context/environments.md` and `context/decision-rights.md`

## Outputs

- Release notes
- Runbook updates for new failure modes
- Rollback plan
- Cut performed only after the gate

## Steps

1. Skill: `ship-notes`
   Agent profile: `releaser`
   Stop if: the commit range is unknown
2. Skill: `write-runbook` for each new failure mode (or `n/a` with reason)
   Agent profile: `releaser`
3. Skill: `spec-observability` if the runbook symptoms are `unknown`
   Agent profile: `releaser`
4. Skill: `plan-rollback`
   Agent profile: `releaser`
   Stop if: no spoken rollback sentence
5. Skill: `build-regression-pack`
   Agent profile: `verifier`
6. Skill: `build-regression-pack` (execute the existing list and attach results)
   Agent profile: `verifier`
   Stop if: required items fail, are unknown or not run, or coverage gaps lack an authorized revision-bound waiver
7. **Human gate:** DevOps + product go/no-go for the exact release revision and environment, with Ready evidence, executed regression output, notes, and rollback. Record evidence using `context/decision-rights.md`.
8. Skill: `cut-release`
   Agent profile: `releaser`
   Stop if: the gate was not signed; do not unattended-prod

## Failure

No rollback sentence → do not cut. Money or account changes → stop (human in the billing account).

## Done

- [ ] Notes cover the real range
- [ ] Rollback can be said out loud
- [ ] Required regression items passed or have authorized waivers, with output for the exact release revision
- [ ] Named humans signed go-live for the exact revision and environment; production execution follows decision rights
