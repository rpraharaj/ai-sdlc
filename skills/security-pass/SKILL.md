---
name: security-pass
description: >
  Threat-model this diff only — new reachable surface, authorization,
  injection, secrets, and PII. Use when the change touches auth, input,
  files, HTML, URLs, or secrets, when ready-to-merge dispatches it, or
  when the user asks for a security review of the change.
license: MIT
metadata:
  pack: ai-sdlc
  version: "0.3"
  stage: "50-verify"
---

# Security pass

Adversarial review of **this delta**. Do not edit product code unless they asked you to fix what you found.

## Is this the right skill?

| Signal | Do this instead |
| --- | --- |
| Data classification of a change | `classify-data` |
| Whole-company audit | stop — this skill is the diff |
| Merge gate | `ready-to-merge` (it dispatches this) |

## Required inputs

- The current diff
- `AGENTS.md`

## Human decisions (do not invent)

- Broadening authz to “fix” a fail (forbidden)

## Procedure

1. Inventory new/changed reachable surfaces, trust boundaries, authz, secrets/PII. If empty, report **no new reachable surface** and still scan for leaked secrets.
2. For each surface walk: authorization (IDOR), untrusted input to sinks, injection/traversal, SSRF, uploads, secrets, PII. Skip items the diff cannot hit.
3. Severity: bug / suggestion / nit.
4. Write [references/security-template.md](references/security-template.md). Findings need `file:line`.

## Output

- Path: reply
- Template: `references/security-template.md`

## Quality bar

- [ ] Inventory listed
- [ ] Secrets pass or fail
- [ ] No theoretical issue without a path from this change

## Done

Pass | fail. Fixes are `implement-change` + `write-tests`.
