# Artifact chain

Skills exist to move these objects. If the previous object is missing, the next skill **stops**.

```text
Opportunity  →  PRD  →  Requirements + Process map
                         ↓
              Architecture (if shape changes) + ADRs
                         ↓
                    Design  →  Contracts + NFRs
                         ↓
                   Dev tasks  →  Shaped slice
                         ↓
              Implementation + Tests + UI verify
                         ↓
           Review  →  Ready-to-merge  →  Release notes
                         ↓
              Runbook / observability / RAID / status
```

## Traceability

| From | Must name |
| --- | --- |
| Must requirement | a PRD goal |
| Test case | a requirement or defect id, or a named shaped-work acceptance check for a small change |
| Dev task | a design slice (or a shaped-work id) |
| Status line | a cited milestone/RAID id, git revision, CI run, or named artifact |
| ADR | the decision the architecture/design left open |

References use artifact path + local id and source revision so `R-1` in two initiatives cannot collide. For initiatives, design reads applicable Must requirements and maps them to slices/contracts/verification; tasks preserve these references and test reports record coverage gaps. A small clear change may use a named shaped-work acceptance check instead of inventing a PRD.

Before dependent work, verify approval evidence from the home named by `context/decision-rights.md`. Changed scope, contracts, code, or release targets require affected downstream checks and approval again.

## One home per artifact type

Default paths in a **consuming** repo. If that repo already has a home (`docs/product/`, `docs/specs/`, …), use the existing home. Do not invent a second folder.

| Artifact | Default path | Produced by | Consumed by |
| --- | --- | --- | --- |
| Opportunity brief | `docs/discover/YYYY-MM-DD-<slug>.md` | `write-opportunity` | `write-prd` |
| Discovery synthesis | `docs/discover/YYYY-MM-DD-<slug>-synthesis.md` | `synthesize-discovery` | `write-prd`, `prioritize-backlog` |
| Backlog rank | `docs/discover/backlog-YYYY-MM-DD.md` | `prioritize-backlog` | `write-prd`, `write-dev-tasks` |
| Experiment | `docs/discover/experiment-YYYY-MM-DD-<slug>.md` | `design-experiment` | `spec-analytics`, `shape-work` |
| Analytics spec | `docs/analytics/<slug>.md` | `spec-analytics` | `implement-change`, `classify-data` |
| PRD | `docs/prd/YYYY-MM-DD-<slug>.md` | `write-prd` | requirements, design, tasks |
| Requirements | `docs/requirements/YYYY-MM-DD-<slug>.md` | `write-requirements` | design, tests, UAT |
| Process map | `docs/process/<slug>.md` | `map-process` | architecture, UAT, change |
| Architecture | `docs/architecture/<area>.md` | `write-architecture` | design, NFR, contracts |
| Design | `docs/design/YYYY-MM-DD-<slug>.md` | `write-design` | tasks, implement, contracts |
| ADR | `docs/adr/NNNN-<slug>.md` | `record-decision` | design, implement |
| NFR spec | `docs/nfr/<slug>.md` | `write-nfr` | design, test strategy, DevOps |
| Integration contract | `docs/contracts/<slug>.md` | `write-integration-contract` | UI, backend, QA |
| Architecture review | `docs/architecture/<area>-review.md` | `review-architecture` | architecture revision |
| Spike | `docs/spikes/YYYY-MM-DD-<slug>.md` | `write-spike` | `record-decision` |
| Data classification | `docs/data/classify-<slug>.md` | `classify-data` | `security-pass` |
| UI spec | `docs/ui/<slug>.md` | `write-ui-spec` | implement, `verify-ui` |
| Design handoff | `docs/ui/<slug>-handoff.md` | `map-design-handoff` | `write-ui-spec`, implement |
| API examples | `docs/contracts/<slug>-examples.md` | `write-api-examples` | `write-tests` |
| Migration plan | `docs/data/migration-<slug>.md` | `plan-data-migration` | `data-change` |
| Dev tasks | `docs/tasks/<slug>.md` | `write-dev-tasks` | `shape-work`, implement |
| Shaped slice | in the conversation or `docs/tasks/<slug>-slice.md` | `shape-work` | implement |
| Test strategy | `docs/qa/strategy-<slug>.md` | `write-test-strategy` | test plan, UAT |
| Test plan | `docs/qa/plan-<slug>.md` | `write-test-plan` | write-tests, UAT |
| Exploratory charters | `docs/qa/charter-<slug>.md` | `charter-exploratory` | `triage-defect` |
| Defect triage | `docs/qa/defect-<id>.md` | `triage-defect` | `debug` |
| A11y pass | `docs/qa/a11y-<slug>.md` | `a11y-pass` | `ready-to-merge` |
| Regression pack | `docs/qa/regression-<slug>.md` | `build-regression-pack` | release |
| UAT pack | `docs/qa/uat-<slug>.md` | `plan-uat` | BA, QA, PM |
| Ready-to-merge record | PR body or `docs/qa/rtm-<id>.md` | `ready-to-merge` | release |
| Release notes | repo’s existing notes path | `ship-notes` | comms, support |
| Runbook | `docs/runbooks/<name>.md` | `write-runbook` | incident, release |
| Pipeline review | `docs/ops/pipeline-review-YYYY-MM-DD.md` | `review-pipeline` | `fix-ci` |
| Environment diff | `docs/ops/env-diff-YYYY-MM-DD.md` | `diff-environments` | DevOps |
| Observability spec | `docs/ops/observability-<slug>.md` | `spec-observability` | runbook |
| Rollback plan | `docs/ops/rollback-<slug>.md` | `plan-rollback` | `cut-release` |
| RAID | `docs/govern/raid.md` | `update-raid` | status, change |
| Status | `docs/govern/status-YYYY-MM-DD.md` | `write-status` | steerco |
| Change assessment | `docs/govern/change-YYYY-MM-DD-<slug>.md` | `assess-change` | decision-rights owner |
| Increment plan | `docs/govern/increment-YYYY-MM-DD.md` | `plan-increment` | `deliver-slice` |
| Blocker triage | `docs/govern/blockers-YYYY-MM-DD.md` | `triage-blockers` | `update-raid` |
| Steerco pack | `docs/govern/steerco-YYYY-MM-DD.md` | `draft-steerco` | program manager |
| Dependency map | `docs/govern/dependencies.md` | `map-dependencies` | contracts, RAID |
| Handoff | `docs/handoffs/YYYY-MM-DD-<slug>.md` | `handoff` | next human or session |

Operational skills that do **not** add a new program-artifact type (they change code, run a check, or write a session report): `explore-codebase`, `explain-code`, `implement-change`, `write-tests`, `debug`, `refactor-safely`, `data-change`, `start-project`, `write-docs`, `commit`, `open-pr`, `review-change`, `lean-review`, `engineering-bar`, `security-pass`, `performance`, `production-pass`, `verify-ui`, `cut-release`, `incident-triage`, `fix-ci`, `revert-change`. They still refuse when their required input is missing.

## Tracker vs git

| Lives in git markdown | Lives in the tracker |
| --- | --- |
| Problem, success, requirements, design, contracts, runbooks, RAID narrative, status narrative | Id, owner, date, state, link back to the git path |

Skills that talk to a tracker write **ids and links**. They do not treat the ticket description as the spec if a git artifact exists.
