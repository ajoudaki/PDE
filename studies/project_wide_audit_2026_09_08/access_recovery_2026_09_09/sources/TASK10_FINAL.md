## Resolution

Under the stated resolution standard, the problem remains **unresolved**.

There is a unique viable scaling regime and an explicit bounded nonlinear activation for which every requested nondegeneracy appears with strictly positive leading coefficients. Thus there is no scaling-level or local-dynamics obstruction. However, a complete affirmative proof still requires a compact-time propagation theorem for an adaptive Gaussian operator/traffic law. Ordinary neuron or edge laws provably do not close, while no universal argument rules out every admissible enriched current-state law. Therefore neither “yes” nor “no” is presently justified.

No project files were inspected.

## 1. Exact causal skeleton

Write
\[
A_i=W_i^{(1)},\qquad U_{ji}=W_{ji}^{(2)},\qquad v_j=W_j^{(3)},
\]
\[
H_i=\phi(A_i),\qquad B=UH,\qquad
q_j=v_j\phi'(B_j),\qquad e=f_n-1.
\]

The continuous gradient flow associated with the required interpolation is
\[
\dot A=-2e\lambda_1\,\phi'(A)\odot U^\top q,
\]
\[
\dot U=-2e\lambda_2\,qH^\top,
\qquad
\dot v=-2e\lambda_3\,\phi(B).
\]

Let \(D_A=\operatorname{diag}(\phi'(A_i)^2)\). Then
\[
\dot B=-2e\Big[
\lambda_2\|H\|^2I+\lambda_1UD_AU^\top
\Big]q.
\]

The three exact kernel pieces are
\[
K_1=\lambda_1\|\phi'(A)\odot U^\top q\|^2,
\]
\[
K_2=\lambda_2\|H\|^2\|q\|^2,
\qquad
K_3=\lambda_3\|\phi(B)\|^2.
\]

Consequently, for the continuous flow,
\[
\dot f_n=-2eK_n,\qquad
\dot L_n=-4K_nL_n.
\]

For the piecewise-linear exact-GD interpolation, the following identity holds exactly on every open grid interval:
\[
V_{n}^{(1)}(t)^2
=
4e_n(t_k)^2\,\frac{\lambda_{1,n}}n\,K_{1,n}(t_k),
\qquad t\in(t_k,t_{k+1}).
\]

This identity is the decisive scale constraint.

## 2. Forced scaling lemma

Assume all requested convergence and uniform-integrability properties hold. Then necessarily
\[
\sigma_{1,n}^2\longrightarrow s^2\in(0,\infty),
\qquad
n\sigma_{2,n}^2\longrightarrow\beta\in(0,\infty),
\]
\[
\frac{\lambda_{1,n}}n\longrightarrow\alpha_1\in(0,\infty),
\qquad
\lambda_{2,n}\longrightarrow\alpha_2\in(0,\infty),
\qquad
n\lambda_{3,n}\longrightarrow\alpha_3\in(0,\infty),
\]
and
\[
n^2\sigma_{3,n}^2\longrightarrow\tau^2\in[0,\infty).
\]

Indeed:

1. The first hidden marginal at \(t=0\) is \(N(0,\sigma_{1,n}^2)\), giving the first limit.

2. Conditionally on \(A(0)\),
   \[
   B_j(0)\sim N\!\left(
   0,\sigma_{2,n}^2\sum_i\phi(A_i(0))^2
   \right).
   \]
   Since \(\mathbb E\phi(N(0,s^2))^2>0\), finite positive second-layer variance forces \(n\sigma_{2,n}^2\to\beta>0\).

3. Since \(e\) stays bounded away from zero on any compact interval on which \(\int K<\infty\), integration of
   \[
   V_{n}^{(1)2}=4e_n^2(\lambda_{1,n}/n)K_{1,n}
   \]
   and positivity of both limiting integrals force \(\lambda_{1,n}/n\to\alpha_1\in(0,\infty)\).

4. Since
   \[
   K_{3,n}=(n\lambda_{3,n})\frac1n\sum_j\phi(B_j)^2
   \]
   and the empirical factor has a positive finite limit, \(n\lambda_{3,n}\to\alpha_3\in(0,\infty)\).

5. Gaussian conditioning at initialization gives
   \[
   \frac{K_{1,n}(0)}
   {(\lambda_{1,n}/n)(n^2\sigma_{3,n}^2)}
   \xrightarrow{\mathbb P}
   \beta\,
   \mathbb E\phi'(X)^2\,
   \mathbb E\phi'(Z)^2>0,
   \]
   where \(X\sim N(0,s^2)\) and
   \(Z\sim N(0,\beta\mathbb E\phi(X)^2)\).
   Finite convergence of \(K_{1,n}(0)\) therefore forces \(n^2\sigma_{3,n}^2=O(1)\), and full-sequence convergence pins its limit.

6. With \(C=nv\) and \(d=C\phi'(B)\),
   \[
   K_{2,n}
   =
   \lambda_{2,n}
   \left\langle\phi(A)^2\right\rangle_n
   \left\langle d^2\right\rangle_n.
   \]
   The output update generates nonzero \(d\) immediately. Hence \(\lambda_{2,n}\to0\) would kill \(K_2\). Conversely,
   \[
   V_{n}^{(2)2}
   \ge
   4e_n^2\lambda_{2,n}
   \left\langle\phi(A)^2\right\rangle_n K_{2,n},
   \]
   so \(\lambda_{2,n}\) cannot diverge.

It also follows that
\[
\operatorname{Var}f_n(0)=O(n^{-1}),
\qquad
f_n(0)\xrightarrow{\mathbb P}0.
\]

Thus \(f(0)=0\), and the step-size assumption necessarily implies
\[
\eta_{0,n}n\longrightarrow0.
\]

## 3. Explicit affirmative blueprint

Take
\[
\phi(z)=2+\sin z,
\]
\[
\sigma_{1,n}^2=1,\qquad
\sigma_{2,n}^2=\frac1n,\qquad
\sigma_{3,n}^2=\frac1{n^4},
\]
\[
\lambda_{1,n}=n,\qquad
\lambda_{2,n}=1,\qquad
\lambda_{3,n}=\frac1n,
\]
and, for example,
\[
\eta_{0,n}=e^{-n^5}.
\]

The output variance is positive for every finite \(n\), while \(C(0)=nW^{(3)}(0)\to0\).

Using normalized inner products \(\langle x,y\rangle_n=n^{-1}x^\top y\), define
\[
C=nv,\qquad H=\phi(A),\qquad B=UH,\qquad
D=C\phi'(B).
\]

The balanced flow is exactly
\[
\dot A=-2e\,\phi'(A)\odot U^\top D,
\]
\[
\dot C=-2e\,\phi(B),
\qquad
\dot U=-\frac{2e}{n}DH^\top.
\]

Its kernel is
\[
K_1=\left\langle
\big(\phi'(A)\odot U^\top D\big)^2
\right\rangle_n,
\]
\[
K_2=\langle H^2\rangle_n\langle D^2\rangle_n,
\qquad
K_3=\langle\phi(B)^2\rangle_n.
\]

Furthermore,
\[
\dot B=-2e
\left[
\langle H^2\rangle_nI+
U\operatorname{diag}(\phi'(A)^2)U^\top
\right]D.
\]

This is nonlinear and all three terms are order one.

Because \(1\le\phi\le3\),
\[
K_3(t)\ge1.
\]
Writing \(r=1-f=-e\), one obtains
\[
\dot r=-2Kr,\qquad 0<r(t)\le e^{-2t}.
\]
Consequently, \(C\), the operator norm of \(U-U(0)\), and the normalized \(L^2\) speeds of \(A\) and \(B\) admit dimension-independent bounds. These estimates give the elementary compactness part of the proposed construction, though not the adaptive Gaussian identification discussed below.

## 4. Exact nonlinear workbench

At limiting initialization, \(C(0)=0\). Let
\[
X\sim N(0,1),\qquad
m=\mathbb E\phi(X)^2=\frac{9-e^{-2}}2,
\]
and let
\[
Z\sim N(0,m).
\]
Put
\[
\rho(z)=\phi(z)\phi'(z),\qquad
R=\mathbb E\rho(Z)^2>0.
\]

Let
\[
M_0=mI+
U_0\operatorname{diag}(\phi'(A_0)^2)U_0^\top
\]
and
\[
J=\lim_{n\to\infty}
\left\langle
\phi'(A_0)^2\big(U_0^\top\rho(B_0)\big)^2
\right\rangle_n.
\]

Gaussian conditioning gives
\[
J=
\mathbb E\phi'(X)^2\,R
+
\big(\mathbb E\rho'(Z)\big)^2
\mathbb E[\phi'(X)^2\phi(X)^2]>0.
\]

The finite-width Taylor equations, followed by their fixed-order Gaussian limits, give
\[
C(t)=2t\phi(B_0)+O(t^2),
\qquad
D(t)=2t\rho(B_0)+O(t^2),
\]
\[
A(t)-A_0
=
2t^2\phi'(A_0)U_0^\top\rho(B_0)+O(t^3),
\]
\[
B(t)-B_0
=
2t^2M_0\rho(B_0)+O(t^3).
\]

Therefore
\[
K_1(t)=4Jt^2+o(t^2),
\]
\[
K_2(t)=4mRt^2+o(t^2),
\]
\[
K_3(t)=K_3(0)+4(mR+J)t^2+o(t^2),
\]
and hence
\[
K(t)=K(0)+8(mR+J)t^2+o(t^2).
\]

The hidden speeds satisfy
\[
V^{(1)}(t)^2=16Jt^2+o(t^2),
\]
\[
V^{(2)}(t)^2
=
16t^2\,
\mathbb E\!\left[(M_0\rho(B_0))^2\right]
+o(t^2),
\]
where
\[
\mathbb E[(M_0\rho(B_0))^2]\ge m^2R>0.
\]

Their squared displacements are respectively
\[
4Jt^4+o(t^4),
\qquad
4\mathbb E[(M_0\rho(B_0))^2]t^4+o(t^4).
\]

There is also an exact finite-width cold-start identity. If \(v(0)=0\), then
\[
K_1''(0)
=
8\lambda_1\lambda_3^2
\rho(B)^\top
U\operatorname{diag}(\phi'(A)^2)U^\top
\rho(B),
\]
\[
K_2''(0)
=
8\lambda_2\lambda_3^2
\|\phi(A)\|^2\|\rho(B)\|^2,
\]
and
\[
K_3''(0)=K_1''(0)+K_2''(0).
\]
Thus
\[
K''(0)=2\big(K_1''(0)+K_2''(0)\big)>0
\]
whenever \(\rho(B)\ne0\). A non-affine \(C^2\) activation cannot satisfy \(\phi\phi'\equiv0\), so this obstruction cannot occur for a nondegenerate Gaussian \(B\).

Finally,
\[
\dot f(0)=2K_3(0)>0,
\qquad
\dot L(0)=-4K_3(0)<0.
\]

Thus properties 4, 5, and 7 are locally compatible at strictly positive order.

For \(Y\sim N(0,v)\),
\[
\inf_{a,b}
\mathbb E\left[
(2+\sin Y-aY-b)^2
\right]
=
\frac{1-e^{-2v}}2-ve^{-v}>0,
\]
because this inequality is equivalent to \(\sinh v>v\). Therefore property 6 holds initially in both hidden layers and would persist on a short interval under the requested Wasserstein continuity.

## 5. Why ordinary mean-field closure is false

At a current state, choose \(w\in\mathbb R^n\) with
\[
\langle w,H\rangle_n=0,\qquad
\langle w^2\rangle_n=1.
\]
Set
\[
\Delta U=\frac{\kappa}{n}Dw^\top.
\]

Then
\[
\Delta B=\Delta U\,H=0.
\]
Every individual edge changes only by \(O(n^{-1})\), so the limiting ordinary edge law—including the law of \(\sqrt n\,U_{ji}\)—is unchanged. Nevertheless,
\[
\Delta(U^\top D)
=
\kappa\langle D^2\rangle_nw,
\]
which is order one. Hence the first-layer velocity and \(K_1\) change at leading order.

Therefore the laws of \(A\), \((B,C)\), and any usual one-edge empirical measure do not determine the next update. An admissible state must retain an operator/traffic hierarchy of contractions involving \(U\) and \(U^\top\).

This does not prove nonexistence: such a current operator-valued state is not excluded by property 2.

## 6. The exact missing theorem

A complete affirmative proof would need the following result.

> For the tied Gaussian matrix \(U_n(0)\) and the adaptive rank-one flow above, prove full-sequence convergence in probability, uniformly on compact time intervals, of every finite two-sorted current-state program built from coordinatewise \(C^2\) maps, \(U_n,U_n^\top\), and normalized contractions. Prove uniform moment and tail estimates, identify a unique solution in an intrinsic depth-weighted traffic state space, show that these solutions form a restartable semigroup, and prove the exact-GD/flow diagonal error vanishes.

This is not supplied by fixed-depth tensor-program results: their computation depth is fixed, whereas here \(T/\eta_{0,n}\to\infty\), with a new transpose-response level generated at each depth. The rigorous DMFT theorem of Gerbelot et al. is likewise stated for each fixed discrete \(t\) and explicitly produces memory kernels; it does not provide the needed uniform growing-time-step or restartable traffic theorem. [Rigorous DMFT theorem](https://arxiv.org/abs/2210.06591), [Tensor Programs IV](https://proceedings.mlr.press/v139/yang21c.html).

Action convergence also does not close the gap: for normalized iid random matrices, the available result gives convergent subsubsequences, not the required unique full-sequence marked dynamic limit. [Action convergence of operators and graphs](https://arxiv.org/abs/1811.00626).

Formally writing
\[
\frac{d}{dt}\tau_t(P)=\tau_t(\mathcal D_{\tau_t}P)
\]
does not prove well-posedness: \(\mathcal D\) raises operator-program depth, so low observables couple to an infinite tail. A depth-weighted no-inflow-from-infinity estimate is needed for uniqueness. Without it, the “traffic closure” merely renames the missing theorem.

## Final claim ledger

- Exact gradient identities: **proved**.
- Necessary scaling: **proved conditional on the requested convergence/UI hypotheses**.
- Explicit bounded nonlinear candidate: **exhibited**.
- Both hidden motions, all kernel blocks, nonlinearity, kernel motion, and loss decrease at fixed small-time order: **proved**.
- Closure by ordinary particle or one-edge laws: **ruled out**.
- Compact-time full Gaussian-traffic convergence, uniqueness, restartability, and joint exact-GD limit: **open**.
- Universal impossibility of every enriched law state: **not proved and not supported by the scaling analysis**.

Therefore, exactly as required by the problem’s resolution rule, the answer is: **unresolved**.
