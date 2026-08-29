# Baseline solution — Bug-fix agent

**Intent:** Fair, simple way to attempt fixes **before** the advanced edit–verify loop.

## Planned approach (Phase 2)
- Single-shot (or minimal) fix prompt given failing test output, **or**
- One-pass agent without a structured retry budget

## Metric
Same as root README: **eval-case success rate** (suite green), plus time-to-green / iterations when solved.

## Status
Phase 0 freeze only — implementation starts after Phase 1 sample apps exist.

## How to run
See root [`REPRO.md`](../REPRO.md) once implemented.
