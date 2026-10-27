#!/usr/bin/env python3
"""Plan or perform an initial, non-overwriting install into a product repo."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

from pack_files import is_secret_filename

ROOT = Path(__file__).resolve().parents[1]


def reviewed_source() -> tuple[dict, set[str]]:
    """Only a clean Git checkout can supply the reviewed initial payload."""
    try:
        def git(*args: str) -> str:
            return subprocess.run(
                ["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=10, check=True,
            ).stdout
        if Path(git("rev-parse", "--show-toplevel").strip()).resolve() != ROOT:
            raise ValueError("the pack source must be its own Git checkout")
        revision = git("rev-parse", "HEAD").strip()
        if git("status", "--porcelain", "--untracked-files=all").strip():
            raise ValueError("source must be clean and pinned; review and commit source changes before installation")
        tracked = set(git("ls-tree", "-r", "--name-only", "-z", "HEAD").split("\0")) - {""}
    except (OSError, subprocess.TimeoutExpired, subprocess.CalledProcessError) as exc:
        raise ValueError("installation requires a clean, pinned Git source checkout") from exc
    return {"commit": revision, "dirty": False}, tracked


def plan(target: Path, navigation: bool, tracked: set[str]) -> tuple[list[tuple[Path, Path]], list[str]]:
    copies: list[tuple[Path, Path]] = []
    preserved: list[str] = []
    manifest = target / ".agents/ai-sdlc-install.json"
    paths = sorted(Path(rel) for rel in tracked)
    skill_names = {path.parts[1] for path in paths
                   if len(path.parts) == 3 and path.parts[0] == "skills" and path.name == "SKILL.md"}
    candidates = [(ROOT / "skills" / name, target / ".agents/skills" / name) for name in sorted(skill_names)]
    if navigation:
        candidates.extend((ROOT / folder, target / folder) for folder in ("agents", "playbooks", "workflows"))
    payload_roots = {}
    for source, dest in candidates:
        if dest.exists() or dest.is_symlink():
            raise ValueError(f"collision: {dest.relative_to(target)}; inspect and merge separately, do not overwrite")
        payload_roots[source.relative_to(ROOT)] = dest
    for path in paths:
        prefix = Path(*path.parts[:2]) if path.parts[0] == "skills" else Path(path.parts[0])
        if prefix in payload_roots:
            copies.append((ROOT / path, payload_roots[prefix] / path.relative_to(prefix)))
    for source in (ROOT / path for path in paths if path.parent == Path("context") and path.suffix == ".md"):
        dest = target / "context" / source.name
        if dest.exists() or dest.is_symlink():
            if not dest.is_file() or dest.is_symlink():
                raise ValueError(f"collision: {dest.relative_to(target)} is not a regular file")
            preserved.append(str(dest.relative_to(target)))
        else:
            copies.append((source, dest))
    agents = target / "AGENTS.md"
    if agents.exists() or agents.is_symlink():
        if not agents.is_file() or agents.is_symlink():
            raise ValueError("collision: AGENTS.md is not a regular file")
        preserved.append("AGENTS.md")
    else:
        copies.append((ROOT / "templates/consuming-AGENTS.md", agents))
    for source, _ in copies:
        if source.relative_to(ROOT).as_posix() not in tracked:
            raise ValueError(f"source file is not in the reviewed revision: {source.relative_to(ROOT)}")
        if is_secret_filename(source):
            raise ValueError(f"secret filename refused in payload: {source.relative_to(ROOT)}")
        if any(parent.is_symlink() for parent in (source, *source.parents) if parent.is_relative_to(ROOT)):
            raise ValueError(f"symlink source refused: {source.relative_to(ROOT)}")
        if not source.is_file() or not source.resolve().is_relative_to(ROOT):
            raise ValueError(f"source is missing, not a regular file, or escapes the pack: {source.relative_to(ROOT)}")
    destinations = [dest for _, dest in copies] + [manifest]
    for dest in destinations:
        if dest.exists() or dest.is_symlink():
            raise ValueError(f"collision: {dest.relative_to(target)}")
        for parent in (dest, *dest.parents):
            if parent == target:
                break
            if parent.is_symlink():
                raise ValueError(f"symlink destination refused: {parent.relative_to(target)}")
            if parent.exists() and not parent.is_dir():
                raise ValueError(f"destination parent is not a directory: {parent.relative_to(target)}")
    return copies, preserved


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("product", type=Path, help="existing product repository directory")
    parser.add_argument("--apply", action="store_true", help="copy after collision checks; default is a dry run")
    parser.add_argument("--navigation", action="store_true", help="also copy agent profiles, playbooks, and workflows")
    args = parser.parse_args()
    target = args.product.resolve()
    if not target.is_dir() or target == ROOT or ROOT.is_relative_to(target) or target.is_relative_to(ROOT):
        print("install-pack: choose an existing product directory outside the pack source", file=sys.stderr)
        return 1
    created: list[Path] = []
    try:
        provenance, tracked = reviewed_source()
        copies, preserved = plan(target, args.navigation, tracked)
        print(f"install-pack: {'apply' if args.apply else 'dry run'}; {len(copies)} files; preserve {len(preserved)} existing files")
        for item in preserved:
            print(f"  preserve: {item}; merge missing program-context and gate rules manually before the pilot")
        if not args.apply:
            print("No files written. Inspect the plan, then repeat with --apply.")
            return 0
        entries = []
        for source, dest in copies:
            dest.parent.mkdir(parents=True, exist_ok=True)
            # Exclusive creation refuses a collision even if a file appeared after planning.
            with dest.open("xb") as stream:
                created.append(dest)
                with source.open("rb") as incoming:
                    shutil.copyfileobj(incoming, stream)
            shutil.copymode(source, dest)
            entries.append({"source": source.relative_to(ROOT).as_posix(), "installed": dest.relative_to(target).as_posix(),
                            "sha256": hashlib.sha256(dest.read_bytes()).hexdigest()})
        manifest = target / ".agents/ai-sdlc-install.json"
        manifest.parent.mkdir(parents=True, exist_ok=True)
        with manifest.open("x", encoding="utf-8") as stream:
            created.append(manifest)
            json.dump({"format": 1, "source": provenance, "files": entries, "preserved": preserved}, stream, indent=2)
            stream.write("\n")
    except (OSError, ValueError) as exc:
        for path in reversed(created):
            path.unlink(missing_ok=True)
        print(f"install-pack: {exc}", file=sys.stderr)
        return 1
    print("Installed without overwrites. Fill context, resolve preserved-file merges, map host permissions, and run the pilot checklist in the source pack's docs/reference/pilot.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
