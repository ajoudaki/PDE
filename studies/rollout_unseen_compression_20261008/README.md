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
(38,10,tanh,6144). The same source/reference seed 601, iid seed10601,
small-control seed20601 and split seed47 are used. No search over these seeds.
For each width use q=ceil(320*(log(en)/log(e*4096))^(5/2)), with source
rank given by the same rule replacing320 by12. This fixes an O(log(en)^5)
model inventory for fixed depth/dimension; accuracy remains to be tested.

Disposable full-interval RK4 sources on training+calibration inputs, physical
horizon32, step0.125, geometric intervals and degree8 Chebyshev fits; float32
source solve and float64 coefficient/metric assembly. Four coordinate trials,
condition cap16; preserve exact initialized paired actions after source
truncation. Scored inputs and labels cannot enter compilation.

All four comparison models use float32 Euler h=0.003125 to time32 (10240
updates); source/reference and compressed models also use h=0.00625 for a
single refinement check. Total36 training runs, six setup jobs maximum; no
rank, solver or horizon-search branch. Per training run cap180seconds, per
setup cap180seconds; use both GPUs with one job on each. If a source or
numerical gate fails, keep the failed result and do not tune it away.

Primary: maximum over saved times (spacing0.5) of unseen-prediction RMS
against the same dense reference, divided by its independent-dense RMS.
Report endpoint and time-average RMS, total moving+fixed model storage,
setup/run time and peak allocated memory. Target: ratio<=3 and roughly100x
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
