# Independent fixed-depth, fixed-batch Gaussian-normal-form lift

**Status:** independent pre-audit derivation, now accepted as a supporting
witness for the theorem in
[DEPTH_FIXED_BATCH_GAUSSIAN_RECURSION.md](DEPTH_FIXED_BATCH_GAUSSIAN_RECURSION.md).
The exact \(H=3,B=2\) contraction and project-level hostile audit found no
index, response, or terminal-contraction discrepancy.

This note records the matrix lift of
[DEPTH_B1_GAUSSIAN_RECURSION.md](DEPTH_B1_GAUSSIAN_RECURSION.md) for fixed
batch size \(B\), fixed hidden
depth \(H\), channel \(c\in\mathbb R^B\), and \(Q^0\succeq0\).  It uses no
Hermite approximation and no covariance inverse.

## 1. Row-vector convention and base pass

A coordinate of any \(n\times B\) program vector is represented by a row
vector in \(\mathbb R^{1\times B}\).  For two such rows \(U,V\), write

\[
 \mathcal G(U,V)=\mathbb E[U^TV]\in\mathbb R^{B\times B}.
\tag{1.1}
\]

Let

\[
 Z_\ell\sim N(0,Q^{\ell-1}),\qquad
 X_\ell^{[0]}=\phi(Z_\ell),\qquad
 Q^\ell=\mathbb E[(X_\ell^{[0]})^TX_\ell^{[0]}],
\tag{1.2}
\]

and

\[
 E^\ell=\mathbb E[\phi'(Z_\ell)^T\phi'(Z_\ell)].
\tag{1.3}
\]

All activations and products of row vectors are coordinatewise unless a
matrix is displayed.

Let \(R_\ell\) be the base reverse carrier and

\[
 R_H=A_0c^T,\qquad
 \Delta_\ell=\phi'(Z_\ell)\odot R_\ell,
\tag{1.4}
\]

\[
 B_\ell=\mathbb E[R_\ell^TR_\ell],\qquad
 P_\ell=\mathbb E[\Delta_\ell^T\Delta_\ell].
\tag{1.5}
\]

The base transpose response is zero by centered-readout parity, giving

\[
 B_H=cc^T,\qquad
 P_\ell=B_\ell\odot E^\ell,\qquad
 B_{\ell-1}=P_\ell.
\tag{1.6}
\]

The matrix NTK recursion is

\[
 \Theta^0=Q^0,\qquad
 \Theta^\ell=Q^\ell+\Theta^{\ell-1}\odot E^\ell.
\tag{1.7}
\]

Consequently the directional initialization coefficient is

\[
 A_{H,c}=c^T\Theta^Hc
 =c^TQ^Hc+\sum_{\ell=1}^H
   \operatorname{tr}(Q^{\ell-1}P_\ell).
\tag{1.8}
\]

## 2. Bottom-up frozen forward jet

Let \(Z_\ell^{[r]},X_\ell^{[r]}\in\mathbb R^{1\times B}\) be the frozen
ordinary derivatives, with the same componentwise chain rules as equations
(4.1)--(4.2) of the scalar note.  At the first layer,

\[
 Z_1^{[1]}=\Delta_1Q^0,\qquad
 Z_1^{[2]}=Z_1^{[3]}=0.
\tag{2.1}
\]

Store the \(B\times B\) derivative Gram blocks

\[
 G_\ell^{rs}
 =\mathbb E[(X_\ell^{[r]})^TX_\ell^{[s]}],
 \qquad 0\le r,s\le3,
\tag{2.2}
\]

and response matrices

\[
 (J_\ell^r)_{ab}
 =\mathbb E\!\left[
   \frac{\partial(X_\ell^{[r]})_b}{\partial(R_\ell)_a}
 \right].
\tag{2.3}
\]

For \(\ell\ge2\), introduce a centered jointly Gaussian block
\((F_\ell^0,F_\ell^1,F_\ell^2,F_\ell^3)\), each entry a row in
\(\mathbb R^B\), with

\[
 \operatorname{Cov}((F_\ell^r)_a,(F_\ell^s)_b)
 =(G_{\ell-1}^{rs})_{ab}.
\tag{2.4}
\]

It is independent of \(R_\ell\).  The response-aware layer transition is

\[
 Z_\ell^{[0]}=F_\ell^0,
\tag{2.5}
\]

\[
 Z_\ell^{[r]}=F_\ell^r
 +\Delta_\ell
 \left(J_{\ell-1}^r+rG_{\ell-1}^{0,r-1}\right),
 \qquad 1\le r\le3.
\tag{2.6}
\]

The first matrix in parentheses is the unique earlier transpose response;
the second is the direct rank-one weight-direction term.  After applying the
componentwise chain rule, (2.2)--(2.3) close the next transition through
finite Gaussian expectations.

The readout-parity involution gives

\[
 G_\ell^{rs}=0\quad(r+s\ {\rm odd}),\qquad
 J_\ell^r=0\quad(r\ {\rm even}).
\tag{2.7}
\]

In particular,

\[
 J_\ell^1=\Theta^{\ell-1}\odot E^\ell,
\qquad
 J_{\ell-1}^1+G_{\ell-1}^{00}=\Theta^{\ell-1}.
\tag{2.8}
\]

## 3. Top-down differentiated reverse jet

At the top,

\[
 \widetilde R_H=(X_H^{[0]}c)c^T,
\tag{3.1}
\]

and

\[
 \widetilde\Delta_\ell
 =\phi''(Z_\ell)\odot Z_\ell^{[1]}\odot R_\ell
  +\phi'(Z_\ell)\odot\widetilde R_\ell.
\tag{3.2}
\]

Define

\[
 \Beta_\ell
 =\mathbb E[\widetilde\Delta_\ell^T\widetilde\Delta_\ell],
\tag{3.3}
\]

and, for \(\ell\ge2\), the four candidate forward responses

\[
 (\rho_\ell^r)_{ab}
 =\mathbb E\!\left[
 \frac{\partial(\widetilde\Delta_\ell)_b}
      {\partial(F_\ell^r)_a}
 \right].
\tag{3.4}
\]

Let \(\mathcal E_{\ell-1}\) be the fresh transpose Gaussian row with
covariance \(\Beta_\ell\).  The complete differentiated transpose rule is

\[
 \widetilde R_{\ell-1}
 =\mathcal E_{\ell-1}
  +X_{\ell-1}^{[0]}P_\ell
  +\sum_{r=0}^3X_{\ell-1}^{[r]}\rho_\ell^r.
\tag{3.5}
\]

Here the middle term is the direct
\((\dot A^\ell)^T\Delta_\ell\) contribution.  The covariance of
\(\mathcal E_{\ell-1}\) with the earlier base transpose innovation is
\(\mathbb E[\Delta_\ell^T\widetilde\Delta_\ell]=0\) by readout parity.
Moreover,

\[
 \rho_\ell^1=\rho_\ell^2=\rho_\ell^3=0:
\tag{3.6}
\]

the \(r=2,3\) fields do not occur in (3.2), while the \(r=1\) derivative is
diagonal with centered entries \(\phi''(Z_{\ell,a})(R_\ell)_a\).
Therefore

\[
 \widetilde R_{\ell-1}
 =\mathcal E_{\ell-1}
  +X_{\ell-1}^{[0]}\Chi_\ell,
\qquad
 \Chi_\ell=P_\ell+\rho_\ell^0.
\tag{3.7}
\]

Equations (3.1)--(3.7) form the proposed top-down local recursion for
\(\Beta_H,\ldots,\Beta_1\).

## 4. Terminal contractions

The straight-line third derivative is

\[
 T_{H,c}
 =\mathbb E[R_H(X_H^{[3]})^T]
  +3c^TG_H^{02}c.
\tag{4.1}
\]

The Hessian-square blocks are

\[
 \mathcal H_{a,c}=c^TG_H^{11}c,
\tag{4.2}
\]

\[
 \mathcal H_{W^1,c}=\operatorname{tr}(Q^0\Beta_1),
\tag{4.3}
\]

\[
 \mathcal H_{W^\ell,c}
 =\operatorname{tr}(Q^{\ell-1}\Beta_\ell)
  +\operatorname{tr}(P_\ell G_{\ell-1}^{11}),
 \qquad 2\le\ell\le H.
\tag{4.4}
\]

The two possible mixed terms vanish because both
\(\mathbb E[\Delta_\ell^T\widetilde\Delta_\ell]\) and
\(G_{\ell-1}^{01}\) vanish by parity.  The terminal coefficient is

\[
 C_{H,c}=2T_{H,c}
 +4\left(\mathcal H_{a,c}
 +\mathcal H_{W^1,c}
 +\sum_{\ell=2}^H\mathcal H_{W^\ell,c}\right).
\tag{4.5}
\]

Every expectation above is a finite Gaussian expectation.  Repeated
inverse-free Wick--Stein contraction of auxiliary coordinates emits literal
atoms

\[
 \mathbb E_{Z\sim N(0,Q^{\ell-1})}
 \prod_j\phi^{(r_j)}(Z_{i_j}),
\tag{4.6}
\]

so singular batch covariances require no separate branch.

## 5. Complete \(H=2\) fixed-batch index check

Under the notation of
[B2_GAUSSIAN_NORMAL_FORM.md](../b2/B2_GAUSSIAN_NORMAL_FORM.md), the state
specializes as

\[
 Q^1=Q,\qquad P_2=\mathsf D,\qquad B_1=\mathsf D,
\tag{5.1}
\]

\[
 J_1^1=\mathsf L,\qquad
 G_1^{11}=\mathsf G,\qquad
 G_1^{02}=\mathsf M,\qquad
 J_1^3=\mathsf N.
\tag{5.2}
\]

Thus (2.6) gives, with the same row orientation as the accepted note,

\[
 Z_2^{[1]}=F_2^1+\Delta_2\mathsf K,\qquad
 Z_2^{[2]}=F_2^2,
\tag{5.3}
\]

\[
 Z_2^{[3]}
 =F_2^3+\Delta_2(3\mathsf M+\mathsf N),
\tag{5.4}
\]

which is exactly its \(\zeta,\sigma,\tau\) registry.  The reverse pass gives

\[
 \Beta_2=\beta,\qquad
 \rho_2^0=\rho,\qquad
 \Chi_2=\mathsf D+\rho=\chi,
\tag{5.5}
\]

and (4.1)--(4.5) become its accepted \(T_c,H_{a,c},H_{W,c},H_{U,c},C_c\)
formulas.  This checks every matrix orientation and direct/response split at
\(H=2\); it is stronger than comparing only the terminal scalar.

## 6. Discharge of the original obligations

This independently written lift was frozen before comparison with the primary
joint recursion.  The following later checks discharge its original
obligations:

1. the exact sparse-polynomial evaluator verifies a nondegenerate nonlinear
   \(H=3,B=2\) case and both accepted one-axis reductions;
2. the hostile audit proves (3.6) is the complete response cancellation;
3. the same audit verifies the fixed-\(H,B\) Tensor-Program theorem mapping
   and arbitrary-label MSE bridge;
4. the primary theorem records \(O(B^2)\) retained state per layer and the
   distinction between the compact DAG and potentially large flat atom list.

See
[DEPTH_FIXED_BATCH_HOSTILE_AUDIT.md](DEPTH_FIXED_BATCH_HOSTILE_AUDIT.md)
for the independent verdict and exact nonclaims.
