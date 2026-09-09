# Quantitative half-step theorem for three hidden layers

## Theorem

Let \(x=1\), and let all three hidden layers have width \(n\).  Initialize

\[
u_j^0,\;W_{ij}^0,\;V_{\alpha i}^0,\;a_\alpha^0
\stackrel{\mathrm{iid}}{\sim}N(0,1).
\]

Assume

\[
\phi\in C^{12}(\mathbb R),\qquad
\mathbb E\phi(Z)^2=1,\qquad Z\sim N(0,1),
\]

and

\[
M_\phi=
\max\left\{
1,\;
\sup_x\frac{|\phi(x)|}{1+|x|},\;
\max_{1\le r\le12}\|\phi^{(r)}\|_\infty
\right\}<\infty .
\tag{T.1}
\]

Write

\[
d=\mathbb E\phi'(Z)^2.
\tag{T.1a}
\]

For the exact feature-ascent dynamics in Section 1, let

\[
F_{k,n}(h)=\mathbb E f_n^k .
\]

At every fixed \(h\), take width first:

\[
F_k(h)=\lim_{n\to\infty}F_{k,n}(h).
\tag{T.2}
\]

The limit in (T.2) exists at all arguments used below.  Define

\[
\Delta(\eta)=F_2(\eta)-F_1(2\eta).
\]

Sections 2--7 construct, using only \(M_\phi\), finitely many
finite-dimensional Gaussian activation integrals, and explicit Gaussian
moments, numbers

\[
\kappa_\phi,\qquad B_\phi<\infty,\qquad h_\phi>0
\]

for which

\[
\boxed{
\left|\Delta(\eta)-\kappa_\phi\eta^3\right|
\le B_\phi|\eta|^5,
\qquad |\eta|\le h_\phi .
}
\tag{T.3}
\]

In particular, for every \(\varepsilon>0\),

\[
|\eta|\le
\eta_0(\phi,\varepsilon)
:=
\min\left\{
h_\phi,\sqrt{\frac{\varepsilon}{1+B_\phi}}
\right\}
\tag{T.4}
\]

implies

\[
\boxed{
|F_2(\eta)-F_1(2\eta)|
\le (|\kappa_\phi|+\varepsilon)|\eta|^3 .
}
\tag{T.5}
\]

The coefficient is not defined from an unknown output derivative.
Section 5.1 gives a seven-call exact Price-jet recursion, specifies every
Gaussian covariance and integrand in that recursion, and sets

\[
\boxed{\kappa_\phi:=\kappa_\phi^{\mathrm{PJ}}}
\tag{T.6}
\]

by formula (5.24).  At the singular point \(h=0\), every call is an
explicit Gaussian integral of \(\phi,\ldots,\phi^{(8)}\); the recursion
terminates after finitely many differentiations and arithmetic operations.
Only after constructing this activation-only number does (5.25) identify
it with the cubic jet of the limiting discrepancy.

## 1. Exact finite-width network

At time \(s\), define

\[
H_j^s=\phi(u_j^s),
\qquad
z_i^s=\frac1{\sqrt n}\sum_jW_{ij}^sH_j^s,
\qquad
G_i^s=\phi(z_i^s),
\]

\[
y_\alpha^s=\frac1{\sqrt n}\sum_iV_{\alpha i}^sG_i^s,
\qquad
f_n^s=\frac1n\sum_\alpha a_\alpha^s\phi(y_\alpha^s).
\tag{1.1}
\]

Write

\[
C_\alpha^s=a_\alpha^s\phi'(y_\alpha^s),\qquad
d_i^s=\frac1{\sqrt n}\sum_\alpha V_{\alpha i}^sC_\alpha^s,
\]

\[
E_i^s=d_i^s\phi'(z_i^s),\qquad
b_j^s=\frac1{\sqrt n}\sum_iW_{ij}^sE_i^s.
\tag{1.2}
\]

One simultaneous recomputed ascent step is

\[
\theta^{s+1}=\theta^s+hn\nabla_\theta f_n^s.
\tag{1.3}
\]

Direct differentiation gives the exact updates

\[
\begin{aligned}
a^{s+1}&=a^s+h\phi(y^s),\\
V^{s+1}&=V^s+\frac h{\sqrt n}C^s(G^s)^T,\\
W^{s+1}&=W^s+\frac h{\sqrt n}E^s(H^s)^T,\\
u^{s+1}&=u^s+h\,b^s\phi'(u^s).
\end{aligned}
\tag{1.4}
\]

Let \(W=W^0\), \(V=V^0\), and use

\[
Q^H_{rs}=\frac1n(H^r)^TH^s,\quad
Q^G_{rs}=\frac1n(G^r)^TG^s,\quad
K^E_{rs}=\frac1n(E^r)^TE^s,\quad
K^C_{rs}=\frac1n(C^r)^TC^s .
\]

For \(P\in\{H,G\}\) and \(R\in\{E,C\}\), use the block notation

\[
Q_P^{[m]}=(Q^P_{rs})_{0\le r,s\le m},\qquad
K_R^{[m]}=(K^R_{rs})_{0\le r,s\le m}.
\]

The learned pieces separate from the reused Gaussian matrices exactly:

\[
\begin{aligned}
z^s&=\frac{WH^s}{\sqrt n}
   +h\sum_{r<s}Q^H_{rs}E^r,\\
y^s&=\frac{VG^s}{\sqrt n}
   +h\sum_{r<s}Q^G_{rs}C^r,\\
d^s&=\frac{V^TC^s}{\sqrt n}
   +h\sum_{r<s}K^C_{rs}G^r,\\
b^s&=\frac{W^TE^s}{\sqrt n}
   +h\sum_{r<s}K^E_{rs}H^r.
\end{aligned}
\tag{1.5}
\]

No current-time term occurs in any sum.

## 2. Width-first Gaussian operator DAG

Introduce mutually independent centered Gaussian source blocks

\[
\xi_{0:2},\quad \chi_{0:1},\quad
\zeta_{0:2},\quad\omega_{0:1},
\]

independent also of \(U,A\sim N(0,1)\), with

\[
\operatorname{Cov}(\xi_r,\xi_s)=Q^H_{rs},\qquad
\operatorname{Cov}(\chi_r,\chi_s)=K^E_{rs},
\]

\[
\operatorname{Cov}(\zeta_r,\zeta_s)=Q^G_{rs},\qquad
\operatorname{Cov}(\omega_r,\omega_s)=K^C_{rs}.
\tag{2.1}
\]

These blocks are extended chronologically, after the relevant Gram has
already been computed.  Set \(u_0=U\), \(H_s=\phi(u_s)\).  For
\(s=0,1,2\), define

\[
\rho^W_{sr}=\mathbb E[\partial_{\chi_r}H_s]\quad(r<s),
\]

\[
z_s=\xi_s+\sum_{r<s}(\rho^W_{sr}+hQ^H_{rs})E_r,
\qquad G_s=\phi(z_s),
\tag{2.2}
\]

\[
\rho^V_{sr}=\mathbb E[\partial_{\omega_r}G_s]\quad(r<s),
\]

\[
y_s=\zeta_s+\sum_{r<s}(\rho^V_{sr}+hQ^G_{rs})C_r,
\]

\[
a_s=A+h\sum_{r<s}\phi(y_r),\qquad
C_s=a_s\phi'(y_s).
\tag{2.3}
\]

For \(s=0,1\), define

\[
\sigma^V_{sr}=\mathbb E[\partial_{\zeta_r}C_s]\quad(r\le s),
\]

\[
d_s=\omega_s+\sum_{r\le s}\sigma^V_{sr}G_r
       +h\sum_{r<s}K^C_{rs}G_r,
\qquad E_s=d_s\phi'(z_s),
\tag{2.4}
\]

\[
\sigma^W_{sr}=\mathbb E[\partial_{\xi_r}E_s]\quad(r\le s),
\]

\[
b_s=\chi_s+\sum_{r\le s}\sigma^W_{sr}H_r
       +h\sum_{r<s}K^E_{rs}H_r,
\]

\[
u_{s+1}=u_s+h\,b_s\phi'(u_s).
\tag{2.5}
\]

Every Gram in (2.1)--(2.5) is the expectation of the corresponding
displayed scalar fields.  The order

\[
H_0,G_0,C_0,E_0,H_1,G_1,C_1,E_1,H_2,G_2,y_2
\]

makes the construction acyclic.  It uses no inverse covariance and is
therefore defined also at \(h=0\).  Its outputs are

\[
F_1(h)=\mathbb E[a_1\phi(y_1)],\qquad
F_2(h)=\mathbb E[a_2\phi(y_2)].
\tag{2.6}
\]

At time zero,

\[
Q^H_{00}=Q^G_{00}=1,\qquad K^C_{00}=d,\qquad K^E_{00}=d^2.
\tag{2.7}
\]

## 3. Fixed-\(h\) identification of the actual network

The raw actions of the two independent reused matrices occur in the
predictable order

\[
\frac{WH^0}{\sqrt n},\
\frac{VG^0}{\sqrt n},\
\frac{V^TC^0}{\sqrt n},\
\frac{W^TE^0}{\sqrt n},\
\frac{WH^1}{\sqrt n},\
\frac{VG^1}{\sqrt n},\
\frac{V^TC^1}{\sqrt n},\
\frac{W^TE^1}{\sqrt n},\
\frac{WH^2}{\sqrt n},\
\frac{VG^2}{\sqrt n}.
\tag{3.1}
\]

In particular, \(H^1\) is not independent of the column of \(W\) already
used in \(W^TE^0\), and \(G^1\) is not independent of the corresponding
history of \(V\).

### Lemma 3.1: two-matrix adaptive conditioning

Let \(M_1,M_2\) be independent standard Gaussian matrices.  Interlace any
finite predictable sequence of row and transpose actions of the two
matrices.  Conditional on the global revealed filtration, the unrevealed
parts have the joint form

\[
P_{C_\ell}^{\perp}\widetilde M_\ell P_{H_\ell}^{\perp},
\qquad \ell=1,2,
\tag{3.2}
\]

where the two \(\widetilde M_\ell\) remain conditionally independent
standard Gaussian matrices.

To prove this, decompose the next predictable query into its old-span and
orthogonal components.  Revealing a row action exposes one Gaussian
projection of the chosen residual and leaves its orthogonal complement
Gaussian; a transpose action is the transposed argument.  Because the
query is already measurable and the other residual is conditionally
independent, revealing the chosen projection gives no additional
information about the other residual.  Induction over the finite action
list proves (3.2).

For one matrix, if old row and transpose queries are the columns of
\(H,C\), put

\[
Y=MH/\sqrt n,\quad D=M^TC/\sqrt n,\quad
Q=H^TH/n,\quad K=C^TC/n,\quad {\cal R}=C^TY/n.
\]

Orthogonal projection of (3.2) gives, for a new transpose query \(c\),

\[
\frac{M^Tc}{\sqrt n}
=DK^{-1}k+HQ^{-1}(r-{\cal R}^TK^{-1}k)
+\tau_cP_H^\perp g,
\tag{3.3}
\]

\[
k=C^Tc/n,\qquad r=Y^Tc/n,\qquad
\tau_c^2=c^Tc/n-k^TK^{-1}k.
\]

For a new row query \(q_*\),

\[
\frac{Mq_*}{\sqrt n}
=YQ^{-1}q+CK^{-1}(v-{\cal R}Q^{-1}q)
+\tau_qP_C^\perp g,
\tag{3.4}
\]

\[
q=H^Tq_*/n,\qquad v=D^Tq_*/n,\qquad
\tau_q^2=q_*^Tq_*/n-q^TQ^{-1}q.
\]

The complete proof, including the singular-span version with orthogonal
projectors, is in WIDTH_DAG.md, Section 4.

### Lemma 3.2: all response terms

Suppose, at a representative coordinate for either matrix, the already
identified actions have the form

\[
y=\xi+Pc,\qquad d=\chi+Sh,
\]

with \(Q=\mathbb E[hh^T]\), \(K=\mathbb E[cc^T]\).  Singular Gaussian
integration by parts gives

\[
{\cal R}:=\mathbb E[cy^T]=SQ+KP^T.
\tag{3.5}
\]

For a new row query \(H_*\), put

\[
q=\mathbb E[hH_*],\qquad
\rho=\mathbb E[\nabla_\chi H_*].
\]

Then

\[
\mathbb E[dH_*]=K\rho+Sq.
\]

Substitution into (3.4) cancels both old-span terms and leaves exactly

\[
\xi_*+\rho^Tc.
\tag{3.6}
\]

For a new transpose query \(C_*\), put

\[
k=\mathbb E[cC_*],\qquad
\sigma=\mathbb E[\nabla_\xi C_*].
\]

Then

\[
\mathbb E[yC_*]=Q\sigma+Pk.
\]

Substitution into (3.3) cancels the two old-span terms and leaves exactly

\[
\chi_*+\sigma^Th.
\tag{3.7}
\]

Applying (3.6)--(3.7) alternately to \(W\) and \(V\) produces every
\(\rho^W,\sigma^W,\rho^V,\sigma^V\) in (2.2)--(2.5).  This explicitly
handles the dependence of \(H^1\) and \(G^1\) on reused columns.

### Lemma 3.3: concentration and uniform integrability

Assume the four two-time population Grams

\[
Q_H^{[1]},\quad Q_G^{[1]},\quad K_C^{[1]},\quad K_E^{[1]}
\tag{3.8}
\]

are positive definite at a fixed \(h\ne0\).  Couple every residual
innovation in (3.1) to one compatible iid Gaussian array.  Stop the proof
representation when an empirical nonterminal Gram eigenvalue is less than
half its population value.

On the stopped event:

1. the regression maps (3.3)--(3.4) are Lipschitz because
   \(\|A^{-1}-B^{-1}\|\le\|A^{-1}\|\|A-B\|\|B^{-1}\|\);
2. the unwanted fixed-rank projection obeys
   \[
   \left\|\|P_Lg\|_{n,p}\right\|_{L^s}
   \le \frac{C}{\sqrt n}\sum_j\|L_j\|_{n,p};
   \]
3. every iid ideal empirical observable concentrates by Rosenthal's
   inequality;
4. the activation envelope transfers each field error through the next
   scalar node by Hölder's inequality.

Executing these four estimates in the ten explicit actions (3.1) proves
convergence of every field, Gram, raw overlap, regression coefficient, and
innovation scale.  At the two terminal forward actions, a possibly zero
Schur complement is handled by

\[
|\sqrt x-\sqrt y|\le\sqrt{|x-y|}.
\]

No three-time Gram is inverted.

Arbitrarily high moment versions of the same estimates make the stopping
failure probability \(O(n^{-M})\) for every fixed \(M\).  Direct energy
majorants for (1.4), together with Gaussian operator-norm tails for
\(W/\sqrt n,V/\sqrt n\), give all raw-network moments needed to remove the
stopping.  In particular the terminal outputs are uniformly integrable.

This is not an appeal to a state-evolution theorem: the ten-action ledger,
the compatible coupling, every empirical conditioning input, the stopping
argument, and the energy recursion are proved in WIDTH_DAG.md, Sections
7--8.  Consequently, at every fixed nonzero \(h\) satisfying (3.8),

\[
\lim_{n\to\infty}F_{2,n}(h)=F_2(h).
\tag{3.9}
\]

The six-action prefix needed for \(F_1(h)\) uses only the positive
time-zero variances \(1,d,d^2\), so

\[
\lim_{n\to\infty}F_{1,n}(h)=F_1(h)
\tag{3.10}
\]

for every fixed \(h\) in the compiler interval.  At \(h=0\), both limits
are zero by the exact network.

## 4. Explicit punctured-rank interval

Assume \(d>0\).  For \(Z\sim N(0,1)\), define the activation moments

\[
\begin{gathered}
u=\mathbb E\phi'(Z)^4,\qquad
v=\mathbb E[\phi(Z)\phi''(Z)],\qquad
m=\mathbb E[\phi(Z)\phi'(Z)^2\phi''(Z)],\\
r=\mathbb E[\phi'(Z)\phi'''(Z)],\qquad
s=\mathbb E\phi''(Z)^2,\qquad
e=\mathbb E[\phi'(Z)^2\phi''(Z)^2],\\
\ell=\mathbb E[\phi(Z)^2\phi'(Z)^2].
\end{gathered}
\tag{4.0}
\]

Define

\[
c_1=1+d,\qquad
\nu_H=d^2u,
\tag{4.1}
\]

\[
\nu_G=du(d^2+c_1^2),\qquad
c_2=1+d+d^2,
\tag{4.2}
\]

\[
\tau_C=\ell+2c_2m+3c_2^2e+\nu_Gs,
\tag{4.3}
\]

\[
k_C=2d+v+c_2(r+s),
\tag{4.4}
\]

\[
\tau_E
=d\tau_C+k_C^2\ell+\nu_Hds
+3c_1^2d^2e+2k_Cc_1dm.
\tag{4.5}
\]

Direct \(L^2\) differentiation of the inverse-free DAG gives

\[
\begin{array}{c|c}
\text{Gram}&\displaystyle
\lim_{h\to0}\frac{\det\operatorname{Gram}(h)}{h^2}\\ \hline
Q_H^{[1]}&\nu_H\\
Q_G^{[1]}&\nu_G\\
K_C^{[1]}&d\tau_C\\
K_E^{[1]}&d^2\tau_E.
\end{array}
\tag{4.6}
\]

For completeness, the four tangent variables yielding (4.6) are

\[
P_H=X\phi'(U)^2,\qquad X\sim N(0,d^2),
\]

\[
R_z=\sqrt{\nu_H}\varepsilon_H+c_1\Omega\phi'(Z),\qquad
P_G=\phi'(Z)R_z,\qquad \Omega\sim N(0,d),
\]

\[
R_y=\sqrt{\nu_G}\varepsilon_G+c_2A\phi'(Y),
\qquad
T_C=\phi(Y)\phi'(Y)+A\phi''(Y)R_y,
\]

\[
\begin{aligned}
T_E={}&\sqrt{\tau_C}\varepsilon_C\phi'(Z)
+k_C\phi(Z)\phi'(Z)\\
&+\sqrt{\nu_H}\,\Omega\varepsilon_H\phi''(Z)
+c_1\Omega^2\phi'(Z)\phi''(Z),
\end{aligned}
\tag{4.7}
\]

where \(\varepsilon_H,\varepsilon_G,\varepsilon_C\sim N(0,1)\), and all
displayed base Gaussians are independent.  The initial vectors are
orthogonal in \(L^2\) to their tangents, and

\[
\mathbb EP_H^2=\nu_H,\quad
\mathbb EP_G^2=\nu_G,\quad
\mathbb ET_C^2=\tau_C,\quad
\mathbb ET_E^2=\tau_E.
\]

The \(\varepsilon_G\)-component proves \(\tau_C>0\) when
\(\mathbb E\phi''(Z)^2>0\); otherwise \(\phi\) is affine and
\(\tau_C=d>0\).  The fresh \(\varepsilon_C\)-component then gives
\(\tau_E\ge d\tau_C>0\).  Hence all four coefficients in (4.6) are
strictly positive.

Let the explicit envelope compiler in Section 5 produce derivative bounds
\(\bar G_{rs,j}\) for every one of these four Grams.  For
\(G=Q_H,Q_G,K_C,K_E\), let \(g_0=1,1,d,d^2\), respectively, and define

\[
D_G
=g_0\bar G_{11,4}
+\sum_{a=0}^4\binom4a\bar G_{01,a}\bar G_{01,4-a}.
\tag{4.8}
\]

If \(a_G\) denotes the corresponding coefficient in (4.6), put

\[
R_G=\min\left\{1,\sqrt{\frac{12a_G}{1+D_G}}\right\},
\]

\[
\boxed{
h_\phi
=\min\left\{\frac12,R_{Q_H},R_{Q_G},R_{K_C},R_{K_E}\right\}.
}
\tag{4.9}
\]

Parity makes every Gram even.  Taylor's formula and (4.8) give

\[
|\det G(h)-a_Gh^2|\le\frac{D_G}{24}|h|^4.
\]

Therefore

\[
\det G(h)\ge\frac12a_Gh^2>0
\qquad(0<|h|\le h_\phi).
\tag{4.10}
\]

Combining (4.10) with Section 3 proves the actual fixed-\(h\), width-first
identification throughout the required punctured interval.  Notice that
the inverse bound is allowed to deteriorate as \(h\to0\): width is sent to
infinity separately at each fixed nonzero \(h\).

## 5. Singular-covariance regularity and the constants

This section specifies the finite algorithm producing all bars in (4.8)
and the fifth-order output bounds.  It never uses a supremum of \(F_1\),
\(F_2\), or their derivatives as a definition.

An envelope pair \((A,p)\) means

\[
|g(x)|\le A(1+\|x\|)^p.
\]

Use

\[
(A,p)\oplus(B,q)=(A+B,\max\{p,q\}),\qquad
(A,p)\odot(B,q)=(AB,p+q),
\tag{5.1}
\]

initialize

\[
{\cal E}(1)={\cal E}(h)=(1,0),\qquad
{\cal E}(x_i)=(1,1),
\]

and propagate exact sums, products, and derivatives.  If
\({\cal E}(g)=(A,p)\), use

\[
{\cal E}(\phi(g))=(M_\phi(1+A),p),\qquad
{\cal E}(\phi^{(r)}(g))=(M_\phi,0),\quad1\le r\le12.
\tag{5.2}
\]

For a previously compiled scalar coefficient \(S\), introduce the tokens
\(S^{[j]}\) with

\[
{\cal E}(S^{[j]})=(\bar S_j,0),\qquad
\partial_hS^{[j]}=S^{[j+1]}.
\]

For a Gaussian node

\[
N(h)=\mathbb E_{X\sim N(0,\Sigma(h))}\psi(h,X),
\tag{5.3}
\]

singular Price differentiation is

\[
N'(h)=\mathbb E\left[
\partial_h\psi+\frac12\Sigma'(h):D_x^2\psi
\right].
\tag{5.4}
\]

Formula (5.4) at a rank-changing covariance follows by Fourier
differentiation of the Gaussian characteristic function, followed by
cutoff, mollification, and polynomially dominated convergence.  Repeating
that argument gives five derivatives.

Here is the numerical recursion.  If

\[
\bar c_j\ge\sup_{|h|\le1}\|\Sigma^{(j)}(h)\|_\Sigma,
\qquad0\le j\le5,
\]

where

\[
\|B\|_\Sigma:=\sum_{r,s}|B_{rs}|,
\]

and if the Gaussian node has dimension \(D\), let
\({\cal I}_{D,s}=\{1,\ldots,D\}^s\) be the set of ordered derivative
index strings, and initialize, for \(j+\lceil s/2\rceil\le5\),

\[
R^{(0)}_{j,s}
=\bigoplus_{(i_1,\ldots,i_s)\in{\cal I}_{D,s}}
{\cal E}(\partial_h^j\partial_{x_{i_1}}\cdots
\partial_{x_{i_s}}\psi).
\tag{5.5}
\]

Whenever \(q+j+\lceil s/2\rceil<5\), recurse by

\[
R^{(q+1)}_{j,s}
=R^{(q)}_{j+1,s}
\oplus
\bigoplus_{a=0}^j
\left[
\left(\frac12\binom ja\bar c_{a+1},0\right)
\odot R^{(q)}_{j-a,s+2}
\right].
\tag{5.6}
\]

If \(R^{(q)}_{0,0}=(A_q,p_q)\), define

\[
\overline{\mathcal J}_q(N)
=A_q\mu_{D,p_q}(\bar c_0),
\tag{5.7}
\]

where

\[
\mu_{D,p}(v)
=\mathbb E(1+\sqrt v\|G_D\|)^p
=\sum_{r=0}^p\binom pr
v^{r/2}2^{r/2}
\frac{\Gamma((D+r)/2)}{\Gamma(D/2)}.
\tag{5.8}
\]

Leibniz's rule applied repeatedly to (5.4) proves

\[
|N^{(q)}(h)|\le\overline{\mathcal J}_q(N),
\qquad |h|\le1.
\tag{5.9}
\]

New covariance entries use the sum of their entrywise bounds.  A response
node uses (5.5)--(5.9) on its differentiated integrand.  For
\(L=S+hQ\), use

\[
\bar L_j=\bar S_j+\bar Q_j+j\bar Q_{j-1},
\qquad \bar Q_{-1}=0.
\tag{5.10}
\]

Apply this constructor in exactly seven calls:

1. \((U,\chi_0)\), covariance \([1]\oplus[d^2]\): compile
   \(Q_H^{[1]},\rho^W_{10}\).
2. \((\xi_0,\xi_1,\omega_0)\), covariance
   \(Q_H^{[1]}\oplus[d]\): compile
   \(Q_G^{[1]},\rho^V_{10}\).
3. \((A,\zeta_0,\zeta_1)\), covariance
   \([1]\oplus Q_G^{[1]}\): compile
   \(F_1,K_C^{[1]},\sigma^V_{10},\sigma^V_{11}\).
   Then set
   \(T^V_{10}=\sigma^V_{10}+hK^C_{01}\) and
   \(T^V_{11}=\sigma^V_{11}\), using (5.10).
4. \((\xi_0,\xi_1,\omega_0,\omega_1)\), covariance
   \(Q_H^{[1]}\oplus K_C^{[1]}\): compile
   \(K_E^{[1]},\sigma^W_{10},\sigma^W_{11}\).
   Then set
   \(T^W_{10}=\sigma^W_{10}+hK^E_{01}\) and
   \(T^W_{11}=\sigma^W_{11}\), using (5.10).
5. \((U,\chi_0,\chi_1)\), covariance
   \([1]\oplus K_E^{[1]}\): compile
   \(Q^H_{r2},\rho^W_{20},\rho^W_{21}\).
6. \((\xi_0,\xi_1,\xi_2,\omega_0,\omega_1)\), covariance
   \(Q_H^{[2]}\oplus K_C^{[1]}\): compile
   \(Q^G_{r2},\rho^V_{20},\rho^V_{21}\).
7. \((A,\zeta_0,\zeta_1,\zeta_2)\), covariance
   \([1]\oplus Q_G^{[2]}\): compile \(F_2\).

At every call, the covariance derivative bound is the sum of the already
compiled entrywise bounds.  Explicitly,

\[
\begin{array}{c|c}
\text{call}&\bar c_j\\ \hline
1&\mathbf1_{\{j=0\}}(1+d^2)\\
2&\displaystyle\sum_{r,s\le1}\bar Q^H_{rs,j}
       +\mathbf1_{\{j=0\}}d\\
3&\displaystyle\mathbf1_{\{j=0\}}
       +\sum_{r,s\le1}\bar Q^G_{rs,j}\\
4&\displaystyle\sum_{r,s\le1}
       (\bar Q^H_{rs,j}+\bar K^C_{rs,j})\\
5&\displaystyle\mathbf1_{\{j=0\}}
       +\sum_{r,s\le1}\bar K^E_{rs,j}\\
6&\displaystyle\sum_{r,s\le2}\bar Q^H_{rs,j}
       +\sum_{r,s\le1}\bar K^C_{rs,j}\\
7&\displaystyle\mathbf1_{\{j=0\}}
       +\sum_{r,s\le2}\bar Q^G_{rs,j}.
\end{array}
\tag{5.10a}
\]

This algorithm terminates: there are seven calls, Gaussian dimension at
most five, and the finite Price index set

\[
\{(q,j,s):q+j+\lceil s/2\rceil\le5\}.
\]

On that set \(j+s\le10\).  A response integrand begins with derivative
order at most two, so no derivative above \(\phi^{(12)}\) occurs.  This
proves \(C^5\) regularity of the width-first DAG at \(h=0\), even though all
four time Grams are singular there.

Let

\[
\overline{\mathcal J}_{1,5}
=\overline{\mathcal J}_5(F_1),\qquad
\overline{\mathcal J}_{2,5}
=\overline{\mathcal J}_5(F_2)
\]

be the numerical results of calls 3 and 7, and define

\[
\boxed{
B_\phi
=\frac{\overline{\mathcal J}_{2,5}
+2^5\overline{\mathcal J}_{1,5}}{120}.
}
\tag{5.11}
\]

Equations (5.1)--(5.11) are a complete finite recursive definition of
\(B_\phi\).  It is activation-defined and contains no output-derived
supremum.

### 5.1 Exact Price jets for the cubic coefficient

We also record an exact, rather than majorizing, version of the same
constructor.  This supplies a non-circular definition of the cubic
coefficient directly from the operator nodes, independently of any compact
algebraic simplification.

For a node (5.3), let

\[
{\cal P}_{\Sigma}
=\partial_h+\frac12\Sigma'(h):D_x^2,
\qquad
\Psi_0=\psi,\qquad
\Psi_{r+1}={\cal P}_{\Sigma}\Psi_r .
\tag{5.12}
\]

The \(h\)-derivative in (5.12) acts on the entire expression, including
all occurrences of \(\Sigma^{(j)}\) and all earlier scalar-node tokens.
For an earlier node \(S\), use formal tokens \(S^{[j]}\) with

\[
\partial_hS^{[j]}=S^{[j+1]},
\qquad
S^{[j]}\big|_{h=0}={\cal J}_j(S).
\tag{5.13}
\]

Define

\[
{\cal J}_r(N)
=\Gamma_{\Sigma(0)}[\Psi_r(0,\cdot)].
\tag{5.14}
\]

Here
\(\Gamma_\Sigma[g]:=\mathbb E_{X\sim N(0,\Sigma)}g(X)\);
an unsubscripted \(\Gamma\) in the seven calls means expectation under
that call's displayed covariance.

Repeated singular Price differentiation, already proved in (5.4), gives

\[
{\cal J}_r(N)=N^{(r)}(0),\qquad 0\le r\le5.
\tag{5.15}
\]

Equations (5.12)--(5.14) are syntactic rules, not an instruction to
differentiate an unknown output.  To make their application completely
explicit, the seven calls are the following expression lists.

In call 1, on \((U,\chi_0)\) with covariance
\([1]\oplus[d^2]\), form

\[
\begin{gathered}
u_0=U,\quad H_0=\phi(U),\quad
u_1=U+h\chi_0\phi'(U),\quad H_1=\phi(u_1),\\
Q^H_{rs}=\Gamma[H_rH_s]\ (r,s\le1),\quad
\rho^W_{10}=\Gamma[\partial_{\chi_0}H_1],\quad
L^W_{10}=\rho^W_{10}+hQ^H_{01}.
\end{gathered}
\tag{5.16}
\]

In call 2, on \((\xi_0,\xi_1,\omega_0)\) with covariance
\(Q_H^{[1]}\oplus[d]\), form

\[
\begin{gathered}
z_0=\xi_0,\quad G_0=\phi(z_0),\quad
E_0=\omega_0\phi'(z_0),\\
z_1=\xi_1+L^W_{10}E_0,\quad G_1=\phi(z_1),\\
Q^G_{rs}=\Gamma[G_rG_s]\ (r,s\le1),\quad
\rho^V_{10}=\Gamma[\partial_{\omega_0}G_1],\quad
L^V_{10}=\rho^V_{10}+hQ^G_{01}.
\end{gathered}
\tag{5.17}
\]

In call 3, on \((A,\zeta_0,\zeta_1)\) with covariance
\([1]\oplus Q_G^{[1]}\), form

\[
\begin{gathered}
y_0=\zeta_0,\quad C_0=A\phi'(y_0),\\
a_1=A+h\phi(y_0),\quad
y_1=\zeta_1+L^V_{10}C_0,\quad C_1=a_1\phi'(y_1),\\
K^C_{rs}=\Gamma[C_rC_s]\ (r,s\le1),\\
\sigma^V_{1r}=\Gamma[\partial_{\zeta_r}C_1]\ (r=0,1),\\
T^V_{10}=\sigma^V_{10}+hK^C_{01},\qquad
T^V_{11}=\sigma^V_{11},\\
{\cal O}_1=F_1=\Gamma[a_1\phi(y_1)].
\end{gathered}
\tag{5.18}
\]

In call 4, on
\((\xi_0,\xi_1,\omega_0,\omega_1)\) with covariance
\(Q_H^{[1]}\oplus K_C^{[1]}\), recompute \(z_0,G_0,E_0,z_1,G_1\)
from (5.17), and form

\[
\begin{gathered}
d_1=\omega_1+T^V_{10}G_0+T^V_{11}G_1,\qquad
E_1=d_1\phi'(z_1),\\
K^E_{rs}=\Gamma[E_rE_s]\ (r,s\le1),\\
\sigma^W_{1r}=\Gamma[\partial_{\xi_r}E_1]\ (r=0,1),\\
T^W_{10}=\sigma^W_{10}+hK^E_{01},\qquad
T^W_{11}=\sigma^W_{11}.
\end{gathered}
\tag{5.19}
\]

In call 5, on \((U,\chi_0,\chi_1)\) with covariance
\([1]\oplus K_E^{[1]}\), form

\[
\begin{gathered}
u_0=U,\quad H_0=\phi(U),\quad
b_0=\chi_0,\quad u_1=u_0+hb_0\phi'(u_0),\quad H_1=\phi(u_1),\\
b_1=\chi_1+T^W_{10}H_0+T^W_{11}H_1,\\
u_2=u_1+hb_1\phi'(u_1),\quad H_2=\phi(u_2),\\
Q^H_{r2}=\Gamma[H_rH_2]\ (0\le r\le2),\\
\rho^W_{2r}=\Gamma[\partial_{\chi_r}H_2]\ (r=0,1),\qquad
L^W_{2r}=\rho^W_{2r}+hQ^H_{r2}.
\end{gathered}
\tag{5.20}
\]

In call 6, on
\((\xi_0,\xi_1,\xi_2,\omega_0,\omega_1)\) with covariance
\(Q_H^{[2]}\oplus K_C^{[1]}\), recompute the call-4 fields and form

\[
\begin{gathered}
z_2=\xi_2+L^W_{20}E_0+L^W_{21}E_1,\qquad G_2=\phi(z_2),\\
Q^G_{r2}=\Gamma[G_rG_2]\ (0\le r\le2),\\
\rho^V_{2r}=\Gamma[\partial_{\omega_r}G_2]\ (r=0,1),\qquad
L^V_{2r}=\rho^V_{2r}+hQ^G_{r2}.
\end{gathered}
\tag{5.21}
\]

In call 7, on \((A,\zeta_0,\zeta_1,\zeta_2)\) with covariance
\([1]\oplus Q_G^{[2]}\), recompute the call-3 fields and form

\[
\begin{gathered}
a_2=A+h\{\phi(y_0)+\phi(y_1)\},\\
y_2=\zeta_2+L^V_{20}C_0+L^V_{21}C_1,\qquad
{\cal O}_2=F_2=\Gamma[a_2\phi(y_2)].
\end{gathered}
\tag{5.22}
\]

At each line, apply (5.12)--(5.14) before moving to the next call.  This is
an acyclic finite recursion.  At \(h=0\), realize the repeated source
coordinates explicitly as

\[
\xi_0=\xi_1=\xi_2=Z_2,\qquad
\zeta_0=\zeta_1=\zeta_2=Z_3,
\]

\[
\chi_0=\chi_1=dZ_b,\qquad
\omega_0=\omega_1=\sqrt d\,Z_c,
\tag{5.23}
\]

with \(U,A,Z_2,Z_3,Z_b,Z_c\) independent standard Gaussians.  Therefore
every quantity in (5.14) is a finite integral of
\(\phi,\ldots,\phi^{(8)}\) against their product Gaussian law.  Expanding
the finite expression and using independence reduces it to finite products
of one-dimensional Gaussian activation integrals and elementary Gaussian
moments.

Define the exact activation integral

\[
\boxed{
\kappa_\phi^{\mathrm{PJ}}
=\frac{{\cal J}_3({\cal O}_2)-8{\cal J}_3({\cal O}_1)}6.
}
\tag{5.24}
\]

By (5.15), only after this activation-only number has been constructed do
we conclude

\[
\kappa_\phi^{\mathrm{PJ}}
=\frac{F_2'''(0)-8F_1'''(0)}6.
\tag{5.25}
\]

The same exact recursion at order one gives the linear cancellation without
using any Euler-intertwining claim.  The first-step source and field
variations are precisely the variables in (4.7): in particular

\[
\dot y_1=R_y=\sqrt{\nu_G}\varepsilon_G+c_2A\phi'(Y),
\qquad \dot a_1=\phi(Y),
\qquad c_2=1+d+d^2.
\]

Direct differentiation of calls 5--7 at the coalesced source gives
\(\dot H_2=2\dot H_1\), then \(\dot G_2=2\dot G_1\), and finally

\[
\dot y_2=2R_y,\qquad \dot a_2=2\phi(Y).
\]

Indeed, at \(h=0\) the two raw time sources coincide, and each of the two
learned-plus-response coefficients has derivative \(c_1=1+d\),
respectively \(c_2\); hence the two identical time contributions add.
Differentiating the two terminal integrands now gives

\[
{\cal J}_1({\cal O}_1)
=\mathbb E[\phi(Y)^2+A\phi'(Y)R_y]
=1+c_2d=1+d+d^2+d^3,
\]

\[
{\cal J}_1({\cal O}_2)=2\mathbb E[\phi(Y)^2+A\phi'(Y)R_y]
=2(1+c_2d)
=2(1+d+d^2+d^3).
\tag{5.26}
\]

Thus \({\cal J}_1({\cal O}_2)-2{\cal J}_1({\cal O}_1)=0\).

## 6. Cubic coefficient and parity

No Euler-intertwining identity is needed for the theorem.  The exact
Price-jet compiler differentiates the already constructed operator DAG
itself, expectation node by expectation node.  Equations (5.15),
(5.24), and (5.25) give directly

\[
\Delta'''(0)
=F_2'''(0)-8F_1'''(0)
=6\kappa_\phi.
\tag{6.1}
\]

The linear terms cancel by the direct order-one compiler evaluation
(5.26):

\[
\Delta'(0)
={\cal J}_1({\cal O}_2)-2{\cal J}_1({\cal O}_1)=0.
\tag{6.2}
\]

It remains to record the exact parity used in the remainder.  In the
seven calls (5.16)--(5.22), apply

\[
h\mapsto-h,\qquad
A\mapsto-A,\qquad
\chi\mapsto-\chi,\qquad
\omega\mapsto-\omega .
\tag{6.3}
\]

Call 1 leaves \(u,H,Q_H\) invariant and negates
\(\rho^W,L^W\).  Call 2 then negates \(E\), leaves \(z,G,Q_G\)
invariant, and negates \(\rho^V,L^V\).  Call 3 leaves \(y,K_C\)
invariant and negates \(a,C,\sigma^V,T^V,{\cal O}_1\).
Call 4 negates \(d,E,\sigma^W,T^W\) and leaves \(K_E\)
invariant.  Calls 5 and 6 repeat the first two conclusions at time two.
Finally, call 7 leaves \(y_2\) invariant and negates
\(a_2,{\cal O}_2\).  The centered Gaussian laws are invariant under the
sign changes.  Hence

\[
F_1(-h)=-F_1(h),\qquad F_2(-h)=-F_2(h).
\tag{6.4}
\]

The \(C^5\) regularity proved in Section 5 therefore implies

\[
\Delta(0)=\Delta''(0)
=\Delta^{(4)}(0)=0.
\tag{6.5}
\]

## 7. Quantitative remainder

For \(|\eta|\le h_\phi\), both \(|\eta|\le1\) and \(|2\eta|\le1\).
Therefore

\[
|\Delta^{(5)}(\eta)|
\le
\overline{\mathcal J}_{2,5}
+2^5\overline{\mathcal J}_{1,5}
=120B_\phi.
\tag{7.1}
\]

Oddness, linear cancellation, and (6.1)--(6.5) give

\[
\Delta(0)=\Delta'(0)
=\Delta''(0)=\Delta^{(4)}(0)=0,
\qquad
\Delta'''(0)=6\kappa_\phi.
\]

Taylor's integral remainder through order four is

\[
\Delta(\eta)-\kappa_\phi\eta^3
=\frac1{24}\int_0^\eta
(\eta-t)^4\Delta^{(5)}(t)\,dt.
\]

Using (7.1) proves (T.3).  If (T.4) holds, then

\[
B_\phi|\eta|^2
\le\frac{B_\phi}{1+B_\phi}\varepsilon
\le\varepsilon,
\]

so (T.3) proves (T.5).

If \(d=0\), continuity and Gaussian full support imply
\(\phi'\equiv0\), while normalization gives \(\phi\equiv\pm1\).  The exact
network then has \(F_k(h)=kh\), so the discrepancy is identically zero.
In this case take

\[
\kappa_\phi=0,\qquad B_\phi=0,\qquad h_\phi=\frac12.
\]

This completes the proof.
