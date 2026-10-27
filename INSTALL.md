# Install this pack into a product repo

Install from a reviewed, pinned source revision. Procedures stay vendor-neutral; the helper uses Python's standard library and never overwrites an existing file.

## 1. Inspect and pin the source

Run `python3 scripts/check-pack.py` in this pack. Record its full git commit id; use a clean source checkout for the pilot. A tag is optional: the commit id is the pin until a reviewed tag exists. Do not treat a dirty checkout's HEAD as the revision of its uncommitted contents.

The installer requires Git and enforces a clean checkout rooted at the pack, for both dry run and apply. Unversioned archives, staged edits, modified files, and untracked files are refused. Review and commit the source changes before using the installer; running pack checks does not require a clean checkout.

## 2. Plan an initial install

From this pack, with an existing product directory:

```sh
python3 scripts/install-pack.py <product-repo> --navigation
```

The default is a dry run. It checks collisions before copying anything. Inspect any existing skill with the same name, including user-level skills in each chosen client. Do not silently replace a team's procedures.

## 3. Apply the inspected plan

```sh
python3 scripts/install-pack.py <product-repo> --navigation --apply
```

The helper:

- Copies only committed payload files into `.agents/skills/`; it excludes the source catalog README. Ignored local files are never selected, even when Git reports a clean checkout. Tracked secret filenames (such as `.env` and private-key files) and source symlinks are refused before any write. Tracked `.env.example` is allowed; executable asset modes are preserved.
- Copies missing `context/*.md` files and creates `AGENTS.md` only when absent.
- Preserves existing `AGENTS.md` and context files. It reports a manual merge: add the program-context, skills, and gate rules from `templates/consuming-AGENTS.md` without replacing existing commands or policies. Update preserved context with new headings such as approval evidence; keep the program's real facts.
- With `--navigation`, copies `agents/`, `playbooks/`, and `workflows/`. Any collision in these directories or a skill directory aborts the initial install. Symlinked destination parents are refused.
- Records source commit, dirty state, installed file paths and SHA-256 digests in `.agents/ai-sdlc-install.json`. This inventory records provenance; it grants no permissions.

A successful copy is not a completed onboarding. Fill context for the real program, resolve reported merges, and map profiles to the host's actual permissions. Unknown authority or required checks remain blocking. The source pack's [pilot checklist](docs/reference/pilot.md) defines readiness.

## 4. Verify the consuming repo

```sh
python3 scripts/check-pack.py --installed <product-repo>
```

This runs the source checks and verifies installed skill presence, inventory paths/digests, and Markdown links. It also applies the structural, template-reference, filename, and portability rules to the actual installed skills, plus headings and skill/profile assignments in pack-owned navigation. Refreshing a digest cannot approve malformed or vendor-specific content. Unrelated product navigation is outside that inventory. Program-owned context and `AGENTS.md` edits are expected and excluded from digest-drift failures. It does not certify program facts, approval evidence, or actual client behavior. Follow [pilot.md](docs/reference/pilot.md): in both selected clients record the loaded skill path/version, context facts, routing, output shape, and missing-input behavior. If discovery fails, use the [pointer adapters](adapters/README.md). Merge an adapter into an existing client file; never overwrite the team's file or fork a skill body.

## 5. Update an existing install

The initial installer deliberately refuses repeat installs. Update through a reviewed product-repo diff:

1. Keep the old source revision and `.agents/ai-sdlc-install.json`. Obtain the new reviewed source commit and run its checks.
2. Compare each previously installed file against its recorded digest. Locally edited skill files need a three-way merge (old source, local copy, new source); do not overwrite them. Preserve filled context and existing `AGENTS.md`.
3. Stage new files and merge template additions. Retain old fields during expand-then-contract migration. Remove a retired skill only after checking references and local modifications.
4. Review the merged content, then update the proposed inventory with the new source revision and digests; distinguish local merges from verbatim source copies. Run source checks with `--installed` against that proposed inventory, consuming-repo checks, and affected two-client smoke cases. Invalid content must be fixed even when its refreshed digest matches. Do not commit the update if any required check fails.
5. Commit the product update and provenance together. A failed update rolls back with that product commit; do not reset unrelated work.

## 6. Remove or roll back

Use the install inventory and product history to identify pack-added files. Revert the reviewed install/update commit when it contains only pack changes. Otherwise remove only unchanged pack-owned files, preserving local edits, program context, specs, and artifacts. Merge out only pack-added instruction/adapter blocks. Do not delete the entire `.agents/skills/` or `context/` directory. No runtime needs undeployment.

Humans use [docs/how-to-use.md](docs/how-to-use.md). Maintainers use root `AGENTS.md` and [CONTRIBUTING.md](CONTRIBUTING.md).
