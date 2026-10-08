# Small empirical test of high-ratio rollout compression on unseen inputs

The user requests an efficient, bounded check of roughly 100-fold compression,
with few labeled samples, different digits, depths and activations. This new
study changes the observable contract from a predeclared panel to inputs
excluded from compilation. Its inputs are the explicitly requested
`paper/figures/capture_trajectory.py`, the canonical model in `docs/`, and
new generated data. No other study is a research input. No theorem is changed.

All implementation stays in the single capture executable. The lead owns its
driver/source compiler and this README. The scoped `deep_rollout_runtime`
agent implements only generalized dense/metric-deficit runtimes and tiny
gradient/pairing/restart checks. A brief output consistency check follows each
comparison; no broad audit or proof program is part of this task.

## Frozen small experiment

Raw sklearn digits, no PCA, 8 training labels and 32 unlabeled calibration
images, disjoint from every scored test image. Unit-normalized raw inputs;
zero readout, canonical MSE mobilities, genuine hidden updates. Calibration
input selection uses a deterministic shuffle without its labels. Readout
correction and selected-source geometry are unchanged, generalized to L
hidden layers. The deployment decoder evaluates arbitrary new inputs, but
no uniform unseen-input error theorem is claimed for these empirical sources.

Six settings: (digits38,L3,tanh,n4096), (38,3,tanh,8192),
(17,3,tanh,8192), (38,3,atan,8192), (38,5,tanh,8192),
(38,10,tanh,6144). The same source/reference seed 601, iid seed 10601,
small-control seed 20601 and split seed 47 are used. No search over these seeds.
For each width use q=ceil(320*(log(en)/log(e*4096))^(5/2)), with source
rank given by the same rule replacing 320 by 12. This fixes an O(log(en)^5)
model inventory for fixed depth/dimension; accuracy remains to be tested.

Disposable full-interval RK4 sources on training+calibration inputs, physical
horizon 32, step 0.125, geometric intervals and degree 8 Chebyshev fits; float32
source solve and float64 coefficient/metric assembly. Four coordinate trials,
condition cap 16; preserve exact initialized paired actions after source
truncation. Scored inputs and labels cannot enter compilation.

All four comparison models use float32 Euler h=0.003125 to time 32 (10240
updates); source/reference and compressed models also use h=0.00625 for a
single refinement check. Total 36 training runs, six setup jobs maximum; no
rank, solver or horizon-search branch. Per training run cap 180 seconds, per
setup cap 180 seconds; use both GPUs with one job on each. If a source or
numerical gate fails, keep the failed result and do not tune it away.

Primary: maximum over saved times (spacing 0.5) of unseen-prediction RMS
against the same dense reference, divided by its independent-dense RMS.
Report endpoint and time-average RMS, total moving+fixed model storage,
setup/run time and peak allocated memory. Target: ratio<=3 and roughly 100x
storage reduction. The matched-small comparison is a separate discriminator.
Training MSE>=.01 is underfit/inconclusive, not a fitting success. Measured
reference-plus-compressed step sensitivity must be <10% of the iid-dense
maximum RMS for the primary GF-resolution diagnostic. Iid/small are compared
at the same Euler step, but are not separately refined in this bounded batch.

H1: a fixed logarithmic budget produces high-ratio compression with unseen
prediction fidelity across these variations. H0: retention depends on the
predeclared test points, source budget or particular shallow/digit instance.
A positive finite grid is empirical support, not proof of a logarithmic
accuracy asymptote, all-time validity, or a high-probability success rate.
Failure tests this initializer/budget, not nonexistence of all such methods.

Generated records: `data/generated/rollout_unseen_compression_20261008/`.
Stop after the six settings and their brief consistency checks. Preserve
unrelated dirty files and the preceding task's uncommitted README.

## Completed results

All six settings and their 36 training runs finished, with no order/seed/horizon
searches or additional numerical refinements. All fit below 0.00028 MSE.
Every fine trajectory uses 10240 Euler steps through time 32, with 65 saved
times. There are 317 unseen test images for digits 3/8 and 321 for digits 1/7.
Each test input is absent from the 8 labeled training inputs and 32 unlabeled
calibration inputs. Calibration labels do not enter initialization or updates.

The following are **same-step Euler results**, not asserted exact-GF results.
RMS means maximum over saved times of prediction RMS over the whole unseen
test set. Dense-pair means the actual independent-dense run versus reference.
All model counts include fixed metrics and inverses, not only moving weights.

| Digits | Hidden layers | Activation | Dense width | Dense model numbers | Compressed model numbers | Reduction | Dense-pair RMS | Compressed RMS | Matched-small RMS |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 3/8 | 3 | tanh | 4096 | 33,820,672 | 737,608 | 45.85x | .02501531 | .02664009 | .04984275 |
| 3/8 | 3 | tanh | 8192 | 134,750,208 | 1,051,726 | 128.12x | .01786203 | .02104338 | .04622449 |
| 1/7 | 3 | tanh | 8192 | 134,750,208 | 1,051,726 | 128.12x | .01613666 | .01830543 | .03606141 |
| 3/8 | 3 | arctan | 8192 | 134,750,208 | 1,051,726 | 128.12x | .01812908 | .01806246 | .04617274 |
| 3/8 | 5 | tanh | 8192 | 268,967,936 | 1,931,860 | 139.23x | .02631489 | .03517673 | .03937875 |
| 3/8 | 10 | tanh | 6144 | 340,137,984 | 3,571,756 | 95.23x | .04936366 | .06707954 | .12158469 |

The compressed/dense-pair RMS ratios in table order are 1.065, 1.178, 1.134,
0.996, 1.337, 1.359, all below the fixed factor-three criterion. Compressed
RMS is below the storage-matched small network in all six cases. However,
**the small controls also satisfy the loose factor-three criterion in all
six cases**; passing it alone does not identify a logarithmic mechanism.
The stronger three-layer contrast is roughly twice the prediction fidelity
at matched storage. Endpoint and time-average comparisons are also favorable
against these small controls; their exact values are in each raw report.

The frozen GF-resolution diagnostic passes only at 4096. The measured sum of
dense and compressed half-step sensitivities, divided by dense-pair RMS, is
respectively 7.36%, 10.50%, 12.05%, 11.09%, 12.77%, 10.12%. The gate was 10%; it is
not relaxed. Thus the latter five **exact-GF comparison conclusions remain
numerically inconclusive**, despite their favorable common-Euler-step
comparisons. These are empirical sensitivity checks, never rigorous solver
error bounds. Iid and small controls were not separately refined.

### Measured costs

RTX 3090, float32 runtime with TF32 disabled, double source/metric assembly.
Run times include loss checks and sparse queries; setup is separate. Peaks
are allocated process memory including execution buffers/restart copies,
not minimal-workspace bounds or device-wide readings. The current-state
model itself has `(3L-2)q^2+65q+8` numbers, of which
`(L-1)q^2+65q+8` move and `(2L-1)q^2` are fixed. The common training data
add 520 numbers; the 2048 calibration-input numbers are discarded after setup.
Benchmark query arrays and saved histories are not deployment state.

| Setting, in table order | Setup seconds | Dense run seconds | Compressed run seconds | Matched-small seconds | Setup peak GiB | Dense run peak MiB | Compressed run peak MiB |
|---|---:|---:|---:|---:|---:|---:|---:|
| 3/8, L3, tanh,4096 | 4.36 | 17.80 | 45.48 | 15.98 | 1.293 | 420.38 | 36.73 |
| 3/8, L3, tanh,8192 | 11.57 | 48.58 | 45.10 | 15.97 | 5.054 | 1576.68 | 38.66 |
| 1/7, L3, tanh,8192 | 12.19 | 49.77 | 45.65 | 16.06 | 5.054 | 1576.68 | 38.66 |
| 3/8, L3, arctan,8192 | 11.61 | 48.82 | 46.43 | 16.62 | 5.054 | 1576.68 | 38.66 |
| 3/8, L5, tanh,8192 | 22.99 | 116.41 | 69.04 | 25.39 | 10.055 | 3114.18 | 44.33 |
| 3/8, L10, tanh,6144 | 28.66 | 121.60 | 129.78 | 48.13 | 12.709 | 3930.47 | 54.97 |

There is **no hundred-fold time speedup**. The five-layer case alone is faster
end to end in these timings (about 92 versus 116 seconds); other cases are
slower once setup is counted. Setup still performs a disposable coarse RK4
solve over the full physical interval and uses dense matrices. The fixed
runtime has no growing history; this is storage compression, not a claim
that setup is logarithmic or that the implementation is the fastest dense
solver alternative. Peak run-memory savings also differ from model-word
ratios because workspaces have their own costs.

### Interpretation and brief checks

The strongest supported claim is useful 95--139-fold **model-storage**
compression with comparable unseen prediction trajectories in this few-shot
Euler regime, surviving two digit pairs, two activations and 3/5/10 hidden
layers without retuning. One initialization per setting and two widths do
not establish a success probability or asymptotic accuracy exponent.
The O(log(en)^5) inventory follows from the prescribed q rule, not a fit to
an empirically established complexity lower envelope. No uniform sphere,
all-time/endpoint-at-infinity, large-sample, or GF theorem is inferred.
These experiments neither certify the finite-panel theorem nor prove that
this rollout initializer inherits an unseen-input logarithmic guarantee.

Before the batch, `deep_rollout_small_checks()` checked canonical gradients
against autograd, full-retention parameter/deficit RHS against dense/JVP,
exact initialized forward/reverse actions, source isometry and restart for
depths 2/3 and both activations. Maximum error was 3.56e-15. A fresh tiny
three-layer source compilation also passed. After each completed setting,
the lead checked raw RMS/storage/gates, and the scoped runtime agent
independently reconstructed raw RMS, checkpoint tensor counts, split
disjointness, step/time compatibility and source hashes. All consistency
checks passed; failed GF gates remain failed. These narrow checks are not
broad theory audits, repeated-seed confirmation or independent experiment
reruns. No extra GPU runs were used for auditing.

The experiment source is commit `eceaa8f`, SHA256
`a3ddd93adeee6113faabb9385e6a2ab9d99d5409e4840b3fa45f574e211aa918`.
After all runs, a CLI-only guard rejects arbitrary steps that would misalign
coarse/fine observation grids, and the step cap uses ceil to permit a final
short step. Neither changes the recorded default configurations or equations.
No shared paper/theorem text or older-study files were edited in this task.

Reproduce any setting with the single executable, a fresh output directory
and the settings above, for example:

```bash
/home/amir/Codes/sber-swap/.venv/bin/python -B paper/figures/capture_trajectory.py \
  compression-probe --width 8192 --depth 3 --activation tanh --digits 3 8 \
  --device cuda:0 --out data/generated/rollout_unseen_compression_20261008/reproduction_digits38_L3_n8192
```

The six original folders are `digits38_L3_tanh_n4096_v1`,
`digits38_L3_tanh_n8192_v1`, `digits17_L3_tanh_n8192_v1`,
`digits38_L3_atan_n8192_v1`, `digits38_L5_tanh_n8192_v1`, and
`digits38_L10_tanh_n6144_v1` under the generated namespace. Each contains
`report.json` (exact command, configuration, versions, hashes, timings and
all metrics), `trajectories.npz` (raw inputs/predictions/labeled split), and
`compiled_model.pt` (only the deployable model tensors and activation/depth).
The bounded batch is complete; no further sweep is authorized by this record.

## Authorized follow-up: approximately thousand-fold storage and modern activations

The user's next request authorizes this bounded continuation, not an open-ended
search. Freeze five comparisons: (digits38,tanh), (38,GELU), (17,SiLU),
(38,softplus), (17,erf). Every case uses two hidden layers, n=16384, q=256,
source rank 6 per family, m=8, and 32 unlabeled calibration images. All other
seeds, raw-input splitting, paired-source construction and condition cap 16
remain unchanged. Dense storage is 269,500,416 numbers; compressed storage
is 278,792 including fixed geometry, a 966.672-fold reduction. This budget
is fixed before testing. No scored-image-driven order or seed search is allowed.

A single training-only pilot at width 512, for each of these five cases,
uses RK4 step .125 through time 32. Pick the common horizon as the first of
16,24,32 at which all five pilot losses are below .001; if none succeeds,
use 32 and retain any underfit outcome. This is numerical pilot selection,
not independent evidence. No scored test predictions enter that choice.
Fine Euler step is .0015625 and coarse step .003125 for the same single
reference/compact refinement check. Iid and matched-small runs use the fine
step. The previous .01 fitting, factor-three fidelity and 10% step-sensitivity
gates remain unchanged. Run/source caps remain 180 seconds; one job per GPU.
Stop after five setups and at most 30 training runs, retaining failures rather
than relaxing geometry or numerical gates. A source failure stops that case.

The new activations use exact GELU (not its tanh approximation), SiLU, smooth
softplus without a threshold splice, and erf. Their value/derivative pairs
are checked against autograd, and the metric optimizer's existing tiny checks
are repeated for them. They satisfy the activation regularity assumption
(a sufficiently narrow strip for SiLU/softplus); this does not certify the
other theorem assumptions or this empirical source construction.

H1 is that approximately thousand-fold retained storage still tracks an iid
dense reference within the factor-three comparison and improves materially
on the storage-matched small network, across the activation choices. H0 is
that the previous advantage disappears at this smaller budget or outside
tanh/arctan. Report both maximum-over-time and endpoint unseen-set RMS,
storage, setup and training time, and the same validity gates. A passing
finite batch supports this empirical regime, not a logarithmic accuracy
asymptote, a success probability, or a theorem about all unseen inputs.

### Training-only pilot and final frozen numerical settings

Pilot losses at times 16 / 24 / 32, in the five-case order above:
tanh .001169 / .0002670 / .00007712;
GELU .0003981 / .00004780 / .000007584;
SiLU .002237 / .0006974 / .0002277;
softplus .002264 / .0003600 / .005315;
erf .0009090 / .0003535 / .0001420.
The frozen common horizon is therefore **24**. The softplus pilot's late loss
increase flags coarse-source integration risk. Before any main comparison,
reduce the RK4 source step to **.0625 for all five cases**; do not change any
other order, Euler step, gate or case. The pilot is not counted as a fidelity
result or source-accuracy certificate. All 12 depth/activation CPU checks
passed, with maximum error 3.56e-15. Full-case numerical failures will still
be recorded, not used to reopen tuning.

### Completed approximately thousand-fold batch

All five setups and all 30 Euler runs completed within their caps. No main
case was rerun or tuned. All six runs per case have training MSE below .0008;
all five reference/compact step-refinement checks pass. Fine trajectories
have 15360 updates through time 24, coarse trajectories 7680, with 49 common
observations at spacing .5. These are same-step Euler results with empirical
refinement diagnostics, not exact-GF certificates; iid and small controls
are still not separately refined.

Each dense model has **269,500,416** numbers. Each compressed model has
**278,792**: 82,184 moving and 196,608 fixed. Each matched-small network has
width 496 and **278,256** numbers. Thus the total-model storage reduction is
**966.67198485x**. The 520 common training-data numbers are separate; including
them in both model-plus-data counts gives about 964.9x. Setup calibration
inputs are discarded. There are 317 scored unseen inputs for digits 3/8 and
321 for 1/7; none enter source construction. No PCA is used.

Primary RMS below is the maximum over the 49 saved times of RMS prediction
discrepancy over the full unseen set, always against the same dense reference.
The fidelity test is compressed RMS <= 3 times iid-dense RMS, with the
previous fitting/numerical gates also required.

| Activation | Digits | Dense-pair RMS | Compressed RMS | Matched-small RMS | Compressed / dense-pair | Fidelity test |
|---|---|---:|---:|---:|---:|---|
| tanh | 3/8 | .01083718 | .04114112 | .04303847 | 3.7963 | FAIL |
| exact GELU | 3/8 | .01623898 | .07565696 | .03890072 | 4.6590 | FAIL |
| SiLU | 1/7 | .01994706 | .02716352 | .08901399 | 1.3618 | PASS |
| softplus | 3/8 | .01432547 | .02495815 | .03149082 | 1.7422 | PASS |
| erf | 1/7 | .00878612 | .05242891 | .03892771 | 5.9672 | FAIL |

For completeness, the endpoint and time-average metrics are different
observables, not replacements for the primary trajectory test:

| Activation | Endpoint dense-pair | Endpoint compressed | Endpoint small | Time-average compressed | Time-average small |
|---|---:|---:|---:|---:|---:|
| tanh | .01072449 | .03074531 | .03627776 | .02834034 | .03467910 |
| exact GELU | .01387286 | .02848046 | .03889049 | .02896282 | .03511620 |
| SiLU | .00920092 | .02240395 | .04173179 | .01966297 | .04092815 |
| softplus | .01322580 | .02469141 | .03149082 | .01868457 | .02490611 |
| erf | .00878612 | .03354973 | .03526881 | .03460137 | .03391275 |

SiLU is the strongest discriminator: compressed maximum RMS is **3.28x
lower** than matched-small RMS, and the small control fails factor three.
Softplus is a second positive compression example, but the small control
also passes and its error is only 1.26x larger. Tanh barely improves the
primary small-control error. GELU and erf are worse on that primary metric,
although every compressed endpoint is closer than its small-control
endpoint. In particular, GELU's compressed peak is at time 3.5, not at the
endpoint. Endpoint-only reporting would conceal its transient failure.

### Follow-up costs and qualifications

Times are measured seconds on the same two RTX 3090 GPUs. All use float32
Euler, TF32 disabled, and float64 source/metric assembly. Each source setup
uses 1720 dense RHS evaluations in a disposable RK4 solve across the full
physical interval, not a short initial-time prefix. It is distinct from the
15360 fine Euler updates used for each training comparison.

| Activation | Setup | Dense training | Compressed training | Small training | Refinement / dense-pair |
|---|---:|---:|---:|---:|---:|
| tanh | 29.10 | 161.99 | 52.00 | 17.18 | 4.989% |
| exact GELU | 28.55 | 140.08 | 54.82 | 19.82 | 7.935% |
| SiLU | 29.16 | 174.54 | 53.36 | 18.08 | 8.620% |
| softplus | 28.43 | 139.17 | 52.71 | 17.57 | 7.627% |
| erf | 28.41 | 139.41 | 51.55 | 17.66 | 7.333% |

Setup peak allocated GPU memory is about **11.067 GiB**, dense-training
process peak **3880.21 MiB**, and compressed-training process peak
**34.08--34.40 MiB**. These are allocated GPU process measurements, not total
host RAM, reserved GPU memory, minimal workspaces, or model-storage counts.
The 967x model-number reduction is not a 967x time or peak-memory reduction.

Conclusion: approximately thousand-fold retained storage with useful
unseen-trajectory fidelity is demonstrated for **two of these five fixed
settings**, most convincingly SiLU. The hoped-for uniformly larger RMS
advantage across activations is not established. The negative cases are
well-fitted and numerically resolved under the stated diagnostic, so they
are fidelity failures at this budget rather than inconclusive solver gates.
One width and one initialization per setting do not establish a logarithmic
accuracy exponent, activation-uniform success, or a probability guarantee.
This empirical rollout initializer is not thereby certified as the paper's
unseen-input Logarithmic decoder. No theorem or main-paper claim was changed.

The lead reconstructed every RMS/count/grid and checked split disjointness
from raw arrays. A scoped second check independently reconstructed the same
quantities for each completed case; no extra GPU run was used. The final
five-case source hash is
`811ef7e346c7f79cba0b40aef2c677df7d9757ab3ccdb1277d7b6da6e1443d91`,
commit `2ce1e9a`. Files are in the five folders
`thousand_digits38_L2_tanh_n16384_v1`,
`thousand_digits38_L2_gelu_n16384_v1`,
`thousand_digits17_L2_silu_n16384_v1`,
`thousand_digits38_L2_softplus_n16384_v1`, and
`thousand_digits17_L2_erf_n16384_v1` in this study's generated namespace.
Each has the exact command/configuration/hashes, raw predictions and inputs,
and compressed initialization checkpoint. Reproduction uses the existing
`compression-probe` CLI with `--width 16384 --depth 2 --budget 256
--source-rank 6 --source-step .0625 --horizon 24 --step .0015625`, the listed
activation/digits and a fresh output directory. The authorized batch is
complete; no follow-up search is part of this record.

## Authorized 24-case activation/depth replication at approximately 100x

The user now requests the full Cartesian product of tanh / exact GELU / SiLU,
hidden depths 2 / 3 / 5 / 10, and digit pairs 3/8 / 1/7. This continues the same
unseen-input investigation. Use the original q/rank law: n=8192 at depths
2/3/5 (q=383, rank15), n=6144 at depth10 (q=356, rank14). These are fixed before
any new scores, targeting roughly 95--139x total model storage, including all
metrics/inverses. All 24 cases retain the same eight labeled examples, 32
unlabeled calibration inputs, disjoint scored sets, seeds, unit-normalized raw
64-pixel inputs, zero readout, mobilities, and Gaussian initialization. No
activation gain or initialization rescaling is implicit. The ordinary small
network is matched to total stored numbers, not to q.

First run one training-only width128 pilot per case, CPU float64 adaptive
DOP853 (rtol1e-6, atol1e-8, maximum step8), stopping at training MSE .001 or
time4096, with a 30-second cap per case. This is only for training-duration
and numerical planning, not compression evidence. Persist all outcomes,
including slow/nonfitting pilots. No scored-query predictions are evaluated.
The main-run horizons, Euler/source steps and caps will be frozen from these
training-only observations before any 24-case fidelity evaluation. Retain
the factor-three trajectory-RMS target, .01 fitting gate, and 10% empirical
reference-plus-compact refinement gate. Primary comparison remains against
an independent dense copy and a total-storage-matched small dense network.
Report endpoint/time-average RMS separately, and all failures/inconclusive
cases. No order, seed or activation search beyond this requested 24-case grid.

Lead owns pilot/numerical settings and records. Scoped `sweep_runner` adds only
a small manifest-driven two-GPU wrapper to the existing single executable;
one process per GPU, bounded runs, no additional experiment files or refactor.

### Pilot outcome and frozen first 20 comparisons

Both training-only pilots completed. Times to .001 training MSE, with entries
given as digits3/8 and digits1/7 respectively:

| Depth | tanh | GELU | SiLU |
|---|---|---|---|
| 2 | 20.82 / 21.18 | 16.14 / 19.06 | 18.78 / 22.52 |
| 3 | 15.90 / 14.53 | 12.07 / 16.11 | 15.39 / 20.99 |
| 5 | 8.98 / 5.76 | 15.15 / 15.84 | 23.99 / 22.75 |
| 10 | 5.57 / 4.52 | 204.26 / 177.04 | 344.28 / 249.18 |

Raw pilot records are `sweep100_pilot_digits38_v1/report.json` and
`sweep100_pilot_digits17_v1/report.json` in this study's generated namespace.
For each activation/depth choose the same horizon for both digit pairs:
the larger pilot time times1.25, rounded up to a multiple of8, minimum16.
The first 20 comparisons therefore use horizons:
L2 (32,24,32), L3 (24,24,32), L5 (16,24,32), L10 tanh16.
They use fine Euler .0015625, coarse .003125, source RK4 .0625, source
Chebyshev degree8, condition cap16, and four coordinate candidates. Rank/q
remain the original prescribed values, identical across activations at a
given depth. Per Euler run cap300 seconds; per setup180; per case1500.
No extra refinement/order/seed branch is allowed after seeing scores.

`SWEEP100_PLAN.json` records these 20 cases. Run them with `compression-sweep`
on GPUs0/1 into a fresh `sweep100_main_v1` generated folder. The remaining
four requested L10 GELU/SiLU cases need much longer physical times (256/432
under the same rule). The user has been asked whether adaptive-step Euler
may be used for these four, with the same numerical rule for every compared
model and refinement checks, or whether fixed-step runtime-cap outcomes
should be reported as inconclusive. They are not silently counted as fitting
or compression successes. The 20 straightforward cases proceed meanwhile.
