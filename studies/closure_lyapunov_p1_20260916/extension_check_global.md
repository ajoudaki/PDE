# Post-freeze analytical check of the angular extension

2026-09-16. Scope: `route_extension.md`, read only after this route's own
antipodal proof was frozen in `route_global.md`. This is an author-side
cross-check, not a fresh isolated review or promotion approval. The original
route file is unchanged. No experiments were performed.

**Conclusion:** the explicit positive interval near antipodal separation,
its physical-time exponential convergence, and the strict endpoint upper
hidden separation gain are supported by the displayed argument. I found no
substantive mathematical gap in the candidate. The constants are very
conservative, as the candidate acknowledges.

## Checks that carry the theorem

The p=1 initialization reduction agrees with my independently frozen route.
Grouping canonical Cholesky coordinates by axis gives the stated positive
entries of m_0 and a_0, and hence k_0>0 without a numerical integration or
a small-ridge assumption.

For the symmetry, substituting the transformed state gives

\[
 a_{TX}(u)=J_1a_X(Ru),\quad
 H_{TX}(u,b_2)=H_X(Ru,S_2b_2),\quad
 f_{TX}(u)=-f_X(Ru).
\]

Since R swaps the pair of inputs, F(TX)=F(X). The map T is an isometry in
the fixed population metric and fixes initialization. Thus its gradient
is equivariant; uniqueness gives TX=X for both the physical loss flow and
the feature-gradient flow. The latter has exactly the stated components,
and multiplying them by 2(A-F) recovers the physical equations, including
the factors from the probability weights and the unhalved loss.

The feature-gradient flow is globally defined on every fixed finite
feature-time interval: its readout, matrix and row speed bounds are
1, s and (2+s^2/2)s, with the bounded lower-mark envelope inserted for
the row supremum norm. These integrate to the stated bounds. They also
justify the local Lipschitz and continuation steps in the characteristic
space with w-g bounded, even though the frozen Gaussian g is unbounded.

For clarity, I recomputed the comparison estimate rather than relying on
the candidate's assertion. Denote the three state errors by E_w,E_c,E_M.
The row velocity error is at most

\[
 R E_c+C(2R+1)E_M+C(2R^2+2B_1R)E_w
 +\{C(2R^2+2B_1R)W+RC\}\delta.
\]

The middle velocity error is at most

\[
 E_c+2CE_M+(2CR+C)(E_w+W\delta),
\]

and the readout velocity error is at most E_M+R(E_w+W delta).
Their sum has exactly the three coefficients printed in the candidate.
Its L dominates each state-error coefficient, and P=L W+RC dominates
the input-error coefficient. Consequently the displayed Q estimate is
valid. The subsequent estimates for U, C and F follow with exactly H
and J as written.

The readout separation is bounded away from zero for the entire auxiliary
interval before interpolation: C_epsilon>=kappa_0/2. Since the axis
prediction at S is at least 2A and its perturbation costs at most A/2,
the perturbed feature trajectory crosses A strictly before S. Positivity
of F_s supplies uniqueness of that crossing.

## Strict endpoint gain

The endpoint gain estimate remains valid when the stopping feature time
depends on epsilon. The uniform gradient bound gives s_*>=A/K_*, and all
axis estimates are uniform on [0,S]. On the axis,

\[
 d(s)\ge s h_*,\qquad
 k_s\ge s h_* k_0^2/R^2,
\]

because k>=k_0, |m|<=R, and the upper gate is at least
sech^2(B_2 R). Also

\[
 \frac{d}{dk}E\tanh^2(\beta_2k)\ge2h_*.
\]

Therefore C_axis(s)-kappa_0>=h_*^2 k_0^2 s^2/R^2. At s=s_* this
is at least g_*. Comparing the perturbed and axis C at each of 0 and s_*
costs at most 4H delta in total. The selected delta_* makes that cost at
most g_*/2, so the perturbed gain is at least g_*/2. Multiplication by four
converts it to the claimed gain 2g_* in squared L2 distance between the
two actual upper hidden representations.

Thus the endpoint gain is neither inferred from loss decay alone nor
obtained by comparing different stopping rules without a uniform bound.

## Physical-time and state limit

On the finite feature interval K is continuous, bounded above by K_* and
below by kappa. The exact scalar identity
e_t=-2Ke makes e positive at every finite physical time and forces the
feature clock to converge to s_* as t tends to infinity. This constructs
the full physical trajectory, which agrees with the canonical one by
uniqueness.

The length estimate

\[
 \|\dot X\|=2e\sqrt K\le-\dot e/\sqrt\kappa
\]

integrates to the claimed finite remaining path length. Hence strong
population-metric convergence follows, as does convergence of the joint
laws under the common frozen-mark coupling. The already bounded
feature-time derivatives also give the stronger supremum convergence of
w-g and c. Continuity at s_* places the endpoint in the fitting set.

## Limits and presentational points

The theorem covers a positive interval of genuine non-antipodal data at
ordinary label amplitude, but does not quantify a useful practical angle
or cover arbitrary pair separations. It is solely a theorem about the
exact p=1 closure, with no claim of all-time identification with a neural
population limit. These scope limits are explicit in the candidate.

The formula defining the pair has a minor u/nu naming inconsistency;
using one symbol throughout would improve readability. Several envelope
and block symbols are reused locally but their types are stated; renaming
the lower block could also make the proof easier to read. Neither affects
the argument.
