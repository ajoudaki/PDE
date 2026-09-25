# Gaussian initialization checks for an exact current-state law

## Scope and claim level

This note is a prompt-only scoped derivation. Its scientific inputs are precisely the one-sample network, training equations, initialization, and population Gaussian-calculus primitive supplied in the assignment. No repository scientific source, other study, external paper, or prior review was consulted. The rigorous-mathematics skill supplied process instructions only. This note tests an already proposed retained state and velocity; it does not choose a new closure or add ad hoc state variables.

The assignment supplies

\[
z_1=W_1x/\sqrt d,\quad h_1=\phi(z_1),\qquad
z_2=W_2h_1,\quad h_2=\phi(z_2),\qquad
f=\langle W_3,h_2\rangle_n,
\]

\[
\delta_2=W_3\odot\phi'(z_2),\quad
b_1=W_2^\top\delta_2,\quad
\delta_1=\phi'(z_1)\odot b_1,
\quad r=f-y,\quad \chi=\|x\|^2/d,
\]

where \(\langle u,v\rangle_n=n^{-1}u^\top v\), and

\[
\dot z_1=-2r\chi\delta_1,\qquad
\dot W_3=-2rh_2,\qquad
\dot W_2=-\frac{2r}{n}\delta_2h_1^\top.
\tag{1}
\]

All activation derivatives and unmarked products of vectors below are componentwise. At initialization \(W_{2,0}\) has independent centered Gaussian entries of variance \(1/n\), independent of the standard Gaussian initialization roots for \(W_1,W_3\). In particular, for fixed \(x\), the first-layer initial preactivation has the law \(\sqrt\chi\,G\) for a standard Gaussian root \(G\).

The permitted population primitive states that each fixed finite initialization expression formed from these roots, \(W_{2,0}\), its transpose, and activation derivatives has a joint scalar population law, whose expectations are evaluated with the specified Gaussian sources and Stein calculus. This does not, by itself, authorize differentiation through a width limit, an infinite expansion, or an expectation without the corresponding regularity and integrability.

The main squared-residual test below concerns exact tagged or collectively coupled motion under the true initialization coupling. A claim about only one-time marginal distributions is weaker and has a different necessary test, explained below.

## Exact derivatives before taking a population limit

Assume \(\phi\in C^2\) and a classical finite-width solution on the time interval considered. Introduce only the abbreviations

\[
q_1=\langle h_1,h_1\rangle_n,\qquad
q_\delta=\langle\delta_2,\delta_2\rangle_n,\qquad
p=\phi'(z_1)^2\odot b_1,
\]

\[
a=q_1\delta_2+\chi W_2p,
\tag{2}
\]

and

\[
c=q_\delta h_1+
W_2^\top\left[
 h_2\odot\phi'(z_2)
 +(W_3\odot\phi''(z_2))\odot a
\right].
\tag{3}
\]

First,

\[
\dot h_1=\phi'(z_1)\odot\dot z_1=-2r\chi p.
\tag{4}
\]

Using both changing factors in \(z_2=W_2h_1\),

\[
\begin{aligned}
\dot z_2
&=\dot W_2h_1+W_2\dot h_1\\
&=-2rq_1\delta_2-2r\chi W_2p=-2ra.
\end{aligned}
\tag{5}
\]

Differentiating the second-layer backward signal gives

\[
\begin{aligned}
\dot\delta_2
&=\dot W_3\odot\phi'(z_2)
 +(W_3\odot\phi''(z_2))\odot\dot z_2\\
&=-2r\left[
h_2\odot\phi'(z_2)+(W_3\odot\phi''(z_2))\odot a
\right].
\end{aligned}
\tag{6}
\]

The transpose operator changes too:

\[
\dot W_2^\top\delta_2
=-\frac{2r}{n}h_1\delta_2^\top\delta_2
=-2rq_\delta h_1.
\]

Consequently,

\[
\dot b_1=\dot W_2^\top\delta_2+W_2^\top\dot\delta_2=-2rc.
\tag{7}
\]

The first term \(q_\delta h_1\) in (3) is the direct response of \(W_2^\top\). It is not part of the response caused by changing \(\delta_2\), and omitting it changes the true acceleration.

For the residual, the normalized pairing and the transpose identity give

\[
\begin{aligned}
\dot r=\dot f
&=\langle\dot W_3,h_2\rangle_n
 +\langle W_3,\phi'(z_2)\odot\dot z_2\rangle_n\\
&=-2r\left[
 \langle h_2,h_2\rangle_n+q_1q_\delta
 +\chi\langle\delta_2,W_2p\rangle_n
\right]\\
&=-2rK,
\end{aligned}
\tag{8}
\]

where

\[
K=\langle h_2,h_2\rangle_n+q_1q_\delta
 +\chi\langle\delta_1,\delta_1\rangle_n\geq0.
\tag{9}
\]

Indeed, \(\langle\delta_2,W_2p\rangle_n
=\langle b_1,p\rangle_n=\langle\delta_1,\delta_1\rangle_n\).
As a sign check, \(\frac d{dt}r^2=-4r^2K\leq0\).

Now differentiate \(\delta_1=\phi'(z_1)\odot b_1\):

\[
\begin{aligned}
\dot\delta_1
&=\phi''(z_1)\odot\dot z_1\odot b_1
 +\phi'(z_1)\odot\dot b_1\\
&=-2r\left[
 \chi\phi''(z_1)\odot\phi'(z_1)\odot b_1^2
 +\phi'(z_1)\odot c
\right].
\end{aligned}
\tag{10}
\]

Therefore the exact first-layer preactivation acceleration is

\[
\boxed{
\ddot z_1
=-2\chi\dot r\,\delta_1
 +4\chi r^2\left[
 \chi\phi''(z_1)\odot\phi'(z_1)\odot b_1^2
 +\phi'(z_1)\odot c
\right].
}
\tag{11}
\]

Equivalently, the first term is \(4\chi rK\delta_1\) after (8).

For a proposed motion state based on the original feature \(h_1\), the relevant acceleration is instead

\[
\ddot h_1=\phi''(z_1)\odot\dot z_1^2
 +\phi'(z_1)\odot\ddot z_1.
\]

Substituting (1) and (11) yields

\[
\boxed{
\begin{aligned}
\ddot h_1
={}&-2\chi\dot r\,\phi'(z_1)^2\odot b_1\\
&+8\chi^2r^2\phi''(z_1)\odot\phi'(z_1)^2\odot b_1^2\\
&+4\chi r^2\phi'(z_1)^2\odot c.
\end{aligned}
}
\tag{12}
\]

Its first term is \(4\chi rKp\). The coefficient \(8\) in the middle term is required: one contribution comes from differentiating the feature map a second time and another from differentiating the backward factor \(\phi'(z_1)\).

Equations (2)–(12) hold at every finite-width time where the solution exists. Evaluating them at time zero puts every term within the stated finite-expression Gaussian primitive. No independence between an operator and its dynamically generated argument was used.

## The exact initial population residual

Let \(X_t\) denote the full state, and let \(m_t=P(X_t)\) be the retained tagged state of the particular proposal under examination. Write \(I_t\) for all current population and operator information that the proposal actually retains. Suppose it proposes

\[
\dot m_t=F(m_t,I_t).
\tag{13}
\]

Define \(V_t=\frac d{dt}P(X_t)\) under the true coupled motion. For an exact pathwise current-state law, a necessary condition at each time where the derivative exists is

\[
\mathcal D_t=\mathbb E\|V_t-F(m_t,I_t)\|^2=0.
\tag{14}
\]

Here the expectation uses the true *joint* coupling of the roots, fields, and operator applications. A nonnegative square has expectation zero exactly when the residual vanishes almost surely. Independent resampling of any repeated operator argument changes the quantity being tested.

In particular, if the motion state contains \((h_1,v_1)\) with \(v_1=\dot h_1\), the coordinate equation \(\dot h_1=v_1\) tests no closure. If the proposed equation is \(\dot v_1=A_1(m,I)\), the informative initial condition is

\[
\mathcal D_{h,0}
=\mathbb E\left|\ddot H_{1,0}-A_1(m_0,I_0)\right|^2=0,
\tag{15}
\]

using the joint population version of (12). The analogous test for a \((z_1,\dot z_1)\) state uses (11). Other retained coordinates and retained operator equations require their own residuals; passing (15) alone is insufficient for the full state.

If the proposal stores only positions, its predicted acceleration must be the total derivative of its velocity functional along the proposed full retained dynamics. This includes dependence through current law and operator variables, not just a derivative with respect to the tagged position. In a differentiable collective state notation \(S\), this is \(D\widehat F(S)\widehat F(S)\) for the relevant component.

For a Gaussian initialization calculation to establish (15) as a population-motion test, the following must be justified:

1. The true and proposed quantities possess a common joint population realization under the supplied primitive. If the proposed velocity is an implicit or infinite operator construction rather than a finite expression, a justified limiting construction is additionally needed.
2. The squared discrepancy is integrable. Convergence in distribution of finite-width expressions alone does not imply convergence of their second moments; uniform integrability or a suitable stronger convergence result is required if finite-width residual expectations are used.
3. The population trajectory is differentiable to the order being tested, and the finite-width derivative limits agree with those derivatives. The Gaussian initialization primitive by itself does not provide this interchange.

Thus a strictly positive justified initial residual falsifies the corresponding exact motion claim. Without condition 3, a positive discrepancy between derivative limits does not by itself disprove convergence of trajectories in a topology controlling only their values.

The degenerate cases also matter. If \(r_0=0\), every velocity in (1) vanishes and the true trajectory is stationary as long as uniqueness holds. If \(\chi=0\), the first-layer feature does not move. First-layer initial motion tests are correspondingly uninformative about nondegenerate motion in these cases.

## Conditional variance: the best possible retained-state prediction

Let \(\mathcal G_t=\sigma(m_t,I_t)\) denote exactly the information that makes the proposed tagged velocity measurable. Include the operator evaluations genuinely available to that tagged calculation, without silently supplying additional hidden microscopic information. For square-integrable, finite-dimensional or Hilbert-valued \(V_t\), conditional expectation gives

\[
\begin{aligned}
\mathbb E\|V_t-F(m_t,I_t)\|^2
={}&\mathbb E\|V_t-\mathbb E[V_t\mid\mathcal G_t]\|^2\\
&+\mathbb E\|\mathbb E[V_t\mid\mathcal G_t]-F(m_t,I_t)\|^2.
\end{aligned}
\tag{16}
\]

To verify the identity, write the residual as the sum of the two differences on the right and expand its square. The second difference is \(\mathcal G_t\)-measurable, while the first has conditional expectation zero, so their expected inner product is zero.

The first term is the expected conditional variance. It is a lower bound for the error of every deterministic velocity using the same retained information. A positive value rules out such an exact tagged closure, irrespective of how its drift is chosen. If it vanishes, the proposal must still equal the conditional mean, as required by the second term. Rich operator information may make the first term vanish; the identity does not presume it is positive.

The same identity applies to acceleration in (15), replacing \(V_t\) by \(\ddot H_{1,t}\). Conditional expectation is used here as a diagnostic and lower bound, not as a recommendation to replace the proposal by a conditional-drift model.

Checking only \(\mathbb E[V_t-F_t]=0\) is much weaker. Even checking
\(\mathbb E[g(m_t,I_t)(V_t-F_t)]=0\) for every bounded scalar measurable \(g\) proves only that the conditional mean residual is zero; it does not remove conditional variance.

## One-time marginals versus coupled motion

Under assumptions allowing differentiation under expectation, every smooth scalar test function satisfies

\[
\frac d{dt}\mathbb E\psi(m_t)
=\mathbb E[\nabla\psi(m_t)\cdot V_t].
\tag{17}
\]

Replacing \(V_t\) by \(\mathbb E[V_t\mid m_t]\) preserves the right side. This produces the correct weak one-time marginal transport along the true law. Turning it into a predictive closed PDE still requires identifying that drift from retained current data and proving the appropriate existence and uniqueness. Equation (17) alone neither establishes tagged trajectories nor the necessary inter-layer, operator, or multi-time couplings. Tests against gradients are even weaker than testing every vector residual against every scalar state function, since a divergence-free flux discrepancy can be invisible in (17).

For a precise logical counterexample, let \(X,Y\) be independent standard Gaussians and set

\[
m_t=X\cos t+Y\sin t.
\]

Its marginal law is standard Gaussian at every time, as is the law under the proposed motion \(\dot m=0\), \(m_0=X\). Yet

\[
\mathbb E|\dot m_0-0|^2=\mathbb EY^2=1,
\qquad
\mathbb E[m_tm_0]=\cos t
\]

for the true motion, whereas the stationary proposal has temporal covariance \(1\). This example is only a counterexample to an inference from marginal agreement to path agreement; it is not a replacement network or proposed closure.

For a collective claim, (14) must cover all retained fields under their common coupling, and the retained operator dynamics must also agree. If the chosen operator state does not admit a Hilbert norm, one may formulate zero squared scalar residuals on a specified separating family of operator evaluations. Extending agreement from a countable dense family to all intended arguments requires the corresponding continuity or boundedness assumptions; it is not automatic.

## What finite and infinite initial jets establish

A failed, justified initial residual is decisive against the tested exact claim. Passing it checks only initialization. Passing finitely many higher derivative checks still does not establish any positive-time interval. Computing further derivatives also requires higher activation regularity and appropriate moment and limit-interchange control at every order.

Even equality of all initial derivatives is insufficient under mere smoothness. Let

\[
g(t)=
\begin{cases}
e^{-1/t^2},&t>0,\\
0,&t\leq0.
\end{cases}
\]

The functions \(0\) and \(g\) have identical derivatives of every order at zero but differ for every positive time. This phenomenon can occur for smooth autonomous retained equations as well: starting from \((\tau,u)=(0,0)\), compare the vector fields \((1,0)\) and \((1,g'(\tau))\). Their trajectories have identical initial jets and distinct second coordinates at positive time.

There is a separate obstacle: the initial Taylor series may have zero radius of convergence even though every derivative is a valid Gaussian expectation. For \(G\sim N(0,1)\), consider

\[
q(t)=\mathbb E\frac1{1+t^2G^2}.
\]

Write \(\eta(s)=(1+s^2)^{-1}\). For each fixed order \(j\), \(\eta^{(j)}\) is bounded on the real line, so
\(|\partial_t^j\eta(tG)|\leq C_j|G|^j\), an integrable bound. Hence \(q\) is smooth and differentiation under expectation is justified at every fixed order. Its formal coefficients are

\[
\frac{q^{(2k)}(0)}{(2k)!}=(-1)^k\mathbb EG^{2k}
=(-1)^k(2k-1)!!,
\qquad q^{(2k+1)}(0)=0.
\]

For \(k\geq2\), at least \(\lfloor k/2\rfloor\) factors in \((2k-1)!!\) are at least \(k\). Thus its \(2k\)-th root diverges at least on the order of \(k^{1/4}\), proving zero Taylor radius. Each finite derivative calculation remains valid.

These examples establish the logical limits of an all-jets argument. Equality of all initial jets can imply local equality if analyticity in an appropriate state topology, with a positive common convergence radius, is separately proved. The stated Gaussian primitive does not establish that property. Uniform remainder estimates or a different uniqueness argument could also supply the missing positive-time control.

## Collective projectability and restart sufficiency

For a sufficient full-dynamics criterion, let \(X\) be the full microscopic or population state, \(\dot X=B(X)\) its well-defined evolution, and let

\[
S=P(X)
\]

be the *entire* retained state: tagged fields, current population information, and retained operators. Suppose the proposal is the closed autonomous equation

\[
\dot S=\widehat F(S).
\tag{18}
\]

Assume that the projection obeys the chain rule along the full trajectories; that the proposed equation exists and is unique in the relevant class; and that, on the forward reachable set under consideration,

\[
DP(X)B(X)=\widehat F(P(X)).
\tag{19}
\]

Then \(S_t=P(X_t)\) satisfies (18) with initial state \(P(X_0)\). Uniqueness of (18) identifies it with the proposed trajectory throughout their common existence interval. This is the full proof of sufficiency. Equality almost everywhere in time along the actual full trajectories is enough for the same integral-equation argument; requiring (19) on every reachable state is a stronger reusable condition.

The structural obstruction is visible on fibres of the projection. If two reachable full states \(X,X'\) have \(P(X)=P(X')\) but

\[
DP(X)B(X)\ne DP(X')B(X'),
\]

no single-valued current-state velocity on that retained state can describe both. Conversely, fibrewise constancy defines a candidate projected vector field; to obtain (18) one must still verify that it is the proposed field and that the resulting evolution is well posed.

Under the sufficient assumptions, the criterion also proves exact restart consistency. At any reachable time \(\tau\), initialize (18) from \(S_\tau=P(X_\tau)\). The projected true continuation solves that same initial-value problem, so uniqueness makes the restart reproduce \(P(X_{\tau+t})\). Two reachable full states with the same retained state therefore have the same retained future. This conclusion concerns the complete collective state and its coupling, not just separate marginal distributions.

Initialization calculations are necessary local checks on (19). They cannot replace its positive-time verification, and an exact tagged equation conditional on an unspecified evolving operator does not establish a closed current-state law for that operator.

## Status

The finite-width differentiation identities and the conditional-variance decomposition above are exact under their stated assumptions. Gaussian initialization makes their finite-expression joint population evaluations available through the supplied primitive, subject to the stated integrability and derivative-limit qualifications. No candidate retained velocity was supplied for substitution, so this note does not assert that a particular closure passes or fails its residual test, nor that a nonlinear population evolution or its analyticity has been established.
