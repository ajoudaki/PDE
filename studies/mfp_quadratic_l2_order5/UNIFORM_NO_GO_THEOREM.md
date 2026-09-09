# Uniform nonzero-step obstruction for a quadratic activation

## Theorem

Let

\[
 \psi(x)=p x+q x^2,\qquad p^2+3q^2=1,
\]

and consider the established width-first, two-hidden-layer, one-input
feature/output-ascent network.  Write

\[
 \Delta_t(h)=F_{2t}(h)-F_t(2h).
\]

If \(q\ne0\), then for every \(\rho>0\),

\[
 \Delta_t(\rho/t)\longrightarrow+\infty .
\]

Consequently, if \(\kappa_t=[h^3]\Delta_t(h)\), then

\[
 \sup_{t\ge1}\ \sup_{0<h\le \rho/t}
 \frac{|\Delta_t(h)-\kappa_t h^3|}{t^4h^5}=\infty .
\]

In fact the same conclusion holds with \(t^4\) replaced by any fixed
polynomial in \(t\).  Thus no fixed nonzero quadratic perturbation of the
identity has the sought horizon-uniform fifth remainder on any positive
total-time interval.

## 1. Exact finite-width setup

At width \(n\), put

\[
 H_j=\psi(u_j),\qquad
 z_i=n^{-1/2}\sum_jW_{ij}H_j,\qquad
 f_n=n^{-1}\sum_i a_i\psi(z_i),
\]

with all \(a_i,u_j,W_{ij}\) independent standard Gaussians at
initialization.  One ascent step is \(\theta^+=\theta+hn\nabla f_n(\theta)\),
or, with \(C_i=a_i\psi'(z_i)\) and
\(b_j=n^{-1/2}\sum_iW_{ij}C_i\),

\[
\begin{aligned}
 a_i^+&=a_i+h\psi(z_i),\\
 W_{ij}^+&=W_{ij}+\frac h{\sqrt n}C_iH_j,\\
 u_j^+&=u_j+h b_j\psi'(u_j).
\end{aligned}
\]

The width-first output is

\[
 F_N(h)=\lim_{n\to\infty}\mathbb E f_n(\theta_N)
\]

at fixed \((N,h)\), as in the established OMFP construction.

The earlier linear-growth bridge does not by itself cover this activation.
For completeness, the quadratic bridge is closed separately in
`FIXED_H_QUADRATIC_WIDTH_LEMMA.md`: the exact identity

\[
 W^s=W^0+\frac h{\sqrt n}\sum_{r<s}C^r(H^r)^T
\]

rewrites every trained action using the finite list
\(W^0H^0,(W^0)^TC^0,\ldots,W^0H^N\), coordinatewise polynomials, and
empirical moments.  The established polynomially-smooth finite-program
theorem then gives almost-sure and every-finite-\(L^r\) convergence at each
fixed \((N,h)\), hence convergence of expectations.  This invocation is
pointwise in \(N\); it supplies no time-uniform estimate.

## 2. Positive-polynomial step-doubling lemma

Let \(\mathbb R_+[x_1,\ldots,x_d,h]\) be ordered coefficientwise.  Suppose
that a polynomial vector field \(g\) and a polynomial observable \(O\) have
nonnegative coefficients.  Put \(E_h(x)=x+hg(x)\).  Then

\[
 O(E_h^{2t}x)-O(E_{2h}^t x)
\]

has nonnegative coefficients.

Indeed, with \(A=E_h\circ E_h\) and \(B=E_{2h}\),

\[
 A(x)=B(x)+L(x),\qquad
 L(x)=h\{g(x+hg(x))-g(x)\}.
\]

For each monomial \(c x^\nu\) of \(g\),

\[
 c\left\{\prod_j(x_j+hg_j(x))^{\nu_j}-x^\nu\right\}
\]

is the sum of the terms in the product expansion which use at least one
\(hg_j\), so it has nonnegative coefficients.  Hence \(L\succeq0\) and
\(A\succeq B\).  Composition by a positive polynomial preserves this
order.  Therefore \(A^t\succeq B^t\), and composition by \(O\) proves the
claim.

The construction is also monotone under deletion of vector-field
monomials.  More precisely, write \(g_\lambda=g_0+\lambda g_1\), where
both fields are positive.  In the preceding product expansion \(L_\lambda\)
has nonnegative coefficients jointly in \((x,h,\lambda)\).  Inductively,
if \(A_\lambda^s=B_\lambda^s+R_{s,\lambda}\) with
\(R_{s,\lambda}\succeq0\), then

\[
 A_\lambda^{s+1}-B_\lambda^{s+1}
 =B_\lambda(A_\lambda^s)-B_\lambda(B_\lambda^s)
  +L_\lambda(A_\lambda^s)
\]

has nonnegative coefficients in \(\lambda\).  The same is true after
composition with \(O\).  Hence the coefficient of \(\lambda^0\), which is
the paired defect for \(g_0\), is a coefficientwise sub-polynomial of the
paired defect at \(\lambda=1\).

For \(p,q\ge0\), every coordinate of the network ascent field and the
observable \(f_n\) has nonnegative coefficients in the raw variables.
Let \(g_0\) be obtained by setting only the \(u\)-update to zero, and let
\(g_1\) be that deleted update.  The lemma applies.  After expectation,
coefficientwise positivity is retained: an independent centered-Gaussian
monomial has expectation zero if an exponent is odd and a positive product
of double factorials if all exponents are even.  Consequently

\[
 \Delta_{t,n}^{\rm full}(h)\ge \Delta_{t,n}^{\rm frozen}(h),
 \qquad h\ge0.                                      \tag{2.1}
\]

## 3. Width limit of the frozen block

In the frozen block, \(H_j\) does not change.  Put

\[
 Q_n=n^{-1}\sum_jH_j^2.
\]

For each top row,

\[
 A^+=A+h\psi(Z),\qquad
 Z^+=Z+hQ_n A\psi'(Z).                              \tag{3.1}
\]

Conditional on the first layer, the row pairs are iid with
\(A\sim N(0,1)\), \(Z\sim N(0,Q_n)\), independently.  Since
\(Q_n\to\mathbb E\psi(G)^2=1\) in every finite moment, and a fixed-horizon
output from (3.1) is a finite polynomial, its expectation converges to the
scalar recursion

\[
 A_{k+1}=A_k+h(pZ_k+qZ_k^2),\qquad
 Z_{k+1}=Z_k+hA_k(p+2qZ_k),                         \tag{3.2}
\]

with independent \(A_0,Z_0\sim N(0,1)\).  Taking the width limit in (2.1)
therefore gives

\[
 \Delta_t(h)\ge D_t(h),                            \tag{3.3}
\]

where \(D_t\) is the fine-minus-coarse expected-output defect of (3.2).

## 4. A surviving all-order term

Let \(\delta_N=2^N-1\).  The largest \(h\)-degree of each of \(A_N,Z_N\)
in (3.2) is \(\delta_N\).  Inside their leading coefficients, select the
pure-quadratic monomials obtained by taking \(qZ^2\) and \(2qAZ\), rather
than the linear terms, at the first update and then recursively taking the
quadratic highest-degree terms.  These distinguished monomials have the
form

\[
\begin{aligned}
 [h^{\delta_N}]A_N
 &\succeq c_Nq^{\delta_N}A_0^{r_N}Z_0^{s_N},\\
 [h^{\delta_N}]Z_N
 &\succeq d_Nq^{\delta_N}A_0^{u_N}Z_0^{v_N},       \tag{4.1}
\end{aligned}
\]

where \(\succeq\) means “contains this monomial with at least the displayed
coefficient,” and \(c_N,d_N\) are positive integers.  This follows by
induction from \(c_0=d_0=1\),
\((r_0,s_0)=(1,0)\), \((u_0,v_0)=(0,1)\), and

\[
 c_{N+1}=d_N^2,\qquad d_{N+1}=2c_Nd_N,
\]

and

\[
 (r_{N+1},s_{N+1})=2(u_N,v_N),\qquad
 (u_{N+1},v_{N+1})=(r_N+u_N,s_N+v_N).
\]

The possible linear choices at the first update create additional
top-\(h\)-degree monomials, all with nonnegative coefficients; they do not
alter this lower bound.  Both displayed exponent pairs have total degree
\(2^N\).  At \(N=1\), the first pair
is even-even and the second odd-odd; the displayed recursion preserves
those parities.  Thus the largest output degree is

\[
 m_N=3\delta_N,
\]

and its coefficient contains the positive contribution

\[
 [h^{m_N}]\mathbb E[A_N\psi(Z_N)]
 \ge c_Nd_N^2q^{3\delta_N+1}
   \mathbb E G^{R_N}\mathbb E G^{S_N}>0,            \tag{4.2}
\]

where \(R_N,S_N\) are even and

\[
 R_N+S_N=3\cdot2^N.                                 \tag{4.3}
\]

For the even horizons used below, the exponents are explicit.  Two
applications of the exponent recursion send the selected output exponent
\(A+2Z\) to

\[
 (2A+2Z)+2(A+3Z)=4(A+2Z).
\]

Since its initial exponent is \((1,2)\),

\[
 (R_{2t},S_{2t})=(4^t,2\cdot4^t).                    \tag{4.3a}
\]

The coarse \(t\)-step polynomial has degree \(m_t\), strictly smaller than
the fine \(2t\)-step degree \(m_{2t}\).  The positive-polynomial lemma says
that every coefficient of \(D_t\) is nonnegative.  Hence, for \(h>0\),

\[
 D_t(h)\ge q^{3(4^t-1)+1}h^{3(4^t-1)}
  \mathbb E G^{R_{2t}}\mathbb E G^{S_{2t}}.         \tag{4.4}
\]

We dropped only the integer factor \(c_{2t}d_{2t}^2\ge1\).

If \(K=2m\), then

\[
 \mathbb E G^K=(2m-1)!!\ge m!\ge(m/\mathrm e)^m.   \tag{4.5}
\]

The last inequality follows from
\(\log m!\ge\int_1^m\log x\,dx\).  Use (4.3a) with
\(K=S_{2t}=2\cdot4^t\), and bound the other even Gaussian moment below by
one.  Therefore

\[
 D_t(\rho/t)\ge L_t,                               \tag{4.6}
\]

where

\[
 L_t=
 q^{3(4^t-1)+1}
 \left(\frac\rho t\right)^{3(4^t-1)}
 \left(\frac{4^t}{\mathrm e}\right)^{4^t}.
                                                               \tag{4.7}
\]

Dividing its logarithm by \(4^t\) gives

\[
 \frac{\log L_t}{4^t}
 =t\log4-3\log t+O_{q,\rho}(1),                   \tag{4.8}
\]

which tends to \(+\infty\).  Hence \(L_t\to\infty\).

## 5. Subtracting the cubic term

The exact cubic coefficient is

\[
 \kappa_t=\frac{t(2t-1)}2J_{p,q},                  \tag{5.1}
\]

where

\[
\begin{aligned}
J_{p,q}={}&48p^{12}+3446p^{10}q^2+54820p^8q^4
 +387560p^6q^6\\
&+1380876p^4q^8+2399274p^2q^{10}+1592952q^{12}.
\end{aligned}                                      \tag{5.2}
\]

Thus

\[
 |\kappa_t|(\rho/t)^3\le J_{p,q}\rho^3/t.         \tag{5.3}
\]

Combining (3.3), (4.6), and (5.3),

\[
 |\Delta_t(\rho/t)-\kappa_t(\rho/t)^3|
 \ge L_t-J_{p,q}\rho^3/t\longrightarrow\infty.    \tag{5.4}
\]

Since \(t^4(\rho/t)^5=\rho^5/t\), the claimed normalized supremum diverges.
The same argument defeats \(t^r h^5\) for every fixed \(r\), because its
value at \(h=\rho/t\) is only polynomial in \(t\).

## 6. Signs of the activation coefficients

It remains only to remove the temporary assumption \(p,q\ge0\).  Two exact
orthogonal conjugacies do this.  First,

\[
 \psi_{p,-q}(-x)=-\psi_{p,q}(x).
\]

With \(R_1(a,W,u)=(-a,W,-u)\),

\[
 f_{p,-q}(R_1\theta)=f_{p,q}(\theta).
\]

Second, replacing \(\psi\) by \(-\psi\) is conjugated by
\(R_2(a,W,u)=(-a,-W,u)\).  Differentiating either identity and using the
orthogonality of \(R_i\) shows that the corresponding Euler ascent maps are
conjugate.  Gaussian initialization is invariant under both maps.  Hence
\(F_N\) depends only on \((|p|,|q|)\), and the theorem holds for every
\(q\ne0\).

## Audit boundary

The order of limits is width first at each fixed \((t,h)\), followed by
\(t\to\infty\) with \(h=\rho/t\).  No Taylor truncation is used in the
obstruction.  Equation (4.2) is an all-order term whose order itself grows
as \(4^t\).  The previously computed fifth jet remains \(O(t^4)\); it is
therefore compatible with, but cannot detect, the nonuniform divergence
proved here.
