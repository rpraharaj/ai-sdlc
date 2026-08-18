# Documentation index

Wave 0–3 (pack files) are in the tree: context, skills, agents, playbooks, workflows, pointer adapters, static evals. Live two-client discovery is still on the consuming program.

## Start here

1. [How to use this pack](how-to-use.md) — install, fill context, run a skill, open your playbook. External changes: [CONTRIBUTING.md](../CONTRIBUTING.md).
2. [PRD](prd/2026-08-18-ai-sdlc-pack.md) — why this pack exists and what success is.
3. [Architecture](architecture/operating-system.md) — four layers, no hosted runtime.
4. [Design](design/2026-08-18-portable-pack.md) — source tree, `.agents/skills/` install, adapter policy.

## Reference (one home per topic)

| Topic | File |
| --- | --- |
| Rules that apply everywhere | [principles](reference/principles.md) |
| Any-tool constraint | [portability](reference/portability.md) |
| Context / skills / agents / workflows | [layers](reference/layers.md) |
| How to write a skill | [skill-standard](reference/skill-standard.md) |
| Nine permission profiles | [agent-standard](reference/agent-standard.md) |
| Markdown workflows | [workflow-standard](reference/workflow-standard.md) |
| What files hand off to what | [artifact-chain](reference/artifact-chain.md) |
| What to build, in what wave | [catalog](reference/catalog.md) |
| Who runs what | [role-cards](reference/role-cards.md) |
| How to introduce this to a program | [rollout](reference/rollout.md) |
| Who owns and versions the pack | [governance](reference/governance.md) |

## Implemented in this repo

- `context/` — Wave 0 templates
- `skills/` — standalone catalog (Wave 1 + Wave 2 + core engineering)
- `agents/` — nine profiles + personas
- `playbooks/` — nine role cards
- `workflows/` — six Markdown workflows
- `adapters/` — pointer files (Claude, Cursor, Copilot, Gemini, Codex, generic)
- `evals/` — fixtures + `cases.json`
- `templates/consuming-AGENTS.md`, `INSTALL.md`

## Not in this tree yet

Generated per-client skill copies (forbidden). A marketplace. Live LLM eval harness.
