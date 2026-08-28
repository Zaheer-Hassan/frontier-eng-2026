# Trace — <phase>: <short title>

| Field | Value |
|-------|--------|
| **ID** | `YYYY-MM-DD_HHMM_<phase>-<slug>` |
| **When (PKT)** | |
| **Duration** | ~__ min |
| **Agent(s)** | Grok (xAI) _(add others if used)_ |
| **Human** | Zaheer ul Hassan |
| **Phase** | kickoff / baseline / advanced / verify / repro / polish / incident |
| **Related changelog** | `[YYYY-MM-DD] — …` |
| **Status** | in-progress / submission-ready |

---

## 0) System state before this session
- Repo / branch:
- What already worked:
- What was broken or unknown:
- Open risks:

## 1) Session goal (falsifiable)
**Done means:** …

## 2) Constraints
- Problem PDF / rules:
- Time box:
- Stack / deps limits:
- Explicit non-goals this session:

## 3) Plan (before coding)
1. …
2. …
3. …

## 4) Agent brief (prompt issued)
```
<exact or faithful prompt>
```

**Why this brief:** (what we wanted the agent to optimize for)

## 5) Execution log
| Step | Actor | Action | Result |
|------|-------|--------|--------|
| 1 | agent/human | | ok / fail — note |
| 2 | | | |

**Files touched:**
- `path` — why

**Commands / checks run:**
```bash
# command
# → exit code / key output
```

## 6) Verification
- [ ] Happy path observed
- [ ] Relevant test / acceptance check
- [ ] Regression spot-check (if applicable)

**Evidence:** …

## 7) Decision record (senior core)
| Decision | Chose | Rejected | Why |
|----------|-------|----------|-----|
| e.g. approach | | | |

**Tradeoff accepted:** …
**Revisit if:** …

## 8) Failure / incident (if any)
- What went wrong:
- Root cause (best guess):
- Fix or workaround:
- Kept in changelog as failed experiment? Y/N

## 9) Risk still open
- …

## 10) Handoff
**Next session starts with:** …

---

### Quality gate (Grok checks before marking submission-ready)
- [ ] Goal was clear and checked
- [ ] Prompt preserved
- [ ] Actions + evidence present
- [ ] At least one real decision/tradeoff
- [ ] Honest about failures
- [ ] Handoff is actionable
- [ ] No secrets
