# Pack changes

## Follow-up — 2026-10-28 installer and installed-validation fixes

The final review reproduced two remaining failures: an ignored `.env` fixture entered an install marked as coming from a clean source, and an installed skill with forbidden frontmatter passed after its inventory digest was refreshed.

- Select initial payloads only from the clean source commit's file list. Refuse dirty/unversioned sources, prohibited secret filenames even when tracked, and source symlinks. Preserve reviewed executable assets and normalize inventory paths to portable separators.
- Reuse the source structural and portability checks on actual installed skills and pack-owned navigation. Check workflow/profile compatibility and secret filenames independently of refreshed digests, without claiming unrelated product documents.
- Add regression cases for both reproduced failures, tracked-secret refusal, source cleanliness, valid assets, source symlinks, invalid merged quality bars/profiles, and product-document ownership. Isolate temporary Git fixtures from host configuration and background maintenance.
- Update installation, update-review, governance, and evaluation guidance. These changes add no runtime dependency to consuming agents and do not modify the portable skill procedures.

## Unreleased — 2026-10-27 pilot hardening

The critical review found contradictory permission envelopes, workflow-only release gates, weak approval and traceability contracts, unsafe copy instructions, and structural checks that accepted broken packs. The four failing validator traces are now CLI regression cases in [scripts/test-check-pack.py](scripts/test-check-pack.py): vendor-only frontmatter, unknown workflow skill, missing template, and an empty quality checklist.

### Procedures and contracts

- Align profiles and workflow assignments: explore reports a read-only map; planner persists documentation; implementer authors tests; verifier executes them. Coordinator reads git/CI evidence; reviewer may write separate findings and inspect a prepared UI. Production execution still follows program decision rights.
- Require revision-bound human evidence for prerequisite approvals and scoped waivers. Unknown/unrun required checks block Ready, and changed baselines invalidate affected review/checks/approval.
- Require standalone release and rollback paths to honor target/environment authority. Release requires executed regression evidence, notes, rollback, and current go/no-go; triage proposes the commander's decision without changing runtime systems.
- Preserve requirement/defect or shaped-acceptance references through design, tasks, implementation, tests, and the Ready report. Resolve blocking reviews before final design approval.
- Add approval, source-revision, coverage, verification, and release-evidence fields to templates while retaining existing headings and report fields. Existing accepted labels must be supplemented with actual human evidence; they are not grandfathered signatures. Legacy managed glossary sections retain a pointer while facts move to the program glossary.

### Skill versions

- Normalize every legacy two-part version to stable `major.minor.patch`.
- Core skills with changed procedures or templates move to `0.4.0`: `cut-release`, `explain-code`, `explore-codebase`, `implement-change`, `incident-triage`, `open-pr`, `ready-to-merge`, `record-decision`, `revert-change`, `review-change`, `write-architecture`, `write-design`, `write-dev-tasks`, `write-prd`, `write-tests`.
- `synthesize-discovery`, `write-integration-contract`, `write-requirements`, and `write-status` move to `0.2.0`; `build-regression-pack` moves to `0.3.0`.

### Installation and verification

- Add a standard-library initial installer with dry run, collision refusal, preserved program files, exclusive file creation, and commit/digest provenance. Repeated installs are refused; reviewed three-way updates and ownership-aware removal are documented in [INSTALL.md](INSTALL.md).
- Check the frontmatter subset, duplicate keys/headings, versions/stages, actual template/link targets, workflow skill/profile references, critical permission assignments, and installed inventory drift. The default pack command includes static cases and negative validator/installer tests. The source repository CI runs that command; no vendor orchestration is added to the portable pack.
- Define the real-program setup record, two-client smoke cases, measurements, and exit/stop criteria in [pilot.md](docs/reference/pilot.md). Live behavior and real program approvals remain unverified until observed; static validation does not certify model adherence.

Validation: `python3 scripts/check-pack.py`. Updates must also run consuming-repo checks and the affected pilot cases; no consuming program is configured by this source change.
