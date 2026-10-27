---
name: a11y-pass
description: >
  Check keyboard access, accessible names, and contrast on the current
  UI diff only. Use when the user asks for an accessibility pass, a11y
  review, or /a11y-pass. Do not score the whole app. Do not invent WCAG
  certificates.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2.0"
  stage: "50-verify"
---

# A11y pass

Judge the **diff**, not the product. This is not `verify-ui` (flow) and not `write-ui-spec`.

Do not edit the product to “fix while reviewing” unless the user asked to implement. Prefer findings.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Exercise the user flow | `verify-ui` |
| Spec states of a screen | `write-ui-spec` |
| Whole-site audit | stop — this skill is diff-only |

## Required inputs

- The UI diff (git vs HEAD, or the files edited this session)
- `AGENTS.md`

If the diff has no interactive UI, say `n/a` and stop.

## Human decisions (do not invent)

- Waiver of a fail
- Target WCAG level if the repo does not already state one — default to the checks below only

## Procedure

1. Read `AGENTS.md` if present. Collect the UI diff.
2. For each new or changed control: can it be reached from the keyboard, does it have an accessible name, is text unreadable on its background (obvious fail only — do not invent a contrast ratio).
3. Find the home: `docs/qa/a11y-<slug-or-id>.md` or put the table in the reply if the user asked for a pass in-session.
4. Open [references/a11y-template.md](references/a11y-template.md). Copy every heading. Write `n/a` when unused.
5. Fail closed: if you did not exercise keyboard on a new control, mark that control `unverified`, not pass.

## Output

- Path: `docs/qa/a11y-<slug-or-id>.md`
- Template: `references/a11y-template.md`

## Quality bar

- [ ] Scope is the diff
- [ ] New controls are pass / fail / unverified (no silent pass)
- [ ] No invented audit score
- [ ] Unused headings are `n/a`

## Done

1. Path or the table in the reply
2. Fail + unverified counts
3. Next skill: `implement-change` to fix, or `ready-to-merge`
