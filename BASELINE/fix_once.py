#!/usr/bin/env python3
"""Baseline bug-fixer: ONE pass of shallow heuristics, then ONE retest.

This is intentionally weaker than the advanced agent loop (no planning,
no multi-step retries, no tool-using LLM). It matches the challenge PDF
example of a "simple script" baseline.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "sample_world" / "cases"
WORK = Path(__file__).resolve().parent / "work"
RESULTS = Path(__file__).resolve().parent / "results"


def list_cases() -> list[str]:
    return sorted(p.name for p in CASES.iterdir() if p.is_dir())


def run_pytest(case_dir: Path) -> tuple[bool, str]:
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", str(case_dir)],
        cwd=str(case_dir),
        capture_output=True,
        text=True,
    )
    out = (proc.stdout or "") + (proc.stderr or "")
    return proc.returncode == 0, out


def apply_one_heuristic(source: str) -> tuple[str, str | None]:
    """Apply at most one shallow rewrite. Order is fixed and incomplete on purpose."""

    # 1) classic off-by-one in while loops
    new, n = re.subn(r"while\s+(\w+)\s*<\s*(\w+)\s*:", r"while \1 <= \2:", source, count=1)
    if n:
        return new, "while_lt_to_le"

    # 2) sorted(..., reverse=True) -> ascending
    new, n = re.subn(
        r"sorted\((.+?),\s*reverse\s*=\s*True\)",
        r"sorted(\1)",
        source,
        count=1,
    )
    if n:
        return new, "sorted_remove_reverse"

    # 3) list.pop() -> pop(0) for queue-like FIFO attempts
    new, n = re.subn(r"self\._items\.pop\(\)", "self._items.pop(0)", source, count=1)
    if n:
        return new, "pop_to_pop0"

    # No more heuristics — leave harder bugs for the advanced agent.
    return source, None


def prepare_work_case(case_id: str) -> Path:
    src = CASES / case_id
    dst = WORK / case_id
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    # Agents/scripts should not lean on spoiler metadata during the fix attempt.
    meta = dst / "meta.json"
    if meta.exists():
        meta.unlink()
    return dst


def fix_case(case_id: str) -> dict:
    t0 = time.perf_counter()
    work = prepare_work_case(case_id)
    app_path = work / "app.py"
    original = app_path.read_text()

    ok_before, out_before = run_pytest(work)
    if ok_before:
        return {
            "id": case_id,
            "ok": True,
            "ok_before": True,
            "heuristic": None,
            "iterations": 0,
            "seconds": round(time.perf_counter() - t0, 3),
            "detail": "already green (unexpected for sample world)",
        }

    patched, heuristic = apply_one_heuristic(original)
    iterations = 0
    ok_after = False
    out_after = out_before

    if heuristic and patched != original:
        app_path.write_text(patched)
        iterations = 1
        ok_after, out_after = run_pytest(work)
    else:
        # Single pass exhausted with no applicable heuristic — give up.
        ok_after = False

    return {
        "id": case_id,
        "ok": ok_after,
        "ok_before": False,
        "heuristic": heuristic,
        "iterations": iterations,
        "seconds": round(time.perf_counter() - t0, 3),
        "detail": "fixed" if ok_after else "failed_after_one_pass",
        "pytest_tail": "\n".join(out_after.strip().splitlines()[-12:]),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Baseline one-pass heuristic fixer")
    parser.add_argument("--case", help="Run a single case id")
    parser.add_argument("--json-out", type=Path, default=RESULTS / "baseline_metrics.json")
    args = parser.parse_args()

    WORK.mkdir(parents=True, exist_ok=True)
    RESULTS.mkdir(parents=True, exist_ok=True)

    case_ids = [args.case] if args.case else list_cases()
    results = [fix_case(cid) for cid in case_ids]
    passed = sum(1 for r in results if r["ok"])
    total = len(results)
    solved = [r for r in results if r["ok"]]
    summary = {
        "approach": "baseline_one_pass_heuristics",
        "passed": passed,
        "total": total,
        "success_rate": round(passed / total, 4) if total else 0.0,
        "median_iterations_solved": (
            sorted(r["iterations"] for r in solved)[len(solved) // 2] if solved else None
        ),
        "median_seconds_solved": (
            sorted(r["seconds"] for r in solved)[len(solved) // 2] if solved else None
        ),
        "results": results,
    }

    args.json_out.write_text(json.dumps(summary, indent=2))
    print(
        f"baseline success_rate={summary['success_rate']:.2%} "
        f"({passed}/{total}) -> {args.json_out}"
    )
    for r in results:
        mark = "PASS" if r["ok"] else "FAIL"
        print(f"  {r['id']}: {mark} heuristic={r['heuristic']} iters={r['iterations']}")


if __name__ == "__main__":
    main()
