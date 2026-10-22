#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Summarize an explicit local action-list CSV without changing it."""

import argparse
import csv
import json
import sys
from pathlib import Path


REQUIRED_COLUMNS = {"action", "owner", "due_date"}


def summarize(path: Path) -> dict[str, int]:
    """Count actions and missing assignments; reject malformed CSV rows."""
    counts = {"actions": 0, "missing_owner": 0, "missing_due_date": 0}
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream, strict=True)
        if not REQUIRED_COLUMNS.issubset(reader.fieldnames or []):
            raise ValueError("CSV must include action, owner, and due_date columns")
        if len(reader.fieldnames) != len(set(reader.fieldnames)):
            raise ValueError("CSV contains duplicate column names")
        for row in reader:
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"Malformed CSV row ending at line {reader.line_num}")
            if not row["action"].strip():
                raise ValueError(f"Missing action at line {reader.line_num}")
            counts["actions"] += 1
            counts["missing_owner"] += row["owner"].strip().casefold() in {"", "unspecified"}
            counts["missing_due_date"] += row["due_date"].strip().casefold() in {"", "unspecified"}
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path, help="Explicit path to a readable UTF-8 CSV")
    args = parser.parse_args()
    try:
        counts = summarize(args.csv_path)
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        print(f"Invalid action list: {error}", file=sys.stderr)
        return 2
    print(json.dumps(counts, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
