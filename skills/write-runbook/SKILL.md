---
name: write-runbook
description: >
  Write an operational runbook — diagnose, mitigate, escalate. Use when
  the user asks for a runbook, ops guide, incident playbook, or
  /write-runbook. Do not invent dashboards or on-call. Do not perform
  production changes.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.1.0"
  stage: "60-release"
---

# Write runbook

Tell on-call **how to recognize, mitigate, and escalate** one failure mode. This is not incident command (`incident-triage`), not a design (`write-design`), and not a deploy (`cut-release`).

Do not implement product code. Do not run production commands. Do not invent dashboards, pager rotations, or SLOs.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| An incident is happening now | `incident-triage` |
| Quality targets | `write-nfr` |
| What to observe on a new feature | `spec-observability` |
| Spoken rollback for a release | `plan-rollback` — may link here |
| How the system is shaped | `write-architecture` |

## Required inputs

- The failure mode (from a design, incident, or `production-pass` note)
- `context/environments.md` and `context/decision-rights.md` if they exist
- `context/systems-of-record.md` for the observability and identity systems

If there is no named failure mode, stop and ask which one. Do not write “generic production support.”

## Human decisions (do not invent)

- Who is escalated to
- Whether a mitigate step may run in production (document only; a human runs it)
- Any SLO or page threshold not already written

## Procedure

1. Read `AGENTS.md` if present. Read `context/environments.md`, `context/decision-rights.md`, and `context/systems-of-record.md` if present.
2. Read the design, NFR, or incident doc that names this failure mode.
3. Find the home: first existing `docs/runbooks/`, or offer to create it. Name: `docs/runbooks/<slug>.md`.
4. Open [references/runbook-template.md](references/runbook-template.md). Copy every heading. Write `n/a` when unused.
5. Symptoms must be observable with a system in `systems-of-record.md` or marked `unknown`.
6. Diagnose and mitigate steps are commands or console clicks this program already has. If unknown, write `unknown` — do not invent a vendor UI.
7. Escalate names a role from `decision-rights.md` or `unassigned`.
8. Rollback is one spoken sentence plus steps, or `n/a` with why.
9. Never include credentials, tokens, or production data.

## Output

- Path: `docs/runbooks/<slug>.md`
- Template: `references/runbook-template.md`

## Quality bar

- [ ] One failure mode in the title
- [ ] Symptoms are observable or `unknown`
- [ ] Mitigate does not require unattended prod from an agent
- [ ] Escalate names a role or `unassigned`
- [ ] No secrets
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Failure mode in one sentence
3. Next skill: `plan-rollback`, `incident-triage` if live, or `spec-observability` if signals are `unknown`
