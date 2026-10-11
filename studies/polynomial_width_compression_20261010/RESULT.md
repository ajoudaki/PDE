# Polynomial width gates: repairs and a Harmonic obstruction

This is a study result, not a paper change or promoted theorem. The paper
and book remain untouched.

The requested affirmative all-three strengthening is **not** established.
There are positive Legendre and Taylor repair routes, and a proved
obstruction to the joint polynomial-in-dimension Harmonic upgrade. The
fixed-dimension Harmonic sample/gap question remains open; it must not be
confused with that obstruction.

## Positive repairs and their exact scope

Keep the compact paper's Gaussian initialization, zero readout, physical
gradient flow, analytic activations with unbounded values allowed, arbitrary
fixed hidden depth, arbitrary sphere training inputs, positive feature-Gram
gap, and existing label condition
\(0<Y\le(\gamma/m)\beta^{-30L}\). No restriction \(m\ge d\) is added.
Errors use the complete training trajectory, including the fitted limit:
the whole sphere for Legendre, and the declared training/passive panel for
Taylor. Passive labels are never supplied.

The positive routes give this quantitative form. For any
\(0<\delta,\varepsilon<1\), a sufficient width for compressed-to-dense
error at most \(\varepsilon\) times the actual independent dense-run
discrepancy, with probability at least \(1-\delta\), is bounded by

\[
\left[C\beta^L\left(1+m+d+p+\gamma^{-1}+Y^{-1}
                    +\delta^{-1}+\varepsilon^{-1}\right)\right]^C,
\]

for an absolute fixed finite \(C\). Here \(p\) is the passive-panel count;
for Legendre take \(p=0\) and omit \(Y^{-1}\). The Taylor inverse-label
gate only simplifies its exact degree to a multiple of \(\log(en)\); it
is not a new small-label condition or a probability-event requirement.
These are enormous sufficient powers, not practical thresholds. The route
files give the explicit constants, separated gates and probability budgets.
Confidence applies at each individual width, not simultaneously over all
widths. No dense upper certificate substitutes for the actual discrepancy.

### Legendre

The original closure and optimizer are unchanged, with current order

\[
q=\left\lceil(m/\gamma)^3n^{1/4}[\log(en)]^2
                          e^{\sqrt{\log(en)}/2}\right\rceil.
\]

Its exact moving inventory remains
\(n(d+1)+1+2(L-1)mnq\), giving the same headline

\[
\beta^{CL}m(m/\gamma)^3n^{5/4}[\log(en)]^2
                          e^{\sqrt{\log(en)}/2}.
\]

Initialized dense hidden mixers remain additional fixed storage. The new
argument subtracts the integrated physical defect from the forward history.
Its second residual-clock derivative has a bounded weighted Legendre norm;
the weight cancels the apparent endpoint singularity. The forward tail
costs \(q^{-2}\), the backward tail \(q^{-1}\), and the exact growing-
projection identity makes their product \(q^{-3}\). That extra order pays
the stability and comparison factors at a polynomial onset.

Proof: [DENSE_LEGENDRE_ROUTE.md](DENSE_LEGENDRE_ROUTE.md).
The finite source is reconstructed, its random-prefix mesh completed, and
its unnecessary \(m\ge d\) restriction removed in
[SOURCE_SCOPE_CHECK.md](SOURCE_SCOPE_CHECK.md).
[LEGENDRE_REVIEW.md](LEGENDRE_REVIEW.md), including its final addendum,
accepts the assembled polynomial-width conclusion. It does not claim a
second complete independent audit of all inherited source files.

### Taylor

The absolute error remains \(Y/n\), and total retained real coordinates
remain bounded by

\[
\beta^{CL}(m+p)^2\left[
 \left(\frac{Ym}{\gamma}\right)^4[\log(en)]^3
 +\left(\frac m\gamma\right)^2[\log(en)]^2
                   [\log(e+\log(en))]^2\right]
 +\beta^{CL}(m+p)d.
\]

A capped initial analytic radius removes the nonpolynomial radius gates.
Its extra panel count is paid by the second term already present above.
Fixed-order common-cavity moments keep confidence out of the state
coefficient. A deterministic mesh of domain levels supplies Gaussian tests
before the full-network-dependent stopping level is selected. This changes
only a proof mesh, not the runtime state or its logarithmic powers.
Coefficients still use initialization jets; no dense training trajectory
is provided as extra information. No new efficient-setup claim is made.

Proof: [TAYLOR_ROUTE.md](TAYLOR_ROUTE.md), with its deficient endpoint
paragraph replaced by [TAYLOR_PREFIX_REPAIR.md](TAYLOR_PREFIX_REPAIR.md).
The original frozen route without this replacement is conditional;
[TAYLOR_REVIEW.md](TAYLOR_REVIEW.md) records the gap and the final assembly
status. The completion's separate fresh check is
[PREFIX_COMPLETION_REVIEW.md](PREFIX_COMPLETION_REVIEW.md).

### Quantitative lower bridge, with a weaker coefficient

The finite scalar argument in
[FINITE_ANTI_CONCENTRATION.md](FINITE_ANTI_CONCENTRATION.md) replaces an
unquantified CLT. Section 2 of the Legendre route verifies its conditional
variance and moment premises and converts the derivative to an actual
positive-time prediction witness, with polynomial qualifying width.

Its lower coefficient has polynomial sample/gap losses, sufficient for the
relative-error claims above. This does **not** establish polynomial onset
for the paper's stronger coefficient
\(c_{\phi,L,\delta}Y\sqrt\gamma\). That original lower-bound statement
remains eventual. Nor is this an endpoint lower bound. The scalar lemma
alone, without those moment and trajectory arguments, is not the complete
dense-variability theorem.

For clarity, the Taylor comparison uses the same event directly. If its
coefficient in the Legendre route is denoted locally by \(a_\delta>0\),
then on the absolute-accuracy and dense-lower events the ratio is at most
\(a_\delta^{-1}[\log(en)]^{5/2}/\sqrt n\). The elementary bound
\([\log(en)]^{5/2}\le64n^{1/4}\), valid for \(n\ge1\), makes
\(n\ge[64/(a_\delta\varepsilon)]^4\) sufficient. Split the requested
failure risk between the Taylor and dense-lower events; a union bound
needs no independence. Since \(a_\delta^{-1}\) is polynomial in the
displayed parameters up to its explicitly defined logarithmic confidence
order, this is a polynomial relative-accuracy gate, not an unquantified
eventual comparison.

## The requested joint strengthening meets a construction-specific obstruction

There cannot be a qualifying width polynomial in input dimension for the
**current Harmonic source construction with its unchanged headline storage
bound**. The obstruction is at initialization. It does not depend on the
complex-time proof, on the dense lower-bound certificate, or on an upper
bound being confused with actual dense variability.

The complete elementary proof is in [HARMONIC_ROUTE.md](HARMONIC_ROUTE.md).
Its finite probability bound and precise source-to-runtime interfaces
passed two fresh independent checks:
[HARMONIC_REVIEW_A.md](HARMONIC_REVIEW_A.md) and
[HARMONIC_REVIEW_B.md](HARMONIC_REVIEW_B.md).

Here is the contradiction in the paper's notation. Fix two correlated
training inputs, two hidden layers, the admissible unbounded activation
\(\phi(z)=z+\cos z\), a positive feature-Gram gap \(\gamma\), and fixed
positive labels obeying the paper's existing small-label cap. For every
fixed exponent \(a>1\), take \(n=\lceil d^a\rceil\). With probability
tending to one as \(d\) grows, every linear neuron space approximating
the initialized first-layer responses uniformly on the sphere to the
current required coordinate error \(1/n\) has dimension exactly \(n\).
The current exact-metric selection must then retain every first-layer
coordinate. Its explicitly stored first matrix alone requires \(nd\)
real coordinates.

But for these same admissible instances, the proposed unchanged headline

\[
C(m+d)^2+\left(\frac Cd\right)^{d+1}
 \left(\frac{Ym}{\gamma}\right)^4[\log(en)]^{3d+2}
\]

is only \(O(d^2)\). Indeed its second term tends to zero along
\(n=\lceil d^a\rceil\), whereas \(nd/d^2\to\infty\).
Choosing \(a\) larger than any proposed polynomial threshold exponent
rules out every such threshold. Width is still the largest growing scale.

This is not caused by requesting unnecessarily tiny error. The corollary
in [HARMONIC_TOLERANCE_COROLLARY.md](HARMONIC_TOLERANCE_COROLLARY.md)
extends the obstruction to **every vanishing coordinate-source tolerance**:
the required rank is \(n(1-o(1))\), still forcing at least \(nd/2\)
explicit first-matrix storage. It passed a separate fresh check in
[HARMONIC_TOLERANCE_REVIEW.md](HARMONIC_TOLERANCE_REVIEW.md).

The proof also gives a version with \(m=d\), orthogonal training inputs,
fixed \(\gamma\), and \(Y=\gamma\beta^{-60}/(2m)\). In that version,
all of \(d,m/\gamma,1/Y\) are polynomial in \(m\), but the same
contradiction holds. The two-input version is stronger regarding labels:
it keeps \(Y\) fixed throughout.

### What is and is not ruled out

This refutes the polynomial-width upgrade for the current **uniform source
approximation plus exact-metric coordinate selection** construction.
It does not refute the paper's existing fixed-problem, sufficiently-large-
width theorem. Nor is it an output-only lower bound for every possible
compressor, or a lower bound for the same runtime initialized using an
alternative source criterion. Removing the source criterion, changing the
finite-parameter storage envelope, or restricting dimension would be a
different theorem or construction, not removal of an unnecessary gate in
the present proof.

It does not prove an unavoidable exponential dependence on sample count
or inverse gap when dimension is held fixed. That question remains open.
The current global Chebyshev--Harmonic radius proof has a superpolynomial
gate there, and the simple radius cap introduces another storage term
whose absorption recreates such a gate. This is a failed repair of an
upper-bound proof, not a fixed-dimension lower bound; see
[HARMONIC_FIXED_DIMENSION_SCOPE.md](HARMONIC_FIXED_DIMENSION_SCOPE.md).

The earlier finite-training-source polynomial-width results are therefore
not in conflict with this example: they do not assert this uniform
whole-sphere source compression and dimension-dependent storage bound.

## Frozen source versions and checks

The Harmonic obstruction was frozen for review at SHA-256
`d19953be9d8182b493bd5677df5f375fb9f005d3a303ecdf769ca6151a56df8d`.
The scalar lemma's post-review edits make conditional independence and
centering explicit, as requested by its two reviewers. The tolerance
corollary's post-review edits clarify convergence in probability and its
example output target. Neither changes a mathematical bound.

The Taylor audit found the missing uniform-prefix event; its new completion
supplies it. A fresh completion audit also requested payment for the loose
control-net amplitude envelope; the final repair explicitly pays it within
the unchanged polynomial width. Frozen review versions and their exact
claim boundaries remain in the respective review reports. No all-three
positive repair or promotion is claimed.

Current paper files checked against these interfaces:

| File | SHA-256 |
|---|---|
| `paper/compact.tex` | `460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe` |
| `paper/compact_foundations.tex` | `6a49f8e35bb637416b7e330f7ace06286e482c942302bf57a46c8253a4cffbf0` |
| `paper/compact_selected.tex` | `3add2b694f38a4d7dbce90e51dafd375a7e8dee2e06d26b2d5af451bddb44885` |
| `paper/compact_legendre.tex` | `862aa37139ad9af67ac04b52949f838031e91077021b2da9060244d36ab4e0f9` |

No empirical claims or experimental runs are involved. No generated data,
commit, shared-index modification, or paper/book edit is part of this study.
