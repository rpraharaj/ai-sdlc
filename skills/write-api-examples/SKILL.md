---
name: write-api-examples
description: >
  Write request and response examples from an existing integration
  contract. Use when the user asks for API examples, sample payloads,
  or /write-api-examples. Do not create a second contract. Do not
  implement.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2.0"
  stage: "40-build"
---

# Write API examples

Illustrate the **contract that already exists**. This is not `write-integration-contract` and not `write-tests`.

Do not add fields the contract does not have. Do not use real secrets or personal data.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| No contract yet | `write-integration-contract` |
| Stored schema migration | `plan-data-migration` / `data-change` |
| Automated tests of the contract | `write-tests` |

## Required inputs

- Path to the integration contract (or an existing OpenAPI/schema in the repo that is already the contract)

If missing, **stop** and name `write-integration-contract`.

## Human decisions (do not invent)

- Whether an example is normative (default: illustrative only)

## Procedure

1. Read `AGENTS.md` if present. Read the contract. List fields.
2. Find the home: sibling `docs/contracts/<slug>-examples.md`.
3. Open [references/examples-template.md](references/examples-template.md). Copy every heading. Write `n/a` when unused.
4. One happy example and one error example per operation the contract names. Types must match the contract.
5. Use obviously fake values (`user@example.com` only if the contract has email; prefer `user@example.invalid`).

## Output

- Path: `docs/contracts/<slug>-examples.md`
- Template: `references/examples-template.md`

## Quality bar

- [ ] Contract path is named
- [ ] No field that is not on the contract
- [ ] Happy + error for each listed operation
- [ ] No secrets or live PII
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Operation count
3. Next skill: `write-tests` or `implement-change`
