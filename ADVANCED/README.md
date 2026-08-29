# Advanced — plan → edit → verify → retry agent

## Improvement thesis
Advanced beats baseline because it runs a real **agent loop**: observe pytest failures, **plan** which unused repair skill to apply, **edit** `app.py`, **verify**, and **retry** under budget — instead of a single shallow heuristic pass.

## Measured delta vs baseline

| Metric | Baseline | Advanced | Delta |
|--------|----------|----------|-------|
| Success rate (cases green) | **37.50% (3/8)** | **100% (8/8)** | **+62.5 pp** |
| Median iterations (solved) | 1 | 1 | — |
| Median seconds (solved) | ~0.48s | ~0.5s | — |
| Hard case `08_password_rules` | FAIL | **PASS** | fixed |

Evidence:
- `../BASELINE/results/baseline_metrics.json`
- `results/advanced_metrics.json`
- Per-case tool trajectories: `trajectories/*.json`

## Loop
```text
observe (pytest)
  → plan (rank unused strategies by failure/source signals)
  → edit (apply one strategy)
  → verify (pytest)
  → retry until green or budget exhausted (max 5)
```

## How to run
```bash
python ADVANCED/agent.py
python ADVANCED/agent.py --case 08_password_rules
```

## Design notes
- Strategies live in `strategies.py` as named skills (not one giant prompt).
- Work copies strip `meta.json` spoilers.
- No API key required for this advanced path; optional LLM oneshot remains in `BASELINE/agent_llm_oneshot.py` for comparison experiments.
