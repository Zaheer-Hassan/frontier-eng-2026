# Baseline — one-pass heuristic fixer

## Approach
Fair **simple script** baseline (allowed by the official PDF):

1. Copy case into `BASELINE/work/<id>/` (strip `meta.json` spoilers)
2. Run pytest
3. Apply **at most one** shallow text heuristic
4. Retest **once**
5. Stop — no planning, no retry budget, no LLM tools

Optional stronger-but-still-baseline path: `agent_llm_oneshot.py` (single LLM call, no retries) when an API key is present.

## Primary results (recorded)

| Metric | Value |
|--------|-------|
| Approach | `baseline_one_pass_heuristics` |
| **Success rate** | **37.50% (3/8)** |
| Solved | `01_sum_inclusive`, `06_queue_fifo`, `07_merge_sorted` |
| Failed | `02`, `03`, `04`, `05`, `08` (incl. hard password case) |
| Median iterations (solved) | 1 |
| Evidence | `results/baseline_metrics.json` |

Command:

```bash
python BASELINE/fix_once.py
```

## Optional LLM one-shot

```bash
cp .env.example .env   # add OPENROUTER_API_KEY or OPENAI_API_KEY or XAI_API_KEY
python BASELINE/agent_llm_oneshot.py
```

## Why this is a fair baseline
It represents a brittle automator a junior might ship on day one: a few regex rewrites and hope. It cannot handle semantic bugs (discount math, slug policy, password rules, ordered dedupe, word reverse).
