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
| `explore` | read-only (+ search commands if the host allows) | docs, git (read) | everyone | edit files |
| `planner` | write-docs + read/search; managed AGENTS map allowed | docs, git (read) | architect, tech lead (plans and specs) | implement product code |
| `shaper` | write-docs + read/search | docs, git (read), tracker (read) | PM, BA | change product code |
| `implementer` | write-code + execute | docs, git, CI (read), browser (verify) | UI + backend | merge; prod deploy |
| `reviewer` | read-only product; separate review reports | docs, git (read), browser (inspect) | anyone reviewing | edit the diff it reviews |
| `verifier` | run existing checks; QA reports only | docs, git (read), CI, browser | QA, authors | delete or skip a failing test |
| `releaser` | approved release path; metadata/docs only | docs, git, CI, observability | DevOps | unattended prod; money; account changes |
| `coordinator` | write-docs + read status; no test execution | tracker (read), git (read), CI (read), chat-draft | program/project manager | change code or architecture |
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
| `reviewer` | deny product/artifact edits; allow separate review reports and prepared UI inspection |
| `verifier` | shell allowed; write denied except test reports |
| `releaser` | shell; prod credentials absent unless a human enables them |
| `coordinator` | docs write + read tracker/git/CI; fresh checks handed to verifier |
| `incident-lead` | observability MCP + incident doc write |

`write-tests` authorship requires implementer. Explore reports a map; planner can persist it, verifier runs checks, and implementer installs dependencies. Reviewer reports must not modify reviewed inputs. Releaser may change approved release metadata, but fix-ci and functional/pipeline edits require implementer. All skills must respect the profile envelope; a skill invocation cannot grant itself more rights.

Before a pilot, record the mapping in each host using [pilot.md](pilot.md). If the host cannot express a necessary restriction, keep that action human-controlled and record the limitation.
