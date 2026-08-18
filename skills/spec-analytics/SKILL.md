---
name: spec-analytics
description: >
  Specify analytics events, properties, and privacy notes without
  inventing baselines. Use when the user asks for event specs,
  instrumentation, tracking plan, or /spec-analytics. Do not write
  product code.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2"
  stage: "10-discover"
---

# Spec analytics

Name **what we will emit** and what we will not. This is not an experiment (`design-experiment`) and not a dashboard design.

Do not invent baselines, funnels, or event names that contradict the repo.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Hypothesis + stop rule | `design-experiment` |
| PII classification of a change | `classify-data` |
| Implementation of the events | `implement-change` |

## Required inputs

- PRD, UI spec, or the user-named journeys to instrument
- `context/` privacy notes if any; existing events in the repo if they exist

## Human decisions (do not invent)

- Whether a property is allowed (PII)
- Any numeric target (that is `write-nfr` or the PRD)

## Procedure

1. Read `AGENTS.md` if present. Search the repo for existing event names before adding new ones. Reuse.
2. Read the PRD / UI spec. Only journeys that exist there.
3. Find the home: first existing `docs/analytics/`, or offer to create it. Name: `docs/analytics/<slug>.md`.
4. Open [references/analytics-template.md](references/analytics-template.md). Copy every heading. Write `n/a` when unused.
5. Each event: name, when it fires, properties, PII (yes/no/unknown). No baseline column unless a number is already in the PRD.
6. **Will not track** is required (or `none` with reason).
7. Do not put examples that look like real emails, phones, or tokens.

## Output

- Path: `docs/analytics/<slug>.md`
- Template: `references/analytics-template.md`

## Quality bar

- [ ] Every event traces to a PRD journey or UI spec
- [ ] Existing event names reused when found
- [ ] PII marked yes / no / unknown per property
- [ ] No invented baseline
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Event count
3. Next skill: `classify-data` if PII is `unknown`; `implement-change` / `write-tests`
