---
name: spec-observability
description: >
  Specify logs, metrics, or traces for a named failure mode using
  systems this program already has. Use when the user asks for an
  observability spec, instrumentation for ops, or /spec-observability.
  Do not invent dashboards or SLOs.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2.0"
  stage: "60-release"
---

# Spec observability

Say **what we will see when this fails**. This is not `write-nfr`, not `write-runbook`, and not `spec-analytics` (product events).

Do not invent dashboards, vendors, or SLOs.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Product analytics events | `spec-analytics` |
| Diagnose / mitigate steps | `write-runbook` |
| Numeric targets | `write-nfr` |

## Required inputs

- A named failure mode (design, runbook, or incident)
- `context/systems-of-record.md` (observability row)

If there is no observability system in context, write `unknown` and stop for a human. Do not pick a vendor.

## Human decisions (do not invent)

- New dashboard or vendor
- Page thresholds

## Procedure

1. Read `AGENTS.md` if present. Read `context/systems-of-record.md` and the runbook/design.
2. Find the home: `docs/ops/observability-<slug>.md`.
3. Open [references/observability-template.md](references/observability-template.md). Copy every heading. Write `n/a` when unused.
4. Each signal: kind (log / metric / trace), name if it already exists, when it fires, how it shows up in the *existing* system — or `unknown`.
5. Point the runbook at this file.

## Output

- Path: `docs/ops/observability-<slug>.md`
- Template: `references/observability-template.md`

## Quality bar

- [ ] Failure mode is named
- [ ] Signals use the existing observability system or `unknown`
- [ ] No invented SLO or vendor
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Signal count + unknown count
3. Next skill: `write-runbook` (link symptoms here) or `implement-change`
