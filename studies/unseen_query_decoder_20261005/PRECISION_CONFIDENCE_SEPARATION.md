# Separate arithmetic precision from whole-sphere confidence

2026-10-06. Lead-author refinement of the locally precise decoder. This
is a candidate until its complete assembly has received bounded checking.
It changes neither the source schedule nor the passive estimator. All
original scientific, label, width, evaluator and independent-reference
qualifications remain in force. No experiment or promotion is claimed.

## 1. Statement

Use the parameters and the single logarithm of
FAST_LOCAL_EFFICIENCY_RESULT.md:

\[
 Z=\log(en)+\log\!\left(e+
 \frac{(m+d+2)\beta^{100L}(1+m/\gamma)}{\delta}\right).
\]

The sufficient numerical word length can be chosen as

\[
 p\le C\beta^{110L}(1+m/\gamma)Z,                       \tag{1}
\]

without the previous factor \(d+1\). This is a constructive sufficient
choice with a large absolute multiplier, not a claim that every smaller
precision works. The omitted dimension factor is charged instead to the
external confidence budget and the number of sampling blocks:

\[
 F\le C(d+1)p,\qquad J\le C(d+1)p.                     \tag{2}
\]

Here \(F\) is the logarithm of the estimator/generator failure union,
and \(J\) is an odd sufficient block-median count. These proof-local
symbols are not additional free model parameters.

Let \(R\) remain comparable to the actual named-field count, including
the \(d\) first-layer roots and the constant. Thus \(d+1\le CR\), and

\[
 R\le C\beta^{201L}(m+d+2)(1+m/\gamma)^2Z^{5/2}.        \tag{3}
\]

Retained internal bits and peak internal bits after initialization are
bounded by

\[
 C\{R^2p+(L+d+2)Rp^2\}.                               \tag{4}
\]

In particular the common envelope improves to

\[
 C\beta^{530L}(m+d+2)^2(1+m/\gamma)^5Z^6.              \tag{5}
\]

The logarithmic power remains six in bits. This refinement does not
prove a fourth- or fifth-power bit representation.

## 2. Numerical requirements do not contain the external union

The finite source precision in FAST_FINITE_SOURCE_BRIDGE.md is
\(C[\chi+\log(1/\rho)]\), where
\(\chi=\beta^{100L}(1+m/\gamma)Z\). Its scientific failure share
\(\rho\) is a fixed share of the requested confidence, not divided by
the number of sphere/time codes. The first-layer coupling needs the
logarithm of \(\sqrt d+1\), already in \(Z\), and uses the inherited
gate \(nY\ge1\). Exact source summation adds \(\log n\).

The local metric replay in FAST_LOCAL_PRECISION_TEST.md adds logarithms
of the number of pairs, selected rows, field cap and inverse acquisition
confidence. The latter again uses a fixed confidence share. It does not
apply a union over queries. Its Gaussian scalar-boundary estimate is
uniform in the pre-noise scalar value and is summed over the actual
\(O(R^2)\) source acquisitions only.

For a passive query, FAST_FINITE_PASSIVE.md, (5) and Section 6, requires
\(C[\chi+\log\mathcal P+\log(1/\delta)]\) bits. Its amplification
\(\mathcal P\) is the displayed fixed-depth polynomial product of the
passive cap, physical posterior-mean/readout norm bound and activation
derivative bounds. Taking its logarithm costs only
\(C(L+2)\) times the logarithms of those bounds. The cap is at most
\(C\beta^{110L}\sqrt{d+1}Z^{3/2}\); the physical norm bound is
polynomial in the supplied physical constants and
\(\sqrt{(L+1)/\delta}\). These logarithms are bounded by (1), with
its explicit exponent slack. There is no factor \(d\) from summing
over inputs in this arithmetic estimate.

On each finite prior packet, all old training fields are evaluated by the
actual finite interpreter. They are not approximated by a continuous
history circuit. New whitening, mean/variance calculations, input
contractions and passive nonlinearities are local protected operations.
The passive Gaussian quadrature/sampling bias estimate in that proof is
uniform over every finite training packet and every guarded context.
It is a deterministic expectation-error bound. It therefore has no
external-code failure union. Its tail cutoff and integrand tolerance
still fit (1).

Finally FAST_PHYSICAL_QUERY_GRID.md requires base input/time precision
at most \(C\beta^{102L}(1+m/\gamma)Z\). Coordinate rounding and
normalization add \(O(\log(d+1))\) bits, not \(d\) copies of that
precision per word. The factor \(d+1\) occurs in the *number of bits
describing an entire code*, hence in the logarithm of the number of
codes. This proves the separation (1)--(2).

The tolerances must be selected before generating the source. Choose a
base \(p_0\) of the order (1) satisfying these numerical requirements.
Choose \(\eta=2^{-\lceil c p_0\rceil}\) with a sufficiently large
absolute \(c\), then the prescribed local grids, finite samplers and
metric tolerance. Finally choose \(p=C_{\rm word}p_0\) to cover all
arithmetic. No tolerance is redefined from this last \(p\). Consequently
\(\log(1/\eta)\) is comparable to \(p\), and the bounded pair-test
cap has logarithm at most \(Cp\). This repeats the noncircular order of
FAST_LOCAL_COMPOSITION.md without its external-union precision padding.

## 3. Generator, median storage and sampling count

The full-vector bad-median test stores one vector of running sums and two
vectors of counters. Its between-packet state uses \(CRp\) bits. Its
thresholds are proof advice, not a query oracle. The packet dimension is
\(D\le CR\). If \(s\) is the block length, the stream level count is

\[
 E=1+\lceil\log_2(Js+2)\rceil\le Cp.
\]

Indeed \(s\le n\), \(J\le C(d+1)p\), and \(\log n\),
\(\log(d+1)\) and \(\log(p+2)\) are covered by (1). The generator
block parameter can therefore still be chosen with

\[
 A=C(Dp+S_{\rm test}+F+E)\le CRp,
\]

using \(d+1\le CR\). Its seeds use \(C(L+1)Rp^2\) bits;
per-packet generator work is \(CR^2p^3\). This step does not hide
the larger failure union in an arithmetic word.

All \(J\) block-mean vectors use \(CRJp\le C(d+1)Rp^2\) bits.
They are discarded between passive stages. The selected packets, metric,
scalar marks/history and coefficient arrays use \(CR^2p\) bits.
Combining these actual live arrays proves (4).

Retain the complete-pair information certificate and its two-sided dyadic
rounding exactly as in FAST_LOCAL_COMPOSITION.md:

\[
 K_+=\max\{1,P\log(1+B_F^2/\eta^2)/(2\alpha)\},\quad
 K_+\le\widehat K\le2K_+,\quad
 s=\lfloor n/(128\widehat K)\rfloor,
\]

with \(P\) comparable to \(R^2\), and require
\(n\ge512\widehat K\). Then \(K_+\) is comparable to
\(R^2p/\alpha\), and \(s\le Cn/(R^2p)\). Confidence dependence
is kept in \(\alpha\); it is harmlessly discarded only in this work
upper bound. The implemented cross-moment error remains

\[
 CB_{\rm pass}\sqrt{(R+1)(\widehat K+1)/n}.
\]

Neither a smaller population-center radius nor a smaller effective
information estimate may silently replace it.

## 4. Resource substitution before any further caching improvement

The unchanged metric initialization and source routines cost

\[
 C\{nR^5p^3+(nR+R^2)p^4+R^5p^2+R^4p^3+nR^2p^2\}
\]

bit operations, and
\(C[nRp+R^3p+R^2p+(L+1)Rp^2]\) peak bits. All training
updates still fit \(C(R^5p^2+R^4p^3)\). Per-packet query work is
\(C(Rp^4+R^2p^3)\). Thus the query work is

\[
 C(L+1)\{(d+1)s(Rp^5+R^2p^4)+R^5p^2+R^4p^3\}.
\]

The stream part is at most
\(C(L+1)(d+1)n(p^4/R+p^3)\). Median sorting costs
\(CRJ\log(J+1)p\le C(d+1)Rp^3\) and is included by
the preparation envelope since \(d+1\le CR\). No assumption
\(p\le R\) is used.

Direct substitution into these formulas gives the following safe bounds,
all with only an absolute suppressed multiplier:

| Resource | Bound |
|---|---:|
| Retained bits; peak training/query bits | \(\beta^{530L}(m+d+2)^2(1+m/\gamma)^5Z^6\) |
| Initialization work | \(n\beta^{1340L}(m+d+2)^5(1+m/\gamma)^{13}Z^{31/2}\) |
| Initialization peak bits | \(\beta^{730L}[n(m+d+2)(1+m/\gamma)^3Z^{7/2}+(m+d+2)^3(1+m/\gamma)^7Z^{17/2}]\) |
| All training updates | \(\beta^{1230L}(m+d+2)^5(1+m/\gamma)^{12}Z^{29/2}\) |
| One unseen query | \(n\beta^{450L}(d+1)(1+m/\gamma)^4Z^4+\beta^{1230L}(m+d+2)^5(1+m/\gamma)^{12}Z^{29/2}\) |

For example \(R^2p\) has powers \(512L,2,5,6\) in
\(\beta,m+d+2,1+m/\gamma,Z\), while \((d+1)Rp^2\) is
covered by powers \(421L,2,4,9/2\). The main initialization term
has powers \(1335L,5,13,31/2\), and the main training term
has powers \(1225L,5,12,29/2\). The finite Gaussian terms are
substituted separately, rather than assumed dominated in \(R,p\).

The previous conservative activation/data call counts remain valid:
\(CnR^3\), \(CR^4\), and
\(C(L+1)[JsR+R^2]\le C(L+1)[n+R^2]\), respectively,
because \((d+1)/R\le C\). Evaluate at (1), charge actual evaluator
work/workspace, and retain all code/data/certificate descriptions. The
certified \(\tanh\) evaluator of FAST_TANH_EVALUATION.md costs
\(O(p^3)\) work and \(O(p)\) scratch and is covered by the displayed
phase envelopes.

## 5. What this refinement does not remove

No new statement is made about the original scientific width threshold,
the onset of absorption into the inherited dense-pair upper certificate,
or arbitrary analytic activation evaluation. In particular polynomial
operation counts do not prove a polynomial sufficient width in the data,
gap, labels or activation parameters. Keep the explicit additional
statistical error and the nonzero-label width gates of the passive proof.
This is still a width-times-polylogarithmic query, not a logarithmic-work
query, and a six-power bit model, not a four-power one.

The research/proof workflows are used to separate this local proof from
the inherited scientific interfaces. Canonical notation keeps only the
shared problem parameters in the headline table; the auxiliary symbols
above belong to the resource derivation.
