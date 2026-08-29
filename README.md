# Frontier Engineering Challenge 2026 — Bug-Fix / PR Agent

**Participant:** Zaheer ul Hassan  
**Host:** micro1 (HackerEarth)  
**Problem choice:** #2 — Automated bug-fix agent for a small failing codebase  
**Format:** Individual · Online · Agents required  
**Deadline:** 31 Aug 2026, 18:00 UTC (11:00 PM PKT)

Official instructions: [`docs/problem-statement.pdf`](./docs/problem-statement.pdf)

---

## Who has this problem?

**Primary user:** A solo developer or small team shipping a service under time pressure.

They have a repo where **tests are red** (regressions, broken handlers, bad edge cases). They need the codebase green again without spending hours hunting stack traces by hand.

## What bottleneck makes it worth solving?

Reading failures, locating the right file, drafting a patch, and re-running tests is slow and easy to get wrong when context is incomplete. A one-shot “fix this” prompt often invents APIs or breaks other tests. The bottleneck is a **reliable edit–verify loop**, not generating more code.

## Why an agent helps

An agent can:

1. Run the test suite  
2. Read failures and relevant source  
3. Propose a minimal patch  
4. Re-run tests  
5. Retry with a budget when verification fails  

That is closer to how senior engineers actually debug.

## Scope (frozen in Phase 0)

| In scope | Out of scope |
|----------|----------------|
| One small sample app with intentional bugs + pytest | Full IDE / GitHub PR bot product |
| Baseline vs Advanced agent on the **same** eval cases | Training models |
| Measured improvement (see metrics) | Multi-repo monorepo simulation |
| Trajectories, changelog, repro, ≤5 min video | Private/customer data |

Sample apps and cases are built in **Phase 1**.

---

## Primary metric (frozen)

**Success rate on fixed eval cases:**  
fraction of cases where the agent (or baseline) leaves the suite **green** within the allowed step/retry budget.

Supporting metrics (reported, not primary):

- Median **time-to-green** (seconds) on cases it solves  
- Median **patch iterations** (test runs) until green or give-up  

Eval protocol: same cases for baseline and advanced; ≥5 cases including ≥1 hard case (Phase 1).

---

## Solutions

| Track | Path | Intent |
|-------|------|--------|
| **Baseline** | `BASELINE/` | Fair simple approach (e.g. single-shot LLM fix or minimal loop) |
| **Advanced** | `ADVANCED/` | Plan → edit → test → verify → retry budget + better tooling |

## Agents used

| Agent | Role |
|-------|------|
| Grok (xAI) | Primary — design, implementation, trajectories |
| _(optional backup)_ | TBD if used |

## How to reproduce

See [`REPRO.md`](./REPRO.md) (filled as implementation lands).

## Improvement history

See [`CHANGELOG.md`](./CHANGELOG.md).

## Agent trajectories

See [`traces/`](./traces/) — written to [`docs/TRAJECTORY_STANDARD.md`](./docs/TRAJECTORY_STANDARD.md).

## Demo video

See [`video/SCRIPT.md`](./video/SCRIPT.md) — ≤ 5 minutes.

## Hot take / main failure mode

_(filled before submit)_

## Task board

[`docs/TASKS.md`](./docs/TASKS.md)

---

## Disclaimer

Submission for the micro1 Frontier Engineering / Agentic Workflows challenge. Governed by the Hackathon Participation Agreement accepted at registration; micro1 may use submissions for AI training and evaluation.
