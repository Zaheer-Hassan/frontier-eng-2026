# Trace — baseline-prep: Phase 1 sample world + eval harness

| Field | Value |
|-------|--------|
| **ID** | `2026-08-29_1410_phase1-sample-world` |
| **When (PKT)** | 2026-08-29 |
| **Duration** | ~40 min |
| **Agent(s)** | Grok (xAI) |
| **Human** | Zaheer ul Hassan |
| **Phase** | kickoff / sample-world (Phase 1) |
| **Related changelog** | `[2026-08-29] — Phase 1: sample world + 8 eval cases` |
| **Status** | submission-ready |

---

## 0) System state before this session
- Phase 0 frozen Problem #2 + primary metric (eval-case success rate)
- No official starter pack from HackerEarth — must own synthetic bugs
- Empty `sample_world` not yet created

## 1) Session goal (falsifiable)
**Done means:** ≥5 eval cases (target 8) each with failing tests; harness `run_case` / `run_all`; docs; measured pre-agent success_rate = 0%.

## 2) Constraints
- Synthetic only; no private data
- Keep apps tiny so 3-day agent work stays feasible
- Include ≥1 hard case
- meta.json may document spoilers for humans — agents should rely on tests

## 3) Plan (before coding)
1. Create 8 case directories with buggy `app.py` + `test_app.py` + `meta.json`
2. Add pytest harness scripts
3. Run suite; force any accidental PASS to FAIL
4. Document EVAL_CASES + REPRO updates
5. Trace + changelog + push

## 4) Agent brief (prompt issued)
```
Start Phase 1
```

**Why this brief:** Build the measurable world before baseline/advanced agents.

## 5) Execution log
| Step | Actor | Action | Result |
|------|-------|--------|--------|
| 1 | agent | Create 8 case scaffolds | ok |
| 2 | agent | Implement intentional bugs + tests | ok |
| 3 | agent | Add `run_case.py` / `run_all.py` + requirements | ok |
| 4 | agent | First `run_all` showed 1/8 PASS on dedupe | fail accidental |
| 5 | agent | Change dedupe bug to `sorted(set(...))` | ok |
| 6 | agent | Re-run `run_all` → 0/8 | ok |

**Commands / checks run:**
```bash
python3 -m pip install -r sample_world/requirements.txt
python3 sample_world/run_all.py
# → success_rate=0.00% (0/8)
```

**Files touched:** `sample_world/**`, `REPRO.md`, `docs/TASKS.md`, `CHANGELOG.md`, traces index

## 6) Verification
- [x] 8 cases present
- [x] ≥1 hard (`08_password_rules`)
- [x] Run instructions documented
- [x] Pre-agent success_rate = 0%

**Evidence:** `run_all.py` output in this session.

## 7) Decision record
| Decision | Chose | Rejected | Why |
|----------|-------|----------|-----|
| World shape | 8 micro modules + pytest | One big Flask app | Faster isolation; clearer per-case metrics |
| Hard case | Password policy | Complex concurrency bug | Still readable in traces; multi-rule failure mode |
| Harness | subprocess pytest per case | In-process import hacks | Matches how an agent would shell out |

**Tradeoff accepted:** Micro-functions are simpler than “real PR on a web app” — acceptable for sprint; README states scope.  
**Revisit if:** Judges want a more product-shaped demo — can wrap cases in a thin CLI later without changing metrics.

## 8) Failure / incident
- `04_dedupe_order` initially used `list(set(items))`, which preserved insertion order on CPython 3.9 and accidentally passed.
- Fix: `sorted(set(items))` to destroy order deterministically.

## 9) Risk still open
- Easy cases may be too easy for single-shot baseline → still OK if hard case differentiates advanced
- Agents might read `meta.json` spoilers — optional to strip at eval time later

## 10) Handoff
**Next session starts with:** Phase 2 — implement baseline single-shot (or minimal) fixer and score it on these 8 cases.

---

### Quality gate
- [x] Goal clear and checked
- [x] Prompt preserved
- [x] Actions + evidence present
- [x] Decision/tradeoff recorded
- [x] Honest about accidental PASS
- [x] Handoff actionable
- [x] No secrets
