---
name: explore-codebase
description: >
  Map an unfamiliar repository — stack, install/run/test/lint commands,
  layout, entry points, and conventions. Write or update AGENTS.md from
  evidence. Use when starting in a new repo, onboarding, or before
  changing code you have not read. Do not invent commands.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3"
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
4. Run **Test** if known; else Lint or Build. If deps are missing, Install once and retry. Capture exit status. Do not start long-lived servers unless a one-shot health check.
5. Map layout from README + shallow listing (not `node_modules` / `vendor` / `dist` / `.git`).
6. Update `AGENTS.md` using [references/agents-template.md](references/agents-template.md). If `AGENTS.md` exists, replace only the managed blocks. Glossary: 5–20 terms from this repo, or `(none yet)`.

## Output

- Path: root `AGENTS.md` (managed sections)
- Template: `references/agents-template.md`

## Quality bar

- [ ] Every command is from a file you opened or a command you ran
- [ ] Unknowns are `(unknown)`
- [ ] No invented glossary terms
- [ ] No secrets

## Done

1. Root and languages
2. Commands you ran and pass/fail
3. Layout + do-not-edit
4. `AGENTS.md` path
5. Next: `shape-work` or `debug` — not a drive-by refactor
