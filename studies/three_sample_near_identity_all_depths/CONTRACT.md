# Accepted target: three inputs and a genuine perturbation of identity

2026-09-08. The user explicitly rejected the overall-gain family and
requires the activation to remain a perturbation of the identity,
with its nonlinear strength controlled by theta. The nonlinear part
may be changed, and a small offset is permitted. The primary family is

    phi_theta(z)=(1-theta)z+theta atan(z), 0<theta<=1/2.

A legitimate alternative to investigate is

    phi_theta(z)=z+theta[b+epsilon atan(z)],

with b small and epsilon>0. It obeys a genuine small C1 perturbation
bound; no factor proportional to 1/theta may be hidden in its nonlinear
part to reproduce a large overall gain. No gain result is an answer to
this accepted target.

For every admissible triple ||x_i||²=d, |x_i^T x_j/d|<=1-delta,
0<delta<=1, arbitrary binary labels and each fixed finite hidden depth
L>=2, seek an explicit positive threshold depending on delta and L
(preferably with good depth dependence) that proves the full global
canonical strong population/GF/raw-GD theorem. Use the original raw
metric, independent Gaussian initialization, finite Gaussian readout
N(0,n^-2), and simultaneous raw-GD step n^-2. Train every block.
Singular three-input Grams cannot be excluded. Full observables include
genuine action adjoints, all L+1 raw kernels, compact-time full-sequence
width limits, same-layer path and velocity W2, moments/speeds, strict
activation nonaffinity and initial feature motion. A time-uniform
nonaffinity constant may depend on fixed depth; a positive absolute
constant uniform over all depths is a separately stronger claim.

The status at this directory's creation is OPEN in this analysis for
the complete accepted theorem, already at L=2 under only pairwise
separation. This is not a literature-wide impossibility or openness
claim. No counterexample to the qualitative positive-theta theorem has
been established. Previous all-depth gain work is outside scope.

New routes after the user's correction: covariance-weighted source
control; true-gradient energy-preserving finite-partition construction;
and an affine comparator with a small offset. The initialization
recursion is audited independently, including its sharp depth scale.
Global fitting, source continuation and identification must not be
inferred merely from initial Gram positivity or bounded raw energy.

The work is theoretical. No experiments, changes to old theorem files,
commits or external publication are undertaken.
