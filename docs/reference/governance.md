# Governance

## Ownership

| Pack area | Owner |
| --- | --- |
| `10-discover`, `20-shape` | Product |
| `30-design` | Architecture |
| `40-build` and core engineering skills | Engineering |
| `50-verify` | QA + engineering |
| `60-release` | DevOps / platform |
| `70-govern`, context decision-rights | PMO |
| Portability, adapters, this docs tree | Enablement |

One owner per skill in `metadata` later. Unowned skills are not merged.

## Versioning

- `metadata.pack`: `ai-sdlc`
- `metadata.version`: semver string on each skill; bump when the procedure or template changes.
- Consuming repos pin a git tag of this pack.

Do not break an artifact template in the same change that consumes the new shape. Expand (accept old + new headings) then contract.

## Change control for the pack

A change to a skill must include:

1. Why the current procedure failed (a real trace, not a vibe).
2. The template or bar that now differs.
3. A note in the skill’s `Done` / changelog line if a consuming artifact shape moved.

A change that only adds vendor frontmatter belongs in `adapters/`, not in the skill.

## Decision rights (pack vs program)

`context/decision-rights.md` is **per consuming program**. This file is **how we change the pack**.

Pack decisions that need a one-page ADR before implementation if anyone disagrees:

- Canonical install path (`.agents/skills/`)
- Markdown-first workflows
- Whether a later install script is needed besides `INSTALL.md`
- The nine-profile limit

## Safety

- No secrets in the pack or in examples.
- Skills must not instruct unattended production changes, purchases, or cloud-account edits.
- Project-level skills are untrusted until the host marks the workspace trusted.
- Reviewer profiles must not edit the diff they review.

## Evaluations (Wave 3)

Static fixtures live under `evals/`. `python3 scripts/check-evals.py` (also run by `check-pack`) grades:

- Skill bodies still contain the refuse language named in `evals/cases.json`
- Good fixtures keep the headings a stranger would need
- Bad fixtures keep their `eval-fail` markers

A live LLM run against those fixtures is still human. Do not replace the quality bar with a hidden rubric.

## Retirement

If a skill is unused for 30 days of a named pilot, file a remove-or-rewrite issue. Invalid skills (see [skill-standard](skill-standard.md)) are removed, not left “for later.”
