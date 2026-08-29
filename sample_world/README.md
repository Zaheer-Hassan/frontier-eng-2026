# Sample world (eval harness)

Tiny, intentional buggy Python modules used to evaluate the **bug-fix agent**.

```text
sample_world/
  cases/<id>/app.py        # broken implementation
  cases/<id>/test_app.py   # correct behavior contract
  cases/<id>/meta.json     # human/harness metadata
  run_case.py              # run one case
  run_all.py               # success-rate summary
  EVAL_CASES.md            # case catalog + commands
```

## Setup

```bash
python -m pip install -r sample_world/requirements.txt
```

## Score

```bash
python sample_world/run_all.py
```

Phase 1 expectation: all cases **FAIL** until baseline/advanced agents repair them in later phases.
