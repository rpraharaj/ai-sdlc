---
name: production-pass
description: >
  Check whether this change is safe to run in production — timeouts,
  retries and idempotency, visibility, rollback, and compatibility.
  Use when the change adds I/O, jobs, queues, webhooks, flags, or
  public contracts, or when ready-to-merge dispatches it.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3"
  stage: "50-verify"
---

# Production pass

Operability of **this delta**. Do not redesign the platform.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Schema expand/contract | `data-change` |
| Spoken rollback for a release | `plan-rollback` |
| Observability for a new failure mode | `spec-observability` |

## Required inputs

- The current diff
- `AGENTS.md`

## Human decisions (do not invent)

- Accepting a breaking public contract

## Procedure

1. Note new/changed outbound I/O, inbound async, public contracts, half-applied state.
2. Check: timeouts; retries/idempotency; backpressure/bounds; visibility; one rollback sentence; compatibility (additive pass; rename/remove in the same step fail — name `data-change`, do not start it from here).
3. Write [references/production-template.md](references/production-template.md). Fails need `file:line`.

## Output

- Path: reply
- Template: `references/production-template.md`

## Quality bar

- [ ] Rollback is one spoken sentence or fail
- [ ] Expand+contract in one step is a fail
- [ ] No invented migration

## Done

Pass | fail. Fixes: `implement-change`.
