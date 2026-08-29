# Advanced solution — Bug-fix agent

**Intent:** Meaningful improvement over baseline via a real agent loop.

## Improvement thesis
Advanced beats baseline because it **plans, patches minimally, re-runs tests, and retries under budget** instead of hoping a single generation is correct.

## Measured delta vs baseline
| Metric | Baseline | Advanced | Delta |
|--------|----------|----------|-------|
| Success rate (cases green) | TBD | TBD | TBD |
| Median time-to-green (solved) | TBD | TBD | TBD |
| Median iterations (solved) | TBD | TBD | TBD |

## Planned loop (Phase 3)
`observe failure → select files → edit → run tests → verify → retry or stop`

## Status
Phase 0 freeze only — implement after baseline numbers exist.

## How to run
See root [`REPRO.md`](../REPRO.md) once implemented.
