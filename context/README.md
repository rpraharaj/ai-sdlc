# Program context templates

Copy this folder into a **consuming** product repository as `context/`. Fill every file with facts about **that** program. Leave a heading as `n/a` only when it truly does not apply. Do not invent users, SLOs, vendors, or systems.

These files are the always-on memory. Point at them from the consuming repo’s `AGENTS.md` (see `templates/consuming-AGENTS.md`).

| File | Owner | Fill with |
| --- | --- | --- |
| [glossary.md](glossary.md) | BA + architect | Domain terms as this program uses them |
| [systems-of-record.md](systems-of-record.md) | PMO + architect | Where truth lives (tracker, git, CI, design, …) |
| [definition-of-done.md](definition-of-done.md) | Eng + QA + DevOps | Story / release / hotfix done — commands, not slogans |
| [decision-rights.md](decision-rights.md) | Program manager | Who decides what; what AI may draft vs a human must sign |
| [environments.md](environments.md) | DevOps | Dev / test / stage / prod and who may promote |

Skills stop if a required file here is missing. They do not invent the contents.
