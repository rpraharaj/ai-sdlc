# deliver-slice

Take one shaped slice to merge-ready.

## When to use

A task or shaped slice is already clear enough to code.

## When not to use

Why or how is still open — `shape-initiative` or `design-initiative`. Do not start here from a slogan.

## Inputs

- Shaped work or a `write-dev-tasks` item with yes/no acceptance
- `AGENTS.md` commands

## Outputs

- Implementation + tests
- Review findings
- Ready-to-merge record with command output

## Steps

1. Skill: `shape-work` if the task is still loose  
   Agent profile: `planner`  
   Stop if: acceptance checks cannot be written
2. Skill: `implement-change`  
   Agent profile: `implementer`
3. Skill: `write-tests`  
   Agent profile: `implementer` or `verifier`
4. Skill: `verify-ui` if the slice touches UI  
   Agent profile: `implementer`
5. Skill: `a11y-pass` if the slice adds or changes interactive UI  
   Agent profile: `reviewer`
6. Skill: `review-change`  
   Agent profile: `reviewer`  
   Stop if: reviewer would edit the diff
7. **Human gate:** Author + reviewer
8. Skill: `ready-to-merge`  
   Agent profile: `verifier`  
   Stop if: any required command was not run or failed

## Failure

Missing command output → not ready. Deleted test to go green → fail. Unverified UI → fail.

## Done

- [ ] Acceptance checks pass
- [ ] `ready-to-merge` printed Ready with command output
- [ ] Reviewer did not edit the author’s diff
