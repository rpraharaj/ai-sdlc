---
name: open-pr
description: >
  Open a pull request for the current branch with summary, risk, and
  test plan. Use when the user wants a PR, merge request, or to send
  work for review. Use the host CLI if authenticated; otherwise print
  the body and push instructions.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3"
  stage: "40-build"
---

# Open PR

Publish the current branch for review. Do not merge.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Uncommitted work they want in the PR | `commit` first |
| On default branch | stop unless they insisted |
| No commits vs base | stop |

## Required inputs

- `git` and commits on this branch vs the default base
- Host CLI (`gh` / `glab`) if they want it created remotely

## Human decisions (do not invent)

- Merge
- Force-push
- Reviewers (only if they named them)

## Procedure

1. Inspect branch, status, remote, log. Detect base (`main` / `master` / `trunk` / remote HEAD).
2. Say if `ready-to-merge` was not run; do not block unless they asked for a merge gate.
3. Write the body from the **diff** using [references/pr-template.md](references/pr-template.md), or the repo’s PR template if it exists.
4. Title matches this repo’s PR style if you can see past PRs; else commit style.
5. If `gh` or `glab` is authenticated: push and create. Else push only if they asked, then print title, body, base, and compare URL. No force-push to a shared branch.

## Output

- Path: PR/MR URL or printed body
- Template: `references/pr-template.md`

## Quality bar

- [ ] Body is from the diff
- [ ] Test plan lists commands you ran or steps
- [ ] Not merged

## Done

URL or printed body. List which test-plan items you actually ran.
