---
name: review-change
description: >
  Review a local or branch diff for bugs and engineering-bar failures.
  Use when the user wants a code review, review of uncommitted work, or
  a second look at a branch. Write structured findings. Do not edit
  product code.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.4.0"
  stage: "50-verify"
---

# Review change

Read-only review of a **diff**. Do not edit product source. Do not commit.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Delete-list / over-engineering only | `lean-review` |
| Merge gate with commands | `ready-to-merge` |
| Architecture doc | `review-architecture` |

## Required inputs

- A diff: named PR/branch, or local staged+unstaged+untracked
- `AGENTS.md`

If the diff is empty, **stop**. If it is huge, summarize by file and ask what to narrow.

## Human decisions (do not invent)

- Posting the review to a host (only if they asked and a host CLI already works)
- Approving/requesting changes on the host

## Procedure

1. Collect the diff. Read changed files, not only hunks, when a finding depends on callers.
2. Load `../engineering-bar/SKILL.md` and `../engineering-bar/references/bar.md`.
3. Also look for incorrect behavior vs stated intent, missing tests (`write-tests`), authz (`security-pass`), over-engineering (`lean-review` — do not turn this into a delete-list).
4. If a shape-work / spec exists, report spec axis separately (missing / extra / wrong).
5. Severity: **bug** / **suggestion** / **nit**. Do not flood nits when there are bugs.
6. Write findings from [references/review-template.md](references/review-template.md). Empty Issues is valid after you read the diff.

## Output

- Path: reply, or a file if they asked
- Template: `references/review-template.md`

## Quality bar

- [ ] Every issue has a file path
- [ ] Product code was not edited
- [ ] No invented findings
- [ ] Spec is n/a if none exists

## Done

Issue counts by severity. Do not implement fixes unless asked (`implement-change` / `debug`).
