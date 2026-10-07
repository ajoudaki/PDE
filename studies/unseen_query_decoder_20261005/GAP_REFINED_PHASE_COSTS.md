# Smaller gap powers in the complete compact-decoder costs

2026-10-06. Internally checked lead-author assembly. The bounded
[physical-source reconstruction](GAP_SOURCE_CHECK.md) and
[finite/passive/resource reconstruction](GAP_TRANSPORT_CHECK.md) both
pass, conditional on their explicitly listed inherited interfaces. This
supersedes the larger sample/gap powers in EXPLICIT_PHASE_COSTS.md.
No experiment or promotion. The checked assembly had SHA-256
`08a5b55cb293f4daf6048ee35b7a0ea81b867ce0daab68104b2ee0936e24443c`;
subsequent edits change status, links and provenance, not formulas.

## Setup

The parameters are dense width \(n\), training count \(m\), input
dimension \(d\), fixed depth \(L\ge2\), positive population feature-Gram
gap \(\gamma\), label RMS \(Y=\|y\|_2/\sqrt m\), and failure
probability \(\delta\). The \(m\ge d\) training inputs span
\(\mathbb R^d\) and lie on its radius-\(\sqrt d\) sphere. Keep
the original Gaussian initialization, zero readout, mean squared loss,
mobilities \((n,1,\ldots,1,n)\), and nonlinear learning in every layer.
Keep the full inherited source/fitting/compact label intersection, not only
its consequence \(16Ym/\gamma\le1\). Zero labels give the separate
exact zero predictor.

For the common strip width \(a\) and layer activations \(\phi_j\), put

\[
 \beta=\max\left\{10,1+\max_{j\le L}|\phi_j(0)|,16/a,
 \max_{j\le L,\,k=1,2}\sup_{|\operatorname{Im}z|\le a/2}
 |\phi_j^{(k)}(z)|\right\},
\]
\[
 Z=\log(en)+\log\!\left(e+
 \frac{(m+d+2)\beta^{100L}(1+m/\gamma)}{\delta}\right).
 \tag{1}
\]

Activation values may be unbounded. The error target remains the inherited
independent-dense-pair upper-certificate scale, uniformly over all sphere
inputs and the entire physical training trajectory including the fitted
endpoint. Unseen query inputs and no test labels are permitted. Queries
use present state and do not replay scalar training. Initialization may
inspect the completed independent virtual source; it is not strictly online.

## Model size and three-phase table

Units are internal bits and bit operations. Suppressed factors are
universal. Tanh activation arithmetic is included. General activation
evaluators and all input/certificate interfaces are explicitly charged
below, not hidden constants.

Retained internal model size, also bounding peak training/query bits:

\[
 O\!\left(\beta^{530L}(m+d+2)^2(1+m/\gamma)^2Z^6\right).
 \tag{2}
\]

| Phase | Time | Peak memory, including the model |
|---|---|---|
| Initialization — generate the virtual source and construct the model | \(n\beta^{1340L}(m+d+2)^5(1+m/\gamma)^5Z^{31/2}\) | \(\beta^{730L}[n(m+d+2)(1+m/\gamma)Z^{7/2}+(m+d+2)^3(1+m/\gamma)^3Z^{17/2}]\) |
| Training — complete all compact updates, excluding queries | \(\beta^{1230L}(m+d+2)^5(1+m/\gamma)^5Z^{29/2}\) | \(\beta^{530L}(m+d+2)^2(1+m/\gamma)^2Z^6\) |
| Querying — predict at one unseen input from the current state | \(n\beta^{450L}(d+1)Z^4+\beta^{1030L}(m+d+2)^4(1+m/\gamma)^4Z^{12}\) | \(\beta^{530L}(m+d+2)^2(1+m/\gamma)^2Z^6\) |

Training counts the entire finite schedule and frozen tail, not one
vector-field evaluation. Query sampling, Gaussian generation, random seeds,
activation interpolation, matrix-function iterations, median sorting and
their scratch are counted. Initialization still uses a noncompact temporary
field table. Multiple queries pay the sum of their individual times.

The corresponding numerical-word count is

\[
 O\!\left(\beta^{410L}(m+d+2)^2(1+m/\gamma)^2Z^5\right),
 \tag{3}
\]

with up to \(C\beta^{110L}Z\) bits per word. Thus the full bit-memory
power is six, not five or four. Fixed retained bitstrings are counted.

## 1. Required sharper physical source interface

The physical proof is [GAP_DEGREE_REFINEMENT.md](GAP_DEGREE_REFINEMENT.md).
Its independent initial derivation is
[ONE_SIDED_INDEPENDENT.md](ONE_SIDED_INDEPENDENT.md).
The bounded source reconstruction checks the complete interface below,
including the noisy tube argument and the work/cache counts; the separate
transport reconstruction checks its use in the full resource table.

In the Euclidean physical coordinates
\((A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)\), the vector field
is the negative gradient of mean squared loss. Its real Jacobian splits
into a negative-semidefinite output-gradient Gram and a residual-weighted
sum of output Hessians. The latter is controlled throughout the original
thin real parameter tube. Residual decay and \(Ym/\gamma\le1/16\)
remove the algebraic inverse-gap factor from the integral of the real
one-sided expansion bound.

This cancellation is not used on complex times. The original short
complex patches remain, and provide Cauchy estimates and nearby analytic
flows locally. Only the global real propagation between patches changes.
The precise required interface is

\[
 \begin{split}
 H&\le C\beta^{100L}(1+m/\gamma)Z\sqrt{\log(en)},\\
 K+\log(1/\epsilon_{\rm pair})+\log(1/\sigma)
       +\text{local arithmetic/activation bits}
   &\le C\beta^{100L}Z,\\
 R&\le C\{d+mL\beta^{200L}(1+m/\gamma)Z^2
                          \sqrt{\log(en)}\}.
 \end{split}                                             \tag{4}
\]

Here \(H,K,R\) are local proof symbols for patch count, Taylor degree,
and actual named-field count. The remaining two local symbols denote the
physical current-operand pair tolerance and initialized-answer noise scale.
The source remains causal with the same law and coefficient conventions;
the normalized whole-sphere parameter/prediction error remains \(n^{-10}\).
The original \(K\le CH\) and row-program work/scratch interfaces must
also remain valid. An error bound only on the exact trajectory, or only
for deterministic Taylor truncation, is insufficient for (4).

## 2. Transport through the finite source and passive decoder

Assume the complete interface (4), including its local-forcing and tube
statements. Every occurrence of the old source numerical certificate in
FAST_FINITE_SOURCE_BRIDGE.md can then use
\(\chi=\beta^{100L}Z\). This needs the following specific checks.

Its raw amplitude and conditioning caps are built from the physical
RMS/operator caps, \(R,K\), the inverse matrix-noise scale, local
interpolation coefficients, inverse label scale and guard margins. The
first group is polynomial in \(\beta^L,1+m/\gamma\); the second
contributes logarithms of the displayed counts; interpolation coefficients
have logarithm \(O(K)\); the noise-scale logarithm is in (4); and
\(nY\ge1\) bounds \(\log(1/Y)\) by \(\log n\). Thus the raw
cap logarithm is bounded by \(C\beta^{100L}Z\), without a new
global-history sensitivity multiplier.

The finite bridge's one-call Gaussian law uses gapped inverse/Sylvester
coefficients. Its coefficient, rounding and finite-Gaussian choices,
equations (17), (20)--(23), are fixed products of these caps, the physical
tolerances, counts and confidence. Their logarithms fit the new certificate.
The initial-root error must be allocated using the new real propagation
bound in place of the old global Gronwall exponent; it is not left at an
old unnecessarily stringent precision. The same conditional affine Gaussian
coupling and completed-call augmentation proof then applies to the new
finite source. Extra complete-table pair acquisitions still occur at
completed-call boundaries, and mandatory innovation contractions remain
within their original call.

For the passive decoder, the source cap \(\mathcal A\) of
FAST_FINITE_PASSIVE.md (13) therefore has logarithm at most this same
new certificate. Its small passive cap is unchanged:
\(\mathcal B\le C\beta^{110L}\sqrt{d+1}Z^{3/2}\).
From its (10), (15), (19) and the physical readout bound one can take

\[
 \mathcal C\le C\{1+\beta^{3L}(1+m/\gamma)
                              +\sqrt{(L+1)/\delta}\}.
 \tag{5}
\]

Consequently \(\log(1+\mathcal C)\le CZ\), and the logarithm of
the fixed-depth amplification \(\mathcal P\) is at most
\(C(L+2)Z\). The common-Gram ridge, finite mean/covariance tolerances,
fresh passive Gaussian expectation bias and old-mark finite interpreter
therefore require no algebraic inverse-gap factor in word length. The
passive choices remain in their original noncircular order: physical/noise
caps, then ridge, then finer scalar/grid tolerances and metric replay.

Whole-sphere confidence does not change this conclusion. The explicit
physical-code precision in FAST_PHYSICAL_QUERY_GRID.md is bounded by
the sum of \(\log n,L\log\beta,\log(1+m/\gamma),\log(H+2)\)
and \(\log(d+1)\), hence by \(CZ\). Its older coarse upper
envelope with an algebraic gap factor is unnecessary for the grid itself.
The code-count logarithm is at most \(C(d+1)Z\). Numerical passive
bias is uniform over guarded contexts; only estimator and generator
failures are unioned over codes, as in the already checked precision split.

Thus sufficient constructive certificates are

\[
 R\le C\beta^{201L}(m+d+2)(1+m/\gamma)Z^{5/2},\qquad
 p\le C\beta^{110L}Z,\qquad J,F\le C(d+1)p.             \tag{6}
\]

Choose base precision, scalar-noise scale, grids, samplers and final word
length in the same order as PRECISION_CONFIDENCE_SEPARATION.md. No
precision fixed-point equation is introduced. The finite-prior posterior
and exact metric-replay lemmas are unchanged statements for this chosen
finite source. One must not modify an already generated source tape to
new tolerances after the fact.

## 3. Complete resource substitution

Use the checked cached-history assembly of EXPLICIT_PHASE_COSTS.md, with
the new actual source counts and precision (6). The source includes the
\(d\) original roots and constant, so \(d+1\le CR\). The generator
block parameter is \(A\le CRp\), its level count is \(E\le Cp\),
its retained seeds use \(C(L+1)Rp^2\) bits, and stage median arrays
use \(C(d+1)Rp^2\) bits. Retained and peak training/query bits are
therefore \(C[R^2p+(L+d+2)Rp^2]\).

Initialization work is

\[
 C\{nR^5p^3+(nR+R^2)p^4+R^5p^2+R^4p^3+nR^2p^2\},
\]

with peak bits
\(C[nRp+R^3p+R^2p+(L+1)Rp^2]\). All training updates cost
\(C(R^5p^2+R^4p^3+R^3p^2)\). A query costs

\[
 C(L+1)\{(d+1)n(p^4/R+p^3)+R^4p^2+R^3p^3\}+CR^2p^2.
 \tag{7}
\]

The cubic norm/projection costs and sorting of all coordinate medians
are covered exactly as in CACHED_PHASE_CHECK.md; no quadratic projection
algorithm or inequality \(p\le R\) is assumed.

For checking substitution, the leading memory term \(R^2p\) has
powers \(512L,2,2,6\) in
\(\beta,m+d+2,1+m/\gamma,Z\). The main initialization term
has powers \(1335L,5,5,31/2\), the main training term
\(1225L,5,5,29/2\), and the main query preparation term, including
\(L+1\le C\beta^L\), has powers \(1025L,4,4,12\).
The other Gaussian, matrix, cached-row, seed and block terms have lower
powers in each parameter than their stated enclosing phase envelope.
They are substituted individually, not removed by comparing unspecified
actual values of \(R\) and \(p\).

## 4. External costs, labels, widths and the unchanged error qualification

For evaluator accounting alone let
\(b=\lceil C\beta^{110L}Z\rceil\). Sufficient activation value-call
counts, respectively for initialization, all training and one query, are

\[
 \begin{gathered}
 n\beta^{201L}(m+d+2)(1+m/\gamma)Z^{5/2},\\
 \beta^{402L}(m+d+2)^2(1+m/\gamma)^2Z^5,\\
 (L+1)[n+\beta^{402L}(m+d+2)^2(1+m/\gamma)^2Z^5].
 \end{gathered}                                          \tag{8}
\]

Multiply by actual evaluator work at \(b\)-bit precision and range,
add one live evaluator workspace, and retain its actual code description.
The \(O(b^3)\)-work, \(O(b)\)-space tanh evaluator fits the main
table. The analytic envelope alone gives no analogous universal bound for
an arbitrary supplied activation evaluator.

Acquiring the normalized training table is charged separately; its
\(m(d+1)\) finite values fit the retained numerical memory. Raw label
access requires

\[
 b+\lceil\log_2(16\sqrt m)\rceil
  +\lceil\log_2\max(1,1/Y)\rceil
\]

fractional bits. Add actual original data/code/certificate/scale descriptions,
certificate production or verification, query/time acquisition, and output
writing. No cost of a supplied population gap certificate or strip-bound
certificate is hidden as a free oracle.

Keep \(n\ge d\), \(nY\ge1\), the original numerical horizon gate
\(n\ge\max\{1,e^{-1}\sqrt{1+66\beta^{100L}m/\gamma}\}\),
and every inherited scientific width condition. A sufficient block-sampling
gate is now

\[
 n\ge\frac{C}{\delta}\,
 \beta^{512L}(m+d+2)^2(1+m/\gamma)^2Z^6.                 \tag{9}
\]

It follows from \(P\asymp R^2\), noise logarithm comparable to
\(p\), confidence share \(\alpha=c\delta\), the two-sided
certificate \(K_+\le\widehat K\le2K_+\), and
\(n\ge512\widehat K\). The chosen block length remains
\(s=\lfloor n/(128\widehat K)\rfloor\); its implemented vector
moment error is still proportional to
\(\sqrt{(R+1)(K_++1)/n}\), not the smaller population-center radius.

The additional passive error
\(CY\mathcal P\sqrt{(R+1)(K_++1)/n}+CYn^{-10}\) must still
be absorbed into the inherited dense-pair upper certificate to advertise
that benchmark. This is an eventual fixed-problem comparison. Its onset,
and the original scientific success threshold, are not made polynomial
by (9). Some inherited source gates themselves have the form
\(\sqrt{\log(en)}\ge\text{problem-dependent quantity}\).
The dependency audit explains why the stronger assertion of no exponential
dependence anywhere is not a consequence of these internal cost estimates.

The checked improvement is in explicit internal gap powers, not in the
logarithmic memory exponent or the query's factor \(n\). The existing
research/proof/canonical-notation workflows require that distinction to
remain visible in both this synthesis and the user-facing table.
