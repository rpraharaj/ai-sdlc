# Bar checks

Walk each section on the **current diff**. Pass, fail, or n/a.

## How to load

Other skills load `../engineering-bar/SKILL.md`, then this file.

## Secret files

Fail commit and ready-to-merge if the change adds:

- `.env`, `.env.*` except a tracked `.env.example`
- private keys, `*.pem`, `*.p12`, `id_rsa`, `id_ed25519`
- credential files, keystores, dumped tokens
- secrets pasted into otherwise-normal files

## Defaults when AGENTS.md is missing

- Do not claim tests, types, lint, or builds passed unless this session ran the command and captured the output.
- Do not commit secrets.
- Match this repository. Do not introduce a new stack, formatter, or test runner.
- Smallest change. Prefer reuse, stdlib, and native platform features. No drive-by refactors.
- Do not force-push shared branches. Do not amend other people's commits.
- Do not delete or skip a failing test to get a green run.

## Correctness

- Acceptance checks from `shape-work` (if any) are met, or the task is not done.
- Happy path, edge cases, and error paths this change can hit are handled.
- No empty `catch` / swallowed rejection / ignored error return.

## Minimum path

Stop at the first rung that holds: Need? Already here? Stdlib? Native platform? Already installed? One line? Only then write the minimum.

**Never cut** to win a smaller diff: validation at trust boundaries, error handling that prevents data loss, authorization, secret handling, or accessibility of new interactive UI.

If you accept a known ceiling, say the ceiling and the trigger to revisit.

## Change hygiene

- Smallest diff after Minimum path.
- No unused code, commented-out blocks, or unrelated cleanup.
- No interface/factory/config for a single implementation or a value that never changes.

## Structure

- Logic lives in the layer that already owns that concept.
- Do not grow a hard-to-scan file when a split is obvious.
- Do not add a flag that turns one function into two programs.

## Failure

- I/O has a timeout or this repo's equivalent.
- Retries are bounded and safe to repeat, or there are no retries.
- Failures carry enough context to debug and never carry secrets.

## Data

- Input is validated where it enters.
- Schema and public contract changes are expand, then deploy, then contract — not both in one step.
- Lists, pages, and jobs are bounded.

## Security (this delta only)

- New reachable surface has authorization, not only authentication, if this repo uses auth.
- Untrusted input stays untrusted.
- Secrets are not in source, logs, client bundles, or fixtures.

## Performance (guard)

- No new query/RPC inside a loop (N+1).
- No unbounded work on a request or UI path.
- No accidental full-collection scan.
- No huge eager import on a hot route.

Do not optimize without a measurement unless the diff clearly adds one of the above. Guess-caching is a fail.

## UI

When the diff adds or changes interactive UI:

- New controls have an accessible name, are keyboard-reachable, and are not unreadable.
- No layout jump from images/embeds/fonts with no reserved size.
- Empty, error, and loading states the change can hit are handled.

Walk-through is `verify-ui`.

## Operability

- A new failure mode is visible with whatever this repo already uses.
- Risky behavior has a rollback sentence you can say out loud.
- Docs, types, or generated clients this change made wrong are updated in the same work.

## Output

Report only fails and waivers, then the list of checks that ran.
