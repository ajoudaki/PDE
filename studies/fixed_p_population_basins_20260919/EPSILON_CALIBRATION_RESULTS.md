# Slower startup growth without disguising the perturbation

2026-09-19. Continuation of the same optimizer investigation. This note
separates a formal schedule change from an improvement at fixed physical
perturbation or trajectory accuracy. No experiment, implementation,
finite-width identification, or promotion.

## 1. Outcome and fixed contract

The previous logarithmic delay was a prescribed activation schedule,
not an intrinsic rate law discovered for the closure. Replacing it by
log log(1/epsilon), or any slower divergence, preserves qualitative
compact-time GF approximation. By itself this is not a substantive
improvement: the same operation makes the certified closeness to GF
decay more slowly, and the deterministic correction after activation
remains fixed strength and can be large near a singular Gram.

Two stronger, quantitative statements survive the audit:

1. In an explicitly fixed discounted physical-state path metric, a
   process that has fitted while GF still has a fixed loss gap must pay
   a logarithmic time cost to make its deviation at most epsilon, up
   to an additive log log correction. This is a finite-window theorem;
   it assumes no actual canonical positive-loss plateau.
2. If the entire added physical force is at most epsilon, the exact
   population closure stays close to ordinary GF through times
   c(log(1/epsilon))^(2/5), with constants independent of epsilon.
   A log-log fitting guarantee under that force bound would therefore
   also prove original-GF fitting, which remains unresolved in general.

Use the canonical p=1,2 finite compatible binary circle laws for the
delayed fitted construction, with complete correlated marks, unhalved
probability-weighted loss and original L2/Frobenius gradient metric.
The comparison statements themselves only require bounded fixed marks,
finite normalized inputs and finite initial state, so they are not
restricted by the p=1,2 initialization Gram theorem. Constants may depend
on these fixed objects but not on epsilon. Physical time, mark dimension,
data weights, metric, loss target, exponential rate, clipping scale and
noise refresh interval are fixed when epsilon varies.

Scientific sources are this study's unchanged conditioning/tangent-noise
theorems and analytic-Gram lemma, the two newly frozen prompt-only routes
EPSILON_DELAY_ROUTE.md and EPSILON_SMALL_FORCE_ROUTE.md, and the canonical
model definitions in the established book. The lead checked both routes
after they froze. Section 3 below adds an actual state-distance lower
bound, beyond the intervention certificate available in the delay route.

## 2. What an arbitrary delayed activation really certifies

Fix lambda>0 and let h(epsilon)>=0 tend to infinity. Draw V uniformly
on (0,1) and activate the existing corrected flow at

\[
 A_\varepsilon=h(\varepsilon)+V/\lambda.
 \tag{1}
\]

Before activation run original GF from the canonical state. Afterwards
retain the full reached state and use correction strength lambda/4.
Zero noise is permitted; the specific bounded tangent colored noise of
NATURAL_TANGENT_NOISE.md can also be included with amplitude epsilon.
An arbitrary noise satisfying only a norm bound is not substituted.
Original GF is finite at all finite times. Its singular-Gram times are
countable, so the absolutely continuous activation law avoids them almost
surely. The unchanged continuation theorem then gives continuous state
paths and a finite strong fitted endpoint, for each fixed epsilon almost
surely. On exceptional singular activations define original GF to continue.

The prior countdown proof works unchanged, with
Psi=e^(lambda a)L and a=(A_epsilon-t)_+. It gives

\[
 E L_\varepsilon(t)\le L_0
 \min\{1,(e-1)e^{\lambda h(\varepsilon)}e^{-\lambda t}\},
\]
\[
 \tau_\varepsilon(\ell)
 \le h(\varepsilon)+\lambda^{-1}[1+\log(L_0/\ell)]
 \quad(0<\ell<L_0),
 \tag{2}
\]

where the second bound is almost sure. For every fixed horizon T, all
sufficiently small epsilon have h(epsilon)>T, giving exact agreement
with GF throughout that horizon. There is no slowest diverging h: for
example sqrt(h) diverges more slowly than h. Thus the qualitative
approximation requirement alone cannot select an optimal epsilon law.

Fix once and for all the following metric on continuous physical-state
paths, with the same lambda and the fixed unit clipping scale:

\[
 D(S_\varepsilon,S^0)=\int_0^\infty
 \lambda e^{-\lambda t}
 \min\{1,\|S_\varepsilon(t)-S^0(t)\|_{\mathcal H}\}\,dt.
 \tag{3}
\]

It is a quantitative measure of actual state deviation. Small D alone
does not ensure compact-uniform convergence for arbitrary paths; narrow
spikes can evade this integral. The present delayed family has compact-
uniform convergence separately from its exact initial agreement.

The discounted amount of time during which correction is enabled is

\[
 Q_\varepsilon=\int_0^\infty\lambda e^{-\lambda t}
                 1_{\{t\ge A_\varepsilon\}}\,dt
 =e^{-\lambda A_\varepsilon}.
\]

Exact initial agreement implies D<=Q, so

\[
 E D\le E Q=(1-e^{-1})e^{-\lambda h(\varepsilon)}.
 \tag{4}
\]

This is an upper certificate, not a lower bound on actual state error.
The correction may coincide with GF after activation, for example at a
fitted state. In that case Q is positive while D is zero.

The precise calibration is A=lambda^(-1)log(1/Q). If the upper certificate
(4) is used to guarantee E D<=delta, it requires

\[
 h\ge\max\{0,\lambda^{-1}\log[(1-e^{-1})/\delta]\}.
 \tag{5}
\]

Replacing epsilon by the certified tolerance delta therefore restores the
same logarithmic dependence. In the following table, constant factors are
suppressed and epsilon is small enough for the iterated logs to exist:

| lambda h(epsilon) | Certified E D scale | Exponential prefactor scale |
|---|---|---|
| log(1/epsilon) | epsilon | 1/epsilon |
| log log(1/epsilon) | 1/log(1/epsilon) | log(1/epsilon) |
| log log log(1/epsilon) | 1/log log(1/epsilon) | log log(1/epsilon) |

These rows improve the displayed formula in an uncalibrated parameter;
they do not improve the certificate at a fixed tolerance. With zero
optional noise they are exactly a reparameterization of the same physical
delayed trajectories. Shrinking an optional tangent noise separately does
not turn the fixed deterministic correction into a small perturbation.

For every regular activation realization (a probability-one event for
each fixed epsilon), the smallest pathwise exponential prefactor is
exactly sup_{0<=s<=A} e^(lambda s)L(S^0(s)), since the postactivation
bound never exceeds its value at A. It may be much smaller than the
worst-case bound in (2) if original GF already learns fast. No prefactor
divergence for a particular canonical dataset is inferred without that
dataset's GF behavior. If the loss target itself is epsilon^q, the
existing exponential estimate additionally costs (q/lambda)log(1/epsilon);
a fixed-target log-log bound must not be reported as that joint-accuracy
guarantee.

## 3. An actual state-error lower bound when extra learning occurs

Unlike Q, the metric D measures physical state deviation. The following
bound applies to any modified process, regardless of its force size or
use of a delay, provided it is defined on the stated interval.

Write u_i=x_i/sqrt(d), ||u_i||<=1, and B_j=ess sup|b_j|. The exact closure
prediction is

\[
 a_i=E_1[b_1\phi(w\cdot u_i)],\quad
 H_i=\phi(b_2^TMa_i),\quad f_i=E_2[cH_i],\quad\phi=\tanh.
\]

On a physical ball ||S||<=R its gradient blocks have norms at most
B_1B_2 R^2, 1, B_1B_2 R respectively. For the w block this uses the
actual M^T in
phi'(w.u_i)u_i b_1^T M^T E_2[c phi'(b_2^T M a_i)b_2]. Thus

\[
 \|\nabla f_i\|\le(1+B_1B_2)(1+R)^2.
 \tag{6}
\]

The same constant bounds the derivative of the weighted prediction
vector, because sum_i mu_i=1. Integrating the first derivative along
segments proves the corresponding Lipschitz estimate; no second
Frechet derivative is invoked.

Let L0=1 and R0=||S0||, as at canonical binary initialization. The GF
energy identity gives ||S^0(t)||<=R0+sqrt(t). Set

\[
 G=(1+B_1B_2)(R_0+3)^2\ge1.
 \tag{7}
\]

If a state S has ||S-S^0(t)||<1, the segment between them lies in the
radius R0+sqrt(t)+1 ball. Since
(R0+2+sqrt(t))² <= (R0+3)²(1+t), (6) gives

\[
 \|(\sqrt{\mu_i}[f_i(S)-f_i(S^0(t))])_i\|
 \le G(1+t)\|S-S^0(t)\|.
 \tag{8}
\]

Suppose 0<=a<b<=1, L(S)<=a and L(S^0(t))>=b. The reverse triangle
inequality for the weighted residual vector makes the left side at
least eta=sqrt(b)-sqrt(a)>0. If the state distance is at least one the
following bound is automatic, while otherwise (8) proves it:

\[
 \min\{1,\|S-S^0(t)\|\}\ge\frac{\eta}{G(1+t)}.
 \tag{9}
\]

**Finite-window theorem.** Suppose original GF has
L(S^0(T+1/lambda))>=b, and with probability at least 1-q the modified
loss is at most a throughout [T,T+1/lambda], where q<1. Then

\[
 E D(S_\varepsilon,S^0)
 \ge \frac{(1-q)(\sqrt b-\sqrt a)(1-e^{-1})}{G}
       \frac{e^{-\lambda T}}{1+T+1/\lambda}.
 \tag{10}
\]

**Proof.** Original loss is nonincreasing, so it is at least b on the
entire interval. On the probability-at-least-1-q event apply (9), restrict
the nonnegative integral defining D to that interval, bound 1/(1+t)
below by 1/(1+T+1/lambda), and integrate lambda exp(-lambda t).
Multiply by the probability of the event. No independence is needed.

For a nonincreasing modified loss, a fitting-time guarantee
P{tau_a<=T}>=1-q supplies exactly the event used above. Combining (10)
with a genuine guarantee E D<=epsilon gives

\[
 \lambda T+\log(1+T+1/\lambda)
 \ge\log(1/\varepsilon)
  +\log\frac{(1-q)(\sqrt b-\sqrt a)(1-e^{-1})}{G}.
 \tag{11}
\]

With fixed a,b,q,lambda and model, this implies as epsilon->0

\[
 T\ge\lambda^{-1}
 [\log(1/\varepsilon)-\log\log(1/\varepsilon)-O(1)].
 \tag{12}
\]

To verify the asymptotic statement, if T>=log(1/epsilon)/lambda it is
immediate; otherwise bound the logarithm on the left of (11) by
log log(1/epsilon) plus a fixed constant. The O(1) contains only the
displayed fixed data and gap parameters. A log-log startup cannot satisfy
(11) while retaining a fixed loss advantage over GF and E D<=epsilon.

This is not a universal lower bound on fitting time: if GF has already
fitted to comparable loss, the separation premise fails. In particular,
no actual positive-loss canonical plateau has been proved here. If such
a plateau existed, choose a<b below that plateau; (12) would apply to
every fitting method obeying this metric budget and monotone-loss/hitting
premises. Conversely an all-accuracy sublogarithmic guarantee with this
budget would exclude every positive plateau of original GF.

## 4. A different calibration: the total force is at most epsilon

The independent EPSILON_SMALL_FORCE_ROUTE.md proves a second statement
directly from the complete closure equations. Assume

\[
 \dot S_\varepsilon=-\nabla L(S_\varepsilon)+v_\varepsilon(t),
 \qquad \|v_\varepsilon(t)\|_{\mathcal H}\le\varepsilon
 \quad\text{a.e.},\qquad S_\varepsilon(0)=S_0.
 \tag{13}
\]

The bound concerns the full added force, including deterministic and
random corrections, in the unchanged physical metric. It is pathwise
for colored random controls. It does not describe Brownian paths or
unbounded-rate jump processes merely because their coefficients are small.

For bounded measurable prescribed controls, the route proves global
existence. For an unspecified feedback rule its estimates concern every
existing solution and do not assume feedback uniqueness. Completing the
energy estimate gives

\[
 L(S_\varepsilon(t))\le L_0+\varepsilon^2t/4,
 \quad
 \|S_\varepsilon(t)-S_0\|
 \le\sqrt{L_0t}+\varepsilon t.
 \tag{14}
\]

The prediction gradients are Lipschitz on radius-R balls with the valid
bound J_R=2B_1B_2(1+B_1B_2)(1+R)^3. A chord Taylor-remainder identity
retains the dissipative square of prediction differences and gives

\[
 \langle S-T,-\nabla L(S)+\nabla L(T)\rangle
 \le J_R[\sqrt{L(S)}+\sqrt{L(T)}]\|S-T\|^2.
 \tag{15}
\]

This uses endpoint losses and first derivatives only, rather than an
unjustified second derivative of an L2-valued tanh map. Combining (14)
and (15) yields the complete pathwise bounds, for all sufficiently small
epsilon and

\[
 C_* =\max\{1,6B_1B_2(1+B_1B_2)(\|S_0\|+3)^3\},
 \quad
 T_\varepsilon=
 \left[\frac{\log(1/\varepsilon)}{2C_*}\right]^{2/5},
\]
\[
 \sup_{t\le T_\varepsilon}\|S_\varepsilon(t)-S^0(t)\|
 \le\sqrt\varepsilon\,T_\varepsilon\to0,
\]
\[
 \sup_{t\le T_\varepsilon}|L(S_\varepsilon(t))-L(S^0(t))|
 \le3(1+B_1B_2)(\|S_0\|+3)^2
        \sqrt\varepsilon\,T_\varepsilon^2\to0.
 \tag{16}
\]

All constants are fixed before epsilon varies. No eigenvalue lower bound,
closure-order limit, sample-size limit, or inverse Gram is hidden here.
The exponent 2/5 is a sufficient comparison scale, not an optimal lower
bound claimed for the actual model.

If original GF had limiting loss ell>0, every trajectory obeying (13)
would remain above any fixed a<ell throughout this horizon, for sufficiently
small epsilon. Thus a genuine log-log fitting theorem, or a fixed-rate
exponential tail with bounded tail prefactor beginning after a log-log
delay, would already rule out positive limiting loss of original GF.
This remains a conditional exclusion; this study supplies no canonical
instance with such a plateau. Bounds merely on the optional random force
do not qualify the previous fixed-strength corrected optimizer for (13).

## 5. Resource audit and exact remaining question

| Quantity | What is actually proved or required |
|---|---|
| Physical time | Unchanged throughout; rescaling cannot be counted as a speedup |
| Approximation parameter | h->infinity alone is qualitative; calibrated D or full-force bounds must be stated separately |
| Delayed correction | Fixed strength after activation, not O(epsilon) globally |
| Noise | Specific tangent colored noise may be small; its amplitude does not bound the deterministic correction |
| Gram inverse | Almost-sure invertibility at activation; no uniform inverse norm or inverse moment bound supplied |
| Numerical work | No step-count, quadrature-cost, or finite-precision complexity guarantee |
| Exponential prefactor | Tracked explicitly by exp(lambda h) and the actual GF prefix |
| Loss target | Fixed independently of epsilon unless its extra accuracy cost is displayed |
| Comparison constants | Bounded marks and fixed initial physical norm; no epsilon-dependent data, width, order or metric |

There is no proved honest log-log improvement for the general canonical
closure at a fixed physical perturbation/approximation specification.
The delayed-family modification alone fails that comparison by changing
what epsilon certifies. Nor has such an improvement been disproved for
canonical data: it may be possible if one proves the missing fitting
behavior of original GF. The new exact statements show what a purported
improvement would have to establish and where a hidden substitution would
appear. The historical logarithmic schedule remains mathematically valid,
but should not be described as an intrinsic or optimized epsilon tradeoff.
