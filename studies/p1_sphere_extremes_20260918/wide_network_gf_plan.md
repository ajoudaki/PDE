# One bounded wide-network gradient-flow diagnostic

Frozen before implementation or numerical execution, 2026-09-18. The user
explicitly requested a quick wide-network GF experiment on the seven-input
configuration to distinguish numerical fitting from remaining near loss
48/49. This is a numerical follow-up to the same configuration investigation.
The finite network is an explicitly different object from the fixed p=1
closure; no identification between their all-time trajectories is assumed.

## Fixed scientific configuration

Use d=3, two hidden tanh layers, no biases, n=1024 neurons per hidden layer,
all weights trained. Inputs are x(theta)=sqrt(3)(C,S cos(theta),S sin(theta)),
C=S=1/sqrt(2). Positive labels have angles 0,2pi/3,4pi/3; negative labels
have angles pi/4,3pi/4,5pi/4,7pi/4. Each sample mass is 1/7. The constant
prediction optimum has f=-1/7 and unhalved loss 48/49. Inputs have no
parallel/antiparallel pair. The configuration is fixed, not tuned to output.

Use canonical finite Gaussian initialization from maintained
`pde.finite_network.initialize`: W1 entries N(0,1), W2 entries N(0,1/n),
stored readout entries N(0,1/n^2), in the maintained draw order. Do not replace
the small random readout by zero. The network is
h1=tanh(W1 X/sqrt(3)), h2=tanh(W2 h1), f=c^T h2/n. Use physical mobilities
(n,1,n), actual W2 transpose, and loss mean((f-y)^2). No optimizer momentum,
weight decay, minibatching, clipping, frozen features, or artificial low rank.

## Decision and interpretation

The primary observation is training loss versus physical time, together
with all seven predictions and hidden-feature RMS displacement. Reaching
loss <=1e-6 is numerical fitting for this experiment, not proof of exact
zero at finite/infinite time. Reaching loss <48/49-1e-2 rules out the
particular 48/49 plateau on that observed valid trajectory. Loss remaining
near 48/49 at the finite stop is inconclusive about an infinite-time plateau;
record its slope rather than infer attraction. Intermediate loss reduction
is reported as such, not reclassified as success or a proved failure.

## Solver and validity controls

Use float64 NumPy and the maintained stable tanh derivative. A study-local
direct RHS is allowed for speed only after every block and predictions agree
with the maintained finite reference on a small initialized and nonzero-
readout perturbed state, with rtol 5e-12 and atol 1e-13. Check the maintained
RHS again at each completed wide endpoint. Verify the physical dissipation
identity against a centered directional loss difference on the small
nontrivial state (relative error <=1e-5).

Integrate with embedded Bogacki--Shampine RK3(2), initial step .02, maximum
step 1, with no modification of accepted parameters. The error norm is the
maximum of the three block physical norms divided by atol+rtol*max(1,current
learned block displacement). Those norms are Frobenius/sqrt(n) for W1,
Frobenius for W2, and Euclidean/sqrt(n) for c. This controls moving increments
rather than allowing the frozen Gaussian middle bulk to dilute tolerance.
Main rtol=2e-5 and atol=2e-8. Reject a trial with embedded norm>1, nonfinite
state/observable, or loss increase above 1e-11*max(1,previous loss); record
rejections. This is numerical GF approximation, not exact GF integration.

Same-seed replay uses tolerances ten times tighter and the same main final
physical horizon. Exact common checkpoints include .1,.2,.5,1,2,5,10,20,50,
100,200,500,1000,2000 and the final horizon, where applicable. Validity
requires maximum prediction discrepancy <=1e-3 on common checkpoints and
final absolute loss discrepancy <=2e-5. Missing replay coverage makes the
uncovered main tail unvalidated; do not silently count it as a verified run.

## Predeclared runs, budget and stop

1. Main width1024 seed20260918: stop at loss<=1e-6, t=2000, or 85 seconds.
2. Same-seed tighter replay: reserve up to105 seconds to the main final time.
3. If main/replay validity passes and at least20 seconds remain, width1024
   seed20260919 with main tolerance: stop at loss<=1e-6, t=2000, or remaining
   budget, with a maximum of45 seconds.

Total numerical process wall-time cap240 seconds, two BLAS/OMP threads,
one process, and anticipated memory below512MiB. The run stops regardless
of result; no width/angle/seed sweep or extra branch is authorized here.
An outer250-second timeout permits final artifact flushing only. Code
verification and all trajectories share the240-second cap. The first
deterministic unit-sized solver check is not empirical replication.

## Reproducibility and scope

Save exact source and plan hashes, maintained-source hashes, HEAD, Python,
NumPy, SciPy and BLAS information, seeds, dtypes, tolerances, timing,
accepted/rejected step counts, data arrays, trajectory CSVs, final arrays,
predictions, movement and validation results in a fresh study-owned generated
run directory. Preserve failures and partial runs. Lead owns plan, script,
results and README. A fresh scoped read-only agent independently verified
the finite scaling and suggested checks using assigned established sources
and the existing seven-input synthesis; it performs no extra experiment.
No established source, shared index, or other study is changed.
