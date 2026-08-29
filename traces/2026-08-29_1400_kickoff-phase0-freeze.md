# Trace — kickoff: Phase 0 problem freeze (#2 bug-fix agent)

| Field | Value |
|-------|--------|
| **ID** | `2026-08-29_1400_kickoff-phase0-freeze` |
| **When (PKT)** | 2026-08-29 ~14:00 |
| **Duration** | ~25 min |
| **Agent(s)** | Grok (xAI) |
| **Human** | Zaheer ul Hassan |
| **Phase** | kickoff |
| **Related changelog** | `[2026-08-29] — Phase 0: freeze Problem #2` |
| **Status** | submission-ready |

---

## 0) System state before this session
- Repo had war-room scaffold, trajectory SOP, commit style, generic TASKS
- Official PDF confirmed as open-ended Agentic Workflows instructions (no Tetris starter pack)
- Zaheer selected **Problem #2** (bug-fix / PR agent) and ordered Phase 0 start

## 1) Session goal (falsifiable)
**Done means:** README states user/bottleneck/value; scope frozen; primary metric frozen; kickoff trace written; PDF stored under `docs/`; Phase 0 tasks marked done in TASKS.

## 2) Constraints
- Must align with official PDF deliverables (baseline, advanced, changelog, repro, video, trajectories)
- 3-day deadline — scope must stay tiny
- No fake “fixed official starter”; we own the sample broken app in Phase 1
- API keys remain local only

## 3) Plan (before coding)
1. Copy PDF into repo for audit trail
2. Rewrite README for Problem #2
3. Freeze metric + in/out scope
4. Update TASKS Phase 0 checkboxes
5. Write this kickoff trace + changelog
6. Commit/push with senior message

## 4) Agent brief (prompt issued)
```
Start Phase 0
```
Plus prior lock: Problem #2, phase-by-phase push, trajectories alongside.

**Why this brief:** Kickoff must freeze the problem before any sample-app implementation drift.

## 5) Execution log
| Step | Actor | Action | Result |
|------|-------|--------|--------|
| 1 | agent | Copy PDF → `docs/problem-statement.pdf` | ok |
| 2 | agent | Rewrite root README for bug-fix agent | ok |
| 3 | agent | Freeze primary metric: eval-case success rate (tests green) | ok |
| 4 | agent | Update `docs/TASKS.md` Phase 0 status | ok |
| 5 | agent | Write kickoff trajectory + changelog entry | ok |
| 6 | agent | Commit + push (Zaheer-Hassan) | pending end of session |

**Files touched:**
- `docs/problem-statement.pdf` — official instructions archive
- `README.md` — problem framing + metric
- `docs/TASKS.md` — Phase 0 progress
- `CHANGELOG.md` — Phase 0 entry
- `traces/2026-08-29_1400_kickoff-phase0-freeze.md` — this file
- `traces/README.md` — index update

## 6) Verification
- [x] User / bottleneck / value present in README
- [x] In-scope / out-of-scope table present
- [x] Primary metric named and comparable for baseline vs advanced
- [x] PDF present in `docs/`

**Evidence:** file contents in repo after this session.

## 7) Decision record
| Decision | Chose | Rejected | Why |
|----------|-------|----------|-----|
| Problem | #2 bug-fix agent | #1 repo valuation, #3 hiring | Best engineering + metric fit for Zaheer + rubric “Agent Solution & Engineering” |
| Primary metric | Success rate (suite green per case) | Only latency or only LOC changed | Matches user goal: “make it pass” |
| Sample strategy | Build tiny broken apps in Phase 1 | Wait for missing official starter zip | Instructions PDF has no starter pack; waiting blocks the sprint |
| Baseline shape (preview) | Single-shot or minimal loop | Full advanced loop as baseline | Need a fair weak-but-real baseline for measured improvement |

**Tradeoff accepted:** We spend Phase 1 building the eval world ourselves.  
**Revisit if:** Organizer publishes a mandatory starter that conflicts — then rebase sample apps.

## 8) Failure / incident
None in Phase 0. Prior confusion (expecting Tetris workspace) resolved by PDF text + HackerEarth page: open-ended problem choice.

## 9) Risk still open
- Eval cases must be hard enough that single-shot baseline fails often — otherwise improvement looks weak
- API cost/budget for agent runs still on Zaheer’s keys
- Scope creep if sample app grows past “tiny”

## 10) Handoff
**Next session starts with:** Phase 1 — create the first tiny broken app + pytest suite and draft the eval-case list (5–10 cases, one hard).

---

### Quality gate
- [x] Goal clear and checked
- [x] Prompt preserved
- [x] Actions + evidence present
- [x] Real decisions/tradeoffs
- [x] Honest about prior confusion
- [x] Handoff actionable
- [x] No secrets
