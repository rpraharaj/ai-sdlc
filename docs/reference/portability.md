# Portability

This pack must work in **any** AI coding tool that can read files in a repo. It is not a Grok pack, not a Claude pack, not a Cursor pack.

## What “portable” means

A person on team A using client X and a person on team B using client Y can:

1. Open the same consuming repository.
2. Load the same `AGENTS.md` facts.
3. Discover the same skills by `name` + `description`.
4. Produce the same artifact shape.

No procedure text is rewritten per client.

A tool that cannot read the repo can still be used in a degraded way: the human pastes the `SKILL.md` body. That is defined. It is not the target.

## Open standards we author against

| Concern | Format | Authority |
| --- | --- | --- |
| Always-on project rules | `AGENTS.md` (plain Markdown, no required schema) | [agents.md](https://agents.md/), Agentic AI Foundation / Linux Foundation |
| On-demand procedures | Folder + `SKILL.md` with YAML `name` + `description` | [Agent Skills specification](https://agentskills.io/specification) |
| Optional tool access | MCP servers configured **by the host**, not by this pack | [Model Context Protocol](https://modelcontextprotocol.io) |

We do not introduce a third format.

## Canonical install locations

The Agent Skills spec defines what is *inside* a skill directory. It does not mandate the parent path. The implementation guide’s interoperability convention is:

| Scope | Path | Use |
| --- | --- | --- |
| Project | `<repo>/.agents/skills/<name>/SKILL.md` | Shared with everyone who clones the repo |
| User | `~/.agents/skills/<name>/SKILL.md` | Personal, all projects |

This pack’s **source** tree keeps skills at `skills/<name>/` and documents install into `.agents/skills/`.

`AGENTS.md` lives at the consuming repo root. Nested `AGENTS.md` files may exist in packages; the closest file to the work wins.

## What may appear in canonical files

Allowed in `skills/*/SKILL.md` frontmatter (spec fields only):

- `name` (required) — lowercase, digits, hyphens; matches folder name
- `description` (required) — what it does **and** when to use it
- `license`
- `compatibility` — environment facts (`Requires git`), **not** “Designed for Vendor X” unless the skill truly cannot run elsewhere
- `metadata` — `pack`, `version`, `stage` as strings
- `allowed-tools` — experimental; excluded from this pack's accepted subset.

Allowed in the body:

- Steps, handoff tables, quality bars, relative links to `references/` and `assets/`
- “Read `AGENTS.md`.” “Run the test command `AGENTS.md` records.” “Use the tracker CLI or MCP this repo already has.”
- Portable scripts in `scripts/` (POSIX shell or Python) with documented dependencies

## Denylist (canonical files)

Do not put any of the following in `skills/`, `context/`, `agents/`, `workflows/`, or `playbooks/`:

| Banned | Why | Where it may live instead |
| --- | --- | --- |
| Vendor tool names (`run_terminal_command`, `spawn_subagent`, `Write`, `mcp_…` as required tools) | Other clients have different tool names | Nowhere. Say “read the file”, “run the command”, “start a read-only sub-session if the host supports it.” |
| Vendor-only frontmatter (`when-to-use`, `disable-model-invocation`, `user-invocable`, `model`, `effort`, Cursor `.mdc` globs) | Not in the Agent Skills spec | `adapters/<client>/` extra files that *point* at the skill |
| Orchestration DSLs as the workflow source (Rhai, vendor hook graphs) | Not readable as a procedure | Optional adapter that implements a Markdown workflow |
| “You are Grok / Claude / Copilot / …” | Locks tone to a vendor | Nowhere |
| Absolute paths to one person’s machine | Not shareable | Nowhere |
| Secrets, tokens, account ids | Safety | Nowhere |

## Adapter policy

An adapter is valid only if:

1. It contains **no procedure steps** that are not in the canonical skill.
2. It only maps discovery (symlink, “read AGENTS.md”, extra frontmatter that points at `.agents/skills/<name>`).
3. Deleting the adapter directory cannot lose information.

Examples of valid adapters:

```text
# consuming repo
CLAUDE.md          → one line: follow ./AGENTS.md
.github/copilot-instructions.md → one line: follow ./AGENTS.md
.claude/skills/write-prd → symlink to ../../.agents/skills/write-prd
```

If a client cannot discover `.agents/skills/` and cannot follow a symlink, document a copy step in `adapters/<client>/README.md`. The copy is generated from source; humans do not edit the copy.

## How common clients consume this pack

This table is **guidance**, not a dependency list. Clients change. Prefer the client’s current docs at install time.

| Client | Reads `AGENTS.md` | Typical extra instruction file | Skills discovery to aim at |
| --- | --- | --- | --- |
| Codex | Yes (native) | — | `.agents/skills/` (and client-native dirs if documented) |
| Cursor | Yes (commonly) | `.cursor/rules/*.mdc` | `.agents/skills/`, often also `.cursor/skills/` |
| GitHub Copilot / VS Code | Yes (when enabled) | `.github/copilot-instructions.md` | `.agents/skills/` (VS Code quickstart uses this path) |
| Claude Code | Often via `CLAUDE.md`; symlink `CLAUDE.md` → `AGENTS.md` | `CLAUDE.md` | `.claude/skills/` and, in many setups, `.agents/skills/` |
| Gemini CLI | Configurable (`context.fileName`) | `.gemini/settings.json` | Client skills dir + `.agents/skills/` where supported |
| Windsurf, Goose, Amp, Factory, OpenCode, Roo, Grok, others | Varies | Varies | Prefer `.agents/skills/`; add a pointer adapter if needed |

Do not special-case the pack for a client in this table. If a client is missing, add an adapter README, not a fork of the skill.

## Agent profiles are not vendor agents

Hosts differ: some have `agents/*.md`, some have `config.toml` roles, some have only permissions prompts.

Canonical profile: Markdown in this pack’s `agents/<profile>.md` describing capability (see [agent-standard](agent-standard.md)).

A host that needs YAML/TOML gets an **generated** adapter later. Until then, humans pick the host’s nearest equivalent (read-only vs full) using the profile as a checklist.

## Workflows are not vendor orchestrators

Canonical workflow: Markdown. A human or any agent can follow it step by step.

If a host can fan-out sub-sessions, an adapter may automate the same steps. The adapter must not add gates or skip human stops that the Markdown workflow names.

## Progressive disclosure is part of portability

Clients load `name` + `description` for every skill at startup, then the body on activation, then `references/` on demand. That behavior is in the spec. Skills that dump everything into `SKILL.md` hurt every client equally. Keep bodies short.

## Validation

Before a skill is called portable:

1. `python3 scripts/check-pack.py` validates this pack's documented subset of Agent Skills frontmatter and its references. This is not a general YAML parser or an external spec certification.
2. A grep over `skills/`, `context/`, `agents/`, `workflows/`, `playbooks/` finds no denylist strings.
3. Both selected clients pass the observed [pilot smoke cases](pilot.md), including the loaded source path/version, context, artifact shape, and gate behavior. Listing a name alone is discovery evidence.
