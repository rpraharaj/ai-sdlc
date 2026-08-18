# Rollout

Do not train 80 people on 40 skills. Train them on **their role card** and one rule: start the skill that matches the next artifact.

## Wave 0 — one week, no new skills

- Write the five [context](layers.md) files for **one** live workstream (not templates-for-their-own-sake).
- Install this pack’s skills into that workstream’s `.agents/skills/`.
- Publish three role cards: product manager, business analyst, implementer.
- Point the consuming repo `AGENTS.md` at the context files.

Exit: a stranger can name systems of record and Definition of Done without a meeting.

## Wave 1 — two to four weeks on a live workstream

Done in this pack repo: the [twelve Wave 1 skills](catalog.md) and the `shaper` / `reviewer` / `coordinator` profiles.

Still per consuming program:

- Run `shape-initiative` on one real feature, end to end, with humans signing the gates.
- Install via `.agents/skills/` and prove discovery in **two** clients (to be named).

Measure:

- Time to first usable draft of each artifact
- How often the next skill refused to start (should be > 0 if people skip steps)
- How many invented facts a reviewer caught

## Wave 2

Done in this pack repo: Wave 2 skills, nine agent profiles, nine playbooks, six Markdown workflows.

Still per consuming program: prove discovery in two clients; adapters only if a client failed that test.

## Wave 3

Done in this pack repo: pointer adapters (`adapters/`) and static eval fixtures (`evals/`, `python3 scripts/check-evals.py`).

Still per consuming program: two-client discovery; adapters only if a client failed that test; kill skills unused in a 30-day pilot.

## What “good” looks like

- The same glossary term appears in the PRD, the requirements, the contract, and the tests.
- `ready-to-merge` is the only way a slice is called done, and it prints command output.
- Status does not contain a fact that is not in RAID, git, or CI.
- A BA and an architect can name the next skill without a meeting.
- Production, money, and account changes still require a human.

## What “failing” looks like

- A `project-manager` agent that writes status, code, and architecture.
- Each tribe keeps a private prompt library.
- Skills restate the glossary.
- Success is “people used a chatbot this week.”
- The model is allowed to invent users, SLOs, vendors, or “green” status.

## Rollback

Remove or pin back the pack in the consuming repo. No runtime to undeploy. Artifacts already written stay; they are ordinary Markdown.
