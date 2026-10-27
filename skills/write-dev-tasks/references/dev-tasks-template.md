# Dev tasks: <initiative>

Keep every heading. Write `n/a` when a section does not apply. Copy the Task block once per task. Do not invent files or acceptance.

- **Status:** draft | in progress
- **Date:** <YYYY-MM-DD>
- **Source:** <PRD / design / architecture / user>
- **Related:** <paths or none>
- **Source revisions / approval evidence:** <baseline revisions and references in the approval home, or unassigned>

## Goal

<one or two sentences>

## Prerequisites

<env, access, flags, prior deploys — or none>

## Order

Do in this order. Do not start N+1 until N is shippable unless a task says it can run in parallel.

## Task 1 — <title>

- **Kind:** defect | change | data-change | docs | spike | verify-ui
- **Depends on:** none | Task N
- **Traces to:** <PRD requirement / design slice / none>
- **Requirement / defect / shaped acceptance:** <artifact path + id and source revision>
- **In scope:**
- **Out of scope:**
- **Acceptance:**
  - [ ] <yes/no a stranger can verify>
- **Likely files:** `<path>` — <why>
- **Prove:** <test command, verify-ui, or n/a>
- **Notes:**
- **Next skill:** `shape-work` | `implement-change` | `data-change` | `write-tests` | `write-docs` | `verify-ui`

## Task 2 — <title>

- **Kind:**
- **Depends on:**
- **Traces to:**
- **Requirement / defect / shaped acceptance:**
- **In scope:**
- **Out of scope:**
- **Acceptance:**
  - [ ]
- **Likely files:**
- **Prove:**
- **Notes:**
- **Next skill:**

## Out of this batch

- <follow-up that must not sneak into Task 1>

## Batch done

- [ ] <the initiative is shipped when these are true>

## Must coverage

| Requirement (path + id) | Source revision | Task ids | Verification | Gap |
| --- | --- | --- | --- | --- |
| | | | | |

## Risks

- Blast radius:
- Data / compatibility:
- Security / privacy:

## Next

<shape-work on Task 1 | implement-change on Task 1 | stop — need user>
