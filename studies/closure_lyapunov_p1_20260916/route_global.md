# Frozen route: an all-time cone theorem for the antipodal axis pair

Frozen candidate: 2026-09-16. Analytical work only; no numerical experiments.
This is a scoped independent route. Inputs are `docs/NOTATION.md` and the
assigned ranges of `docs/global_nonlinear.md`, in particular (H3.1),
(H3.N1)–(H3.N2), (H3.CS7)–(H3.CS9), and the fixed-order existence argument
in (H40.C9). Required research-contract and adversarial-audit references were
read. No other study or route was read.

## Contract and conclusion

The object is the exact canonical population closure at order p=1, with its
prescribed ridge eta=1/4096, Gaussian mark law, actual middle transpose,
zero initial population readout, unhalved probability-weighted square loss,
and physical training time. Both populations remain continuum populations.
There is no particle rule, time discretization, neural-width limit, or
replacement by a frozen-feature system.

For the balanced two-point law

\[
 \mu=\tfrac12\delta_{(e_1,+1)}+\tfrac12\delta_{(-e_1,-1)},
 \qquad u=x/\sqrt2,
\]

the exact initialized closure has exponential loss decay, converges to a
finite interpolating state, and has strictly moving middle and lower
features after time zero. The proof gives an explicit positive rate from
initialization. Coordinate exchange gives the same theorem for e_2.
The antipodal geometry collapses the training constraints to one scalar
constraint because the represented predictions are odd in input. This is a
substantive all-time closure theorem for that geometry, but does not settle
the non-antipodal, variable-separation question.

## Complete initialization reduction

Write

\[
 v=E\tanh^2G,\quad \tau=E\tanh^2(\sqrt vG),
 \quad \alpha=1-\tau,
 \qquad G\sim N(0,1).
\]

All are strictly positive. For i=1,2, let

\[
 h_i=\tanh g_i,\quad p_i=\zeta_i+\alpha h_i,
 \quad y_i=\tanh p_i,\quad \chi_i=(h_i,y_i)^T,
\]

where the pairs (g_i,zeta_i) are independent, g_i is standard Gaussian,
and zeta_i is Gaussian of variance tau. Put

\[
 k=E[h_iy_i],\quad \sigma=E[y_i^2],\quad
 S=\begin{pmatrix}v&k\\k&\sigma\end{pmatrix},\quad
 R=S+\eta I,
 \quad \ell\ell^T=R,
 \quad b_i=\ell^{-1}\chi_i\in\mathbb R^2.
\]

Here b_i denotes the two active lower mark coordinates belonging to axis i,
not a quadrature particle. The full lower Cholesky ordering is constant,
h_1,h_2,y_1,y_2. Its nonzero off-diagonal entries connect only h_i with y_i;
thus grouping the coordinates into the two displayed blocks reproduces the
same Cholesky whitening. The constant is (1+eta)^(-1/2). The two blocks are
independent and identically distributed, have zero mean, and change sign
under (g_i,zeta_i) -> (-g_i,-zeta_i). Also

\[
 E[b_ib_i^T]=I-\eta\ell^{-1}\ell^{-T}\le I.
\]

The upper nonconstant marks are

\[
 \beta_i=\frac{\tanh\xi_i}{\sqrt{\tau+\eta}},\qquad
 \xi_i\stackrel{\rm iid}{\sim}N(0,v),
\]

and its constant coordinate is again (1+eta)^(-1/2). The upper and lower
populations are distinct. Each beta_i has a symmetric distribution,
is bounded, and satisfies E beta_i^2=tau/(tau+eta)<1.

By (H3.1), the raw contraction from chi_i to the i-th upper feature is

\[
 (\alpha v,\;\alpha k+\tau\gamma),\qquad
 \gamma=E[1-y_i^2].
\]

It equals E[p_i chi_i]^T. Indeed E[p_i h_i]=alpha v, while integration by
parts in zeta_i gives
E[p_i y_i]=alpha k+tau E sech^2(p_i). The bounded integrand and bounded
derivative justify that integration by parts. Every cross-axis contraction
and every contraction involving a constant is zero by independence and
sign symmetry. Thus the initialized middle matrix has two identical rows
on the corresponding lower blocks, with column-vector notation

\[
 m_0=\frac{\ell^{-1}E[\chi_i p_i]}{\sqrt{\tau+\eta}}.
\]

The initial active lower contraction for e_1 is

\[
 a_0=E[b_1h_1]=\ell^{-1}(v,k)^T,
 \qquad B_0=m_0^Ta_0.
\]

Crucially, B_0>0. To prove this without assuming a sign for the whitened
features, observe first k>0: for a nonzero h, the conditional expectation
E_zeta tanh(zeta+alpha h) has the sign of h, because it is odd and strictly
increasing. Write j=E[p_i tanh p_i]>0 and
Delta=(v+eta)(sigma+eta)-k^2>0. Then

\[
 B_0=\frac{(\alpha v,j)R^{-1}(v,k)^T}{\sqrt{\tau+\eta}}
 =\frac{\alpha v\,[v(\sigma+\eta)-k^2]+j\eta k}
 {\sqrt{\tau+\eta}\,\Delta}>0.                 \tag{1}
\]

Cauchy–Schwarz gives v sigma-k^2>=0, so the first bracket is at least
v eta>0. Thus strict positivity does not depend on a small-ridge limit or
a numerically determined rank.

## Exact invariant subsystem

For the antipodal law the two data contributions agree after oddness of
tanh is used. On e_1, set

\[
 z=w\cdot e_1,\quad a=E_1[b_1\tanh z],\quad
 B=m^Ta,\quad H(\beta)=\tanh(\beta B),
\]
\[
 f=E_2[cH],\quad e=1-f,\quad
 d=E_2[\beta c\operatorname{sech}^2(\beta B)],\quad
 k_m=m^Tb_1.
\]

The scalar upper mark beta here is beta_1. The exact restricted equations
in physical time are

\[
 \dot z=2e\,d\,k_m\operatorname{sech}^2z,\qquad
 \dot m=2e\,d\,a,\qquad
 \dot c(\beta)=2e\,\tanh(\beta B).             \tag{2}
\]

Initially z=g_1, m=m_0 and c=0. The second row coordinate stays w_2=g_2;
the second middle block stays equal to its initialized value m_0. Neither
enters the e_1 prediction.

For completeness, this is an invariant subsystem of the full closure,
not an imposed model change. The function z depends only on the first
lower mark pair and is odd under its sign reversal. Therefore the lower
constant contraction is zero, and the second lower-block contraction is
zero by independence and zero mean. The readout depends only on beta_1 and
is odd in it. Its backward contraction has zero constant and beta_2
coordinates. Consequently the full matrix velocity has only its first
upper-row/first-lower-block entries, and the full row velocity has only
its e_1 component. Every asserted dependence and parity is preserved by
(2). The initial state satisfies them. The fixed-order characteristic
uniqueness in the assigned sources identifies this subsystem with the
full canonical closure. The global finite-time bounds in (H40.C9)
ensure its continuation through each finite physical time.

## Theorem and proof

Define the explicit initialized readout rate

\[
 \kappa=E_2\tanh^2(\beta B_0)>0.                         \tag{3}
\]

Then for every t>=0 the canonical population closure satisfies

\[
 0<1-f(t)\le e^{-2\kappa t},\qquad
 \mathcal L(t)=(1-f(t))^2\le e^{-4\kappa t}.              \tag{4}
\]

Moreover, w-g and c converge in their population supremum norms and M
converges in Frobenius norm to a finite state that interpolates both data
points. Their errors are bounded by constants times exp(-2 kappa t).

The proof has three steps: the residual remains positive at finite times;
the common scalar upper coefficient B cannot decrease; and its initial
positive size supplies a uniform readout-kernel lower bound.

First, differentiation in the population gradient metric gives

\[
 \dot f=2e K,\qquad
 K=E_2H^2+d^2\left(|a|^2+E_1[k_m^2\operatorname{sech}^4z]\right)\ge0.
                                                               \tag{5}
\]

This also follows directly by differentiating (2): the three terms are
the readout, middle and lower-row squared gradient norms. All derivatives
and expectations are justified on every compact physical interval by
bounded marks and the characteristic bounds. Hence

\[
 e(t)=\exp\!\left(-2\int_0^tK(s)\,ds\right)>0
\]

at every finite t. Introduce feature time s(t)=2 integral_0^t e(tau)d tau.
It is strictly increasing at finite times and changes no optimizer. In
this coordinate,

\[
 z_s=d k_m\operatorname{sech}^2z,\quad m_s=d a,\quad
 c_s=H,\quad
 a_s=d E_1[b_1b_1^T\operatorname{sech}^4z]m,
\]
\[
 B_s=d\left(|a|^2+E_1[k_m^2\operatorname{sech}^4z]\right).       \tag{6}
\]

On any interval on which B>0,

\[
 c(s,\beta)=\int_0^s\tanh(\beta B(\sigma))\,d\sigma
\]

has the sign of beta for s>0 and beta!=0. Therefore d>=0, and (6) makes
B nondecreasing there. Since B_0>0, a first-exit argument gives
B(s)>=B_0 on the entire reached feature-time interval: a first value
B<=0 is impossible for a function nondecreasing up to that value.
In fact d>0 for s>0 because beta has no atom at zero and every finite
sech^2 gate is positive.

Since |tanh(beta B)| is nondecreasing in B>=0, (5) now gives
K>=E tanh^2(beta B_0)=kappa. Inserting this into the exact residual
formula proves (4).

It remains to prove convergence of the state rather than only its
predictions. Formula (4) gives

\[
 s_\infty:=\lim_{t\to\infty}s(t)\le\kappa^{-1},\qquad
 s_\infty-s(t)\le\kappa^{-1}e^{-2\kappa t}.             \tag{7}
\]

In feature time, |c(s,beta)|<=s. Also |a|<=1 and |d|<=s, since both
mark synthesis maps are L2 contractions. Consequently

\[
 |m(s)-m_0|\le s^2/2,\quad
 \|z_s\|_\infty\le s\,B_1(|m_0|+s^2/2),
 \qquad B_1=\operatorname*{ess\,sup}|b_1|<\infty.
\]

The three feature-time derivatives are therefore uniformly bounded on
0<=s<s_infty. They have respective bounds

\[
 V_z=\frac{B_1}{\kappa}\left(|m_0|+\frac1{2\kappa^2}\right),
 \qquad V_m=\kappa^{-1},\qquad V_c=1.
\]

Each field is Cauchy as s approaches s_infty. The limits belong to the
same characteristic state space and, by (7),

\[
 \|z(t)-z_\infty\|_\infty+|m(t)-m_\infty|
 +\|c(t)-c_\infty\|_\infty
 \le\frac{V_z+V_m+V_c}{\kappa}e^{-2\kappa t}.             \tag{8}
\]

The unchanged coordinates add no error. Bounded gates make prediction
continuous in these norms; (4) therefore gives f_infty(e_1)=1 and,
by input oddness, f_infty(-e_1)=-1. This proves the theorem.

The dynamics are not frozen. For every s>0, d>0 and B>=B_0>0 imply a!=0,
so m_s=d a!=0 and B_s>0. Furthermore S is positive definite: a relation
A h+B y=0 almost surely would, after fixing almost every g and varying
the independent nondegenerate zeta, force B=0 and then A=0. Hence the
whitened b covariance is positive definite. Since m!=0,
E k_m^2>0; positivity of sech^4z then implies ||z_s||_2>0. Thus both
middle and lower-layer features move at every positive finite time.

## Exact obstruction to the same proof at variable separation

Consider the reflection-symmetric pair

\[
 u_+=(a,b),\quad u_-=(a,-b),\quad a,b>0,\quad a^2+b^2=1,
 \qquad y_+=1,\quad y_-=-1,
 \quad \rho=u_+\cdot u_-=a^2-b^2.
\]

The law is balanced. Reflecting the second lower mark pair and beta_2,
together with reflecting the input, proves by uniqueness that
f(u_-)=-f(u_+), M remains block diagonal, and c is even in beta_1 and odd
in beta_2. This uses the p=1 coordinate-reflection symmetry; arbitrary
rotations of this finite dictionary are not assumed.

For the plus input write a_i=E[b_i tanh(w dot u_+)],
k_i=m_i^T b_i, B_i=m_i^Ta_i, and

\[
 Z_+=\beta_1B_1+\beta_2B_2,\qquad
 Z_-=\beta_1B_1-\beta_2B_2,
\quad d_i=E[\beta_i c\operatorname{sech}^2Z_+].
\]

With the same feature clock s'=2(1-f(u_+)), the exact equations include

\[
 (m_i)_s=d_i a_i,\qquad
 c_s=\tfrac12[\tanh Z_+-\tanh Z_-].                     \tag{9}
\]

Put S_+=sech^2(w dot u_+) and S_-=sech^2(w dot u_-). The lower equation is

\[
 w_s=\tfrac12\{S_+(d_1k_1+d_2k_2)u_+
                   +S_-(d_1k_1-d_2k_2)u_-\}.
\]

The second-block signal therefore obeys the exact identity

\[
 (B_2)_s=d_2|a_2|^2+\tfrac12d_1 C+\tfrac12d_2 T_2,\quad
 C=E[k_1k_2 S_+^2],\quad
 T_2=E[k_2^2(S_+^2-\rho S_+S_-)]\ge0.                  \tag{10}
\]

To verify it, differentiate a_2 and use the displayed w_s; the term
E[b_2 k_1 S_+S_-] vanishes under second-mark reflection. The same
reflection gives E[k_2^2 S_+^2]=E[k_2^2 S_-^2], and therefore

\[
 T_2=\tfrac12 E[k_2^2\{(S_+-S_-)^2
                              +2(1-\rho)S_+S_-\}]\ge0.
\]

As long as B_2>0 along the preceding trajectory, (9) makes beta_2 c>=0,
strictly positive away from beta_2=0 at positive s. Hence d_2>0.
Pairing beta_1 with -beta_1 additionally gives d_1 B_1<=0: the difference
of the two sech^2 gates has sign opposite to beta_1 beta_2 B_1 B_2,
and c has the sign of beta_2. In particular B_1=0 implies d_1=0.

The missing estimate for extending this cone mechanism is

\[
                       B_1(t)\,C(t)\le0.               \tag{11}
\]

Together with the upper sign relation this would make d_1 C>=0 and
preserve B_2 by (10). The middle/lower tangent matrix being positive
semidefinite does not supply the sign of its off-diagonal entry C.
Moreover the initial lower marks contain the independent reverse-action
Gaussian zeta_i, so a pointwise assumption that k_i has the sign of w_i
is not a permissible consequence of canonical initialization. No proof
of (11), no counterexample to (11) on the reached canonical trajectory,
and no general variable-separation convergence theorem is claimed here.

Even a proof of (11) would need a separate uniform readout-mode estimate:
growth of B_2 alone does not bound the difference
tanh(beta_1 B_1+beta_2 B_2)-tanh(beta_1 B_1-beta_2 B_2) away from zero
if an uncontrolled common coefficient |B_1| diverges. The antipodal
axis proof avoids that issue because the common coefficient is exactly zero.

## Evidence status and hostile audit

- Exact initialization reduction, invariant subsystem, cone preservation,
  exponential loss estimate, and state convergence: proved above for the
  antipodal coordinate-axis pair, internally checked and not independently
  reviewed or promoted.
- Exact variable-separation identity (10): proved above, with both
  population expectations and the actual transpose retained.
- General variable-separation convergence: open. The explicit missing
  lower-feature sign estimate is (11), followed by control of the common
  upper coefficient.
- No accuracy claim about the order-one closure versus the full neural
  population trajectory follows from this all-time optimization theorem.
- The strongest scope objection is geometry: antipodal odd-label data
  impose only one independent fitting constraint. The theorem does not
  erase that restriction. Its nontrivial content is the all-time behavior
  of the fully evolving canonical closure at ordinary label amplitude,
  including uniform dissipation and convergence of the trained fields.
- No numerical artifact, time mesh, particle population, selected random
  seed, or limit exchange enters the argument.
