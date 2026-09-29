# All-time prediction error against the dense population

28 September 2026. Continuation of the width-uniform old-clock study, now with
test prediction rather than parameter distance as the reported observable.
The readout starts at exactly zero and the small positive label RMS is fixed
as width and order vary. No network experiment or manuscript change is made.

## 1. Setting and the precise population distinction

Keep the canonical Gaussian tanh network, fixed input dimension d, finite
training data of size m, fixed hidden depth L, canonical gradient-flow block
mobilities, and the autonomous old-clock response-memory algorithm. The
limiting initial readout-feature Gram has a positive gap. Fix 0<Y<=Y_* so
the study's small-label activity, spectral-slack, and Gaussian bounds all
apply. The threshold is independent of width n and memory order q.

Let f_D(t,x) be the deterministic dense population predictor constructed in
SMALL_LABEL_GAUSSIAN.md. Let f_n^D and fhat_(n,q) be the dense and closure
finite-network predictors, respectively, on the same initialized arrays.
An infinite-width predictor limit of the fixed-q closure will be denoted F_q.
The existence of predictor limit points proved below is not identification
or uniqueness of an autonomous population moment ODE.

The current proved parameter estimate in SLOW_ORDER_UNIFORM_BOUND.md is

\[
 E_n(q):=\sup_{t\ge0}d_n(\widehat\theta_{n,q}(t),\theta_n^D(t))
 \le A(q)+b_n,\qquad
 A(q)=\frac{C_0}{q}\exp\!\left(K\sqrt{\log(e+q)}\right),
 \quad b_n\xrightarrow{\Pr}0.
 \tag{1}
\]

This holds on common good initialization events G_n with probability tending
to one, simultaneously for all q. The constants are independent of n,q,t.
The parameter distance is the sum of first-layer Frobenius difference divided
by sqrt(n), hidden learned-matrix Frobenius differences, and readout difference
divided by sqrt(n). The floor b_n depends on the dense trajectory, not q.

Intersect G_n with a fixed bound on ||W_(1,0)||_F/sqrt(n), which also holds
with probability tending to one under the prescribed Gaussian initialization.
The small-label total variation estimate preserves a common bound on this
norm for all times and orders. We continue to write G_n for the intersection.

For a test probability law mu on R^d define r(x)=||x||_2/sqrt(d). Constants
may depend on the fixed data, depth, initial Gram and physical bounds, and
where stated on mu or an input radius. They never depend on elapsed time.

## 2. Main prediction statements

There are constants B<=C Y and C_* such that, with

\[
 \Psi_\mu(s)=\left[\int
       \min\{4B^2,C_*^2r(x)^2s^2\}\,\mu(dx)\right]^{1/2},
 \tag{2}
\]

one has, simultaneously in all orders on G_n,

\[
 \sup_{t\ge0}\|\widehat f_{n,q}(t)-f_D(t)\|_{L^2(\mu)}
 \le \Psi_\mu(A(q))+\eta_{n,\mu},\qquad
 \eta_{n,\mu}\xrightarrow{\Pr}0.
 \tag{3}
\]

In fact every test-L2 statement below holds for the stronger error

\[
 \mathcal E_\mu(g,h)
 :=\left[\int\sup_{t\ge0}|g(t,x)-h(t,x)|^2\,\mu(dx)\right]^{1/2}.
 \tag{3a}
\]

It dominates the time supremum of the L2 error. Continuity in time makes
the pointwise supremum measurable by restriction to rational times. The
width remainder in (3) is defined using this stronger norm in Section 4.

The remainder is independent of q. No numerical rate in width has been
proved for it. The function Psi_mu tends to zero at zero for every fixed
probability law, including laws with no finite moments. Thus every prescribed
sequence q_n->infinity approximates the dense population predictor in test
L2, uniformly over all physical time, in probability.

If mu has finite second moment, the explicit estimate simplifies to

\[
 \sup_{t\ge0}\|\widehat f_{n,q}(t)-f_D(t)\|_{L^2(\mu)}
 \le C_*\left(\frac{\mathbb E_\mu\|X\|_2^2}{d}\right)^{1/2}
            \frac{C_0 e^{K\sqrt{\log(e+q)}}}{q}
       +\eta_{n,\mu}.
 \tag{4}
\]

In particular, for every fixed 0<gamma<1 this is bounded by
C_(mu,gamma) q^(-gamma)+eta_(n,mu). Unbounded support is permitted.
For a fixed bounded input domain K, let R_K=sup_(x in K)r(x). Then

\[
 \sup_{t\ge0,x\in K}|\widehat f_{n,q}(t,x)-f_D(t,x)|
 \le C_* R_K A(q)+\eta_{n,K},\qquad\eta_{n,K}\xrightarrow{\Pr}0.
 \tag{5}
\]

This covers an entire circle, sphere, cube, or ball, rather than a finite
test mesh. No test inputs need be added to the trained batch.

At the population-predictor level, every fixed-q infinite-width predictor
limit obeys, almost surely,

\[
 |F_q(t,x)-f_D(t,x)|
       \le\min\{2B,C_*r(x)A(q)\}
             \quad\hbox{for all }t\ge0,\ x\in\mathbb R^d.
 \tag{6}
\]

Such subsequential predictor limits exist in the weighted whole-input,
all-time topology described in Section 6. Therefore (6) is not predicated
on an unproved unique fixed-q population closure. It bounds every possible
predictor limit. If a unique autonomous fixed-q population closure is later
identified with these limits, it inherits exactly (6).

Consequently, for every test law,

\[
 \sup_{t\ge0}\|F_q(t)-f_D(t)\|_{L^2(\mu)}\le\Psi_\mu(A(q)),
 \tag{7}
\]

and for finite second moment the right side is C_mu q^(-1+o(1)), in the
explicit sense of (4) without its width remainder. For bounded K the whole
input-domain supremum is at most C_* R_K A(q). These statements do not
claim an unweighted supremum bound tending to zero over unbounded R^d.

## 3. Deterministic observation estimate, with no input sampling

On the common physical bounded region let R>=1 bound hidden operator norms,
F bound the full first-row RMS norm, and B bound readout RMS norms. The
population version uses the corresponding L2 and operator norms. Zero initial
readout and the exact readout equation give pointwise
|w_i(t)|<=2 integral_0^t rho(s)ds<=CY; hence both predictors have magnitude
at most B<=CY for every input, independently of its norm.

Since tanh is one-Lipschitz, bounded by one, and vanishes at zero,

\[
 \|h_\ell(x)\|_{\rm RMS}
       \le\min\{1,F R^{\ell-1}r(x)\}.
\]

Write e_1=||Delta W_1||_F/sqrt(n), e_l=||Delta W_l||_F for l>=2, and
e_w=||Delta w||_2/sqrt(n). The first feature difference is at most r(x)e_1.
Subtracting the two preactivations at every later layer gives

\[
 \|\widehat h_\ell-h_\ell\|_{\rm RMS}
 \le R\|\widehat h_{\ell-1}-h_{\ell-1}\|_{\rm RMS}
       +F R^{\ell-2}r(x)e_\ell.
\]

Induction bounds the last feature difference by C r(x) sum_(l<=L)e_l.
At readout, Cauchy--Schwarz bounds the changed-readout term by
e_w||hhat_L||_RMS and the changed-feature term by B times its RMS norm.
Thus

\[
 |\widehat f(t,x)-f(t,x)|
       \le\min\{2B,C_*r(x)d_n(\widehat\theta(t),\theta(t))\}.
 \tag{8}
\]

The factor r, rather than 1+r, uses the absence of biases and tanh(0)=0.
The constants are uniform in time and width on G_n. Taking time suprema and
integrating proves the finite-network comparison by Psi_mu(E_n(q)).
Bounded dominated integration proves Psi_mu(s)->0 as s->0. Also Psi_mu is
increasing and subadditive: use min(a,b+c)<=min(a,b)+min(a,c) pointwise
and then the L2 triangle inequality. Hence (1) implies

\[
 \sup_t\|\widehat f_{n,q}(t)-f_n^D(t)\|_{L^2(\mu)}
       \le\Psi_\mu(A(q))+\Psi_\mu(b_n).
 \tag{9}
\]

For any 0<p<=2, min(u^2,v^2)<=u^(2-p)v^p gives the additional explicit bound

\[
 \Psi_\mu(s)\le(2B)^{1-p/2}(C_*s)^{p/2}
                \bigl(\mathbb E_\mu r(X)^p\bigr)^{1/2}.
 \tag{10}
\]

Finite second moment preserves the near-one order exponent; finite pth
moment below two gives exponent p/2 of the same envelope. Without moments,
(2) is the exact available input-tail modulus. It can also be bounded by
C_*sR+2B sqrt(mu{r>R}) for every radius R.

## 4. Dense finite-to-population convergence over all time and inputs

The dense population construction gives finite-network prediction convergence
on every fixed physical interval for any finite list of passive test inputs.
Adding passive observations to the fixed Gaussian programs does not change
the training equations. Forward propagation gives a common input Lipschitz
constant at all times on G_n, using the full first-row RMS bound. A finite
input net consequently extends this convergence to each compact input ball.

Dense residual decay and the physical velocity bound yield, at finite width
on G_n and at population level,

\[
 \int_T^\infty\|\dot\theta_D(t)\|_{\rm sum}\,dt
       \le C e^{-\lambda T}.
\]

Apply (8) between two times of either dense path. For a bounded input ball
this gives a uniform tail-motion bound C_R exp(-lambda T); for an arbitrary
fixed test law it gives Psi_mu(C exp(-lambda T)). Both vanish as T grows.
Choose T first, then take width large in the fixed-horizon comparison.
For unbounded test support first choose an input ball with small complement
probability; global amplitude B bounds the complement in L2 by
2B sqrt(mu{r>R}). These choices prove

\[
 s_{n,K}:=\sup_{t\ge0,x\in K}|f_n^D(t,x)-f_D(t,x)|
          \xrightarrow{\Pr}0,
\qquad
 s_{n,\mu}:=\mathcal E_\mu(f_n^D,f_D)
          \xrightarrow{\Pr}0.
 \tag{11}
\]

For the second statement explicitly use
`s_(n,mu)^2 <= s_(n,K_R)^2 + 4 B^2 mu{r>R}`. This also proves the
stronger norm claim (3a), since (8) already bounds each input uniformly
over all time before any input integration.

The stronger whole-input weighted error also tends to zero:

\[
 s_n^w:=\sup_{t\ge0,x\in\mathbb R^d}
          \frac{|f_n^D(t,x)-f_D(t,x)|}{1+r(x)}
       \xrightarrow{\Pr}0.
 \tag{12}
\]

Indeed the spatial complement is bounded by 2B/(1+R), and the input ball is
controlled by (11). This is a weighted, not unweighted, supremum.

Combining (9) and (11) proves (3) with
eta_(n,mu)=Psi_mu(b_n)+s_(n,mu). Combining (8) on K with (11) proves (5).
Combining (8) with (12) also gives a width remainder for weighted whole-input
approximation. All these remainders depend on dense quantities, not order.
No interchange of an infinite horizon with width was used: the tail is first
made uniformly small, then the fixed compact comparison is applied.

## 5. Test risk, interpretation of width, and slow schedules

For any g in L2(mu), the reverse triangle inequality gives

\[
 \big|\operatorname{RMSE}_\mu(\widehat f(t),g)
          -\operatorname{RMSE}_\mu(f_D(t),g)\big|
       \le\|\widehat f(t)-f_D(t)\|_{L^2(\mu)}.
 \tag{13}
\]

The same holds for a joint test law of inputs and noisy square-integrable
labels. Thus every bound above controls the difference of the two test RMSEs,
uniformly in time, including their fitted endpoints. It does not assert that
the dense predictor itself has small error against the target. For squared
risks, multiply the discrepancy bound by at most 2(B+||g||_L2).

For every deterministic q_n->infinity, (3) tends to zero in probability.
In particular this holds for logarithmic or iterated-logarithmic orders.
For finite-second-moment mu a sufficiently slow nonconstructive schedule can
absorb the joint dense width remainders and yield a pure
C_(mu,gamma) q_n^(-gamma) bound with probability tending to one, for each
fixed gamma in (0,1). As in SLOW_ORDER_UNIFORM_BOUND.md, choose widths N_j
where the relevant dense remainders are at most 1/j with failure probability
at most 1/j, and set q_n=j between successive thresholds; make N_j>=j^4
if q_n<=n^(1/4) is desired. No numerical threshold or particular named slow
schedule is certified at that pure rate.

Uniform constants do not remove finite-width population-sampling error.
Even as q tends to infinity at one fixed width, the closure approaches that
width's dense network, whose predictor need not equal f_D. Therefore (3)
retains a width remainder. A pure order-only population estimate is the
width-limit statement (6)--(7), not a uniform finite-width identification
with f_D at every fixed n.

## 6. Predictor limit points exist and obey the population bound

This section uses the stronger all-order exponential closure fitting and
physical velocity estimates, equations (19)--(20) of
SMALL_LABEL_SPECTRAL_SLACK.md. If necessary choose the common small-label
threshold to be the minimum of the thresholds already stated above. On G_n,
for all q, the physical velocity is at most C exp(-kappa t). For any input,
the prediction differential in the normalized parameter metric is at most
C(1+r(x)): gates are bounded, hidden operators and backward RMS norms are
bounded, and only the first block contributes the extra input norm. Therefore

\[
 |\partial_t\widehat f_{n,q}(t,x)|
       \le C(1+r(x))e^{-\kappa t}.
 \tag{14}
\]

Set u=1-exp(-kappa t), including u=1 for the terminal prediction, and define
g_(n,q)(u,x)=fhat_(n,q)(t(u),x)/(1+r(x)). Equations (14) give one common
Lipschitz constant in u on [0,1]. The earlier input Lipschitz and amplitude
bounds give common local spatial equicontinuity. Also
|g_(n,q)(u,x)|<=B/(1+r(x)), so the spatial tail vanishes uniformly.

These functions lie on G_n in a common compact set in the uniform norm.
To check compactness directly, first choose a large input ball to control
the tail. A finite grid on this ball times [0,1] controls the function through
the common continuity bounds. Quantizing bounded values on this finite grid
gives a finite net at each positive tolerance. Thus the set is totally
bounded; its closed envelope is compact in the complete continuous-function
space. Replacing a predictor by zero off G_n changes it only on an event whose
probability tends to zero and puts all laws on this compact set.

Probability laws on a compact metric set have weakly convergent subsequences,
obtained by diagonal extraction on successively finer finite covers. It follows
that every fixed-q predictor sequence has a subsequential population-predictor
law. A diagonal extraction gives a joint limit for any countable collection
of orders as well. This compactness statement identifies no population ODE.

To prove (6), fix q and one rational time/input pair. Equations (1), (8),
and dense convergence imply that the probability of violating
|fhat_(n,q)-f_D|<=C_*r A(q)+epsilon tends to zero for every epsilon>0.
Evaluation is continuous in the weighted topology. Hence every weak predictor
limit assigns probability zero to the corresponding open violation event.
A countable union over rational pairs and positive rational epsilon, followed
by continuity, proves the inequality simultaneously for all finite times and
inputs; (14) extends it to the terminal time. Amplitude bounds give the other
part 2B. This proves (6), and integration proves (7). The same argument works
simultaneously over the countable integer orders in a joint limit family.

Every possible population predictor limit is therefore within the same
deterministic order envelope of f_D. This is stronger than a statement merely
assuming a population predictor exists. It does not prove that the limit is
deterministic, unique at fixed q, or generated by a uniquely restartable
autonomous population closure. No such claim is needed for the error bound.

## 7. The boundary of the whole-input claim

For a bounded input domain, (5)--(7) are unweighted uniform guarantees over
the entire domain. For a fixed probability law on unbounded R^d, (2)--(4)
and (7) are full-domain RMS guarantees. Over all of R^d without an input
weight or a probability law, the current unconditional estimate is only
bounded by 2B at large radii, and need not vanish uniformly in that radius.

WHOLE_INPUT_PREDICTION_ROUTE.md proves an optional observation lemma under
a uniform anti-concentration assumption on the trained dense first-row
projections. It also shows why Gaussian initialization plus small L2 motion
alone does not imply that trained-row assumption. Those examples are
diagnostics of an estimate, not counterexamples to actual canonical training.
No such assumption is added to the test-RMSE theorem above.

Changing from parameter discrepancy to predictions therefore gives a more
direct and broader input-law interpretation, but has not by itself improved
the explicit order exponent beyond the inherited q^(-1+o(1)) envelope.
The exact C/q endpoint, an explicit finite-width sampling rate, unique fixed-q
population-closure identification, and unweighted whole-R^d convergence remain
separate open claims in the present theory.

## 8. Sources and internal check status

The complete companion observation derivation is WHOLE_INPUT_PREDICTION_ROUTE.md.
The separate population-limit derivation is POPULATION_TEST_LIMIT_ROUTE.md.
The prior discrepancy proof is SLOW_ORDER_UNIFORM_BOUND.md, with its specified
Gaussian/energy inputs. The spectral-slack source is used only for uniform
time regularity of closure predictor limit points, not to assume closure
population existence. Check coverage and final file hashes are recorded in
the study README. These are study-level deductions, not promotion or a new
published population-closure theorem.
