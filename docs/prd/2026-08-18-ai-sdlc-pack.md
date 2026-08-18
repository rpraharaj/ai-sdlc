# PRD: Portable AI SDLC pack

Keep every heading. Write `n/a` when a section does not apply. Do not invent users, metrics, or legal rules.

- **Status:** accepted
- **Date:** 2026-08-18
- **Author:** this session
- **Reviewers:** none
- **Related:**
  - [Architecture](../architecture/operating-system.md)
  - [Design](../design/2026-08-18-portable-pack.md)
  - [Doc index](../README.md)

## Summary

A large program has program managers, project managers, product managers, business analysts, solution architects, UI developers, backend developers, QA, and DevOps. They need a shared way of working with AI coding tools — not a different prompt library per tribe, and not a pack that only runs in one vendor’s agent.

This product is a **portable delivery operating system**: shared program context, skills that produce named artifacts, a small set of agent profiles, role cards, and gated workflows. It is written against open formats ([AGENTS.md](https://agents.md/), [Agent Skills / SKILL.md](https://agentskills.io/specification)) so the same files work in Claude Code, Cursor, Codex, GitHub Copilot, Gemini CLI, Windsurf, Grok, and any other client that reads those formats.

Success is that two people on different tools produce the same kind of artifact, with the same traces and the same human stops.

## Problem

Programs adopt “everyone use AI” and get nine overlapping assistants. Each role invents users, status, and architecture. Specs do not chain. Job-title agents cannot be shared. A pack written for one tool’s slash commands, proprietary agent YAML, or orchestration language is unusable for the rest of the team.

Evidence from the shaping conversation: the program needed one portable pack (program + engineering) in this repo, not a prompt library per tribe.

## Current behavior

- This repository is a standalone pack: context templates, 66 portable skills (program + core engineering), nine agent profiles, nine role cards, six workflows, pointer adapters, and static evals.
- A consuming product repo is not created until someone follows `INSTALL.md` and fills `context/` for that program.
- Two-client discovery on a live workstream has not been proven.

## Audience

- Primary: people delivering a multi-team software program who will run skills in whatever AI coding tool their team already uses.
- Secondary: platform / enablement owners who will version and distribute the pack.
- Out of audience: people looking for a chatbot persona named after their job title; people who want a vendor lock-in to one IDE.

## Goals

- One work-type taxonomy (not an org chart) that every role can navigate.
- Artifacts that chain: opportunity → PRD → requirements → architecture/design → tasks → implementation → tests → ready-to-merge → release → status.
- Skills and context that install via open conventions and do not name a vendor’s tools in the procedure.
- Human decision rights stay human (scope, money, go-live, production, legal).
- A first slice small enough to pilot on one workstream.

## Non-goals

- One agent per job title.
- A second copy of these procedures in another repo as the source of truth.
- A custom runtime, marketplace, or new orchestration language as a requirement.
- Replacing Jira / Azure DevOps / Figma as trackers — they hold ids, owners, dates; git markdown holds specs.
- Mandating a single AI product for the program.
- Training 80 people on 40 skills in one town hall.

## Scope

- In: operating model, portability rules, skill/agent/workflow standards, artifact chain, catalogs, role cards, rollout, governance, and the pack files those documents describe (`context/`, `skills/`, `agents/`, `playbooks/`, `workflows/`, `adapters/`, `evals/`).
- Out: filling `context/` for a live workstream (that happens in the consuming product repo); live two-client discovery; a marketplace or live LLM eval harness.

## Success

- Baseline today: this pack is implemented in this repo. A consuming product repo is not created until someone follows `INSTALL.md`. Two-client discovery on a live workstream has not been proven.
- Target: a skill installed into `.agents/skills/` is usable without edits in at least two different Agent Skills clients; a reviewer can refuse the next artifact if the previous one is missing.
- Checks:
  - [x] A stranger can name the next artifact from the chain (`docs/reference/artifact-chain.md`); skills refuse when the previous artifact is missing.
  - [x] Every skill has a verb+artifact name, a handoff table, a template, a yes/no bar, and a human-stop list (`skills/` — 66).
  - [x] Portability rules forbid vendor tool names and lock `.agents/skills/` + `AGENTS.md` (`docs/reference/portability.md`); `scripts/check-pack.py` enforces the denylist on canonical files.
  - [x] Role cards exist as `playbooks/*.md`.
  - [x] Adapters are pointers only (`adapters/`); eval fixtures and refuse-language cases exist (`evals/`).
  - [ ] A human listed the same skill from `.agents/skills/` in two different clients on a consuming repo.

## User stories

1. As a **product manager**, I can run the same `write-prd` procedure in Cursor or Codex, so that the BA receives one PRD shape.
2. As a **business analyst**, I can refuse to write requirements when there is no PRD, so that we do not invent scope.
3. As a **solution architect**, I can point implementers at a design and contracts, so that UI and backend do not invent a second API.
4. As a **developer**, I can use this pack’s engineering skills plus the program `context/`, so that “done” is the same command list everywhere.
5. As a **QA lead**, I can trace a test case to a Must requirement, so that UAT is not a surprise.
6. As a **program manager**, I can produce status that only cites RAID, git, or CI, so that steerco is not theatre.
7. As an **enablement owner**, I can ship one pack that both Claude Code and Copilot discover, so that we do not maintain two libraries.

## Journeys

- Happy path: human names the next artifact → agent loads the matching skill from `.agents/skills/` → reads required inputs → writes the template → stops on human decisions → names the next skill.
- Empty / first-time: no program context yet → Wave 0 writes glossary, systems of record, definition of done, decision rights, environments → then the first opportunity brief.
- Error / denied: previous artifact missing, or a human-stop is required → skill stops and names what is needed. It does not invent users, SLOs, vendors, or RAG status.
- Permission / role variants: implementer may edit product code; reviewer may not edit the diff it reviews; releaser may not deploy production without a human; coordinator may not change architecture.

## Requirements

### Must

- Taxonomy is **work type**, not job title. Role cards are indexes.
- Canonical files are Markdown. Skills follow the Agent Skills spec (`name`, `description`, `SKILL.md` body). Context follows AGENTS.md (plain Markdown, no required fields).
- Install surface for skills is `.agents/skills/` in a consuming repo (project) and `~/.agents/skills/` (user). See [portability](../reference/portability.md).
- Skill bodies do not name vendor-specific tools, slash-command dialects, or orchestration languages.
- Every skill has: when-not-to-use handoff table, required inputs, human-stop list, output path + template, yes/no quality bar, next skill.
- One home per fact (glossary, DoD, system names, this catalog).
- Git markdown is canonical for specs; trackers are canonical for ids/owners/dates.
- Production, money, account, and legal decisions stay human.

### Should

- Thin adapters (symlinks or one-line pointers) for tools that do not yet scan `.agents/skills/` or `AGENTS.md`.
- Engineering delivery skills live in this same pack (standalone repo).
- Workflows are Markdown sequences first; a vendor orchestrator is an optional adapter, not the source of truth.
- Agent profiles describe capability (read / write / execute / MCP), not personality.

### Later

- Live LLM eval harness (static fixtures already exist under `evals/`).
- Organization-wide marketplace.
- Auto-generated adapter folders for every client.

## UX notes

n/a as a UI product. The “UX” is: a person opens their usual AI coding tool in a repo, types the work they need (or `/skill-name` if the client supports it), and the same procedure runs. Role cards are one-page start-here documents.

## Analytics

n/a — this product has no telemetry of its own. Rollout measures (time to first draft, refuse rate, invented-fact rate) are manual until a later slice.

## Privacy and data

Skills must not instruct agents to paste secrets, production data, or credentials into prompts, tickets, or git. Program context files must not contain secrets. Live customer data is out of scope for examples.

## Constraints

- Technical: must remain valid Agent Skills + AGENTS.md. No new runtime required to use the pack.
- Legal / privacy: do not invent compliance rules; `context/decision-rights.md` and `classify-data` record what the program already decided.
- Timeline: pack files are implemented; a consuming-program install is the next human step.
- Budget / staffing: n/a.

## Dependencies

- [AGENTS.md](https://agents.md/) (Agentic AI Foundation / Linux Foundation).
- [Agent Skills specification](https://agentskills.io/specification).
- Consuming program’s systems of record (tracker, git, CI, design tool) — named in context files, not hard-coded here.

## Rollout

- Flag / experiment: pilot one live workstream before a program mandate.
- Markets / segments: one program first.
- Support / comms: role cards, not a 40-skill town hall.
- Rollback of the product change: delete or disable the pack in the consuming repo; no runtime to roll back.

Detail: [rollout](../reference/rollout.md).

## Risks

- Tool vendors add incompatible frontmatter; we stay on the spec’s required fields only.
- Teams still keep private prompt libraries; governance must treat the pack as the only shared procedure.
- Skills that are too generic become “be a helpful PM”; the standard forbids that.
- Adapters multiply and become a second source of truth; adapters may only point, never copy procedure text.

## Assumptions

- Teams will use *some* Agent Skills–compatible client, or can follow a Markdown skill by pasting it. A tool that cannot read files cannot use this pack fully.
- The program will keep specs in git (or will accept that as the recommendation).
- Humans remain accountable for decisions the skills flag as human-stops.

## Open questions

- Blocking: none for the pack itself.
- Non-blocking:
  - Which two clients will the first install test target?
  - What is the consuming program’s real tracker and CI (named later in that repo’s `context/systems-of-record.md`)?

## Next

Install this pack into one live product repo (`INSTALL.md`) and prove discovery in two clients.
