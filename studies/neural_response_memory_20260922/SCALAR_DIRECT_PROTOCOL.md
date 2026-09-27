# Direct scalar versus population experiment, 2026-09-26

This user-authorized continuation isolates aggregate truncation. No Fourier
coordinates, spatial projection, learned dictionary, population refresh or
future-reference data enter the scalar solver. Root owns scalar_direct.py,
run_scalar_direct.py, check_scalar_direct.py, this protocol and the report;
the scoped reference agent owns scalar_population_reference.py. Existing main
consolidated code is not edited.

## Question and fixed models

Does a practical increasing cutoff of the clipped scalar contraction
hierarchy track its own order-P population parent through nonlinear learning?
H1: affordable cutoffs preserve output and hidden Gram trajectories; H0:
boundary deletion corrupts those dynamics even with accurate integration.
The existing finite-horizon theorem does not predict success at small K.

Use two hidden tanh layers, unit circle inputs already divided by sqrt(d),
no biases/normalization, canonical block mobilities (n,1,n), mean squared
training loss, Gaussian first entries N(0,1), middle N(0,1/n), stored readout
N(0,1/n^2), and the original activity clock. Primary memory order P=1;
a fixed P=2 flagship extension tests mode transport if resources permit.
The shared initialized middle matrix and transpose remain represented by
the same decorated edges. Keeping two nonlinear hidden layers retains
the reused matrix, trainable features and learned response-memory feedback.

Tasks fixed before running:

* broad_pair: angles 10,125 degrees, labels +1,-1;
* close_pair: angles 10,45 degrees, labels +1,-1;
* triple: angles 10,75,145 degrees, labels +1,-1,+1.

Passive queries: 55,205,310 degrees. They have no labels, residuals, history
sources or training weight. Hidden activation Gram matrices of all training
inputs are retained at both layers. Query-Gram entries are not needed.
Widths 16 and 64; seeds 20260920 and 20260921. Same actual initialization,
P, inputs and physical times for each scalar-parent comparison.

## Construction

Compile the output/Gram-reachable ordinary contraction trees, complexity K
equal to vertex+edge+decoration count. Delete a whole RHS product if one of
its connected factors exceeds K. Sources and Legendre transport are derived
for the specified P; there are no frozen boundary values.
Primary clipping uses rigorous diagram-specific bounds from bounded tanh,
the readout energy bound, history integral bounds and absolute W0 actions.
The raw scalar state is not projected after a time step: clip only arguments
of the RHS and reported readouts, as in the proved construction. Include an
unclipped ablation at the largest completed flagship cutoff.

Compiler tables depend on task/P/K/readout set but not on n or random seed.
Initialization may contract neuron fields once. A runtime-only object must
contain only scalar initial values, caps, coefficient/index arrays and data.

## Metrics and interpretation

Primary: maximum over 121 common times in [0,12] of RMS prediction
discrepancy, separately over training and the three passive inputs, against
the same-order population parent. Also final discrepancies, each layer's
training Gram RMS error, training RMS/loss, clock error, and parent Gram
motion. Record PSD/activation-Gram constraint violations and clipping.
These sampled maxima are empirical path diagnostics, not continuous suprema.
Record predictions at the parent's first training-RMS <=0.05 crossing when
it occurs, and flag missing fits. Never compare different own stopping
times as the primary metric.

Successful witness: train and passive maximum RMS discrepancies <=0.02 and
both Gram maximum RMS discrepancies <=0.02, with resolved numerics.
Failure: any maximum RMS discrepancy >0.10. Otherwise inconclusive/intermediate.
An order trend is reported per cell; no monotonic trend is assumed.
A failed solver/compilation is a resource or numerical failure, not an accuracy
measurement. Lack of parent fitting does not invalidate fixed-time tracking,
but prevents a claim about a fitted endpoint.

## Validation and bounded branches

Before training: compare all exact primitive templates against independent
population chain rules at nonzero histories for P=1,2; verify retained scalar
rows plus omitted terms against finite differences; initialization, stationary
zero residual, transpose orientation and passive nonfeedback. Check the
reference against the existing reference at depth three where applicable.
Primary DOP853 float64 tolerances rtol=2e-7, atol=2e-9. Refine the largest
completed flagship scalar and its parent to 2e-9/2e-11. Required readout
change <=1e-4 and <=5% of any discrepancy used to assert failure.

Compile K=3,5,7 sequentially, sharing tables across widths/seeds. Try K=9
on broad_pair P1 only if K7 completes. Stop increasing K for a task at a
compile cap. Run the declared width/seed panel for all completed primary
cutoffs. Try broad_pair P2 at K=3,5,7 subject to the same cap and total budget.
No task/seed/label search and no cap tuning based on accuracy.

Hard bounds: at most 1800 seconds cumulative compilation/initialization/solve
wall time, 100 scalar/reference solves, 60 seconds per compilation,
45 seconds per solve, 12000 diagrams, 1000000 retained terms and 1.5 GiB
compiler RSS. High-K failure does not trigger a larger budget. Source edits
repairing correctness require rerunning affected comparisons; performance
changes must preserve exact RHS semantics. Retain failed/incomplete records.
Fresh products: data/generated/neural_response_memory_20260922/scalar_direct01/.
End after the predeclared panel and refinement, regardless of outcome.
