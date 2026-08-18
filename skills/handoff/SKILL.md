---
name: handoff
description: >
  Write a continuation brief so another person or session can pick up
  the work — what changed, what is left, how to verify, landmines. Use
  when stopping mid-task, switching agents, ending a session, or the
  user says handoff, wrap up, or continue later.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3"
  stage: "70-govern"
---

# Handoff

Leave a brief another session can trust. Do not implement more product code unless they asked to finish, not to hand off.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Finish the feature | `implement-change` |
| Incident still live | `incident-triage` then this |

## Required inputs

- This session’s goal, files actually changed, commands actually run
- `AGENTS.md`

Do not invent. If you did not run a command, write **unverified**.

## Human decisions (do not invent)

- None. Do not invent pass/fail.

## Procedure

1. Gather: goal and acceptance; `git status` / `git diff --stat`; commands and last result; open fails; leftover questions; existing artifacts (point, do not restate).
2. Write [references/handoff-template.md](references/handoff-template.md). File only if they asked or the repo keeps handoffs (`docs/handoffs/`).
3. No secrets. Point at variable names. `<REDACTED>` if a value leaked.

## Output

- Path: reply or `docs/handoffs/YYYY-MM-DD-<slug>.md`
- Template: `references/handoff-template.md`

## Quality bar

- [ ] Not done is honest
- [ ] Verify lists real AGENTS.md commands when known
- [ ] Next skills are real names from this pack
- [ ] No secrets

## Done

Show the brief. Stop.
