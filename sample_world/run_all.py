#!/usr/bin/env python3
"""Run all eval cases and print a success-rate summary.

Usage:
  python sample_world/run_all.py
  python sample_world/run_all.py --json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from run_case import CASES_DIR, run_case


def list_cases() -> list[str]:
    return sorted(
        p.name for p in CASES_DIR.iterdir() if p.is_dir() and not p.name.startswith(".")
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Run all sample_world eval cases")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    results = [run_case(case_id) for case_id in list_cases()]
    passed = sum(1 for r in results if r["ok"])
    total = len(results)
    summary = {
        "passed": passed,
        "total": total,
        "success_rate": (passed / total) if total else 0.0,
        "results": [
            {"id": r["id"], "ok": r["ok"], "hard": r["hard"], "difficulty": r["difficulty"]}
            for r in results
        ],
    }

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(f"success_rate={summary['success_rate']:.2%} ({passed}/{total})")
        for r in summary["results"]:
            mark = "PASS" if r["ok"] else "FAIL"
            hard = " hard" if r["hard"] else ""
            print(f"  {r['id']}: {mark} ({r['difficulty']}{hard})")

    # For the broken sample world, expecting failures is normal until an agent fixes cases.
    raise SystemExit(0)


if __name__ == "__main__":
    main()
