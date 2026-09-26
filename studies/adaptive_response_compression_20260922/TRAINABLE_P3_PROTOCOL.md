# One-case test: unfreeze the derivative p3 dictionary

Frozen before implementation/training on 2026-09-22. The user explicitly
clarified that p3 means the SAME initialized derivative-dictionary vectors,
then letting those vectors train. This supersedes the streaming rank-three
interpretation for this test. It is factor-parameter gradient flow, not the
adaptive response-cache/sketch algorithm or canonical dense-W2-coordinate flow.

## Scope and inputs

One task: two_outliers_alternating, n=2048, original seed20260920. Eight
normalized inputs at degrees [15,27,39,51,63,75,165,285], labels
[+1,-1,+1,-1,+1,-1,+1,-1], uniform probabilities. No rotation, extra seed,
task, order, optimizer sweep or performance-selected baseline.

The user-requested archival comparison narrowly authorizes the derivative
study and original-circle archive for this benchmark's exact initialization,
task, producer semantics and saved references. Other studies/theories remain
excluded. Import actual initial w,c,M,b1,b2 from
data/generated/gradient_flow_probe_dictionary_20260921/suite_refined01/
two_outliers_alternating_new_p3/arrays.npz. Preserve all arrays exactly.
No dense residual is added; no dense matrix is retained during training.

Reference: data/generated/random_dictionary_learned_circle_20260920/
scaling_discovery_refined01/two_outliers_alternating_full/arrays.npz.
Reuse archived frozen p3/p7, and reproduce frozen p3 once with the new
producer's basis-freeze flag to check the comparison.

## Model and metric

W2=B2 M B1^T/n, B1 shape(2048,6), B2 shape(2048,12), M shape(12,6).
Read-in w and readout c train as before. B1/B2 start in the exact previous
inverse-Cholesky ridge-normalized coordinates, then train too. No subsequent
normalization, whitening, rank deletion, penalty, clipping, momentum or Adam.

Unhalved probability MSE. Population L2 metric for w,c,B1,B2 (summed over
columns); Frobenius metric for M. Finite mobilities n,n,n,n and 1 respectively.
No tuned relative basis learning rate. This defines the factorized flow;
it does not assert equivalence to canonical dense-weight dynamics.

18 dictionary vectors, middle rank at most6. Trainable scalars43,080 versus
6,216 frozen-p3 and7,340 frozen-p7. The36,864 basis scalars were previously
stored but frozen. Improvements are NOT trainable-parameter matched; total
working-model storage is unchanged from p3 when dictionary storage counts.

## Decision and validation

H1: unfreezing improves dense-function circle RMS over frozen p3 and even p7.
H0: it does not despite greater trainable capacity. Training loss alone is
insufficient. Primary metric: RMS output difference on identical8192-angle
grid, at each model's OWN first training-MSE0.001 crossing. This is agreement
with the dense learned function, not ground-truth test error. Secondary:
sampled maximum error, fitting time, basis motion/norms and training loss.

Base rtol6.25e-5 and1.5625e-5, atol=rtol/100, float64 adaptive Heun with
embedded Euler error, h0=.05,hmax=2,hmin=1e-7,Tmax10000,30000 accepted steps.
Historical RMS w,c and increment-Frobenius M controllers are preserved;
trainable B1/B2 add columnwise RMS controllers, maximum over columns.
Require finite state, fitting, independent output/state replay<=1e-10,
identical initialization/grids, 8192/4096 RMS agreement<=1e-3, adaptive
endpoint primary/finer sampled maximum difference<=.01. Frozen replay
must match archived finer endpoint within.001 max and fit time within.001.

Pass versus each comparator: both adaptive scores lower by>=.01 RMS and all
gates pass. Fail: both higher by>=.01 with valid numerics. Smaller differences,
mixed directions or failed gates are inconclusive. Always select latest/finer,
never best score. Exactly one extra rtol3.90625e-6 is permitted ONLY if both
base levels fit and endpoint max difference>.01; then compare latest two.
No retry for poor RMS, fitting failure or wall/step caps.

## Budget and ownership

At most two adaptive base runs, one frozen replay and one gated extra.
Use both GPUs concurrently for the two base levels. Integration caps180s per
adaptive base,100s frozen replay,100s extra; reserve40s checks/output. Maximum
600 summed GPU-worker seconds, within last recorded unused996.2095660865307s.
Stop when complete or capped. No performance-driven extension. CPU tests and
reporting capped10 minutes total. Record commands, sources/input/output hashes,
environment, solver diagnostics, actual runtimes and all failed attempts.

Root owns protocol/model/runner/analysis/report/README; scoped agents own
benchmark and implementation checks. Fresh outputs in this study's generated
namespace. Preserve old sources/data, concurrent work and Git index.

This establishes at most a one-seed, task-specific comparison. No hierarchy
convergence, parameter-efficiency, dense-flow equivalence or success of the
earlier streaming/cache proposal follows from this test.
