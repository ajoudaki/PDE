# Exponential fitting with small feature-weighted readout noise

2026-09-19. Lead theoretical continuation; no experiments or promotion.
This is a second variant, distinguished from prediction-isotropic noise.
Its update requires no Gram inverse, no fitted readout, and no residual
direction. Input geometry appears explicitly in its convergence rate.

## 1. Exact setup and statement

Use the full physical closure, finite compatible binary circle data,
merged observation count m, readout map A and weighted Gram K=AA* from
RATE_ADAPTED_READOUT.md, Section 1:

\[
H_i=\phi(b_2^TMa_i),\qquad
(Az)_i=\sqrt{\mu_i}E_2[zH_i],\qquad
L=|e|^2,\quad e_i=\sqrt{\mu_i}(E_2[cH_i]-y_i).
\tag{1}
\]

Here phi=tanh and a_i=E_1[b_1 phi(w dot x_i/sqrt2)]. The physical fields,
canonical correlations, dictionary normalization, and full-gradient
metric are exactly those in that source. In particular

\[
\|A\|^2=\|K\|\le \operatorname{tr}K
 =\sum_i\mu_i E_2[H_i^2]\le1.
\tag{2}
\]

Start from any finite Hilbert state with L0>0 and K0 positive definite.
Canonical initialization has this property for all finite compatible
circle datasets at p=1 and p=2, as established in INITIAL_EXCLUSION.md
and INITIAL_REVIEW.md, Section 6; no linear-independence or separation
assumption on the inputs is required. For p=3 the optional data-only,
loss-neutral hidden refresh in the source also suffices. All assertions
below stop trivially when the initial loss is zero.

Put

\[
\kappa=\tfrac12\lambda_{\min}(K_0),\quad
\eta=\frac{\kappa}{4m},\quad
\theta=1-\frac{\kappa^2}{4m},\quad
q_*=\frac{e^{-2}}{2\sqrt{2\pi}}.
\tag{3}
\]

Equation (2) implies 0<kappa<=1/2, so 0<theta<1.
Use the explicit positive GF duration h from equation (3) of
RATE_ADAPTED_READOUT.md with this theta. At a held state of loss ell>0,
draw independent G~N(0,I_m) and propose the readout-only change

\[
\delta c=\eta\sqrt{\ell}\,A^*G
 =\eta\sqrt{\ell}\sum_{i=1}^m\sqrt{\mu_i}G_iH_i.
\tag{4}
\]

Accept if L(w,c+delta c,M)<=theta ell. Hold the state fixed on rejection.
After acceptance, run the exact full original gradient flow in w,c,M
for the fixed duration h. Repeat. The scalar eta here is a noise scale,
not the canonical dictionary ridge.

**Theorem.** This process is well defined at every stage, stays in the
deterministic hidden tube of the source, and satisfies K>=kappa I.
Writing L_k for loss after k proposals and their optional flow segments,

\[
E L_k\le L_0
 \left(1-\frac{q_*\kappa^2}{4m}\right)^k
 \le L_0\exp\left(-\frac{q_*\kappa^2}{4m}k\right).
\tag{5}
\]

For 0<epsilon<L0, if N_epsilon is the number of proposals until
L<=epsilon, then

\[
E N_\epsilon
\le \frac1{q_*}
 \left\lceil\frac{\log(L_0/\epsilon)}{\log(1/\theta)}\right\rceil
\le\frac{1+(4m/\kappa^2)\log(L_0/\epsilon)}{q_*}.
\tag{6}
\]

Also P(L_k>epsilon)<=
(L0/epsilon) exp[-q_* kappa^2 k/(4m)].
The population state has a finite strong Hilbert limit with loss zero
almost surely. For every fixed 0<a<q_* kappa^2/(4m), almost surely
L_k<=L0 exp(-a k) for all sufficiently large k.

These conclusions are unconditional from canonical initialization at
p=1,2: persistence of the Gram is proved, not assumed along the path.

## 2. Accepted steps obey the same deterministic tube bound

On the hidden tube K>=kappa I. For any z in range(A*), write z=A*v and
diagonalize the positive m-by-m matrix K. Its eigenvalues are at least
kappa, so

\[
\|Az\|^2=v^TK^2v\ge\kappa v^TKv=\kappa\|z\|_2^2.
\tag{7}
\]

Every proposal (4) lies in this range. For an accepted proposal,
the triangle inequality gives

\[
\|A\delta c\|=|e^{\rm trial}-e|
\le(1+\sqrt\theta)\sqrt{\ell},\qquad
\|\delta c\|_2\le
\frac{1+\sqrt\theta}{\sqrt\kappa}\sqrt{\ell}.
\tag{8}
\]

The deterministic proof in source Section 2 uses only the last bound,
the fact that a kick leaves w,M unchanged, and the fractional reduction.
It does not otherwise use the proposal distribution. Explicitly,
ell_j<=theta^j L0 makes the sum of accepted-step norm bounds finite;
the exact speeds

\[
\|\dot c\|\le2\sqrt L,\quad
\|\dot M\|\le2B_1B_2\|c\|\sqrt L,\quad
\|\dot w\|\le2B_1B_2\|M\|\|c\|\sqrt L
\tag{9}
\]

bound the cumulative readout norm and hidden travel. The source's h
makes the latter at most half the hidden-tube radius. Its Gram
perturbation inequality prevents any first exit. Thus exactly the same
finite-history argument proves K>=kappa I for every history of this
algorithm, without a probabilistic confinement event.

## 3. A uniform probability of fractional improvement

Conditional on a positive-loss held state, v=e/sqrt(ell) is a unit vector,
and the exact trial loss ratio is

\[
\frac{L^{\rm trial}}{\ell}
 =|v+\eta KG|^2
 =1+2\eta v^TKG+\eta^2|KG|^2.
\tag{10}
\]

K is symmetric and K>=kappa I, so |Kv|>=kappa.
Consider the Gaussian event where the component of G in direction
Kv/|Kv| lies in [-2,-1], and the squared norm of its orthogonal component
is at most 2(m-1). The former has probability at least
exp(-2)/sqrt(2pi); the latter is independent and has probability at least
1/2 by Markov's inequality when m>1, and probability one when m=1.
Thus this event has conditional probability at least q_*.

On the event, v^TKG<=-|Kv|<=-kappa, while (2) gives
|KG|^2<=|G|^2<=2m+2<=4m. Substitution into (10) yields

\[
\frac{L^{\rm trial}}{\ell}
\le1-2\eta\kappa+4m\eta^2
=1-\frac{\kappa^2}{4m}=\theta.
\tag{11}
\]

This proves a history-uniform lower bound q_* on acceptance probability.
The direction Kv/|Kv| is used only to prove the bound; proposals do not
use it. Unlike the source's isotropic prediction variant, actual success
probabilities may change with the state, and successes are not claimed
to be iid.

At any trial, success multiplies loss by at most theta, rejection
preserves it, and following full flow can only decrease it. Conditional
expectation therefore gives

\[
E[L_{k+1}\mid\mathcal F_k]
\le [1-q_*(1-\theta)]L_k.
\tag{12}
\]

Iteration proves (5). At each held stage independent trials have the
same conditional probability p(S)>=q_*; their conditional geometric
mean is at most 1/q_*. Summing these conditional expectations over at
most the displayed number of stages proves (6). Every stage finishes
almost surely; countably many such statements ensure infinitely many
successes unless the process terminates at zero.

The same summable jump and full-flow travel bounds in (8)--(9) prove a
strong state limit, and continuity of loss makes its loss zero.
The probability bound follows by Markov's inequality; applying it at
epsilon=L0 exp(-a k) gives a summable exceptional-event bound whenever
a<q_* kappa^2/(4m), proving the claimed almost-sure rate.

## 4. Perturbation size, clock, and interpretation

The conditional physical covariance and mean squared size of a trial are

\[
\operatorname{Cov}(\delta c\mid S)
 =\ell\eta^2 A^*A,\qquad
E[\|\delta c\|_2^2\mid S]
 =\ell\eta^2\operatorname{tr}K
 \le\frac{\kappa^2}{16m^2}\ell.
\tag{13}
\]

Thus typical perturbations are small in the original physical metric
and vanish with the loss. This is a second-moment statement; Gaussian
trials are not uniformly bounded. Rejected candidates never enter the
actual state, and every accepted move satisfies (8).
No inverse of the current Gram is evaluated by (4). Only the fixed
starting eigenvalue (or a certified smaller positive bound) is required
to choose the scalar scale, threshold, and GF schedule. Replacing
kappa0 in every schedule formula by the same certified lower bound
preserves all inequalities.

With a declared exact-oracle proposal duration Delta>0, the elapsed
hybrid clock satisfies

\[
E L(t)\le L_0\exp\left[
-\frac{q_*\kappa^2}{4m}
\left\lfloor\frac{t}{\Delta+h}\right\rfloor\right].
\tag{14}
\]

The mean elapsed hitting time is at most
J_epsilon(Delta/q_*+h), where J_epsilon is the ceiling in (6).
This counts rejections and every intervening physical flow interval.
It is not a computational cost bound for evaluating population integrals.
Infinitely many successes give infinite accumulated full-GF time since
h is fixed and positive, while the state travel remains summable.

The precise tradeoff is now explicit. Prediction-isotropic perturbations
remove input conditioning from the proposal rate by inverting K.
The present small physical perturbations avoid that inverse, at the
cost of the kappa^2 factor in the exponential rate and a potentially
small h. Both train the hidden fields during every GF segment and
preserve their conditioning by limiting total hidden travel.
Neither gives a rate for unmodified GF, SGD, arbitrary additive noise,
or unrestricted hidden excursions. These are readout-driven fitting
algorithms; the proof is not a global saddle-escape mechanism.

Dependencies are exactly RATE_ADAPTED_READOUT.md and its declared
model/initialization inputs. Every new probability and norm estimate
needed for this variant is proved above. This candidate awaits separate
internal mathematical checking.
