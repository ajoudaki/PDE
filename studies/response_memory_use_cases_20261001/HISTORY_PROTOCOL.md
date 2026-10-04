# Historical coordination and repair: frozen first-screen protocol

Status: written before implementation or experiments, 2026-10-01. This is a
bounded diagnostic route within the new practical-use study, not a continuation
of any prior generalization study.

## Questions

1. Do the centered forward/backward histories carry useful coordinated weight
   changes beyond their separate means? Compare removing their pairing and
   rotating one history's centered temporal coefficients while preserving its
   integrated second moments. A simultaneous rotation is an invariance control.
2. Can compressed historical writes from corrupted examples supply effective
   repair edits, followed by a fixed clean-training budget? The exact accumulated
   writes are the matched oracle. This is an intervention, never a leave-one-out
   or certified unlearning claim.

## System and data

Two tanh hidden layers, no biases or normalization, canonical Gaussian gains,
exact zero readout, normalized circle rows (cos(theta),sin(theta)), unhalved MSE,
source Flow Euler updates with mobilities (n,1,n). Pilot n=128, dt=1/64,
T=32, seeds 101,102,103. Twelve equally spaced training inputs with offset0.13;
teacher y(theta)=sin(theta)+0.5 sin(3theta). Evaluation uses 512 interlaced angles.
The corrupted panel reverses labels at indices1 and7, an antipodal pair, so odd
symmetry does not create an artificial fitting obstruction. Fitting is reported
separately; fixed-horizon effects remain meaningful if RMS exceeds0.1.

## History representation

Record the dense trajectory's pre-update h, residual-weighted delta and rho.
Regard these as piecewise constant on each physical Euler interval. Their exact
activity-history interaction reproduces the discrete hidden-weight increment.
Compute Legendre integrals over each interval analytically (not endpoint sampled).
For interpretation use actual learning interval [1,tau], excluding artificial
prefix; this is a post-training observer and intervention, not the autonomous
closure or the manuscript's prefix-including zeroth mode.

Reconstruct orders q=1,4,8,16,32. Full-history matrix accumulators serve as the
oracle. q32 must approximate the total and corrupted-sample increments within
2% relative Frobenius norm for primary interpretation; otherwise the diagnostic
is inconclusive with one allowed q64 refinement. Check simultaneous orthogonal
rotation invariance below1e-10 relative in float64.

## Interventions and metrics

Coordination: remove centered pairing, retain half, or apply five fixed seeded
orthogonal rotations to centered backward coefficients only. Use q32 or valid
q64. Match each intervention with a random matrix perturbation with identical
singular values (random left/right singular vectors). Report training/evaluation
RMS, dense-prediction difference and perturbation Frobenius norm; retain means
and both unpaired second moments as explicit invariants. A positive coordination
screen requires at least20% relative evaluation degradation on all three pilots
and median damage at least twice the matched random-perturbation damage. Failure
does not prove histories are uninformative; it rejects this intervention claim.

Repair: subtract the corrupted examples' recorded hidden updates, using exact
history or q1/4/8 reconstruction. Outer weights remain unchanged at surgery.
Compare no edit and a current clean-gradient hidden edit with the same Frobenius
norm; then apply the same T_clean=2 dense updates to all edited states using
corrected labels. Positive screen: q4 orq8 recovers at least80% of exact-history
repair benefit and reduces clean evaluation MSE by at least10% vs equal-budget
no-edit on all three pilot seeds. Exact-history failure is a valid negative
result; no temporal-window search follows it.

## Validity, branches and limits

Use float64 on CPU for initial n128 checks and screens (one thread, at most
10 CPU-minutes); GPU only when assigned by root. Record all source/environment
hashes and deterministic teacher arrays. A positive route gets five fresh
seeds201..205 at n256, dt1/64, with seeds201/202 repeated at dt1/128. If the
positive effect is smaller than twice the step-refinement change, call it
inconclusive. One T64 extension is allowed only if first-screen total hidden
increment Frobenius norm/n is below0.01. Maximum24 training trajectories and
15 GPU-minutes (if used). Retain all failures and don't tune on confirmation.

## Pre-confirmation implementation strengthening

Pilots101/102/103 passed the repair gate (19.7--23.9% benefit) and failed the
20% coordination-damage gate. Keep that negative coordination result; do not
extend its horizon to manufacture a pass. Proceed only with repair confirmation.
Before fresh seeds, replace offline q1/4/8 repair coefficients by genuinely online
moments. Store J_k=integral h(xi)(xi/S)^k dxi (and the analogous backward
history), where S is actual activity length. On adding a piecewise constant
interval of mass dS, update J_k <- alpha^k J_k + h S_new
(1-alpha^(k+1))/(k+1), alpha=S_old/S_new. Convert by the shifted-Legendre
polynomial coefficients. This is an invertible coordinate change of degree<8
moments, with exact insertion for the recorded Euler histories. Require agreement
with independently integrated offline moments within1e-6 relative. Float64
q<=8 only; no high-order power-basis stability claim. Retain original code as
`history_probe_initial.py` for exact pilot reproduction. The main repair
criterion and confirmation seeds remain unchanged.
