# Activation robustness on the two hardest circle tasks

Frozen before implementation or width-4096 execution, 2026-09-25.
This is the user's explicit immediate continuation of the same closure
investigation: switch activations and test the two hardest prior cases.
It does not reopen the completed tanh campaign or start a different
scientific target. Old producer, analysis and evidence files remain unchanged.

## Question and fixed scientific scope

Does the chronological response-history closure retain useful prediction
agreement with the corresponding dense network when tanh is replaced by
ReLU, exact GELU, standard SELU or logistic sigmoid?

Use three bias-free hidden layers, each width 4096, and two trained internal
dense matrices. Uniform eight-sample unhalved squared loss, output c^T h3/n,
mobilities (n,1,1,n), unit-circle inputs with no additional scaling. Retain
NumPy default_rng(20260920) with draw order w,W20,W30,c and entry standard
deviations 1,1/sqrt(n),1/sqrt(n),1/n. Every model and activation uses the same
parameter draws. There is no activation-specific initialization, gain,
learning-rate tuning, bias, centering or label change. Thus this tests the
closure under the inherited scaling, not optimized performance of each
activation or SELU's self-normalization hypotheses.

The two tasks were chosen from the completed prior results because they
had the largest P1 and P3 discrepancies among the five tested cases:

- two_outliers_alternating: 15,27,39,51,63,75,165,285 degrees; +-+-+-+-.
- quadrant_alternating: 10,20,30,40,50,60,70,80 degrees; +-+-+-+-.

All eight literal points are retained. No oddness quotient applies to these
activations. `activation_circle_cases.json` freezes the eight activation/task
combinations and their original task identifiers.

Activations and selected derivatives are:

- ReLU: max(0,z), derivative 1 for z>0 and 0 for z<=0.
- GELU: z Phi(z), with the exact normal CDF, derivative Phi(z)+z phi(z).
  No tanh approximation is used.
- SELU: lambda*z for z>0 and lambda*alpha*expm1(z) for z<=0;
  derivative lambda for z>0 and lambda*alpha*exp(z) for z<=0.
  lambda=1.0507009873554804934193349852946,
  alpha=1.6732632423543772848170429916717.
- Sigmoid: 1/(1+exp(-z)), evaluated stably, derivative h*(1-h).

The same activation is used in every hidden layer. The moment transport,
shared activity clock and physical matrix reconstruction are unchanged,
with sources evaluated using the correct activation derivative. P=1,2,3
is fixed in advance. Both initialized matrices and actual transposes remain.
The general derivation and kink qualifications belong in
`ACTIVATION_CIRCLE_DERIVATION.md`. Production uses direct activation
coordinates, with no blanket rational-RHS or nonsmooth uniqueness claim.

## Observable, competing outcomes and numerical gates

Primary: RMS difference from the same-activation dense prediction over 8192
equally spaced circle directions, at each model's own numerical training-MSE
.001 crossing. Dense references are freshly trained for every activation/task.
This is matched loss, not matched time or held-out target-label error.
Record loss milestones .9,.5,.1,.03,.01,.003,.001 and secondary physical-time
observations at 10,100,1000 when reached before stopping. Query predictions
do not control steps, fitting, initialization or closure dynamics.

H1: P2 and/or P3 yields useful dense-prediction fidelity across the activation
changes after substantial fitting. H0: activation-dependent history changes
or nonsmooth switching make the tested low orders inaccurate. A third outcome
is failure to fit or unresolved numerical error. RMS<=.1 is the inherited
coarse-agreement criterion for labels +/-1; RMS>.1 is adverse for that tested
P only when numerical gates pass. Report every order; do not presume P3 best.
Feature motion and derivative/activation diagnostics distinguish meaningful
learning from agreement near an untrained or saturated state.

At every shared loss milestone compare rtol=1.25e-5 with 3.125e-6,
atol=rtol/100. Require the dense and closure predictor RMS refinement changes
each <=.005 and <=10% of the fine closure-dense discrepancy, nested
8192/4096-grid score change <=1e-5, and actual milestone MSE within 1%.
Use one common finest dense reference per activation/task. An order ranking
is resolved only when its score gap exceeds both comparisons' summed dense
and closure sensitivities. These are empirical numerical diagnostics, not
certified error bounds. The same checks may be reported separately for
common physical-time observations, with exact requested-time metadata.

If .001 is not jointly reached, explicitly mark the primary comparison
unavailable. Report the smallest common reached loss milestone and available
matched-time diagnostics separately, together with final losses, times and
stopping reasons. A close near-initial predictor does not establish fidelity
after fitting. Do not treat a solver cap or invalid gate as closure failure.

## Bounded execution and predeclared branches

Float64 deterministic Torch, no TF32, one numerical CPU thread and one
training worker per RTX 3090, at most two workers. Use the previous physical
error controller and adaptive Heun/Euler scheme: initial step .05, max step 2,
internal-matrix error Frobenius/sqrt(n), relative scale given by the learned
increment with unit floor. All accepted ratios <=1. Use 32 bisections of the
quadratic Heun continuous extension for bracketed loss events. Save fixed-time
observations from that same extension, restricted to the actual interval
before a target crossing. No forced loss-decrease rejection.

Each full trajectory stops on MSE .001, physical time 10000, 30000 accepted
steps or 300 integration-wall seconds, whichever comes first. The lower
wall allowance than the old tanh campaign is an explicit resource limit;
the present conclusion compares closures with their own activation's dense
reference, and does not rank optimized activation training performance.

1. Eight feasibility pilots: dense and P3 for each activation on the outlier
   task, at most 30 accepted steps or 30 integration-wall seconds. Width and
   data are unchanged; pilots may use 128 query directions and no milestones.
   They check finite fields, memory, scaling and execution, not scientific fit.
2. Primary: 4 activations x 2 tasks x 4 models x 2 tolerances =64 trajectories.
3. Conditional numerical branch: if shared-milestone validity fails, one
   additional rtol=7.8125e-7 trajectory per affected model, at most 32. Include
   a dense model if any paired closure requires its refinement. No refinement
   merely to rescue a training cap. Compare the latest two resolutions;
   gates still failing remain unresolved. No fourth tolerance or order search.
   A grid-only failure remains an unresolved panel-resolution check; it does
   not identify a model for solver-tolerance refinement. Matched-time checks
   are secondary and do not independently trigger a new trajectory.
4. Reproducibility: repeat dense and P3 on the outlier task for each activation
   at the finest executed tolerance, at most eight trajectories, swapping
   GPUs. If capped by wall time, compare the shared deterministic accepted
   prefix and common saved events, explicitly excluding unequal cap endpoints.
   The purpose is reproduction, not more seeds or extra scientific tuning.

Maximum 112 trajectories including all pilots and branches. Hard cumulative
33000 summed GPU integration-wall seconds, including observations and any
last-step overshoot. A launcher reserves a 35-second last-step guard, allows
30 seconds of integration-watchdog grace, and stops when the next run
would exceed the remaining budget. Setup, final serialization/inference,
analysis and independent replay are separately timed and not training budget.
Preserve every failed/capped run. Stop after these branches regardless of outcome.

Before the first pilot, the independent implementation audit clarified the
35-second guard above: one final accepted step may include loss-root searches,
full-circle observations, checkpoint writes and CRC reads. The five seconds
beyond the watchdog grace cover polling and termination accounting. An external
watchdog termination remains an execution failure, never evidence against
closure fidelity. A completed integration's final saving is not governed by
the integration watchdog.

## Integrity, checks and ownership

Before primary runs, test each activation/derivative against an independent
autograd reference, including the selected kink values, extreme finite inputs,
all four physical gradients, matched initialization, both transpose actions,
moment transport, physical defects and zero residual. Test event ordering,
training-only stopping and fixed-time interpolation without query feedback.
CRC-validate newly saved archives, in addition to source/config/data hashes,
because the preceding campaign found one recoverable archive-bit discrepancy.
Do not silently overwrite or repair a failed archive in place.

Afterward independently replay checkpoints/predictions using explicit
physical matrices and the declared activation, rescore comparisons, verify
repetitions, and retain activation/hidden-feature motion diagnostics.
Retain exact inputs, sources/hashes, environment, solver traces, statuses,
state sizes, timings and measured memory. State that initialized dense
storage and multiplication remain and that one seed is not a distributional
or hierarchy-convergence result.

Root owns protocol, literal cases, execution, analysis and README/results.
activation_theory owns the new derivation. Implementation and independent
audit assignments are scoped separately; no old producer files are edited.
Source remains flat in this study and generated products use new
activation_circle_* namespaces. No maintained-source changes, promotion or
Git-index writes are requested.
