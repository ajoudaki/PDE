# Singular-covariance regularity supplement

This supplement closes the two analytic details compressed in Sections 5--6
of `PROOF.md`: repeated Price differentiation when the Gaussian covariance
loses rank, and the derivative-order count showing that \(C^{12}\) regularity
of the activation is sufficient.  It uses the inverse-free DAG (3.1)--(3.3)
and the envelope compiler (6.1) of that file.

## 1. Price differentiation without an inverse covariance

Let \(I=[-1,1]\), let \(C\in C^5(I;\mathbb S_+^m)\), and let
\(\psi:I\times\mathbb R^m\to\mathbb R\).  Assume that every derivative

\[
 \partial_h^jD_x^\alpha\psi,
 \qquad j+\left\lceil\frac{|\alpha|}{2}\right\rceil\le5,
 \tag{S.1}
\]

exists and is jointly continuous.  Assume also that there are finite
\(A,P\), independent of \(h\), such that every derivative in (S.1) obeys

\[
 \left|\partial_h^jD_x^\alpha\psi(h,x)\right|
 \le A(1+\|x\|)^P .
 \tag{S.2}
\]

There is no loss in using one \((A,P)\): the index set in (S.1) is finite,
so one may take the maximum of the finitely many constants and exponents.
For \(X_h\sim N(0,C(h))\), define

\[
 N(h)=\mathbb E\psi(h,X_h),
 \qquad
 \mathscr L g=\partial_hg+\frac12 C'(h):D_x^2g,
 \tag{S.3}
\]

and recursively \(\Psi_0=\psi\), \(\Psi_{r+1}=\mathscr L\Psi_r\).

**Lemma S.1.**  Under (S.1)--(S.2), \(N\in C^5(I)\), with one-sided
derivatives at the endpoints, and

\[
 N^{(r)}(h)=\mathbb E\Psi_r(h,X_h),
 \qquad 0\le r\le5.
 \tag{S.4}
\]

This conclusion remains valid at every \(h\) for which \(C(h)\) is
singular or changes rank.

### Proof

First record the domination used below.  Compactness of \(I\) gives

\[
 V:=\sup_{h\in I}\operatorname{tr}C(h)<\infty.
\]

For each \(h\), realize \(X_h=C(h)^{1/2}G\), where \(G\sim N(0,I_m)\).
Since \(\|C(h)^{1/2}\|_{\mathrm{op}}^2\le\operatorname{tr}C(h)\),

\[
 \|X_h\|\le\sqrt V\,\|G\|.
 \tag{S.5}
\]

Consequently, for every finite \(p\),

\[
 \sup_{h\in I}\mathbb E(1+\|X_h\|)^p<\infty
 \tag{S.6}
\]

and, by dominated convergence,

\[
 \sup_{h\in I}\mathbb E\!\left[(1+\|X_h\|)^p
        \mathbf1_{\{\|X_h\|>R\}}\right]\longrightarrow0.
 \tag{S.7}
\]

The implication in (S.7) follows directly from (S.5): its left side is
bounded by

\[
 \mathbb E\!\left[(1+\sqrt V\|G\|)^p
        \mathbf1_{\{\sqrt V\|G\|>R\}}\right].
\]

We next establish the formula for smooth compactly supported spatial
integrands.  Suppose \(g(h,\cdot)\in C_c^\infty(\mathbb R^m)\), all
supports lie in one compact set, and the required \(h\)-derivatives have
the same properties.  Fourier inversion and the Gaussian characteristic
function give

\[
 \mathbb E g(h,X_h)
 =\frac1{(2\pi)^m}\int_{\mathbb R^m}
   \widehat g(h,\zeta)e^{-\zeta^TC(h)\zeta/2}\,d\zeta.
 \tag{S.8}
\]

All derivatives through order five may be taken under the integral: every
such derivative is a finite sum of a polynomial in \(\zeta\), of degree at
most ten, times a Fourier transform of an \(h\)-derivative of \(g\).  To
obtain isotropic decay, choose an integer \(k\) with \(2k>m+10\).  For
every required \(h\)-derivative, Fourier transformation of
\((1-\Delta_x)^k\partial_h^jg\) gives

\[
 |\widehat{\partial_h^jg}(h,\zeta)|
 \le (1+\|\zeta\|^2)^{-k}
 \|(1-\Delta_x)^k\partial_h^jg(h,\cdot)\|_{L^1}.
\]

The \(L^1\)-norms on the right are uniformly bounded in \(h\), because
the supports lie in one compact set and all displayed derivatives are
continuous there.  Hence every differentiated Fourier integrand is
bounded by a constant times
\((1+\|\zeta\|)^{10}(1+\|\zeta\|^2)^{-k}\), which is integrable on
\(\mathbb R^m\).  Differentiating (S.8) once therefore yields

\[
 \frac d{dh}\mathbb E g(h,X_h)
 =\mathbb E\left[\partial_hg(h,X_h)
       +\frac12C'(h):D_x^2g(h,X_h)\right],
 \tag{S.9}
\]

because multiplication by \(-\zeta_a\zeta_b\) is the Fourier multiplier
of \(\partial_{ab}\).  No inverse of \(C(h)\) occurs.  Reapplying (S.9)
gives (S.4) for such \(g\), whether or not \(C(h)\) has full rank.

We now remove the compact-support and smoothness assumptions.  Choose
\(\vartheta\in C_c^\infty(\mathbb R^m)\) with \(0\le\vartheta\le1\),
\(\vartheta=1\) on \(\{\|x\|\le1\}\), and \(\vartheta=0\) on
\(\{\|x\|\ge2\}\), and put \(\vartheta_R(x)=\vartheta(x/R)\) for
\(R\ge1\).  Then

\[
 |D^\beta\vartheta_R(x)|\le c_\beta R^{-|\beta|}.
 \tag{S.10}
\]

Choose \(\varrho\in C_c^\infty(\mathbb R^m)\), \(\varrho\ge0\),
\(\int\varrho=1\), supported on \(\{\|y\|\le1\}\), and put
\(\varrho_\epsilon(y)=\epsilon^{-m}\varrho(y/\epsilon)\) for
\(0<\epsilon\le1\).  Set

\[
 \psi_{R,\epsilon}(h,x)
 =\varrho_\epsilon*\bigl(\vartheta_R\psi(h,\cdot)\bigr)(x).
 \tag{S.11}
\]

For fixed \(R\), this is spatially smooth and compactly supported.
Joint continuity in (S.1), hence uniform continuity on
\(I\times\{\|x\|\le2R+1\}\), shows that for every allowed \((j,\alpha)\),

\[
 \partial_h^jD_x^\alpha\psi_{R,\epsilon}
 \longrightarrow
 \partial_h^jD_x^\alpha(\vartheta_R\psi)
 \quad\text{uniformly on }I\times\mathbb R^m
 \tag{S.12}
\]

as \(\epsilon\downarrow0\).  Outside the common compact support both sides
vanish.  Moreover, Leibniz's rule, (S.2), and (S.10) give, uniformly in
\(R\ge1\),

\[
 \left|\partial_h^jD_x^\alpha(\vartheta_R\psi)(h,x)\right|
 \le A_{j,\alpha}(1+\|x\|)^P.
 \tag{S.13}
\]

Convolution changes the right side only by a factor at most \(2^P\), since
\(1+\|x-y\|\le2(1+\|x\|)\) on the support of the mollifier.

For clarity about repeated differentiation, induction on \(r\) in (S.3)
shows that each

\[
 \partial_h^jD_x^\alpha\Psi_r,
 \qquad r+j+\left\lceil\frac{|\alpha|}{2}\right\rceil\le5,
 \tag{S.14}
\]

is a finite sum of a derivative from (S.1) multiplied by entries of
\(C',\ldots,C^{(5)}\).  Indeed, \(\partial_h\) either differentiates such a
covariance factor or adds one \(h\)-derivative to the derivative of
\(\psi\), while \(D_x^2\) adds two spatial derivatives.  The weighted
order of the derivative of \(\psi\) can therefore increase by at most one
at each recursion.  All covariance factors are uniformly bounded on
\(I\).  Thus (S.12)--(S.13) imply, for every \(0\le r\le5\), uniform in
\(h\) convergence and domination of

\[
 \mathbb E\Psi_{r,R,\epsilon}(h,X_h)
 \longrightarrow
 \mathbb E\Psi_{r,R}(h,X_h)
 \quad(\epsilon\downarrow0),
 \tag{S.15}
\]

where the subscripts mean that the recursion starts from
\(\psi_{R,\epsilon}\) or \(\vartheta_R\psi\), respectively.

We use the following elementary closure fact twice.  If \(f_n\in C^k(I)\)
and \(f_n^{(r)}\to g_r\) uniformly for \(0\le r\le k\), then
\(g_0\in C^k(I)\) and \(g_0^{(r)}=g_r\).  To prove it, uniform limits make
all \(g_r\) continuous, and for \(1\le r\le k\),

\[
 f_n^{(r-1)}(h)-f_n^{(r-1)}(0)
 =\int_0^h f_n^{(r)}(t)\,dt
\]

passes uniformly to
\(g_{r-1}(h)-g_{r-1}(0)=\int_0^hg_r(t)\,dt\).  Hence
\(g_{r-1}'=g_r\), including the corresponding one-sided endpoint
statements.

Apply this closure fact to (S.15) and the already proved smooth formula.
It gives (S.4) with \(\psi\) replaced by \(\vartheta_R\psi\).

Finally, expanding a derivative of \(\vartheta_R\psi-\psi\) shows that it
is a sum of the following two types:

\[
 (\vartheta_R-1)\partial_h^jD_x^\alpha\psi,
 \qquad
 (D^\beta\vartheta_R)
 \partial_h^jD_x^{\alpha-\beta}\psi\quad(\beta\ne0).
\]

Both vanish on \(\{\|x\|<R\}\), and by (S.2), (S.10) they are bounded by
\(A'(1+\|x\|)^{P'}\mathbf1_{\{\|x\|\ge R\}}\), uniformly in \(h,R\).
The finite-sum representation (S.14) and the uniform tail estimate (S.7)
therefore give

\[
 \sup_{h\in I}\left|
 \mathbb E\Psi_{r,R}(h,X_h)-\mathbb E\Psi_r(h,X_h)
 \right|\longrightarrow0,
 \qquad 0\le r\le5.
 \tag{S.16}
\]

A second application of the closure fact proves (S.4).  This completes the
proof of Lemma S.1.

## 2. Why twelve activation derivatives suffice

We now verify the derivative budget for every chronological node of the DAG.
An **activation atom of order \(r\)** is an occurrence of
\(\phi^{(r)}(g)\) in a raw integrand; \(\phi(g)\) has order zero.  Scalar
coefficient tokens such as \(Q_{rq}^{[j]},K_{rq}^{[j]},\rho_{rq}^{[j]}\),
and \(\sigma_{rq}^{[j]}\) contain no activation atom in the current pass:
their regularity and numerical bounds have already been established in an
earlier chronological pass.

**Lemma S.2 (un differentiated integrands).**  At every finite time:

1. each raw state expression \(u_s,H_s,b_s,z_s,a_s,C_s\) contains no
   activation atom of order greater than one;
2. each Gram or terminal integrand \(H_rH_q\), \(C_rC_q\), and
   \(a_s\phi(z_s)\) contains no activation atom of order greater than one;
3. each response integrand \(\partial_{\chi_r}H_s\) and
   \(\partial_{\xi_r}C_s\) contains no activation atom of order greater
   than two.

**Proof.**  Treat the already constructed scalar coefficients as tokens.
Initially \(u_0=U\), \(H_0=\phi(U)\), \(z_0=\xi_0\), \(a_0=A\), and
\(C_0=A\phi'(\xi_0)\), so the assertion holds.  Suppose it holds through
time \(s\).  In

\[
 z_s=\xi_s+\sum_{r<s}(\rho_{sr}+hQ_{rs})C_r,
 \qquad
 a_s=A+h\sum_{r<s}\phi(z_r),
\]

the only new atom is \(\phi(z_r)\), of order zero; all atoms inside its
argument were already of order at most one.  Thus \(z_s,a_s\), and
\(C_s=a_s\phi'(z_s)\) have maximal atom order at most one.  Similarly,

\[
 b_s=\chi_s+\sum_{r\le s}\sigma_{sr}H_r
       +h\sum_{r<s}K_{rs}H_r,
 \qquad
 u_{s+1}=u_s+hb_s\phi'(u_s)
\]

introduce no atom above order one, and
\(H_{s+1}=\phi(u_{s+1})\) preserves this property.  This proves item 1 by
chronological induction, and products do not increase the maximum atom
order, proving item 2.  A single ambient-coordinate derivative obeys the
product and chain rules and replaces any atom \(\phi^{(r)}(g)\), when it
hits that atom, by \(\phi^{(r+1)}(g)\partial g\).  It therefore increases
the maximal atom order by at most one.  Applying this once to \(H_s\) or
\(C_s\) proves item 3.  The derivative is an ambient derivative on
\(\mathbb R^{s+1}\), so it remains well-defined when the Gaussian law is
supported on a proper subspace.  \(\square\)

**Lemma S.3 (compiler derivative budget).**  Let \(\psi\) be any Gram,
response, or terminal integrand in Lemma S.2, and define \(\Psi_r\) from it
as in (S.3).  Every expression requested by the compiler,

\[
 \partial_h^jD_x^\alpha\Psi_r,
 \qquad r+j+\left\lceil\frac{|\alpha|}{2}\right\rceil\le5,
 \tag{S.17}
\]

uses activation derivatives only through \(\phi^{(12)}\).

**Proof.**  One formal \(h\)- or spatial derivative increases the maximal
activation-atom order by at most one, by the same product/chain-rule
argument used in Lemma S.2.  Starting from \(\psi\), a term of
\(\partial_h^jD_x^\alpha\Psi_r\) applies at most

\[
 2r+j+|\alpha|
 \tag{S.18}
\]

formal derivatives to \(\psi\): each of the \(r\) Price recursions applies
either one \(h\)-derivative or two spatial derivatives, so counting two for
every recursion is an upper bound.  Put \(q=|\alpha|\).  From (S.17),

\[
 q\le2(5-r-j),
\]

and hence

\[
 2r+j+q\le2r+j+2(5-r-j)=10-j\le10.
 \tag{S.19}
\]

Lemma S.2 gives base activation order at most two, so (S.19) gives maximal
order at most \(2+10=12\).  Covariance derivatives and earlier scalar
tokens introduce no activation atom in the current pass.  Thus the guarded
recursion never requests \(\phi^{(13)}\).  \(\square\)

## 3. Joint continuity, envelopes, and chronological closure

Assume the activation class in Section 1 of `PROOF.md`:

\[
 \phi\in C^{12},\qquad
 |\phi(x)|\le M_\phi(1+|x|),\qquad
 \|\phi^{(r)}\|_\infty\le M_\phi\quad(1\le r\le12).
 \tag{S.20}
\]

At the first pass, every coefficient token is constant.  At a later pass,
all tokens and covariance entries were produced by earlier passes.  Suppose
chronologically that they are \(C^5\) and that their derivatives through
order five obey the numerical bounds already returned by (6.1).  Lemma S.3
and (S.20) imply that every mixed derivative requested in (S.17) exists and
is jointly continuous: it is a finite sum of products of continuous token
derivatives, raw Gaussian coordinates, and continuous
\(\phi^{(r)}\), \(r\le12\).

The same syntactic induction yields a uniform polynomial envelope.  Raw
coordinates have envelope \((1,1)\); bounded token derivatives have
envelope \((\bar S_j,0)\); sums and products use \(\oplus,\odot\);
\(\phi(g)\) has envelope \((M_\phi(1+A),p)\) when \(g\) has envelope
\((A,p)\); and \(\phi^{(r)}(g)\), \(r\ge1\), has envelope
\((M_\phi,0)\).  Repeated product and chain rules therefore produce exactly
the finite envelopes in (6.1).  Finiteness is not an assumption: for fixed
terminal time \(N\), there are \(2N\) internal passes and one terminal pass,
the index set in (S.17) is finite, and every differentiation creates a
finite sum.

Lemma S.1 consequently applies at the current pass, including at \(h=0\),
where the covariance is singular.  It proves that every newly produced Gram
entry or response coefficient is \(C^5\) and that its derivatives are
bounded by the compiler.  This is precisely the chronological induction
hypothesis for the next pass.  Beginning at the constant initial covariance
and iterating through the finite DAG proves

\[
 F_N\in C^5([-1,1]),
 \qquad
 |F_N^{(5)}(h)|\le\overline{\mathcal J}_{N,5}
 \quad(|h|\le1)
\]

for every fixed finite \(N\), without an inverse covariance, a continuity
modulus of the output, or an interchange of the width and learning-rate
limits.

There is therefore no remaining singular-covariance or activation-order
regularity gap in Sections 5--6.  This supplement makes no assertion about
the separate fixed-width identification or cubic-algebra obligations.
