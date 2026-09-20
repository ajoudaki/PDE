# Independent review of cyclic uniformity

**Verdict: PASS.** The corollary establishes a single strictly positive
scalar fitting rate and uniform bounded-state constants over every
canonical cyclic three-input orbit. The zero-moment folded endpoint is
correct. No independent-perturbation conclusion outside the previously
proved small-opening family is inferred.

Review date: 2026-09-18. The complete new file was read, using only the
previously assigned frozen initialization and scalar-clock arguments and
their exact canonical scientific inputs. No experiment, numerical
diagnostic, other study, README, or other review was read or used.

Reviewed `cyclic_uniformity.md` SHA256:
`c415c05c28cf51164dd44f4368648c7bc78d8eb114286df7155590489942e598`.

## 1. Normalization and initialized activity on the entire sphere

The displayed raw inputs are `x_j=sqrt(3)P^jv`. Under the canonical
convention `u=x/sqrt(d)` with `d=3`, their normalized inputs are exactly
`u_j=P^jv`. Thus the contraction `a_0(v)` and the unit-input clock bounds
are the correct ones; no factor of sqrt(3) is missing from the dynamics.

The audited positivity certificate proves that T is odd and has the strict
sign of its argument. Its expectation formula is continuous on the closed
interval `[-1,1]`, including both endpoints, by dominated convergence.
Therefore

\[
 z(v)=(T(v_1),T(v_2),T(v_3))\ne0
 \qquad(v\in S^2).
\]

This conclusion covers all unit directions, rather than only a neighborhood
of the diagonal. The exact canonical coefficient and mark permutation
symmetries give `z(P^jv)=P^jz(v)` for the same fixed dictionary.

For any nonzero z, the initialized averaged upper feature cannot vanish
identically near zero. Writing `l_j(B)=B^T P^jz`, its linear term is

\[
 \frac13\sum_j l_j(B)
 =\frac{z_1+z_2+z_3}{3}(B_1+B_2+B_3).
\]

This is nonzero if the coordinate sum of z is nonzero. Otherwise
`l_0+l_1+l_2=0`, and its cubic term is

\[
 -\frac19\sum_j l_j(B)^3
 =-\frac13 l_0(B)l_1(B)l_2(B).
\]

Every factor is a nonzero linear polynomial because each `P^jz` is nonzero.
Their product is a nonzero polynomial. A nonzero Taylor term rules out
vanishing on any neighborhood of zero. The upper mark law has strictly
positive density on an open cube containing zero, so a neighborhood on
which the feature is nonzero has positive probability. Consequently
`k(v)>0` for every v, including the dependent cyclic orbits.

## 2. Compactness, clock protection, and uniform constants

For every fixed upper mark, `m_v` is continuous in v. Since `|m_v|<=1`,
dominated convergence proves continuity of `k(v)=E[m_v^2]` on all of
`S^2`. A continuous positive function on this compact domain attains its
minimum at some point, and positivity at that point proves

\[
 k_*:=\min_{v\in S^2}k(v)>0.
\]

No neighborhood-dependent lower bound is substituted for this argument.
The definition uses only fixed canonical initialization expectations and
the fixed input sphere. It is an exact positive constant, although the
corollary supplies no numerical evaluation or explicit numerical lower
bound; neither is needed for its asserted existence and uniformity.

For each v, equal weights and the cyclic permutation symmetry make the
three reached predictions equal. This remains true at the fixed points of
P, where the three inputs are compatible duplicates. The previously
proved scalar-clock lemma therefore applies without an independence
assumption and gives

\[
 F_s\ge k(v)\ge k_*,\qquad s_*\le1/k_*,
 \qquad L'(t)=-4F_sL(t)\le-4k_*L(t).
\]

Canonical initialization gives `L(0)=1`. The physical-time bound and actual
fitted endpoint consequently follow exactly as stated. Evaluating the
clock's polynomial state bounds at the common time `1/k_*` gives uniform
bounds because the feature envelopes, D, and normalized input norms are
fixed. For the first layer, the supremum bound concerns `w-g`; w itself
is bounded in L2, as in the underlying theorem. No boundedness of Gaussian
g in supremum norm is required.

## 3. Full opening interval and the signed zero-moment endpoint

For `v_theta=cos(theta)(1,1,1)/sqrt(3)+sin(theta)(2,-1,-1)/sqrt(6)`,
the already verified Gram eigenvalues are

\[
 3\cos^2\theta,\qquad\tfrac32\sin^2\theta,
 \qquad\tfrac32\sin^2\theta.
\]

They prove independence throughout `0<theta<pi/2`. At zero the directions
coincide. At `pi/2`, the three unit directions have pairwise dot product
`-1/2` and sum zero, hence form the stated planar 120-degree orbit.
The positivity and compactness proof includes both endpoints, so the
same scalar rate applies throughout this closed interval.

Let the three raw inputs at the planar endpoint before sign folding be
`X_1,X_2,X_3`, so `X_1+X_2+X_3=0`. Set

\[
 (x_1,x_2,x_3)=(X_1,X_2,-X_3),\qquad
 (y_1,y_2,y_3)=(1,1,-1).
\]

Then `x_3=x_1+x_2` and, for weights `p_i=1/3`,
`sum_i p_i y_i x_i=(x_1+x_2-x_3)/3=0`. A homogeneous linear
predictor fitting the first two labels would predict 2 at `x_3`, so it
cannot fit the third label -1. The assertion concerns linear predictors;
it does not claim an obstruction to affine predictors with an intercept.

At every state, the bias-free closure is odd in its input. Simultaneously
negating one input and its label thus leaves its squared loss equal as a
function of the entire state, and hence preserves the complete gradient
vector field. This verifies the signed version for any selected subset of
inputs, including the displayed endpoint. Nonlinear fitting of this
configuration is therefore an exact consequence of the scalar theorem,
not an inference from the vanishing input moment.

## 4. Scope check

The result concerns cyclic orbits of the fixed coordinate permutation,
with equal weights and labels obtained by the specified simultaneous
input-label sign changes. It does not imply arbitrary rotation invariance,
arbitrary triples, arbitrary weights, balanced mixed-label masses, or
finite-population/finite-network fitting. The signed three-point reference
has class masses 2/3 and 1/3. The degenerate endpoints are expressly
identified; scalar protection there does not supply full three-residual
rank or an open neighborhood of successful independent perturbations.
The corollary correctly preserves that distinction.

All claimed obligations are supplied by the frozen inputs and the complete
new argument. No correction or conditional downgrade is required.
