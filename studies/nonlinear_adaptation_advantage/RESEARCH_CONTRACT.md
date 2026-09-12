# Frozen research contract: E₀

This study asks for a theorem, not an experiment. It is not assumed that the
requested positive result is true. Its failure on one family or by one proof
route is not an impossibility theorem.

## Exact object and comparison

Use all conventions, initialized Gaussian action reuse and actual adjoint of
`docs/global_nonlinear.md` C.4.9–C.4.10. Bias-free two-hidden-layer tanh;
physical input x=sqrt(2)u, u on S¹; stored Gaussian variances (1,1/n,1/n²),
mobilities (n,1,n), output division by n, unhalved squared loss, actual GF.
Retain full first-row fields and actual finite random initial readout.
Every actual network trains from original initialization throughout on
mu_(epsilon,nu)=(1-epsilon)nu_*+epsilon nu, with exactly weighted known anchors
nu_*=(delta_(sqrt(2)e1,+1)+delta_(sqrt(2)e2,-1))/2. No endpoint restart of an
actual network is admissible.

Let theta_dagger and F_* be the established fitted reference. Let d_dagger(u)
=Pi_dagger g_dagger(u), using every raw parameter block. The full frozen kernel
is k_dagger(u,v)=<d_dagger(u),d_dagger(v)>_raw. In angular pullback and normalized
arc measure rho, with input density p and regression q, compare nonlinear
selected prediction P_nu with

    (F_fr)'(tau,u)=-2 integral k_dagger(u,v)(F_fr(tau,v)-q(v))p(v)d rho(v),
    F_fr(0)=F_*.

Both start at the same predictor, use the same data, metric and canonical slow
clock tau=epsilon t. This is neither original-initialization NTK nor readout-only.

## Required theorem and interpretation

Choose an explicit ordinary task family independently of trained predictions,
starting from B's q=q0+h v, q0=cos³(alpha)-sin³(alpha), h=sin²(2alpha), with
weighted odd Fourier coefficients; a fixed finite cap suffices. Require
multiple independently varying quantitatively active harmonic components,
full-circle density support, stated coefficient ranges, and robustness radii
for target and density perturbations in specified topologies, relative to the
target scale. Exclude stationary/degenerate cases explicitly. Do not turn a
single favorable witness into the intended class only by continuity.

Prove one common finite T>0 and a>0 with

    E_nu(F_fr(T))-E_nu(P_nu(T)) >= a,
    E_nu(f)=integral |f-q|² p d rho,

uniformly on the declared family. T and a must not vanish with width,
contamination or sample count. State every dependence and evaluate enough
constants/remainders to verify positivity, disclose impractical or unevaluated
conditioning, and compare the advantage to total learning achieved.

Also prove a beneficial change in relative learning of task components using
a justified prediction-space decomposition or normalization in the common
metric, fixed for an independently interpretable purpose. Account for all
interactions and remainders at finite T. Hidden motion, a nonproportional
kernel, favorable initial derivatives, formal jets, an assumed Taylor radius,
or conditional continuation do not complete this requirement. The base risk
theorem uses matched clocks. Scalar controls interpret the effect without
requiring superiority to arbitrary frozen acceleration. Any stronger tuned
comparison needs an explicit cumulative-clock budget and shared/task-specific
tuning rule. Attribute initially to nonlinear constrained evolution; a middle
layer attribution requires extra proof. No initialized-NTK, unknown-structure,
trained-shallow or resource-efficiency superiority follows automatically.

## Sampling and finite networks

Use identical iid added observations and noisy labels for both empirical
learners. Keep B's exactly weighted known anchors and bounded conditionally
centered noise. Prove positive population-risk comparison after sampling with
sample threshold and confidence. Preserve width-first, contamination-second,
sample-last order unless stronger order is proved. Distinguish uniform
population conclusions from finite-width convergence for each fixed member.
Any claimed finite frozen realization needs its own approximation argument.

## Search, evidence and completion

Develop a small genuinely diverse portfolio in fresh contexts. Independent
routes receive only this contract, required skills/process instructions and
specified established source scope; they do not read one another until frozen.
Each returns precise claims, complete derivations, checked dependencies,
counterexample/sanity checks, exact gaps and a route status. No experiments.

No imposed numerical research budget; concurrency is at most three independent
workers plus coordinator. Focus each route on its decisive proof obligation.
Do not repeatedly shrink/redesign the family to manufacture a positive result.
Preserve the strongest valid results if substantive alternative routes leave a
decisive gap. E₀ then remains unresolved, not complete. Successful results must
undergo the full repository promotion process before established files change.

All source, configurations and original review records stay flat in this study;
generated checks use its generated-data namespace. Root alone edits shared
current notes and performs scoped Git transactions under the shared writer lock.
