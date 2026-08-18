---
name: start-project
description: >
  Start a new project from an empty or near-empty directory using the
  stack the user named. Use when there is no existing app, or the user
  says new project, scaffold, greenfield, or from scratch. Do not invent
  a stack they did not choose.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3"
  stage: "40-build"
---

# Start project

Create the **smallest runnable project** they asked for. Do not pick a framework for them. Do not add a product feature beyond hello + checks that prove it runs.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Workspace already has an application | `explore-codebase` / `implement-change` |
| Add an app in a monorepo | stay in the named package; match siblings |

Stop if there is a source tree with a manifest, lockfile, or more than bootstrap files.

## Required inputs

- Language, kind (app / lib / CLI / service), and tools the user named

If any are missing, ask **one** blocking question listing the gaps. Do not recommend a trendy stack. Do not run a third-party `create-*` unless they named that exact tool.

## Human decisions (do not invent)

- The stack

## Procedure

1. Prefer the official init for the named toolchain. Match the package manager they named.
2. One entry point that runs. One test that fails if the entry is broken, in that toolchain’s runner.
3. Root `README` with Install / Run / Test from commands you actually used.
4. Fill `AGENTS.md` from `../explore-codebase/references/agents-template.md` using those commands.
5. Load `engineering-bar`. Climb Minimum path. No extra CI unless asked. No secrets.

## Output

- Path: new project files + `AGENTS.md` + `README.md`
- Session report: [references/start-notes.md](references/start-notes.md)
- `AGENTS.md` body: `../explore-codebase/references/agents-template.md`

## Quality bar

- [ ] Stack is user-named
- [ ] Test command was run or marked unverified
- [ ] No extra dependencies you were not asked for
- [ ] No secrets committed

## Done

1. Stack and kind
2. Files created
3. Commands run and results
4. Next: `write-prd` if product is open, else `shape-work`
