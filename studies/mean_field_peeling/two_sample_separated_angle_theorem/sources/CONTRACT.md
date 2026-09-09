# Two-sample extension contract — 2026-09-05

User target: extend the proved one-sample L=3 joint population/GF result
to TWO fixed RMS-unit inputs with labels in {+1,-1}, distinct directions.
Activation changes are authorized, but effective affine collapse and a
lazy/frozen-hidden/kernel regime are prohibited. No numerical experiments.
We retain the stronger previous full MF/GF/exact-GD and observable contract.

USER CLARIFICATION: one IDENTICAL activation for ALL nonzero input angles
is the ultimate goal. Angle-dependent fixed coefficients are authorized
only as intermediate existence/sanity checks leading toward that goal.
They must not be presented as resolving the ultimate two-sample theorem.

Fix d and x_1,x_2 in R^d with ||x_a||_2^2/d=1 and
rho=x_1^T x_2/d<1. We include rho=-1 (antipodal), since the user excluded
angle zero but did not explicitly exclude angle pi. Constants may depend
on the fixed input pair; no separation uniform as rho approaches 1 is
asserted. No activation parameter may depend on width, final physical
horizon, mesh, clipping, or realized training trajectory. A data-dependent
fixed choice, if eventually needed, must be explicitly disclosed rather
than silently replacing a universal-activation assertion.

Use W^(1) of size n by d with independent N(0,1/d) initial entries,
z^(1)_a=W^(1)x_a, so the two first-layer initial coordinates have centered
Gaussian covariance [[1,rho],[rho,1]]. W^(2),W^(3) have independent
N(0,1/n) entries; the RESCALED W^(4) has independent N(0,n^-2) entries.
All initial blocks are independent. Hidden widths equal n; every block
is trained. h^(ell)_a=phi(z^(ell)_a), z^(ell)_a=W^(ell)h^(ell-1)_a,
f_a=(W^(4))^T h^(3)_a/n, r_a=f_a-y_a.

Loss convention is the average squared loss L=(r_1^2+r_2^2)/2.
With eta=n^-2, the natural RMS-input extension of the old raw updates is

 W^(1)+=W^(1)-eta sum_a r_a delta^(1)_a x_a^T/d;
 W^(ell)+=W^(ell)-eta sum_a r_a delta^(ell)_a(h^(ell-1)_a)^T/n, ell=2,3;
 W^(4)+=W^(4)-eta sum_a r_a h^(3)_a.

The 1/d factor makes a single RMS-unit input induce exactly the old
z^(1) update. Equivalently the raw metric is (d/n)||dW^(1)||_F^2,
ordinary matrix Frobenius norms for blocks 2,3, and ||dW^(4)||_2^2/n.
Consequently dot z^(1)_a=-sum_b r_b rho_ab delta^(1)_b.
Backwards deltas exclude the residual and use the original phi' gates
and both transposes. Physical t=k eta; raw parameters are interpolated
linearly and hidden objects recomputed. Right derivatives at nodes and
terminal-left convention are retained.

The limiting state may contain one R^d-valued first-layer field, the two
bounded population operators, and the readout field on three separate
neuron populations. Both hidden matrix orientations, all four 2-by-2 raw
kernel blocks (including off-diagonal entries), joint per-neuron sample
and time laws, hidden paths/velocities, prediction/loss, autonomy and
reached-state restart are required. Finite fields/operators are expressly
allowed, as in the original contract; no growing-width hidden state or
oracle trajectory forcing is allowed. No cross-layer neuron pairing.

The audited ONE-SAMPLE result remains valid and unchanged:
/tmp/l3-activation-design-oaGjWO/READ_ME_FIRST.md
Full proof hash d50b7708b767f20010437e48a716366ac32b5dd6db6e6e12beb94cd1d15897e5;
response hash 65579a94f883f1b9f9240430039f334f5b3b663599cd7ab16bb15c35f7bacc43;
generic Gaussian/action dependency:
/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/L3_LOCAL_COMPLETE_PROOF.md,
hash f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4.

Current two-sample status: OPEN. No global extension follows merely from
the one-sample theorem. Main is analyzing small fixed nonlinear
perturbations of affine activation as a potential route; no such model
has yet been chosen or certified. The existing bounded shifted-arctan
model is also retained as a candidate. Any partial same-label result
must not be presented as the arbitrary-label theorem.

Research uses solve-math-rigorously and investigate-conjectures, including
the required references. Fresh-context agents are authorized by the
continuing research/audit instructions; complete candidates require
isolated adversarial proof-only reviews. No source-task/agent resumption,
repository/branch/commit operation, or numerical experiment is requested.
