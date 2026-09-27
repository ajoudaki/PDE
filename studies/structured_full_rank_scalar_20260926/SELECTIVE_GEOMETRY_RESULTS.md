# Fixed selective closure across eight new input configurations

2026-09-27. Eight preselected configurations were tested with the same
selective scalar closure. Four reached the requested core training MSE
0.01; their raw circle RMS discrepancies from canonical Gaussian were
0.0429, 0.0613, 0.0768 and 0.2118. Four reached the 45-second training cap.
All eight Gaussian controls and all eight matched block-population controls
fitted to MSE 0.01.

The strongest new diagnostic is the two-input, opposite-label case: fitted
core predictions agree with Gaussian on the training inputs to RMS 0.00107,
but passive predictions differ from Gaussian around the circle by RMS
0.21179. This isolates a substantial off-training discrepancy even when
the fitted training predictions are very similar. It is not a theorem about
all possible scalar compressions.

## Frozen setup

The experiment uses tanh, block size k=4, response-memory order P=1,
initialization seed1, n=1024, and the existing smallest selective zero-boundary
rule. Exact immediate derivatives of outputs, essential feedback and both
hidden-layer Gram matrices remain protected. The cutoff and solver settings
are fixed across tasks. Initial scalar contractions come from the matched
finite block realization; these population arrays are discarded before the
scalar ODE evolves.

The primary observable is raw RMS of scalar passive outputs minus canonical
Gaussian predictions on 64 equally spaced circle angles. Gaussian and block
controls are saved on 256 angles. The test metric is not teacher risk and
has no signal-amplitude denominator. All training inputs are also included
as passive probes, excluded from the circle-RMS average, to measure the
previously observed input-identification defect.

The eight task definitions, exact angles and labels are fixed in
[geometry_tasks.py](geometry_tasks.py). The
[protocol](SELECTIVE_GEOMETRY_PROTOCOL.md) records the metrics, stopping
rules, numerical checks and conditional follow-ups before training.

## Results

An asterisk marks an unfinished scalar trajectory stopped by the 45-second
training budget. Its circle number compares that partial endpoint with a
fitted Gaussian endpoint; it is not a fitted-network comparison.

| Input configuration | Samples | Core training MSE | Circle RMS vs Gaussian | Circle RMS vs matched block | Training seconds |
|---|---:|---:|---:|---:|---:|
| Opposite labels, 60-degree separation (`pair_cos3`) | 2 | 0.0100 | 0.21179 | 0.21333 | 13.69 |
| Opposite labels, 20-degree separation (`near_pair_sin9`) | 2 | 0.5855* | 0.28826* | 0.27633* | 44.76 |
| Orthogonal inputs, smooth labels | 2 | 0.0100 | 0.06128 | 0.05724 | 0.93 |
| Symmetric triple, cosine-3 labels | 3 | 0.5574* | 0.32036* | 0.31773* | 44.78 |
| Clustered triple, smooth cosine-1 labels | 3 | 0.0100 | 0.07683 | 0.07374 | 8.48 |
| Spread-out triple, mixed labels | 3 | 0.0100 | 0.04291 | 0.04428 | 2.85 |
| Four inputs, broad ridge | 4 | 0.02614* | 0.09459* | 0.09818* | 44.83 |
| Four inputs, mixed labels | 4 | 0.06914* | 0.09169* | 0.09148* | 44.86 |

Training MSE 0.01 corresponds to training RMS 0.1. Training errors are
against labels; circle discrepancies are against the Gaussian fitted
function. A small circle discrepancy on an unfinished trajectory is not
evidence that it met the training target. Conversely, hitting the time cap
does not prove that a trajectory could never fit with additional computation.

The matched block-population controls have their own 256-angle Gaussian
discrepancies, in the same task order:

    0.006554, 0.020833, 0.008756, 0.021596,
    0.007991, 0.003979, 0.008166, 0.004489.

Every such control fitted. Therefore block initialization replacement alone
does not account for the scalar method's larger discrepancies or failure
to reach the target within the allotted time.

## What changed in the empirical assessment

Three of four newly fitted scalar cases pass the predeclared coarse screen
of circle RMS at most 0.1. The opposite-label pair lies between the 0.1
and 0.3 screens. There is no newly fitted case above 0.3, so neither
conditional numerical follow-up was triggered. No favorable seeds or
alternative cutoffs were selected after seeing the results.

The opposite-label pair is especially informative because its fitted
training predictions nearly coincide with Gaussian (RMS 0.00107), its
maximum training/passive identification gap is only 0.00917, and its
nested circle-grid sensitivity is 0.00000656. Nevertheless, its circle
discrepancy is 0.21179. This is a cleaner example of off-training error
than either a run that did not fit or a large duplicate-input inconsistency.
The previous statement that no such pronounced training-versus-circle
discrepancy had been observed was limited to the earlier campaign.

The smooth-label cluster also separates two causes: it uses the same
angles as the earlier unsuccessful clustered cosine-9 task, but now fits
with circle RMS 0.07683. Thus clustering alone does not explain that earlier
failure. Label variation across nearby inputs matters in these observations.
This is a single-seed comparison, not a universal classification of tasks.

## Passive versus training-output consistency

Every new run starts with zero disagreement between passive copies and
their corresponding training-output states. Later differences are:

| Task | Core training RMS | Passive predictor's training RMS | Maximum disagreement at the same input |
|---|---:|---:|---:|
| Opposite labels, 60 degrees | 0.1000 | 0.0923 | 0.0092 |
| Opposite labels, 20 degrees, unfinished | 0.7652 | 0.6360 | 0.1597 |
| Orthogonal inputs | 0.1000 | 0.1078 | 0.0110 |
| Symmetric cosine-3 triple, unfinished | 0.7466 | 0.5551 | 0.3401 |
| Smooth cluster | 0.1000 | 0.1338 | 0.0367 |
| Spread-out mixed triple | 0.1000 | 0.1077 | 0.0126 |
| Broad quartet, unfinished | 0.1617 | 0.1595 | 0.0556 |
| Mixed quartet, unfinished | 0.2630 | 0.1802 | 0.1602 |

All four unfinished runs exceed the predeclared maximum-disagreement flag
of 0.05; none of the four fitted runs does. This does not prove the defect
causes fitting failure. It does establish that the finite hierarchy still
does not maintain a unique exact output value for identical inputs across
its different observable representations. A fitted core loss cannot be
silently attributed to the passive circle predictor.

## Efficiency and verification

Compilation now rejects an omitted derivative child before expensive graph
canonicalization when its additive decoration/node-count signature cannot
match any selected state. This is an exact computation shortcut. Selected
trees, coefficient arrays and RHS values were bitwise identical to the
original compiler on the tested two- and three-input configurations,
including active clipping penalties. No scientific cutoff was changed.
Two-, three- and four-input templates compiled in approximately 0.12,
0.45 and 1.30 seconds in the actual campaign.

The scalar ODE sizes include the clock and every passive probe:

| Training samples | Training core plus clock | Circle probes | Passive training copies | Total evolving scalars |
|---|---:|---:|---:|---:|
| 2 | 527 | 64 | 2 | 23,627 |
| 3 | 1,824 | 64 | 3 | 53,012 |
| 4 | 4,629 | 64 | 4 | 99,965 |

These sizes are independent of width and elapsed time. The probe costs
are explicit; this experiment does not produce a post-training arbitrary
input decoder or a reconstructed dense network.

Total scalar training was 205.18 seconds and initialization 59.03 seconds.
All sixteen reference trainings together took 13.17 seconds. There were
no reruns or extra orders. All jobs stopped after the preselected screen.

Independent checks passed for all eight scalar and sixteen reference
records: source/data hashes, finite states, exact query ordering, predictions
decoded directly from saved scalar states, losses, alias differences and
raw RMS recomputation. Passive inputs leave the training RHS unchanged;
vectorized and individual query evaluations agree to floating-point error.

For the four fitted scalar cases, 64-versus-32 angle RMS sensitivity was
at most 0.00000656. Only the unfinished close opposite-label pair exceeded
the 0.001 quadrature flag, at 0.00243. Reference 256-versus-128 grid
sensitivity was at most 3.78e-8. These are numerical diagnostics, not
rigorous continuum error bounds or convergence in width.

## Most informative next target

The fitted 60-degree opposite-label pair isolates the next approximation
problem particularly well: successful core fitting, small same-input
inconsistency, a close matched block control, but circle discrepancy 0.212.
A refinement of the selective cutoff should be judged on whether it reduces
that off-training error at modest extra state cost. This campaign does not
establish a global small-error guarantee, and no further experiment is
authorized by this note alone.

## Reproduction and evidence

Source files:

- [geometry_tasks.py](geometry_tasks.py): preselected tasks.
- [true_aggregate_selective_fast.py](true_aggregate_selective_fast.py): exact
  compiler optimization, preserving the previous zero-boundary ODE.
- [run_selective_geometry.py](run_selective_geometry.py): cached templates,
  scalar training and all passive input probes.
- [run_geometry_references.py](run_geometry_references.py): unchanged
  canonical and block reference APIs with new tasks registered locally.
- [analyze_selective_geometry.py](analyze_selective_geometry.py): metric
  tables computed from saved predictions; optional plots require matplotlib.
- [check_geometry_results.py](check_geometry_results.py): independent
  saved-state and metric verification.

Generated evidence is under
`data/generated/structured_full_rank_scalar_20260926/selective_geometry_20260927/`:
`scalar/`, `references/`, `compiler/`, `checks/`, and `analysis/summary.csv`.
Each run records its exact command and source/configuration hashes.
The analysis command is:

```bash
OPENBLAS_NUM_THREADS=1 python studies/structured_full_rank_scalar_20260926/analyze_selective_geometry.py --run data/generated/structured_full_rank_scalar_20260926/selective_geometry_20260927
```

The maintained book and APIs were not changed; this is study evidence with
internal independent checks, not a promoted theorem or general guarantee.
