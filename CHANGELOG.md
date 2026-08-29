# Improvement Changelog

Every meaningful iteration goes here, linked to evidence (tests, metrics, traces).

---

## Template (copy per entry)

### [YYYY-MM-DD HH:MM PKT] — Entry title
- **From → To:** baseline state → new state
- **Why:** what evidence triggered this change
- **Change:** what we actually did
- **Evidence:** test output / metric / screenshot / trace file
- **Result:** pass/fail + measured delta
- **Next:** what we try next (or stop)

---

## Entries

### [2026-08-29] — Phase 2: baseline one-pass fixer @ 37.5%
- **From → To:** 0% pre-agent world → baseline success_rate 37.5% (3/8)
- **Why:** need a fair weak reference before building the advanced retry agent
- **Change:** `BASELINE/fix_once.py`, optional `agent_llm_oneshot.py`, metrics JSON, README/REPRO
- **Evidence:** `BASELINE/results/baseline_metrics.json`; `traces/2026-08-29_1430_phase2-baseline.md`
- **Result:** Solved 01/06/07 via shallow heuristics; semantic bugs remain failing
- **Next:** Phase 3 advanced agent with plan/edit/test/retry to beat 37.5%

### [2026-08-29] — Phase 1: sample world + 8 eval cases
- **From → To:** no eval world → 8 failing synthetic cases + harness
- **Why:** need a fixed case set to measure baseline vs advanced success rate
- **Change:** added `sample_world/` cases, `run_case.py`, `run_all.py`, EVAL docs; fixed accidental dedupe PASS
- **Evidence:** `python sample_world/run_all.py` → `success_rate=0.00% (0/8)`; `traces/2026-08-29_1410_phase1-sample-world.md`
- **Result:** Phase 1 complete — ready for Phase 2 baseline agent
- **Next:** implement baseline fixer and score on the same 8 cases

### [2026-08-29] — Phase 0: freeze Problem #2 (bug-fix agent)
- **From → To:** open problem choice → locked bug-fix / PR agent scope
- **Why:** need a falsifiable user bottleneck and comparable metric before building sample apps
- **Change:** README rewrite; primary metric = eval-case success rate (tests green); PDF copied to `docs/problem-statement.pdf`; kickoff trace
- **Evidence:** `traces/2026-08-29_1400_kickoff-phase0-freeze.md`, `README.md`
- **Result:** Phase 0 complete — ready for Phase 1 sample world
- **Next:** build tiny broken app + pytest + 5–10 eval cases

### [2026-08-28] — Remove practice-only traces
- **From → To:** practice traces present → cleaned
- **Why:** those files were format drills, not submission evidence
- **Change:** deleted `2026-08-28_practice-trace-format.md` and `2026-08-28_pre-kickoff-setup.md`; refreshed traces index
- **Evidence:** `traces/` now has `_TEMPLATE.md` + ownership lock trace only
- **Result:** cleaner trajectory folder for kickoff
- **Next:** first real problem trace at PDF drop

### [2026-08-28] — Senior trajectory ownership
- **From → To:** ad-hoc traces → senior SOP owned by Grok
- **Why:** submission traces must signal deliberate engineering judgment
- **Change:** `docs/TRAJECTORY_STANDARD.md`, upgraded `traces/_TEMPLATE.md`, `docs/SESSION_CARD.md`, index + ownership trace
- **Evidence:** `traces/2026-08-28_trajectory-standard-lock.md`
- **Result:** cadence locked — Zaheer says `trace close karo`, Grok delivers submission-ready traces
- **Next:** apply standard on kickoff PDF session

### [2026-08-28] — Prep pack: traces + stubs + kickoff plan
- **From → To:** basic scaffold → submission-ready templates
- **Why:** PDF not out yet; reduce friction on kickoff night
- **Change:** added `traces/_TEMPLATE.md`, practice trace, `.env.example`, `BASELINE/README.md`, `ADVANCED/README.md`, `docs/KICKOFF.md`
- **Evidence:** files in repo; practice trace documents the session
- **Result:** format locked for trajectories + night-of checklist ready
- **Next:** wait for problem PDF → follow `docs/KICKOFF.md`

### [2026-08-28] — Repo scaffold (pre-kickoff)
- **From → To:** empty → war-room folder structure
- **Why:** prepare for PDF release without revealing problem work early
- **Change:** created README, CHANGELOG, REPRO, BASELINE/, ADVANCED/, traces/, video/
- **Evidence:** repo tree
- **Result:** ready for kickoff
- **Next:** wait for problem PDF → define baseline scope
