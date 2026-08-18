---
name: write-ui-spec
description: >
  Specify UI states — happy, empty, error, loading — and accessibility
  notes that trace to requirements. Use when the user asks for a UI spec,
  screen states, interaction spec, or /write-ui-spec. Do not implement.
  Do not invent journeys the PRD does not have.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2"
  stage: "30-design"
---

# Write UI spec

Lock **what the person sees and can do** in each state. This is not visual design, not `map-design-handoff`, and not `verify-ui`.

Do not implement. Do not invent journeys.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Frames → existing components | `map-design-handoff` |
| Exercise a built screen | `verify-ui` / `a11y-pass` |
| Functional contract | `write-requirements` |
| How we build it | `write-design` |

## Required inputs

- Requirements or PRD path (journeys)
- Design or architecture if they exist

If there is no journey in a spec, **stop**. Do not spec a screen from a vibe.

## Human decisions (do not invent)

- Copy that is legal/compliance
- Whether a state is in this slice

## Procedure

1. Read `AGENTS.md` if present. Read the PRD/requirements journeys (happy, empty, error).
2. Find the home: first existing `docs/ui/`, or offer to create it. Name: `docs/ui/<slug>.md`.
3. Open [references/ui-spec-template.md](references/ui-spec-template.md). Copy every heading. Write `n/a` when unused.
4. Each view: purpose, entry, happy / empty / error / loading, keyboard, accessible name notes.
5. Trace controls to requirement ids.
6. Do not specify CSS framework or folder layout.

## Output

- Path: `docs/ui/<slug>.md`
- Template: `references/ui-spec-template.md`

## Quality bar

- [ ] Every view traces to a requirement or PRD journey
- [ ] Empty, error, and loading are present or `n/a` with why
- [ ] New interactive controls mention an accessible name
- [ ] Unused headings are `n/a`

## Done

1. Path
2. View count
3. Next skill: `map-design-handoff`, `shape-work`, or `implement-change`
