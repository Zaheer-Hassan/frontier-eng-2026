# Reproduction Guide

Written for a judge starting from a **clean machine**.

## Prerequisites
| Item | Version / note |
|------|----------------|
| OS | macOS / Linux / Windows (WSL OK) |
| Python | **3.9+** (developed on 3.9.6) |
| Git | any recent |
| Network | not required for baseline/advanced heuristic agents |

## Clone
```bash
git clone https://github.com/Zaheer-Hassan/frontier-eng-2026.git
cd frontier-eng-2026
```

## Environment
```bash
python -m pip install -r sample_world/requirements.txt
# pins: pytest>=7,<9  (verified with pytest 8.4.2)
```

Optional LLM oneshot baseline only:
```bash
cp .env.example .env
# set OPENROUTER_API_KEY or OPENAI_API_KEY or XAI_API_KEY
# never commit .env
```

## 1) Pristine sample world (before fixes)
```bash
python sample_world/run_all.py
```
**Expected:** `success_rate=0.00% (0/8)`  
Catalog: [`sample_world/EVAL_CASES.md`](./sample_world/EVAL_CASES.md)

One case:
```bash
python sample_world/run_case.py 01_sum_inclusive
# exit code 1, pytest failures
```

## 2) Baseline
```bash
python BASELINE/fix_once.py
```
**Expected:** `baseline success_rate=37.50% (3/8)`  
**Solved:** `01_sum_inclusive`, `06_queue_fifo`, `07_merge_sorted`  
**Artifact:** `BASELINE/results/baseline_metrics.json`  
**Runtime:** ~2–4 seconds total on a laptop

Optional:
```bash
python BASELINE/agent_llm_oneshot.py
```

## 3) Advanced
```bash
python ADVANCED/agent.py
```
**Expected:** `advanced success_rate=100.00% (8/8) delta_vs_baseline=+62.50%`  
**Artifacts:**
- `ADVANCED/results/advanced_metrics.json`
- `ADVANCED/trajectories/<case_id>.json` (tool-level steps)

**Runtime:** ~4–8 seconds total  
**Approx API cost:** **$0** for the primary advanced path (no cloud LLM required)

## 4) Side-by-side comparison (same cases)
```bash
python BASELINE/fix_once.py
python ADVANCED/agent.py
```

| Stage | Success rate |
|-------|----------------|
| Pristine world | 0% (0/8) |
| Baseline | 37.5% (3/8) |
| Advanced | **100% (8/8)** |

## Data required
Synthetic only: `sample_world/cases/*/app.py` + `test_app.py`.  
No private datasets. Work copies are created under `BASELINE/work/` and `ADVANCED/work/` (gitignored).

## Notes for judges
- Primary metric = eval-case success rate (full pytest suite green).
- `meta.json` spoilers are stripped from work copies during agent runs.
- Do not commit secrets; `.env` is local-only.
