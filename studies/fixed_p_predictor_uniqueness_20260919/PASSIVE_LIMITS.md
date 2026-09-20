# Passive predictor limits and readout nonuniqueness

Frozen independent candidate, 2026-09-19. Author: scoped agent
`unique_passive_limits`. Scientific inputs: only the supervisor's prompt containing
the model and requested questions. Process inputs: the supplied AGENTS.md,
RESEARCH_WORKFLOW.md, `solve-math-rigorously`, and `investigate-conjectures`
including its adversarial-audit reference. No other study, established scientific
source, external source, numerical experiment, or other route's findings was read.
This file is a study result, not established repository material. Its arguments
are exact under the stated assumptions; author self-check is not independent
review or promotion. The candidate is frozen for subsequent comparison.

## 1. Model and state-to-predictor continuity

Let both carriers be fixed probability spaces. Take fixed bounded measurable
maps $b_1:\Omega_1\to\mathbb R^{p_1}$ and
$b_2:\Omega_2\to\mathbb R^{p_2}$, and put
$\beta_j=\|b_j\|_{L^2}$. The state is

\[
 S=(w,M,c)\in \mathcal S
 =L^2(\Omega_1;\mathbb R^d)\times\mathbb R^{p_2\times p_1}
       \times L^2(\Omega_2),\qquad d\ge1.
\]

Use the complete product norm
$\|S\|_{\mathcal S}=\|w\|_2+\|M\|_F+\|c\|_2$. Set

\[
 a_w(x)=\mathbb E_1[b_1\tanh(w\cdot x/\sqrt d)],\quad
 H_{w,M}(x)=\tanh(b_2^TMa_w(x)),\quad
 f_S(x)=\langle c,H_{w,M}(x)\rangle_{L^2(\Omega_2)}.
\]

Every integral is well defined: the activations have absolute value at most one,
the carriers have mass one, and $L^2\subset L^1$. No independence between random
state coordinates is assumed. The carrier variables are integration variables,
distinct from any randomness generating the state.

The elementary bounds $|\tanh u-\tanh v|\le|u-v|$ and Cauchy--Schwarz give

\[
 \|a_w(x)\|\le\beta_1,\qquad
 \|a_w(x)-a_{\widetilde w}(x)\|
 \le \frac{\beta_1\|x\|}{\sqrt d}\|w-\widetilde w\|_2.
 \tag{1}
\]

For $S=(w,M,c)$, $\widetilde S=(\widetilde w,\widetilde M,\widetilde c)$,
decompose

\[
 Ma_w-\widetilde M a_{\widetilde w}
 =(M-\widetilde M)a_w+\widetilde M(a_w-a_{\widetilde w}).
\]

Since $|b_2^Tz|\le\|b_2\|\|z\|$, for the closed input ball $B_R$,

\[
 \sup_{x\in B_R}\|H_{w,M}(x)-H_{\widetilde w,\widetilde M}(x)\|_2
 \le\beta_1\beta_2\left(
 \|M-\widetilde M\|_F+
 \frac{R\|\widetilde M\|_{\rm op}}{\sqrt d}
                  \|w-\widetilde w\|_2\right).
 \tag{2}
\]

Finally use $f_S-f_{\widetilde S}=\langle c-\widetilde c,H_{w,M}\rangle
+\langle\widetilde c,H_{w,M}-H_{\widetilde w,\widetilde M}\rangle$ and
$\|H_{w,M}(x)\|_2\le1$. This proves

\[
 \|f_S-f_{\widetilde S}\|_{C(B_R)}
 \le\|c-\widetilde c\|_2+
 \|\widetilde c\|_2\beta_1\beta_2
 \left(\|M-\widetilde M\|_F+
 \frac{R\|\widetilde M\|_{\rm op}}{\sqrt d}
                  \|w-\widetilde w\|_2\right).
 \tag{3}
\]

Consequently, **strong convergence in the displayed state norm implies uniform
predictor convergence on every compact input set**. In particular, if
$S_t\to S_\infty$, then the limit predictor is $f_{S_\infty}$, not merely an
unspecified subsequential continuous function. Taking
$\widetilde S=S_\infty$ in (3) proves the assertion directly.

This implication holds pathwise for random states. On any event on which the
state convergence holds, it holds on all compact input sets simultaneously,
because the same event yields (3) for every finite $R$. It does not assert that
the random state limit, or its predictor, is deterministic.

## 2. Input Lipschitz bounds and finite travel

For $x,z\in\mathbb R^d$, the same calculation gives

\[
 |f_S(x)|\le\|c\|_2,\qquad
 |f_S(x)-f_S(z)|\le L(S)\|x-z\|,
 \quad
 L(S)=\frac{\beta_1\beta_2}{\sqrt d}
       \|c\|_2\|M\|_{\rm op}\|w\|_2.
 \tag{4}
\]

Indeed, first bound the difference of $a_w$ by
$\beta_1\|w\|_2\|x-z\|/\sqrt d$, then apply the matrix, the second
activation, and Cauchy--Schwarz against $c$. Hence any family bounded in the
state norm has uniformly bounded predictors and a common global input Lipschitz
constant. Strong convergence alone gives these uniform bounds on a sufficiently
late time tail; local boundedness gives them on the whole time interval.

Suppose $S:[0,\infty)\to\mathcal S$ is locally absolutely continuous and

\[
 \int_0^\infty\bigl(\|\dot w_t\|_2+
          \|\dot M_t\|_F+\|\dot c_t\|_2\bigr)\,dt<\infty.
 \tag{5}
\]

The fundamental integral formula for an absolutely continuous Hilbert-space
curve yields, for $u\ge t$,

\[
 \|S_u-S_t\|_{\mathcal S}
 \le\int_t^u\|\dot S_s\|_{\mathcal S}\,ds.
\]

The integrable tail tends to zero, so $S_t$ is Cauchy as $t\to\infty$.
Completeness gives $S_\infty$, and (3) proves uniform convergence on compacts.
More quantitatively, if $T(t)=\int_t^\infty\|\dot S_s\|_{\mathcal S}ds$,

\[
 \|f_{S_t}-f_{S_\infty}\|_{C(B_R)}
 \le\left[1+\beta_1\beta_2\|c_\infty\|_2
       \left(1+\frac{R\|M_\infty\|_{\rm op}}{\sqrt d}\right)\right]T(t).
 \tag{6}
\]

The same proof covers finite total variation in the state norm: differences on a
tail are bounded by tail variation. In discrete time it covers
$\sum_k\|S_{k+1}-S_k\|_{\mathcal S}<\infty$. Each is a sufficient condition,
not an assertion about the variation of any unspecified training process.

Finite **squared-speed energy** is weaker. Section 4 constructs an exact-fit
family $c_q$ with $f_{c_q}(x)=f_{c_0}(x)+q$. Taking
$q(t)=\sin\log(1+t)$, and leaving hidden features fixed, gives a bounded smooth
state curve with constant zero training loss and no limiting query prediction.
Its squared-speed integral is bounded by

\[
 \frac{1}{\|r\|_2^2}\int_0^\infty\frac{dt}{(1+t)^2}
 =\frac{1}{\|r\|_2^2}<\infty,
\]

because $\dot c_t=\cos\log(1+t)\,r/[(1+t)\|r\|_2^2]$.
This is a generic admissible state curve, **not a claimed gradient-flow
trajectory**. It disproves an inference from bounded state, zero loss, and finite
squared-speed energy alone to predictor convergence.

## 3. What query meshes can and cannot establish

For any two functions $f,g$ with Lipschitz constants $L_f,L_g$, any compact
$K$, and any finite $\eta$-net $Z\subset K$, choose for each $x\in K$
some $z\in Z$ with $\|x-z\|\le\eta$. The triangle inequality proves

\[
 \|f-g\|_{C(K)}
 \le\max_{z\in Z}|f(z)-g(z)|+(L_f+L_g)\eta.
 \tag{7}
\]

Thus a uniformly Lipschitz family that is Cauchy at every point of a dense subset
of $K$ is uniformly Cauchy on $K$: choose a finite mesh from that dense subset,
first make the last term small, then make all finitely many mesh differences
small. Its uniform limit is continuous because uniform limits preserve the
epsilon--delta continuity bound. The same argument proves that two Lipschitz
limits agreeing on a dense subset agree on $K$.

A bounded state family also has subsequential compactness of its predictors on
$K$. To verify this without a compactness assumption on the state space, take a
countable dense subset of $K$, extract successive subsequences on which the
bounded real predictions at its first, second, and subsequent points converge,
and use the diagonal subsequence. Formula (7) makes that subsequence uniformly
Cauchy. **Subsequential predictor compactness does not identify its limit or
give convergence of the entire family.**

Now let the finite training law have inputs $x_1,\ldots,x_n$, labels
$y_1,\ldots,y_n$, and weights $\mu_i>0$, with

\[
 \mathcal L(f)=\sum_{i=1}^n\mu_i(f(x_i)-y_i)^2,
 \qquad \mu_{\min}=\min_i\mu_i>0.
\]

Every individual residual obeys
$|f(x_i)-y_i|\le\sqrt{\mathcal L(f)/\mu_i}$. For predictors $f,g$ and a query
$x$, comparison through training point $x_i$ gives

\[
 |f(x)-g(x)|\le
 \sqrt{\mathcal L(f)/\mu_i}+\sqrt{\mathcal L(g)/\mu_i}
 +(L_f+L_g)\|x-x_i\|.
 \tag{8}
\]

Writing $\delta_X(K)=\sup_{x\in K}\min_i\|x-x_i\|$, it follows that

\[
 \|f-g\|_{C(K)}\le
 \frac{\sqrt{\mathcal L(f)}+\sqrt{\mathcal L(g)}}{\sqrt{\mu_{\min}}}
 +(L_f+L_g)\delta_X(K).
 \tag{9}
\]

Consequently, vanishing loss and a common Lipschitz bound give a quantitative
bound on cross-realization disagreement. A fixed finite training set generally
has positive fill distance on a continuum compact set, so this bound need not
tend to zero. A proof of equality on successively finer query meshes would suffice
by (7); observations or bounds at only the fixed training points do not provide
that premise. Pathwise strong state convergence and finite total state travel
likewise contain no cross-realization comparison premise.

## 4. Exact fitting alternatives in a readout nullspace

Fix a hidden state $h=(w,M)$. Put $H_i=H_h(x_i)$ and $H_x=H_h(x)$, regarded
as vectors in the real Hilbert space $L^2(\Omega_2)$. Assume the $n+1$ vectors
$H_1,\ldots,H_n,H_x$ are linearly independent. Define

\[
 G_{ij}=\langle H_i,H_j\rangle,\quad
 g_i=\langle H_i,H_x\rangle,\quad
 c_* =\sum_j(G^{-1}y)_jH_j,
 \qquad r=H_x-\sum_j(G^{-1}g)_jH_j.
 \tag{10}
\]

These expressions exist because, for nonzero $v\in\mathbb R^n$,
$v^TGv=\|\sum_i v_iH_i\|_2^2>0$, so $G$ is invertible.
For each $i$, direct multiplication gives
$\langle c_*,H_i\rangle=y_i$ and $\langle r,H_i\rangle=0$.
The additional independence gives $r\ne0$. Also
$\langle r,H_x\rangle=\|r\|_2^2$, by substituting the expression for $H_x$
and using these orthogonality identities. Therefore, for every $q\in\mathbb R$,

\[
 c_q=c_*+\frac{q}{\|r\|_2^2}r
 \quad\Longrightarrow\quad
 f_{(h,c_q)}(x_i)=y_i\ \ (1\le i\le n),\qquad
 f_{(h,c_q)}(x)=f_{(h,c_*)}(x)+q.
 \tag{11}
\]

Every readout lies in $L^2$, with
$\|c_q\|_2^2=\|c_*\|_2^2+q^2/\|r\|_2^2$. Thus even a fixed cap
$\|c\|_2\le C>\|c_*\|_2$ permits a nontrivial interval of query alternatives,
$|q|\le\|r\|_2\sqrt{C^2-\|c_*\|_2^2}$.

These are **represented exact-fit states**. No argument here says that two of
them are reachable from a specified common initialization under a specified
canonical full-network noisy process. Reachability and its probability law are
additional dynamical obligations.

The independence condition has a concrete fixed-width instance in the supplied
architecture. Set $d=p_1=p_2=1$, let $\Omega_1$ be a singleton, put $b_1=w=M=1$,
and let $\Omega_2$ have two equally weighted atoms with $b_2=1,2$, respectively.
Then

\[
 a(x)=\tanh x,\qquad H(x)=(\tanh(a(x)),\tanh(2a(x))).
 \tag{12}
\]

Take training input $x_1=1$ and query $x=2$. Both first components are positive,
and their component ratios are

\[
 \frac{\tanh(2a)}{\tanh a}=\frac{2}{1+\tanh^2a}.
\]

This ratio is strictly decreasing for $a>0$, while $a(2)>a(1)>0$; the two
vectors are linearly independent. All carrier features are bounded, and all
displayed state coordinates have finite required norms. No width limit is used.

## 5. Frozen-feature noise comparator and its limitation

This section is a deliberately specified **frozen-feature comparator**, not the
full trained hidden-state dynamics or an identification with an unspecified
canonical noise model. Use the architecture (12), its single training feature
$u=H(1)$, its query $H_x=H(2)$, and any nonzero label $y$. Put

\[
 \gamma=\|u\|_2^2>0,\qquad
 r=H_x-\frac{\langle u,H_x\rangle}{\gamma}u,\qquad
 e=r/\|r\|_2,\qquad \lambda=2\mu\gamma,
\]

where $\mu>0$ is the training weight. Here $\langle e,u\rangle=0$ and
$\langle e,H_x\rangle=\|r\|_2>0$. Let $\xi$ take values $+1,-1$ with equal
probability, fix $\sigma>0$, and start all realizations at $c(0)=0$. The
randomly forced readout gradient equation is

\[
 \dot c_t=-2\mu(\langle c_t,u\rangle-y)u
                 +\sigma\xi e^{-t}e.
 \tag{13}
\]

Direct differentiation and orthogonality verify its exact solution

\[
 c_t=\frac{y}{\gamma}(1-e^{-\lambda t})u
                 +\sigma\xi(1-e^{-t})e.
 \tag{14}
\]

Its loss is $\mu y^2e^{-2\lambda t}$, and

\[
 \int_0^\infty\|\dot c_t\|_2dt
 \le\frac{|y|}{\sqrt\gamma}+\sigma<\infty,\qquad
 c_\infty=\frac{y}{\gamma}u+\sigma\xi e.
\]

Thus every realization has finite total state travel, converges strongly, and
fits the training sample exactly in the limit. Nonetheless its limiting query
prediction is

\[
 f_\infty(x)=\frac{y}{\gamma}\langle u,H_x\rangle
                 +\sigma\xi\|r\|_2,
 \tag{15}
\]

which takes two distinct values. This already proves that the passive convergence
conditions plus exact fitting cannot by themselves force a common predictor
across random forcings. The random sign is fixed at time zero; (13) is random
forcing, not white noise.

A genuine diffusion version with the same deterministic initialization is also
explicit. For a real standard Brownian motion $B$, prescribe

\[
 dc_t=-2\mu(\langle c_t,u\rangle-y)u\,dt
                +\sigma\mathbf1_{[0,1]}(t)e\,dB_t.
 \tag{16}
\]

The solution is the first term of (14) plus $\sigma B_{t\wedge1}e$, as can be
checked by substituting it into the integral equation. It converges strongly
almost surely to $yu/\gamma+\sigma B_1e$. Its limiting query has variance
$\sigma^2\|r\|_2^2>0$, because $B_1$ has variance one. This argument needs no
infinite-horizon martingale convergence theorem: the stochastic part stops
exactly at time one. Finite state travel is not asserted for (16).

The noise direction is essential. To expose its exact limitation, freeze any
features $H_i$ and set $V=\operatorname{span}\{H_i\}$. Each per-sample squared
loss gradient equals a scalar multiple of $H_i$, and therefore belongs to
$V$. Any trajectory whose readout increments are formed only from these
gradients, including sampled-gradient updates, preserves $P_{V^\perp}c$.
For a continuous model the same conclusion follows by applying the orthogonal
projection to its integral equation when both drift and noise coefficients
lie in $V$.

For a deterministic common initial readout $c_0$, any two strong limiting
readouts produced by such a frozen-feature process and fitting all samples have
the same $V^\perp$ component. Their difference lies in $V$; exact fitting also
makes it orthogonal to every $H_i$, so it lies in $V^\perp$, and hence is zero.
Thus **conditional on existence of exact-fit limits**, pure sampled-gradient
readout dynamics with fixed common features and initialization have the same
limiting readout, even when their transient sample paths differ. This argument
does not require independent $H_i$. It proves neither convergence nor exact
fitting.

Accordingly, (13) and (16) are counterexamples to an inference from passive
conditions, and examples for their specified nullspace forcing. They are not
counterexamples to the preceding frozen sampled-gradient statement, and they
settle no uniqueness question for evolving hidden features under an unspecified
canonical noise law.

## 6. Boundary of the result

The proved implications are: strong state convergence or finite total state
travel gives locally uniform predictor convergence; state bounds give query
Lipschitz estimates and subsequential predictor compactness; fine query meshes
control uniform discrepancies; a readout nullspace supplies explicit represented
exact fits with different query values; and the specified frozen comparators can
converge to noise-dependent exact-fit predictors. No experiment was needed.

What remains outside this route is whether a particular fully trained canonical
process converges, whether its endpoints lie in one predictor equivalence class,
whether its noise reaches readout nullspace alternatives through feature motion,
or whether its own invariants instead select a unique predictor. Those questions
require the actual dynamics and initialization, which were not supplied as
scientific input to this route.
