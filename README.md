# AI SDLC

**One way of working for a whole delivery program — in any AI coding tool.**

Program managers, product, BAs, architects, UI and backend, QA, and DevOps share the same procedures, the same artifact names, and the same human stops. Not a chatbot per job title. Not a pack that only runs in one vendor’s agent.

This repo is **not an application**. You install it into a product repository, fill in that program’s facts, then ask your usual coding agent for the *next artifact*.

[How to use](docs/how-to-use.md) · [Install](INSTALL.md) · [Your role](playbooks/) · [Catalog](docs/reference/catalog.md) · [Contribute](CONTRIBUTING.md)

---

## Why this exists

Teams tell everyone to “use AI” and get nine overlapping assistants. Each role invents users, status, and architecture. Specs do not chain. A prompt library written for one IDE is useless to the rest of the program.

This pack is a **file-based operating system** for that problem:

| Layer | What it is |
| --- | --- |
| **Context** | Facts about *this* program (glossary, systems of record, definition of done, who decides) |
| **Skills** | How to produce or check **one** named artifact |
| **Agents** | Permission envelopes (read / write docs / write code / prod-gated) — not personas |
| **Playbooks** | One page per role: what you run, what you own, what you still decide |
| **Workflows** | Optional gated paths (shape → design → deliver → release) |

Skills are [Agent Skills](https://agentskills.io/specification) (`SKILL.md`). Always-on rules are [AGENTS.md](https://agents.md/). Vendor folders are **pointers only**.

## What’s in the box

| | Count |
| --- | ---: |
| Portable skills | **66** |
| Agent profiles | **9** |
| Role playbooks | **9** |
| Markdown workflows | **6** |
| Client adapters (pointers) | **6** |

Skills cover the full chain: opportunity and PRD, requirements and process, architecture and contracts, implement and test, review and ready-to-merge, release and incident, RAID and status.

Every skill has a handoff table (“do this instead”), required inputs, a human-stop list, a template, and a yes/no quality bar. If the previous artifact is missing, the skill is supposed to **stop** — not invent a second program.

```text
Opportunity → PRD → Requirements + process
                    ↓
         Architecture / ADRs / design / contracts
                    ↓
              Tasks → shaped slice
                    ↓
         Implementation + tests + UI verify
                    ↓
      Review → ready-to-merge → notes → release
                    ↓
           Runbook / RAID / status
```

## Quick start

```sh
# from this pack, into a product repo
cp -R context <product>/context
cp templates/consuming-AGENTS.md <product>/AGENTS.md   # only if that repo has none
mkdir -p <product>/.agents/skills
cp -R skills/. <product>/.agents/skills/
```

1. Fill `<product>/context/` for **that** program. Do not leave the templates blank and expect good output.
2. Open the product repo in Cursor, Claude Code, Codex, Copilot, Gemini CLI, or any client that reads `.agents/skills/`.
3. Ask for the next artifact — `/write-prd`, `/write-requirements`, `/ready-to-merge` — or open your [playbook](playbooks/).
4. If the client does not list skills, use an [adapter](adapters/README.md). Never fork a `SKILL.md` into a vendor folder.

Full copy steps: [INSTALL.md](INSTALL.md). Day-one path: [docs/how-to-use.md](docs/how-to-use.md).

## How a session should feel

A BA types “write requirements for the export.” The agent loads `write-requirements`, looks for a PRD, and **stops** if there isn’t one. A developer runs `implement-change` on a shaped slice, then `ready-to-merge`, which prints command output or it is not ready. A program manager runs `write-status`; every progress line has to cite RAID, git, or CI — RAG stays a human decision.

Production, money, and cloud-account changes stay human. That is in `context/decision-rights.md`, not a slogan.

## Who opens what

| Role | Start here |
| --- | --- |
| Product | [playbooks/product-manager.md](playbooks/product-manager.md) |
| Business analysis | [playbooks/business-analyst.md](playbooks/business-analyst.md) |
| Architecture | [playbooks/solution-architect.md](playbooks/solution-architect.md) |
| UI / backend | [playbooks/ui-developer.md](playbooks/ui-developer.md) · [backend-developer.md](playbooks/backend-developer.md) |
| QA | [playbooks/qa.md](playbooks/qa.md) |
| DevOps | [playbooks/devops.md](playbooks/devops.md) |
| Program / project | [playbooks/program-manager.md](playbooks/program-manager.md) · [project-manager.md](playbooks/project-manager.md) |

## What this is not

- A hosted agent platform or a marketplace
- One agent named after each job title
- A requirement to use a particular AI product
- Proof that every client already discovers `.agents/skills/` — check that on your tools after install

## Check the pack

From this repository:

```sh
python3 scripts/check-pack.py
```

Validates skill frontmatter, required headings, templates, adapters (pointers only), and static eval fixtures.

## Docs

| Doc | For |
| --- | --- |
| [How to use](docs/how-to-use.md) | First day |
| [Catalog](docs/reference/catalog.md) | Every skill |
| [Artifact chain](docs/reference/artifact-chain.md) | What hands off to what |
| [Portability](docs/reference/portability.md) | Any-tool rules |
| [PRD / architecture / design](docs/README.md) | Why the pack is shaped this way |

## Contributing

Issues and pull requests are welcome. Change a procedure only with a real failed trace; keep skills portable; run `python3 scripts/check-pack.py`. Details: [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
