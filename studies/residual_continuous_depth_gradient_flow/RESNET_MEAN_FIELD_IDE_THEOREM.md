# A compact-time mean-field and continuous-depth theorem for a nonlinear residual network

## Status and scope

This document proves a theorem for a specific scalar residual particle network.  It combines exact continuous-time training with two limits:

1. exact continuous gradient flow in training time;
2. the width limit in a depth-averaged topology, and blockwise at every fixed depth;
3. the continuous-depth limit of the residual architecture.

The limiting object is a single-training-time integro-differential equation (IDE).  Its depth variable is a spatial coordinate, not a second training time.  At each current training time the IDE performs a forward depth solve, a backward adjoint solve, and then one autonomous transport update of the current depth-indexed parameter law.  It stores neither a training history nor a two-time covariance.

The result is not a theorem for a dense, CLT-scaled Gaussian-matrix network.  The architecture below is deliberately a mean-field residual particle architecture.  That distinction is part of the theorem rather than a suppressed substitution.

## 1. Model and notation

Fix a batch size \(B\in\mathbb N\), scalar inputs \(\xi_1,\ldots,\xi_B\), scalar labels \(y_1,\ldots,y_B\), and a learning-rate constant \(\eta>0\).  All are independent of width and depth.

Let \(\sigma(u)=\tanh u\).  A raw neuron parameter is

\[
 \theta=(\alpha,\omega,\beta)\in\mathbb R^3,
\]

and its residual feature is

\[
 \Phi(\theta,x)
 =\sigma(\alpha)\,
  \sigma\!\left(\sigma(\omega)x+\sigma(\beta)\right).
 \tag{1.1}
\]

Thus every raw parameter is unconstrained, but the effective amplitude, slope, and bias are smoothly bounded.  Gradient flow below is Euclidean gradient flow in the raw coordinates \((\alpha,\omega,\beta)\); it is not Euclidean flow in the transformed effective weights.

For depth \(L\ge1\), width \(n\ge1\), and \(h=L^{-1}\), define

\[
 X^{n,L}_{b,0}=\xi_b,
\]

\[
 X^{n,L}_{b,\ell+1}
 =X^{n,L}_{b,\ell}
 +\frac1{nL}\sum_{i=1}^n
   \Phi\!\left(\theta_{\ell i},X^{n,L}_{b,\ell}\right),
 \qquad 0\le\ell<L.
 \tag{1.2}
\]

The identity skip is added after the nonlinear residual branch.  There is no independent trainable skip matrix.  The output and one-sample-averaged MSE are

\[
 F_b^{n,L}=X^{n,L}_{b,L},
 \qquad
 \mathcal E^{n,L}
 =\frac1{2B}\sum_{b=1}^B(F_b^{n,L}-y_b)^2.
 \tag{1.3}
\]

All residual-block parameters are trained by

\[
 \dot\theta_{\ell i}
 =-\eta nL\,\nabla_{\theta_{\ell i}}\mathcal E^{n,L}.
 \tag{1.4}
\]

The factor \(n\) is the mean-field width scaling.  The additional factor \(L\) compensates for the \(L^{-1}\) residual scale.  Section 3 verifies this normalization exactly.

The initial parameters are independent over \((\ell,i)\) and satisfy

\[
 \theta_{\ell i}(0)\sim\rho_0,
 \qquad \rho_0\in\mathcal P_2(\mathbb R^3).
 \tag{1.5}
\]

The shifted Gaussian \(N(m,\Sigma)\), with fixed finite covariance, is the principal example.  Gaussianity is used in Section 13 to give an explicit symmetry-breaking witness, but it is not needed for the convergence theorem.  No Gaussian closure of the evolved law is assumed.

For \(\mu,\nu\in\mathcal P_1(\mathbb R^3)\), let \(W_1(\mu,\nu)\) be the 1-Wasserstein distance.  For two depth-\(L\) profiles set

\[
 d_L(\boldsymbol\mu,\boldsymbol\nu)
 =\frac1L\sum_{\ell=0}^{L-1}W_1(\mu_\ell,\nu_\ell).
 \tag{1.6}
\]

The averaged depth topology is intentional.  A supremum over all individual layer laws is a stronger statement and is not part of the joint width-depth theorem.

## 2. The limiting single-time IDE

Let \(s\in[0,1]\) denote continuous depth and \(t\ge0\) training time.  The current state is a measurable profile

\[
 s\longmapsto\rho_t(s)\in\mathcal P_1(\mathbb R^3).
\]

Given this current profile, define the forward features by

\[
 \partial_s x_b(s,t)
 =\int_{\mathbb R^3}\Phi(\theta,x_b(s,t))\,\rho_t(s,d\theta),
 \qquad x_b(0,t)=\xi_b.
 \tag{2.1}
\]

Define the unit terminal sensitivities by

\[
 -\partial_s r_b(s,t)
 =r_b(s,t)
  \int_{\mathbb R^3}\partial_x\Phi(\theta,x_b(s,t))
       \,\rho_t(s,d\theta),
 \qquad r_b(1,t)=1.
 \tag{2.2}
\]

Put

\[
 f_b(t)=x_b(1,t),
 \qquad
 p_b(s,t)=\frac1B r_b(s,t)(f_b(t)-y_b).
 \tag{2.3}
\]

The continuum loss is

\[
 \mathcal E(t)=\frac1{2B}\sum_{b=1}^B(f_b(t)-y_b)^2.
\]

The current parameter velocity is

\[
 v_t(s,\theta)
 =-\eta\sum_{b=1}^B
 p_b(s,t)\nabla_\theta\Phi(\theta,x_b(s,t)).
 \tag{2.4}
\]

The IDE is the continuity equation

\[
 \partial_t\rho_t(s)
 +\nabla_\theta\!\cdot
  \bigl(\rho_t(s)v_t(s,\cdot)\bigr)=0,
 \qquad \rho_0(s)=\rho_0.
 \tag{2.5}
\]

Equations (2.1)--(2.5) are autonomous in training time: the right-hand side at \(t\) is a function only of the current profile \(\rho_t\).  The forward and backward depth equations are instantaneous current-state readouts, not stored histories.

A **characteristic solution** of (2.5) is a profile of maps \(\Theta_t(s,\cdot)\) such that

\[
 \frac d{dt}\Theta_t(s,a)
 =v_t(s,\Theta_t(s,a)),
 \qquad \Theta_0(s,a)=a,
 \tag{2.6}
\]

for \((ds\otimes\rho_0)\)-almost every \((s,a)\), and

\[
 \rho_t(s)=(\Theta_t(s,\cdot))_\#\rho_0.
 \tag{2.7}
\]

It is a weak solution because, for every \(\psi\in C_c^1(\mathbb R^3)\), differentiation of \(\psi(\Theta_t(s,a))\) gives, for almost every depth \(s\) and almost every training time \(t\),

\[
 \frac d{dt}\int\psi(\theta)\rho_t(s,d\theta)
 =\int\nabla\psi(\theta)\cdot v_t(s,\theta)\rho_t(s,d\theta).
 \tag{2.8}
\]

## 3. Exact finite-width identities

Define

\[
 A^{n,L}_{b,\ell}
 =\frac1n\sum_{i=1}^n
  \partial_x\Phi(\theta_{\ell i},X^{n,L}_{b,\ell}).
 \tag{3.1}
\]

The exact downstream sensitivity is

\[
 R^{n,L}_{b,L}=1,
 \qquad
 R^{n,L}_{b,\ell}
 =R^{n,L}_{b,\ell+1}
  \left(1+\frac1L A^{n,L}_{b,\ell}\right).
 \tag{3.2}
\]

Indeed, differentiating (1.2) with respect to its input gives

\[
 \frac{\partial X^{n,L}_{b,\ell+1}}
      {\partial X^{n,L}_{b,\ell}}
 =1+\frac1L A^{n,L}_{b,\ell},
\]

so \(R^{n,L}_{b,\ell}\) is exactly
\(\partial X^{n,L}_{b,L}/\partial X^{n,L}_{b,\ell}\).

Layer \(\ell\) first changes node \(X_{b,\ell+1}\).  Consequently,

\[
 \nabla_{\theta_{\ell i}}F_b^{n,L}
 =\frac1{nL}R^{n,L}_{b,\ell+1}
  \nabla_\theta\Phi(\theta_{\ell i},X^{n,L}_{b,\ell}).
 \tag{3.3}
\]

Substitution into (1.4) yields the exact particle equation

\[
 \dot\theta_{\ell i}
 =-\frac\eta B\sum_{b=1}^B
  (F_b^{n,L}-y_b)R^{n,L}_{b,\ell+1}
  \nabla_\theta\Phi(\theta_{\ell i},X^{n,L}_{b,\ell}).
 \tag{3.4}
\]

This proves that the \(nL\) scaling produces an \(O(1)\) particle velocity.  With only the usual factor \(n\), the right-hand side would carry an additional factor \(L^{-1}\), so the parameter law would freeze on every fixed training-time interval as \(L\to\infty\).

The raw Euclidean NTK is \(\sum_{\ell,i}\nabla F_b\cdot\nabla F_c\).  The kernel relevant to (1.4) is its scaled version

\[
 K^{n,L}_{bc}
 =nL\sum_{\ell=0}^{L-1}\sum_{i=1}^n
  \nabla_{\theta_{\ell i}}F_b^{n,L}
  \cdot\nabla_{\theta_{\ell i}}F_c^{n,L}.
 \tag{3.5}
\]

By (3.3),

\[
\begin{aligned}
 K^{n,L}_{bc}
 =\frac1L\sum_{\ell=0}^{L-1}
 R^{n,L}_{b,\ell+1}R^{n,L}_{c,\ell+1}
 \frac1n\sum_{i=1}^n
 &\nabla_\theta\Phi(\theta_{\ell i},X^{n,L}_{b,\ell})\\
 &\cdot
 \nabla_\theta\Phi(\theta_{\ell i},X^{n,L}_{c,\ell}).
\end{aligned}
 \tag{3.6}
\]

Therefore

\[
 \dot F_b^{n,L}
 =-\frac\eta B\sum_{c=1}^B
 K^{n,L}_{bc}(F_c^{n,L}-y_c).
 \tag{3.7}
\]

The matrix \(K^{n,L}\) is positive semidefinite because it is a Gram matrix.  If

\[
 q_{\ell i}^{n,L}
 =\frac1B\sum_{b=1}^B
  (F_b^{n,L}-y_b)R^{n,L}_{b,\ell+1}
  \nabla_\theta\Phi(\theta_{\ell i},X^{n,L}_{b,\ell}),
\]

then (3.3)--(3.4) also give the exact dissipation identity

\[
 \frac d{dt}\mathcal E^{n,L}
 =-\frac\eta L\sum_{\ell=0}^{L-1}
  \frac1n\sum_{i=1}^n|q_{\ell i}^{n,L}|^2\le0.
 \tag{3.8}
\]

## 4. Uniform activation and state bounds

Let

\[
 X_\ast=1+\max_b|\xi_b|.
\]

Since \(|\Phi|\le1\), (1.2) and (2.1) imply

\[
 |X^{n,L}_{b,\ell}(t)|\le X_\ast,
 \qquad
 |x_b(s,t)|\le X_\ast
 \tag{4.1}
\]

for every width, depth, layer, and training time on which the solution exists.

On \(\mathbb R^3\times[-X_\ast,X_\ast]\), direct differentiation of (1.1) gives a finite constant \(C_\Phi\), depending only on \(X_\ast\), such that

\[
\begin{aligned}
 |\Phi|+|\partial_x\Phi|
 &+\|\nabla_\theta\Phi\|
 +\|\nabla_\theta^2\Phi\|_{\rm op}\\
 &+\|\partial_x\nabla_\theta\Phi\|
 +\|\nabla_\theta\partial_x\Phi\|
 +|\partial_x^2\Phi|
 \le C_\Phi.
\end{aligned}
 \tag{4.2}
\]

There is no hidden compact-parameter assumption: factors involving a raw parameter are multiplied by derivatives of \(\tanh\), and all effective weights are bounded.  In particular, (4.2) is uniform over \(\theta\in\mathbb R^3\).

Moreover, \(|\partial_x\Phi|\le1\).  Hence

\[
 |R^{n,L}_{b,\ell}|
 \le(1+L^{-1})^{L-\ell}\le e,
 \tag{4.3}
\]

and the solution of (2.2) has the explicit form

\[
 r_b(s,t)
 =\exp\!\left(
   \int_s^1\int\partial_x\Phi(\theta,x_b(u,t))
   \,\rho_t(u,d\theta)\,du
   \right),
 \tag{4.4}
\]

so \(e^{-1}\le r_b\le e\).  Equations (3.4) and (4.1)--(4.3) show that every finite particle velocity is bounded by a constant depending only on the data, \(B\), and \(\eta\).  The finite-dimensional vector field is smooth and bounded, hence every finite \((n,L)\) flow exists uniquely for all \(t\ge0\).

## 5. The depth-\(L\) population program

For a profile \(\boldsymbol\mu=(\mu_0,\ldots,\mu_{L-1})\), replace every empirical average in (1.2), (3.1), and (3.2) by integration against \(\mu_\ell\).  Thus

\[
 X^L_{b,0}=\xi_b,
 \qquad
 X^L_{b,\ell+1}
 =X^L_{b,\ell}
 +\frac1L\int\Phi(\theta,X^L_{b,\ell})\mu_\ell(d\theta),
 \tag{5.1}
\]

\[
 R^L_{b,L}=1,
 \qquad
 R^L_{b,\ell}
 =R^L_{b,\ell+1}
  \left(1+\frac1L
   \int\partial_x\Phi(\theta,X^L_{b,\ell})\mu_\ell(d\theta)
  \right).
 \tag{5.2}
\]

Set \(F_b^L=X^L_{b,L}\) and

\[
 V_\ell^L[\boldsymbol\mu](\theta)
 =-\frac\eta B\sum_{b=1}^B
  (F_b^L-y_b)R^L_{b,\ell+1}
  \nabla_\theta\Phi(\theta,X^L_{b,\ell}).
 \tag{5.3}
\]

The population dynamics are

\[
 \partial_t\mu_\ell^L
 +\nabla_\theta\cdot
  \bigl(\mu_\ell^L V_\ell^L[\boldsymbol\mu^L]\bigr)=0,
 \qquad \mu_\ell^L(0)=\rho_0.
 \tag{5.4}
\]

The empirical measures

\[
 \widehat\mu_{\ell,t}^{n,L}
 =\frac1n\sum_{i=1}^n\delta_{\theta_{\ell i}(t)}
 \tag{5.5}
\]

satisfy exactly the same equations in the weak sense, with their empirical initial data.  This follows directly from (3.4); no limit theorem is used here.

The corresponding population kernel, used below, is the direct measure replacement in (3.6):

\[
\begin{aligned}
 K^L_{bc}[\boldsymbol\mu]
 =\frac1L\sum_{\ell=0}^{L-1}
 R^L_{b,\ell+1}R^L_{c,\ell+1}
 \int
 &\nabla_\theta\Phi(\theta,X^L_{b,\ell})\\
 &\cdot\nabla_\theta\Phi(\theta,X^L_{c,\ell})
 \,\mu_\ell(d\theta).
\end{aligned}
 \tag{5.6}
\]

In particular,

\[
 K^{n,L}(t)=K^L[\widehat{\boldsymbol\mu}^{n,L}(t)],
 \qquad
 K^L(t)=K^L[\boldsymbol\mu^L(t)].
\]

## 6. Uniform-in-depth stability of the population program

We first establish a deterministic estimate.  Let \(\boldsymbol\mu\) and \(\boldsymbol\nu\) be two current profiles, write

\[
 w_\ell=W_1(\mu_\ell,\nu_\ell),
 \qquad
 d=d_L(\boldsymbol\mu,\boldsymbol\nu),
\]

and let \(\delta X_\ell=\max_b|X^\mu_{b,\ell}-X^\nu_{b,\ell}|\).  Kantorovich--Rubinstein duality and (4.2) imply

\[
 \delta X_{\ell+1}
 \le(1+C_\Phi/L)\delta X_\ell
   +(C_\Phi/L)w_\ell.
 \tag{6.1}
\]

Since \(\delta X_0=0\), discrete Gronwall gives

\[
 \max_{\ell,b}|X^\mu_{b,\ell}-X^\nu_{b,\ell}|
 \le C d,
 \tag{6.2}
\]

where \(C\) is independent of \(L\).

Apply the same argument backward to (5.2).  The terminal difference is zero, \(|R|\le e\), and

\[
\begin{aligned}
 &\left|
 \int\partial_x\Phi(\theta,X^\mu_{b,\ell})\mu_\ell(d\theta)
 -\int\partial_x\Phi(\theta,X^\nu_{b,\ell})\nu_\ell(d\theta)
 \right|\\
 &\hspace{3cm}\le C_\Phi(\delta X_\ell+w_\ell).
\end{aligned}
\]

Backward discrete Gronwall and (6.2) yield

\[
 \max_{\ell,b}|R^\mu_{b,\ell}-R^\nu_{b,\ell}|
 \le C d.
 \tag{6.3}
\]

Equations (4.2), (5.3), (6.2), and (6.3) now give, for every \(\theta,\widetilde\theta\),

\[
 |V_\ell^L[\boldsymbol\mu](\theta)
  -V_\ell^L[\boldsymbol\nu](\widetilde\theta)|
 \le C\bigl(|\theta-\widetilde\theta|+d\bigr),
 \tag{6.4}
\]

with the same kind of \(L\)-independent constant.  The velocities are also uniformly bounded.

Choose an optimal initial coupling \(\pi_\ell^0\) of \(\mu_\ell^L(0)\) and \(\nu_\ell^L(0)\), and transport its two coordinates using the respective characteristic flows.  Define

\[
 D_\ell(t)
 =\int|\Theta_\ell^\mu(t,a)-\Theta_\ell^\nu(t,\widetilde a)|
   \,\pi_\ell^0(da,d\widetilde a),
 \qquad
 D(t)=\frac1L\sum_\ell D_\ell(t).
\]

The transported coupling gives

\[
 W_1(\mu_\ell^L(t),\nu_\ell^L(t))\le D_\ell(t).
\]

Using (6.4), for almost every \(t\),

\[
 D'(t)\le C D(t).
\]

Therefore

\[
 d_L(\boldsymbol\mu^L(t),\boldsymbol\nu^L(t))
 \le e^{Ct}d_L(\boldsymbol\mu^L(0),\boldsymbol\nu^L(0)).
 \tag{6.5}
\]

This also proves existence and uniqueness of (5.4).  Indeed, freeze a trial continuous measure curve, solve its globally Lipschitz characteristic ODE, and push forward the initial measures.  Estimate (6.4), integrated in training time, makes this map a contraction on a sufficiently short interval.  The interval length depends only on the constants above, not on \(L\), and uniform boundedness permits indefinite iteration.

Write \(F_b^L[\boldsymbol\mu]=X^L_{b,L}[\boldsymbol\mu]\).  The same estimates show that the output, sensitivities, and scaled kernel are Lipschitz readouts:

\[
 \max_b|F_b^L[\boldsymbol\mu]-F_b^L[\boldsymbol\nu]|
 +\max_{b,c}|K^L_{bc}[\boldsymbol\mu]-K^L_{bc}[\boldsymbol\nu]|
 \le C d_L(\boldsymbol\mu,\boldsymbol\nu).
 \tag{6.6}
\]

For the kernel, use (4.2)--(4.3) to see that its integrand is bounded and globally Lipschitz in \(\theta\), both state arguments, and both sensitivities; then sum the layerwise Kantorovich bounds with weight \(L^{-1}\).

## 7. Width convergence at exact continuous training time

Let \(\boldsymbol\mu^L(t)\) be the deterministic population solution of (5.4), initialized by \(\mu_\ell^L(0)=\rho_0\), and let \(\widehat{\boldsymbol\mu}^{n,L}(t)\) be the exact empirical solution (5.5).  Define

\[
 \delta_{n,L}
 =\frac1L\sum_{\ell=0}^{L-1}
  W_1(\widehat\mu_{\ell,0}^{n,L},\rho_0).
 \tag{7.1}
\]

Equations (6.2)--(6.6) give the pathwise estimate, for every \(T<\infty\),

\[
\begin{aligned}
 \sup_{0\le t\le T}\Bigl[&
 d_L(\widehat{\boldsymbol\mu}^{n,L}(t),\boldsymbol\mu^L(t))
 +\max_{b,\ell}|X^{n,L}_{b,\ell}(t)-X^L_{b,\ell}(t)|\\
 &+\max_{b,\ell}|R^{n,L}_{b,\ell}(t)-R^L_{b,\ell}(t)|
 +\max_{b,c}|K^{n,L}_{bc}(t)-K^L_{bc}(t)|
 \Bigr]
 \le C_T\delta_{n,L}.
\end{aligned}
 \tag{7.2}
\]

Let \(Z_1,Z_2,\ldots\) be i.i.d. with law \(\rho_0\), and put

\[
 q_n
 =\mathbb E W_1\!\left(
   \frac1n\sum_{i=1}^n\delta_{Z_i},\rho_0
   \right).
 \tag{7.3}
\]

Then \(q_n\to0\).  To verify this without a quantitative empirical-process theorem: the empirical laws converge weakly almost surely, and the empirical first moments converge almost surely by the strong law.  Weak convergence plus convergence of first moments is equivalent to \(W_1\) convergence.  Moreover,

\[
 W_1\!\left(\frac1n\sum_i\delta_{Z_i},\rho_0\right)
 \le\frac1n\sum_i|Z_i|+\mathbb E|Z_1|.
\]

The right-hand side is uniformly square-integrable because \(\rho_0\) has a finite second moment.  Thus the Wasserstein distances are uniformly integrable and their expectations tend to zero.

Since the layer initial laws are identically distributed,

\[
 \mathbb E\delta_{n,L}=q_n
 \tag{7.4}
\]

for every \(L\).  Markov's inequality and (7.2) therefore prove compact-training-time width convergence in probability, uniformly over arbitrary choices of \(L=L_n\).  No training-time Euler mesh has been introduced.

## 8. Well-posedness of the continuous-depth IDE

Let \(\mathfrak M\) be the set of Borel measurable profiles

\[
 \mu:[0,1]\longrightarrow\mathcal P_1(\mathbb R^3)
\]

such that

\[
 \int_0^1W_1(\mu(s),\delta_0)ds<\infty,
\]

modulo equality for almost every depth.  Equip it with the metric

\[
 \mathcal D(\mu,\nu)
 =\int_0^1W_1(\mu(s),\nu(s))\,ds.
 \tag{8.1}
\]

This metric space is complete.  Indeed, from any Cauchy sequence choose a subsequence whose successive \(\mathcal D\)-distances are summable.  Fubini then shows that it is pointwise \(W_1\)-Cauchy for almost every \(s\); completeness of \((\mathcal P_1,W_1)\) gives a pointwise limit.  Because \((\mathcal P_1,W_1)\) is a Polish space, an almost-everywhere pointwise limit of Borel profile maps has a Borel version.  The triangle inequality and Fatou's lemma show that this version has integrable first moment, and the summable-distance bound gives convergence in \(\mathcal D\).

For two current profiles \(\mu,\nu\in\mathfrak M\), forward Gronwall applied to (2.1) gives

\[
 \max_b\|x_b^\mu-x_b^\nu\|_{L^\infty_s}
 \le C\mathcal D(\mu,\nu).
 \tag{8.2}
\]

Using (4.4) and (4.2) similarly gives

\[
 \max_b\|r_b^\mu-r_b^\nu\|_{L^\infty_s}
 +\max_b\|p_b^\mu-p_b^\nu\|_{L^\infty_s}
 \le C\mathcal D(\mu,\nu).
 \tag{8.3}
\]

Consequently,

\[
 |v[\mu](s,\theta)-v[\nu](s,\widetilde\theta)|
 \le C\left(|\theta-\widetilde\theta|+\mathcal D(\mu,\nu)\right),
 \tag{8.4}
\]

and \(v[\mu]\) is uniformly bounded.

Given a trial curve \(\bar\mu\in C([t_0,t_0+\tau];\mathfrak M)\), solve the globally Lipschitz characteristic ODE driven by \(v[\bar\mu]\), starting from a current profile \(\mu^\ast\), and push \(\mu^\ast\) forward.  For two trial curves, (8.4) and characteristic Gronwall give

\[
 \sup_{t_0\le t\le t_0+\tau}
 \mathcal D(\Gamma\bar\mu(t),\Gamma\bar\nu(t))
 \le C\tau e^{C\tau}
 \sup_{t_0\le t\le t_0+\tau}
 \mathcal D(\bar\mu(t),\bar\nu(t)).
 \tag{8.5}
\]

This construction is well defined as a map into
\(C([t_0,t_0+\tau];\mathfrak M)\) without choosing representatives separately at every training time.  For each equivalence class \(\mu\in\mathfrak M\), the depth integral equations (2.1)--(2.3) select unique absolutely continuous, hence continuous, representatives of \(x^\mu,r^\mu,p^\mu\).  Equations (8.2)--(8.4), evaluated at the same \(\theta\), show that

\[
 \mu\longmapsto v[\mu]
\]

is a Lipschitz map from \(\mathfrak M\) into the bounded continuous velocity fields, equipped with the supremum norm on \([0,1]\times\mathbb R^3\).  Therefore a curve \(t\mapsto\bar\mu(t)\) continuous in \(\mathfrak M\) produces a velocity \((t,s,\theta)\mapsto v[\bar\mu(t)](s,\theta)\) that is jointly continuous and globally Lipschitz in \(\theta\).  The Picard iterates for the characteristic ODE are jointly Borel in \((s,t,a)\), and their locally uniform limit is therefore jointly Borel.  Pushing a Borel current probability kernel forward by this flow gives a Borel measure profile.  Finally, boundedness of the velocity yields

\[
 \mathcal D((\Gamma\bar\mu)(t),(\Gamma\bar\mu)(u))
 \le C|t-u|,
\]

so the image curve is continuous in \(\mathfrak M\).

For sufficiently small \(\tau\), \(\Gamma\) is a contraction.  This constructs a unique characteristic solution.  The constants are independent of \(t_0\), and

\[
 \int_0^1\int|\theta|\rho_t(s,d\theta)ds
 \le\int|\theta|\rho_0(d\theta)+Ct,
\]

so the construction can be iterated to every finite training time.

Thus, for every \(T<\infty\), (2.1)--(2.5) have a unique characteristic solution

\[
 \rho\in C([0,T];\mathfrak M).
 \tag{8.6}
\]

Starting the same construction at \(t_\ast\) from \(\rho_{t_\ast}\) yields the unique continuation, so the IDE is restartable and defines a semigroup.

## 9. Depth regularity

The initial profile is constant in depth.  From (2.1), (2.2), and the uniform bounds,

\[
 |x_b(s,t)-x_b(u,t)|
 +|r_b(s,t)-r_b(u,t)|
 +|p_b(s,t)-p_b(u,t)|
 \le C|s-u|.
 \tag{9.1}
\]

Hence

\[
 \sup_\theta|v_t(s,\theta)-v_t(u,\theta)|
 \le C|s-u|.
 \tag{9.2}
\]

Couple the characteristics at depths \(s\) and \(u\) by the same initial raw parameter \(a\sim\rho_0\).  Equations (8.4) and (9.2) give

\[
 \frac d{dt}|\Theta_t(s,a)-\Theta_t(u,a)|
 \le C|\Theta_t(s,a)-\Theta_t(u,a)|+C|s-u|.
\]

Since the initial difference is zero, training-time Gronwall yields

\[
 W_1(\rho_t(s),\rho_t(u))
 \le C_T|s-u|,
 \qquad 0\le t\le T.
 \tag{9.3}
\]

This selects a canonical \(W_1\)-continuous representative on the closed depth interval.  It is the regularity needed for a first-order depth Euler estimate.

## 10. Continuous-depth convergence

Let \(s_\ell=\ell/L\), and compare the population program (5.1)--(5.4) with the IDE at \(s_\ell\).  Because of (9.1)--(9.3), the right-hand side of the forward depth ODE is Lipschitz in \(s\).  Therefore

\[
 x_b(s_{\ell+1},t)
 =x_b(s_\ell,t)
 +\frac1L\int\Phi(\theta,x_b(s_\ell,t))
      \,\rho_t(s_\ell,d\theta)
 +O_T(L^{-2}),
 \tag{10.1}
\]

uniformly in \(\ell,b,t\le T\).  The backward equation similarly gives

\[
 r_b(s_\ell,t)
 =r_b(s_{\ell+1},t)
  \left(1+\frac1L
   \int\partial_x\Phi(\theta,x_b(s_\ell,t))
       \,\rho_t(s_\ell,d\theta)
  \right)
 +O_T(L^{-2}).
 \tag{10.2}
\]

Let

\[
 E_L(t)=\max_{0\le\ell<L}
 W_1(\mu_\ell^L(t),\rho_t(s_\ell)).
\]

Forward discrete Gronwall using (10.1) gives

\[
 \max_{b,\ell}|X^L_{b,\ell}(t)-x_b(s_\ell,t)|
 \le C_T(L^{-1}+E_L(t)).
 \tag{10.3}
\]

Backward discrete Gronwall using (10.2) then gives

\[
 \max_{b,\ell}|R^L_{b,\ell}(t)-r_b(s_\ell,t)|
 \le C_T(L^{-1}+E_L(t)).
 \tag{10.4}
\]

Since the discrete layer velocity uses \(R^L_{b,\ell+1}\), compare it with \(r_b(s_\ell)\).  The difference between \(r_b(s_{\ell+1})\) and \(r_b(s_\ell)\) is \(O_T(L^{-1})\) by (9.1).  Equations (10.3)--(10.4) consequently imply

\[
 \sup_{\ell,\theta}
 |V_\ell^L[\boldsymbol\mu^L](\theta,t)
  -v_t(s_\ell,\theta)|
 \le C_T(L^{-1}+E_L(t)).
 \tag{10.5}
\]

Couple \(\mu_\ell^L(t)\) and \(\rho_t(s_\ell)\) by characteristics starting from the same \(a\sim\rho_0\), and put

\[
 \Delta_L(t)
 =\max_{\ell<L}
  \int|\Theta_\ell^L(t,a)-\Theta_t(s_\ell,a)|\rho_0(da).
\]

Then \(E_L(t)\le\Delta_L(t)\), \(\Delta_L(0)=0\), and (8.4), (10.5) give

\[
 \Delta_L(t)
 \le C_T\int_0^t(\Delta_L(q)+L^{-1})dq.
\]

Training-time Gronwall proves

\[
 \sup_{0\le t\le T}E_L(t)\le\frac{C_T}{L}.
 \tag{10.6}
\]

Substitution into (10.3)--(10.4) gives

\[
 \sup_{0\le t\le T}
 \max_{b,\ell}
 \left(
 |X^L_{b,\ell}(t)-x_b(s_\ell,t)|
 +|R^L_{b,\ell}(t)-r_b(s_\ell,t)|
 \right)
 \le\frac{C_T}{L}.
 \tag{10.7}
\]

For the piecewise-constant interpolation

\[
 \bar\mu_t^L(s)=\mu_\ell^L(t),
 \qquad s\in[s_\ell,s_{\ell+1}),
\]

equations (9.3) and (10.6) imply

\[
 \sup_{0\le t\le T}
 \int_0^1W_1(\bar\mu_t^L(s),\rho_t(s))ds
 \le\frac{C_T}{L}.
 \tag{10.8}
\]

## 11. The continuum kernel and its convergence

Define

\[
 g_b(s,\theta,t)
 =\nabla_\theta\Phi(\theta,x_b(s,t)).
\]

The continuum kernel is

\[
 K_{bc}(t)
 =\int_0^1r_b(s,t)r_c(s,t)
   \int g_b(s,\theta,t)\cdot g_c(s,\theta,t)
   \,\rho_t(s,d\theta)ds.
 \tag{11.1}
\]

It is positive semidefinite because, for every \(z\in\mathbb R^B\),

\[
 z^\mathsf TK(t)z
 =\int_0^1\int
   \left|\sum_bz_br_b(s,t)g_b(s,\theta,t)\right|^2
   \,\rho_t(s,d\theta)ds\ge0.
 \tag{11.2}
\]

The required training-time differentiation is justified by the characteristic representation.  Namely,

\[
 x_b(s,t)=\xi_b+\int_0^s\int
 \Phi(\Theta_t(u,a),x_b(u,t))\rho_0(da)du.
\]

The velocity is continuous in training time and bounded, so each characteristic \(t\mapsto\Theta_t(u,a)\) is continuously differentiable.  Boundedness of \(\nabla_\theta\Phi\) and \(\partial_x\Phi\) supplies an integrable bound for the difference quotients.  Subtracting the integral equations at \(t+h\) and \(t\), dividing by \(h\), and applying dominated convergence plus Volterra Gronwall shows that \(t\mapsto x_b(\cdot,t)\) is continuously differentiable and that its derivative is the unique solution of the differentiated equation below.

Thus the derivative \(\dot x_b\) solves the linear depth equation

\[
 \partial_s\dot x_b
 =a_b(s,t)\dot x_b
  +\int g_b(s,\theta,t)\cdot v_t(s,\theta)
       \,\rho_t(s,d\theta),
 \qquad \dot x_b(0,t)=0,
\]

where \(a_b=\int\partial_x\Phi\,d\rho_t(s)\).  Variation of constants, or multiplication by the downstream factor \(r_b\), gives

\[
 \dot f_b(t)
 =\int_0^1r_b(s,t)
   \int g_b(s,\theta,t)\cdot v_t(s,\theta)
       \,\rho_t(s,d\theta)ds.
\]

Substituting (2.3)--(2.4) yields

\[
 \dot f_b(t)
 =-\frac\eta B\sum_{c=1}^B
  K_{bc}(t)(f_c(t)-y_c).
 \tag{11.3}
\]

Consequently,

\[
 \frac d{dt}\left[
  \frac1{2B}\sum_b(f_b-y_b)^2
  \right]
 =-\eta\int_0^1\int
   \left|\sum_bp_b(s,t)g_b(s,\theta,t)\right|^2
   \,\rho_t(s,d\theta)ds\le0.
 \tag{11.4}
\]

The integrand in (11.1) is uniformly bounded and Lipschitz in depth by (4.2), (9.1), and (9.3).  Equations (10.6)--(10.7), Kantorovich--Rubinstein duality, and the first-order Riemann-sum estimate therefore give

\[
 \sup_{0\le t\le T}\max_{b,c}|K^L_{bc}(t)-K_{bc}(t)|
 \le\frac{C_T}{L}.
 \tag{11.5}
\]

## 12. Main theorem

**Theorem 12.1 (joint exact-gradient-flow, mean-field, and continuous-depth limit).**
Fix \(B\), the data, \(\eta>0\), and the activation (1.1).  Let the raw initialization law \(\rho_0\) have a finite second moment; in particular, (1.5) is admissible.  Then:

1. For every finite \((n,L)\), the exact gradient flow (1.4) has a unique global solution.
2. For every \(L\), the population program (5.1)--(5.4) has a unique global characteristic solution.
3. For every \(T<\infty\), the single-time IDE (2.1)--(2.5) has a unique restartable characteristic solution in \(C([0,T];\mathfrak M)\).
4. There is a constant \(C_T\), independent of \(n\) and \(L\), such that the following estimate holds pathwise for every initialization realization with finite empirical first moments, and therefore almost surely under (1.5):

\[
\begin{aligned}
 \sup_{0\le t\le T}\Bigg[&
 \frac1L\sum_{\ell=0}^{L-1}
 W_1(\widehat\mu_{\ell,t}^{n,L},\rho_t(s_\ell))\\
 &+\max_{\substack{1\le b\le B\\0\le\ell\le L}}|X^{n,L}_{b,\ell}(t)-x_b(s_\ell,t)|
 +\max_{\substack{1\le b\le B\\0\le\ell\le L}}|R^{n,L}_{b,\ell}(t)-r_b(s_\ell,t)|\\
 &+\max_{1\le b,c\le B}|K^{n,L}_{bc}(t)-K_{bc}(t)|
 \Bigg]
 \le C_T\left(\delta_{n,L}+\frac1L\right).
\end{aligned}
 \tag{12.1}
\]

Here \(\delta_{n,L}\) is the initial empirical error (7.1).
Every grid value \(\rho_t(s_\ell)\) refers to the canonical
\(W_1\)-continuous representative constructed in Section 9; it is not an
evaluation of an arbitrary almost-everywhere representative.

5. If \(n_k\to\infty\) and \(L_k\to\infty\) are arbitrary deterministic sequences, with no relation between their rates, then the left-hand side of (12.1) converges to zero in probability.  In particular,

\[
 \sup_{0\le t\le T}\max_b
 |F_b^{n_k,L_k}(t)-f_b(t)|
 \xrightarrow{\mathbb P}0,
 \tag{12.2}
\]

\[
 \sup_{0\le t\le T}
 |\mathcal E^{n_k,L_k}(t)-\mathcal E(t)|
 \xrightarrow{\mathbb P}0,
 \tag{12.3}
\]

and

\[
 \sup_{0\le t\le T}\max_{b,c}
 |K^{n_k,L_k}_{bc}(t)-K_{bc}(t)|
 \xrightarrow{\mathbb P}0.
 \tag{12.4}
\]

**Proof.** Parts 1--3 were proved in Sections 4, 6, and 8.  Apply (7.2) to compare the empirical exact flow with the depth-\(L\) population flow, then apply (10.6)--(10.8) and (11.5) to compare that population flow with the continuous-depth IDE.  The triangle inequality gives (12.1).  Equations (7.3)--(7.4) imply \(\mathbb E\delta_{n,L}=q_n\to0\), uniformly in \(L\).  Markov's inequality proves convergence in probability for arbitrary \((n_k,L_k)\).  Output convergence is included in the forward-state term.  The MSE is Lipschitz on the uniformly bounded output range, yielding (12.3), and (12.4) is the kernel term of (12.1).  \(\square\)

The proof treats training time exactly.  The only Euler discretization is the architectural depth discretization \(s_\ell=\ell/L\); there is no training-time mesh and no interchange between width and a diverging number of optimizer steps.

## 13. A strictly nonlinear, nonlazy instance

The theorem does not claim that every initialization and dataset moves: matched labels or a symmetry can make the initial velocity vanish.  A concrete nondegenerate choice is

\[
 B=1,
 \qquad \xi_1=1,
 \qquad y_1=0,
 \qquad \rho_0=N((2,2,0),I_3).
 \tag{13.1}
\]

Let \(A=\tanh\alpha\), \(W=\tanh\omega\), and \(C=\tanh\beta\).  Independence gives

\[
 \int\Phi(\theta,1)\rho_0(d\theta)
 =\mathbb E[A]\,\mathbb E[\tanh(W+C)].
\]

Since \(\alpha\sim N(2,1)\) and \(\tanh\) is odd and strictly increasing, \(\mathbb E[A]>0\).  The law of \(C\) is symmetric.  Hence

\[
 g(w)=\mathbb E_C[\tanh(w+C)]
\]

is odd and strictly increasing.  The function \(\omega\mapsto g(\tanh\omega)\) is also odd and strictly increasing.  Shifting a symmetric Gaussian by \(2\) therefore makes its expectation strictly positive.  Thus

\[
 \int\Phi(\theta,1)\rho_0(d\theta)>0.
 \tag{13.2}
\]

The averaged initial residual field

\[
 \overline\Phi(x)=\int\Phi(\theta,x)\rho_0(d\theta)
\]

is itself strictly nonlinear.  Indeed, symmetry of \(C\) gives \(\overline\Phi(0)=0\), while (13.2) gives \(\overline\Phi(1)>0\).  Since \(\overline\Phi\) is bounded on \(\mathbb R\), it cannot be a nonconstant affine function; the two different values show that it is not constant either.

The continuous-depth forward solution is consequently not the identity map.  More explicitly, its derivative is positive at \(s=0\), so \(x_1(\varepsilon,0)>1\) for some \(\varepsilon>0\).  Since \(|\partial_sx_1|\le1\),

\[
 f_1(0)=x_1(1,0)
 \ge x_1(\varepsilon,0)-(1-\varepsilon)>\varepsilon>0.
\]

Thus the label-zero output residual is nonzero.  Furthermore, \(\nabla_\theta\Phi(\theta,x_1(s,0))\) is nonzero on a set of positive \(\rho_0\)-measure.  For example, its \(\alpha\)-component is

\[
 \operatorname{sech}^2(\alpha)
 \tanh\!\left(\tanh(\omega)x_1(s,0)+\tanh(\beta)\right),
\]

which vanishes only on a null hypersurface under the nondegenerate Gaussian law.  Since \(r_1>0\), the integrand in (11.4) is positive on a set of positive \((s,\rho_0)\)-measure.  Hence (11.4) is strict at \(t=0\):

\[
 \dot{\mathcal E}(0)<0.
 \tag{13.3}
\]

Thus the limiting transport velocity is nonzero and the loss changes at order one in the scaled training time.  In this document, **nonlazy** means precisely this non-frozen limiting transport behavior; no claim that \(\dot K(0)\ne0\) is made.  Finally,

\[
 \partial_x^2\Phi(\theta,x)
 =-2\tanh(\alpha)\tanh(\omega)^2
   \operatorname{sech}^2(u)\tanh(u),
 \qquad
 u=\tanh(\omega)x+\tanh(\beta),
\]

is not identically zero on a positive-measure set.  The witness is strictly nonlinear and nonlazy, rather than a disguised affine or frozen-feature limit.

## 14. Audit ledger and precise limitations

### Audit A: normalization and indexing

- A layer contribution to the forward state is \(1/(nL)\).
- The exact output derivative with respect to one raw parameter is therefore \(1/(nL)\) times the downstream sensitivity.
- The learning-rate multiplier \(nL\) is necessary for an \(O(1)\) particle velocity and an \(O(1)\) kernel.
- The layer-\(\ell\) gradient uses \(R_{\ell+1}\), not \(R_\ell\).
- The displayed kernel is \(nL\) times the raw Euclidean NTK.

### Audit B: topology

- Parameter-law convergence is averaged over depth as in (1.6).
- This topology preserves causal layer ordering; it does not replace the profile by one depth-averaged law.
- It controls all forward states, outputs, sensitivities, loss, and the integrated kernel.
- It does not imply \(\max_\ell W_1\) for the empirical layer laws.  A supremum-layer empirical result would require a stronger source estimate, generally involving the growth of \(L\) relative to \(n\).

### Audit C: limits

- Finite networks evolve by exact continuous gradient flow.
- Width stability is uniform in \(L\).
- Depth consistency is uniform on every compact training interval.
- Consequently arbitrary joint sequences \(n,L\to\infty\) are allowed.
- The theorem asserts convergence in probability, not blanket almost-sure convergence for arbitrary independently resampled triangular arrays.

### Audit D: well-posedness

- The feature range is bounded without an assumption.
- All activation derivatives needed for the characteristic estimates are globally bounded in the raw parameters on that feature range.
- Particle velocities are bounded, so finite raw parameters cannot escape in finite training time.
- The IDE vector field is globally Lipschitz in each characteristic and Lipschitz in the current measure profile under the integrated \(W_1\) metric.
- The characteristic fixed point therefore provides existence, uniqueness, and restartability.

### Audit E: no Gaussian or finite-moment closure

- Gaussianity is an initialization condition only.
- The pushed-forward law need not remain Gaussian, and no Gaussian closure is assumed or used.
- The IDE state is the current depth-indexed probability law, not a finite list of means and covariances.
- No oracle trajectory, future coefficient, response history, or two-training-time object is stored.

### Audit F: nontriviality and degenerate controls

- Strict nonlinearity of the neuron does not by itself force training motion.
- If the labels already match the outputs, the velocity vanishes.
- A centered independent amplitude parameter can make the initialized forward residual field vanish by symmetry.
- Section 13 supplies explicit data and a shifted Gaussian law for which the averaged residual field is nonlinear and both the depth evolution and limiting transport velocity are nontrivial.

### Audit G: architectural boundary

The proof depends on the mean-field residual form

\[
 x\mapsto x+L^{-1}\int\Phi(\theta,x)d\mu(\theta).
\]

The current law enters the forward and backward maps through Wasserstein-Lipschitz empirical averages.  There is no dense random matrix whose actual transpose is queried by a vector adaptively dependent on that same matrix.  Therefore this theorem does not establish the corresponding claim for a dense Gaussian-matrix \(\mu\)P ResNet.  It establishes an explicit nonlinear residual architecture for which the full single-time gradient-flow program is rigorous.

### Audit H: horizon

Every assertion is uniform on a fixed compact training interval \([0,T]\).  Constants may depend on \(T\).  The theorem does not assert convergence to a global minimizer, interpolation at infinite time, or estimates uniform as \(T\to\infty\).
