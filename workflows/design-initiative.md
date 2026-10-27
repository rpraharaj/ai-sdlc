# design-initiative

Lock how this initiative is built, including contracts and sticky decisions.

## When to use

A signed PRD and applicable accepted requirements exist (or an authorized prerequisite waiver), and “how” is still open.

## When not to use

The first slice **is** the whole goal — use `shape-work`. A single library choice — use `record-decision` only.

## Inputs

- PRD and applicable requirements, with current approval evidence or authorized prerequisite waiver
- Existing architecture if the system already exists

## Outputs

- Architecture (only if boundaries change)
- Design
- ADRs for irreversible choices
- Dev tasks

## Steps

1. Skill: `write-architecture` if boundaries or stores change; else skip and say why
   Agent profile: `planner`
   Stop if: product why is still open (`write-prd`)
2. Skill: `write-nfr`
   Agent profile: `planner`
   Stop if: you would invent numbers — leave `unknown` and continue only if that does not block slice 1
3. Skill: `write-design`
   Agent profile: `planner`
4. Skill: `record-decision` for each irreversible choice the design left open
   Agent profile: `planner`
5. Skill: `write-integration-contract` if two sides share a shape
   Agent profile: `planner`
6. Skill: `review-architecture` if an architecture file was written
   Agent profile: `reviewer`
   Stop if: blocking claims fail or remain unverified; return to the author, then review the revised artifact
7. Skill: `review-change` on the design/contracts document diff, with the `design-reviewer` persona
   Agent profile: `reviewer`
   Stop if: applicable Must coverage is missing or blocking findings remain; return to the author and review the revised diff before approval
8. **Human gate:** Architect signs the final approach and irreversible choices, including artifact revisions and resolved review findings, using the approval home in `context/decision-rights.md`. Missing or stale evidence means stop. Changes after approval return to affected review and approval.
9. Skill: `write-dev-tasks`
   Agent profile: `planner`
   Stop if: applicable Must coverage is missing or baseline approval is not current

## Failure

Missing PRD → stop. Invented SLOs → `unknown`, do not proceed as if targets exist.

## Done

- [ ] An engineer can start slice 1 without guessing the approach
- [ ] Blocking findings were resolved before the architect signed the final revisions
- [ ] Breaking contract changes are absent or explicitly accepted
