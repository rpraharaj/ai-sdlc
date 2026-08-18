# Design: Portable pack layout and adapters

Keep every heading. Write `n/a` when a section does not apply. Do not invent APIs, SLOs, or files that are not decided.

- **Status:** accepted
- **Date:** 2026-08-18
- **Author:** this session
- **Reviewers:** none
- **PRD:** [docs/prd/2026-08-18-ai-sdlc-pack.md](../prd/2026-08-18-ai-sdlc-pack.md)
- **Architecture:** [docs/architecture/operating-system.md](../architecture/operating-system.md)
- **ADRs:** none

## Summary

We keep **one canonical tree of Markdown** in this repository. Consuming product repos install skills into `.agents/skills/` and load program facts through a root `AGENTS.md`. Vendor-specific paths are adapters only. Program skills and core engineering skills are both in `skills/`.

## Problem

If we write skills for one tool’s directories, frontmatter extras, and orchestration language, half the program cannot use them. The pack has to be generic and still be discoverable.

## Goals and non-goals

- Goals: a repo layout that is the source of truth; an install story that does not fork procedure text; skill/agent/workflow file shapes that match open specs; a documented adapter policy.
- Non-goals: generating every vendor adapter now; a custom installer binary; a live LLM eval harness.

## Constraints

- Agent Skills spec: `name`, `description` required; `SKILL.md` in a folder named after `name`; keep body under ~500 lines; extra fields only in `metadata`.
- AGENTS.md: plain Markdown, no required schema; closest file wins in a monorepo.
- Cross-client skill directory convention: `<repo>/.agents/skills/` and `~/.agents/skills/`.
- Do not put secrets in the pack.
- Do not spend money or change cloud accounts from any skill (program rule).

## Current vs proposed

- Today: this repo holds design docs, Wave 0 `context/`, standalone `skills/` (Wave 1 + Wave 2 + core engineering), `agents/`, `playbooks/`, `workflows/`, pointer `adapters/`, and static `evals/`.
- A consuming repo has `AGENTS.md`, `.agents/skills/<name>/` (copy or link), filled-in `context/`, and optional adapter pointers.

## Approach

**This pack repo** (source):

```text
ai-sdlc/
  README.md                 # humans
  AGENTS.md                 # how to work on *this* pack repo
  INSTALL.md
  CONTRIBUTING.md
  LICENSE
  context/                  # templates for program memory (not a live program)
    README.md
    glossary.md
    systems-of-record.md
    definition-of-done.md
    decision-rights.md
    environments.md
  skills/
    <skill-name>/
      SKILL.md
      references/           # templates, long notes (loaded on demand)
      assets/               # only if a static file is required
      scripts/              # only if a portable script is required
  agents/
    README.md
    <profile>.md            # capability envelope, Markdown
    personas/               # optional writer/reviewer overlays
  workflows/
    <workflow-name>.md      # Markdown sequence + human gates
  playbooks/
    <role>.md               # human start-here
  adapters/
    README.md
    claude/                 # pointers only
    cursor/
    copilot/
    gemini/
    codex/
    generic/
  evals/                    # fixtures + static cases
  templates/consuming-AGENTS.md
  scripts/check-pack.py
  docs/                     # this design set
```

**A consuming product repo** (after install):

```text
product/
  AGENTS.md                 # pointers into context/ + engineering commands
  context/                  # filled-in program facts
  docs/prd|requirements|design|architecture|tasks|...
  .agents/skills/
    write-prd/SKILL.md      # installed from this pack
    ...
```

Discovery: clients that follow the Agent Skills implementation guide scan `.agents/skills/` at project and user scope. Clients that also scan `.<vendor>/skills/` can keep a **symlink** from that folder to `../../.agents/skills/<name>` or to this pack. Procedure text is never duplicated.

Engineering skills (`implement-change`, `ready-to-merge`, …) live in this pack under `skills/`. Do not maintain a second copy in another repo as the source of truth.

## Public surface

What a human or agent outside this repo sees:

- `AGENTS.md` — always-on rules and pointers.
- `.agents/skills/*/SKILL.md` — discovered by name + description; invoked by task match or `/<name>` where the client has slash commands.
- `playbooks/<role>.md` — human navigation.
- Artifact paths in the consuming repo (see [artifact chain](../reference/artifact-chain.md)).

No HTTP API. No CLI required. An optional later `scripts/install.sh` that only creates symlinks is allowed; it is not required to use the pack (copying folders is enough).

## Data and contracts

Contracts are file shapes, not schemas in a database.

| Contract | Spec |
| --- | --- |
| Skill | [skill-standard](../reference/skill-standard.md) + [agentskills.io specification](https://agentskills.io/specification) |
| Context | [layers](../reference/layers.md) — Markdown files named in `AGENTS.md` |
| Agent profile | [agent-standard](../reference/agent-standard.md) |
| Workflow | [workflow-standard](../reference/workflow-standard.md) |
| Artifact types | [artifact-chain](../reference/artifact-chain.md) |

Expand then contract: add the shared path first; delete vendor copies of the same instructions only after two clients load the shared path. Do not drop `SKILL.md` required fields in the same change that adds adapters.

## Sequence

1. Enablement merges a skill into this pack.
2. Consuming repo updates its install (copy, submodule pin, or subtree).
3. Human opens any compatible client in that repo.
4. Client catalogs `name` + `description`.
5. Human asks for the work or types `/write-requirements`.
6. Client loads `SKILL.md`, which tells the agent to read `AGENTS.md` and the required previous artifact.
7. Agent writes the next artifact into `docs/...` in the consuming repo.
8. Human signs anything on the human-stop list.
9. Status/RAID/release skills read git + tracker + CI; they do not invent progress.

## UI

n/a. Client UIs (slash menu, skills panel) are owned by those products. We only require that descriptions are specific enough to trigger. Verification of a consuming product’s UI is a later `verify-ui` skill, not this pack’s UI.

## Failure

- Previous artifact missing → stop; name the skill that produces it.
- Context file missing → stop; name the Wave 0 file.
- Human-stop reached → stop; do not invent the decision.
- Client cannot discover `.agents/skills/` → use the documented adapter; if none, human pastes `SKILL.md` (degraded but defined).
- Skill script fails → report stderr; do not skip the check.
- No retries as a pack concern. Idempotent writes: overwrite the named artifact path or create `YYYY-MM-DD-slug.md` as the skill specifies.

## Security

- Untrusted input: ticket text, interview notes, and user paste are untrusted. Skills must not interpolate them into shell commands unsanitized.
- Secrets: never in `context/`, examples, or artifacts. Fail if a change would add `.env`, keys, or tokens.
- Authz: agent profiles restrict write/execute; production and billing stay human.
- Project skills load only in a trusted workspace (host feature). This pack must not ask to disable that.

## Performance

n/a as a service. Progressive disclosure: short `SKILL.md`, long material in `references/` loaded only when the body says when to read it. Do not ship a skill that requires loading the whole catalog’s bodies.

## Observability

n/a as a service. Static fixture graders live under `evals/` (`scripts/check-evals.py`). Live LLM runs against those fixtures are still human.

## Rollout and rollback

See [rollout](../reference/rollout.md). Rollback: revert the install commit in the consuming repo. No feature flag.

## Compatibility and migration

- Old clients that only read `CLAUDE.md` or `.github/copilot-instructions.md`: adapter is a short file that says “read `/AGENTS.md` and use `.agents/skills/`.”
- Skills authored with vendor-only frontmatter (`disable-model-invocation`, Grok `when-to-use`, Cursor `.mdc` globs): **not** in canonical `SKILL.md`. If a client needs them, they live in `adapters/<client>/` as extra files that *point* at the skill, not as a second procedure.
- Renames: expand (add new skill name) then contract (remove old) in a later change.

## Config

No required environment variables. Optional later:

- `AISDLC_TRACKER` — kind only (`jira` / `azure-devops` / `github-issues` / `none`), never credentials.
- Install pin (git tag) in the consuming repo.

Never values or secrets.

## Testing

These must fail before a skill change is called done:

- A validator (e.g. `skills-ref validate` from the Agent Skills project) accepts every `skills/*/SKILL.md`.
- No canonical file contains a vendor tool name from the denylist in [portability](../reference/portability.md).
- Opening the handoff table: given only a PRD, `write-design` (or our `write-requirements`) instructions say to stop if the required input is missing — checked by a fixture, not by vibe.
- Two-client discovery: after install, both chosen clients list `name` + `description` for a sample skill (manual until automated).

## Alternatives

### A. Canonical `.agents/skills/` + adapters (chosen)

- Why: matches the Agent Skills implementation guide’s interoperability path; one procedure text.

### B. Author natively in every vendor folder

- Why not: n copies; guaranteed drift.

### C. Only AGENTS.md, no skills

- Why not: AGENTS.md is always-on and must stay short; procedures need progressive disclosure.

### D. Workflows as a required orchestrator (Rhai, hooks, custom DSL)

- Why not: not portable. Markdown workflows first; orchestrators optional later as adapters.

## Key decisions

- Canonical skills live under `skills/` in this repo and install to `.agents/skills/` — why: documented cross-client convention. ADR: none yet.
- Adapters may not contain procedure steps — why: one home per fact.
- Agent profiles are Markdown capability envelopes, not vendor agent YAML — why: portability. A client that needs YAML generates it from the Markdown in an adapter, later.
- Engineering skills are in this pack — why: the repo must stand alone.

## Risks

- Blast radius: a bad skill in `.agents/skills/` is loaded by every client in that repo.
- Data / compatibility: adapter drift if someone “just copies” a SKILL.md into `.claude/skills/` and edits it there.
- Security / privacy: project-level skills in an untrusted clone; rely on host trust + no secrets in the pack.

## Assumptions

- At least one widely used client on the program already scans `.agents/skills/` or can follow a symlink.
- Consuming repos will commit the installed skills or a pin, so CI and cloud agents see them.
- People will use role cards; we will not also build a portal.

## Open questions

- Blocking: none for writing more design docs.
- Non-blocking:
  - First two clients for the install test.
  - Whether a later `scripts/install.sh` is worth more than `INSTALL.md` copy steps.

## Delivery

Ordered slices. Each must be independently reviewable. Detailed tickets live in a later task list.

1. Documentation set — done.
2. Wave 0 context templates — done.
3. Wave 1 + Wave 2 + core engineering skills — done.
4. Nine agent profiles + nine role cards — done.
5. Markdown workflows — done.
6. Pointer adapters — done (live two-client proof is still human).
7. Static eval fixtures — done.

## Next

Install into one product repo (`INSTALL.md`). Prove discovery in two clients.
