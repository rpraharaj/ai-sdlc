<!-- eval: fixture — not a live program -->
<!-- eval-pass: sourced-rows -->

# RAID

- **Updated:** 2026-01-20
- **Author of this update:** fixture

## Risks

| Id | Statement | Severity | Owner | Next action | Source | Status |
| --- | --- | --- | --- | --- | --- | --- |
| RSK-1 | Large filter export may time out on the existing query | unassigned | unassigned | measure after first implementation | evals/fixtures/prd-good.md | open |

## Assumptions

| Id | Statement | If false | Owner | Source | Status |
| --- | --- | --- | --- | --- | --- |
| ASM-1 | Posted-journals query is safe to reuse for export | need a new query | unassigned | evals/fixtures/prd-good.md | open |

## Issues

| Id | Statement | Owner | Next action | Source | Status |
| --- | --- | --- | --- | --- | --- |
| ISS-1 | (none yet) | | | | |

## Dependencies

| Id | We need | From | Needed by | Source | Status |
| --- | --- | --- | --- | --- | --- |
| DEP-1 | journal-read already exists | identity system named in context | unknown | user: fixture | open |
