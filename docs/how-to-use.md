# How to use this pack

This repository is **not an application**. It is a set of procedures you install into a **product** repo, then run with whatever AI coding tool that team already uses.

## 1. Install into a product repo

Follow [INSTALL.md](../INSTALL.md). Minimum:

1. Run the initial installer dry run from a reviewed, pinned source checkout; inspect collisions, then use `--apply`. Existing program rules and facts are preserved.
2. Fill `context/` for that program and merge missing starter sections into an existing `AGENTS.md`. Record exact check commands, actual decision owners, and approval evidence.
3. Complete [pilot.md](reference/pilot.md) in two selected clients before widening use. Source checks and client skill listing alone do not prove behavior.

Do not work in *this* pack repo unless you are changing the pack itself.

## 2. Fill context before you run skills

Leave a field as unknown only while it is still unknown. Skills stop or invent if `context/` is still a blank template.

## 3. Open your usual AI tool in the product repo

You do not pick a “PM agent” or “BA agent.” You ask for the **next artifact**:

- “Write an opportunity brief for …”
- `/write-prd`
- `/write-requirements`
- `/ready-to-merge`

The client should load the matching skill from `.agents/skills/` (name + description). If it does not list the skill, use an [adapter](../adapters/README.md) — symlink or one-line pointer. **Never copy a `SKILL.md` body into a vendor folder.**

## 4. Open your role card

Start at [playbooks/](../playbooks/). That page names the skills you run, what you own, and what you must still decide.

One rule: **start the skill that matches the next artifact.** If the previous file is missing, the skill should stop and name what produces it. Do not invent users, SLOs, RAG, or dates.

## 5. Use a workflow only for a gated path

Optional. Anyone can run skills one at a time. The sequences with human gates are in [workflows/](../workflows/):

| When | Workflow |
| --- | --- |
| New problem, why still open | `shape-initiative` |
| How to build it is open | `design-initiative` |
| One slice to merge | `deliver-slice` |
| Cut a release | `release-train` |
| Weekly pulse | `weekly-program` |
| Prod is hurting | `incident` |

Resolve blocking review findings before final approval, and repeat affected checks/approval when their revision changes. Standalone release skills retain the workflow prerequisites.

Humans still sign what [context/decision-rights.md](../context/decision-rights.md) names (scope, money, go-live, production).

## 6. What each layer is

| You open | It is |
| --- | --- |
| `context/` | Facts about **this** program |
| `.agents/skills/<name>/` | How to produce or check **one** artifact |
| `agents/` | Permission envelope (read / write docs / write code / prod-gated) — map onto your host |
| `playbooks/` | Your start-here page |
| `workflows/` | Several skills in a fixed order |

More detail: [layers](reference/layers.md), [artifact chain](reference/artifact-chain.md), [catalog](reference/catalog.md).

## 7. Changing the pack itself

Work in this repo only to edit procedures. After skill or context-template edits:

```sh
python3 scripts/check-pack.py
```

Rules for that work: root [AGENTS.md](../AGENTS.md). External PRs: [CONTRIBUTING.md](../CONTRIBUTING.md).
