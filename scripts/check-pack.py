#!/usr/bin/env python3
"""Validate this pack's skills, agents, playbooks, workflows, and denylist."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from pack_files import is_secret_filename

ROOT = Path(__file__).resolve().parents[1]

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
    "May use tool kinds:",
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

FRONTMATTER_FIELDS = {"name", "description", "license", "compatibility", "metadata"}
STAGES = {"10-discover", "20-shape", "30-design", "40-build", "50-verify", "60-release", "70-govern"}
SEMVER = re.compile(r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\Z")
REFERENCE = re.compile(r"(?:\.\./[a-z0-9-]+/)?references/[a-zA-Z0-9_./-]+\.md")
PROFILE_REQUIREMENTS = {
    "write-tests": {"implementer"}, "implement-change": {"implementer"},
    "ready-to-merge": {"verifier"}, "cut-release": {"releaser"},
    "review-change": {"reviewer"}, "review-architecture": {"reviewer"},
    "write-status": {"coordinator"}, "explore-codebase": {"explore"},
}


def scalar(value: str) -> str:
    """Read the deliberately small YAML string subset used by this pack."""
    if value.startswith('"'):
        try:
            result = json.loads(value)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid quoted scalar: {value!r}") from exc
        if not isinstance(result, str):
            raise ValueError("frontmatter scalar must be a string")
        return result
    if value.startswith("'"):
        if not re.fullmatch(r"'(?:[^']|'')*'", value):
            raise ValueError(f"invalid quoted scalar: {value!r}")
        return value[1:-1].replace("''", "'")
    if (not value or value[0] in "[{}]&*!|>\"%@`" or value.endswith(":")
            or ": " in value or " #" in value or "\t" in value
            or value.lower() in {"true", "false", "null", "~", "yes", "no", "on", "off"}
            or value[0] in "+-0123456789"):
        raise ValueError(f"unsupported scalar {value!r}; quote strings, do not use YAML collections or aliases")
    return value


def parse_frontmatter(text: str) -> tuple[dict, str]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("SKILL.md must start with YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("unterminated frontmatter") from exc
    fields: dict = {}
    index = 1
    while index < end:
        line = lines[index]
        index += 1
        if not line.strip() or line.startswith("#"):
            continue
        match = re.fullmatch(r"([a-z][a-z0-9-]*):(?: (.*))?", line)
        if not match:
            raise ValueError(f"unsupported frontmatter line or indentation: {line!r}")
        key, value = match.group(1), match.group(2) or ""
        if key in fields:
            raise ValueError(f"duplicate frontmatter key: {key}")
        if key not in FRONTMATTER_FIELDS:
            raise ValueError(f"unsupported frontmatter field: {key}")
        if key == "metadata":
            if value:
                raise ValueError("metadata must be an indented mapping of string scalars")
            metadata: dict[str, str] = {}
            while index < end and lines[index].startswith("  "):
                child = re.fullmatch(r"  ([a-z][a-z0-9-]*): (.+)", lines[index])
                if not child:
                    raise ValueError(f"invalid metadata scalar: {lines[index]!r}")
                name, content = child.groups()
                if name in metadata:
                    raise ValueError(f"duplicate metadata key: {name}")
                metadata[name] = scalar(content)
                index += 1
            fields[key] = metadata
        elif value in {">", "|"}:
            block = []
            while index < end and (lines[index].startswith("  ") or not lines[index].strip()):
                block.append(lines[index][2:])
                index += 1
            fields[key] = (" " if value == ">" else "\n").join(block).strip()
        else:
            fields[key] = scalar(value)
    return fields, "\n".join(lines[end + 1:]).lstrip("\n")


def prose(text: str) -> str:
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    return re.sub(r"^(`{3,}|~{3,})[^\n]*\n.*?^\1[^\n]*$", "", text, flags=re.M | re.S)


def sections(text: str) -> dict[str, str]:
    parts = re.split(r"^## ([^\n]+)\n", prose(text), flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts), 2)}


def check_skill(dirpath: Path, errors: list[str], root: Path) -> None:
    skill_md = dirpath / "SKILL.md"
    rel = skill_md.relative_to(root)
    if not skill_md.is_file():
        errors.append(f"{rel}: missing SKILL.md")
        return
    text = skill_md.read_text(encoding="utf-8")
    try:
        meta, body = parse_frontmatter(text)
    except ValueError as exc:
        errors.append(f"{rel}: {exc}")
        return
    name, desc = meta.get("name", ""), meta.get("description", "")
    if not NAME_RE.fullmatch(name) or len(name) > 64 or name != dirpath.name:
        errors.append(f"{rel}: invalid name {name!r}; must match directory and be at most 64 characters")
    if not desc or len(desc) > 1024:
        errors.append(f"{rel}: description must have 1–1024 characters")
    metadata = meta.get("metadata", {})
    if metadata.get("pack") != "ai-sdlc":
        errors.append(f"{rel}: metadata.pack must be ai-sdlc")
    if not SEMVER.fullmatch(metadata.get("version", "")):
        errors.append(f"{rel}: metadata.version must use stable semver major.minor.patch")
    if metadata.get("stage") not in STAGES:
        errors.append(f"{rel}: missing or invalid metadata.stage")
    if len(body.splitlines()) >= 500:
        errors.append(f"{rel}: body must be under 500 lines")
    found = sections(body)
    titles = re.findall(r"^## ([^\n]+)", prose(body), re.M)
    if len(titles) != len(set(titles)):
        errors.append(f"{rel}: duplicate section heading")
    for heading in SKILL_HEADINGS:
        if not any(title.rstrip("?") == heading or title.startswith(heading + " (") for title in found):
            errors.append(f"{rel}: missing heading {heading!r}")
    if not re.search(r"^- \[[ xX]\] .+", found.get("Quality bar", ""), re.M):
        errors.append(f"{rel}: Quality bar needs a yes/no checklist")
    routing = found.get("Is this the right skill?", found.get("Is this the right skill", ""))
    # The question mark is part of the canonical heading.
    if not routing:
        routing = next((content for title, content in found.items() if title.startswith("Is this the right skill")), "")
    if not re.search(r"^\|.*\|.*\|", routing, re.M):
        errors.append(f"{rel}: routing needs a handoff table")
    refs = dirpath / "references"
    if not refs.is_dir() or not any(refs.glob("*.md")):
        errors.append(f"{rel}: missing references/*.md template")
    if not REFERENCE.search(found.get("Output", "")):
        errors.append(f"{rel}: Output needs a template reference")
    references = set(REFERENCE.findall(body))
    if not references:
        errors.append(f"{rel}: missing reference to an output template")
    for target in sorted(references):
        path = (dirpath / target).resolve()
        if not path.is_relative_to(root.resolve()) or not path.is_file():
            errors.append(f"{rel}: missing reference {target}")


def check_named_markdown(folder: Path, expected: list[str], snippets: list[str],
                         errors: list[str], label: str, root: Path, allow_extra: bool = False) -> None:
    if not folder.is_dir():
        errors.append(f"{folder.relative_to(root)}: missing")
        return
    found = {p.stem for p in folder.glob("*.md") if p.name != "README.md"}
    for name in sorted(set(expected) - found):
        errors.append(f"missing {label}: {name}")
    if allow_extra:
        found &= set(expected)
    else:
        for name in sorted(found - set(expected)):
            errors.append(f"unexpected {label}: {name}")
    for name in sorted(found):
        path = folder / f"{name}.md"
        text = prose(path.read_text(encoding="utf-8"))
        for snippet in snippets:
            if snippet.lower() not in text.lower():
                errors.append(f"{path.relative_to(root)}: missing {snippet!r}")


def check_workflows(root: Path, errors: list[str], paths: list[Path] | None = None) -> None:
    for path in sorted(paths if paths is not None else (root / "workflows").glob("*.md")):
        if not path.is_file():
            continue  # Missing named files are reported by check_named_markdown.
        steps = sections(path.read_text()).get("Steps", "")
        for step in re.split(r"^\d+\. ", steps, flags=re.M):
            match = re.search(r"Skill: `([^`]+)`", step)
            if not match:
                if "Skill:" in step:
                    errors.append(f"{path.relative_to(root)}: malformed Skill reference")
                continue
            skill = match.group(1)
            if skill not in EXPECTED_SKILLS:
                errors.append(f"{path.relative_to(root)}: unknown skill {skill}")
            profile_line = re.search(r"Agent profile: ([^\n]+)", step)
            profiles = re.findall(r"`([^`]+)`", profile_line.group(1)) if profile_line else []
            if not profiles:
                errors.append(f"{path.relative_to(root)}: skill {skill} needs an Agent profile")
            for profile in profiles:
                if profile not in EXPECTED_AGENTS:
                    errors.append(f"{path.relative_to(root)}: unknown profile {profile}")
                permitted = PROFILE_REQUIREMENTS.get(skill)
                if permitted and profile not in permitted:
                    errors.append(f"{path.relative_to(root)}: {skill} requires {' or '.join(sorted(permitted))}, not {profile}")


def check_links(root: Path, paths: list[Path], errors: list[str]) -> None:
    for path in paths:
        text = prose(path.read_text(encoding="utf-8"))
        for match in re.finditer(r"\[[^\]\n]*\]\(([^\s)]+)(?:\s+[^)]*)?\)", text):
            target = match.group(1).strip("<>")
            try:
                parsed = urlsplit(target)
            except ValueError:
                errors.append(f"{path.relative_to(root)}: invalid link {target}")
                continue
            if parsed.scheme or target.startswith(("#", "//")):
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                errors.append(f"{path.relative_to(root)}: missing link {target}")


def check_denylist(root: Path, errors: list[str], folders: list[Path] | None = None) -> None:
    for folder in folders if folders is not None else [root / name for name in SCAN_DIRS]:
        for path in [folder] if folder.is_file() else folder.rglob("*"):
            if is_secret_filename(path) and (path.is_file() or path.is_symlink()):
                errors.append(f"{path.relative_to(root)}: secret filename forbidden in pack")
                continue
            if not path.is_file() or path.suffix not in {".md", ".py", ".sh"}:
                continue
            text = path.read_text(encoding="utf-8")
            for pattern, why in DENYLIST:
                if pattern.search(text):
                    errors.append(f"{path.relative_to(root)}: denylist ({why}) matched {pattern.pattern}")


def check_adapters(root: Path, errors: list[str]) -> None:
    folder = root / "adapters"
    if not (folder / "README.md").is_file():
        errors.append("adapters: missing README.md")
    found = {p.name for p in folder.iterdir() if p.is_dir()} if folder.is_dir() else set()
    if found != set(EXPECTED_ADAPTERS):
        errors.append("adapters: missing or unexpected adapter directories")
    for path in folder.rglob("*"):
        if path.name == "SKILL.md":
            errors.append(f"{path.relative_to(root)}: adapters must not contain SKILL.md")
        if not path.is_file() or path.suffix not in {".md", ".mdc"}:
            continue
        text = path.read_text(encoding="utf-8")
        if "AGENTS.md" not in text or any(banned in text for banned in ADAPTER_PROCEDURE):
            errors.append(f"{path.relative_to(root)}: adapters must be pointers to AGENTS.md, without procedures")


def run_check(script: Path, args: list[str], errors: list[str], timeout: int = 60) -> None:
    if not script.is_file():
        errors.append(f"missing check: {script.name}")
        return
    try:
        result = subprocess.run([sys.executable, str(script), *args], cwd=script.parent.parent,
                                capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        errors.append(f"{script.name}: timed out after {timeout} seconds")
        return
    detail = (result.stdout + result.stderr).strip()
    if result.returncode:
        errors.append(f"{script.name} failed:\n{detail}")
    elif detail:
        print(detail)


def validate_pack(root: Path) -> list[str]:
    errors: list[str] = []
    skills = root / "skills"
    found = {p.name for p in skills.iterdir() if p.is_dir()} if skills.is_dir() else set()
    for name in sorted(set(EXPECTED_SKILLS) - found):
        errors.append(f"missing skill: {name}")
    for name in sorted(found - set(EXPECTED_SKILLS)):
        errors.append(f"unexpected skill: {name}")
    for name in sorted(found):
        check_skill(skills / name, errors, root)
    check_named_markdown(root / "agents", EXPECTED_AGENTS, AGENT_SNIPPETS, errors, "agent", root)
    check_named_markdown(root / "playbooks", EXPECTED_PLAYBOOKS, PLAYBOOK_SNIPPETS, errors, "playbook", root)
    check_named_markdown(root / "workflows", EXPECTED_WORKFLOWS, WORKFLOW_SNIPPETS, errors, "workflow", root)
    check_workflows(root, errors)
    check_denylist(root, errors)
    check_adapters(root, errors)
    documents = [p for p in root.rglob("*.md") if not any(part.startswith(".") for part in p.relative_to(root).parts)]
    check_links(root, documents, errors)
    return errors


def check_installed(target: Path, errors: list[str]) -> None:
    manifest = target / ".agents/ai-sdlc-install.json"
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or data.get("format") != 1 or not isinstance(data.get("files"), list) or not data["files"]:
            raise ValueError("expected a format 1 inventory with nonempty files")
        seen: set[str] = set()
        for entry in data["files"]:
            if not isinstance(entry, dict) or not isinstance(entry.get("installed"), str) or not isinstance(entry.get("sha256"), str):
                raise ValueError("invalid inventory entry")
            rel = entry["installed"]
            if rel in seen:
                raise ValueError(f"duplicate inventory path: {rel}")
            seen.add(rel)
            path = (target / rel).resolve()
            if not path.is_relative_to(target) or not path.is_file():
                errors.append(f"installed pack: missing or unsafe inventory path {rel}")
                continue
            # Filled program facts and merged AGENTS rules are intentionally local.
            if rel == "AGENTS.md" or rel.startswith("context/"):
                continue
            if hashlib.sha256(path.read_bytes()).hexdigest() != entry["sha256"]:
                errors.append(f"installed pack: local drift needs review and inventory update: {rel}")
        for name in EXPECTED_SKILLS:
            folder = target / ".agents/skills" / name
            if not (folder / "SKILL.md").is_file():
                errors.append(f"installed pack: missing skill {name}")
            else:
                check_skill(folder, errors, target)
    except (OSError, ValueError) as exc:
        errors.append(f"installed pack: cannot validate inventory: {exc}")
        return
    skill_folders = [target / ".agents/skills" / name for name in EXPECTED_SKILLS]
    documents = [path for folder in skill_folders for path in folder.rglob("*.md")]
    policy_folders = list(skill_folders)
    navigation = (
        ("agents", EXPECTED_AGENTS, AGENT_SNIPPETS, "agent"),
        ("playbooks", EXPECTED_PLAYBOOKS, PLAYBOOK_SNIPPETS, "playbook"),
        ("workflows", EXPECTED_WORKFLOWS, WORKFLOW_SNIPPETS, "workflow"),
    )
    for name, expected, snippets, label in navigation:
        if not any(rel.startswith(name + "/") for rel in seen):
            continue  # Navigation is optional; do not claim unrelated product documents.
        folder = target / name
        check_named_markdown(folder, expected, snippets, errors, label, target, allow_extra=True)
        owned_files = [target / rel for rel in seen if rel.startswith(name + "/") and (target / rel).is_file()]
        policy_folders.extend(owned_files)
        documents.extend(path for path in owned_files if path.suffix == ".md")
        if name == "workflows":
            check_workflows(target, errors, [folder / f"{item}.md" for item in expected])
    check_denylist(target, errors, policy_folders)
    check_links(target, documents, errors)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--structure-only", action="store_true", help="structural checks only (used by validator regression tests)")
    parser.add_argument("--installed", type=Path, help="also check installed skill and navigation links in a product repo")
    args = parser.parse_args()
    errors = validate_pack(ROOT)
    if args.installed:
        target = args.installed.resolve()
        check_installed(target, errors)
    if not args.structure_only:
        run_check(ROOT / "scripts/check-evals.py", [], errors)
        run_check(ROOT / "scripts/test-check-pack.py", [], errors, timeout=120)
    if errors:
        print(f"check-pack: {len(errors)} failure(s)")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"check-pack: ok ({len(EXPECTED_SKILLS)} skills, {len(EXPECTED_AGENTS)} agents, "
          f"{len(EXPECTED_PLAYBOOKS)} playbooks, {len(EXPECTED_WORKFLOWS)} workflows, {len(EXPECTED_ADAPTERS)} adapters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
