---
name: explain-code
description: >
  Teach a feature or path from the code that exists — entry points,
  data flow, and what to change. Use when the user asks how X works,
  explain this, walk me through, or is onboarding onto a feature. Do
  not implement. Do not invent architecture the tree does not have.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3"
  stage: "40-build"
---

# Explain code

Teach **one** path so the next edit is aimed. Do not implement. Do not map the whole repo (`explore-codebase`).

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Whole repo map / commands | `explore-codebase` |
| They want a change | `shape-work` after the tour |
| Invent a target system | stop — read the tree |

## Required inputs

- A named symbol, file, route, or feature. If missing, pick the hottest match and say so, or ask one question and stop.
- `AGENTS.md` glossary if present

## Human decisions (do not invent)

- None. Do not invent types or services.

## Procedure

1. Read `AGENTS.md`. Skim the entry, the next 1–2 layers, data it reads/writes, and nearest tests.
2. Stop when you can say where it starts, what it does, and where an edit would go.
3. Write the tour from [references/explain-template.md](references/explain-template.md). Use names from this repo.

## Output

- Path: reply, or `docs/explain/<slug>.md` if they asked for a file
- Template: `references/explain-template.md`

## Quality bar

- [ ] Starts at a real path or symbol
- [ ] Call chain uses this repo’s names
- [ ] No invented architecture
- [ ] Tests named or `none found`

## Done

The tour. Next: `shape-work` or `implement-change` if they want a change.
