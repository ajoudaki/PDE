# Width-2048 scalar versus dense comparison

2026-09-25. The user rejects widths128/256 as too small for the intended
population-scale comparison, requires width at least2048, and explicitly
directs dense experiments onto GPU. This authorizes the same investigation
at the corrected scale. Earlier small-width results remain implementation
and finite-width diagnostics; they cannot settle large-width accuracy.

## Decision and fixed model

Repeat both original scalar endpoint tasks, equal_mixed_odd (four distinct
training inputs after the exact odd antipodal quotient) and
quadrant_alternating (all eight inputs), with width2048 in each of three
hidden tanh layers and seeds20260920,20260927. The literal tasks remain in
deep_circle_cases.json. No change to normalization, initialization,
architecture, output, training metric, coefficient law or labels is allowed.

Inputs are U=(cos(theta),sin(theta))=x/sqrt(2), already normalized. Initialize
with NumPy default_rng in the original draw order: first weights std1,
two internal dense matrices std1/sqrt(n), stored readout std1/n. Prediction
is c^T h3/n. Train every parameter with physical mobilities(n,1,1,n),
unhalved mean squared loss and float64 computation. Dense states are real
2048-wide networks, not history-factor surrogates. All dense research
trajectories, including pilots, run on GPU. Record device and precision;
disable TF32 and enable deterministic algorithms.

H1: the declared scalar candidate matches the dense final circle function
at width2048 once both fit. H0: its small-width discrepancy persists at the
larger width. A validity failure or missing fitted endpoint is inconclusive.
Neither outcome proves the existence/nonexistence of general scalar
compression or establishes a width-limit theorem. Width2048 is the user's
minimum test scale, not a mathematical threshold for a population limit.

## Scalar law, initialization and computational preparation

Use the unchanged order-four scalar hierarchy with original frozen Q and
passive circle readout. Start every run from its own timezero initialized
scalar coefficients. Use the audited implicit BDF solver, exact sparse
Jacobian and local-signature recentering from SCALAR_LONG_TIME_PROTOCOL.md.
No neuron population or dense operator is consulted by the scalar RHS.

The old dense-jet initialization may be replaced by algebraically exact
low-rank direction actions and cached first responses. g_c is rank one in
each matrix block; Dg_c[g_d] has rank at most two. Retain the full initialized
Gaussian operators, their actual transposes, all ordered mixed derivatives
and the moving-direction term. This is computational refactoring only,
not low-rank approximation of initialized matrices or coefficient fitting.
Use batches of128 passive inputs, at most4 CPU BLAS threads for coefficient
initialization, and one thread for scalar integration.

Before research execution, compare the new initializer with the complete old
one on deterministic small widths, both depths and nontrivial readout scales.
For the first width2048 eight-input configuration also compare four specified
passive points (angles0,pi/7 plus the first two training inputs) with the old
initializer at the same original parameters. Require each tensor's maximum
difference <=1e-11+1e-9 times its maximum magnitude. This is an initialization
identity check, not a new training run.

## Matched endpoints and numerical gates

Every trained model stops at its own first numerically detected downward
crossing of training MSE1e-6. Dense physical cap2048; scalar physical cap1e9.
Compare functions at their own crossing times, never at equal clock time.
Initialize1024 uniform circle probes,32 fixed off-grid angles and the
training inputs; test points do not influence training. Preserve all
initial coefficients and source/data hashes. Dense endpoints are fresh
for this width and seed; no small-width or other model endpoint is reused.

The primary metric is full-circle RMS of scalar-minus-dense predictions.
Agreement: RMS<=0.1; adverse: RMS>0.2; intermediate: inconclusive. Also report
relative RMS against dense-function RMS, maximum observed error, training
fit, physical time, initialization cost, integration wall time and storage
separately. Include the exact frozen-kernel order-two scalar control at its
own first MSE1e-6 crossing, analytically evaluated within physical cap1e9.

Primary dense GPU runs use the existing adaptive Heun solver and block-aware
error control at rtol1.25e-5 and3.125e-6, atol=rtol/100, max_step2, initial_step.05.
These parameter error tolerances are not equated with output-error bounds.
Primary scalar BDF tolerances are1e-7 and1e-9 with atol=rtol/100.

Require for each model: endpoint prediction RMS change under refinement
<=0.002 and <=10% of measured scalar/dense discrepancy (floor1e-6), relative
fitting-time change<=0.001, and matching fitted statuses. Scalar peak
training-probe RMS discrepancy must be<=1e-4. If either model fails, allow
one additional run for that model/configuration only: dense rtol7.8125e-7
or scalar rtol1e-11. Compare the latest two resolutions. No further change
of model or optimizer is permitted. A cap is not evidence of permanent
nonfitting.

Compare RMS on512 nested versus1024 circle points, requiring difference
<=0.001 and <=1% of measured error (floor1e-6). If this fails, allow one
2048-point passive initialization/replay of saved scalar segments plus
dense endpoint reevaluation for that configuration. No retraining or
dense trajectory refresh is allowed. Unresolved quadrature stays inconclusive.

Encode the scalar endpoint function with Fourier modes64, conditionally128
then256, requiring grid/off-grid RMS<=1e-5 and maximum<=1e-4. Keep this
encoding gate separate from integration, direct-grid discrepancy and fitting.
The complete encoded-function verdict requires all gates. A failed encoding
check does not undo an independently validated training fit.

## Reproduction, pilots and limits

One first-seed eight-input dense feasibility pilot at width2048, the coarse
tolerance, and at most40 accepted steps or90 seconds checks GPU memory and
throughput. It is not independent scientific confirmation. One full first
hard configuration coefficient initialization plus the old-initializer
four-probe comparison is allowed as the initialization feasibility check,
with a600-second cap; its saved original coefficients may then be used by
primary runs. No pilot based on final model agreement chooses the design.

Mandatory reproduction: first-seed eight-input fine dense and fine scalar
runs from their own original initialization in fresh directories. Require
the same endpoint/time gates. The scalar reproduction uses the independently
recomputed original coefficients; reproduce probe coefficients too. No new
seed is selected after seeing an outcome. Other primary runs are tolerance
replicated; one full configuration is independently repeated end to end.

Hard limits: one GPU worker at a time on a device with no other compute
process when launched (the user's existing work is not stopped), at most4
CPU initialization threads and one scalar integration worker; GPU allocation
limit12GiB and process RSS limit8GiB. Each dense primary/refinement/reproduction
trajectory has900 seconds and100000 accepted steps; each scalar run has240
seconds; each coefficient initialization has600 seconds. At most8 primary
dense,8 primary scalar,4 conditional dense,4 conditional scalar,2 reproduction
trajectories and one40-step pilot. Frozen controls need no training integration.
The cumulative active research wall budget is7200 seconds, including pilots,
initialization, production and reproduction (GPU waiting excluded). Stop on
budget/cap and report incomplete cases explicitly. No unregistered sweep,
new model tuning or extra width is authorized by unused budget.

Root owns this protocol, preparation/campaign runner, results and README.
long_time_scalar_design owns scalar_wide_initialization.py, its deterministic
tests and derivation note. scalar_wide_dense_gpu owns scalar_wide_dense.py and
tests. eight_input_fitting_check owns independent checks/report. New data use
scalar_wide_* under this study's generated namespace. Preserve concurrent
activation work and the shared index; no maintained edit or promotion.
