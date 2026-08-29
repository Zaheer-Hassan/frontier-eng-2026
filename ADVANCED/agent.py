#!/usr/bin/env python3
"""Advanced bug-fix agent: plan → edit → test → verify → retry.

Tools:
  - read app.py
  - run pytest
  - apply a named repair strategy (edit)
  - record trajectory steps

Budget: MAX_RETRIES attempts per case (default 5).
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

from strategies import plan_next_strategy

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "sample_world" / "cases"
WORK = Path(__file__).resolve().parent / "work"
RESULTS = Path(__file__).resolve().parent / "results"
TRAJ_DIR = Path(__file__).resolve().parent / "trajectories"

MAX_RETRIES = 5


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


def prepare_work_case(case_id: str) -> Path:
    src = CASES / case_id
    dst = WORK / case_id
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    meta = dst / "meta.json"
    if meta.exists():
        meta.unlink()
    return dst


def fix_case(case_id: str, max_retries: int = MAX_RETRIES) -> dict:
    t0 = time.perf_counter()
    work = prepare_work_case(case_id)
    app_path = work / "app.py"
    trajectory: list[dict] = []
    tried: set[str] = set()

    ok, out = run_pytest(work)
    trajectory.append(
        {
            "step": 0,
            "action": "observe",
            "tool": "pytest",
            "ok": ok,
            "pytest_tail": "\n".join(out.strip().splitlines()[-8:]),
        }
    )
    if ok:
        result = {
            "id": case_id,
            "ok": True,
            "iterations": 0,
            "seconds": round(time.perf_counter() - t0, 3),
            "strategies_used": [],
            "trajectory": trajectory,
        }
        _write_traj(case_id, result)
        return result

    strategies_used: list[str] = []
    for attempt in range(1, max_retries + 1):
        source = app_path.read_text()
        strat = plan_next_strategy(source, out, tried)
        if strat is None:
            trajectory.append(
                {
                    "step": attempt,
                    "action": "plan",
                    "decision": "no_unused_applicable_strategy",
                    "tried": sorted(tried),
                }
            )
            break

        planned = {
            "step": attempt,
            "action": "plan",
            "strategy": strat.name,
            "rationale": "selected_by_signal_overlap_among_unused_strategies",
        }
        trajectory.append(planned)

        new_source = strat.apply(source)
        tried.add(strat.name)
        if new_source is None or new_source == source:
            trajectory.append(
                {
                    "step": attempt,
                    "action": "edit",
                    "strategy": strat.name,
                    "ok": False,
                    "detail": "strategy_noop",
                }
            )
            continue

        app_path.write_text(new_source)
        strategies_used.append(strat.name)
        trajectory.append(
            {
                "step": attempt,
                "action": "edit",
                "tool": "write:app.py",
                "strategy": strat.name,
                "ok": True,
            }
        )

        ok, out = run_pytest(work)
        trajectory.append(
            {
                "step": attempt,
                "action": "verify",
                "tool": "pytest",
                "ok": ok,
                "pytest_tail": "\n".join(out.strip().splitlines()[-8:]),
            }
        )
        if ok:
            result = {
                "id": case_id,
                "ok": True,
                "iterations": attempt,
                "seconds": round(time.perf_counter() - t0, 3),
                "strategies_used": strategies_used,
                "trajectory": trajectory,
            }
            _write_traj(case_id, result)
            return result

    result = {
        "id": case_id,
        "ok": False,
        "iterations": len(strategies_used),
        "seconds": round(time.perf_counter() - t0, 3),
        "strategies_used": strategies_used,
        "trajectory": trajectory,
        "detail": "budget_exhausted_or_no_strategy",
    }
    _write_traj(case_id, result)
    return result


def _write_traj(case_id: str, result: dict) -> None:
    TRAJ_DIR.mkdir(parents=True, exist_ok=True)
    path = TRAJ_DIR / f"{case_id}.json"
    path.write_text(json.dumps(result, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description="Advanced plan-edit-verify bugfix agent")
    parser.add_argument("--case", help="Single case id")
    parser.add_argument("--max-retries", type=int, default=MAX_RETRIES)
    parser.add_argument("--json-out", type=Path, default=RESULTS / "advanced_metrics.json")
    args = parser.parse_args()

    WORK.mkdir(parents=True, exist_ok=True)
    RESULTS.mkdir(parents=True, exist_ok=True)
    TRAJ_DIR.mkdir(parents=True, exist_ok=True)

    case_ids = [args.case] if args.case else list_cases()
    results = [fix_case(cid, max_retries=args.max_retries) for cid in case_ids]
    passed = sum(1 for r in results if r["ok"])
    total = len(results)
    solved = [r for r in results if r["ok"]]
    summary = {
        "approach": "advanced_plan_edit_verify_retry",
        "max_retries": args.max_retries,
        "passed": passed,
        "total": total,
        "success_rate": round(passed / total, 4) if total else 0.0,
        "median_iterations_solved": (
            sorted(r["iterations"] for r in solved)[len(solved) // 2] if solved else None
        ),
        "median_seconds_solved": (
            sorted(r["seconds"] for r in solved)[len(solved) // 2] if solved else None
        ),
        "baseline_success_rate": 0.375,
        "improvement_pp": round(((passed / total) if total else 0.0) - 0.375, 4),
        "results": [
            {
                "id": r["id"],
                "ok": r["ok"],
                "iterations": r["iterations"],
                "seconds": r["seconds"],
                "strategies_used": r.get("strategies_used", []),
            }
            for r in results
        ],
    }
    args.json_out.write_text(json.dumps(summary, indent=2))
    print(
        f"advanced success_rate={summary['success_rate']:.2%} ({passed}/{total}) "
        f"delta_vs_baseline={summary['improvement_pp']:+.2%} -> {args.json_out}"
    )
    for r in summary["results"]:
        mark = "PASS" if r["ok"] else "FAIL"
        print(
            f"  {r['id']}: {mark} iters={r['iterations']} strategies={r['strategies_used']}"
        )


if __name__ == "__main__":
    main()
