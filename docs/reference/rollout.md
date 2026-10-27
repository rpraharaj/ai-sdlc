# Rollout

Do not train 80 people on 40 skills. Train them on **their role card** and one rule: start the skill that matches the next artifact.

The live acceptance record, two-client cases, measurements, and exit/stop criteria have one home: [pilot.md](pilot.md). Timings below are rollout guidance, not program commitments.

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
- Install via `.agents/skills/` and name two clients and pass the observed pilot cases.

Measure:

- Time to first usable draft of each artifact
- Correct and unnecessary refusals, checked against the pilot cases
- How many invented facts a reviewer caught

## Wave 2

Done in this pack repo: Wave 2 skills, nine agent profiles, nine playbooks, six Markdown workflows.

Still per consuming program: complete two-client behavior checks; adapters only if a client failed that test.

## Wave 3

Done in this pack repo: pointer adapters (`adapters/`) and static eval fixtures (`evals/`, `python3 scripts/check-evals.py`).

Still per consuming program: two-client behavior checks; adapters only if discovery failed; kill skills unused in a 30-day pilot.

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

Follow the ownership-aware rollback/removal steps in [INSTALL.md](../../INSTALL.md). Preserve program facts, product artifacts, unrelated skills, and local modifications. No runtime needs undeployment.
