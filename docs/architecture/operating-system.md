# Architecture: AI SDLC operating system

Keep every heading. Write `n/a` when a section does not apply. Do not invent services, SLOs, or vendors.

- **Status:** accepted
- **Date:** 2026-08-18
- **Author:** this session
- **Reviewers:** none
- **Related:**
  - [PRD](../prd/2026-08-18-ai-sdlc-pack.md)
  - [Design](../design/2026-08-18-portable-pack.md)
  - [Layers](../reference/layers.md)
  - [Portability](../reference/portability.md)

## Summary

The system is a **file-based operating system for AI-assisted delivery**, not a hosted product. Shared context, skills, agent profiles, workflows, and role cards live in git as Markdown. Any coding agent that can read the repo is a runtime. The main trade-off: we optimize for portability and one source of truth, and we refuse vendor-native features (proprietary agent YAML, orchestration DSLs, slash-only commands) as the canonical form. Those may exist only as thin adapters.

## Context

A multi-role program wants everyone to use AI tools. The shape is how to package procedures so they survive tool choice, org-chart change, and new people. This repository **is** that package: program skills and core engineering skills live in one standalone tree.

## Scope of this doc

- In: layers, boundaries, what is data vs control flow, how tools attach, what is out of the runtime.
- Out: file-by-file install layout (that is the [design](../design/2026-08-18-portable-pack.md)); the skill catalog (that is [catalog](../reference/catalog.md)); rollout waves (that is [rollout](../reference/rollout.md)).

## Goals and non-goals

- Goals:
  - Four layers: context, skills, agents, workflows — plus role cards as an index, not a layer that executes.
  - Work-type taxonomy; artifacts as the contract between roles.
  - Open formats only at the core.
- Non-goals:
  - A central agent server the program must run.
  - Job-title agents as first-class types.

## Current state

This repo holds the operating system: `docs/`, `context/` templates, `skills/` (66), `agents/`, `playbooks/`, `workflows/`, `adapters/`, `evals/`. A consuming product repo is created by `INSTALL.md`, not by this tree growing an application.

## Actors and systems

**People:** program manager, project manager, product manager, business analyst, solution architect, UI developer, backend developer, QA, DevOps, enablement owner.

**Runtimes (any one is enough):** an Agent Skills–compatible coding agent in a local or cloud workspace that can read the repo. Examples of clients that document support (not dependencies): Claude Code, Cursor, Codex, GitHub Copilot / VS Code, Gemini CLI, Windsurf, Goose, Amp, Factory, Grok, and others listed at [agentskills.io](https://agentskills.io/home) and [agents.md](https://agents.md/).

**External systems the pack talks *about*, not *as*:** work tracker, git host, CI, design tool, observability, chat. Named per program in context; reached via whatever the local agent already has (MCP, CLI). The pack does not ship those integrations.

## Proposed shape

### Boundaries

| Boundary | What it is | Can fail / deploy apart |
| --- | --- | --- |
| **Context** | Always-on facts: glossary, systems of record, definition of done, decision rights, environments. Loaded via `AGENTS.md`. | Yes — a program can update context without changing skills. |
| **Skills** | On-demand procedures. One skill = one artifact or one check. Agent Skills folders. | Yes — add/remove a skill without changing agents. |
| **Agent profiles** | Permission and tool envelopes (read / write docs / write code / execute / prod-gated). | Yes — same skills, different envelope. |
| **Workflows** | Ordered skill sequences with human gates. Markdown playbooks. | Yes — optional; people can run skills one at a time. |
| **Role cards** | Human index: which skills this role runs. | Yes — docs only; never executed as an agent. |
| **Adapters** | Symlinks or one-line pointers for a specific client. | Yes — must not contain procedure text. |
| **Core engineering skills** | Implement, test, review, merge, release, incident — folders under `skills/`. | Yes — same install path as program skills. |

Things that are **not** boundaries: job titles, vendor products, individual teams.

### Data

There is no database. Durable data is files:

| Kind | Owner | Moves how |
| --- | --- | --- |
| Program facts | Enablement + domain owners | Edited in `context/`; pointed to from `AGENTS.md` |
| Procedures | Pack maintainers | Edited in `skills/<name>/SKILL.md` |
| Artifacts a skill produces | The role that owns that artifact | Written into the *consuming* product repo (`docs/prd/`, etc.), not into this pack |
| Decision log / RAID / status | PMO | Consuming repo or agreed tracker; pack only defines shape |
| Agent profile | Enablement | `agents/*.md` — capability, not persona prose |

One home per fact. Skills point at context; they do not restate the glossary or DoD.

### Control flow

There is no request server. Control flow is:

1. Human states the work (or invokes a skill by name if the client supports it).
2. Runtime discovers skills (catalog = name + description only).
3. Runtime loads one `SKILL.md` when the task matches.
4. Skill reads required inputs from the consuming repo. If missing, it **stops**.
5. Skill writes or checks one artifact.
6. Skill names the next skill. A workflow, if used, is just this sequence written down, with explicit human gates.

Sync, human-paced. No background jobs in the pack itself.

### Identity and tenancy

n/a as a service. Trust follows the coding agent’s project-trust model: project-level skills come from the repo and should only load in a trusted workspace. The pack must not instruct an agent to bypass the host’s permission system.

### External

Optional: Model Context Protocol servers the *host* already configured (tracker, git, docs, observability). The pack names *kinds* of tools (“the project tracker CLI or MCP”), never a required vendor. Money, account, and production-control APIs are forbidden as unattended targets.

## Deployment and environments

The pack is files in git. “Deploy” means: merge to the pack repo, then install (copy, submodule, or subtree) into a consuming repo’s `.agents/skills/` and commit `AGENTS.md` pointers.

No regions, no runtime environment. Consuming programs have their own dev/test/stage/prod — described in *their* `context/environments.md`, not here.

## Quality attributes

Use numbers this repo already has, or targets the user set. Otherwise `n/a` — do not invent SLOs.

- Availability: n/a (files)
- Consistency: one source of truth per fact; adapters never diverge
- Latency: n/a
- Throughput: n/a
- Durability: git history of the pack and of consuming artifacts
- Security / tenancy: no secrets in the pack; skills refuse to write secrets; production actions require a human
- Cost: n/a (token cost is a client concern; skills stay short via progressive disclosure)

## Data classification

This pack contains procedures and templates only. No PII, no credentials. Consuming artifacts may contain business information; skills must say “do not put secrets or live personal data in git or in the prompt.” Per-program classification belongs in the consuming `context/` and, for a given change, in `classify-data`.

## Migration and coexistence

Greenfield for this repo. Coexistence with:

- Vendor files already in a repo (`CLAUDE.md`, `.cursor/rules`, `.github/copilot-instructions.md`) — adapters point at `AGENTS.md`; do not fork instructions.
- Private prompt libraries — superseded for shared procedures; personal user-level skills remain allowed under `~/.agents/skills/`.

Expand-then-contract: add `.agents/skills/` and `AGENTS.md` first; remove duplicate vendor copies only after two clients have loaded the shared path.

## Alternatives considered

### A. Work-type pack on open formats (chosen)

- Pros: portable; one artifact chain; matches how Agent Skills and AGENTS.md actually load; small agent set.
- Cons: less “wow” than named role bots; some clients need a thin adapter.

### B. One agent per job title, per vendor

- Pros: easy to sell in a slide.
- Cons: overlapping procedures; cannot share; invents a second program; dies when the org chart or the tool changes.

### C. Hosted orchestration platform

- Pros: pretty dashboards, enforced gates.
- Cons: new runtime, procurement, lock-in; fails the “any AI coding tool” requirement.

## Decisions

- Taxonomy is work type, not job title. Detail: [principles](../reference/principles.md).
- Canonical skill path is `.agents/skills/`. Detail: [portability](../reference/portability.md).
- Workflows are Markdown first. Vendor orchestrators are adapters.
- Nine capability profiles, not nine departments. Detail: [agent standard](../reference/agent-standard.md).
- Git markdown is canonical for specs. Trackers hold tracking fields.
- Engineering and program skills live in this same pack.

Sticky choices that should get a one-page ADR if anyone later disagrees: skill install path; markdown-first workflows; the nine-profile limit.

## Risks and operability

- Failure modes: a client ignores `.agents/skills/`; a skill invents facts; adapters drift; people bypass skills.
- Observability: later, evals on fixture artifacts. Today, human review of drafts.
- Rollback: revert the pack commit in the consuming repo.
- Disaster recovery (RPO/RTO if this repo has them): n/a

## Evolution

Not solved yet: live LLM eval harness, org marketplace, per-client adapter generation. Revisit after the pack is run on a real workstream in two clients. Static eval fixtures already live under `evals/`.

## Open questions

- Blocking: none for the pack itself.
- Non-blocking: first two clients for the install test.

## Next

The [portable pack design](../design/2026-08-18-portable-pack.md) is how the files are laid out. Next for a program: install into one product repo and prove two-client discovery.
