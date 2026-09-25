# Evolving response memory: what is established and what remains open

Theory-only assessment, 2026-09-22. This document addresses the user's new
response-history formulation. It does not reopen the discarded trainable
dictionary experiment or use that experiment as scientific input. The user's
zero-radius assertion is accepted; its book theorem was not searched for.

## 1. The distinction that changes the question

A finite derivative chain produces a polynomial in time only under a particular
terminal law, such as setting its highest derivative to zero. Retaining current
position and velocity with feedback gives, for example,

\[
\dot z=v,\qquad \dot v=-\lambda v,\qquad
z(t)=z(0)+\frac{v(0)}{\lambda}(1-e^{-\lambda t}),\quad\lambda>0.
\]

There is an exponential plateau with two scalar states. Even a polynomial vector
field need not produce a polynomial trajectory: the scalar equation
\(\dot v=-v^2\), with \(v(0)>0\), gives
\(v(t)=v(0)/(1+tv(0))\). These formulas follow by differentiating the displayed
solutions and checking initial values. No neural approximation is asserted.

The canonical finite neural model already has an autonomous first-order ODE.
The problem is to evaluate an accurate smaller ODE without the dense operator.
It is not to find a type of differential equation capable of saturation.
Plateaus alone do not demonstrate that a small closure exists.

## 2. Zero Taylor radius need not mean complex microscopic state

Here is a self-contained Gaussian example, independent of any neural theorem.
Let \(G\sim N(0,1)\) be a fixed mark of each population member and evolve

\[
\dot q_G=-G^4q_G,\quad q_G(0)=1,\qquad
Q(t)=\mathbb E[q_G(t)]=\mathbb E[e^{-tG^4}],\quad t\ge0.
\]

Every member follows one scalar linear ODE and has an entire time trajectory.
All right derivatives of the population mean exist. For each fixed integer
\(k\), the differentiated integrand is bounded on \(t\ge0\) by \(|G|^{4k}\),
which is integrable. Dominated convergence therefore gives

\[
Q^{(k)}(0+)=(-1)^k\mathbb E[G^{4k}]=(-1)^k(4k-1)!!.
\]

The Gaussian moment formula follows recursively by integration by parts:
\(\mathbb E[G^{2j}]=(2j-1)\mathbb E[G^{2j-2}]\), starting from one.
For the absolute Taylor coefficient \(a_k=(4k-1)!!/k!\),

\[
\frac{a_{k+1}}{a_k}=\frac{(4k+3)(4k+1)}{k+1}\longrightarrow\infty.
\]

Thus the Taylor series has radius zero, even though the state per population
member is one evolving scalar plus one fixed Gaussian mark. Also
\(Q(t)\to0\) by dominated convergence, since \(e^{-tG^4}\to0\) almost surely
and lies between zero and one. The example does not claim that the neural
observable has this mechanism. It shows that the given nonanalyticity premise
does not imply a singular per-neuron ODE or rule out a small per-neuron state.

A population of low-dimensional states is not a finite total-dimensional
deterministic ODE for its mean. An exact finite analytic ODE with analytic
readout would have a locally analytic output; retaining a population avoids
that inference because averaging need not preserve analyticity without uniform
integrable control in a complex neighborhood. Here each microscopic trajectory
is entire, but for every negative real time its population expectation diverges.
Numerically resolving the population remains a separate cost.

## 3. The exact moving response hierarchy

Canonical conventions are taken only from the established
`docs/global_nonlinear.md`, C.4.7.8, part 1, equations (H1)–(H2). For finite
width \(n\), normalized input \(x/\sqrt d\), and training law
\(\sum_a\rho_a\delta_{(x_a,y_a)}\), write

\[
H^{(1)}_a=\tanh(W^{(1)}x_a/\sqrt d),\quad
Z^{(2)}_a=W^{(2)}H^{(1)}_a,\quad H^{(2)}_a=\tanh Z^{(2)}_a,
\]
\[
f_a=\frac1n(W^{(3)})^TH^{(2)}_a,\quad r_a=f_a-y_a,\quad
\Delta^{(2)}_a=W^{(3)}\odot[1-(H^{(2)}_a)^2],\quad
Q_a=(W^{(2)})^T\Delta^{(2)}_a.
\]

Products and squares within a neuron population are componentwise. With
unhalved probability MSE and physical mobilities \((n,1,n)\),

\[
\dot W^{(2)}=-2\sum_b\rho_b r_b\Delta^{(2)}_b\otimes H^{(1)}_b,
\qquad (a\otimes b)v=a\langle b,v\rangle_1,
\quad\langle b,v\rangle_1=b^Tv/n.
\]

The second population uses the same normalization:
\(\langle a,u\rangle_2=a^Tu/n\).

The exact product rules give

\[
\dot Z^{(2)}_a=-2\sum_b\rho_b r_b\Delta^{(2)}_b
 \langle H^{(1)}_b,H^{(1)}_a\rangle_1
 +W^{(2)}\dot H^{(1)}_a,
\]
\[
\dot Q_a=-2\sum_b\rho_b r_b H^{(1)}_b
 \langle\Delta^{(2)}_b,\Delta^{(2)}_a\rangle_2
 +(W^{(2)})^T\dot\Delta^{(2)}_a.
\]

The first terms use present responses and population contractions. The last
terms require new operator actions on moving probes. Keeping those actions
as current states and differentiating produces further actions. For example,
where the derivatives exist, the exact ladder includes

\[
A_{k,a}=W^{(2)}\partial_t^kH^{(1)}_a,\qquad
B_{k,a}=(W^{(2)})^T\partial_t^k\Delta^{(2)}_a,
\]
\[
\dot A_{k,a}=\dot W^{(2)}\partial_t^kH^{(1)}_a+A_{k+1,a},\qquad
\dot B_{k,a}=\dot W^{(2)T}\partial_t^k\Delta^{(2)}_a+B_{k+1,a}.
\]

This describes moving responses, not a Taylor reconstruction from their initial
values. The finite-width identities are exact. Population versions require the
corresponding products and differentiations to be justified; no unrestricted
all-order population differentiability claim is made here. The companion
`NEURAL_RESPONSE_ROUTE.md` expands the first missing responses, gives a
finite-state nonclosure example, and verifies the exact positive semidefinite
output kernel and loss dissipation.

A candidate finite terminal law must preserve the coupling of the same matrix
and its actual adjoint. It must also preserve the fact that all exact motion
stops when all residuals vanish. Independently assigning fresh Gaussian forward
and reverse actions, or damping all learned responses to zero, would violate
the target. The initialization law matters: canonical finite hidden Gaussian
weights have variances \((1,1/n,1/n^2)\), while the limiting readout is zero;
zero limiting readout does not justify changing finite initialization.

## 4. A precise form of history compression

An elementary linear example exposes the mechanism without postulating a
neural closure. Let resolved \(z\) and hidden \(y\) obey

\[
\dot z=Az+By,\qquad\dot y=Cz+Dy.
\]

Variation of constants gives exactly

\[
\dot z(t)=Az(t)+Be^{Dt}y(0)
 +\int_0^t Be^{D(t-s)}Cz(s)\,ds.
\]

The history kernel and the effect of hidden initialization must both be kept.
An auxiliary state \(m\in\mathbb R^P\) with

\[
\dot z=Az+Rm,\qquad\dot m=Tm+Sz
\]

reproduces this equation exactly for the specified initial states if

\[
Re^{Tt}S=Be^{Dt}C,\qquad Re^{Tt}m(0)=Be^{Dt}y(0).
\]

It approximates the original system only insofar as these quantities are
approximated and the resulting feedback is controlled. The second condition
cannot be omitted even when the driven kernel has a small representation.
The companion `MEMORY_STATE_ROUTE.md` proves the minimum exact dimension for
a specified initial subspace, conditional finite-horizon approximation, and
the additional assumptions needed for all-time error and plateau accuracy.

A scalar building block is particularly transparent:

\[
\dot m_j=-\lambda_jm_j+s(t),\qquad
m_j(t)=e^{-\lambda_jt}m_j(0)
 +\int_0^t e^{-\lambda_j(t-u)}s(u)\,du.
\]

Here \(s\) is a current source and \(m_j\) an evolving summary of its past.
If the memory contribution is \(\sum_j a_jm_j\), its driven kernel is
\(K_P(t)=\sum_j a_je^{-\lambda_jt}\) and, for sufficiently large
\(\operatorname{Re}\zeta\), its Laplace transform is

\[
\widehat K_P(\zeta)=\sum_{j=1}^P\frac{a_j}{\zeta+\lambda_j}.
\]

This is the precise rational connection: rationality in Laplace frequency,
not necessarily rationality of the trajectory in physical time. The general
matrix form is \(R(\zeta I-T)^{-1}S\); zero modes and appropriate coupled modes
can retain offsets or other behavior. Negative decay is not assumed for all
neural responses. A hierarchy increases the retained response state rather
than the order of an initial Taylor polynomial.

This memory/auxiliary-state connection is also used in generalized Langevin
model reduction; see Lei, Baker and Li (2016),
[Data-driven parameterization of the generalized Langevin equation](https://arxiv.org/html/1606.02596).
The complete main text was read. Its equilibrium, stationary-noise and
fluctuation-dissipation assumptions are not assumptions of neural training,
and its fitted coefficients are not supplied neural coefficients. The linear
identities here were derived directly and do not invoke its statistical claims.

## 5. The remaining neural research question

The credible target is a population of neurons carrying current responses and
\(P\) auxiliary memory coordinates, with closed laws computed from that retained
population and the defining training problem. Merely writing down unknown
functions for those laws is not a completed compression method. In particular:

1. Neural response kernels can depend on both times and on the evolving law;
   they have not been shown to be stationary sums of exponentials.
2. Model-derived initialization must retain reuse of the same initial Gaussian
   weights and the induced response correlations. Nonlinear responses need
   not be jointly Gaussian. An unknown full initialization-driven
   process would hide part of the original problem.
3. Coefficients must be obtainable without the dense matrix, unbounded history,
   or a previously solved target trajectory. Arbitrarily trained auxiliary
   factors would not meet this contract.
4. Useful approximation requires a small omitted observable-memory contribution
   and stable propagation of its error. Finitely many inputs or outputs alone
   do not prove a low memory dimension.
5. Sample-indexed response fields scale with sample count; fixed input dimension
   does not remove that dependence. Continuous input populations require a
   separate input representation or justified population-law computation.

The most direct theoretical next target is a nonzero finite terminal law for
the first missing forward/backward actions, including initialization and
adjoint consistency, followed by a bound on its defect along reachable states.
Its coefficients and smallness are open. No claim is made that this will beat
the old dictionaries, converge for the canonical population, or have a useful
rate. What has been clarified is that neither plateaus nor zero Taylor radius
blocks the proposed per-neuron state formulation; the substantive obstacle is
the closure and efficiency of the history's effect on future responses.
