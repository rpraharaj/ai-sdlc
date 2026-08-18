# design-initiative

Lock how this initiative is built, including contracts and sticky decisions.

## When to use

A signed PRD (or accepted requirements) exists and “how” is still open.

## When not to use

The first slice **is** the whole goal — use `shape-work`. A single library choice — use `record-decision` only.

## Inputs

- PRD and/or requirements
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
6. **Human gate:** Architect signs the approach (`context/decision-rights.md`)
7. Skill: `review-architecture` if an architecture file was written  
   Agent profile: `reviewer`  
   Stop if: reviewer has no evidence — finding stays unverified
8. Skill: `write-dev-tasks`  
   Agent profile: `planner`

## Failure

Missing PRD → stop. Invented SLOs → `unknown`, do not proceed as if targets exist.

## Done

- [ ] An engineer can start slice 1 without guessing the approach
- [ ] Architect signed
- [ ] Breaking contract changes are absent or explicitly accepted
