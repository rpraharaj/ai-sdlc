# Agent defaults

These rules apply in every session in this repository, in any coding agent.

- Do not claim tests, types, lint, or builds passed unless this session ran the command and captured the output.
- Do not commit secrets, `.env` files, credentials, or private keys.
- Match this repository's tools and style. Do not introduce a new stack or formatter.
- Smallest change that satisfies the request. Prefer reuse, the standard library, and native platform features over new code or new dependencies. No drive-by refactors.
- Do not force-push shared branches. Do not amend other people's commits.
- Do not delete or skip a failing test to get a green run.

Run `ready-to-merge` before calling a change done. It applies `engineering-bar`.

## This repo

<!-- managed-by: explore-codebase -->

- **Root:** (unknown)
- **Languages:** (unknown)
- **Install:** (unknown)
- **Run:** (unknown)
- **Test:** (unknown)
- **Lint:** (unknown)
- **Typecheck:** (unknown)
- **Build:** (unknown)
- **Layout:** (unknown)
- **Do not edit:** (unknown)

<!-- end-managed-by: explore-codebase -->

## Glossary

<!-- managed-by: explore-codebase-glossary -->

See `context/glossary.md`; keep domain facts there.

<!-- end-managed-by: explore-codebase-glossary -->

## Program context

Read `context/glossary.md`, `context/systems-of-record.md`, `context/definition-of-done.md`, `context/decision-rights.md`, and `context/environments.md` when installed. Missing facts stay unknown. The glossary has one home in `context/glossary.md`; do not maintain a second glossary here.

Replace `(unknown)` with commands evidenced by `explore-codebase` or the README / CI config. A planner may persist the proposed map; a verifier runs checks. Never infer pass from discovering a command. When updating an existing file, preserve its unmanaged text and context pointers. For legacy managed glossary blocks, move evidenced terms into `context/glossary.md` before replacing the duplicate block with a pointer.
