#!/usr/bin/env python3
"""Optional baseline: single LLM call (no retries).

Requires one of:
  OPENROUTER_API_KEY, OPENAI_API_KEY, XAI_API_KEY

Usage:
  python BASELINE/agent_llm_oneshot.py --case 01_sum_inclusive
  python BASELINE/agent_llm_oneshot.py   # all cases
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "sample_world" / "cases"
WORK = Path(__file__).resolve().parent / "work"
RESULTS = Path(__file__).resolve().parent / "results"


def load_dotenv() -> None:
    env_path = ROOT / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def llm_config() -> tuple[str, str, str]:
    if os.environ.get("OPENROUTER_API_KEY"):
        return (
            "https://openrouter.ai/api/v1/chat/completions",
            os.environ["OPENROUTER_API_KEY"],
            os.environ.get("BASELINE_MODEL", "openai/gpt-4o-mini"),
        )
    if os.environ.get("OPENAI_API_KEY"):
        return (
            "https://api.openai.com/v1/chat/completions",
            os.environ["OPENAI_API_KEY"],
            os.environ.get("BASELINE_MODEL", "gpt-4o-mini"),
        )
    if os.environ.get("XAI_API_KEY"):
        return (
            "https://api.x.ai/v1/chat/completions",
            os.environ["XAI_API_KEY"],
            os.environ.get("BASELINE_MODEL", "grok-2-latest"),
        )
    raise SystemExit(
        "No API key found. Set OPENROUTER_API_KEY or OPENAI_API_KEY or XAI_API_KEY in .env"
    )


def chat(prompt: str) -> str:
    url, key, model = llm_config()
    body = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You fix Python bugs. Return ONLY the full fixed app.py source. No markdown.",
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode(),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        payload = json.loads(resp.read().decode())
    content = payload["choices"][0]["message"]["content"]
    content = content.strip()
    if content.startswith("```"):
        content = re.sub(r"^```(?:python)?\n?", "", content)
        content = re.sub(r"\n?```$", "", content)
    return content


def run_pytest(case_dir: Path) -> tuple[bool, str]:
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", str(case_dir)],
        cwd=str(case_dir),
        capture_output=True,
        text=True,
    )
    return proc.returncode == 0, (proc.stdout or "") + (proc.stderr or "")


def prepare(case_id: str) -> Path:
    src = CASES / case_id
    dst = WORK / case_id
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    meta = dst / "meta.json"
    if meta.exists():
        meta.unlink()
    return dst


def fix_case(case_id: str) -> dict:
    t0 = time.perf_counter()
    work = prepare(case_id)
    app_path = work / "app.py"
    tests = (work / "test_app.py").read_text()
    source = app_path.read_text()
    ok_before, out_before = run_pytest(work)
    if ok_before:
        return {"id": case_id, "ok": True, "iterations": 0, "seconds": round(time.perf_counter() - t0, 3)}

    prompt = (
        "Fix app.py so tests pass. Return only Python source for app.py.\n\n"
        f"### app.py\n{source}\n\n### test_app.py\n{tests}\n\n"
        f"### pytest output\n{out_before}\n"
    )
    try:
        fixed = chat(prompt)
        app_path.write_text(fixed)
        ok_after, out_after = run_pytest(work)
        return {
            "id": case_id,
            "ok": ok_after,
            "iterations": 1,
            "seconds": round(time.perf_counter() - t0, 3),
            "detail": "llm_oneshot",
            "pytest_tail": "\n".join(out_after.strip().splitlines()[-8:]),
        }
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, KeyError) as exc:
        return {
            "id": case_id,
            "ok": False,
            "iterations": 0,
            "seconds": round(time.perf_counter() - t0, 3),
            "detail": f"llm_error:{type(exc).__name__}",
        }


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("--case")
    parser.add_argument("--json-out", type=Path, default=RESULTS / "baseline_llm_metrics.json")
    args = parser.parse_args()
    WORK.mkdir(parents=True, exist_ok=True)
    RESULTS.mkdir(parents=True, exist_ok=True)
    case_ids = [args.case] if args.case else sorted(p.name for p in CASES.iterdir() if p.is_dir())
    results = [fix_case(cid) for cid in case_ids]
    passed = sum(1 for r in results if r["ok"])
    total = len(results)
    summary = {
        "approach": "baseline_llm_oneshot",
        "passed": passed,
        "total": total,
        "success_rate": round(passed / total, 4) if total else 0.0,
        "results": results,
    }
    args.json_out.write_text(json.dumps(summary, indent=2))
    print(f"llm baseline success_rate={summary['success_rate']:.2%} ({passed}/{total})")
    for r in results:
        print(f"  {r['id']}: {'PASS' if r['ok'] else 'FAIL'}")


if __name__ == "__main__":
    main()
