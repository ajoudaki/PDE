# Continuous depth and dense residual models

Sections 1–13 prove global characteristic well-posedness and joint width and
depth convergence of exact gradient flow for a scalar residual particle
architecture, with a general fixed finite batch and the parameter regularity
assumptions A1--A2 below. It is a separate architecture benchmark. It is not a
dense Gaussian-matrix ResNet and does not establish the correlated dense
feature-learning theorem. It is neither an admissible substitution for that
architecture nor a recommendation to replace it.

Section 14 separately derives exact finite dense-ResNet gradients, kernels,
energy and training-response identities, with chronological factorial tails
along a supplied trajectory. It retains the dense matrices and distinguishes
exact backward sources from recomputed ones. It establishes no dense width
or continuous-depth limit, autonomous compressed flow, or fitting theorem.

Section 15 proves global existence, uniqueness and restart for a coherent
dense kernel model with normalization `W/n`, fixed bounded endpoints and
a strong row/column kernel space, with exact gradient and energy identities.
Finite-network approximation and the Gaussian
`W/sqrt(n)` model remain separate questions.

In the scalar-particle architecture there is one scalar hidden state per
sample at each depth. Width counts
parameter particles whose scalar residual features are averaged within a
layer; there are no trainable dense hidden matrices or separate readout
weights. The continuous model stores one current probability-measure field
over depth. Its forward states, backward sensitivities, outputs, kernel, and
loss are determined by that current field. A fixed number of field types
does not mean a finite-dimensional scalar state, and resolving the depth
coordinate still requires work proportional to the chosen depth resolution.

The scalar-particle proof first bounds all forward states and backward sensitivities
independently of width and depth. Coupling estimates then give a global
characteristic flow on a complete space of measure profiles. Constant
initialization in depth selects a canonical continuous representative and
gives a first-order depth discretization error. Combining this error with
stability in the depth-averaged Wasserstein distance proves convergence along
arbitrary joint width and depth sequences.

## 1. Architecture, notation, and assumptions

Fix a batch \((x_a,y_a)_{a=1}^m\in(\mathbb R\times\mathbb R)^m\), with
\(1\le m<\infty\) independent of width and depth. Inputs are scalar in this
architecture, so \(d=1\). No distinctness, orthogonality, Gram-matrix
nondegeneracy, or realizability condition is imposed on the batch. Let
\(n\ge1\) be the number of particles per layer, \(L\ge1\) the residual depth,
\(h=1/L\) its architectural mesh, and \(p\ge1\) the parameter dimension.
Each raw parameter \(\theta_{\ell i}\) belongs to \(\mathbb R^p\), for
\(0\le\ell<L\) and \(1\le i\le n\).

The residual feature is a specified map

\[
\Phi:\mathbb R^p\times\mathbb R\longrightarrow\mathbb R,
\qquad (\theta,z)\longmapsto\Phi(\theta,z).
\tag{1.1}
\]

Here \(\Phi\) denotes the entire parameterized particle feature. It is not
the coordinatewise activation \(\phi\) of a dense matrix network. Finite
hidden states are \(z_{a,\ell}^{n,L}\); population hidden states are
capitalized \(Z_a\), or \(Z_{a,\ell}^{L,\boldsymbol\mu}\) for a discrete
depth population. Backward sensitivities are \(p_{a,\ell}^{n,L}\) and
\(P_a\), respectively. The symbol \(r\) is reserved for output residuals
\(f-y\); sensitivities do not include a residual factor.

Assume \(\Phi\in C^1(\mathbb R^p\times\mathbb R)\) and the following.

**A1 (uniform forward growth).** There are nonnegative finite constants
\(c_0,c_1\) such that

\[
\sup_\theta|\Phi(\theta,0)|\le c_0,
\qquad
\sup_{\theta,z}|\partial_z\Phi(\theta,z)|\le c_1.
\tag{1.2}
\]

In particular, \(|\Phi(\theta,z)|\le c_0+c_1|z|\).

**A2 (uniform parameter regularity on bounded state strips).** For every
finite \(R\ge0\) there is a finite \(C_R\) such that

\[
\sup_{\theta,\,|z|\le R}\|\nabla_\theta\Phi(\theta,z)\|\le C_R,
\tag{1.3}
\]

and, for all \(\theta,\widetilde\theta\in\mathbb R^p\) and
\(|z|,|\widetilde z|\le R\),

\[
\begin{aligned}
&|\partial_z\Phi(\theta,z)
       -\partial_z\Phi(\widetilde\theta,\widetilde z)|\\
&\quad+\|\nabla_\theta\Phi(\theta,z)
       -\nabla_\theta\Phi(\widetilde\theta,\widetilde z)\|
\le C_R\bigl(\|\theta-\widetilde\theta\|+|z-\widetilde z|\bigr).
\end{aligned}
\tag{1.4}
\]

These assumptions apply to the chosen raw parameterization; an arbitrary
nonlinear change of parameter coordinates need not preserve them. They
allow features with linear growth in the state and do not require a bounded
parameter support.

The training clock \(t\) is physical time and \(\kappa>0\) is a fixed
mobility multiplier. The loss in this chapter is explicitly the half mean
squared loss \(\mathcal L=(2m)^{-1}\sum_a r_a^2\). Relative to the convention
\(m^{-1}\sum_a r_a^2\), this halves the gradient velocity at a fixed mobility.
The notation \(\eta_n\) is reserved for an actual gradient-descent step.
The results below concern exact continuous training time and impose no
gradient-descent step condition or joint width/depth/GD conclusion.

## 2. Exact finite network and gradient identities

For time-dependent parameters define

\[
z_{a,0}^{n,L}=x_a,
\qquad
z_{a,\ell+1}^{n,L}
=z_{a,\ell}^{n,L}
+\frac1{nL}\sum_{i=1}^n
  \Phi(\theta_{\ell i},z_{a,\ell}^{n,L}),
\qquad 0\le\ell<L.
\tag{2.1}
\]

Set

\[
f_a^{n,L}=z_{a,L}^{n,L},
\qquad r_a^{n,L}=f_a^{n,L}-y_a,
\qquad
\mathcal L^{n,L}=\frac1{2m}\sum_{a=1}^m(r_a^{n,L})^2.
\tag{2.2}
\]

All raw parameters train with block mobility \(\kappa nL\):

\[
\dot\theta_{\ell i}
=-\kappa nL\nabla_{\theta_{\ell i}}\mathcal L^{n,L}.
\tag{2.3}
\]

The initialization variables are independent over \((\ell,i)\), each with
law \(\rho_0\in\mathcal P_1(\mathbb R^p)\). Deterministic finite initial
parameters are also allowed in the pathwise statements.

Define the exact downstream sensitivities by

\[
p_{a,L}^{n,L}=1,
\qquad
p_{a,\ell}^{n,L}
=p_{a,\ell+1}^{n,L}
 \left(1+\frac1{nL}\sum_{i=1}^n
 \partial_z\Phi(\theta_{\ell i},z_{a,\ell}^{n,L})\right).
\tag{2.4}
\]

Thus \(p_{a,\ell}^{n,L}\) is the derivative of the output with respect to
the hidden state at depth \(\ell\), holding downstream parameters fixed.
The factor contributed by a parameter in layer \(\ell\) enters the next
hidden state, so the chain rule gives the index \(\ell+1\):

\[
\nabla_{\theta_{\ell i}}f_a^{n,L}
=\frac1{nL}p_{a,\ell+1}^{n,L}
 \nabla_\theta\Phi(\theta_{\ell i},z_{a,\ell}^{n,L}).
\tag{2.5}
\]

Consequently the finite flow is exactly

\[
\dot\theta_{\ell i}=-\kappa q_{\ell i}^{n,L},
\qquad
q_{\ell i}^{n,L}
=\frac1m\sum_{a=1}^m r_a^{n,L}p_{a,\ell+1}^{n,L}
 \nabla_\theta\Phi(\theta_{\ell i},z_{a,\ell}^{n,L})
\in\mathbb R^p.
\tag{2.6}
\]

The scaled tangent kernel is

\[
\begin{aligned}
K_{ab}^{n,L}
={}&\frac1L\sum_{\ell=0}^{L-1}
p_{a,\ell+1}^{n,L}p_{b,\ell+1}^{n,L}\frac1n\sum_{i=1}^n
\nabla_\theta\Phi(\theta_{\ell i},z_{a,\ell}^{n,L})
\cdot\nabla_\theta\Phi(\theta_{\ell i},z_{b,\ell}^{n,L})\\
={}&nL\sum_{\ell,i}
\nabla_{\theta_{\ell i}}f_a^{n,L}
\cdot\nabla_{\theta_{\ell i}}f_b^{n,L}.
\end{aligned}
\tag{2.7}
\]

It is positive semidefinite, as is seen by inserting an arbitrary vector
of sample coefficients into the final Gram expression. Differentiating
outputs and loss along (2.3) gives

\[
\dot f_a^{n,L}=-\frac\kappa m\sum_{b=1}^mK_{ab}^{n,L}r_b^{n,L},
\tag{2.8}
\]

\[
\frac d{dt}\mathcal L^{n,L}
=-\kappa nL\sum_{\ell,i}
 \|\nabla_{\theta_{\ell i}}\mathcal L^{n,L}\|^2
=-\frac\kappa L\sum_{\ell=0}^{L-1}\frac1n\sum_{i=1}^n
 \|q_{\ell i}^{n,L}\|^2\le0.
\tag{2.9}
\]

No independence approximation enters these identities, including after
training has coupled particles and layers.

## 3. Current-state continuous-depth equation

Let \(\mathcal P_1(\mathbb R^p)\) be the Borel probability laws with finite
first Euclidean moment. The Wasserstein distance used throughout is

\[
\mathcal W_1(\mu,\nu)
=\inf_{\pi\in\Pi(\mu,\nu)}
 \int\|\theta-\widetilde\theta\|\,\pi(d\theta,d\widetilde\theta),
\tag{3.1}
\]

where \(\Pi(\mu,\nu)\) is the set of couplings. For Borel depth profiles put

\[
\mathcal D(\mu,\nu)=\int_0^1\mathcal W_1(\mu(s),\nu(s))\,ds.
\tag{3.2}
\]

The state space \(\mathfrak M\) consists of profiles
\(\mu:[0,1]\to\mathcal P_1(\mathbb R^p)\) with

\[
\int_0^1\int\|\theta\|\,\mu(s,d\theta)\,ds<\infty,
\tag{3.3}
\]

modulo equality for almost every depth. The distance \(\mathcal D\) is
therefore a metric on \(\mathfrak M\). It averages over depth; it is not the
maximum discrepancy of the individual layer laws.

For any current profile \(\mu\in\mathfrak M\), define the absolutely
continuous forward state and sensitivity by

\[
\partial_s Z_a^\mu(s)
=\int\Phi(\theta,Z_a^\mu(s))\,\mu(s,d\theta),
\qquad Z_a^\mu(0)=x_a,
\tag{3.4}
\]

\[
-\partial_s P_a^\mu(s)
=P_a^\mu(s)\int\partial_z\Phi(\theta,Z_a^\mu(s))\,\mu(s,d\theta),
\qquad P_a^\mu(1)=1.
\tag{3.5}
\]

These equations initially hold for almost every \(s\); their integral
forms define unique continuous representatives. Set

\[
f_a^\mu=Z_a^\mu(1),\qquad r_a^\mu=f_a^\mu-y_a,
\qquad
Q[\mu](s,\theta)=\frac1m\sum_{a=1}^m
 r_a^\mu P_a^\mu(s)\nabla_\theta\Phi(\theta,Z_a^\mu(s)),
\tag{3.6}
\]

where \(Q[\mu](s,\theta)\in\mathbb R^p\), and define
\(v[\mu]= -\kappa Q[\mu]\). The evolution is

\[
\partial_t\rho_t(s)
+\nabla_\theta\cdot\bigl(\rho_t(s)v[\rho_t](s,\cdot)\bigr)=0,
\qquad \rho_{t=0}(s)=\rho_0.
\tag{3.7}
\]

A characteristic solution means that the maps
\(\Theta_t(s,\vartheta)\in\mathbb R^p\) solve

\[
\partial_t\Theta_t(s,\vartheta)
=v[\rho_t](s,\Theta_t(s,\vartheta)),\qquad
\Theta_0(s,\vartheta)=\vartheta,
\qquad
\rho_t(s)=(\Theta_t(s,\cdot))_\#\rho_0.
\tag{3.8}
\]

For a general initial profile \(\mu_{\rm in}\), replace \(\rho_0\) on the
right side of (3.8) by \(\mu_{\rm in}(s)\), for almost every depth.
Pushforward means the law of the image under the indicated map. In particular, for every
\(\zeta\in C_c^1(\mathbb R^p)\) the characteristic solution satisfies

\[
\int\zeta\,d\rho_t(s)-\int\zeta\,d\rho_u(s)
=\int_u^t\int\nabla\zeta(\theta)\cdot
 v[\rho_\tau](s,\theta)\,\rho_\tau(s,d\theta)\,d\tau.
\tag{3.9}
\]

The sole evolution time is \(t\). The coordinate \(s\in[0,1]\) is depth;
at each training time, (3.4)--(3.6) are forward and backward depth readouts
of the current measure field. The state equation is autonomous. Exposing
its solver variables uses one measure-field type, \(2m\) scalar depth
fields, and \(m\) output or residual scalars, a count independent of
\(n,L,t\). Eliminating readouts leaves one evolving measure field, without
a claim of minimality among arbitrary encodings.

For the solution write \(Z_a(s,t)=Z_a^{\rho_t}(s)\),
\(P_a(s,t)=P_a^{\rho_t}(s)\), \(f_a(t)=Z_a(1,t)\), and
\(r_a(t)=f_a(t)-y_a\). Its current kernel is

\[
\begin{aligned}
K_{ab}(t)=\int_0^1 P_a(s,t)P_b(s,t)
\int &\nabla_\theta\Phi(\theta,Z_a(s,t))\\[-1mm]
&\cdot\nabla_\theta\Phi(\theta,Z_b(s,t))
\,\rho_t(s,d\theta)\,ds.
\end{aligned}
\tag{3.10}
\]

## 4. Global flow and joint limit theorem

Let \(s_\ell=\ell/L\), and define the empirical layer laws and initial
average error by

\[
\widehat\mu_{\ell,t}^{n,L}
=\frac1n\sum_{i=1}^n\delta_{\theta_{\ell i}(t)},
\qquad
\varepsilon_{n,L}
=\frac1L\sum_{\ell=0}^{L-1}
 \mathcal W_1(\widehat\mu_{\ell,0}^{n,L},\rho_0).
\tag{4.1}
\]

**Theorem 4.1.** Under A1--A2, for every fixed finite scalar batch,
\(\kappa>0\), and \(\rho_0\in\mathcal P_1(\mathbb R^p)\), the following
statements hold.

1. Every finite flow (2.3), from any finite initial parameters, has a unique
   solution for all \(t\ge0\).
2. Equation (3.7) has a unique global characteristic solution in
   \(C([0,\infty);\mathfrak M)\). More generally this holds from every
   initial profile in \(\mathfrak M\), and the resulting autonomous maps
   form a semigroup on \(\mathfrak M\). Thus the exact restart domain is
   the current profile space \(\mathfrak M\).
3. For the constant initial profile \(\rho_0\), the solution has a unique
   \(\mathcal W_1\)-continuous depth representative, constructed in Section
   8. For every \(T<\infty\), a deterministic constant \(C_T<\infty\),
   independent of \(n,L\) and of the realized finite initial parameters,
   gives the pathwise estimate

\[
\begin{aligned}
\sup_{0\le t\le T}\Bigg[&
\frac1L\sum_{\ell=0}^{L-1}
 \mathcal W_1(\widehat\mu_{\ell,t}^{n,L},\rho_t(s_\ell))\\
&+\max_{a,\,0\le\ell\le L}
 |z_{a,\ell}^{n,L}(t)-Z_a(s_\ell,t)|\\
&+\max_{a,\,0\le\ell\le L}
 |p_{a,\ell}^{n,L}(t)-P_a(s_\ell,t)|
 +\max_{a,b}|K_{ab}^{n,L}(t)-K_{ab}(t)|\Bigg]
\le C_T\bigl(\varepsilon_{n,L}+L^{-1}\bigr).
\end{aligned}
\tag{4.2}
\]

Every grid value \(\rho_t(s_\ell)\) in this estimate refers to that canonical
representative, not to arbitrary values assigned to an almost-everywhere
equivalence class.

4. For the independent initialization specified in Section 2, the left
   side of (4.2) tends to zero in probability along every deterministic
   sequence \(n_k,L_k\to\infty\), with no relation between the two rates.
   Outputs, residuals, half mean squared losses, and scaled tangent kernels
   therefore converge uniformly on each fixed compact training-time
   interval.

The constants may depend on the batch, \(\Phi\), \(\kappa\), and \(T\).
No assertion is made for growing horizons \(T=T_{n,L}\), for a discrete
training algorithm, or for convergence to a fitted batch as
\(t\to\infty\).

## 5. Bounds and elementary comparison facts

Write

\[
x_* =\max_a|x_a|,\qquad y_* =\max_a|y_a|,
\qquad Z_*=e^{c_1}(x_*+c_0),\qquad P_*=e^{c_1}.
\tag{5.1}
\]

Throughout the proof \(C\) denotes a finite constant depending only on the
fixed batch, A1--A2 on the strip \([-Z_*,Z_*]\), and \(\kappa\); it can
increase from line to line. A subscript \(T\) permits dependence on the
finite training horizon. Neither constant depends on width, depth, or
parameter support.

The integral Gronwall estimate used here is the following specialization:
if a nonnegative continuous \(u\) satisfies
\(u(s)\le A+\int_0^s(bu(v)+g(v))\,dv\), where \(A,b\ge0\) and
\(g\ge0\) is integrable, then

\[
u(s)\le e^{bs}\left(A+\int_0^s g(v)\,dv\right).
\tag{5.2}
\]

Indeed the right side of the original inequality defines an absolutely
continuous majorant \(U\) with \(U'\le bU+g\); multiply by \(e^{-bs}\)
and integrate. Its discrete counterpart, obtained by iterating
\(u_{\ell+1}\le(1+bh)u_\ell+h g_\ell\), is

\[
u_\ell\le e^{b\ell h}
 \left(u_0+h\sum_{j<\ell}g_j\right).
\tag{5.3}
\]

Reversing the depth index gives the same backward estimate.

A1 and these inequalities imply, for every parameter configuration or
current probability profile,

\[
|z_{a,\ell}^{n,L}|\le Z_*,\qquad
|Z_a^\mu(s)|\le Z_*,\qquad
|r_a^{n,L}|,|r_a^\mu|\le Z_*+y_*.
\tag{5.4}
\]

For example,
\(|z_{a,\ell+1}^{n,L}|\le(1+c_1h)|z_{a,\ell}^{n,L}|+c_0h\),
which yields (5.4); the continuous equation has the corresponding integral
inequality. The forward depth equation is well-defined even for a merely
Borel profile: its right side is measurable in depth, globally
\(c_1\)-Lipschitz in state, and bounded at state zero by \(c_0\). Picard
iteration of the integral equation on an interval with \(c_1\) times its
length less than one is a contraction on continuous paths. Successive
intervals and (5.4) give its unique absolutely continuous solution on
\([0,1]\). If \(c_1=0\), the same construction has no interval restriction.

The sensitivity bounds are

\[
|p_{a,\ell}^{n,L}|\le(1+c_1/L)^L\le P_*,
\qquad
P_a^\mu(s)=\exp\left(
 \int_s^1\int\partial_z\Phi(\theta,Z_a^\mu(u))
 \,\mu(u,d\theta)\,du\right),
\tag{5.5}
\]

and hence \(P_*^{-1}\le P_a^\mu(s)\le P_*\). The continuous sensitivity
is positive. The discrete bound uses absolute values and does not require
\(L>c_1\) or positivity of each discrete factor.

By A2 and (5.4)--(5.5), all parameter velocities are bounded by \(C\),
uniformly over current profiles, and the velocity at a fixed profile is
globally \(C\)-Lipschitz in its parameter argument. Thus
\(\|\theta_{\ell i}(t)-\theta_{\ell i}(0)\|\le Ct\) on any finite
solution interval. The finite vector field is locally Lipschitz in the
full collection of parameters: the forward recursion is \(C^1\), and
A2 makes the sensitivity and parameter-gradient compositions locally
Lipschitz. Picard iteration therefore gives a unique local solution.
If a maximal finite endpoint existed, bounded velocity would make the
parameter vector Cauchy at that endpoint; restarting local existence from
its finite limit would extend it. This proves the finite global assertion.

We will repeatedly use the coupling inequality

\[
\left\|\int g\,d\mu-\int g\,d\nu\right\|
\le \operatorname{Lip}(g)\,\mathcal W_1(\mu,\nu)
\tag{5.6}
\]

for a Lipschitz scalar or vector function \(g\) with defined integrals.
For any coupling, subtract the two integrands and bound by
\(\operatorname{Lip}(g)\|\theta-\widetilde\theta\|\); taking the infimum
proves (5.6). On our state strip, A2 and integration along parameter line
segments give

\[
|\Phi(\theta,z)-\Phi(\widetilde\theta,\widetilde z)|
\le C\|\theta-\widetilde\theta\|+c_1|z-\widetilde z|.
\tag{5.7}
\]

The functions \(\partial_z\Phi\), \(\nabla_\theta\Phi\), and the pairwise
products
\(\nabla_\theta\Phi(\theta,z)\cdot\nabla_\theta\Phi(\theta,\widetilde z)\)
are bounded and jointly Lipschitz on this strip. For the products this
follows by adding and subtracting one mixed product and using the bounded
gradient factors. These are all the transport estimates needed below.

## 6. Population stability at a fixed discrete depth

For a probability profile
\(\boldsymbol\mu=(\mu_0,\ldots,\mu_{L-1})\in\mathcal P_1(\mathbb R^p)^L\),
define population quantities by

\[
Z_{a,0}^{L,\boldsymbol\mu}=x_a,
\quad
Z_{a,\ell+1}^{L,\boldsymbol\mu}
=Z_{a,\ell}^{L,\boldsymbol\mu}
+h\int\Phi(\theta,Z_{a,\ell}^{L,\boldsymbol\mu})\,\mu_\ell(d\theta),
\tag{6.1}
\]

\[
P_{a,L}^{L,\boldsymbol\mu}=1,
\quad
P_{a,\ell}^{L,\boldsymbol\mu}
=P_{a,\ell+1}^{L,\boldsymbol\mu}
 \left(1+h\int\partial_z\Phi(\theta,Z_{a,\ell}^{L,\boldsymbol\mu})
 \,\mu_\ell(d\theta)\right).
\tag{6.2}
\]

Write \(r_a^{L,\boldsymbol\mu}=Z_{a,L}^{L,\boldsymbol\mu}-y_a\) and

\[
V_\ell^L[\boldsymbol\mu](\theta)
=-\frac\kappa m\sum_a r_a^{L,\boldsymbol\mu}
 P_{a,\ell+1}^{L,\boldsymbol\mu}
 \nabla_\theta\Phi(\theta,Z_{a,\ell}^{L,\boldsymbol\mu}).
\tag{6.3}
\]

The kernel \(K^{L,\boldsymbol\mu}\) is defined by (2.7) with these
population states and sensitivities and with the empirical integral
replaced by \(\mu_\ell\). All bounds of Section 5 apply to these objects.

For two such profiles let

\[
w_\ell=\mathcal W_1(\mu_\ell,\nu_\ell),
\qquad d_L(\boldsymbol\mu,\boldsymbol\nu)=h\sum_{\ell=0}^{L-1}w_\ell.
\tag{6.4}
\]

Put \(e_\ell=\max_a|Z_{a,\ell}^{L,\boldsymbol\mu}
-Z_{a,\ell}^{L,\boldsymbol\nu}|\). Subtract (6.1), first compare state
arguments at a common law, and then use (5.6)--(5.7). This gives

\[
e_0=0,\qquad
e_{\ell+1}\le(1+c_1h)e_\ell+Chw_\ell,
\qquad
\max_\ell e_\ell\le C d_L(\boldsymbol\mu,\boldsymbol\nu).
\tag{6.5}
\]

For \(b_\ell=\max_a|P_{a,\ell}^{L,\boldsymbol\mu}
-P_{a,\ell}^{L,\boldsymbol\nu}|\), subtract (6.2). The coefficient
difference is at most \(C(e_\ell+w_\ell)\), while the other sensitivity
factor is at most \(P_*\). Consequently

\[
b_L=0,\qquad
b_\ell\le(1+c_1h)b_{\ell+1}+Ch(e_\ell+w_\ell),
\qquad
\max_\ell b_\ell\le C d_L(\boldsymbol\mu,\boldsymbol\nu).
\tag{6.6}
\]

The output residual difference is bounded by \(e_L\). Substituting these
estimates into (6.3) yields the uniform velocity estimate

\[
\|V_\ell^L[\boldsymbol\mu](\theta)
-V_\ell^L[\boldsymbol\nu](\widetilde\theta)\|
\le C\bigl(\|\theta-\widetilde\theta\|
             +d_L(\boldsymbol\mu,\boldsymbol\nu)\bigr).
\tag{6.7}
\]

Similarly, each kernel summand differs by at most
\(C(e_\ell+b_{\ell+1}+w_\ell)\), by the product estimate in Section 5.
Averaging gives

\[
\max_{a,b}|K_{ab}^{L,\boldsymbol\mu}
-K_{ab}^{L,\boldsymbol\nu}|
\le C d_L(\boldsymbol\mu,\boldsymbol\nu).
\tag{6.8}
\]

Consider the characteristic population equations

\[
\partial_t\mu_{\ell,t}^L+
\nabla_\theta\cdot
 \bigl(\mu_{\ell,t}^L V_\ell^L[\boldsymbol\mu_t^L]\bigr)=0.
\tag{6.9}
\]

For two solutions, take at each layer an initial coupling with expected
distance at most \(w_\ell(0)+\epsilon\), and transport it by their
characteristic flows. Denote the resulting expected distances by
\(H_\ell(t)\). Equation (6.7) implies

\[
H_\ell(t)\le H_\ell(0)+C\int_0^t
 \bigl(H_\ell(u)+d_L(\boldsymbol\mu_u^L,\boldsymbol\nu_u^L)\bigr)\,du.
\tag{6.10}
\]

Since \(d_L(\boldsymbol\mu_t^L,\boldsymbol\nu_t^L)
\le h\sum_\ell H_\ell(t)\), averaging, applying (5.2), and letting
\(\epsilon\downarrow0\) gives

\[
d_L(\boldsymbol\mu_t^L,\boldsymbol\nu_t^L)
\le e^{Ct}d_L(\boldsymbol\mu_0^L,\boldsymbol\nu_0^L).
\tag{6.11}
\]

Existence and uniqueness of (6.9) follow by the characteristic contraction
construction in Section 7, applied to the complete finite product space
with metric \(d_L\), velocity bound \(C\), and estimate (6.7). The
contraction interval is independent of \(L\). Empirical laws solve (6.9)
exactly: their readouts equal (2.1) and (2.4), and differentiating a compactly
supported \(C^1\) test function along each atom gives (6.9) in weak form.
Uniqueness of the characteristic solution identifies them with that
population flow from their empirical initial profiles.

## 7. Complete profile space, global characteristics, and restart

We first justify the metric framework. The space
\((\mathcal P_1(\mathbb R^p),\mathcal W_1)\) is complete and separable.
For completeness, from a Cauchy sequence choose a subsequence whose
successive distances are summable. Choose couplings of successive laws
with summable expected distances. These couplings can be put on one
probability space using the following form of disintegration: a Borel
probability \(\pi\) on \(\mathbb R^p\times\mathbb R^p\) with first
marginal \(\mu\) admits a Borel probability kernel \(k\) such that
\(\pi(d\theta,d\widetilde\theta)=\mu(d\theta)k(\theta,d\widetilde\theta)\).
Apply this to each successive coupling and sample the next coordinate
from its kernel. The consistent finite-dimensional products of these
kernels define a countable joint law. Each adjacent pair has the chosen
coupling by construction. The resulting random variables satisfy
\(\sum_j\mathbb E\|U_{j+1}-U_j\|<\infty\), so their successive distances
are summable almost surely, and they converge in the complete space
\(\mathbb R^p\) to an integrable random variable \(U\). The tail bound gives
\(\mathbb E\|U_j-U\|\to0\), hence convergence of the laws in
\(\mathcal W_1\). The original Cauchy sequence has the same limit.
Separability follows by truncating a law, moving its mass to a finite
rational grid, and approximating those masses by rational probabilities;
the coupling costs of these operations tend to zero.

Now let \((\mu_j)\) be \(\mathcal D\)-Cauchy in \(\mathfrak M\). Choose
a subsequence, relabeled \((\mu_j)\), with
\(\sum_j\mathcal D(\mu_j,\mu_{j+1})<\infty\). Fubini gives a full-measure
set of depths where the successive \(\mathcal W_1\) distances are summable.
Pointwise completeness yields a limit law \(\mu(s)\) there; assign a fixed
law on the exceptional set. The convergence set is Borel, and a pointwise
limit of Borel maps into a metric space is Borel. The triangle inequality
and Fatou give

\[
\mathcal D(\mu_j,\mu)
\le\sum_{k\ge j}\mathcal D(\mu_k,\mu_{k+1})\longrightarrow0.
\tag{7.1}
\]

Also \(\mathcal D(\mu,\delta_0)<\infty\), because it is bounded by the
distance to one \(\mu_j\) plus its finite first moment. Here \(\delta_0\)
denotes the constant profile of point masses at zero, and
\(\mathcal W_1(\mu(s),\delta_0)=\int\|\theta\|\,d\mu(s)\).
Thus \(\mu\in\mathfrak M\), and the full Cauchy sequence converges to it.
The same facts prove completeness of the finite product used in Section 6.

For \(\mu,\nu\in\mathfrak M\), the continuous version of (6.5) is

\[
|Z_a^\mu(s)-Z_a^\nu(s)|
\le\int_0^s\left(c_1|Z_a^\mu(u)-Z_a^\nu(u)|
+C\mathcal W_1(\mu(u),\nu(u))\right)\,du.
\tag{7.2}
\]

It gives \(\max_a\|Z_a^\mu-Z_a^\nu\|_\infty\le C\mathcal D(\mu,\nu)\).
In the exponential formula (5.5), the exponents lie in \([-c_1,c_1]\).
Their difference is bounded, using A2 and (5.6), by
\(C\int_0^1(|Z_a^\mu-Z_a^\nu|+\mathcal W_1(\mu(u),\nu(u)))\,du\).
The exponential is \(e^{c_1}\)-Lipschitz on this interval. Therefore

\[
\max_a\|Z_a^\mu-Z_a^\nu\|_\infty
+\max_a\|P_a^\mu-P_a^\nu\|_\infty
+\max_a|r_a^\mu-r_a^\nu|
\le C\mathcal D(\mu,\nu).
\tag{7.3}
\]

This implies

\[
\|v[\mu](s,\theta)-v[\nu](s,\widetilde\theta)\|
\le C\bigl(\|\theta-\widetilde\theta\|+\mathcal D(\mu,\nu)\bigr).
\tag{7.4}
\]

Furthermore, (3.4)--(3.5) and the uniform bounds imply for every current
profile, without assuming its depth continuity,

\[
|Z_a^\mu(s)-Z_a^\mu(u)|+|P_a^\mu(s)-P_a^\mu(u)|
\le C|s-u|,
\qquad
\sup_\theta\|v[\mu](s,\theta)-v[\mu](u,\theta)\|
\le C|s-u|.
\tag{7.5}
\]

Thus \(v[\mu]\) has a bounded jointly continuous representative on
\([0,1]\times\mathbb R^p\), and \(\mu\mapsto v[\mu]\) is Lipschitz
from \(\mathfrak M\) into that space with the supremum norm. This map is
well-defined on equivalence classes: null-set changes in a profile leave
the depth integrals, hence their continuous readouts, unchanged.

Fix \(\mu_{\rm in}\in\mathfrak M\), and a continuous trial curve
\(\bar\mu\in C([t_0,t_0+\tau];\mathfrak M)\). Its velocity is jointly
continuous in time, depth, and parameter, bounded by \(C\), and globally
\(C\)-Lipschitz in parameter. For each \((s,\vartheta)\), solve

\[
\Theta_t(s,\vartheta)=\vartheta+
 \int_{t_0}^t v[\bar\mu_u](s,\Theta_u(s,\vartheta))\,du.
\tag{7.6}
\]

The exact ODE fact needed is that a continuous bounded vector field,
globally Lipschitz in the state with one uniform constant, has a unique
global solution from every initial point, with continuous dependence on
parameters for which the field is continuous. To see it here, iterate the
right side of (7.6) on continuous paths; it contracts when \(C\tau<1\).
Uniform limits of the iterates preserve joint continuity in
\((t,s,\vartheta)\), and bounded velocity permits successive intervals of
the same length. Applying (5.2) to two integral equations proves uniqueness
and the required dependence estimates.

Define

\[
(\Gamma\bar\mu)_t(s)
=(\Theta_t(s,\cdot))_\#\mu_{\rm in}(s).
\tag{7.7}
\]

These are Borel profiles: integration of a bounded Borel function of
\((s,\vartheta)\) against a Borel probability kernel is Borel, as follows
first for indicator rectangles and then for bounded functions by simple
approximation. Apply this to test functions of the continuous map
\(\Theta_t\); truncation also gives measurability of its first moment.
To check Borel measurability specifically in the \(\mathcal W_1\) topology,
quantize any such kernel on a fixed finite grid in a ball of radius \(N\),
with mesh tending to zero, and send the exterior to zero. The resulting
laws have Borel masses on a fixed finite support, hence are Borel as
\(\mathcal W_1\)-valued maps. At each depth they converge in
\(\mathcal W_1\) to the original law: the coupling cost is bounded by
the mesh error plus its first-moment tail outside that ball. Their
pointwise limit is therefore Borel in the required topology.
The displacement estimate \(\|\Theta_t-\vartheta\|\le C(t-t_0)\) proves
that (7.7) lies in \(\mathfrak M\). Coupling two times by the same initial
parameter gives continuity, indeed a \(C\)-Lipschitz bound, in
\(\mathcal D\).

For two trial curves with the same starting profile, couple characteristics
using exactly the same initial parameter. Equation (7.4) and (5.2) give,
uniformly in \(s,\vartheta,t\),

\[
\|\Theta_t^{\bar\mu}(s,\vartheta)
-\Theta_t^{\bar\nu}(s,\vartheta)\|
\le C\tau e^{C\tau}
\sup_{u\in[t_0,t_0+\tau]}\mathcal D(\bar\mu_u,\bar\nu_u).
\tag{7.8}
\]

Push forward the common law and integrate in depth. The map \(\Gamma\)
is a contraction on the complete space of continuous curves when
\(C\tau e^{C\tau}<1\). For completeness, iterating a contraction of
factor \(q<1\) gives successive distances bounded by a geometric series;
completeness supplies a limit, continuity of the map makes it a fixed
point, and \(d(u,v)\le qd(u,v)\) proves uniqueness. Applied to \(\Gamma\),
this constructs the characteristic solution. Differentiating a test
function along each characteristic, using bounded velocity, proves (3.9).

The constants do not depend on \(\mu_{\rm in}\), and

\[
\mathcal D(\rho_t,\rho_u)\le C|t-u|,
\qquad
\int_0^1\int\|\theta\|\,\rho_t(s,d\theta)\,ds
\le\int_0^1\int\|\theta\|\,\mu_{\rm in}(s,d\theta)\,ds+Ct.
\tag{7.9}
\]

The construction therefore iterates for all nonnegative times, from every
initial profile in \(\mathfrak M\). Uniqueness is in the characteristic
class specified in (3.8); no larger class of unspecified distributional
solutions is needed.

One can obtain stability on all of \(\mathfrak M\) without selecting a
measurable family of optimal couplings. Let \(\rho,\widetilde\rho\) start
from \(\mu_{\rm in},\nu_{\rm in}\), respectively. At each individual
depth and for any coupling of those initial laws, let \(H_s(t)\) be the
expected distance after transporting the coupling by the two flows.
Their integral equations and (7.4) bound \(H_s(t)\) by its initial value plus
\(C\int_0^t\bigl(H_s(u)+\mathcal D(\rho_u,\widetilde\rho_u)\bigr)\,du\).
Gronwall and an infimum over that depth's initial couplings yield

\[
\mathcal W_1(\rho_t(s),\widetilde\rho_t(s))
\le e^{Ct}\mathcal W_1(\mu_{\rm in}(s),\nu_{\rm in}(s))
+C\int_0^t e^{C(t-u)}\mathcal D(\rho_u,\widetilde\rho_u)\,du.
\tag{7.10}
\]

Both sides are measurable in depth. Integrating and applying Gronwall
again gives
\(\mathcal D(\rho_t,\widetilde\rho_t)
\le e^{Ct}\mathcal D(\mu_{\rm in},\nu_{\rm in})\), with a possibly larger
\(C\). Finally the velocity depends only on the current state. Restarting
at time \(u\) with \(\rho_u\in\mathfrak M\) yields its unique
continuation. If \(S_t\) is the resulting map on profiles, uniqueness
gives \(S_0=\mathrm{id}\) and \(S_{t+u}=S_tS_u\).

## 8. Canonical depth representative and depth consistency

Return to the constant initial profile \(\rho_0\). The continuous velocity
constructed in Section 7 defines \(\Theta_t(s,\vartheta)\) at every
\(s\in[0,1]\). Use (3.8) to define \(\rho_t(s)\) at every depth, including
the endpoints. This agrees almost everywhere with the profile solution.
At two depths couple characteristics with the same
\(\vartheta\sim\rho_0\). By (7.4)--(7.5),

\[
\|\Theta_t(s,\vartheta)-\Theta_t(u,\vartheta)\|
\le C\int_0^t
 \bigl(\|\Theta_\tau(s,\vartheta)-\Theta_\tau(u,\vartheta)\|
       +|s-u|\bigr)\,d\tau.
\tag{8.1}
\]

Thus, on every \([0,T]\),

\[
\mathcal W_1(\rho_t(s),\rho_t(u))\le C_T|s-u|,
\qquad
\mathcal W_1(\rho_t(s),\rho_v(s))\le C|t-v|.
\tag{8.2}
\]

This is the canonical continuous depth representative. Any other
continuous representative agreeing almost everywhere agrees everywhere:
its distance from this one is a continuous nonnegative function, which
cannot be positive at one point while zero almost everywhere. The
construction uses constant initialization; arbitrary profiles in
\(\mathfrak M\) need not acquire a continuous depth representative.

For clarity set, in this section only,

\[
F_a(s,t)=\int\Phi(\theta,Z_a(s,t))\,\rho_t(s,d\theta),
\qquad
B_a(s,t)=\int\partial_z\Phi(\theta,Z_a(s,t))\,\rho_t(s,d\theta).
\tag{8.3}
\]

These are scalar depth coefficients, not outputs or matrices. By
(5.6)--(5.7), A2, and (8.2), both are uniformly \(C_T\)-Lipschitz in
depth. The forward integral equation consequently has the local defect

\[
Z_a(s_{\ell+1},t)
=Z_a(s_\ell,t)+h F_a(s_\ell,t)+d_{a,\ell}^{Z}(t),
\qquad |d_{a,\ell}^{Z}(t)|\le C_T h^2.
\tag{8.4}
\]

The exact backward integral equation is
\(P_a(s_\ell,t)=P_a(s_{\ell+1},t)
+\int_{s_\ell}^{s_{\ell+1}}P_a(u,t)B_a(u,t)\,du\).
Replacing its integrand by
\(P_a(s_{\ell+1},t)B_a(s_\ell,t)\) costs at most \(C_T h^2\), since
both factors are bounded and depth-Lipschitz. Hence the precise discrete
adjoint convention has defect

\[
P_a(s_\ell,t)
=P_a(s_{\ell+1},t)(1+h B_a(s_\ell,t))
+d_{a,\ell}^{P}(t),
\qquad |d_{a,\ell}^{P}(t)|\le C_T h^2.
\tag{8.5}
\]

Let \(\boldsymbol\mu_t^L\) solve (6.9) from
\(\mu_{\ell,0}^L=\rho_0\) at every layer, and abbreviate its readouts by
\(Z_{a,\ell}^{L},P_{a,\ell}^{L},V_\ell^L,K_{ab}^{L}\). Define

\[
E_L(t)=\max_{0\le\ell<L}
 \mathcal W_1(\mu_{\ell,t}^L,\rho_t(s_\ell)).
\tag{8.6}
\]

Subtract (8.4) from (6.1). The resulting state errors obey (6.5) with
\(w_\ell\le E_L(t)\) and an added \(C_T h^2\) at each step. Subtracting
(8.5) from (6.2) gives (6.6) with the same extra defect. Applying (5.3)
in each direction yields

\[
\max_{a,\ell}|Z_{a,\ell}^{L}(t)-Z_a(s_\ell,t)|
+\max_{a,\ell}|P_{a,\ell}^{L}(t)-P_a(s_\ell,t)|
\le C_T\bigl(E_L(t)+h\bigr).
\tag{8.7}
\]

In comparing velocities, the finite-depth velocity uses
\(P_{a,\ell+1}^{L}\) and the continuous one uses \(P_a(s_\ell,t)\).
Their difference is bounded by (8.7) plus
\(|P_a(s_{\ell+1},t)-P_a(s_\ell,t)|\le Ch\). Residual and feature-gradient
differences are bounded by (8.7) and A2. Consequently

\[
\sup_{\ell,\theta}
 \|V_\ell^L(\theta,t)-v[\rho_t](s_\ell,\theta)\|
\le C_T\bigl(E_L(t)+h\bigr).
\tag{8.8}
\]

Let \(\Theta_{\ell,t}^L(\vartheta)\) be the characteristic of
\(V_\ell^L\). Couple it with \(\Theta_t(s_\ell,\vartheta)\) from the same
\(\vartheta\sim\rho_0\), and write

\[
H_L(t)=\max_{\ell<L}\int
 \|\Theta_{\ell,t}^L(\vartheta)-\Theta_t(s_\ell,\vartheta)\|
 \,\rho_0(d\vartheta).
\tag{8.9}
\]

Then \(E_L\le H_L\), \(H_L(0)=0\), and parameter Lipschitzness together
with (8.8) gives

\[
H_L(t)\le C_T\int_0^t(H_L(u)+h)\,du.
\tag{8.10}
\]

There is no maximum over random empirical layer errors here: these are
deterministic population solutions from the common law. Gronwall proves

\[
\sup_{t\le T}\left[
E_L(t)+\max_{a,\ell}|Z_{a,\ell}^{L}(t)-Z_a(s_\ell,t)|
+\max_{a,\ell}|P_{a,\ell}^{L}(t)-P_a(s_\ell,t)|\right]
\le C_T L^{-1}.
\tag{8.11}
\]

For the kernel, the continuous integrand in (3.10), after integrating in
parameter, is bounded and \(C_T\)-Lipschitz in depth. Comparing a discrete
summand with its value at \(s_\ell\) costs at most
\(C_T(E_L(t)+h)\), by (8.7), the sensitivity index shift, and the
coupling estimate for the gradient product. A Lipschitz scalar function
\(g\) satisfies

\[
\left|h\sum_{\ell=0}^{L-1}g(s_\ell)-\int_0^1g(s)\,ds\right|
\le\sum_\ell\int_{s_\ell}^{s_{\ell+1}}
 \operatorname{Lip}(g)|s-s_\ell|\,ds
\le\tfrac12\operatorname{Lip}(g)h.
\tag{8.12}
\]

Using (8.11) and this Riemann-sum bound proves

\[
\sup_{t\le T}\max_{a,b}|K_{ab}^{L}(t)-K_{ab}(t)|\le C_T L^{-1}.
\tag{8.13}
\]

## 9. Width convergence and completion of the joint theorem

The exact empirical flow and the discrete-depth population flow are two
solutions of (6.9). Their initial distance is \(\varepsilon_{n,L}\).
Equations (6.5)--(6.8) and (6.11) imply pathwise

\[
\begin{aligned}
\sup_{t\le T}\Big[&
d_L(\widehat{\boldsymbol\mu}_t^{n,L},\boldsymbol\mu_t^L)
+\max_{a,\ell}|z_{a,\ell}^{n,L}(t)-Z_{a,\ell}^{L}(t)|\\
&+\max_{a,\ell}|p_{a,\ell}^{n,L}(t)-P_{a,\ell}^{L}(t)|
+\max_{a,b}|K_{ab}^{n,L}(t)-K_{ab}^{L}(t)|\Big]
\le C_T\varepsilon_{n,L}.
\end{aligned}
\tag{9.1}
\]

The triangle inequality with (8.11) and (8.13) proves (4.2).
In particular, only the average of the empirical initialization errors
appears. Replacing it by a layer maximum would impose an unnecessary
restriction on how fast depth could grow.

We prove the initialization convergence under exactly the first-moment
assumption. For independent \(\vartheta_i\sim\rho_0\), put

\[
\alpha_n=\mathbb E\mathcal W_1\left(
 \frac1n\sum_{i=1}^n\delta_{\vartheta_i},\rho_0\right).
\tag{9.2}
\]

Let \(T_R\) be radial projection onto the closed Euclidean ball of radius
\(R>0\). Coupling each point to its projection and using the triangle
inequality gives

\[
\alpha_n\le
\mathbb E\mathcal W_1\left(
 \frac1n\sum_i\delta_{T_R\vartheta_i},(T_R)_\#\rho_0\right)
+2\mathbb E\|\vartheta_1-T_R\vartheta_1\|.
\tag{9.3}
\]

Here is a direct finite-partition proof that the first term tends to zero
for fixed \(R\). Cover the ball by finitely many sets of diameter at most
\(\epsilon\), form a Borel partition subordinate to that cover, and send
each nonempty cell to a representative point in that cell. Denote its
\(J\) cell probabilities by \(\pi_j\) and the empirical frequencies by
\(\widehat\pi_j\). Quantizing both measures costs at most
\(2\epsilon\). The unmatched mass of the quantized measures is
\(\tfrac12\sum_j|\widehat\pi_j-\pi_j|\), and it can be moved within
diameter \(2R\). Independence gives
\(\mathbb E|\widehat\pi_j-\pi_j|
\le\sqrt{\pi_j(1-\pi_j)/n}\) by the variance formula and Cauchy--Schwarz.
Therefore

\[
\mathbb E\mathcal W_1\left(
 \frac1n\sum_i\delta_{T_R\vartheta_i},(T_R)_\#\rho_0\right)
\le2\epsilon+R\sum_{j=1}^J
 \sqrt{\frac{\pi_j(1-\pi_j)}n}.
\tag{9.4}
\]

First let \(n\to\infty\), then \(\epsilon\downarrow0\). Finally the tail
term in (9.3) tends to zero as \(R\to\infty\), since
\(\|\vartheta-T_R\vartheta\|=(\|\vartheta\|-R)_+\le\|\vartheta\|\)
and the first moment is finite. This proves \(\alpha_n\to0\), without
a dimension-dependent rate claim.

Every layer has the same initialization distribution, so linearity of
expectation gives, for every \(L\),

\[
\mathbb E\varepsilon_{n,L}=\alpha_n.
\tag{9.5}
\]

Independence across layers is part of the specified initialization but is
not needed for this expectation identity. If \(\mathscr E_{n,L}(T)\)
denotes the nonnegative left side of (4.2), then for \(\epsilon>0\),

\[
\mathbb P\{\mathscr E_{n,L}(T)>\epsilon\}
\le\frac{\mathbb E\mathscr E_{n,L}(T)}\epsilon
\le\frac{C_T}{\epsilon}(\alpha_n+L^{-1})\longrightarrow0
\tag{9.6}
\]

along every deterministic joint sequence in the theorem. Taking the
terminal forward state gives output and residual convergence. Since all
residuals have absolute value at most \(Z_*+y_*\),

\[
|\mathcal L^{n,L}(t)-\mathcal L(t)|
\le (Z_*+y_*)\max_a|f_a^{n,L}(t)-f_a(t)|,
\qquad \mathcal L(t)=\frac1{2m}\sum_a r_a(t)^2.
\tag{9.7}
\]

This proves the stated loss convergence and completes Theorem 4.1.

Equivalently, make the empirical profile piecewise constant on the depth
cells. Its distance \(\mathcal D\) to \(\rho_t\) is at most the first
term in (4.2) plus \(C_T/L\), by (8.2). Thus the measure convergence is
also convergence in the specified profile metric, uniformly on compact
training intervals. No training-time Euler discretization has been used;
the Euler defects above are solely the architectural depth discretization.

## 10. Differentiable output and dissipation readouts

The kernel (3.10) is positive semidefinite: for every \(c\in\mathbb R^m\),

\[
c^T K(t)c
=\int_0^1\int
 \left\|\sum_{a=1}^m c_a P_a(s,t)
 \nabla_\theta\Phi(\theta,Z_a(s,t))\right\|^2
 \,\rho_t(s,d\theta)\,ds\ge0.
\tag{10.1}
\]

We justify differentiating the output using characteristics. By (7.3) and
(7.9), \(Z_a\), \(P_a\), and \(r_a\) are Lipschitz in training time,
uniformly in depth. In the characteristic forward integral equation,

\[
Z_a(s,t)=x_a+\int_0^s\int
 \Phi(\Theta_t(u,\vartheta),Z_a(u,t))
 \,\rho_0(d\vartheta)\,du,
\tag{10.2}
\]

both arguments change by at most a constant times the training-time
increment. The derivatives of \(\Phi\) on the state strip are bounded
and Lipschitz by A1--A2. The fundamental theorem of calculus along the
segment between two argument pairs therefore writes the difference
quotient of the integrand as its current derivatives times the argument
difference quotients, with a uniformly vanishing remainder. The parameter
quotient converges uniformly to
\(v[\rho_t](u,\Theta_t(u,\vartheta))\), by the characteristic equation
and continuity of the velocity. Subtraction of the resulting linear
Volterra equation and (5.2) then makes the state quotient converge
uniformly in depth. Boundedness permits integration over
\(\rho_0\) and depth. Thus \(U_a(s,t)=\partial_t Z_a(s,t)\) exists and
satisfies

\[
\partial_s U_a(s,t)=B_a(s,t)U_a(s,t)+J_a(s,t),
\qquad U_a(0,t)=0,
\tag{10.3}
\]

where the scalar coefficients are

\[
B_a(s,t)=\int\partial_z\Phi(\theta,Z_a(s,t))\,\rho_t(s,d\theta),
\qquad
J_a(s,t)=\int\nabla_\theta\Phi(\theta,Z_a(s,t))\cdot
 v[\rho_t](s,\theta)\,\rho_t(s,d\theta).
\tag{10.4}
\]

The coefficients depend continuously on training time, so this derivative
is continuous as well; at \(t=0\) take the right derivative. Multiplying
(10.3) by \(P_a\), and using \(\partial_sP_a=-B_aP_a\), gives
\(\partial_s(P_aU_a)=P_aJ_a\). Integrate in depth, use
\(P_a(1,t)=1\), and substitute (3.6):

\[
\dot f_a(t)=\int_0^1P_a(s,t)J_a(s,t)\,ds
=-\frac\kappa m\sum_{b=1}^mK_{ab}(t)r_b(t).
\tag{10.5}
\]

It follows that

\[
\frac d{dt}\mathcal L(t)
=-\frac\kappa{m^2}r(t)^T K(t)r(t)
=-\kappa\int_0^1\int\|Q[\rho_t](s,\theta)\|^2
 \,\rho_t(s,d\theta)\,ds\le0.
\tag{10.6}
\]

For a general initial profile \(\mu_{\rm in}\in\mathfrak M\), the same
proof replaces \(\rho_0(d\vartheta)\) in (10.2) by
\(\mu_{\rm in}(u,d\vartheta)\); bounded derivatives and velocities give
the same domination, with depth equations understood almost everywhere.
Thus these formulas remain current-profile readouts on the entire restart
domain. Positive dissipation energy is the precise condition
for strictly decreasing loss at an instant. For a batch, a nonzero
residual vector and nonzero individual gradients can still cancel in
\(Q\); positivity of the full energy in (10.6) is required. A1--A2 do not
give a positive lower kernel bound or eventual zero loss. For example,
\(\Phi\equiv0\) satisfies both assumptions and leaves any unmatched input
and label unchanged for all training times.

## 11. A concrete general activation class

Take \(p=3\) and the explicitly typed scalar maps
\(A,U,B:\mathbb R\to\mathbb R\). Suppose each map and its first
derivative are bounded and each first derivative is globally Lipschitz;
write this condition as \(A,U,B\in C_b^{1,1}(\mathbb R)\). Let
\(\sigma:\mathbb R\to\mathbb R\) be continuously differentiable with
bounded, globally Lipschitz derivative. Define the particle feature by

\[
\Phi((\alpha,\omega,\beta),z)
=A(\alpha)\,\sigma\bigl(U(\omega)z+B(\beta)\bigr).
\tag{11.1}
\]

The scalar nonlinearity \(\sigma\) is only a component of \(\Phi\); the
bounded maps specify the raw parameterization to which the theorem applies.
Let \(u=U(\omega)z+B(\beta)\). Direct differentiation gives

\[
\begin{aligned}
\partial_z\Phi&=A(\alpha)\sigma'(u)U(\omega),\\
\partial_\alpha\Phi&=A'(\alpha)\sigma(u),\\
\partial_\omega\Phi&=A(\alpha)\sigma'(u)U'(\omega)z,\\
\partial_\beta\Phi&=A(\alpha)\sigma'(u)B'(\beta).
\end{aligned}
\tag{11.2}
\]

Because \(\sigma'\) is bounded,
\(|\sigma(u)|\le|\sigma(0)|+\|\sigma'\|_\infty|u|\).
At \(z=0\), the argument \(B(\beta)\) is bounded; this bounds
\(\Phi(\theta,0)\). The first line of (11.2) is bounded on all parameter
and state space, proving A1. On any bounded state strip, \(u\) and
\(\sigma(u)\) are bounded. The argument map is Lipschitz jointly in raw
parameters and state there, and each factor in (11.2) is bounded and
Lipschitz there. Expanding differences of these products proves all of A2.

Examples of \(\sigma\) include tanh, arctangent, logistic sigmoid, erf,
sine, softsign, identity, affine functions, softplus, and GELU, as well as
positive rescalings and affine recenterings. For the smooth bounded
examples, bounded first and second derivatives verify the conditions.
Softsign \(\sigma(u)=u/(1+|u|)\) has continuous derivative
\((1+|u|)^{-2}\), which is bounded and globally Lipschitz even at zero.
Softplus \(\log(1+e^u)\) has a bounded logistic derivative with bounded
derivative. For exact GELU, write
\(\sigma(u)=u\mathcal N(u)\), where \(\mathcal N\) is the standard
normal distribution function and \(\gamma\) its density. Then
\(\sigma'(u)=\mathcal N(u)+u\gamma(u)\) and
\(\sigma''(u)=(2-u^2)\gamma(u)\) are bounded. These checks allow linear
growth of \(\sigma\).

For instance, choosing \(A(\alpha)=\tanh\alpha\),
\(U(\omega)=\tanh\omega\), \(B(\beta)=\tanh\beta\), and
\(\sigma=\tanh\) gives a nonlinear admissible feature. Nonaffinity is
not needed for the convergence theorem. Nontrivial motion is possible
whenever there is a pair \((\theta_*,z_*)\) with
\(\nabla_\theta\Phi(\theta_*,z_*)\ne0\): take one input \(x_1=z_*\),
the constant atomic initialization \(\rho_0=\delta_{\theta_*}\), and a
label different from its initial output. By continuity, the gradient is
nonzero on a positive interval of depths near zero, and \(P_1>0\), so
the energy in (10.6) is positive initially. In contrast, nonaffinity and
an unmatched label alone do not ensure motion at a specified
initialization.

Exact ReLU is outside the differentiability assumptions. Treating its
kinks through a differential inclusion or a crossing argument would
require a different result. An untruncated superlinear feature is not
covered by A1. If only stripwise forward regularity is available, the
comparison estimates have a local version on an independently controlled
state strip, with constants depending on that control; this does not
establish global existence without a separate bound. Unbounded effective
raw weights generally also violate A1 or A2. Extending the global result
to those parameterizations would require additional propagated moment or
coercivity estimates and an appropriate weighted transport metric.

## 12. Limits of finite linear-moment closure

A measure field can sometimes have a shorter special representation. The
following exact obstruction specifies what fails for general fixed moment
lists; it is not a claim about every possible nonlinear encoding.

**Proposition 12.1.** Fix an integer \(J\ge0\) and real-valued functions
\(\psi_1,\ldots,\psi_J\) on \(\mathbb R^p\). Fix a scalar state \(z\).
Suppose that any two finitely supported probability laws with equal
values of all \(\int\psi_j\,d\mu\) also have equal values of
\(\int\Phi(\theta,z)\,\mu(d\theta)\). Then

\[
\Phi(\cdot,z)\in\operatorname{span}\{1,\psi_1,\ldots,\psi_J\}.
\tag{12.1}
\]

Conversely, this span condition makes that integral a function of the
declared moments for every finitely supported probability law.

**Proof.** Put \(b(\theta)=(1,\psi_1(\theta),\ldots,\psi_J(\theta))\).
If every finite relation \(\sum_i c_i b(\theta_i)=0\) also satisfied
\(\sum_i c_i\Phi(\theta_i,z)=0\), the assignment

\[
\sum_i c_i b(\theta_i)\longmapsto
\sum_i c_i\Phi(\theta_i,z)
\tag{12.2}
\]

would define a well-defined linear functional on the span of the vectors
\(b(\theta)\) in \(\mathbb R^{J+1}\). Extending a basis to that of
\(\mathbb R^{J+1}\) would represent it by a coefficient vector, expressing
\(\Phi(\cdot,z)\) in the span in (12.1). Thus, if (12.1) fails, there
exist finitely many points and coefficients with

\[
\sum_i c_i=0,\qquad
\sum_i c_i\psi_j(\theta_i)=0\quad(1\le j\le J),\qquad
\sum_i c_i\Phi(\theta_i,z)\ne0.
\tag{12.3}
\]

The positive and negative parts of \((c_i)\) have equal total mass
\(M>0\). Define probability laws
\(\mu_+=M^{-1}\sum_i(c_i)_+\delta_{\theta_i}\) and
\(\mu_-=M^{-1}\sum_i(-c_i)_+\delta_{\theta_i}\). Their declared moments
are identical, while their forward-feature integrals differ by the
nonzero last quantity in (12.3) divided by \(M\). This contradicts the
hypothesis. The converse follows by integrating the linear combination
in (12.1). \(\square\)

It follows that if

\[
\operatorname{span}\{\Phi(\cdot,z):z\in I\}
\quad\hbox{is infinite-dimensional}
\tag{12.4}
\]

on a state interval \(I\), no fixed finite list of state-independent
linear moments recovers the forward coefficient for every finitely
supported law and every \(z\in I\). Such moments cannot give a universal
exact closure of the training equation with those readouts.

Here are sufficient nondegeneracy conditions for (12.4) in (11.1).
Suppose \(A(\alpha_0)\ne0\), fix \(B(\beta_0)=b_0\), assume the range
of \(U\) contains a neighborhood of zero, and assume \(\sigma\) is real
analytic near \(b_0\) with infinitely many nonzero Taylor coefficients
there. Let \(I\) contain a nonzero open subinterval. Choose arbitrarily
many distinct states of one sign in a smaller subinterval. On the fixed
parameter slice the functions of the effective slope \(w\) are
\(\sigma(b_0+wz)\), with \(w\) ranging over a neighborhood of zero.
An identity among \(N\) such functions, with coefficients \(c_j\), would
force

\[
\sum_{j=1}^N c_j z_j^{k_i}=0,\qquad 1\le i\le N,
\tag{12.5}
\]

for any \(N\) distinct orders \(0\le k_1<\cdots<k_N\) with nonzero
Taylor coefficients. The matrix in (12.5) is nonsingular for
distinct positive \(z_j\). To prove this, a nonzero linear combination
of \(N\) monomials with increasing real exponents has at most \(N-1\)
distinct positive zeros. Divide by the smallest power. If there were
\(N\) distinct zeros, Rolle's theorem would give at least \(N-1\) zeros
of the derivative, which has at most \(N-1\) nonzero monomial terms and
therefore at most \(N-2\) zeros by induction. The one-term base case has
no positive zero; omitted zero coefficients only reduce the term count.
A singular matrix would supply a nonzero combination vanishing at all
\(N\) positive points, a contradiction. For negative \(z_j\), each row
differs from the corresponding matrix for \(|z_j|\) by the nonzero sign
\((-1)^{k_i}\), giving the same result. Thus all the coefficients in the
putative identity vanish. Since \(N\) was arbitrary, (12.4) holds.

These hypotheses cover nondegenerate variable-slope parameterizations
using analytic nonpolynomial nonlinearities such as tanh, arctangent,
sine, and logistic sigmoid. The activation name alone does not establish
the hypotheses: for example,
\(\Phi(\theta,z)=A(\theta)\sigma(w_0z+b_0)\) with fixed slope and bias
has forward feature span of dimension at most one.

The proposition concerns exact recovery by fixed linear moments,
uniformly over all finitely supported laws and a continuum of state
values. It does not exclude approximate truncations, moments adapted to
the current depth or state, closure along a single specially reachable
orbit, a finite set of sampled state values, or a nonlinear encoding of
an entire law. If an initialization has \(J\) atoms, deterministic
characteristics preserve those atom masses and give an exact description
by \(J\) parameter-valued depth fields. These fields are still functions
of depth, rather than a fixed finite-dimensional scalar state for the
whole continuous-depth system.

Finite forward feature span is only a necessary first condition for a
universal moment closure. For \(C^1\) moment functions and finitely
supported characteristic laws, differentiate the finite sums. Writing
\(M_j(s,t)=\int\psi_j(\theta)\,\rho_t(s,d\theta)\) gives

\[
\partial_t M_j(s,t)
=-\frac\kappa m\sum_a r_a(t)P_a(s,t)
\int \nabla\psi_j(\theta)\cdot
 \nabla_\theta\Phi(\theta,Z_a(s,t))\,\rho_t(s,d\theta).
\tag{12.6}
\]

For a general initial law the same identity holds on \([0,T]\), at each
depth under consideration, provided \(\psi_j\) is initially integrable
and
\(\int\sup_{t\le T}\|\nabla\psi_j(\Theta_t(s,\vartheta))\|
\,\mu_{\rm in}(s,d\vartheta)<\infty\).
Indeed the bounded velocity then supplies an integrable bound for the
time derivative of \(\psi_j\) along each characteristic, justifying
differentiation under the integral.

For a closure required uniformly over laws, data, and residual
coefficients that can isolate each relevant state value, the readouts
must also recover the sensitivity coefficients
\(\partial_z\Phi(\cdot,z)\), and the moment span must be invariant under
the relevant generators

\[
\psi\longmapsto\nabla\psi(\cdot)\cdot\nabla_\theta\Phi(\cdot,z).
\tag{12.7}
\]

This follows by applying Proposition 12.1 to each integral that must be
recovered. Kernel readouts additionally require the gradient-product
integrals. For one fixed batch and reachable trajectory, only the
combinations that actually occur must be recoverable; if the velocity
vanishes, there is no dynamic moment requirement. The proposition is
therefore an obstruction to universal fixed linear-moment closure, not
a classification of every special orbit.

There are nonlinear special closures outside the global theorem. To make
that boundary explicit, formally take a scalar parameter \(\vartheta\),
a nonzero \(C^1\) function \(\chi:\mathbb R\to\mathbb R\), and

\[
\Phi(\vartheta,z)=\tfrac12\vartheta^2\chi(z),
\qquad M_2(s,t)=\int\vartheta^2\,\rho_t(s,d\vartheta).
\tag{12.8}
\]

On any interval where a classical solution exists with finite second
moment and the following coefficients locally integrable, its readouts
and characteristic velocity are

\[
\partial_s Z_a=\tfrac12 M_2\chi(Z_a),\qquad
-\partial_s P_a=\tfrac12 P_aM_2\chi'(Z_a),\qquad
v_t(s,\vartheta)=-b(s,t)\vartheta,
\tag{12.9}
\]

where
\(b(s,t)=(\kappa/m)\sum_a r_a(t)P_a(s,t)\chi(Z_a(s,t))\).
Its characteristic is
\(\Theta_t(s,\vartheta)=\vartheta\exp(-\int_0^t b(s,u)\,du)\).
Consequently, exactly on such an interval,

\[
\partial_t M_2(s,t)
=-\frac{2\kappa}{m}M_2(s,t)
 \sum_a r_a(t)P_a(s,t)\chi(Z_a(s,t)),
\tag{12.10}
\]

and the kernel is
\(K_{ab}=\int_0^1P_aP_bM_2\chi(Z_a)\chi(Z_b)\,ds\).
This gives a formal single-moment-field closure wherever it is defined.
It satisfies neither A1 nor A2: if \(\chi'\) is nonzero anywhere,
\(\partial_z\Phi=\tfrac12\vartheta^2\chi'\) violates A1; if
\(\chi\) is a nonzero constant, \(\Phi(\vartheta,0)\) violates A1.
Also \(\partial_\vartheta\Phi=\vartheta\chi(z)\) violates A2 on any strip
containing a point with \(\chi(z)\ne0\). The example supplies no global
existence, joint-limit, or fitting claim. It demonstrates only that
nonlinearity alone cannot imply an unconditional need for a full measure
state.

## 13. Scope of the established conclusions

The finite identities are exact, and A1--A2 give global characteristic
existence and restart on \(\mathfrak M\). For constant depth initialization
with a finite first moment, the continuous-depth error is \(O_T(L^{-1})\),
and width errors propagate in the depth-averaged \(\mathcal W_1\) metric
with constants independent of depth. These statements combine into
arbitrary joint width and depth convergence in probability, uniformly on
each fixed compact interval of exact gradient-flow time, including the
displayed hidden states, sensitivities, outputs, losses, and scaled kernels.

Loss is nonincreasing, but eventual fitting and convergence to a minimizer
are not established. No joint gradient-descent limit, nonsmooth ReLU
extension, unbounded-weight polynomial extension, or dense Gaussian-matrix
width/depth limit follows from Sections 1–13. The scalar particle architecture
remains a separate benchmark and cannot substitute for the correlated
dense feature-learning architecture or its theorem.

## 14. Exact dense residual-network identities and response tails

This section concerns a separate, fully dense residual architecture. All
identities and existence statements are at fixed finite width and depth.
The response estimate approximates derivatives along a supplied trajectory;
its matrices and vectors retain their original dimensions. It supplies no
width limit, continuous-depth limit, or autonomous compressed training model.
The scalar particle results of Sections 1–13 are not assumptions here.

### 14.1 Architecture, initialization, and physical clock

Fix integers \(n,L,d,m\ge1\), a finite batch
\((x_a,y_a)_{a=1}^m\in(\mathbb R^d\times\mathbb R)^m\), and a real
residual strength \(\gamma\). Inputs may be correlated, singular, or
coincident. The trainable parameters are \(B\in\mathbb R^{n\times d}\),
\(W_\ell\in\mathbb R^{n\times n}\) for \(0\le\ell<L\), and the stored
readout \(\mathbf a\in\mathbb R^n\). Define

\[
h_a^0=Bx_a,\qquad z_a^\ell=W_\ell h_a^\ell,\qquad
h_a^{\ell+1}=h_a^\ell+\frac\gamma L\phi(z_a^\ell),\qquad
\phi(z)=\tanh z,
\quad f_a=\frac{\mathbf a^T h_a^L}{n}.
\tag{14.1}
\]

Activation is coordinatewise. Here \(L\) counts residual blocks, and the
linear input map has **no** \(1/\sqrt d\) factor. In particular the input
pairing in the formulas below is \(x_a^Tx_b=dG_{ab}\), with the canonical
\(G_{ab}=x_a^Tx_b/d\). The Gaussian initialization for this architecture is
independent entries and blocks with

\[
(W_\ell(0))_{ij}\sim N(0,\sigma_w^2/n),\quad
B_{ij}(0)\sim N(0,1),\quad
\mathbf a_i(0)\sim N(0,A^2),
\tag{14.2}
\]

where \(\sigma_w,A>0\) are fixed. This is an order-one stored readout,
distinct from the small-readout initialization elsewhere in the book.
Every result below holds for every finite initial parameter state, so no
probability estimate or Gaussian theorem is needed to obtain it.

Use residuals \(r_a=f_a-y_a\), full mean loss
\(\mathcal L=m^{-1}\sum_a r_a^2\), and physical gradient flow

\[
\dot W_\ell=-L\nabla_{W_\ell}\mathcal L,\qquad
\dot B=-n\nabla_B\mathcal L,\qquad
\dot{\mathbf a}=-n\nabla_{\mathbf a}\mathcal L.
\tag{14.3}
\]

All matrices remain unconstrained and all blocks train. If a half-sum loss
\(E=\tfrac12\sum_a r_a^2\) is used with the same mobilities, its vector
field must be multiplied by \(2/m\) to obtain (14.3): a half-sum trajectory
\(\theta_E\) yields \(\theta(t)=\theta_E(2t/m)\). The depth factor
\(1/L\) in (14.1) is architectural, not a physical training step.

### 14.2 Adjoint, gradient, kernel, and finite global flow

Define unit-output adjoints and gated adjoints by

\[
p_a^L=\mathbf a,\qquad
D_a^\ell=\operatorname{diag}(\phi'(z_a^\ell)),\qquad
\beta_a^\ell=D_a^\ell p_a^{\ell+1},\qquad
p_a^\ell=\left(I+\frac\gamma L W_\ell^TD_a^\ell\right)p_a^{\ell+1}.
\tag{14.4}
\]

Indeed the Jacobian of one forward block is
\(I+(\gamma/L)D_a^\ell W_\ell\), so the chain rule gives
\(p_a^\ell=n\,\partial f_a/\partial h_a^\ell\). A variation of each
parameter block therefore gives the three output gradients

\[
\nabla_{\mathbf a}f_a=\frac{h_a^L}{n},\qquad
\nabla_Bf_a=\frac{p_a^0x_a^T}{n},\qquad
\nabla_{W_\ell}f_a=\frac\gamma{nL}\beta_a^\ell(h_a^\ell)^T.
\tag{14.5}
\]

Substituting \(\nabla\mathcal L=(2/m)\sum_b r_b\nabla f_b\) yields

\[
\dot{\mathbf a}=-\frac2m\sum_b r_bh_b^L,\qquad
\dot B=-\frac2m\sum_b r_bp_b^0x_b^T,\qquad
\dot W_\ell=-\frac{2\gamma}{mn}\sum_b
r_b\beta_b^\ell(h_b^\ell)^T.
\tag{14.6}
\]

For any one of these vector families write its sample Gram as
\(G^{u,\ell}_{ab}=(u_a^\ell)^Tu_b^\ell/n\). The scaled tangent kernel is

\[
K_{ab}=G^{h,L}_{ab}+(x_a^Tx_b)G^{p,0}_{ab}
+\frac{\gamma^2}{L}\sum_{\ell=0}^{L-1}
G^{h,\ell}_{ab}G^{\beta,\ell}_{ab},\qquad
\dot f=-\frac2m Kr.
\tag{14.7}
\]

To check every factor, the metric kernel is the sum of output-gradient
pairings weighted by the mobilities in (14.3). For the middle blocks the
Frobenius pairing of the rank-one gradients in (14.5), multiplied by \(L\),
is \(\gamma^2G^{h,\ell}_{ab}G^{\beta,\ell}_{ab}/L\); the other two
blocks give the first two terms. It is positive semidefinite directly:
these terms are the Euclidean Gram matrices of
\(h_a^L/\sqrt n\), \(x_a\otimes p_a^0/\sqrt n\), and
\(\gamma h_a^\ell\otimes\beta_a^\ell/(n\sqrt L)\), respectively.
The tensor identity
\((u\otimes v)^T(\widetilde u\otimes\widetilde v)
=(u^T\widetilde u)(v^T\widetilde v)\) follows by summing the two indices.
Thus \(c^TKc\) is a sum of squared norms for every \(c\in\mathbb R^m\).

Consequently

\[
-\dot{\mathcal L}=\frac4{m^2}r^TKr
=\frac{\|\dot{\mathbf a}\|_2^2}{n}
+\frac{\|\dot B\|_F^2}{n}
+\frac1L\sum_\ell\|\dot W_\ell\|_F^2.
\tag{14.8}
\]

These equations have a unique solution for every \(t\ge0\), from every
finite initial state. Here is the continuation argument. At fixed \(n,L\)
the parameter vector field is smooth. On a small closed parameter ball it
has a bound \(M\) and a Lipschitz constant \(C\). On a time interval of
length \(\tau\) with \(\tau M\) smaller than the ball radius and
\(\tau C<1\), the map \(u\mapsto\theta_0+\int_0^t F(u(s))\,ds\)
preserves that closed ball of continuous paths and contracts distances by
\(\tau C\). Its iterations are uniformly Cauchy by a geometric-series
bound and give a unique local solution. Flatten the parameters into
\(\theta=(\mathbf a,B,W_0,\ldots,W_{L-1})\), and let
\(D_{\rm res}\) be the diagonal matrix with entry \(n\) on readout and
input coordinates and \(L\) on every residual-matrix coordinate. Then
\(\|D_{\rm res}^{-1/2}\dot\theta\|_2^2\) is the last expression in
(14.8). For \(s<t\), Cauchy–Schwarz and (14.8) give

\[
\|D_{\rm res}^{-1/2}(\theta(t)-\theta(s))\|_2
\le\sqrt{(t-s)\,[\mathcal L(s)-\mathcal L(t)]}
\le\sqrt{(t-s)\mathcal L(0)}.
\tag{14.9}
\]

If a maximal interval had finite endpoint, (14.9) would give a finite
parameter limit there. The local construction at that limit extends the
solution, a contradiction. This proves finite-dimensional global flow;
loss monotonicity alone supplies no eventual fitting conclusion.

For later bounds put \(E_0=\mathcal L(0)\). On \([0,T]\), (14.9) gives

\[
\begin{split}
\frac{\|\mathbf a(t)\|_2}{\sqrt n}
&\le\frac{\|\mathbf a(0)\|_2}{\sqrt n}+\sqrt{TE_0},\qquad
\frac{\|B(t)\|_F}{\sqrt n}
\le\frac{\|B(0)\|_F}{\sqrt n}+\sqrt{TE_0},\\
\frac1L\sum_\ell\|W_\ell(t)\|_{\rm op}
&\le\frac1L\sum_\ell\|W_\ell(0)\|_{\rm op}+\sqrt{TE_0}.
\end{split}
\tag{14.10}
\]

For the last inequality, bound each operator norm by its Frobenius norm,
apply Cauchy–Schwarz to the average over layers, and then use (14.9).
Since \(|\tanh|\le1\), the forward recurrence also gives

\[
\frac{\|h_a^\ell(t)\|_2}{\sqrt n}
\le\left(\frac{\|B(0)\|_F}{\sqrt n}+\sqrt{TE_0}\right)\|x_a\|_2
+|\gamma|.
\tag{14.11}
\]

This bound retains the linear input map of (14.1).

### 14.3 Exact training-time responses

All derivatives here are in physical training time. Set
\(v_a^\ell=\dot h_a^\ell\), \(w_a^\ell=\dot p_a^\ell\), and
\(\mathsf A_a^\ell=\gamma D_a^\ell W_\ell\). Differentiating the
forward and adjoint recurrences gives

\[
\begin{split}
v_a^0&=-\frac2m\sum_b r_b(x_b^Tx_a)p_b^0,\\
v_a^{\ell+1}&=(I+\mathsf A_a^\ell/L)v_a^\ell+F_a^\ell/L,\qquad
F_a^\ell=-\frac{2\gamma^2}{m}\sum_b
r_bD_a^\ell\beta_b^\ell G^{h,\ell}_{ba},\\
w_a^L&=-\frac2m\sum_b r_bh_b^L,\\
w_a^\ell&=(I+(\mathsf A_a^\ell)^T/L)w_a^{\ell+1}+S_a^\ell/L,
\qquad S_a^\ell=(\dot{\mathsf A}_a^\ell)^Tp_a^{\ell+1}.
\end{split}
\tag{14.12}
\]

The exact backward source is determined without an extra assumption by

\[
\begin{split}
\dot z_a^\ell&=W_\ell v_a^\ell
-\frac{2\gamma}{m}\sum_b r_b\beta_b^\ell G^{h,\ell}_{ba},\\
\dot D_a^\ell&=\operatorname{diag}
  (\phi''(z_a^\ell)\odot\dot z_a^\ell),\\
\dot{\mathsf A}_a^\ell
&=\gamma(\dot D_a^\ell W_\ell+D_a^\ell\dot W_\ell),\qquad
\dot\beta_a^\ell=\dot D_a^\ell p_a^{\ell+1}+D_a^\ell w_a^{\ell+1}.
\end{split}
\tag{14.13}
\]

For example \(\dot W_\ell h_a^\ell\) in (14.6) is the second term of
\(\dot z_a^\ell\); multiplying it by \(\gamma D_a^\ell\) gives
\(F_a^\ell\). The product rule gives every remaining term in
(14.12)–(14.13), including the transpose in \(S\). For any vector family,
\(\dot G^{u,\ell}_{ab}=[(\dot u_a^\ell)^Tu_b^\ell
+(u_a^\ell)^T\dot u_b^\ell]/n\), so hidden Gram derivatives are also
determined. These formulas retain both directions of each same dense matrix.

### 14.4 Chronological products and exact-source tails

Fix a training time and sample for the next algebra, suppress their indices,
and set

\[
P(\ell,b)=(I+\mathsf A^{\ell-1}/L)\cdots(I+\mathsf A^b/L),
\quad P(b,b)=I.
\tag{14.14}
\]

Later-depth matrices stand on the left. Repeated substitution in (14.12)
gives exactly

\[
v^\ell=P(\ell,0)v^0+\frac1L\sum_{b<\ell}P(\ell,b+1)F^b.
\tag{14.15}
\]

Each degree-\(j\) part of \(P(\ell,b)\) is the sum
\(L^{-j}\mathsf A^{i_j}\cdots\mathsf A^{i_1}\) over strictly ordered
indices \(b\le i_1<\cdots<i_j<\ell\). With
\(c_i=\|\mathsf A^i\|_{\rm op}/L\), its norm is at most
\(\sum_{i_1<\cdots<i_j}c_{i_1}\cdots c_{i_j}\le(\sum_i c_i)^j/j!\).
The last inequality follows by expanding the scalar power: each product
with distinct indices occurs \(j!\) times, and all repeated-index terms
are nonnegative. This proof neither commutes matrices nor uses eigenvalues.

The same grading can be generated without explicitly forming products:

\[
\begin{array}{ll}
v^{[0],\ell}=v^0+L^{-1}\sum_{b<\ell}F^b,&
v^{[j],0}=0\quad(j\ge1),\\
v^{[j],\ell+1}=v^{[j],\ell}
+L^{-1}\mathsf A^\ell v^{[j-1],\ell}&(j\ge1),\\[2pt]
w^{[0],\ell}=w^L+L^{-1}\sum_{b\ge\ell}S^b,&
w^{[j],L}=0\quad(j\ge1),\\
w^{[j],\ell}=w^{[j],\ell+1}
+L^{-1}(\mathsf A^\ell)^Tw^{[j-1],\ell+1}&(j\ge1).
\end{array}
\tag{14.16}
\]

Thus \(v^\ell=\sum_{j=0}^L v^{[j],\ell}\) and
\(w^\ell=\sum_{j=0}^L w^{[j],\ell}\). To verify this, sum the recurrences
over grades; no grade above \(L\) survives the strictly ordered indices.
The sums have the same boundary values and inhomogeneous recurrences as
(14.12), whose solution is unique by successive substitution.
The source itself has grade zero: the grade counts only additional
propagator factors, not every matrix or nonlinear factor inside \(F,S\).

For a fixed \(T<\infty\), define the actual trajectory bounds

\[
\begin{split}
\Lambda_T&=\sup_{a,t\le T}\frac1L\sum_\ell
                 \|\mathsf A_a^\ell(t)\|_{\rm op},\\
B_{v,T}&=\sup_{a,t\le T}\left(
  \frac{\|v_a^0\|_2}{\sqrt n}
  +\frac1L\sum_\ell\frac{\|F_a^\ell\|_2}{\sqrt n}\right),\\
B_{w,T}&=\sup_{a,t\le T}\left(
  \frac{\|w_a^L\|_2}{\sqrt n}
  +\frac1L\sum_\ell\frac{\|S_a^\ell\|_2}{\sqrt n}\right).
\end{split}
\tag{14.17}
\]

They are finite at fixed \(n,L,T\) by global existence and continuity.
In particular (14.10) and \(\|D\|_{\rm op}\le1\) give
\(\Lambda_T\le|\gamma|[L^{-1}\sum_\ell\|W_\ell(0)\|_{\rm op}
+\sqrt{TE_0}]\); (14.4) gives
\(\|p_a^\ell\|_2/\sqrt n\le e^{\Lambda_T}
[\|\mathbf a(0)\|_2/\sqrt n+\sqrt{TE_0}]\).
For integer \(K\ge0\) set
\(R_K(\Lambda)=\sum_{j>K}\Lambda^j/j!\). The ordered-product bound in
(14.15), applied separately to the boundary and every forcing insertion,
proves

\[
\begin{split}
\sup_{a,\ell,t\le T}
\frac{\|v_a^\ell-\sum_{j=0}^K v_a^{[j],\ell}\|_2}{\sqrt n}
&\le B_{v,T}R_K(\Lambda_T),\\
\sup_{a,\ell,t\le T}
\frac{\|w_a^\ell-\sum_{j=0}^K w_a^{[j],\ell}\|_2}{\sqrt n}
&\le B_{w,T}R_K(\Lambda_T),\qquad
R_K(\Lambda)\le e^\Lambda\frac{\Lambda^{K+1}}{(K+1)!}.
\end{split}
\tag{14.18}
\]

For the backward equation reverse depth and transpose each generator;
their norms and the counting argument are unchanged. The scalar tail bound
uses \((K+1+j)!\ge(K+1)!j!\) term by term. Both actual errors vanish for
\(K\ge L\). Uniform constants for a family of widths or depths require
uniform bounds in (14.17); no such probabilistic or limiting assertion is
made here. The factorial is a count of depth orderings, not a claim of
analyticity in training time.

### 14.5 Recomputed backward sources

Keep the supplied trajectory, generators, and terminal \(w^L\) fixed, but
replace \(S\) in the grade-\(K\) backward recursion by a source
\(\widetilde S\). Let \(\widetilde w_K\) denote the resulting truncated
sum and put
\(E_{S,T}=\sup_{a,t\le T}L^{-1}\sum_\ell
\|S_a^\ell-\widetilde S_a^\ell\|_2/\sqrt n\).
Linearity of the source-to-response map and the sum of its degree bounds
give

\[
\sup_{a,\ell,t\le T}
\frac{\|w_a^\ell-\widetilde w_{K,a}^\ell\|_2}{\sqrt n}
\le B_{w,T}R_K(\Lambda_T)+e^{\Lambda_T}E_{S,T}.
\tag{14.19}
\]

For clarity, subtract the two truncated recursions with sources
\(S,\widetilde S\); their boundary difference is zero. Each source
difference is propagated by the sum of degrees \(0,\ldots,K\) of the
appropriate ordered product, of norm at most
\(\sum_{j=0}^K\Lambda_T^j/j!\le e^{\Lambda_T}\). Summing its
\(1/L\)-weighted norms proves the second term of (14.19); (14.18)
supplies the first.

For the particular replacement obtained by using
\(v_K=\sum_{j=0}^K v^{[j]}\) in (14.13), while keeping
\(W,\dot W,h,p,z,D,r\) exact, the source difference is exactly

\[
S_a^\ell-\widetilde S_a^\ell
=\gamma W_\ell^T\left[
\phi''(z_a^\ell)\odot p_a^{\ell+1}
\odot W_\ell(v_a^\ell-v_{K,a}^\ell)\right].
\tag{14.20}
\]

Consequently \(E_{S,T}\le C_T B_{v,T}R_K(\Lambda_T)\), where

\[
C_T=\sup_{a,t\le T}\frac{|\gamma|}{L}\sum_\ell
\|W_\ell\|_{\rm op}^2
\|\phi''(z_a^\ell)\odot p_a^{\ell+1}\|_\infty.
\tag{14.21}
\]

Indeed multiply the two operator-norm bounds and the coordinate multiplier
bound in (14.20), then use (14.18). This finite-state constant is finite;
the normalized adjoint bound above does not give a width-independent
coordinate maximum. If the approximate dynamics also change the trajectory
or \(\dot W\), (14.20) is no longer its entire source error. Establishing
an autonomous response approximation would require control of those changes
and of their full nonlinear feedback. The identities and supplied-trajectory
tail estimates do not provide that theorem, fitting, or nonlazy limit claims.

## 15. Global training flow for a coherent dense residual kernel

This section treats a separate residual architecture: its dense, untied
trunk has the coherent normalization \(W/n\), and its input features and
readout are fixed and bounded. The continuum state is an actual kernel on
a neuron label space. It is not the Gaussian \(W/\sqrt n\) construction,
and it is not the scalar particle model. We prove existence and uniqueness
of the kernel training flow, including its exact gradient and energy
identity. No width or depth limit is assumed in this existence theorem.

### 15.1 Finite calculus and the metric being continued

Here \(L\) counts residual blocks, \(n\) is their common width, and
\(m\) is a fixed positive finite number of samples. Use the activation
and loss regularity specified in Section 15.3. Fix \(\alpha>0\). For fixed
input vectors \(x_a^{[n]}\in\mathbb R^n\) and a fixed readout
\(c^{[n]}\in\mathbb R^n\), set

\[
h_a^{(0)}=x_a^{[n]},\qquad
z_a^{(\ell)}=\frac{W_\ell h_a^{(\ell-1)}}n,\qquad
h_a^{(\ell)}=h_a^{(\ell-1)}+
\frac{\alpha}{L}\phi(z_a^{(\ell)}),\qquad
f_{n,a}=\frac{(c^{[n]})^T h_a^{(L)}}n.
\tag{15.1}
\]

All \(Ln^2\) trunk entries are independent parameter coordinates; no
diagonality, low rank, symmetry, or tying of different blocks is imposed.
Only these trunk matrices are trained. Let
\(\mathcal E_n=\mathcal R(f_{n,1},\ldots,f_{n,m})\), and write
\(q_a=\partial_a\mathcal R(f_n)\). For the library's mean full squared
loss, \(q_a=2r_{n,a}/m\), where \(r_{n,a}=f_{n,a}-y_a\). The mean half
squared loss instead has \(q_a=r_{n,a}/m\); at the same mobility it runs
at half the physical speed.

Use the residual-free adjoint

\[
p_a^{(L)}=c^{[n]},\qquad
b_a^{(\ell)}=p_a^{(\ell)}\odot\phi'(z_a^{(\ell)}),\qquad
p_a^{(\ell-1)}=p_a^{(\ell)}+
\frac{\alpha}{Ln}W_\ell^T b_a^{(\ell)}.
\tag{15.2}
\]

Indeed \(p_a^{(\ell)}=n\,\partial f_{n,a}/\partial h_a^{(\ell)}\),
so the transpose in (15.2) is that of the same forward matrix. Varying
one matrix gives

\[
\nabla_{W_\ell}f_{n,a}
=\frac{\alpha}{Ln^2}b_a^{(\ell)}(h_a^{(\ell-1)})^T,
\qquad
\nabla_{W_\ell}\mathcal E_n
=\frac{\alpha}{Ln^2}\sum_{a=1}^m
q_a b_a^{(\ell)}(h_a^{(\ell-1)})^T.
\tag{15.3}
\]

Thus mobility \(Ln^2\) for every raw matrix gives

\[
\dot W_\ell=-\alpha\sum_{a=1}^m
q_a b_a^{(\ell)}(h_a^{(\ell-1)})^T,
\qquad
\frac{d\mathcal E_n}{dt}
=-\frac1{Ln^2}\sum_{\ell=1}^L\|\dot W_\ell\|_F^2.
\tag{15.4}
\]

These are exact finite identities. In particular, full-batch dissipation
uses the squared norm of the sum in (15.4). If
\(\mathcal R\ge E_*\), integration and Cauchy--Schwarz give

\[
\left(\frac1{Ln^2}\sum_\ell
\|W_\ell(t)-W_\ell(0)\|_F^2\right)^{1/2}
\le\sqrt{t\,[\mathcal E_n(0)-E_*]}.
\tag{15.5}
\]

At fixed \(n,L\), the right side bounds every parameter displacement
on a finite time interval. The locally Lipschitz finite vector field
therefore extends globally. This observation makes no assertion uniform
in \(n,L\).

To identify the continuum metric, embed a matrix as a kernel constant on
the \(n^2\) equal neuron cells, and embed the blocks on the \(L\) equal
depth cells. Its squared \(L^2(ds\,du\,dv)\) norm is exactly
\((Ln^2)^{-1}\sum_\ell\|W_\ell\|_F^2\). The corresponding integral
operator acts as \(W_\ell/n\), and the integral readout as
\((c^{[n]})^Th/n\). This identifies the normalization and metric; it
does not prove that discretized training converges.

### 15.2 A strong kernel carrier

Put \(U=(0,1)\), with Lebesgue measure. For a measurable real kernel
\(k\) on \(U^2\), define its row and column bounds by

\[
\rho(k)=\operatorname*{ess\,sup}_{u\in U}
\left(\int_U|k(u,v)|^2\,dv\right)^{1/2},\qquad
\chi(k)=\operatorname*{ess\,sup}_{v\in U}
\left(\int_U|k(u,v)|^2\,du\right)^{1/2}.
\tag{15.6}
\]

Let \(\mathcal K\) be the space of such kernels, modulo almost-everywhere
equality, for which both bounds are finite, with norm

\[
\|k\|_{\mathcal K}=
\bigl(\rho(k)^2+\chi(k)^2\bigr)^{1/2}.
\]

This is a Banach space. To see completeness, a Cauchy sequence in this
norm converges in each of the Banach mixed spaces
\(L^\infty_u(L^2_v)\) and \(L^\infty_v(L^2_u)\). Both limits have the
same \(L^2(U^2)\) representative, since both embeddings into that space
are continuous. Hence they define one element of \(\mathcal K\), and
convergence holds in both components of its norm.

The depth carrier and the energy space are

\[
\mathbb K=L^2\bigl((0,1)_s;\mathcal K\bigr),\qquad
\mathbb H=L^2\bigl((0,1)_s\times U^2\bigr),\qquad
\|w\|_{\mathbb K}^2=
\int_0^1[\rho(w(s))^2+\chi(w(s))^2]\,ds.
\tag{15.7}
\]

The first space is the **Bochner** \(L^2\) space: its elements are
strongly measurable \(\mathcal K\)-valued depth profiles, represented
by almost-everywhere limits of simple profiles, with the displayed finite
norm. Joint scalar measurability of \(w(s,u,v)\) and the displayed norm
alone are not substituted for this requirement. Bochner \(L^2\) of a
Banach space is complete: for example, a subsequence of a Cauchy sequence
whose successive \(L^2\) differences have summable norms has an
almost-everywhere absolutely convergent series of differences, yielding
a strongly measurable limit and convergence in \(L^2\). There is a
continuous embedding \(\mathbb K\hookrightarrow\mathbb H\).

For \(g\in L^2(U)\), define

\[
(T_kg)(u)=\int_Uk(u,v)g(v)\,dv,\qquad
(T_k^*g)(v)=\int_Uk(u,v)g(u)\,du.
\]

Cauchy--Schwarz and Fubini give

\[
\|T_kg\|_\infty\le\rho(k)\|g\|_2,\qquad
\|T_k^*g\|_\infty\le\chi(k)\|g\|_2,\qquad
\|T_k\|_{2\to2}\le\|k\|_{L^2(U^2)}
\le\min\{\rho(k),\chi(k)\}.
\tag{15.8}
\]

Here \(T_k^*\) is the actual Hilbert-space adjoint of \(T_k\).
For bounded functions \(b,x\), the kernel
\((b\otimes x)(u,v)=b(u)x(v)\) satisfies

\[
\rho(b\otimes x)=\|b\|_\infty\|x\|_2,
\qquad
\chi(b\otimes x)=\|x\|_\infty\|b\|_2.
\tag{15.9}
\]

The actions \(\mathcal K\times L^\infty\to L^\infty\) in (15.8)
and the outer product \(L^\infty\times L^\infty\to\mathcal K\) in
(15.9) are continuous bilinear maps. They therefore preserve strong
measurability when applied to strongly measurable arguments: approximate
the arguments by simple functions and use continuity. These facts will
ensure that all depth and training integrals below are Bochner integrals.

### 15.3 The global theorem

Assume throughout this section that

* \(1\le m<\infty\), \(\alpha>0\), and the input profiles
  \(X_a^0\in L^\infty(U)\) and readout \(c\in L^\infty(U)\) are
  fixed and untrained;
* \(\phi\in C_b^2(\mathbb R)\): the function and its first two
  continuous derivatives are bounded; write
  \(M_j=\|\phi^{(j)}\|_\infty\), \(j=0,1,2\);
* \(\mathcal R\in C^2(\mathbb R^m)\) and
  \(\mathcal R\ge E_*\) for some finite real \(E_*\);
* \(w_0\in\mathbb K\).

The profiles \(X_a^0\) are the inputs of this kernel model. A fixed
bounded feature map applied to finite-dimensional data is one way to
specify them. No orthogonality, normalization, or nonsingularity of the
sample Gram matrix is assumed, and there is no population-of-data limit.
In particular, arbitrary fixed labels are allowed in squared loss.

At each training state \(w\), solve the depth equations

\[
\begin{aligned}
\partial_sX_a(s)&=\alpha\phi(Z_a(s)),&
Z_a(s)&=T_{w(s)}X_a(s),&X_a(0)&=X_a^0,\\
-\partial_sP_a(s)&=\alpha T_{w(s)}^*B_a(s),&
B_a(s)&=P_a(s)\phi'(Z_a(s)),&P_a(1)&=c.
\end{aligned}
\tag{15.10}
\]

Products and activations of functions on \(U\) are pointwise. Define

\[
f_a(w)=\int_Uc(u)X_a(1,u)\,du,\quad
q_a(w)=\partial_a\mathcal R(f(w)),\quad
\mathcal E(w)=\mathcal R(f(w)),
\]

\[
\mathcal G(w)(s)=\alpha\sum_{a=1}^m
q_a(w)B_a(s)\otimes X_a(s).
\tag{15.11}
\]

The adjoint \(P_a\) is residual-free: all loss factors occur in
\(q_a\). The training equation is

\[
\partial_tw(t)=-\mathcal G(w(t)),\qquad w(0)=w_0.
\tag{15.12}
\]

**Theorem 15.1 (global strong kernel flow).** Under the stated assumptions,
(15.10)--(15.12) have a unique solution
\(w\in C^1([0,\infty);\mathbb K)\). For each \(w\in\mathbb K\),
the forward and adjoint depth solutions in (15.10) are unique Bochner
absolutely continuous \(L^\infty(U)\)-valued curves, with derivatives
in \(L^1((0,1);L^\infty(U))\). The map
\(\mathcal G:\mathbb K\to\mathbb K\) is Lipschitz on each bounded
ball. The loss is Fréchet differentiable on \(\mathbb K\), with

\[
D\mathcal E(w)[v]=\langle\mathcal G(w),v\rangle_{\mathbb H}
\quad(v\in\mathbb K),\qquad
\frac{d}{dt}\mathcal E(w(t))
=-\|\partial_tw(t)\|_{\mathbb H}^2.
\tag{15.13}
\]

Consequently, for every finite \(T\),

\[
\int_0^T\|\partial_tw(t)\|_{\mathbb H}^2\,dt
=\mathcal E(w_0)-\mathcal E(w(T))
\le\mathcal E(w_0)-E_*,
\qquad
\|w(t)-w_0\|_{\mathbb H}
\le\sqrt{t\,[\mathcal E(w_0)-E_*]}.
\tag{15.14}
\]

The solution can restart uniquely from every point of \(\mathbb K\),
with the fixed data, readout, activation, and loss retained. Thus its
autonomous solution maps form a semigroup on this carrier. The theorem
does not assert well-posedness for arbitrary initial kernels in
\(\mathbb H\) alone.

**Proof: depth existence and estimates.** Write
\(C_X=\max_a\|X_a^0\|_\infty+\alpha M_0\). For any fixed
\(w\in\mathbb K\), the forward integral equation is a contraction
on a depth interval on which
\(\alpha M_1\int\rho(w(s))\,ds<1\), since \(U\) has measure one
and (15.8) applies. The integral of \(\rho(w)\) is finite, so finitely
many such intervals cover \([0,1]\). Boundedness of \(\phi\) gives,
at every depth,

\[
\|X_a(s)\|_\infty\le C_X.
\tag{15.15}
\]

The resulting curve is continuous into \(L^\infty\); its integrand is
strongly measurable by (15.8) and the Lipschitz Nemytskii map for
\(\phi\), and is bounded by \(\alpha M_0\). It is therefore a
Bochner absolutely continuous solution. The same local contraction
argument backwards in depth constructs \(P_a\), now with contraction
constant \(\alpha M_1\int\chi(w(s))\,ds\). It yields

\[
\sup_s\|P_a(s)\|_\infty
\le\|c\|_\infty
\exp\!\left(\alpha M_1\int_0^1\chi(w(s))\,ds\right).
\tag{15.16}
\]

Uniqueness follows from the same integral inequalities and Gronwall.
All arguments remain in \(L^\infty\); the adjoint integrand has an
integrable norm, so it too gives the asserted Bochner derivative.
In contrast to the bounded states and adjoints, the local field has only
the depth bound

\[
\|Z_a\|_{L^2_sL^\infty_u}
\le C_X\|\rho(w)\|_{L^2_s}.
\tag{15.17}
\]

An essential supremum of \(Z_a\) over depth is not required.

**Proof: local Lipschitzness in the strong carrier.** Fix \(A<\infty\)
and two kernels \(w,\widetilde w\) with carrier norms at most \(A\).
In this paragraph constants denoted \(C_A\) depend only on \(A\) and
the fixed problem data. Write \(d=w-\widetilde w\), and use a tilde
for the depth fields of \(\widetilde w\). Subtracting the forward
integral equations, applying (15.8), and then Gronwall gives

\[
\sup_s\|X_a(s)-\widetilde X_a(s)\|_\infty
\le C_A\|d\|_{\mathbb K}.
\tag{15.18}
\]

For completeness, the two terms in the integral inequality are
\(\alpha M_1\rho(w(s))\|X_a-\widetilde X_a\|_\infty\) and
\(\alpha M_1C_X\rho(d(s))\). Their depth integrals are controlled
by the \(L^2\) row bounds in (15.7). Hence

\[
\|Z_a-\widetilde Z_a\|_{L^2_sL^\infty_u}
\le C_X\|\rho(d)\|_{L^2_s}
+\|\rho(w)\|_{L^2_s}
\sup_s\|X_a-\widetilde X_a\|_\infty
\le C_A\|d\|_{\mathbb K}.
\tag{15.19}
\]

To compare adjoints, expand the difference of their integrands as

\[
\begin{split}
T_w^*B_a-T_{\widetilde w}^*\widetilde B_a
={}&T_w^*\bigl(\phi'(Z_a)(P_a-\widetilde P_a)\bigr)\\
&+T_w^*\bigl(\widetilde P_a
 [\phi'(Z_a)-\phi'(\widetilde Z_a)]\bigr)
+T_d^*\widetilde B_a.
\end{split}
\tag{15.20}
\]

The first term has \(L^\infty\) norm at most
\(M_1\chi(w)\|P_a-\widetilde P_a\|_\infty\). By (15.16), the
second term is bounded by
\(C_A M_2\chi(w)\|Z_a-\widetilde Z_a\|_\infty\), whose depth
integral is controlled by Cauchy--Schwarz and (15.19). The third term
is bounded by \(C_A M_1\chi(d)\). Backward Gronwall therefore gives

\[
\sup_s\|P_a-\widetilde P_a\|_\infty
+\|B_a-\widetilde B_a\|_{L^2_sL^\infty_u}
\le C_A\|d\|_{\mathbb K}.
\tag{15.21}
\]

For the second term in (15.21), use
\(B_a-\widetilde B_a
=\phi'(Z_a)(P_a-\widetilde P_a)
+\widetilde P_a[\phi'(Z_a)-\phi'(\widetilde Z_a)]\).
This estimate uses two square-integrable depth factors in (15.20),
not a bound on the maximum local field over depth.

All outputs lie in the fixed compact cube
\([-\|c\|_1C_X,\|c\|_1C_X]^m\). The gradient and Hessian of
\(\mathcal R\) are bounded there. Equation (15.18) thus also bounds
\(|q(w)-q(\widetilde w)|\) by \(C_A\|d\|_{\mathbb K}\).
For each sample, the outer-product difference in (15.11) expands as
\[
q_aB_a\otimes X_a-\widetilde q_a\widetilde B_a\otimes\widetilde X_a
=(q_a-\widetilde q_a)B_a\otimes X_a
+\widetilde q_a(B_a-\widetilde B_a)\otimes X_a
+\widetilde q_a\widetilde B_a\otimes(X_a-\widetilde X_a).
\]
By (15.9), \(\|b\otimes x\|_{\mathcal K}
\le\sqrt2\|b\|_\infty\|x\|_\infty\). Applying this inequality
pointwise in depth and then taking its \(L^2\) norm, using (15.15),
(15.16), (15.18), and (15.21), proves

\[
\|\mathcal G(w)\|_{\mathbb K}\le C_A,\qquad
\|\mathcal G(w)-\mathcal G(\widetilde w)\|_{\mathbb K}
\le C_A\|w-\widetilde w\|_{\mathbb K}.
\tag{15.22}
\]

Strong measurability of \(\mathcal G(w)(s)\) follows from the
continuous bilinear maps following (15.9) and from strong measurability
of \(X_a,P_a,Z_a\) as \(L^\infty\)-valued profiles. In particular
(15.22) concerns the Bochner carrier itself.

The training integral map
\(v(t)\mapsto w_0-\int_0^t\mathcal G(v(\tau))\,d\tau\)
is a contraction on a sufficiently short interval in a closed ball of
\(C([0,\varepsilon];\mathbb K)\): choose \(\varepsilon\) so that
the first bound in (15.22) keeps the image in the ball and the second
makes the contraction constant less than one. This constructs a unique
local \(C^1\) solution and, by successive restarts, a unique maximal
solution on \([0,T_*)\).

**Proof: differentiation and the exact gradient.** Fix \(w\in\mathbb K\)
and a variation \(v\in\mathbb K\). The proposed derivative of the
forward field is the unique solution of

\[
\partial_sY_a=\alpha\phi'(Z_a)
  (T_wY_a+T_vX_a),\qquad Y_a(0)=0.
\tag{15.23}
\]

The forward contraction argument, or its linear integral inequality,
shows that \(v\mapsto Y_a\) is bounded and linear from \(\mathbb K\)
to \(C([0,1];L^\infty(U))\). We verify that it is the Fréchet
derivative, since only a depth \(L^2\) bound for the local field is
available. Let \(e_a=X_a(w+v)-X_a(w)\) and
\(\zeta_a=Z_a(w+v)-Z_a(w)\). On a fixed ball, (15.18)--(15.19) give
\(\|e_a\|_{C_sL^\infty_u}=O(\|v\|_{\mathbb K})\) and
\(\|\zeta_a\|_{L^2_sL^\infty_u}=O(\|v\|_{\mathbb K})\).
Taylor's theorem gives the pointwise remainder

\[
|\phi(Z_a+\zeta_a)-\phi(Z_a)-\phi'(Z_a)\zeta_a|
\le\frac{M_2}{2}|\zeta_a|^2.
\]

Since
\(\zeta_a=T_we_a+T_vX_a+T_ve_a\), subtraction of (15.23)
shows that \(e_a-Y_a\) solves the same linear homogeneous integral
equation as \(Y_a\), with forcing equal to
\(\alpha\phi'(Z_a)T_ve_a\) plus the Taylor remainder. The integral
of the forcing norm is at most

\[
\alpha M_1\|\rho(v)\|_{L^1_s}\|e_a\|_{C_sL^\infty_u}
+\frac{\alpha M_2}{2}
\|\zeta_a\|_{L^2_sL^\infty_u}^2
=O(\|v\|_{\mathbb K}^2).
\]

Gronwall then proves
\(\|e_a-Y_a\|_{C_sL^\infty_u}=O(\|v\|_{\mathbb K}^2)\),
which establishes the asserted Fréchet derivative.

Both \(P_a\) and \(Y_a\) are absolutely continuous into \(L^2(U)\).
The product rule for their pairing is valid: their derivatives have
integrable \(L^2\) norms, and the curves have bounded \(L^2\) norms.
Using the adjoint of the same operator in (15.10), the homogeneous
terms cancel and leave

\[
\frac{d}{ds}\langle P_a,Y_a\rangle_{L^2(U)}
=\alpha\langle B_a,T_vX_a\rangle_{L^2(U)}.
\]

Integrating, using \(Y_a(0)=0\) and \(P_a(1)=c\), and applying
Fubini gives

\[
Df_a(w)[v]
=\alpha\int_0^1\langle B_a(s)\otimes X_a(s),v(s)\rangle_{L^2(U^2)}\,ds.
\tag{15.24}
\]

All terms are integrable by the preceding bounds. The finite-dimensional
chain rule for \(\mathcal R\) proves the first identity in (15.13).
The representer \(\mathcal G(w)\) belongs to \(\mathbb K\subset\mathbb H\),
and (15.22) makes the derivative continuous. Thus it is precisely the
gradient in the \(\mathbb H\) pairing, for the functional defined on
the strong carrier. This statement does not extend the functional or its
Fréchet differentiability to an open set of bare \(\mathbb H\).
Along the local \(C^1\) training curve, the chain rule and (15.12)
now yield the energy identity in (15.13). Its integral and
Cauchy--Schwarz give (15.14) on every interval of local existence.

**Proof: global continuation in the strong carrier.** Fix a finite
\(T>0\), and consider \(0\le t<\min\{T,T_*\}\). All constants in
this paragraph are independent of \(t\) in that interval. Define

\[
D=\mathcal E(w_0)-E_*\ge0,\qquad
H_T=\|w_0\|_{\mathbb H}+\sqrt{TD},\qquad
Q=\max_{z\in[-\|c\|_1C_X,\|c\|_1C_X]^m}\max_a|\partial_a\mathcal R(z)|.
\tag{15.25}
\]

Equations (15.14)--(15.15) give
\(\|w(t)\|_{\mathbb H}\le H_T\) and \(|q_a(t)|\le Q\).
Using the \(L^2\)-operator bound in (15.8) in the backward equation,
and then Gronwall and Cauchy--Schwarz in depth, gives

\[
\sup_s\|P_a(s,t)\|_2
\le\|c\|_2
\exp\!\left(\alpha M_1\int_0^1\|w(s,t)\|_{L^2(U^2)}\,ds\right)
\le\|c\|_2e^{\alpha M_1H_T}=:P_{2,T}.
\tag{15.26}
\]

Set
\(C_w(t)=\|\chi(w(\cdot,t))\|_{L^2_s}\) and
\(R_w(t)=\|\rho(w(\cdot,t))\|_{L^2_s}\). The column estimate
in (15.9) now closes without an \(L^\infty\) adjoint bound:

\[
\chi(\partial_tw(s,t))
\le\alpha\sum_a|q_a(t)|\|X_a(s,t)\|_\infty\|B_a(s,t)\|_2
\le\alpha mQ C_XM_1P_{2,T}=:A_T.
\]

Taking the depth \(L^2\) norm and integrating in training time, using
the triangle inequality for the column seminorm, yields

\[
C_w(t)\le C_w(0)+A_Tt.
\tag{15.27}
\]

Next integrate the backward equation directly in \(L^\infty\),
using its column operator bound and (15.26):

\[
\sup_s\|P_a(s,t)\|_\infty
\le\|c\|_\infty+
\alpha M_1P_{2,T}\int_0^1\chi(w(s,t))\,ds
\le\|c\|_\infty+
\alpha M_1P_{2,T}[C_w(0)+A_Tt].
\tag{15.28}
\]

Finally (15.9) gives

\[
\rho(\partial_tw(s,t))
\le\alpha mQM_1C_X
\bigl(\|c\|_\infty+\alpha M_1P_{2,T}[C_w(0)+A_Tt]\bigr)
=:B_{0,T}+B_{1,T}t.
\]

Consequently,

\[
R_w(t)\le R_w(0)+B_{0,T}t+\tfrac12B_{1,T}t^2.
\tag{15.29}
\]

Equations (15.27) and (15.29) bound the full \(\mathbb K\) norm on
every finite interval of existence. This separate argument is necessary:
the kernels \(k_N(u,v)=\sqrt N\,\mathbf1_{\{u<1/N\}}\) have
\(\|k_N\|_2=1\) but \(\rho(k_N)=\sqrt N\), so an energy bound
alone would not control the carrier.

If \(T_*<\infty\), take \(T=T_*\) in these bounds. The first estimate
in (15.22) then bounds \(\|\partial_tw\|_{\mathbb K}\) uniformly
on \([0,T_*)\). Hence \(w(t)\) is Cauchy in the Banach carrier as
\(t\uparrow T_*\), and has a limit there. Local existence from that
limit extends the solution past \(T_*\), a contradiction. Thus
\(T_*=\infty\). Local uniqueness at each restart proves global
uniqueness and the semigroup assertion. This completes the proof.

### 15.4 What the theorem supplies

The theorem applies, in particular, to \(\phi=\tanh\), to arbitrary
fixed bounded input profiles and readout, and to every initial coherent
kernel in the Bochner carrier (15.7). It supplies a global autonomous
training flow in physical time, an exact loss gradient, and the exact
energy law. The state remains an infinite-dimensional depth-indexed
kernel; no finite scalar closure or Gaussian initialization is imposed.

The bounded activation is material to the uniform forward bound, compact
output set, and ordered continuation proof. The result does not
automatically extend to ReLU, to trained endpoints, or to other metrics
and clocks. Nor does the energy identity by itself imply fitting,
nonzero feature motion, a training-time limit, or a finite-width
approximation theorem.

In particular, adding microscopic centered Gaussian matrices to a finite
coherent initialization raises a separate discrete-to-continuum problem.
The present proof asserts no noisy joint width/depth convergence rate,
no raw-kernel convergence for such noise, and no maximum-over-depth
control of local preactivations. It also makes no assertion about the
surviving Gaussian bulk at the different \(W/\sqrt n\) normalization.
