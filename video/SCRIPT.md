# Demo Video Script (≤ 5 minutes)

**Record with:** Loom or OBS  
**Export to:** `video/demo.mp4` (gitignored if large — upload with HackerEarth submission)  
**Repo to show:** https://github.com/Zaheer-Hassan/frontier-eng-2026

---

## Timing guide
| Time | Section | On screen |
|------|---------|-----------|
| 0:00–0:40 | Problem + user + bottleneck | README “Who has this problem?” |
| 0:40–1:30 | Pristine world red | `python sample_world/run_all.py` → 0/8 |
| 1:30–2:20 | Baseline | `python BASELINE/fix_once.py` → **37.5%** |
| 2:20–3:40 | Advanced end-to-end | `python ADVANCED/agent.py` + open one trajectory JSON |
| 3:40–4:20 | Comparison table | README headline metric / both JSON files |
| 4:20–4:50 | Changelog: best change + removed experiment | CHANGELOG Phase 3 entry |
| 4:50–5:00 | Hot take + close | README hot take |

---

## Spoken outline (read naturally)

1. **Problem (0:00)**  
   “I’m Zaheer. This project is a bug-fix agent for a developer under time pressure. When tests are red, the bottleneck isn’t writing more code — it’s a reliable edit–verify loop.”

2. **Pristine world (0:40)**  
   “Here are eight synthetic failing cases. Before any fixer, success rate is zero.”

3. **Baseline (1:30)**  
   “Baseline is a simple one-pass script: at most one shallow heuristic, one retest, then stop. It reaches three of eight — 37.5%. It plateaus on semantic bugs.”

4. **Advanced (2:20)**  
   “Advanced is an agent loop: observe pytest, plan which unused strategy skill to apply, edit app.py, verify, retry under budget. Watch it clear all eight, including the hard password policy case. Each case writes a tool trajectory JSON.”

5. **Comparison (3:40)**  
   “Same cases, same metric: baseline 37.5%, advanced 100% — plus 62.5 points.”

6. **Changelog (4:20)**  
   “Best change: strategy skills plus verify gates. We rejected ‘just retry the baseline heuristics in a loop’ — retries without new skills waste budget.”

7. **Close (4:50)**  
   “Hot take: reliability comes from explicit skills, verify gates, and honest stop conditions — not more blind generations. Thanks.”

---

## Recording checklist
- [ ] Screen + mic clear
- [ ] Terminal font large enough
- [ ] No `.env` / API keys visible
- [ ] Show `pwd` inside repo root
- [ ] Show baseline then advanced outputs
- [ ] Open `ADVANCED/trajectories/08_password_rules.json` briefly
- [ ] Export MP4 ≤ 5:00
