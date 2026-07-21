#!/usr/bin/env python3
"""
PDS URL validation for GitHub Actions CI.

Scans all SKILL.md files for PDS URLs and validates HTTP status codes.
Flags any 404 / 410 / timeout errors for manual review.

Usage:
  python scripts/ci_check_pds_urls.py
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple
import requests
from urllib.parse import urlparse

# Skills directory
SKILLS = [
    "lubricant-recommender",
    "coolant-recommender",
    "diesel-recommender",
    "adblue-def-recommender",
    "grease-recommender",
]

# URL pattern: matches markdown links or inline URLs followed by (PDS DATE)
URL_PATTERN = r'https?://[^\s\)]+(?:\s*\(PDS\s+\d{2}\.\d{2}\.\d{4}\))?'

# URLs to skip (internal, no-check, etc.)
SKIP_PATTERNS = [
    "localhost",
    "127.0.0.1",
    "example.com",
]

def is_skippable(url: str) -> bool:
    """Check if URL should be skipped."""
    for pattern in SKIP_PATTERNS:
        if pattern in url:
            return True
    return False

def validate_url(url: str, timeout: int = 5) -> Tuple[int, str]:
    """Validate URL. Returns (status_code, status_text)."""
    try:
        resp = requests.head(url, timeout=timeout, allow_redirects=True)
        return resp.status_code, "OK" if resp.status_code == 200 else f"HTTP {resp.status_code}"
    except requests.exceptions.Timeout:
        return -1, "Timeout"
    except requests.exceptions.ConnectionError:
        return -2, "Connection error"
    except Exception as e:
        return -3, str(type(e).__name__)

def check_skill_file(skill_path: Path) -> List[Tuple[str, int, str]]:
    """
    Check a single SKILL.md file.
    Returns list of (url, status_code, status_text) for failed checks.
    """
    skill_file = skill_path / "SKILL.md"
    if not skill_file.exists():
        return []

    failures = []
    with open(skill_file, encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')

    for line_num, line in enumerate(lines, start=1):
        # Find all URLs in the line
        for match in re.finditer(URL_PATTERN, line):
            url = match.group(0).strip()

            # Remove trailing PDS date if present
            url = re.sub(r'\s*\(PDS.*?\)$', '', url).strip()

            # Skip internal/test URLs
            if is_skippable(url):
                continue

            status_code, status_text = validate_url(url)

            # Flag failures: 404, 410, timeout, connection error
            if status_code in [404, 410, -1, -2, -3]:
                failures.append((url, status_code, status_text))

    return failures

def main():
    print("🔗 Checking PDS URLs...")
    all_failures = {}

    for skill in SKILLS:
        skill_path = Path(skill)
        if not skill_path.exists():
            continue

        failures = check_skill_file(skill_path)
        if failures:
            all_failures[skill] = failures

    if all_failures:
        print(f"\n❌ Found {sum(len(v) for v in all_failures.values())} stale PDS URL(s):\n")
        for skill, failures in all_failures.items():
            print(f"  [{skill}]")
            for url, status_code, status_text in failures:
                status_emoji = "🚫" if status_code in [404, 410] else "⏱️"
                print(f"    {status_emoji} {url}")
                print(f"       → {status_text}")
        print("\n💡 Action: Update stale URLs or verify producers haven't relocated their PDS.")
        sys.exit(1)
    else:
        print("✅ All PDS URLs valid (or skipped)")
        sys.exit(0)

if __name__ == "__main__":
    main()
