# A readable explicit corollary

The dense and Legendre coefficient envelopes and compact comparison width
threshold below are superseded by
[SAMPLE_POLYNOMIAL_STATEMENT.md](SAMPLE_POLYNOMIAL_STATEMENT.md).
That refinement preserves the setup and label range, keeps actual Y
explicit, and removes sample/gap dependence from the dense and Legendre
exponential width factors. This earlier corollary remains valid as a
record of the looser estimates.

2026-10-04. This is a conservative numerical corollary of the merged
results, produced at the user's request to remove the long constant
recurrences from the theorem statement. It preserves the activation,
architecture, data, norm, and time scope, and the asymptotic width and
storage rates. It does not claim equivalence to the sharper numerical
label allowances and coefficients in RESULT.md. The source probability
threshold is still eventual, not effective. These are internal research
calculations, not promotion reviews.

## Setup

Use the canonical Gaussian, zero-readout, mean-square gradient flow of
RESULT.md, with L>=2 hidden layers, all of width n, m fixed sphere inputs
of norm sqrt(d), arbitrary fixed real labels, and block mobilities
(n,1,...,1,n). Activations may differ across layers, are real on the real
axis, holomorphic on |Im z|<a, and have bounded derivative on that strip.
Their values need not be bounded. Define

\[
Y=\|y\|_2/\sqrt m,\qquad
\gamma=\lambda_{\min}(Q^{(L)})>0,
\]

where the initialized covariance starts at Q^(0)_ab=x_a^T x_b/d
and is iterated through the layerwise Gaussian activation covariance.
There is no 1/m in gamma. Define just two envelope coefficients:

\[
\beta=\max\left\{10,\ 1+\max_\ell|\phi_\ell(0)|,
\frac{16}{a},\
\max_{\ell,\,j=1,2}\sup_{|\operatorname{Im}z|\le a/2}
|\phi_\ell^{(j)}(z)|\right\},\qquad
B=\beta^{100L}(1+m/\gamma)^4.
\]

All comparisons use
\[
\|f-g\|_*=
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}|f(t,x)-g(t,x)|.
\]

The common sufficient label condition is
\[
0<Y\le\frac{\gamma}{m}\beta^{-30L}.
\tag{1}
\]
Zero labels give the exact zero predictor separately. At fixed confidence
1-delta, let N_0(delta) denote a sufficient width for the initialization,
source probability, and eventual construction requirements. All fixed
problem parameters are suppressed in this notation. Such a finite
threshold exists for every fixed delta in (0,1), but no numerical formula
for it has been proved. The statements require n>=N_0(delta), not just
the delta-independent deterministic threshold displayed below. This is
one probability assertion per width, not an event simultaneous over
infinitely many independent widths.

## Independent dense copies

\[
\|f_n-\widetilde f_n\|_*
\le BY\exp\left\{B\frac{Ym}{\gamma}\sqrt{\log(en)}\right\}
\sqrt{\frac{\log\left(8(n+1)(1+2n)^d/\delta\right)}n}.
\tag{2}
\]
Each model has (L-1)n^2+n(d+1) trainable coordinates, excluding the
common data. This is n^(-1/2+o(1)), not strict root width.

The Y-prefactor is obtained by integrating the readout difference, whose
initial value is zero, before applying the existing whole-sphere Gaussian
extension argument. It does not require a new stochastic sensitivity
estimate. The complete finite-envelope calculation is in
[SIMPLE_CONSTANTS_DENSE_CHECK.md](SIMPLE_CONSTANTS_DENSE_CHECK.md).

## Original-clock Legendre closure

Take the same initial Gaussian arrays, original residual-RMS clock and
moment prefixes, and order
\[
q_n=\left\lceil n^{1/4}\exp\{B\sqrt{\log(en)}\}\right\rceil.
\tag{3}
\]
Then
\[
\|f_{n,q_n}-f_n\|_*\le Y/\sqrt n.
\tag{4}
\]
Explicitly, for every fixed 0<delta<1 and every n>=N_0(delta), (4)
and the following state-count conclusion hold with probability at least
1-delta. The coefficient B and order (3) do not depend on delta.
The moving-state count is exactly
\[
n(d+1)+1+2(L-1)mnq_n,
\tag{5}
\]
and fixed mixers add (L-1)n^2 coordinates. Thus q_n=n^(1/4+o(1)) and
the moving state is n^(5/4+o(1)) at fixed problem parameters.
The order and absorption calculations are in
[SIMPLE_CONSTANTS_LEGENDRE_CHECK.md](SIMPLE_CONSTANTS_LEGENDRE_CHECK.md).

## Compact autonomous representation

The corrected-readout autonomous model in
EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md retains no original-width arrays
or externally supplied trajectory after initialization-only preprocessing.
It uses its own residual and moving hidden arrays. It is a modified
optimizer, not ordinary gradient flow in a smaller canonical Gaussian
network. Its all-retained storage, including fixed metrics, data and
specified caches, satisfies
\[
\begin{split}
\operatorname{size}(C)\le{}&
\beta^{(64+6d)L}\frac{(d+3)^d}{(d!)^2}
\left(\frac{Ym}{\gamma}\right)^4
[\log(en)]^{3d+2}\\
&+2040(L+1)(2m+d+1)^2+10m(d+1).
\end{split}
\tag{6}
\]
Include the confidence-dependent source width in the threshold:
\[
n\ge\max\left\{N_0(\delta),\ e^{64B^2},\ (4B/Y)^4\right\}.
\tag{7}
\]
Then
\[
\|f_C-f_n\|_*\le Y/\sqrt n.
\tag{8}
\]
The error bound (8) and the storage bound (6) hold together with
probability at least 1-delta. The previously displayed numerical terms
in (7) alone do not certify any specified confidence.
The all-retained size is O(log^(3d+2)n) at fixed problem parameters.
The numerical coefficients and width threshold can be enormous; these
are asymptotic storage conclusions, not practical runtime or precision
claims. Preprocessing work and exact-real bit precision are outside the
retained-coordinate count.

The activation/source and storage envelope is checked in
[SIMPLE_CONSTANTS_SOURCE_CHECK.md](SIMPLE_CONSTANTS_SOURCE_CHECK.md).

## How the common label and compact threshold are certified

The source envelope proves S_*^src>=beta^(-26L). Since L>=2 and
beta>=10, condition (1) gives 16Ym/gamma<=beta^(-26L).
The dense and closure fitting caps already follow from beta^(-5L)
and beta^(-10L), respectively.

For the runtime fitting cap, its forward constants satisfy
H_c<=(20 beta)^L<=beta^(5L/2). Its exact recurrence solves to
\[
F_c=4s^2(18s)^{2L-2}
+16H_c^2s^2\sum_{j=0}^{L-2}(18s)^{2j}.
\]
For s>=1 and H_c>=1 this is at most
5H_c^2 s^2(18s)^(2L-2). Thus
\[
16H_c\sqrt{F_c}\le2H_c^2(18s)^L\le\beta^{8L}.
\]
This verifies the runtime label cap without any new assumption.

For the compact error, the source comparison coefficients are bounded
by B; see the source check. Its already proved order inversion (53),
with prescribed coefficient P=Y, requires only
\[
n\ge\max\{e^{\max(8a_0,64b_0^2,2)},
(2e^{1/4}C_{\rm out}/Y)^4,
(2C_{\rm tail}/Y)^{2/15}\}.
\]
The bounds a_0,b_0,C_out,C_tail<=B, B>=1, and 0<Y<1 make (7)
sufficient. The latter label bound follows from
gamma/m<=H^2<=beta^(3L) and (1).

## Exact remaining limitations

The general strict-root independent-dense comparison is still open.
The source confidence-dependent sufficient width remains unquantified.
The constants here are rigorous conservative envelopes and do not replace
the sharper recurrence formulas as numerically optimal values. The onset
derivative calibration still gives no universal lower bound in the full
prediction norm or at the fitted endpoint. Hence matching compression
to dense-copy variability remains an upper-bound calibration.

## Confidence audit

The source proof constructs one good event at each width, independent
of the requested confidence, whose probability tends to one. Its
deterministic consequences include the Legendre order/error statement
and the compact rank, storage, and error statements. The constructed
models and their sizes do not depend on the proof's moment order.

Specifically, source equation (29), with its budget equal to
1024 exp(2) L, gives for every fixed positive integer p
\[
\limsup_{n\to\infty}\Pr\{\text{a source budget fails}\}
\le mL(64e^2)^{-p}.
\]
Choose p at least ceil(log(4mL/delta)/log(64e^2)), then increase width
until the fixed-p remainders and the other vanishing failure probabilities
are sufficiently small. This proves existence of N_0(delta), but the
proof does not quantify those remainders. Increasing confidence therefore
changes the required width, not the displayed error or storage formula
at a fixed width. No fixed-width arbitrary-confidence guarantee, or
numerical guarantee for delta=delta_n tending to zero, is asserted.

This audit checks probability quantifiers; it adds no confidence rate.
Simply replacing log(en) by log(en/delta) would not supply the missing
finite-width control of the source remainders.

## Coordinator check record

The coordinator read all three complete SIMPLE_CONSTANTS_*_CHECK.md
derivations after their completion. The source recurrence was checked
term by term, including the borderline L=2, beta=10 coefficient
absorptions, the source-smallness minimum, both dimension branches in
the storage count, and the compact comparison threshold. The dense
readout refinement, residual damping, Gaussian extension, confidence
allocation and endpoint-net remainder were reconstructed. The Legendre
absorption and order inversion were checked against the original
EXPLICIT_LEGENDRE_COMPARISON.md formula. The source-envelope dependencies
listed as pending in the scoped dense and Legendre reports are discharged
by SIMPLE_CONSTANTS_SOURCE_CHECK.md and this coordinator check.

Outcome: the displayed conservative corollary is internally checked,
subject to the same established-in-study source interfaces and eventual
probability threshold as the full merged theorem. No numerical experiment
or new probabilistic theorem was used, and this is not a promotion review.
