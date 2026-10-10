# Reused-context internal audit of the both-tanh construction

2026-10-10. Reviewer context: `two_layer_persistence`. This is a reused-context
internal mathematical check, not a fresh independent review and not promotion.
The reviewer previously contributed to the geometry arguments. The audit read
both complete frozen files below, used the required proof, research-audit and
canonical-notation instructions, and performed no experiments or external
literature retrieval. No proof file was edited by this reviewer.

## Frozen inputs and verdict

| Input | SHA-256 |
|---|---|
| `TANH_BAD_BASIN.md` | `f975c3bd44d9ad97ca22102908e69a181ac1bd4de491781497e9ce65d3d55a53` |
| `TANH_GEOMETRY.md` | `3ac627b10bfe44001724359a0917b201577238a8312df907f79f7031e1e00cd0` |

**Internal PASS for the stated finite-width claims.** No unresolved mathematical
gap was found in either frozen input. In particular, the first file proves an
open bad basin on the exact zero-readout initialization slice, not merely a
positive-readout local minimum. The data and labels can be fixed independently
of width. The resulting Gaussian probability is positive separately at each
fixed width; no lower bound uniform in width follows.

The verdict concerns exactly the hashes above. It does not supply the fresh
independent reviews or approval required for promotion.

## Nine functions and the residual moments

The independence proof in Section 2 is valid. After division by the strictly
positive top derivative and the substitution `u=tanh(t)`, the coefficients of
the quadratic polynomial in `arctanh(u)` are analytic near `u=1`. Writing
`v=1-u` produces a polynomial in `log(v)` with analytic coefficients. If any
coefficient were nonzero, selecting the smallest finite Taylor order would
leave a nonzero polynomial in `log(v)` plus a remainder tending to zero. Such
a polynomial cannot tend to zero as `v` decreases to zero. Thus all three
coefficient functions vanish.

The subsequent reductions also check: the limits after division by
`chi=1-u^2` eliminate the quadratic-log terms; nonconstancy of `u*tanh(u)`
eliminates the linear-log terms. Multiplication of the remaining identity by
`cosh(u)` gives an entire identity. The `exp(3u)` term eliminates its first
coefficient, and exponential growth followed by polynomial parity eliminates
the rest. This excludes a relation on every open real interval.

Consequently nine distinct invertible evaluation nodes exist in the prescribed
interval. The factors of one half in the paired residuals correctly make each
pair contribute `rho_j F_k(t_j)`. The two positive matrix-moment entries are
`1` and `2-1=1`; the corresponding zero-matrix entries are `0` and `0-0`.
Off-diagonal entries and second vector coordinates cancel between pairs.
Every identity in (6) follows with the stated signs. Its final identity proves
that the residual is nonzero, while `h^T r=0` implies that `bar y=h-r` is also
nonzero.

## Full Hessian and attraction

The Hessian calculation covers arbitrary variations of every neuron and every
matrix entry. Re-expansion gives

\[
\delta^2 f_a=\frac1n\sum_i\left[
2c_i\psi_a\delta Z_{ia}
+\epsilon(-2h_a\psi_a)(\delta Z_{ia})^2
+\epsilon\psi_a\delta^2Z_{ia}\right].
\]

The contracted mixed readout, mixed matrix/first-layer, and mean-first-layer
terms vanish by the specified moments. The two surviving residual terms are

\[
\sum_a r_a\delta^2f_a
=\frac{\epsilon}{n}
\left(\sum_i b_i^2+\sum_j\|a_j\|^2\right).
\]

The actual residual at the proposed minimum is `epsilon r`, giving exactly
the `epsilon^2` coefficients in (11). In particular, neuron splitting has
not been restricted to symmetric directions. The kernel is exactly (12),
since `epsilon>0` and the feature vector `h` is nonzero.

The kernel is the tangent space of the actual affine critical manifold (13).
Every point of that manifold has identical features and predictions. The
first-layer gradient has a possibly varying column coefficient multiplying
the same zero vector moment, so criticality is retained throughout the
manifold.

The local attraction argument is sufficient: in affine normal and tangent
coordinates, continuity preserves a strictly positive normal Hessian near
the reference point. Taylor integration at a fixed tangent coordinate gives
both the quadratic bounds for the loss excess and the lower gradient bound.
The dissipation identity then gives exponential excess decay and the stated
finite-path estimate. Choosing an inner neighborhood with path allowance
less than its distance to the outer boundary closes the trapping argument.
The limiting point lies on (13). The constants and neighborhood may depend
on width and label scale, as the file explicitly permits.

## Reachability from zero readout and actual hidden motion

The symmetric subspace is invariant under the full canonical flow. Its
restricted metric is exactly `||delta p||^2+delta q^2+delta s^2`; in particular
the factors `W_ij=q/n` and the first/readout mobilities cancel the apparent
width factors. The reduced physical flow is therefore independent of width.

After `s=epsilon b`, the equations (17) are exact. Their `epsilon=0` limit
has the explicit solution (19). Choose the strongly convex ball and inner
sublevel for the fixed objective `ell` first, and then choose a finite time
at which this explicit solution is strictly inside that sublevel. Finite-time
continuous dependence supplies a positive `epsilon_0` independent of width.
For each fixed positive `epsilon<epsilon_0`, the sublevel barrier and strong
convexity prove convergence to the exact reduced minimum. This step does not
require any uniform-in-time comparison with the `epsilon=0` trajectory.

For each fixed width, the reference trajectory subsequently enters the full
attracting neighborhood. Its finite-time preimage on the slice `w(0)=0` is
nonempty and open. This supplies the required intersection with zero readout;
it is not inferred solely from openness of the positive-readout basin.

The added acceleration identities (22)--(23) also check. Differentiating
`dot p=-(2sq/m) sum R psi chi xbar` and its `q` counterpart at `s=0` leaves
only the derivative of `s`. Substitution of `dot s=epsilon k`,
`R=-epsilon(h-r)` and the zero residual moments gives
`ddot p=(2 epsilon^2 k/m)P` and `ddot q=(2 epsilon^2 k/m)Q`.
The displayed feature accelerations follow by the chain rule because all
initial hidden velocities vanish. For the paired data `P=(P_1,0)` with
`P_1>0`; hence every feature acceleration is strictly positive. These are
finitely many strict inequalities at each fixed width, so shrinking the open
initial neighborhood preserves them before taking the full-rank intersection.
No width-uniform neighborhood size or acceleration lower bound is implied.

## Full-rank starts, Gaussian probability and extensions

The distinct-absolute-projection argument in Section 5 proves independence
of the first-layer sample functions even when the input matrix has dependent
columns. Peeling the slowest exponential tail after removing the constant
limit proves every coefficient is zero. Thus a full-column-rank `U` is
realizable at every `n>=m`. Prescribing the first `m` rows of `WU` to equal a
nonzero diagonal matrix then gives a simultaneous full-rank realization for
both hidden feature matrices.

The product of the two Gram determinants is consequently a nonzero analytic
function. Its nonzero locus is open and dense, which suffices to intersect
the already constructed open bad basin. On that intersection the initial
loss derivative is strictly negative. Every limiting feature matrix is rank
one because the limit belongs to (13). The same full-rank realization permits
an interpolating readout, establishing nonglobality of the bad minima.

The explicitly stated Gaussian variances give a positive density everywhere
at each fixed width. Therefore the open initial set has positive probability.
The population Gram claims also hold: first-layer function independence gives
`Q^(1)>0`; a nondegenerate Gaussian on sample space and the coordinatewise
tanh map give `Q^(2)>0`.

For the extension to `m>18`, adding zero residual entries preserves all signed
moment identities. Extra Jacobian-square terms are nonnegative. The enlarged
vector `P` need not retain a zero second coordinate, but

\[
\bar x_a^\top P
=\sum_b h_b\psi_b\chi_b\,\bar x_a^\top\bar x_b>0
\]

because all coefficients and all pairwise inner products are positive.
Thus the revised extension correctly preserves the acceleration signs.

## Complementary geometry note

All factors in the tangent contribution, residual equation and loss equation
in `TANH_GEOMETRY.md` check. Its scalar Gram lower bound uses
`U^T U>=n kappa I`; it does not incorrectly commute the positive diagonal
matrices with the sample Gram. The readout lower bound following a strict
loss decrease uses bounded top features and needs no parameter bound. The
loss exponent is correctly `-4 b^2/m` times the indicated integral.

A finite limit of this continuous autonomous flow is stationary: otherwise
a projection onto its nonzero limiting velocity would have a derivative
bounded away from zero near the limit, contradicting convergence. The
stationarity argument therefore correctly forces lower-feature rank loss
at any finite non-fitting endpoint after a strict loss decrease.

The strict-saddle construction is valid under its stated assumptions
`rank(X)=m`, `n>=m` and nonzero readout. Its pure matrix direction leaves
predictions exactly fixed. In the mixed derivative the term differentiating
the top activation derivative vanishes because `v^T U=0`. The remaining
mixed Hessian entry is exactly (6), so the two-dimensional restriction has
negative determinant. The revised heading correctly restricts this claim to
nonzero-readout critical points. No saddle-avoidance conclusion for the
zero-readout initialization slice is being supplied.

## Limits of the checked result

- The construction is existential for specially chosen data and labels, with
  `m>=18`, `d=2` and `n>=m`; it does not address every dataset or label vector.
- Data and label scale are independent of width. Basin neighborhoods,
  capture times and Gaussian basin probabilities need not be.
- Positive failure probability separately at every finite width does not
  refute sufficiently-large-width high-probability fitting. Those probabilities
  may tend to zero.
- Non-fitting does not establish incompressibility, and no compression lower
  bound, typical failure mechanism or large-label threshold is proved.
- This reused-context audit is internal evidence only. It cannot replace
  the repository's fresh independent promotion reviews or user approval.
