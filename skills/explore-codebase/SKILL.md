---
name: explore-codebase
description: >
  Map an unfamiliar repository — stack, install/run/test/lint commands,
  layout, entry points, and conventions. Report a map and proposed AGENTS.md updates from
  evidence without writing files. Use when starting in a new repo, onboarding, or before
  changing code you have not read. Do not invent commands.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.4.0"
  stage: "40-build"
---

# Explore codebase

A stranger can run, test, and change this repo without guessing. Do not implement product features. Do not invent commands you did not see in a file or run successfully.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| How one feature works | `explain-code` |
| Empty tree, start an app | `start-project` |
| Shape a change you already understand | `shape-work` |

## Required inputs

- A workspace you can list and read
- Git root if this is a repo (`git rev-parse --show-toplevel`)

## Human decisions (do not invent)

- None for the map. Do not invent glossary jargon.

## Procedure

1. Read root `AGENTS.md` if present. Record **Root**.
2. Detect stack only from files that exist (manifests, lockfiles, CI). See [references/stack-evidence.md](references/stack-evidence.md).
3. Resolve **Install / Run / Test / Lint / Typecheck / Build** from manifests or CI. Prefer the CI command. Else `(unknown)`. Never invent `npm test`.
4. Stay read-only: use read/search commands only. Record discovered checks as `not run`; hand execution to `verifier` and dependency installation to `implementer`. Do not run tests, install dependencies, or start servers in an explore session.
5. Map layout from README + shallow listing (not `node_modules` / `vendor` / `dist` / `.git`).
6. Open [references/agents-template.md](references/agents-template.md) and report proposed managed blocks. A `planner` session may persist them: replace only matching managed blocks; if absent, append the managed repo section without overwriting existing commands or program-context pointers. Flag conflicting commands for resolution. Glossary facts live only in `context/glossary.md`; propose additions there, or report terms in the reply if that file does not exist.

## Output

- Path: reply; optional planner handoff for root `AGENTS.md` managed sections
- Template: `references/agents-template.md`

## Quality bar

- [ ] Every command is from a file you opened or a command you ran
- [ ] Unknowns are `(unknown)`
- [ ] No invented glossary terms
- [ ] No secrets
- [ ] No files edited or executable checks run by the explore profile

## Done

1. Root and languages
2. Commands you ran and pass/fail
3. Layout + do-not-edit
4. Proposed `AGENTS.md` blocks and any planner / verifier / implementer handoffs
5. Next: `shape-work` or `debug` — not a drive-by refactor
