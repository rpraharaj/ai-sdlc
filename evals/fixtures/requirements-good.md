<!-- eval: fixture — not a live program -->
<!-- eval-pass: traces -->
<!-- eval-pass: acceptance -->

# Requirements: Fixture Ledger export

- **Status:** accepted
- **Date:** 2026-01-16
- **Author:** fixture
- **PRD:** evals/fixtures/prd-good.md
- **Related:** none

## Summary

Testable contract for CSV export of the posted-journals screen filter.

## Scope

- In: export of the current filter
- Out: warehouse, other screens

## Assumptions

- Posted-journals query is reused

## Functional requirements

| Id | Statement | Priority | Traces to | Acceptance | Accountable |
| --- | --- | --- | --- | --- | --- |
| R-1 | Analyst with journal-read can download the active book+date filter as CSV | Must | PRD goal: download CSV | Control exists; file contains exactly the rows on screen for that filter | unassigned |
| R-2 | Empty filter result yields header-only CSV | Must | PRD success: empty | File has headers and zero data rows | unassigned |
| R-3 | Caller without journal-read is denied | Must | PRD journeys: denied | Denied response; no file | unassigned |
| R-4 | Filename includes book id and dates | Should | PRD Should | Filename contains book id and both dates | unassigned |

## Non-functional pointers

- NFR doc: none — run write-nfr

## Data and privacy notes

Amounts may appear. No new personal fields.

## Open questions

- Blocking: none
- Non-blocking: filename exact pattern

## Next

write-design
