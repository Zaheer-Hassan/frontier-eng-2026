# Agent Trajectory Standard (Owner: Grok)

**Bar:** Every trace must read like a **senior engineer (10+ years)** ran an agent — not like a student pasted a chat.

Judges should feel: clear problem framing, deliberate tool use, measured decisions, explicit tradeoffs, verification, and honest failure handling.

Zaheer drives product intent and final calls. **Grok owns** drafting, structuring, and quality-checking every trajectory before it lands in `traces/`.

---

## What “senior” looks like

| Junior vibe (avoid) | Senior vibe (required) |
|---------------------|------------------------|
| “Agent wrote the code” | “Scoped X, constrained Y, verified Z” |
| Dump full chat | Curated narrative + evidence |
| No why | Decision + tradeoff + rejected alternative |
| “It works” | Command + expected vs actual + metric |
| Hide failures | Document failed path and why it was dropped |
| Vague next steps | Single crisp next action |

---

## Non-negotiables (every trace)

1. **Context** — what state the system was in before this session  
2. **Goal** — one falsifiable outcome for this session  
3. **Constraints** — time, PDF rules, stack, risk  
4. **Plan** — 2–5 steps before coding (even if short)  
5. **Agent brief** — exact/near-exact prompt given to the agent  
6. **Execution log** — actions, tools, files (ordered)  
7. **Verification** — what was run; pass/fail; evidence  
8. **Decision record** — what we chose, what we rejected, why  
9. **Risk / failure mode** — what still can break  
10. **Handoff** — next session’s first action  

If any of 1–10 is missing, the trace is **not submission-ready**.

---

## Cadence (how we work)

```text
Session start  → Grok opens new trace from senior template
During work    → Grok notes decisions, failures, commands
Session end    → Grok completes trace to senior bar
               → Link CHANGELOG entry + files touched
               → Zaheer skims 1 min; says OK / fix
```

Zaheer shortcut: after any meaningful block, say **"trace close karo"** — Grok finishes the file.

---

## Naming

```text
traces/YYYY-MM-DD_HHMM_<phase>-<slug>.md

Phases:
  kickoff | baseline | advanced | verify | repro | polish | incident
```

Examples:
- `2026-08-28_2015_kickoff-scope-cut.md`
- `2026-08-28_2140_baseline-health-v0.md`
- `2026-08-29_1930_advanced-retry-budget.md`
- `2026-08-30_2210_verify-repro-clean-machine.md`

---

## Evidence attachments

Prefer in-repo pointers over vibes:

- command + exit code  
- test name + result  
- metric table row  
- file paths changed  
- screenshot only if UI-critical (`traces/assets/`)  

Never paste secrets / API keys.

---

## Volume target (3-day sprint)

| Phase | Min traces |
|-------|------------|
| Kickoff / scoping | 1 |
| Baseline build + harden | 3–4 |
| Advanced + measurement | 3–4 |
| Failed experiment (at least one honest) | 1 |
| Repro / video / submit polish | 1–2 |
| **Total** | **~9–12** |

Quality > quantity, but empty days look junior.

---

## Pre-submit audit (Grok runs this)

- [ ] Agents disclosed in root README  
- [ ] Every meaningful CHANGELOG row has a linked trace  
- [ ] At least one trace shows a **rejected** approach  
- [ ] At least one trace shows **verification commands**  
- [ ] Baseline vs Advanced improvement is evidenced in a trace  
- [ ] No raw secret material  
- [ ] `traces/README.md` index is complete and ordered  

---

## Voice & tone

Write in crisp engineering English (short paragraphs, bullets OK).  
First person plural (“we”) is fine — team of human + agent.  
No hype (“revolutionary”), no résumé flex, no fake years-of-experience claims in prose.  
Seniority shows in **judgment**, not in bragging.
