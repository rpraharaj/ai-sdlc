---
name: write-spike
description: >
  Time-box a technical question and state what will be thrown away.
  Use when the user asks for a spike, spike brief, research ticket, or
  /write-spike. Do not implement the production design. Do not invent
  the time box.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2"
  stage: "30-design"
---

# Write spike

Frame a **question with an end**. This is not `write-design`, not `implement-change`, and not an ADR (`record-decision` comes after the spike).

Do not implement production code in the spike unless the user said the spike **is** a throwaway prototype and the doc says what to delete.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Approach is already chosen | `write-design` / `record-decision` |
| Production slice | `shape-work` / `implement-change` |
| Missing SLO number | `write-nfr` (`unknown`) |

## Required inputs

- The question (one sentence)
- A time box from the user (hours or days). If missing, **stop** and ask — do not invent “two days.”

## Human decisions (do not invent)

- Duration
- Whether any prototype may land in the main branch (default: no)

## Procedure

1. Read `AGENTS.md` if present. Read the design/architecture that left this question open.
2. Find the home: first existing `docs/spikes/`, or offer to create it. Name: `docs/spikes/YYYY-MM-DD-<slug>.md`.
3. Open [references/spike-template.md](references/spike-template.md). Copy every heading. Write `n/a` when unused.
4. Success = what answer would end the spike. Out of scope = what we will not solve.
5. **Throw away** names files or a rule (“delete the branch”). Empty throw-away is a fail.
6. After the spike is run (later), fill Results; then `record-decision` if a sticky choice remains.

## Output

- Path: `docs/spikes/YYYY-MM-DD-<slug>.md`
- Template: `references/spike-template.md`

## Quality bar

- [ ] One question
- [ ] Time box is user-set
- [ ] Throw-away rule is non-empty
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Question + time box
3. Next skill: do the spike (`implementer` on a throwaway branch), then `record-decision`
