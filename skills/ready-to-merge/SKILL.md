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
  version: "0.4.0"
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
- `context/definition-of-done.md` and `context/decision-rights.md` when installed; identify any missing required check or approval policy before a verdict

If the diff is empty, **stop**.

## Human decisions (do not invent)

- Waivers (must be explicit)
- Commit / open PR (only if they asked)

## Procedure

1. Identify the target revision and base. Include staged, unstaged, and untracked changes. For a committed branch with a clean working tree, use its merge-base with the default base; a clean tree does not mean an empty change. Stop if the base cannot be established.
2. Inventory required checks from `AGENTS.md` and the program's definition of done. Run format, lint, typecheck, focused tests, Test, and any required build or other check. Record each as `pass`, `fail`, `not applicable`, `unknown`, or `not run`, with command, exit status, output, and target revision. `not applicable` needs a reason; `(unknown)` is not `not applicable`. Required checks that are `unknown`, `not run`, or `fail` block Ready unless a human authorized in `context/decision-rights.md` explicitly waives that check for this revision. No executable check evidence means unverified, not Ready.
3. Secret scan via `engineering-bar`. Any match is not ready.
4. Walk `engineering-bar` on the diff.
5. Acceptance: read the shaped slice, named task, and applicable Must requirements. Link each acceptance check to its evidence. Missing acceptance is unverified; use `n/a` only for an explicitly explained non-behavioral change. Verify required human approvals and waivers using the evidence convention in `context/decision-rights.md`. A label such as `accepted` is insufficient. If the diff changes after verification, rerun affected checks and obtain any affected approval again.
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

- [ ] Ready only if every required check and dispatch passed or has a revision-bound human waiver, secrets are clean, the bar has no unwaived fails, acceptance is evidenced or explicitly not applicable, and required approvals are current
- [ ] Command output from this session
- [ ] Unknown or unrun required checks cannot silently pass; target revision and base are recorded

## Done

The verdict. Next: `commit` then `open-pr` if they asked.
