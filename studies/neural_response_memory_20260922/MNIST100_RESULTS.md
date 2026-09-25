# MNIST with 100 training images and width 4096

The response-history closures closely reproduce the dense network on 1984
held-out images with learned-correction rank bounded by 100,200,300. All eight
primary trajectories reached training MSE .001, and every predeclared
numerical-resolution gate passed. Fresh dense/P3 repetitions on the opposite
GPUs reproduce every scientific output array and all five checkpoint states
bit-for-bit. The bounded campaign is complete.
These are finite experiments, not a population theorem or an asymptotic rate.

## Design

Digits 3 and 8; 50 training examples of each, selected without replacement from
the previous 1000-image training panel by fixed seed 20260924. The complete
official-test 3/8 panel remains unchanged: 1010 threes and 974 eights. Inputs
are 784 pixels normalized individually to Euclidean length one. No PCA,
augmentation, whitening, centering or validation-fitted transformations.
Labels are -1 for 3 and +1 for 8. Exact IDs and parent positions are retained.

Two tanh hidden layers, each width 4096, no biases, canonical Gaussian
initialization and physical block mobilities (n,1,n), unhalved MSE. Every model
shares the exact initial weights and training data. Full-batch gradient flow
is integrated by float64 adaptive Heun/Euler; no Adam, minibatch SGD or direct
factor optimization. The equations and scientific runner are unchanged from
the earlier experiment. P counts history modes per sample. The fixed W0 and
its actual transpose remain; only the learned correction uses moments.

Each model stops at its own first training-MSE .001 crossing. This is a
matched-training-loss comparison, not equal-time or infinite-time comparison.
Primary RMS is sqrt(mean_validation((closure_prediction-dense_prediction)^2)).
The validation panel is absent from evolution, numerical control and stopping.
All five frozen loss milestones are reported; no endpoint or seed selection
was performed using prediction agreement.

## Prediction fidelity

Finest executed rtol 3.125e-6, atol3.125e-8:

| Model | Validation RMS from dense | Correction rank bound | Physical stopping time |
|:---|---:|---:|---:|
| Dense |0 by definition |4096 |109.34602 |
| P=1 |0.0032475604 |100 |110.31154 |
| P=2 |0.0010844347 |200 |109.61399 |
| P=3 |0.0011992242 |300 |108.83227 |

P2 and P3 improve on P1. P3 is slightly worse than P2 at this endpoint;
there is no monotone order trend across all three. The P2-to-P3 RMS increase
0.00011478946 narrowly exceeds their combined observed refinement sensitivity
0.00009998602 under the frozen diagnostic rule. All errors are far below the
predeclared coarse .1 agreement threshold. This supports fidelity of the
specified history truncation with genuinely restricted correction rank on
this dataset; it does not establish optimal compression or an order rate.

Every model achieves100% training classification and 94.70766% held-out
classification. Label MSEs are .18478947 dense, .18414120 P1, .18460321 P2,
.18450511 P3. These are secondary: similar label accuracy is not the evidence
for prediction fidelity. Reducing sample count and increasing width both
change the comparison with the earlier1000-image run.

## Size, memory and runtime

All rank statements are structural upper bounds, not measured numerical ranks.
The history factors contain 2*n*100*P evolving scalars versus n squared entries
in an unrestricted middle correction:

| P | History coordinates | Factor storage, float64 | Reduction versus 4096 squared entries |
|---:|---:|---:|---:|
|1 |819200 |6.25 MiB |20.48 x |
|2 |1638400 |12.50 MiB |10.24 x |
|3 |2457600 |18.75 MiB |6.83 x |

The fixed W0 adds 128 MiB. First-layer/readout weights and scalar coordinates
are additional. Separate accounting is essential:

| Model | Moving state MiB | Moving state plus fixed W0 MiB | Measured CUDA peak MiB | Finest integration seconds |
|:---|---:|---:|---:|---:|
| Dense |152.53125 |152.53125 |1941.88086 |102.97555 |
| P1 |30.78127 |158.78127 |544.26563 |139.89330 |
| P2 |37.03127 |165.03127 |603.14063 |149.92219 |
| P3 |43.28128 |171.28128 |654.39063 |152.26930 |

Moving-plus-fixed counts exclude retained initialization copies, solver
stages, data and workspace. Actual peaks include those GPU allocations;
the dense implementation retains an initial matrix copy and evolves larger
solver states. Thus these implementations show lower peak allocation for
closures, despite larger minimal moving-plus-fixed totals, and slower
integration at the stated common tolerances. These runs do not measure a
GPU-independent speedup. Only the learned correction is compressed; W0
still has quadratic storage and dense action cost.

## Numerical checks and provenance

Primary resolutions rtol 1.25e-5 and 3.125e-6, atol=rtol/100. At training MSE
.001, their validation-prediction differences are .00004810438 for dense,
.00000393116 for P1, .00000211840 for P2, .00000165886 for P3. Each is below both
.005 and 10% of the corresponding closure-dense RMS. All 15 comparisons across
the five loss milestones pass. No conditional refinement is triggered.
These observed sensitivities are empirical diagnostics, not rigorous error
bounds or confidence intervals. MNIST100_NUMERICAL_DECISIONS.md retains the
branch decision and the prescribed cross-GPU repetitions.

Five existing moment tests and five runner tests pass. Independent checks
reconstruct raw IDX preprocessing and nested sample selection, canonical
autograd gradients, noninitial moment/defect/transport identities, and
validation-image/label isolation. Independent NumPy calculations reconstruct
all 56 saved observations across 8 primary runs, verify all 40 crossing states,
and audit15 comparisons,56 label-metric rows and exported scatter points.
An explicit4096-square reconstruction additionally checks both actions and
predictions against the factor calculation. Full checks and scope are in
MNIST100_CHECK.md. Both prescribed same-resolution repetitions match all saved
scientific arrays and all five checkpoint states bitwise, including every
validation prediction, despite swapping GPUs.

Two pilots, eight primary runs and two repetitions consumed 1086.17028
summed GPU integration seconds excluding observations, or 1115.78990 seconds
including observations during integration. Both totals are below the frozen
8460-second cap; no individual trajectory hit a cap. The ten full trajectories
all reached their targets. Separate final/query work is recorded in each
summary and the complete resource receipt is
mnist100_audit01/resource_accounting.json. No conditional refinement was
needed and no further training remains.

Frozen scientific source hashes are unchanged:

- Runner:a5d5b0f75b2ff99651737d0fa3ac7f344f9744beeba84e2f7265593dde964df3.
- Moment base:ebf39cf377f1eb0f5dea64fa1ab946fddcb11a662b2368472017abef9237acd9.
- Orthogonal engine:32f80cf35c44b5015821fa8c8726bb8ff3bc6f7eb3e1b7abe9ee62ea8f529909.
- Prepared data:a57a903d382cbbb6d3ca79915ee6b9d371691d21d290decdf1f3f9e5e884c9a4.
- Initialization:5fc2a6ae306d63a6302b6b2c8fb7bc28b9b03f4f971bb9475f1fb195a0fe6797.
- Metrics:7d29598d72df94c74b6397455d670fdd35c249eb8dd775540e237d53f28f93ae.

The analyzer's explicit mnist100 mode preserves the old default: all previous
scientific metrics/prediction arrays are unchanged, and legacy CSVs/report/PNG
figures reproduce byte-identically. Its compatibility check is retained.

## Artifacts and reproduction

All paths below are under data/generated/neural_response_memory_20260922:

- mnist100_data01:prepared inputs, parent/source hashes, original image IDs.
- mnist100_pilot01:two30-step feasibility checks, no scientific selection.
- mnist100_primary01:eight full runs, exact commands, checkpoints, raw outputs,
  source_snapshots/source_manifest and execution_environment.json.
- mnist100_reproduction01:two prescribed fresh runs at the fine tolerance.
- mnist100_analysis01:metrics_summary.json, prediction/endpoint/label CSVs,
  per-image predictions/errors, scatter_primary.png/pdf, rms_vs_order.png/pdf
  and train_loss_vs_time.png/pdf; supplemental rms_vs_rank.png/pdf.
- mnist100_audit01:independent data/algebra/reconstruction/analysis receipts
  and default-analyzer backwards-compatibility check.

From checkout root, use /home/amir/miniconda3/bin/python -B, with
PYTHONDONTWRITEBYTECODE=1, OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1,
MKL_NUM_THREADS=1 and CUBLAS_WORKSPACE_CONFIG=:4096:8. Example commands:

```text
python -B studies/neural_response_memory_20260922/prepare_mnist100_moments.py --parent data/generated/neural_response_memory_20260922/mnist_data01/prepared.npz --output <fresh-data-directory>
python -B studies/neural_response_memory_20260922/run_mnist100_campaign.py --phase primary --dataset <prepared.npz> --out <fresh-primary-directory>
python -B studies/neural_response_memory_20260922/analyze_mnist_moments.py --protocol mnist100 --dataset <prepared.npz> --runs <primary-directory> --output <fresh-analysis-directory>
```

Run summaries retain exact repeat commands, numerical/environment settings
and hashes. Use fresh directories; never overwrite consumed results. Root
owns protocol/launch/results, mnist100_data_analysis owns data/analysis,
mnist100_audit owns independent checks. Concurrent changes and all previous
results are preserved. No maintained code/docs, Git index or promotion.
