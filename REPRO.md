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
# filled in Phase 2
```

**Expected output:** _(Phase 2)_

## Run advanced
```bash
# filled in Phase 3
```

**Expected output:** _(Phase 3)_

## Run evaluation / comparison
```bash
# filled when agents exist — same cases for baseline vs advanced
python sample_world/run_all.py --json
```

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
