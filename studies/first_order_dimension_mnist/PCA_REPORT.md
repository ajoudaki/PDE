# PCA98: first-order closure fidelity and compute savings

The PCA continuation is complete. Reducing the input from 784 to 240 dimensions
makes the p=1 closure 3.75–3.96× faster than the reduced-input network and cuts
its peak live GPU allocation by 80.20%. At a common attainable training loss,
its relative validation prediction RMS against that network is 4.09–4.62%,
similar to the original-input closure/network comparison (4.35–4.54%).

Preserving the original network's predictions is a different outcome: the
PCA closure differs from them by relative RMS 10.41–11.23%, and the PCA
network itself differs by 9.96–10.04%. Thus PCA delivers substantial compute
savings while retaining good closure-to-network fidelity on the reduced
representation; it also changes the learned prediction map. These are finite
three-seed results on MNIST 3 (+1) / 5 (-1), with P=n=4096. Raw per-image
validation agreement is the primary accuracy criterion.

## Input representation

PCA is fitted only to the 10,552 training rows of the existing normalized
784-pixel data. Ordinary centered PCA retains **240 components**, the smallest
dimension retaining at least 98% of centered variance: **98.00167%** at 240,
versus 97.98198% at 239. The same training mean and basis transform all 1,000
validation and 1,902 test inputs. Labels and image IDs are unchanged. There is
no whitening or post-projection renormalization.

The transform is `z=(u-mean_train)@components.T`, where `u` denotes the
original model input. Both engines consume z directly; the canonical raw
input interpretation is `x_new=sqrt(240)*z`. No extra dimension multiplier is
inserted. Models retain two hidden tanh layers, no biases, the stored Gaussian
initialization and physical gradient metric, and unhalved training MSE. The
closure remains order p=1 with its full learned operator. Nominal P=4096 uses
2048 independent base marks plus implicit negative partners per population.

The 98% statement concerns variance around the training mean. Centering also
changes the input geometry and scale seen by these bias-free nonlinear
models. Projected inputs retain 53.05% of the original uncentered squared
energy, since centering removes a mean component containing 45.87% of it.
Accuracy differences cannot be attributed solely to discarding the last
2% of centered variance. The mean is preserved in the transform archive for
reconstruction. Fitting, transforming all splits and writing the prepared
data take 1.17 CPU wall seconds, with 306.10 MiB peak CPU-process RSS including
Python/loading. This is separate from GPU training allocation.

## Measured computation

The following fresh benchmark runs integrate through the same physical T100,
using network step 0.25 and closure step 0.125, float32 with TF32 disabled and
full-batch sums blocked at 2048. Each model runs once on each RTX3090; the
second repetition swaps GPU assignments and reverses original/PCA order.
Integration timing synchronizes each step and excludes initialization,
observations and serialization. Complete training-loop timing is retained
separately. The ratio ranges below always compare the same physical GPU.

| Inputs and model | Input dimension | Integration time to T100 | Peak live GPU training allocation |
|---|---:|---:|---:|
| Original actual network | 784 | 49.68–63.03 s | 756.96 MiB |
| Original p=1 closure | 784 | 30.29–33.43 s | 278.42 MiB |
| PCA actual network | 240 | 44.99–52.73 s | 659.07 MiB |
| PCA p=1 closure | 240 | 12.01–13.30 s | 130.52 MiB |

| Candidate relative to reference | Integration speedup | Peak GPU memory reduction |
|---|---:|---:|
| Original closure versus original network | 1.64–1.89× | 63.22% |
| PCA closure versus PCA network | 3.75–3.96× | 80.20% |
| PCA closure versus original network | 4.14–4.74× | 82.76% |
| PCA closure versus original closure | 2.51–2.52× | 53.12% |

PCA lowers the network's integration time by 9.43–16.34%, versus 60.20–60.35%
for the closure. At fixed width the dense network retains its 4096 × 4096
hidden matrix, whereas the p=1 learned operator shrinks from 784 × 1568 to
240 × 480. This accounts for the different dimension dependence in these
implementations; the finite measurements do not establish asymptotic speed
factors. Both implementations also retain activation buffers and other working
memory beyond the moving parameter arrays.

Network timing varies by more than 15% across the two devices/repetitions, so
the observed ranges should not be read as precise universal speed ratios.
Peak live allocation is PyTorch-allocated memory including working tensors
and the best-checkpoint copy, not reserved memory or whole-system GPU usage.
All repeated training/validation predictions and Grams are bitwise equal;
original-data benchmark prefixes also reproduce the earlier full runs.

## Per-image validation fidelity

All six PCA scientific runs reach T600, matching the existing six original-input
runs. They use seeds 1729, 2718 and 3141 and the same 1,000 validation image
IDs. Each candidate is compared with the three-network mean for the stated
reference representation. RMS is computed over individual images, then
averaged across candidate seeds; relative RMS divides each candidate's RMS
by the RMS of that reference output. No output calibration is used. The
analysis also retains all nine individual candidate/network seed pairings.

The most comparable fit-level diagnostic selects one attainable target
training MSE, **0.011080311898**, the largest terminal training MSE across all
twelve runs. Every run independently selects its nearest saved training-loss
snapshot. Original networks select T460, original closures T300/290/290,
PCA networks T600, and PCA closures T570. Actual losses differ from this
target by at most 1.85%; selection uses no validation predictions.

| Candidate versus reference network mean | Mean individual RMS | Relative RMS across seeds | Sign disagreements / 1,000 |
|---|---:|---:|---:|
| Original closure versus original network | 0.04318 | 4.35–4.54% | 2–3 |
| PCA closure versus PCA network | 0.04163 | 4.09–4.62% | 3–5 |
| PCA closure versus original network | 0.10531 | 10.41–11.23% | 5–9 |
| PCA network versus original network | 0.09750 | 9.96–10.04% | 4–5 |

![Common training-loss comparison](../../data/generated/first_order_dimension_mnist/pca_analysis_001/pca_common_training_loss.png)

Horizontal position is the actual-network mean output for an image; vertical
position is one candidate model's output for that same image. All three
candidate seeds are overlaid. Orange denotes digit 3 and blue digit 5. The
dashed diagonal denotes identical predictions. The top row measures closure
fidelity within each representation. The bottom row measures changes from
the original-input network; the bottom-right candidate is itself a network.
The common-loss comparison shows that the representation effect persists
after controlling approximately for training loss. It does not isolate
centering, discarded directions, input scale, and finite-seed effects.

At equal physical T600 the corresponding mean RMS values are 0.05288,
0.04060, 0.10474 and 0.09842. The PCA closure's within-digit correlations
against its own network mean are 0.979–0.984 for digit 3 and 0.977–0.981
for digit 5, providing a check beyond separation of the two classes.

A separate diagnostic keeps each representation's network fixed at T600
and matches closures to its mean final training loss. Original closures
select T380/370/370 and give mean RMS 0.04412; PCA closures select T570
and give 0.04163. Matching loss improves the original comparison but slightly
worsens the PCA comparison. Neither PCA model reaches the original networks'
mean T600 training MSE 0.0066432 during the recorded horizon, so that particular
cross-representation loss match is unavailable and is not extrapolated.
[Equal-time and own-reference loss plots](../../data/generated/first_order_dimension_mnist/pca_analysis_001/pca_validation_comparison.png)
retain both diagnostics.

Speed factors above concern fixed-T100 integration work. They are not measured
time-to-matched-loss claims; the scientific prediction comparisons use T600
or their explicitly stated training-loss snapshots.

## Classification and full-run costs

Classification is secondary to prediction fidelity. All twelve main runs
select their T600 checkpoint using the existing validation rule; official
test outputs are evaluated after selection. Ranges below are across three
seeds, not confidence intervals.

| Model | Final training MSE | Validation accuracy | Mean official-test accuracy |
|---|---:|---:|---:|
| Original network | 0.00662–0.00668 | 99.1–99.4% | 99.53% |
| Original closure | 0.00233–0.00245 | 99.2–99.3% | 99.40% |
| PCA network | 0.01090–0.01108 | 98.8–99.1% | 99.09% |
| PCA closure | 0.00991–0.01004 | 98.6–98.8% | 98.93% |

The reduction changes both final training loss and validation accuracy at
this horizon. It does not show a permanent limit on accuracy after further
training. [Loss trajectories](../../data/generated/first_order_dimension_mnist/pca_analysis_001/pca_training_losses.png)
and every recorded prediction are retained.

The three complete PCA-network integration times are 274.12 s (GPU1),
306.67 s (GPU0), and 273.64 s (GPU1). PCA closures take 82.18 s (GPU0),
78.61 s (GPU0), and 73.85 s (GPU1). These scheduling choices serve completion
time; the crossed benchmark above supplies the controlled same-GPU ratios.
The fresh benchmark, six main PCA runs and two numerical controls together
consume 35.74 summed GPU-process minutes, within the declared 40-minute cap.
Original scientific trajectories are reused; original timing was rerun in
the fresh benchmark. No further training is queued.

## Numerical checks and limits

The PCA preparation checks pass, including independent centered-matrix SVD,
minimum retained dimension, direct reconstruction and exact saved projections.
The arbitrary-norm CPU engine checks pass, preserving actual gradients and
antithetic folding without extra input scaling. Both fresh full-data
seed 1729 half-step controls pass the declared RMS/accuracy gates at all 61
saved times. Final validation RMS changes are 8.46e-6 for the network and
3.39e-6 for the closure; maxima over saved times are 4.69e-4 and 1.10e-4.
Neither control changes a classification sign at any saved time. All six main
PCA checkpoints and both controls pass direct NumPy replay of their saved
arrays, with maximum prediction discrepancy 1.14e-6 and zero sign changes.
An independent recomputation verifies 5,607 scalar analysis metrics, all
four comparisons and nine seed pairs each, and every exported per-image
NPZ/CSV prediction. Maximum metric discrepancy is 3.20e-14.

These are internally checked numerical results, not a theorem of
high-dimensional trained-network convergence. Remaining limits include one
digit pair, three seeds, fixed p=1, finite n/P, the recorded finite horizon,
and no full-horizon float64 or same-step bitwise training reproduction.
The short timing repetitions are bitwise reproducible; the full half-step
runs check step-size sensitivity.

## Evidence and reproduction

[Plan](PCA_PLAN.md), [PCA preparation and checks](PCA_DATA_CHECK.md),
[independent benchmark audit](PCA_SPEED_CHECK.md),
[benchmark data](../../data/generated/first_order_dimension_mnist/pca_benchmark_analysis_003/summary.json).
The independent engine/control record is [PCA_RUN_CHECK.md](PCA_RUN_CHECK.md).
[Complete scientific metrics and provenance](../../data/generated/first_order_dimension_mnist/pca_analysis_001/summary.json),
[per-image CSV](../../data/generated/first_order_dimension_mnist/pca_analysis_001/validation_samples.csv),
[prediction arrays](../../data/generated/first_order_dimension_mnist/pca_analysis_001/sample_predictions.npz),
and [completion manifest](../../data/generated/first_order_dimension_mnist/pca_completion_manifest.json)
retain the final outputs and checks.
Sources remain flat in this study and generated products remain in its
generated namespace. No earlier results are overwritten or promoted.

Run from `/home/amir/Codes/PDE` using `/home/amir/miniconda3/bin/python -B`:
`PCA_DATA.py` prepares fresh data, `PCA_BATCH.py benchmark` runs the crossed
timing wave, `PCA_BATCH.py gate` runs seed 1729 and its half-step controls, and
`PCA_BATCH.py remaining` requires the recorded passing gate. The actual
commands include the `studies/first_order_dimension_mnist/` prefix.
`PCA_ANALYZE.py --output <fresh-output>` produces figures and all per-image
metrics after training. Run-directory snapshots and exact hashes identify
the used versions; existing output directories deliberately block overwrites.
