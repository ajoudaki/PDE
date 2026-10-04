# Endpoint reconstruction and comparison with proved dense variability

2026-10-04. Coordinator reconstruction and elementary corollary. This is
an internal collaborative check, not an independent promotion review.

The complete endpoint proof checked is INTEGRATED_ENDPOINT_CONFIDENCE.md,
SHA-256 f7c2eda7efd9f8cc517a72e3252c1eb120d08a9625e2014102a625a3b36ebef4.
Its complete nonlinear source and initialized CLT had already been
reconstructed in INTEGRATED_COMPARISON_CHECK.md and
INTEGRATED_INITIAL_VARIABILITY_CHECK.md. The compact comparison below
inherits the checked two-tanh runtime theorem and label-sensitive storage
interface; it does not reprove their source-selection theorem.

## Endpoint check

All factors in the one-input dense flow agree with mean squared loss and
mobilities (n,1,n). The auxiliary feature coordinate u is used to analyze
the actual physical flow; no clock modification is made to the model.
For u<=1, bounded tanh gives ||w||_infinity<=u and the mixer increment
at most u^2/2. The first-feature path then has RMS increment at most
11u^2/2, and the top-feature RMS increment is at most 61u^2. The positive
three-term derivative of the training prediction along u has the stated
n factors. At u_0=g_0^(1/4)/16 its feature-Gram term stays above g_0/2,
because 61/256<1/4 and (3/4)^2>1/2.

Consequently y<=g_0^(5/4)/32 gives an actual interpolating endpoint
u_infinity<=2y/g_0. The scalar physical ODE approaches it exponentially
and every parameter converges. The proposed confidence-dependent cap
g_0^2 delta^(3/4)/sqrt(144000) is smaller than this fitting cap, since
32g_0^(3/4)delta^(3/4)/sqrt(144000)<1.

Integration of the readout and the final interpolation equation give,
respectively, 61u_infinity^3/3 and 244u_infinity^3/3. Dividing the latter
by G_n>=g_0 and using u_infinity<=2y/g_0 gives the full readout
remainder 2440y^3/(3g_0^4), in normalized Euclidean norm. The exact
query gradient has the required factor 1/n. Its three differences have
coefficients 11*2440/(3g_0^4), 2/g_0^3 and 40/g_0^3. Because g_0<=1,
their sum is at most (26966/3)/g_0^4<9000/g_0^4.

The unused first-layer column remains independent of the training
sigma-field, including the fitted endpoint. Oddness therefore centers
the entire nonlinear remainder, not only its leading term. Conditional
Gaussian Poincare gives its second moment at most
9000^2 y^6/(g_0^8 n). This is the essential width-uniform estimate.
Its two-copy variance on the joint training event has coefficient two,
because both conditional means vanish. No independence between a run's
leading term and its own remainder is assumed.

The initialized covariance CLT gives
sqrt(n)(kappa_n/G_n-tilde_kappa_n/tilde_G_n) converging in distribution
to N(0,2nu_2/q^2), with nu_2=q^2+a_2^4Q^2>=q^2. G_n>0 almost surely
and G_n converges in probability to q>0, so division is legitimate.
No inverse-Gram moment convergence is used. At threshold delta/2 the
limiting small-ball probability is at most delta/(2sqrt(pi))<delta/2.
The strict margin gives the stated eventual finite-width probability.

With b_n=delta|y|/(2sqrt(n)), Markov at b_n/2 gives the remainder
failure bound 32*9000^2*y^4/(g_0^8 delta^2). At the stated cap it is
delta/8, since 32*9000^2/144000^2=1/8. The training-event width threshold
in (19) controls each exponential by delta/64; the two-copy coefficients
sum to eight, so its failure is at most delta/8. The total loss is
3delta/4. The claimed success probability 1-delta and lower coefficient
delta/4 are therefore valid, including both actual fitted endpoints.

The CLT and training-event thresholds depend only on delta and fixed
tanh moments, not the nonzero label under its cap or the unused ambient
dimension. The proof asserts a bound for each deterministic label, not a
simultaneous event over all labels. The sign symmetry is exact. No
predictor endpoint on the bad event is invented for the probability
calculation. **PASS.**

## A concrete compression-at-dense-variability corollary

This gives one rigorous form of the user's requested calibration,
without assuming the still-open general strict-root dense upper bound.
It is restricted to the present one-input, two-tanh model.

Fix d>=2 and confidence 0<delta<1. Train on x_1=sqrt(d)e_1; use
x_*=sqrt(d)e_2 as the witness query. Let f_n be a canonical dense run,
tilde f_n an independent run, and f_C the established autonomous
corrected-readout compressor for f_n. Define

\[
 Q=\mathbb E\tanh^2 Z,\quad
 \gamma=\mathbb E\tanh^2(\sqrt QZ),\quad
 g_0=\tfrac12\mathbb E\tanh^2(\sqrt{Q/2}Z),\qquad Z\sim N(0,1).
\]

Suppose the fixed nonzero label satisfies the explicit cap

\[
 |y|\le\min\left\{
 2.8\times10^{-7}\gamma,\quad
 \frac{g_0^2(\delta/2)^{3/4}}{\sqrt{144000}}
 \right\}.
 \tag{1}
\]

For all sufficiently large n, with probability at least 1-delta,
the three trajectories exist, fit and converge, and, in the SAME norm

\[
 \|f-g\|_*=
 \sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}|f(t,x)-g(t,x)|,
\]

both inequalities hold:

\[
 \|f_C-f_n\|_*
 \le2.8\times10^5\gamma^{-3/2}\frac{|y|}{\sqrt n},
 \qquad
 \|f_n-\widetilde f_n\|_*
 \ge\frac\delta8\frac{|y|}{\sqrt n}.
 \tag{2}
\]

In particular

\[
 \|f_C-f_n\|_*
 \le\frac{2.24\times10^6}{\delta\gamma^{3/2}}
                 \|f_n-\widetilde f_n\|_*.
 \tag{3}
\]

The factor is explicit and independent of width, physical time and
ambient dimension. It is large, so (3) is an asymptotic constant-factor
statement, not a practical near-one noise ratio. Independence between
the compressor event and the dense-copy event is not required.

Proof: use the compact runtime certificate at failure probability
delta/2, and the endpoint lower theorem with its confidence parameter
delta/2. Their failure probabilities sum to at most delta. The endpoint
query difference lower-bounds the same all-time sphere norm in (2).
Dividing the two nonzero bounds gives (3). The first restriction in
(1) is precisely the proved compressor cap at m=1, L=2; the second is
the proved endpoint cap. There is no extra unproved response assumption.

For clarity, the retained size guarantee is the existing explicit
source construction from INTEGRATED_LABEL_STORAGE_ROUTE.md. With its
fully specified U(S),c_q(S), let S=16|y|/gamma, a=1/2 and

\[
 A_n(|y|)=\frac{2^{20}9^d}{d!}\frac{U(S)}a
     c_q(S)^{-(d-1)}
     \left(\frac{|y|}{\gamma}\right)^2\log(en)^{3d/2+1}.
\]

Then every moving and fixed retained real coordinate, including metrics,
data and solve caches, is covered by

\[
 \operatorname{size}(C)
 \le3060[A_n(|y|)+d+3]^2+10(d+1).
 \tag{4}
\]

The fixed-positive-label width thresholds in that theorem remain in
force. Equation (4) is polylogarithmic in n at fixed d,y. Dense learned
storage is n^2+n(d+1). Thus this construction already has a proved
constant-factor comparison to actual fitted dense variability while
retaining polylogarithmically many coordinates. It is not an assertion
that arbitrary dimension, sample, depth or activation constants are
uniform, and it does not resolve the general requested theorem.

If the label ALSO lies in the inherited general Legendre theorem's
small-label range, its explicit near-quarter order schedule yields
o(n^(-1/2)) same-run error. Apply the same intersection argument to
conclude that its error is eventually below the dense-copy lower
threshold. That additional threshold is presently qualitative; it is
not claimed to follow numerically from (1). The resulting moving count
is n^(5/4+o(1)), with n^2 fixed Gaussian-mixer entries still retained.

## The endpoint calibration has a necessary dense width power

For delta=1/4 in the endpoint theorem itself, assume explicitly
0<|y|<=g_0^2(1/4)^(3/4)/sqrt(144000). Independent dense runs
have endpoint witness discrepancy at least |y|/(16sqrt(n)) with
probability at least 3/4. A dense-copy upper tolerance epsilon with
success probability greater than 1/4 therefore requires
n>=y^2/(256epsilon^2), in the sufficiently-wide asymptotic regime.
The hidden dense matrix alone then contains at least
y^4/(65536epsilon^4) learned coordinates. For a common deterministic
reference, success probability greater than 1/2 for each independent
run instead gives the width lower bound y^2/(1024epsilon^2), by the
triangle inequality and independence.

These are necessary powers for the conventional iid dense family under
the stated confidence criteria. They neither bound all possible encodings
from below nor control a population bias. They validate the dense
epsilon^(-4) calibration at an actual fitted endpoint in this example.

The endpoint-proof author separately checked this corollary from its
quoted compact/size premises: PASS for label caps, probability losses,
relative coefficient, L=2,m=1 state count, and all necessary width/storage
constants. This is a collaborative cross-check, not a promotion review.
