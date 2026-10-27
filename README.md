# AI SDLC: Agent Skills for AI-Assisted Software Development

AI SDLC is an open-source, vendor-neutral pack of **66 AI agent skills** for the **software development lifecycle (SDLC)**. It gives product, engineering, QA, DevOps, and program teams shared procedures for requirements, architecture, implementation, testing, code review, release, and status reporting.

Install the pack into an existing product repository, fill in the program's context, and use your AI coding assistant to produce the next artifact. Requirements, design decisions, tasks, tests, and release evidence stay connected through named files and source references.

**Markdown procedures · AGENTS.md context · SKILL.md skills · Human approval gates · MIT licensed**

[Quick start](#quick-start-install-into-a-product-repository) · [Skill catalog](docs/reference/catalog.md) · [Role playbooks](playbooks/README.md) · [Workflows](workflows/README.md) · [Pilot checklist](docs/reference/pilot.md) · [Contributing](CONTRIBUTING.md)

## What does this AI SDLC pack do?

AI coding tools can help write code, but a delivery team also needs agreement on the problem, requirements, interfaces, acceptance checks, and who approves a change. This pack puts those procedures and handoffs in the repository where the team works.

Each skill explains when to use it, required inputs, decisions that need a human, an output template, and a checkable quality bar. Missing prerequisites are supposed to stop dependent work; unknown facts stay unknown.

| Work you need to do | Example skills | Output or evidence |
| --- | --- | --- |
| Define a product problem | [write-opportunity](skills/write-opportunity/SKILL.md), [write-prd](skills/write-prd/SKILL.md) | Opportunity brief and product requirements document |
| Specify behavior and interfaces | [write-requirements](skills/write-requirements/SKILL.md), [write-integration-contract](skills/write-integration-contract/SKILL.md) | Testable requirements and API, event, or file contracts |
| Design the solution | [write-architecture](skills/write-architecture/SKILL.md), [write-design](skills/write-design/SKILL.md), [record-decision](skills/record-decision/SKILL.md) | Architecture, technical design, and architecture decision records |
| Implement a scoped change | [shape-work](skills/shape-work/SKILL.md), [implement-change](skills/implement-change/SKILL.md), [debug](skills/debug/SKILL.md) | A defined slice, code changes, and verification results |
| Test and review the change | [write-tests](skills/write-tests/SKILL.md), [review-change](skills/review-change/SKILL.md), [ready-to-merge](skills/ready-to-merge/SKILL.md) | Tests, findings, and a readiness record with command output |
| Prepare release and operations | [build-regression-pack](skills/build-regression-pack/SKILL.md), [plan-rollback](skills/plan-rollback/SKILL.md), [write-runbook](skills/write-runbook/SKILL.md) | Regression evidence, rollback plan, and operational instructions |
| Coordinate delivery | [update-raid](skills/update-raid/SKILL.md), [write-status](skills/write-status/SKILL.md), [map-dependencies](skills/map-dependencies/SKILL.md) | Risks, assumptions, issues, dependencies, and sourced status |

Browse all 66 procedures in the [AI SDLC skill catalog](docs/reference/catalog.md).

## How the development workflow fits together

Artifacts are the handoff between roles. A requirement points to a product goal; design and tasks preserve its reference; tests record the requirement, defect, or shaped acceptance check they verify.

```text
Opportunity → PRD → Requirements + process
                         ↓
             Architecture / design / contracts / ADRs
                         ↓
                 Tasks → shaped slice
                         ↓
              Implementation + tests + UI verification
                         ↓
               Review → ready-to-merge
                         ↓
             Release evidence → human go/no-go
                         ↓
                Runbooks / RAID / status
```

Use the [artifact chain](docs/reference/artifact-chain.md) for input/output paths and the [six workflows](workflows/README.md) for shaping, design, delivery, release, weekly program coordination, and incidents. A small, clear defect can use the shorter shaped-change path; it does not need a full initiative document set.

## Quick start: install into a product repository

You need Git, Python 3 for the pack's scripts, an existing product directory, and an AI coding client that can read repository files. The consuming project keeps its own language, framework, package manager, and test runner.

From a reviewed, clean checkout of this pack:

```sh
# Validate the pack before installation.
python3 scripts/check-pack.py

# Preview the initial install into your product repository.
python3 scripts/install-pack.py <product-repo> --navigation

# Apply after inspecting the plan. Existing files are not overwritten.
python3 scripts/install-pack.py <product-repo> --navigation --apply
```

The installer copies committed skill files into `.agents/skills/`, adds missing context templates, and optionally copies profiles, playbooks, and workflows. It preserves existing `AGENTS.md` and context files, reports required manual merges, and refuses conflicting skill directories. Ignored local files are excluded; prohibited secret filenames are rejected.

Before the first run:

1. Fill the program's glossary, systems of record, definition of done, decision rights, and environments in `context/`.
2. Add the context and skill pointers to an existing `AGENTS.md`, keeping the product's real commands and rules.
3. Map the agent profiles to the client's actual read, write, and execution permissions.
4. Ask for the next artifact using an existing input path, then review the result and any required human decisions.
5. Record the [supervised pilot cases](docs/reference/pilot.md) in two selected clients before widening adoption.

Follow [installation, updates, and removal](INSTALL.md) for the complete procedure, source pinning, and ownership-aware rollback. Start with [how to use AI SDLC](docs/how-to-use.md) for the day-one workflow.

## Example requests for your AI coding assistant

After installation and context setup, name the work and its source. These requests illustrate skill selection; they are not claims that a feature or approval already exists.

```text
Use write-requirements with the approved PRD at <prd-path>.
Preserve goal references and flag missing approval evidence or priorities.

Use implement-change for the accepted task at <task-path>.
Follow this repository's patterns and run its recorded checks.

Use ready-to-merge on this change.
Show acceptance evidence and required check results; identify anything unverified.

Use write-status for <reporting-window> from <raid-path>, git, and CI evidence.
Leave the overall RAG rating unassigned unless a human has set it.
```

Use natural-language requests or the skill's name. Slash commands are optional and depend on the client. If a required input is missing, the agent should identify the missing artifact or decision rather than invent it.

## What's included

| Component | Included | Purpose |
| --- | ---: | --- |
| [Agent skills](skills/README.md) | 66 | Procedures for one artifact or check, with supporting templates |
| [Program context](context/README.md) | 5 core templates | Shared facts, commands, environments, and decision ownership |
| [Agent profiles](agents/README.md) | 9 | Permission envelopes for exploration, shaping, planning, implementation, review, verification, release, coordination, and incidents |
| [Role playbooks](playbooks/README.md) | 9 | Starting points, artifact ownership, and decisions for each delivery role |
| [Markdown workflows](workflows/README.md) | 6 | Ordered skill sequences with human gates |
| [Client adapters](adapters/README.md) | 6 | Discovery pointers that keep procedure text in one place |

Skills use [the Agent Skills format](https://agentskills.io/specification), with `SKILL.md` and on-demand references. Program rules and context pointers use [AGENTS.md](https://agents.md/). There is no hosted runtime or database to operate.

### Client adapters and portability

This repository includes pointer adapters for [Claude Code](adapters/claude/README.md), [Codex](adapters/codex/README.md), [Cursor](adapters/cursor/README.md), [GitHub Copilot](adapters/copilot/README.md), [Gemini CLI](adapters/gemini/README.md), and a [generic client](adapters/generic/README.md).

The canonical skills remain vendor-neutral. Client discovery and permission behavior must be verified in your environment; included adapters do not prove universal compatibility. See [portability rules](docs/reference/portability.md) and record the loaded skill paths and versions during the pilot.

## Who should use it?

Use AI SDLC when multiple delivery roles need shared AI-assisted development procedures, traceable handoffs, and explicit decision ownership. It can also give a smaller team a consistent path from a scoped request to reviewed, tested code.

| Your role | Start here |
| --- | --- |
| Product manager | [Product discovery, prioritization, and PRDs](playbooks/product-manager.md) |
| Business analyst | [Requirements, process maps, and UAT](playbooks/business-analyst.md) |
| Solution architect | [Architecture, technical design, and decisions](playbooks/solution-architect.md) |
| UI developer | [UI implementation and verification](playbooks/ui-developer.md) |
| Backend developer | [Service implementation, APIs, and data changes](playbooks/backend-developer.md) |
| QA | [Test strategy, cases, regression, and acceptance](playbooks/qa.md) |
| DevOps | [Pipelines, release preparation, and operations](playbooks/devops.md) |
| Program or project manager | [Program governance](playbooks/program-manager.md) and [project delivery](playbooks/project-manager.md) |

## Human oversight and pilot status

The pack's procedures are intended to preserve human decisions about scope, priority, irreversible technology choices, go-live, production, money, and legal matters. Approval evidence and waivers belong in the home named by the consuming program's `context/decision-rights.md`.

Permission profiles and workflows are instructions. The host client and the team must enforce access boundaries and witness the required approvals. The pack does not supply an automatic authorization service or replace the program's tracker, CI, or operational controls.

**Adoption starts with a supervised pilot.** Pack files, validators, and regression tests are implemented. Observed two-client behavior, real program approvals, and adoption outcomes remain to be recorded in a consuming repository. Use the [pilot setup, smoke cases, and exit criteria](docs/reference/pilot.md); keep merge and production release under human control during the first pilot.

## Frequently asked questions

### Is AI SDLC an application or an agent orchestration platform?

It is a repository of skills, templates, profiles, and workflow documents. Your existing AI coding client reads the files and performs permitted actions. No additional agent server is required.

### How is this different from a prompt library?

Skills have required inputs, named outputs, templates, handoff guidance, human decision points, and quality checks. Shared program context gives facts a single home, and artifact references connect work across roles.

### Can I use it with an existing application?

Yes. Install it alongside the existing product code and preserve that repository's commands, conventions, rules, and documentation homes. Review collisions and merge missing context pointers before use; see [INSTALL.md](INSTALL.md).

### Do I need every skill for every change?

No. Start with the skill that matches the next artifact. A small, clear change can go through `shape-work` or `implement-change`; a new initiative can use the longer discovery and design workflows.

### Does a passing validator prove the AI will follow the process?

No. The validator checks file structure, references, portability rules, and regression cases. The pilot evaluates actual routing, handoffs, refusals, approval handling, and output quality in the selected clients.

## Validate the pack

From this source repository:

```sh
python3 scripts/check-pack.py
```

The command checks skill frontmatter, required headings and quality bars, template references, links, workflow skill/profile assignments, pointer adapters, static eval fixtures, and validator/installer regression tests. The source repository's CI runs the same command.

To also validate an installed pack, run from the source checkout:

```sh
python3 scripts/check-pack.py --installed <product-repo>
```

Installed checks inspect actual skills and pack-owned navigation independently of inventory digests. They do not certify program facts or live model behavior. Details: [evaluation coverage](evals/README.md).

## Documentation and contributing

- [Documentation index](docs/README.md): product rationale, architecture, design, and reference standards.
- [Artifact chain](docs/reference/artifact-chain.md): required handoffs, traceability, and default output paths.
- [Skill catalog](docs/reference/catalog.md): all procedures grouped by lifecycle stage.
- [Contributing guide](CONTRIBUTING.md): propose a change with a real failed trace, preserve portability, and run the checks.
- [Changelog](CHANGELOG.md): procedure, template, installation, and validation changes.

## License

AI SDLC is available under the [MIT License](LICENSE).
