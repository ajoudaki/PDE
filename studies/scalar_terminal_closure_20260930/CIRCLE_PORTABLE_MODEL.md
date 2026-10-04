# Standalone 729-number circle terminal model

Implementation/check by `scalar_control`, 2026-09-30. This is a scoped
implementation of the authorized circle experiment, with no new training.
Source: `evaluate_circle_scalar.py`. Scientific inputs were this study's
experiment plan, complete producer and current terminal theorem, plus the
selected completed case in `circle_width1024_02`. No other study was read.

The model NPZ contains exactly four float64 arrays:

| Key | Shape | Entries |
|---|---:|---:|
| `matrix` | (8,8) | 64 |
| `drift` | (8,) | 8 |
| `fourier` | (64,10) | 640 |
| `initial_state` | (17,) | 17 |
| Total | | **729** |

The state is `(r[8], integral(r)[8], integral(norm(r))[1])`. Export initializes
the nine integrals to zero. The fixed Fourier columns contain the handoff
output, eight query-response columns, and the query drift. Rows are cosine
coefficients for frequencies 1,3,...,63 followed by sine coefficients for
those frequencies. The final query output is the Fourier basis applied to
`fourier @ [1, -integral(r), integral(norm(r))]`.

No global handoff time, angle panel, labels, population arrays or width-sized
state is in this model. Optional provenance is a separate JSON that the
evaluator never reads. Model loading rejects extra keys, wrong shapes,
non-float64 arrays and nonfinite values. In particular it rejects the
producer's population handoff NPZ rather than using it as a runtime model.

The `evaluate` command integrates only these entries using DOP853,
`rtol=1e-10`, `atol=1e-12`, matching the producer. Inputs are elapsed duration
and a caller-supplied one-dimensional NPY angle grid in radians. Outputs are
an elapsed-time array, the 17-state curve, its residual loss, the supplied
angles and the final circle outputs. It imports no producer or project code.
`evaluate_model` also accepts a supplied finite 17-state for restart, with
the original coefficients and accumulated integrals retained.

## Usage

Use the producer's recorded Python environment, which provides NumPy, SciPy
and threadpoolctl. The system `python` lacks threadpoolctl. From repository
root, export any completed case's selected primary MSE-0.01 handoff:

```bash
/home/amir/miniconda3/bin/python studies/scalar_terminal_closure_20260930/evaluate_circle_scalar.py export \
  --run data/generated/scalar_terminal_closure_20260930/circle_width1024_02 \
  --case two_outliers_alternating \
  --output /tmp/two_outliers_scalar.npz \
  --provenance /tmp/two_outliers_scalar.provenance.json
```

Export consults `results.json` to select `fine` or `refined`. Overall run
completion is unnecessary when the chosen case is already complete. Existing
output files are never overwritten. Evaluate independently, supplying an
angle-grid NPY and a fresh output path:

```bash
/home/amir/miniconda3/bin/python studies/scalar_terminal_closure_20260930/evaluate_circle_scalar.py evaluate \
  --model /tmp/two_outliers_scalar.npz --duration 64.375 \
  --angles data/generated/scalar_terminal_closure_20260930/circle_portable_check_01/recheck_01/angles.npy \
  --samples 1031 --output /tmp/two_outliers_prediction.npz
```

The duration above is the checked case's recorded endpoint interval; a user
may supply another finite nonnegative elapsed duration and another angle
grid. Zero duration returns the supplied initial state. Solver runs are
capped at two BLAS threads and have a 60-second deadline.

The `check` command reproduces the export and runs a copied evaluator as an
independent child program inside a fresh output directory. That child receives
only the standalone model, duration and angle grid, with no source-run path
or provenance file. The completed-case reference is read only by the parent
check command. Use a fresh `--output-dir` when reproducing:

```bash
OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 \
/home/amir/miniconda3/bin/python studies/scalar_terminal_closure_20260930/evaluate_circle_scalar.py check \
  --run data/generated/scalar_terminal_closure_20260930/circle_width1024_02 \
  --case two_outliers_alternating \
  --output-dir data/generated/scalar_terminal_closure_20260930/circle_portable_check_REPRO
```

## Executed consistency check

Case: `two_outliers_alternating`, selected `fine`; global handoff 180.125,
recorded endpoint 244.5, elapsed duration 64.375. These global times are only
provenance. The independent evaluator used 8192 angles and 1031 scalar
observation times, with no training or population evaluation.

| Check or diagnostic | Observed maximum error | Result |
|---|---:|---|
| Endpoint circle outputs, tolerance 1e-8 | 2.2039037261833982e-12 | PASS |
| Endpoint 17-state, tolerance 1e-8 | 1.7543302016165621e-12 | PASS |
| Endpoint residual loss, tolerance 1e-8 | 8.110340469959926e-19 | PASS |
| Extra whole-trajectory state diagnostic, tolerance 1e-8 | 1.0273772861309552e-8 | **FALSE** |
| Whole-trajectory residual loss diagnostic | 4.1668968622787794e-13 | reported |
| Elapsed-grid difference | 0 | exact |
| Zero-duration state difference | 0 | exact |
| Reject raw population handoff as model | rejected | PASS |

The requested endpoint check passes. The extra whole-trajectory state
threshold remains false. The first check incorrectly used that additional
diagnostic as an overall gate; its original false report is preserved at
`data/generated/scalar_terminal_closure_20260930/circle_portable_check_01/check.json`.
The corrected check gates only the assigned endpoint requirement and retains
the same full-curve discrepancy as a diagnostic. Its evidence is
`circle_portable_check_01/recheck_01/check.json`, alongside the exported
`model.npz`, separate provenance, copied source and `evaluation.npz`.
No solver method, tolerances, coefficients or evaluation equations changed.

The first system-Python invocation failed before creating artifacts because
threadpoolctl was unavailable. The recorded producer environment succeeded.
The two scalar checks took 0.385 and 0.364 seconds internally; including the
failed dependency invocation, measured command wall time was about 1.36
seconds, below the cumulative 60-second computation budget. Both reported
BLAS libraries were limited to two threads. Environment: Python 3.10.14,
NumPy 1.26.4, SciPy 1.11.4. No training was run.

## Hashes and limits

SHA256 records:

* Evaluator: `ba902372cfe222400441cafeb56b4868fcd30d3ac5421d479a9750281ded94b8`.
* Model: `5553d438dc83a17ca80f73b35b61ea71334cc65b25530ad40fee9cd16002dd79`.
* Evaluation output: `da05b22aefd3464a16f418165ece9b9b6cbb18617f2fe4cfa583fbc4725989cb`.
* Corrected endpoint-check report: `12bf1d653c953a5f41e65eb051b169b73bb286aaf963c848733161b2a33c2bde`.
* Original extra-gate false report: `3ece94e39c28ff1b3d396a90be5481e600727f61bc32caf154593c0d7dfcb99d`.
* Producer: `f5ea7959bbd440aa161b6cb0ee484e68d9e81d5e7cce5e4b9b1df590a170c6ba`.
* Source handoff: `ebc47b245699875715c5dd75cb6d7b0c5f8725b8d7114188d9fc994b3b71dccc`.
* Raw scalar curves: `3becaf943ba37a755de590c0ce271c84e37741d27ba65f8f59bc7501c0b2d8ed`.

This verifies portable evaluation of the already selected terminal model.
Producing its coefficients still incurred the full offline q=1 handoff
cost. The check does not establish initialization-only compression, dense
network accuracy, a population theorem, an infinite-time numerical endpoint
or uniform whole-circle accuracy. Residual loss is the internal residual
ODE's loss; Fourier evaluation at training angles need not reproduce those
residuals exactly because the spatial representation is truncated. Only one
completed case was exported and checked here; later case exports are left
to the coordinating task. No README, empirical report, main run or Git index
was modified by this subtask.

## Final campaign exports by the coordinating task

After the original campaign and its separately planned endpoint extension
completed, the coordinating task exported and checked all five primary
models from `circle_width1024_extension_01`. The artifacts are in
`data/generated/scalar_terminal_closure_20260930/circle_portable_final_01/`,
with one case directory containing `model.npz`, separate provenance, a copied
standalone evaluator, queries, predictions and `check.json`. The combined
`summary.json` reports five passing assigned endpoint checks and exactly
729 entries in every model. This supersedes the earlier one-case coverage
limit for the campaign as a whole, while preserving that original check.

Maximum final-circle discrepancies from the campaign scalar evaluator are
2.204e-12, 1.015e-13, 2.120e-14, 8.555e-14 and 6.662e-16 in the prescribed
task order. All five elapsed observation grids match exactly. Their combined
command wall time was 3.330 seconds. The first case retains the previously
reported 1.02738e-8 whole-trajectory state diagnostic; no tolerance or equation
was changed. The center/edges export is evaluated through the supplemental
time-950 endpoint using the original time-129 switch coefficients.
