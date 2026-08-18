# Principles

These rules apply to every file this pack contains. They are not restated inside each skill.

## 1. Work type, not job title

The catalog is named by the artifact or check (`write-prd`, `update-raid`, `plan-uat`). Job titles appear only on [role cards](role-cards.md), which are indexes.

If two roles would run the same steps on the same inputs, that is one skill.

## 2. One home per fact

Glossary terms, Definition of Done, system names, environment names, and decision rights each live in one context file. Skills point. They do not copy.

Adapters point. They do not copy procedure text.

## 3. Artifacts are the contract

Roles do not hand off “knowledge.” They hand off a named file with a template and traces. The next skill **stops** if that file is missing. See [artifact-chain](artifact-chain.md).

## 4. Human stops stay human

The model drafts. A named human decides:

- scope, priority Must vs Should
- dates, funding, killing a workstream
- irreversible technology choice (via an ADR they sign)
- go-live, production deploy
- legal / compliance
- money and cloud-account changes

A skill that needs one of these and does not have a signed answer **stops**. It does not invent the answer.

## 5. Evidence or stop

Do not invent users, personas, SLOs, vendors, baselines, or RAG status. Unknowns stay `unknown` or `n/a`. Status may only cite RAID, git, CI, or a named artifact.

## 6. Portable by default

Canonical files are valid on any Agent Skills + AGENTS.md client. Vendor features are adapters. See [portability](portability.md).

## 7. Progressive disclosure

Always-on context (`AGENTS.md`) stays short. Procedures live in skills. Long templates and notes live in `references/` and are loaded only when the skill says when to open them.

## 8. Smallest next artifact

Do not write a PRD for a one-line bug. Do not write architecture for a local rename. Every skill has a “do this instead” table.

## 9. Reuse before rewrite

Call an existing skill by name. Do not fork its body into a second folder or a vendor adapter.

## 10. Kill unused procedure

If a skill is not run in 30 days of a pilot, remove it or rewrite it from a real trace. A skill that only says “be a helpful project manager” is invalid.
