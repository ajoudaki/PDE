# Directly trained low-rank control (2026-09-24)

Prospectively specified continuation of the response-memory comparison. The
user explicitly requests a rank-matched, directly trained factor correction,
measured by full-circle discrepancy from the dense trained function. This is
not a new task-label generalization experiment or a QR/SVD truncation experiment.

## Question and controls

Does direct factor gradient flow reproduce the same dense endpoint function
as accurately as response-history moments at the same correction rank?
One possible outcome is that ordinary trainable factors explain comparable
endpoint accuracy. Another is that the moment evolution selects a substantially
more faithful dense-network function. Results concern these specified flows,
not optimality among all low-rank algorithms.

Use all five already tested cases, n=2048, P=1,3,7, and the exact existing
initial W1,W0,W3 (network seed 20260920). The original data and tanh architecture,
unhalved probability MSE and outer mobilities (n,n) are unchanged. The existing
exact antipodal quotient has four representatives; other cases have eight.
Rank is P times represented sample count: 8/24/56, or 4/12/28 for the quotient.
The correction has two trainable factors, 2nr coordinates, matching the two
moment-factor arrays; the moment implementation also has lifted responses.
Both methods retain exactly the same fixed dense W0 and its transpose.

The control is W2=W0+AB, with A of shape (n,rank), B of shape (rank,n).
Both factors follow ordinary Euclidean gradient flow with mobility one.
A starts at zero; entries of B are independent N(0,1/rank). Consequently
AB starts exactly at zero and E[B^T B]=I, so the expected initial induced
matrix velocity equals the canonical dense middle velocity. This expectation
does not make the realized factor flow canonical matrix gradient flow.
The scale is fixed analytically before outcomes, not selected for circle RMS.
Both-zero initialization is prohibited because it freezes both factors.
The actual induced velocity is

    d(AB)/dt = - (dL/dW2) B^T B - A A^T (dL/dW2).

No Adam, momentum, weight decay, reference-fitting, optimized learning rate,
or SVD compression. Factor seeds 20260924 and 20260925 are reported separately,
never selected by taking the better seed. Random directions are shared across
tasks and nested across rank (before the explicit 1/sqrt(rank) scaling).

## Measurements and numerical validation

Each model stops at its own first physical training-MSE 0.001 crossing, as in
the existing campaign. Primary metric: RMS prediction difference over the
same 8192 uniform circle nodes. Use the finest already validated dense target
for each case: fresh level2 references for four cases, original refined target
for the hard outlier case. Also retain archival-target scores for provenance.
No values of this metric or dense predictions enter the training equations.
Training loss is a stopping condition, not the ranking metric. Saved common-time
predictions supplement the endpoint comparison without replacing it.

Float64 adaptive explicit Heun/Euler, initial step .05, max step 2,
min step 1e-7, canonical physical horizon cap 10000, at most 30000 accepted
steps, 32 bisections to locate the loss crossing. Control local errors of raw
outer/factor coordinates and the represented matrix correction. Integrate
levels 0 and 1 (rtol 6.25e-5 and 1.5625e-5, atol=rtol/100).
Reject numerical steps that increase loss beyond rounding allowance, consistent
with the exact energy identity for this factor gradient flow. This is a time-step
acceptance rule, not an additional term in the differential equations.

Validity requires fitted status; exact initial weights and zero correction;
independently recomputed endpoint loss within 1% of 0.001; finite states;
8192 versus nested4096 RMS agreement within 1e-5; and level0/1 endpoint maximum
prediction change at most 0.01. A failed refinement gate or a comparison gap
within three times the observed combined numerical RMS sensitivity permits
one level2 run for that cell, up to 15 such runs. Finest available level is
selected irrespective of whether its score improves. Unresolved cells remain
inconclusive. Observed refinement differences are not certified error bounds.

Report every paired score. A directional difference is called resolved only
when it exceeds three times the largest observed factor, moment, or dense RMS
refinement change; within that scale call it numerically unresolved. A factor
of two or more is labelled a substantial difference only after this check.
No pooled best-of-seeds score or asymptotic rate is inferred.

## Budget, provenance and stopping

60 primary trajectories = five cases, three ranks, two factor seeds, two
tolerances. At most 15 conditional numerical refinements, hence 75 total.
Cumulative integration cap 3600 GPU-seconds; each trajectory at most 240
seconds. Run one worker on each available GPU. Stop at completed protocol,
budget exhaustion, or a numerical blocker; do not add tuning branches.
This is a new authorization; the earlier completed moment budget is closed.

New outputs go to data/generated/neural_response_memory_20260922/factor_control01
and a fresh analysis directory. Save factors, outer weights, predictions,
loss/time traces, initialization and source/data hashes, commands, software,
hardware, timings and all failures. Existing closure and reference files are
read-only. New engine identities receive deterministic CPU checks and final
comparisons receive an independent reconstruction check before synthesis.

Root owns this protocol, README and synthesis. factor_control_impl owns the
three new implementation/test files; factor_control_design provides a prompt-only
normalization check. These are internal checks, not promotion reviews.
