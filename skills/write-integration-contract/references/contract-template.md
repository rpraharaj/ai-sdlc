# Contract: <title>

Keep every heading. Write `n/a` when a section does not apply. Do not invent auth or error codes this repo does not use.

- **Status:** draft | review | accepted
- **Date:** <YYYY-MM-DD>
- **Author:** <names or "this session">
- **Related:** <design / architecture / ADR / none>

## Summary

<one paragraph: who talks to whom, over what, why this file exists>

## Parties

- Producer:
- Consumer:
- Transport: <HTTP / event / file / other already in this program>
- Identity: <how the consumer is known — existing pattern or `unknown`>

## Compatibility

- Kind: expand (additive) | break (human accepted) | document-existing
- What old consumers still do:
- What they must not assume:

## Fields

| Name | Type | Required | New? | Meaning |
| --- | --- | --- | --- | --- |
| | | yes / no | yes / no | |

## Errors

| Code or name | When | Consumer must |
| --- | --- | --- |
| | | |

or `unknown — need human` / `n/a`

## Idempotency and delivery

<existing pattern, or `unknown — need human`, or `n/a`>

## Versioning

<how this shape is versioned in this program, or `unknown`>

## Open questions

- Blocking:
- Non-blocking:

## Next

<write-dev-tasks | write-test-strategy | write-api-examples | stop — need user>
