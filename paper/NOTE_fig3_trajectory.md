# Figure 3: denser shared-time capture completed

Updated on 2026-09-27 after pulling merged `main` at `5c30c04`.
The selected archives contained only eight shared circle-prediction checkpoints;
their denser time records held losses, not query predictions or restart states.
We therefore replayed this one task. No study sources or archived runs changed.

## Data and protocol

The figure now uses **39 genuine shared checkpoints**: initialization, 32
geometrically spaced times from 0.5 to 80, and the original shared times
1, 2, 5, 10, 20, 40, 80 (deduplicated). The lower log-time panel has 38
positive-time measurements. The four radial panels remain at 0, 5, 20, 80.
The integrator lands on each requested time; predictions are not interpolated.

Preserved model: paired-label circle task, eight training samples, two hidden
tanh layers, width 2048, seed 20260920, unhalved mean squared loss, canonical
mobilities, and the original Gaussian initialization. Queries are the same
2048 circle directions. Initial weights match all three original SHA-256 hashes.

Eight runs cover dense and P1/P3/P7 at two numerical resolutions. All use
float64 adaptive explicit Heun, the original error controllers and, for the
closures, the original rational activation lift. The closure modules are
loaded from `studies/neural_response_memory_20260922/legacy_experiments.zip`;
their hashes exactly match the original experiment records. Dense uses
rtol 1.5625e-5 / 3.90625e-6 and closures use 6.25e-5 / 1.5625e-5; atol is
rtol/100. All models continue to physical time 80 rather than stopping at a
training-loss threshold. No parameter tuning or further tasks were run.

Each model had a 300-second/30,000-trial cap. All eight completed on one
RTX 3090, in **110.27 seconds total model runtime** (setup and queries included;
interpreter startup, final bundle writing and plotting excluded).

## Checks and interpretation

The independent small-network loss-gradient and reconstructed-matrix checks
had maximum absolute discrepancy 3.82e-17. All shared predictions have shape
`(39, 2048)` and are finite. Every RMS and sensitivity value was independently
recomputed. All nontrajectory arrays in the portable bundle are unchanged.

At the original eight checkpoints, maximum RMS changes from the archived
fine predictions were:

| Model | Largest change |
|---|---:|
| Dense | 4.23e-6 |
| P1 | 1.12e-6 |
| P3 | 2.80e-6 |
| P7 | 1.66e-6 |

All passed the predeclared replay check (5e-6 plus twice the old combined
sensitivity at each checkpoint). Changes arise because the denser observation
schedule changes adaptive step boundaries. This is a numerical replay check,
not a continuous-flow error certificate.

At time 80, dense-discrepancy RMS is 0.0361423 / 0.00207208 / 0.000175201
for P1/P3/P7. The coarse/fine sensitivity scales are respectively
6.43e-5 / 6.47e-5 / 6.36e-5. Sensitivity is the **sum of the separate dense
and closure coarse/fine prediction RMS changes**, not a confidence interval.
The smallest early discrepancies remain comparable to or below that scale.

The lower panel uses log time, small measured points and thin connecting
guides. Light shading extends from the axis floor to each order's sensitivity
scale; it does not assert a bound around the error curve. The plot occupies
about two-thirds of the figure width, with the key alongside it. No spline
smoothing or fabricated measurements are used. The rank plot is unchanged.

## Files and reproduction

- `figures/capture_trajectory.py`: bounded capture and replay checks.
- `figures/response_memory_source.npz`: updated portable bundle with the same
  `common_*` keys, plus coarse predictions so sensitivity can be recomputed.
- `figures/trajectory_capture_manifest.json`: protocol, source/input hashes,
  environment, timings, all archive checks and bundle validation.
- `scripts/tikz_figures.py trajectory`: render the updated `figures/trajectory.pdf`.

The bundle retains the old selected-archive metadata under `trajectory_previous`
and the new protocol/results under `trajectory_capture`. The per-run original
records and the previous bundle are retained locally in
`/tmp/pde-trajectory-capture-20260927`; all predictions needed for the current
figure and sensitivity are also in the portable bundle.

From the repository root, redraw without training:

```bash
OPENBLAS_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B \
  paper/scripts/tikz_figures.py trajectory
```

To reproduce training, use a fresh output directory and an available GPU:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B \
  paper/figures/capture_trajectory.py --device cuda:1 \
  --out /tmp/paper-trajectory-new --per-run-seconds 300
```

Capture writes a candidate bundle in that new directory and never overwrites
the paper bundle. The script requires NumPy, PyTorch and the preserved solver
ZIP; rendering requires NumPy, TikZ and pdflatex. It needs no other study's data.
The scientific comparison remains one finite-width, single-seed task.
