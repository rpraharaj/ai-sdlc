---
name: map-design-handoff
description: >
  Map design frames to existing UI components and list gaps only. Use
  when the user asks for a design handoff, component map, Figma-to-code
  map, or /map-design-handoff. Do not invent components. Do not implement.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2.0"
  stage: "30-design"
---

# Map design handoff

Show **what already exists** and the gaps. This is not a UI spec (`write-ui-spec`) and not implementation.

Do not invent a design-system component that is not in the repo.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| States and a11y of a screen | `write-ui-spec` |
| Build the screen | `implement-change` |
| Visual QA of a built flow | `verify-ui` |

## Required inputs

- Named frames (paths, links, or filenames the user provides)
- The UI tree in this repo (search existing components)

If you cannot see the frames and the user did not describe them, **stop**.

## Human decisions (do not invent)

- Whether a gap is “build new” vs “change the design to match existing”

## Procedure

1. Read `AGENTS.md` if present. Search the repo for existing components/patterns before listing a gap.
2. List each frame → existing component path, or `gap`.
3. Find the home: `docs/ui/<slug>-handoff.md`.
4. Open [references/handoff-template.md](references/handoff-template.md). Copy every heading. Write `n/a` when unused.
5. Gaps only get a one-line need. Do not design a new system in this file.

## Output

- Path: `docs/ui/<slug>-handoff.md`
- Template: `references/handoff-template.md`

## Quality bar

- [ ] Every frame maps to a path or `gap`
- [ ] Gaps were checked against the repo (say how)
- [ ] No new component invented as if it exists
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Mapped count / gap count
3. Next skill: `write-ui-spec` for gaps that need states; `implement-change` for reuse
