# A fixed-confidence lower bound for the actual trained predictor

2026-10-04. Coordinator. This combines two separately derived inputs in
this study: INTEGRATED_DENSE_LOWER_ROUTE.md (full nonlinear remainder)
and INTEGRATED_INITIAL_VARIABILITY.md (initialized finite-depth CLT).
Their complete proofs and check reports remain the dependencies. No
experiment, clipped algorithm or frozen-feature comparison is introduced.

## Statement

Use two tanh hidden layers of width n, canonical independent Gaussian
initialization, zero readout and mean-loss mobilities (n,1,n). Fix m≥1,
d≥m+1, training inputs x_a=sqrt(d)e_a, and arbitrary deterministic
labels y with

\[
 0<Y=\|y\|_2/\sqrt m\le1/m.
\]

The query is x_*=sqrt(d)e_{m+1}. Let f_n and tilde f_n be independent
actual dense runs. Define explicit activation moments

\[
 Q=\mathbb E\tanh^2 Z,\quad
 q=\mathbb E\tanh^2(\sqrt Q Z),\quad Z\sim N(0,1).
\]

Here the limiting top training Gram is q I, so the user's unnormalized
gap is gamma=q. For every fixed 0<delta<1 and all sufficiently large n,

\[
 \Pr\left\{
  |f_n(t_\delta,x_*)-\widetilde f_n(t_\delta,x_*)|
  \ge \frac{q^2\delta^{5/2}}{112000}
          \frac{\sqrt m\,Y}{\sqrt n}
 \right\}\ge1-\delta,
\qquad
 t_\delta=\frac{m q\delta^{3/2}}{56000}.
 \tag{1}
\]

The same lower bound holds for the supremum over all physical time and
the whole input sphere. The coefficient is fully explicit and independent
of width, time, m and d except for the displayed factors. The sufficient
width is not quantified here: the proof uses a fixed-dimensional CLT,
so m,d,delta and the labels are fixed before n grows. This is different
from the earlier small-probability theorem's explicit growing-m region.

The proof gives a conservative delta^(5/2) coefficient, not a claim of
sharp confidence dependence. The m and n powers are established for
the stated family. It is not an endpoint lower bound for general m.

## Proof with all probability losses retained

Use the training-only event T in the dense lower source, and its
independent counterpart tilde T. In its notation

\[
 K_y(g)=\frac1{mn}(H_0^{(2)}y)^\top\tanh(W_0\tanh g),
\]

where g is the untouched first-layer query column, independent of the
entire training path. The actual predictor, with t=m tau, is exactly

\[
 f_n(m\tau,x_*)=2m\tau K_y(g)+R_n(m\tau,g).
 \tag{2}
\]

For tau≤1/sqrt(1464) and mY≤1, the checked deterministic/Gaussian
remainder estimate is

\[
 \mathbb E[R_n(m\tau,g)^2\mathbf1_T]
 \le7000^2 mY^2\tau^4/n.                         \tag{3}
\]

For each training realization, the remainder is odd in its independent
Gaussian query column, so E[R_n 1_T]=0. The two-copy difference R−tilde R
on T∩tilde T therefore satisfies the sharper summed-variance bound

\[
 \mathbb E[(R-\widetilde R)^2\mathbf1_{T\cap\widetilde T}]
 =2\Pr(T)\mathbb E[R^2\mathbf1_T]
 \le2\cdot7000^2mY^2\tau^4/n.                    \tag{4}
\]

Put a2=E tanh'(sqrt(Q)Z) and nu2=q²+a2⁴Q². The initialized covariance
CLT proved in INTEGRATED_INITIAL_VARIABILITY gives

\[
 \frac{\sqrt n}{\sqrt mY}
       2m\tau(K_y-\widetilde K_y)
 \Longrightarrow N(0,8\nu_2\tau^2),\qquad \nu_2\ge q^2.
 \tag{5}
\]

This only concerns the leading term of (2); the actual nonlinear
remainder is still controlled by (4). Set tau=q delta^(3/2)/56000.
Since q<1 and delta<1, tau<1/56000<1/sqrt(1464), so (3) applies.
Let

\[
 b_n=\delta q\tau\,\sqrt mY/\sqrt n.
\]

For a standard normal N, boundedness of its density gives

\[
 \Pr\{|N|\le a\}\le\sqrt{2/\pi}\,a.
\]

The limiting probability that the leading difference has magnitude
smaller than b_n is therefore at most

\[
 \sqrt{2/\pi}\,\frac{\delta q}{\sqrt{8\nu_2}}
 \le \frac\delta{2\sqrt\pi}<\frac\delta2.
 \tag{6}
\]

The Gaussian boundary has zero probability. For the fixed tau,delta,m,y,
convergence in (5) implies that the finite-width probability is at most
delta/2 for all sufficiently large n. Also Pr((T∩tilde T)^c)≤delta/8
eventually, by the explicit training-good tail in the lower source.

On the joint good event, Markov and (4) give

\[
 \Pr\{|R-\widetilde R|\ge b_n/2, T\cap\widetilde T\}
 \le\frac{8\cdot7000^2\tau^2}{\delta^2q^2}
 =\frac\delta8.                                  \tag{7}
\]

Outside the union of these three failure events, (2) has absolute
two-copy difference at least b_n/2. Their total probability is at most
3delta/4≤delta. Substituting tau into b_n/2 gives (1).
All statements are at the same physical time; no inference about the
fitted endpoint was used. ∎

## Consequence for a calibrated dense width

For example fix delta=1/4 in (1). Then the all-time dense-copy discrepancy
is at least

\[
 \frac{q^2}{3584000}\frac{\sqrt mY}{\sqrt n}
\]

with probability at least 3/4 for sufficiently large width. Write
c_*=q²/3584000. If the dense-copy discrepancy is at most epsilon with
probability strictly greater than 1/4, these two probability statements
force n≥c_*²mY²/epsilon², in the sufficiently-wide asymptotic regime.
Indeed their events must intersect, and their simultaneous inequalities
require c_*sqrt(m)Y/sqrt(n)≤epsilon.

For comparison to a common deterministic reference function, suppose
each dense run is within epsilon of that reference in the all-time sphere
norm with probability p>1/2. Independence gives simultaneous success
probability p²>1/4, and the triangle inequality then gives dense-copy
error at most 2epsilon. The necessary width bound becomes
n≥c_*²mY²/(4epsilon²). This implication controls random variability;
it supplies neither a bound on the reference bias nor a population
convergence theorem.

In particular dense learned storage has an epsilon^(−4) necessary power
for each fixed nonzero-label task in this family, when calibrated in
either of these probability senses. This is not a lower bound for
coordinated autonomous compressors.
