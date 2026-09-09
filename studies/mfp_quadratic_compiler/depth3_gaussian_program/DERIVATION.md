# Depth-3 nested detransposition derivation

This note derives the recurrence implemented in `depth3_exact_jet.py`.  The
network and limit convention are frozen in `PROTOCOL.md`.

## 1. Exact flow before the width limit

Write normalized empirical inner products as

\[
\langle r,s\rangle_n=\frac1n\sum_i r_i s_i
\]

and define

\[
B_3=A\odot T,
\qquad R_2=n^{-1/2}V^\top B_3,
\qquad B_2=Z\odot R_2,
\qquad R_1=n^{-1/2}W^\top B_2.
\]

Direct differentiation of
(f_n=n^{-1}\sum_k A_kT_k^2) under
(D_n=n\nabla f_n\cdot\nabla) gives

\[
\dot A=T^2,
\qquad
\dot V=\frac2{\sqrt n}B_3Y^\top,
\qquad
\dot W=\frac4{\sqrt n}B_2X^\top.
\tag{1.1}
\]

The bottom derivative is
(\dot u=8u\odot R_1), hence

\[
\dot X=2u\odot\dot u=16X\odot R_1.
\tag{1.2}
\]

Integrating both matrix equations before reusing the matrices yields the
four exact identities

\[
\begin{aligned}
Z(t)&=n^{-1/2}W_0X(t)
+4\int_0^t B_2(s)\langle X(s),X(t)\rangle_n\,ds,\\
R_1(t)&=n^{-1/2}W_0^\top B_2(t)
+4\int_0^t X(s)\langle B_2(s),B_2(t)\rangle_n\,ds,\\
T(t)&=n^{-1/2}V_0Y(t)
+2\int_0^t B_3(s)\langle Y(s),Y(t)\rangle_n\,ds,\\
R_2(t)&=n^{-1/2}V_0^\top B_3(t)
+2\int_0^t Y(s)\langle B_3(s),B_3(t)\rangle_n\,ds.
\end{aligned}
\tag{1.3}
\]

These identities retain the fixed-matrix/transpose correlations that would
be lost by replacing every multiplication with a fresh independent Gaussian.

## 2. Three limiting scalar laws

At each fixed Taylor order the width limit is represented by three centered
Gaussian polynomial laws:

- bottom law ({\cal L}_1): (u\sim N(0,1)) and (W^\top) innovations
  \(\xi^W_k\);
- middle law ({\cal L}_2): (W) innovations (\eta^W_k) and
  (V^\top) innovations (\xi^V_k);
- top law ({\cal L}_3): (a\sim N(0,1)) and (V) innovations
  \(\eta^V_k\).

The only nonzero innovation covariances are

\[
\begin{aligned}
\mathbb E_2[\eta^W_k\eta^W_j]&=\mathbb E_1[X_kX_j],&
\mathbb E_1[\xi^W_k\xi^W_j]&=\mathbb E_2[B_{2,k}B_{2,j}],\\
\mathbb E_3[\eta^V_k\eta^V_j]&=\mathbb E_2[Y_kY_j],&
\mathbb E_2[\xi^V_k\xi^V_j]&=\mathbb E_3[B_{3,k}B_{3,j}].
\end{aligned}
\tag{2.1}
\]

The (W)- and (V)-innovation families in the middle law have zero mutual
covariance because the two initialization matrices are independent.  The
dependence caused by transpose reuse is instead carried by the following
Stein responses:

\[
\begin{aligned}
\widehat Z_k
&=\eta^W_k+
\sum_{j<k}\mathbb E_1[\partial_{\xi^W_j}X_k]B_{2,j},\\
\widehat R_{1,k}
&=\xi^W_k+
\sum_{j\le k}\mathbb E_2[\partial_{\eta^W_j}B_{2,k}]X_j,\\
\widehat T_k
&=\eta^V_k+
\sum_{j<k}\mathbb E_2[\partial_{\xi^V_j}Y_k]B_{3,j},\\
\widehat R_{2,k}
&=\xi^V_k+
\sum_{j\le k}\mathbb E_3[\partial_{\eta^V_j}B_{3,k}]Y_j.
\end{aligned}
\tag{2.2}
\]

The strict inequality in each forward sum is causal: the order-(k)
forward feature has not yet used the order-(k) transpose innovation.  The
backward sums include the current forward innovation and therefore use
(j\le k).

## 3. Ordinary-Taylor recurrence

Let (G(t)=\sum_{k\ge0}G_kt^k).  Start with

\[
A_0=a,
\qquad X_0=u^2.
\]

For (k\ge1), equations (1.1)--(1.2) give

\[
A_k=\frac1k\sum_{p+q=k-1}T_pT_q,
\qquad
X_k=\frac{16}{k}\sum_{p+q=k-1}X_pR_{1,q}.
\tag{3.1}
\]

Expanding the four Volterra terms in (1.3) gives

\[
\begin{aligned}
Z_k={}&\widehat Z_k+
4\!\sum_{p+q+r+1=k}
\frac{B_{2,p}\,\mathbb E_1[X_qX_r]}{p+q+1},\\
T_k={}&\widehat T_k+
2\!\sum_{p+q+r+1=k}
\frac{B_{3,p}\,\mathbb E_2[Y_qY_r]}{p+q+1},\\
R_{2,k}={}&\widehat R_{2,k}+
2\!\sum_{p+q+r+1=k}
\frac{Y_p\,\mathbb E_3[B_{3,q}B_{3,r}]}{p+q+1},\\
R_{1,k}={}&\widehat R_{1,k}+
4\!\sum_{p+q+r+1=k}
\frac{X_p\,\mathbb E_2[B_{2,q}B_{2,r}]}{p+q+1}.
\end{aligned}
\tag{3.2}
\]

The algebraic carriers are

\[
Y_k=\sum_{p+q=k}Z_pZ_q,
\qquad
B_{3,k}=\sum_{p+q=k}A_pT_q,
\qquad
B_{2,k}=\sum_{p+q=k}Z_pR_{2,q}.
\tag{3.3}
\]

At a fixed (k), (3.1)--(3.3) are evaluated in the acyclic order

\[
(A_k,X_k)\to Z_k\to Y_k\to T_k\to B_{3,k}
\to R_{2,k}\to B_{2,k}\to R_{1,k}.
\tag{3.4}
\]

Finally,

\[
F^{(k)}(0)
=k!\,\mathbb E_3
\sum_{p+q+r=k}A_pT_qT_r.
\tag{3.5}
\]

## 4. Independent coefficient normalization

The audit route stores (G^{(k)}(0)), not (G_k).  Binary products use

\[
(PQ)^{(k)}(0)=\sum_{j=0}^k {k\choose j}P^{(j)}(0)Q^{(k-j)}(0).
\]

For example, a Volterra summand with (p+q+r+1=k) acquires the integer
weight

\[
\frac{k!}{p!q!r!(p+q+1)}
={k\choose r}{p+q\choose p}.
\tag{4.1}
\]

Thus this route assembles every ODE, product, memory term, and output with
binomial or multinomial weights.  The innovation variables and their
covariances are derivative-normalized as well, so the response formulas
(2.2) retain coefficient one.  Agreement of the two routes is consequently
an exact check of all factorial and integration weights, although both routes
still rely on the same derived Gaussian-program identities (2.1)--(2.2).

## 5. Scope

The recurrence is exact for each fixed order under the standard width-first
Gaussian-program limit.  Its successful order-nine execution is not an
all-order complexity theorem and does not establish a positive-time limit or
any Stieltjes property.
