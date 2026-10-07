# Three-phase costs with precision separation and cached history

2026-10-06. Lead-author synthesis of two resource refinements in the same
unseen-input study. The [precision check](PRECISION_CONFIDENCE_CHECK.md)
and [cached-phase check](CACHED_PHASE_CHECK.md) pass this resource assembly
under its inherited scientific and computational interfaces. No scientific
scope, accuracy target or label allowance is strengthened. This note
supersedes the resource table of FAST_LOCAL_EFFICIENCY_RESULT.md; its
original scientific interfaces remain inputs. No experiment, executable
implementation or promotion is claimed.

## Shared setup and notation

Use dense width \(n\), \(m\) training inputs in dimension \(d\),
fixed depth \(L\ge2\), positive initial population feature-Gram gap
\(\gamma\), label RMS \(Y=\|y\|_2/\sqrt m\), and confidence
\(1-\delta\). The training inputs span \(\mathbb R^d\), so
\(m\ge d\), and lie on the radius-\(\sqrt d\) sphere. Preserve
the original Gaussian initialization, zero readout, mean-squared loss,
mobilities \((n,1,\ldots,1,n)\), and learning in every layer.

For the given common analytic strip width \(a\) and layer activations
\(\phi_j\), the explicit activation envelope is

\[
 \beta=\max\left\{10,1+\max_{j\le L}|\phi_j(0)|,16/a,
 \max_{j\le L,\,k=1,2}\sup_{|\operatorname{Im}z|\le a/2}
 |\phi_j^{(k)}(z)|\right\}.
\]

Activation values may be unbounded. Use just one shared logarithm:

\[
 Z=\log(en)+\log\!\left(e+
 \frac{(m+d+2)\beta^{100L}(1+m/\gamma)}{\delta}\right).
 \tag{1}
\]

Retain the full inherited source/fitting/compact label intersection.
Its consequence \(16Ym/\gamma\le1\) does not replace it.
Zero labels give the separate exact zero predictor. For nonzero labels,
the tables concern the sufficiently-large-individual-width branch.

The predictor accepts unseen inputs using its present compact state,
without replaying scalar training or using test labels. Its high-probability
guarantee covers the whole sphere and entire physical training trajectory,
including the fitted endpoint, at the inherited independent-dense-pair
**upper-certificate scale**. This is not near-\(1/n\) accuracy for a
specified initialized dense model, or a guarantee relative to the realized
discrepancy of two particular dense runs.

## Model size and the three phases

Units are bits and bit operations. Table entries suppress only universal
multiplicative constants. For \(\tanh\), activation arithmetic is
included; for the full analytic class, actual evaluator costs are the
explicit additions below. Original data/code/certificate descriptions and
input/output costs are not declared constant.

The retained internal model size is at most

\[
 O\!\left(\beta^{530L}(m+d+2)^2(1+m/\gamma)^5Z^6\right).
 \tag{2}
\]

| Phase | Time | Peak memory, including the model |
|---|---|---|
| Initialization — generate the virtual source and construct the compact model | \(n\beta^{1340L}(m+d+2)^5(1+m/\gamma)^{13}Z^{31/2}\) | \(\beta^{730L}\big[n(m+d+2)(1+m/\gamma)^3Z^{7/2}+(m+d+2)^3(1+m/\gamma)^7Z^{17/2}\big]\) |
| Training — complete all compact updates, excluding queries | \(\beta^{1230L}(m+d+2)^5(1+m/\gamma)^{12}Z^{29/2}\) | \(\beta^{530L}(m+d+2)^2(1+m/\gamma)^5Z^6\) |
| Querying — predict at one unseen input from the current state | \(n\beta^{450L}(d+1)(1+m/\gamma)^4Z^4+\beta^{1030L}(m+d+2)^4(1+m/\gamma)^{10}Z^{12}\) | \(\beta^{530L}(m+d+2)^2(1+m/\gamma)^5Z^6\) |

Initialization may inspect the completed finite virtual source. It is not
a strictly online algorithm, and its peak memory is not compact. No dense
\(n\)-by-\(n\) Gaussian matrix collection is materialized. Training
counts the complete finite schedule and tail freeze, not just a vector-field
evaluation. Queries cost the sum of their individual times. The same
success event covers adaptively selected sphere inputs and requested times.

For comparison with a real-coordinate size statement, the internal
numerical-word count remains bounded by

\[
 O\!\left(\beta^{410L}(m+d+2)^2(1+m/\gamma)^4Z^5\right),
 \tag{3}
\]

but each word has up to \(C\beta^{110L}(1+m/\gamma)Z\) bits.
Fixed bitstrings are finitely packed and all their bits are counted in
(2). Equation (3) does not prove a fifth-power bit model.

## Derivation of the improvements

All symbols in this paragraph are local to the derivation. The actual
field count \(R\) and sufficient word length \(p\) obey

\[
 R\le C\beta^{201L}(m+d+2)(1+m/\gamma)^2Z^{5/2},\qquad
 p\le C\beta^{110L}(1+m/\gamma)Z.
 \tag{4}
\]

The [precision separation](PRECISION_CONFIDENCE_SEPARATION.md) removes
the old factor \(d+1\) from each word. The physical-grid union is paid
in the number of median blocks \(J\le C(d+1)p\) and generator error,
not in every arithmetic operation's precision. The generator parameter
is still \(A\le CRp\), since the actual source includes \(d\) roots
and the constant. Thus retained and peak training/query storage are

\[
 C[R^2p+(L+d+2)Rp^2].                                   \tag{5}
\]

The [cached-history refinement](PARAMETER_FACTOR_REFINEMENT.md) retains
only already acquired finite coefficient vectors. They are functions of
the current scalar prefix. Source and selected-packet fields keep their
creation-time arguments; exact cached metric contractions reproduce the
same scalar tape. A fresh prior packet still evaluates its whole old
nonlinear row interpreter, but never resolves all historical conditioning
systems. Only the new passive-layer systems are prepared.

Constructing the scalar rank weights costs \(CR^2p^2\); this does not
assert quadratic work for every norm or projection. General rank-list
Frobenius norm contractions can cost \(C(L+1)R^3p^2\), included in
the matrix-preparation bound below. The check makes this distinction
explicit and does not endorse the separate sharper per-layer table.

Consequently one query costs at most

\[
 C(L+1)\{(d+1)n(p^4/R+p^3)+R^4p^2+R^3p^3\}
       +CR^2p^2.                                       \tag{6}
\]

The two query-preparation monomials substitute to activation exponents
at most \(1025L\) and \(934L\), data powers four and three, gap
powers ten and nine, and logarithmic powers twelve and \(21/2\).
They are covered by the query table's second term. Median sorting costs
\(CRJ\log(J+1)p\le C(d+1)Rp^3\); because \(d+1\le CR\),
this is covered by \(CR^3p^3\) in (6). Seed generation, finite Gaussian
generation, integer ranges and simultaneous block-vector storage are all
included. No relation \(p\le R\) is assumed.

Initialization and the conservative complete training bounds remain
those substituted in PRECISION_CONFIDENCE_SEPARATION.md. The sharper
per-layer inventory in PARAMETER_FACTOR_REFINEMENT.md additionally
retains explicit powers of \(L\) and separates \(d+1\) from \(m\);
the headline table above uses the simpler valid envelope (4), with all
depth factors absorbed into the *displayed* powers of \(\beta^L\).
They are never suppressed as universal constants.

Relative to the preceding checked table, the retained-memory data power
drops from three to two; initialization and training data powers drop
from eight and seven to five; the query-stream dimension factor drops
from \((d+1)^4\) to \(d+1\); and query preparation drops from
\(Z^{29/2}\) to \(Z^{12}\). The inverse-gap powers are not newly
reduced by these changes.

## General activations, input costs and label scale

For this evaluator accounting alone, use sufficient precision and
argument-length allowance

\[
 b=\lceil C\beta^{110L}(1+m/\gamma)Z\rceil.
 \tag{7}
\]

The cached schedules need the following sufficient numbers of activation
value calls at that precision:

- Initialization: \(n\beta^{201L}(m+d+2)(1+m/\gamma)^2Z^{5/2}\).
- All training: \(\beta^{402L}(m+d+2)^2(1+m/\gamma)^4Z^5\).
- One query: \((L+1)[n+\beta^{402L}(m+d+2)^2(1+m/\gamma)^4Z^5]\).

Multiply each count by the actual evaluator work. Add one live evaluator
workspace to phase peak memory and its retained code to model size. The
older larger value-call envelopes also remain valid; the improved ones
follow from evaluating each finite source or selected-row field only
once when created. The query bound uses
\(JsR\le C(d+1)n/R\le Cn\), not a unit-cost Gaussian integral.
Coefficient arithmetic remains in the main table.

The certified tanh implementation costs \(O(b^3)\) work and
\(O(b)\) scratch per call, and these products fit all three displayed
phase bounds. Bare analyticity alone does not give a computational-cost
bound from \(\beta\): even the description or evaluation of an allowed
activation need not have any such polynomial bound.

Obtaining the \(m(d+1)\) normalized training coordinates and labels
to precision \(b\) is separately charged; their resulting finite table
fits (2). Raw absolute-precision labels require

\[
 b+\lceil\log_2(16\sqrt m)\rceil
   +\lceil\log_2\max(1,1/Y)\rceil
 \tag{8}
\]

fractional bits. Retain the actual output-scale encoding for \(Y\).
Charge original retained data descriptions, query/time acquisition,
certificate production/verification and output writing, with their actual
work and scratch. Supplied gap/activation certificates are not obtained
by free quadrature or optimization. These are explicit unresolved input
interfaces, not constants in the table.

## Width and accuracy qualifications

Keep the original scientific thresholds. Additional explicit gates are

\[
 n\ge d,\qquad nY\ge1,\qquad
 n\ge\max\{1,e^{-1}\sqrt{1+66\beta^{100L}m/\gamma}\}.
 \tag{9}
\]

One sufficient sampling gate, with a large absolute constant, is

\[
 n\ge \frac{C}{\delta}\,
 \beta^{512L}(m+d+2)^2(1+m/\gamma)^5Z^6.                \tag{10}
\]

It follows from the complete-pair certificate
\(K_+=\max\{1,P\log(1+B_F^2/\eta^2)/(2\alpha)\}\),
\(P\asymp R^2\), \(\alpha=c\delta\), and
\(K_+\le\widehat K\le2K_+\), with
\(n\ge512\widehat K\). This gate has polynomial-times-logarithm
dependence; it is not the complete scientific success threshold.

In addition, the actual passive remainder remains
\(CY\mathcal P\sqrt{(R+1)(K_++1)/n}+CYn^{-10}\), with the
fixed-depth amplification specified in FAST_FINITE_PASSIVE.md. Its
absorption into the original dense-pair certificate remains an eventual
fixed-problem comparison. The [dependency audit](HIDDEN_DEPENDENCY_AUDIT.md)
identifies the exact comparison and its possible exponential-width onset.
Neither the original scientific threshold nor this absorption onset is
proved polynomial in all problem parameters. The table therefore does
**not** establish absence of exponential dependence everywhere in an
end-to-end theorem. It establishes polynomial internal costs at a width
where the inherited accuracy theorem applies.

## Status and remaining targets

The resource refinement is a proof/accounting change, not a new guarantee
of logarithmic-work querying. Query work still has a factor \(n\),
retained bits still have logarithmic power six, and several data/gap
degrees remain large. The [memory-route analysis](MEMORY_POWER_REFINEMENT.md)
shows why lossless re-encoding of selected original packets cannot by
itself achieve the desired power reduction; it does not prove a lower
bound against different sufficient-summary representations. Its separate
noise-mark coarsening is not needed for this table.

The research, rigorous-proof and canonical-notation workflows separated
the improved resource assembly from unresolved width, activation-interface
and faster-decoder questions. The earlier model and scientific guarantees
are not silently strengthened by these scheduling refinements.

The checks reconstructed the original synthesis hash
`827f9ba57d875d80852789a6e48e645701196fb03eaaa5655f9d040e58d7abc9`.
Afterward only the status/check links, this provenance, and the above
cubic norm/projection clarification were added. Displayed resource,
precision, sampling and scientific qualifications are unchanged.
