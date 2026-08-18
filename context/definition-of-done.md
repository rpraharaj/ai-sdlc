# Definition of done

Commands and observations, not slogans. Copy the exact commands from this consuming repo’s `AGENTS.md`. Write `(unknown)` if the repo has no command yet — do not invent `npm test`.

## Story / slice

A slice is done when all of the following are true:

- [ ] Acceptance checks on the shaped work (or the named task) pass
- [ ] Lint: `(unknown)`
- [ ] Typecheck: `(unknown)`
- [ ] Tests: `(unknown)`
- [ ] `ready-to-merge` (or this repo’s equivalent) printed **Ready** with command output
- [ ] No secrets in the diff

## Release

A release is done when:

- [ ] Release notes cover the real commit range
- [ ] Runbook for new failure modes exists or is `n/a` with a reason
- [ ] Rollback sentence can be said out loud
- [ ] Named humans signed go-live (`context/decision-rights.md`)

## Hotfix

A hotfix is done when:

- [ ] The incident doc names blast radius and the fix
- [ ] The same mechanical checks as a story, or an explicit waiver by the incident commander
- [ ] A follow-up work item exists if the fix is incomplete

## Not done

“LGTM”, “works on my machine”, or a green status with no command output is not done.
