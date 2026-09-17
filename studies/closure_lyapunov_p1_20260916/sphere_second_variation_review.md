# Independent review of the trained sphere second variation

Date: 2026-09-16.

**Verdict: PASS for the stated finite-horizon theorem and structural conclusions.**
I found no mathematical defect that invalidates the C2 solution map, the cubic
Taylor remainder, the displayed variation systems, global positivity of C0,
the five symmetry cancellations, or the small-time global Hessian-sign
obstruction. This is an internal mathematical review, not promotion approval.
The minor clarifications below do not change the conclusions.

## Frozen inputs and exact review scope

The complete 707-line target was
`sphere_second_variation.md`, SHA256
`8f8d25d84f6bbb41b09ad1f5900970bb5ccbd7ea266ac0c6179ef961752eb1a8`.
The hash was verified before review. I also read the complete
`perturbation_modes.md`. After explicit expansion of the review scope, I read
the complete 711-line `three_coordinate_candidate.md`, verified as SHA256
`531b1cb1fe5e5844fcc6da25486e6ee52450860030dd770246e3ee78592521ce`.
The latter supplied the exact initialized scalar representation and its
strict-monotonicity proof, and the full-state permutation isometries.

Established inputs read were complete `docs/NOTATION.md`, complete
`docs/observable_p1.md`, `docs/global_nonlinear.md` C.4.7.9 through its
state/dynamics/well-posedness/restart argument, complete C.4.7.10.B and D.3,
and C.4.7.10.C.1 through the exact finite equations. The review used the
required mathematical skill and the conjecture skill's adversarial audit.
I read no study README, history, earlier verdict, other reviewer report, or
other study. References inside these inputs were not followed outside this
scope. No experiment, numerical sign calculation, code audit, or network-limit
extension was undertaken.

The audited claim is dependence of the fixed p=1 characteristic flow on the
six data coordinates, for each separately fixed finite physical horizon.
The initialization, both populations, dictionary, full middle matrix,
transpose, and population-L2/Frobenius metric remain those specified in the
target. I did not require an all-time perturbation theorem, a Hessian sign at
the symmetric reference, or a perturbed Lyapunov inequality.

## Mathematical checks

### 1. Base flow and weighted regularity

The normalized feature maps are contractions by the exact ridge-Cholesky
identity. Consequently the energy identity and bounds (18) have the stated
constants: the mean absolute residual is at most one, the readout speed is
at most 2, the matrix speed is at most 4t, and the row speed is at most
`4 B1 t (d0+2t^2)`. Integrating gives precisely the displayed polynomial
bounds. Bounded increments and speeds in the local supremum-norm existence
space give continuation through every finite time. No higher-dimensional
network theorem is needed for this finite-feature characteristic argument.

The spaces E_k in (19) are appropriate to the actual Gaussian marks. Only g
needs a polynomial weight; the reverse Gaussian marks enter through bounded
frozen features. For every k, their lower component embeds continuously in L2
with factor `(E rho^(2k))^(1/2)`. The upper component retains its L-infinity
norm, so the embedding is into the entire product norm stated in the theorem.

The Lipschitz estimate (20) is valid on bounded c/M regions without an
unweighted bound on w. The row gate difference is bounded by a constant times
the row difference. The other occurrence of that difference is contracted
against bounded b1 and hence costs only a finite Gaussian moment. All
remaining row multipliers, particularly Q_i, are uniformly bounded on the
region. This reasoning applies to the true state and the polynomial
approximation even though the latter need not have a bounded row increment
over g in the original local-existence norm.

The first-response homogeneous operator is bounded on every E_k. Its data
source is O(rho), and the second-response source is O(rho^2), including both
first-response products and the sphere curvature. Thus (22) and (23) follow
from the stated linear integral argument. The unknown second response enters
with the same homogeneous state operator as the first response.

The cubic remainder estimate survives the unbounded Gaussian tail. For the
quadratic state polynomial, the preactivation increment is bounded by
`C (|epsilon| rho + |epsilon|^2 rho^2)`. Cubing it is bounded by
`C |epsilon|^3 rho^6` for `|epsilon| <= 1`; the lower-order discarded chart
and product terms obey that bound as well. Tanh and the gate have the bounded
derivatives needed for this scalar Taylor estimate. Integrating lower
contractions uses the finite sixth moment. The actual upper fields and
approximating c/M blocks remain bounded, so multiplication introduces no
additional unbounded factor. The degree-zero through degree-two cancellation
is exactly (10)--(11), proving (24). Stability in E_6 then gives the cubic
remainder in the asserted path-space norm.

The derivative-continuity argument uses the correct weight losses: changing
a lower gate costs O(data difference times rho); multiplying by a first
response costs rho^2 and multiplying by a second response costs rho^3.
Differences of products of two first responses also fit E_3, using the E_2
first-response comparison. On a common smooth chart these bounds are locally
uniform in the base data and directions. The uniform quadratic expansions
and these continuous linear/bilinear coefficients identify continuous
Frechet derivatives. The proof is therefore stronger than a formal or
pointwise directional calculation. It does not assert a C2 vector field on
an unrestricted L2 state ball.

### 2. Variation equations and scalar composition

I checked every product-rule term in (5)--(11). The sphere chart gives
`v_eta,theta = -(eta dot theta) v`; the lower preactivation includes this
normal term and both state/input mixed terms. The reverse pass differentiates
the same M transposed. The gradient row includes the two first-input terms
and its normal-curvature term. The factor `-2/3` is consistent with the
unhalved mean-square loss and physical metric. Since all initialized state
blocks are data independent, all initial state derivatives are zero.

Equations (12)--(15) have the complete Gram, loss, readout-norm, and prediction
derivatives. The initialized hidden field varies with the input even though
the initialized state does not; (14) accounts for this distinction. The
fixed-state prediction Hessian (15) is correctly separated from the trained
Hessian (8).

All partial derivatives in (16) are correct, including A_FC, A_qC, and A_CC.
The full chain and product rules in (17) include the changing C0 and all mixed
terms. They agree with the separate frozen-normalization convention only
after the C0 derivatives are explicitly set to zero. There is no omitted
dataset dependence in the target's chosen potential.

### 3. Global positivity of C0

Section 5 of the supplied initialization dependency proves (25) for every
unit input, not just the symmetric triple. Its scalar monotonicity argument
allows a negative coefficient A and establishes a strictly positive lower
bound for the derivative of `A x + B m(x)`. In particular the estimates
`B <= 1/gamma <= 1/(q_* b_*)` and
`d(Ax+Bm(x))/dx >= 34 alpha/529` have the correct inequality directions.
The Gaussian integration-by-parts formula then proves that kappa is odd and
strictly increasing, with continuity at its endpoints. Thus k(v) is nonzero
for every unit v, as the target requires.

If C0 vanished, positive density and continuity would make the sum of the
three tanh linear forms vanish throughout the open cube. A line avoiding
their three zero planes makes all three slopes nonzero. Real analyticity
extends the identity along the entire real line, while its positive-infinite
limit is an odd sum of signs and cannot vanish. This proves strict positivity
for every triple, including duplicate and antipodal triples. Continuity on
the compact product of spheres then gives a positive minimum. The proof
claims no computable numerical lower bound and needs none here.

The separate loss obstruction at `(v,v,-v)` is also exact: oddness enforces
loss at least 8/9. Since the potential dominates the loss, an all-data
positive-rate exponential decay inequality is impossible. This does not
contradict the symmetric theorem or local perturbative fitting.

### 4. Hessian sign and symmetry

At time zero, the only nonzero state velocity is `c_dot = 2 U0`. It follows
that `F_dot = 2 C0`, `L_dot = -4 C0`, `A = 2`, and `A_dot = 0`.
Hence (27) has the correct coefficient `Phi_dot = -8 C0`. The response
equations give the time derivatives of both data responses and justify (28);
no unproved infinite-time Taylor expansion is being used.

The two triples `(v,v,v)` and `(v,v,-v)` have C0 values in ratio nine. Their
different initial potential velocities imply that Phi(t,.) is nonconstant
for every sufficiently small positive t. A scalar function with an
everywhere semidefinite sphere Hessian would be constant on each periodic
great circle, hence independent of each input. The contradiction proves
both a positive direction somewhere and a negative direction somewhere.
The same argument applied only to single-input great circles verifies the
stronger assertion that each sign can occur on a direction moving one input.
It supplies no sign at a specified point, exactly as the target states.

The permutation isometries apply to the entire trained flow and frozen
dictionary. At the symmetric data, invariant tangent matrices have common
diagonal x and off-diagonal y subject to `a x + 2 b y = 0`, so the invariant
space is one dimensional and the averaging kernel is five dimensional.
Thus (29) proves all five listed scalar first variations vanish on that
kernel. This is a guaranteed cancellation subspace; it does not assert that
a particular scalar has a nonzero derivative on its remaining direction.

The alternating line (30) is tangent and is the sole sign representation.
Group averaging therefore removes Hessian cross terms among that line, the
invariant line, and their orthogonal complement. It does not make either
four-dimensional restriction scalar or impose rotational invariance.
Finally (31)--(32) correctly separate the positive disagreement term from
the unconstrained second trained mean, readout, and initialization responses.

## Defects versus clarifications

**Rigorous defects requiring correction:** none found in the stated scope.

**Minor presentation improvements:**

1. In the theorem, explicitly qualify the Hessian identification by “in the
   chart (2), or any chart normal to second order.” An arbitrary smooth sphere
   chart has an additional first-derivative/connection term. Section 2 already
   supplies the correct qualification and curvature formula, so this is a
   wording clarification rather than a failure of the argument. Likewise,
   cubic constants in other charts are local constants on a neighborhood with
   bounded derivatives of the coordinate change.
2. Near (24), display the polynomial as
   `X_hat = X + X_epsilon + (1/2) X_epsilon,epsilon`, and state that the
   response-continuity comparisons use one common smooth local frame/chart.
   This makes the identification of the bilinear response with the second
   Frechet derivative easier to check; the needed estimates are present.
3. Name `three_coordinate_candidate.md`, Section 5, immediately before (25),
   and Section 4 when invoking its permutation isometries. The introduction
   declares this dependency, but the local references would make the two
   nontrivial imported premises easier to locate.

The explicit claim boundary in Section 8 is respected. No conclusion here
provides uniform-in-time response bounds, transverse coercivity, a reference
Hessian sign, generic fitting, closure-order accuracy, or a d=3 trained-network
limit.
