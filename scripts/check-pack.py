#!/usr/bin/env python3
"""Validate this pack's skills, agents, playbooks, workflows, and denylist."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
AGENTS = ROOT / "agents"
PLAYBOOKS = ROOT / "playbooks"
WORKFLOWS = ROOT / "workflows"

WAVE1 = [
    "write-opportunity",
    "synthesize-discovery",
    "write-requirements",
    "map-process",
    "write-nfr",
    "write-integration-contract",
    "write-test-strategy",
    "plan-uat",
    "update-raid",
    "write-status",
    "assess-change",
    "write-runbook",
]

WAVE2 = [
    "prioritize-backlog",
    "design-experiment",
    "spec-analytics",
    "review-architecture",
    "write-spike",
    "classify-data",
    "write-ui-spec",
    "map-design-handoff",
    "write-api-examples",
    "plan-data-migration",
    "a11y-pass",
    "write-test-plan",
    "charter-exploratory",
    "triage-defect",
    "build-regression-pack",
    "review-pipeline",
    "diff-environments",
    "spec-observability",
    "plan-rollback",
    "plan-increment",
    "triage-blockers",
    "draft-steerco",
    "map-dependencies",
]

CORE = [
    "write-prd",
    "shape-work",
    "write-dev-tasks",
    "write-architecture",
    "write-design",
    "record-decision",
    "explore-codebase",
    "explain-code",
    "implement-change",
    "write-tests",
    "debug",
    "refactor-safely",
    "data-change",
    "review-change",
    "lean-review",
    "engineering-bar",
    "security-pass",
    "performance",
    "production-pass",
    "verify-ui",
    "ready-to-merge",
    "cut-release",
    "ship-notes",
    "incident-triage",
    "fix-ci",
    "handoff",
    "start-project",
    "write-docs",
    "commit",
    "open-pr",
    "revert-change",
]

EXPECTED_SKILLS = WAVE1 + WAVE2 + CORE

EXPECTED_AGENTS = [
    "explore",
    "planner",
    "shaper",
    "implementer",
    "reviewer",
    "verifier",
    "releaser",
    "coordinator",
    "incident-lead",
]

EXPECTED_PLAYBOOKS = [
    "program-manager",
    "project-manager",
    "product-manager",
    "business-analyst",
    "solution-architect",
    "ui-developer",
    "backend-developer",
    "qa",
    "devops",
]

EXPECTED_WORKFLOWS = [
    "shape-initiative",
    "design-initiative",
    "deliver-slice",
    "release-train",
    "weekly-program",
    "incident",
]

EXPECTED_ADAPTERS = [
    "claude",
    "cursor",
    "copilot",
    "gemini",
    "codex",
    "generic",
]

ADAPTER_PROCEDURE = (
    "Is this the right skill",
    "Quality bar",
    "## Procedure",
)

SKILL_HEADINGS = [
    "Is this the right skill",
    "Required inputs",
    "Human decisions",
    "Procedure",
    "Output",
    "Quality bar",
    "Done",
]

AGENT_SNIPPETS = [
    "Mode:",
    "May edit product code:",
    "May run commands:",
    "Must not:",
    "Session rules",
]

PLAYBOOK_SNIPPETS = ["Jobs", "Run", "Own", "Consume", "Still decide"]

WORKFLOW_SNIPPETS = [
    "When to use",
    "When not to use",
    "Inputs",
    "Outputs",
    "Steps",
    "Human gate",
    "Failure",
    "Done",
]

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

DENYLIST = [
    (re.compile(r"run_terminal_command"), "vendor tool name"),
    (re.compile(r"spawn_subagent"), "vendor tool name"),
    (re.compile(r"^disable-model-invocation\s*:", re.M), "vendor frontmatter"),
    (re.compile(r"^when-to-use\s*:", re.M), "vendor frontmatter"),
    (re.compile(r"^user-invocable\s*:", re.M), "vendor frontmatter"),
    (re.compile(r"You are Grok", re.I), "vendor persona"),
    (re.compile(r"You are Claude", re.I), "vendor persona"),
    (re.compile(r"You are Copilot", re.I), "vendor persona"),
]

SCAN_DIRS = ("skills", "context", "templates", "agents", "playbooks", "workflows")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    rest = text[3:]
    end = rest.find("\n---")
    if end < 0:
        raise ValueError("unterminated frontmatter")
    raw = rest[:end].strip("\n")
    body = rest[end + 4 :].lstrip("\n")
    meta: dict[str, str] = {}
    key: str | None = None
    folded: list[str] = []
    for line in raw.splitlines():
        if key and (line.startswith("  ") or line.startswith("\t")):
            folded.append(line.strip())
            continue
        if key:
            meta[key] = " ".join(folded).strip()
            key = None
            folded = []
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"cannot parse frontmatter line: {line!r}")
        k, _, v = line.partition(":")
        k, v = k.strip(), v.strip()
        if v in (">", "|"):
            key = k
            folded = []
        else:
            meta[k] = v.strip("\"'")
    if key:
        meta[key] = " ".join(folded).strip()
    return meta, body


def check_skill(dirpath: Path, errors: list[str]) -> None:
    skill_md = dirpath / "SKILL.md"
    rel = skill_md.relative_to(ROOT)
    if not skill_md.is_file():
        errors.append(f"{dirpath.relative_to(ROOT)}: missing SKILL.md")
        return
    text = skill_md.read_text(encoding="utf-8")
    try:
        meta, body = parse_frontmatter(text)
    except ValueError as exc:
        errors.append(f"{rel}: {exc}")
        return
    name = meta.get("name", "")
    desc = meta.get("description", "")
    if not name:
        errors.append(f"{rel}: missing name")
    elif not NAME_RE.fullmatch(name):
        errors.append(f"{rel}: invalid name {name!r}")
    elif name != dirpath.name:
        errors.append(f"{rel}: name {name!r} != directory {dirpath.name!r}")
    if not desc:
        errors.append(f"{rel}: missing description")
    elif len(desc) > 1024:
        errors.append(f"{rel}: description is {len(desc)} chars (max 1024)")
    for snippet in SKILL_HEADINGS:
        if snippet.lower() not in body.lower():
            errors.append(f"{rel}: missing heading containing {snippet!r}")
    refs = dirpath / "references"
    if not refs.is_dir() or not any(refs.glob("*.md")):
        errors.append(f"{dirpath.relative_to(ROOT)}: missing references/*.md template")


def check_named_markdown(
    folder: Path,
    expected: list[str],
    snippets: list[str],
    errors: list[str],
    label: str,
) -> None:
    if not folder.is_dir():
        errors.append(f"{folder.relative_to(ROOT)}/: missing")
        return
    found = sorted(
        p.stem
        for p in folder.iterdir()
        if p.is_file() and p.suffix == ".md" and p.name != "README.md"
    )
    for name in expected:
        if name not in found:
            errors.append(f"missing {label}: {name}")
    extra = set(found) - set(expected)
    if extra:
        errors.append(f"unexpected {label}s: {', '.join(sorted(extra))}")
    for name in found:
        text = (folder / f"{name}.md").read_text(encoding="utf-8")
        for snippet in snippets:
            if snippet.lower() not in text.lower():
                errors.append(f"{folder.relative_to(ROOT)}/{name}.md: missing {snippet!r}")


def check_denylist(errors: list[str]) -> None:
    for folder in SCAN_DIRS:
        root = ROOT / folder
        if not root.is_dir():
            continue
        for path in root.rglob("*"):
            if not path.is_file() or path.suffix not in {".md", ".py", ".sh"}:
                continue
            text = path.read_text(encoding="utf-8")
            for pattern, why in DENYLIST:
                if pattern.search(text):
                    errors.append(
                        f"{path.relative_to(ROOT)}: denylist ({why}) matched {pattern.pattern}"
                    )


def check_adapters(errors: list[str]) -> None:
    root = ROOT / "adapters"
    if not root.is_dir():
        errors.append("adapters/: missing")
        return
    if not (root / "README.md").is_file():
        errors.append("adapters/README.md: missing")
    found = sorted(p.name for p in root.iterdir() if p.is_dir())
    for name in EXPECTED_ADAPTERS:
        if name not in found:
            errors.append(f"missing adapter: {name}")
    extra = set(found) - set(EXPECTED_ADAPTERS)
    if extra:
        errors.append(f"unexpected adapter dirs: {', '.join(sorted(extra))}")
    for path in root.rglob("*"):
        if path.name == "SKILL.md":
            errors.append(f"{path.relative_to(ROOT)}: adapters must not contain SKILL.md")
        if not path.is_file():
            continue
        if path.suffix not in {".md", ".mdc"}:
            continue
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        if "AGENTS.md" not in text:
            errors.append(f"{rel}: adapter must point at AGENTS.md")
        for banned in ADAPTER_PROCEDURE:
            if banned in text:
                errors.append(f"{rel}: adapter contains procedure text {banned!r}")


def check_evals(errors: list[str]) -> None:
    script = ROOT / "scripts" / "check-evals.py"
    if not script.is_file():
        errors.append("scripts/check-evals.py: missing")
        return
    result = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        detail = (result.stdout or result.stderr).strip() or f"exit {result.returncode}"
        errors.append(f"check-evals failed:\n{detail}")


def check_write_requirements_stops(errors: list[str]) -> None:
    path = SKILLS / "write-requirements" / "SKILL.md"
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8").lower()
    if "stop" not in text or "write-prd" not in text:
        errors.append(
            "skills/write-requirements/SKILL.md: must stop and name write-prd when PRD is missing"
        )


def main() -> int:
    errors: list[str] = []
    if not SKILLS.is_dir():
        print("skills/: missing", file=sys.stderr)
        return 1
    found = sorted(p.name for p in SKILLS.iterdir() if p.is_dir() and (p / "SKILL.md").exists())
    for name in EXPECTED_SKILLS:
        if name not in found:
            errors.append(f"missing skill: {name}")
    extra = set(found) - set(EXPECTED_SKILLS)
    if extra:
        errors.append(f"unexpected skill dirs: {', '.join(sorted(extra))}")
    for name in found:
        check_skill(SKILLS / name, errors)
    check_named_markdown(AGENTS, EXPECTED_AGENTS, AGENT_SNIPPETS, errors, "agent")
    check_named_markdown(PLAYBOOKS, EXPECTED_PLAYBOOKS, PLAYBOOK_SNIPPETS, errors, "playbook")
    check_named_markdown(WORKFLOWS, EXPECTED_WORKFLOWS, WORKFLOW_SNIPPETS, errors, "workflow")
    check_denylist(errors)
    check_write_requirements_stops(errors)
    check_adapters(errors)
    check_evals(errors)
    if errors:
        print(f"check-pack: {len(errors)} failure(s)")
        for err in errors:
            print(f"  - {err}")
        return 1
    print(
        f"check-pack: ok ({len(found)} skills, "
        f"{len(EXPECTED_AGENTS)} agents, "
        f"{len(EXPECTED_PLAYBOOKS)} playbooks, "
        f"{len(EXPECTED_WORKFLOWS)} workflows, "
        f"{len(EXPECTED_ADAPTERS)} adapters)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
