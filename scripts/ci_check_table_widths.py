#!/usr/bin/env python3
"""
Markdown table width validation for GitHub Actions CI.

Ensures all markdown tables fit within 1024px width (GitHub rendering limit).
Flags tables with > 7 columns (general heuristic for 1024px constraint).

Usage:
  python scripts/ci_check_table_widths.py
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple

# All markdown files to check
MARKDOWN_PATTERNS = [
    "README.md",
    "CONTRIBUTING.md",
    "CONTRIBUTORS.md",
    "NOTICE",
    "SUBMISSION_GUIDE.md",
    "docs/**/*.md",
    "**/CONTRIBUTING.md",
    "**/SKILL.md",
]

# Markdown table pattern: lines starting with |
TABLE_LINE_PATTERN = r'^\s*\|'

def find_table_headers(content: str) -> List[Tuple[int, int]]:
    """
    Find markdown table header row indices.
    Returns list of (start_line, column_count).
    """
    lines = content.split('\n')
    tables = []

    for i, line in enumerate(lines):
        if re.match(TABLE_LINE_PATTERN, line):
            # Check if this is a header (next line should be separator)
            if i + 1 < len(lines) and '---' in lines[i + 1]:
                # Count columns
                columns = len([x for x in line.split('|') if x.strip()])
                tables.append((i + 1, columns))  # Line number (1-indexed)

    return tables

def check_markdown_file(file_path: Path) -> List[Tuple[int, int]]:
    """
    Check a single markdown file.
    Returns list of (line_number, column_count) for wide tables.
    """
    try:
        with open(file_path, encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return []

    failures = []
    tables = find_table_headers(content)

    for line_num, col_count in tables:
        if col_count > 7:
            failures.append((line_num, col_count))

    return failures

def main():
    print("📊 Checking markdown table widths...")

    from glob import glob

    all_failures = {}

    # Collect all markdown files
    md_files = set()
    for pattern in MARKDOWN_PATTERNS:
        md_files.update(glob(pattern, recursive=True))

    # Filter to only markdown files
    md_files = [Path(f) for f in md_files if f.endswith(('.md', 'CONTRIBUTING', 'NOTICE', 'CONTRIBUTORS.md'))]

    for md_file in sorted(md_files):
        if not md_file.exists() or not md_file.is_file():
            continue

        failures = check_markdown_file(md_file)
        if failures:
            all_failures[str(md_file)] = failures

    if all_failures:
        print(f"\n⚠️  Found {sum(len(v) for v in all_failures.values())} wide table(s) (> 7 columns):\n")
        for file_path, failures in all_failures.items():
            print(f"  {file_path}")
            for line_num, col_count in failures:
                print(f"    Line {line_num}: {col_count} columns (max: 7 for 1024px GitHub rendering; Standard + Upgraded comparison uses 7 columns)")
        print("\n💡 Action: Split wide tables into narrower ones (≤7 columns) or use per-row format.")
        print("   Example: Instead of |A|B|C|D|E|F|, use two tables: |A|B|C|D| and |E|F|G|H|")
        sys.exit(1)
    else:
        print("✅ All table widths within limits (≤ 7 columns)")
        sys.exit(0)

if __name__ == "__main__":
    main()
