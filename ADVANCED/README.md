# Advanced solution — Bug-fix agent

**Intent:** Meaningful improvement over baseline via a real agent loop.

## Improvement thesis
Advanced beats baseline because it **plans, patches minimally, re-runs tests, and retries under budget** instead of hoping a single generation is correct.

## Measured delta vs baseline
| Metric | Baseline | Advanced | Delta |
|--------|----------|----------|-------|
| Success rate (cases green) | **37.50% (3/8)** | TBD Phase 3 | TBD |
| Median time-to-green (solved) | ~0.48s | TBD | TBD |
| Median iterations (solved) | 1 | TBD | TBD |

## Planned loop (Phase 3)
`observe failure → select files → edit → run tests → verify → retry or stop`

## Status
Phase 0 freeze only — implement after baseline numbers exist.

## How to run
See root [`REPRO.md`](../REPRO.md) once implemented.
