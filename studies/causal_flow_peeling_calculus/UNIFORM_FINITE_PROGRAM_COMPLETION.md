# Uniform Finite-Program Completion

## Claim level

This note proves a reusable completion lemma and applies it to the linear hidden-depth ladder and the one-hidden-layer coordinate flow.  It is the first established component of CFPC.  It does **not** cover a nonlinear adaptive matrix query; that requires the graded source-response norm currently under investigation.

## 1. Uniform Picard peeling lemma

The lemma isolates a simple but important way to cross the fixed-program/continuous-time gap.  The number of Picard stages is chosen from the desired accuracy before the width limit is taken.  Consequently, only a fixed finite program is sent through the static mean-field evaluator.

### Lemma 1 (uniform finite-program approximation)

For each `n`, let `X_n` be a Banach space, let `B_n` be a closed ball, and let

\[
\dot Y_n=F_n(Y_n),\qquad Y_n(0)=Y_{n,0}.
\]

Assume, on events `Omega_n` with probability tending to one:

1. the solution and every Picard iterate below remain in `B_n` on `[0,T]`;
2. uniformly in `n`,
   \[
   \|F_n(y)\|\le M,
   \qquad
   \|F_n(y)-F_n(y')\|\le \Lambda\|y-y'\|
   \quad(y,y'\in B_n);
   \]
3. `Q_n` is a scalar observable with a uniform Lipschitz constant `L_Q` on `B_n`;
4. for every fixed Picard index `k`, the finite program
   \[
   Y_n^{[0]}(t)=Y_{n,0},
   \qquad
   Y_n^{[k+1]}(t)=Y_{n,0}+\int_0^tF_n(Y_n^{[k]}(s))\,ds
   \]
   has a deterministic scalar limit
   \[
   Q_n(Y_n^{[k]}(\cdot))\longrightarrow q^{[k]}(\cdot)
   \quad\text{uniformly on }[0,T].
   \]

Then `q^[k]` converges uniformly to a continuous function `q`, and

\[
\sup_{t\le T}|Q_n(Y_n(t))-q(t)|\longrightarrow0
\]

in probability.

The same assertion holds jointly for every fixed finite family of observables.  If the complement of `Omega_n` and the observables have a uniform-integrability bound of the required order, convergence holds in the corresponding `L^p`.

### Proof

The standard Picard estimate is uniform in `n`.  The first difference obeys

\[
\sup_{s\le t}\|Y_n^{[1]}(s)-Y_n^{[0]}(s)\|\le Mt.
\]

Inductively,

\[
\|Y_n^{[k+1]}(t)-Y_n^{[k]}(t)\|
\le
M\frac{\Lambda^k t^{k+1}}{(k+1)!}.
\]

Summing the tail gives

\[
\sup_{t\le T}\|Y_n(t)-Y_n^{[k]}(t)\|
\le
M\sum_{j=k}^{\infty}
\frac{\Lambda^jT^{j+1}}{(j+1)!}
=:\epsilon_k,
\tag{1}
\]

where `epsilon_k -> 0` independently of `n`.  Hence

\[
\sup_{t\le T}
|Q_n(Y_n(t))-Q_n(Y_n^{[k]}(t))|
\le L_Q\epsilon_k.
\tag{2}
\]

For two indices `k,m`, take `n -> infinity` in the triangle inequality between the two finite programs and use (2).  This shows

\[
\|q^{[k]}-q^{[m]}\|_\infty
\le L_Q(\epsilon_k+\epsilon_m).
\]

Thus the deterministic limits are uniformly Cauchy.  If `q` is their limit, then

\[
\begin{aligned}
\|Q_n(Y_n)-q\|_\infty
&\le L_Q\epsilon_k
+\|Q_n(Y_n^{[k]})-q^{[k]}\|_\infty
+\|q^{[k]}-q\|_\infty.
\end{aligned}
\]

First choose `k` and then take `n -> infinity`.  This proves the claim on `Omega_n`; its complement is negligible.  Uniform integrability gives the last assertion.  No program whose length grows with `n` or with a time mesh was used.  ∎

### Corollary 2 (one-time algebraic state)

Suppose the finite-program convergence in Lemma 1 holds jointly for every finite family from a countable dense typed observable algebra that includes the immutable sources.  Then the limiting evaluations define a positive character `chi_t`.  The family is restartable and satisfies the semigroup law.

### Proof

Positivity and normalization pass to limits of finite-width closed contractions.  At a fixed restart time `s`, append the current state and the unchanged sources to the finite program.  Apply Lemma 1 to Picard iteration on `[s,s+t]`.  The result depends only on their joint character at `s`; it is therefore a current-state transition.  Applying the construction once over `s+t`, or first over `s` and then over `t`, gives the same finite-width flow.  Uniform approximation and uniqueness pass this equality to the limit.  ∎

This corollary does not encode the past in the state: it retains only the current fields and their joint algebraic law with the fixed sources.

## 2. Deep-linear application

Set `phi(s)=s`.  Put

\[
P=G_{L-1}\cdots G_1,
\qquad
x_\ell=G_{\ell-1}\cdots G_1u,
\qquad
b_{\ell+1}=G_{\ell+1}^*\cdots G_{L-1}^*A,
\]

with empty products equal to the identity.  The flow becomes

\[
\dot A=Pu,
\qquad
\dot u=P^*A,
\qquad
\dot G_\ell=b_{\ell+1}\otimes_n x_\ell.
\tag{3}
\]

Write

\[
a=\|A\|_n,
\qquad q=\|u\|_n,
\qquad m_\ell=\|G_\ell\|_{\rm op}.
\]

The normalized rank-one convention gives exactly

\[
\|b\otimes_nx\|_{\rm op}=\|b\|_n\|x\|_n.
\]

Consequently,

\[
\begin{aligned}
\dot a&\le q\prod_jm_j,\\
\dot q&\le a\prod_jm_j,\\
\dot m_\ell&\le
aq\prod_{j\ne\ell}m_j.
\end{aligned}
\tag{4}
\]

If

\[
R=1+a+q+\sum_jm_j,
\]

then, for a constant depending only on depth,

\[
\dot R\le C_LR^{L+1}.
\tag{5}
\]

The exponent in (5) is deliberately non-optimal; it is a uniform scalar majorant.  On every interval lying strictly before the blow-up time of this scalar equation, (4) gives a common state ball.

On that ball, matrix composition and the normalized rank-one map are multilinear bounded operations, so the vector field in (3) has a width-independent Lipschitz constant in

\[
\|(A,u,G_1,\ldots,G_{L-1})\|
=\|A\|_n+\|u\|_n+\sum_\ell\|G_\ell\|_{\rm op}.
\tag{6}
\]

The predictor and raw kernel

\[
f_n=\langle A,Pu\rangle_n,
\]

\[
\Theta_n=
\|Pu\|_n^2
+\sum_{\ell=1}^{L-1}
\|b_{\ell+1}\|_n^2\|x_\ell\|_n^2
+\|P^*A\|_n^2
\tag{7}
\]

are uniformly Lipschitz on the same ball.

Every Picard iterate of (3), and every coefficient of (7) evaluated on it, is a finite expression made only from source matrices, their exact transposes, seed vectors, normalized contractions, and rank-one maps.  It is therefore a fixed finite MFP/Tensor Program.  Its scalar contractions have a joint deterministic limit.  Because the Picard iterates are polynomials in time, coefficientwise convergence is uniform on a compact interval.

For iid Gaussian initialization, `||Gamma_l||op` and the normalized seed norms lie in a deterministic ball with probability tending to one.  Applying Lemma 1 proves:

### Theorem 3 (linear ladder)

For each fixed hidden depth `L`, hence in particular for `L=1,2,3`, the predictor, raw tangent kernel, and every fixed typed polynomial observable converge uniformly in probability on compact intervals certified by the scalar majorant (5).  Their limiting joint character is autonomous, shares the original source and transpose relations, and is restartable.

The theorem is local up to the certified maximal interval because deep-linear feature ascent can blow up.  It is not a statement about descent under a particular loss time change.

## 3. Generic one-hidden-layer application

At hidden depth one there is no inter-hidden Gaussian matrix.  Each coordinate solves the same two-dimensional system

\[
\dot A=\phi(u),
\qquad
\dot u=A\phi'(u).
\tag{8}
\]

Let `Psi_t` denote its flow.  Assume:

1. the vector field in (8) is locally Lipschitz;
2. the initial iid law `mu_0` has the moments needed below;
3. on `[0,T]`, a deterministic envelope supplies an integrable dominating function for `A phi(u)`, `phi(u)^2`, and `A^2 phi'(u)^2`, uniformly over initial points outside a set of arbitrarily small `mu_0` mass.

Then

\[
\mu_t=(\Psi_t)_\#\mu_0
\tag{9}
\]

is the unique one-time limit state.  The empirical measure at width `n` is exactly the empirical measure of iid trajectories `Psi_t(A_i(0),u_i(0))`.  A grid in time, the ordinary law of large numbers on the grid, and equicontinuity from the envelope yield compact-time convergence.  Truncating the initial envelope removes the compact-support restriction by uniform integrability.

Thus

\[
f_\infty(t)=\int A\phi(u)\,d\mu_t,
\]

\[
\Theta_\infty(t)=
\int\left(\phi(u)^2+A^2\phi'(u)^2\right)d\mu_t.
\tag{10}
\]

This is a reusable **coordinate-transport rule**, not an arctangent identity.  It proves the generic one-hidden-layer rung for every activation/initial law satisfying the three stated, directly checkable hypotheses.

## 4. What these results do and do not resolve

The completion lemma converts a width-uniform deterministic approximation into a compact-time mean-field theorem while invoking static Gaussian machinery only at fixed program size.  It completely discharges the continuous-time issue for the deep-linear ladder and the coordinate-only nonlinear rung.

It does not yet supply the needed uniform state norm for a nonlinear adaptive matrix flow.  In normalized `L^2`, the map

\[
(A,z)\mapsto A\odot\phi'(z)
\]

is not locally Lipschitz with a dimension-free constant when `A` is unbounded, and source action on an adaptive vector needs response control.  The next calculus component must build a graded space on which these two operations are tame.  Assuming that component would simply restate the remaining problem.
