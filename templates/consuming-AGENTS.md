# AGENTS.md

Instructions for coding agents working in **this** product repository. Humans read `README.md`.

## This repo

- **Install:** `(unknown)` — replace with the command this repo actually uses
- **Run:** `(unknown)`
- **Test:** `(unknown)`
- **Lint:** `(unknown)`
- **Typecheck:** `(unknown)`
- **Build:** `(unknown)`

Do not invent these commands. If a command is unknown, write `(unknown)` and stop claiming that check passed.

## Program context

Read these before inventing facts. If a file is still a template (contains `(none yet)` or empty tables), treat those fields as unknown.

- `context/glossary.md`
- `context/systems-of-record.md`
- `context/definition-of-done.md`
- `context/decision-rights.md`
- `context/environments.md`

## Skills

Project skills live in `.agents/skills/`. Follow the matching skill when the task matches its `description`. Do not invent users, SLOs, vendors, or RAG status. If the previous artifact in the chain is missing, stop and name the skill that produces it.

## Do not

- Commit secrets, `.env` files, private keys, or credentials
- Unattended production deploys, purchases, or cloud-account changes
- Delete or skip a failing test to get a green run
- Expand and contract a stored contract in the same change

## Do not edit

`(none found)` — list generated or vendored paths
