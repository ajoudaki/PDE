# Internal reconstruction of the four structural claims

Reviewed source: `STRUCTURAL_CHECKS.md`, complete frozen file.

SHA256:
`a47060168a45c6cdf9434c7b44303d9e4de9c1f65c12120b48dea54a0f666854`

Date: 2026-10-05. This check read no other route. The source was not changed.
The rigorous-math and conjecture-investigation instructions were reused;
the custom notation skill remains inaccessible. This is an internal check,
not an independent promotion review.

Overall finding: all four claims pass at their stated elementary scope.
The author incorporated the covering edge cases and the product-law
measurability hypothesis after the first check; this report was then rebound
to the complete revised source and hash above. Claim 4 needs no loss in its
probability threshold. No result here resolves autonomous neural compression
or gives a general decoder-size lower bound.

## 1. Exact dimension of polynomial restrictions

**PASS.** Write `P_k` for the polynomials in `d` variables of total degree at
most `k`, and `q(x)=sum_j x_j^2-d`. Division in the last variable is legitimate
over the coefficient ring `R[x_1,...,x_(d-1)]`, because `q` is monic in that
variable. At each division step the removed quotient term has total degree
at most `k-2`; its product with `q` has total degree at most `k`. Thus the
source's degree bookkeeping is valid.

The remainder has the form `A(x') x_d+B(x')`. If it vanishes on the sphere,
evaluate at `x_d=+sqrt(d-||x'||_2^2)` and its negative, for every
`||x'||_2<sqrt(d)`. The square root is strictly positive there, so subtraction
gives `A(x')=0`, and addition gives `B(x')=0`. A polynomial that vanishes on
an open set is zero: restrict successively to open coordinate intervals and
use that a nonzero univariate polynomial has finitely many roots. Hence
the restriction kernel is exactly `q P_(k-2)`.

Multiplication by nonzero `q` is injective in the polynomial ring. Therefore

\[
 \dim(P_k|_{S^{d-1}_{\sqrt d}})
 =\binom{d+k}{d}-\binom{d+k-2}{d}
 =\binom{d+k-1}{d-1}+\binom{d+k-2}{d-1}.
\]

The last identity follows by applying Pascal's identity to the two
successive differences. For fixed `d>=2`, its leading term is
`2 k^(d-1)/(d-1)!`, so the stated `Theta_d(k^(d-1))` is correct. In particular,
for `d=2` the exact answer is `2k+1`. At degrees zero and one the dimensions
are respectively `1` and `d+1`, as stated. No assertion for joint growing
`d,k` is justified by this fixed-dimensional asymptotic.

The interpretation is also correct: this is the dimension of a linear space
and the size of its unrestricted full coefficient table. It cannot be a
lower bound for every implicit nonlinear representation. The supplied sine
example demonstrates that distinction and is not offered as a neural-flow
construction.

## 2. Stabilizer and the role of full input rank

**PASS.** Let `V` be the span of the training inputs and let `dim V=r`.
An orthogonal transformation fixing all those inputs fixes every linear
combination, hence is the identity on `V`. It preserves `V^perp` and may be
any orthogonal map on that complement. For sphere points `x=v+u` and
`x'=v'+u'`, being in one stabilizer orbit requires `v=v'`. Conversely,
`v=v'` forces `||u||_2=||u'||_2` from the common sphere radius, and an
orthogonal transformation of the complement maps `u` to `u'`. This includes
zero perpendicular components, `r=0`, and `r=d`.

Thus any invariant predictor factors through the `r` projected coordinates.
For `r=d` the stabilizer is the identity, and its orbits are singletons. The
source correctly distinguishes the rank assumption from `m>=d`.

For a stabilizer element `R`, replacing the first matrix by `A R^T` and the
query by `R x` leaves `A x/sqrt(d)` unchanged. The parameter transformation
is orthogonal in the first matrix's Frobenius coordinates and commutes with
the stated scalar block mobility. The transformed loss agrees with the
original loss because `R x_a=x_a`. The chain rule therefore transforms the
gradient field equivariantly; uniqueness gives the same relation for the
flow on its existence interval. Right-orthogonal invariance of the Gaussian
first matrix then gives predictor-law invariance. It does not give
invariance of each realized predictor. A deterministic limit in a topology
identifying the stated query observables inherits the symmetry.

## 3. Covering a finite-parameter Lipschitz image

**PASS, with the now explicit accuracy and singleton conventions.** For `A>0`,
choose a coordinate grid with spacing at most `epsilon/A`. It has no more
than `ceil(2RA/epsilon)+1 <= 2+2RA/epsilon` points per coordinate, and the
nearest grid point is within `epsilon/A` in maximum norm. Applying the
`A`-Lipschitz map gives the displayed covering count and its logarithm.
If `A=0`, the image is a singleton; avoid the written division by `A` and
use a one-point cover. The cases `R=0` and `p=0` are also singletons.

The conditional neural application may have a parameter domain that is a
subset of the cube, because the data must remain normalized and uniformly
gapped. No Lipschitz extension theorem is needed: partition the cube into
cells of maximum-norm diameter at most `epsilon/A`, retain one admissible
representative per occupied cell, and apply the same count. The bound by
`m(d+1)` ambient data-and-label coordinates is an upper bound and does not
claim those coordinates are independent.

The source correctly leaves all-time Lipschitz dependence unproved and
distinguishes a covering-number upper bound from a computable autonomous
evaluator. Its warning about the direction of analytic-class inclusion is
valid.

## 4. Averaging centers and pairwise variability

**PASS under the source's explicit product-measurability convention.** Let `mu` be the
trajectory law and assume that

\[
 (f,g)\longmapsto\mathbf 1_{\{\|f-g\|\le\epsilon\}}
\]

is measurable for `mu tensor mu`, with measurable sections, so that Tonelli's
theorem applies. Independence then gives, for
`h(g)=mu({f:||f-g||<=epsilon})`,

\[
 \int h(g)\,d\mu(g)
 =\mathbb P(\|F-F'\|\le\epsilon)\ge1-\delta.
\]

For `0<=delta<1`, put `c=1-delta>0`. If `h<c` almost surely, the nonnegative
random variable `c-h` is strictly positive almost surely. Some set
`{c-h>=1/j}` must have positive measure, since their union is `{c-h>0}`;
therefore `int(c-h) dmu>0`, contradicting `int h dmu>=c`. Consequently the
set `{g:h(g)>=c}` has positive measure. In particular a center can be chosen
inside any prescribed full-measure set of valid trajectories. There is no
need to replace the probability threshold by `1-delta-eta`. At `delta=0`,
`h=1` almost surely; at `delta=1`, every center satisfies the asserted
nonnegative lower bound. The natural accuracy convention is `epsilon>=0`.

The revised source explicitly includes the product-distance measurability
needed above. This is a substantive clarification: in an arbitrary
nonseparable metric trajectory space, Borel measurability of the individual
random elements does not by itself exhibit the product-measurability step;
continuity of distance on the product topology is not a substitute for
measurability with respect to the product sigma-algebra. No Banach-valued
expectation or regular conditional-law theorem is needed once the displayed
indicator is product measurable.

For the intended continuous neural trajectories, this condition has an
elementary sufficient justification. The domain consisting of all finite
physical times and sphere queries has a countable dense subset. For two
continuous bounded trajectories the supremum of their difference equals
the supremum over that subset. Hence their supremum distance is a countable
supremum of measurable differences of evaluation maps, and the required
indicator is product measurable. Separably supported norm laws are another
sufficient setting. The revised source names these settings and directly
assumes product measurability.

The claimed interpretation passes: an existence center may itself require
the full dense trajectory for storage or generation. Pairwise concentration
alone yields neither a compact center nor a lower bound forcing one to
retain each realization's initialization randomness.

## Revision disposition

The first checked version had hash
`e64aebe7865f6c2a357bfcbf78f26fc246679812aa10bd3746407349b6eadcd6`.
Its two requested clarifications are present in the final reviewed source:
positive accuracy and the singleton image cases in claim 3, and explicit
product-distance measurability in claim 4. I reread the complete revised
source before assigning the intermediate hash
`380092010da677493ac92b7b96ebcab7fc2e7dd3979d3d634baeb185dc10f4cb`.

No incorrect sphere dimension, symmetry claim, covering constant, or
averaging threshold was found. The measurability clarification closes the
only nontrivial scope qualification identified. The source hash above identifies the
version checked; any subsequent source correction requires its own version
record rather than silently transferring this check.

### Title-only recheck

The title was subsequently changed from “Three distinctions” to “Four
distinctions”. The resulting source hash is the current reviewed hash at
the top of this report. Replacing only `Four` by `Three` in its first line
reproduces the intermediate hash `380092010da677493ac92b7b96ebcab7fc2e7dd3979d3d634baeb185dc10f4cb`,
confirming that no mathematical text changed. The mathematical PASS
therefore applies unchanged to current hash
`a47060168a45c6cdf9434c7b44303d9e4de9c1f65c12120b48dea54a0f666854`.
