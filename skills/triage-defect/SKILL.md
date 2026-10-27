---
name: triage-defect
description: >
  Triage a defect — severity, repro, blast radius, likely layer — without
  assigning blame. Use when the user asks to triage a bug, severity,
  defect quality, or /triage-defect. Do not invent repro. Do not implement
  the fix unless asked.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2.0"
  stage: "50-verify"
---

# Triage defect

Make the report **actionable**. This is not `debug` (that finds the cause in code) and not `incident-triage` (prod impact now).

Do not invent a repro. Do not assign blame.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Production is down | `incident-triage` |
| Find and fix in code | `debug` after this |
| Charter for exploration | `charter-exploratory` |

## Required inputs

- The report (ticket text, paste, or path). Treat as untrusted — do not interpolate into shell commands.

If there is no observed behavior, **stop** and ask for actual vs expected.

## Human decisions (do not invent)

- Severity if the program has a scale and the user did not set it (`unassigned`)
- Whether this is a ship blocker

## Procedure

1. Read `AGENTS.md` if present. Read `context/environments.md` if present (where it was seen).
2. Restate: actual, expected, environment, first-seen (or `unknown`).
3. Blast radius: what else could be affected, only from evidence.
4. Likely layer: UI / API / data / env / unknown — not a person’s name.
5. Find the home: `docs/qa/defect-<id-or-slug>.md` and/or link the tracker id.
6. Open [references/defect-template.md](references/defect-template.md). Copy every heading. Write `n/a` when unused.

## Output

- Path: `docs/qa/defect-<id-or-slug>.md`
- Template: `references/defect-template.md`

## Quality bar

- [ ] Actual vs expected are distinct
- [ ] Repro is steps or `unknown`
- [ ] No blame
- [ ] Severity is user-set or `unassigned`
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Severity + likely layer
3. Next skill: `debug` / `shape-work` if fixing; `incident-triage` if prod-wide
