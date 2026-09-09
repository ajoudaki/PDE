# Start here: fixed-\(P=5\) PDE generalization release

This compact release contains the complete source-first reproduction package,
processed evidence, three figures, and the self-contained final report. The
1.35 GB of raw trajectory arrays is intentionally omitted and can be
regenerated.

## Read the result

- `PDE_GENERALIZATION_FINAL_REPORT.md` is the complete scientific report.
- `figures/all_case_errors.png` is the uncertainty-aware case summary.
- `figures/loss_curves.png` and `figures/gram_motion_curves.png` show all
  global curves through \(t=32\).

The result is encouraging but deliberately not labeled a universal pass:
every observed normalized curve error is below 5%, but the frozen
simultaneous-confidence and numerical/plateau rules give the overall verdict
`boundary_or_unresolved`.

## Verify this archive

From the release root:

```bash
python verify_release.py
```

The command validates every included file against `SHA256SUMS.txt`.

## Reproduce the omitted raw evidence

```bash
cd study
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-lock.txt
PYTHONPATH=src python protocol/reproduce_generalization_postfreeze.py
```

See `study/REPRODUCTION.md` for compute tiers, parallelism controls, the full
verification path, and the two disclosed execution-only amendments.

`study/README.md` is retained byte-for-byte because it belongs to the frozen
scientific manifest. Its original one-command path predates the disclosed
compatibility wrappers and should not be used for reproduction.
