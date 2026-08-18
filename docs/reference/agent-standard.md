# Agent standard

An agent profile is a **permission and tool envelope**. It is not a colleague and not a personality.

Hosts differ. The canonical file is Markdown in this pack. Humans (or a later adapter) map it onto whatever the host calls roles, permission modes, or sub-sessions.

## When a new profile is allowed

Only if it needs a different mix of:

- read vs write vs execute
- whether product code may be edited
- whether production systems may be touched
- which **kinds** of MCP/CLI (tracker, CI, observability) it may use

A different checklist or tone is a skill or a short persona paragraph, not a new agent.

## Canonical file

`agents/<profile>.md`:

```markdown
# <profile>

- **Mode:** read-only | write-docs | write-code | execute | prod-gated
- **May edit product code:** yes | no
- **May run commands:** yes | no
- **May use tool kinds:** none | tracker | git | ci | observability | chat-draft
- **Typical skills:** comma-separated names
- **Must not:** …

## Session rules

Short bullets. No procedure that belongs in a skill.
```

No “you are a senior architect with 20 years…”.

## The nine profiles

| Profile | Mode | MCP / CLI kinds | Used by | Must not |
| --- | --- | --- | --- | --- |
| `explore` | read-only (+ search commands if the host allows) | none or docs | everyone | edit files |
| `planner` | write-docs | none | architect, tech lead (plans and specs) | implement product code |
| `shaper` | write-docs | tracker (read) | PM, BA | change product code |
| `implementer` | write-code + execute | git | UI + backend | merge; prod deploy |
| `reviewer` | read-only | git | anyone reviewing | edit the diff it reviews |
| `verifier` | execute tests; no product edits | CI | QA, authors | delete or skip a failing test |
| `releaser` | execute in non-prod; prod is gated | CI, observability | DevOps | unattended prod; money; account changes |
| `coordinator` | write-docs (status) | tracker, chat-draft | program/project manager | change code or architecture |
| `incident-lead` | read runtime + write incident doc | observability | DevOps, on-call | silent prod changes |

That is the full set. UI developer and backend developer share `implementer`. Package-level `AGENTS.md` in the consuming repo teaches the stack.

## Personas (optional, not agents)

Use a short persona only when the **same** profile runs two opposed jobs (writer vs reviewer). Canonical home: `agents/personas/<name>.md` with an input/output contract (which file in, which file out).

Personas (in `agents/personas/`):

- requirements-writer / requirements-reviewer
- design-writer / design-reviewer
- status-skeptic
- security-reviewer

## Mapping to a host (later adapters)

| This profile | Typical host mapping |
| --- | --- |
| `explore` | read-only / “ask” / explore sub-session |
| `planner` | docs write in `docs/architecture`, `docs/design`, `docs/tasks` — no product code |
| `shaper` | normal session in `docs/` + `context/` |
| `implementer` | agent mode, workspace write + shell |
| `reviewer` | read-only review sub-session |
| `verifier` | shell allowed; write denied except test reports |
| `releaser` | shell; prod credentials absent unless a human enables them |
| `coordinator` | docs write + tracker MCP |
| `incident-lead` | observability MCP + incident doc write |

If the host cannot express a restriction, the **skill** still states the restriction, and the human is responsible for not granting extra tools.
