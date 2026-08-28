# Commit message standard (Owner: Grok)

Every commit title should read like a **senior engineer** left a clear audit trail — not like a casual WIP note.

## Format

```text
<type>: <imperative summary ≤ ~72 chars>

<optional body: why, tradeoff, verification>
```

## Types we use

| Type | When |
|------|------|
| `feat` | New user-facing capability |
| `fix` | Bug fix |
| `refactor` | Structure change, behavior same |
| `test` | Tests only |
| `docs` | Docs / traces / README / changelog process |
| `chore` | Tooling, scaffold, repo hygiene |
| `perf` | Measured performance improvement |
| `build` | Dependencies / build pipeline |

## Title rules

- Imperative mood: **Add** / **Fix** / **Tighten** / **Isolate** (not “Added”, “Fixed”)
- Specific outcome, not vague (“update stuff”)
- Prefer domain words: baseline, advanced, repro, verifier, trajectory, acceptance
- No emoji, no hype, no “final!!!”, no “WIP pls”
- Optional scope: `feat(baseline): …` / `docs(traces): …`

## Good vs weak

| Weak | Senior |
|------|--------|
| `update files` | `docs(traces): lock senior trajectory standard and ownership` |
| `fix bug` | `fix(baseline): handle empty input in acceptance path` |
| `changes` | `feat(advanced): add retry budget and surface failure taxonomy` |
| `push code` | `chore: remove practice-only traces before kickoff` |
| `final submit` | `docs(repro): complete clean-machine runbook for judges` |

## Body (use when non-obvious)

```text
Why:
- …

Tradeoff:
- …

Verify:
- <command> → <result>
```

## Cadence with challenge

- Meaningful code/docs change → commit soon (small, reviewable)
- Every commit that maps to a decision → related `CHANGELOG` / trace when applicable
- Grok drafts the message; Zaheer can tweak before push
