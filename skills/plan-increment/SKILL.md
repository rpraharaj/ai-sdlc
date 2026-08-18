---
name: plan-increment
description: >
  Plan an increment from stated capacity, dependencies, and existing
  artifacts. Use when the user asks for a sprint plan, increment plan,
  iteration plan, or /plan-increment. Do not invent headcount or dates
  that are not on the baseline.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2"
  stage: "70-govern"
---

# Plan increment

Fit work to **capacity someone stated**. This is not `write-dev-tasks` and not `write-status`.

Do not invent headcount, velocity, or a commitment date.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Break a design into tasks | `write-dev-tasks` |
| Rank the backlog | `prioritize-backlog` |
| Weekly RAG | `write-status` |
| Scope change | `assess-change` |

## Required inputs

- Capacity the team already stated this session or in a file (people × time, or a number they use)
- Candidates with artifact paths (tasks, requirements, backlog rank)
- RAID if it exists (dependencies)

If capacity is missing, **stop**. Forecast without capacity is forbidden.

## Human decisions (do not invent)

- Commitment vs forecast
- What is in vs out of the increment

## Procedure

1. Read `AGENTS.md` if present. Read RAID and the backlog/tasks named.
2. Find the home: `docs/govern/increment-YYYY-MM-DD.md`.
3. Open [references/increment-template.md](references/increment-template.md). Copy every heading. Write `n/a` when unused.
4. In: only items with a path and a rough size **from the user or the task file**. Out: everything else.
5. Dependencies stay as RAID ids. Do not invent a date.

## Output

- Path: `docs/govern/increment-YYYY-MM-DD.md`
- Template: `references/increment-template.md`

## Quality bar

- [ ] Capacity is sourced (user or file)
- [ ] Every in-item has an artifact path
- [ ] Commitment vs forecast is `unassigned` unless the user set it
- [ ] Unused headings are `n/a`

## Done

1. Path
2. In count / out count
3. Next skill: `write-status` / `triage-blockers` / `deliver-slice` on item 1
