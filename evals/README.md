# Evals

Static checks that refusal instructions and fixture labels are present. These checks do not demonstrate that a model follows the instructions.

```sh
python3 scripts/check-evals.py
```

`scripts/check-pack.py` runs this too.

## What is automated

- Skill bodies still contain the refuse language named in [cases.json](cases.json) (`stop`, next skill, `unknown`).
- “Good” fixtures have the headings a stranger would need.
- “Bad” fixtures keep their `eval-fail` markers so we do not accidentally clean them into passing docs.

The source validator also runs negative CLI regression tests in `scripts/test-check-pack.py`: forbidden or malformed frontmatter, broken references, unknown workflow skills/profiles, incompatible test authorship, missing quality bars, and non-overwriting installation. Initial-install tests use disposable clean Git snapshots and verify ignored-file exclusion, tracked-secret refusal, dirty/unversioned-source refusal, and retained regular assets. Installed-content tests refresh inventory digests before checking invalid skills/workflows so a matching digest cannot conceal a bad merge.

## What is not automated

Running a model against a fixture. To do that by hand:

1. Copy `evals/fixtures/<file>` into a scratch product repo that already has `context/` and `.agents/skills/`.
2. Invoke the skill named in the case.
3. Use the observed cases and run-log contract in [pilot.md](../docs/reference/pilot.md); `cases.json` contains static string assertions, not behavioral `expect` verdicts.
4. For a valid-input case, establish fixture approval evidence in the scratch context first and apply the skill quality bar. Fictional fixture signers are only test data, never approval for real work.
5. Missing-input and adversarial cases must stop or label unknowns as the pilot case specifies. Save actual outputs and a human verdict in both clients.

## Fixtures

| File | Intent |
| --- | --- |
| [prd-good.md](fixtures/prd-good.md) | Content-valid PRD; requires fixture approval evidence before use |
| [prd-bad.md](fixtures/prd-bad.md) | Invented users, no success, solution-as-problem |
| [requirements-good.md](fixtures/requirements-good.md) | Must items trace to the good PRD |
| [requirements-bad.md](fixtures/requirements-bad.md) | No traces, invented Must |
| [raid-good.md](fixtures/raid-good.md) | Every row has a source |
| [status-invented.md](fixtures/status-invented.md) | Green with no citations |
| [nfr-invented.md](fixtures/nfr-invented.md) | Typical SLOs with no source |
