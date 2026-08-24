# A constant-species single-time IDE for residual particle networks

Status: proved and independently audited, 22 August 2026.

## Status and relation to the depth-two arctangent theorem

This note proves the general-activation version of the residual-network
theorem.  It uses the phrase **constant species** in exactly the sense used by
the audited depth-two arctangent operator IDE:

- the number of kinds of current fields is independent of width, depth,
  training time, and the number of time steps used by a numerical solver;
- an individual field may nevertheless be infinite-dimensional.

Thus “constant species” does not mean a finite-dimensional scalar ODE.  The
arctangent theorem retains two current (L^2) fields, one trace-class field,
one scalar residual, and an infinite-dimensional immutable action source.
The residual particle model below has an even shorter autonomous state: one
current probability-measure field

\[
 \rho_t:\ [0,1]\longrightarrow\mathcal P_1(\mathbb R^p).
 \tag{0.1}
\]

The depth coordinate is the domain of this one field; it is not a second
training time.  Forward features, adjoints, outputs, kernels, and loss are
instantaneous readouts of \(\rho_t\), not stored histories.  The price is that
\(\rho_t\) is infinite-dimensional and a depth discretization still costs
order \(L\) operations.  Section 12 proves why a finite list of ordinary
moments cannot give an exact universal replacement for nondegenerate
infinite-rank activation parameterizations.

This is a theorem for a residual **particle** architecture.  It is not a
theorem for a dense Ginibre-matrix ResNet.  The latter reuses a matrix and its
transpose and can require an immutable action source of the kind appearing in
the arctangent theorem.

## 1. Admissible residual features

Let \(p\ge1\) and let

\[
 \Phi:\mathbb R^p\times\mathbb R\longrightarrow\mathbb R
 \tag{1.1}
\]

be continuously differentiable.  We call \(\Phi\) **uniformly admissible** if
the following hold.

**A1 (global forward growth).**  There are \(c_0,c_1<\infty\) such that

\[
 \sup_\theta|\Phi(\theta,0)|\le c_0,
 \qquad
 \sup_{\theta,x}|\partial_x\Phi(\theta,x)|\le c_1.
 \tag{1.2}
\]

In particular,

\[
 |\Phi(\theta,x)|\le c_0+c_1|x|.
 \tag{1.3}
\]

**A2 (uniform parameter regularity on bounded state strips).**  For every
\(R<\infty\) there is \(C_R<\infty\) such that, whenever
\(|x|,|\widetilde x|\le R\),

\[
 \sup_{\theta,|z|\le R}\|\nabla_\theta\Phi(\theta,z)\|\le C_R
 \tag{1.4}
\]

and

\[
\begin{aligned}
 &|\partial_x\Phi(\theta,x)-
       \partial_x\Phi(\widetilde\theta,\widetilde x)|\\
 &\quad+
 \|\nabla_\theta\Phi(\theta,x)-
       \nabla_\theta\Phi(\widetilde\theta,\widetilde x)\|
 \le C_R\bigl(|\theta-\widetilde\theta|+|x-\widetilde x|\bigr).
\end{aligned}
 \tag{1.5}
\]

These assumptions state uniform \(C^{1,1}\) regularity directly for the
chosen raw parameterization.  They are not invariant under an arbitrary
nonlinear reparameterization.  They are weaker than requiring bounded
\(\Phi\): linearly growing activations are allowed.

## 2. Finite residual network and exact gradient flow

Fix a batch \((\xi_b,y_b)_{b=1}^B\), with \(B\) independent of width and
depth, and \(\eta>0\).  For width \(n\), depth \(L\), and \(h=L^{-1}\), set

\[
 X^{n,L}_{b,0}=\xi_b,
 \qquad
 X^{n,L}_{b,\ell+1}
 =X^{n,L}_{b,\ell}
 +\frac1{nL}\sum_{i=1}^n
   \Phi(\theta_{\ell i},X^{n,L}_{b,\ell}).
 \tag{2.1}
\]

The output and MSE are

\[
 F_b^{n,L}=X^{n,L}_{b,L},
 \qquad
 \mathcal E^{n,L}=\frac1{2B}\sum_{b=1}^B(F_b^{n,L}-y_b)^2,
 \tag{2.2}
\]

and the mean-field/continuous-depth feature-learning flow is

\[
 \dot\theta_{\ell i}
 =-\eta nL\,\nabla_{\theta_{\ell i}}\mathcal E^{n,L}.
 \tag{2.3}
\]

The initialization variables are independent over \((\ell,i)\), with common
law \(\rho_0\in\mathcal P_1(\mathbb R^p)\).

Define the exact downstream sensitivities

\[
 R^{n,L}_{b,L}=1,
 \qquad
 R^{n,L}_{b,\ell}
 =R^{n,L}_{b,\ell+1}
 \left[
 1+\frac1{nL}\sum_{i=1}^n
 \partial_x\Phi(\theta_{\ell i},X^{n,L}_{b,\ell})
 \right].
 \tag{2.4}
\]

Direct differentiation gives the finite identities

\[
 \nabla_{\theta_{\ell i}}F_b^{n,L}
 =\frac1{nL}R^{n,L}_{b,\ell+1}
 \nabla_\theta\Phi(\theta_{\ell i},X^{n,L}_{b,\ell}),
 \tag{2.5}
\]

\[
 \boxed{
 \dot\theta_{\ell i}
 =-\frac\eta B\sum_{b=1}^B
 (F_b^{n,L}-y_b)R^{n,L}_{b,\ell+1}
 \nabla_\theta\Phi(\theta_{\ell i},X^{n,L}_{b,\ell}).}
 \tag{2.6}
\]

The scaled tangent kernel is

\[
\begin{aligned}
 K^{n,L}_{bc}
 =\frac1L\sum_{\ell=0}^{L-1}
 R^{n,L}_{b,\ell+1}R^{n,L}_{c,\ell+1}\frac1n\sum_{i=1}^n
 &\nabla_\theta\Phi(\theta_{\ell i},X^{n,L}_{b,\ell})\\[-2mm]
 &\cdot\nabla_\theta\Phi(\theta_{\ell i},X^{n,L}_{c,\ell}).
\end{aligned}
 \tag{2.7}
\]

Consequently,

\[
 \dot F_b^{n,L}
 =-\frac\eta B\sum_cK^{n,L}_{bc}(F_c^{n,L}-y_c),
 \tag{2.8}
\]

and, with

\[
 q^{n,L}_{\ell i}
 =\frac1B\sum_b(F_b^{n,L}-y_b)R^{n,L}_{b,\ell+1}
 \nabla_\theta\Phi(\theta_{\ell i},X^{n,L}_{b,\ell}),
\]

\[
 \frac d{dt}\mathcal E^{n,L}
 =-\frac\eta L\sum_{\ell=0}^{L-1}\frac1n\sum_{i=1}^n
 |q^{n,L}_{\ell i}|^2\le0.
 \tag{2.9}
\]

Equations (2.4)--(2.9) are exact finite-dimensional identities; no limit or
independence approximation is used.

## 3. The constant-species single-training-time IDE

Let \(s\in[0,1]\) be continuous depth and \(t\ge0\) training time.  Given
the one current state field \(\rho_t(s)\), solve

\[
 \partial_sx_b(s,t)
 =\int\Phi(\theta,x_b(s,t))\rho_t(s,d\theta),
 \qquad x_b(0,t)=\xi_b,
 \tag{3.1}
\]

\[
 -\partial_sr_b(s,t)
 =r_b(s,t)\int\partial_x\Phi(\theta,x_b(s,t))
                  \rho_t(s,d\theta),
 \qquad r_b(1,t)=1.
 \tag{3.2}
\]

Put

\[
 f_b(t)=x_b(1,t),
 \qquad
 p_b(s,t)=\frac1B r_b(s,t)(f_b(t)-y_b),
 \tag{3.3}
\]

and define the current velocity

\[
 v_t(s,\theta)
 =-\eta\sum_{b=1}^Bp_b(s,t)
    \nabla_\theta\Phi(\theta,x_b(s,t)).
 \tag{3.4}
\]

The IDE is the characteristic continuity equation

\[
 \boxed{
 \partial_t\rho_t(s)
 +\nabla_\theta\!\cdot\bigl(\rho_t(s)v_t(s,\cdot)\bigr)=0,
 \qquad \rho_{t=0}(s)=\rho_0.}
 \tag{3.5}
\]

The notation contains two independent coordinates, but only \(t\) is an
evolution time.  At each fixed \(t\), (3.1) is a forward spatial solve in
depth and (3.2) a backward spatial solve.  Equations (3.1)--(3.4) are a
deterministic readout map \(\rho_t\mapsto(x,r,p,v)\).  Hence (3.5) is
autonomous and can be restarted from the current \(\rho_{t_*}\) without a
training history.

If one exposes every solver variable rather than eliminating readouts, the
description has one measure-field species, \(2B\) scalar depth-field species,
and \(B\) scalar residual/output species.  Since \(B\) is fixed, this count
is independent of \(n,L,t\).  The minimal dynamic state found here is just
the one measure field \(\rho_t\); no minimality among arbitrary encodings is
claimed.

## 4. The theorem

For a measurable profile \(\mu:[0,1]\to\mathcal P_1(\mathbb R^p)\), write

\[
 \mathcal D(\mu,\nu)
 =\int_0^1W_1(\mu(s),\nu(s))\,ds.
 \tag{4.1}
\]

Let \(\widehat\mu^{n,L}_{\ell,t}=n^{-1}\sum_i
\delta_{\theta_{\ell i}(t)}\), let \(s_\ell=\ell/L\), and define

\[
 \delta_{n,L}
 =\frac1L\sum_{\ell=0}^{L-1}
 W_1(\widehat\mu^{n,L}_{\ell,0},\rho_0).
 \tag{4.2}
\]

**Theorem 4.1 (general-activation constant-species limit).**  Suppose
\(\Phi\) satisfies A1--A2 and \(\rho_0\in\mathcal P_1(\mathbb R^p)\).
Then:

1. every finite \((n,L)\) flow (2.3) has a unique global solution;
2. for every \(T<\infty\), (3.1)--(3.5) has a unique global characteristic
   solution
   \(\rho\in C([0,T];\mathfrak M)\), where \(\mathfrak M\), defined in
   Section 7, is the complete metric space of measurable
   \(\mathcal P_1\)-profiles under \(\mathcal D\);
3. this solution is autonomous, restartable, and defines a semigroup;
4. there is \(C_T<\infty\), independent of \(n,L\), such that pathwise

\[
\begin{aligned}
 \sup_{t\le T}\Bigg[&
 \frac1L\sum_{\ell=0}^{L-1}
 W_1(\widehat\mu^{n,L}_{\ell,t},\rho_t(s_\ell))\\
 &+\max_{b,\,0\le\ell\le L}
 |X^{n,L}_{b,\ell}(t)-x_b(s_\ell,t)|\\
 &+\max_{b,\,0\le\ell\le L}
 |R^{n,L}_{b,\ell}(t)-r_b(s_\ell,t)|
 +\max_{b,c}|K^{n,L}_{bc}(t)-K_{bc}(t)|\Bigg]
 \le C_T\left(\delta_{n,L}+\frac1L\right),
\end{aligned}
 \tag{4.3}
\]

where

\[
\begin{aligned}
 K_{bc}(t)=\int_0^1&r_b(s,t)r_c(s,t)\\[-1mm]
 &\times\int
 \nabla_\theta\Phi(\theta,x_b(s,t))\cdot
 \nabla_\theta\Phi(\theta,x_c(s,t))
 \rho_t(s,d\theta)\,ds.
\end{aligned}
 \tag{4.4}
\]

Every grid value \(\rho_t(s_\ell)\) in (4.3) refers to the canonical
\(W_1\)-continuous depth representative constructed in Section 8, not to an
arbitrary representative of an almost-everywhere profile class.

5. for arbitrary deterministic \(n_k,L_k\to\infty\), with no relation
   between their rates, the left side of (4.3) converges to zero in
   probability.  In particular, output, MSE, and scaled tangent kernel
   converge uniformly on every compact training-time interval.

## 5. Uniform bounds

Let \(\xi_*=\max_b|\xi_b|\) and

\[
 X_*=e^{c_1}(\xi_*+c_0),
 \qquad R_*=e^{c_1}.
 \tag{5.1}
\]

From (1.3), the discrete and continuous depth Gronwall inequalities give

\[
 |X^{n,L}_{b,\ell}|,\ |x_b(s)|\le X_*.
 \tag{5.2}
\]

Equation (2.4) and \(|\partial_x\Phi|\le c_1\) give

\[
 |R^{n,L}_{b,\ell}|\le(1+c_1/L)^L\le R_*.
 \tag{5.3}
\]

The continuous adjoint is explicitly

\[
 r_b(s)=\exp\left\{
 \int_s^1\int\partial_x\Phi(\theta,x_b(u))\rho(u,d\theta)du
 \right\},
 \tag{5.4}
\]

so \(R_*^{-1}\le r_b\le R_*\).  On the state strip
\([-X_*,X_*]\), A2 bounds \(\nabla_\theta\Phi\), and therefore both the
finite velocity (2.6) and continuum velocity (3.4) are bounded and globally
Lipschitz in \(\theta\), with constants depending only on the fixed data,
\(\Phi,B,\eta\).  This proves global existence of every finite flow and
prevents any width-dependent stability constant.

## 6. Uniform-in-depth population stability

For a depth-\(L\) profile
\(\boldsymbol\mu=(\mu_0,\ldots,\mu_{L-1})\), replace every empirical average
in (2.1), (2.4), and (2.6) by integration against \(\mu_\ell\).  Denote the
resulting forward states, adjoints, and velocities by
\(X^{\boldsymbol\mu},R^{\boldsymbol\mu},V^L[\boldsymbol\mu]\), and evolve

\[
 \partial_t\mu^L_\ell+
 \nabla_\theta\cdot(\mu^L_\ell V^L_\ell[\boldsymbol\mu^L])=0.
 \tag{6.1}
\]

The empirical laws solve (6.1) exactly in the weak sense.  This is merely a
rewriting of (2.6).

For two profiles set

\[
 d_L(\boldsymbol\mu,\boldsymbol\nu)
 =\frac1L\sum_\ell W_1(\mu_\ell,\nu_\ell).
\]

Kantorovich--Rubinstein duality, A1--A2, and forward discrete Gronwall give

\[
 \max_{b,\ell}|X^{\boldsymbol\mu}_{b,\ell}
                 -X^{\boldsymbol\nu}_{b,\ell}|
 \le C d_L(\boldsymbol\mu,\boldsymbol\nu).
 \tag{6.2}
\]

Indeed, if \(w_\ell=W_1(\mu_\ell,\nu_\ell)\), the one-step inequality is

\[
 \Delta^X_{\ell+1}
 \le(1+C/L)\Delta^X_\ell+(C/L)w_\ell.
 \tag{6.3}
\]

The identical backward argument, using (5.3), yields

\[
 \max_{b,\ell}|R^{\boldsymbol\mu}_{b,\ell}
                 -R^{\boldsymbol\nu}_{b,\ell}|
 \le C d_L(\boldsymbol\mu,\boldsymbol\nu).
 \tag{6.4}
\]

Substitution in the velocity gives the decisive estimate

\[
 |V^L_\ell[\boldsymbol\mu](\theta)
   -V^L_\ell[\boldsymbol\nu](\widetilde\theta)|
 \le C\bigl(|\theta-\widetilde\theta|
             +d_L(\boldsymbol\mu,\boldsymbol\nu)\bigr),
 \tag{6.5}
\]

with \(C\) independent of \(L\).  Transport optimal initial couplings by the
two characteristic flows.  Averaging their distances over layers and using
(6.5) gives

\[
 d_L(\boldsymbol\mu^L_t,\boldsymbol\nu^L_t)
 \le e^{Ct}d_L(\boldsymbol\mu^L_0,\boldsymbol\nu^L_0).
 \tag{6.6}
\]

The same estimates show that the forward states, adjoints, and kernel are
Lipschitz readouts of the current profile.  Equations (6.5)--(6.6) both
construct the depth-\(L\) population flow and prove its uniqueness.

## 7. Well-posedness and strict Markov closure of the IDE

Let \(\mathfrak M\) consist of Borel profiles
\(\mu:[0,1]\to\mathcal P_1(\mathbb R^p)\) satisfying

\[
 \int_0^1\int|\theta|\mu(s,d\theta)ds<\infty,
\]

modulo almost-everywhere equality, with metric \(\mathcal D\) from (4.1).
It is complete: choose a subsequence of any Cauchy sequence with summable
successive \(\mathcal D\)-distances, apply Fubini and completeness of
\((\mathcal P_1,W_1)\) pointwise, and then use Fatou and the summable bound to
obtain a measurable limit in \(\mathfrak M\).

For current profiles \(\mu,\nu\), continuous-depth Gronwall and the explicit
adjoint formula give

\[
 \max_b\|x_b^\mu-x_b^\nu\|_\infty
 +\max_b\|r_b^\mu-r_b^\nu\|_\infty
 +\max_b\|p_b^\mu-p_b^\nu\|_\infty
 \le C\mathcal D(\mu,\nu).
 \tag{7.1}
\]

Therefore

\[
 |v[\mu](s,\theta)-v[\nu](s,\widetilde\theta)|
 \le C\bigl(|\theta-\widetilde\theta|+
             \mathcal D(\mu,\nu)\bigr).
 \tag{7.2}
\]

Given a trial curve \(\bar\mu\in C([t_0,t_0+\tau];\mathfrak M)\), solve the
globally Lipschitz characteristic ODE driven by \(v[\bar\mu]\), push forward
the current law profile, and call the resulting curve \(\Gamma\bar\mu\).
For two trial curves, characteristic Gronwall and (7.2) imply

\[
 \|\Gamma\bar\mu-\Gamma\bar\nu\|_{C_t\mathfrak M}
 \le C\tau e^{C\tau}
 \|\bar\mu-\bar\nu\|_{C_t\mathfrak M}.
 \tag{7.3}
\]

For small \(\tau\) this is a contraction.  The depth integral equations
select continuous representatives of \(x,r,p\); their dependence on the
measure-profile equivalence class is fixed by (7.1).  In fact, (7.1)--(7.2)
show that

\[
 \mu\longmapsto v[\mu]
 \tag{7.4}
\]

is Lipschitz from \(\mathfrak M\) into
\(C_b([0,1]\times\mathbb R^p;\mathbb R^p)\) in the supremum norm.  Therefore
a \(C_t(\mathfrak M)\) trial curve produces a sup-norm-continuous, jointly
continuous velocity.  Picard iterates of the characteristic equation are
jointly Borel in depth, time, and initial parameter, so their pushforwards
are Borel profiles.  Bounded velocity gives

\[
 \mathcal D(\rho_t,\rho_u)\le C|t-u|,
 \qquad
 \int_0^1\int|\theta|\rho_t(s,d\theta)ds
 \le\int|\theta|\rho_0(d\theta)+Ct.
 \tag{7.5}
\]

Thus the same contraction interval can be iterated on every compact time
horizon.  Existence and uniqueness are global in the stated characteristic
class.  Restarting the fixed-point construction at \(t_*\) with current
state \(\rho_{t_*}\) gives the unique continuation.  This proves the strict
Markov, no-history claim.

## 8. Depth regularity and the \(O(L^{-1})\) consistency estimate

The initial profile is constant in depth.  Equations (3.1)--(3.2) and the
uniform bounds first imply, without assuming any regularity of \(\rho_t\),

\[
 |x_b(s,t)-x_b(u,t)|+|r_b(s,t)-r_b(u,t)|
 +|p_b(s,t)-p_b(u,t)|\le C|s-u|.
 \tag{8.1}
\]

Consequently,

\[
 \sup_\theta|v_t(s,\theta)-v_t(u,\theta)|\le C|s-u|.
 \tag{8.2}
\]

Couple the characteristics at depths \(s,u\) using the same initial
\(a\sim\rho_0\).  Equations (7.2), (8.2), and training-time Gronwall give

\[
 W_1(\rho_t(s),\rho_t(u))\le C_T|s-u|.
 \tag{8.3}
\]

This selects a canonical continuous depth representative.  Now the right
sides of both depth equations are Lipschitz in \(s\).  One forward Euler
step and one backward Euler step therefore have local defects \(O_T(L^{-2})\).

Let \(\boldsymbol\mu^L\) be the depth-\(L\) population flow initialized by
\(\rho_0\), and set

\[
 E_L(t)=\max_{\ell<L}W_1(\mu^L_{\ell,t},\rho_t(s_\ell)).
\]

Discrete forward and backward Gronwall yield

\[
 \max_{b,\ell}\bigl(
 |X^L_{b,\ell}-x_b(s_\ell)|
 +|R^L_{b,\ell}-r_b(s_\ell)|\bigr)
 \le C_T\bigl(L^{-1}+E_L(t)\bigr).
 \tag{8.4}
\]

The discrete and continuum velocities consequently satisfy

\[
 \sup_{\ell,\theta}|V^L_\ell(\theta,t)-v_t(s_\ell,\theta)|
 \le C_T\bigl(L^{-1}+E_L(t)\bigr).
 \tag{8.5}
\]

Couple their characteristics from the same initial parameter.  If
\(\Delta_L\) is the maximum expected characteristic distance, then
\(E_L\le\Delta_L\), \(\Delta_L(0)=0\), and

\[
 \Delta_L(t)\le C_T\int_0^t
 [\Delta_L(q)+L^{-1}]\,dq.
 \tag{8.6}
\]

Hence

\[
 \sup_{t\le T}E_L(t)
 +\sup_{t\le T}\max_{b,\ell}\bigl(
 |X^L_{b,\ell}-x_b(s_\ell)|
 +|R^L_{b,\ell}-r_b(s_\ell)|\bigr)
 \le\frac{C_T}{L}.
 \tag{8.7}
\]

The kernel integrand is bounded and Lipschitz by A2.  The same coupling and
the first-order Riemann-sum estimate give

\[
 \sup_{t\le T}\max_{b,c}|K^L_{bc}(t)-K_{bc}(t)|
 \le\frac{C_T}{L}.
 \tag{8.8}
\]

## 9. Width convergence and completion of Theorem 4.1

Apply (6.6) to the exact empirical solution and the depth-\(L\) population
solution.  Together with the readout estimates, this gives pathwise

\[
 \sup_{t\le T}
 \left[d_L(\widehat{\boldsymbol\mu}^{n,L}_t,
                 \boldsymbol\mu^L_t)
       +\text{all corresponding state, adjoint, and kernel errors}\right]
 \le C_T\delta_{n,L}.
 \tag{9.1}
\]

For iid \(Z_i\sim\rho_0\in\mathcal P_1\),

\[
 q_n=\mathbb E W_1\left(n^{-1}\sum_i\delta_{Z_i},\rho_0\right)
 \longrightarrow0.
 \tag{9.2}
\]

One direct proof truncates \(Z_i\) to a fixed ball, uses weak empirical
convergence on that compact set, and then lets the truncation radius tend to
infinity.  If \(T_R\) denotes radial projection to that ball and
\(\rho_0^R=(T_R)_\#\rho_0\), then

\[
 q_n\le
 \mathbb E W_1\left(n^{-1}\sum_i\delta_{T_RZ_i},\rho_0^R\right)
 +2\,\mathbb E|Z_1-T_RZ_1|.
 \tag{9.3}
\]

The first term tends to zero for fixed \(R\) by bounded convergence, and the
second tends to zero as \(R\to\infty\) by the first-moment assumption.  Since
every layer has the same initialization law,

\[
 \mathbb E\delta_{n,L}=q_n
 \tag{9.4}
\]

for every \(L\).  Combining (8.7)--(9.1) proves (4.3).  Markov's inequality
and (9.2)--(9.4) prove convergence in probability along every deterministic
joint sequence \(n,L\to\infty\), with no rate relation.  This completes the
proof of Theorem 4.1.

No training-time Euler mesh was used.  The only Euler error is the
architectural discretization of continuous depth.

## 10. Output, kernel, and loss readouts

The continuum kernel (4.4) is positive semidefinite because

\[
 z^\mathsf TK(t)z
 =\int_0^1\int
 \left|\sum_bz_br_b(s,t)
 \nabla_\theta\Phi(\theta,x_b(s,t))\right|^2
 \rho_t(s,d\theta)ds\ge0.
 \tag{10.1}
\]

Differentiate the characteristic form of (3.1).  Bounded
\(\nabla_\theta\Phi\), bounded \(\partial_x\Phi\), dominated convergence,
and Volterra Gronwall justify the differentiation.  The adjoint (3.2) then
gives

\[
 \dot f_b(t)
 =-\frac\eta B\sum_cK_{bc}(t)(f_c(t)-y_c).
 \tag{10.2}
\]

Thus

\[
 \frac d{dt}\left[\frac1{2B}\sum_b(f_b-y_b)^2\right]
 =-\eta\int_0^1\int
 \left|\sum_bp_b(s,t)
 \nabla_\theta\Phi(\theta,x_b(s,t))\right|^2
 \rho_t(s,d\theta)ds\le0.
 \tag{10.3}
\]

These are direct current-state readouts.  No covariance history or second
training-time kernel is present.

## 11. A large concrete activation class

Let

\[
 \Phi((\alpha,\omega,\beta),x)
 =A(\alpha)\,
  \sigma\bigl(W(\omega)x+C(\beta)\bigr),
 \tag{11.1}
\]

where \(A,W,C\in C_b^{1,1}(\mathbb R)\): the maps and their first
derivatives are bounded, and the first derivatives are globally Lipschitz.
Assume

\[
 \sigma\in C^{1,1}(\mathbb R),
 \qquad \|\sigma'\|_\infty<\infty.
 \tag{11.2}
\]

Then \(\sigma\) has at most linear growth, and direct differentiation shows
that (11.1) satisfies A1--A2.  Therefore Theorem 4.1 applies.  This includes,
among many others,

- tanh, arctangent, logistic sigmoid, erf, sine, and softsign;
- identity and affine activations;
- softplus, GELU, and other smooth ReLU-like activations with bounded first
  derivative and Lipschitz derivative;
- any positive rescaling or affine recentering of these activations.

The earlier model is recovered with

\[
 A(\alpha)=W(\omega)=C(\beta)=\tanh(\cdot),
 \qquad \sigma=\tanh.
\]

Strict nonlinearity is not needed for the limit theorem.  It matters only
for exhibiting a nontrivial feature-learning instance.  Such data and an
initialization can be chosen for any nondegenerate nonaffine example, but
nonaffinity and an unmatched label alone are not sufficient.  The sharp
instantaneous condition is a nonzero residual together with positive
gradient energy in the right side of (10.3).

Exact ReLU is not covered because the classical gradient vector field is not
\(C^1\) at a kink.  A differential-inclusion or almost-everywhere crossing
argument would be a different theorem.  Superlinearly growing activations
such as untruncated powers are not covered by Theorem 4.1; the same proof has
only a local variant if a separate invariant-state bound is first proved.
Unbounded effective raw weights would require explicit propagated weighted
moment or coercivity estimates in addition to a weighted transport metric;
that extension is not claimed here.

## 12. Why one generally cannot replace \(\rho_t\) by finitely many moments

The following obstruction already appears in the forward depth equation.

**Proposition 12.1 (finite linear-moment obstruction).**  Fix functions
\(\psi_1,\ldots,\psi_m\) on parameter space.  Suppose that, for a fixed
state value \(x\),

\[
 \int\Phi(\theta,x)\rho(d\theta)
 \tag{12.1}
\]

is determined for every finitely supported probability law \(\rho\) solely
by the \(m\) numbers \(\int\psi_jd\rho\).  Then

\[
 \Phi(\cdot,x)\in
 \operatorname{span}\{1,\psi_1,\ldots,\psi_m\}.
 \tag{12.2}
\]

**Proof.**  If (12.2) fails, finite-dimensional linear algebra supplies
finitely many parameter points \(\theta_i\) and real coefficients \(c_i\)
such that

\[
 \sum_i c_i=0,
 \qquad \sum_i c_i\psi_j(\theta_i)=0\quad(1\le j\le m),
 \qquad \sum_i c_i\Phi(\theta_i,x)\ne0.
\]

The positive and negative parts of \((c_i)\) have the same total mass.
After normalization they define two finitely supported probability laws with
identical declared moments but different values of (12.1), a contradiction.
\(\square\)

Consequently, if

\[
 \operatorname{span}\{\Phi(\cdot,x):x\in I\}
\]

is infinite-dimensional on some state interval \(I\), no fixed finite list
of ordinary moments can even close the exact forward equation, much less the
training dynamics.  This condition holds for the standard nondegenerate
variable-slope parameterization of analytic nonpolynomial neurons.  More
precisely, assume that \(A(\alpha_0)\ne0\), that \(C(\beta_0)=0\) (or fix
another analytic center), that the range of \(W\) contains a neighborhood of
zero, and that the reachable state interval \(I\) contains a nonzero open
subinterval.  Choose a smaller one-sign subinterval and, if it is negative,
reflect both its state coordinate and the slope coordinate.  Restricting to
this parameter slice gives the functions

\[
 w\longmapsto\sigma(wx),\qquad x>0,
\]

which have infinite-dimensional span whenever the Taylor series of
\(\sigma\) has infinitely many nonzero coefficients.  Linear dependence for
\(N\) distinct positive values of \(x\) would force a generalized
Vandermonde system for \(N\) nonzero Taylor orders; that system is
nonsingular.

Under those nondegeneracy hypotheses, the proposition rules out finite
**linear-moment** closure for tanh, arctangent, sine, sigmoid, and analogous
analytic nonpolynomial activations.  Naming the activation alone is not
enough: for example, a frozen-slope parameterization can have finite feature
rank even with tanh.  The proposition does not rule out special algebraic
activations, approximation schemes, or pathological nonlinear encodings of
an entire measure into a real number.  Finite feature span is only a
necessary condition for a finite moment closure, not a sufficient one,
because the transport equation can generate a larger moment hierarchy.

The quantifiers matter.  Proposition 12.1 concerns exact recovery, by fixed
state-independent moments, uniformly over all finitely supported laws and a
continuum of state values.  It does not exclude:

- an approximate moment truncation;
- moments chosen adaptively as functions of depth, time, or the current
  state;
- closure only along one specially reachable orbit;
- a finite set of sampled state values; or
- a \(K\)-atomic initial law, which remains \(K\)-atomic under a deterministic
  characteristic flow and can be represented by its atom trajectories.

Even when the forward feature span is finite, a dynamic moment closure needs
more.  If \(m_j=\int\psi_jd\rho\), then

\[
 \partial_t m_j(s)
 =\int\nabla\psi_j(\theta)\cdot v_t(s,\theta)\rho_t(s,d\theta).
 \tag{12.3}
\]

Thus a closure intended to hold uniformly over data and residual
coefficients that can isolate each relevant \(x\) must also contain the
adjoint readouts such as \(\partial_x\Phi(\cdot,x)\) and be invariant under
every transport generator

\[
 \psi\longmapsto
 \nabla\psi(\cdot)\cdot\nabla_\theta\Phi(\cdot,x)
 \tag{12.4}
\]

generated by the relevant state values (with the additional products needed
for kernel readouts).  For one fixed batch, only the linear combinations
that actually occur in \(v\) must be recoverable; if \(p\equiv0\), there is
no dynamical obligation at all.  The uniform invariance is exceptional.
Proposition 12.1 is therefore a sharp obstruction to the first step of
universal finite-moment closure, not a complete classification of every
special finite orbit.

There are genuine nonlinear special closures.  For example, formally taking

\[
 \Phi(a,x)=\frac12a^2h(x)
 \tag{12.5}
\]

makes the forward and adjoint coefficients functions of the single moment
\(q=\int a^2d\rho\), while the characteristic velocity gives

\[
 \partial_tq(s)
 =-2\eta q(s)\sum_bp_b(s)h(x_b(s)).
 \tag{12.6}
\]

This example lies outside A1--A2 because its parameter derivative is
unbounded, but it disproves any unconditional statement that nonlinearity by
itself forces a full measure state.  Likewise a \(K\)-atomic initialization
has an exact representation by \(K\) atom fields.

## 13. Claim ledger

| Claim | Level |
|---|---|
| Finite forward, adjoint, gradient, kernel, and dissipation identities | exact finite-dimensional identities |
| IDE well-posedness and restartability under A1--A2 | theorem |
| Width convergence at exact continuous training time | theorem in averaged-depth \(W_1\) |
| Continuous-depth error \(O(L^{-1})\) | theorem |
| Arbitrary joint \(n,L\to\infty\) compact-time convergence | theorem in probability |
| Constant number of state species | exact semantic consequence of the displayed IDE |
| Finite scalar/moment closure for nondegenerate infinite-rank parameterizations | ruled out for universal fixed linear moments by Proposition 12.1 |
| Dense matrix ResNet, exact ReLU, unbounded-weight polynomial model | not claimed |
| Long-time convergence to a minimizer | not claimed |
