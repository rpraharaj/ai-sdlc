---
name: review-pipeline
description: >
  Review CI pipeline config for missing gates, secrets, and flakes —
  from files you can read. Use when the user asks to review CI, review
  the pipeline, or /review-pipeline. Do not invent jobs. Do not add YAML
  unless asked to implement.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2"
  stage: "60-release"
---

# Review pipeline

Read the **pipeline that exists**. This is not `fix-ci` (that fixes a red run) and not `cut-release`.

Do not invent jobs. Do not “add more YAML” as the whole answer.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| A specific red run | `fix-ci` |
| Env drift | `diff-environments` |
| Release go/no-go | `plan-rollback` / `cut-release` |

## Required inputs

- CI config in the repo (paths you find) or a log the user named
- `AGENTS.md` (what checks the repo claims)

If there is no CI file and no log, **stop**.

## Human decisions (do not invent)

- Which missing gate is required vs nice

## Procedure

1. Read `AGENTS.md` if present. Find CI configs (common names: `.github/workflows/`, `.gitlab-ci.yml`, `Jenkinsfile`, `azure-pipelines.yml`). Read what exists.
2. Compare claimed checks in `AGENTS.md` to jobs you saw. Gaps are findings.
3. Look for: secrets in the file, unbounded matrix, no test job, skip-on-failure of the required check.
4. Find the home: `docs/ops/pipeline-review-YYYY-MM-DD.md`.
5. Open [references/pipeline-review-template.md](references/pipeline-review-template.md). Copy every heading. Write `n/a` when unused.

## Output

- Path: `docs/ops/pipeline-review-YYYY-MM-DD.md`
- Template: `references/pipeline-review-template.md`

## Quality bar

- [ ] Every finding cites a path or log line
- [ ] No invented job name
- [ ] Secrets called out if present in the config you read
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Finding count
3. Next skill: `fix-ci` or `implement-change` if the user wants a fix
