# Quantitative fitting by isotropic prediction perturbations

2026-09-19. Lead candidate. Continuation of accepted-noise investigation;
not promoted. Exact theoretical result; no experiment or discretization.

## 1. Model, scope, and algorithmic change

Use the exact physical population closure and full Hilbert state S=(w,c,M)
from ESCAPE_AND_LIMITS.md, Section 1. The activation is phi=tanh, the fixed
columns b1,b2 are bounded, the transpose and initialization correlations
are unchanged, and

\[
a_i=E_1[b_1\phi(w\cdot x_i/\sqrt2)],\quad
H_i=\phi(b_2^TMa_i),\quad f_i=E_2[cH_i],\quad
L=\sum_i\mu_i(f_i-y_i)^2.
\]

Inputs are finite circle data with binary labels y_i in {-1,1}.
Combine duplicates and antipodes, with
compatible label signs, into m representatives and positive weights
summing to one. This preserves the loss and its exact full gradient.
Below all vectors and matrices indexed by observations use these reduced
representatives. No input independence or minimum separation is assumed.

Define the current readout map and weighted Gram by

\[
(Ah)_i=\sqrt{\mu_i}E_2[hH_i],\qquad K=AA^*,\qquad
e_i=\sqrt{\mu_i}(f_i-y_i),\qquad L=|e|^2.                 \tag{1}
\]

The theorem starts from any S0 with K0 positive definite, finite physical
norm and L0>0. An exact fit is terminal. Canonical initialization satisfies
this hypothesis for EVERY compatible finite circle dataset at p=1 and p=2:
see INITIAL_EXCLUSION.md, equation (18), and INITIAL_REVIEW.md, Section 6.
The proof of that feature independence retains the actual ridge and
reverse-response correlations. No unproved landscape theorem is used.

Fix theta in (0,1), sigma>0, and the positive GF duration h selected below.
At each stage:

1. Let S be the current state and ell=L(S)>0. HOLD S FIXED during failed trials.
2. Draw independent Z~N(0,sigma^2 I_m) and propose ONLY a readout change

\[
\delta c=\sqrt{\ell}\,A^*K^{-1}Z,\qquad
S^{\rm trial}=(w,c+\delta c,M).                          \tag{2}
\]

3. Accept iff L(S^trial)<=theta ell. On acceptance run the full original
   gradient flow, in all three trainable blocks, for time h.
4. Start the next stage at that flow endpoint. Stop if exact loss zero occurs.

The map A and Gram are current-state quantities. No fitted endpoint,
future path, readout interpolant, or desired displacement -e is supplied.
The Gaussian is centered in the current feature span; its covariance is
ell sigma^2 A^*K^{-2}A. In particular this is NOT the previous fixed
full-support additive Gaussian and is NOT minibatch sampling noise.
The amplitude shrinks with residual size and is amplified in weak current
prediction directions.

Failed candidates are evaluated but do not become states. Full GF is
paused while they are rejected, just as in the previous fractional rule.
No hidden block is frozen during any GF interval. The proof deliberately
keeps the hidden representation in a region where its readout Gram remains
positive, so it is not a theorem for unrestricted large hidden excursions.

## 2. An explicit fixed GF duration suffices for all time

Let B1,B2 be essential bounds on |b1|,|b2|, and set B=B1 B2>0. Put

\[
\begin{split}
\kappa_0&=\lambda_{\min}(K_0)>0,\qquad \kappa=\kappa_0/2,\\
M_0&=\|M(S_0)\|_F,\qquad
\rho=\frac{\kappa_0}{4B\max(1,M_0)},\qquad \overline M=M_0+\rho,\\
R_*&=\frac{\sqrt{L_0}}{1-\sqrt\theta},\\
\overline C&=\|c_0\|_2+
 R_*\left(\frac{1+\sqrt\theta}{\sqrt\kappa}+2\sqrt\theta\right),\\
h&=\min\left\{1,\,
\frac{\rho}{4B\overline C(1+\overline M)\sqrt\theta R_*}\right\}>0.
\end{split}                                                     \tag{3}
\]

The M0 symbol in (3) is a scalar norm; the canonical initialized matrix
is still D. All constants in (3) are computed once from the actual
starting state and fixed data.

We prove every realized finite collection of accepted trials and flow
segments stays within

\[
\|w-w_0\|_2+\|M-M(S_0)\|_F<\rho,\qquad
K\ge\kappa I,\qquad \|c\|_2\le\overline C.                \tag{4}
\]

The proof does not assume future successful trials or future boundedness.

First, |phi|<=1 gives ||A||<=1, and for arbitrary hidden fields

\[
|a_i(w)-a_i(w_0)|\le B_1\|w-w_0\|_2,\qquad |a_i(w)|\le B_1.
\]

Using M a_i(w)-M(S0)a_i(w0)=(M-M(S0))a_i(w)+M(S0)(a_i(w)-a_i(w0))
and the Lipschitz property of phi gives

\[
\|A-A_0\|_{\rm op}
 \le B\left(\|M-M(S_0)\|_F+M_0\|w-w_0\|_2\right).
\]

Consequently

\[
\|K-K_0\|_{\rm op}\le
2B\max(1,M_0)
 \left(\|w-w_0\|_2+\|M-M(S_0)\|_F\right).               \tag{5}
\]

This depends only on the hidden fields, so a readout kick leaves K unchanged.
Equation (5) and the radius in (3) imply K>=kappa I on the hidden tube.

Next (2) gives EXACTLY, at fixed hidden fields,

\[
e^{\rm trial}=e+\sqrt{\ell}Z.                            \tag{6}
\]

At every accepted trial, |e^trial|<=sqrt(theta ell); hence
|Z|<=1+sqrt(theta). Since ||A^*K^{-1}||<=kappa^{-1/2},

\[
\|\delta c\|_2\le
\frac{1+\sqrt\theta}{\sqrt\kappa}\sqrt{\ell}.             \tag{7}
\]

Let ell_j be the loss before stage j, starting j=0. Acceptance and subsequent
energy dissipation give ell_j<=theta^j L0. Therefore
sum_j sqrt(ell_j)<=R_*. This upper bound applies to all partial histories.

On a full GF segment following stage j, L<=theta ell_j. The exact physical
velocities, from the original equations, satisfy

\[
\|\dot c\|_2\le2\sqrt L,\quad
\|\dot M\|_F\le2B\|c\|_2\sqrt L,\quad
\|\dot w\|_2\le2B\|M\|_F\|c\|_2\sqrt L.                \tag{8}
\]

Equations (7)--(8), h<=1, and the geometric sum give the readout bound
in (4) up to any first exit from the hidden tube. There ||M||<=Mbar, so
the sum of hidden travel over every partial sequence of flow segments is

\[
\int(\|\dot w\|_2+\|\dot M\|_F)\,dt
\le 2Bh\,\overline C(1+\overline M)\sqrt\theta R_*
\le\rho/2.                                             \tag{9}
\]

Since kicks do not move hidden fields, a first exit at distance rho is
impossible. Global finite-time GF existence was proved on the full Hilbert
space in ESCAPE_AND_LIMITS.md. It justifies every segment and the first-exit
argument even for unbounded pointwise fields. This proves (4) for all
finite histories and makes the process well defined stage by stage.

The argument intentionally does not identify the hidden path with a
fixed-feature model: both original hidden velocities in (8) are retained.
The bounded-travel condition is an imposed regime of this optimizer.

## 3. Constant success probability and explicit rates

By (6), every trial succeeds precisely when

\[
\left|\frac e{\sqrt\ell}+Z\right|^2\le\theta.
\]

The vector e/sqrt(ell) has norm one. Rotational invariance of the prescribed
m-dimensional Gaussian gives the SAME conditional success probability

\[
q_{m,\theta,\sigma}
 =\Pr\{|e_1+\sigma G|^2\le\theta\}>0,\qquad G\sim N(0,I_m),       \tag{10}
\]

at every trial, regardless of current state, labels, or data conditioning.
It is an explicit finite Gaussian integral. All uniforms here concern
trial probability, not physical sizes or conditioning costs of (2).

The successive success indicators are Bernoulli(q): conditioning on any
finite previous history gives the same probability q, so multiplication
of conditional probabilities gives the product joint law. Waiting times
between accepted stages are iid geometric(q). This statement applies until
exact zero; after zero, append independent fictitious indicators if needed.
The exact-zero event at a positive-loss Gaussian trial has probability zero,
and full GF cannot first hit an equilibrium in finite time by uniqueness.

If k counts ALL proposal trials, including rejections, energy dissipation
and the acceptance threshold yield

\[
\mathbb E L_k\le L_0[1-q(1-\theta)]^k
 \le L_0 e^{-q(1-\theta)k}.                             \tag{11}
\]

This is an unconditional expectation, not an expectation conditioned on a
successful confinement event: confinement was deterministic in (4).

For 0<epsilon<L0, put

\[
J_\epsilon=
\left\lceil\frac{\log(L_0/\epsilon)}{\log(1/\theta)}\right\rceil .
\]

At most J_epsilon successes suffice. Therefore the total number N_epsilon
of trials needed obeys

\[
\mathbb E N_\epsilon\le J_\epsilon/q,\qquad
\Pr\{L_k>\epsilon\}\le (L_0/\epsilon)e^{-q(1-\theta)k}.   \tag{12}
\]

Every accepted readout jump has total norm bounded by (7), and full GF
has summable travel by (8)--(9). Thus the actual population state converges
strongly almost surely to a finite state of loss zero. This strengthens
loss fitting to a state endpoint for this modified process.

For an almost-sure rate, choose 0<a<q(1-theta). Markov's inequality in
(11) gives P(L_k>L0 exp(-a k))<=exp(-(q(1-theta)-a)k).
The sum is finite; the union-bound proof of the elementary
Borel--Cantelli implication gives L_k<=L0 exp(-a k) eventually almost
surely. There is no deterministic bound on the random last exceptional k.

## 4. A dimension-polynomial choice of Gaussian scale

Taking theta fixed away from one can make q exponentially small in m.
One can avoid that particular penalty. Choose

\[
\sigma=\frac1{4m},\qquad \theta=1-\frac1{4m},\qquad
q_*=\frac{e^{-2}}{2\sqrt{2\pi}}>0.                       \tag{13}
\]

In coordinates with e/sqrt(ell)=e1, consider
-2<=G1<=-1 and sum_(j>=2) G_j^2<=2(m-1).
For m>1 the second event has probability at least 1/2 by Markov's inequality
and is independent of G1; for m=1 it holds surely. The first event has
probability at least exp(-2)/sqrt(2pi). On their intersection,

\[
|e_1+\sigma G|^2
\le1-\frac1{2m}+\frac{2m+2}{16m^2}
\le1-\frac1{4m}=\theta.
\]

Thus q>=q_* uniformly in m>=1. Equations (11)--(12) become

\[
\mathbb E L_k\le L_0\exp\left(-\frac{q_*}{4m}k\right),\qquad
\mathbb E N_\epsilon\le
\frac{1+4m\log(L_0/\epsilon)}{q_*}.                      \tag{14}
\]

The label-independent coordinate e1 is used only to evaluate the Gaussian
probability, not to center the algorithm's noise toward the residual.
The proposed Z remains centered and isotropic in (1)'s weighted output space.

The physical parameter covariance and h still depend on input geometry
through K and kappa0. Equation (14) is not a geometry-independent
small-parameter-perturbation theorem, nor a bound on computing exact
population expectations or solving K systems.

## 5. Elapsed time and accumulated GF time

Assign each proposal/evaluation a fixed duration Delta>0 while holding the
state fixed, and each successful proposal the full physical GF interval h.
There is no flow during rejected trials. Each trial-plus-possible-flow
costs at most Delta+h. At elapsed time t at least

\[
k(t)=\left\lfloor t/(\Delta+h)\right\rfloor
\]

trials and their optional intervals have been completed. Nonincreasing
loss and (11) give

\[
\mathbb E L(t)\le L_0
 \exp[-q(1-\theta)\lfloor t/(\Delta+h)\rfloor].            \tag{15}
\]

Moreover

\[
\mathbb E\tau(\epsilon)
\le J_\epsilon(\Delta/q+h),\qquad
\Pr\{\tau(\epsilon)>t\}
\le \min\{1,(L_0/\epsilon)e^{-q(1-\theta)k(t)}\}.         \tag{16}
\]

These are actual elapsed-clock estimates for the specified hybrid algorithm,
not only successful-stage estimates. This is not wall-clock complexity
of an infinite-population implementation; Delta is a declared exact-oracle
trial clock.

Unless already fitted, infinitely many stages succeed almost surely.
Since h is fixed and strictly positive, the accumulated original GF
physical time is also infinite. Hidden learning has not been stopped
after a finite total amount of GF time, although its total path length
is finite as loss vanishes.

## 6. Extension when canonical initial feature independence is unavailable

The current-state theorem itself applies to any bounded fixed dictionary
with positive definite starting readout Gram. For canonical p=3 this study
has not proved initial feature independence for every compatible dataset;
do not silently assume it.

There is an explicit OPTIONAL data-only initial hidden refresh valid for
p=1,2,3. Section 2 of NOISE_GLOBAL_PROGRESS.md constructs, from the input
directions and canonical mark laws alone, finite hidden fields w_T,M_* with
linearly independent H_i. It selects a sign-pattern mixture and sufficiently
large finite T; no labels or fitted readout are needed to select these
hidden fields. Keeping c=0 preserves every initialized prediction and L0=1.
After that loss-neutral hidden jump, K0>0 and this theorem applies.

This gives an unconditional all-compatible-data variant at all three orders,
but it explicitly changes the hidden state before training and must not be
described as the unchanged canonical trajectory. At p=1,2 no such refresh
is needed: the original canonical initialized Gram is already positive.

## 7. Meaning and limitations

The gain over fixed full-support noise is quantitative and structural:
equalized prediction noise makes success probability independent of the
state, while a fixed positive schedule of full-GF intervals preserves
the invertibility needed to define it. Vanishing readout noise and summable
travel avoid indefinite jitter at the fitted endpoint.

This is an anisotropic, state-dependent, finite-rank perturbation law.
It can make large physical moves in poorly conditioned directions.
It uses exact current population features and an m-by-m inverse, and
deliberately limits accumulated hidden displacement. It does not prove
that ordinary infinitesimal isotropic noise, minibatch noise, or the
previous fixed Gaussian law enjoys (14)--(16). It does not establish
unrestricted nonlinear feature organization along the unmodified flow.
No probability of entering a good basin was left as an assumption:
the canonical p=1,2 Gram and the explicit schedule prove its preservation.

All new ingredients above are derived from the exact closure equations.
The only in-study dependencies are ESCAPE_AND_LIMITS.md Section 1,
INITIAL_EXCLUSION.md, INITIAL_REVIEW.md Section 6, and (only for the optional
refresh) NOISE_GLOBAL_PROGRESS.md Section 2. Required skills were applied.
