# Isolated internal audit of compatible-collision interpolation

Date: 2026-09-18. Verdict: **PASS within the assigned scope.** This is an
internal mathematical audit, not a promotion review or a proof of geometric
protection along the canonical trajectory. No experiment was performed.

## Scope and frozen inputs

The assignment was to check Section 8, including Sections 8.1--8.4, of
`energy_geometry_route.md`: uniform bounded odd interpolation for at most
three sign-folded codes in a compact annulus separated from antipodal
collisions, the readout-norm identity, and the conditional logarithmic loss
bound. Scientific inputs read were exactly that section,
`docs/observable_p1.md` in full, and Section 3 of `initial_geometry.md` in
full. No other source sections, study README, other studies, history, or
review reports were read. The required `solve-math-rigorously` skill was
read. Full-file hashes below are metadata; they do not expand the scientific
reading scope.

SHA-256 identifiers at review and reconfirmed before writing this report:

- `energy_geometry_route.md`, full file:
  `8c386feeae81bd2bbcf5a201f5cb3ba2a44fed92b29be16fe583146f38f0a391`.
- Its assigned Section 8, from its level-two heading through end of file:
  `1eff706052f63a46fe6c809eb5f3c4da2c04a6cceb1823ba927706e100dc5c9c`.
- `docs/observable_p1.md`, full file:
  `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba`.
- `initial_geometry.md`, full file:
  `6856fb3d2cca5d59d1b00c4bd3cf87dd74f87315999e244b42dd1662647f091d`.
- Its assigned Section 3, including the trailing blank lines before Section 4:
  `c47a9f7b0223ad6b7c3f994dff842498b76a3614a0476897986d7ff9309a95e0`.

## Interpolation theorem

The theorem is correct as stated. Its constant is uniform over the full
allowed configuration set for fixed positive `r,R,delta`, fixed canonical
upper law, and code count at most three. It does not require a lower bound
on separation between equal-target sign-folded codes.

The supplied exact upper law has independent coordinates
`b_j=tanh(sqrt(v) Z_j)/sqrt(tau+eta)` in the active two-dimensional odd
sector, with `v>0` and `tau+eta>0`. Consequently its support is bounded, its
law is invariant under negation, and it has strictly positive density on
an open square containing zero. These are the three properties of the
law used in Section 8. Bounded marks give all the claimed uniform Banach
space derivative bounds for `F(x)(b)=tanh(b dot x)`. Positive density and
continuity turn an almost-sure linear relation into an identity on that
square. Every feature and every difference quotient used in the proof is
odd under mark negation.

Sign folding is exact: `F(y_i z_i)=y_i F(z_i)` for `y_i` equal to plus or
minus one. Thus the transformed target is one for every code, including
duplicates. The compact annulus excludes the identically zero feature;
the antipodal exclusion prevents inconsistent targets at opposite codes.

### Confluent independence

The four-function independence argument is valid. After division by the
strictly positive `sech^2(s)`, the relation becomes

`(A/2)sinh(2s) + b dot p - 2B(b dot v)^2 tanh(s) = 0`,

where `s=b dot x`. Restriction to `s=0` forces `p=lambda x`. If `v` has a
nonzero transverse component, varying the transverse coordinate at a fixed
small nonzero `s` forces `B=0`, after which the cubic and linear terms force
`A=lambda=0`. If `v=nu x`, the coefficients of orders one, three, and five
are exactly

`A+lambda=0`, `2A/3-2B nu^2=0`,
`2A/15+2B nu^2/3=0`.

They imply `16A/45=0` and then all coefficients vanish. This covers every
nonzero `x,v`, including radial derivative directions.

The double-cluster independence argument is also valid. An admissible line
direction `e` exists by excluding finitely many proper lines. Put
`ell=e dot x`, `h=e dot v`, `k=e dot z`, `X=ell^2`, `Y=k^2`.
The needed conditions are `ell h k != 0` and `X != Y`; the hypotheses
`x,z != 0`, `z != +/-x`, and `v != 0` give exactly these exclusions.
The displayed shift computation gives
`2Bh X^(n+1)(X-Y)=0`.
One can verify this step using only Taylor orders one, three, and five:
after cancellation of the coefficients `1,-1/3,2/15`, the three-column
coefficient matrix has determinant

`2 ell h k X (Y-X)^2`,

which is nonzero. No assertion about all higher tanh Taylor coefficients
is needed for the independence conclusion.

Pointwise independence does yield the asserted uniform Gram bound on each
compact admissible parameter set: the squared L2 norm is continuous jointly
in parameters and a coefficient vector on the unit sphere, and its minimum
cannot vanish. The source uses this argument on parameter sets satisfying
the strict independence hypotheses, not on their degenerate boundaries.

### Three-point collisions at unequal scales

The farthest-pair parametrization is valid. The two endpoint distance bounds
give `0<=a<=1` and `|b|<=1`. For three distinct points the denominator

`d=sqrt(h^2 b^2+h^4 a^2(1-a)^2/4)`

is strictly positive.

The divided third-feature estimate remains uniform even when `a` approaches
zero or one arbitrarily faster than `h`, and when the transverse displacement
approaches zero at an unrelated rate. More explicitly, with a common
constant `K` on the compact region, the transverse remainder satisfies

`||R_transverse||_infinity <= K h^2 |b|`,

because the whole transverse segment stays within `O(h)` of `x`. The
one-dimensional interpolation Green kernel is nonnegative and integrates
to `a(1-a)/2`, so the longitudinal remainder satisfies

`||R_segment||_infinity <= K h^3 a(1-a)`.

Since `d>=h|b|` and `d>=h^2 a(1-a)/2`, their sum divided by `d` is at most
`3K h`, with the zero terms omitted when appropriate. Thus the asserted
`O(h)` remainder contains no hidden lower bound on the smallest separation.
The sign of the second-derivative coefficient is correctly negative.

The limiting third function is
`alpha DF(x)[u]+beta D^2F(x)[v,v]`, with `alpha^2+beta^2=1`.
If `beta!=0`, independence from `F(x),DF(x)[v]` follows from the proved
four-function result. If `beta=0`, then `alpha!=0`, and the two independent
directions `u,v` give the same conclusion. The annulus, unit directions,
perpendicular choices, and unit coefficient circle form a compact parameter
set. The Gram lower bound is therefore uniform before taking `h` small.
The uniform L-infinity approximation transfers it to the actual divided
features and also uniformly bounds those features in L-infinity.

The transformed targets are exactly `(1,0,0)`: the numerator of the third
target is `1-(1-a)-a=0`. This exact cancellation is essential, and the proof
uses it correctly. If `G>=kappa I` and the target is `q`, the coefficient
vector `G^(-1)q` obeys `|G^(-1)q|<=|q|/kappa`, while the resulting readout
has squared L2 norm `q^T G^(-1)q<=|q|^2/kappa`. Uniform feature suprema then
bound its L-infinity norm. This justifies both requested norm bounds.

### Exhaustion of configurations

The compactness contradiction covers all allowed code counts and all
collision patterns. Any unbounded sequence of optimal interpolation costs
has a subsequence of fixed code count whose codes converge within the
annulus; the antipodal separation remains at least `delta` in the limit.
Distinct limiting codes have an invertible feature Gram by the supplied
ridge-independence proof. That proof depends only on nonzero codes distinct
up to sign, so it applies to these arbitrary upper codes as well as the
initial codes of its original formulation.

With exactly two merging codes and a distinct third limit, normalized
differences converge after taking a subsequence of their unit directions.
The three limiting features are the proved double-cluster family and have
target `(1,0,1)`. With all three limits equal, the preceding three-point
argument applies. Exact repeated codes can be removed; passing to a further
subsequence with a fixed equality pattern, if needed, leaves the single
feature or two-feature confluent cases. The same reasoning covers original
code counts one and two. These finitely many alternatives exhaust every
subsequence, contradicting unbounded interpolation costs. In particular,
there is no quantifier change from a configuration-dependent bound to a
uniform bound hidden in the conclusion.

## Readout norm and conditional loss consequence

For the stated unhalved loss, labels `y_i` of magnitude one, weights of total
mass one, zero initial readout, and the stated readout gradient equation,

`d||c||_2^2/dt = -4 sum_i mu_i (f_i-y_i) f_i`
`= 1 - 4 sum_i mu_i (f_i-y_i/2)^2 <= 1`.

Thus `||c(t)||_2^2<=t` is correct. This calculation requires no geometric
protection and uses the normalization and initialization provided by
`docs/observable_p1.md`.

At any current state admitting the interpolant,
`<dot c,c-c_*> = -2 L` is an exact algebraic identity. There is no time
derivative of `c_*`, so neither differentiability nor a coherent time-varying
selection of comparators is required. Cauchy--Schwarz and the uniform L2
bound yield

`||dot c||_2^2 >= 4 L^2/(||c||_2+C)^2`.

Under the gradient-flow dissipation identity used in the statement,
`dot L<=-||dot c||_2^2`. Consequently, if the same positive `r,R,delta` work
for the whole trajectory, then

`dot L <= -4L^2/(sqrt(t)+C)^2 <= -2L^2/(t+C^2)`.

The second inequality is justified by
`(sqrt(t)+C)^2<=2(t+C^2)`. Integrating the reciprocal of the positive loss
from `L(0)=1` gives exactly

`L(t)<=1/[1+2 log(1+t/C^2)]`.

If loss reaches zero at a finite time, dissipation keeps it zero and the
bound remains valid. The positive interpolation constant can always be
enlarged, so the displayed division by `C^2` causes no degeneracy.

## Objections and limits of the verdict

No blocking mathematical objection was found in the assigned theorem or its
conditional consequences. The only optional exposition improvement is to
use the three explicit Taylor orders above in the double-cluster proof;
this avoids an unnecessary implicit fact about all tanh Taylor coefficients.

The audit does **not** establish that the canonical trajectory remains in a
fixed compact annulus or stays uniformly separated from antipodal pairs.
Those hypotheses are exactly the unproved bridge acknowledged in Section
8.4. Nor does the audit independently establish existence and regularity of
the full canonical population flow outside the assigned inputs; the risk
consequence is conditional on its stated gradient-flow equations and
dissipation identity. The interpolation theorem alone is unconditional
over its specified geometric configuration class. No unconditional fitting
theorem or exponential decay claim follows from this section.
