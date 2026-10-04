# Reusing the general near-quarter Legendre theorem

2026-10-04. Coordinator. This note is an elementary consequence of the
user-authorized, internally checked DEPTH_EXTENSION_RESULT.md in
studies/dense_cutoff_population_rate_20261001. It does not claim new
numerical values for that source's label threshold or physical constants.

## Unchanged source theorem

Fix finite data, sphere dimension and hidden depth L≥2. Use canonical
Gaussian initialization, zero initial readout, mean squared loss, and
mobilities (n,1,...,1,n). Assume the compatible initialized Gram gap is
positive and the fixed label RMS is below the source's small threshold.
Every activation is C³ with globally bounded first three derivatives;
activation values may be unbounded. Dense and the original residual-RMS
Legendre closure share initialization. Both exist, fit and converge.

The inherited simultaneous-in-q estimate controls the normalized physical
parameter distance, and hence the all-time whole-sphere prediction norm,
by

\[
 C\exp(K\sqrt{\log(e+n)})\,
       q^{-2}\sqrt{\log(e+q)}.                         \tag{1}
\]

Here C,K are fixed problem constants, independent of n,q,t. At fixed
confidence the good event holds at every sufficiently large n. This is
the later same-width study theorem, stronger in this respect than the
current manuscript's estimate with its separate width remainder.
No population comparison or width-bias term is used in (1).

The paper's original memories and normalization remain

\[
 \dot\tau=\widehat\rho,\quad\tau(0)=1,\qquad
 \widehat W^{(\ell)}=W_0^{(\ell)}-
 \frac2{mn\tau}\sum_{a=1}^m\sum_{j=0}^{q-1}(2j+1)
       \bar\delta_{a,j}^{(\ell)}\bar h_{a,j}^{(\ell-1)\top}.
\]

The zeroth forward memory starts at the initialized feature; the other
forward memories and every backward memory start at zero. Each closure
uses its own residual, states and clock. There is no learned dense hidden
matrix in its stored state.

## An explicit schedule without an unknown coefficient in q

Set s=log(e+n) and

\[
 q_n=\left\lceil n^{1/4}e^{s^{3/4}}\right\rceil.
 \tag{2}
\]

Since q_n≤2 n^(1/4)e^(s^(3/4)) and s≥1,

\[
 \log(e+q_n)\le\log(e+2)+s/4+s^{3/4}\le4s.
\]

Consequently (1) at q_n is at most

\[
 \frac C{\sqrt n}\,2\sqrt s
       \exp(K\sqrt s-2s^{3/4}).                       \tag{3}
\]

If s≥max(1,K⁴), then K sqrt(s)≤s^(3/4), and
2 sqrt(s)exp(−s^(3/4))≤2/e<1. The last inequality follows because
the logarithmic derivative 1/(2s)−(3/4)s^(−1/4) is negative for s≥1.
Thus (3) is at most C/sqrt(n). The function
q↦q^(−2)sqrt(log(e+q)) is decreasing for q≥1, by direct
differentiation, so the same event and constant control every q≥q_n.

This is a strict root-width consequence with a completely specified
order schedule. The extra explicit sufficient-width condition is
log(e+n)≥K⁴; the inherited probability threshold and the numerical
values of C,K,Y* remain to be quantified. The schedule is conservative
and keeps q_n=n^(1/4+o(1))=o(n).

## State and accuracy arithmetic

The moving state has exactly

\[
 2(L-1)mnq_n+n(d+1)+1
\]

real coordinates, including the clock. Fixed Gaussian hidden mixers add
(L−1)n². For fixed data/depth and a strict target C/sqrt(n)≤epsilon,
n is of order epsilon^(−2), moving Legendre storage is
epsilon^(−5/2+o(1)), and total storage including mixers is
epsilon^(−4). These are sufficient representation costs, not a
lower bound for every alternative autonomous encoding.

The special two-tanh q=n^(1/6+o(1)) result in this study's RESULT.md
remains valid in its scope but is not required or generalized here.
