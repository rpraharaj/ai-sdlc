---
name: map-process
description: >
  Map current and future business process — steps, owners, and systems.
  Use when the user asks for a process map, as-is/to-be flow, journey
  across teams, or /map-process. Do not write architecture or product code.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.1.0"
  stage: "20-shape"
---

# Map process

Show **who does what, in which system, today and after**. This is not architecture (`write-architecture`), not requirements (`write-requirements`), and not a UI spec.

Do not implement. Do not invent owners or systems.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Testable functional contract | `write-requirements` |
| System boundaries and stores | `write-architecture` |
| API / event shape | `write-integration-contract` |
| UAT scripts | `plan-uat` (consume this map first) |
| Impact of a scope change | `assess-change` |

## Required inputs

- A PRD or requirements path, **or** a named process the user already runs
- `context/systems-of-record.md` if it exists — systems on the map should match it
- `context/glossary.md` if it exists

If neither a spec nor a described current process exists, stop and ask which process to map. Do not invent a happy-path.

## Human decisions (do not invent)

- Who owns each step in the business
- Whether a to-be step is in scope for this initiative

## Procedure

1. Read `AGENTS.md` if present. Read `context/systems-of-record.md` and `context/glossary.md` if present.
2. Read the PRD/requirements if named. Note actors and systems they already mention.
3. Find the home: first existing `docs/process/`, or offer to create it. Name: `docs/process/<slug>.md`.
4. Open [references/process-template.md](references/process-template.md). Copy every heading. Write `n/a` when unused.
5. Draw **current** first. Every step has: actor, action, system (or `offline`), output.
6. Draw **future** only for steps this initiative changes. Unchanged steps say `unchanged`.
7. List handoffs and failure/exception paths the sources mention. Do not invent exception paths.
8. Systems not in `systems-of-record.md` are marked `not in systems-of-record`.

## Output

- Path: `docs/process/<slug>.md`
- Template: `references/process-template.md`

## Quality bar

- [ ] Current path has at least two steps with actors
- [ ] Every step names a system or `offline`
- [ ] Future path does not silently add systems that are not in context or the spec
- [ ] Exceptions are sourced or `none in sources`
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Step count current / future
3. Next skill: `write-architecture`, `write-requirements`, or `plan-uat`
