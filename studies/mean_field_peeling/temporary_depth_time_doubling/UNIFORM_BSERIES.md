# Uniform time-doubling: exact defect factorization and the remaining core estimate

## 1. Conclusion of this note

There is a short, exact numerical-analysis mechanism behind the conjectured
power \(t^4\).  Write

\[
 E_h(x)=x+h g(x),\qquad C_h=E_{2h},\qquad B_h=E_h^2.
\]

The fine macro-step differs from the coarse step by an exact factor \(h^2\).
After telescoping over the \(t\) macro-steps one obtains

\[
 \mathcal F(C_h^t\theta _0)-\mathcal F(B_h^t\theta _0)
 =h^2Q_t(h).                                      \tag{1.1}
\]

The Gaussian sign involution makes the left side odd, hence \(Q_t\) is
odd.  Three differentiations of each transported local defect cost at
most \(t^3\), and there are \(t\) defects.  Thus a time-uniform generated-
core estimate gives \(\sup |Q_t'''|\le C t^4\), and Taylor's formula for
\(Q_t\), rather than a fifth-order Taylor formula for the output, gives
the desired remainder.

Sections 2--4 prove this assertion, with explicit constants, for an honest
\(C^4\) vector field.  Section 5 audits its application to the population
MLP.  The audit finds one precise bridge which is **not proved in the
present study**: a quantitative, horizon-independent \(C^4\) estimate on
the reachable all-moment core.  The fixed connector
\(W_{a,0}=I_a+J_a^*\) is bounded only on \(L^2\); neither it nor the
Nemytskii activation has the Banach-space regularity that would make the
finite-dimensional theorem automatic.  The existing fixed-horizon core
induction proves finiteness but gives a constant depending on the number
of exposed history coordinates.

Consequently this note proves the \(t^4\) time combinatorics and gives an
exact sufficient population lemma, but it does **not** close that lemma
for the actual reused-matrix dynamics.  Under the qualifications of
`PROOF.md`, the stronger theorem therefore remains open unless that lemma
is supplied independently.

## 2. Exact macro-defect identity

Let \(X\) be a real Banach space, \(U\subset X\) open,
\(g:U\to X\), and \(f:U\to\mathbb R\).  All maps in this section are
assumed to remain in \(U\).  For \(h\in\mathbb R\), put

\[
 E_h(x)=x+hg(x),\qquad C_h=E_{2h},\qquad B_h=E_h\circ E_h.
\]

The fundamental theorem of calculus gives

\[
 B_hx=C_hx+h^2a_h(x),                              \tag{2.1}
\]

where

\[
 a_h(x)=\int_0^1Dg\bigl(x+shg(x)\bigr)g(x)\,ds.   \tag{2.2}
\]

Indeed,

\[
\begin{aligned}
 B_hx
 &=x+hg(x)+hg(x+hg(x))\\
 &=x+2hg(x)+h\{g(x+hg(x))-g(x)\},
\end{aligned}
\]

and the expression in braces equals
\(h\int_0^1Dg(x+shg(x))g(x)\,ds\).

For a map \(M\), let \(P_Mu=u\circ M\).  The algebraic identity

\[
 A^t-B^t=\sum_{j=0}^{t-1}A^{t-1-j}(A-B)B^j       \tag{2.3}
\]

is valid for arbitrary linear operators \(A,B\); commutativity is not
used.  Apply it to \(P_{C_h}\) and \(P_{B_h}\).  For every \(C^1\)
test function \(u\), (2.1) gives

\[
 (P_{C_h}-P_{B_h})u(x)
 =-h^2\int_0^1
 Du\bigl(C_hx+sh^2a_h(x)\bigr)[a_h(x)]\,ds.       \tag{2.4}
\]

Define the operator

\[
 R_hu(x)=-\int_0^1
 Du\bigl(C_hx+sh^2a_h(x)\bigr)[a_h(x)]\,ds.       \tag{2.5}
\]

Equations (2.3)--(2.5), evaluated at \(\theta _0\), prove the exact
identity

\[
\begin{aligned}
 d_t(h)
 &:=f(C_h^t\theta _0)-f(B_h^t\theta _0)\\
 &=h^2Q_t(h),                                      \tag{2.6}\\
 Q_t(h)
 &:=\sum_{j=0}^{t-1}
 \bigl[P_{C_h}^{t-1-j}R_hP_{B_h}^{j}f\bigr](\theta _0).
                                                               \tag{2.7}
\end{aligned}
\]

This factorization is exact at nonzero constant step size.  It is not a
finite-width Taylor expansion and contains no limit exchange.

## 3. Oddness reduces fifth order to three derivatives

Assume that \(Q_t\in C^3([-c/t,c/t])\) and that \(d_t\) is odd.  Equation
(2.6) first shows on the punctured interval that \(Q_t(-h)=-Q_t(h)\).
Continuity extends this to \(h=0\), so

\[
 Q_t(0)=Q_t''(0)=0.                                \tag{3.1}
\]

Set

\[
 \kappa_t=Q_t'(0)=\frac{d_t'''(0)}6.               \tag{3.2}
\]

Taylor's formula with integral remainder, applied to \(Q_t\), is

\[
 Q_t(h)-\kappa_th
 =\frac12\int_0^h(h-s)^2Q_t'''(s)\,ds.             \tag{3.3}
\]

Combining (2.6) and (3.3) yields the sharp reduction

\[
 \left|d_t(h)-\kappa_th^3\right|
 \le \frac{|h|^5}{6}
       \sup_{|s|\le |h|}|Q_t'''(s)|.               \tag{3.4}
\]

Thus the desired estimate follows from a \(t^4\) bound on the third
derivative of transported *local* defects.  No fifth derivative of the
unknown output is used.

For the population MLP, the sign involution already proved in
`CUBIC_DEPTH_TIME.md`, (5.6), applies to independent macro-step variables
as well as a common step.  It therefore makes \(d_t\) in (2.6) odd.  The
cubic calculation in that file gives

\[
 \kappa_t=-\frac{t(2t-1)}2J_{\phi,L}.              \tag{3.5}
\]

## 4. A completely explicit Banach-space theorem

The following theorem isolates the numerical argument from the Gaussian
regularity issue.

**Theorem 4.1 (uniform transported-defect bound).**  Let
\(\overline B=B(\theta _0,1)\subset U\).  Suppose \(f\in C^4(U)\),
\(g\in C^4(U;X)\), and, for some \(K\ge1\),

\[
 \sup_{x\in\overline B}\|D^rg(x)\|\le K
 \quad(0\le r\le4),\qquad
 \sup_{x\in\overline B}\|D^rf(x)\|\le K
 \quad(1\le r\le4).                               \tag{4.1}
\]

Assume \(d_t\) is odd.  Define

\[
 c_K=\min\{1,(16K)^{-1}\}.                         \tag{4.2}
\]

The finite recursion (4.3)--(4.12) below defines a number \(C_K<\infty\)
depending only on \(K\).  For every integer \(t\ge1\) and
\(|h|\le c_K/t\),

\[
 \left|f(C_h^t\theta _0)-f(B_h^t\theta _0)
       -\kappa_th^3\right|
 \le C_Kt^4|h|^5.                                  \tag{4.3a}
\]

Here \(\kappa_t=d_t'''(0)/6\); the theorem does not define a network
coefficient through an output derivative.  In the MLP application it is
replaced by the activation integral (3.5).

To define the constant, put \(c=c_K\) and

\[
 X_1=8K,                                             \tag{4.3}
\]

\[
 X_2=2\{8KX_1+4cKX_1^2\},                          \tag{4.4}
\]

\[
 X_3=2\{12K(X_1^2+X_2)
          +4cK(X_1^3+3X_1X_2)\}.                   \tag{4.5}
\]

Define

\[
 G_0=K,\quad G_1=KX_1,\quad
 G_2=K(X_2+X_1^2),
\]

\[
 G_3=K(X_3+3X_1X_2+X_1^3),                         \tag{4.6}
\]

and, for \(0\le r\le3\),

\[
 A_r=\sum_{q=0}^r{r\choose q}G_qG_{r-q}.           \tag{4.7}
\]

Use the convention \(A_{-1}=A_{-2}=0\), and put, for \(1\le r\le3\),

\[
 Z_r=X_r+c^2A_r+2rcA_{r-1}+r(r-1)A_{r-2}.          \tag{4.8}
\]

Starting from

\[
 T_1=2(Z_1+2K),
\]

define

\[
 T_2=2\{Z_2+4KT_1+2cKT_1^2\},
\]

\[
 T_3=2\{Z_3+6K(T_1^2+T_2)
             +2cK(T_1^3+3T_1T_2)\}.               \tag{4.9}
\]

Put

\[
 H_0=K,\quad H_1=KT_1,\quad
 H_2=K(T_2+T_1^2),
\]

\[
 H_3=K(T_3+3T_1T_2+T_1^3).                        \tag{4.10}
\]

Finally define \(W_0=2A_0\), and successively for \(r=1,2,3\),

\[
\begin{aligned}
 W_r=2\bigg\{A_r
 &+2c\sum_{q=1}^r{r\choose q}H_qW_{r-q}\\
 &+2r\sum_{q=0}^{r-1}{r-1\choose q}H_qW_{r-1-q}
 \bigg\},                                           \tag{4.11}
\end{aligned}
\]

and

\[
 C_K=\frac16\sum_{q=0}^3{3\choose q}H_qW_{3-q}.   \tag{4.12}
\]

All indices in (4.3)--(4.12) have fixed finite ranges; hence the
definition terminates.

**Proof.**  We give the estimates because the power of \(t\) is the
substantive point.

First consider an arbitrary variable-step Euler path

\[
 x_{m+1}=x_m+\alpha_mh g(x_m),\qquad
 0\le\alpha_m\le2,qquad \sum_m\alpha_m\le4t.       \tag{4.13}
\]

As long as the path is in \(\overline B\),

\[
 \|x_m-\theta _0\|
 \le |h|K\sum_{r<m}\alpha_r\le4cK\le\frac14.
\]

The first-exit argument therefore shows that the whole path lies in
\(\overline B\).  The interpolation points in (2.2) and (2.5) add at most
\(c^2K^2\le1/256\).  A path containing such a point uses at most
\(2t\) Euler weight before it and at most \(2t\) after it, so the same
first-exit estimate, with this extra \(1/256\), keeps the complete path
strictly inside \(\overline B\).

Differentiate (4.13).  If a prime denotes \(d/dh\), then

\[
 x_{m+1}'=(I+\alpha_mhDg)x_m'+\alpha_mg,             \tag{4.14}
\]

\[
 x_{m+1}''=(I+\alpha_mhDg)x_m''
 +2\alpha_mDg[x_m']
 +\alpha_mhD^2g[x_m',x_m'],                         \tag{4.15}
\]

and

\[
\begin{aligned}
 x_{m+1}'''=(I+\alpha_mhDg)x_m'''
 &+3\alpha_m\{D^2g[x_m',x_m']+Dg[x_m'']\}\\
 &+\alpha_mh\{D^3g[x_m'^3]
                 +3D^2g[x_m',x_m'']\}.             \tag{4.16}
\end{aligned}
\]

The product of the homogeneous factors is bounded by

\[
 \prod_m(1+\alpha_m|h|K)
 \le \exp\!\left(K|h|\sum_m\alpha_m\right)
 \le e^{4cK}<2.                                     \tag{4.17}
\]

Divide the \(r\)-th derivative by \(t^r\), sum the inhomogeneous
terms in (4.14)--(4.16), and use
\(\sum\alpha_m/t\le4\) and \(|h|t\le c\).
Equations (4.3)--(4.5), with deliberately enlarged coefficients, give

\[
 \sup_m\|x_m^{(r)}\|\le X_rt^r,qquad 1\le r\le3. \tag{4.18}
\]

For example, (4.15) gives before the final factor two

\[
 8KX_1+4cKX_1^2;
\]

(4.16) gives the expression inside braces in (4.5).  This verifies rather
than merely asserts the recursion.

For the field in (2.2), the curve
\(x(h)+shg(x(h))\) is exactly the old variable-step path with one
additional Euler coefficient \(s\in[0,1]\).  Its total coefficient is
still below \(4t\), so (4.18) applies to it with the same \(X_r\).
The Banach-space chain rule applied to \(g(x(h))\) and to
\(Dg(x(h)+shg(x(h)))\) now gives exactly the four bounds (4.6), after
division by \(t^r\).
Leibniz's rule in (2.2) therefore gives

\[
 \|a_h(x(h))^{(r)}\|\le A_rt^r,qquad0\le r\le3,    \tag{4.19}
\]

because integration over \(s\in[0,1]\) has mass one.  Differentiating
\(h^2a_h\) gives

\[
 (h^2a_h)^{(r)}
 =h^2a_h^{(r)}+2rh a_h^{(r-1)}+r(r-1)a_h^{(r-2)}.
\]

After division by \(t^r\), (4.19), \(|h|t\le c\), and \(t\ge1\)
give (4.8).  Repeating (4.14)--(4.16) for the fine path beginning at this
interpolation point proves (4.9).  The constants are enlarged by the
same factor two from (4.17).

It remains to differentiate the transported direction.  If \(z^+=
z+hg(z)\), its tangent satisfies

\[
 w^+=w+hDg(z)w.                                    \tag{4.20}
\]

For \(0\le r\le3\), Leibniz's rule gives

\[
\begin{aligned}
 (w^+)^{(r)}=w^{(r)}
 &+h\sum_{q=0}^r{r\choose q}(Dg(z))^{(q)}w^{(r-q)}\\
 &+r\sum_{q=0}^{r-1}{r-1\choose q}
      (Dg(z))^{(q)}w^{(r-1-q)}.                    \tag{4.21}
\end{aligned}
\]

The \(q=0\) term in the first sum is the homogeneous factor from
(4.17).  The remaining terms, summed over at most \(2t\) fine
micro-steps, give (4.11); the initial bounds are (4.19).  Thus

\[
 \|w^{(r)}\|\le W_rt^r,qquad0\le r\le3.           \tag{4.22}
\]

The scalar integrand in (2.5), after the remaining fine macro-steps, is
\(Df(z)[w]\).  The chain rule bounds the derivatives of \(Df(z)\) by
the numbers \(H_0,\ldots,H_3\) in (4.10), and a last use of Leibniz gives

\[
 \left|\frac{d^3}{dh^3}Df(z(h))[w(h)]\right|
 \le t^3\sum_{q=0}^3{3\choose q}H_qW_{3-q}.        \tag{4.23}
\]

Integration over the interpolation variable does not change the bound.
There are exactly \(t\) summands in (2.7), hence

\[
 \sup_{|h|\le c/t}|Q_t'''(h)|\le6C_Kt^4.           \tag{4.24}
\]

Equation (3.4) proves (4.3a). \(\square\)

The proof also shows why \(t^4\), rather than the naive \(t^5\), occurs:
the exact factor \(h^2\) is removed before differentiating, leaving only
three time derivatives on each of \(t\) local defects.

## 5. Application audit for the population MLP

### 5.1 The exact sufficient lemma

Theorem 4.1 applies verbatim to the population construction if the
following statement is proved.

**Uniform generated-core lemma \(\mathrm{UGC}_{4}(\phi,L)\).**  There are
explicit numbers \(K_{\phi,L}\ge1\) and \(r_{\phi,L}>0\), computed only
from \(M_\phi\), finitely many Gaussian moments, and \(L\), such that the
following holds.  For every finite Euler history with total variation at
most \(r_{\phi,L}\), every interpolation in (2.2), every transported
tangent in (4.20), and every scalar derivative of these objects through
order three:

1. the object belongs to the common fixed Gaussian all-moment core;
2. the forward, reverse, rank-one, activation, and adjoint-response
   operations may be differentiated node by node;
3. the analogues of (4.1), restricted to those generated directions, are
   bounded by \(K_{\phi,L}\), uniformly in the number and placement of
   the Euler steps.

If this lemma holds, take

\[
 c_{\phi,L}=\min\{r_{\phi,L}/2,(16K_{\phi,L})^{-1},1\},
\qquad C_{\phi,L}=C_{K_{\phi,L}}.                  \tag{5.1}
\]

Then (3.5) and Theorem 4.1 give

\[
\left|
F_{t,L}(2h)-F_{2t,L}(h)
+\frac{t(2t-1)}2J_{\phi,L}h^3
\right|
\le C_{\phi,L}t^4|h|^5,
\qquad |h|\le c_{\phi,L}/t.                       \tag{5.2}
\]

Thus \(\mathrm{UGC}_{4}\) is sufficient and contains no time
combinatorics still to be proved.

### 5.2 Why the existing core proof does not prove \(\mathrm{UGC}_4\)

The fixed connector is

\[
 W_{a,0}=I_a+J_a^*:L^2(\Omega_{a-1})\to L^2(\Omega_a).
\]

Its operator norm is at most two on \(L^2\).  This fact cannot be promoted
to the \(L^p\) bounds needed for products of generated variations.  For
any \(p>2\), choose
\(c\in L^2(\Omega_a)\setminus L^p(\Omega_a)\).  Since \(J_a\) is an
isometry onto a first-chaos subspace, \(x=J_ac\) is Gaussian and hence
belongs to every finite \(L^q(\Omega_{a-1})\), but

\[
 J_a^*x=J_a^*J_ac=c\notin L^p(\Omega_a).            \tag{5.3}
\]

Therefore no bound

\[
 \|J_a^*x\|_p\le C_p\|x\|_q
\]

can hold on the ambient spaces for any finite \(q\), even on inputs with
all Gaussian moments.

Nor is the activation map globally \(C^2:L^2\to L^2\) for a non-affine
\(C^2\) activation.  Choose a constant \(z_0\) with
\(\phi''(z_0)\ne0\).  A bounded second derivative at the constant field
\(z_0\), evaluated first on bounded directions \(u,v\), is forced by
two scalar directional differentiations to equal
\(\phi''(z_0)uv\).  It would therefore require pointwise
multiplication to be a bounded bilinear map \(L^2\times L^2\to L^2\).
On a nonatomic probability space, with

\[
 v_n=\sqrt n\,\mathbf 1_{[0,1/n]},
\]

one has \(\|v_n\|_2=1\) but \(\|v_n^2\|_2=\sqrt n\).  Hence the ordinary
Banach-space hypotheses of Theorem 4.1 do not follow from bounded
derivatives of \(\phi\).

`CUBIC_DEPTH_TIME.md`, Section 4.1, correctly avoids these false ambient
claims: for a **fixed finite horizon** it expands each adjoint action as a
finite response sum and proves that every generated jet has all moments.
That proof establishes membership and differentiability but does not give
a bound uniform in the number of response coordinates.  The fixed-
\(t\) Price compiler likewise counts every exposed coordinate and produces
the rapidly growing exponent \(E_{L,2t}\).  Neither argument proves that
the response sum can be bounded only by the total step variation.

The missing estimate can be stated more concretely.  One must prove, for
each connector and \(p\) needed through fourth generated order, bounds of
the form

\[
 \left\|\sum_{r<s}\rho^a_{sr}\Delta_{a,r}\right\|_p
 +\left\|\sum_{r\le s}\sigma^a_{sr}X_{a-1,r}\right\|_p
 \le \mathfrak C_{\phi,L,p}(\tau),                 \tag{5.4}
\]

and the analogous bounds for three step-size derivatives, where

\[
 \tau=\sum_{r<s}|\varepsilon_r|,
\]

and where \(\mathfrak C_{\phi,L,p}\) is independent of \(s\) and of the
rank or conditioning of the history Grams.  Formula (5.4) must exploit
the intrinsic cancellations in \(J_a^*\) and \(I_a^*\); an entrywise
\(\ell^1\) estimate of the response coordinates generally grows with the
horizon and is not sufficient.

No estimate of the form (5.4) is proved in the current files.  Equation
(5.3) shows that it cannot be replaced by an ambient \(L^p\) operator
bound.  It has to be a genuinely dynamical, generated-core estimate.

## 6. Claim status

The exact identities (2.6)--(2.7), the odd reduction (3.4), and Theorem
4.1 are proved.  They establish the optimal \(t^4\) time combinatorics
under the explicit local regularity bounds (4.1), and reduce the actual
MLP theorem to the single quantitative statement \(\mathrm{UGC}_4\).

For the actual width-first reused-matrix population network under only the
activation assumptions in `PROOF.md`, \(\mathrm{UGC}_4\) is presently
unproved.  Therefore (5.2) is conditional, not a theorem of this study.
The obstruction is not the Euler/B-series calculation; it is uniform
high-moment control of the moving adjoint responses on the reachable core.
