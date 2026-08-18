# Workflow standard

A workflow is an ordered list of skills with **named human gates**. It is optional. Anyone can run the skills one at a time.

## Canonical file

Markdown only: `workflows/<name>.md`.

```markdown
# <name>

One sentence outcome.

## When to use
## When not to use

## Inputs
## Outputs

## Steps

1. Skill: `<skill-name>`
   Agent profile: `<profile>`
   Stop if: <missing input>
2. **Human gate:** <who> signs <what>
3. Skill: `<skill-name>`
   …

## Failure
What to do if a step refuses.

## Done
Yes/no checks.
```

No orchestration language in this file.

## Rules

- Every step is a skill that exists in the [catalog](catalog.md).
- Every human gate names a role from `context/decision-rights.md` (or “the author” / “the reviewer”).
- A step that would invent a missing artifact is a stop, not a skip.
- Fan-out (“review these three dimensions”) is written as a list. A host adapter may run them in parallel; the Markdown still lists them.
- Adversarial checks fail closed: missing evidence means unverified, not passed.

## Workflows (in `workflows/`)

| Workflow | Steps (skill names) | Human gate |
| --- | --- | --- |
| `shape-initiative` | `write-opportunity` → `write-prd` → `write-requirements` | Product manager signs problem + success |
| `design-initiative` | `write-architecture` (if shape changes) → `write-design` → `record-decision` → `write-dev-tasks` | Architect signs approach |
| `deliver-slice` | `shape-work` → `implement-change` → `write-tests` → `review-change` → `ready-to-merge` | Author + reviewer |
| `release-train` | `ship-notes` → `write-runbook` → `plan-rollback` → `cut-release` | DevOps + product go/no-go |
| `weekly-program` | `update-raid` → `triage-blockers` → `write-status` | Program manager sends it |
| `incident` | `incident-triage` → `write-runbook` (update) → `handoff` | Incident commander |

All named skills live in this pack.

## Adapters

A host may automate a workflow (sub-sessions, hooks). The adapter:

- does not add or remove human gates
- does not become the source of truth
- can be deleted without losing the procedure
