<!-- eval: fixture — not a live program -->
<!-- eval-pass: success-checks -->
<!-- eval-pass: non-goals -->

# PRD: Fixture Ledger export

- **Status:** accepted
- **Date:** 2026-01-15
- **Author:** fixture
- **Reviewers:** fixture
- **Related:** none

## Summary

Finance analysts on Fixture Ledger cannot get a CSV of posted journals for one book and one date range. They export by hand from the posted-journals screen. Success is a download that matches the on-screen table for that filter.

## Problem

Analysts re-key posted journals into a spreadsheet every close. The hurt is re-key time and missed rows, not “we need a data platform.”

## Current behavior

The posted-journals screen filters by book and date. There is no export control. Count of journals on screen is the only total they have.

## Audience

- Primary: finance analyst role already named in the glossary of a consuming program (here: “analyst”)
- Secondary: none
- Out of audience: customers of Fixture Ledger

## Goals

- An analyst can download the current filter as CSV

## Non-goals

- General-purpose warehouse
- Changing how journals are posted
- Real-time streaming

## Scope

- In: CSV of the rows the posted-journals screen already shows
- Out: other screens, PDF, scheduled email

## Success

- Baseline today: no export control on the posted-journals screen
- Target: n/a (no product metric file in this fixture)
- Checks (at least one fails today):
  - [ ] Posted-journals screen has a control that downloads CSV for the active book + date filter
  - [ ] CSV column set matches the on-screen table for that view
  - [ ] Empty filter result downloads a header-only file

## User stories

1. As an analyst, I can download the current posted-journals filter as CSV, so that I do not re-key rows.

## Journeys

- Happy path: filter set, download, file opens with those rows
- Empty / first-time: no rows → header-only file
- Error / denied: user without journal-read is denied
- Permission / role variants: journal-read required

## Requirements

### Must

- Export is the current filter, not the whole book unless that is the filter

### Should

- Filename includes book id and dates

### Later

- Other screens

## UX notes

New control on the existing posted-journals screen. Empty and denied states as above.

## Analytics

n/a — this fixture has no event catalog

## Privacy and data

Journal rows may contain amounts. No new personal fields. Do not put live customer data in git.

## Constraints

- Technical: reuse the query the screen already runs
- Legal / privacy: unknown
- Timeline: n/a
- Budget / staffing: n/a

## Dependencies

none

## Rollout

- Flag / experiment: n/a
- Markets / segments: n/a
- Support / comms: n/a
- Rollback of the product change: remove the control

## Risks

- Export of a large filter may be slow — measure after; no invented SLO

## Assumptions

- Posted-journals query is the source of truth for those rows

## Open questions

- Blocking: none
- Non-blocking: filename format

## Next

write-requirements
