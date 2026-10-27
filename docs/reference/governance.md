# Governance

## Ownership

| Pack area | Owner |
| --- | --- |
| `10-discover`, `20-shape` | Product |
| `30-design` | Architecture |
| `40-build` | Engineering |
| `50-verify` | QA + engineering |
| `60-release` | DevOps / platform |
| `70-govern`, context decision-rights | PMO |
| Portability, adapters, this docs tree | Enablement |

Each skill inherits the accountable role for its `metadata.stage` from this table. A consuming program names the actual human owners in context. Optional per-skill owner overrides belong in metadata; until named, do not invent an individual owner.

## Versioning

- `metadata.pack`: `ai-sdlc`
- `metadata.version`: stable semver `major.minor.patch` on each skill; bump when the procedure or template changes. The pre-pilot two-part values are normalized in this hardening change; substantive procedure/template changes also receive a minor bump.
- Consuming repos pin a full clean git commit; a reviewed tag may name that commit. No release tag is implied by a version string. The install inventory records file digests and dirty-source state. See [INSTALL.md](../../INSTALL.md) for initial installation, merge-aware updates, and removal.

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

`scripts/test-check-pack.py` checks rejected mutations and safe installation against disposable copies. `python3 scripts/check-pack.py` runs structural checks, static eval cases, and those regression tests; the source repository CI runs that same command. These checks do not execute a model or prove instruction adherence.

Initial payloads come only from committed files in a clean source checkout, with prohibited secret filenames rejected. The installed validator rechecks actual skill and pack-owned navigation content independently of the inventory digests, including after a local merge. Filename policy is shared in `scripts/pack_files.py`; a digest records bytes, not approval or validity.

Observed two-client behavior follows [pilot.md](pilot.md). Do not replace the quality bar with a hidden rubric.

## Retirement

If a skill is unused for 30 days of a named pilot, file a remove-or-rewrite issue. Invalid skills (see [skill-standard](skill-standard.md)) are removed, not left “for later.”
