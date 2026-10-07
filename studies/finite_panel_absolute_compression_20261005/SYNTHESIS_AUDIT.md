# Internal audit of the finite-panel synthesis

2026-10-05. Final verdict: **PASS for the stated eventual-width,
retained-real-coordinate theorem, relative to the explicitly inherited
scientific interfaces.** The final RESULT.md is bound to SHA-256

    38ca06a2e812d8e2b45c6b7350c0437d710433b11a00b89aa66487a9229b028b

The two minor presentation points found on the initial version are now
resolved. No required correction remains within this bounded review scope.

This is a bounded internal post-author check, not an independent promotion
review or a fresh audit of the inherited stochastic insertion and selection
proofs. The initially checked RESULT.md had exactly 502 lines and SHA-256

    4e6d7baa5fa8c0960a462b4270374b8a9181a0d7a5834dc553089a8fb81246a4

That entire version was read; the final 506-line version was then verified
by exact delta and hash correspondence as recorded in Section 4.
RESULT.md was not edited by this reviewer. No other route's verdict was read.

## 1. Mathematical construction and storage

The localized radius is used correctly. With
\(\lambda=\gamma/m\), \(\ell=\log(en)\), and \(T=32\ell/\lambda\), the
authorized localized source gives

\[
r=\frac{\chi}{\lambda\sqrt\ell},\qquad
\alpha=\frac{r}{4T}=\frac{\chi}{128\ell^{3/2}}.
\]

The source coefficient \(\chi\) obeys \(0<\chi\le1\), equals one on the
simple cap, and has a positive activation/depth-only lower bound on the
entire original recurrence allowance. No smaller label cap is silently
used in the full-range conclusion.

The localized event covers all four needed source families. Forward
preactivation poles are controlled at the declared real queries. Backward
responses are holomorphic compositions of those gates, the holomorphic
training weights and the readout. Their RMS bounds follow from bounded
gates and complex operator bounds, without needing a passive carrier
coordinate maximum. The source comparison only uses training carrier
coordinate maxima in changed-gate estimates.

The Chebyshev coefficient and truncation estimates in Section 2 are
conservative and valid. In particular

\[
\log(64M_0n^{3/2}/\alpha)
=\log(8192M_0/\chi)+\tfrac32\log n+\tfrac32\log\ell
\le3.5\ell.
\]

Since \(\alpha\le1\) and \(\ell\ge1\), the ceiling gives
\(K+1\le6\ell/\alpha\). Four families at \(p\) inputs therefore require
at most \(3072p\chi^{-1}\ell^{5/2}\) coefficient vectors. These are
discrete time curves, not a polynomial in \(p\) spatial variables.
The exact initialized additions are the inherited ones needed for
the training Gram, first weights and paired initialized actions.

The source-selection interface is finite-source-space selection and
therefore applies to these paired temporal coefficient spaces. Its
use here is an inherited interface, explicitly identified as such,
not a newly proved coordinate sparsification theorem.

All storage roundings pass, including \(p=m=d=1\). Writing

\[
R=\left\lceil3072p\chi^{-1}\ell^{5/2}\right\rceil+2m+d+1,
\]

the ceiling and padding cost at most \(3p+2\le5p\). Since
\(\chi^{-1}\ell^{5/2}\ge1\),

\[
R\le3077p\chi^{-1}\ell^{5/2},\qquad
q_j\le9R\le27693p\chi^{-1}\ell^{5/2}.
\]

The proposed rounded width 30000 is safe. Direct integer arithmetic gives

\[
2048\cdot3077^2=19390318592
<68719476736=2^{36}.
\]

The simultaneous panel implementation also fits. Eight \(p\)-by-\(q_j\)
buffers per layer cost at most \(72LpR\le72LR^2\). Adding this to the
inherited \(1020(L+1)R^2\) inventory leaves more than \(956(L+1)R^2\)
of the displayed \(2048(L+1)R^2\) allowance. This covers the stated
linear output and extra solve scratch, while \(16p(d+1)\) covers stored
inputs and labels with slack over \(10m(d+1)\). First weights, initialized
copies, fixed metrics, current training arrays and Gram solves are already
included in the inherited inventory; they are not omitted or counted as
free functions.

The absolute exponent is consequently five. Fixed depth, activation
bounds, data geometry, gap and confidence still influence admissibility
and sufficient width. The statement correctly does not turn fixed-panel
probability estimates into a joint growing-\(p,d,m\) theorem.

## 2. Runtime, information flow and all-time comparison

Equations (14)--(15) are exactly the inherited corrected-readout runtime
with \(m\) training indices and denominator \(m\). The only inverse is the
training Gram; repeated passive inputs do not affect its invertibility.
No passive labels or passive fitting constraints are introduced.
Metric adjoints are retained, and the text explicitly avoids identifying
the specified direction field with ordinary gradient flow.

The optional chain rule (16) is correct. With consistent initial values,
its right side is the derivative of the forward preactivation at that
panel input. Uniqueness preserves that identity. Storing these additional
values cannot change the core training equations.

The deterministic comparison uses precisely the source accuracy,
isometry, image-pair identities and training initialization retained by
the temporal construction. Forward query control is the only part that
changes its observable domain. No additional factor \(p\), differentiated
source error, or missing passive adjoint estimate enters the output
comparison. The simple-cap constant 10 and the full-range universal
constant are attributed to their separate imported theorems.

The fitted endpoint is covered by independently integrating the two
systems' remaining velocity tails after \(T\). The compressed runtime
continues autonomously. The proof does not freeze a trajectory or infer
uniform infinite-time convergence from compact-time convergence.

The claimed compilation uses the inherited finite initial-jet and
quadrature interface. It does not receive future target observations.
Temporary original-width arrays and coefficients are explicitly discarded;
the retained matrices and state contain the complete autonomous runtime.
The text does not claim efficient preprocessing, a finite-bit theorem, or
an uncharged activation oracle. It requires the original activation
evaluator and its workspace to be counted. Within that explicitly stated
computational convention, no additional constructivity overclaim was
identified. This review does not independently implement or prove the
older compilation interface.

## 3. Actual dense variability and probability

The additional complete source GENERAL_VARIABILITY_LOWER_RESULT.md
states the lower bound for every fixed \(m\ge2\), \(Y>0\) and positive
training covariance gap in the same analytic activation class. It
requires no additional orthogonality or centered-feature assumption.
Crucially, its witness is at a deterministic training input and at an
early positive physical time. That input belongs to the panel, so the
lower bound transfers to the panel maximum, not merely to a larger
whole-sphere norm.

Consequently RESULT (17) is the inherited lower statement in the correct
observable. Combining it with the compression bound yields a deterministic
ratio envelope proportional to

\[
n^{-1/2}\ell^{5/2}e^{2\sqrt\ell}
\]

on the simple cap, which tends to zero. The full-range factor
\((1+\sqrt\ell)e^{32\sqrt\ell}\) has the same conclusion. For any fixed
failure tolerance, choose the lower event at half that tolerance and
intersect with the compression event. The union bound needs no
independence between those events. Taking the width sufficiently large
then proves convergence in probability of the ratio.

The lower theorem also implies that the denominator-zero event has
probability tending to zero. Assigning a value to the ratio there is
legitimate. The synthesis correctly excludes a universal ratio claim
at \(m=1\) or \(Y=0\), and distinguishes a whole-trajectory ratio from
pointwise relative error or endpoint separation.

## 4. Initial-version qualifications, now resolved

1. The source moment argument also has the explicit deterministic gate
   \(\ell\ge\max(e^2,2\mathcal B)\), with
   \(\mathcal B=1024e^2L\). Thus the convenient additional entry is
   \(\ell\ge2048e^2L\). RESULT (20) does not display it. The surrounding
   text retains the source event and an eventual, unquantified width
   threshold, so this does not invalidate the stated eventual-width
   theorem. It should be displayed if (20) is meant to list all explicit
   source gates. It is inherited, not a new scientific restriction.

2. RESULT (4) is the core independent dynamical-array count. If the
   optional simultaneous chain-rule panel values are retained as
   additional moving coordinates, their literal stored moving-coordinate
   count is larger than (4). They are already included in the correct
   all-retained bound (19). Calling (4) the “core moving-state count”
   would remove this minor ambiguity; it has no effect on the principal
   total-storage theorem.

Neither point blocks the theorem's finite-panel extension. Both are
resolved in the final version: its moving count is explicitly called
the core parameter-and-residual count, the passive dynamic coordinates
are explicitly assigned to the total-storage bound, and (20) displays
\(\ell\ge2048e^2L\).

The final file's hash was verified directly. Reversing exactly the
three corresponding textual substitutions in a read-only stream
reproduced the initial reviewed hash
4e6d7baa5fa8c0960a462b4270374b8a9181a0d7a5834dc553089a8fb81246a4.
Thus there are no additional changes between the completely read
initial version and the final version. This binds the final PASS to
38ca06a2e812d8e2b45c6b7350c0437d710433b11a00b89aa66487a9229b028b.

## 5. Read coverage and limitations

Completely read during this bounded synthesis check: frozen RESULT.md
(502 lines), GENERAL_VARIABILITY_LOWER_RESULT.md (286),
GENERAL_EXPLICIT_FITTING.md (410), and SIMPLE_CONSTANTS_SOURCE_CHECK.md
(441). The previously completely read authorized inputs were reused:
UNBOUNDED_COMPRESSOR_BRIDGE.md, EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md,
COMPACT_SOURCE_ENERGY.md, COMPACT_POLYNOMIAL_COMPARISON.md,
COMPACT_FULL_LABEL_RANGE.md, and GENERAL_TRAJECTORY_LOWER_BRIDGE.md,
along with this route's frozen PANEL_AUDIT.md.

The rigorous mathematics and conjecture-investigation instructions,
their applicable audit references, the explicit canonical-notation
contract and maintained notation were reused. The custom canonical
skill remains permission denied, as previously reported.

No experiments, external retrieval, shared-file edits, or Git mutations
were performed. This is not a new reconstruction of the initialized CLT,
source probability proof, selection theorem or complete older dependency
chain. Those remain named inherited interfaces.

Additional input hashes:

    GENERAL_VARIABILITY_LOWER_RESULT.md
    20ae373e664a5440b670dc2c8a5b74cb4ed099dd5a08d66e61e988596b13fd2b
    GENERAL_EXPLICIT_FITTING.md
    5c6f12b78847a2b2874c5bc82eb1cea5f4929ee071b114d09b098397c5e2b8d6
    SIMPLE_CONSTANTS_SOURCE_CHECK.md
    cc1096f354e38c97b5cab8fe2000323ca21811c9801a4a33a4c5dbaf0a08938a
