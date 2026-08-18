# incident

Stabilize, write down what you know, hand off. Do not silently patch production.

## When to use

Users are impacted, data is wrong in prod, or someone called an incident.

## When not to use

A non-urgent defect — `triage-defect`. A planned rollback of a release — `plan-rollback`.

## Inputs

- What is broken, as observed
- `context/environments.md`, `context/decision-rights.md`, `context/systems-of-record.md`

## Outputs

- Incident notes (from `incident-triage`)
- Updated or new runbook
- Handoff if the next human or session takes over

## Steps

1. Skill: `incident-triage`  
   Agent profile: `incident-lead`  
   Stop if: you would make a silent prod change
2. **Human gate:** Incident commander decides mitigate vs fix vs rollback
3. Skill: `write-runbook` (update or create for this failure mode)  
   Agent profile: `incident-lead` or `releaser`
4. Skill: `plan-rollback` if rollback is the mitigate  
   Agent profile: `releaser`
5. Skill: `handoff` when the next person takes the incident  
   Agent profile: `incident-lead`
6. After stabilize: `implementer` may hotfix via `deliver-slice`

## Failure

Unknown blast radius stays `unknown`. Missing observability is not “all clear.”

## Done

- [ ] Incident doc names blast radius or `unknown`
- [ ] Commander named the path (mitigate / fix / rollback)
- [ ] No unattended production change by an agent
