#!/usr/bin/env python3
"""Static evals: skill refuse language + labeled fixtures. Stdlib only."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "evals" / "cases.json"


def skill_body(name: str) -> str:
    path = ROOT / "skills" / name / "SKILL.md"
    if not path.is_file():
        raise FileNotFoundError(f"skills/{name}/SKILL.md")
    return path.read_text(encoding="utf-8")


def run_case(case: dict) -> str | None:
    cid = case.get("id", "?")
    kind = case.get("assert")
    needles = case.get("needles")
    if not isinstance(needles, list) or not needles or any(not isinstance(n, str) or not n for n in needles):
        return f"{cid}: needles must be a nonempty list of nonempty strings"
    if kind == "skill_contains":
        name = case.get("skill")
        if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            return f"{cid}: invalid skill"
        try:
            text = skill_body(name)
        except FileNotFoundError as exc:
            return f"{cid}: {exc}"
        fold = text.lower()
        for n in needles:
            if n.lower() not in fold:
                return f"{cid}: skills/{name}/SKILL.md missing {n!r}"
        return None
    if kind in {"file_contains", "file_lacks"}:
        rel = case.get("fixture")
        if not isinstance(rel, str):
            return f"{cid}: missing fixture"
        path = (ROOT / rel).resolve()
        if not path.is_relative_to((ROOT / "evals/fixtures").resolve()):
            return f"{cid}: fixture must stay under evals/fixtures"
        if not path.is_file():
            return f"{cid}: missing {rel}"
        text = path.read_text(encoding="utf-8")
        if kind == "file_contains":
            for n in needles:
                if n not in text:
                    return f"{cid}: {rel} missing {n!r}"
        else:
            for n in needles:
                if n in text:
                    return f"{cid}: {rel} should not contain {n!r}"
        return None
    return f"{cid}: unknown assert {kind!r}"


def main() -> int:
    if not CASES.is_file():
        print("evals/cases.json: missing", file=sys.stderr)
        return 1
    try:
        cases = json.loads(CASES.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"evals/cases.json: {exc}", file=sys.stderr)
        return 1
    if not isinstance(cases, list) or not cases:
        print("evals/cases.json: empty or not a list", file=sys.stderr)
        return 1
    errors = []
    seen = set()
    for case in cases:
        if not isinstance(case, dict):
            errors.append("non-object case")
            continue
        cid = case.get("id")
        if not isinstance(cid, str) or not cid or cid in seen:
            errors.append("case id must be a unique nonempty string")
            continue
        seen.add(cid)
        err = run_case(case)
        if err:
            errors.append(err)
    if errors:
        print(f"check-evals: {len(errors)} failure(s)")
        for err in errors:
            print(f"  - {err}")
        return 1
    print(f"check-evals: ok ({len(cases)} cases)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
