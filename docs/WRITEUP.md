# Project write-up

## Approach
We treat “make the suite green” as an agentic control problem.

1. **Sample world** — eight synthetic buggy modules with pytest contracts and a success-rate harness.
2. **Baseline** — a fair weak automator: one shallow heuristic, one retest, stop (37.5%).
3. **Advanced** — plan → edit → verify → retry with a catalog of named strategy skills and a signal-based planner (100%).

Building and debugging were done with **Grok (xAI)** as the coding agent; runtime advanced trajectories are recorded per case under `ADVANCED/trajectories/`.

## What improved outcomes
| Change | Effect |
|--------|--------|
| Shared fixed eval cases | Comparable baseline vs advanced |
| Verify-after-edit gate | Prevents silent wrong patches |
| Strategy skills + planner | Semantic bugs become reachable |
| Retry budget with stop | Avoids infinite flailing |

## Failures & removed experiment
- **Accidental baseline-strength bug:** `list(set(...))` preserved order on CPython — fixed sample world so order destruction is deterministic.
- **Removed experiment:** re-looping only the three baseline heuristics. Retries without new skills cannot fix semantic cases; rejected.

## Hot take
Agent reliability comes less from “more generations” and more from **explicit skills, verify gates, and honest stop conditions**.

## Main remaining failure mode
A narrow skill catalog that doesn’t generalize beyond this sample world. Next iteration: add an LLM proposal skill behind the same verify gate once API keys are available.
