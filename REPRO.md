# Reproduction Guide

Written for a judge starting from a **clean machine**.

## Prerequisites
- OS: macOS / Linux / Windows (WSL OK)
- Python **3.9+**
- Git

## Clone
```bash
git clone https://github.com/Zaheer-Hassan/frontier-eng-2026.git
cd frontier-eng-2026
```

## Environment
```bash
python -m pip install -r sample_world/requirements.txt
# Later phases may add agent requirements — see BASELINE/ and ADVANCED/ when present
```

## Sample world (eval cases)
```bash
# all cases — expect ~0% success before agents fix them
python sample_world/run_all.py

# one case
python sample_world/run_case.py 01_sum_inclusive
```

**Expected (Phase 1, unbroken apps):** `success_rate=0%` (8/8 failing).

Case catalog: [`sample_world/EVAL_CASES.md`](./sample_world/EVAL_CASES.md)

## Run baseline
```bash
python BASELINE/fix_once.py
# optional LLM oneshot (needs API key in .env):
# python BASELINE/agent_llm_oneshot.py
```

**Expected output (heuristic baseline):**  
`baseline success_rate=37.50% (3/8)`  
Artifact: `BASELINE/results/baseline_metrics.json`

## Run advanced
```bash
python ADVANCED/agent.py
# single case:
# python ADVANCED/agent.py --case 08_password_rules
```

**Expected output:**  
`advanced success_rate=100.00% (8/8) delta_vs_baseline=+62.50%`  
Artifacts: `ADVANCED/results/advanced_metrics.json`, `ADVANCED/trajectories/*.json`

## Run evaluation / comparison
```bash
python BASELINE/fix_once.py
python ADVANCED/agent.py

# pristine world still red before fixes:
python sample_world/run_all.py
```

**Expected comparison:** baseline **37.5%** vs advanced **100%** on the same 8 cases.

## Data required
- Synthetic cases under `sample_world/cases/` only (no private data)

## Versions & approximate cost
| Item | Value |
|------|-------|
| Runtime (sample world suite) | < 5s typically |
| Runtime (baseline) | TBD Phase 2 |
| Runtime (advanced) | TBD Phase 3 |
| Approx agent / API cost | TBD |
| Key dependency versions | `pytest` per `sample_world/requirements.txt` |

## Notes
- Do not commit secrets / API keys
- Use `.env.example` → `.env` locally only
