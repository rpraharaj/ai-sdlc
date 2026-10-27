---
name: design-experiment
description: >
  Design an experiment with a hypothesis, an existing product metric,
  and a stop rule. Use when the user asks for an A/B test, experiment
  design, hypothesis, or /design-experiment. Do not invent metrics or
  baselines. Do not write product code.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2.0"
  stage: "10-discover"
---

# Design experiment

Write a **falsifiable bet** using a metric this product already has. This is not a PRD, not `spec-analytics`, and not implementation.

Do not invent dashboards, baselines, or sample sizes.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| What events to emit | `spec-analytics` |
| What to build if the bet is already decided | `write-prd` / `shape-work` |
| Quality targets | `write-nfr` |

## Required inputs

- A hypothesis the user can state (or an opportunity/PRD to extract one from)
- A metric **already** in the product, PRD analytics section, or an existing dashboard the user names

If no existing metric exists, **stop**. Name `spec-analytics` only for adding events; do not invent a success number.

## Human decisions (do not invent)

- Stop rule (ship / iterate / drop)
- Who may be in the experiment
- Any duration not already constrained

## Procedure

1. Read `AGENTS.md` if present. Read the PRD or opportunity if named.
2. Confirm the metric exists in a file or a named dashboard. Otherwise `unknown` and stop for the human.
3. Find the home: `docs/discover/experiment-YYYY-MM-DD-<slug>.md`.
4. Open [references/experiment-template.md](references/experiment-template.md). Copy every heading. Write `n/a` when unused.
5. Hypothesis: if we X, then metric Y (already exists) moves in direction Z, because …
6. Guardrails: what must not get worse (existing metrics only, or `unknown`).
7. No secrets. No live personal data in the doc.

## Output

- Path: `docs/discover/experiment-YYYY-MM-DD-<slug>.md`
- Template: `references/experiment-template.md`

## Quality bar

- [ ] Metric names a source (path, dashboard this program already uses, or user-named)
- [ ] No invented baseline
- [ ] Stop rule is present or `unknown — need human`
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Metric + stop rule or `unknown`
3. Next skill: `spec-analytics` if events are missing; `shape-work` if they will implement a flag
