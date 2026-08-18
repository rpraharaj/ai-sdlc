---
name: classify-data
description: >
  Classify data a change touches — PII, retention, residency — without
  inventing legal rules. Use when the user asks to classify data, mark
  PII, data handling, or /classify-data. Do not write product code.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.2"
  stage: "30-design"
---

# Classify data

Say **what data this change touches** and what you do not know. This is not `write-nfr`, not `security-pass` (that is a diff), and not legal advice.

Do not invent retention periods, residency, or lawful basis.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Threat model of a diff | `security-pass` |
| Event list | `spec-analytics` |
| Schema expand/contract | `data-change` / `plan-data-migration` |

## Required inputs

- The change: requirements, design, or contract path
- `context/` if it already states data rules

## Human decisions (do not invent)

- Retention, residency, lawful basis
- Whether a field is allowed to be stored

## Procedure

1. Read `AGENTS.md` if present. Read `context/` files that mention data or privacy.
2. Read the named spec. List fields / artifacts the change stores, sends, or logs.
3. Find the home: first existing `docs/data/`, or offer to create it. Name: `docs/data/classify-<slug>.md`.
4. Open [references/classify-template.md](references/classify-template.md). Copy every heading. Write `n/a` when unused.
5. Each item: name, flows where, PII yes/no/unknown, retention source or `unknown`, residency source or `unknown`.
6. Secrets and credentials are **never** “unknown PII” — they are secrets; do not put values in the doc.
7. Point legal questions at `context/decision-rights.md`. Do not answer them.

## Output

- Path: `docs/data/classify-<slug>.md`
- Template: `references/classify-template.md`

## Quality bar

- [ ] Spec path is named
- [ ] Every field has PII yes / no / unknown
- [ ] Retention/residency are sourced or `unknown`
- [ ] No legal rule invented
- [ ] Unused headings are `n/a`

## Done

1. Path
2. Field count + unknown count
3. Next skill: `security-pass` on the implementation; human on unknowns
