# Fixed-step width limit at arbitrary hidden depth

## 1. The width-first theorem

Fix an integer \(L\ge2\), the number of hidden layers, and a step size
\(0<|h|\le1\).  All hidden widths
are \(n\), the input is the scalar \(1\), and the network and ascent rule are
those in Section 2.  Assume

\[
 \phi\in C^2(\mathbb R),\qquad
 |\phi(x)|\le M(1+|x|),\qquad
 \|\phi'\|_\infty+\|\phi''\|_\infty\le M,                 \tag{1.1}
\]

\[
 \mathbb E\phi(Z)^2=1,\qquad
 d:=\mathbb E\phi'(Z)^2>0,\qquad Z\sim N(0,1).             \tag{1.2}
\]

The \(C^{12}\) activation envelope used in the quantitative discrepancy
theorem implies (1.1).  For a fixed \(h\ne0\), let the population scalar DAG
of Section 5 produce, for every connector \(\ell=2,\ldots,L\), the two
two-time second-moment matrices

\[
 Q_{\ell-1}^{[1]}(h)
   =\bigl(\mathbb E[H_{\ell-1}^rH_{\ell-1}^s]\bigr)_{r,s=0}^1,
 \qquad
 K_{\ell}^{[1]}(h)
   =\bigl(\mathbb E[C_{\ell}^rC_{\ell}^s]\bigr)_{r,s=0}^1. \tag{1.3}
\]

Suppose that all \(2(L-1)\) matrices in (1.3) are positive definite.
Then, at this fixed \(h\), every finite-width field in the exact
\(5(L-1)\)-action chronology of Section 3 converges to its counterpart in
the scalar DAG.  More precisely, there is a joint coupling under which,
for every finite \(p,P\),

\[
 \left\|\|X_n-\widehat X_n\|_{n,p}\right\|_{L^P}\longrightarrow0       \tag{1.4}
\]

for every raw action, preactivation, feature, backsignal, and cotangent in
the chronology.  Every empirical Gram and every raw overlap entering a
Gaussian conditioning formula converges in every finite \(L^P\), and is
uniformly integrable.  The stopped/extended regression coefficients
defined in Section 8.6 also converge in every finite \(L^P\).  Consequently,

\[
 \lim_{n\to\infty}\mathbb E f_{n,L}^k=F_{k,L}(h),
 \qquad k=1,2,                                             \tag{1.5}
\]

where \(F_{k,L}(h)\) is the output of the scalar DAG after \(k\) recomputed
steps.  The limit in (1.5) is pointwise at fixed \(h\); no step-size
expansion is made before the width limit.

The terminal \((0,1,2)\)-time feature Grams may be singular.  They are
never inverted.

There is also a rank-free statement for the one-step side of the
comparison.  For every fixed \(0<|h|\le1\),

\[
 \lim_{n\to\infty}\mathbb E f_{n,L}^1=F_{1,L}(h)           \tag{1.6}
\]

without assuming (1.3).  Only the strictly positive scalar initialization
Grams

\[
 Q_{\ell-1,00}=1,\qquad
 K_{\ell,00}=d^{\,L-\ell+1},\qquad 2\le\ell\le L,          \tag{1.7}
\]

are inverted.  Thus (1.6) applies directly with \(h=2\eta\), while (1.5)
applies to the two-step term with \(h=\eta\).

If \(d=0\), continuity and full support of Gaussian measure imply
\(\phi'\equiv0\).  Normalization then makes \(\phi\) a constant of modulus
one.  All hidden gradients vanish and
\(\mathbb E f_{n,L}^s=sh\) exactly, so the theorem holds without any rank
condition.  For \(L=1\), write the coordinate recursion explicitly as

\[
 A_j^{s+1}=A_j^s+h\phi(U_j^s),\qquad
 U_j^{s+1}=U_j^s+hA_j^s\phi'(U_j^s),\qquad s=0,1.
 \tag{1.8}
\]

The pairs \((A_j^s,U_j^s)\) are iid over \(j\), and

\[
 f_{n,1}^s=\frac1n\sum_{j=1}^n A_j^s\phi(U_j^s),\qquad
 \mathbb E f_{n,1}^s=\mathbb E[A_1^s\phi(U_1^s)]
 \tag{1.9}
\]

for every \(n\), not merely in the limit.  The linear-growth and bounded-
derivative assumptions bound the two-step summand by a fixed polynomial in
\(|A_j^0|+|U_j^0|\), so it has moments of every finite order.  Rosenthal's
inequality gives empirical convergence in every finite \(L^P\), and the
same polynomial bound gives uniform integrability.  Thus the fixed-\(h\)
identification is exact at \(L=1\).  We therefore prove the nontrivial
matrix statement below for \(L\ge2\) and \(d>0\).

## 2. Exact finite-width network

Let

\[
 u_j^0,\ a_j^0,\ (W_\ell^0)_{ij},
 \qquad 1\le j,i\le n,\quad 2\le\ell\le L,                 \tag{2.1}
\]

be mutually independent standard Gaussian variables.  There are no
biases.  Write

\[
 Z_{1,j}^s=u_j^s,\qquad H_{1,j}^s=\phi(Z_{1,j}^s),          \tag{2.2}
\]

and, for \(2\le\ell\le L\),

\[
 Z_\ell^s=\frac{W_\ell^sH_{\ell-1}^s}{\sqrt n},
 \qquad H_\ell^s=\phi(Z_\ell^s),                            \tag{2.3}
\]

with componentwise application of \(\phi\).  The output is

\[
 f_{n,L}^s=\frac1n(a^s)^TH_L^s.                            \tag{2.4}
\]

The top cotangent and the descending backpropagation fields are

\[
 C_L^s=a^s\odot\phi'(Z_L^s),                               \tag{2.5}
\]

\[
 B_{\ell-1}^s=\frac{(W_\ell^s)^TC_\ell^s}{\sqrt n},
 \qquad
 C_{\ell-1}^s=B_{\ell-1}^s\odot\phi'(Z_{\ell-1}^s),
 \quad \ell=L,L-1,\ldots,2.                                \tag{2.6}
\]

One simultaneous mean-field feature-ascent step is

\[
 \theta^{s+1}=\theta^s+hn\nabla_\theta f_{n,L}^s.          \tag{2.7}
\]

Direct differentiation gives, with all right-hand sides evaluated at time
\(s\),

\[
 \begin{aligned}
 a^{s+1}&=a^s+hH_L^s,\\
 W_\ell^{s+1}
   &=W_\ell^s+\frac h{\sqrt n}C_\ell^s(H_{\ell-1}^s)^T,
       &&2\le\ell\le L,\\
 Z_1^{s+1}&=Z_1^s+hC_1^s .
 \end{aligned}                                             \tag{2.8}
\]

For example,

\[
 \frac{\partial f_{n,L}^s}{\partial W_\ell^s}
   =\frac1{n\sqrt n}C_\ell^s(H_{\ell-1}^s)^T,\qquad
 \frac{\partial f_{n,L}^s}{\partial u^s}
   =\frac1nC_1^s,                                         \tag{2.9}
\]

which verifies all scalings in (2.8).

Keep only the initialization matrices in the raw actions:

\[
 X_\ell^s=\frac{W_\ell^0H_{\ell-1}^s}{\sqrt n},\qquad
 R_{\ell-1}^s=\frac{(W_\ell^0)^TC_\ell^s}{\sqrt n},
 \quad 2\le\ell\le L.                                     \tag{2.10}
\]

Define the empirical second moments

\[
 Q_{\ell,rs}^{(n)}
   =\frac1n(H_\ell^r)^TH_\ell^s,\qquad
 K_{\ell,rs}^{(n)}
   =\frac1n(C_\ell^r)^TC_\ell^s.                           \tag{2.11}
\]

Summing (2.8) and substituting into (2.3) and (2.6) gives the exact,
finite-\(n\) identities

\[
 Z_\ell^s
   =X_\ell^s+h\sum_{r<s}Q_{\ell-1,rs}^{(n)}C_\ell^r,
 \qquad 2\le\ell\le L,                                    \tag{2.12}
\]

\[
 B_{\ell-1}^s
   =R_{\ell-1}^s+h\sum_{r<s}K_{\ell,rs}^{(n)}
                         H_{\ell-1}^r,
 \qquad 2\le\ell\le L,                                    \tag{2.13}
\]

\[
 a^s=a^0+h\sum_{r<s}H_L^r,\qquad
 Z_1^s=Z_1^0+h\sum_{r<s}C_1^r.                            \tag{2.14}
\]

No current-time Gram occurs in (2.12)--(2.14).

## 3. The exact \(5(L-1)\)-action chronology

For \(s=0,1\), a recomputed gradient step first performs a forward sweep
and then a backward sweep.  The terminal output performs only a forward
sweep.  Thus the raw initialization-matrix actions, in their reveal order,
are

\[
 \begin{split}
 \mathcal A_L={}&
 (X_2^0,X_3^0,\ldots,X_L^0;\,
   R_{L-1}^0,R_{L-2}^0,\ldots,R_1^0;\\
 &X_2^1,X_3^1,\ldots,X_L^1;\,
   R_{L-1}^1,R_{L-2}^1,\ldots,R_1^1;\\
 &X_2^2,X_3^2,\ldots,X_L^2).
                                                               \tag{3.1}
 \end{split}
\]

There are

\[
 (L-1)+(L-1)+(L-1)+(L-1)+(L-1)=5(L-1)                    \tag{3.2}
\]

actions.  Every query is measurable before its action:

* in a forward sweep, \(H_{\ell-1}^s\) is available before
  \(W_\ell^0H_{\ell-1}^s\);
* in a backward sweep, \(C_\ell^s\) is available before
  \((W_\ell^0)^TC_\ell^s\).

The query may depend on every earlier action of every matrix.  In
particular, \(H_{\ell-1}^1\) contains the entire time-zero descending
backpropagation through matrices \(W_L^0,\ldots,W_2^0\), including the
column action of \(W_\ell^0\) itself.  This dependence is retained.

The one-step output uses the prefix

\[
 (X_2^0,\ldots,X_L^0;\
   R_{L-1}^0,\ldots,R_1^0;\
   X_2^1,\ldots,X_L^1),                                   \tag{3.3}
\]

which has \(3(L-1)\) actions.

## 4. Adaptive conditioning for finitely many reused matrices

The following finite-dimensional lemma is the only matrix-probability
input.

**Lemma 4.1 (predictable multi-matrix Gaussian conditioning).**
Let \(M_2,\ldots,M_L\) be independent \(n\times n\) standard Gaussian
matrices, independent of an external sigma-field \(\mathcal E\).  Consider
any finite sequence of row actions \(M_\ell q/\sqrt n\) and transpose
actions \(M_\ell^Tc/\sqrt n\).  At each stage, the matrix label and query
are measurable with respect to the sigma-field generated by
\(\mathcal E\) and all earlier queries and actions.

For one matrix \(M\), let \(H\) and \(C\) collect its previously used row
and column queries, and put

\[
 Y=MH/\sqrt n,\qquad D=M^TC/\sqrt n.                       \tag{4.1}
\]

Conditionally on the global revealed filtration,

\[
 M=P_C M+MP_H-P_CMP_H
      +P_C^\perp\widetilde M P_H^\perp,                    \tag{4.2}
\]

where, jointly over \(\ell=2,\ldots,L\), the residual matrices
\(\widetilde M_\ell\) are conditionally independent standard Gaussian
matrices and are independent of the revealed filtration.

Let

\[
 Q=H^TH/n,\quad K=C^TC/n,\quad
 \mathcal R=C^TY/n=D^TH/n.                                \tag{4.3}
\]

When \(Q,K\) are invertible, a new transpose query \(c\) has conditional
representation

\[
 \frac{M^Tc}{\sqrt n}
 =DK^{-1}k+HQ^{-1}(r-\mathcal R^TK^{-1}k)
   +\tau_cP_H^\perp g,                                    \tag{4.4}
\]

\[
 k=C^Tc/n,\quad r=Y^Tc/n,\quad
 \tau_c^2=c^Tc/n-k^TK^{-1}k.                              \tag{4.5}
\]

A new row query \(q_{\rm new}\) has representation

\[
 \frac{Mq_{\rm new}}{\sqrt n}
 =YQ^{-1}q+CK^{-1}(v-\mathcal RQ^{-1}q)
   +\tau_qP_C^\perp g,                                    \tag{4.6}
\]

\[
 q=H^Tq_{\rm new}/n,\quad v=D^Tq_{\rm new}/n,\quad
 \tau_q^2=q_{\rm new}^Tq_{\rm new}/n-q^TQ^{-1}q.          \tag{4.7}
\]

Empty blocks are omitted.  Orthogonal projectors and Moore--Penrose
inverses give the corresponding identities when a block is singular.

**Proof.**
Let \(\mathcal F_t\) be the global filtration after \(t\) actions.  We
induct on \(t\).  Initially the residual matrices are the independent
matrices \(M_\ell\).

Assume (4.2), with mutually independent residuals, holds at time \(t\).
Suppose the next action is \(M_jq\).  The query is
\(\mathcal F_t\)-measurable.  Write

\[
 q=P_{H_j}q+q_\perp.                                      \tag{4.8}
\]

Every term except
\(P_{C_j}^\perp\widetilde M_jq_\perp\) is already determined.
If \(q_\perp\ne0\), put \(e=q_\perp/\|q_\perp\|\).  For a standard
Gaussian matrix, the two orthogonal Gaussian projections

\[
 \widetilde M_jee^T,\qquad
 \widetilde M_j(I-ee^T)                                   \tag{4.9}
\]

are independent.  Revealing the first leaves

\[
 P_{C_j}^\perp\widetilde M_j
 P_{\operatorname{span}(H_j,q)}^\perp                     \tag{4.10}
\]

fresh.  It remains independent of every untouched residual
\(\widetilde M_\ell\), \(\ell\ne j\), because the new observation is a
function only of the \(j\)-th residual conditional on \(\mathcal F_t\).
If \(q_\perp=0\), no residual component is revealed.  A transpose action
is the same argument with rows and columns exchanged.  This proves (4.2)
for every \(t\), including arbitrarily interlaced cross-dependent queries.

To derive (4.4), decompose

\[
 c=CK^{-1}k+c_\perp.                                      \tag{4.11}
\]

The first component contributes \(DK^{-1}k\).  The projection of
\(M^Tc_\perp/\sqrt n\) onto \(\operatorname{span}(H)\) is

\[
 HQ^{-1}\frac{Y^Tc_\perp}{n}
 =HQ^{-1}(r-\mathcal R^TK^{-1}k),                         \tag{4.12}
\]

and the remaining conditional covariance is
\(\tau_c^2P_H^\perp\).  This is (4.4)--(4.5).
Transposition gives (4.6)--(4.7).  The projector formulation proves the
pseudoinverse version. \(\square\)

Applying this lemma with \(M_\ell=W_\ell^0\) proves, in particular, that
revealing an action of one connector does not expose any component of the
unrevealed double-orthogonal residual of another connector.  This is the
multi-layer adaptive-dependence point needed below.

## 5. The arbitrary-depth Gaussian operator DAG

All definitions in this section are chronological; no fixed-point equation
is imposed.

For every connector \(2\le\ell\le L\), introduce centered Gaussian blocks

\[
 \xi_\ell=(\xi_{\ell,0},\xi_{\ell,1},\xi_{\ell,2}),\qquad
 \chi_\ell=(\chi_{\ell,0},\chi_{\ell,1}),                  \tag{5.1}
\]

and independent \(U,A\sim N(0,1)\).  All fresh standard-normal innovations
used for different connectors, directions, and coordinates are mutually
independent.  Their covariances are

\[
 \mathbb E[\xi_{\ell,r}\xi_{\ell,s}]
   =Q_{\ell-1,rs}:=\mathbb E[H_{\ell-1}^rH_{\ell-1}^s],
                                                               \tag{5.2}
\]

\[
 \mathbb E[\chi_{\ell,r}\chi_{\ell,s}]
   =K_{\ell,rs}:=\mathbb E[C_\ell^rC_\ell^s].              \tag{5.3}
\]

Each block is extended only after the right-hand side is known.  More
explicitly, if \(G^{[s-1]}\) is the already constructed covariance and
\(g\) is the vector of covariances with a new coordinate, set

\[
 X_s=g^T(G^{[s-1]})^{-1}X_{0:s-1}
     +\sqrt{G_{ss}-g^T(G^{[s-1]})^{-1}g}\,Z_s,             \tag{5.4}
\]

with a fresh independent \(Z_s\).  At a terminal singular extension, use
the Moore--Penrose regression; the square root is allowed to be zero.

Set

\[
 Z_1^0=U,\qquad H_1^s=\phi(Z_1^s).                         \tag{5.5}
\]

For \(s=0,1,2\), perform the following ascending forward sweep.  For
\(\ell=2,\ldots,L\), after \(H_{\ell-1}^s\) has been constructed, define

\[
 \rho_{\ell,sr}
   :=\mathbb E\!\left[\partial_{\chi_{\ell,r}}
                       H_{\ell-1}^s\right],
 \qquad 0\le r<s,                                         \tag{5.6}
\]

\[
 Z_\ell^s
   =\xi_{\ell,s}
      +\sum_{r<s}\bigl(\rho_{\ell,sr}
                       +hQ_{\ell-1,rs}\bigr)C_\ell^r,
 \qquad
 H_\ell^s=\phi(Z_\ell^s).                                 \tag{5.7}
\]

For \(s=0,1\), after this forward sweep, put

\[
 a^s=A+h\sum_{r<s}H_L^r,\qquad
 C_L^s=a^s\phi'(Z_L^s),                                   \tag{5.8}
\]

and perform the descending sweep.  For
\(\ell=L,L-1,\ldots,2\), after \(C_\ell^s\) has been constructed, define

\[
 \sigma_{\ell,sr}
   :=\mathbb E\!\left[\partial_{\xi_{\ell,r}}C_\ell^s\right],
 \qquad 0\le r\le s,                                      \tag{5.9}
\]

\[
 B_{\ell-1}^s
  =\chi_{\ell,s}
    +\sum_{r\le s}\sigma_{\ell,sr}H_{\ell-1}^r
    +h\sum_{r<s}K_{\ell,rs}H_{\ell-1}^r,                  \tag{5.10}
\]

\[
 C_{\ell-1}^s=B_{\ell-1}^s\phi'(Z_{\ell-1}^s).             \tag{5.11}
\]

At the end of the descending sweep set

\[
 Z_1^{s+1}=Z_1^s+hC_1^s.                                  \tag{5.12}
\]

After the terminal forward sweep \(s=2\), put

\[
 a^2=A+h(H_L^0+H_L^1),\qquad
 F_{k,L}(h)=\mathbb E[a^kH_L^k],\quad k=1,2.              \tag{5.13}
\]

This is a finite DAG.  To see explicitly that covariance construction
does not run in a circle:

1. At time zero, construct \(\xi_{2,0},\ldots,\xi_{L,0}\) in the forward
   sweep.
2. Construct \(C_L^0\), hence \(K_{L,00}\), then
   \(\chi_{L,0}\), \(C_{L-1}^0\), \(K_{L-1,00}\), and continue downward.
3. Equation (5.12) gives \(H_1^1\).  Extend \(\xi_{2}\) to time one,
   construct \(H_2^1\), then extend \(\xi_3\), and continue upward.
4. Extend \(\chi_L\) to time one after \(C_L^1\) is known, then proceed
   downward.
5. Repeat only the ascending extension of each \(\xi_\ell\) at time two.

Every response derivative in (5.6) and (5.9) is also finite and
constructive.  Regard already evaluated Grams and responses as
deterministic coefficients.  Initialize the derivative of its own Gaussian
source coordinate to one and all other source derivatives to zero; then
propagate through the displayed assignments using

\[
 D(\phi(X))=\phi'(X)DX,\qquad
 D(\phi'(X))=\phi''(X)DX,\qquad
 D(XY)=X\,DY+Y\,DX.                                      \tag{5.14}
\]

The chronology above orders every node before the node that uses it, so
this recursion terminates after \(5(L-1)\) matrix actions.  Assumption
(1.1) gives polynomial Gaussian envelopes for all fields and all
first-source derivatives, proving that (5.6) and (5.9) are integrable.

At time zero,

\[
 \sigma_{L,00}
   =\mathbb E[A\phi''(\xi_{L,0})]=0.                       \tag{5.15}
\]

Descending induction gives

\[
 B_{\ell-1}^0=\chi_{\ell,0},\qquad 2\le\ell\le L,
                                                                    \tag{5.16}
\]

and, for \(3\le\ell\le L\),

\[
 \sigma_{\ell-1,00}=0,\qquad
 K_{\ell-1,00}=dK_{\ell,00}.                              \tag{5.17}
\]

Indeed, for \(3\le\ell\le L\), if
\(\sigma_{\ell,00}=0\), then (5.10) gives
\(B_{\ell-1}^0=\chi_{\ell,0}\).  This centered Gaussian is independent
of \(\xi_{\ell-1,0}=Z_{\ell-1}^0\), so

\[
 \mathbb E\partial_{\xi_{\ell-1,0}}C_{\ell-1}^0
 =\mathbb E[\chi_{\ell,0}\phi''(\xi_{\ell-1,0})]=0,
 \qquad
 \mathbb E(C_{\ell-1}^0)^2=K_{\ell,00}d.                 \tag{5.18}
\]

Since \(K_{L,00}=d\), this proves (1.7).  Forward induction and
\(\mathbb E\phi(Z)^2=1\) give \(Q_{\ell,00}=1\).

## 6. Reused-matrix response cancellation at every depth

We prove one identity that applies to every one of the \(5(L-1)\) actions.
Consider one connector and suppress its layer label.  At a representative
output and input coordinate, collect its old row queries and column queries
as \(h\) and \(c\), and its old raw actions as \(y\) and \(d\).  The
inductively identified fields have the form

\[
 y=\xi+Pc,\qquad d=\chi+Sh,                               \tag{6.1}
\]

where \(P\) is the row-query response to column-source coordinates and
\(S\) is the column-query response to row-source coordinates.  Let

\[
 Q=\mathbb E[hh^T],\qquad K=\mathbb E[cc^T].               \tag{6.2}
\]

For a centered, possibly singular Gaussian \(X\) of covariance \(\Sigma\)
and a \(C^1\) polynomial-growth function \(g\),

\[
 \mathbb E[Xg(X)^T]=\Sigma\,\mathbb E[Dg(X)^T].            \tag{6.3}
\]

Indeed, write \(X=BZ\), apply one-dimensional Gaussian integration by
parts to each coordinate of \(Z\), and use \(BB^T=\Sigma\).  The polynomial
envelope justifies integration by parts and the finite sum.

Equation (6.3), first in \(\xi\) and then in \(\chi\), gives the old cross
block

\[
 \mathcal R:=\mathbb E[cy^T]=SQ+KP^T.                     \tag{6.4}
\]

For a new row query \(H_{\rm new}\), set

\[
 q=\mathbb E[hH_{\rm new}],\qquad
 \rho=\mathbb E[\nabla_\chi H_{\rm new}].                 \tag{6.5}
\]

Then

\[
 v:=\mathbb E[dH_{\rm new}]=K\rho+Sq.                     \tag{6.6}
\]

The population form of (4.6) is

\[
 y^TQ^{-1}q+c^TK^{-1}(v-\mathcal RQ^{-1}q)
 +\hbox{orthogonal innovation}.                           \tag{6.7}
\]

Using (6.4)--(6.6),

\[
 K^{-1}(v-\mathcal RQ^{-1}q)
   =\rho-P^TQ^{-1}q.                                      \tag{6.8}
\]

The \(c^TP^TQ^{-1}q\) part of the first term in (6.7) cancels
the last term in (6.8).  Gaussian regression combines the remaining
\(\xi\)-regression and innovation into the new source coordinate.  Thus

\[
 y_{\rm new}=\xi_{\rm new}+\rho^Tc.                        \tag{6.9}
\]

After adjoining this row action, take a new column query \(C_{\rm new}\)
and set

\[
 k=\mathbb E[cC_{\rm new}],\qquad
 \sigma=\mathbb E[\nabla_\xi C_{\rm new}].                \tag{6.10}
\]

Then

\[
 r:=\mathbb E[yC_{\rm new}]=Q\sigma+Pk.                   \tag{6.11}
\]

The population form of (4.4) is

\[
 d^TK^{-1}k+h^TQ^{-1}(r-\mathcal R^TK^{-1}k)
 +\hbox{orthogonal innovation}.                           \tag{6.12}
\]

Equations (6.4) and (6.11) give

\[
 Q^{-1}(r-\mathcal R^TK^{-1}k)
   =\sigma-S^TK^{-1}k.                                    \tag{6.13}
\]

The last term cancels the \(h^TS^TK^{-1}k\) part of
\(d^TK^{-1}k\), and Gaussian regression gives

\[
 d_{\rm new}=\chi_{\rm new}+\sigma^Th.                    \tag{6.14}
\]

For connector \(W_\ell^0\), substitute

\[
 (h,c,y,d,\xi,\chi)
  =(H_{\ell-1},C_\ell,X_\ell,R_{\ell-1},
    \xi_\ell,\chi_\ell).                                  \tag{6.15}
\]

Equations (6.9) and (6.14) therefore identify all its five raw actions:

\[
 X_\ell^s
   \ \longrightarrow\
   \xi_{\ell,s}+\sum_{r<s}\rho_{\ell,sr}C_\ell^r,
 \qquad s=0,1,2,                                          \tag{6.16}
\]

\[
 R_{\ell-1}^s
   \ \longrightarrow\
   \chi_{\ell,s}+\sum_{r\le s}\sigma_{\ell,sr}
                                  H_{\ell-1}^r,
 \qquad s=0,1.                                            \tag{6.17}
\]

Adding the exact learned terms (2.12)--(2.13) yields precisely
(5.7) and (5.10).  Since Lemma 4.1 permits the queries in (6.15) to depend
on the entire previously revealed history of all other connectors, this
single calculation accounts for every cross-layer and reused-column
dependence.  No response term is omitted.

## 7. Complete conditioning-data ledger

For a fixed connector \(\ell\), define the exact empirical cross block

\[
 \mathcal R_{\ell}^{(n)}
  =\frac1n(C_\ell^{\rm old})^TX_\ell^{\rm old}
  =\frac1n(R_{\ell-1}^{\rm old})^TH_{\ell-1}^{\rm old}.    \tag{7.1}
\]

The equality is the matrix identity
\((C_\ell^{\rm old})^TW_\ell^0H_{\ell-1}^{\rm old}/(n\sqrt n)\)
written in two ways.

At a forward action \(X_\ell^s\), the complete list of new inputs to
(4.6)--(4.7) is

\[
 \frac1n(H_{\ell-1}^{0:s-1})^TH_{\ell-1}^s,\qquad
 \frac1n(R_{\ell-1}^{0:s-1})^TH_{\ell-1}^s,\qquad
 \mathcal R_\ell^{(n)},                                   \tag{7.2}
\]

together with the old feature and cotangent Grams.  At a transpose action
\(R_{\ell-1}^s\), the complete list of new inputs to (4.4)--(4.5) is

\[
 \frac1n(C_\ell^{0:s-1})^TC_\ell^s,\qquad
 \frac1n(X_\ell^{0:s})^TC_\ell^s,\qquad
 \mathcal R_\ell^{(n)},                                   \tag{7.3}
\]

again together with the old Grams.  Empty vectors at \(s=0\) are omitted.
Equations (7.2)--(7.3), for

\[
 (\ell,s)\in
 \{2,\ldots,L\}\times\{0,1,2\}
\quad\hbox{forward},\qquad
 \{2,\ldots,L\}\times\{0,1\}
\quad\hbox{transpose},                                    \tag{7.4}
\]

are exactly the \(5(L-1)\) conditioning ledgers.  There is no mixed-layer
Gram to invert; cross-layer dependence is in the predictable queries and
the deterministic responses.

## 8. Concentration, coupling, and uniform integrability

This section proves (1.4)--(1.6) for the actual network.

### 8.1 Two elementary estimates

For \(x\in\mathbb R^n\), write

\[
 \|x\|_{n,p}
   =\left(\frac1n\sum_{i=1}^n|x_i|^p\right)^{1/p}.         \tag{8.1}
\]

If \(Y_i\) are iid centered with a finite \(P\)-th moment, Rosenthal's
inequality, divided by \(n\), gives for \(P\ge2\)

\[
 \left\|\frac1n\sum_{i=1}^nY_i\right\|_{L^P}
 \le C_P\left(
       n^{-1/2}\|Y_1\|_{L^2}
       +n^{-1+1/P}\|Y_1\|_{L^P}\right).                   \tag{8.2}
\]

For an \(n\times n\) standard Gaussian matrix \(M\),

\[
 \mathbb P(\|M\|_{\rm op}>2\sqrt n+t)\le2e^{-t^2/2},       \tag{8.3}
\]

so \(\|M/\sqrt n\|_{\rm op}\) has every fixed moment uniformly in \(n\).

We also need a projection estimate.  Let \(V\in\mathbb R^{n\times r}\)
with fixed \(r\), suppose
\(\lambda_{\min}(V^TV/n)\ge\gamma>0\), and let
\(g\sim N(0,I_n)\) be conditionally independent of \(V\).  Since

\[
 P_Vg=V(V^TV/n)^{-1}\frac{V^Tg}{n},                       \tag{8.4}
\]

the conditional covariance of the coefficient vector is
\((V^TV/n)^{-1}/n\).  Gaussian moments and Minkowski's inequality give,
for finite \(p,P\),

\[
 \left\|\|P_Vg\|_{n,p}\right\|_{L^P(g\mid V)}
 \le \frac{C_{p,P,r,\gamma}}{\sqrt n}
       \sum_{j=1}^r\|V_j\|_{n,p}.                          \tag{8.5}
\]

Thus replacing \(P_V^\perp g\) by \(g\) costs \(o(1)\) in every normalized
finite moment.

### 8.2 One compatible ideal array

For every physical hidden layer, take iid coordinate copies of the scalar
Gaussian marks assigned to it:

* layer \(1\): \(U\) and \(\chi_2\);
* layer \(1<\ell<L\): \(\xi_\ell\) and \(\chi_{\ell+1}\);
* layer \(L\): \(\xi_L\) and \(A\).

Different physical-layer arrays and all fresh Gram--Schmidt normals are
independent.  Extend every time block chronologically by (5.4), and between
extensions apply (5.5)--(5.12).  Coordinates are iid within each physical
layer, while all same-coordinate time dependence is retained.

At each finite-width action, use the same fresh Gaussian vector for the
conditional residual in Lemma 4.1 and for the matching ideal
Gram--Schmidt innovation.  Lemma 4.1 makes these choices simultaneous over
all \(L-1\) connectors despite their interlacing.  This constructs one
joint coupling of the entire list (3.1), rather than separate marginal
couplings.

### 8.3 Good events

Fix \(h\ne0\) satisfying (1.3).  The action list uses only:

* the positive scalar matrices in (1.7);
* the \(2(L-1)\) positive definite two-time matrices in (1.3);
* the positive Schur complements associated with those two-time
  extensions.

This is a finite set.  Let four times its smallest eigenvalue or Schur
complement be \(4\gamma_{L,h}>0\).

Immediately before each action \(t\), let \(\mathcal G_t\) be the
intersection of the preceding good event and the requirements that every
empirical Gram inverted at that action have smallest eigenvalue at least
\(2\gamma_{L,h}\), and every new innovation variance used in a later
action be at least \(2\gamma_{L,h}\).  No lower bound is placed on a
time-two feature innovation.  Stop only the conditional representation,
not the raw network, at the first failure of a good event.

### 8.4 The finite-action induction

Fix arbitrary finite moment orders \(p,P\).  We prove after action \(t\),
simultaneously, the following four assertions.

1. Every stopped field already constructed satisfies (1.4).
2. Every stopped and ideal field has all higher finite moments needed in
   the remaining finite computation, uniformly in \(n\).
3. Every empirical quantity in (7.2)--(7.3) already formed converges in
   \(L^P\) to its displayed population expectation.
4. Before the terminal time-two forward sweep, all three errors are
   \(O_{L,h,p,P}(n^{-1/2})\).

For the base, the coordinates \(H_{1,j}^0=\phi(U_j)\) are iid and
(8.2) gives

\[
 Q_{1,00}^{(n)}\longrightarrow\mathbb E\phi(U)^2=1
\quad\hbox{in every }L^P.                                 \tag{8.6}
\]

Conditionally on \(H_1^0\), the coordinates of
\(X_2^0=W_2^0H_1^0/\sqrt n\) are iid
\(N(0,Q_{1,00}^{(n)})\).  Couple them to \(\xi_{2,0}\) with the same
standard normals.  On \(Q_{1,00}^{(n)}\ge1/2\),

\[
 |\sqrt{Q_{1,00}^{(n)}}-1|
 \le |Q_{1,00}^{(n)}-1|.                                  \tag{8.7}
\]

The complement has probability \(O(n^{-m})\) for arbitrary \(m\), by
applying (8.2) at a sufficiently high moment.  This proves assertions
1--4 for \(X_2^0\).

We now give the full implication from one action to the next.  Every new
query or nonlinear field is obtained from earlier fields and empirical
coefficients by finitely many sums, products, and applications of
\(\phi,\phi'\).  The mean-value theorem and (1.1) show that its coordinate
map \(\Psi\) obeys, for some finite integer \(r=r(L)\),

\[
 |\Psi(x;\theta)-\Psi(x';\theta')|
 \le C_{L,h,M}
   (1+\|x\|^r+\|x'\|^r)
   (\|x-x'\|+\|\theta-\theta'\|).                          \tag{8.8}
\]

Hölder's inequality, using assertion 2 at orders
\(2P\) and \(2Pr\), transfers assertion 1 through this map and preserves
the claimed rate before the terminal sweep.

For the new matrix action, every coefficient in (4.4) or (4.6) is a
rational function of the finite list (7.2) or (7.3).  On the good event,

\[
 \|A^{-1}-B^{-1}\|
 \le\|A^{-1}\|\,\|A-B\|\,\|B^{-1}\|,                      \tag{8.9}
\]

and both inverse norms are at most
\((2\gamma_{L,h})^{-1}\).  A nonterminal innovation standard deviation is
Lipschitz because its variance is bounded below by
\(2\gamma_{L,h}\).  Assertions 3--4 therefore imply
\(O(n^{-1/2})\) convergence of all regression coefficients before the
terminal sweep.  Couple the fresh innovations as in Section 8.2 and use
(8.5); this proves assertion 1 for the new raw action.

For every ideal coordinate observable \(\Theta\) occurring in
(7.2)--(7.3), its coordinates in the relevant physical layer are iid and
have moments of every finite order.  Hence (8.2) gives

\[
 \left\|\frac1n\sum_{i=1}^n\Theta_i-\mathbb E\Theta_1
 \right\|_{L^P}
 \le C_{L,h,P}n^{-1/2}.                                   \tag{8.10}
\]

The actual-minus-ideal empirical difference is controlled by (8.8),
Hölder, and assertion 1.  This proves assertion 3.  The same polynomial
envelopes prove assertion 2.  Thus all four assertions propagate from one
action to the next.

Starting from \(X_2^0\), apply this proved implication successively to the
remaining \(5(L-1)-1\) entries of the explicit list (3.1).  The number is
finite for fixed \(L\), so the induction terminates and does not conceal a
limit in depth.

At a terminal time-two forward action, the new feature Schur complement
may vanish.  For nonnegative \(x,y\), use

\[
 |\sqrt x-\sqrt y|\le\sqrt{|x-y|}.                         \tag{8.11}
\]

The square root in (8.11) can weaken the rate at each successive terminal
connector, so the error must be propagated recursively rather than kept at
\(O(n^{-1/4})\).  We give that recursion explicitly.  Let
\({\cal T}_a\) be the finite ledger of all terminal time-two fields formed
through physical layer \(a\), and write \(Y^{(n)},\widehat Y^{(n)}\) for
the coupled actual and ideal vectors associated with a ledger entry
\(Y\).  For fixed finite \(p,P\), put

\[
 e_{a,n}(p,P)
 =\max_{Y\in{\cal T}_a}
   \left\|\|Y^{(n)}-\widehat Y^{(n)}\|_{n,p}\right\|_{L^P}
 \tag{8.11a}
\]

which is a common majorant for all actual-minus-ideal terminal fields through
physical layer \(a\).  Here and below, whenever Hölder is used, the same
simultaneous induction is invoked at sufficiently larger finite orders
\(p',P'\).  The preterminal part just proved gives
\(e_{1,n}(p,P)\le Cn^{-1/2}\).  If the terminal error through layer \(a\)
is \(e_{a,n}\), then (8.10) for the ideal empirical average and (8.8) plus
Hölder for the actual-minus-ideal part give, for every newly used overlap,

\[
 r_{a,n}(P)
 \le C_{L,h,p,P}\bigl(n^{-1/2}+e_{a,n}(p',P')\bigr).
 \tag{8.11b}
\]

The next connector inverts only its old time-\((0,1)\) Grams.  Their
inverses are uniformly bounded on the good event, so (8.9) shows that its
conditional-mean coefficients and its innovation *variance* have error at
most \(C r_{a,n}\).  If the actual and ideal innovation standard deviations
are \(\tau_{a+1,n}\) and \(\tau_{a+1}\), (8.11), first at moment order
\(2P\), yields

\[
 \|\tau_{a+1,n}-\tau_{a+1}\|_{L^P}
 \le C r_{a,n}(2P)^{1/2}.                                \tag{8.11c}
\]

The old-subspace projection costs \(O(n^{-1/2})\) by (8.5).  The raw
action, its learned term, the preactivation, and its nonlinear image then
obey, by (8.8),

\[
 e_{a+1,n}(p,P)
 \le C_{L,h,p,P}
 \bigl(n^{-1/2}+e_{a,n}(p',P')\bigr)^{1/2}.               \tag{8.11d}
\]

Equivalently, a scalar majorant may be chosen recursively as

\[
 \delta_{1,n}=n^{-1/2},\qquad
 \delta_{a+1,n}=C_a\bigl(n^{-1/2}+\delta_{a,n}\bigr)^{1/2}.
 \tag{8.11e}
\]

Thus \(\delta_{a,n}=O(n^{-2^{-a}})=o(1)\) for every fixed \(a\).  No
terminal time-three Gram is inverted, so this weakened terminal modulus
never affects the lower bounds for the old two-time inverses.  Iterating
(8.11d) through the finite sweep \(X_2^2,\ldots,X_L^2\) therefore proves
(1.4), even if every terminal feature Schur complement vanishes.

### 8.5 Identification of every response coefficient

The empirical regression coefficients use only the raw overlaps
(7.2)--(7.3).  Section 8.4 proves convergence of each overlap to its
population expectation.  Applying the singular-valid Gaussian integration
by parts identity (6.3) gives exactly (6.4), (6.6), and (6.11), and the
algebra (6.8), (6.13) identifies their limits with the responses
\(\rho_{\ell,sr}\) and \(\sigma_{\ell,sr}\).

Thus no finite-width derivative is introduced, and no initialization jet
is imported from the opposite order of limits.  The response coefficients
are consequences of fixed-\(h\) overlap limits.

### 8.6 Removing the stopping and proving uniform integrability

Let \(\Theta_{t,n}\) denote all empirical inverse-Gram coefficients and
innovation scales at action \(t\).  Extend them off the good event by their
deterministic population values:

\[
 \widetilde\Theta_{t,n}
  =\Theta_{t,n}\mathbf1_{\mathcal G_t}
   +\Theta_t\mathbf1_{\mathcal G_t^c}.                     \tag{8.12}
\]

Equations (8.9) and (8.11) show that
\(\widetilde\Theta_{t,n}\to\Theta_t\) in every finite \(L^P\).
They are therefore uniformly integrable.  This extension is only a proof
device; the raw network never contains an inverse empirical Gram.

By running Section 8.4 at arbitrarily high moment order, entrywise Gram
convergence, Weyl's eigenvalue inequality, and Markov's inequality give,
for every prescribed \(m\),

\[
 \mathbb P(\mathcal G_t^c\cap\mathcal G_{t-1})
 \le C_{L,h,m}n^{-m}.                                     \tag{8.13}
\]

The union over \(5(L-1)\) actions has the same form.

It remains to bound the raw network on this exceptional event.  Put

\[
 \mathsf z_{1,s}=\|Z_1^s\|_{n,2},\qquad
 \mathsf a_s=\|a^s\|_{n,2},\qquad
 \mathsf m_{\ell,s}=\|W_\ell^s/\sqrt n\|_{\rm op}.         \tag{8.14}
\]

For \(s=0,1\), define deterministic majorants by the following finite
recursion:

\[
 \mathsf h_{1,s}=M(1+\mathsf z_{1,s}),                    \tag{8.15}
\]

\[
 \mathsf z_{\ell,s}=\mathsf m_{\ell,s}\mathsf h_{\ell-1,s},
 \qquad
 \mathsf h_{\ell,s}=M(1+\mathsf z_{\ell,s}),
 \quad \ell=2,\ldots,L,                                   \tag{8.16}
\]

\[
 \mathsf c_{L,s}=M\mathsf a_s,\qquad
 \mathsf b_{\ell-1,s}=\mathsf m_{\ell,s}\mathsf c_{\ell,s},
 \qquad
 \mathsf c_{\ell-1,s}=M\mathsf b_{\ell-1,s},
 \quad \ell=L,\ldots,2,                                   \tag{8.17}
\]

\[
 \begin{aligned}
 \mathsf a_{s+1}&=\mathsf a_s+\mathsf h_{L,s},\\
 \mathsf z_{1,s+1}&=\mathsf z_{1,s}+\mathsf c_{1,s},\\
 \mathsf m_{\ell,s+1}
   &=\mathsf m_{\ell,s}
     +\mathsf c_{\ell,s}\mathsf h_{\ell-1,s},
       \qquad 2\le\ell\le L .
 \end{aligned}                                             \tag{8.18}
\]

For the terminal time \(s=2\), use only (8.15)--(8.16).
Cauchy--Schwarz and

\[
 \left\|\frac h nxy^T\right\|_{\rm op}
 \le |h|\|x\|_{n,2}\|y\|_{n,2}                            \tag{8.19}
\]

show by direct ascending and descending substitution that every actual
normalized Euclidean field is bounded by the corresponding majorant.
For fixed \(L\), the recursion terminates after finitely many additions and
products.  Hence every majorant is a polynomial with nonnegative
coefficients in

\[
 1+M+\|Z_1^0\|_{n,2}+\|a^0\|_{n,2}
    +\sum_{\ell=2}^L\|W_\ell^0/\sqrt n\|_{\rm op}.         \tag{8.20}
\]

Gaussian vector moments and (8.3) give uniform moments of every order for
(8.20).  For \(p\ge2\),

\[
 \|x\|_{n,p}\le n^{1/2-1/p}\|x\|_{n,2},                   \tag{8.21}
\]

and for \(p<2\), \(\|x\|_{n,p}\le\|x\|_{n,2}\).
Thus every raw field needed in the finite list is bounded by a fixed
polynomial in (8.20) times a fixed power of \(n\).  Choose \(m\) in
(8.13) larger than that power and apply Hölder's inequality.  The
contribution of the exceptional event to every field, Gram, overlap, and
terminal output tends to zero in the required \(L^P\).  This removes the
stopping and proves uniform integrability.

Finally,

\[
 |f_{n,L}^s|
 \le\|a^s\|_{n,2}\|H_L^s\|_{n,2}
 \le\mathsf a_s\mathsf h_{L,s}.                            \tag{8.22}
\]

The right-hand side has a uniform \(L^{1+\delta}\) bound for every fixed
\(\delta>0\).  Coupled field convergence and (8.10) may therefore be
passed through expectation, proving (1.5).

### 8.7 Rank-free one-step prefix

For the prefix (3.3), all actions before the time-one forward sweep invert
only the scalar Grams in (1.7).  At \(X_\ell^1\), the new feature
innovation may have zero population variance.  Use (8.11), propagate its
\(o(1)\) error through \(H_\ell^1\), and pass that field as the predictable
query of the next, independent connector \(W_{\ell+1}^0\).  That next
connector again inverts only its own scalar time-zero feature and
cotangent Grams.  There is no time-one transpose sweep and no time-two
forward sweep, so no newly formed two-time Gram is ever inverted.

Iterating this argument through the finite list
\(X_2^1,\ldots,X_L^1\), and using Sections 8.5--8.6 unchanged, proves
(1.6).

## 9. Exact rank obligation and width-first conclusion

For each connector \(\ell=2,\ldots,L\), the two nonterminal innovation
Schur complements are

\[
 q_{\ell-1}
 =Q_{\ell-1,11}
   -\frac{Q_{\ell-1,01}^2}{Q_{\ell-1,00}},\qquad
 k_{\ell}
 =K_{\ell,11}
   -\frac{K_{\ell,01}^2}{K_{\ell,00}}.                    \tag{9.1}
\]

Since the diagonal entries in (1.7) are positive,

\[
 q_{\ell-1}>0,\quad k_\ell>0,\qquad 2\le\ell\le L,         \tag{9.2}
\]

is equivalent to the \(2(L-1)\) positive-definiteness requirements (1.3).
These are exactly the ranks subsequently used:

* \(Q_{\ell-1}^{[1]}\) is inverted at \(R_{\ell-1}^1\) and
  \(X_\ell^2\);
* \(K_\ell^{[1]}\) is inverted at \(X_\ell^2\).

No three-time Gram and no mixed-connector Gram is inverted.

Sections 2--8 therefore prove the fixed-\(h\), width-first identification
for every fixed finite depth \(L\), including all \(5(L-1)\) adaptive
matrix actions, all response terms, all conditioning overlaps,
concentration, and uniform integrability.

This note does not assert that (9.2) holds on a depth-uniform interval, nor
does it assert depth-uniform \(C^5\) bounds for the scalar DAG.  Those are
the remaining analytic obligations for the general-depth quantitative
theorem.  Conditional only on an activation-defined proof of those
obligations, this width bridge supplies the required identities for
\(F_{2,L}(\eta)\) and \(F_{1,L}(2\eta)\).  No dynamic-cavity or
fixed-\(h\) identification gap remains in the finite-depth statement
proved here.
