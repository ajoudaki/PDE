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
