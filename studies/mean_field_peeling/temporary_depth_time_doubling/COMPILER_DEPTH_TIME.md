# The depth--time singular-Price compiler

This note proves the analytic part of the depth--time comparison.  It does
not use a finite-width Taylor expansion.  The finite-width, fixed-step
identification is a separate theorem: once that theorem identifies the
network output with the inverse-free DAG below at every fixed nonzero step,
all bounds in this note apply to the width-first output.

Throughout, \(L,N\geq1\), \(G\sim N(0,1)\),

\[
 \phi\in C^{12}(\mathbb R),\qquad \mathbb E\phi(G)^2=1,
 \tag{1.1}
\]

and

\[
 M_\phi=\max\left\{1,
  \sup_x\frac{|\phi(x)|}{1+|x|},
  \max_{1\le r\le12}\|\phi^{(r)}\|_\infty\right\}<\infty .
 \tag{1.2}
\]

The branch \(\mathbb E\phi'(G)^2=0\) is treated in Section 9.

## 1. The inverse-free DAG at arbitrary depth and time

Write \(Z_{\ell s},X_{\ell s},D_{\ell s}\) for the preactivation,
activation, and cotangent at hidden layer \(\ell\) and time \(s\).  Put

\[
 Q^\ell_{rs}=\mathbb E[X_{\ell r}X_{\ell s}],\qquad
 K^\ell_{rs}=\mathbb E[D_{\ell r}D_{\ell s}].
 \tag{1.3}
\]

For each connector \(\ell=2,\ldots,L\), introduce independent centered
Gaussian source blocks \(\xi_\ell\) and \(\chi_\ell\), independent also
between connectors and directions, with

\[
 \mathbb E\xi_{\ell r}\xi_{\ell s}=Q^{\ell-1}_{rs},\qquad
 \mathbb E\chi_{\ell r}\chi_{\ell s}=K^\ell_{rs}.
 \tag{1.4}
\]

Let \(A,U\) be independent standard Gaussians, independent of these
blocks.  Define the response coefficients

\[
 \rho^\ell_{sr}
   =\mathbb E\,\partial_{\chi_{\ell r}}X_{\ell-1,s}
       \quad(0\le r<s),
 \qquad
 \sigma^\ell_{sr}
   =\mathbb E\,\partial_{\xi_{\ell r}}D_{\ell s}
       \quad(0\le r\le s),
 \tag{1.5}
\]

and

\[
 R^\ell_{sr}=\rho^\ell_{sr}+hQ^{\ell-1}_{rs}\quad(r<s),
 \tag{1.6}
\]

\[
 T^\ell_{sr}=\sigma^\ell_{sr}+hK^\ell_{rs}\quad(r<s),
 \qquad T^\ell_{ss}=\sigma^\ell_{ss}.
 \tag{1.7}
\]

The state recursion is

\[
 Z_{1,0}=U,\qquad X_{1,s}=\phi(Z_{1,s}),\qquad
 Z_{1,s+1}=Z_{1,s}+hD_{1,s},
 \tag{1.8}
\]

\[
 Z_{\ell s}=\xi_{\ell s}+\sum_{r<s}R^\ell_{sr}D_{\ell r},
 \qquad X_{\ell s}=\phi(Z_{\ell s}),
 \quad 2\le\ell\le L,
 \tag{1.9}
\]

\[
 A_s=A+h\sum_{r<s}X_{Lr},\qquad
 D_{Ls}=A_s\phi'(Z_{Ls}),
 \tag{1.10}
\]

and, downward for \(\ell=L-1,\ldots,1\),

\[
 H_{\ell s}=\chi_{\ell+1,s}
     +\sum_{r\le s}T^{\ell+1}_{sr}X_{\ell r},
 \qquad D_{\ell s}=H_{\ell s}\phi'(Z_{\ell s}).
 \tag{1.11}
\]

The terminal output is

\[
 F_{N,L}(h)=\mathbb E[A_NX_{LN}].
 \tag{1.12}
\]

There is no covariance inverse in (1.3)--(1.12).  Thus these equations
remain defined at \(h=0\), when every repeated-time source block has rank
one.

## 2. A complete chronological construction

The following action-by-action order makes (1.3)--(1.12) acyclic.  Before
time zero set \(Q^1_{00}=1\).

For each \(s=0,\ldots,N-1\):

1. In increasing order \(\ell=2,\ldots,L-1\), use the Gaussian block

   \[
   (\xi_{\ell,0:s},\chi_{\ell+1,0:s-1}),
   \qquad
   Q^{\ell-1}[s]\oplus K^{\ell+1}[s-1],
   \tag{2.1}
   \]

   where the second block is empty for \(s=0\).  Reconstruct
   \(D_{\ell r}\), \(r<s\), form \(Z_{\ell s},X_{\ell s}\), and compile
   the new row of \(Q^\ell[s]\) and all
   \(\rho^{\ell+1}_{sr}\), \(r<s\).

2. Use \((A,\xi_{L,0:s})\), with covariance
   \([1]\oplus Q^{L-1}[s]\), to form \(Z_{Ls},X_{Ls},A_s,D_{Ls}\).
   Compile the new row of \(K^L[s]\), all
   \(\sigma^L_{sr}\), \(r\le s\), and the intermediate output
   \(\mathbb E[A_sX_{Ls}]\).

3. In decreasing order \(\ell=L-1,\ldots,2\), use

   \[
   (\xi_{\ell,0:s},\chi_{\ell+1,0:s}),
   \qquad Q^{\ell-1}[s]\oplus K^{\ell+1}[s],
   \tag{2.2}
   \]

   to reconstruct the local histories, form \(D_{\ell s}\), and compile
   the new row of \(K^\ell[s]\) and all
   \(\sigma^\ell_{sr}\), \(r\le s\).

4. Use \((U,\chi_{2,0:s})\), with covariance
   \([1]\oplus K^2[s]\), to form \(D_{1s},Z_{1,s+1},X_{1,s+1}\).
   Compile the new row of \(Q^1[s+1]\) and all
   \(\rho^2_{s+1,r}\), \(r\le s\).

At terminal time \(N\), perform only items 1 and 2, stopping after
\(F_{N,L}\).  Empty layer ranges are omitted.  There are exactly

\[
 m_{L,N}=(2N+1)(L-1)
 \tag{2.3}
\]

Gaussian calls when \(L\ge2\).  Their dimensions are, respectively,
\(2s+1,s+2,2s+2,s+2\); the terminal interior and top dimensions are
\(2N+1\) and \(N+2\).  Hence every dimension is at most

\[
 D_N:=2N+2.
 \tag{2.4}
\]

This is deliberately an uncompressed construction: calls that can be
combined are left separate so that the order agrees exactly with the
\((2N+1)(L-1)\) predictable matrix-action chronology.  For \(L=1\), one
call on independent \((A,U)\) unrolls the scalar recursion

\[
 A_{s+1}=A_s+h\phi(Z_s),\qquad
 Z_{s+1}=Z_s+hA_s\phi'(Z_s),qquad0\le s<N.
 \tag{2.5}
\]

## 3. Singular Price differentiation

We record the inverse-free differentiation lemma used at every call.

**Lemma 3.1.**  Let \(I=[-1,1]\), let
\(C\in C^5(I;\mathbb S_+^d)\), and let \(\psi(h,x)\) have jointly
continuous mixed derivatives

\[
 \partial_h^jD_x^\alpha\psi,
 \qquad j+\left\lceil\frac{|\alpha|}{2}\right\rceil\le5.
 \tag{3.1}
\]

Suppose all these derivatives have one common bound
\(A(1+\|x\|)^p\).  If \(Y_h\sim N(0,C(h))\), then
\(G(h)=\mathbb E\psi(h,Y_h)\) is \(C^5\), including at rank changes,
and

\[
 G^{(r)}(h)=\mathbb E\Psi_r(h,Y_h),\qquad
 \Psi_0=\psi,\quad
 \Psi_{r+1}=\partial_h\Psi_r+\frac12C'(h):D_x^2\Psi_r.
 \tag{3.2}
\]

**Proof.**  Put \(C_\epsilon=C+\epsilon I\).  For
\(\epsilon>0\), differentiation of the Gaussian density followed by two
integrations by parts gives (3.2) once.  Iteration gives it through order
five.  Couple
\(Y_{\epsilon,h}=C_\epsilon(h)^{1/2}G_d\) and
\(Y_h=C(h)^{1/2}G_d\).  The positive-semidefinite square-root inequality
gives

\[
 \sup_{h\in I}\|C_\epsilon(h)^{1/2}-C(h)^{1/2}\|_{\rm op}
 \le\sqrt\epsilon .
 \tag{3.3}
\]

Writing \(v=\sup_h\sum_{a,b}|C_{ab}(h)|\), both variables are bounded by
\(\sqrt{v+1}\|G_d\|\) for \(0<\epsilon\le1\).  On
\(\{\|G_d\|\le R\}\), (3.3) and uniform continuity on compact sets give
uniform-in-\(h\) convergence of every derived integrand.  On the
complement, the common polynomial envelope is dominated by

\[
 A'(1+\sqrt{v+1}\|G_d\|)^{p'}
       \mathbf1_{\{\|G_d\|>R\}},
\]

whose expectation tends to zero as \(R\to\infty\).  First let
\(\epsilon\downarrow0\), then \(R\to\infty\), in the integrated
derivative identity.  Repeating this argument for the finitely many
derived integrands proves (3.2) through order five.  No inverse of
\(C(h)\) was used. \(\square\)

## 4. The exact finite compiler

An envelope is a pair \((A,p)\), meaning
\(|g(x)|\le A(1+\|x\|)^p\).  Use

\[
 (A,p)\oplus(B,q)=(A+B,\max\{p,q\}),\qquad
 (A,p)\odot(B,q)=(AB,p+q).
 \tag{4.1}
\]

On \(|h|\le1\), initialize

\[
 {\cal E}(1)={\cal E}(h)=(1,0),\qquad
 {\cal E}(x_i)=(1,1).
 \tag{4.2}
\]

If \({\cal E}(g)=(A,p)\), set

\[
 {\cal E}(\phi(g))=(M_\phi(1+A),p),\qquad
 {\cal E}(\phi^{(r)}(g))=(M_\phi,0),\quad1\le r\le12.
 \tag{4.3}
\]

Expand sums, products, and derivatives exactly.  If an earlier scalar node
\(S\) has already received bounds \(\bar S_0,\ldots,\bar S_5\), use
tokens \(S^{[j]}\) with

\[
 \partial_hS^{[j]}=S^{[j+1]},\qquad
 {\cal E}(S^{[j]})=(\bar S_j,0).
 \tag{4.4}
\]

The guard below prevents differentiating \(S^{[5]}\).

For one call

\[
 T(h)=\mathbb E_{Y\sim N(0,C(h))}\psi(h,Y),
 \tag{4.5}
\]

suppose

\[
 \bar c_j\ge\sup_{|h|\le1}\sum_{a,b}|C^{(j)}_{ab}(h)|,
 \qquad0\le j\le5.
 \tag{4.6}
\]

For ordered spatial multiindices of length \(q\), put

\[
 P^{(0)}_{j,q}
 =\bigoplus_{\mathbf i\in\{1,\ldots,d\}^q}
   {\cal E}(\partial_h^j\partial_{Y_{\mathbf i}}\psi),
 \qquad j+\lceil q/2\rceil\le5.
 \tag{4.7}
\]

Whenever \(r+j+\lceil q/2\rceil<5\), recurse by

\[
 P^{(r+1)}_{j,q}=P^{(r)}_{j+1,q}
 \oplus\bigoplus_{a=0}^j
 \left[
  \left(\frac12\binom ja\bar c_{a+1},0\right)
  \odot P^{(r)}_{j-a,q+2}
 \right].
 \tag{4.8}
\]

If \(P^{(r)}_{0,0}=(A_r,p_r)\), define

\[
 \overline{\cal J}_r(T)
 =A_r\mu_{d,p_r}(\bar c_0),
 \tag{4.9}
\]

where

\[
 \mu_{d,p}(v)=\sum_{q=0}^p\binom pqv^{q/2}2^{q/2}
       \frac{\Gamma((d+q)/2)}{\Gamma(d/2)}.
 \tag{4.10}
\]

Lemma 3.1 and Leibniz's rule prove

\[
 |T^{(r)}(h)|\le\overline{\cal J}_r(T),
 \qquad |h|\le1,\quad0\le r\le5.
 \tag{4.11}
\]

For a new covariance, sum the bounds of all its entries.  For (1.6) and
(1.7), use

\[
 \overline R_j=\bar\rho_j+\bar Q_j+j\bar Q_{j-1},\qquad
 \overline T_j=\bar\sigma_j+\bar K_j+j\bar K_{j-1},
 \qquad \bar Q_{-1}=\bar K_{-1}=0,
 \tag{4.12}
\]

with \(\overline T_{ss,j}=\bar\sigma_{ss,j}\).  Apply
(4.7)--(4.12), in the exact order of Section 2, to every new Gram entry,
response, full coefficient, and output.  This completely specifies the
compiler.

The index set in (4.7)--(4.8) is finite and has \(j+q\le10\).  An
undifferentiated state or Gram integrand contains activation atoms only of
order zero or one.  A response applies one ambient derivative and hence
has atom order at most two.  Each reachable term in (4.8) applies at most
\(2r+j+q\le10\) further formal derivatives.  Thus no derivative above
\(\phi^{(12)}\) is requested.  Equations (1.2), (4.1)--(4.4) give a
common polynomial envelope for every requested mixed derivative.
Chronological induction using Lemma 3.1 therefore proves

\[
 F_{N,L}\in C^5([-1,1]),\qquad
 |F_{N,L}^{(5)}(h)|\le\overline{\cal J}_5(F_{N,L}).
 \tag{4.13}
\]

This conclusion includes the singular covariance at \(h=0\).

## 5. A closed, shared-base majorant

We now replace the exact but lengthy bound (4.9) by one explicit exponent.
All quantities in this section are definitions by integer recursion.

Let \(D=D_N=2N+2\).  Define

\[
 R_{N,0}=1,\qquad
 R_{N,k+1}=16(N+2)(R_{N,k}+1),
 \quad0\le k<8(N+1),
 \tag{5.1}
\]

\[
 c_{N,0}=4(R_{N,8(N+1)}+1),
 \tag{5.2}
\]

and

\[
 c_{N,r+1}=64(D+1)^{10}(c_{N,r}+1)^2,
 \quad0\le r<24,
 \qquad C_N=c_{N,24}.
 \tag{5.3}
\]

Finally put

\[
 \nu_N=\mu_{D,C_N}((D+1)^2),
 \qquad
 \alpha_N=\left\lceil\log_2(2^{C_N}\nu_N)\right\rceil,
 \tag{5.4}
\]

\[
 p_N=2C_N,qquad r_N=C_N+\alpha_N.
 \tag{5.5}
\]

Every recursion has its upper index displayed, so these numbers are
computable and terminate.

**Lemma 5.1 (one-call majorant).**  Suppose all incoming scalar tokens and
all their derivatives through order five are bounded by \(S\ge2\), and
every covariance entry used in a call has the same bound.  Then every
number returned by that call is at most

\[
 B_\phi^{r_N}S^{p_N},
 \qquad B_\phi:=\max\{4,M_\phi\}.
 \tag{5.6}
\]

**Proof.**  Give leaves size one, unary activation nodes size one plus the
child size, and binary sums and products size one plus the child sizes.
Before measuring size, make the following expansion convention: an integer
coefficient \(m\) is replaced by \(|m|\) signed unit summands, every
binomial coefficient is expanded in this way, every covariance contraction
is expanded over its ordered coordinate pair, and (4.7) is expanded over
all ordered multiindices.  Thus no integer or dimension-dependent
multiplicity remains hidden in a scalar leaf.

A sum of at most \(2N+3\) monomials, each a product of at most three
already constructed expressions, has size at most
\(16(N+2)(R+1)\) if its inputs have size at most \(R\).  In any call of
Section 2, an interior forward or backward call reconstructs at most
\((Z_{\ell r},X_{\ell r},H_{\ell r},D_{\ell r})\) for each
\(0\le r\le s\); a top call reconstructs at most
\((Z_{Lr},X_{Lr},A_r,D_{Lr})\); and a bottom call reconstructs at most
\((Z_{1r},X_{1r},H_{1r},D_{1r})\).  Thus each matrix call uses at most
\(4(N+1)\) raw assignments.  In the \(L=1\) recursion, the four
assignments \(X_s=\phi(Z_s)\), \(D_s=A_s\phi'(Z_s)\), \(A_{s+1}\), and
\(Z_{s+1}\), together with the terminal activation, use fewer than
\(4(N+1)+2\le8(N+1)\) assignments.  Hence the
\(8(N+1)\) iterations in (5.1) cover every call, including \(L=1\).
A Gram or terminal product, or the expression before the one ambient
derivative defining a response, has size at most (5.2).

For a fully expanded expression \(e\), one formal derivative obeys

\[
 |\partial e|\le2(|e|+1)^2.
 \tag{5.7}
\]

This follows by structural induction from the product and chain rules.
There are at most ten mixed-derivative levels, one extra response
derivative, one aggregation of at most \(D^{10}\) ordered spatial
multiindices, at most five Price levels, and two coefficient/covariance
assembly levels.  At a Price level the expansion convention above gives
at most

\[
 1+D^2\sum_{a=0}^j\binom ja\le1+32D^2
 \tag{5.8}
\]

terms.  Thus one application of the map in (5.3) absorbs any one of these
operations.  The required number is at most

\[
 10+1+1+5+2=19<24.
\]

Consequently \(C_N\) bounds simultaneously the final syntax size, the
number of incoming-token leaves, and the polynomial-envelope exponent.
In particular, all integer, binomial, \(D^q\), and covariance-pair
multiplicities have already become syntax nodes before this conclusion.

If a tree has these three bounds, structural induction in (4.1)--(4.3)
gives envelope coefficient at most

\[
 (2B_\phi)^{C_N}S^{C_N}.
 \tag{5.9}
\]

The entrywise covariance norm is at most \((D+1)^2S\).  Since
\(S\ge1\), (4.10) gives

\[
 \mu_{d,C_N}((D+1)^2S)
 \le S^{C_N/2}\mu_{D,C_N}((D+1)^2)
 =S^{C_N/2}\nu_N
 \tag{5.10}
\]

for every \(d\le D\).  Multiplying (5.9) and (5.10), using
\(S^{3C_N/2}\le S^{2C_N}\), and using
\(2^{C_N}\nu_N\le B_\phi^{\alpha_N}\), proves (5.6). \(\square\)

At initialization put

\[
 d_\phi=\mathbb E\phi'(G)^2.
\]

The forward variances equal one and the cotangent variances are powers
\(d_\phi^j\), \(0\le j\le L\).  Since
\(d_\phi\le M_\phi^2\le B_\phi^2\), every initial token is bounded by
\(B_\phi^{2L}\).  Define

\[
 M_{L,N}=\begin{cases}
 (2N+1)(L-1),&L\ge2,\\
 1,&L=1,
 \end{cases}
 \tag{5.11}
\]

and

\[
 \boxed{
 E_{L,N}=2L\,p_N^{M_{L,N}}
   +r_N\frac{p_N^{M_{L,N}}-1}{p_N-1}.}
 \tag{5.12}
\]

Indeed, if \(S_m=B_\phi^{a_m}\), Lemma 5.1 gives

\[
 a_0=2L,\qquad a_{m+1}=r_N+p_Na_m,
 \tag{5.13}
\]

whose exact solution is (5.12).  Therefore

\[
 \boxed{
 \overline{\cal J}_5(F_{N,L})\le B_\phi^{E_{L,N}}.}
 \tag{5.14}
\]

All activation dependence in (5.14) is in the single base \(B_\phi\);
all depth and time dependence is the explicit integer \(E_{L,N}\).

**Lemma 5.2 (horizon monotonicity).**  For fixed \(L\),
\(E_{L,N}\) is nondecreasing in \(N\ge1\).

**Proof.**  Increase \(N\) by one.  The multiplier \(16(N+2)\) in
(5.1) increases and the number of iterations increases by eight, so
induction in \(k\) gives a no smaller terminal \(R\).  Thus \(c_{N,0}\)
does not decrease.  Both \(D_N\) and the multiplier in (5.3) increase;
induction through its 24 steps gives \(C_{N+1}\ge C_N\).

Couple \(G_{D_N}\) with the first \(D_N\) coordinates of
\(G_{D_{N+1}}\).  Since \(D_{N+1}\ge D_N\), \(C_{N+1}\ge C_N\), and
\(1+(D+1)\|G_D\|\ge1\), this coupling gives

\[
 \nu_{N+1}
 =\mathbb E[1+(D_{N+1}+1)\|G_{D_{N+1}}\|]^{C_{N+1}}
 \ge\nu_N.
\]

Hence \(\alpha_N,p_N,r_N\) are nondecreasing.  For \(L\ge2\), the call
count \(M_{L,N}\) also increases; for \(L=1\) it remains one.  Finally,
(5.12) is the value after \(M_{L,N}\) iterations of
\(a\mapsto r_N+p_Na\), starting at \(2L\).  This map is increasing in
\(a,p_N,r_N\) and maps positive numbers upward.  Increasing its
parameters and applying it no fewer times cannot decrease the result.
Thus \(E_{L,N+1}\ge E_{L,N}\). \(\square\)

## 6. Exact activation-integral jets

The exact counterpart of the envelope compiler is also finite.  In every
call (4.5), set

\[
 {\cal P}_C=\partial_h+\frac12C'(h):D_Y^2,
 \qquad \Psi_0=\psi,\qquad \Psi_{r+1}={\cal P}_C\Psi_r.
 \tag{6.1}
\]

Earlier scalar tokens obey

\[
 \partial_hS^{[j]}=S^{[j+1]},\qquad
 S^{[j]}\big|_{h=0}={\cal J}_j(S),
 \tag{6.2}
\]

and, in the order of Section 2,

\[
 {\cal J}_r(T)=
 \mathbb E_{Y\sim N(0,C(0))}\Psi_r(0,Y),
 \qquad0\le r\le5.
 \tag{6.3}
\]

This defines \({\cal J}_r\) before identifying it as a derivative.
Lemma 3.1 subsequently proves

\[
 {\cal J}_r(T)=T^{(r)}(0).
 \tag{6.4}
\]

At \(h=0\), every time block coalesces.  It may be represented using
independent standard Gaussians

\[
 A,G_1,\ldots,G_L,B_1,\ldots,B_{L-1},
 \tag{6.5}
\]

with every forward source at layer \(\ell\) equal to \(G_\ell\) and
each backward source equal to its initialization standard deviation times
\(B_{\ell-1}\).  Expanding (6.1)--(6.3) therefore reduces every jet to a
finite sum of products of elementary moments

\[
 I_{a,\boldsymbol\beta}(\phi)
 =\mathbb E\left[G^a
    \prod_{r=0}^{12}\phi^{(r)}(G)^{\beta_r}\right]
 \tag{6.6}
\]

and ordinary Gaussian moments of \(A,B_1,\ldots,B_{L-1}\).  Equations
(2.1)--(2.5) and (6.1)--(6.3) are a completely specified terminating
formula for those activation integrals; there are \(M_{L,N}\) calls and
only five Price iterations per call.

## 7. Parity and the linear clock

Under

\[
 h\mapsto-h,qquad A\mapsto-A,qquad
 \chi_{\ell s}\mapsto-\chi_{\ell s},
 \tag{7.1}
\]

with all forward sources fixed, induction through (1.6)--(1.11) leaves
\(Z,X,Q,K\) fixed and changes the sign of
\(A_s,D,H,\rho,R,\sigma,T\).  The primitive Gaussian laws are invariant,
so

\[
 F_{N,L}(-h)=-F_{N,L}(h).
 \tag{7.2}
\]

For completeness, the first-order exact compiler has the following clock
identity.  Put

\[
 \Theta_L=\sum_{j=0}^L d_\phi^j.
 \tag{7.3}
\]

**Lemma 7.1 (nodewise clock identity).**

\[
 {\cal J}_1(F_{N,L})=N\Theta_L.
 \tag{7.4}
\]

**Proof.**  Fully expand (6.1)--(6.3), and
mark the primitive update factor \(h\) at which a first derivative lands.
Induction over the chronological calls proves that every first-jet term
has exactly one mark.  Indeed, \(\partial_h\) either marks an explicit
factor in (1.6)--(1.11), or differentiates one earlier scalar token;
the latter already has exactly one mark by induction.  The covariance
part of (6.1) differentiates one earlier Gram entry and therefore carries
the unique mark of that Gram.  It creates no new kind of term.

At \(h=0\), all time copies of a source coalesce and all unmarked update
maps are identities.  Every response has zeroth jet zero.  This last fact
is also nodewise: \(X_{\ell-1,s}\) has no dependence on a backward source
when all explicit update edges are set to zero; for \(r<s\),
\(D_{\ell s}\) has no dependence on \(\xi_{\ell r}\); and for \(r=s\)
the derivative contains one centered independent upper carrier (at the
top, that carrier is \(A\)).  Its expectation is zero.  Consequently,
deleting the unmarked time slices is a bijection from terms marked in time
slice \(r\) to terms marked in time slice zero: the state immediately
before the mark is the initialization state, and after the mark it is
merely reevaluated by zero-step forward/backward sweeps.  This bijection
also preserves the Price contraction, because a covariance-mark term is,
by the preceding induction, the Gram of the same marked state term.
There are exactly \(N\) possible marked slices.

It remains to evaluate the single marked slice.  The readout edge gives

\[
 \mathbb E X_{L0}^2=1.
\]

For the matrix edge from layer \(\ell-1\) to \(\ell\),
\(2\le\ell\le L\), the response contraction gives

\[
 Q^{\ell-1}_{00}K^\ell_{00}
 =1\cdot d_\phi^{L-\ell+1}.
\]

The bottom-vector edge gives \(K^1_{00}=d_\phi^L\).  These identities
follow directly downward from
\(D_{L0}=A\phi'(G_L)\): each additional layer contributes the independent
factor \(\mathbb E\phi'(G)^2=d_\phi\), while every initialization feature
Gram is one by (1.1).  Thus a marked slice contributes
\(1+d_\phi+\cdots+d_\phi^L=\Theta_L\).  Multiplication by its \(N\)
possible locations proves (7.4) entirely inside the exact Price compiler.
\(\square\)

In particular, (7.2)--(7.4) give

\[
 F_{N,L}(0)=F_{N,L}^{(2)}(0)=F_{N,L}^{(4)}(0)=0,
 \qquad F_{N,L}'(0)=N\Theta_L.
 \tag{7.5}
\]

## 8. The quantitative time-doubling remainder

For \(t\ge1\), define the activation-integral coefficient

\[
 \boxed{
 \kappa_{\phi,L,t}
 =\frac{8{\cal J}_3(F_{t,L})-{\cal J}_3(F_{2t,L})}{6}.}
 \tag{8.1}
\]

This is the finite Gaussian recursion of Section 6, not a definition in
terms of an unknown output derivative.  Only after the recursion is
constructed does (6.4) identify it with the cubic jet.

Apply Taylor's formula with integral remainder separately to
\(F_{t,L}(2\eta)\) and \(F_{2t,L}(\eta)\).  The constant and even terms
vanish by (7.5), and the linear terms cancel because
\(2t\Theta_L=2t\Theta_L\).  Hence

\[
 \begin{aligned}
 &\left|F_{t,L}(2\eta)-F_{2t,L}(\eta)
       -\kappa_{\phi,L,t}\eta^3\right|\\
 &\qquad\le
 \frac{32\overline{\cal J}_5(F_{t,L})
       +\overline{\cal J}_5(F_{2t,L})}{120}|\eta|^5.
 \end{aligned}
 \tag{8.2}
\]

Every recursion in (5.1)--(5.5) is nondecreasing in \(N\); so are
\(M_{L,N}\) and the closed expression (5.12).  Thus the horizon \(2t\)
majorant bounds both terminal times \(t\) and \(2t\).  Since
\(33/120<1\), (5.14) gives

\[
 \boxed{
 \left|F_{t,L}(2\eta)-F_{2t,L}(\eta)
       -\kappa_{\phi,L,t}\eta^3\right|
 \le B_\phi^{E_{L,2t}}|\eta|^5,
 \qquad |\eta|\le\frac12.}
 \tag{8.3}
\]

Thus a shared activation-only pair may be taken as

\[
 \boxed{B_\phi=\max\{4,M_\phi\},\qquad
 h_\phi=(2B_\phi)^{-1}.}
 \tag{8.4}
\]

The deliberately conservative shared-base version is

\[
 \boxed{
 \left|F_{t,L}(2\eta)-F_{2t,L}(\eta)
       -\kappa_{\phi,L,t}\eta^3\right|
 \le B_\phi^{E_{L,2t}}|\eta|^5,
 \qquad |\eta|\le h_\phi^{E_{L,2t}}.}
 \tag{8.5}
\]

For the requested three-hidden-layer testbed, (5.11)--(5.12) become the
literal formula

\[
 \boxed{
 E_{3,2t}=6p_{2t}^{8t+2}
   +r_{2t}\frac{p_{2t}^{8t+2}-1}{p_{2t}-1}.}
 \tag{8.5a}
\]

Thus (8.5) at \(L=3\) has no hidden depth or time constant: its only
activation-dependent base is \(B_\phi\), and its exact numerical exponent
is (8.5a).

Consequently, for every \(\varepsilon>0\),

\[
 |F_{t,L}(2\eta)-F_{2t,L}(\eta)|
 \le(|\kappa_{\phi,L,t}|+\varepsilon)|\eta|^3
 \tag{8.6}
\]

whenever

\[
 |\eta|\le
 \min\left\{h_\phi^{E_{L,2t}},
 \sqrt{\frac{\varepsilon}{1+B_\phi^{E_{L,2t}}}}\right\}.
 \tag{8.7}
\]

No constant in (8.3)--(8.7) is defined through a supremum of an output,
a trained trajectory, or an unspecified continuity modulus.

## 9. Constant activation

If \(d_\phi=0\), continuity and Gaussian full support imply
\(\phi'\equiv0\).  By (1.1), \(\phi\equiv\pm1\).  Every hidden feature
is fixed and only the readout moves, so

\[
 F_{N,L}(h)=Nh.
\]

Therefore \(F_{t,L}(2\eta)-F_{2t,L}(\eta)=0\) identically.  On this
branch one may take \(\kappa_{\phi,L,t}=0\), remainder constant zero, and
radius arbitrary.

## 10. Scope audit

The note proves, for the inverse-free width-first DAG:

* singular-covariance \(C^5\) regularity for every finite \((L,N)\);
* a terminating exact Gaussian activation-integral formula for the cubic
  coefficient;
* the explicit shared-base fifth-order bound (8.5), with all \((L,t)\)
  dependence in (5.1)--(5.5), (5.11)--(5.12).

It does **not** prove that the finite-width network converges to this DAG at
fixed nonzero \(h\).  In particular, adaptive reused-matrix conditioning,
population-history rank, stopping removal, concentration, and terminal
uniform integrability are not consequences of the Price compiler.  The
network theorem is unconditional only after those independent bridges are
proved for the full depth--time chronology.
