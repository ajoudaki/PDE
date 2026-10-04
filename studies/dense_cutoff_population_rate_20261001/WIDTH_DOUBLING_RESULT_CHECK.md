# Check of the width-doubling synthesis

2026-10-03. Scoped internal reconstruction by the author of
WIDTH_DOUBLING_BLOCK_ROUTE.md. This is a check of the coordinator's
synthesis, not an independent re-review of the block-route proof or a
promotion review. No other study, experiment, manuscript edit, or Git
write was used.

**Verdict: PASS for the claims actually stated.** The source proves the
split-block endpoint comparison and the equivalence of two still-open
quantitative targets. It does not prove canonical width doubling or a
near-root dense-to-population rate. No correction to the frozen source
was needed.

The complete checked source is WIDTH_DOUBLING_RESULT.md, SHA-256

    8a4948901b4a4b1b2e3ac1c21b4206cc594d55ace3df5855481ca4ba796320de

The previously read proof dependencies retained for this reconstruction
are GENERAL_SELF_AVERAGING.md, SHA-256

    bfbc14cbb3cccf902420db74ca6e3627e341f27a84b52a229362848b376a56d5

and WIDTH_DOUBLING_BLOCK_ROUTE.md, SHA-256

    452fffc78086900b9ccb550ee4903353dc542246c2153772b7a0f17bfcabacdf

GENERAL_SELF_AVERAGING.md was reread completely. The current manuscript
and its mathematical inputs were read completely in the preceding
scoped work; the exact population-convergence passages were reread
here. Their current hashes are:

- paper/results.tex:
  6e76e83aae3a3e36f588bdf37dddf72ac811bf2644de664fb0b4b83f117704a1.
- paper/proof_alltime.tex:
  f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d.
- paper/proof_tracking.tex:
  e75f8122ab0ed0bc5f8c0b5f979b7e1a1b779c94440367d62d9a98892d3e53be.

## 1. Objects and hypotheses match

For a fixed query law \(\mu\) with finite second moment, put
\[
 \|h\|_\mu
 =\left(\int\sup_{t\in[0,\infty]}|h(t,x)|^2\,d\mu(x)\right)^{1/2},
 \qquad
 a_n(K)=n^{-1/2}\exp\{K\sqrt{\log(e+n)}\}.
 \tag{1}
\]
This is a seminorm on measurable prediction paths and a norm after
identifying paths equal \(\mu\)-almost everywhere in the time-supremum
sense. Its triangle inequality follows from the pointwise triangle
inequality for the time supremum and then Minkowski in \(L^2(\mu)\).
All uses of a triangle inequality in the source are valid in this
same norm; there is no exchange of the time supremum and query integral.

The canonical models have fixed depth and data, zero initial readout,
the stated independent Gaussian matrices and canonical mobilities.
The small fixed label threshold, feature-Gram gap and fixed positive
sample weights are unchanged. The broad \(C^3\) activation class with
bounded first three derivatives is contained in the manuscript's
\(C^1\) class with bounded Lipschitz derivative. The activation value
has at most linear growth; bounded activation values are not required.

For exact duplicate or parity quotients, the weighted data reduction
preserves the original parameter equations and physical time. The
weighted tangent is conjugated by
\(D_p=\operatorname{diag}(\sqrt{p_a})\).
The positive gap and all residual norms must be read in that
convention, as the source states.

The fitted endpoint exists on the good events. Probability statements
include those events, whose probabilities tend to one. Values outside
them need not be assigned fitted endpoints or integrated in an
unconditional expectation.

## 2. Probabilistic doubling is equivalent to a deterministic center gap

Let \(c_n(t,x)\) be the deterministic scalar-extension center from
GENERAL_SELF_AVERAGING.md. That construction gives, for every
\(\eta>0\), constants \(A_{\eta,\mu}\) and \(n_{\eta,\mu}\) such that
for all \(n\ge n_{\eta,\mu}\),
\[
 \Pr\{\|f_n-c_n\|_\mu\le A_{\eta,\mu}a_n(K_0),
             \ \text{the fitting event holds}\}\ge1-\eta.
 \tag{2}
\]
The exponent \(K_0\) is fixed independently of width and confidence.
The centers are deterministic functions, not unverified autonomous
expectations.

First suppose there is a deterministic bound
\[
 \|c_n-c_{2n}\|_\mu\le A_\mu a_n(K_1)
 \quad\text{for all }n\ge n_*.
 \tag{3}
\]
For any requested failure probability \(\delta\), apply (2) to each
marginal with failure probability \(\delta/2\). On their intersection,
the triangle inequality through the two centers proves the desired
canonical doubling estimate. Independence is not needed for this
deduction; correct marginal laws suffice.

For the reverse implication, suppose the requested canonical doubling
estimate is true. Fix each of its failure probability and the two
failure probabilities in (2) to \(1/8\). For all sufficiently large
\(n\), the three events have intersection probability at least \(5/8\)
under the product law of the two canonical initializations. On that
intersection,
\[
 \|c_n-c_{2n}\|_\mu
 \le \|c_n-f_n\|_\mu+\|f_n-f_{2n}\|_\mu
                      +\|f_{2n}-c_{2n}\|_\mu.
 \tag{4}
\]
For \(K\ge0\),
\[
 a_{2n}(K)\le
 2^{-1/2}\exp\{K\sqrt{\log2}\}\,a_n(K).
 \tag{5}
\]
Thus the right side of (4) is at most
\(A_\mu a_n(\max(K,K_0))\), with a fixed constant.

The left side of (4) has no random argument. A positive-probability
intersection is enough to establish its deterministic upper bound
for that \(n\). The same constants and width threshold apply to every
sufficiently large integer \(n\). No random event common to all
widths is asserted or needed. Fixing confidence at \(1/8\) also means
that no free confidence parameter remains in the deterministic
constant. This verifies both directions of the source's center
equivalence.

## 3. The qualitative population input is in the required norm

The manuscript's population construction supplies a unique deterministic
dense predictor \(f_\infty(t,x)\), with the same canonical dynamics and
the same small-label scope. In paper/proof_tracking.tex, subsection
“Whole-input prediction and population convergence,” the proof first
extends finite-probe convergence to bounded query sets, then extends
finite time to all time using
\[
 |\partial_t f_n(t,x)|
 \le C e^{-\kappa t}(1+\|x\|_2/\sqrt d).
 \tag{6}
\]
The same physical bounds hold for the population predictor.
The tail beyond a large query radius is controlled by
\(\int_{\|x\|>R}(1+\|x\|_2/\sqrt d)^2\,d\mu(x)\).
Consequently that proof explicitly gives
\[
 \|f_n-f_\infty\|_\mu\xrightarrow{\Pr}0.
 \tag{7}
\]
This is exactly (1), including the fitted endpoint by the integrated
time-tail bound. It is not merely fixed-time convergence, convergence
of a few training coordinates, or a norm with the supremum outside
the integral. Fixed positive sample weights do not change this
passage after the exact data reduction.

Since \(a_n(K_0)\to0\), (2) implies
\(\|f_n-c_n\|_\mu\to0\) in probability. For any \(\varepsilon>0\),
for all sufficiently large \(n\), the two events
\[
 \|f_n-c_n\|_\mu\le\varepsilon/2,\qquad
 \|f_n-f_\infty\|_\mu\le\varepsilon/2
\]
have positive-probability intersection. Hence the deterministic
quantity \(\|c_n-f_\infty\|_\mu\) is at most \(\varepsilon\).
This proves the full-sequence deterministic convergence of centers
used in the source. It uses no uniform integrability or expectation
of the original prediction off the good event.

## 4. Dyadic summation gives the quantitative equivalence

For every integer \(j\ge0\),
\[
 \frac{a_{2^j n}(K)}{a_n(K)}
 \le 2^{-j/2}\exp\{K\sqrt{j\log2}\}.
 \tag{8}
\]
Indeed \(e+2^j n\le2^j(e+n)\), followed by
\(\sqrt{u+v}\le\sqrt u+\sqrt v\), gives the exponent bound.
For fixed \(K\), the series of the right side converges: its logarithm
is \(-j\log2/2+K\sqrt{j\log2}\), which is eventually at most
\(-j\log2/4\). Thus
\[
 \sum_{j=0}^\infty a_{2^j n}(K)\le C_K a_n(K),
 \tag{9}
\]
with \(C_K\) independent of \(n\).

Suppose the center increment bound (3) has been established. For
\(n\ge n_*\) and any finite \(J\), every intermediate width \(2^j n\)
also exceeds \(n_*\), and the finite triangle inequality gives
\[
 \|c_n-f_\infty\|_\mu
 \le A_\mu\sum_{j=0}^{J-1}a_{2^j n}(K_1)
       +\|c_{2^J n}-f_\infty\|_\mu.
 \tag{10}
\]
The last term tends to zero by Section 3. Taking \(J\to\infty\) in
this scalar inequality and using (9) proves
\[
 \|c_n-f_\infty\|_\mu\le C_\mu a_n(K_1).
 \tag{11}
\]
Combining (11) with (2) proves the near-root dense-to-population
estimate at every fixed confidence. Conversely, two such population
estimates at widths \(n\) and \(2n\), a union bound and the triangle
inequality imply canonical doubling.

Every infinite operation above is deterministic. The only random
intersection used to infer the center increment involves three events
at two widths and one fixed confidence level. There is no hidden
countable union, width-dependent confidence, or demand for a
quantitative probability bound on the complement of the fitting
event.

The exponent may increase to the maximum of the requested doubling
exponent and the existing concentration exponent. The equivalence is
therefore an equivalence within the stated class
\(n^{-1/2}\exp\{K\sqrt{\log(e+n)}\}\), not a claim of equality of
optimal constants or exponents.

## 5. The split endpoint is represented and used correctly

At total width \(N=2n\), the profile has within-block hidden variance
\(2/N=1/n\), cross-block variance zero, and matched hidden mobility
two within each block. The first and readout mobilities are \(N\).
With output normalization \(1/N\), these choices give two exact
canonical width-\(n\) block equations driven by their common
averaged-output residual. Their training paths are coupled; the source
does not call them independent.

The comparison references are the two independent autonomous
width-\(n\) flows from the same respective initializations.
Writing weighted residuals throughout, let \(s=(r_1+r_2)/2\),
\(d=(r_1-r_2)/2\), and \(e=R-s\). Their exact residual equations yield
\[
 \dot e=-2\widetilde{\bar\Gamma}e
   -2(\widetilde{\bar\Gamma}-\bar\Gamma)s
   +(\Gamma_1-\Gamma_2)d,\qquad e(0)=0,
 \tag{12}
\]
as stated. The source's unweighted display has this same meaning after
the stated conjugation by \(D_p\).

The block-route proof provides the coupled physical tube and fitting
from its initial average feature Gram. It uses the carrier maximum
only on each independent reference. Damping (12), parameter
subtraction, and the finite reference activity give
\[
 \sup_t(D_1+D_2)
 \le C\exp\{CS(1+M_n)\}
           \int_0^\infty\|d(t)\|\,dt.
 \tag{13}
\]
There is no unproved carrier assumption on the shared-residual
training paths.

Same-width concentration applied to a fixed mixture of the query law
and training law controls \(\sup_t\|d(t)\|\) and the query
disagreement on a common event. If its training bound is
\(\varepsilon_n\), exponential fitting also gives
\(\|d(t)\|\le CYe^{-\kappa t}\). Splitting the integral at
\(\kappa^{-1}\log(CY/\varepsilon_n)\) gives
\[
 \int_0^\infty\|d(t)\|\,dt
 \le\frac{\varepsilon_n}{\kappa}
              [1+\log(CY/\varepsilon_n)]
 \tag{14}
\]
when \(0<\varepsilon_n<CY\). Zero labels are handled separately.
For the stated near-root \(\varepsilon_n\), the logarithmic factor
is \(O(\log(e+n))\), while \(M_n=CS\sqrt{\log(e+n)}\).
Both factors in (13)--(14) are absorbed into a fixed increase in the
near-root exponent. The query factor is linear in
\(1+\|x\|_2/\sqrt d\), so the second query moment suffices.

Thus the source's endpoint theorem and its consequence for comparison
to either independent width-\(n\) reference follow from the exact
block proof and the established same-width theorem.

## 6. Claim boundaries

The profile value \(s=1/2\) has hidden variance \(1/(2n)\) and mobility
one, so it is the canonical width-\(2n\) network. The proved endpoint
at \(s=0\) is a different auxiliary law. Its near-root proximity to
width \(n\) does not estimate the change from \(s=0\) to \(s=1/2\).
The source preserves that distinction.

The two additional route notes cited in the synthesis were not used
to establish a new positive estimate in this check. Their claimed
failure to close the remaining contrast is consistent with the
synthesis's explicit open status; this report is not a fresh audit
of those separate candidate calculations.

The exact conditional equivalence is a useful characterization of
the missing bias estimate. It does not remove that estimate or add it
as an assumed hypothesis of an advertised unconditional theorem.
No strict-root, large-label, growing-depth, or unconditional
expectation conclusion is justified or claimed here.
