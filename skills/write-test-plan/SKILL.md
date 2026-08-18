---
name: write-test-plan
description: >
  Write test cases from requirements and contracts, each with data and
  expected result. Use when the user asks for a test plan, test cases,
  QA cases, or /write-test-plan. Do not invent requirements. Do not
  implement product code.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2"
  stage: "50-verify"
---

# Write test plan

Turn the contract into **cases**. This is not strategy (`write-test-strategy`), not UAT (`plan-uat`), and not `write-tests`.

Do not invent requirements.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Layers / will-not-automate | `write-test-strategy` first if missing |
| Business sign-off scripts | `plan-uat` |
| Code tests in the repo | `write-tests` |
| Time-boxed exploration | `charter-exploratory` |

## Required inputs

- Requirements path and/or contracts
- Test strategy if it exists (honor will-not-automate)

If there is no spec, **stop**.

## Human decisions (do not invent)

- Environment not in `context/environments.md`
- Cases that contradict will-not-automate (must be explicit)

## Procedure

1. Read `AGENTS.md` if present. Read strategy, requirements, contracts.
2. Find the home: `docs/qa/plan-<slug>.md`.
3. Open [references/test-plan-template.md](references/test-plan-template.md). Copy every heading. Write `n/a` when unused.
4. Each case: id, traces to requirement or contract or defect, data (synthetic), expected, layer.
5. Include at least one deny/error case when the spec has those journeys.
6. Do not list cases the strategy said will not be automated unless marked `manual`.

## Output

- Path: `docs/qa/plan-<slug>.md`
- Template: `references/test-plan-template.md`

## Quality bar

- [ ] Every case traces to a requirement, contract, or defect id
- [ ] Data is synthetic
- [ ] Will-not-automate from strategy is respected or explicitly overridden
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Case count
3. Next skill: `write-tests`, `charter-exploratory`, `plan-uat`
