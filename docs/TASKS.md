# Task list — Problem #2: Bug-fix / PR agent

**Owner:** Grok (build) · **Zaheer:** approvals, API keys, video record, HackerEarth submit  
**Chosen problem:** Agent that takes a small broken app, sees failing tests/errors, patches, re-runs until green (baseline vs advanced).

---

## Phase 0 — Freeze
1. [x] Problem statement lock (user, bottleneck, value) in README
2. [x] Scope: one small broken sample app (not a huge monorepo)
3. [x] Primary metric lock (eval-case success rate = suite green; plus time-to-green / iterations)
4. [x] Kickoff senior trace (`traces/2026-08-29_1400_kickoff-phase0-freeze.md`)
5. [x] Official PDF archived at `docs/problem-statement.pdf`

## Phase 1 — Sample world (broken apps + eval cases)
5. [x] Create tiny buggy modules + tests (`sample_world/cases/*`)
6. [x] Define 8 eval cases (includes hard `08_password_rules`)
7. [x] Document run commands (`EVAL_CASES.md`, `run_case.py`, `run_all.py`, `REPRO.md`)
8. [x] Synthetic/public only — no private secrets
9. [x] Verified pre-agent `success_rate=0.00%` (0/8)

## Phase 2 — Baseline
9. [x] Baseline approach: one-pass heuristic script (+ optional LLM oneshot)
10. [x] Run baseline on all eval cases → **37.50% (3/8)**
11. [x] Record baseline metrics (`BASELINE/results/baseline_metrics.json`)
12. [x] `BASELINE/` code + README + changelog + trajectory
13. [x] Commit + push (senior message)


## Phase 3 — Advanced agent
14. [ ] Advanced design: plan → edit → run tests → verify → retry budget
15. [ ] Implement agent (Python recommended) + tools (read/edit/shell/test)
16. [ ] Human checkpoint / sandbox rules where needed
17. [ ] Run advanced on same eval cases
18. [ ] Metric table: baseline vs advanced (measurable delta)
19. [ ] `ADVANCED/` + changelog + trajectories (incl. one failed experiment)
20. [ ] Commit + push

## Phase 4 — Proof pack
21. [ ] Complete `REPRO.md` (clean machine: baseline + advanced + eval)
22. [ ] README write-up: approach, failures, hot take
23. [ ] Trajectory audit (senior standard)
24. [ ] Video script ≤5 min; Zaheer records
25. [ ] Secrets check; public/private repo ready for judges

## Phase 5 — Submit
26. [ ] Final pack checklist
27. [ ] HackerEarth **Start submission** (Zaheer)
28. [ ] Buffer fixes before deadline (31 Aug 18:00 UTC / 11:00 PM PKT)

---

## Non-goals
- Full production IDE product
- Training models
- Huge multi-repo enterprise simulator
