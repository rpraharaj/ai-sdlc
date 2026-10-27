#!/usr/bin/env python3
"""Exercise the validator and installer CLIs against disposable pack copies."""

from __future__ import annotations

import json
import hashlib
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1]
FIXTURE_ENV = {**os.environ, "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull}


class PackChecks(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="ai-sdlc-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "pack"
        shutil.copytree(
            SOURCE, self.root,
            ignore=shutil.ignore_patterns(".git", ".agents", ".codex", "__pycache__"),
        )

    def command(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, *args], capture_output=True, text=True, timeout=30, env=FIXTURE_ENV,
        )

    def validate(self) -> subprocess.CompletedProcess[str]:
        return self.command(str(self.root / "scripts/check-pack.py"), "--structure-only")

    def change(self, rel: str, old: str, new: str) -> None:
        path = self.root / rel
        text = path.read_text()
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1))

    def rejects(self, diagnostic: str) -> None:
        result = self.validate()
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(diagnostic, result.stdout + result.stderr)

    def test_current_pack_passes(self) -> None:
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_vendor_frontmatter_rejected(self) -> None:
        self.change("skills/write-prd/SKILL.md", "license: MIT", "model: example\neffort: high\nlicense: MIT")
        self.rejects("frontmatter field")

    def test_duplicate_yaml_key_rejected(self) -> None:
        self.change("skills/write-prd/SKILL.md", "license: MIT", "name: write-prd\nlicense: MIT")
        self.rejects("duplicate")

    def test_malformed_yaml_rejected(self) -> None:
        self.change("skills/write-prd/SKILL.md", "license: MIT", "license: [unfinished")
        self.rejects("scalar")

    def test_invalid_version_rejected(self) -> None:
        path = self.root / "skills/write-prd/SKILL.md"
        path.write_text(re.sub(r'  version: .*', '  version: "0.1"', path.read_text()))
        self.rejects("semver")

    def test_missing_metadata_stage_rejected(self) -> None:
        self.change("skills/write-prd/SKILL.md", '  stage: "20-shape"', '  stage: "99-missing"')
        self.rejects("stage")

    def test_unknown_workflow_skill_rejected(self) -> None:
        self.change("workflows/deliver-slice.md", "Skill: `implement-change`", "Skill: `does-not-exist`")
        self.rejects("unknown skill")

    def test_unknown_workflow_profile_rejected(self) -> None:
        self.change("workflows/deliver-slice.md", "Agent profile: `implementer`", "Agent profile: `does-not-exist`")
        self.rejects("unknown profile")

    def test_test_authoring_cannot_use_verifier(self) -> None:
        path = self.root / "workflows/deliver-slice.md"
        text, count = re.subn(r"(Skill: `write-tests`[ \t]*\n[ \t]+Agent profile: )`implementer`", r"\1`verifier`", path.read_text())
        self.assertEqual(count, 1)
        path.write_text(text)
        self.rejects("write-tests requires implementer")

    def test_missing_template_rejected(self) -> None:
        self.change("skills/write-prd/SKILL.md", "references/prd-template.md", "references/missing-template.md")
        self.rejects("missing reference")

    def test_output_must_declare_template(self) -> None:
        self.change("skills/write-prd/SKILL.md", "- Template: `references/prd-template.md`", "- Template: none")
        self.rejects("Output needs a template reference")

    def test_unquoted_workflow_skill_rejected(self) -> None:
        self.change("workflows/deliver-slice.md", "Skill: `implement-change`", "Skill: implement-change")
        self.rejects("malformed Skill reference")

    def test_broken_markdown_link_rejected(self) -> None:
        with (self.root / "docs/README.md").open("a") as stream:
            stream.write("\n[missing](missing-document.md)\n")
        self.rejects("missing link")

    def test_quality_heading_without_checks_rejected(self) -> None:
        path = self.root / "skills/write-prd/SKILL.md"
        before, rest = path.read_text().split("## Quality bar\n", 1)
        _, after = rest.split("## Done", 1)
        path.write_text(before + "## Quality bar\nNo checks.\n\n## Done" + after)
        self.rejects("Quality bar needs")

    def test_heading_in_comment_does_not_count(self) -> None:
        self.change("skills/write-prd/SKILL.md", "## Required inputs", "<!-- ## Required inputs -->")
        self.rejects("missing heading")

    def test_unregistered_skill_directory_rejected(self) -> None:
        (self.root / "skills/unfinished").mkdir()
        self.rejects("unexpected skill")

    def test_non_string_metadata_rejected(self) -> None:
        self.change("skills/write-prd/SKILL.md", "  pack: ai-sdlc", "  pack: true")
        self.rejects("scalar")

    def test_duplicate_metadata_rejected(self) -> None:
        self.change("skills/write-prd/SKILL.md", "  pack: ai-sdlc", "  pack: ai-sdlc\n  pack: ai-sdlc")
        self.rejects("duplicate metadata")

    def test_duplicate_heading_rejected(self) -> None:
        with (self.root / "skills/write-prd/SKILL.md").open("a") as stream:
            stream.write("\n## Required inputs\nDuplicate.\n")
        self.rejects("duplicate section")

    def test_body_length_limit(self) -> None:
        with (self.root / "skills/write-prd/SKILL.md").open("a") as stream:
            stream.write("\nextra line" * 500)
        self.rejects("under 500 lines")

    def test_invalid_eval_json_has_diagnostic(self) -> None:
        (self.root / "evals/cases.json").write_text("[")
        result = self.command(str(self.root / "scripts/check-evals.py"))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("evals/cases.json:", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_duplicate_eval_id_rejected(self) -> None:
        path = self.root / "evals/cases.json"
        cases = json.loads(path.read_text())
        path.write_text(json.dumps(cases + [cases[0]]))
        result = self.command(str(self.root / "scripts/check-evals.py"))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unique", result.stdout)

    def test_eval_fixture_cannot_escape_root(self) -> None:
        path = self.root / "evals/cases.json"
        path.write_text(json.dumps([{"id": "escape", "fixture": "README.md", "assert": "file_contains", "needles": ["AI"]}]))
        result = self.command(str(self.root / "scripts/check-evals.py"))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("under evals/fixtures", result.stdout)

    def install(self, product: Path, *options: str) -> subprocess.CompletedProcess[str]:
        self.prepare_source()
        return self.command(str(self.root / "scripts/install-pack.py"), str(product), *options)

    def git(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
             "-c", "commit.gpgsign=false", "-c", "gc.auto=0", "-c", "maintenance.auto=false",
             "-c", f"core.hooksPath={self.temp.name}/empty-hooks", *args],
            cwd=self.root, capture_output=True, text=True, check=True, timeout=30, env=FIXTURE_ENV,
        )

    def prepare_source(self) -> None:
        if not (self.root / ".git").exists():
            self.git("init", "-q")
            self.git("add", "--all")
            self.git("commit", "-qm", "Fixture source snapshot")

    def refresh_inventory(self, product: Path, rel: str) -> None:
        path = product / ".agents/ai-sdlc-install.json"
        data = json.loads(path.read_text())
        entries = [entry for entry in data["files"] if entry["installed"] == rel]
        self.assertEqual(len(entries), 1)
        entries[0]["sha256"] = hashlib.sha256((product / rel).read_bytes()).hexdigest()
        path.write_text(json.dumps(data))

    def check_product(self, product: Path) -> subprocess.CompletedProcess[str]:
        return self.command(str(self.root / "scripts/check-pack.py"), "--structure-only", "--installed", str(product))

    def test_ignored_local_env_never_enters_payload(self) -> None:
        self.prepare_source()
        with (self.root / ".git/info/exclude").open("a") as stream:
            stream.write("\n.env\nlocal-note.txt\n")
        (self.root / "skills/write-prd/.env").write_text("FIXTURE_ONLY=not-a-real-secret\n")
        (self.root / "skills/write-prd/local-note.txt").write_text("Unreviewed local data\n")
        self.assertEqual(self.git("status", "--porcelain").stdout, "")
        product = Path(self.temp.name) / "product"
        product.mkdir()
        result = self.install(product, "--apply")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertFalse((product / ".agents/skills/write-prd/.env").exists())
        self.assertFalse((product / ".agents/skills/write-prd/local-note.txt").exists())
        inventory = json.loads((product / ".agents/ai-sdlc-install.json").read_text())
        self.assertFalse(inventory["source"]["dirty"])
        self.assertFalse(any(entry["installed"].endswith(("/.env", "/local-note.txt")) for entry in inventory["files"]))

    def test_committed_secret_filename_aborts_before_writes(self) -> None:
        self.prepare_source()
        (self.root / "skills/write-prd/.env").write_text("FIXTURE_ONLY=not-a-real-secret\n")
        self.git("add", "-f", "skills/write-prd/.env")
        self.git("commit", "-qm", "Fixture prohibited payload")
        product = Path(self.temp.name) / "product"
        product.mkdir()
        result = self.install(product, "--apply")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("secret filename", result.stderr)
        self.assertEqual(list(product.iterdir()), [])

    def test_refreshed_digest_does_not_approve_vendor_frontmatter(self) -> None:
        product = Path(self.temp.name) / "product"
        product.mkdir()
        result = self.install(product, "--apply")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        rel = ".agents/skills/write-prd/SKILL.md"
        path = product / rel
        path.write_text(path.read_text().replace("license: MIT", "model: fixture-only\nlicense: MIT", 1))
        self.refresh_inventory(product, rel)
        result = self.check_product(product)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("frontmatter field", result.stdout)

    def test_refreshed_digest_does_not_approve_broken_workflow(self) -> None:
        product = Path(self.temp.name) / "product"
        product.mkdir()
        result = self.install(product, "--apply", "--navigation")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        rel = "workflows/deliver-slice.md"
        path = product / rel
        path.write_text(path.read_text().replace("Skill: `implement-change`", "Skill: `does-not-exist`", 1))
        self.refresh_inventory(product, rel)
        result = self.check_product(product)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unknown skill", result.stdout)

    def test_dirty_source_aborts_before_writes(self) -> None:
        self.prepare_source()
        with (self.root / "README.md").open("a") as stream:
            stream.write("\nUnreviewed source change.\n")
        product = Path(self.temp.name) / "product"
        product.mkdir()
        result = self.install(product, "--apply")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("clean and pinned", result.stderr)
        self.assertEqual(list(product.iterdir()), [])

    def test_unversioned_source_aborts_before_writes(self) -> None:
        product = Path(self.temp.name) / "product"
        product.mkdir()
        result = self.command(str(self.root / "scripts/install-pack.py"), str(product), "--apply")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Git source checkout", result.stderr)
        self.assertEqual(list(product.iterdir()), [])

    def test_tracked_regular_assets_and_executable_modes_survive(self) -> None:
        scripts = self.root / "skills/write-prd/scripts"
        scripts.mkdir()
        probe = scripts / "probe.sh"
        probe.write_text("#!/bin/sh\nexit 0\n")
        probe.chmod(0o755)
        (self.root / "skills/write-prd/.env.example").write_text("EXAMPLE_ONLY=placeholder\n")
        product = Path(self.temp.name) / "product"
        product.mkdir()
        result = self.install(product, "--apply")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        installed = product / ".agents/skills/write-prd/scripts/probe.sh"
        self.assertEqual(installed.read_text(), "#!/bin/sh\nexit 0\n")
        self.assertTrue(installed.stat().st_mode & stat.S_IXUSR)
        self.assertTrue((product / ".agents/skills/write-prd/.env.example").is_file())

    def test_tracked_source_symlink_is_not_followed(self) -> None:
        outside = Path(self.temp.name) / "outside.txt"
        outside.write_text("Fixture data outside the reviewed source\n")
        (self.root / "skills/write-prd/outside.txt").symlink_to(outside)
        product = Path(self.temp.name) / "product"
        product.mkdir()
        result = self.install(product, "--apply")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("symlink source", result.stderr)
        self.assertEqual(list(product.iterdir()), [])

    def test_refreshed_digest_does_not_approve_empty_quality_bar(self) -> None:
        product = Path(self.temp.name) / "product"
        product.mkdir()
        result = self.install(product, "--apply")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        rel = ".agents/skills/write-prd/SKILL.md"
        path = product / rel
        before, rest = path.read_text().split("## Quality bar\n", 1)
        _, after = rest.split("## Done", 1)
        path.write_text(before + "## Quality bar\nNo checks.\n\n## Done" + after)
        self.refresh_inventory(product, rel)
        result = self.check_product(product)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Quality bar needs", result.stdout)

    def test_refreshed_digest_does_not_approve_incompatible_profile(self) -> None:
        product = Path(self.temp.name) / "product"
        product.mkdir()
        result = self.install(product, "--apply", "--navigation")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        rel = "workflows/deliver-slice.md"
        path = product / rel
        text, count = re.subn(r"(Skill: `write-tests`[ \t]*\n[ \t]+Agent profile: )`implementer`", r"\1`verifier`", path.read_text())
        self.assertEqual(count, 1)
        path.write_text(text)
        self.refresh_inventory(product, rel)
        result = self.check_product(product)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("write-tests requires implementer", result.stdout)

    def test_undeclared_local_secret_in_installed_skill_is_rejected(self) -> None:
        product = Path(self.temp.name) / "product"
        product.mkdir()
        result = self.install(product, "--apply")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        (product / ".agents/skills/write-prd/.env").write_text("FIXTURE_ONLY=not-a-real-secret\n")
        result = self.check_product(product)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("secret filename", result.stdout)

    def test_unrelated_product_navigation_is_not_pack_owned(self) -> None:
        product = Path(self.temp.name) / "product"
        (product / "workflows").mkdir(parents=True)
        (product / "workflows/team.md").write_text("[Team-owned link](not-a-pack-file.md)\n")
        result = self.install(product, "--apply")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        result = self.check_product(product)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_new_team_document_does_not_expand_pack_inventory(self) -> None:
        product = Path(self.temp.name) / "product"
        product.mkdir()
        result = self.install(product, "--apply", "--navigation")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        (product / "workflows/team.md").write_text("[Team-owned link](not-a-pack-file.md)\n")
        result = self.check_product(product)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_install_dry_run_has_no_side_effects(self) -> None:
        product = Path(self.temp.name) / "product"
        product.mkdir()
        result = self.install(product)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(list(product.iterdir()), [])

    def test_install_preserves_existing_program_facts(self) -> None:
        product = Path(self.temp.name) / "product"
        (product / "context").mkdir(parents=True)
        (product / "AGENTS.md").write_text("Existing rules\n")
        (product / "context/glossary.md").write_text("Real program glossary\n")
        result = self.install(product, "--apply", "--navigation")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual((product / "AGENTS.md").read_text(), "Existing rules\n")
        self.assertEqual((product / "context/glossary.md").read_text(), "Real program glossary\n")
        self.assertIn("merge", result.stdout.lower())
        result = self.command(str(self.root / "scripts/check-pack.py"), "--structure-only", "--installed", str(product))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_skill_collision_aborts_before_writes(self) -> None:
        product = Path(self.temp.name) / "product"
        collision = product / ".agents/skills/write-prd"
        collision.mkdir(parents=True)
        (collision / "custom.txt").write_text("Keep me")
        result = self.install(product, "--apply")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("collision", result.stdout + result.stderr)
        self.assertFalse((product / "context").exists())
        self.assertEqual((collision / "custom.txt").read_text(), "Keep me")

    def test_symlink_destination_rejected(self) -> None:
        product = Path(self.temp.name) / "product"
        outside = Path(self.temp.name) / "outside"
        product.mkdir(); outside.mkdir()
        (product / ".agents").symlink_to(outside, target_is_directory=True)
        result = self.install(product, "--apply")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(list(outside.iterdir()), [])

    def test_reinstall_does_not_overwrite(self) -> None:
        product = Path(self.temp.name) / "product"
        product.mkdir()
        first = self.install(product, "--apply")
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        second = self.install(product, "--apply")
        self.assertNotEqual(second.returncode, 0)
        self.assertIn("collision", second.stdout + second.stderr)

    def test_missing_installed_skill_detected(self) -> None:
        product = Path(self.temp.name) / "product"
        product.mkdir()
        result = self.install(product, "--apply")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        (product / ".agents/skills/write-prd/SKILL.md").unlink()
        result = self.command(str(self.root / "scripts/check-pack.py"), "--structure-only", "--installed", str(product))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing skill write-prd", result.stdout)

    def test_installed_skill_drift_detected(self) -> None:
        product = Path(self.temp.name) / "product"
        product.mkdir()
        result = self.install(product, "--apply")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        with (product / ".agents/skills/write-prd/SKILL.md").open("a") as stream:
            stream.write("\nLocal procedure change.\n")
        result = self.command(str(self.root / "scripts/check-pack.py"), "--structure-only", "--installed", str(product))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("local drift", result.stdout)

    def test_filling_program_context_is_expected(self) -> None:
        product = Path(self.temp.name) / "product"
        product.mkdir()
        result = self.install(product, "--apply")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        (product / "context/glossary.md").write_text("Program-owned domain facts\n")
        (product / "AGENTS.md").write_text("Program-owned commands and context pointers\n")
        result = self.command(str(self.root / "scripts/check-pack.py"), "--structure-only", "--installed", str(product))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_navigation_collision_aborts_before_writes(self) -> None:
        product = Path(self.temp.name) / "product"
        (product / "workflows").mkdir(parents=True)
        result = self.install(product, "--apply", "--navigation")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("collision", result.stderr)
        self.assertFalse((product / ".agents").exists())


if __name__ == "__main__":
    unittest.main()
