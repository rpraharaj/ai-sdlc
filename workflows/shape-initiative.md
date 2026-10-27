# shape-initiative

Lock the problem and the testable contract before design.

## When to use

A new initiative still has an open why, who, or success.

## When not to use

One-line bug or a tiny already-clear change — use `shape-work` only.

## Inputs

- Evidence of a hurt (ticket, note, metric this program already has)
- `context/` filled enough to name systems and terms

## Outputs

- Opportunity brief (optional if a PRD is already justified)
- PRD
- Requirements

## Steps

1. Skill: `write-opportunity`
   Agent profile: `shaper`
   Stop if: no evidence of a hurt
2. Skill: `synthesize-discovery` (skip if sources are already thin and cited in the brief)
   Agent profile: `shaper`
   Stop if: no sources
3. Skill: `write-prd`
   Agent profile: `shaper`
   Stop if: opportunity was dropped
4. **Human gate:** Product manager signs problem + success for the exact PRD revision. Record evidence using `context/decision-rights.md`; an accepted label alone is insufficient.
5. Skill: `write-requirements`
   Agent profile: `shaper`
   Stop if: no signed PRD
6. Skill: `map-process` when more than one team or system is involved
   Agent profile: `shaper`
7. **Human gate:** Business owner + BA confirm requirements priorities, accountable owners, and the baseline revision using the approval home in `context/decision-rights.md`. Unassigned decisions or missing evidence block the design handoff.

## Failure

A step that would invent users, success, or Must vs Should stops. Do not skip to `write-design`.

## Done

- [ ] PRD has yes/no success checks
- [ ] Requirements exist and every Must traces to a PRD goal
- [ ] Product manager signed problem + success
- [ ] Business owner + BA accepted the requirements baseline with current evidence
