# DevOps

Profile: `releaser`. Production, money, and account changes stay human.

Hand `fix-ci` and pipeline or product edits to `implementer`; use `incident-lead` for incident triage. A release profile does not grant production approval.

| | |
| --- | --- |
| Jobs this week | Pipeline, environments, release, incident |
| Run | `review-pipeline`, `diff-environments`, `write-runbook`, `spec-observability`, `cut-release`, `incident-triage`, `plan-rollback`, `fix-ci` |
| Own | Pipelines, runbooks, environments (`context/environments.md`) |
| Consume | Designs, NFRs |
| Still decide | Production deploy; account and billing changes |

## This week

1. Fill `context/environments.md` before inventing a promo path.
2. `review-pipeline` and `diff-environments` from files you can read.
3. New failure mode → `write-runbook` + `spec-observability` + `plan-rollback`.
4. Live incident → `incident` workflow. You do not silently patch prod.

Workflows: `release-train`, `incident`.
