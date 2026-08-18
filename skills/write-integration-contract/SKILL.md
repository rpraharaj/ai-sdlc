---
name: write-integration-contract
description: >
  Write an API, event, or file contract with compatibility rules. Use when
  the user asks for an integration contract, API contract, event schema,
  interface agreement, or /write-integration-contract. Do not implement.
  Do not break compatibility in the same change that adds a field.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.1"
  stage: "30-design"
---

# Write integration contract

Lock the **shape two sides share**. This is not a design of internals (`write-design`), not examples-only (`write-api-examples`), and not a migration plan (`data-change`).

Do not implement. Do not drop or rename a field in the same document that adds one unless the human explicitly accepts a breaking change.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| How the initiative is built | `write-design` (then this, if a public shape exists) |
| Stored schema / expand-then-contract steps | `data-change` |
| Request/response examples only | `write-api-examples` |
| Process handoffs, not payloads | `map-process` |
| Why we picked this protocol | `record-decision` |

If there is no design or architecture and the shape is not already in the repo, **stop** and offer `write-design` first — unless the user is documenting an existing interface. Then read the code or spec that exists.

## Required inputs

- A design, architecture, or existing interface (path or code)
- Producer and consumer named from `context/systems-of-record.md` or the design
- `AGENTS.md`

## Human decisions (do not invent)

- Breaking vs expandable change
- Authz model if the repo has no existing pattern
- Error catalog that is not already in the repo

## Procedure

1. Read `AGENTS.md` if present. Read `context/systems-of-record.md` if present.
2. Read the design/architecture or the existing interface. Prefer types and routes that already exist.
3. Find the home: first existing `docs/contracts/`, or offer to create it. Name: `docs/contracts/<slug>.md`.
4. Open [references/contract-template.md](references/contract-template.md). Copy every heading. Write `n/a` when unused.
5. State producer, consumer, transport, and identity as this program already uses them.
6. Fields: name, type, required, meaning. Mark new vs existing. **Add** is allowed. **Remove/rename** requires a human breaking-change yes and a compatibility section.
7. Errors, idempotency, and versioning: copy the repo’s existing pattern or write `unknown — need human`.
8. No secrets. No production URLs with credentials.

## Output

- Path: `docs/contracts/<slug>.md`
- Template: `references/contract-template.md`

## Quality bar

- [ ] Producer and consumer are named
- [ ] Every field has type and required/optional
- [ ] Compatibility section is not empty (expand / break+waiver / existing unchanged)
- [ ] Remove/rename is absent unless a human accepted a break
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Transport + field count
3. Next skill: `write-dev-tasks`, `write-test-strategy`, or `write-api-examples`
