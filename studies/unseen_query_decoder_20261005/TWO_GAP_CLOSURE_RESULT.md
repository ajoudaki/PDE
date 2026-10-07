# Finite probability and dense-scale error: closure with a different decoder

2026-10-07. Current-study synthesis of the finite training-source theorem,
source-seeded query construction, and numerical mesh lemma. The new source
and query implications have separate bounded independent reconstructions.
This is internally checked research, not promotion into the maintained book.
The [bounded assembly check](TWO_GAP_CLOSURE_CHECK.md) verifies the final
probability allocation, center/tail implication, error absorption and
parameter-explicit cost composition at the stated component boundaries.

**Outcome.** The source-probability gate has an explicit polynomial width.
The final passive-bias gate can be avoided by a modified decoder which
regenerates the finite source rows and keeps their full conditional
covariance correction. It reaches the original leading dense-pair
upper-certificate scale without waiting for an exponential error factor
to dominate a statistical remainder. This is not a proof for the unchanged
sixth-power-memory decoder. The new construction uses more memory and still
has a factor of dense width in query work.

## 1. Setup and preserved scope

The parameters are dense width \(n\), training count \(m\), dimension
\(d\), fixed hidden depth \(L\ge2\), population feature-Gram gap
\(\gamma>0\), label RMS \(Y=\|y\|_2/\sqrt m\), and confidence
\(1-\delta\), with \(0<\delta<1/4\). Training inputs span
\(\mathbb R^d\), have norm \(\sqrt d\), and \(m\ge d\).

Keep the original Gaussian initialization, zero initial readout, mean
squared loss, mobilities \((n,1,\ldots,1,n)\), and nonlinear learning
in every hidden layer. For the common analytic strip of width \(a\),
use exactly the existing envelope
\[
 \beta=\max\left\{10,1+\max_j|\phi_j(0)|,16/a,
 \max_{j,\,r=1,2}\sup_{|\operatorname{Im}z|<a/2}
                       |\phi_j^{(r)}(z)|\right\}.
\]
For the resource bounds use the single logarithm
\[
 Z=\log(en)+\log\left(e+
       \frac{(m+d+2)\beta^{100L}(1+m/\gamma)}\delta\right).
\]
Activation values need not be bounded. The full original fitting/source
label intersection is retained, with its explicit finite source recurrence;
it is recorded in FULL_FINITE_SOURCE_PROBABILITY.md, Section 1, and the
authorized integrated proof's (38). No moment-dependent or smaller label
cap is imposed. At \(Y=0\) use the exact stationary zero predictor.

The compact state permits unseen inputs and uses no test labels. A query
uses only the present retained state and its seeds. It does not re-integrate
the scalar training dynamics. Setup may inspect a completed independent
virtual source, as before; it is not a strictly online construction.
All retained seeds, all ensemble members and peak decoding memory count.
The existing finite activation/input/certificate interfaces remain charged.

Write \(b_n\) for the label-refined dense-pair upper certificate at
confidence \(\delta/256\). Its leading coefficient, exponential factor
and logarithmic power are unchanged. Its previously unspecified \(Y/n\)
mesh coefficient is now explicitly instantiated by the original physical
modulus, as described in Section 3. Thus this is not a claim about an
arbitrarily pre-fixed smaller numerical mesh coefficient, nor about a
sharp dense variability rate or a lower bound on dense discrepancy.

## 2. Finite-confidence width

Use the integer moment order
\[
 p=\max\left\{1,
 \left\lceil\frac{\log(2^{22}emL/\delta)}{\log(64e^2)}\right\rceil
 \right\}.
 \tag{1}
\]
The checked source theorem, applied at failure \(2^{-20}\delta\), gives
the explicit sufficient width
\[
 \boxed{\displaystyle
 n\ge
 \left\lceil\left[
 \frac{2^{20}\beta^{2000L}}{\delta}
 (1+m/\gamma)^4(m+d+p+1)^4
 \right]^{20000}\right\rceil.}
 \tag{2}
\]
This is polynomial in the displayed major parameters, although its powers
are extremely conservative. In particular it is not a practical onset
estimate. It contains no inverse \(Y\), no exponential in \(m\),
\(d\), \(1/\gamma\), or \(\beta^L\), and no unspecified
stochastic threshold.

The theorem is at each individual width, not one event for all widths
or all label vectors. It proves the training-source complex-time domain
with radius
\[
 \frac{1}{p\beta^{100L}(1+\gamma/m)\sqrt{\log(en)}}.
\]
The real fitting theorem supplies the whole-sphere physical trajectory
and fitted endpoint. A whole-sphere complex source is not needed by this
training-only program and is not asserted here.

There is no additional unquantified dense-center event hidden here.
The structural dense good-pair comparison uses only the all-time fitting,
Gram, operator and RMS bounds together with a training-carrier maximum.
The new source supplies these through \(32(m/\gamma)\log(en)\).
The explicit carrier-tail gate in POLYNOMIAL_SOURCE_WIDTH.md (29)--(30)
extends that maximum with a factor two to all time; its sufficient width
is at most \(\max\{1,(\beta^{23L}/8)^{1/15}\}\), already dominated
by (2). That note's physical horizon gate is also dominated by (2).
Apply the same deterministic good-pair estimate and Gaussian extension
argument to this new good set. Its deterministic center is a proof
object, not decoder advice. No old qualitative source-probability limit
is needed for this step. The fitting label cap implies \(Y\le1\),
as required by the label-refined comparison. The smaller source failure
allocation above leaves the required shares for the independent dense
event, its Gaussian concentration, and whole-source amplification.

The proof initializes every required rectangular cavity, controls the
nonlinear insertion remainder in label-normalized coordinates, includes
the omitted response port and direct reverse observable, and transfers
the pole/response/budget stops. Its finite distinct-root moments and
collision count yield a probability bound at the chosen \(p\), rather
than taking width to infinity and then moment order to infinity.

Proof: [FULL_FINITE_SOURCE_PROBABILITY.md](FULL_FINITE_SOURCE_PROBABILITY.md).
Fresh isolated reconstruction:
[FULL_FINITE_SOURCE_PROBABILITY_CHECK.md](FULL_FINITE_SOURCE_PROBABILITY_CHECK.md).

Numerical implementation has separate explicit gates. For the unchanged
word-precision table retain \(nY\ge1\), namely \(n\ge1/Y\).
This is a numerical sufficient-width condition, not an extra upper label
restriction or a premise of (2). For smaller positive labels the stated
additional \(\log_+(1/(nY))\) precision must instead be charged. Ordinary
finite arithmetic, sampling and numerical-error gates are polynomial;
their composition is recorded separately in
[CLOSURE_COMPOSITION_COSTS.md](CLOSURE_COMPOSITION_COSTS.md).
Concretely the remaining source/query Gaussian RMS failures are at most
\(C(R+L)e^{-cn}\), where the local field count satisfies
\(R\le Cp\beta^{201L}(m+d+2)(1+m/\gamma)Z^{5/2}\).
A sufficient gate is
\[
 n\ge C\left[
 \frac{2^{20}p\beta^{201L}(m+d+2)(1+m/\gamma)}\delta
 \right]^2,
\]
with universal \(C\). It is dominated by (2) after a universal
absolute enlargement; alternatively retain this explicit additional gate.
All other finite sampler, one-call Gaussian-law and metric rounding
failures are controlled by the pre-setup precision allocations, not by
an unspecified eventual-width premise. For tiny labels,
\(\log_+(1/Y)\le\log n+\log_+(1/(nY))\), explaining the extra
precision beyond the baseline \(\log n\) budget.

## 3. Final error without the old passive bias

The new decoder retains a short seed for each virtual finite source.
At a query it regenerates those actual empirical rows, evaluates their
already acquired row instructions, and keeps the full two-orientation
Gaussian covariance correction. It does not substitute prior expectations
for posterior moments or replace the finite covariance by a scalar one.
Therefore the old root-width passive comparison term is absent; it has
not been absorbed into an enlarged constant.

A finite-transcript argument transfers each fixed-query source experiment
to its short-seed version. A median of complete source models, with an
additional counted seed for the ensemble, controls all sphere/time codes.
Repeating only passive queries on one shared source would not establish
this simultaneous event and is not the construction used here.

The checked comparison is
\[
 \sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
 |\widehat f(t,x)-f_n^{\rm independent}(t,x)|
 \le 2b_n+A_{\rm num}Y n^{-10}
 \quad\text{with probability at least }1-\delta.
 \tag{3}
\]
The local symbol \(A_{\rm num}\) is the total explicitly allocated
numerical error coefficient; source, query and input/time tolerances can
be allocated with an absolute total. The source and query precision must
be chosen together before setup. Refining only new query arithmetic while
retaining coarser source moments is not sufficient.

The original physical modulus supplies a declared mesh coefficient
between \(32\) and \(C\beta^{4L}(1+m/\gamma)\), so
\(b_n\ge32Y/n\). Hence the entirely explicit additional gate
\[
 n\ge\max\{1,(A_{\rm num}/32)^{1/9}\}
\]
gives
\[
 \boxed{\displaystyle
 \sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
 |\widehat f(t,x)-f_n^{\rm independent}(t,x)|\le3b_n.}
 \tag{4}
\]
No lower bound on an unspecified leading dense coefficient and no
eventual dominance by \(\exp(cY^2\sqrt{\log n})\) is used.

The numerical coefficient choice preserves the original leading
label-refined certificate. It uses its original mesh proof, not the
different weaker leading coefficient in the explicit dense fallback.
Its full definition and proof are in
[NUMERICAL_BENCHMARK_ABSORPTION.md, Section 5](NUMERICAL_BENCHMARK_ABSORPTION.md).
The exact-query construction and common precision schedule are in
[SOURCE_SEED_EXACT_QUERY.md](SOURCE_SEED_EXACT_QUERY.md), with the
independent reconstruction and correction recheck in
[SOURCE_SEED_EXACT_QUERY_CHECK.md](SOURCE_SEED_EXACT_QUERY_CHECK.md).

## 4. Costs and what is not achieved

At fixed problem parameters, including confidence and positive label
scale, \(Z\) is proportional to \(\log(en)\).
The modified decoder's internal retained size and peak training/query
memory are \(O(Z^7\log(e+Z))\) bits; an absolute integer logarithmic
power eight suffices. The complete setup, complete compact training,
and single-query work bounds are respectively
\[
 O(nZ^{33/2}+Z^{15}\log(e+Z)),\qquad
 O(Z^{31/2}+Z^{15}\log(e+Z)),\qquad
 O(nZ^{14}+Z^{15}\log(e+Z)).
\]
The finite-moment refinement additionally contributes \(p^2\) to
memory, \(p^5\) to setup/training and \(p^4\) to query work in the
parameter-explicit envelopes. These are not hidden confidence constants.
The complete parameter substitution and input/evaluator charges are in
[CLOSURE_COMPOSITION_COSTS.md](CLOSURE_COMPOSITION_COSTS.md). Its explicit
polynomial gate for quadratic internal bit work is already dominated by
(2). This does not bound arbitrary external activation or data-access
costs by quadratic work.

This closes the two specified gates for this modified representation,
not the unchanged earlier passive estimator or its sixth-power bit table.
It does not prove logarithmic query work, fifth-power bit storage, a
practical sufficient width, sharp sample/gap dependence of dense
self-variability, or a training-time speedup. Existing label, numerical
access and non-online setup qualifications are not removed. No material
outside this study has been changed or promoted.
