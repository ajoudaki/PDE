# Gaussian initialization: an exact local-label theorem and the global bridge

Status: first independent round, 2026-10-10. The arbitrary-fixed-label
high-probability fitting target is **open** in this route. The proved result is
an all-time, finite-width theorem for a width-independent small-label class,
including nonorthogonal data and mixed labels. No experiment was run and no
other research artifact was consulted. This is a scoped, prompt-only attempt;
the investigation, rigorous-proof, and canonical-notation skills were applied.

## Contract and exact flow

Let \(X=[x_1,\ldots,x_m]\in\mathbb R^{d\times m}\) have unit columns. The
data are fixed as width \(n\) grows. The two hidden layers, readout, residual,
and loss are

\[
 U=\tanh(AX),\qquad H=\tanh(WU),\qquad
 f=\frac1nH^\top w,\qquad r=f-y,\qquad
 \mathcal L=\frac1m\|r\|_2^2,
\]

where \(A\in\mathbb R^{n\times d}\),
\(W\in\mathbb R^{n\times n}\), and \(w\in\mathbb R^n\). Activation
functions act entrywise. The actual gradient-flow mobilities are \((n,1,n)\)
for \((A,W,w)\). Initialization is precisely

\[
 A_{ij}(0)\sim N(0,1),\qquad W_{ij}(0)\sim N(0,1/n),
 \qquad w(0)=0,
\]

with all indicated Gaussian entries mutually independent. Write

\[
 E=1-U\odot U,\qquad D=1-H\odot H,\qquad
 C=(w\mathbf1_m^\top)\odot D,\qquad B=E\odot(W^\top C).
\]

The exact flow is

\[
 \begin{aligned}
 \dot w&=-\frac2mHr,\\
 \dot W&=-\frac{2}{mn}C\operatorname{diag}(r)U^\top,\\
 \dot A&=-\frac2m B\operatorname{diag}(r)X^\top.
 \end{aligned}
\]

For example, the last equation follows by multiplying
\(\nabla_A\mathcal L=2B\operatorname{diag}(r)X^\top/(mn)\) by mobility
\(n\). The induced tangent Gram matrix is

\[
 K=\frac1nH^\top H
 +\frac1{n^2}(U^\top U)\odot(C^\top C)
 +\frac1n(X^\top X)\odot(B^\top B).
\]

Each summand is a Gram matrix: the second uses tensor products of the
corresponding columns of \(U,C\), and the third those of \(X,B\). Thus

\[
 \dot r=-\frac2mKr,\qquad
 \dot{\mathcal L}=-\frac4{m^2}r^\top Kr\le0,
 \qquad K\succeq\frac1nH^\top H.                  \tag{1}
\]

All dynamics above remain the original nonlinear dynamics. No features,
parameters, or Gram matrices have been frozen.

## Exact feature-transport bounds

Define the accumulated residual and the normalized readout norm by

\[
 S(t)=\frac2{\sqrt m}\int_0^t\|r(s)\|_2\,ds
     =2\int_0^t\sqrt{\mathcal L(s)}\,ds,
 \qquad q(t)=\frac{\|w(t)\|_2}{\sqrt n}.
\]

Let \(b_0=\|W(0)\|_{\mathrm{op}}\). Since activation and derivative
magnitudes are at most one,

\[
 \|H\|_{\mathrm{op}},\|U\|_{\mathrm{op}}\le\sqrt{nm},\qquad
 \|C\operatorname{diag}(r)\|_F\le\|w\|_2\|r\|_2.
\]

The readout equation and \(w(0)=0\) give \(q(t)\le S(t)\). The second-layer
equation then gives

\[
 \|\dot W\|_F
 \le\frac2{\sqrt m}q\|r\|_2=q\dot S,
 \qquad
 \|W(t)-W(0)\|_F\le\frac12S(t)^2.                 \tag{2}
\]

For the first layer, the entrywise multiplier \(E\) contracts Frobenius norm,
so

\[
 \frac{\|\dot A\|_F}{\sqrt n}
 \le\frac2m\|W\|_{\mathrm{op}}q\|r\|_2\|X\|_{\mathrm{op}}
 \le\frac{\|X\|_{\mathrm{op}}}{\sqrt m}
       (b_0+S^2/2)S\dot S.
\]

Integration yields

\[
 \frac{\|A(t)-A(0)\|_F}{\sqrt n}
 \le\frac{\|X\|_{\mathrm{op}}}{\sqrt m}
       \left(\frac{b_0S(t)^2}{2}+\frac{S(t)^4}{8}\right).       \tag{3}
\]

The activation is one-Lipschitz. Split
\(WU-W(0)U(0)=(W-W(0))U+W(0)(U-U(0))\), and apply (2), (3). With
\(\gamma=\|X\|_{\mathrm{op}}^2/m\le1\), this gives

\[
 \frac{\|H(t)-H(0)\|_F}{\sqrt n}\le D_{b_0,X}(S(t)),
 \quad
 D_{b_0,X}(s)=\sqrt m\left[
 \frac{s^2}{2}+\gamma b_0\left(\frac{b_0s^2}{2}+\frac{s^4}{8}\right)
 \right].                                                       \tag{4}
\]

These are deterministic identities/inequalities for every finite width and
every label vector. They exhibit quadratic initial hidden motion, but do not
make it vanish as width grows.

They also prove global finite-width existence. On a finite time interval,
(1) gives \(S(t)\le2t\sqrt{\mathcal L(0)}\). Equations (2), (3), and
\(\|w\|_2\le\sqrt nS\) then bound every parameter. The smooth vector field
is locally Lipschitz, so its local solution cannot terminate at finite time
while all parameters remain bounded.

## Deterministic all-time bootstrap

Suppose, for some \(\lambda>0\) and \(b\ge b_0\),

\[
 \lambda_{\min}\!\left(\frac1nH(0)^\top H(0)\right)\ge\lambda,
 \qquad
 D_{b,X}\left(\frac{4\sqrt m\|y\|_2}{\lambda}\right)
 <\frac{\sqrt\lambda}{2}.                              \tag{5}
\]

Then the exact nonlinear flow satisfies, for every \(t\ge0\),

\[
 \lambda_{\min}\!\left(\frac1nH(t)^\top H(t)\right)\ge\frac\lambda4,
 \qquad
 \mathcal L(t)\le\mathcal L(0)e^{-\lambda t/m}.           \tag{6}
\]

To prove this, take any interval on which
\(\|H(t)-H(0)\|_F/\sqrt n<\sqrt\lambda/2\). For a unit vector
\(v\in\mathbb R^m\), the triangle inequality gives

\[
 \frac{\|H(t)v\|_2}{\sqrt n}
 \ge\frac{\|H(0)v\|_2}{\sqrt n}
       -\frac{\|(H(t)-H(0))v\|_2}{\sqrt n}
 >\frac{\sqrt\lambda}{2}.
\]

Consequently (1) gives
\(\dot{\mathcal L}\le-(\lambda/m)\mathcal L\), and hence

\[
 S(t)\le\frac2{\sqrt m}\|y\|_2
      \int_0^te^{-\lambda s/(2m)}\,ds
 \le\frac{4\sqrt m\|y\|_2}{\lambda}.
\]

By (4) and the strict inequality in (5), the feature displacement stays
strictly below the assumed boundary. A first-exit argument extends this
estimate to every time, proving (6). If \(y=0\), all initial gradients vanish
and the conclusion is immediate. For nonzero labels, (6) also makes
\(S(\infty)\) finite. The parameter velocities in the preceding estimates
are integrable, so all three parameter arrays converge at each fixed width.

No premise in this argument restricts input inner products or label signs.
The restriction is quantitative label magnitude.

## Gaussian probability tending to one

For \(a\sim N(0,I_d)\), define the first-layer population covariance

\[
 \Sigma_{ab}=\mathbb E[\tanh(a^\top x_a)\tanh(a^\top x_b)].
\]

For \(G\sim N(0,\Sigma)\), define the initial second-layer feature Gram

\[
 Q_{ab}=\mathbb E[\tanh(G_a)\tanh(G_b)],\qquad
 \kappa=\lambda_{\min}(Q)>0.                              \tag{7}
\]

Positive definiteness in (7) is the supplied population-feature assumption;
it is not deduced here merely from distinct/nonantipodal inputs.

The finite-width matrix \(U(0)^\top U(0)/n\) converges in probability to
\(\Sigma\), entrywise and thus in operator norm, by the elementary law of
large numbers for bounded independent rows. Conditional on \(U(0)\), the
rows of \(W(0)U(0)\) are independent centered Gaussian vectors with that
covariance. Their activated outer products have entries bounded by one.
Conditional variance bounds and a union bound show that their empirical
mean differs in probability by \(o(1)\) from its conditional expectation.
That expectation converges to \(Q\): couple the Gaussians as
\(\Sigma_n^{1/2}g\), where \(g\sim N(0,I_m)\); continuity of the
positive-semidefinite square root and bounded continuous activations give
convergence of the expectation. Therefore

\[
 \frac1nH(0)^\top H(0)\longrightarrow Q
 \quad\text{in probability}.                            \tag{8}
\]

A width-independent bound on \(b_0\) also holds with probability tending to
one. For completeness, take a \(1/4\)-net of the unit sphere with at most
\(9^n\) points. Such a net follows by packing disjoint radius-\(1/8\) balls
centered on a maximal separated subset inside the radius-\(9/8\) ball.
For fixed unit vectors \(u,v\), \(u^\top W(0)v\sim N(0,1/n)\), so

\[
 \Pr\left(\max_{u,v\text{ in net}}|u^\top W(0)v|>4\right)
 \le2\exp[-(8-2\log9)n].
\]

Approximating a maximizing pair of unit vectors by net points loses at most
\(\|W(0)\|_{\mathrm{op}}/2\), so \(\|W(0)\|_{\mathrm{op}}\le8\) off
this exceptional event. Independence between this event and (8) is
unnecessary; a union bound suffices.

Consequently, if the fixed label vector satisfies

\[
 D_{8,X}\left(\frac{8\sqrt m\|y\|_2}{\kappa}\right)
 <\frac12\sqrt{\frac\kappa2},                            \tag{9}
\]

then with probability tending to one as \(n\to\infty\), the exact
finite-width flow satisfies

\[
 \mathcal L(t)\le\mathcal L(0)e^{-\kappa t/(2m)}
 \quad\text{for every }t\ge0,
 \qquad \lim_{t\to\infty}\mathcal L(t)=0.               \tag{10}
\]

The constants are deliberately elementary and conservative. The label class
in (9) has a positive radius independent of width for every fixed dataset
satisfying (7); it includes fixed mixed labels and nonorthogonal geometries.
It excludes arbitrary bounded label magnitudes, so (10) is not the requested
full theorem.

## Exact bridge for unrestricted labels

There is a useful form of the remaining coercivity problem that does not
require a uniform lower eigenvalue. Whenever \(r(t)\ne0\), define the
residual-aligned tangent value by

\[
 k(t)=\frac{r(t)^\top K(t)r(t)}{\|r(t)\|_2^2}\ge0,
 \qquad e(t)=\sqrt{\mathcal L(t)}.
\]

Equation (1) gives

\[
 \dot e=-\frac2m k e,\qquad \dot S=2e,
 \qquad \frac{de}{dS}=-\frac1m k(t(S)).                  \tag{11}
\]

Here \(t(S)\) is well defined on any interval of positive loss because
\(\dot S>0\). Thus a deterministic lower bound

\[
 k(t)\ge g(S(t)),\qquad g\ge0,\qquad
 \int_0^\infty g(s)\,ds=\infty                          \tag{12}
\]

would force \(\mathcal L(t)\to0\) for arbitrary labels. Indeed, positive
limiting loss would imply \(S(t)\to\infty\), and integration of (11) would
give \(e(t)\le e(0)-m^{-1}\int_0^{S(t)}g(s)\,ds<0\) eventually. A positive
constant lower bound on \(k\) would additionally give an exponential rate.

What is **not proved** is a bound such as (12) for Gaussian-initialized
trajectories, either in a rigorously identified population limit or with
probability tending to one for finite-width trajectories. Bound (4) gives
the explicit minorant
\([\sqrt\lambda-D_{b,X}(S)]_+^2\), whose integral is finite. That is exactly
why this argument closes only below a label threshold. Replacing this
minorant by a nonintegrable one is a substantial missing theorem, not a
constant improvement or an omitted technical estimate.

## Two tempting bridges that do not suffice

**Finite-time support.** A pushforward can have full Gaussian support at
every finite time while its feature covariance collapses. For example,
\(Z_t=e^{-t}Z_0\) with \(Z_0\sim N(0,I_m)\) has full support and

\[
 \mathbb E[\tanh(Z_t)\tanh(Z_t)^\top]
 =\mathbb E[\tanh(e^{-t}Z_{0,1})^2]I_m
 \preceq e^{-2t}I_m.
\]

This is not asserted to be a network trajectory or a fitting counterexample.
It proves only that full support at each finite time, by itself, supplies no
all-time spectral estimate. Quantitative transported mass or an alternate
residual-aligned mechanism is needed. The shrinking eigenvalue in this
example even has a finite time integral.

**Population fitting and compact-time convergence.** Suppose separately
that a correctly identified deterministic population loss tends to zero and
that \(\mathcal L_n(T)\) converges in probability to it for every fixed
\(T\). By monotonicity, these assumptions imply

\[
 \text{for every }\varepsilon>0,\qquad
 \Pr\bigl(\lim_{t\to\infty}\mathcal L_n(t)\le\varepsilon\bigr)
 \longrightarrow1.
\]

Choose a finite \(T\) with population loss below \(\varepsilon/2\), then
use compact-time convergence and \(\mathcal L_n(\infty)\le\mathcal L_n(T)\).
This argument does **not** show
\(\Pr(\mathcal L_n(\infty)=0)\to1\); deterministic positive terminal losses
\(1/n\) already separate the assertions. A finite-width all-time estimate
such as the bootstrap above is an additional bridge.

## Route disposition

The exact nonlinear local-label theorem is established by the derivation
above, pending independent review. The unrestricted-label population route
is blocked at quantitative persistence of residual-aligned feature diversity.
Neither a strong probabilistic failure construction nor an arbitrary-label
positive theorem has been obtained. A productive reopening would provide
either a nonintegrable minorant in (12), a verified population support
mechanism plus an all-time finite-width trapping estimate, or a mechanism
showing a fixed positive-probability basin of nonzero limiting loss. Mere
Gaussian full support, generic initial positive definiteness, or a
compact-time mean-field limit does not close this gap.

## Second-round result: capture near a nonlinear population endpoint

The small-label theorem above is frozen as an auxiliary result. The following
local statement permits arbitrarily large original labels; it requires only
a sufficiently small *remaining* residual at a suitable later time.

Fix a finite-width snapshot at time \(T\). Suppose

\[
 \frac{\|w(T)\|_2}{\sqrt n}\le q,\quad
 \|W(T)\|_{\mathrm{op}}\le b,\quad
 \lambda_{\min}\left(\frac1nH(T)^\top H(T)\right)\ge\lambda>0.
\]

Let \(S_T(t)=2\int_T^t\sqrt{\mathcal L(s)}\,ds\), and define

\[
 M_q(s)=qs+s^2/2,\qquad
 D_{q,b,X}(s)=\sqrt m\left[
 M_q(s)+\gamma b\left(bM_q(s)+M_q(s)^2/2\right)\right].   \tag{13}
\]

The same exact estimates, now with a nonzero initial readout, give

\[
 \begin{aligned}
 \|w(t)\|_2/\sqrt n&\le q+S_T(t),\\
 \|W(t)-W(T)\|_F&\le M_q(S_T(t)),\\
 \|A(t)-A(T)\|_F/\sqrt n
 &\le\frac{\|X\|_{\mathrm{op}}}{\sqrt m}
       \left[bM_q(S_T(t))+M_q(S_T(t))^2/2\right],\\
 \|H(t)-H(T)\|_F/\sqrt n&\le D_{q,b,X}(S_T(t)).
 \end{aligned}                                                   \tag{14}
\]

The first two follow by integrating \(q+S_T\). For the third, use
\(\|W(t)\|_{\mathrm{op}}\le b+M_q(S_T)\) and
\(M_q'(s)=q+s\); the integral is exactly
\(bM_q+M_q^2/2\). The last follows from the same decomposition of \(WU\)
as in (4), now based at time \(T\).

Consequently the explicit capture condition is

\[
 D_{q,b,X}\left(\frac{4\sqrt m\|r(T)\|_2}{\lambda}\right)
 <\frac{\sqrt\lambda}{2}.                                \tag{15}
\]

Under (15), for every \(t\ge T\),

\[
 \lambda_{\min}\left(\frac1nH(t)^\top H(t)\right)\ge\lambda/4,
 \qquad
 \mathcal L(t)\le\mathcal L(T)e^{-\lambda(t-T)/m}.          \tag{16}
\]

The proof is the previous first-exit argument with \(r(T)\), (13), and (14).
In particular, (15) defines a positive residual radius depending only on
\(q,b,\lambda,X,m\), not on width, and not on the original label magnitude.
Unlike a purely qualitative finite-dimensional local-convergence theorem,
this radius is uniform over widths and over all snapshots obeying the
displayed bounds.

### A precise population-to-finite-width theorem

Consider the original Gaussian initializations and exact flows at every
width. Suppose an independently justified population analysis supplies
deterministic continuous functions \(\mathcal L_\infty(t)\ge0\) and
\(Q_\infty(t)\in\mathbb R^{m\times m}\) with these properties:

1. On each finite physical-time interval,
   \(\sup_{0\le t\le T}|\mathcal L_n(t)-\mathcal L_\infty(t)|\to0\)
   in probability.
2. At each fixed finite time,
   \(H_n(T)^\top H_n(T)/n\to Q_\infty(T)\) in probability.
3. \(\mathcal L_\infty(t)\to0\) and
   \(S_\infty^*=2\int_0^\infty\sqrt{\mathcal L_\infty(t)}\,dt<\infty\).
4. \(Q_\infty(t)\to Q_*\) with
   \(\kappa_*:=\lambda_{\min}(Q_*)>0\).

Then

\[
 \Pr\left(\lim_{t\to\infty}\mathcal L_n(t)=0\right)\longrightarrow1.
                                                               \tag{17}
\]

Moreover, there are deterministic \(T<\infty\) and \(c>0\), independent
of width, such that with probability tending to one,
\(\mathcal L_n(t)\le\mathcal L_n(T)e^{-c(t-T)}\) for every \(t\ge T\).

Here is a complete proof of this implication. Set
\(q=S_\infty^*+1\), \(b=8+q^2/2\), and \(\lambda=\kappa_*/2\).
Continuity of (13) and \(D_{q,b,X}(0)=0\) give a fixed \(\delta>0\) such
that (15) holds whenever \(\|r(T)\|_2<\delta\). Choose a fixed finite
\(T\) sufficiently large that
\(\lambda_{\min}(Q_\infty(T))>3\kappa_*/4\) and
\(m\mathcal L_\infty(T)<\delta^2/4\).

By assumption 1 and
\(|\sqrt a-\sqrt b|\le\sqrt{|a-b|}\) for \(a,b\ge0\),

\[
 S_n(T):=2\int_0^T\sqrt{\mathcal L_n(t)}\,dt
 \longrightarrow 2\int_0^T\sqrt{\mathcal L_\infty(t)}\,dt
 \le S_\infty^*
\]

in probability. Thus \(S_n(T)\le q\), \(\|r_n(T)\|_2<\delta\), and
\(\lambda_{\min}(H_n(T)^\top H_n(T)/n)\ge\lambda\) jointly hold with
probability tending to one. Intersect with
\(\|W_n(0)\|_{\mathrm{op}}\le8\), already proved to have that probability.
The exact initial-time bounds imply

\[
 \|w_n(T)\|_2/\sqrt n\le q,\qquad
 \|W_n(T)\|_{\mathrm{op}}\le8+S_n(T)^2/2\le b.
\]

All hypotheses of (15) now hold on this single event, and (16) proves (17)
with \(c=\kappa_*/(2m)\). There is no interchange of width and infinite-time
limits: approximation is used only at the chosen finite \(T\); exact
finite-width estimates control every later time.

The finite accumulated residual in assumption 3 can be replaced by any
independently proved bounds on normalized readout norm and second-layer
operator norm at arbitrarily accurate fitting snapshots, provided these
bounds remain uniform as the chosen snapshots approach zero loss. In its
present form, the finite-feature-time mechanism supplies those bounds through
the exact inequalities (2)--(3).

### What finite feature time must actually provide

If a population symmetry reduces the residual to a fixed direction and its
feature clock satisfies \(ds/dt=c\sqrt{\mathcal L_\infty(t)}\) for a fixed
\(c>0\), then reaching an endpoint at \(s_*<\infty\) implies
\(S_\infty^*=2s_*/c<\infty\). If the population output-feature Gram is
continuous through that endpoint and positive definite there, assumptions 3
and 4 above follow once zero endpoint loss and approach to the endpoint have
been proved. The actual value of \(c\) must be derived from the chosen
normalization; clocks are not identified merely because both are called
feature time.

For population preactivation law \(\mu_*\) on \(\mathbb R^m\), a sufficient
condition for endpoint output-Gram positive definiteness is that
\(\operatorname{supp}\mu_*\) contain a nonempty open set. Indeed, a zero
quadratic form would give \(v^\top\tanh z=0\) on that open set by continuity.
Differentiating in coordinate \(z_a\) gives
\(v_a\operatorname{sech}^2z_a=0\), hence every \(v_a=0\).

This sufficient condition concerns an actual identified population marginal
at the endpoint. Finite-width Gaussian full support does not establish it.
Nor does invertibility of a flow on the *joint* neuron state automatically
preserve interior support of its preactivation marginal: the joint smooth
system \(\dot z=-w,\dot w=z\), initialized at \(w=0\), has
\(z(s)=\cos(s)z(0)\), which collapses that marginal at \(s=\pi/2\) while
the joint flow remains invertible. This is a logical counterexample to that
support inference, not a claim about the neural gradient flow.

The theorem above uses output-feature Gram positive definiteness. Full
tangent-Gram positive definiteness alone has not been substituted for it:
that substitution would require a width-uniform continuity estimate for the
first-layer tangent block, whose factors include
\((1-U^2)\odot W^\top C\). The output-feature estimate (14) already closes
the desired bridge whenever output diversity survives.

### Scope for pairs and multiple symmetry characters

The capture theorem applies to arbitrary fixed labels once its population
hypotheses are proved. For two samples, a construction with
\(y=(a,-a)\) for arbitrary fixed \(a\) would therefore yield a true
finite-width high-probability theorem if it establishes finite accumulated
residual and a positive-definite two-by-two endpoint output Gram. Positivity
only in the antisymmetric label direction is insufficient for this theorem:
finite-width errors can have a symmetric component.

A proof for one symmetry character does not extend by linear superposition
to labels involving several characters. The hidden dynamics are nonlinear,
and the corresponding residual-driven vector fields need not commute.
If the identified population evolution is continuous in the label vector
on finite time intervals, a snapshot satisfying the strict capture condition
persists under sufficiently small label perturbations, giving an open label
class around any such proved example. The size of that neighborhood, and
whether these neighborhoods cover all mixed labels, require additional
analysis; they are not consequences of the capture lemma alone.

The new endpoint-capture bridge is complete under its exact hypotheses. The
remaining network-specific obligation is population endpoint fitting with
quantitative state control and output diversity, plus a compact-time
approximation theorem for the actual Gaussian μP dynamics.

## Third-round result: full tangent capture from a fourth moment

The preceding restriction to positive-definite *output* Gram can be removed.
The needed extra control is a fourth moment of the backward preactivation
\(Y=W^\top C\) at the capture snapshot. It does not require a bound on its
largest coordinate or persistence of its fourth moment after the snapshot.

The canonical mobility metric on parameter displacements is

\[
 \|(\Delta A,\Delta W,\Delta w)\|_{\mathrm{mob}}^2
 =\frac1n\|\Delta A\|_F^2+\|\Delta W\|_F^2
  +\frac1n\|\Delta w\|_2^2.
\]

The associated tangent feature matrix \(V\) has one column per sample and
three stacked blocks. Its column \(a\) is

\[
 V_a=\begin{bmatrix}
 H_a/\sqrt n\\
 (U_a\otimes C_a)/n\\
 (x_a\otimes B_a)/\sqrt n
 \end{bmatrix},\qquad K=V^\top V.                         \tag{18}
\]

Tensor-factor order is immaterial to these Gram products. This is the actual
weighted Jacobian, not a kernel approximation.

Fix a snapshot \(T\) with

\[
 \|w(T)\|_\infty\le p,\qquad
 \|W(T)\|_{\mathrm{op}}\le b,\qquad
 \left(\frac1n\sum_{i=1}^n\sum_{a=1}^m
          |Y_{ia}(T)|^4\right)^{1/4}\le M_4.              \tag{19}
\]

All constants here are scalar upper bounds. For \(s\ge0\), define

\[
 \begin{aligned}
 M_p(s)&=ps+s^2/2,\\
 \alpha(s)&=\frac{\|X\|_{\mathrm{op}}^2}{\sqrt m}
       [bM_p(s)+M_p(s)^2/2],\\
 \delta(s)&=\sqrt mM_p(s)+b\alpha(s),\\
 \chi(s)&=\sqrt m s+2p\delta(s),\\
 \beta(s)&=M_p(s)\sqrt m(p+s)+b\chi(s)
              +M_4\sqrt{2\alpha(s)},\\
 J(s)&=\left[\delta(s)^2+(p\alpha(s)+\chi(s))^2+
                                      \beta(s)^2\right]^{1/2}.
 \end{aligned}                                                    \tag{20}
\]

Every function is continuous, nondecreasing, and zero at zero. The exact
flow satisfies

\[
 \|V(t)-V(T)\|_{\mathrm{op}}
 \le\|V(t)-V(T)\|_F\le J(S_T(t)).                         \tag{21}
\]

Here is the proof, including the non-Lipschitz term. Each individual readout
coordinate satisfies
\(|\dot w_i|\le2\|r\|_2/\sqrt m=\dot S_T\), so
\(\|w(t)\|_\infty\le p+S_T(t)\). In particular, (14) applies with
\(q=p\), and yields

\[
 \|\Delta U\|_F/\sqrt n\le\alpha(S_T),\quad
 \|\Delta H\|_F/\sqrt n\le\delta(S_T),\quad
 \|\Delta W\|_F\le M_p(S_T).
\]

Here and below \(\Delta\) means current value minus snapshot value. Since
\(|\Delta D|\le2|\Delta H|\), splitting
\(\Delta C=(\Delta w\mathbf1_m^\top)\odot D
 +(w(T)\mathbf1_m^\top)\odot\Delta D\) gives

\[
 \|\Delta C\|_F/\sqrt n\le\chi(S_T),\qquad
 \|C(t)\|_F/\sqrt n\le\sqrt m(p+S_T).
\]

For the second block in (18), split the samplewise tensor product as
\(\Delta U_a\otimes C_a(T)+U_a(t)\otimes\Delta C_a\).
Use \(\|C_a(T)\|_2\le p\sqrt n\),
\(\|U_a(t)\|_2\le\sqrt n\), and the triangle inequality in the sum of
squared sample norms. Its Frobenius displacement is at most
\(p\alpha(S_T)+\chi(S_T)\).

For the third block, set \(Y=W^\top C\). The decomposition
\(\Delta Y=\Delta W^\top C(t)+W(T)^\top\Delta C\) gives

\[
 \|\Delta Y\|_F/\sqrt n
 \le M_p(S_T)\sqrt m(p+S_T)+b\chi(S_T).
\]

Crucially, \(B=E\odot Y\) can be compared using the *snapshot* \(Y(T)\):

\[
 \Delta B=E(t)\odot\Delta Y+\Delta E\odot Y(T).
\]

Since \(0\le E\le1\), we have \(|\Delta E|\le1\) and
\(|\Delta E|\le2|\Delta U|\). Applying the finite-sum Hölder inequality,

\[
 \begin{aligned}
 \frac{\|\Delta E\odot Y(T)\|_F}{\sqrt n}
 &\le M_4\left(\frac1n\sum_{ia}|\Delta E_{ia}|^4\right)^{1/4}\\
 &\le M_4\left(\frac{\|\Delta E\|_F}{\sqrt n}\right)^{1/2}
 \le M_4\sqrt{2\alpha(S_T)}.
 \end{aligned}
\]

Thus \(\|\Delta B\|_F/\sqrt n\le\beta(S_T)\). Because every
\(\|x_a\|_2=1\), this is also the Frobenius displacement bound for the
third block of (18). Combining the three blocks proves (21).

If \(\lambda_{\min}(K(T))\ge\lambda>0\), then the full-tangent capture
condition is

\[
 J\left(\frac{4\sqrt m\|r(T)\|_2}{\lambda}\right)
 <\frac{\sqrt\lambda}{2}.                                \tag{22}
\]

Under (22),

\[
 K(t)\succeq(\lambda/4)I_m,\qquad
 \mathcal L(t)\le\mathcal L(T)e^{-\lambda(t-T)/m}
 \quad(t\ge T).                                         \tag{23}
\]

To verify this final implication, repeat the first-exit argument on the
smallest singular value of \(V\), using (21) in place of the output-feature
estimate. While \(\|\Delta V\|_{\mathrm{op}}<\sqrt\lambda/2\), (1)
bounds \(S_T\) by \(4\sqrt m\|r(T)\|_2/\lambda\); (22) prevents a first
exit. Thus full tangent positivity is sufficient even when the output Gram
is singular.

For fixed \(p,b,M_4,X,m\), the modulus in (20) is generally
\(O(\sqrt s)\) near zero. It nevertheless gives a positive capture radius
independent of width. A Hölder modulus is sufficient; a Lipschitz Jacobian
estimate is not necessary.

### Transfer theorem with full tangent positivity

In the population-to-finite-width theorem above, replace assumptions 2 and 4
by convergence of the *full* \(K_n(T)\) to \(K_\infty(T)\) and
\(K_\infty(t)\to K_*\succ0\). Retain finite accumulated population
residual and compact-time loss convergence. Also suppose that a fixed
\(M_4<\infty\) bounds the snapshot quantity in (19) with probability
tending to one, at all sufficiently late fixed population times. The bound
is uniform in those times, but convergence is required only one fixed time
at a time.

Then the conclusion (17) and eventual exponential capture still hold. In
the proof choose \(p=S_\infty^*+1\), use
\(\|w_n(T)\|_\infty\le S_n(T)\), and choose the residual threshold through
(22). All other steps are unchanged. Thus an endpoint with singular
output-feature Gram can still yield actual finite-width exact fitting.

The fourth-moment assumption can be weakened to uniform tightness. Precisely,
suppose for every \(\eta>0\) there is a finite \(M_{4,\eta}\) such that,
at every sufficiently late fixed \(T\),

\[
 \limsup_{n\to\infty}
 \Pr\left(\left[\frac1n\sum_{ia}|Y_{ia,n}(T)|^4\right]^{1/4}
                 >M_{4,\eta}\right)\le\eta.             \tag{24}
\]

Choose the capture threshold using \(M_{4,\eta}\), then choose a fixed
\(T_\eta\) with sufficiently small population residual. All other snapshot
conditions have probability tending to one, so
\(\limsup_n\Pr(\mathcal L_n(\infty)>0)\le\eta\). Letting
\(\eta\downarrow0\) proves (17). A uniform bound on
\(\mathbb E[n^{-1}\sum_{ia}|Y_{ia,n}(T)|^4]\) gives (24) directly by
Markov's inequality. This avoids assuming a law of large numbers for a
dependent fourth-moment field.

An \(n^{o(1)}\) bound alone does not combine with qualitative compact-time
convergence to prove capture: its shrinking radius may require a physical
time depending on width, outside the given approximation theorem. One would
then need an explicit approximation rate valid to such times, or a uniform
moment-tightness argument such as (24). Population fourth moments by
themselves also do not prove (24); a corresponding finite-width moment bound
or justified moment convergence remains necessary.

The exact new bridge therefore reduces the endpoint task to three concrete
network-specific inputs: finite accumulated population residual, positive
definiteness of the full population tangent Gram at its endpoint, and
uniform tightness of the finite-width backward fourth moment at late fixed
times, in addition to compact-time identification. No output-Gram assumption
or all-time propagation-of-chaos statement is needed.

The fourth moment is convenient rather than sharp. A snapshot bound
\(M_\nu=(n^{-1}\sum_{ia}|Y_{ia}(T)|^\nu)^{1/\nu}\) for any fixed \(\nu>2\)
replaces the final term of \(\beta\) by

\[
 M_\nu[2\alpha(s)]^{1-2/\nu}.
\]

To check this, Hölder uses the exponent \(q_\nu=2\nu/(\nu-2)\) on \(\Delta E\),
and \(|\Delta E|\le1\) gives
\((n^{-1}\sum|\Delta E|^{q_\nu})^{1/q_\nu}
 \le(\|\Delta E\|_F/\sqrt n)^{2/q_\nu}\).
Equivalently, uniform integrability of the normalized squared backward
coordinates supplies a continuity modulus through

\[
 \frac{\|\Delta E\odot Y(T)\|_F}{\sqrt n}
 \le2R\alpha(s)
 +\left[\frac1n\sum_{ia}|Y_{ia}(T)|^2
                      \mathbf1_{\{|Y_{ia}(T)|>R\}}\right]^{1/2}.
\]

For a fixed positive tangent margin, first make the tail smaller than a
fixed fraction of that margin, then choose \(s\) small. Mere boundedness of
the normalized second moment does not make this tail uniformly small.

## Full-rank tanh continuation: a constraint on escape, not compactness

This bounded continuation considered full-column-rank \(X\) with both
activations still exactly tanh. It found no global boundedness theorem and no
Gaussian positive-probability failure event. An independently rederived
obstruction to a generalized trace-balance potential is redundant with an
earlier result in this study, as identified by the supervisor; it is not
counted as a new advance. The following accumulated-motion statement is an
exact necessary condition on any putative escape.

At every fixed finite width, put \(R(t)=\|w(t)\|_2^2/n\). Readout linearity
and the prescribed mobility give

\[
 \dot R(t)=-\frac4m r(t)^\top f(t)
 =\frac1m\bigl(\|y\|_2^2-\|2f(t)-y\|_2^2\bigr)
 \le\mathcal L(0).                                      \tag{25}
\]

The exact loss dissipation is

\[
 -\dot{\mathcal L}
 =\frac1n\|\dot A\|_F^2+\|\dot W\|_F^2
   +\frac1n\|\dot w\|_2^2
 \ge\left(\frac{d}{dt}\sqrt R\right)^2.                 \tag{26}
\]

The final inequality holds almost everywhere because the norm is Lipschitz
and its derivative is bounded by the norm of the vector derivative. In
particular,

\[
 \int_0^\infty\left(\frac{d}{dt}\sqrt{R(t)}\right)^2dt
 \le\mathcal L(0)-\mathcal L(\infty)<\infty.              \tag{27}
\]

More generally the entire parameter trajectory has finite squared speed in
the mobility metric. This implies

\[
 \|\theta(t)-\theta(0)\|_{\mathrm{mob}}=o(\sqrt t),
 \qquad R(t)=o(t)\quad(t\to\infty)                       \tag{28}
\]

at each fixed width. To prove the first assertion, choose \(T\) so the
integral of squared speed after \(T\) is below \(\varepsilon^2\). The
triangle and Cauchy--Schwarz inequalities give

\[
 \|\theta(t)-\theta(0)\|_{\mathrm{mob}}
 \le\|\theta(T)-\theta(0)\|_{\mathrm{mob}}
     +\varepsilon\sqrt{t-T}.
\]

Divide by \(\sqrt t\), take the upper limit, and then let
\(\varepsilon\downarrow0\). This proof does not give a tail time uniform
in width.

Integrating (25), using \(R(0)=0\), now yields the unconditional average
constraint

\[
 \frac1t\int_0^t r(s)^\top f(s)\,ds\longrightarrow0.     \tag{29}
\]

If the prediction vector itself has a limit \(f_*\), then (29) implies

\[
 (f_*-y)^\top f_*=0,\qquad
 \|y\|_2^2=\|f_*\|_2^2+\|f_*-y\|_2^2.                 \tag{30}
\]

Thus a convergent positive-loss escape cannot sustain a residual with a
nonzero limiting radial readout drive. It must have the projection-type
orthogonality in (30). This is a necessary geometric condition, not a claim
that \(f_*\) is the projection onto a proved limiting feature subspace.

There is also a quantitative version. Suppose on an interval \([T_0,T_1]\)
one has \(R(T_0)>0\) and \(\dot R\ge c>0\). Then (26) gives

\[
 \mathcal L(T_0)-\mathcal L(T_1)
 \ge\frac14\int_{T_0}^{T_1}\frac{\dot R^2}{R}\,dt
 \ge\frac c4\log\frac{R(T_1)}{R(T_0)}.
\]

Since \(R(T_1)\ge R(T_0)+c(T_1-T_0)\), such an interval must obey

\[
 T_1-T_0\le\frac{R(T_0)}c
       \left[\exp\!\left(\frac{4\mathcal L(T_0)}c\right)-1\right].
\]

These restrictions still permit logarithmic or other sub-square-root
parameter escape with finite energy and vanishing radial drive. They give
neither finite accumulated residual nor a lower bound on tanh derivatives.
For example, the scalar curve \(z(t)=\log(1+t)\) has finite squared speed
but diverges, and \(\operatorname{sech}^2z(t)\) has a finite time integral.
This curve is not asserted to be a neural trajectory; it demonstrates why
finite energy alone cannot exclude saturation. Full input rank supplies no
additional term in (25)--(29) that closes this gap.

For clarity, the redundant trace-potential obstruction has the following
precise scope. A universal invariant of the form
\(F(A)-(n/2)\|W\|_F^2\), with \(F\in C^2\), would require
\((\nabla_A F)X=\sinh(AX)\odot\cosh(AX)\). With
\(G=X^\top X\succ0\) and \(Z=AX\), fixing the component of \(A\)
orthogonal to the data gives
\(\nabla_ZF=[\sinh Z\odot\cosh Z]G^{-1}\).
Equality of mixed partials requires
\((G^{-1})_{ab}(\cosh(2Z_{ib})-\cosh(2Z_{ia}))=0\) for every \(Z\).
Hence \(G^{-1}\), and therefore \(G\), must be diagonal. For unit
orthogonal inputs the potential is \(F=\frac12\sum_{ia}\sinh^2Z_{ia}\).
This rules out that particular direct balance extension on nonorthogonal
data; it does not rule out a different invariant or a dynamical proof.
