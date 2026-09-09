## 8. Comparison: the shallow characteristic population

This is a one-hidden-layer nonlinear comparison, not an extension of the
three-hidden-layer linear theorem to nonlinear activations. Take one datum
\(m=d=1,x_1=1,y_1=y\in\mathbb R\), a common mobility \(\kappa\ge0\),
and full squared loss \(\mathcal L_n=(f_n-y)^2\). Assume

\[
\phi\in C^2(\mathbb R),\qquad
\|\phi'\|_\infty+\|\phi''\|_\infty<\infty,\qquad
|\phi(z)|\le C(1+|z|).
\tag{EC8.1}
\]

There is no condition \(\mathbb E\phi(G)^2=1\). Write
\(a_i=W_i^{(2)},u_i=W_i^{(1)}\), with all initial coordinates independent
\(N(0,1)\). Thus the stored readout has variance one. The two mobilities
are \(n\kappa,n\kappa\), and the exact finite equations are

\[
\begin{gathered}
f_n=\frac1n\sum_i a_i\phi(u_i),\qquad r_n=f_n-y,\\
\dot a_i=-2\kappa r_n\phi(u_i),\qquad
\dot u_i=-2\kappa r_n a_i\phi'(u_i),\\
K_n=\frac1n\sum_i\{\phi(u_i)^2+a_i^2\phi'(u_i)^2\},\qquad
\dot r_n=-2\kappa r_nK_n.
\end{gathered}
\tag{EC8.2}
\]

On the fixed mark probability space \((\mathbb R^2,\gamma_2)\), let
\((a_0,u_0)\) be the two independent standard Gaussian coordinate maps.
The population fields \(A=W^{(2)}\), \(U=Z^{(1)}\) and the scalar residual
solve

\[
\begin{aligned}
\dot A&=-2\kappa r\phi(U),&\dot U&=-2\kappa r A\phi'(U),\\
K&=\mathbb E[\phi(U)^2+A^2\phi'(U)^2],&
\dot r&=-2\kappa rK,
\end{aligned}
\quad (A,U,r)(0)=(a_0,u_0,-y).
\tag{EC8.3}
\]

**Theorem EC8.** There is a unique global canonical marked solution of
(EC8.3). Its fields have every finite moment, uniformly on each compact
physical-time interval, and

\[
f=\mathbb E[A\phi(U)]=y+r,\qquad \mathcal L=r^2.
\tag{EC8.4}
\]

For every fixed \(T<\infty\),

\[
\sup_{0\le t\le T}
\bigl(|f_n-f|+|K_n-K|+|r_n-r|+|r_n^2-r^2|\bigr)
\xrightarrow{\mathbb P}0.
\tag{EC8.5}
\]

The two separate block energies in (EC8.2) also converge uniformly. Under
the nested coupling using one infinite iid mark sequence, these convergences
are almost sure. No empirical path-law convergence is needed or asserted.
The restart state is the full marked pair \((A,U)\) and \(r\), with
\(r=\mathbb E[A\phi(U)]-y\); the tuple \((f,K,r)\) is not specified
as a restart state. One admissible restart domain is marked pairs with
every finite moment and this consistency relation. This includes every
state reached from the canonical initialization.

**Proof.** First construct characteristics on both signs of feature time:

\[
\partial_s\widehat A_s=\phi(\widehat U_s),\qquad
\partial_s\widehat U_s=\widehat A_s\phi'(\widehat U_s),\qquad
(\widehat A_0,\widehat U_0)=(a_0,u_0).
\tag{EC8.6}
\]

The vector field is locally Lipschitz on \(\mathbb R^2\). The integral
equations and (EC8.1), followed by the elementary integral Grönwall bound,
give, for every finite \(S\),

\[
1+|\widehat A_s|+|\widehat U_s|
\le e^{C_\phi S}(1+|a_0|+|u_0|),\qquad |s|\le S.
\tag{EC8.7}
\]

Here the same estimate is applied to the reversed vector field for negative
times. It precludes finite-time escape in the finite-dimensional ODE and
therefore proves global characteristic existence and uniqueness. Local
existence itself follows from the integral-map contraction on a bounded
ball with time length smaller than the inverse of its Lipschitz constant.

Set

\[
F(s)=\mathbb E[\widehat A_s\phi(\widehat U_s)],\quad
H_s=\phi(\widehat U_s)^2+\widehat A_s^2\phi'(\widehat U_s)^2.
\tag{EC8.8}
\]

The integrands in (EC8.8) have a quadratic envelope in
\(J=1+|a_0|+|u_0|\), uniformly on \([-S,S]\). Differentiating along
(EC8.6) gives

\[
\partial_s[\widehat A_s\phi(\widehat U_s)]=H_s,\qquad
\partial_sH_s=4\widehat A_s\phi(\widehat U_s)
                 \phi'(\widehat U_s)^2
 +2\widehat A_s^3\phi'(\widehat U_s)^2\phi''(\widehat U_s).
\tag{EC8.9}
\]

The last expression is bounded by \(C_SJ^3\). Gaussian tails make all
powers of \(J\) integrable. Difference quotients may consequently be
integrated by the dominated convergence theorem, giving
\(F'(s)=\mathbb E H_s=:K(s)\ge0\), with continuous \(K\).
Independence and centering of \(a_0\) give \(F(0)=0\).

Solve the scalar physical clock

\[
\dot s=-2\kappa(F(s)-y),\qquad s(0)=0.
\tag{EC8.10}
\]

Along every local solution,
\(r(t)=F(s(t))-y\) obeys

\[
r(t)=-y\exp\left(-2\kappa\int_0^tK(s(v))\,dv\right),\qquad
|s(t)|\le2\kappa|y|t.
\tag{EC8.11}
\]

These identities follow by differentiating \(F(s)-y\) and solving its
scalar linear equation. They hold also when no root of \(F(s)=y\) exists.
The second bound prevents a finite-time escape of the clock. Setting
\((A,U)(t)=(\widehat A,\widehat U)_{s(t)}\) proves (EC8.3)--(EC8.4)
and all moment bounds. Conversely, for any classical marked solution in
this moment class, define \(s(t)=-2\kappa\int_0^t r(v)\,dv\).
For each mark, uniqueness of the nonautonomous equation with this scalar
coefficient identifies its fields with (EC8.6) evaluated at \(s(t)\).
Also differentiation under the expectation preserves (EC8.4). It must
therefore satisfy (EC8.10), proving uniqueness. This proof starts at any
of the stated consistent restart states: (EC8.7) then uses
\(1+|A_*|+|U_*|\), and the clock bound uses \(|r_*|\).

We give the uniform empirical step rather than assuming a continuous-time
law of large numbers. For any one of the integrands in (EC8.8), or either
summand of \(H_s\), there is an integrable random Lipschitz constant
\(C_SJ^3\) on \([-S,S]\). Indeed the derivatives of the two summands are
\(2\widehat A\phi(\widehat U)\phi'(\widehat U)^2\) and
\(2\widehat A\phi(\widehat U)\phi'(\widehat U)^2+
2\widehat A^3\phi'(\widehat U)^2\phi''(\widehat U)\).
All these variables have finite fourth moments. For centered iid \(X_i\)
with a finite fourth moment,

\[
\mathbb E\left|\frac1n\sum_{i=1}^n X_i\right|^4
=\frac{n\mathbb E X_1^4+3n(n-1)(\mathbb E X_1^2)^2}{n^4}
\le\frac{C}{n^2}.
\tag{EC8.12}
\]

Markov's inequality and the summability of \(n^{-2}\) imply almost-sure
convergence of the averages: the probability of an error exceeding
\(\varepsilon\) for some \(n\ge N\) is bounded by a tail of that
summable series. Apply this to a countable sequence of finite rational
nets and to the Lipschitz envelope. If \(g_s\) is one of our integrands,
a net of spacing at most \(\delta\) gives

\[
\sup_{|s|\le S}|\mathbb E_n g_s-\mathbb E g_s|
\le\max_{q\text{ in net}}|\mathbb E_n g_q-\mathbb E g_q|
 +\delta(\mathbb E_n C_SJ^3+\mathbb E C_SJ^3).
\tag{EC8.13}
\]

Here \(\mathbb E_n\) is the ordinary average over the first \(n\)
marks. First take \(n\to\infty\), then \(\delta\downarrow0\).
This proves almost-sure uniform convergence of \(F_n,K_n\) and both
block energies on every fixed compact feature interval.

At finite width the exact flow is the same set of characteristics at
the common clock \(s_n\), where
\(\dot s_n=-2\kappa(F_n(s_n)-y)\). Its true initial residual is
\(F_n(0)-y\). Since \(F_n'=K_n\ge0\), its residual equation gives
\(|s_n(t)|\le2\kappa|F_n(0)-y|t\) on every local interval;
this proves global finite flow as well. Eventually almost surely
\(|F_n(0)|\le1\). Both clocks then stay in
\([-S_T,S_T]\), with \(S_T=2\kappa(|y|+1)T+1\).
If \(M_T=\sup_{|s|\le S_T}|F'(s)|\) and
\(\epsilon_n=\sup_{|s|\le S_T}|F_n(s)-F(s)|\), subtracting the clock
integral equations gives

\[
\sup_{v\le t}|s_n(v)-s(v)|
\le2\kappa T\epsilon_n e^{2\kappa M_TT},\qquad t\le T.
\tag{EC8.14}
\]

The estimate follows by iteration of the inequality
\(E(t)\le2\kappa T\epsilon_n+2\kappa M_T\int_0^tE(v)dv\).
Uniform empirical convergence and uniform continuity of the deterministic
readouts now apply at these converging clocks. This proves (EC8.5) and
the block-energy assertion. Almost-sure convergence under this coupling
implies the stated intrinsic convergence in probability because each
coupled width has the prescribed law. If \(\kappa=0\), all clocks are
zero and the same empirical argument applies directly. \(\square\)

