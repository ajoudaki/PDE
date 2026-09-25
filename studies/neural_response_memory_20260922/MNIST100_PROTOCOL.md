# MNIST 100-image, width-4096 continuation

Authorized 2026-09-24: rerun the same dense and response-history moment models
with 100 total training samples and n=4096; report held-out prediction RMS.
This is a continuation of MNIST_PROTOCOL.md, not a new method or seed search.

## Frozen design

Digits 3/8, labels -1/+1. Select 50 images of each digit without replacement
from the previous 1000-image prepared training set using NumPy generator seed
20260924, then shuffle. Preserve all 1984 previous official-test validation
images, labels and order exactly. Producer records parent positions, original
IDs, hashes and source provenance. All inputs retain per-image unit length,
784 pixels, no PCA or fitted preprocessing. Validation never selects data,
states, integration steps, endpoints or hyperparameters.

Use unchanged mnist_moment_run.py, moment_engine.py and
orthogonal_moment_engine.py: two bias-free tanh hidden layers, width4096,
canonical Gaussian initialization seed20260924 and mobilities(n,1,n),
unhalved full-batch mean squared loss. All four models share exact initial
weights. Dense evolves its full middle matrix. P=1,2,3 closures retain W0
and its actual transpose and replace only the learned correction by the
MOMENT_CONSTRUCTION.md history-product projection. Direct tanh coordinates,
prefix length one, no Adam/SGD/free-factor fitting or scientific-model edits.

Primary metric is validation RMS of closure prediction minus dense prediction.
Each model stops at its own first training-MSE .001 crossing. Save the same
secondary milestones .1,.03,.01,.003. If caps prevent a common .001 endpoint,
use the smallest milestone reached by all four at both primary resolutions
and disclose every cap. No fitted-endpoint claim if .1 is not jointly reached.
These are matched-loss, not matched-physical-time comparisons. Preserve loss
curves and produce scatter/RMS figures. Label accuracy is secondary.

Hypothesis: the previous strong dense-prediction fidelity persists when
learned-correction rank is restricted to at most100,200,300 out of4096.
RMS below .1 is the inherited coarse agreement threshold for labels +/-1;
resolved large discrepancy or failure to fit is adverse evidence. Invalid
numerical comparisons are inconclusive. No universal rate follows from one
digit pair/initialization. This test isolates neither changing width nor
changing sample count from the previous experiment, since both are requested.

## Numerical validation and bounded execution

Adaptive Heun/Euler, float64, deterministic Torch, TF32 disabled. Two primary
tolerances rtol1.25e-5 and3.125e-6, atol=rtol/100; these start tighter than the
previous campaign. Same max step2, time10000, 30000-step cap, training-only
32-bisection loss-crossing location. Each trajectory has600 wall-seconds
during integration including intermediate observations. Save all capped runs.

Two throughput pilots only: dense/P3, at most30 steps and30 seconds each.
Width4096 is fixed by the user; there is no width/sample fallback. If memory
fails, reduce only inference block size, record it, and retain failed logs.

Eight primary trajectories (four models times two tolerances), scheduled over
both RTX3090s without two training jobs on the same device. At every shared
milestone require each predictor's tolerance-refinement RMS to be <= .005
and <=10% of the fine closure-dense discrepancy. Each model that fails any
relevant gate may receive one additional run at rtol7.8125e-7, max600s.
The dense reference receives its extra run if it fails any closure's gate.
At most four such refinements. Assess final comparisons using latest two
resolutions and common finest available dense reference; retain unresolved
gates explicitly. Order rankings require the gap to exceed the sum of both
comparisons' observed dense-plus-closure refinement changes; diagnostics are
not rigorous error bounds.

Independently reproduce the selected dense and P3 configurations once each
in fresh directories at their finest executed tolerances, max600s each.
These check reproducibility, not new seeds. Total maximum8460 summed GPU
integration-wall seconds:60 pilots+4800 primary+2400 conditional+1200 repeat.
Counters are checked between steps; record any final-step overshoot. Setup,
final inference, saved-state auditing and plots are timed separately. Stop
after the bounded branches; no further order/seed/subset search.

## Size and accounting

History state has2*n*100*P scalars:819200,1638400,2457600. Delta W rank is at
most100P; these are structural bounds, not measured numerical ranks. Report
learned-state savings separately from fixed W0 (4096 squared scalars), outer
weights, all retained arrays, integrator workspace and measured CUDA peaks.
Keeping W0 prevents equating correction compression with eliminating dense
total storage or a guaranteed speedup.

## Provenance and ownership

New generated namespaces: mnist100_data01, mnist100_pilot01,
mnist100_primary01, mnist100_refined01, mnist100_reproduction01,
mnist100_analysis01/02, mnist100_audit01. Preserve all previous outputs.
Root owns this protocol, launcher, README/results and runs. Scoped
mnist100_data_analysis owns the nested-subset producer and backwards-compatible
analyzer extension. Scoped mnist100_audit owns the independent checkpoint,
data/provenance, rank/state and metric checker and MNIST100_CHECK.md. Freeze
source/data/config hashes per run. No maintained-source or Git-index writes.
