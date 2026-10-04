# Saved dense references for the cubic aggregate experiment

Scoped read-only inventory, 2026-09-30. No training was run and no saved
reference was modified. Inputs were restricted to this study and its generated
data. This report is an inventory and replay check, not a review of the cubic
approximation.

## Reusable panel

All nine tasks below have complete canonical dense Gaussian and block-memory
`k=4, P=1` reference checkpoints at width 1024, seed 1, and independently
stopped training MSE at most 0.001. All live in:

`/home/amir/Codes/PDE/data/generated/structured_full_rank_scalar_20260926/all_tasks_j2_20260927/references/`

For each task name `TASK`, the exact dense path is
`TASK__gaussian.npz`; the optional block control is
`TASK__block_k4_P1_canonical.npz`. Each has a sibling `.json` metadata file.
The first eight rows form the recommended panel. The last row is an available
same-geometry, lower-frequency alternative.

| Task | Training inputs | Dense final MSE | Dense endpoint time | Block vs dense circle RMS |
|---|---:|---:|---:|---:|
| `pair_cos3` | 2 | 0.0009999999989693813 | 4.553972207556661 | 0.007328522156439948 |
| `pair_orthogonal_cos1` | 2 | 0.0009999999999999335 | 5.902997788719396 | 0.009589017163527036 |
| `near_pair_sin9` | 2 | 0.000999999999372283 | 8.338558835015990 | 0.019464448940555042 |
| `cluster_triple_cos9` | 3 | 0.0009999999999999848 | 28.691782348457316 | 0.057967273270261355 |
| `triple_wide_mixed` | 3 | 0.0009999999996141075 | 11.691998066640291 | 0.004517823842860378 |
| `quartet_mixed` | 4 | 0.0009999999999999970 | 33.046256585950740 | 0.007604425709946183 |
| `broad_ridge6` | 6 | 0.0009999999999999879 | 13.277391558763380 | 0.0033896068935322364 |
| `alternating3` | 6 | 0.0009999999991782286 | 12.397466888179236 | 0.015401129916749300 |
| `cluster_triple_cos1` | 3 | 0.0009999999999999603 | 3.424570160412638 | 0.008445795653003222 |

`triple_mixed` itself has no complete seed-1, width-1024 checkpoint at MSE
0.001 in this inventory. `triple_wide_mixed` supplies the requested varied
three-input case without training a new reference. `alternating5` has a
0.001 Gaussian checkpoint in `quick_blocks1024_loss001_20260926`, but its
individual row omits a seed and there is no matching canonical k4/P1 pair
there; `alternating3` supplies a fully matched uniform design.

## Exact dense initialization and normalization

Use the study module `dense_compare.initialize(1024, 1, 'gaussian')`.
The resulting arrays are `w` of shape `(1024,2)`, `W` of shape
`(1024,1024)`, and `c` of shape `(1024,)`. In the cubic derivation's notation,
these are the input and middle initial weights, respectively; preserve their
orientation when forming training and query features.

The streams are NumPy `default_rng(SeedSequence([seed, stream]))`:

- `w`: stream 1, independent standard normal entries.
- `W`: stream 101, independent standard normal entries divided by `sqrt(n)`.
- `c`: stream 2, independent standard normal entries divided by `n`.

The C-contiguous raw-byte SHA256 hashes of the seed-1 initial arrays are:

| Array | SHA256 |
|---|---|
| `w` | `4635fbf0a2ec035841f0225a28a42e7c1d92013978b80d9a3b1764cc4a66fcf1` |
| `W` | `c9617c6a451cbf03d8253b436fcab8d96c7655fed9840a35ca5d2afe2fac9095` |
| `c` | `3910d9d95ced08104f48f1d8b2df09a63757bbdc159b472d239f9b3500bff877` |

Input rows are `u(theta)=(cos(theta),sin(theta))`, already incorporating the
book's normalized input convention. Apply no further `sqrt(2)` factor.
The network is `f=c @ tanh(W @ tanh(w @ u.T)) / n`.
The loss is the unhalved empirical mean `mean((f-y)**2)`; training weights
are `1/m`, and the layer mobilities are `(n,1,n)`.

All eight recommended dense references share the same initial `w,W,c`.
Zeroing scalar `c(0)` changes its initial output from the dense output by
circle RMS `1.407900285928593e-5` and maximum absolute value
`1.8174035387345424e-5` on the saved 256-point grid. This quantifies the
initial discrepancy only; it does not bound its later effect.

## Task definitions and passive query API

The union of `circle_tasks.BY_NAME` and `geometry_tasks.BY_NAME` provides the
frozen task definitions. `task.data()` returns `(unit_directions, labels)`;
`task.angles` preserves the sample order and `task.target(angles)` supplies
the teacher. No target amplitude normalization is applied.

```python
import sys
from pathlib import Path
import numpy as np

study = Path('/home/amir/Codes/PDE/studies/structured_full_rank_scalar_20260926')
sys.path.insert(0, str(study))
import dense_compare
import circle_tasks, geometry_tasks
import true_aggregate_references as refs

tasks = {**circle_tasks.BY_NAME, **geometry_tasks.BY_NAME}
initial = dense_compare.initialize(1024, 1, 'gaussian')
u, y = tasks['pair_cos3'].data()
reference_dir = Path('/home/amir/Codes/PDE/data/generated/structured_full_rank_scalar_20260926/all_tasks_j2_20260927/references')
checkpoint = refs.load_checkpoint(reference_dir / 'pair_cos3__gaussian.npz')
angles = 2*np.pi*np.arange(256)/256
prediction = checkpoint.predict(angles)  # arbitrary passive angles also work
```

Set BLAS thread environment variables before importing NumPy for inexpensive
small-task evaluation. `true_aggregate_references` sets them internally but
that is too late if NumPy/BLAS has already been loaded elsewhere.

Dense NPZ payloads include `w,W,c`, `angles,prediction`,
`train_angles,train_labels,train_prediction`, and a `history` array whose
columns are physical time and training MSE. Continuations also have
`continuation_history`. Histories do not contain intermediate weight states.
The circle grid is exactly `2*pi*arange(256)/256`, with uniform weight
`1/256`; its endpoint is excluded.

## Replay and provenance checks

The inventory replay loaded all 18 complete dense/block checkpoints and found:

- Every NPZ SHA256 equals its sibling JSON's `data_sha256`.
- All train angles/labels match the current task definitions exactly.
- All saved query grids equal the stated 256-point grid exactly.
- Re-evaluating complete saved weights reproduces every stored train and grid
  prediction bit-for-bit, and reproduces each reported training MSE exactly.
- Reconstructing the seed-1 dense initialization reproduces the first
  recorded training MSE exactly for each of the nine tasks.
- All eight source hashes in the campaign manifest match the current study
  producer modules, including `dense_compare.py`, task definitions, and the
  dense adaptive integrator.

The campaign manifest and completion are in the same reference directory as
`manifest.json` and `completion.json`. The references were either reused,
continued from their saved complete state, or initialized once. The completed
campaign records 18 fitted endpoints and 7.5257154032588005 seconds of new
reference training, with no reruns.

The dense producer uses RK45 with `rtol=1e-5`, `atol_w=atol_c=1e-8`,
`atol_W=1e-8/sqrt(1024)`, a maximum of per-layer scaled RMS error norms,
and dense-interpolant/Brent threshold location. Reused reference metadata
may omit solver fields; follow its `source_checkpoint` chain to the original
producer metadata. This inventory checks stored-state integrity and replay,
not an independent solver-refinement error bound.

Optional k4/P1 controls use identical initial `w,c` streams and independent
Gaussian 4-by-4 marks from stream `300+4`, divided by `sqrt(4)`. The nominal
absolute-entry cutoff is 3; the seed-1 producer records zero redraws. They
are finite-width block-memory controls, not full Gaussian initializations.

## If another task is required

No regeneration is necessary for the recommended panel. The existing
`run_all_tasks_references.py` accepts an explicit subset, automatically reuses
or continues a compatible source, preserves originals, and requires a new
output directory plus an explicit cumulative training budget for training.
For example, a future authorized fit of the currently missing exact
`triple_mixed` task can use:

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python studies/structured_full_rank_scalar_20260926/run_all_tasks_references.py \
  --output data/generated/structured_full_rank_scalar_20260926/NEW_RUN/references \
  --run --tasks triple_mixed --fit-seconds 44 --training-budget 90
```

The script fixes `n=1024`, seed 1, MSE 0.001, 256 query points, and both
Gaussian and canonical k4/P1 tags. Its `inventory(output)` Python API is
read-only; its CLI without `--run` still writes inventory metadata to the
chosen output directory. Neither training nor the CLI was invoked here.
