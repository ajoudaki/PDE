# Exact linear-Gaussian detransposition recurrence

This note derives the two recurrences implemented in `identity_exact_jet.py`.
The networks and width-first convention are frozen in `PROTOCOL.md`.

## 1. Two hidden layers

Write normalized inner products as

\[
 \langle r,s\rangle_n=n^{-1}r^\top s,
\]

and put \(R=n^{-1/2}W^\top A\).  The exact finite-width feature-ascent
flow is

\[
 \dot A=Z,\qquad \dot X=R,\qquad
 \dot W=n^{-1/2}AX^\top.
\tag{1.1}
\]

Integrating the moving matrix before reusing it gives

\[
\begin{aligned}
 Z(t)&=n^{-1/2}W_0X(t)
 +\int_0^t A(s)\langle X(s),X(t)\rangle_n\,ds,\\
 R(t)&=n^{-1/2}W_0^\top A(t)
 +\int_0^t X(s)\langle A(s),A(t)\rangle_n\,ds.
\end{aligned}
\tag{1.2}
\]

In the width limit use a bottom scalar law containing \(u\) and transpose
innovations \(\xi^W_k\), and a top scalar law containing \(a\) and forward
innovations \(\eta^W_k\).  Their nonzero innovation covariances are

\[
 \mathbb E[\eta^W_k\eta^W_j]=\mathbb E[X_kX_j],\qquad
 \mathbb E[\xi^W_k\xi^W_j]=\mathbb E[A_kA_j].
\tag{1.3}
\]

Chronological detransposition gives

\[
\widehat Z_k=\eta^W_k+
 \sum_{j<k}\mathbb E[\partial_{\xi^W_j}X_k]A_j,
\qquad
\widehat R_k=\xi^W_k+
 \sum_{j\le k}\mathbb E[\partial_{\eta^W_j}A_k]X_j.
\tag{1.4}
\]

For ordinary Taylor coefficients \(G(t)=\sum_{k\ge0}G_kt^k\),

\[
 A_0=a,\quad X_0=u,\qquad
 A_k={Z_{k-1}\over k},\quad X_k={R_{k-1}\over k}\quad(k\ge1),
\tag{1.5}
\]

and (1.2) becomes

\[
\begin{aligned}
 Z_k&=\widehat Z_k+
 \sum_{p+q+r+1=k}{A_p\,\mathbb E[X_qX_r]\over p+q+1},\\
 R_k&=\widehat R_k+
 \sum_{p+q+r+1=k}{X_p\,\mathbb E[A_qA_r]\over p+q+1}.
\end{aligned}
\tag{1.6}
\]

Finally,

\[
 F_2^{(k)}(0)=k!\sum_{p+q=k}\mathbb E[A_pZ_q].
\tag{1.7}
\]

## 2. Three hidden layers

Put

\[
 R_2=n^{-1/2}V^\top A,\qquad
 R_1=n^{-1/2}W^\top R_2.
\]

The exact finite-width flow is

\[
 \dot A=T,\qquad \dot X=R_1,\qquad
 \dot V=n^{-1/2}AZ^\top,\qquad
 \dot W=n^{-1/2}R_2X^\top.
\tag{2.1}
\]

Thus

\[
\begin{aligned}
 Z(t)&=n^{-1/2}W_0X(t)
 +\int_0^t R_2(s)\langle X(s),X(t)\rangle_n\,ds,\\
 R_1(t)&=n^{-1/2}W_0^\top R_2(t)
 +\int_0^t X(s)\langle R_2(s),R_2(t)\rangle_n\,ds,\\
 T(t)&=n^{-1/2}V_0Z(t)
 +\int_0^t A(s)\langle Z(s),Z(t)\rangle_n\,ds,\\
 R_2(t)&=n^{-1/2}V_0^\top A(t)
 +\int_0^t Z(s)\langle A(s),A(t)\rangle_n\,ds.
\end{aligned}
\tag{2.2}
\]

Use three scalar laws: bottom \((u,\xi^W_k)\), middle
\((\eta^W_k,\xi^V_k)\), and top \((a,\eta^V_k)\).  The innovation
covariances are

\[
\begin{aligned}
 \mathbb E[\eta^W_k\eta^W_j]&=\mathbb E[X_kX_j],&
 \mathbb E[\xi^W_k\xi^W_j]&=\mathbb E[R_{2,k}R_{2,j}],\\
 \mathbb E[\eta^V_k\eta^V_j]&=\mathbb E[Z_kZ_j],&
 \mathbb E[\xi^V_k\xi^V_j]&=\mathbb E[A_kA_j].
\end{aligned}
\tag{2.3}
\]

The two middle innovation families have zero mutual covariance.  Their
dependence is retained by the causal responses

\[
\begin{aligned}
 \widehat Z_k&=\eta^W_k+
  \sum_{j<k}\mathbb E[\partial_{\xi^W_j}X_k]R_{2,j},\\
 \widehat R_{1,k}&=\xi^W_k+
  \sum_{j\le k}\mathbb E[\partial_{\eta^W_j}R_{2,k}]X_j,\\
 \widehat T_k&=\eta^V_k+
  \sum_{j<k}\mathbb E[\partial_{\xi^V_j}Z_k]A_j,\\
 \widehat R_{2,k}&=\xi^V_k+
  \sum_{j\le k}\mathbb E[\partial_{\eta^V_j}A_k]Z_j.
\end{aligned}
\tag{2.4}
\]

The ordinary-Taylor dynamics are

\[
 A_0=a,\quad X_0=u,\qquad
 A_k={T_{k-1}\over k},\quad X_k={R_{1,k-1}\over k}.
\tag{2.5}
\]

Each of the four identities in (2.2) uses the same Volterra coefficient
rule as (1.6), with source/overlap triples respectively

\[
 (R_2;X,X),\quad(X;R_2,R_2),\quad(A;Z,Z),\quad(Z;A,A).
\tag{2.6}
\]

The output is

\[
 F_3^{(k)}(0)=k!\sum_{p+q=k}\mathbb E[A_pT_q].
\tag{2.7}
\]

## 3. Derivative-normalized audit route

If every stored jet is an actual derivative at zero, the dynamics in
(1.5) and (2.5) lose their factors \(1/k\).  A Volterra term indexed by
\(p+q+r+1=k\) instead receives the integer weight

\[
 {k!\over p!q!r!(p+q+1)}
 ={k\choose r}{p+q\choose p}.
\tag{3.1}
\]

The output product uses \({k\choose p}\).  This is the second assembler.

## 4. Why the recurrence is small

All initial coordinates and innovations are centered Gaussian, and every
right-hand side above is a scalar linear combination of coordinate states.
Consequently every coordinate jet remains linear-Gaussian.  Expectations are
therefore exact covariance contractions; no higher Wick pairing or sparse
polynomial expansion occurs.  The construction is exact at every fixed
order under the same width-first Gaussian-program/detransposition limit used
by the nonlinear compilers.  It does not establish a positive-time solution
or an all-order complexity bound.

