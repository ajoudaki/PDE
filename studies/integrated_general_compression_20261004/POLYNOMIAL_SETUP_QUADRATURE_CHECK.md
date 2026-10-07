# Reconstruction audit of the quadrature candidate

2026-10-06. Scoped cross-route mathematical audit. This is not an independent
original discovery or a promotion review. The candidate was not edited.

**Verdict:** the quadrature, coefficient-error, exact-pairing, and operation-count
arguments check out on the original Harmonic construction domain. One statement
correction is required if Section 1 is to serve as a standalone lemma: make that
domain explicit. No substantive defect was found in the audited quadrature
proof. The result remains conditional on a certified source-value procedure;
it is not an efficient initialization algorithm by itself.

## Exact inputs and read coverage

Read the entire candidate, Sections 1--7, including every displayed formula:

- `POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md`, SHA-256
  `a41113722245f637b6128e1f16c28cb9ec3fee5635603dbca697a1734074cac2`.
- Cited relevant portions of `RESULT.md`, SHA-256
  `c2cbd1bb0e6a39de87181df89be977eaf2e272fda4f1459ac934396d84e1b278`.

The `RESULT.md` dependencies checked were the Harmonic source families,
analytic radii and domain, coefficient count/budget and cost statements;
the complete source-expansion and finite-initial-jet construction;
coordinate selection and exact source metric; the all-horizon source extension;
and the complete factored-jet, compiled-temporal-map, geometric-basis and
selection/assembly cost derivations. Previously read portions with this same
hash were reused. The probabilistic source event was treated as the candidate's
explicit inherited hypothesis, not independently reproved. No other scientific
source, another candidate, or another review was retrieved for this audit.

Applied the accessible rigorous-math and conjecture-audit instructions and the
already read canonical notation contract. The canonical-notation skill's
previously reported operating-system read restriction remains. No numerical
experiment was run. Checks below are algebraic reconstruction of the proof.

## Required statement correction

**D1 — Section 1, lines 22--23, equations (1), (4)--(6): state the permitted
horizon and tolerance explicitly.** The opening currently specifies merely a
finite horizon \(T\) and \(\eta>0\). The formulas need positive \(T\),
the asserted \(\alpha=r_t/(4T)\le1\), and a nonempty retained set.
In particular the imported cutoff is

\[
H(T,\eta)=2\log\frac{16M_nP_T}{\eta}.
\]

At any otherwise allowed \(T\), choosing
\(\eta>16M_nP_T\) makes the cutoff negative. Then \(\Lambda\) is
empty, \(N=0\), the maxima defining \(p,J\) do not exist, and
\(\epsilon_c=\eta/(16N\mathcal Y_J)\) is undefined. An unrestricted
finite \(T\) also permits \(T=0\), where (1) divides by zero.

The smallest repair is to state the original analytic construction conditions
\(T\ge T_0>0\), \(0<\eta\le\eta_0=\min(1,Y,S)\), together with
the original positive-label and width/source gates. This preserves every
intended application and all subsequent formulas. Alternatively supply explicit
loose-tolerance and zero-horizon branches. Section 7's later phrase “permitted
\(T,\eta\)” suggests the intended inherited restriction, but should not
be relied on to repair the formal opening retroactively.

This is a domain-specification defect, not a failure of the exponential
quadrature estimate on the intended domain.

## Reconstruction checks

### Positivity and exactness

For the polar rule, the discrete cosine orthogonality at
\(\omega_r=(2r+1)\pi/(2M)\) gives the displayed degree-\(M-1\)
interpolant. Integrating each Chebyshev mode gives (18), including the even
and odd cases. The lower bound

\[
w_r\ge \frac1M\left(1-2\sum_{k=1}^{\lfloor(M-1)/2\rfloor}
                      \frac1{4k^2-1}\right)>0
\]

follows from the stated telescoping sum. The empty sums at \(M=1,2\)
cause no exception. Exactness for the constant establishes total weight one;
exactness through degree \(M-1\) establishes the polynomial cancellation
needed in (20). No Gaussian-quadrature theorem is being assumed.

The Chebyshev tail bound is
\(2Be^{-M\sigma}/(1-e^{-\sigma})\). Subtracting the polynomial from
both operators multiplies this by at most two, giving precisely (20).
The periodic rule's aliasing sum gives \(2B/(e^{bN}-1)\), as in (17).

The weights including the sphere Jacobian need not integrate constants
*exactly* on the sphere. The proof correctly uses unit mass and contraction
only for the bare product rules, puts the Jacobian inside the analytic
integrand, and uses its real bound \(A_d\) for nodal perturbations.
Thus that possible objection does not invalidate the argument.

### Joint analytic domain

The polar Jacobian has exponents \(d-1-i\), whose sum is
\((d-2)(d-1)/2\), matching (10)--(12). A complex coordinate-plane
rotation preserves the algebraic quadric and increases the hyperbolic radius
by at most its imaginary angle magnitude. Summing the \(d-1\) angle
increments puts the image in \(\mathcal Q_{r_q/2}\). The Bernstein
ellipses may overshoot the real polar interval; this is harmless because the
rotation argument is valid for every real part of every angle.

A homogeneous degree-\(\ell\) harmonic composed with these angles has
frequency at most \(\ell\) in each separate variable. Applying the
one-variable Laurent-polynomial argument successively therefore gives (15)
without an omitted dimension factor. Multiplying the source, cosine,
harmonic and Jacobian bounds yields exactly (16).

### Sum of errors and matrix pairing

For the temporal order in (22),
\(2B_{\rm int}/(e^{aN_t}-1)\le\epsilon_c/(2d)\); the same calculation
applies to azimuth. Each of the \(d-2\) polar contributions is bounded by
\(\epsilon_c/(2d)\) because of the factor \(8d\) in its order formula.
There are exactly \(d\) univariate variables, so (21) sums to at most
\(\epsilon_c/2\).

The cosine normalization \(\gamma_k\le2\) is already inside
\(B_{\rm int}\). The nodal contribution is independently bounded by
\(2A_d\mathcal Y_J\delta_{\rm node}=\epsilon_c/2\). Reconstruction
then costs \(N\mathcal Y_J\epsilon_c=\eta/16\); adding the original
tail gives \(\eta/8\). No additional factor two is missing.

The candidate correctly distinguishes separate accuracy from exact paired
provenance. Its hypothesis \(\widetilde{Ag}=A\widetilde g\), together
with identical scalar quadrature and mode restrictions, gives coefficient
pairing by finite-sum linearity. The original finite initial-jet backend
satisfies that hypothesis and can make every member separately accurate.
No invalid \(\ell_\infty\)-to-operator-norm conversion is used.

The retained source generators remain coefficient vectors. Consequently the
count \(2m+d+1+4N\), or \(2m+d+1+8N_1\) in dimension one, is
unchanged. The candidate also correctly declines to preserve accidental
rank deficiencies under perturbation. The separate two-point treatment at
\(d=1\) and the circle treatment at \(d=2\) have the right normalizations
and error allocations.

### Cost and asymptotic exponents

Direct Fejér-weight construction costs \(O(N_\theta^2)\). Cached sine
powers cost \(O(dN_\theta)\) work and storage; enumerating tensor nodes
and their sphere coordinates costs \(O(dN_x)\). These agree with (30).
The imported separated harmonic recurrences give (31).

Streaming temporal accumulation followed by spatial projection costs
\(O(LnN_x(p+1)(N_t+H))\). Its temporal buffer fits inside \(LnR\)
because the retained degree-zero spherical modes alone give \(N\ge p+1\).
The analogous dimension-one inequality also holds. The unchanged rank-aware
orthogonalization, selection and assembly costs are correctly carried into
(33). Nodal image actions and streaming-induced recomputation are explicitly
charged to \(\mathcal T_{\rm val}\), rather than treated as free.

For fixed dimension and the stated regime, write \(\ell_n=\log(en)\).
Then \(\alpha^{-1}=O(\ell_n^{3/2})\), the joint cutoff is
\(O(\ell_n)\), and the simplex count gives

\[
N=O\!\left(\ell_n^d\ell_n^{3/2}
                       \ell_n^{(d-1)/2}\right)
 =O(\ell_n^{3d/2+1}).
\]

The integrand growth contributes only \(O(\ell_n)\) to its logarithm.
The polar denominator contributes an additional \(O_d(\log\ell_n)\),
which does not change the leading power. Thus
\(N_t=O_d(\ell_n^{5/2})\),
\(N_x=O_d(\ell_n^{3(d-1)/2})\), and
\(N_tN_x=O_d(\ell_n^{3d/2+1})\), including the separate dimension-one
case. The candidate correctly restricts these powers to fixed dimension and
polynomial target accuracy; it does not claim them at arbitrary growing
supplied budget or arbitrary horizon.

## Remaining scope boundary

The unbounded source-value costs \(\mathcal T_{\rm val}\) and
\(\mathcal M_{\rm val}\) are the decisive unresolved bridge to efficient
setup. The candidate states this clearly and does not substitute an oracle
for initialization-only recovery. Numerical rank stability, finite-precision
pairing and activation-evaluation bit complexity are explicitly outside the
lemma. None of those omissions invalidates its stated exact-real quadrature
result, but none is resolved by the polylogarithmic number of nodes.

After D1 is clarified, this audit finds no further must-fix mathematical defect
in the scoped candidate. This verdict does not validate an efficient
initialization algorithm, the complete inherited probabilistic source proof,
or a promotion package.

## Revised-input verification addendum

2026-10-06. The revised candidate has SHA-256
`2d58da5a418f6d5a8f1bb54ce343b205978770424c0940789b15231e251daf42`.
The inherited `RESULT.md` input is unchanged. The original audit above is
retained as the record for its original input hash.

Read the revised opening and all of Section 7. The opening now explicitly
requires

\[
T\ge T_0=32(m/\gamma)\log(en),\qquad
0<\eta\le\eta_0=\min(1,Y,16Ym/\gamma),
\]

and states that the retained set is nonempty. These are precisely the original
Harmonic analytic-construction conditions. They make \(T\) strictly positive
and keep the imported cutoff positive under the original source gates, so
\(p,J,N\) and \(\epsilon_c\) are defined. **D1 is resolved.**

Every occurrence of the local abbreviation \(\ell_n\) in Section 7 has
been replaced by its defining expression \(\log(en)\). Rechecking the
displayed powers and logarithms confirms that these are notation-only changes;
the complexity exponents and their scope are unchanged.

For exact change verification, a read-only Node script reversed the two declared
edits in memory and computed the resulting SHA-256. It reproduced the original
audited candidate hash exactly:
`a41113722245f637b6128e1f16c28cb9ec3fee5635603dbca697a1734074cac2`.
The comparison returned `exact_two_edit_reversal_matches: true`. This verifies
that the remainder of the current candidate is byte-for-byte the material
already audited; no candidate file was written by the check.

**Updated verdict:** no outstanding must-fix defect was found in this scoped
exact-arithmetic quadrature lemma at the revised hash. The source-value recovery
and full efficient-initializer limitations remain exactly as recorded above.
