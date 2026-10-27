---
name: performance
description: >
  Investigate slowness with measure-first profiling, or guard a diff for
  regressions (N+1, unbounded work, heavy imports). Use when something
  is slow, the user asks to profile, or ready-to-merge asks for a
  performance guard.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3.0"
  stage: "50-verify"
---

# Performance

Two modes. Pick one and say which: **Investigate** (user says it is slow) or **Guard** (`ready-to-merge` or “will this make it slower”).

Do not rewrite on a hunch. Guess-caching is a fail.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| NFR numbers | `write-nfr` |
| Production timeouts/retries | `production-pass` |

## Required inputs

- Guard: the current diff
- Investigate: a named surface (or the hottest path in the complaint)
- `AGENTS.md`

## Human decisions (do not invent)

- A budget number that is not in the repo or from the user

## Procedure

**Guard:** fail if the diff adds N+1, unbounded lists, full-collection scan, heavy import on a hot route, sync work this repo usually defers, or UI layout jump without reserved size — unless a matching bound already exists. If none apply, pass. No micro-optimizations.

**Investigate:** name the surface; measure first with what this repo already has; classify one bottleneck; change one thing; measure again. If you cannot measure, **unverified**. See [references/performance-template.md](references/performance-template.md).

## Output

- Path: reply
- Template: `references/performance-template.md`

## Quality bar

- [ ] Mode is named
- [ ] Guard has checked/fails lines
- [ ] Investigate has a number or unverified
- [ ] No invented cache

## Done

The template. Do not commit unless asked.
