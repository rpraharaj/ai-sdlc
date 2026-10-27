---
name: write-test-strategy
description: >
  Write a test strategy — risks, layers, and what will not be automated.
  Use when the user asks for a test strategy, test approach, QA strategy,
  or /write-test-strategy. Do not write the full case list (that is
  write-test-plan). Do not implement product code.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.1.0"
  stage: "50-verify"
---

# Write test strategy

Decide **how we will learn the change is safe**, and what we will not automate. This is not a case list (`write-test-plan`), not UAT scripts (`plan-uat`), and not `write-tests`.

Do not implement. Do not invent environments or SLOs.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Detailed cases and data | `write-test-plan` |
| Business acceptance scripts | `plan-uat` |
| Unit/integration tests in the repo | `write-tests` |
| Quality numbers | `write-nfr` first if they are missing |
| Merge gate for a diff | `ready-to-merge` |

## Required inputs

- Requirements path, **or** a design plus contracts
- `context/definition-of-done.md` and `context/environments.md` if they exist
- `AGENTS.md` (for the real test command)

If there is no spec, **stop** and name `write-requirements` or `write-design`. Do not write “test everything.”

## Human decisions (do not invent)

- What we will **not** automate, and why
- Any environment that is not in `context/environments.md`

## Procedure

1. Read `AGENTS.md` if present. Read `context/definition-of-done.md` and `context/environments.md` if present.
2. Read requirements, NFR, contracts, and process map if they exist. List risks (data loss, authz, money, irreversible migrate).
3. Find the home: first existing `docs/qa/`, or offer to create it. Name: `docs/qa/strategy-<slug>.md`.
4. Open [references/test-strategy-template.md](references/test-strategy-template.md). Copy every heading. Write `n/a` when unused.
5. For each risk, name the **layer** that catches it (unit, contract, UI, UAT, monitoring) using only layers this program already runs or has agreed to add.
6. Record the test command from `AGENTS.md`. If it is `(unknown)`, say so. Do not invent `npm test`.
7. **Will not automate** is required and non-empty (or `none — everything in scope is automated`, which must be believable from the repo).

## Output

- Path: `docs/qa/strategy-<slug>.md`
- Template: `references/test-strategy-template.md`

## Quality bar

- [ ] Spec path is named
- [ ] At least one risk traces to a requirement or NFR
- [ ] Each in-scope risk names a layer
- [ ] Will-not-automate is non-empty or an explicit `none` with reason
- [ ] Test command is from `AGENTS.md` or `(unknown)`
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Risk count and will-not-automate count
3. Next skill: `plan-uat` and/or `write-test-plan` / `write-tests`
