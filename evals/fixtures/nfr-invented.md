<!-- eval: fixture — not a live program -->
<!-- eval-fail: invented-slo -->

# NFR: Fixture Ledger export

- **Status:** draft
- **Date:** 2026-01-16
- **Author:** fixture
- **Related:** evals/fixtures/prd-good.md

## Summary

Must be fast, secure, and infinitely scalable.

## Targets

| Attribute | Target | Applies to | Source | Missed-target behavior |
| --- | --- | --- | --- | --- |
| Availability | 99.99% | all | industry typical | none |
| Latency | 50ms p99 | export | we assumed | none |
| Throughput | millions of rows | export | (none) | none |
| Durability | n/a | | | |
| Consistency | n/a | | | |
| Recovery (RPO/RTO) | n/a | | | |
| Security / tenancy | bank-grade | | | |
| Accessibility | n/a | | | |
| Other | | | | |

## Out of scope

- …

## Open questions

- Blocking: none
- Non-blocking: none

## Next

write-design
