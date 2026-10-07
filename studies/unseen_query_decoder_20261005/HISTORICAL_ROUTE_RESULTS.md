# Historical route results before the current-state construction

This is the preserved earlier synthesis, superseded for the main existence
question by [RESULT.md](RESULT.md) and its complete current-state proof.
Its exact identities, scoped counterexamples and initialization-independent
near-1/n obstruction remain valid. Statements below that the main target
was open describe the earlier stage, not the present conclusion.

Updated 2026-10-06. The requested whole-sphere,
all-time decoder with an absolute logarithmic storage exponent is
**not proved**. Neither is a general impossibility theorem. The existing
finite-panel compression theorem remains unchanged. The resumed search
allows any absolute exponent and counts peak decoding workspace. It does
not retain all past training forwards and backwards.

## 1. Target and present conclusion

Keep the model and full label allowance of the authorized integrated compact
proof: hidden width n, fixed depth L>=2, analytic nonlinear activations with
bounded strip derivatives but possibly unbounded values, iid Gaussian first
and hidden weights, zero initial readout, mean training loss and mobilities
(n,1,...,1,n). There are m training inputs x_a of norm sqrt(d), spanning R^d
with m>=d; y_a are their labels. Write Y=||y||_2/sqrt(m)>0 and gamma>0 for
the unweighted initial population feature-Gram gap. All structural parameters
and confidence are fixed before the width limit.

The query x is supplied only after compilation/training and may be any point
of the sphere. The desired representation and its decoder must count all
retained arrays, program parameters and live workspace. It may do more than
a network forward pass, but cannot retrieve the discarded dense network,
encode it in arbitrary-precision real constants, store an uncounted function,
or replace nonlinear feature learning by a frozen kernel.

There are two distinct accuracy targets:

- The user's original dense-variability tolerance: the existing specified
  upper certificate, of root-width size times its growing subpolynomial
  factor, with the original task-dependent coefficients. Bare notation
  n^(-1/2+o(1)) alone would not specify this tolerance.
- The current finite-panel theorem's stronger matched-reference error:
  n^(-1+o(1)). For m>=2 this additionally retains fluctuations of the
  realized dense reference that a population-only decoder cannot reproduce.

The probability event must control all physical times including the fitted
endpoint and all sphere queries simultaneously. A statement for each fixed
query, or a finite predeclared panel, is not that statement. Merely evaluating
the current small network at a new input is possible, but its finite-panel
error proof supplies no accuracy guarantee there.

## 2. Exact scalar identity for the decoder's missing information

Let h_n(t,x) be the dense top hidden feature vector, and let w(t) be its
stored readout. The exact readout equation and initialization are

\[
\dot w(t)=\frac2m\sum_{a=1}^m
 (y_a-f_n(t,x_a))h_n(t,x_a),\qquad w(0)=0.
\]

Integrating and taking the current normalized readout gives

\[
f_n(t,x)=\frac2m\sum_{a=1}^m\int_0^t
 (y_a-f_n(s,x_a))
 \frac{h_n(s,x_a)^T h_n(t,x)}n\,ds.
\tag{1}
\]

No linearization or infinite-width limit is used. The original fitting
estimate makes the residual integrable, and its feature bounds plus
parameter convergence justify taking the fitted endpoint by dominated
convergence. Equation (1) remains an identity there.

Thus a comparison-based decoder need not reconstruct every dense feature.
It could instead evaluate the scalar, mixed-time similarities in (1).
But those are similarities of the **learned features**, not the raw inputs
and not merely the current training Gram. The finite-panel construction
does not provide their values at an undeclared input.

The available selection proof preserves initialized matrix actions on its
chosen temporal source spaces. It leaves an action defect for a query
feature outside those spaces. Nonlinear gates can turn an unresolved
component into a component seen by the retained readout. The exact defect
and an explicit local example are in [UNIFORM_SOURCE_DECODER.md](UNIFORM_SOURCE_DECODER.md).
That example invalidates a particular projection closure, not every decoder.

The current-feature projection decomposition in
[COMPARISON_DECODER.md](COMPARISON_DECODER.md) gives another version of the
same issue: the exact output equals its training-feature interpolation term
plus a readout/query remainder. The readout's derivative lies in the current
training-feature span, but the readout itself need not, because that span
moves. Input rank m>=d does not close either nonlinear feature-space gap.

## 3. A rigorous distinction between population decoding and matched decoding

Assume m>=2. Let g_n be any predictor determined by the fixed dataset and
width, independently of the realized dense initialization. It may have
arbitrary computational power and storage. Define the complete trajectory
norm by

\[
\|f-g\|_*=
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}|f(t,x)-g(t,x)|.
\]

For any deterministic positive sequence epsilon_n with

\[
\varepsilon_n\sqrt n[\log(en)]^{5/2}\longrightarrow0,
\]

the inherited dense variability lower theorem implies

\[
\mathbb P\{\|f_n-g_n\|_*\le\varepsilon_n\}\longrightarrow0.
\tag{2}
\]

Proof. Couple two independent dense copies with this same g_n. For every
fixed eta>0, the lower theorem eventually gives, with probability at least
1-eta, a separation at least c_{phi,L,eta}Y sqrt(gamma)/
(sqrt(n)log(en)^(5/2)). Its coefficient is positive. The assumption on
epsilon_n therefore implies

\[
\mathbb P\{\|f_n-\widetilde f_n\|_*\le2\varepsilon_n\}
\longrightarrow0.
\]

If both copies are within epsilon_n of g_n, the triangle inequality makes
their separation at most 2epsilon_n. For deterministic g_n, independence
therefore bounds the square of the probability in (2) by a quantity tending
to zero. This proves (2). If g_n uses auxiliary randomness independent of
both dense initializations, condition on that randomness. The probability
of both successes is the expectation of the squared conditional success
probability, at least the square of the unconditional probability. The
same argument applies.

In particular a population-only decoder cannot preserve the near-1/n
matched-reference guarantee. This is not a logarithmic storage lower bound:
an initialization-dependent compact state is not covered by (2). Nor does
it rule out root-width or larger tolerances, including the intended existing
dense upper certificate. The only non-elementary input to this corollary is the
authorized existing lower theorem, not a newly proved dense lower bound.

## 4. What the explored routes establish

| Route | Defensible conclusion | Missing part of the requested result |
|---|---|---|
| Comparisons with current training features | Exact decomposition, including the nonzero-span remainder; simple input interpolation is false even for spanning data | Uniform small remainder and a compact evaluator for unseen learned similarities |
| Nearest predeclared anchors | Exact all-time unseen-query error extension from anchor accuracy and the dense Lipschitz bound | Its covering certificate uses polynomially many anchors; the available panel-dependent storage bound does not certify the target |
| Scalar Gaussian decoding | A complete uniform initial-velocity decoder for deep sine networks uses O(md+m+L) storage at root-width accuracy | Actual nonlinear training destroys the layerwise conditional-independence argument; the full trajectory is not covered |
| Temporal covariance/response calculation | A candidate Gaussian-program representation has a tentative log(en)^5 covariance-storage count; new inverse-free source estimates and one complete reused-matrix law step are proved | Full growing-program law identification, stable finite evaluator/workspace and autonomous realization |
| Dense recomputation | Conditional all-time, whole-sphere evaluation has absolute-polylogarithmic working memory with explicit arithmetic and input qualifications | The repeatable dense initialization is not compressed and still counts |

The anchor derivation, including its precise probability qualification, is
in [ANCHOR_DECODER.md](ANCHOR_DECODER.md). It does not prove that all
interpolants or all decoders require its anchor count.

The initial-velocity construction and its full concentration argument are
in [UNIFORM_SOURCE_DECODER.md](UNIFORM_SOURCE_DECODER.md). Its success shows
that a spatial basis count cannot by itself establish an impossibility
theorem for scalar decoders. It is expressly not a frozen-feature model
substituted for deep nonlinear training.

The population-response route is documented in
[POPULATION_DECODER.md](POPULATION_DECODER.md). Counting covariance entries
is not a proof that their update/evaluation can be performed at the stated
accuracy and memory cost. A theorem for every fixed Gaussian computation
does not justify a computation whose history length grows with n. A clock
plus recomputation of an uncounted dense trajectory is not an autonomous
compact feature-learning model under this contract.

## 5. New proof progress under the counted-workspace contract

The following improvements are partial results, not a relabeling of a
storage count as an accuracy theorem.

First, scalar Gaussian matrix-action errors can be compared to their
**total** response derivatives at root-width accuracy without dividing by
the smallest history-Gram eigenvalue. The good-set vector-extension proof
works with RMS amplitude and actual-root Lipschitz bounds. A separate
Gaussian covariance coupling has the same eigenvalue-free root-width
rate. Both proofs, and a counterexample to replacing that coupling by
chronological Cholesky factors, are in
[ROOT_RESPONSE_AND_COVARIANCE.md](ROOT_RESPONSE_AND_COVARIANCE.md).
Its [independent reconstruction](ROOT_RESPONSE_AND_COVARIANCE_CHECK.md)
checks Sections 1--3 within their partial scope.

Second, the existing complex source domain and real good-pair estimates
give the required complex initialization sensitivity for training fields
and forward-query features. Analytic-patch summation then makes the scalar
response error simultaneous over the entire sphere and both source times
up to the existing logarithmic fitting horizon. Spatial coefficients are
proof devices only and are not retained by a decoder. The complete result
is [SOURCE_SUPREMUM_EXTENSION.md](SOURCE_SUPREMUM_EXTENSION.md), with its
[independent reconstruction](SOURCE_SUPREMUM_EXTENSION_CHECK.md).
It does not cover arbitrary Stein-test fields or passive-query backward
vectors, or assert endpoint derivative regularity.

Third, [GROWING_PROGRAM_STABILITY.md](GROWING_PROGRAM_STABILITY.md)
proves a full smooth-test Gaussian law for one forward/transpose reuse,
including its response mean and all finite-width feedback terms. It also
controls the first additional covariance loop. These explicit calculations
identify the remaining difficulty: general dependent histories introduce
nonzero causal responses that must be retained, not discarded as errors.
This longer note currently has author checks, not a complete independent
review of every new claim.

Finally, [RECOMPUTATION_SPACE.md](RECOMPUTATION_SPACE.md) and its
[check](RECOMPUTATION_SPACE_CHECK.md) give a fully specified conditional
working-space evaluator for the actual dense flow. It retains nonlinear
feature learning and covers the fitted endpoint and all sphere queries,
but still reads the original initialized coordinates. That information
cannot be excluded from total storage. Its corrected numerical specification
also counts input precision, projection arithmetic and nested recursion.
It is not the desired compact model and is not claimed to be fast.

Other salvaged constructive results are the all-time fixed-order label
recursion in [LABEL_SERIES_DECODER.md](LABEL_SERIES_DECODER.md) and an
initialization-oracle-free polynomial expectation algorithm in
[GAUSSIAN_EXPECTATION_SPACE.md](GAUSSIAN_EXPECTATION_SPACE.md). The former
has no proved width-uniform convergent full-label series; the latter's
direct activation composition has a depth-dependent degree. Neither closes
the target by itself.

## 6. Research outcome and next precise obligation

No positive all-time, whole-sphere absolute-polylog theorem is claimed. No general
decoder-size lower bound is claimed. No original compression theorem is
retracted or extended. The decisive next obligation is to construct a
finite evaluator for the learned mixed-time similarities in (1), or an
equivalent nonlinear response representation, and prove its uniform error
and counted workspace as the temporal resolution grows with n. For the
near-1/n target it must retain reference-specific fluctuations as well.

This study has no numerical experiment, implementation benchmark or promotion.
The three scoped routes were independent until their initial findings were
frozen; later communication is recorded in their notes. The lead reconstructed
the exact identities, the anchor estimate and (2), and checked the scalar
initial-velocity proof. The full desired theorem remains open, so these
checks are not an internal PASS for that theorem. After its own route was
frozen, unseen_uniform_sources additionally reconstructed this note's
Sections 1--3 and the full anchor note against the complete inherited lower
statement. It confirmed the algebra and probability argument, and requested
the explicit-anchor-list and accuracy-scale qualifications now retained.
This was not a blind review of the full research program.

Source snapshots used directly by the lead:

- finite-panel RESULT: `38ca06a2e812d8e2b45c6b7350c0437d710433b11a00b89aa66487a9229b028b`.
- integrated RESULT: `5e4697060e52c5db6c229240747cd061050c6cc93c37400cab765830abe5d23a`.
- integrated GENERAL_EXPLICIT_FITTING: `5c6f12b78847a2b2874c5bc82eb1cea5f4929ee071b114d09b098397c5e2b8d6`.
- integrated GENERAL_VARIABILITY_LOWER_RESULT:
  `20ae373e664a5440b670dc2c8a5b74cb4ed099dd5a08d66e61e988596b13fd2b`,
  read completely on 2026-10-05;
  used as the user-authorized inherited theorem for (2), not freshly audited
  through all its dependencies in this study.
