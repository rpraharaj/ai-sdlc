# Adapters

Pointer files only. Procedure text lives in `skills/` and `AGENTS.md`. Deleting this directory must not lose a step.

Copy the file named in each client README into the **consuming** product repo. Do not edit a copy of `SKILL.md` into a vendor skills folder.

| Client | What to copy | Destination in the product repo |
| --- | --- | --- |
| [claude](claude/README.md) | `CLAUDE.md` | `CLAUDE.md` |
| [cursor](cursor/README.md) | `aisdlc.mdc` | `.cursor/rules/aisdlc.mdc` |
| [copilot](copilot/README.md) | `copilot-instructions.md` | `.github/copilot-instructions.md` |
| [gemini](gemini/README.md) | snippet in that README | `.gemini/settings.json` |
| [codex](codex/README.md) | nothing | native `AGENTS.md` + `.agents/skills/` |
| [generic](generic/README.md) | nothing extra | any client that already reads those two |

If a client still cannot see `.agents/skills/`, symlink *the skill directory* (not a rewritten body):

```sh
mkdir -p <product>/.claude/skills
ln -s ../../.agents/skills/write-requirements <product>/.claude/skills/write-requirements
```

Humans do not maintain the symlink target as a second source.
