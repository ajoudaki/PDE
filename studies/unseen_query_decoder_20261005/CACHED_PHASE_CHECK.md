# Check of cached-history scheduling and the combined phase table

2026-10-06. Independent bounded reconstruction of the assigned resource
assembly. This is conditional accounting, not promotion or an independent
proof of the underlying scientific approximation theorem.

## Verdict and boundary

**Conditional PASS for the combined table in `EXPLICIT_PHASE_COSTS.md`.**
Immutable selected-row values, their metric images, and completed-call
affine coefficients can be retained with the claimed memory and work.
The query needs only its current passive-layer systems, rather than all
historical conditioning solves. The displayed initialization, training,
query, memory, evaluator, and tanh envelopes cover the resulting costs.

Two qualifications must accompany that verdict:

1. The smaller word length and the confidence/generator interfaces in
   `PRECISION_CONFIDENCE_SEPARATION.md` are assumed here. Their numerical
   justification is assigned to a separate check. The physical/source,
   passive, statistical, and evaluator interfaces remain conditional inputs.
2. Quadratic work for constructing scalar rank weights does not imply
   quadratic work for every rank-list norm or projection. Ordinary matrix
   norm/projection preparation can require cubic work. Charging
   \(C Q R^3p^2\) for these operations leaves the combined table unchanged,
   because its matrix-preparation allowance already dominates this term.

The sharper per-layer inventory and the resulting fully separated table
in `PARAMETER_FACTOR_REFINEMENT.md`, (6), (8), and (21), are outside this
verdict. I use only the supplied coarse history dimension \(r\le CR\).
The modular query formula (16) in that note also needs an explicit median
sorting term when \(J\) is left arbitrary; the combined table supplies and
dominates that term after its stated substitution.

## Frozen inputs and method

The following ten scientific files were read completely. Their hashes were
checked again after the reconstruction. All paths below are relative to
`studies/unseen_query_decoder_20261005/`.

| File | SHA-256 |
|---|---|
| `PARAMETER_FACTOR_REFINEMENT.md` | `2defdb1cdae71355a80498ff4ab03a6ec9623669c907c37855b05e3c2346b8e1` |
| `EXPLICIT_PHASE_COSTS.md` | `827f9ba57d875d80852789a6e48e645701196fb03eaaa5655f9d040e58d7abc9` |
| `PRECISION_CONFIDENCE_SEPARATION.md` | `bcbc6d72ddc94b33d2b3a51cad9e1c721b9bbc8b708ad221481bc10836325596` |
| `FAST_LOCAL_COMPOSITION.md` | `7d101fd08dd5e612963263bb5dd565b146d4ca3b330adb074bd5673b77f40bb2` |
| `FAST_FINITE_SOURCE_BRIDGE.md` | `7ef69972a213fb26b77cd1c0ed4dcbd8b7d12f9e3b06906f351f7443f79894e6` |
| `FAST_FINITE_PASSIVE.md` | `7f298bc637afffc207375692ee725290e752cdeb818b42f82563646f74416777` |
| `FAST_TAYLOR_NOISE.md` | `71c67ce4de343077f3795aa9a9892052560da7b7ab51a59f6609027744c8881c` |
| `SANE_DECODER_CORE.md` | `701de0d9ed9a429e6f9d771a9e4a96854872c9600509866a617da70690139fa4` |
| `SANE_METRIC_PACKETS.md` | `1683563689c824593613cb636590ae3180f4cc897913c8ed5acb3c12170adeea` |
| `FAST_TANH_EVALUATION.md` | `55f4128718603b64371fc0f6e74968cc992aa01b181c958044f668a6a1a3e618` |

No linked scientific source outside this list, study history, prior review,
other study, web source, or experiment was used. Only this report was written.
The research/adversarial, rigorous-proof, canonical-notation, and neural
notation instructions were read and applied. This check reconstructed
identities and operation counts; it did not execute an implementation.

## Setup used by the count

Let \(n\) be width, \(m\ge d\ge1\) the training sample count and input
dimension, \(L\ge2\) depth, \(\gamma>0\) the population Gram gap, and
\(\beta\ge10\) the supplied analytic envelope. Write

\[
 G=1+m/\gamma,\qquad M=m+d+2,
 \qquad
 Z=\log(en)+\log\!\left(e+\frac{M\beta^{100L}G}{\delta}\right).
\]

The nonzero-label branch retains all inherited label conditions; the zero
branch remains the exact zero predictor. Let \(R\ge2\) be comparable to
the actual named-field count, including the constant and the \(d\) initial
roots; let \(p\) be the constructive sufficient word length. The interfaces
used here are

\[
 R\le C\beta^{201L}MG^2Z^{5/2},\qquad
 p\le C\beta^{110L}GZ,\qquad d+1\le CR,
\]
\[
 P\asymp R^2,\quad q,D\le CR,\quad Q\le C(L+1),\quad
 J\le C(d+1)p,\quad A\le CRp,\quad E\le Cp.
\]

Here \(P\) counts actual pair acquisitions, \(q\) selected packets,
\(D\) packet coordinates, \(Q\) passive stages, \(J\) median blocks,
and \(A,E\) the block-generator parameter and level count. Logarithms of
all array dimensions and integer ranges fit \(Cp\). No relation between
the actual values of \(R\) and \(p\) is obtained by comparing their
upper envelopes.

## Exact caching and active scratch

The finite-source chronology fixes a named field's creation-time scalar
arguments. Later acquisitions therefore cannot change its finite row
values. At its creation, evaluate the new part of its row program on all
selected packets and retain \(v(I)\in\mathbb R^q\). The chronological
interpreter need not reevaluate old fields at each pair request.

The row-arithmetic interface in `SANE_DECODER_CORE.md` (14), together with
the Taylor interpolation count (40), gives \(CR^2\) scalar operations per
complete packet. Incremental evaluation on \(q\) selected packets costs
\(CqR^2p^2\le CR^3p^2\), besides evaluator calls.

The scratch argument needs all active centers, not just one interpolation.
With \(H\) Taylor patches and degree \(K\), interpolation and successive
power coefficients require \(CmLK^2\) scalar scratch per active row.
`FAST_TAYLOR_NOISE.md` proves \(K\le CH\), while the actual named-field
certificate covers \(mLHK\). Thus

\[
 mLK^2\le CmLHK\le CR.
\]

Discard a completed patch's interpolation scratch after retaining its named
outputs. Across all selected packets, active scratch and the old field-value
array each use at most \(CqRp\le CR^2p\) bits. Fresh prior-packet
interpretation at a query uses the same chronology and scratch release.

Let \(\widehat M\) be the fixed finite selected-coordinate metric. Cache

\[
 w_v=\widehat Mv(I).
\]

Form this product exactly on its dyadic grid. Then every requested pair
can be computed as the exact dot product \(u(I)^T w_v\). The equality
to \(u(I)^T\widehat Mv(I)\) is an algebraic reassociation before the
prescribed scalar rounding. Multiplication and summation use only a fixed
multiple of \(p\) bits: each such expression has bounded product depth,
and its \(\log q\) accumulation allowance is already included. In
particular the cached images must not be prematurely rounded back to the
original field grid.

There are \(O(R)\) images and \(P\asymp R^2\) pair requests. The work is

\[
 C(q^2R+qP)p^2\le CR^3p^2,
\]

and image storage is another \(CqRp\le CR^2p\) bits. This reproduces
the same rounded metric acquisition tape exactly. Equality with the virtual
source tape still relies on the supplied metric-replay event; finite metric
rounding is not made exact by caching.

Mandatory innovation contractions remain inside their completed call with
frozen coefficient arrays. Additional complete-table pairs are acquired
only at the stated completed-call boundaries. The cache changes neither
the pair schedule nor scalar marks, so it needs no additional rounding-
boundary probability estimate.

## Historical affine coefficients and the current query

The actual finite source call has the form

\[
 \widehat y=Q_{h_y}(\widetilde m+U\widetilde T\widehat t+c\widehat g).
\]

The mean is an affine combination of old named fields, \(\widetilde T\)
and \(c\) are rounded once before the innovation acquisition, and
\(\widehat t\) is the resulting finite scalar vector. After that vector
has been acquired, retain the mean's coefficient vector, the exact vector
\(\widetilde T\widehat t\), and \(c\). Their bounded-depth exact dyadic
arithmetic costs \(O(p)\) bits per coefficient. At a new packet this is
the identical affine argument to the same final rounding operation.

There are \(O(R)\) completed calls and at most \(CR\) coefficients per
call, hence \(CR^2p\) retained bits. The representation keeps references
to named parent fields; it does not expand every field into a formula in
the original Gaussian roots. Row-dependent activation centers, polynomial
samples, products, and rounded gates are still evaluated on each new packet.

Every retained historical coefficient is a deterministic function of the
already acquired scalar prefix. Source initialization may compute a full
virtual tape for metric construction, but its future scalar answers and
future completed-call coefficient vectors must be discarded. Compact
training repopulates the cache as its own prefix advances. Private selected
packets/metric and pre-generated scalar noise marks retain exactly their
existing roles; none is added to the passive posterior's conditioning data.
Thus this is neither stored future-answer playback nor scalar training replay.

For each current passive layer, `FAST_FINITE_PASSIVE.md` (11)--(20) uses
a bounded number of posterior mean/Sylvester maps, common-Gram functions,
variance matrices, and whitening maps on histories of dimension at most
\(CR\). These are functions of the retained pair table, current time,
and the held-fixed incoming passive context. The small-matrix interface
therefore charges

\[
 C Q(R^4p^2+R^3p^3)
\]

for new systems. The historical cache removes the former \(R\) factor
counting old systems. One stage's matrices and block vectors suffice;
after its medians are complete, retain its outgoing moment vector and
discard its matrices before preparing the next stage.

### Rank weights and projections require distinct counts

The source has \(O(mLHK^2)\) scalar rank weights. At a within-patch time,
even separately evaluating a degree-\(K\) scalar polynomial for every
weight costs at most \(CmLHK^3\) scalar operations. The Taylor count (40)
gives \(mLHK^3\le CR^2\). This supplies the conservative
\(CR^2p^2\) scalar-weight construction allowance without the sharpened
per-layer history inventory. Completed patch coefficients and frozen
training projections are already present in the acquired prefix.

A general current matrix-norm projection does not follow from that count.
For example, write a current learned matrix as
\(D=TAS^T/n\), where columns of \(T,S\) are named fields, and define
\(G_T=T^TT/n\), \(G_S=S^TS/n\). Its Frobenius norm obeys

\[
 \|D\|_F^2=\operatorname{tr}(A^TG_T A G_S).
\]

Evaluating this contraction by ordinary small-matrix products takes
\(O(R^3)\) scalar operations in general. A bounded number of such
norm/projection operations per passive layer, with the supplied finite
local error budgets and positive floors, costs \(CQR^3p^2\), with
\(CR^2p\) scratch. It is contained in the matrix-preparation term above.
This gives a complete allowance without asserting an unproved quadratic
algorithm for every projection. Spectral projections are already charged
to the small-matrix routine. Old finite row operations and their rounding
conventions are not replaced by a newly rounded reassociation.

## Modular resource reconstruction

The unchanged exact metric construction and source implementation give

\[
\begin{aligned}
 W_{\rm init}\le C\{&nR^5p^3+(nR+R^2)p^4
                      +R^5p^2+R^4p^3+nR^2p^2\},\\
 W_{\rm train}\le C\{&R^5p^2+R^4p^3+R^3p^2\}.
\end{aligned}
\]

The last training term includes the new field/image/pair caches. These
coarse bounds suffice; no improved per-layer factor is needed.

Keeping the median count explicit, a complete query allowance is

\[
\begin{aligned}
 W_{\rm query}\le C\{&QJs(Rp^4+R^2p^2+A^2E)
                   +Q(R^4p^2+R^3p^3)\\
                   &+QR^3p^2+R^2p^2
                   +QRJ\log(J+1)p\}.
\end{aligned}
\]

The last term counts comparison sorting of the \(J\) block means for
every coordinate at every stage. It is absent from the factor note's
fully modular (16), so that formula should not be used for arbitrary
\(J\) without this addition. Under the combined choices,

\[
 RJ\log(J+1)p\le C(d+1)Rp^3\le CR^2p^3\le CR^3p^3.
\]

The original two-sided information certificate and sampling gate give

\[
 K_*\asymp R^2p/\alpha,\qquad
 K_*\le\widehat K\le2K_*,\qquad
 s=\lfloor n/(128\widehat K)\rfloor,
 \qquad n\ge512\widehat K.
\]

Thus \(s\le Cn/(R^2p)\). Substituting the stated \(J,A,E\) bounds
and absorbing the cubic projection/sorting terms yields exactly the
combined query allowance

\[
 C(L+1)\{(d+1)n(p^4/R+p^3)+R^4p^2+R^3p^3\}+CR^2p^2.
\]

There is no assumption \(p\le R\). The cancellation uses the actual
complete pair count and preserves its statistical price.

Historical coefficients, selected packets, metric, scalar marks/history,
field/image caches, active interpolation scratch, and current small matrices
use \(CR^2p\) bits. All independent stage seeds use \(CQAE\) bits.
One stage's retained block vectors use \(CRJp\) bits. Consequently

\[
 S_{\rm model},S_{\rm train/query}
       \le C\{R^2p+(L+d+2)Rp^2\}.
\]

Initialization additionally has the full finite packet/field array and
expanded exact-integer metric scratch, giving \(C(nRp+R^3p)\) bits.
The retained seed and coefficient arrays also remain charged. Median
arrays need not be allocated until a query occurs.

## Explicit substitutions and evaluator charges

For a monomial in the following table, the four entries denote its powers
of \(\beta^L,M,G,Z\), before rounding the final envelope upward. A
factor \(Q\le C\beta^L\) is included where shown; factors \(n\) are
listed separately in the term name.

| Term | Powers of \(\beta^L,M,G,Z\) |
|---|---|
| \(R^2p\) | \((512,2,5,6)\) |
| \((L+1)Rp^2\) | \((422,1,4,9/2)\) |
| \((d+1)Rp^2\) | bounded by \((421,2,4,9/2)\) |
| \(nR^5p^3\) | \((1335,5,13,31/2)\) |
| \(nRp^4\) | \((641,1,6,13/2)\) |
| \(R^2p^4\) | \((842,2,8,9)\) |
| \(R^5p^2\) | \((1225,5,12,29/2)\) |
| \(R^4p^3\) | \((1134,4,11,13)\) |
| \(nR^2p^2\) | \((622,2,6,7)\) |
| \(R^3p^2\) | \((823,3,8,19/2)\) |
| \(QR^4p^2\) | \((1025,4,10,12)\) |
| \(QR^3p^3\) | \((934,3,9,21/2)\) |
| \(nRp\) | \((311,1,3,7/2)\) |
| \(R^3p\) | \((713,3,7,17/2)\) |

Since \(n,M,G,Z\ge1\), these separately substituted terms are dominated
by the displayed phase table. In particular Gaussian terms are not
discarded using an unsupported inequality between \(R\) and \(p\).
The stream uses \(R\ge1\), giving
\(Cn\beta^{441L}(d+1)G^4Z^4\), covered by exponent \(450L\).
The added cubic projection term is smaller than \(QR^4p^2\). The
numerical-word envelope (3) follows from \(R^2+(L+d+2)Rp\), whose
terms fit \(C\beta^{410L}M^2G^4Z^5\); it is not a bit count.

The real-value interpolation construction uses at most
\(2nmLH(J_{\rm act}+1)\le CnR\) evaluator calls, where
\(J_{\rm act}\le CK\) is distinct from the median count \(J\).
Incremental selected-row evaluation therefore uses \(CqR\le CR^2\)
calls over all compact training. A query retains the safe allowance
\(CQ(JsR+R^2)\). Here

\[
 JsR\le C(d+1)n/R\le Cn,
\]

so the three call envelopes in the combined table are valid. They are
actual calls at the stated range/precision, not free analytic primitives.

The supplied tanh algorithm uses \(O(p)\) Taylor terms with
\(p+O(\log(p+2))\) guard bits, a bounded-denominator final division,
and \(O(\log(p+2))\) squarings. Schoolbook operations give
\(O(p^3)\) work and \(O(p)\) live scratch. Its integer saturation
cutoff controls large arguments; the logarithmic guard covers the
polynomial summation and squaring error. Input acquisition remains
separate. The resulting added work is bounded by

\[
 CnRp^3,\qquad CR^2p^3,\qquad CQ(n+R^2)p^3,
\]

respectively. Initialization is dominated by \(nR^5p^3\); training by
\(R^4p^3\); query by its stream and \(QR^3p^3\) preparation.
Thus no displayed phase exponent needs increasing for tanh.

Actual general-activation evaluator work and one live workspace, original
data/code/certificate descriptions, label normalization, output scale,
query/time acquisition, and output writing remain explicit additions.
The finite \(m(d+1)\) normalized training values fit \(CR^2p\), since
the actual source includes the training fields and input roots. Tiny-label
input precision is still charged separately.

## Scientific limits of the verdict

The caching schedule does not alter the sampler, block length, pair count,
prior, or rounded row functions. Conditional on the supplied interfaces,
the whole-sphere/all-time independent-reference guarantee is therefore
unchanged, including the endpoint and the larger implemented remainder

\[
 CY\mathcal P\sqrt{(R+1)(K_*+1)/n}+CYn^{-10}.
\]

The sampling gate and all inherited scientific/label gates remain required.
Substitution gives the stated sufficient sampling allowance of order
\(\delta^{-1}\beta^{512L}M^2G^5Z^6\); it does not make the complete
scientific threshold or the certificate-absorption onset polynomial in all
problem parameters. This report does not independently establish those
statistical interfaces, the sharpened per-layer inventory, a smaller bit-
memory logarithmic power, or a query bound without its factor \(n\).
