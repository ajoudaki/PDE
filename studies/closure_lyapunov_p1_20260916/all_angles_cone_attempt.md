# Frozen analytical continuation: all-angle initialization of the cone

2026-09-16. This bounded continuation uses only the original assigned
canonical equations/initialization and this route's own frozen files.
No new route findings, other studies, experiments, or numerical constants
were read or used. Original files remain unchanged.

**Result.** For every distinct reflection-symmetric pair
u_+=(a,b), u_-=(a,-b), a>=0, b>0, a^2+b^2=1, the canonical p=1
initialization has strictly positive antisymmetric upper coefficient
B_2(0). For a>0 it also has B_1(0)>0 and strictly negative cross term
C_cross(0). Thus the cone's initialization is valid at every such angle,
not only near antipodality. Persistence of the cross-sign condition along
training remains open in this attempt. No counterexample on a reached
canonical trajectory is claimed.

These statements refer to the fixed coordinate axes of the p=1 dictionary.
Arbitrary rotations are not treated as dictionary symmetries. Unit opposite
labels, exact Gaussian populations, eta=1/4096, the actual matrix transpose,
and all trained closure coordinates are retained throughout.

## 1. Initialized effective lower scalar

Let g be standard Gaussian, zeta independently N(0,tau), and set

\[
 h=\tanh g,\quad p=\zeta+\alpha h,\quad y=\tanh p,
 \qquad
 v=E h^2,\quad \tau=E\tanh^2(\sqrt vG),\quad \alpha=1-\tau.
\]

Here G is standard Gaussian, and 0<v,tau,alpha<1. Write

\[
 k=E[hy],\quad \sigma=E[y^2],\quad
 \gamma=E\operatorname{sech}^2p>0,
 \quad R=\begin{pmatrix}v+\eta&k\\k&\sigma+\eta\end{pmatrix}.
\]

The exact initialization reduction in the frozen route gives the active
lower scalar k_init=m_0^T b as

\[
 k_{\rm init}
   =\frac{Ah+By}{\sqrt{\tau+\eta}},\qquad
 \begin{pmatrix}A\\B\end{pmatrix}
   =R^{-1}\begin{pmatrix}\alpha v\\\alpha k+\tau\gamma\end{pmatrix}.
                                                               \tag{1}
\]

This is just the raw-coordinate expression of the prescribed ridge and
Cholesky contraction. It is not a new fitted coefficient or an alternative
initialization. Neither A nor the individual realization k_init is assumed
positive. Independent reverse-action noise can make k_init and g have
opposite signs.

The useful statement is conditional:

**Lemma 1.** There is an explicit constant c_0>0 such that, for every g>0,

\[
 E[k_{\rm init}\mid g]\ge
          \frac{c_0}{\sqrt{\tau+\eta}}\tanh g>0,
 \qquad
 c_0=\alpha\left(\frac{v}{v+\eta}-\frac56\right)>0.       \tag{2}
\]

The conditional expectation is odd in g, so it has the strict sign of g
for every g!=0. This is enough for all the initialization signs below.

### Proof of Lemma 1

First, 0<B<=1/gamma. The regression equations in (1) give

\[
 B=\frac{\alpha k\eta+\tau\gamma(v+\eta)}{\Delta},\qquad
 A=\frac{\alpha v-Bk}{v+\eta},\quad
 \Delta=(v+\eta)(\sigma+\eta)-k^2>0.                    \tag{3}
\]

The covariance k is positive: conditional on h, E_zeta tanh(zeta+alpha h)
is an odd strictly increasing function of h. To bound B above, the
orthogonal L2 random variables h and zeta yield

\[
 \sigma\ge\frac{k^2}{v}+\tau\gamma^2.                   \tag{4}
\]

Indeed E[hy]=k, E[zeta y]=tau gamma by Gaussian integration by parts,
E[h zeta]=0, and expansion of
E[(y-(k/v)h-gamma zeta)^2]>=0 proves (4). All variables are integrable;
y and its zeta derivative are bounded, so the integration by parts is
justified.

It follows that

\[
 \begin{aligned}
 \Delta
 &\ge(v+\eta)\tau\gamma^2
         +\eta(k^2/v+v+\eta)\\
 &\ge(v+\eta)\tau\gamma^2+\alpha\gamma k\eta.
 \end{aligned}                                               \tag{5}
\]

The last step uses k^2/v+v>=2k and alpha gamma<1. Comparing (5) with
the numerator of B in (3) proves 0<B<=1/gamma.

Next define

\[
 G_0=E_\zeta\operatorname{sech}^2\zeta>0,\qquad
 F(h)=E_\zeta\tanh(\zeta+\alpha h).
\]

For 0<h<=1 we have

\[
             G_0\tanh\alpha\le\frac{F(h)}h\le\alpha G_0,
 \qquad       \gamma\ge G_0\operatorname{sech}^2\alpha.   \tag{6}
\]

Here are elementary derivations of all three bounds. If T=tanh zeta and
t>=0, pairing zeta and -zeta in the addition formula gives

\[
 E\tanh(\zeta+t)
  =\tanh t\ E\frac{1-T^2}{1-\tanh^2t\,T^2}
  \ge G_0\tanh t.
\]

Taking t=alpha h and using concavity of tanh on the positive half-line
gives tanh(alpha h)>=h tanh alpha, proving the lower bound for F/h.

For the upper bound let
J(t)=E sech^2(zeta+t). This is even and nonincreasing for t>=0.
To verify the latter property explicitly, let q_tau be the N(0,tau)
density. Differentiation under the bounded derivative gives, for t>0,

\[
 J'(t)=\int_0^\infty
 [-2\operatorname{sech}^2x\tanh x]
             [q_\tau(x-t)-q_\tau(x+t)]\,dx\le0.
\]

The first factor is negative and the second nonnegative. Thus
F(h)=integral_0^(alpha h) J(t)dt<=alpha h J(0)=alpha h G_0.

Finally, the addition formula for sech^2, followed by pairing zeta,
gives for every real t

\[
 J(t)=\operatorname{sech}^2t\ E\!\left[
 \operatorname{sech}^2\zeta\,
 \frac{1+T^2\tanh^2t}{(1-T^2\tanh^2t)^2}\right]
 \ge G_0\operatorname{sech}^2t.
\]

Since |alpha h|<=alpha, averaging this bound over h proves the last
inequality in (6).

By the upper bound in (6), k/(v+eta)<=k/v<=alpha G_0. Thus the
conditional numerator in (1) satisfies, for h>0,

\[
 \begin{aligned}
 \frac{Ah+BF(h)}h
 &=\frac{\alpha v}{v+\eta}
                  +B\left(\frac{F(h)}h-\frac{k}{v+\eta}\right)\\
 &\ge\frac{\alpha v}{v+\eta}
                         -\frac{G_0}{\gamma}(\alpha-\tanh\alpha)\\
 &\ge\frac{\alpha v}{v+\eta}
                         -(\alpha-\tanh\alpha)\cosh^2\alpha\\
 &\ge\alpha\left(\frac{v}{v+\eta}-\frac56\right)=c_0.
 \end{aligned}                                               \tag{7}
\]

For the final estimate, tanh alpha>=alpha-alpha^3/3 follows by
integrating sech^2 t=1-tanh^2 t>=1-t^2 from 0 to alpha. Also
0<alpha<1 and cosh^2(1)<5/2 give
(alpha-tanh alpha)cosh^2 alpha<=5alpha/6.

To check c_0>0 with no numerical integration, on the two intervals
1<=|g|<=2 one has tanh^2 g>1/4 and the Gaussian density is greater
than 1/24. Their total length is two, so v>1/48. These elementary
constants follow, for example, from e^2<8, sqrt(2pi)<3 and tanh1>1/2.
Consequently

\[
 \frac{v}{v+\eta}>\frac{256}{259}>\frac56
 \qquad(\eta=1/4096).
\]

The harmless bound cosh^2(1)<5/2 can likewise be checked from
2<e<11/4: e^2+e^(-2)<121/16+1/4<8. This completes (7), hence (2).
Oddness follows by simultaneously reversing g and zeta.

## 2. All-angle initial signal and strict cross sign

For each coordinate, let k_i=m_0^T b_i be the initialized scalar from
(1); the pairs (g_i,zeta_i) are independent copies. The initial plus-input
upper coefficient is

\[
 B_i(0)=E_1[k_i\tanh(a g_1+b g_2)].                     \tag{8}
\]

Let Q(g)=E[k_init|g]. By Lemma 1, Q is odd and strictly positive on
g>0. For example, define

\[
 J_2(t)=E_{g_1}\tanh(a g_1+bt).
\]

When b>0 this is odd and strictly increasing in t, with derivative
b E sech^2(a g_1+bt)>0. It therefore has the sign of t. Conditional
expectation in (8) gives

\[
                    B_2(0)=E[Q(g_2)J_2(g_2)]>0.       \tag{9}
\]

This includes a=0. Similarly, if a>0 then B_1(0)>0; if a=0 then
B_1(0)=0 by independence and zero mean. More generally the sign of
each initialized B_i for a single input is the sign of that input's
i-th coordinate, when the coordinate is nonzero.

For a,b>0 the cross term at initialization is

\[
 C_{\rm cross}(0)
 =E[Q(g_1)Q(g_2)\operatorname{sech}^4(a g_1+b g_2)]<0.  \tag{10}
\]

To see the strict sign, integrate the two Gaussian variables over their
four sign quadrants. If q is the standard normal density, the result is

\[
 2\int_0^\infty\!\!\int_0^\infty
 Q(x)Q(y)q(x)q(y)
 \{\operatorname{sech}^4(ax+by)
       -\operatorname{sech}^4(ax-by)\}\,dx\,dy.
\]

The prefactor is strictly positive and
|ax+by|>|ax-by| for x,y>0. Since sech^4 is strictly decreasing in
absolute value on the positive half-line, the brace is strictly negative.
All integrands are bounded and integrable. This proves (10).

In particular B_1(0) C_cross(0)<0 for every a,b>0. Characteristic
continuity preserves that strict inequality on some positive feature-time
interval for each fixed pair. No interval uniform up to input coincidence
is asserted. At the antipodal endpoint a=0, B_1=C_cross=0 and the
separate exact axis theorem applies.

## 3. What the attempted persistence calculation does and does not give

The frozen cross-sign note proves that, once B_2(0)>0 is known, the
single trajectory estimate

\[
                         B_1(s)C_{\rm cross}(s)\le0     \tag{11}
\]

would simultaneously give B_2(s)>=B_2(0), |B_1(s)|<=|B_1(0)|,
a uniform positive readout separation, exponential physical loss decay,
and full-state convergence. Lemma 1 and (9) discharge the previously
separate initialization premise for every distinct reflection pair.

I attempted the direct boundary-invariance calculation. Define
ell_i=a_i^T b_i, z=w dot u_+, and retain
S_+=sech^2 z, S_-=sech^2(w dot u_-). Exact differentiation gives

\[
 \begin{aligned}
 (C_{\rm cross})_s={}&
 d_1 E_1[\ell_1 k_2 S_+^2]
 +d_2 E_1[k_1\ell_2 S_+^2]\\
 &-2E_1\!\left[k_1k_2\tanh z\,S_+^2
 \{S_+(d_1k_1+d_2k_2)+\rho S_-(d_1k_1-d_2k_2)\}\right].
 \end{aligned}                                               \tag{12}
\]

Indeed (k_i)_s=d_i ell_i, the exact row equation gives
z_s=[S_+(d_1k_1+d_2k_2)+rho S_-(d_1k_1-d_2k_2)]/2, and
(sech^4 z)_s=-4 tanh z sech^4 z z_s. Substitution proves (12).

At a prospective boundary B_1>0, C_cross=0, the available upper signs
are d_1<=0 and d_2>=0. They do not assign signs to the distinct mixed
moments in (12). Their vanishing is not implied by C_cross=0, which
controls only one quadratic weighted moment. Likewise, positivity of
the tangent Gram matrix does not fix its cross entry. Thus this
calculation does not supply the inward-pointing condition needed to
propagate (11).

The specific initial proof cannot simply be repeated at later times:
initially the gate depends only on (g_1,g_2), so zeta_1,zeta_2 can be
integrated out to produce Q(g_1)Q(g_2). Later w depends on the reverse
marks, and this conditional factorization fails. Lemma 1 establishes
a conditional mean sign, not a pointwise sign of k_i relative to w_i.
Replacing the former by the latter would be an unjustified strengthening.

These observations expose a proof gap rather than disprove (11).
No sign violation or full-reflection-family convergence theorem was
established in this bounded attempt. The precise remaining obligation
for the cone route is a reached-state estimate controlling (12), or a
different argument establishing (11), or a canonical trajectory
counterexample that rejects this sufficient cone criterion. General
two-input arrangements additionally require a route that does not assume
coordinate-reflection symmetry; the p=1 dictionary cannot be rotated
without justification.

## Status

- Conditional initialized lower-field sign: proved in Lemma 1, with
  explicit constants and no quadrature.
- Positive initial antisymmetric coefficient at every nonzero
  reflection-pair separation: proved in (9).
- Strict initial cross-sign condition at every non-antipodal distinct
  reflection pair: proved in (10).
- Short-time persistence for each fixed such pair: follows from strictness
  and characteristic continuity, with no quantitative uniform duration.
- All-time cross-sign persistence and all-angle convergence by this route:
  open. Equation (12) identifies the remaining mixed-moment obstacle.
- No implication for a full-network limit, no experimental evidence, and
  no arbitrary-rotation symmetry claim is made.
