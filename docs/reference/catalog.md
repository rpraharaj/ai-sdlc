# Catalog

Work-type catalog. All named skills live under `skills/` in this repo (standalone pack).

Legend:

- **Core** — engineering delivery skills in this pack.
- **Wave 1 / Wave 2** — program/BA/QA/DevOps skills. All three sets are implemented here.
- **Later** — only if a real trace shows the need.

## 10 — Discover

| Skill | Wave | Primary users | Produces |
| --- | --- | --- | --- |
| `write-opportunity` | 1 | PM, program | Opportunity brief |
| `synthesize-discovery` | 1 | PM, BA | Insights + evidence (no invented personas) |
| `prioritize-backlog` | 2 | PM | Ranked list + rejected items, from written evidence |
| `design-experiment` | 2 | PM | Hypothesis, existing metric, stop rule |
| `spec-analytics` | 2 | PM, UI | Events, properties, privacy; no invented baselines |

## 20 — Shape

| Skill | Wave | Primary users | Produces |
| --- | --- | --- | --- |
| `write-prd` | Core | PM | PRD |
| `write-requirements` | 1 | BA | Functional + NFRs traces + acceptance |
| `map-process` | 1 | BA | Current/future process, owners, systems |
| `shape-work` | Core | anyone scoping a slice | Shaped slice |
| `write-dev-tasks` | Core | PM, tech lead | Ordered tasks |

## 30 — Design

| Skill | Wave | Primary users | Produces |
| --- | --- | --- | --- |
| `write-architecture` | Core | Architect | Durable system shape |
| `write-design` | Core | Architect, tech lead | How this initiative is built |
| `record-decision` | Core | Architect | One-page ADR |
| `write-nfr` | 1 | Architect, BA, DevOps | Measurable NFRs or explicit `unknown` |
| `write-integration-contract` | 1 | Architect, backend | API / event / file contract + compatibility |
| `review-architecture` | 2 | Architect | Adversarial pass on an architecture doc |
| `write-spike` | 2 | Architect, implementer | Time-boxed question + what we throw away |
| `classify-data` | 2 | Architect, security | PII / retention / residency for a change |
| `write-ui-spec` | 2 | UI, BA | States, empty/error/loading, a11y notes |
| `map-design-handoff` | 2 | UI | Design frames → existing components; gaps only |

## 40 — Build

| Skill | Wave | Primary users | Produces |
| --- | --- | --- | --- |
| `explore-codebase` | Core | anyone | Repo map / AGENTS.md updates |
| `explain-code` | Core | anyone | How a path works |
| `implement-change` | Core | UI, backend | The change |
| `write-tests` | Core | implementer, QA | Tests at public seams |
| `debug` | Core | implementer, QA | Fix + proof |
| `refactor-safely` | Core | implementer | Behavior-preserving cleanup |
| `data-change` | Core | backend | Expand-then-contract data change |
| `start-project` | Core | anyone on an empty tree | Smallest runnable project |
| `write-docs` | Core | anyone | README / API / runbook from the code |
| `commit` | Core | implementer | One honest git commit |
| `open-pr` | Core | implementer | PR/MR for review |
| `write-api-examples` | 2 | backend | Examples from the contract (not a second contract) |
| `plan-data-migration` | 2 | backend | Slices that then call `data-change` |

## 50 — Verify

| Skill | Wave | Primary users | Produces |
| --- | --- | --- | --- |
| `review-change` | Core | reviewer | Findings |
| `lean-review` | Core | reviewer | Delete-list only |
| `engineering-bar` | Core | any author | Pass/fail on the diff |
| `security-pass` | Core | reviewer | Threat model of this diff |
| `performance` | Core | reviewer | Guard, not heroics |
| `production-pass` | Core | reviewer, DevOps | Timeouts, retries, rollback sentence |
| `verify-ui` | Core | UI | Exercised flow, not a screenshot |
| `a11y-pass` | 2 | UI, QA | Keyboard, names, contrast on the diff |
| `ready-to-merge` | Core | author | Yes/no with command output |
| `write-test-strategy` | 1 | QA, architect | Risks, layers, what we will not automate |
| `write-test-plan` | 2 | QA | Cases from requirements + contracts |
| `charter-exploratory` | 2 | QA | Time-boxed charters from risk |
| `triage-defect` | 2 | QA | Severity, repro, blast radius, likely layer |
| `build-regression-pack` | 2 | QA | What must run for this release train |
| `plan-uat` | 1 | BA, QA, PM | Scope, data, scripts, exit criteria |

## 60 — Release

| Skill | Wave | Primary users | Produces |
| --- | --- | --- | --- |
| `revert-change` | Core | DevOps, implementer | Undo a known change without rewriting shared history |
| `cut-release` | Core | DevOps | Version + this repo’s release path |
| `ship-notes` | Core | PM, DevOps | Notes from the real commit range |
| `write-runbook` | 1 | DevOps, backend | Diagnose → mitigate → escalate |
| `incident-triage` | Core | DevOps | First response |
| `fix-ci` | Core | DevOps, implementer | Green because the cause is fixed |
| `review-pipeline` | 2 | DevOps | Flaky jobs, secrets, missing gates |
| `diff-environments` | 2 | DevOps | Config/version drift |
| `spec-observability` | 2 | DevOps, backend | Logs/metrics/traces for a new failure mode |
| `plan-rollback` | 2 | DevOps | One spoken sentence + steps |

## 70 — Govern

| Skill | Wave | Primary users | Produces |
| --- | --- | --- | --- |
| `update-raid` | 1 | program, project | RAID |
| `write-status` | 1 | program, project | One-page RAG + decisions needed |
| `assess-change` | 1 | program, BA, architect | Impact of a scope/date/design change |
| `plan-increment` | 2 | project | Capacity, dependencies, milestone slice |
| `triage-blockers` | 2 | project | Cluster, owner, escalate |
| `draft-steerco` | 2 | program | Decisions asked, options, recommendation |
| `map-dependencies` | 2 | program, architect | Team × system × date |
| `handoff` | Core | anyone | Continuation brief |

## Wave 1 — implemented (twelve)

1. `write-opportunity`
2. `synthesize-discovery`
3. `write-requirements`
4. `map-process`
5. `write-nfr`
6. `write-integration-contract`
7. `write-test-strategy`
8. `plan-uat`
9. `update-raid`
10. `write-status`
11. `assess-change`
12. `write-runbook`

## Core — implemented (this pack)

`write-prd`, `shape-work`, `write-dev-tasks`, `write-architecture`, `write-design`, `record-decision`, `explore-codebase`, `explain-code`, `implement-change`, `write-tests`, `debug`, `refactor-safely`, `data-change`, `review-change`, `lean-review`, `engineering-bar`, `security-pass`, `performance`, `production-pass`, `verify-ui`, `ready-to-merge`, `cut-release`, `ship-notes`, `incident-triage`, `fix-ci`, `handoff`, `start-project`, `write-docs`, `commit`, `open-pr`, `revert-change`.

## Wave 2 — implemented

`prioritize-backlog`, `design-experiment`, `spec-analytics`, `review-architecture`, `write-spike`, `classify-data`, `write-ui-spec`, `map-design-handoff`, `write-api-examples`, `plan-data-migration`, `a11y-pass`, `write-test-plan`, `charter-exploratory`, `triage-defect`, `build-regression-pack`, `review-pipeline`, `diff-environments`, `spec-observability`, `plan-rollback`, `plan-increment`, `triage-blockers`, `draft-steerco`, `map-dependencies`.

## Explicitly out of the catalog

- `pm-agent`, `ba-agent`, `architect-agent`, or any job-title agent.
- A second `write-prd` / `write-design` that forks these skills.
- Chat-only “summarize this meeting” with no artifact home (use `synthesize-discovery` or `write-status`).
