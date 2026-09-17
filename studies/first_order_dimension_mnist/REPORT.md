# First-order closure: individual MNIST prediction fidelity

The completed [PCA98 continuation](PCA_REPORT.md) reduces input dimension from
784 to 240 at P=n=4096. At a common training loss, relative validation RMS
is 4.09–4.62% for the closure versus the PCA network, with 3.75–3.96× faster
fixed-horizon integration and 80.20% lower peak live GPU allocation. Its
relative RMS versus the original-input network is larger, 10.41–11.23%;
the PCA network itself differs from that original reference by about 10%.
The linked report separates representation changes from closure approximation,
with complete prediction exports and passed numerical/audit checks.
The sections below retain their original-input scope.

## Matching training loss at P=n=4096

The user's requested replot uses saved predictions only. The actual-network
reference remains the mean of the three T=600 validation outputs. The target
training MSE is 0.0066432037, the arithmetic mean of the three networks'
individual final losses. Each closure snapshot is chosen solely by its nearest
saved training loss, without using validation agreement, interpolating outputs,
or calibrating their values.

| Closure seed | Saved time | Training MSE | Relative loss mismatch | Validation RMS at equal time | Validation RMS at matched loss |
|---:|---:|---:|---:|---:|---:|
| 1729 | 380 | 0.00664821 | +0.075% | 0.05360 | 0.04371 |
| 2718 | 370 | 0.00675285 | +1.651% | 0.05205 | 0.04352 |
| 3141 | 370 | 0.00664527 | +0.031% | 0.05298 | 0.04511 |

Mean individual-closure RMS falls from 0.0528773 to 0.0441157, a **16.57%**
reduction. Relative RMS is now 4.45–4.61%, versus 5.32–5.48% at equal T=600.
Within-digit correlations improve to 0.973–0.977 for 3s and 0.954–0.958 for 5s.
Both saved snapshots bracketing the target improve over T=600 for every seed;
matching separately to each network's final loss gives the same saved times
for all nine network/closure pairs. The result is therefore insensitive to
this small snapshot-spacing and target-averaging choice.

This supports a contribution from differing training progress to the output
gap. It does not establish that a change of clock eliminates the discrepancy:
network/network seed RMS is still only 0.01916–0.01941. Nor is every image
improved. Sign disagreements are 2, 4, 4 after matching versus 2, 4, 3 before;
the largest individual error rises from 0.35555 to 0.38705. Earlier equal-time
results remain valid for that distinct comparison.

[Side-by-side scatter](../../data/generated/first_order_dimension_mnist/matched_loss4096_001/matched_loss_scatter.png),
[residual plot](../../data/generated/first_order_dimension_mnist/matched_loss4096_001/matched_loss_residuals.png),
[per-image predictions](../../data/generated/first_order_dimension_mnist/matched_loss4096_001/validation_samples.csv),
[complete metrics and provenance](../../data/generated/first_order_dimension_mnist/matched_loss4096_001/summary.json).
The [method](MATCHED_LOSS_PLAN.md) and [independent array/implementation check](MATCHED_LOSS_CHECK.md)
record scope and checks. This is postprocessing of previously audited training
runs, not a fresh training reproduction. Reproduce the analysis with
`MPLCONFIGDIR=/tmp/pde-mnist-matplotlib /home/amir/miniconda3/bin/python -B studies/first_order_dimension_mnist/MATCHED_LOSS.py --output <fresh-directory>`
from the repository root.

## Full P=n=4096 rerun

The requested full rerun uses the same data, preprocessing, three seeds, model, arithmetic, integration steps and validation-based stopping rule as the original 2048 campaign. All three actual networks and all three p=1 closures finish and select T=600. Each closure population has nominal P=4096, represented by 2048 independent base particles and their implicit negative partners. The trained operator remains unrestricted.

For a fair width comparison, use the shared time T=500 and compare each width's closures with its **own three-network mean** on exactly the same 1,000 validation images:

| P=n | Mean individual-closure RMS | Relative RMS across seeds | Mean absolute error across seeds | Sign disagreements / 1,000 |
|---:|---:|---:|---:|---:|
| 2048 | 0.06525 | 6.53–6.87% | 0.04228–0.04438 | 4–5 |
| 4096 | 0.05402 | 5.46–5.59% | 0.03660–0.03713 | 1–4 |

Mean RMS is 17.20% lower in this doubling experiment. Both particle count and network width changed, so it does not isolate either resolution axis or establish convergence at fixed p=1. [Complete same-time width comparison](../../data/generated/first_order_dimension_mnist/width_comparison_001/summary.json).

At the 4096 runs’ final T=600, the per-image comparisons are:

| Closure seed | RMS error | Relative RMS | Mean absolute error | 95th percentile absolute error | Sign disagreements / 1,000 |
|---:|---:|---:|---:|---:|---:|
| 1729 | 0.05360 | 5.48% | 0.03555 | 0.11166 | 2 |
| 2718 | 0.05205 | 5.32% | 0.03502 | 0.10804 | 4 |
| 3141 | 0.05298 | 5.42% | 0.03575 | 0.10738 | 3 |

Within-class correlations are 0.957–0.966 for digit 3 and 0.938–0.942 for digit 5. All nine individual closure/network seed pairings give RMS 0.05224–0.05535 and 1–5 sign disagreements. The remaining discrepancy is larger than the network/network seed RMS spread 0.01916–0.01941. The largest individual-closure error against the network mean is 0.35555; averaging closures reduces ensemble-to-ensemble RMS to 0.05024 but does not replace the individual-closure headline.

Test accuracy is secondary: all networks achieve 99.5268%; the closures achieve 99.3165%, 99.4742%, 99.4217% (mean 99.4041%). The full runs preserve the measured training peak allocations 756.96 MiB (network) and 278.42 MiB (closure). Main network runs use GPU1 and closures GPU0 to finish sooner; the earlier crossed-GPU benchmark in SPEED_4096.md remains the appropriate controlled source for the 1.61–1.77× speed comparison.

- [Final prediction comparison](../../data/generated/first_order_dimension_mnist/validation4096_001/validation_prediction_comparison.png), [per-image CSV](../../data/generated/first_order_dimension_mnist/validation4096_001/validation_samples.csv), [raw trajectories](../../data/generated/first_order_dimension_mnist/validation4096_001/sample_predictions.npz), [worst-image examples](../../data/generated/first_order_dimension_mnist/validation4096_001/worst_validation_images.png), [full metrics](../../data/generated/first_order_dimension_mnist/validation4096_001/summary.json).
- [Secondary loss/accuracy plots](../../data/generated/first_order_dimension_mnist/analysis4096_001/mnist_comparison.png), [Gram movement](../../data/generated/first_order_dimension_mnist/analysis4096_001/gram_movement.png), [secondary metrics and controls](../../data/generated/first_order_dimension_mnist/analysis4096_001/summary.json). The closure reaches lower training loss and greater relative Gram movement, especially in layer 2. Improved output fidelity therefore does not imply identical training losses or hidden features; the Gram plot measures movement from each model's own initialization, not entrywise prediction error.
- [Independent full4096 checks](FULL_4096_CHECK.md). The first T=100 segment matches both earlier speed repetitions bitwise for both models. Full-horizon seed 1729 half-step reruns pass: final validation RMS changes are 1.18e-5 (network) and 5.59e-6 (closure), with no endpoint sign changes. Maximum RMS over all 61 recorded times is 5.84e-4 and 1.15e-4, respectively. These changes are much smaller than the closure/network discrepancy. Direct saved-checkpoint NumPy replay and the late precision probes also check correspondence/arithmetic. No full-horizon same-step bitwise rerun or full-horizon float64 rerun is claimed for 4096.

Commands for this continuation are `BATCH.py full4096`, then `BATCH.py controls4096 --control-model network --control-gpu 0` and `BATCH.py controls4096 --control-model closure --control-gpu 1` once those GPUs are idle. Primary figures/metrics use `VALIDATION_ANALYSIS.py --run-group main4096 --width 4096 --output validation4096_001`; `WIDTH_COMPARE.py` compares them with `analysis_generalization_check_001`, whose scientific metrics reproduce the original 2048 analysis exactly. Secondary figures/controls use `ANALYZE.py --run-group main4096 --control-group controls4096 --width 4096 --output analysis4096_001`. Used-source snapshots and data hashes are retained per run; all output directories are fresh. The six main runs and two controls consume 45.52 summed GPU-process minutes within the declared 50-minute continuation budget. Earlier statements below describe the original 2048 campaign.

## Original P=n=2048 campaign

The first-order closure gives a useful, imperfect approximation of the actual network's validation outputs on MNIST 3 versus 5. This conclusion concerns the **raw prediction of each image**, rather than merely similar classification accuracy. Both models were trained independently from the same training data; the closure was not fitted or calibrated to network predictions.

## Main comparison

The experiment uses all 784 pixel coordinates, 10,552 training images, 1,000 validation images (500 per digit), and all 1,902 relevant official test images. Three actual networks have two hidden layers of width n=2,048. Three p=1 closures use nominal P=2,048 particles per population. The main comparison is at the same physical time T=500, the last time recorded by all six runs.

For each validation image i, let the reference be the mean output of the three actual networks,

\[
\bar f_i^{\mathrm{net}}=\frac13\sum_{s=1}^3 f_s^{\mathrm{net}}(x_i,500),
\qquad e_{s,i}=f_s^{(1)}(x_i,500)-\bar f_i^{\mathrm{net}}.
\]

RMS means \(\sqrt{1000^{-1}\sum_i e_{s,i}^2}\); relative RMS divides this by the RMS of the reference output. The raw targets are +1 for digit 3 and −1 for digit 5.

| Closure seed | Output RMS error | Relative RMS | Mean absolute error | 95th percentile absolute error | Sign disagreements / 1,000 |
|---:|---:|---:|---:|---:|---:|
| 1729 | 0.06378 | 6.53% | 0.04228 | 0.12721 | 4 |
| 2718 | 0.06482 | 6.64% | 0.04268 | 0.13048 | 5 |
| 3141 | 0.06714 | 6.87% | 0.04438 | 0.14153 | 4 |

About 90.7–91.5% of images have absolute error at most 0.1. Overall correlation is 0.99769–0.99791, but the two separated classes can make that number look deceptively strong. Within digit 3 alone, correlations are 0.940–0.945; within digit 5 alone, 0.903–0.927. Thus agreement also captures substantial variation between images of the same digit. As a descriptive reference, returning each image's true ±1 label gives RMS difference 0.17637 from the network mean. That label-only diagnostic uses validation truth; it is not a deployable predictor or a training baseline.

The remaining error is substantial relative to network seed variation. The three network/network pairwise RMS differences are 0.02615–0.02762. Their reference variances differ from closure-versus-ensemble comparisons, so this is context, not an error bound. Across **all nine individual closure/network pairings**, RMS differences are 0.06431–0.07000 with 3–6 sign disagreements. Seed-number matching does not couple initial weights. Averaging the three closures reduces ensemble-versus-ensemble RMS to 0.06044, but this is not the headline individual-closure result.

Agreement is not uniform: the largest individual-closure error against the network mean is 0.56433. The worst-image panel deliberately shows the largest discrepancies between the two model means. Raw values for all six runs and all 1,000 images are exported, including errors that reverse the predicted class.

- [Primary plot](../../data/generated/first_order_dimension_mnist/validation_analysis_002/validation_prediction_comparison.png): top left is raw prediction agreement; the diagonal is exact agreement. Top right shows signed errors. Bottom left tracks equal-time RMS; the dashed curve is mean network/network seed difference. Bottom right includes the complete absolute-error distribution. Orange scatter points are 3s; blue points are 5s.
- [Every validation image's predictions](../../data/generated/first_order_dimension_mnist/validation_analysis_002/validation_samples.csv), [all shared-time prediction arrays](../../data/generated/first_order_dimension_mnist/validation_analysis_002/sample_predictions.npz), [complete metrics](../../data/generated/first_order_dimension_mnist/validation_analysis_002/summary.json), [worst-image panel](../../data/generated/first_order_dimension_mnist/validation_analysis_002/worst_validation_images.png).

## Secondary observations

Validation-only checkpoint selection chose T600 for all networks and T600, T500, T500 for the closures. At those independently selected checkpoints, test accuracy is **99.474%** for each network and **99.264%, 99.422%, 99.316%** for the closures (mean 99.334%). These are supporting results, not the prediction-fidelity criterion. The selected-time comparisons must not be presented as equal-time comparisons.

Features move appreciably. On the fixed 64-input training/validation panel, seed1729's relative Gram changes from initialization at T500 are 0.741 and 2.119 for the network's first and second hidden layers; closure changes are 0.792 and 2.114. These movement norms show that this was a feature-learning regime. Similar movement magnitudes alone do not establish entrywise Gram agreement.

The preceding d=8 regression sanity check used 24 training directions and 512 independent test directions, with target tanh(2u₁−1.5u₂)+0.35 sin(3u₃). Across two seeds, selected test MSE was 0.01556–0.01633 for p=1 and 0.01694–0.01807 for the network. This is a small sanity check, not a performance ranking.

[Loss, accuracy and test plots](../../data/generated/first_order_dimension_mnist/analysis_001/mnist_comparison.png), [Gram movement plot](../../data/generated/first_order_dimension_mnist/analysis_001/gram_movement.png), and [secondary metrics](../../data/generated/first_order_dimension_mnist/analysis_001/summary.json).

## Computation and the general-dimensional construction

Both engines run on RTX3090 GPUs with device-resident data, blocked full-batch sums and explicit Heun integration. X1 improvements cache fixed weighted bases, reuse buffers, and select matrix multiplication association by arithmetic cost. Numerical equivalence is checked before timing. The representative identical-formula benchmark improved from 2.411 ms to 2.178 ms per RHS, about 1.1×. This is a modest measured improvement, not an optimality claim; full campaign timing also depends on numerical step size and horizon.

The general-d p=1 initializer reduces population coefficient construction to scalar/two-dimensional integrals and repeated small covariance blocks, avoiding a high-dimensional empirical Gram and dense Cholesky. Its lower and upper dictionaries have dimensions 2d+1 and d+1. The reverse-response term is retained. The learned operator remains a full matrix: initial coordinate-diagonal structure is never imposed during training.

An explicitly chosen sign-paired quadrature uses P/2 independent base draws and their negatives. Exact symmetry permits storing only the base half and omitting inactive constant features. P=2,048 therefore means 1,024 stored base rows per population; it does **not** mean 2,048 independent draws or paired neural-network neurons. This quadrature choice is distinct from X1's algebraically equivalent implementation changes.

The moving closure state requires O(Pd+d²) scalars versus O(nd+n²) for the network. With P=n and fixed d, that removes the quadratic dependence on width. There is no uniform saving when d grows with n. Fixed marks, caches, input data, integrator stages and checkpoint copies also cost memory.

| Measured/countable quantity, d=784 and n=P=2,048 | Actual network | p=1 closure |
|---|---:|---:|
| Moving state | 22.13 MiB | 7.76 MiB |
| Retained current model plus initial/fixed arrays and caches | 44.27 MiB | 33.89 MiB |
| Peak live GPU allocation during main training | 320.16 MiB | 207.32 MiB |
| Integration seconds per physical time unit, three-seed range | 0.169–0.186 | 0.176–0.180 |

Peak training allocation includes working tensors and the retained best checkpoint, excludes the later optional float64 probe, and is not reserved GPU memory or whole-system usage. Moving state is 2.85× smaller and measured peak allocation about 35% lower. At this size, runtime is approximately comparable. Both use the same precision, but the validated closure step is half the network step.

[Initialization derivation](INITIALIZATION_THEORY.md), [computation checks and timings](COMPUTE_REPORT.md), [model/counting audit](MODEL_SCOPE_CHECK.md).

## Numerical reliability and scope

Both models are bias-free two-hidden-layer tanh models with scalar output, unhalved mean squared training loss and the canonical physical metric. The actual network uses stored Gaussian variances (1,1/n,1/n²), output cᵀh₂/n and block mobilities (n,1,n). The closure begins with c=0, matching the limiting small-readout convention; the finite network keeps its small random initial readout. Normalized image rows u have unit length and represent x/√d; no additional dimension normalization is applied.

The original MNIST files come from the [CVDF mirror](https://github.com/cvdfoundation/mnist/blob/master/README.md), with canonical checksums verified against [torchvision's dataset source](https://docs.pytorch.org/vision/stable/_modules/torchvision/datasets/mnist.html). Preprocessing uses all pixels divided by 255, followed by per-image Euclidean normalization. No PCA, centering, augmentation or test-fitted transform is used. Validation IDs are sampled only from official training data using seed20260915. The prepared archive SHA256 is `bc18a91521dff93f563a3828a0ba3d941ac7f23436978db7810aeeee06ef8c7f`.

Training and stopping never use test labels or network/closure agreement. Continuation starts with T200 and adds 100 while validation MSE improves by at least 0.001 over the previous 100, capped at T600. The validation set consequently participates in stopping and is not an untouched final test set. Common T500 follows the last shared recorded time; it was not chosen to minimize prediction discrepancy.

Coarse-step pilots failed and are retained. Refined production steps are 0.25 for the network and 0.125 for the closure, float32 with TF32 disabled. Full-data, seed1729, half-step reruns through T600 give final validation RMS changes **2.13×10⁻⁵** and **1.02×10⁻⁵**, with unchanged classification signs. Maximum RMS over all recorded times is 5.71×10⁻⁴ and 9.61×10⁻⁵, respectively. These are much smaller than the observed closure/network discrepancy.

Float64 algebraic oracles, toy trajectories, initial MNIST pilots and late same-state continuation checks support the arithmetic choice. The final closure pilot's precision comparison was at step0.25, while its separate step-refinement check selected0.125; the late production probe uses the actual production step. Late probes change predictions by RMS below7×10⁻⁸. They do not bound accumulated full-horizon floating-point error; no full T600 float64 MNIST rerun was performed. Gaussian coefficient refinement is a numerical diagnostic, not a certified integration-error bound.

Independent NumPy replay reconstructs saved checkpoint predictions and Grams from raw arrays, without importing either engine. All six main runs pass, with maximum prediction discrepancy below4.88×10⁻⁷ and zero sign changes. A separate raw-IDX audit reconstructs every split ID, label and normalized pixel. The primary metric audit checks all 51 shared times, all nine seed pairs and all exported image identities. Fresh seed1729 training reproductions for both models match **every one of the 61×1,000 saved validation outputs bitwise**, including selected times and signs. Full evidence is retained in the [runner audit](REVIEW_RUNNER.md).

These are internally checked finite experiments and construction identities, not established book results. Fixed p=1 leaves a truncation approximation; three seeds, one digit pair and one main width do not establish a high-dimensional convergence theorem. The optional width4096 diagnostic was deferred in favor of full-horizon numerical and reproducibility controls. No higher-order MNIST comparison was run, so this experiment says nothing directly about improvement with closure order.

## Reproduction

All commands run from the repository root using `/home/amir/miniconda3/bin/python`. Sources and notes remain flat in this study. Data, source snapshots, configurations, checkpoints and results remain under `data/generated/first_order_dimension_mnist/`.

`DATA.py` prepares/verifies the digit dataset. `PILOT_GATE.py` reconstructs the checked numerical gate from retained pilot arrays, explicitly recording the source step of its precision check. It writes a fresh file; the consumed original gate is preserved. `BATCH.py main`, `controls`, and `reproduction` are the executed bounded waves; existing destinations deliberately prevent overwriting. To repeat a single main trajectory into a new directory, use a fresh output name:

```sh
/home/amir/miniconda3/bin/python -B studies/first_order_dimension_mnist/RUN.py \
  --task mnist --model network --width 2048 --seed 1729 --dtype float32 \
  --gpu 0 --step 0.25 --horizon 200 --continue-validation --block 2048 \
  --max-seconds 240 --output fresh_check/network_1729
```

For the matching closure, use `--model closure --gpu 1 --step 0.125` and a separate fresh output. Repeat seeds2718 and3141 for the main ensemble. `VALIDATION_ANALYSIS.py --output <fresh-analysis-name>` and `ANALYZE.py --output <fresh-analysis-name>` analyze the retained main paths; their source identifies every consumed run. `REPLAY.py --audit-analysis <analysis-directory> --output <fresh-audit-directory>` independently verifies the primary metrics. Run snapshots and per-source hashes, rather than Git HEAD alone, identify the actual implementation used.
