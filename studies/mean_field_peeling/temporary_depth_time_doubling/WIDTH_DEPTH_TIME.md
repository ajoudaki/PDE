# Width-first identification at arbitrary finite depth and time

This supplement proves the probabilistic bridge used by the depth--time
comparison.  The width limit is taken at a fixed nonzero step.  No expansion
in the step size occurs anywhere below.

## 1. The theorem

Fix integers \(L\ge1\) and \(N\ge1\), and fix \(h\in\mathbb R\setminus
\{0\}\).  Assume

\[
 \phi\in C^2(\mathbb R),\qquad
 |\phi(x)|\le M(1+|x|),\qquad
 \|\phi'\|_\infty+\|\phi''\|_\infty\le M,                 \tag{1.1}
\]

\[
 \mathbb E\phi(G)^2=1,\qquad G\sim N(0,1).                \tag{1.2}
\]

The \(C^{12}\) activation class in the main study implies (1.1).

For the exact network in Section 2, let \(f_{n,L}^N\) be the output after
\(N\) simultaneous, recomputed ascent steps.  If \(\phi\) is nonconstant,
then every population history Gram used by the
\((2N+1)(L-1)\)-action conditioning chronology is positive definite, and

\[
 \boxed{
 \lim_{n\to\infty}\mathbb E f_{n,L}^N=F_{N,L}(h),}        \tag{1.3}
\]

where \(F_{N,L}(h)\) is the output of the inverse-free Gaussian DAG in
Section 5.  More precisely, one joint coupling identifies every raw matrix
action, preactivation, feature, backsignal, cotangent, empirical Gram, and
raw response cross-moment in every finite mixed normalized \(L^p\) moment.
The empirical regression coefficients, extended as in Section 9, converge
in every finite moment, and the terminal outputs are uniformly integrable.

If \(\phi\) is constant, (1.2) gives \(\phi\equiv\pm1\) and

\[
 \mathbb E f_{n,L}^N=Nh                                           \tag{1.4}
\]

for every \(n\).  Thus (1.3) also holds in that branch, without a cotangent
Gram inversion.

The theorem is pointwise for every fixed \(h\ne0\).  Its constants may
depend on the fixed triple \((L,N,h)\).  It asserts neither a
depth-uniform nor a time-uniform conditioning gap.

For \(L=1\), there is no reused matrix.  The exact coordinate recursion is

\[
 a_j^{s+1}=a_j^s+h\phi(u_j^s),\qquad
 u_j^{s+1}=u_j^s+ha_j^s\phi'(u_j^s),                     \tag{1.5}
\]

and

\[
 f_{n,1}^N={1\over n}\sum_{j=1}^n a_j^N\phi(u_j^N).
                                                                    \tag{1.6}
\]

The coordinate pairs remain iid for every finite \(N\).  Iterating linear
growth and bounded \(\phi'\) bounds the summand in (1.6) by a finite
polynomial in \(|a_j^0|+|u_j^0|\), so it has all finite moments.  Hence
\(\mathbb E f_{n,1}^N=\mathbb E[a_1^N\phi(u_1^N)]\) for every \(n\),
and the claimed identification is exact.  The rest of the supplement
treats the nontrivial case \(L\ge2\).

## 2. Exact finite-width network and updates

All hidden layers have width \(n\), the scalar input is \(1\), and there
are no biases.  Initialize all entries of

\[
 u^0,a^0,W_2^0,\ldots,W_L^0                                  \tag{2.1}
\]

independently as \(N(0,1)\).  At time \(s\), set

\[
 Z_1^s=u^s,\qquad H_1^s=\phi(Z_1^s),                       \tag{2.2}
\]

and, for \(2\le\ell\le L\),

\[
 Z_\ell^s={W_\ell^sH_{\ell-1}^s\over\sqrt n},\qquad
 H_\ell^s=\phi(Z_\ell^s).                                 \tag{2.3}
\]

The output and backpropagated cotangents are

\[
 f_{n,L}^s={1\over n}(a^s)^TH_L^s,\qquad
 C_L^s=a^s\odot\phi'(Z_L^s),                              \tag{2.4}
\]

\[
 B_{\ell-1}^s={(W_\ell^s)^TC_\ell^s\over\sqrt n},\qquad
 C_{\ell-1}^s=B_{\ell-1}^s\odot\phi'(Z_{\ell-1}^s),
 \quad \ell=L,L-1,\ldots,2.                              \tag{2.5}
\]

One mean-field feature-ascent step is

\[
 \theta^{s+1}=\theta^s+hn\nabla_\theta f_{n,L}^s.          \tag{2.6}
\]

Direct differentiation, with every right-hand side evaluated at time
\(s\), gives

\[
 \begin{aligned}
 a^{s+1}&=a^s+hH_L^s,\\
 W_\ell^{s+1}&=W_\ell^s+{h\over\sqrt n}
 C_\ell^s(H_{\ell-1}^s)^T,\qquad 2\le\ell\le L,\\
 Z_1^{s+1}&=Z_1^s+hC_1^s.
 \end{aligned}                                             \tag{2.7}
\]

Indeed,

\[
 \nabla_{W_\ell}f_{n,L}^s
 ={1\over n\sqrt n}C_\ell^s(H_{\ell-1}^s)^T,\qquad
 \nabla_{u}f_{n,L}^s={1\over n}C_1^s.                    \tag{2.8}
\]

Put \(W_\ell=W_\ell^0\), and retain only the initialization matrices in
the raw actions

\[
 X_\ell^s={W_\ell H_{\ell-1}^s\over\sqrt n},\qquad
 R_{\ell-1}^s={W_\ell^TC_\ell^s\over\sqrt n}.             \tag{2.9}
\]

For every layer define the empirical second moments

\[
 Q_{\ell,rs}^{(n)}={1\over n}(H_\ell^r)^TH_\ell^s,\qquad
 K_{\ell,rs}^{(n)}={1\over n}(C_\ell^r)^TC_\ell^s.       \tag{2.10}
\]

Summing (2.7) before substituting in (2.3) and (2.5) yields the exact
finite-\(n\) identities

\[
 Z_\ell^s=X_\ell^s+h\sum_{r<s}Q_{\ell-1,rs}^{(n)}C_\ell^r,
 \qquad 2\le\ell\le L,                                  \tag{2.11}
\]

\[
 B_{\ell-1}^s=R_{\ell-1}^s
   +h\sum_{r<s}K_{\ell,rs}^{(n)}H_{\ell-1}^r,
 \qquad 2\le\ell\le L,                                  \tag{2.12}
\]

\[
 a^s=a^0+h\sum_{r<s}H_L^r,\qquad
 Z_1^s=Z_1^0+h\sum_{r<s}C_1^r.                            \tag{2.13}
\]

There is no current-time term in any sum in (2.11)--(2.13).

## 3. The exact \((2N+1)(L-1)\) chronology

For \(0\le s<N\), first reveal the forward actions

\[
 \mathsf F_{s,2},\mathsf F_{s,3},\ldots,\mathsf F_{s,L},
 \qquad \mathsf F_{s,\ell}:=X_\ell^s,                    \tag{3.1}
\]

then the backward actions

\[
 \mathsf B_{s,L},\mathsf B_{s,L-1},\ldots,\mathsf B_{s,2},
 \qquad \mathsf B_{s,\ell}:=R_{\ell-1}^s.               \tag{3.2}
\]

After the \(N\)-th update reveal only the terminal forward sweep

\[
 \mathsf F_{N,2},\ldots,\mathsf F_{N,L}.                  \tag{3.3}
\]

Thus the number of initialization-matrix actions is exactly

\[
 N\{2(L-1)\}+(L-1)=(2N+1)(L-1).                         \tag{3.4}
\]

An explicit action index is

\[
 \begin{aligned}
 \iota(\mathsf F_{s,\ell})
   &=2s(L-1)+(\ell-1), &&0\le s<N,\\
 \iota(\mathsf B_{s,\ell})
   &=2s(L-1)+(L-1)+(L-\ell+1), &&0\le s<N,\\
 \iota(\mathsf F_{N,\ell})
   &=2N(L-1)+(\ell-1).
 \end{aligned}                                             \tag{3.5}
\]

At \(\mathsf F_{s,\ell}\), the query \(H_{\ell-1}^s\) is known because
the forward sweep has already reached layer \(\ell-1\).  At
\(\mathsf B_{s,\ell}\), the query \(C_\ell^s\) is known because the
backward sweep has already reached layer \(\ell\).  Each query may depend
on every earlier action of every matrix.  In particular,
\(H_{\ell-1}^s\) contains all preceding descending passes through
\(W_\ell^T\), including the reused-column actions of the same matrix.
This is predictable dependence, not independence.

For connector \(\ell\), immediately before \(\mathsf F_{s,\ell}\), the
old row and column query blocks are

\[
 H_{\ell-1}^{<s}=(H_{\ell-1}^0,\ldots,H_{\ell-1}^{s-1}),
 \qquad C_\ell^{<s}=(C_\ell^0,\ldots,C_\ell^{s-1}),       \tag{3.6}
\]

and immediately before \(\mathsf B_{s,\ell}\) they are

\[
 H_{\ell-1}^{\le s},\qquad C_\ell^{<s}.                  \tag{3.7}
\]

Empty blocks at \(s=0\) are omitted.

## 4. Adaptive conditioning for all reused matrices

**Lemma 4.1 (predictable multi-matrix Gaussian conditioning).**
Let \(M_2,\ldots,M_L\) be independent \(n\times n\) standard Gaussian
matrices, independent of an external sigma-field.  Consider any finite
interlacing of actions \(M_\ell q/\sqrt n\) and
\(M_\ell^Tc/\sqrt n\), where the matrix label and the next query are
measurable with respect to all preceding queries and actions.  For a fixed
matrix, collect its old row and column queries in \(H,C\), and set

\[
 Y=MH/\sqrt n,\qquad D=M^TC/\sqrt n.                      \tag{4.1}
\]

Conditionally on the global revealed filtration,

\[
 M=P_CM+MP_H-P_CMP_H+P_C^\perp\widetilde M P_H^\perp,    \tag{4.2}
\]

where the residual matrices \(\widetilde M_2,\ldots,\widetilde M_L\)
are conditionally independent standard Gaussian matrices and independent
of the revealed filtration.

Put

\[
 Q=H^TH/n,\qquad K=C^TC/n,\qquad
 \mathcal R=C^TY/n=D^TH/n.                               \tag{4.3}
\]

If \(Q,K\) are invertible, a new column query \(c_*\) satisfies

\[
 {M^Tc_*\over\sqrt n}
 =DK^{-1}k+HQ^{-1}(r-\mathcal R^TK^{-1}k)
   +\tau_cP_H^\perp g,                                   \tag{4.4}
\]

\[
 k=C^Tc_*/n,\quad r=Y^Tc_*/n,\quad
 \tau_c^2=c_*^Tc_*/n-k^TK^{-1}k.                         \tag{4.5}
\]

A new row query \(q_*\) satisfies

\[
 {Mq_*\over\sqrt n}
 =YQ^{-1}q+CK^{-1}(v-\mathcal RQ^{-1}q)
   +\tau_qP_C^\perp g,                                   \tag{4.6}
\]

\[
 q=H^Tq_*/n,\quad v=D^Tq_*/n,\quad
 \tau_q^2=q_*^Tq_*/n-q^TQ^{-1}q.                         \tag{4.7}
\]

Empty blocks are omitted.  The projector/Moore--Penrose versions remain
valid if a block is singular.

**Proof.**  Induct on the global action number.  Suppose (4.2) holds
before a row query to \(M_j\).  Decompose
\(q_*=P_{H_j}q_*+q_\perp\).  All terms in the action except
\(P_{C_j}^\perp\widetilde M_jq_\perp\) are already measurable.  If
\(q_\perp\ne0\), put \(e=q_\perp/\|q_\perp\|\).  The Gaussian projections

\[
 \widetilde M_jee^T,\qquad \widetilde M_j(I-ee^T)          \tag{4.8}
\]

are independent.  Revealing the first leaves

\[
 P_{C_j}^\perp\widetilde M_j
 P_{\operatorname{span}(H_j,q_*)}^\perp                   \tag{4.9}
\]

fresh and independent of every other matrix residual.  If \(q_\perp=0\),
no residual is revealed.  A transpose action is the same argument with
left and right projections exchanged.  This proves (4.2) after every
adaptive, cross-matrix-dependent action in (3.1)--(3.3).

For (4.4), write \(c_*=CK^{-1}k+c_\perp\).  The first term contributes
\(DK^{-1}k\).  The projection of \(M^Tc_\perp/\sqrt n\) onto
\(\operatorname{span}(H)\) is

\[
 HQ^{-1}{Y^Tc_\perp\over n}
 =HQ^{-1}(r-\mathcal R^TK^{-1}k),                         \tag{4.10}
\]

and its remaining conditional covariance is
\(\tau_c^2P_H^\perp\).  This proves (4.4)--(4.5).
Transposition proves (4.6)--(4.7). \(\square\)

## 5. The population inverse-free Gaussian DAG

All assignments below are chronological.  For every connector
\(2\le\ell\le L\), introduce centered Gaussian source blocks

\[
 \xi_\ell=(\xi_{\ell,0},\ldots,\xi_{\ell,N}),\qquad
 \chi_\ell=(\chi_{\ell,0},\ldots,\chi_{\ell,N-1}),        \tag{5.1}
\]

and independent \(U,A\sim N(0,1)\).  All source blocks, including the
\(\xi\)- and \(\chi\)-blocks belonging to the same connector, are mutually
independent.  Their within-block covariances are

\[
 \mathbb E\xi_{\ell,r}\xi_{\ell,s}
   =Q_{\ell-1,rs}:=\mathbb E[H_{\ell-1}^rH_{\ell-1}^s],   \tag{5.2}
\]

\[
 \mathbb E\chi_{\ell,r}\chi_{\ell,s}
   =K_{\ell,rs}:=\mathbb E[C_\ell^rC_\ell^s].             \tag{5.3}
\]

Each new source coordinate is adjoined only after the covariance on the
right is known.  Section 7 proves that every nonterminal covariance is
positive definite for nonconstant \(\phi\); hence an ordinary Gaussian
regression plus an independent innovation constructs it.  Equivalently,
one may simply take the unique centered Gaussian law with the displayed
finite covariance.  No covariance inverse appears in the DAG assignments
below.

Start with

\[
 Z_1^0=U,\qquad H_1^s=\phi(Z_1^s).                        \tag{5.4}
\]

For each \(s=0,\ldots,N\), perform the ascending sweep.  For
\(\ell=2,\ldots,L\), define

\[
 \rho_{\ell,sr}
 :=\mathbb E[\partial_{\chi_{\ell,r}}H_{\ell-1}^s],
 \qquad 0\le r<s,                                        \tag{5.5}
\]

\[
 Z_\ell^s=\xi_{\ell,s}
  +\sum_{r<s}(\rho_{\ell,sr}+hQ_{\ell-1,rs})C_\ell^r,
 \qquad H_\ell^s=\phi(Z_\ell^s).                         \tag{5.6}
\]

If \(s<N\), set

\[
 a^s=A+h\sum_{r<s}H_L^r,\qquad
 C_L^s=a^s\phi'(Z_L^s),                                  \tag{5.7}
\]

and descend from \(\ell=L\) to \(2\).  Define

\[
 \sigma_{\ell,sr}
 :=\mathbb E[\partial_{\xi_{\ell,r}}C_\ell^s],
 \qquad 0\le r\le s,                                    \tag{5.8}
\]

\[
 B_{\ell-1}^s=\chi_{\ell,s}
   +\sum_{r\le s}\sigma_{\ell,sr}H_{\ell-1}^r
   +h\sum_{r<s}K_{\ell,rs}H_{\ell-1}^r,                 \tag{5.9}
\]

\[
 C_{\ell-1}^s=B_{\ell-1}^s\phi'(Z_{\ell-1}^s).          \tag{5.10}
\]

At the bottom set

\[
 Z_1^{s+1}=Z_1^s+hC_1^s.                                 \tag{5.11}
\]

After the terminal forward sweep,

\[
 a^N=A+h\sum_{r<N}H_L^r,\qquad
 \boxed{F_{N,L}(h)=\mathbb E[a^NH_L^N].}                 \tag{5.12}
\]

This is a finite DAG, not a fixed-point definition.  At a given time,
the current \(\xi\)-coordinate is extended in ascending layer order; the
current \(\chi\)-coordinate is then extended in descending layer order.
The source derivative in (5.5) or (5.8) is computed by initializing its
own source derivative to one, all other source derivatives to zero, and
propagating through earlier assignments with

\[
 D\phi(X)=\phi'(X)DX,\quad D\phi'(X)=\phi''(X)DX,\quad
 D(XY)=XDY+YDX.                                           \tag{5.13}
\]

There are finitely many nodes.  Linear growth of \(\phi\), bounded
\(\phi',\phi''\), and Gaussian moments give polynomial Gaussian envelopes
for every value and derivative field.  Therefore all responses in
(5.5),(5.8) are finite, and the derivative expectations are justified by
dominated convergence.

## 6. Response cancellation at every action

Fix one connector and suppress its layer label.  Before an action collect
the old row queries, old column queries, and their raw actions into random
vectors \(\mathsf h,\mathsf c,\mathsf y,\mathsf d\).  Inductively the
population actions have the form

\[
 \mathsf y=\xi+P\mathsf c,\qquad
 \mathsf d=\chi+S\mathsf h,                               \tag{6.1}
\]

where \(P\) is strictly causal and \(S\) is causal.  Put

\[
 Q=\mathbb E[\mathsf h\mathsf h^T],\qquad
 K=\mathbb E[\mathsf c\mathsf c^T].                       \tag{6.2}
\]

For any centered, possibly singular Gaussian vector \(X\) and any
\(C^1\) polynomial-growth \(g\),

\[
 \mathbb E[Xg(X)^T]=\operatorname{Cov}(X)\,
                    \mathbb E[Dg(X)^T].                  \tag{6.3}
\]

To prove (6.3), write \(X=BZ\) with \(Z\) standard Gaussian, apply
one-dimensional integration by parts to each coordinate of \(Z\), and
use \(BB^T=\operatorname{Cov}(X)\).  The polynomial envelope justifies
the integration by parts even when \(B\) is singular.

Applying (6.3) separately to the independent \(\xi\)- and \(\chi\)-blocks
gives the old cross block

\[
 \mathcal R:=\mathbb E[\mathsf c\mathsf y^T]=SQ+KP^T.     \tag{6.4}
\]

For a new row query \(H_*\), let

\[
 q=\mathbb E[\mathsf hH_*],\qquad
 \rho=\mathbb E[\nabla_\chi H_*].                        \tag{6.5}
\]

Then

\[
 v:=\mathbb E[\mathsf dH_*]=K\rho+Sq.                    \tag{6.6}
\]

The population limit of (4.6) is

\[
 \mathsf y^TQ^{-1}q+
 \mathsf c^TK^{-1}(v-\mathcal RQ^{-1}q)
 +\text{orthogonal innovation}.                          \tag{6.7}
\]

Equations (6.4)--(6.6) imply

\[
 K^{-1}(v-\mathcal RQ^{-1}q)
 =\rho-P^TQ^{-1}q.                                       \tag{6.8}
\]

The \(\mathsf c^TP^TQ^{-1}q\) part of the first term in
(6.7) cancels the last term in (6.8).  Gaussian regression combines the
remaining old-source regression and orthogonal innovation into the new
source coordinate.  Hence

\[
 X_\ell^s\ \Longrightarrow\
 \xi_{\ell,s}+\sum_{r<s}\rho_{\ell,sr}C_\ell^r.          \tag{6.9}
\]

After adjoining that row action, consider a new column query \(C_*\).  Put

\[
 k=\mathbb E[\mathsf cC_*],\qquad
 \sigma=\mathbb E[\nabla_\xi C_*].                       \tag{6.10}
\]

Gaussian integration by parts gives

\[
 r:=\mathbb E[\mathsf yC_*]=Q\sigma+Pk.                  \tag{6.11}
\]

The population limit of (4.4) is

\[
 \mathsf d^TK^{-1}k+
 \mathsf h^TQ^{-1}(r-\mathcal R^TK^{-1}k)
 +\text{orthogonal innovation}.                          \tag{6.12}
\]

Now

\[
 Q^{-1}(r-\mathcal R^TK^{-1}k)
 =\sigma-S^TK^{-1}k.                                     \tag{6.13}
\]

The last term cancels the \(\mathsf h^TS^TK^{-1}k\) part of
\(\mathsf d^TK^{-1}k\), so

\[
 R_{\ell-1}^s\ \Longrightarrow\
 \chi_{\ell,s}+\sum_{r\le s}\sigma_{\ell,sr}
                                  H_{\ell-1}^r.           \tag{6.14}
\]

Adding the exact learned terms (2.11)--(2.12) gives (5.6) and (5.9).
Lemma 4.1 allows every query here to depend on all earlier actions of all
connectors.  Thus (6.9)--(6.14) include, rather than discard, the dependence
of \(H_{\ell-1}^s\) on every reused column of \(W_\ell\).

## 7. Strict rank for every finite history

Write

\[
 Q_\ell^{[s]}=(\mathbb E H_\ell^rH_\ell^q)_{0\le r,q\le s},
 \qquad
 K_\ell^{[s]}=(\mathbb E C_\ell^rC_\ell^q)_{0\le r,q\le s}.
                                                                    \tag{7.1}
\]

At a forward action, the inverted old-query Grams are
\(Q_{\ell-1}^{[s-1]}\) and \(K_\ell^{[s-1]}\), with the \(Q\)-block
empty at \(s=0\); its row-query Schur complement extends
\(Q_{\ell-1}^{[s-1]}\) to \(Q_{\ell-1}^{[s]}\).  At the subsequent
transpose action, the inverted blocks are \(Q_{\ell-1}^{[s]}\) and
\(K_\ell^{[s-1]}\), and its column-query Schur complement extends
\(K_\ell^{[s-1]}\) to \(K_\ell^{[s]}\).  These statements apply for
\(2\le\ell\le L\); empty blocks are omitted.

We prove the stronger collection needed by the layer-time induction:

\[
 Q_\ell^{[s]}>0\quad(1\le\ell\le L,\ 0\le s\le N),       \tag{7.2}
\]

\[
 K_\ell^{[s]}>0\quad(1\le\ell\le L,\ 0\le s<N).        \tag{7.3}
\]

Here \(K_1\) is not inverted; including it makes the bottom induction
transparent.

### 7.1 Two elementary facts

If \(g:\mathbb R\to\mathbb R\) is continuous and nonconstant, then

\[
 \operatorname{Var}(g(x+\tau G))>0
 \quad\text{for every }x\in\mathbb R,\ \tau>0.           \tag{7.4}
\]

Indeed, zero variance would make \(g\) constant almost everywhere for a
law with a strictly positive density; continuity would make it constant
everywhere.

Second, suppose \(X_0,\ldots,X_{s-1}\) are measurable with respect to
\(\mathcal F\), their second-moment Gram is positive definite, and

\[
 \mathbb E\operatorname{Var}(X_s\mid\mathcal F)>0.        \tag{7.5}
\]

Then the Gram of \(X_0,\ldots,X_s\) is positive definite.  For if the
coefficient of \(X_s\) in a linear combination is nonzero, conditioning
leaves strictly positive mean-square residual by (7.5); if it is zero, use
the old positive Gram.

### 7.2 Initialization

Let

\[
 d=\mathbb E\phi'(G)^2.                                  \tag{7.6}
\]

If \(\phi\) is nonconstant, then \(d>0\).  At time zero every forward
preactivation is standard Gaussian and, by (1.2),

\[
 Q_{\ell,00}=1\qquad(1\le\ell\le L).                     \tag{7.7}
\]

The time-zero response coefficients vanish by centering of the independent
top weight and the descending centered Gaussian carriers.  Descending from
the top gives

\[
 K_{\ell,00}=d^{L-\ell+1}>0,\qquad 1\le\ell\le L.         \tag{7.8}
\]

Also

\[
 \mathbb P\{\phi'(Z_1^0)\ne0\}>0                         \tag{7.9}
\]

because \(Z_1^0=U\) has full support and \(\phi'\not\equiv0\).

### 7.3 The layer-time induction

Assume at the beginning of forward time \(s\) that
\(Q_1^{[s]}>0\), all \(K_\ell^{[s-1]}>0\) when \(s\ge1\), and

\[
 \mathbb P\{\phi'(Z_1^s)\ne0\}>0.                        \tag{7.10}
\]

For \(s=0\), these are (7.7)--(7.9), with the old \(K\)-condition empty.

Ascend through \(\ell=2,\ldots,L\).  Once
\(Q_{\ell-1}^{[s]}>0\), Gaussian regression realizes

\[
 \xi_{\ell,s}=m_{\ell,s}(\xi_{\ell,<s})+
                     \tau_{\ell,s}E_{\ell,s},\qquad
 \tau_{\ell,s}>0,                                       \tag{7.11}
\]

where \(E_{\ell,s}\) is independent of every source revealed earlier.
All terms in (5.6) other than \(\tau_{\ell,s}E_{\ell,s}\) are measurable
without this innovation.  All older \(H_\ell^r\), \(r<s\), are measurable
there as well.  Conditional on that sigma-field,

\[
 H_\ell^s=\phi(x+\tau_{\ell,s}E_{\ell,s}).                \tag{7.12}
\]

Equations (7.4)--(7.5) prove \(Q_\ell^{[s]}>0\).  This ascending induction
establishes (7.2) at time \(s\) for every layer.  It also shows, for every
\(\ell\ge2\),

\[
 \mathbb P\{\phi'(Z_\ell^s)\ne0\}>0,                     \tag{7.13}
\]

because conditionally \(Z_\ell^s\) has full support and the nonempty open
set \(\{x:\phi'(x)\ne0\}\) has positive Gaussian probability.

Suppose now \(s<N\).  We first extend the top cotangent Gram.  If \(\phi'\)
is nonconstant, use the same fresh innovation in \(\xi_{L,s}\).  The
quantity \(a^s\) is measurable without it, and

\[
 C_L^s=a^s\phi'(x+\tau_{L,s}E_{L,s}).                     \tag{7.14}
\]

Moreover,

\[
 \mathbb P\{a^s\ne0\}>0.                                 \tag{7.15}
\]

For \(s=0\), \(a^0=A\).  For \(s\ge1\), condition on the chronological
sigma-field immediately before the fresh \(\xi_{L,s-1}\) innovation is
adjoined.  Then

\[
 a^s=a^{s-1}+h\phi(x+\tau_{L,s-1}E_{L,s-1})               \tag{7.16}
\]

has positive conditional variance by (7.4), since \(h\ne0\).
On the positive-probability event in (7.15), (7.4) applied to \(\phi'\)
and (7.5) show \(K_L^{[s]}>0\).

The remaining possibility for a nonconstant \(C^1\) activation is that
\(\phi'\) is constant.  Then

\[
 \phi(x)=px+c,\qquad p\ne0.                               \tag{7.17}
\]

The scalar \(K_{L,00}=p^2\) is positive.  For \(s\ge1\), condition as in
(7.16).  Since \(C_L^s=pa^s\), its fresh innovation is

\[
 hp^2\tau_{L,s-1}E_{L,s-1},                               \tag{7.18}
\]

whose conditional variance is \(h^2p^4\tau_{L,s-1}^2>0\).
All old \(C_L^r\), \(r<s\), exclude this innovation.  Thus (7.5) again
proves \(K_L^{[s]}>0\).  This is the affine branch; it is not covered by
an appeal to nonconstancy of \(\phi'\).

Now descend through \(\ell=L-1,L-2,\ldots,1\).  Once
\(K_{\ell+1}^{[s]}>0\), write the current source as

\[
 \chi_{\ell+1,s}=\widetilde m_{\ell,s}(\chi_{\ell+1,<s})
                   +\upsilon_{\ell,s}G_{\ell,s},\qquad
 \upsilon_{\ell,s}>0.                                   \tag{7.19}
\]

The current forward field \(Z_\ell^s\), every old \(C_\ell^r\), and all
other terms in \(B_\ell^s\) are measurable without \(G_{\ell,s}\).
Consequently

\[
 C_\ell^s=(x+\upsilon_{\ell,s}G_{\ell,s})
                           \phi'(Z_\ell^s).               \tag{7.20}
\]

The multiplier is nonzero with positive probability by (7.13) for
\(\ell\ge2\), and by (7.10) for \(\ell=1\).  Therefore

\[
 \mathbb E\operatorname{Var}(C_\ell^s\mid\mathcal F)>0,
\]

and (7.5) proves \(K_\ell^{[s]}>0\).  This completes the backward rank
induction.

Finally, use the current \(\chi_{2,s}\) innovation in
\(Z_1^{s+1}=Z_1^s+hC_1^s\).  Without that innovation,

\[
 H_1^{s+1}
 =\phi\!\left(x+h\upsilon_{1,s}\phi'(Z_1^s)G_{1,s}\right).
                                                                    \tag{7.21}
\]

On the event in (7.10), the Gaussian coefficient is nonzero.  Equations
(7.4)--(7.5) give \(Q_1^{[s+1]}>0\).  On the same event the argument of
\(\phi\) in (7.21) has full support, so the nonempty open set
\(\{x:\phi'(x)\ne0\}\) is hit with positive conditional probability.
Hence

\[
 \mathbb P\{\phi'(Z_1^{s+1})\ne0\}>0.                    \tag{7.22}
\]

This supplies the induction hypotheses at time \(s+1\).  Starting from
Section 7.2 and iterating for \(s=0,\ldots,N-1\) proves (7.2)--(7.3).
Every Schur complement used to create a new source coordinate is therefore
strictly positive.  The proof is pointwise on the entire punctured
\(h\)-line and uses no small-step expansion.

## 8. Complete empirical conditioning ledger

For connector \(\ell\), distinguish the cross block before the forward
action from the enlarged block before the backward action:

\[
 \mathcal R_{\ell,s}^{F,(n)}
 ={1\over n}(C_\ell^{<s})^TX_\ell^{<s}
 ={1\over n}(R_{\ell-1}^{<s})^TH_{\ell-1}^{<s}.           \tag{8.1}
\]

The equality is the exact matrix identity
\((C_\ell^{<s})^TW_\ell H_{\ell-1}^{<s}/(n\sqrt n)\)
written in two ways.  After \(\mathsf F_{s,\ell}\), the row-query block
has one additional column, so

\[
 \begin{aligned}
 \mathcal R_{\ell,s}^{B,(n)}
 &={1\over n}(C_\ell^{<s})^TX_\ell^{\le s}
   ={1\over n}(R_{\ell-1}^{<s})^TH_{\ell-1}^{\le s}\\
 &=\left[\mathcal R_{\ell,s}^{F,(n)},
 {1\over n}(R_{\ell-1}^{<s})^TH_{\ell-1}^s\right].       \tag{8.1a}
 \end{aligned}
\]

Thus the extra column in the backward cross block is exactly the second
query cross-moment already formed for the forward action; it is not
dropped.

At \(\mathsf F_{s,\ell}\), the full list of new regression data is

\[
 {1\over n}(H_{\ell-1}^{<s})^TH_{\ell-1}^s,\qquad
 {1\over n}(R_{\ell-1}^{<s})^TH_{\ell-1}^s,\qquad
 {1\over n}\|H_{\ell-1}^s\|_2^2,\qquad
 \mathcal R_{\ell,s}^{F,(n)},                            \tag{8.2}
\]

together with the old feature and cotangent Grams.  At
\(\mathsf B_{s,\ell}\), it is

\[
 {1\over n}(C_\ell^{<s})^TC_\ell^s,\qquad
 {1\over n}(X_\ell^{\le s})^TC_\ell^s,\qquad
 {1\over n}\|C_\ell^s\|_2^2,\qquad
 \mathcal R_{\ell,s}^{B,(n)},                            \tag{8.3}
\]

together with \(Q_{\ell-1}^{[s]}\) and \(K_\ell^{[s-1]}\).  Equations
(8.2)--(8.3), over precisely the index set (3.1)--(3.3), contain every
empirical quantity in (4.4)--(4.7).  No mixed-connector Gram is inverted.

## 9. Joint coupling, concentration, and stopping

Set

\[
 \mathcal A=(2N+1)(L-1),\qquad \Lambda=3\mathcal A+1.     \tag{9.1}
\]

The following explicit micro-ledger has at most \(\Lambda\) entries.
First construct the initialization marks, \(H_1^0\), and their empirical
moments.  For each action in (3.5), in order:

1. perform the Gaussian matrix action;
2. perform every coordinate assignment made possible by it (including
   the top cotangent after \(\mathsf F_{s,L}\), the lower update after
   \(\mathsf B_{s,2}\), and the terminal output after
   \(\mathsf F_{N,L}\));
3. form every pair moment in (8.2)--(8.3) needed by the next action.

Empty bundles count as one harmless entry.  Thus there are at most one
initial entry plus three for each of the exactly \(\mathcal A\) actions,
which proves (9.1).

### 9.1 Ideal coordinate arrays

For each physical layer use iid coordinate copies of the following scalar
marks:

\[
 \begin{array}{c|c}
 \text{physical layer}&\text{marks}\\
 \hline
 1&U,\chi_2\\
 1<\ell<L&\xi_\ell,\chi_{\ell+1}\\
 L&\xi_L,A.
 \end{array}                                               \tag{9.2}
\]

Arrays belonging to different physical layers are independent.  Within a
layer, the same coordinate is reused through time with the covariance in
(5.2)--(5.3).  This retains every within-coordinate temporal dependence,
while coordinates within one physical population are iid.

Here is the action-by-action extension, including the alternating physical
layers.  At \(\mathsf F_{s,\ell}\), after the ideal query
\(\bar H_{\ell-1}^s\) and \(Q_{\ell-1}^{[s]}\) have been formed, write

\[
 \begin{cases}
 \alpha_{\ell,0}^{\xi}=0,\quad
       (\tau_{\ell,0}^{\xi})^2=Q_{\ell-1,00},&s=0,\\[2mm]
 \alpha_{\ell,s}^{\xi}
 =Q_{\ell-1,s,<s}(Q_{\ell-1}^{[s-1]})^{-1},\quad
 (\tau_{\ell,s}^{\xi})^2
 =Q_{\ell-1,ss}
  -Q_{\ell-1,s,<s}(Q_{\ell-1}^{[s-1]})^{-1}
     Q_{\ell-1,<s,s},&s\ge1.
 \end{cases}                                             \tag{9.2a}
\]

For the \(i\)-coordinates of physical layer \(\ell\), take a fresh iid Gaussian vector
\(g_{\mathsf F_{s,\ell}}\) and set

\[
 \bar\xi_{\ell,s}
 =\alpha_{\ell,s}^{\xi}\bar\xi_{\ell,<s}
   +\tau_{\ell,s}^{\xi}g_{\mathsf F_{s,\ell}}.             \tag{9.2b}
\]

Use this coordinate in (5.6), then make the coordinate and moment bundles
before the next action.  At \(\mathsf B_{s,\ell}\), after
\(\bar C_\ell^s\) and \(K_\ell^{[s]}\) have been formed, put

\[
 \begin{cases}
 \alpha_{\ell,0}^{\chi}=0,\quad
       (\tau_{\ell,0}^{\chi})^2=K_{\ell,00},&s=0,\\[2mm]
 \alpha_{\ell,s}^{\chi}
 =K_{\ell,s,<s}(K_\ell^{[s-1]})^{-1},\quad
 (\tau_{\ell,s}^{\chi})^2
 =K_{\ell,ss}
  -K_{\ell,s,<s}(K_\ell^{[s-1]})^{-1}K_{\ell,<s,s},&s\ge1.
 \end{cases}                                             \tag{9.2c}
\]

For the \(j\)-coordinates of physical layer \(\ell-1\), take a fresh iid vector
\(g_{\mathsf B_{s,\ell}}\) and set

\[
 \bar\chi_{\ell,s}
 =\alpha_{\ell,s}^{\chi}\bar\chi_{\ell,<s}
   +\tau_{\ell,s}^{\chi}g_{\mathsf B_{s,\ell}}.            \tag{9.2d}
\]

Use it in (5.9), then make the next coordinate and moment bundles.
All vectors \(g_{\mathsf F_{s,\ell}},g_{\mathsf B_{s,\ell}}\), over the
exact order (3.5), are mutually independent and independent of the initial
arrays.  At the matching raw action use that same fresh vector for the
conditional residual in Lemma 4.1.  Conditional independence of the
remaining matrix residuals makes this simultaneous even when the next
action belongs to another connector or the opposite physical layer.
Induction over (3.5), integrating the exact next-action kernel against the
already matched past law, proves that the raw side of this one coupling has
exactly the joint law of the network in Section 2.

### 9.2 Spectral stopping

By Section 7, the finite list of population old-query Grams and
nonterminal query Schur complements is strictly positive.  Define

\[
 4\gamma_{L,N,h}=\min\{1,\lambda_{\min}(G),v:\
 G\text{ is inverted and }v\text{ is a source Schur complement in the
 chronology}\}>0.                                        \tag{9.3}
\]

The terminal forward innovations are included.  Immediately before an
action, first test that every required empirical old Gram has least
eigenvalue at least \(2\gamma_{L,N,h}\).  Only on that branch evaluate its
Schur formula, then test that every new empirical innovation variance is at
least \(2\gamma_{L,N,h}\).  This defines a predictable good event and
never evaluates the inverse of a failed Gram.

On the good event use the exact coefficients and projected residual in
(4.4) or (4.6).  Off it, replace all coefficients and innovation scales by
their deterministic population values and replace the residual projection
by the identity.  These are the *extended* actions.  The raw network is not
altered.  Formally, set \(\mathcal G_{-1}=\Omega\) and let
\(\mathcal G_q\) be \(\mathcal G_{q-1}\) intersected with the tests first
needed at action \(q\).  On \(\mathcal G_{q-1}\), the raw and extended
histories agree before the tests, so the event is simultaneously an event
of either history.  Independently, generate the raw action on every event
from the exact Moore--Penrose conditional kernel in Lemma 4.1.  Thus the
extension is only a coupling device and never changes the raw law.

### 9.3 Three estimates

For \(x\in\mathbb R^n\), write

\[
 \|x\|_{n,p}=\left(\frac1n\sum_{i=1}^n|x_i|^p\right)^{1/p}.
 \tag{9.3a}
\]

For iid centered \(Y_i\) and \(r\ge2\), Rosenthal's inequality gives

\[
 \left\|{1\over n}\sum_{i=1}^nY_i\right\|_{L^r}
 \le C_rn^{-1/2}\|Y_1\|_{L^r}.                            \tag{9.4}
\]

If fields \(X_n,Y_n\) are coupled to iid coordinate fields
\(\bar X,\bar Y\), normalized Cauchy--Schwarz and Holder give

\[
 \begin{aligned}
 &\left\|{1\over n}X_n^TY_n-\mathbb E\bar X_1\bar Y_1
       \right\|_{L^r}\\
 &\quad\le
 \left\|\|X_n-\bar X\|_{n,2r}\right\|_{L^{2r}}
 \left\|\|Y_n\|_{n,2r}\right\|_{L^{2r}}\\
 &\qquad+
 \left\|\|\bar X\|_{n,2r}\right\|_{L^{2r}}
 \left\|\|Y_n-\bar Y\|_{n,2r}\right\|_{L^{2r}}
 +C_rn^{-1/2}\|\bar X_1\bar Y_1\|_{L^r}.                \tag{9.5}
 \end{aligned}
\]

Thus field errors \(O(n^{-1/2})\) at order \(2r\) imply the same rate for
every empirical entry in (8.2)--(8.3) at order \(r\).

For a matrix action, on the good event the inverse identity

\[
 A^{-1}-B^{-1}=A^{-1}(B-A)B^{-1}                          \tag{9.6}
\]

gives the following explicit coefficient estimate.  Let \(\delta_n\) be
the maximum error of all Gram and cross-moment entries in (8.2) or (8.3),
and let \(\mathcal Z_n\) be one plus the sum of their absolute values and
their population counterparts.  Expanding (4.4) or (4.6), replacing one
factor at a time, and using the good-event inverse bound gives

\[
 \max_j|\alpha_{j,n}-\alpha_j|
   +|\tau_n^2-\tau^2|
 \le C_{L,N,h}\mathcal Z_n^2\delta_n.                    \tag{9.6a}
\]

For example, the longest coefficient is
\(K_n^{-1}\mathcal R_nQ_n^{-1}q_n\); its difference is the sum of the
four terms obtained by replacing \(K_n^{-1},\mathcal R_n,Q_n^{-1},q_n\)
in turn, with each inverse replacement controlled by (9.6).  The other
coefficients have fewer factors.  The Schur expression for
\(\tau_n^2\) has at most two unbounded moment factors.  On the good event
both inverse factors are bounded deterministically, so no term contains
more than two factors from \(\mathcal Z_n\); this proves (9.6a), rather
than leaving the replacement implicit.  Since empirical and population
innovation variances are at least \(2\gamma_{L,N,h}\),

\[
 |\sqrt{x}-\sqrt y|
 \le {1\over2\sqrt{2\gamma_{L,N,h}}}|x-y|.                \tag{9.7}
\]

The Schur complement is a squared orthogonal-residual norm, so
\(0\le\tau_n^2\le n^{-1}\|q_*\|_2^2\) (and similarly for a column
query).  Thus preceding query moments also bound every moment of
\(\tau_n\); no upper spectral stopping is required.

If \(V\) has at most \(N+1\) old query columns,
\(\lambda_{\min}(V^TV/n)\ge2\gamma_{L,N,h}\), and
\(g\sim N(0,I_n)\) is conditionally fresh, then

\[
 \left(\mathbb E_g\|P_Vg\|_{n,r}^r\right)^{1/r}
 \le C_{r,N,\gamma}n^{-1/2}
              \sum_j\|V_j\|_{n,r}.                       \tag{9.8}
\]

Indeed, the coefficient vector in
\(P_Vg=V(V^TV/n)^{-1}(V^Tg/n)\) is conditionally Gaussian with covariance
\((V^TV/n)^{-1}/n\).  It remains to combine these estimates without
hiding any field-error term.

To display every error term, write either row or column action on the good
event in the common form

\[
 T_n=\sum_{j=1}^d\alpha_{j,n}V_{j,n}
             +\tau_nP_{\mathcal S_n}^{\perp}g,\qquad
 \bar T=\sum_{j=1}^d\alpha_j\bar V_j+\tau g,              \tag{9.8a}
\]

where the old-span fields \(V_j\) include the old raw actions and old
queries appearing in (4.4) or (4.6), and
\(\mathcal S_n\) is the old opposite-query span.  With the same fresh
\(g\),

\[
 \begin{aligned}
 T_n-\bar T
 ={}&\sum_j\alpha_{j,n}(V_{j,n}-\bar V_j)
   +\sum_j(\alpha_{j,n}-\alpha_j)\bar V_j\\
  &+(\tau_n-\tau)g-\tau_nP_{\mathcal S_n}g.              \tag{9.8b}
 \end{aligned}
\]

The first line contains, separately, the preceding-query/old-action errors
and the old-span coefficient errors.  The second line contains the scale
error and the removed finite-dimensional projection.  Holder, (9.6a),
(9.7), and (9.8) bound the four terms in (9.8b), respectively, by
\(Cn^{-1/2}\), \(Cn^{-1/2}\), \(Cn^{-1/2}\), and \(Cn^{-1/2}\) in
\(L^r(\|\cdot\|_{n,r})\), provided the preceding field and empirical
errors and moments are available at order \(8r\).  Thus

\[
 \text{input errors at order }8r
 \quad\Longrightarrow\quad
 \text{new action error at order }r\text{ is }O(n^{-1/2}). \tag{9.9}
\]

Off the good event, the extended and ideal Gaussian terms use identical
population coefficients and the same full \(g\); their difference contains
only preceding extended-field errors.  Hence (9.9) holds globally for the
extended action, without an empirical inverse off the good event.

### 9.4 The finite moment tower

For a desired terminal moment \(r_*\ge2\), set

\[
 R_\Lambda=r_*,\qquad R_{j-1}=8R_j\quad(1\le j\le\Lambda).
                                                                    \tag{9.10}
\]

Thus \(R_0=8^\Lambda r_*<\infty\).  A coordinate bundle consumes at most
order \(4r\): the only nonlinear products are an empirical scalar times a
field and \(a\phi'(z)\) or \(b\phi'(z)\); bounded \(\phi',\phi''\) and
Holder give the factor four.  A pair-moment bundle consumes order \(2r\)
by (9.5), and a matrix action consumes order \(8r\) by (9.9).  Therefore
(9.10) supplies every moment used by each of the at most \(\Lambda\)
microsteps.

At the initial microstep the marks are Gaussian and \(\phi\) has linear
growth, so moment \(R_0\) is finite.  Applying, in the exact order of the
micro-ledger, the coordinate estimate, (9.5), and (9.9) proves for every
microstep \(j\), every fixed \(r\ge2\),

\[
 \sup_n\mathcal M_{j,r}(n)<\infty,
 \qquad \mathcal E_{j,r}(n)\le C_{j,r}n^{-1/2},           \tag{9.11}
\]

where \(\mathcal M\) is the maximum moment of all extended fields and
observables already constructed and \(\mathcal E\) is their maximum
extended-to-ideal error.  This is a literal induction over the explicitly
indexed list of at most \(3(2N+1)(L-1)+1\) entries; (9.10) shows that it
terminates and does not hide an all-orders assumption.

On the good branch every empirical regression coefficient is one of the
finite rational expressions (4.4)--(4.7); off it the extended coefficient
is its population value.  Equations (9.6)--(9.11), at arbitrary finite
moment order, therefore also prove convergence of every extended
coefficient in every finite \(L^r\).  Taking any larger order than one
gives its uniform integrability.

For a requested failure exponent \(m\ge1\), run (9.10) with
\(r_*=2m\).  Weyl's inequality, (9.11), and Markov's inequality show at
each action that a first violation of a threshold in Section 9.2 has
probability at most \(C_mn^{-m}\).  A union bound over the exactly
\(\mathcal A\) actions gives

\[
 \mathbb P(\text{stopping occurs})
 \le C_{L,N,h,M,m}n^{-m}.                                \tag{9.12}
\]

The largest initialization moment used for this assertion is explicitly

\[
 2m\,8^{3(2N+1)(L-1)+1}.                                \tag{9.13}
\]

## 10. Removing stopping and terminal uniform integrability

Define normalized raw-network quantities

\[
 A_s=\|a^s\|_{n,2},\quad U_s=\|Z_1^s\|_{n,2},\quad
 M_{\ell,s}=\|W_\ell^s/\sqrt n\|_{\mathrm{op}}.           \tag{10.1}
\]

Let \(H=|h|\).  Starting from these quantities, make the following finite
deterministic majorant recursion for \(0\le s<N\):

\[
 \widehat H_{1,s}=M(1+\widehat U_s),                      \tag{10.2}
\]

\[
 \widehat Z_{\ell,s}=\widehat M_{\ell,s}
                         \widehat H_{\ell-1,s},\qquad
 \widehat H_{\ell,s}=M(1+\widehat Z_{\ell,s}),
 \quad \ell=2,\ldots,L,                                  \tag{10.3}
\]

\[
 \widehat C_{L,s}=M\widehat A_s,                         \tag{10.4}
\]

\[
 \widehat B_{\ell-1,s}=\widehat M_{\ell,s}
                         \widehat C_{\ell,s},\qquad
 \widehat C_{\ell-1,s}=M\widehat B_{\ell-1,s},
 \quad \ell=L,\ldots,2,                                  \tag{10.5}
\]

\[
 \begin{aligned}
 \widehat A_{s+1}&=\widehat A_s+H\widehat H_{L,s},\\
 \widehat U_{s+1}&=\widehat U_s+H\widehat C_{1,s},\\
 \widehat M_{\ell,s+1}&=\widehat M_{\ell,s}
      +H\widehat C_{\ell,s}\widehat H_{\ell-1,s}.
 \end{aligned}                                             \tag{10.6}
\]

Initialize

\[
 \widehat A_0=\widehat U_0=\widehat M_{\ell,0}=\mathcal R_n,
 \qquad 2\le\ell\le L,                                  \tag{10.7a}
\]

where

\[
 \mathcal R_n=1+\|a^0\|_{n,2}+\|u^0\|_{n,2}
       +\sum_{\ell=2}^L\|W_\ell^0/\sqrt n\|_{\mathrm{op}}, \tag{10.7}
\]

and after the last update perform only the terminal forward recursion
(10.2)--(10.3) at \(s=N\).  Let \(P_{L,N,h,M}(\mathcal R_n)\) be one plus
the sum of every hatted variable in this finite list.  It is an explicitly
constructed polynomial with nonnegative coefficients.  Direct use of
Cauchy--Schwarz, \(\|\phi(x)\|_{n,2}\le M(1+\|x\|_{n,2})\), and

\[
 \left\|{h\over n}xy^T\right\|_{\mathrm{op}}
 \le H\|x\|_{n,2}\|y\|_{n,2}                             \tag{10.8}
\]

proves that it dominates every raw normalized Euclidean field and every
initialization-matrix action through terminal time.

Normalized Gaussian vector norms have every moment uniformly in \(n\).
Also \(\|G_n\|_{\mathrm{op}}/\sqrt n\), for an iid Gaussian matrix, has
every uniform moment: a \(1/4\)-net of the unit sphere with at most \(9^n\)
points and a union bound give

\[
 \mathbb P\{\|G_n\|_{\mathrm{op}}/\sqrt n>y\}
 \le2\exp\{n\log81-ny^2/8\},                             \tag{10.9}
\]

and integration of the tail proves the moment claim.  Hence

\[
 \sup_n\mathbb E\mathcal R_n^q<\infty
 \quad\text{and}\quad
 \sup_n\mathbb E P_{L,N,h,M}(\mathcal R_n)^q<\infty
 \qquad(q<\infty).                                       \tag{10.10}
\]

For \(p\ge2\),

\[
 \|x\|_{n,p}\le n^{1/2-1/p}\|x\|_{n,2};                \tag{10.11}
\]

for \(p\le2\), omit the factor.  Fix desired mixed orders \(p,P\), put
\(r=\max\{p,P,2\}\), and use (9.12) with \(m=2r\).  Holder,
(10.10)--(10.11), and \(1/2-1/p\le1/2\) give, for every raw field,

\[
 \begin{aligned}
 \left\|\|X_n\|_{n,p}\mathbf1_{\{\mathrm{stop}\}}
       \right\|_{L^P}
 &\le C n^{(1/2-1/p)_+}
       \mathbb P(\mathrm{stop})^{1/(2P)}\\
 &\le Cn^{(1/2-1/p)_+-r/P}=o(1).                         \tag{10.12}
 \end{aligned}
\]

On the complement, raw and extended fields agree.  Extended and ideal
fields have the required moments by (9.10)--(9.11), so their stopped-event
pieces also vanish.  This removes stopping from every field.  Normalized
Cauchy--Schwarz and the same polynomial majorant remove it from all Grams
and cross-moments in (8.2)--(8.3).

Finally,

\[
 |f_{n,L}^N|
 \le \|a^N\|_{n,2}\|H_L^N\|_{n,2}
 \le P_{L,N,h,M}(\mathcal R_n)^2.                         \tag{10.13}
\]

Equation (10.10) bounds the right side in every finite moment, so the
terminal outputs are uniformly integrable.  The coupled field convergence
and an iid law of large numbers for the ideal top-layer coordinates give

\[
 f_{n,L}^N-{1\over n}\sum_{i=1}^n\bar a_i^N\bar H_{L,i}^N
 \longrightarrow0\quad\text{in }L^1.                    \tag{10.14}
\]

The ideal summands are iid and have expectation \(F_{N,L}(h)\).  Taking
expectations proves (1.3).  Every empirical Gram and raw cross-moment is
bounded by a product of two Euclidean field norms, hence is uniformly
integrable as well.

## 11. What has been closed

For every fixed finite \((L,N)\) and every fixed \(h\ne0\), Sections
2--10 prove all of the following for the actual fully trained network:

1. the exact \((2N+1)(L-1)\) predictable action chronology;
2. the adaptive reused-row/reused-column Gaussian conditional law across
   all independently initialized matrices;
3. every response cancellation, including current features that depend on
   earlier transpose actions of the same reused matrix;
4. strict full history rank for every nonconstant activation, with the
   affine top-cotangent branch treated separately;
5. convergence and uniform integrability of every empirical conditioning
   quantity and terminal output, with the explicit finite moment tower
   (9.10)--(9.13);
6. pointwise fixed-\(h\) identification with the inverse-free Gaussian DAG.

The proof uses no finite-width Taylor expansion, no interchange of the
width and step-size limits, and no unproved state-evolution induction.
