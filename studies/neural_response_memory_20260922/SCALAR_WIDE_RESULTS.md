# Width2048 matched-loss scalar results

The canonical width2048 GPU dense networks and order4 scalar systems all
reach training MSE1e-6. Increasing the dense width does not remove the
eight-input scalar candidate's large full-circle error. Order4 nevertheless
improves substantially over the frozen-kernel order2 control, motivating the
separately authorized order5/6 continuation in SCALAR_HIGH_ORDER_PROTOCOL.md.

These are empirical finite-width results for the exact declared three-hidden
layer tanh model, not a population limit or a verdict on all scalar closures.
Every comparison uses each model's own first detected MSE1e-6 crossing.

| Inputs | Seed | Dense time | Order4 time | Order2 circle RMS | Order4 circle RMS |
|---:|---:|---:|---:|---:|---:|
|4|20260920|16.6442|43.6271|.191298|.174756|
|4|20260927|16.6864|45.6936|.192063|.170470|
|8|20260920|158.017|46056.6|160.449|39.2742|
|8|20260927|154.449|47815.4|193.555|63.8109|

The two eight-input improvements are4.09x and3.03x. Order4 errors are still
25.90x and41.41x the RMS size of the respective dense functions. The models
fit all eight labels while extrapolating differently outside the training arc.
The four-input errors lie in the preregistered .1–.2 indifference interval;
the eight-input errors are adverse under the >.2 criterion.

## Numerical and implementation evidence

All dense and scalar tolerance comparisons pass. Largest dense endpoint
refinement change is9.20e-5 RMS; largest scalar change is3.25e-5. The maximum
relative dense fitting-time change is4.00e-4 and scalar change9.59e-6, below
.001. Peak scalar passive-training discrepancies remain below2.00e-6, versus
the1e-4 gate. Nested512/1024 circle quadrature and mode64 Fourier encoding
pass for every configuration. No conditional refinement branch was needed.

The first eight-input configuration was repeated from freshly regenerated
initial parameters and all original coefficients, including passive probes.
The dense and scalar fine trajectories reproduce their endpoints bit for bit.
Five exact initialization tests pass, and the width2048 legacy four-probe
comparison differs by at most1.12e-16 in any coefficient tensor. Dense adapter
tests check canonical arithmetic, GPU/CPU agreement, serialization and caps.
The independent saved-data audit is recorded in SCALAR_WIDE_AUDIT.md.

The new initializer factors parameter derivative directions exactly; it does
not approximate the initialized Gaussian matrices. The scalar solver uses
only scalar tensors after this one-time initialization. No future dense
trajectory, refreshed population or dense output enters scalar training.

Hidden activations move substantially in the dense reference: RMS change
relative to initial RMS is .56–1.21 across layers on the four-input task and
1.03–1.52 on the eight-input task. The references therefore exhibit feature
learning at this finite width; one width alone does not show width convergence.

## Cost and interpretation

| Inputs | Seed | Coefficient initialization, CPU seconds | Order4 run, CPU seconds | Dense integration, GPU seconds |
|---:|---:|---:|---:|---:|
|4|20260920|17.215|.241|11.822|
|4|20260927|16.342|.233|12.029|
|8|20260920|61.482|6.331|26.918|
|8|20260927|58.233|8.623|29.246|

Dense runs use one RTX3090, float64 and deterministic algorithms with TF32
disabled. Initialization uses CPU BLAS, and the scalar integration uses one
CPU thread. Scalar run timing includes readout/saving; dense integration
timing excludes those operations. These are measured implementation costs
on different hardware, not an accuracy-matched speedup claim. The scalar
candidate is cheaper to integrate but initialization dominates this setup.

The eight-input order4 ODE has584 evolving training scalars plus584 local
signature scalars and4096 frozen highest-order coefficients. Its dense
reference has8,394,752 moving parameter scalars. Passive query coefficients
cost additional storage:622,440 scalar entries for1064 probes. The final
mode64 Fourier encoding has129 real coordinates. Width independence of
these scalar counts does not imply independence of sample count or order.

## Reproduction and artifacts

SCALAR_WIDE_PROTOCOL.md fixes the original design. run_scalar_wide.py prepares,
integrates and scores; launch_scalar_wide.py sequences GPU and CPU lanes.
scalar_wide_initialization.py and scalar_wide_dense.py implement the optimized
exact initialization and canonical dense adapter. analyze_scalar_wide.py reads
saved arrays and produces the endpoint table and figures without training.

All paths below are under data/generated/neural_response_memory_20260922/:

- scalar_wide_configs01: literal execution configurations.
- scalar_wide_source01: original coefficients, source snapshots and hashes.
- scalar_wide_primary01: both tolerances of all four configurations and scores.
- scalar_wide_source_reproduction01 and scalar_wide_reproduction01: fresh repeat.
- scalar_wide_analysis01: endpoints.csv, analysis.json, three PNG/PDF figure pairs.
- scalar_wide_audit* receipts: independent arithmetic, replay and provenance checks.

The implementation-only postrun change to run_scalar_wide.py filters directory
searches so adjacent log/configuration files are not mistaken for runs. Original
source snapshots and corrected reproduction snapshots are both retained. No
scientific equation, initial coefficient, solver or threshold changed.

This bounded stage is complete. The user-authorized higher-order stage remains
separate and must pass its own coefficient, integration and reproduction checks.
Nothing is promoted to maintained documentation or code.
