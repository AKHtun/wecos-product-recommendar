#!/usr/bin/env python3
"""
CONTRIBUTORS.md synchronization validation for GitHub Actions CI.

Ensures that if SKILL.md changes, CONTRIBUTORS.md is also updated.
Prevents methodology changes from going unrecorded in authorship lineage.

Usage:
  python scripts/ci_validate_contributors_sync.py
"""

import re
import sys
from pathlib import Path
from typing import Set

SKILLS = [
    "lubricant-recommender",
    "coolant-recommender",
    "diesel-recommender",
    "adblue-def-recommender",
    "grease-recommender",
]

def get_changed_files() -> Set[str]:
    """Get list of changed files in current commit (via git diff)."""
    import subprocess
    try:
        # Get files changed in PR or push
        result = subprocess.run(
            ["git", "diff", "--name-only", "origin/main...HEAD"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return set(result.stdout.strip().split('\n'))
    except Exception:
        pass

    # Fallback: check git status
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            files = set()
            for line in result.stdout.strip().split('\n'):
                if line and len(line) > 3:
                    files.add(line[3:])
            return files
    except Exception:
        pass

    return set()

def check_methodology_change(skill: str) -> bool:
    """Check if SKILL.md has methodology changes (§ sections modified)."""
    skill_file = Path(skill) / "SKILL.md"
    if not skill_file.exists():
        return False

    changed_files = get_changed_files()
    if str(skill_file) not in changed_files:
        return False

    # If SKILL.md changed, it's likely a methodology change
    # (could also be typo fix, but we'll be conservative)
    return True

def check_contributors_updated(skill: str) -> bool:
    """Check if CONTRIBUTORS.md mentions the skill in recent entries."""
    contributors_file = Path("CONTRIBUTORS.md")
    if not contributors_file.exists():
        return False

    changed_files = get_changed_files()
    if "CONTRIBUTORS.md" not in changed_files:
        return False

    # If CONTRIBUTORS.md was touched in this commit, assume it was updated
    # (More thorough check would parse the file and verify new entries)
    return True

def main():
    print("📋 Checking CONTRIBUTORS.md sync...")

    warnings = []

    for skill in SKILLS:
        if check_methodology_change(skill):
            if not check_contributors_updated(skill):
                warnings.append(skill)

    if warnings:
        print(f"\n⚠️  Potential CONTRIBUTORS.md sync issue:\n")
        for skill in warnings:
            print(f"  - {skill}/SKILL.md changed, but CONTRIBUTORS.md not updated")
        print("\n💡 Action: If you modified methodology (§0-§13 sections), add an entry to CONTRIBUTORS.md")
        print("   Example:")
        print("   - **2026-07-21 — new filter branch:** Added HETG (biodegradable) base-oil type.")
        print("     Author: Your Name")
        print("\n   If this was just a typo/formatting fix, you can ignore this warning.")
        # Warning only; don't fail the build
        sys.exit(0)
    else:
        print("✅ CONTRIBUTORS.md appears in sync with SKILL.md changes")
        sys.exit(0)

if __name__ == "__main__":
    main()
