# Eval cases — Phase 1

Primary metric: **success rate** = fraction of cases whose pytest suite is green.

All cases are synthetic teaching bugs. Agents should fix `app.py` so `test_app.py` passes.  
`meta.json` is for humans/harness — do not treat it as a spoiler the agent must read (optional).

| ID | Title | Difficulty | Hard? | Intentional bug (spoiler) |
|----|-------|------------|-------|---------------------------|
| `01_sum_inclusive` | Inclusive range sum | easy | no | Off-by-one (`< high`) |
| `02_word_reverse` | Reverse word order | easy | no | Reverses characters |
| `03_discount` | Percent discount | easy | no | Subtracts percent points |
| `04_dedupe_order` | Dedupe preserve order | easy | no | `set()` loses order |
| `05_slugify` | URL slugify | medium | no | Missing lowercase / normalization |
| `06_queue_fifo` | FIFO queue | medium | no | `pop()` is LIFO |
| `07_merge_sorted` | Merge sorted lists | medium | no | Sorts descending |
| `08_password_rules` | Password policy | hard | **yes** | Symbol rule broken / ignored |

## How to run one case

```bash
cd /Users/zaheer/Projects/frontier-eng-2026
python -m pip install -r sample_world/requirements.txt
python sample_world/run_case.py 01_sum_inclusive
```

Or manually:

```bash
cd sample_world/cases/01_sum_inclusive
python -m pytest -q
```

## How to run all cases (scoreboard)

```bash
python sample_world/run_all.py
python sample_world/run_all.py --json
```

## Expected Phase 1 baseline of the world

Before any agent fixes: **success_rate ≈ 0%** (all intentionally failing).
