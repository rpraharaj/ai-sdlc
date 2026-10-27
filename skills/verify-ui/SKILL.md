---
name: verify-ui
description: >
  Exercise a UI change the way a user would — the changed flow, shared
  routes that read the same state, empty/error/loading, and desktop plus
  narrow viewports. Use when the change touches UI, when ready-to-merge
  dispatches it, or the user asks to verify the UI. Do not stop at a
  screenshot.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3.0"
  stage: "50-verify"
---

# Verify UI

Prove the **changed UI** still works for a person. A screenshot of the happy path is not enough.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Keyboard/name/contrast on the diff only | `a11y-pass` |
| Spec states of a screen | `write-ui-spec` |
| No UI in the diff | report n/a and stop |

## Required inputs

- The UI diff
- `AGENTS.md` Run / e2e command if any

## Human decisions (do not invent)

- Inventing a browser harness (do not)

## Procedure

1. Inventory routes, screens, components, CSS, and client state the change touches.
2. Drive with the first that exists: browser/preview tool; this repo’s UI/e2e runner; running app + script; existing component test. If you cannot drive it, **unverified** and list what a human should click.
3. Exercise: changed flow end to end; shared surfaces; empty/error/loading/denied; desktop and ~375px if layout changed; bar UI (name, keyboard, readable).
4. Write [references/verify-ui-template.md](references/verify-ui-template.md).

## Output

- Path: reply
- Template: `references/verify-ui-template.md`

## Quality bar

- [ ] Not only a screenshot
- [ ] Shared surfaces considered or n/a
- [ ] Unverified if you only read code

## Done

The template. Fixes: `implement-change` then re-run this skill.
