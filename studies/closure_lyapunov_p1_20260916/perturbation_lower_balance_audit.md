# Audit of the first-layer balance and angular defect

2026-09-16. Fresh scoped mathematical check; no experiments and no other
study or route findings were consulted. The audited input is the complete
`perturbation_lower_balance.md`, frozen at SHA-256
`297cb7217b9318422548d0965b55e8e5f8588bf6b23ad69eafb2972f6ac3c3aa`.
This report applies to that version, before any author clarification.

**Verdict:** the algebraic identities, finite-horizon estimate, and narrow
pointwise cancellation obstruction are correct. Two minor scope
qualifications should be explicit: section 5 continues section 4's
assumption `m=d` with invertible input-coordinate matrix; section 3's
supremum envelopes are for a fixed bounded dictionary, here the prescribed
`p=1` dictionary, and are not uniform in closure order. Neither issue
invalidates the intended three-coordinate, fixed-order conclusions.

## Inputs and exact coverage

I read the complete frozen note and `docs/NOTATION.md`; checked the saved
state, physical equations, fixed-order existence and energy argument in
`docs/global_nonlinear.md` C.4.7.9; checked C.4.7.10 C.1's complete
equations, metric, and three-block kernel; and checked D.3's fixed-order
characteristic existence and envelopes. I also read the complete
`docs/observable_p1.md` for the general-dimensional initialized marks and
coefficient formulas. The note's reference to a study-specific proved
three-coordinate flow was not followed: that artifact was outside the
supplied input scope. The calculations below do not require it.

Coverage comprises every numbered formula (1)--(14), their signs and
physical factors, integrability and finite-horizon quantifiers, the exact
scope of the curl obstruction, and the local metric interpretation.
Required rigorous-math and research adversarial-audit instructions were
applied. No neural-network approximation or all-time convergence claim is
added.

## Gradient and balance identities

For a population row variation, differentiating the first pairing gives
`delta a_i=E1[b1 sech²(z_i) (delta w.u_i)]`. Substitution into
`delta f_i=d_i^T M delta a_i` gives the stated row gradient. The readout
and matrix variations give `H_i²` and `d_i a_i^T`. Their direct-sum
population-L2/Frobenius inner products prove (1), without any sample
weight inside K. With loss `L=m^(-1) sum r_i²`, the output equation is
`f_dot=-(2/m)Kr`; label conjugation therefore gives the displayed signed
equation. Each block is a Gram, even when individual off-diagonal entries
are negative. Applying the ordinary Gram inequality to the random scalar
coefficients `x_i sech²(z_i)q_i` proves (2), including equality at G=I.

The middle equation yields

    d/dt ||M||F² = -(4/m) sum_j r_j d_j^T M a_j,
    d_j^T M a_j = E1[tanh(z_j) q_j].

The derivative of `sinh² z_i` is `sinh(2z_i) z_i_dot`, with
`z_i_dot=-(2/m) sum_j r_j G_ij sech²(z_j)q_j`. These are exactly (4)
and (5). The diagonal identity
`sinh(2z_j)sech²(z_j)=2 tanh(z_j)` cancels the whole middle derivative.
Thus (6) has the correct positive sign, factor `2/m`, and ordered
off-diagonal sum. At G=I this proves conservation for arbitrary fixed
labels. With w(0)=g, every unit projection is standard normal, so
`E sinh²(g.u_i)=(e²-1)/2`, proving (7), without needing independence
among those projections.

The statement that both trained hidden contributions vanish initially
uses c(0)=0 and is correct. For the coordinate-axis orthogonal reference
of the prescribed p=1 dictionary, initial upper activations have the
form `tanh(kappa H_i)` with kappa>0 and independent symmetric H_i.
This follows directly from the coordinate-diagonal coefficient bands
in `observable_p1.md`: `E[h_i k_i]=beta>0`, since the conditional mean
of `tanh(sqrt(tau)Z+alpha h_i)` is increasing and has the sign of h_i;
all remaining factors and denominators in the two bands are positive.
The activation Gram is therefore diagonal with positive diagonal.
This verifies the stated reference positivity; it is not an assertion
of fixed-dictionary rotation invariance.

## Gaussian integrability and uniform finite-horizon bounds

The bounds need only finite fixed feature envelopes
`B_l=ess sup |b_l|`, finite initial D, and `Y²=m^(-1) sum y_i²`.
The usual local characteristic contraction applies in bounded
`w-g,c,M`. Along its local solution, the exact energy identity implies
`L<=Y²` and `m^(-1)sum |r_i|<=Y`. Consequently

    ||c(t)||infinity <= 2Yt,
    |a_i| <= B_1,   |d_i| <= 2B_2Yt,
    ||M(t)||F <= ||D||F + 2Y² B_1 B_2 t².

For any fixed T, let
`R_T=||D||F+2Y²B_1B_2T²` and `Q_T=2YT B_1B_2R_T`.
Then every input has `||q_i||infinity<=Q_T`, and
`||w-g||infinity<=A_T:=2YTQ_T`. These bounds prevent escape from the
local existence class at finite time. They are uniform over the unit
input configurations and depend on the fixed dictionary. They do not
assert uniformity in dictionary size/order or in T.

Since `|w.u_i|<=|g.u_i|+A_T`, the absolute values of `sinh²(z_i)`,
`sinh(2z_i)`, and the time-derivative integrands are bounded by constants
times `exp(2|g.u_i|)`. This Gaussian majorant is integrable. Dependence
between b_1 and g causes no problem because q is bounded by Q_T.
Dominated differentiation therefore justifies (3)--(6).

In (6), each fixed j has m-1 cross terms. Bounding each expectation by
`C_T=Q_T exp(2A_T) E exp(2|G|)` yields

    |B_dot| <= (2/m)(m-1) epsilon C_T sum_j |r_j|
             <= 2(m-1) epsilon C_T sqrt(L).

Integration proves both parts of (9); unit labels give L(0)=1. The
note correctly stops at compact horizons and does not infer all-time
smallness.

For the first-order coefficient in section 3, “perturbation of a
configuration” must have its ordinary meaning that the actual input
vectors tend to the fixed reference configuration, with the initialized
dictionary held fixed. Continuity suffices: (6) already has an
off-diagonal factor of order epsilon, so no trajectory derivative is
needed. On bounded existence balls, input variation and the bounded
features give a Gronwall estimate in row L2, readout supremum and matrix
norms. Gaussian exponential majorants then give continuity of the mixed
expectations. A Gram expansion alone, with arbitrary rotations of all
inputs relative to a fixed dictionary, would not identify a reference
trajectory. The note does not claim that stronger invariance.

## Pointwise cancellation obstruction and transformed metric

For a lower pointwise primitive J, coefficient matching against each
arbitrary drive `r_j q_j` requires

    sech²(z_j) (G grad J)_j = 2 tanh(z_j).

The gate is strictly positive at every finite z, so this is equivalent
to (10). Symmetry of `G^(-1)` then gives exactly (11). For any distinct
i,j one can choose z with different `cosh(2z_i),cosh(2z_j)`; hence a C2
primitive on the whole coordinate space forces every off-diagonal entry
of `G^(-1)` to vanish. The unit diagonal of G then forces G=I.
Conversely `J=sum sinh²(z_i)` works at G=I. Expanding the inverse gives
the displayed first-order nonzero curl. This is a complete obstruction
to the pointwise arbitrary-drive ansatz, not an obstruction for actual
reachable drives, expectation-only cancellation, or coupled potentials.

Finally `T'=cosh²`, so (12) follows by the ordinary chain rule. Under
the continued assumption m=d and invertible input matrix U (rows u_i),
`dz=U dw`, `UU^T=G`, and

    |dw|² = dz^T G^(-1) dz
           = d rho^T D(z)G^(-1)D(z) d rho.

This proves (13). The input configuration is fixed during training, so
G has no time derivative. Differentiating D gives exactly (14).
For a displacement v, the full quadratic derivative is
`2 v_dot^T H v + v^T H_dot v`, with H the matrix in (13).

If section 5 were instead read as covering m<d merely because G has
full rank, (13) would omit `|dw_perp|²`, the variation perpendicular
to the input span. It remains valid for variations restricted to that
span, including flow velocities, but not for the full state metric.
Explicitly retaining m=d is the appropriate clarification for the
intended application. The finite-state metric remains positive definite;
small gates supply no global uniform lower comparison constant.

The audited results are exact identities or compact-horizon estimates
within the finite closure. They do not establish an exponential
Lyapunov function, generic interpolation, or a trajectory-level
nonexistence theorem.
