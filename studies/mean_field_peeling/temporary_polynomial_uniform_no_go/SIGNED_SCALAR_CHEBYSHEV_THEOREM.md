# Signed-polynomial scalar obstruction via Chebyshev

## Theorem

Let

\[
 P(x)=\sum_{j=0}^{d}c_jx^j,\qquad d\ge2,\qquad c_d>0,
 \qquad \mathbb E P(G)^2=1,
\]

where the lower coefficients have arbitrary signs.  For independent
standard Gaussians \(A_0,Z_0\), define

\[
 A_{k+1}=A_k+hP(Z_k),\qquad
 Z_{k+1}=Z_k+hA_kP'(Z_k),\qquad
 Q_k(h)=\mathbb E[A_kP(Z_k)].
\]

Put \(D_t(h)=Q_{2t}(h)-Q_t(2h)\).  For every \(\rho>0\),

\[
 \boxed{\sup_{0\le h\le \rho/t}|D_t(h)|\longrightarrow\infty.}
 \tag{1}
\]

If \(\kappa_t=[h^3]D_t(h)\), then

\[
 \boxed{
 \sup_{0<h\le\rho/t}
 \frac{|D_t(h)-\kappa_th^3|}{t^4h^5}\longrightarrow\infty .}
 \tag{2}
\]

This is a theorem for the frozen scalar top block.  It does not, by itself,
identify or lower-bound the full two-hidden-layer OMFP discrepancy when the
lower coefficients of \(P\) have arbitrary signs.

## 1. Extremal coefficient lemma

If \(R(x)=a_mx^m+\cdots\) has exact degree \(m\), then, for every \(H>0\),

\[
 \max_{0\le x\le H}|R(x)|
 \ge 2^{1-2m}|a_m|H^m.                              \tag{3}
\]

Indeed, put \(x=H(y+1)/2\).  The coefficient of \(y^m\) in the resulting
polynomial is \(a_m(H/2)^m\).  Among degree-\(m\) polynomials with prescribed
leading coefficient \(b\), the smallest sup norm on \([-1,1]\) is
\(|b|/2^{m-1}\), attained by a multiple of the Chebyshev polynomial
\(T_m\).  This gives (3).  Notice that (3) requires no information about
the signs of the lower coefficients.

## 2. The two highest possible step orders

Set

\[
 \delta_N=\frac{d^N-1}{d-1},\qquad
 m_N=(d+1)\delta_N,
 \qquad r=d^{N-1},\quad s=d^N.
 \tag{4}
\]

Both state coordinates have maximal \(h\)-degree \(\delta_N\), and the
observable has maximal degree \(m_N\).  If

\[
 a_1=P(Z_0),\qquad z_1=A_0P'(Z_0),
\]

then the maximal branch after the first step is

\[
 [h^{m_N}]\{A_NP(Z_N)\}
   =C_{d,N}a_1^rz_1^s,\qquad C_{d,N}>0.             \tag{5}
\]

To see this, after time one the maximal coefficients satisfy

\[
 a_{k+1}=c_dz_k^d,\qquad
 z_{k+1}=dc_da_kz_k^{d-1}.
\]

The output exponent row \((1,d)\) is a left eigenvector, with eigenvalue
\(d\), of the exponent update
\((u,v)\mapsto(dv,u+(d-1)v)\).  This proves the exponents \((r,s)\) in
(5).  All factors used to form \(C_{d,N}\) are \(c_d\) and positive
integers.  In particular, with \(c_*=\min(1,c_d)\),

\[
 C_{d,N}\ge c_*^{m_N+1}.                             \tag{6}
\]

When \(d\) is odd, (5) has zero expectation.  Before computing the next
order, depress the polynomial.  Set

\[
 \mu=\frac{c_{d-1}}{dc_d},\qquad Y=Z+\mu,
 \qquad \widetilde P(y)=P(y-\mu).
 \tag{6a}
\]

This is an exact conjugacy of the scalar recursion: \(Y_0\sim N(\mu,1)\),
independently of \(A_0\), and

\[
 A^+=A+h\widetilde P(Y),\qquad
 Y^+=Y+hA\widetilde P'(Y).
\]

The coefficient of \(y^{d-1}\) in \(\widetilde P\) is zero.  We henceforth
rename \((Y,\widetilde P)\) as \((Z,P)\), remembering that the Gaussian may
have mean \(\mu\).

Now the coefficient one order below (5) is obtained uniquely by taking one
identity term, rather than its first Euler increment, in the expansion of
\(a_1^rz_1^s\).  An identity choice made at a later time loses at least
\(d\) step powers.  A lower activation monomial at the second update can
lose one step power only through the degree-\((d-1)\) coefficient, which is
zero by (6a); all other lower monomials lose at least two.  Therefore

\[
\begin{aligned}
 [h^{m_N-1}]Q_N(h)=C_{d,N}\{&r\,\mathbb EA_0^{s+1}
   \mathbb E[P(Y)^{r-1}P'(Y)^s]\\
 &+s\,\mathbb EA_0^{s-1}
   \mathbb E[YP(Y)^rP'(Y)^{s-1}]\}.
                                                               \tag{7}
\end{aligned}
\]

Here \(Y\sim N(\mu,1)\).  Formula (7) follows by replacing one of the
\(r\) factors \(hP(Y_0)\) by \(A_0\), or one of the \(s\) factors
\(hA_0P'(Y_0)\) by \(Y_0\), respectively.

## 3. Activation-only tail bounds

For even \(d\), use the original coefficients and put \(\mu=0\).  For odd
\(d\), use the depressed coefficients from (6a).  In either case, denote
the coefficients now in use again by \(c_j\), and define

\[
 C_0=\sum_{j<d}|c_j|,\qquad
 C_1=\sum_{1\le j<d}j|c_j|,
\]

and

\[
 R=\max\left\{1,\frac{2C_0}{c_d},
                    \frac{2C_1}{dc_d}\right\}.
 \tag{8}
\]

For \(|x|\ge R\),

\[
 |P(x)|\ge\frac{c_d}{2}|x|^d,qquad
 |P'(x)|\ge\frac{dc_d}{2}|x|^{d-1}.                \tag{9}
\]

If \(d\) is odd, additionally

\[
 P'(x)>0,qquad xP(x)>0\qquad(|x|\ge R).            \tag{10}
\]

For \(K\ge R^2\), integration over
\([\sqrt K,\sqrt K+K^{-1/2}]\) gives, when \(G_\mu\sim N(\mu,1)\), the
explicit bound

\[
 \mathbb E[|G_\mu|^K\mathbf1_{\{|G_\mu|\ge R\}}]
 \ge \frac1{\sqrt{2\pi K}}K^{K/2}
 \exp\!\left[-\frac12
   \left(\sqrt K+K^{-1/2}+|\mu|\right)^2\right].    \tag{11}
\]

For an even integer \(q\),

\[
 \mathbb EG^q=(q-1)!!\ge(q/(2e))^{q/2}.             \tag{12}
\]

Suppose first that \(d\) is even.  Then \(r,s\) are even, so (5) gives

\[
 [h^{m_N}]Q_N(h)
 =C_{d,N}\mathbb EG^s
   \mathbb E[P(G)^rP'(G)^s]>0.                       \tag{13}
\]

The second expectation is pointwise nonnegative, and (9)--(11), with
\(K=dr+(d-1)s=ds\), give a completely explicit lower bound.

Now suppose that \(d\) is odd and use the depressed polynomial and shifted
Gaussian from (6a).  Put

\[
 B_0=\sum_{j=0}^d|c_j|R^j,qquad
 B_1=\sum_{j=1}^dj|c_j|R^{j-1}.
\]

The two integrands in (7) are nonnegative outside \([-R,R]\), by (10).
Their exterior parts are bounded below, using (9)--(11), with respective
Gaussian powers

\[
 K_1=d(s-1),\qquad K_2=ds-d+2.                     \tag{14}
\]

Their possible negative interior parts have absolute values at most

\[
 B_0^{r-1}B_1^s,qquad RB_0^rB_1^{s-1}.            \tag{15}
\]

The logarithm of either exterior lower bound is
\((d/2)s\log s+O_P(s)\), whereas the logarithm of (15) is \(O_P(s)\).
Consequently there is a finite activation-defined \(N_P\): define it as the
least integer such that, for every \(N\ge N_P\), the two displayed exterior
bounds are at least twice (15), and \(K_1,K_2\ge R^2\).  This definition is
nonempty because each exterior/interior logarithmic difference tends to
\(+\infty\).  A fully numerical upper bound is obtained by substituting
(11) and checking the resulting explicit scalar inequalities; no output or
trajectory quantity enters the definition.  For every \(N\ge N_P\), both
expectations in (7) are positive and at least half their exterior lower
bounds.

Thus the exact degree of \(Q_N\), for all sufficiently large \(N\), is

\[
 k_N=\begin{cases}
 m_N,&d\text{ even},\\
 m_N-1,&d\text{ odd},
 \end{cases}                                           \tag{16}
\]

and its leading coefficient \(L_N\) has the explicit positive lower bounds
obtained from (6), (9), (11), (12), and, in odd degree, the first term of
(7).

## 4. Chebyshev defeats every polynomial time bound

Take \(N=2t\).  Since \(k_{2t}>m_t\) for all sufficiently large \(t\), the
coarse polynomial \(Q_t(2h)\) cannot alter \([h^{k_{2t}}]Q_{2t}(h)\).
Hence \(D_t\) has exact degree \(k_{2t}\) and leading coefficient
\(L_{2t}>0\).  Apply (3) with \(H=\rho/t\):

\[
 \sup_{0\le h\le\rho/t}|D_t(h)|
 \ge 2^{1-2k_{2t}}L_{2t}(\rho/t)^{k_{2t}}.          \tag{17}
\]

Let \(s=d^{2t}\).  The logarithm of the right side, divided by \(s\), is
bounded below by

\[
 (d+1)t\log d
 -\frac{d+1}{d-1}\log t+O_{P,\rho}(1),            \tag{18}
\]

where the first term comes from the two Gaussian moments of total power
\((d+1)s+O_d(1)\); the factors in (6), (9), and the Chebyshev factor cost
only \(O_{P,d}(s)\).  The right side of (18) tends to \(+\infty\), proving
(1).

Finally apply (3) directly to
\(R_t(h)=D_t(h)-\kappa_th^3\).  Subtracting a cubic changes neither its
degree \(k_{2t}\) nor its leading coefficient \(L_{2t}\).  Thus (17)
holds verbatim with \(R_t\) in place of \(D_t\).  At a maximizer \(h_t>0\),

\[
 \frac{|R_t(h_t)|}{t^4h_t^5}
 \ge \frac{|R_t(h_t)|}{t^4(\rho/t)^5}
 =\frac{t}{\rho^5}|R_t(h_t)|\longrightarrow\infty.
\]

This proves (2) without any separate estimate on \(\kappa_t\).

## Audit boundary

The proof is sign-robust because Chebyshev is applied before evaluating at
the endpoint \(h=\rho/t\).  It proves that some learning rate in the
allowed interval is bad.  It does not assert endpoint divergence.

The proof does **not** permit deleting the bottom-layer update in the full
network.  Such deletion was monotone for coefficientwise-positive
activations, but it is not monotone for arbitrary signed coefficients.
Therefore (1)--(2) cannot be promoted to the full \(L=2\) OMFP output
without a separate full-DAG coefficient theorem.
