---
name: revert-change
description: >
  Safely undo a commit, merge, PR, or deploy without rewriting shared
  history. Use when the user asks to revert, roll back, undo a merge,
  or back out a change. Do not reset shared branches.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3"
  stage: "60-release"
---

# Revert change

Undo a **known** change. Prefer a new revert commit. Do not `reset --hard` or force-push a branch other people use.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Live incident, action not yet chosen | `incident-triage` first |
| Spoken rollback plan for a release | `plan-rollback` then this if git undo is the step |
| Not a git repo | stop |

## Required inputs

- Exact target: commit SHA, merge, PR/MR, tag, or release
- `git`

If you cannot name the target, **stop**.

## Human decisions (do not invent)

- `reset --hard` (only if they asked to discard, local branch, unpushed)
- Push (only if asked; never force to default branch)

## Procedure

1. Identify the target (`git log`, `status`, current branch).
2. Shared/pushed/merge → `git revert` (`-m 1` on a merge). Default branch → revert only, never reset. Unpushed local commits on your branch → reset only as they asked.
3. Deploy already out: revert git, then this repo’s existing rollback. If none, say what a human must roll back.
4. Secret files: a revert must not restore committed secrets without telling the user.
5. Run `AGENTS.md` Test if cheap. If this stopped a fire, a focused check is enough — say what you did not run.

## Output

- Path: the revert commit (or local reset)
- Template: [references/revert-report.md](references/revert-report.md)

## Quality bar

- [ ] Target named
- [ ] Shared history not rewritten
- [ ] No force to main/master/trunk

## Done

Fill the report. Do not push unless asked.
