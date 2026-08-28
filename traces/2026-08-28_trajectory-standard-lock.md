# Trace — polish: lock senior trajectory standard

| Field | Value |
|-------|--------|
| **ID** | `2026-08-28_trajectory-standard-lock` |
| **When (PKT)** | 2026-08-28 |
| **Duration** | ~20 min |
| **Agent(s)** | Grok (xAI) |
| **Human** | Zaheer ul Hassan |
| **Phase** | polish (pre-kickoff process) |
| **Related changelog** | `[2026-08-28] — Senior trajectory ownership` |
| **Status** | submission-ready |

---

## 0) System state before this session
- Repo scaffold and basic traces existed
- Zaheer flagged confusion on what trajectories are
- Risk: traces would look like chat dumps → weak judging signal

## 1) Session goal (falsifiable)
**Done means:** Written SOP + senior template + clear ownership (Grok drafts, Zaheer approves) + session card for kickoff cadence.

## 2) Constraints
- No problem PDF yet — process only, no solution code
- Must stay honest (no fake résumé claims in prose)
- Seniority via judgment structure, not hype

## 3) Plan (before coding)
1. Define non-negotiable sections for every trace
2. Replace template with senior decision-record format
3. Document cadence (“trace close karo”)
4. Index + changelog

## 4) Agent brief (prompt issued)
```
Trajectories are your responsibility — set up the work so judges feel
a 10+ year engineer ran the agent. Create the setup.
```

**Why this brief:** Submission quality hinges on traces as much as code; process must be locked before PDF.

## 5) Execution log
| Step | Actor | Action | Result |
|------|-------|--------|--------|
| 1 | human | Assigned trajectory ownership to Grok | ok |
| 2 | agent | Wrote `docs/TRAJECTORY_STANDARD.md` | ok |
| 3 | agent | Replaced `traces/_TEMPLATE.md` with senior template | ok |
| 4 | agent | Added `docs/SESSION_CARD.md` | ok |
| 5 | agent | Updated `traces/README.md` index + ownership | ok |

**Files touched:**
- `docs/TRAJECTORY_STANDARD.md` — quality bar + cadence
- `traces/_TEMPLATE.md` — senior sections 0–10
- `docs/SESSION_CARD.md` — lightweight start ritual
- `traces/README.md` — operating manual + index

## 6) Verification
- [x] Template includes decision record, verification, handoff
- [x] SOP states owner and pre-submit audit
- [x] Practice path clear for kickoff (`trace close karo`)

**Evidence:** files present under `docs/` and `traces/`.

## 7) Decision record
| Decision | Chose | Rejected | Why |
|----------|-------|----------|-----|
| Trace authorship | Grok drafts every trace | Zaheer writes from scratch | Consistency + speed; human approves |
| Style | Structured decision logs | Raw chat export dumps | Judges need signal, not noise |
| Senior signal | Judgment sections | Claiming “10+ YOE” in text | Honesty; bar is observable quality |

**Tradeoff accepted:** Slightly more writing time per session.  
**Revisit if:** PDF mandates a specific trace file format from micro1.

## 8) Failure / incident
None.

## 9) Risk still open
- PDF may add required trajectory schema — adapt template then
- If sessions aren’t closed with “trace close karo”, gaps appear

## 10) Handoff
**Next session starts with:** On PDF drop, open `docs/KICKOFF.md` + new trace from `_TEMPLATE.md` for kickoff scope-cut.

---

### Quality gate
- [x] Goal clear and checked
- [x] Prompt preserved
- [x] Actions + evidence present
- [x] Real decisions/tradeoffs
- [x] Honest about scope (process only)
- [x] Handoff actionable
- [x] No secrets
