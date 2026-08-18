# Skill standard

A skill is a folder that teaches **any** compatible agent how to produce or check one artifact. It is not a job description.

## Directory

```text
skills/<name>/
  SKILL.md              # required
  references/           # templates and long notes, loaded on demand
  assets/               # static files only if required
  scripts/              # portable scripts only if required
```

`<name>` matches frontmatter `name`.

## Frontmatter

Only [Agent Skills spec](https://agentskills.io/specification) fields in the canonical file:

```yaml
---
name: write-requirements
description: >
  Turn an approved PRD into testable functional requirements with traces
  and acceptance. Use when the user asks for requirements, a BRD,
  functional spec, or /write-requirements. Do not write product code.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.1"
  stage: "20-shape"
---
```

`description` must include **what** and **when**, plus trigger phrases. Max 1024 characters. This is how clients auto-invoke. “Helps with requirements” is invalid.

Do not add vendor-only keys here. See [portability](portability.md).

## Body shape (required sections)

The spec does not mandate body headings. This pack does, so skills compose.

```markdown
# <Title>

One sentence: what this produces, and what it is not.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| … | <other-skill> |

## Required inputs

- Path to the previous artifact (or stop)
- Named systems from `context/systems-of-record.md` when relevant

## Human decisions (do not invent)

- …

## Procedure

Numbered steps. Read evidence. Name actions in portable language
(“read the file”, “run the test command recorded in AGENTS.md”).

## Output

- Path: `docs/<area>/YYYY-MM-DD-<slug>.md` (or the consuming repo’s existing home)
- Template: `references/<name>-template.md`
- Keep every heading; write `n/a` if unused

## Quality bar

Yes/no checks a stranger can apply. At least one would fail today.

## Done

1. Path (or the text if the repo has no docs home yet)
2. The one-line result
3. Next skill
```

## Rules for the procedure

- Point at `context/` and `AGENTS.md`. Do not paste the glossary or DoD.
- Keep `SKILL.md` under 500 lines. Put the template in `references/`. Tell the agent **when** to open each reference file.
- Prefer a default tool (“use the tracker CLI this repo already has”) over a menu of vendors.
- If a script is bundled, it must be self-contained and fail with a clear stderr.
- Do not implement product code unless the skill’s job is implementation (`implement-change` and the other `40-build` skills).

## Naming

`verb-artifact` or `verb-check`: `write-prd`, `update-raid`, `plan-uat`, `ready-to-merge`.

Invalid: `pm-agent`, `ba-helper`, `helpful-architect`.

## Stages (metadata only)

Used to group the catalog, not to create separate runtimes:

| `metadata.stage` | Meaning |
| --- | --- |
| `10-discover` | opportunity, research, priority |
| `20-shape` | PRD, requirements, process, scope |
| `30-design` | architecture, design, ADR, NFR, contracts |
| `40-build` | implement, explain, refactor |
| `50-verify` | review, test strategy, UAT, ready-to-merge |
| `60-release` | release, runbook, incident, observability |
| `70-govern` | status, RAID, comms, change control |
| `00-context` | not skills — context files |

## Quality of the skill itself

A skill is invalid if:

- It has no “do this instead” table.
- It has no human-stop list (unless the skill is a pure mechanical check).
- Success is “good” or “complete” rather than yes/no.
- It restates another skill’s template.
- It names a vendor tool or “you are \<role\>” as the whole body.
