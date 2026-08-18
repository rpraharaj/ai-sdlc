# Install this pack into a product repo

No installer required. Copy files. Procedure text has one home: `skills/` in this repository.

After install, humans follow [docs/how-to-use.md](docs/how-to-use.md).

## 1. Context (Wave 0)

```sh
cp -R context <product-repo>/context
cp templates/consuming-AGENTS.md <product-repo>/AGENTS.md
```

If the product repo already has an `AGENTS.md`, do not overwrite it. Add a “Program context” section that points at `context/*.md` and fill in real install/run/test commands.

Fill every file under `<product-repo>/context/` for **that** program. Leave placeholders only while the fact is still unknown.

## 2. Skills

```sh
mkdir -p <product-repo>/.agents/skills
cp -R skills/. <product-repo>/.agents/skills/
```

A later pin (submodule, subtree, or tag) is better than an unversioned copy. Until then, a copy is enough.

This repo is standalone. `write-prd`, `implement-change`, `ready-to-merge`, and the rest of the engineering skills live under `skills/` here.

## 3. Humans and hosts (optional copy)

```sh
cp -R playbooks <product-repo>/playbooks
cp -R workflows <product-repo>/workflows
```

`agents/` stays in this pack as the permission checklist. Map each profile onto the host’s read-only / write / execute mode. Do not rewrite procedure text into vendor agent YAML.

## 4. Adapters (only if discovery fails)

See [adapters/README.md](adapters/README.md). Copy the one-line pointer for that client, or symlink `CLAUDE.md` → `AGENTS.md`. Never fork a `SKILL.md` into a vendor folder.

## 5. Check discovery

Open the product repo in two AI coding clients and confirm each lists a skill by `name` (for example `write-requirements`). If a client does not scan `.agents/skills/`, use step 4.

## 6. Check this pack itself

From this repository:

```sh
python3 scripts/check-pack.py
```
