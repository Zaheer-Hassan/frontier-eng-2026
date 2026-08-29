#!/usr/bin/env python3
"""Run pytest for a single eval case directory.

Usage:
  python sample_world/run_case.py 01_sum_inclusive
  python sample_world/run_case.py 01_sum_inclusive --json
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

CASES_DIR = Path(__file__).resolve().parent / "cases"


def run_case(case_id: str) -> dict:
    case_dir = CASES_DIR / case_id
    if not case_dir.is_dir():
        raise SystemExit(f"Unknown case: {case_id} (expected under {CASES_DIR})")

    meta_path = case_dir / "meta.json"
    meta = json.loads(meta_path.read_text()) if meta_path.exists() else {"id": case_id}

    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", str(case_dir)],
        cwd=str(case_dir),
        capture_output=True,
        text=True,
    )
    return {
        "id": case_id,
        "ok": proc.returncode == 0,
        "returncode": proc.returncode,
        "difficulty": meta.get("difficulty"),
        "hard": bool(meta.get("hard", False)),
        "stdout": proc.stdout,
        "stderr": proc.stderr,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run one sample_world eval case")
    parser.add_argument("case_id", help="e.g. 01_sum_inclusive")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    args = parser.parse_args()

    result = run_case(args.case_id)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        status = "PASS" if result["ok"] else "FAIL"
        print(f"{result['id']}: {status}")
        if result["stdout"].strip():
            print(result["stdout"])
        if result["stderr"].strip():
            print(result["stderr"], file=sys.stderr)
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
