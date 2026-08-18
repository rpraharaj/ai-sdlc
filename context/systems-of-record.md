# Systems of record

Where truth lives for this program. Name the real tool and the URL or workspace the team already uses. Do not invent a vendor. Write `none` if the program does not have that kind of system.

| Kind | System (name only) | What it is canonical for | Notes |
| --- | --- | --- | --- |
| Work tracker | | Ids, owners, dates, state; link to the git spec | |
| Specs / design docs | git (`docs/`) unless this row says otherwise | Problem, requirements, design, contracts, runbooks | Prefer git markdown |
| Source | | Code and history | |
| CI | | Pass/fail of checks named in `AGENTS.md` | |
| Design files | | Visuals, not the requirements | |
| Identity | | Who a user is | |
| Observability | | Runtime evidence | |
| Chat | | Drafts and links only — not specs | |
| Other | | | |

Credentials never go in this file.
