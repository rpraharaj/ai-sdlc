---
name: review-architecture
description: >
  Adversarially review an architecture document; fail closed without
  evidence. Use when the user asks to review architecture, challenge a
  system shape, or /review-architecture. Do not edit the architecture
  file. Do not implement.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2"
  stage: "30-design"
---

# Review architecture

Attack the **shape**, not the author’s pride. This is not `write-architecture`, not `write-design`, and not `review-change` (that is a code diff).

Do not edit the architecture file. Missing evidence means unverified, not passed.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| No architecture file yet | `write-architecture` |
| How this initiative is built | `write-design` |
| One sticky choice | `record-decision` |
| Code diff | `review-change` |

## Required inputs

- Path to the architecture document
- Access to the repo (or an explicit “greenfield — no code”) so claims can be checked

If the file is missing, **stop**.

## Human decisions (do not invent)

- Whether a finding is accepted
- Quality targets not already in the doc or `write-nfr`

## Procedure

1. Read `AGENTS.md` if present. Read `context/systems-of-record.md` if present.
2. Read the architecture file. List claims that can be checked (services, stores, actors).
3. Check each checkable claim against the repo or named context. Unchecked → `unverified`.
4. Find the home: sibling of the architecture file, `docs/architecture/<area>-review.md`.
5. Open [references/architecture-review-template.md](references/architecture-review-template.md). Copy every heading. Write `n/a` when unused.
6. Findings: severity, section, evidence path, suggestion. Empty list is valid only after you checked claims.
7. Look for: invented SLOs, missing trust boundaries, expand+contract ignored, alternatives missing.

## Output

- Path: `docs/architecture/<area>-review.md`
- Template: `references/architecture-review-template.md`

## Quality bar

- [ ] Architecture path is named
- [ ] Every finding has evidence or is marked `unverified`
- [ ] The architecture file was not edited
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Finding count (including unverified)
3. Next skill: `write-architecture` (author revises) or `record-decision`
