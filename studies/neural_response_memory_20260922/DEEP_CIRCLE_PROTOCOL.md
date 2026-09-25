# Three-hidden-layer circle continuation

Frozen before width-4096 execution, 2026-09-24. The user explicitly requests
continuation of this study, derivation of the deeper closure, and the same
circle tasks at n=4096 with P=1,2,3. This authorizes this new campaign only;
no old training campaign or other study is reopened.

## Model and finite construction

Three bias-free tanh hidden layers, width4096 each; first matrix4096x2,
two internal4096x4096 matrices, scalar readout divided by4096. Inputs are
u=(cos(theta),sin(theta))=x/sqrt(2). Unhalved mean squared training loss,
physical gradient-flow mobilities(n,1,1,n). NumPy default_rng(20260920)
draws w,W20,W30,c in that order with standard deviations1,1/sqrt(n),
1/sqrt(n),1/n. Every dense/closure model shares exactly these draws.

DEEP_CIRCLE_DERIVATION.md gives the equations before the experiments.
Both initialized matrices and actual transposes remain fixed in the closure.
Each link has its own pair of P-mode chronological Legendre history arrays,
coupled through current forward/backward responses and a common learning
activity length1+s. The two omitted covariance defects are explicit.
Numerics use direct tanh coordinates, as the recent MNIST continuation did:
this is the same continuous closure on its consistent response manifold;
the evaluated numerical RHS itself is not the rational lifted RHS.
There is no retained dense learned correction, free factor optimization,
teacher-trajectory forcing or fitted damping.

## Frozen tasks and observable

Literal tasks are retained in deep_circle_cases.json, taken only from this
study's HARD_BENCHMARK_INPUTS.md and ADDITIONAL_BENCHMARK_INPUTS.md:

1. two_outliers_alternating:15,27,39,51,63,75,165,285 degrees,+-+-+-+-.
2. quadrant_alternating:10,20,30,40,50,60,70,80 degrees,+-+-+-+-.
3. quadrant_pairs:same angles,++--++--.
4. quadrant_center_edges:15,21,27,33,39,45,53,60 degrees,--++++--.
5. equal_mixed_odd:0,45,...,315 degrees,++-+--+-; use the same exact
   oddness quotient to0,45,90,135 degrees with labels+,+,-,+, equal weights.

This repeats the five prior moment tasks, with deeper architecture and the
requested width. No old learned predictions supply new references. It is
a deliberate set of hard tasks, one network seed, not a random task sample.

Primary: RMS(closure minus dense prediction) on8192 equally spaced circle
directions, at each model's own first bracketed training-MSE .001 crossing.
The 4096 nested grid tests resolution. These are matched-loss endpoints,
not equal physical times or generalization errors against test labels.
Record sampled loss trajectories and secondary .1,.03,.01,.003 crossings.
No training decisions use the circle-query predictions. If .001 is not
jointly reached, report the cap and the smallest common milestone separately;
do not relabel it as a fitted .001 endpoint.

H1: useful prediction fidelity survives this depth extension at small P,
with P3 more accurate than P1. H0: coupled defects produce large discrepancies
or the apparent accuracy is numerical. RMS<=.1 is coarse agreement for labels
plus/minus1; RMS>.1 is adverse evidence for that P on that task. P3-vs-P1
ordering must be resolved by the numerical criteria below. Nonmonotonic
P1/P2/P3 outcomes are retained. No universal or asymptotic rate is inferred.

## Numerical validity and fixed budget

Float64 deterministic Torch, no TF32, one CPU numerical thread per worker,
one training worker on each of the two available RTX3090s. Adaptive explicit
Heun with Euler difference, initial step.05, maxstep2. The physical hidden
error is Frobenius/sqrt(n), with scale max(1,norm of current/candidate learned
increment/sqrt(n)), identical between dense and reconstructed moment links.
Other state blocks use RMS and a unit scale floor. All accepted ratios<=1.
32 bisections on the quadratic Heun continuous extension locate physical
training-loss crossings; this is a numerical event rule, not exact flow.

Two predeclared feasibility pilots, dense and P3 on the first task, at most
30 accepted steps or30 integration-wall seconds each. Width/sample count
remain fixed. They test memory and throughput only, not scientific accuracy.
Their query panel may use128 points; primary panels remain8192.

Primary campaign:5 cases x(dense,P1,P2,P3) x2 tolerances =40 trajectories.
rtol=1.25e-5 and3.125e-6, atol=rtol/100. Every trajectory stops at its target,
physical time10000,30000 accepted steps, or600 integration-wall seconds,
whichever comes first. Keep every failed/capped run. No forced loss-decrease
rejection is used for the perturbed closure.

At each shared milestone, require each model's circle RMS change on
refinement <=.005 and <=10% of its fine closure-dense discrepancy. Dense
must meet that relative criterion for each paired closure. Require nested
8192/4096 score change <=1e-5 and physical milestone MSE within1% of its
target. A failing model may get ONE additional numerical resolution at
rtol7.8125e-7 (atol/100), at most20 conditional runs. A dense run is triggered
if it fails any relevant pair's gate. Compare the latest two resolutions
against the finest common dense reference; unresolved gates remain explicit.
Order gaps must exceed the sum of both comparisons' observed dense-plus-
closure refinement changes. These changes are diagnostics, not certified
error bounds. Record coarse agreement separately from resolved fine digits.

Repeat the hardest-task dense and P3 configurations once each in fresh
directories at their finest executed tolerances, swapping GPUs relative to
their originals. These are reproducibility checks, not additional seeds.
The total is at most64 trajectories including pilots and repeats, with a
hard cumulative12600 summed GPU integration-wall-second cap. Per-run
overshoots from a final step/observation are recorded and counted. Setup,
final inference, serialization and independent audit time are separate.
Stop after these declared branches regardless of scientific outcome.

## Checks, provenance and ownership

Before primary runs: independent tiny autograd/NumPy dense gradients,
canonical scaling, matched initialization, both shared adjoints, physical
derivatives/defect signs, moment transport, controller parity, training-only
endpoint location and no query feedback. Afterward independently reconstruct
saved checkpoints and predictions, check hashes and rescore all comparisons.
Keep exact configurations, source hashes, environment/hardware, seed,
precision, state counts, peaks, timings, exit codes, traces and checkpoints.

History coordinates total4*n*M*P; each learned matrix has rank<=M*P.
Fixed initialization remains2*n*n scalars. Account separately for moving
state, fixed matrices, retained copies, solver workspace and measured peaks;
no whole-model memory or speed advantage is presumed.

Root owns protocol,cases,campaign,analysis,README/results and execution.
deep_derivation owns DEEP_CIRCLE_DERIVATION.md and context digest;
deep_engine owns deep_moment_engine.py,deep_circle_run.py and its tests;
deep_audit owns check_deep_circle.py,DEEP_CIRCLE_CHECK.md and audit scratch.
New generated namespaces deep_circle_pilot01,deep_circle_primary01,
deep_circle_refined01,deep_circle_reproduction01,deep_circle_analysis01,
deep_circle_audit01. Keep earlier artifacts. No maintained-source or Git-index
write, promotion, or external scientific-source retrieval is needed.
