---
name: ready-to-merge
description: >
  Decide if the current change is ready to merge. Run this repo's
  checks; secret-scan; apply engineering-bar; dispatch security,
  performance, production, data-change, or verify-ui when the diff
  matches. Use when the user says ready to merge, are we done,
  definition of done, or ship check.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3"
  stage: "50-verify"
---

# Ready to merge

Gate the **current change**. Do not add features. Do not declare ready without this session’s command output.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Still implementing | `implement-change` |
| Review comments only | `review-change` |
| Cut a release | `cut-release` after this is Ready |

## Required inputs

- A non-empty diff
- `AGENTS.md` commands

If the diff is empty, **stop**.

## Human decisions (do not invent)

- Waivers (must be explicit)
- Commit / open PR (only if they asked)

## Procedure

1. Collect the diff (working tree vs HEAD, or named branch vs merge-base with default base).
2. Run mechanical checks from `AGENTS.md` in order: format, lint, typecheck, focused tests, Test. Skip `(unknown)`. Record exit status.
3. Secret scan via `engineering-bar`. Any match is not ready.
4. Walk `engineering-bar` on the diff.
5. Acceptance: first existing shape-work checks, named task, or PRD success this change was meant to satisfy.
6. Dispatch when the diff matches — load sibling `../NAME/SKILL.md`:

| Diff signal | Run |
| --- | --- |
| Auth, input, uploads, HTML, URLs, secrets, PII | `security-pass` |
| Query/RPC in a loop, pagination, hot path, large import | `performance` guard |
| Network, queue, job, webhook, retry, timeout, flag | `production-pass` |
| Schema, migration, protobuf, OpenAPI, event shape | `data-change` (check plan; do not start a new migration unless asked) |
| UI components, routes, CSS, views, client state | `verify-ui` |

Silent skips are **not ready**.

## Output

- Path: reply
- Template: [references/rtm-template.md](references/rtm-template.md)

## Quality bar

- [ ] Ready only if every ran command exited 0, secrets clean, bar has no unwaived fails, acceptance pass or n/a, every dispatch pass or explicit waiver
- [ ] Command output from this session

## Done

The verdict. Next: `commit` then `open-pr` if they asked.
