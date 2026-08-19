# Independent analytic derivation of the \(L=2,B=1\) coefficient

**Status:** independently derived and atomwise-canonicalized closed form;
the fixed-program joint-limit and annealed bridge are theorem-certified under
the polynomially-smooth activation envelope  
**Date:** 2026-08-18

This note preserves the grouping of an analytic tangent-field derivation that
was obtained independently of `L2_B1_GAUSSIAN_NORMAL_FORM.md`.  It gives a
literal one-dimensional Gaussian normal form for

\[
C=\lim_{n\to\infty}\mathbb E[D_n^3f_n]
\]

and records exactly where a probabilistic leading-width argument enters.

## 1. Model and the effective first-layer metric

Write

\[
u_j=\frac{w_j^\top x}{\sqrt{d_0}},\qquad
x_j=\phi(u_j),\qquad
z_i=\frac1{\sqrt n}\sum_jW_{ij}x_j,
\]

\[
y_i=\phi(z_i),\qquad
f_n=\frac1n\sum_i a_i y_i,\qquad
q=\frac{\|x\|^2}{d_0}.
\]

All entries of \(w,W,a\) are independent standard Gaussians.  For any two
functions of the one-input coordinates,

\[
\sum_{r=1}^{d_0}
\frac{\partial A}{\partial w_{jr}}
\frac{\partial B}{\partial w_{jr}}
=q\frac{\partial A}{\partial u_j}
\frac{\partial B}{\partial u_j}.
\tag{1.1}
\]

Thus the raw feature-ascent derivation is exactly

\[
D_nA=n\left(
\sum_i\partial_{a_i}f_n\,\partial_{a_i}A
+\sum_{ij}\partial_{W_{ij}}f_n\,\partial_{W_{ij}}A
+q\sum_j\partial_{u_j}f_n\,\partial_{u_j}A
\right).
\tag{1.2}
\]

Equivalently, \(u_j=\sqrt q\,v_j\) with \(v_j\sim N(0,1)\) whitens the last
metric block.  This is the origin of every explicit power of \(q\) below.

## 2. Exact finite-width cubic skeleton

Let \(M\) be the constant metric in (1.2), let
\(V=nM\nabla f_n\), and let \(H,T\) be the raw-coordinate Hessian and third
derivative tensor of \(f_n\).  Direct differentiation gives the exact identity

\[
D_n^3f_n=2T[V,V,V]+4\,n(HV)^\top M(HV).
\tag{2.1}
\]

Indeed, \(D_nf_n=\nabla f_n\cdot V\),
\(D_n^2f_n=2H[V,V]\), and
\(D_nV=nMHV\).  Define

\[
\mathcal T_n=T[V,V,V],\qquad
\mathcal H_n=n(HV)^\top M(HV).
\tag{2.2}
\]

If \(V'=D_nV\), then another exact expression is

\[
\mathcal H_n=\frac1n(V')^\top M^{-1}V'.
\tag{2.3}
\]

Equations (2.1)--(2.3) fix all factors of \(n,2,4\) before any limit is
taken.

Put \(\varepsilon=n^{-1/2}\), and use primes for derivatives of \(\phi\).
The exact vector field at initialization is

\[
\dot a_i=y_i,\qquad
\dot W_{ij}=\varepsilon a_i y_i'x_j,\qquad
\dot u_j=q x_j'g_j,
\tag{2.4}
\]

where

\[
g_j=\varepsilon\sum_iW_{ij}a_i y_i'.
\tag{2.5}
\]

Let \(v_i=D_nz_i\).  For the frozen-direction derivatives used in
\(\mathcal T_n\), write \(s_i=\delta^2z_i\) and
\(t_i=\delta^3z_i\), where \(\delta\theta=V(\theta_0)\) and
\(\delta V=0\).  Product and chain rules give, still exactly,

\[
v_i=\varepsilon\sum_j
(\dot W_{ij}x_j+W_{ij}x_j'\dot u_j),
\tag{2.6}
\]

\[
s_i=\varepsilon\sum_j
(2\dot W_{ij}x_j'\dot u_j+W_{ij}x_j''\dot u_j^2),
\tag{2.7}
\]

\[
t_i=\varepsilon\sum_j
(3\dot W_{ij}x_j''\dot u_j^2+W_{ij}x_j'''\dot u_j^3).
\tag{2.8}
\]

Consequently,

\[
\mathcal T_n=\frac1n\sum_i\left\{
a_i\big(y_i'''v_i^3+3y_i''v_is_i+y_i't_i\big)
+3y_i\big(y_i''v_i^2+y_i's_i\big)
\right\}.
\tag{2.9}
\]

For the Hessian-square term, differentiating the actual vector field gives

\[
\ddot a_i=y_i'v_i,
\tag{2.10}
\]

\[
\ddot W_{ij}=\varepsilon\left[
x_j(y_i y_i'+a_i y_i''v_i)
+q a_i y_i'x_j'^2g_j
\right],
\tag{2.11}
\]

\[
\ddot u_j=q\left(qx_j''x_j'g_j^2+x_j'\dot g_j\right),
\tag{2.12}
\]

and therefore

\[
\mathcal H_n=\frac1n\left(
\sum_i\ddot a_i^2+\sum_{ij}\ddot W_{ij}^2
+\frac1q\sum_j\ddot u_j^2
\right).
\tag{2.13}
\]

This finite-width scalarization does not use parity to discard any term.

## 3. Literal Gaussian atom dictionary

Let

\[
U\sim N(0,q),\qquad
Q=\mathbb E[\phi(U)^2],\qquad
Z\sim N(0,Q).
\tag{3.1}
\]

Every expectation below is therefore an atom of dimension one, with covariance
matrix respectively \([q]\) or \([Q]\).  There are no implicit random fields
in the final answer.

The inner-layer atoms are

\[
\begin{aligned}
d&=\mathbb E[\phi'(U)^2],
&r_4&=\mathbb E[\phi'(U)^4],\\
m&=\mathbb E[\phi(U)\phi''(U)\phi'(U)^2],
&\ell&=\mathbb E[\phi'''(U)\phi'(U)^3],\\
s&=\mathbb E[\phi''(U)^2\phi'(U)^2],
&e&=\mathbb E[\phi(U)^2\phi'(U)^2].
\end{aligned}
\tag{3.2}
\]

The outer-layer atoms are

\[
\begin{aligned}
D&=\mathbb E[\phi'(Z)^2],\\
S_0&=\mathbb E[\phi'(Z)^2+\phi(Z)\phi''(Z)],\\
S_1&=\mathbb E[\phi''(Z)^2+\phi'(Z)\phi'''(Z)],\\
P_1&=\mathbb E[\phi(Z)\phi''(Z)\phi'(Z)^2],\\
P_2&=\mathbb E[\phi(Z)\phi''(Z)],\\
P_3&=\mathbb E[\phi'''(Z)\phi'(Z)^3],\\
P_4&=\mathbb E[\phi'''(Z)\phi'(Z)],\\
R&=\mathbb E[\phi'(Z)^4],\\
E_0&=\mathbb E[\phi(Z)^2\phi'(Z)^2],\\
E_{12}&=\mathbb E[\phi'(Z)^2\phi''(Z)^2],\\
E_2&=\mathbb E[\phi''(Z)^2].
\end{aligned}
\tag{3.3}
\]

Define five derived deterministic scalars

\[
\alpha=Q+qd,\qquad
\nu=q^2r_4D,\qquad
\kappa=q^2Dm,
\tag{3.4}
\]

\[
\beta=E_0+2\alpha P_1+3\alpha^2E_{12}+\nu E_2,
\qquad
\chi=D+S_0+\alpha S_1.
\tag{3.5}
\]

All symbols on the right sides of (3.4)--(3.5) are the explicit atoms in
(3.1)--(3.3).

## 4. Leading tangent-field peel

The following identities explain, independently, every grouping in the final
polynomial.

For a representative row, the diagonal response and the bulk column sum in
(2.6) give

\[
v\ \Longrightarrow\ \alpha\,\mathsf a\,\phi'(Z)+\xi,
\qquad
\mathsf a\sim N(0,1),\quad \xi\sim N(0,\nu),
\tag{4.1}
\]

with \(\mathsf a,Z,\xi\) mutually independent.  The two deterministic pieces
of \(\alpha\) are the direct middle-weight contribution \(Q\) and the
same-row first-layer response \(qd\).  The leave-one-row fluctuation has
variance \(q^2r_4D=\nu\).

The second frozen derivative in (2.7) is needed only through its response
against a smooth test function \(F\).  The leading contraction is

\[
\lim_{n\to\infty}\mathbb E[s_iF(z_i)]
=\kappa\,\mathbb E[F'(Z)],
\qquad \kappa=q^2Dm.
\tag{4.2}
\]

It is the covariance between the row sum
\(q^2n^{-1/2}\sum_jW_{ij}\phi''(u_j)\phi'(u_j)^2g_j^2\)
and \(z_i\).  The first term of (2.7) has strictly lower global width degree.

In (2.8), the explicit middle-weight hit and the self-row term inside
\(g_j^3\) give

\[
t_i=3D(q^2m+q^3\ell)\,a_i\phi'(z_i)
+\text{a centered term orthogonal to the required readout contraction}
+o_{L^1}(1).
\tag{4.3}
\]

For a representative column, differentiating (2.5) and peeling its
distinguished row gives

\[
\dot g\ \Longrightarrow\ \chi\phi(U)+\eta,
\qquad \eta\sim N(0,\beta),
\tag{4.4}
\]

where \(\eta\) is asymptotically independent of \(U\) and of
\(g\sim N(0,D)\).  To see the response coefficient, put

\[
B(Z,\mathsf a,\xi)
=\phi(Z)\phi'(Z)
+\mathsf a\phi''(Z)
\big(\alpha\mathsf a\phi'(Z)+\xi\big).
\tag{4.5}
\]

The direct derivative of \(W_{ij}\) contributes \(D\phi(U)\), while the
Gaussian response of \(W_{ij}B_i\) contributes

\[
\mathbb E[\partial_ZB]=S_0+\alpha S_1.
\tag{4.6}
\]

Moreover,

\[
\mathbb E[B^2]
=E_0+2\alpha P_1+3\alpha^2E_{12}+\nu E_2=\beta,
\tag{4.7}
\]

because \(\mathbb E\mathsf a^4=3\).  Finally
\(\mathbb E[B\,\mathsf a\phi'(Z)]=0\), which is the zero covariance between
\(\eta\) and \(g\) in (4.4).

Equations (4.1)--(4.7) are the only probabilistic leading-width inputs to the
remaining algebra.  Their joint validity for the exact finite program is
proved in `PEELING_AND_PROBABILITY_LEDGER.md` via the unrestricted-transpose
master theorem.

## 5. Cubic directional contraction

Substituting (4.1)--(4.3) into the exact expression (2.9), and using

\[
\mathbb E[\mathsf a v\mid Z]=\alpha\phi'(Z),
\]

\[
\mathbb E[v^2\mid Z]=\alpha^2\phi'(Z)^2+\nu,
\]

\[
\mathbb E[\mathsf a v^3\mid Z]
=3\alpha^3\phi'(Z)^3+3\alpha\nu\phi'(Z),
\tag{5.1}
\]

as well as (4.2), gives

\[
\lim_{n\to\infty}\mathbb E\mathcal T_n=3\mathcal T_*,
\tag{5.2}
\]

where

\[
\boxed{
\begin{aligned}
\mathcal T_*={}&
\alpha^2P_1+\nu P_2+\kappa S_0
+\alpha^3P_3+\alpha\nu P_4+\alpha\kappa S_1\\
&+D^2(q^2m+q^3\ell).
\end{aligned}}
\tag{5.3}
\]

For example, the three terms containing \(s_i\) reduce to Gaussian
integration by parts in the form
\(\mathbb E[sF(Z)]=\kappa\mathbb E F'(Z)\); this produces
\(\kappa S_0\) and \(\alpha\kappa S_1\), with no unevaluated Stein derivative
left in (5.3).

## 6. Hessian-square contraction

The readout block of (2.13) gives

\[
\lim\frac1n\sum_i\mathbb E\ddot a_i^2
=\alpha^2R+\nu D.
\tag{6.1}
\]

The middle-weight block, using (4.5)--(4.7), gives

\[
\lim\frac1n\sum_{ij}\mathbb E\ddot W_{ij}^2
=Q\beta+\nu D.
\tag{6.2}
\]

For the first-layer block, use
\(g\sim N(0,D)\), so \(\mathbb E g^4=3D^2\), and substitute (4.4) into
(2.12).  This yields

\[
\lim\frac1{nq}\sum_j\mathbb E\ddot u_j^2
=q\left(
3q^2D^2s+\chi^2e+\beta d+2qD\chi m
\right).
\tag{6.3}
\]

Combining the three parameter blocks,

\[
\lim_{n\to\infty}\mathbb E\mathcal H_n=\mathcal H_*,
\tag{6.4}
\]

with

\[
\boxed{
\mathcal H_*=
\alpha^2R+2\nu D+Q\beta
+q\left(
3q^2D^2s+\chi^2e+\beta d+2qD\chi m
\right).}
\tag{6.5}
\]

## 7. Closed Gaussian normal form

Equations (2.1), (5.2), and (6.4) give the coefficient

\[
\boxed{C=6\mathcal T_*+4\mathcal H_*.}
\tag{7.1}
\]

This is a finite polynomial in the one-dimensional Gaussian atoms
(3.1)--(3.3); it contains no neuron index, random weight, empirical
covariance, tangent variable, response variable, or unevaluated limit.

For comparison, the initialization NTK coefficient is

\[
\boxed{
A=Q_2+\alpha D,
\qquad Q_2=\mathbb E[\phi(Z)^2].}
\tag{7.2}
\]

Provided \(A>0\), the first scalar Stieltjes coefficient (always a
well-defined first nonlinear feature coefficient, but not necessarily a
nonnegative Stieltjes moment) and the first feature-dependent loss term are
therefore

\[
\mu_0=\frac{C}{2A^2},
\tag{7.3}
\]

\[
L(t)=1-4\eta At+8\eta^2A^2t^2
-\left(\frac{32}{3}\eta^3A^3+\frac83\eta^3C\right)t^3+O(t^4),
\tag{7.4}
\]

The concentration and uniform-integrability conditions needed to pass from
the finite-width loss identities to their deterministic annealed limits are
discharged for polynomially-smooth activations by the fixed-program \(L^p\)
theorem cited in Section 9.

## 8. Exact and independently solvable controls

### Constant activation

If \(\phi\equiv c\), every derivative atom vanishes.  Thus
\(A=c^2\) and \(C=0\), as required for readout-only training.

### Linear activation

For \(\phi(x)=x\),

\[
Q=q,\quad d=r_4=D=R=1,\quad e=E_0=q,
\]

all atoms involving \(\phi''\) or \(\phi'''\) vanish, and

\[
\alpha=2q,\quad \nu=q^2,\quad \beta=q,\quad \chi=2.
\]

Hence

\[
\mathcal T_*=0,\qquad \mathcal H_*=12q^2,
\qquad \boxed{C=48q^2}.
\tag{8.1}
\]

At \(q=1\), direct finite-width polynomial differentiation and Gaussian Wick
evaluation give

\[
\mathbb E[D_n^3f_n]=48+\frac{60}{n},
\tag{8.2}
\]

which independently confirms the limit and its normalization.

### Affine activation

For \(\phi(x)=x+b\) and \(q=1\), (7.1) reduces to

\[
\boxed{C=48+52b^2+12b^4.}
\tag{8.3}
\]

Direct finite-width polynomial/Wick enumeration gives the stronger identity

\[
\mathbb E[D_n^3f_n]
=48+52b^2+12b^4+\frac{60+64b^2}{n}.
\tag{8.4}
\]

In particular, \(b=1\) gives \(C=112\).

### Canonical quadratic activation

For \(\phi(x)=x^2\) and \(q=1\), the atom values are

\[
\begin{gathered}
Q=3,\ d=4,\ r_4=48,\ m=24,\ \ell=0,\ s=16,\ e=60,\\
D=12,\ S_0=18,\ S_1=4,\ P_1=216,\ P_2=6,
\ P_3=P_4=0,\\
R=432,\ E_0=1620,\ E_{12}=48,\ E_2=4.
\end{gathered}
\]

They give

\[
\alpha=7,\quad \nu=576,\quad \kappa=288,
\quad\beta=14004,\quad\chi=58,
\]

\[
\mathcal T_*=30744,\qquad
\mathcal H_*=375180,
\]

and hence

\[
\boxed{C=6(30744)+4(375180)=1\,685\,184.}
\tag{8.5}
\]

Also \(Q_2=27\), so \(A=27+7(12)=111\) and

\[
\mu_0=\frac{1\,685\,184}{2(111)^2}
=\frac{280864}{4107}.
\tag{8.6}
\]

These are exactly the accepted quadratic-compiler values.

## 9. Probabilistic certification

The separately generated atom normal form in
`L2_B1_GAUSSIAN_NORMAL_FORM.md` canonicalizes term by term to (7.1), not only
after numerical substitution.  In that note's notation the exact map is

\[
c_{\rm there}=\alpha,\qquad
\tau_{\rm there}=\beta,\qquad
\alpha_{\rm there}=S_0+\alpha S_1,
\]

\[
k_{\rm there}=\chi,\qquad
\kappa_{\rm there}=3D(q^2m+q^3\ell),
\]

and its straight-line contraction is \(S_{\star,{\rm there}}=3\mathcal T_*\),
while its Hessian contraction is exactly \(H_{\star,{\rm there}}=\mathcal
H_*\).  This discharges the algebraic canonicalization comparison.

The algebra from (2.1) through (2.13), and the reduction from the atom
dictionary to (7.1), are exact.  The formerly open joint leading-width
statements (4.1)--(4.4) are now certified by the exact Tensor Program and
response ledger in `PEELING_AND_PROBABILITY_LEDGER.md`.  In particular, that
proof covers:

1. the leave-one-row bulk fluctuation in (4.1);
2. the covariance response (4.2), including proof that the other branch of
   (2.7) is globally subleading;
3. the self-row contribution of \(g_j^3\) in (4.3);
4. the simultaneous response and fluctuation decomposition (4.4), including
   covariance replacement for \(\beta\);
5. almost-sure convergence of the scalar itself, without a separate
   multi-copy argument.

The constant, linear, affine, quadratic, activation-scaling, and numerical
smooth-activation controls, together with the completed algebraic
canonicalization, remain independent falsification tests.  Tensor Programs
III, Theorem E.15 supplies the joint Gaussian/Onsager and empirical-moment
limit.  For polynomially-smooth \(\phi\), Non-Gaussian Tensor Programs,
Theorem 3.7 additionally gives almost-sure and \(L^p\) convergence for every
finite \(p\), hence uniform integrability and \(\mathbb EC_n\to C\).

If only \(\phi^{(0)},\ldots,\phi^{(3)}\) are assumed polynomially controlled,
the almost-sure theorem remains available under pseudo-Lipschitz regularity,
but the annealed conclusion needs the separate tail condition recorded in
Section 8.3 of the peeling ledger.
