# Nonvanishing exponents and the gradient-flow limit

2026-09-19. Lead continuation of the same optimizer investigation.
Exact theoretical statements below; no experiment, implementation,
finite-width identification, or promotion. The strong uniform-rate
question remains open for the canonical closure.

## 1. Target, information, and two different rate claims

Use the canonical p=1 or p=2 population closure on a finite compatible
binary circle law, with the complete initialized joint marks, actual
transpose, unhalved probability-weighted loss L, and physical Hilbert
state S=(w,c,M). Aggregate compatible duplicates and antipodes before
forming the current weighted feature Gram K. The formulas and metric are
exactly those in NATURAL_CONDITIONING_FLOW.md Section 1. Write S^0 for
ordinary GF from the same canonical S0, and L0=L(S0)=1.

The desired approximation is S_epsilon(t) -> S^0(t) in probability for
every fixed physical time, preferably uniformly on every compact time
interval. No time rescaling is permitted. Constants may depend on the
fixed dataset but their epsilon dependence must be explicit.

Two requests are mathematically distinct:

1. A uniform estimate E L(S_epsilon(t)) <= C L0 exp(-lambda t) for all
   t>=0 and sufficiently small epsilon, with C<infinity and lambda>0
   independent of epsilon.
2. The same exponent lambda with a prefactor C_epsilon or a warmup time
   T_epsilon that may diverge as epsilon tends to zero.

The first transfers to ordinary GF itself. The second can be constructed
unconditionally using the existing corrected flow, but has a diverging
worst-case time to reach fixed accuracy. It is not a resolution of the
first request or a uniformly small-force theorem.

Only current state, finite data, prescribed clocks and independent
randomness are algorithmic inputs. No original future trajectory or
unknown fitted endpoint is supplied to a construction.

## 2. A uniform bound transfers without exchanging infinite-time limits

**Proposition.** Let L be a nonnegative continuous function on a metric
state space. Suppose S_epsilon(t) -> S^0(t) in probability at each fixed
t, where S^0 is deterministic. Then

\[
 L(S^0(t))\le\liminf_{\varepsilon\to0}E L(S_\varepsilon(t)).
 \tag{1}
\]

Consequently a common C,lambda as in Section 1 implies

\[
 L(S^0(t))\le C L_0e^{-\lambda t}\quad\text{for every }t\ge0.
 \tag{2}
\]

**Proof.** Fix t and put ell=L(S^0(t)). If ell=0, nonnegativity proves
(1). If ell>0, for every 0<a<ell continuity and convergence in probability
give P{L(S_epsilon(t))>=a}->1. Hence E L(S_epsilon(t)) >=
a P{L(S_epsilon(t))>=a}, whose liminf is at least a. Let a increase to
ell. Substitute the common bound to obtain (2). No uniform integrability
or interchange of t=infinity and epsilon=0 is used. The same proof works
along any approximation sequence and for exponents lambda_epsilon with
a positive lower bound. A pathwise common bound implies the expectation
bound and therefore has the same consequence.

Data dependence does not remove this implication: fix the dataset first.
The closure's general original-GF exponential fitting theorem is not
proved in this study. Thus (1) is a precise reduction of the proposed
uniform strengthening, not a counterexample or an impossibility theorem
for its canonical initialization.

More generally any common deterministic upper envelope B(t) tending to
zero transfers by the same argument. Removing the word exponential does
not evade the underlying ordinary-GF fitting obligation.

### Quantitative prefactor and approximation tradeoffs

If a fixed exponent lambda is retained but C_epsilon varies, then for
every fixed t with ell=L(S^0(t))>0, convergence in probability ensures
P{L(S_epsilon(t))>=ell/2}>=1/2 for sufficiently small epsilon. Therefore

\[
 C_\varepsilon\ge\frac{\ell}{4L_0}e^{\lambda t}.
 \tag{3}
\]

If sup_t exp(lambda t)L(S^0(t)) is infinite, (3), choosing t first,
proves C_epsilon -> infinity. No particular divergence rate in epsilon
follows without a quantitative approximation horizon.

Conversely fix t with ell>0 and choose delta>0 small enough that
||S-S^0(t)||<delta implies L(S)>ell/2. Nonnegativity gives the explicit
estimate

\[
 P\{\|S_\varepsilon(t)-S^0(t)\|\ge\delta\}
 \ge 1-\frac{2E L(S_\varepsilon(t))}{\ell}.
 \tag{4}
\]

Thus a process that has already reduced expected loss far below that
of GF must have appreciable probability of a physically detectable
deviation at that same time.

For continuous nonincreasing losses define tau_a=inf{t:L(t)<=a}.
If L(S^0(T))>a, then P{tau_a(S_epsilon)<=T}->0: by monotonicity that
event is exactly {L(S_epsilon(T))<=a}, excluded in probability by the
fixed-time limit. A uniform accuracy-time guarantee would consequently
also be an original-GF fitting theorem, up to arbitrarily small accuracy
slack at equality.

## 3. The current estimate is a floor, not the actual decay rate

For the immediate corrected flow at strength epsilon, with its tangent
noise, set h=1+epsilon R and q=<nabla L,nabla R>. Direct differentiation,
including the safeguard and noise orthogonality, gives

\[
 -\dot L=h\|\nabla L\|^2+\varepsilon L[q]_+.
 \tag{5}
\]

For k=lambda_min K>0, ||nabla_c L||²=4e^TKe>=4kL and R>=1/k.
Keeping both terms in k h gives the stronger elementary bound

\[
 -\dot L\ge4(k+\varepsilon)L,\qquad
 L(t)\le L_0\exp\left[-4\varepsilon t-4\int_0^t k(S_\varepsilon(s))ds\right]
 \tag{6}
\]

before fitted absorption; afterward L=0. Thus the prior exponent
4epsilon does not say actual training slows down to that rate.
A proved lower bound int_0^t k ds >= gamma t-B, uniformly for small
epsilon, would give C=exp(4B) and lambda=4gamma, independent of epsilon.
This geometric estimate has not been proved for general canonical data.

It is sufficient but stronger than necessary to control the entire
readout Gram. Let e_i=sqrt(mu_i)(f_i-y_i), J=De and Theta=J J* be the
full weighted prediction tangent Gram in the original physical metric.
The readout block is A, K=AA*, so Theta>=K. Original GF has exactly

\[
 -\frac{d}{dt}\log L(S^0(t))
 =4\frac{e^T\Theta e}{|e|^2}.
 \tag{7}
\]

On positive-loss intervals, integrating (7) shows that (2) is equivalent
to the accumulated lower bound

\[
 4\int_0^t\frac{e(s)^T\Theta(S^0(s))e(s)}{|e(s)|^2}\,ds
 \ge\lambda t-\log C.
 \tag{8}
\]

The first and middle hidden blocks are included in Theta. Equation (8)
identifies the missing dynamical estimate without requiring every
feature direction to remain nondegenerate. It is an exact criterion,
not a newly proved lower bound or a substitute for proving one.

## 4. A fixed eventual exponent with explicit logarithmic warmup

The following weaker construction is unconditional for the canonical
data scope of Section 1. Fix any lambda>0, set alpha=lambda/4, and for
0<epsilon<1 put

\[
 T_\varepsilon=\lambda^{-1}\log(1/\varepsilon),\qquad
 A_\varepsilon=T_\varepsilon+V/\lambda,
 \quad V\sim\operatorname{Unif}(0,1).
 \tag{9}
\]

The activation time is sampled independently at initialization.
Run exact original GF until A_epsilon. Then retain the full current
state and run the conditioning/tangent-noise flow from
NATURAL_TANGENT_NOISE.md with correction strength alpha, noise amplitude
epsilon, and fixed positive physical refresh interval. In particular
Phi_alpha=L(1+alpha R), beta_alpha uses alpha, and the noise is
epsilon sqrt(L) B(S)U_t. After activation the correction strength does
not tend to zero. The restart state includes the time remaining until
the sampled alarm, activation flag, and noise refresh information.

The analytic-Gram lemma in NATURAL_CONTINUOUS_ROUTE.md Section 3 proves
that singular-Gram times of original canonical GF are locally finite.
The absolutely continuous activation time avoids them almost surely.
On the null exceptional event define original GF to continue forever;
no almost-sure or expectation conclusion changes.

At a regular activation state, the complete conditioning theorem applies
from any finite state with K>0. It proves continuous state paths,
nonincreasing L, and a finite strong fitted endpoint almost surely, with

\[
 L_\varepsilon(t)\le
 L(S^0(A_\varepsilon))e^{-\lambda(t-A_\varepsilon)}
 \le L_0e^{-\lambda(t-A_\varepsilon)},\quad t\ge A_\varepsilon.
 \tag{10}
\]

Before activation L<=L0. As A_epsilon<=T_epsilon+1/lambda,

\[
 L_\varepsilon(t)\le
 L_0\exp[-\lambda(t-T_\varepsilon-1/\lambda)_+]
 =L_0\min\{1,(e/\varepsilon)e^{-\lambda t}\}
 \quad\text{almost surely}.
 \tag{11}
\]

The same bound holds in expectation. There is no integrability assumption
on the random inverse Gram at activation: (10) uses the bounded actual
loss prefactor, not the random potential prefactor. More sharply, for
t>=T_epsilon+1/lambda, integrating V gives

\[
 E L_\varepsilon(t)\le
 \frac{e-1}{\varepsilon}L_0e^{-\lambda t}.
 \tag{12}
\]

For every fixed horizon T, if epsilon<exp(-lambda T), activation occurs
after T. Hence the paths agree exactly on [0,T], proving unconditional
compact-time convergence. For every fixed epsilon, (11) gives

\[
 \limsup_{t\to\infty}\frac1t\log\frac{L_\varepsilon(t)}{L_0}
 \le-\lambda,
 \quad
 \tau_a\le\lambda^{-1}
 [\log(1/\varepsilon)+1+\log(L_0/a)]
 \quad(0<a<L_0)
 \tag{13}
\]

almost surely, with log(0)=-infinity. The guarantee's accuracy time
diverges logarithmically as epsilon->0; it need not be the actual
hitting time if original GF already fits sooner. The exponent remains
fixed precisely because a fixed-strength correction eventually activates.

This is a legitimate variant with the weaker asymptotic interpretation.
It neither keeps the full force uniformly small nor retains a bounded
prefactor. Replacing T_epsilon by any prescribed increasing-to-infinity
schedule also works, with the corresponding exp(lambda T_epsilon+1)
prefactor. No distinguished fastest warmup follows from compact-time
convergence alone.

## 5. Why flat fitting can make this issue real

An elementary scalar example illustrates the obstruction without making
any assertion about reachability in the population closure. Let
L(x)=x^4, x(0)=1. There is one critical point and it is a zero-loss global
minimum. Original GF is x'=-4x^3 and has

\[
 x(t)=(1+8t)^{-1/2},\qquad L(t)=(1+8t)^{-2}.
 \tag{14}
\]

Thus absence of bad equilibria alone does not give an exponential rate.
The smooth perturbation x'=-4x^3-epsilon x converges to original GF on
each finite interval. Solving for x² gives, for epsilon>0,

\[
 L_\varepsilon(t)
 =\left[\frac{\varepsilon}
 {(\varepsilon+4)e^{2\varepsilon t}-4}\right]^2,
 \qquad
 \lim_{t\to\infty}\frac1t\log L_\varepsilon(t)=-4\varepsilon.
 \tag{15}
\]

Direct substitution verifies (14)--(15), and expansion at epsilon=0
recovers (14). This counterexample only excludes an abstract inference
from a benign landscape to a uniform near-GF exponential rate. It is
not a canonical closure counterexample.

Writing tau=epsilon t in an exp(-epsilon t) guarantee changes the clock;
ordinary GF then has velocity -nabla L/epsilon with respect to tau.
It does not improve the physical-time guarantee while retaining GF.
Likewise fast random increments of size epsilon can accumulate an
order-one effect if their frequency is of order epsilon^{-2}; whether
they converge to GF must still be proved. They cannot evade (1) if that
convergence actually holds.

## 6. Status and decisive remaining task

- Proved: any uniform expected-loss envelope transfers to original GF;
  prefactor/deviation tradeoffs (3)--(4); the sharper state-dependent
  dissipation (6); and the delayed fixed-exponent construction (9)--(13).
- Open: an epsilon-uniform nonzero exponent with bounded prefactor for
  general compatible canonical p=1,2 data while approaching original GF.
- Not disproved: original canonical GF exponential fitting. An abstract
  flat-minimum example is not evidence that the canonical path has it.
- Missing estimate: original-flow residual-direction accumulated
  coercivity such as (8), or a comparably strong uniform estimate along
  a near-GF family. A schedule cannot silently supply this geometry.

The exact newly strengthened claim is the fixed eventual exponent with
its explicit delay, not a uniform physical-time fitting theorem for GF.
Scientific dependencies are the unchanged same-study conditioning and
tangent-noise proofs, the analytic-Gram lemma, and the model definitions
in the established book. The separate prompt-only limit route is checked
after freezing; check provenance and hashes are recorded in the README.
