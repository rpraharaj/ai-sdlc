---
name: incident-triage
description: >
  First response for a production or customer-facing incident — blast
  radius, stabilize vs fix, evidence to gather. Use when production is
  down, data is wrong in prod, users are impacted, or the user says
  incident, outage, sev, or page.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.4.0"
  stage: "60-release"
---

# Incident triage

Stabilize first. Do not start a feature. Do not silently patch production.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Local test failure / no live impact | `debug` or `shape-work` |
| Known change to undo after stabilize | `revert-change` |
| Root-cause after the fire is contained | `debug` |

## Required inputs

- Symptom (what users or systems see)
- `context/environments.md` and `context/decision-rights.md` if present

## Human decisions (do not invent)

- Rollback vs mitigate vs fix-forward vs observe
- Destructive data repairs

## Procedure

1. Snapshot immediately (unknown allowed): started, symptom, expected, scope, severity, known/unknown. Template: [references/incident-template.md](references/incident-template.md).
2. Blast radius from logs, metrics, flags, recent deploys — read, do not rewrite yet.
3. Propose **one** primary action: rollback/flag off; mitigate; fix forward; observe. The incident commander decides using `context/decision-rights.md`; record decision evidence and environment before any runtime action. This triage profile remains read-only on runtime systems. Rollback/mitigate before a clever fix.
4. Gather only evidence that changes the next action. No secrets.
5. Running log of actions. When contained: `debug` + `write-tests`; `handoff` if another session takes over. Workflow: `incident`.

## Output

- Path: reply (file only if asked or the repo stores incident notes)
- Template: `references/incident-template.md`

## Quality bar

- [ ] Snapshot exists with unknowns labeled
- [ ] One primary action named
- [ ] No silent prod change
- [ ] Next skill named

## Done

Snapshot, blast radius, action, evidence, next skill.
