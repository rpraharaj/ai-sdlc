# Layers

Four executable layers, plus one human index. Detail for each file type lives in the matching standard.

```text
Context (always on)     what is true about this program
        ↓
Skills (on demand)      how to produce or check one artifact
        ↓
Agents (session)        who may read / write / run / talk to tools
        ↓
Workflows (gates)       several skills in a fixed order, with human stops

Role cards              which of the above a human should open
```

## When to create which

| Layer | Create when | Do not create when |
| --- | --- | --- |
| **Context** | A fact every session must know | The fact is only needed by one procedure |
| **Skill** | A repeatable procedure with a named output | It is a one-off, or it is only a persona |
| **Agent profile** | Different **tools, MCP, or write rights** | You only want a different tone or checklist |
| **Workflow** | A fixed multi-step path with a quality gate | A single skill already covers it |
| **Role card** | Humans need a start-here page | You are tempted to encode the org chart as agents |

## Context (always on)

Loaded through the consuming repo’s `AGENTS.md`. Keep `AGENTS.md` itself short: commands, do-not-edit paths, and **pointers** to:

| File | Owner | Contents |
| --- | --- | --- |
| `context/glossary.md` | BA + architect | Domain terms as **this program** uses them (20–40, not a thesaurus) |
| `context/systems-of-record.md` | PMO + architect | Tracker, wiki, git, design, CI, observability, identity — where truth lives |
| `context/definition-of-done.md` | Eng + QA + DevOps | Story / release / hotfix done. Commands, not slogans |
| `context/decision-rights.md` | Program manager | Who decides scope, date, architecture, go-live, prod access. What AI may draft vs what a human signs |
| `context/environments.md` | DevOps | Dev / test / stage / prod, promotion path, who may deploy |

`AGENTS.md` also records install / run / test / lint / typecheck / build for **that** repo. Never invent those commands in a skill.

## Skills (on demand)

See [skill-standard](skill-standard.md) and [catalog](catalog.md).

## Agent profiles (session)

See [agent-standard](agent-standard.md). Nine profiles. Not nine departments.

## Workflows (gates)

See [workflow-standard](workflow-standard.md). Optional. People can run skills one at a time.

## Role cards (index)

See [role-cards](role-cards.md). One page per role. Never executed as an agent.
