# Environments

Promotion path for this program. Name real environments. Write `n/a` if a row does not exist. Do not invent a production URL or credentials.

| Name | Purpose | Who may deploy | How (command or pipeline, from `AGENTS.md`) | Data |
| --- | --- | --- | --- | --- |
| dev | | | | |
| test | | | | |
| stage | | | | |
| prod | | | | |

## Promotion

1. …
2. …

## Rules

- Production deploy is a human decision (`context/decision-rights.md`).
- Secrets live in the secret store this program already uses — never in git, skills, or prompts.
- If an environment is missing, say so. Do not pretend prod is stage.
