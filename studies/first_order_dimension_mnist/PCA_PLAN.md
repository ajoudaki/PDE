# PCA98 dimension and computation continuation

The user explicitly requests rerunning the current MNIST network/closure
comparison after PCA, with accuracy versus time/memory savings. This continues
the same general-dimensional p=1 investigation and its original-input baseline.
All source/evidence remain flat in this study; generated products stay in its
existing generated namespace. No other study is an input and no promotion is
attempted. Shared Git state is preserved.

## Fixed comparison

Use the existing MNIST3(+1)/5(-1) split: 10,552 training, 1,000 validation,
1,902 official-test examples. Fit ordinary centered PCA to saved normalized
training inputs only, float64 covariance eigendecomposition, smallest dimension
retaining at least98% of centered training variance. Use the same fixed mean
and orthonormal projection for validation/test. No whitening, no post-PCA
renormalization. Record that centering changes inputs as well as truncation;
98% is variance around the training mean, not raw uncentered signal energy.

Both models retain two hidden tanh layers without biases, canonical initial
Gaussian scaling and physical mobility, unhalved training MSE, P=n=4096,
float32 with TF32 disabled, blocked full-batch Heun. Nominal closure P uses
2048 independent base draws with implicit negative partners per population;
the full evolving operator remains unrestricted. Main steps remain0.25
network and0.125 closure. Use seeds1729,2718,3141 and save outputs every10.

Run both PCA models to fixed T600 for direct comparison with the completed
original-input T600 runs. Validation selects secondary checkpoints on the
existing eligible clock; test is evaluated only after selection. Report
terminal and selected validation/test metrics with their own times explicitly.
The training trajectories are not stopped or selected for agreement with each
other. No claimed learning-rate or architecture improvement is sought.

## Outputs and controls

Primary: raw sample-by-sample validation prediction RMS, relative RMS, MAE,
within-digit correlation and sign disagreements. Show p1 versus actual-network
mean separately on PCA and original inputs at equal T600 and at matched
training loss (nearest saved closure snapshot; no validation fitting).
Also compare PCA network and PCA closure to original-network predictions on
the same image IDs, to expose the total effect of preprocessing plus closure.
Retain all nine model-seed pairs and per-image exports; accuracy is secondary.

Compute peak live training GPU allocation, moving/retained state, integration
time and complete training-loop time. Benchmark both models on both input
representations at fixed T100 with two repetitions, swapped GPU assignments
and reversed input-order scheduling: eight short fresh runs. Use same-GPU
ratios, separate initialization/serialization from integration, include PCA
fit/transform cost separately. Do not infer asymptotic complexity from ratios.
If repeated times differ by >15%, show the observed range and flag precision
rather than repeating indefinitely.

Full-data seed1729 half-step reruns through T600 check both PCA models:
validation RMS at every saved time <=0.002 and accuracy change <=0.2 percentage
points, with endpoint signs explicitly recorded. If a gate fails, preserve
failure and permit one step refinement and its control before any more seeds;
otherwise use unchanged steps. Check saved endpoint predictions independently
from weights. The PCA producer gets independent trace/orthogonality/projection
checks, including minimum component count and unchanged IDs/labels. Same-data
short benchmark repetitions check deterministic trajectory reproduction.

Lower cost with comparable raw-output fidelity supports a useful reduced-input
tradeoff; poorer fidelity is retained as an adverse outcome. Improved
classification alone does not meet the primary prediction-fidelity question.
No high-dimensional convergence or invariance of p1 under PCA is claimed.

An additional saved-data comparison matches all four model/representation
groups to one attainable training loss: the largest terminal training MSE
among all twelve scientific runs. Each run independently selects its nearest
saved training loss, using no validation values. This is declared before the
remaining seeds finish and avoids extrapolating the PCA models to the original
network's lower terminal loss. Report actual loss mismatches and selected
times; compare both within-representation pairs and PCA/original outputs at
that common fit level. It requires no extra training or time-to-target claim.

## Budget and ownership

At most40 additional summed GPU-process minutes, 6GiB additional generated
products, 18GiB live GPU allocation and10 CPU minutes of PCA/analysis/checks.
Main/benchmark/control process limits are600/180/850 seconds respectively.
One job per GPU; no hidden multijob timing contention on one GPU. Stop after
the six PCA trajectories, numerical controls, crossed benchmark and report;
no additional scientific data or digit pairs. If a hard budget or numerical
gate blocks completion, report the partial outcome and unresolved comparison.

Scheduling refinement before the remaining-seed wave: once both full-horizon
numerical gates pass, place seed2718's network then closure on GPU0 and
seed3141's network then closure on GPU1. This balances the two expensive dense
network jobs across the cards. It changes neither the scientific configuration
nor the controlled same-GPU benchmark; repeated benchmark predictions already
agree bitwise across these devices. Gate-wave seed1729 remains networkGPU1/
closureGPU0.

Root owns RUN.py changes, PCA_BATCH.py, PCA_ANALYZE.py, this plan and README/
report. Scoped PCA contributor owns PCA_DATA.py, PCA_DATA_CHECK.md and generated
data_pca98/pca_data_check. Engine reviewer owns PCA_RUN_CHECK.md, REPLAY.py
adaptations if needed, and generated pca_checks. All are scoped to this study
and permitted established dependencies; no contributor runs unassigned GPU
work. Previous artifacts and completion manifests remain unchanged.
