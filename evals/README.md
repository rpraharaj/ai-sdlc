# Evals

Static checks that the pack still refuses invented facts and that fixtures are labeled. This is not a live LLM run.

```sh
python3 scripts/check-evals.py
```

`scripts/check-pack.py` runs this too.

## What is automated

- Skill bodies still contain the refuse language named in [cases.json](cases.json) (`stop`, next skill, `unknown`).
- “Good” fixtures have the headings a stranger would need.
- “Bad” fixtures keep their `eval-fail` markers so we do not accidentally clean them into passing docs.

## What is not automated

Running a model against a fixture. To do that by hand:

1. Copy `evals/fixtures/<file>` into a scratch product repo that already has `context/` and `.agents/skills/`.
2. Invoke the skill named in the case.
3. For `expect: refuse` cases, the agent must stop and name the next skill — not write the artifact.
4. For `expect: produce` cases, the artifact must pass that skill’s quality bar.

## Fixtures

| File | Intent |
| --- | --- |
| [prd-good.md](fixtures/prd-good.md) | Signed-shaped PRD a BA can consume |
| [prd-bad.md](fixtures/prd-bad.md) | Invented users, no success, solution-as-problem |
| [requirements-good.md](fixtures/requirements-good.md) | Must items trace to the good PRD |
| [requirements-bad.md](fixtures/requirements-bad.md) | No traces, invented Must |
| [raid-good.md](fixtures/raid-good.md) | Every row has a source |
| [status-invented.md](fixtures/status-invented.md) | Green with no citations |
| [nfr-invented.md](fixtures/nfr-invented.md) | Typical SLOs with no source |
