---
name: engineering-bar
description: >
  Shared engineering quality bar for any change — correctness, hygiene,
  structure, failure, data, security, performance guards, operability,
  and UI. Use when another skill says to apply the engineering bar,
  when asked if work meets engineering standards, or before calling a
  change done.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3.0"
  stage: "50-verify"
---

# Engineering bar

Apply this to the **current diff**, not the whole product. Other skills load this file (sibling `../engineering-bar/SKILL.md`). The detailed checks live in [references/bar.md](references/bar.md) — **open that file when you apply the bar**.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Full merge gate | `ready-to-merge` (it applies this bar) |
| Threat model of the diff | `security-pass` |
| Delete-list only | `lean-review` |

## Required inputs

- The current diff
- `AGENTS.md` if present (repo commands win)

## Human decisions (do not invent)

- Waiving a fail

## Procedure

1. Read [references/bar.md](references/bar.md).
2. Walk each section on this diff. Mark pass, fail, or n/a.
3. Fix fails or get an explicit user waiver. Do not invent extra standards this repo does not use.

## Output

- Path: reply (fails and waivers only)
- Template: `references/bar.md`

## Quality bar

- [ ] Secret files section applied
- [ ] Fails have a file or an explicit waiver
- [ ] Silence on a section means pass or n/a — say which

## Done

Report only fails and waivers, then the list of checks that ran.
