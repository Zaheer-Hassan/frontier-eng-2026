# Kickoff night checklist (PDF release)

**Kickoff (target):** 28 Aug 2026 ~ **8:00 PM PKT** (15:00 UTC)  
**Hard deadline:** 31 Aug 2026 ~ **11:00 PM PKT** (18:00 UTC)

Work with Grok in the existing chat. Keep VS Code on this repo open.

---

## T−30 min (before PDF)
- [ ] `gh auth switch --user Zaheer-Hassan`
- [ ] `cd /Users/zaheer/Projects/frontier-eng-2026 && git status` clean or commit WIP
- [ ] HackerEarth challenge page open + logged in
- [ ] Agent ready (Grok chat + optional Cursor)
- [ ] API credits / `.env` from `.env.example` ready
- [ ] Water / charger / notifications muted

---

## 0:00–0:20 — Read & scope
- [ ] Download / open problem PDF + starter materials
- [ ] Paste PDF text or key constraints into Grok chat
- [ ] Write in `README.md`: user, bottleneck, why it matters
- [ ] Start new trace: copy `traces/_TEMPLATE.md` → `traces/YYYY-MM-DD_HHMM_kickoff-read.md`
- [ ] **Scope cut:** list Must / Should / Won’t for 3 days
- [ ] Define **one** improvement metric for Advanced (number you can measure)

## 0:20–1:30 — Baseline v0
- [ ] Scaffold code under `BASELINE/`
- [ ] Make it run once (happy path)
- [ ] Minimal test or acceptance check green
- [ ] Update `BASELINE/README.md` + `REPRO.md` baseline commands
- [ ] Changelog entry #1
- [ ] Trace entry for this session

## 1:30–2:00 — Lock the night
- [ ] Commit + push (`Zaheer-Hassan`)
- [ ] Write tomorrow’s first task at top of `CHANGELOG.md` or a sticky note in chat
- [ ] Sleep if exhausted — don’t force Advanced tonight

---

## Day 2 focus
- [ ] Harden baseline (edge cases from PDF)
- [ ] Start Advanced with clear thesis + metric table in `ADVANCED/README.md`
- [ ] Keep traces continuous (every meaningful agent session)

## Day 3 focus
- [ ] Finish Advanced + measured comparison
- [ ] Polish REPRO + README + Changelog
- [ ] Record ≤5 min video (`video/SCRIPT.md`)
- [ ] Package trajectories
- [ ] **Soft submit ~8:00 PM PKT**, then buffer for fixes before 11:00 PM

---

## Submission gate (before upload)
- [ ] Baseline runs from clean instructions
- [ ] Advanced runs + shows measured improvement
- [ ] Changelog complete
- [ ] REPRO complete
- [ ] Video ≤ 5 min
- [ ] Agent list + trajectories present
- [ ] No secrets in git
- [ ] HackerEarth latest submission complete

## Help
- Organizer: yeison@micro1.ai
- Challenge page Help / clarifications
