# Peeling and probability ledger for the \(L=2,B=1\) coefficient

**Status:** the fixed-width observable is encoded exactly as a finite Tensor
Program (equivalently, a NETSOR\({}^\top+\) program).  Under the
polynomially-smooth activation hypothesis below, an existing master theorem
gives the required almost-sure and \(L^p\), hence annealed, limit.  If the
frozen contract is read as controlling only
\(\phi^{(0)},\ldots,\phi^{(3)}\), the same conclusion is not theorem-covered
without an additional uniform-integrability argument.  
**Date:** 2026-08-18  
**Scope:** the model and limit order in `PROOF_CONTRACT.md`

## 1. Bottom line and exact claim level

Let

\[
C_n=D_n^3f_n,
\qquad
C=6\mathcal T_*+4\mathcal H_*
\]

with \(\mathcal T_*\) and \(\mathcal H_*\) given in
`INDEPENDENT_ANALYTIC_DERIVATION.md`.  This ledger establishes the following
scoped statement.

> **Polynomially-smooth activation theorem.**  Suppose \(\phi\) is
> polynomially smooth: \(\phi\in C^\infty(\mathbb R)\), and every derivative
> \(\phi^{(k)}\), \(k\geq0\), is bounded in absolute value by a polynomial
> (whose degree and coefficient may depend on \(k\)).  Then
> \[
> C_n\longrightarrow C\quad\text{almost surely and in }L^p
> \quad(1\le p<\infty),
> \qquad
> \mathbb E C_n\longrightarrow C.
> \tag{1.1}
> \]

This is a direct application of Theorem 3.7 of Eugene Golikov and Greg Yang,
[*Non-Gaussian Tensor
Programs*](https://proceedings.neurips.cc/paper_files/paper/2022/file/8707924df5e207fa496f729f49069446-Paper-Conference.pdf),
to the exact scalar program in Section 3.  Its Setup 3.6 includes the present
Gaussian matrix as a special case, and the theorem states convergence of
**every scalar in the program** almost surely and in \(L^p\) for every finite
\(p\).  Thus uniform integrability is a conclusion of the invoked theorem,
not an extra assumption, under the displayed polynomially-smooth envelope.

There is a real regularity boundary.  The algebraic formula uses only
\(\phi^{(0)},\ldots,\phi^{(3)}\), but Theorem 3.7 requires each coordinate map
in the program to be polynomially smooth.  Since those maps contain
\(\phi^{(j)}\), this is guaranteed by polynomial growth of
\(\phi^{(k)}\) for **all** \(k\), not merely \(k\le3\).  If only the latter
finite list is assumed pseudo-Lipschitz, Theorem E.15 of Greg Yang,
[*Tensor Programs III: Neural Matrix
Laws*](https://arxiv.org/pdf/2009.10685), still gives the fixed-program
almost-sure limit

\[
C_n\longrightarrow C\quad\text{almost surely}.
\tag{1.2}
\]

It does not by itself yield the annealed conclusion for this unbounded scalar.
Thus, under only finite-order polynomial-growth control,

\[
\mathbb E C_n\to C
\tag{1.3}
\]

still requires a separate uniform-integrability hypothesis; see Section 8.3.
This distinction is not cosmetic.  In particular, \(C^3\) plus polynomial
growth through order three is insufficient to invoke Theorem 3.7 as written.

Tensor Programs III supplies the recurrent Gaussian/response formula used to
identify the deterministic limit \(C\).  It allows arbitrary reuse of a
Gaussian matrix and its transpose, empirical `Moment` scalars, and
pseudo-Lipschitz coordinate nonlinearities without a separate rank-stability
assumption.  Its unrestricted transpose rule splits every multiplication into
a fresh Gaussian channel plus the finite span of earlier opposite-orientation
uses.  Treating \(W\) and \(W^\top\) as independent would delete leading
terms.

## 2. Frozen notation

Write

\[
q=q_0=\frac{\|x\|^2}{d_0},
\qquad
M_n(v)=\frac1n\sum_{i=1}^nv_i,
\qquad
A=\frac{W}{\sqrt n}.
\tag{2.1}
\]

The entries of \(A\) are iid \(N(0,1/n)\).  The two initial vectors are

\[
u_i\stackrel{\rm iid}{\sim}N(0,q),
\qquad
a_i\stackrel{\rm iid}{\sim}N(0,1),
\tag{2.2}
\]

independent of each other and of \(A\).  Put, coordinatewise,

\[
x_r=\phi^{(r)}(u),\qquad
z=Ax_0,\qquad
y_r=\phi^{(r)}(z),\qquad 0\le r\le3,
\tag{2.3}
\]

and use \(\odot\) for coordinatewise multiplication.  Define

\[
b=a\odot y_1,
\qquad
r=A^\top b.
\tag{2.4}
\]

The symbol \(r\) in this ledger is the backward vector, not a derivative
order.

## 3. Exact finite NETSOR\({}^\top+\) program

Every line below is an exact finite-width identity.  It uses only the
`MatMul`, `Nonlin+`, and `Moment` operations of NETSOR\({}^\top+\).

First define

\[
Q_n=M_n(x_0^2),\qquad
D_n^{\rm b}=M_n(b^2).
\tag{3.1}
\]

The first frozen tangent of the top preactivation is

\[
\zeta=Q_nb+qA(x_1^2\odot r).
\tag{3.2}
\]

The second tangent is

\[
c_n=M_n(x_0\odot x_1^2\odot r),
\]

\[
\sigma=2q c_nb+q^2A(x_2\odot x_1^2\odot r^2).
\tag{3.3}
\]

The third tangent is

\[
m_n=M_n(x_0\odot x_2\odot x_1^2\odot r^2),
\]

\[
\tau=3q^2m_nb+q^3A(x_3\odot x_1^3\odot r^3).
\tag{3.4}
\]

For the actual derivative of the backward vector, put

\[
B=y_0\odot y_1+a\odot y_2\odot\zeta,
\]

\[
\dot r=D_n^{\rm b}x_0+A^\top B.
\tag{3.5}
\]

The straight-line third derivative is exactly the `Moment` scalar

\[
\begin{aligned}
\mathcal T_n=M_n\big[&
a\odot(y_3\odot\zeta^3
+3y_2\odot\zeta\odot\sigma+y_1\odot\tau)\\
&+3y_0\odot(y_2\odot\zeta^2+y_1\odot\sigma)
\big].
\end{aligned}
\tag{3.6}
\]

The three exact Hessian-square blocks are

\[
\mathcal H_{a,n}=M_n[(y_1\odot\zeta)^2],
\tag{3.7}
\]

\[
\begin{aligned}
\mathcal H_{W,n}={}&
Q_nM_n(B^2)
+q^2M_n(b^2)M_n(x_1^4\odot r^2)\\
&+2qM_n(b\odot B)M_n(x_0\odot x_1^2\odot r),
\end{aligned}
\tag{3.8}
\]

and

\[
\mathcal H_{u,n}
=qM_n\left[
\big(qx_2\odot x_1\odot r^2+x_1\odot\dot r\big)^2
\right].
\tag{3.9}
\]

Consequently,

\[
\boxed{
C_n=2\mathcal T_n
+4(\mathcal H_{a,n}+\mathcal H_{W,n}+\mathcal H_{u,n}).}
\tag{3.10}
\]

Equation (3.10) is not an asymptotic representation.  It is the exact
finite-width identity obtained from
\(D_n^3f_n=2T[V,V,V]+4n(HV)^\top M(HV)\), after factoring the two rank-one
terms in the middle-weight acceleration.  It proves that the target is a
single fixed-size NETSOR\({}^\top+\) scalar program: its number of program
lines and nonlinearities does not depend on \(n\).

## 4. Master-theorem hypothesis map

The exact program is admissible both for Tensor Programs III, Theorem E.15,
and for Non-Gaussian Tensor Programs, Theorem 3.7.  The latter paper states
explicitly after its Definition 3.1 that its TP syntax is equivalent to
NETSOR\({}^\top+\).  The detailed hypothesis map is:

| Theorem object | Present object | Verification |
|---|---|---|
| independent matrix entries, mean zero, variance \(1/n\) | \(A=W/\sqrt n\) | Exact: iid \(N(0,1/n)\) |
| scaled higher moments \(\mathbb E|A_{ij}|^k\le\nu_kn^{-k/2}\) for every \(k\ge3\) | Gaussian entries | Exact with \(\nu_k=\mathbb E|G|^k\) |
| standard-Gaussian initial vectors | take independent \(g,a\sim N(0,I_n)\) and write \(u=\sqrt q\,g\) inside coordinate maps | Exact reparameterization; no nonstandard initial law is needed |
| all moments of initial scalars | the sole nontrivial one is deterministic \(q\in(0,\infty)\) | Exact |
| fixed finite program | (2.3)--(3.10) | Exact; line count is independent of \(n\) |
| a matrix or its transpose may be reused | \(Ax_0,A^\top b,A(\cdot),A^\top B\) | Literal TP syntax in Definition 3.1 |
| empirical scalar lines | \(Q_n,D_n^{\rm b},c_n,m_n\), (3.6)--(3.10) | Each is a `Moment`; products of earlier scalars are absorbed into the next coordinate map |
| scalar-dependent coordinate maps | multiplication by \(Q_n,c_n,m_n,D_n^{\rm b}\) | Literal `Nonlin+`/TP coordinate maps |
| polynomially-smooth coordinate maps | finite sums/products/compositions of coordinates, earlier scalars, and \(\phi^{(j)}\), \(0\le j\le3\) | Verified if every \(\phi^{(k)}\), \(k\ge0\), has polynomial growth; this property is closed under finite sums, products, derivatives, and compositions used here |
| deterministic scalar limit | the recurrent Gaussian/response evaluation in Sections 5--7 | Theorem E.15/3.7 identifies the limit with the Gaussian master-theorem recurrence |

The last regularity row is the only non-algebraic activation condition.  It is
fully verified for polynomial, sine, tanh, and other polynomially-smooth
controls used in this project.  It is not verified merely from bounds on
\(\phi,\phi',\phi'',\phi'''\), and it excludes ReLU.

Theorem E.15 supplies almost-sure convergence of every generated scalar under
the weaker pseudo-Lipschitz envelope and does not require rank stability.
Theorem 2.10 of the same source makes explicit that using both \(A\) and
\(A^\top\) produces a deterministic correction in addition to the fresh
Gaussian part; the introductory example \(A^\top Av\) is the elementary
instance of the response mechanism.  Theorem 3.7 then strengthens the scalar
convergence to \(L^p\) for every finite \(p\) under polynomial smoothness.

No feature-learning or positive-time theorem is being invoked.  We apply a
fixed finite initialization program only.  Tensor Programs IV is therefore
not needed for (1.1) or (1.2).

## 5. Symbolic limit and complete response registry

Let

\[
U\sim N(0,q),\quad
Q=\mathbb E\phi(U)^2,\quad
Z\sim N(0,Q),\quad
A_0\sim N(0,1)
\tag{5.1}
\]

be independent unless a covariance is explicitly displayed.  Let

\[
D=\mathbb E\phi'(Z)^2,
\qquad
d=\mathbb E\phi'(U)^2,
\qquad
r_4=\mathbb E\phi'(U)^4.
\tag{5.2}
\]

The following table lists every possible opposite-orientation response in
program order.  Completeness follows from the NETSOR\({}^\top\) rule: the
response lies in the finite span of the vectors used by every earlier
opposite-orientation multiplication.  A direction absent from the table has
zero formal derivative because the current input does not depend on its
corresponding Gaussian channel.

| Current multiplication | Earlier opposite-orientation direction | Response coefficient | Status |
|---|---|---:|---|
| \(A^\top b\) | \(x_0\), from \(z=Ax_0\) | \(\mathbb E[A_0\phi''(Z)]=0\) | exact readout parity; no response |
| \(A(x_1^2r)\) | \(b\), from \(r=A^\top b\) | \(\mathbb E[\partial_R(\phi'(U)^2R)]=d\) | leading Onsager response \(db\) |
| \(A(x_2x_1^2r^2)\) | \(b\) | \(2\mathbb E[\phi''(U)\phi'(U)^2R]=0\) | centered-\(R\) parity |
| \(A(x_3x_1^3r^3)\) | \(b\) | \(3\mathbb E[\phi'''(U)\phi'(U)^3R^2]=3D\ell\) | leading Onsager response \(3D\ell b\) |
| \(A^\top B\) | \(x_0\), from \(z=Ax_0\) | \(S_0+\alpha S_1\) | leading nested response |
| \(A^\top B\) | \(x_1^2r\), from \(A(x_1^2r)\) | \(q\mathbb E[A_0\phi''(Z)]=0\) | readout parity |
| \(A^\top B\) | second/third-tangent inputs | \(0\) | \(B\) does not depend on those channels |

Here

\[
\ell=\mathbb E[\phi'''(U)\phi'(U)^3],
\]

\[
\alpha=Q+qd,
\]

\[
S_0=\mathbb E[\phi'(Z)^2+\phi(Z)\phi''(Z)],
\]

\[
S_1=\mathbb E[\phi''(Z)^2+\phi'(Z)\phi'''(Z)].
\tag{5.3}
\]

The symbolic random variables generated by the master theorem are therefore:

1. For \(r=A^\top b\),
   \[
   Z^r=R,\qquad R\sim N(0,D),
   \tag{5.4}
   \]
   fresh and independent of \(U,A_0,Z\).  The only available response was
   killed in the first row of the table.

2. For \(A(x_1^2r)\),
   \[
   Z^{A(x_1^2r)}=dA_0\phi'(Z)+\Gamma,
   \qquad
   \Gamma\sim N(0,r_4D),
   \tag{5.5}
   \]
   with \(\Gamma\) independent of \((A_0,Z)\).  Its fresh covariance with
   \(Z\) is zero because
   \(\mathbb E[\phi(U)\phi'(U)^2R]=0\).  Hence
   \[
   Z^\zeta=\alpha A_0\phi'(Z)+q\Gamma.
   \tag{5.6}
   \]

3. The scalar in the first part of (3.3) satisfies
   \[
   c_n\longrightarrow
   \mathbb E[\phi(U)\phi'(U)^2R]=0.
   \tag{5.7}
   \]
   For
   \(\Omega=Z^{A(x_2x_1^2r^2)}\),
   \[
   \operatorname{Cov}(Z,\Omega)
   =D\,m,
   \qquad
   m=\mathbb E[\phi(U)\phi''(U)\phi'(U)^2],
   \tag{5.8}
   \]
   while
   \(\operatorname{Cov}(\Gamma,\Omega)=0\) by
   \(\mathbb ER^3=0\).  Thus
   \[
   Z^\sigma=q^2\Omega.
   \tag{5.9}
   \]

4. The scalar in (3.4) satisfies \(m_n\to Dm\).  If
   \(\Lambda\) is the fresh Gaussian part of
   \(A(x_3x_1^3r^3)\), then
   \[
   Z^\tau
   =3D(q^2m+q^3\ell)A_0\phi'(Z)+q^3\Lambda.
   \tag{5.10}
   \]
   The covariance \(\operatorname{Cov}(\Lambda,\Gamma)\) need not vanish;
   it equals
   \[
   3D^2\mathbb E[\phi'''(U)\phi'(U)^5].
   \tag{5.11}
   \]
   This atom does not survive because the only occurrence of \(\Lambda\) in
   (3.6) is multiplied by a single centered \(A_0\).

5. Define the limiting row channel
   \[
   \mathsf B=\phi(Z)\phi'(Z)
   +A_0\phi''(Z)
   \big(\alpha A_0\phi'(Z)+q\Gamma\big).
   \tag{5.12}
   \]
   Then
   \[
   \beta=\mathbb E\mathsf B^2
   =E_0+2\alpha P_1+3\alpha^2E_{12}+\nu E_2,
   \qquad
   \nu=q^2r_4D.
   \tag{5.13}
   \]
   The nested response is
   \[
   \mathbb E[\partial_Z\mathsf B]=S_0+\alpha S_1,
   \tag{5.14}
   \]
   and
   \[
   \mathbb E[A_0\phi'(Z)\mathsf B]=0.
   \tag{5.15}
   \]
   Therefore
   \[
   Z^{\dot r}=\chi\phi(U)+\Eta,
   \qquad
   \chi=D+S_0+\alpha S_1,
   \qquad
   \Eta\sim N(0,\beta),
   \tag{5.16}
   \]
   where \(\Eta\) is independent of \((U,R)\).  Equation (5.15) is the
   covariance certificate for the independence from \(R\).

These five symbolic rules are exactly those used by both independent normal
form derivations.  The master theorem guarantees that no additional leading
response direction is omitted.

## 6. Equality and negative-width ledger

The following explicit leave-one-out counts give a second interpretation of
the response registry.  They are a local width ledger, not a substitute for
the joint conditioning theorem used below.  Write

\[
r_j=r_j^{(-i)}+A_{ij}b_i,
\qquad A_{ij}=O_p(n^{-1/2}).
\tag{6.1}
\]

For a single sum over \(j\), a fresh term with one \(A_{ij}\) has variance
\(n\cdot n^{-1}=O(1)\).  A single equality response contains
\(n\) terms with \(A_{ij}^2\), hence is also \(O(1)\).  Every further
same-row identification in these displayed expansions loses at least another
factor \(n^{-1/2}\).  Entries labelled \(O_p(n^{-1/2})\) record this local
power count; the rigorous fact used later is their zero symbolic response and
the master-theorem convergence, not an unproved global rate claim.

| Source | Leave-one-out branch | Width/status | Certificate |
|---|---|---|---|
| \(A(x_1^2r)\) | \(A_{ij}x_{1,j}^2r_j^{(-i)}\) | \(O_p(1)\), fresh | conditional Gaussian channel \(\Gamma\) |
| same | \(A_{ij}^2x_{1,j}^2b_i\) | \(O_p(1)\), equality | LLN gives \(db_i\) |
| \(A(x_2x_1^2r^2)\) | \(A_{ij}x_2x_1^2(r_j^{(-i)})^2\) | \(O_p(1)\), fresh | channel \(\Omega\) |
| same | \(2A_{ij}^2x_2x_1^2b_ir_j^{(-i)}\) | \(O_p(n^{-1/2})\) | centered \(r^{(-i)}\); response coefficient zero |
| same | \(A_{ij}^3x_2x_1^2b_i^2\) | \(O_p(n^{-1/2})\) or smaller | one extra equality power |
| \(A(x_3x_1^3r^3)\) | \(A_{ij}x_3x_1^3(r_j^{(-i)})^3\) | \(O_p(1)\), fresh | channel \(\Lambda\) |
| same | \(3A_{ij}^2x_3x_1^3b_i(r_j^{(-i)})^2\) | \(O_p(1)\), equality | LLN gives \(3D\ell b_i\) |
| same | \(3A_{ij}^3x_3x_1^3b_i^2r_j^{(-i)}\) | \(O_p(n^{-1/2})\) or smaller | extra equality plus centered field |
| same | \(A_{ij}^4x_3x_1^3b_i^3\) | \(O_p(n^{-1})\) | two extra equality powers |
| \(c_n\) in (3.3) | distinct-row/column average | \(O_p(n^{-1/2})\) | limiting integrand is odd in fresh \(R\) |
| \(A^\top B\) | fresh orthogonal component | \(O_p(1)\) | variance \(\beta\) |
| same | response along \(x_0\) | \(O_p(1)\) | coefficient (5.14) |
| same | response along \(x_1^2r\) | exactly zero in the limit | \(\mathbb E[A_0\phi''(Z)]=0\) |

For the nonlinear transpose line \(A^\top B\), (6.1) is not by itself a
complete Taylor proof.  The unrestricted NETSOR\({}^\top\) conditioning
theorem supplies the rigorous statement: after projection onto the complete
finite span of earlier forward inputs, the residual is asymptotically
Gaussian, and the projection coefficients are the expected weak derivatives
listed in Section 5.  Therefore unlisted higher Taylor branches are not being
silently discarded; they are covered by the theorem's Gaussian-conditioning
remainder.

Two delicate zero branches merit separate certificates.

1. The first term of \(\sigma\) is \(2qc_nb\).  The scalar \(c_n\) is itself
   a `Moment` line, so Theorem E.15 gives, almost surely,
   \[
   c_n\to\mathbb E[\phi(U)\phi'(U)^2R]=0.
   \tag{6.2}
   \]
   Because \((c_n,b)\) and every scalar in which their product appears are
   part of the same program, the theorem applies to the product jointly.
   Thus this branch vanishes in (3.6); no standalone \(O_p(n^{-1/2})\)
   estimate for \(c_n\) is required.

2. For \(\dot r\), the theorem is applied once to the full program containing
   \(r=A^\top b\), \(B\), and \(A^\top B\).  The fresh covariance is
   \[
   \operatorname{Cov}(R,\Eta)
   =\mathbb E[A_0\phi'(Z)\mathsf B]=0,
   \tag{6.3}
   \]
   by (5.15) and readout parity.  The two potentially nonzero response
   coefficients are
   (5.14) and \(q\mathbb E[A_0\phi''(Z)]=0\), respectively.  Hence (5.16)
   is a joint Gaussian statement, not a marginal-CLT plus an independence
   assumption.

## 7. Final contraction: survival and cancellation ledger

Substitution of (5.6), (5.9), (5.10), and (5.16) into the exact scalar program
gives the following complete list.

### 7.1 Straight-line tensor block

| Exact source in (3.6) | Surviving branches | Vanishing branches |
|---|---|---|
| \(3y_0y_2\zeta^2\) | \(3\alpha^2P_1+3\nu P_2\) | response--fresh cross: centered \(\Gamma\) |
| \(3y_0y_1\sigma\) | \(3\kappa S_0\), \(\kappa=q^2Dm\) | scalar branch \(c_n\to0\); no Onsager response in \(\Omega\) |
| \(a y_3\zeta^3\) | \(3\alpha^3P_3+3\alpha\nu P_4\) | terms odd in \(\Gamma\) or in \(a\) |
| \(3a y_2\zeta\sigma\) | \(3\alpha\kappa S_1\) | \(\operatorname{Cov}(\Gamma,\Omega)=0\); remaining terms odd in \(a\) |
| \(a y_1\tau\) | \(3D^2(q^2m+q^3\ell)\) | fresh \(\Lambda\) term has one centered \(a\) |

Thus

\[
\lim\mathcal T_n=3\mathcal T_*.
\tag{7.1}
\]

The potentially nonzero covariance (5.11) is retained until the complete
contraction is formed; it vanishes only because the \(\Lambda\) source contains
no second readout factor.  This avoids an invalid blanket-independence claim.

### 7.2 Hessian-square blocks

For (3.7), the response-square and fresh-square branches give

\[
\mathcal H_a\to\alpha^2R+\nu D.
\tag{7.2}
\]

For (3.8),

\[
Q_nM_n(B^2)\to Q\beta,
\]

\[
q^2M_n(b^2)M_n(x_1^4r^2)\to q^2D(r_4D)=\nu D.
\]

The mixed rank-one contraction vanishes because

\[
M_n(x_0x_1^2r)\to\mathbb E[\phi(U)\phi'(U)^2R]=0;
\tag{7.3}
\]

independently, \(M_n(bB)\to0\) by readout parity.  Hence

\[
\mathcal H_W\to Q\beta+\nu D.
\tag{7.4}
\]

Finally, using \(\mathbb ER^4=3D^2\) and (5.16), (3.9) gives

\[
\mathcal H_u\to
q\big(3q^2D^2s+\chi^2e+\beta d+2qD\chi m\big).
\tag{7.5}
\]

The terms containing one \(\Eta\) vanish because it is centered and
independent of \((U,R)\).  Equations (7.2), (7.4), and (7.5) give

\[
\lim(\mathcal H_{a,n}+\mathcal H_{W,n}+\mathcal H_{u,n})
=\mathcal H_*.
\tag{7.6}
\]

This recovers

\[
C=6\mathcal T_*+4\mathcal H_*
\]

from a theorem-covered finite program.

## 8. Almost-sure limit versus annealed expectation

### 8.1 Almost-sure peeling under the weaker hypothesis

If the coordinate maps are only pseudo-Lipschitz, Theorem E.15 applies
directly to (2.3)--(3.10).  It gives almost-sure convergence of each `Moment`
scalar and hence of \(C_n\).  This proves (1.2).  This is convergence of the
actual empirical scalar, not merely convergence in distribution of one
coordinate.  It also resolves the simultaneous joint law needed for
\(\dot r\): all earlier channels and \(A^\top B\) occur in one program, so the
master theorem produces their joint Gaussian covariance and every transpose
response in a single induction.

Almost-sure convergence alone does not justify exchanging limit and
initialization expectation for an unbounded observable.

### 8.2 \(L^p\) convergence and uniform integrability

Under polynomial smoothness, Theorem 3.7 applies to the same exact program.
The chain of implications is literal:

\[
\text{Theorem 3.7}
\quad\Longrightarrow\quad
C_n\to C\text{ in }L^p\text{ for every }1\le p<\infty
\quad\Longrightarrow\quad
\mathbb E C_n\to C.
\tag{8.1}
\]

For example, taking \(p=2\) gives

\[
\sup_{n\ge n_0}\mathbb E|C_n|^2<\infty.
\tag{8.2}
\]

Thus \(\{C_n:n\ge n_0\}\) is uniformly integrable; adjoining the finite set
\(n<n_0\) changes nothing.  This supplies precisely the annealed bridge in
the proof contract.  No independent conditional-chaos or operator-norm bound
is needed.

The same theorem may be applied after adjoining the finite collection of
fixed-order scalar lines required by the direct loss audit
(`AUDIT_REPORT.md`).  Products such as fixed powers of \(f_n,K_n,J_n,C_n\)
are encoded as one more empirical scalar line, whose coordinate map is still
polynomially smooth.  Hence the finite collection is jointly \(L^p\)-controlled
under the same hypothesis.  This statement is only about the fixed loss jet;
it is not uniform in time or derivative order.

### 8.3 Exact uncovered regularity class

Suppose instead that only \(\phi^{(0)},\ldots,\phi^{(3)}\) are
pseudo-Lipschitz/polynomially bounded.  Theorem E.15 proves (1.2), but the
hypotheses of Theorem 3.7 have not been verified: differentiating a coordinate
map arbitrarily often invokes \(\phi^{(k)}\) for unbounded \(k\).  The exact
additional tail condition sufficient for the annealed target is, for some
\(\epsilon>0\),

\[
\boxed{
\sup_{n\ge1}\mathbb E|C_n|^{1+\epsilon}<\infty.}
\tag{8.3}
\]

This ledger does not derive (8.3) from finite-order regularity alone.  Nor may
Gaussian smoothing be used to remove the issue without a separate
approximation-error estimate uniform in \(n\); doing so would change the
activation before the limit.  Bounded \(C^3\) is likewise not, by itself, the
published theorem's polynomial-smoothness hypothesis.

## 9. Claim ledger and hostile audit

| Claim | Status | Dependency or falsifier |
|---|---|---|
| (3.10) exactly represents \(D_n^3f_n\) | **Exact finite-width identity** | Falsified by a missing product-rule or metric factor; all three parameter blocks independently checked |
| The program is admissible NETSOR\({}^\top+\)/TP | **Exact syntactic encoding** | Would fail only if a width-dependent or non-coordinatewise operation had been hidden; none is present |
| The response registry in Section 5 is complete | **Theorem-covered** | Uses unrestricted transpose rule; not a gradient-independence assumption |
| \(C_n\to C\) almost surely under pseudo-Lipschitz finite-order maps | **Proved** | Direct application of Theorem E.15 to the exact program |
| \(C_n\to C\) in every finite \(L^p\) for polynomially-smooth \(\phi\) | **Proved** | Direct application of Theorem 3.7, Setup 3.6 |
| \(\mathbb EC_n\to C\) for polynomially-smooth \(\phi\) of polynomial growth | **Proved** | Theorem 3.7 gives \(L^1\) directly and \(L^2\) supplies UI |
| \(\mathbb EC_n\to C\) assuming only polynomial bounds through derivative order three | **Open without (8.3)** | Polynomial smoothness of the program maps has not been verified |
| Typical deterministic coefficient/concentration | **Proved for this fixed scalar program under Theorem E.15** | Does not imply a positive-time trajectory or uniform-in-derivative-order theorem |
| Positive-time or arbitrary-depth MFP closure | **Unchanged/open** | Not addressed by this finite program |

The strongest structural objection was that the same matrix is reused through
\(A,A^\top,A,A^\top\), so an iid-gradient shortcut could miss response terms.
Sections 4--6 close that objection for fixed order by an unrestricted
transpose theorem and explicitly retain both nonzero responses \(db\) and
\((S_0+\alpha S_1)x_0\).

The annealed tail objection is closed for polynomially-smooth activations,
including unbounded polynomial activations, by Theorem 3.7.  It survives only
if the activation contract is weakened to finite-order regularity.  In that
weaker tier it must not be described as merely technical until (8.3) is
proved from the intended assumptions.

## 10. Consequence for the extension program

The \(L=2,B=1\) Gaussian normal form is now supported at three distinct
levels:

1. exact finite-width differentiation and scalarization;
2. theorem-controlled almost-sure peeling with every transpose response;
3. theorem-controlled \(L^p\) and annealed convergence for every
   polynomially-smooth activation of polynomial growth.

It is therefore legitimate to use this base case as the regression oracle for
the \(B=2\) construction.  If `PROOF_CONTRACT.md` intends polynomial control
of every derivative, the fixed-order probabilistic bridge is discharged.  If
it intends control only through order three, an annealed theorem must still
carry (8.3) as an explicit hypothesis or strengthen the activation envelope.
Nothing in this ledger proves an \(O(L)\) depth-uniform state closure or a
positive-time mean-field limit.
