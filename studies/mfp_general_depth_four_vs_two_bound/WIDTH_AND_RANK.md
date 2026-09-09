# Fixed-step width limit and time-four ranks

This note proves the width-first bridge for the actual network in
`RESEARCH_CONTRACT.md`.  No learning-rate derivative occurs in this note.

## 1. Exact finite-width chronology

Write the top and descending cotangents as

\[
 C_L^s=a^s\odot\phi'(Z_L^s),\qquad
 B_{\ell-1}^s=\frac{(W_\ell^s)^TC_\ell^s}{\sqrt n},\qquad
 C_{\ell-1}^s=B_{\ell-1}^s\odot\phi'(Z_{\ell-1}^s).
 \tag{1.1}
\]

Keeping only the initialization matrices in the raw actions, put

\[
 X_\ell^s=\frac{W_\ell^0H_{\ell-1}^s}{\sqrt n},\qquad
 R_{\ell-1}^s=\frac{(W_\ell^0)^TC_\ell^s}{\sqrt n}.
 \tag{1.2}
\]

For

\[
 Q_{\ell,rs}^{(n)}=\frac1n(H_\ell^r)^TH_\ell^s,
 \qquad
 K_{\ell,rs}^{(n)}=\frac1n(C_\ell^r)^TC_\ell^s,
 \tag{1.3}
\]

the exact accumulated updates are

\[
 Z_\ell^s=X_\ell^s+h\sum_{r<s}Q_{\ell-1,rs}^{(n)}C_\ell^r,
 \tag{1.4}
\]

\[
 B_{\ell-1}^s=R_{\ell-1}^s
       +h\sum_{r<s}K_{\ell,rs}^{(n)}H_{\ell-1}^r,
 \tag{1.5}
\]

\[
 a^s=a^0+h\sum_{r<s}H_L^r,
 \qquad Z_1^s=Z_1^0+h\sum_{r<s}C_1^r.
 \tag{1.6}
\]

There is no current-time Gram in (1.4)--(1.6).

For four recomputed steps, the initialization matrices are exposed through

\[
 \begin{split}
 &X_2^0,\ldots,X_L^0;\ R_{L-1}^0,\ldots,R_1^0;\\
 &X_2^1,\ldots,X_L^1;\ R_{L-1}^1,\ldots,R_1^1;\\
 &X_2^2,\ldots,X_L^2;\ R_{L-1}^2,\ldots,R_1^2;\\
 &X_2^3,\ldots,X_L^3;\ R_{L-1}^3,\ldots,R_1^3;\\
 &X_2^4,\ldots,X_L^4.
 \end{split}                                               \tag{1.7}
\]

This is exactly \(9(L-1)\) predictable actions.  A forward query may
depend on every earlier transpose action of the same matrix, and a
transpose query may depend on the current forward action.  Nothing in the
conditioning argument below removes that dependence.

For one connector, a forward action at time \(s\) uses the old feature and
cotangent blocks \(Q^{[s-1]},K^{[s-1]}\).  A transpose action at time
\(s\) uses \(Q^{[s]},K^{[s-1]}\).  Consequently the largest blocks ever
inverted in (1.7) are

\[
 Q_{\ell-1}^{[3]},\qquad K_\ell^{[3]},
 \qquad 2\le\ell\le L.                                  \tag{1.8}
\]

No time-four Gram is inverted.

## 2. Inverse-free population DAG

For every connector \(2\le\ell\le L\), introduce centered Gaussian
blocks

\[
 \xi_\ell=(\xi_{\ell,0},\ldots,\xi_{\ell,4}),\qquad
 \chi_\ell=(\chi_{\ell,0},\ldots,\chi_{\ell,3}),
 \tag{2.1}
\]

and independent \(U,A\sim N(0,1)\).  Their covariances are constructed
chronologically from

\[
 \mathbb E\xi_{\ell,r}\xi_{\ell,s}
   =Q_{\ell-1,rs}:=\mathbb E[H_{\ell-1}^rH_{\ell-1}^s],
 \tag{2.2}
\]

\[
 \mathbb E\chi_{\ell,r}\chi_{\ell,s}
   =K_{\ell,rs}:=\mathbb E[C_\ell^rC_\ell^s].            \tag{2.3}
\]

Different connectors and directions use independent primitive Gaussian
innovations.  Singular covariance blocks are allowed; a centered Gaussian
law is defined by any square root of its positive-semidefinite covariance.

Set \(Z_1^0=U\), \(H_1^s=\phi(Z_1^s)\).  For \(s=0,\ldots,4\), perform
the ascending sweep

\[
 \rho_{\ell,sr}=\mathbb E[\partial_{\chi_{\ell,r}}H_{\ell-1}^s],
 \qquad 0\le r<s,                                       \tag{2.4}
\]

\[
 Z_\ell^s=\xi_{\ell,s}
   +\sum_{r<s}(\rho_{\ell,sr}+hQ_{\ell-1,rs})C_\ell^r,
 \qquad H_\ell^s=\phi(Z_\ell^s).                       \tag{2.5}
\]

For \(s=0,\ldots,3\), put

\[
 a^s=A+h\sum_{r<s}H_L^r,
 \qquad C_L^s=a^s\phi'(Z_L^s),                          \tag{2.6}
\]

and descend via

\[
 \sigma_{\ell,sr}=\mathbb E[\partial_{\xi_{\ell,r}}C_\ell^s],
 \qquad0\le r\le s,                                    \tag{2.7}
\]

\[
 B_{\ell-1}^s=\chi_{\ell,s}
 +\sum_{r\le s}\sigma_{\ell,sr}H_{\ell-1}^r
 +h\sum_{r<s}K_{\ell,rs}H_{\ell-1}^r,
 \tag{2.8}
\]

\[
 C_{\ell-1}^s=B_{\ell-1}^s\phi'(Z_{\ell-1}^s),
 \qquad Z_1^{s+1}=Z_1^s+hC_1^s.                         \tag{2.9}
\]

At terminal time four,

\[
 a^4=A+h\sum_{r<4}H_L^r,
 \qquad F_{4,L}(h)=\mathbb E[a^4H_L^4].                 \tag{2.10}
\]

Stopping the same DAG at times two and one defines \(F_{2,L}\) and
\(F_{1,L}\).  Equations (2.2)--(2.10) are acyclic: one constructs a
forward covariance upward, a cotangent covariance downward, and repeats.
They contain no covariance inverse and remain meaningful at \(h=0\).

At initialization,

\[
 Q_{\ell,00}=1,
 \qquad K_{\ell,00}=d^{L-\ell+1},
 \qquad d=\mathbb E\phi'(G)^2.                           \tag{2.11}
\]

## 3. Positive time-history Grams

We use the following conditional-variance fact.  If
\(Y_0,\ldots,Y_s\in L^2\), their old Gram is positive definite,
\(Y_0,\ldots,Y_s\) are measurable with respect to \({\cal G}\), and

\[
 \mathbb E\operatorname{Var}(Y_{s+1}\mid{\cal G})>0,
 \tag{3.1}
\]

then the enlarged Gram is positive definite.  Indeed, for arbitrary
coefficients \(c_r\),

\[
 \mathbb E\left(Y_{s+1}-\sum_{r\le s}c_rY_r\right)^2
 \ge\mathbb E\operatorname{Var}(Y_{s+1}\mid{\cal G})>0.
 \tag{3.2}
\]

The explicit compiler in `COMPILER_AND_CONSTANTS.md` constructs a number
\({\cal S}_{T,L}\ge1\), from activation data only, satisfying

\[
 \sup_{|h|\le1}\max_{0\le s\le T}\mathbb E(H_L^s)^2
 \le{\cal S}_{T,L}.                                     \tag{3.3}
\]

**Lemma 3.1 (finite-horizon rank).**  Let \(T\ge1\), \(L\ge2\), and
suppose \(\phi\) is nonconstant.  If

\[
 0<|h|\le r_{T,L}:=\frac1{2T\sqrt{{\cal S}_{T,L}}},       \tag{3.4}
\]

then, in the horizon-\(T\) extension of (2.2)--(2.9),

\[
 Q_\ell^{[s]}\succ0\quad(0\le s\le T),
 \qquad
 K_\ell^{[s]}\succ0\quad(0\le s<T),
 \qquad1\le\ell\le L.                                 \tag{3.5}
\]

*Proof.*  The base \(s=0\) is (2.11), since nonconstancy and continuity
give \(d>0\).  We induct chronologically in time, upward for \(Q\) and
downward for \(K\).

First consider the bottom feature at time \(s+1\).  By the induction
hypothesis, the newest conditional innovation of \(\chi_{2,s}\) has
variance \(k_{2,s}>0\).  Condition on all primitive variables except its
fresh standard normal \(E\).  Equations (2.8)--(2.9) give

\[
 Z_1^{s+1}=R+h\phi'(Z_1^s)\sqrt{k_{2,s}}E.               \tag{3.6}
\]

On \(\{\phi'(Z_1^s)\ne0\}\), this is a full-support conditional Gaussian.
A continuous nonconstant \(\phi\) cannot be constant under such a law, so
the conditional variance of \(H_1^{s+1}\) is positive there.  The event
has positive probability: it does at \(s=0\) because \(Z_1^0\) is
standard Gaussian and \(d>0\); (3.6) then shows inductively that every
nonempty open subset of \(\mathbb R\), in particular
\(\{x:\phi'(x)\ne0\}\), is hit with positive probability.  Equation
(3.2) proves \(Q_1^{[s+1]}\succ0\).

Proceed upward.  Once \(Q_{\ell-1}^{[s+1]}\succ0\), write

\[
 \xi_{\ell,s+1}=R+\sqrt{q_{\ell,s+1}}E,
 \qquad q_{\ell,s+1}>0,                                 \tag{3.7}
\]

relative to its old source block.  All learned and response terms in
\(Z_\ell^{s+1}\) use cotangents of times at most \(s\), hence are
measurable without this fresh \(E\).  Thus
\(Z_\ell^{s+1}=R'+\sqrt{q_{\ell,s+1}}E\).  Conditional variance and
(3.2) prove \(Q_\ell^{[s+1]}\succ0\).  The same full-support statement
also gives

\[
 \mathbb P\{\phi'(Z_\ell^{s+1})\ne0\}>0.                \tag{3.8}
\]

Suppose first that \(\phi\) is non-affine.  Then \(\phi'\) is continuous
and nonconstant.  At the top,

\[
 C_L^{s+1}=a^{s+1}\phi'(R+\sqrt q\,E),\qquad q>0,       \tag{3.9}
\]

where the fresh forward innovation \(E\) is absent from every previous
top cotangent.  For every \(R\) and \(q>0\),
\(\operatorname{Var}[\phi'(R+\sqrt qE)]>0\); otherwise continuity and
Gaussian full support would make \(\phi'\) constant globally.  Moreover,
by (3.3)--(3.4), for \(s+1<T\),

\[
 \|a^{s+1}-A\|_2
 \le |h|\sum_{r\le s}\|H_L^r\|_2
 \le |h|T\sqrt{{\cal S}_{T,L}}
 \le\frac12.                                             \tag{3.10}
\]

Hence \(\|a^{s+1}\|_2\ge1/2\), so it is nonzero with positive
probability.  Conditioning additionally on \(a^{s+1}\) and applying
(3.2) proves \(K_L^{[s+1]}\succ0\).

Descend from layer \(\ell+1\) to \(\ell\).  The positive new Schur
complement of \(K_{\ell+1}^{[s+1]}\) gives

\[
 B_\ell^{s+1}=R+\sqrt{k_{\ell+1,s+1}}E.                 \tag{3.11}
\]

The current \(Z_\ell^{s+1}\) uses only older cotangents and is independent
of this fresh transpose innovation.  Therefore

\[
 \operatorname{Var}(C_\ell^{s+1}\mid\text{all but }E)
 =k_{\ell+1,s+1}\phi'(Z_\ell^{s+1})^2,                  \tag{3.12}
\]

which is positive on the positive-probability event (3.8).  Equation
(3.2) proves the next \(K\)-rank and closes the downward induction.

If \(\phi(x)=\alpha x+\beta\), \(\alpha\ne0\), the feature arguments
above remain valid.  For the top cotangent,

\[
 C_L^{s+1}=\alpha a^{s+1}
 =\alpha a^s+h\alpha H_L^s.                              \tag{3.13}
\]

The fresh innovation in \(\xi_{L,s}\) enters \(H_L^s\) with coefficient
\(\alpha\sqrt{q_{L,s}}\), and it is absent from
\(C_L^0,\ldots,C_L^s\).  Thus the new conditional variance is
\(h^2\alpha^4q_{L,s}>0\).  In (3.12), \(\phi'=\alpha\), so every
downward conditional variance is also positive.  This completes the
affine branch and the induction. \(\square\)

For time four, (3.5) proves exactly (1.8).  The proof also establishes the
stronger arbitrary-fixed-horizon rank statement; it makes no claim of a
horizon-uniform lower eigenvalue.

If \(d=0\), then \(\phi\equiv\pm1\).  All hidden gradients vanish and
\(F_{k,L}(h)=kh\), so the four-versus-two discrepancy is identically zero.
For \(L=1\), there is no matrix Gram: the coordinate recursion is iid and
exact for every \(n\).

## 4. Adaptive conditioning and response cancellation

The sole matrix-probability input is the following finite-action lemma.
Let \(M_2,\ldots,M_L\) be independent standard Gaussian matrices,
independent of an external sigma-field.  Consider a finite interlaced
sequence of row and transpose actions whose matrix label and query are
measurable with respect to the global previously revealed filtration.  For
one matrix, collect its old row queries, column queries, and actions as

\[
 H,\quad C,\quad Y=MH/\sqrt n,\quad D=M^TC/\sqrt n.
\]

Conditionally on the global predictable filtration,

\[
 M=P_CM+MP_H-P_CMP_H+P_C^\perp\widetilde MP_H^\perp,    \tag{4.1}
\]

where the residual matrices \(\widetilde M_\ell\) are conditionally
independent standard Gaussian matrices and are independent of the revealed
filtration.

To prove this, suppose (4.1) holds before a new row action of \(M_j\), and
write its predictable query as \(q=P_Hq+q_\perp\).  Every part of
\(M_jq\) except

\[
 P_C^\perp\widetilde M_jq_\perp                         \tag{4.1a}
\]

is already revealed.  If \(q_\perp\ne0\), put
\(e=q_\perp/\|q_\perp\|\).  The orthogonal Gaussian projections
\(\widetilde M_jee^T\) and \(\widetilde M_j(I-ee^T)\) are independent.
Revealing (4.1a) therefore leaves

\[
 P_C^\perp\widetilde M_j
 P_{\operatorname{span}(H,q)}^\perp
\]

fresh.  It remains independent of every untouched connector residual,
because the new observation is a function only of the \(j\)-th residual
conditional on the old global filtration.  If \(q_\perp=0\), no residual
component is exposed.  A transpose action is the identical argument with
rows and columns exchanged.  Induction over the finite action list proves
(4.1) for arbitrarily interlaced, cross-dependent queries.

Put

\[
 Q=H^TH/n,\qquad K=C^TC/n,\qquad {\cal R}=C^TY/n=D^TH/n.
\]

When the old nonempty blocks are invertible, a new transpose query \(c\)
satisfies

\[
 \frac{M^Tc}{\sqrt n}
 =DK^{-1}k+HQ^{-1}(r-{\cal R}^TK^{-1}k)
   +\tau_cP_H^\perp g,                                   \tag{4.2}
\]

\[
 k=C^Tc/n,\qquad r=Y^Tc/n,\qquad
 \tau_c^2=c^Tc/n-k^TK^{-1}k.                            \tag{4.3}
\]

The row formula for a new query \(x_*\) is

\[
 \frac{Mx_*}{\sqrt n}
 =YQ^{-1}q+CK^{-1}(v-{\cal R}Q^{-1}q)
   +\tau_xP_C^\perp g,                                   \tag{4.4}
\]

with

\[
 q=H^Tx_*/n,\qquad v=D^Tx_*/n,
 \qquad \tau_x^2=x_*^Tx_*/n-q^TQ^{-1}q.                 \tag{4.4a}
\]

Empty blocks and their terms are omitted.  Equations (4.1)--(4.4a) follow
by decomposing the new query orthogonally against the old query span; they
are exact conditional Gaussian identities, not asymptotic formulas.

At population level, old actions have the form

\[
 y=\xi+Pc,\qquad d=\chi+Sx.                              \tag{4.5}
\]

Every field in (4.5) is continuously differentiable in its Gaussian
coordinates and has a polynomial Gaussian envelope.  Gaussian integration
by parts is therefore justified; at a singular covariance it follows by
adding \(\epsilon I\) and using the same domination as in the singular
Price lemma.  It gives

\[
 {\cal R}=\mathbb E[cy^T]=SQ+KP^T.                       \tag{4.6}
\]

For a new row query, define

\[
 q=\mathbb E[xH_{\rm new}],\qquad
 \rho=\mathbb E[\nabla_\chi H_{\rm new}].
\]

Then \(v=K\rho+Sq\), and hence

\[
 K^{-1}(v-{\cal R}Q^{-1}q)=\rho-P^TQ^{-1}q.             \tag{4.7}
\]

The last term cancels the old-action projection in (4.4), leaving

\[
 y_{\rm new}=\xi_{\rm new}+\rho^Tc.                     \tag{4.8}
\]

For a new transpose query, define

\[
 k=\mathbb E[cC_{\rm new}],\qquad
 \sigma=\mathbb E[\nabla_\xi C_{\rm new}].
\]

Then \(r=Q\sigma+Pk\), and

\[
 Q^{-1}(r-{\cal R}^TK^{-1}k)=\sigma-S^TK^{-1}k.         \tag{4.9}
\]

The matching projection cancels in (4.2), leaving

\[
 d_{\rm new}=\chi_{\rm new}+\sigma^Tx.                  \tag{4.10}
\]

Adding the exact learned pieces (1.4)--(1.5) produces precisely
(2.5) and (2.8).  These identities are independent of history length, so
they cover all \(9(L-1)\) actions and every reused-column dependence.

The complete empirical data at a forward action are the old \(Q,K,{\cal R}\)
blocks together with

\[
 (H^{0:s-1})^TH^s/n,\qquad (R^{0:s-1})^TH^s/n.         \tag{4.11}
\]

At a transpose action they are the old blocks together with

\[
 (C^{0:s-1})^TC^s/n,\qquad (X^{0:s})^TC^s/n.           \tag{4.12}
\]

Thus (4.11)--(4.12) list every regression input; no mixed connector Gram
is inverted.

## 5. Concentration and expected-output convergence

Fix a nonzero \(h\) in the interval (3.4).  By Lemma 3.1, every population
Gram inverted in (1.7), and every query Schur complement producing one of
its nine innovations per connector, is strictly positive.  This is a
finite set.  Let \(4\gamma_{L,h}>0\) be its minimum.

For \(x\in\mathbb R^n\), write

\[
 \|x\|_{n,p}=\left(n^{-1}\sum_i|x_i|^p\right)^{1/p}.
\]

For iid centered \(Y_i\) and \(P\ge2\), Rosenthal's inequality gives

\[
 \left\|\frac1n\sum_iY_i\right\|_{L^P}
 \le C_P\left(n^{-1/2}\|Y_1\|_2
       +n^{-1+1/P}\|Y_1\|_P\right).                    \tag{5.1}
\]

If \(V\) has a fixed number of columns and
\(\lambda_{\min}(V^TV/n)\ge\gamma_{L,h}\), then, conditionally on \(V\),

\[
 \left\|\|P_Vg\|_{n,p}\right\|_{L^P(g\mid V)}
 \le C_{p,P,L,h}n^{-1/2}\sum_j\|V_j\|_{n,p}.             \tag{5.2}
\]

Indeed, in
\(P_Vg=V(V^TV/n)^{-1}V^Tg/n\), the coefficient vector is centered
Gaussian with covariance \((V^TV/n)^{-1}/n\).

### 5.1 One compatible ideal array and good events

For each physical layer, take iid coordinate copies of the scalar marks in
the population DAG: \((U,\chi_2)\) at layer one,
\((\xi_\ell,\chi_{\ell+1})\) at an interior layer, and
\((\xi_L,A)\) at the top.  Different physical-layer arrays are independent.
Extend every time block chronologically by Gaussian regression from its
population Gram.  At a finite-width action, use the same fresh Gaussian
vector for the residual in (4.1) and for the matching ideal innovation.
The multi-matrix induction above makes this coupling simultaneous across
all connectors.

Immediately before action \(t\), let \({\cal G}_t\) be the intersection of
the previous good event with both requirements:

1. every empirical old Gram inverted at action \(t\) has smallest
   eigenvalue at least \(2\gamma_{L,h}\);
2. every empirical new-query Schur complement already formed and used at
   this action or a later one is at least \(2\gamma_{L,h}\).

The relevant Schur complement is measurable before its associated fresh
matrix action, since it depends only on the predictable query and old
queries.  Stop only the conditional representation at the first failure;
the raw network is never stopped.  Extend a stopped inverse coefficient or
innovation scale off \({\cal G}_t\) by its deterministic population value.

### 5.2 The finite-action induction

Fix finite \(p,P\).  After each action in (1.7), prove simultaneously:

1. every stopped field constructed so far converges to its coupled ideal
   field in \(L^P(\|\cdot\|_{n,p})\);
2. stopped and ideal fields have every larger finite moment needed by the
   remaining finite computation, uniformly in \(n\);
3. every empirical Gram, rectangular cross block, and query overlap in
   (4.11)--(4.12) formed so far converges in \(L^P\) to its population
   value;
4. all these errors are \(O_{L,h,p,P}(n^{-1/2})\).

For the base action, the coordinates
\(H_{1,j}^0=\phi(U_j)\) are iid, and (5.1) gives

\[
 Q_{1,00}^{(n)}\longrightarrow\mathbb E\phi(U)^2=1
 \quad\hbox{in every }L^P.                              \tag{5.3}
\]

Conditionally on \(H_1^0\),
\(X_2^0=W_2^0H_1^0/\sqrt n\) has iid coordinates
\(N(0,Q_{1,00}^{(n)})\).  Couple them to \(\xi_{2,0}\) with the same
standard normals.  On \(Q_{1,00}^{(n)}\ge1/2\),

\[
 |\sqrt{Q_{1,00}^{(n)}}-1|
 \le |Q_{1,00}^{(n)}-1|.                                \tag{5.4}
\]

The complement has probability \(O(n^{-m})\) for arbitrary \(m\), by
(5.1) at sufficiently high moment order.  This proves the four assertions
for the base.

Assume them before a later action.  A new query or nonlinear field is a
finite composition of sums, products, \(\phi\), and \(\phi'\).  The
activation envelope and the mean-value theorem give, for a finite integer
\(r=r(L)\),

\[
 |\Psi(x;\theta)-\Psi(x';\theta')|
 \le C_{L,h,M_\phi}(1+\|x\|^r+\|x'\|^r)
 (\|x-x'\|+\|\theta-\theta'\|).                         \tag{5.5}
\]

Hölder at moment orders \(2P\) and \(2Pr\) propagates assertions 1 and 2
through this map.

Every conditional coefficient in (4.2)--(4.4a) is a rational function of
the finite ledger (4.11)--(4.12).  On \({\cal G}_t\),

\[
 \|A^{-1}-B^{-1}\|
 \le\|A^{-1}\|\,\|A-B\|\,\|B^{-1}\|,                  \tag{5.6}
\]

and the inverse norms are at most \((2\gamma_{L,h})^{-1}\).  Both the
empirical and population innovation variances are at least
\(2\gamma_{L,h}\), so the square-root map is Lipschitz there.  Thus the
regression coefficients and innovation scales differ by
\(O(n^{-1/2})\).  Couple the fresh residual and use (5.2); this proves
assertions 1 and 4 for the new raw action.

For each ideal coordinate observable \(\Theta\) in the new ledger, the
coordinates in its physical layer are iid and have every finite moment.
Thus

\[
 \left\|n^{-1}\sum_i\Theta_i-\mathbb E\Theta_1\right\|_{L^P}
 \le C_{L,h,P}n^{-1/2}.                                  \tag{5.7}
\]

The actual-minus-ideal part is bounded by (5.5), Hölder, and assertion 1.
This proves assertion 3, including the rectangular block
\({\cal R}=C^TY/n=D^TH/n\).  The same envelope proves assertion 2.  Hence
the implication from one action to the next is complete.  Applying it to
the explicit \(9(L-1)\)-action list proves all four assertions after the
terminal forward sweep.  There is no degenerate terminal square root:
Lemma 3.1 includes \(Q_\ell^{[4]}\succ0\).

The population limits of the overlaps in (4.11)--(4.12) obey (4.6)--(4.9)
by the singular-valid integration by parts already proved.  Thus every
limiting regression coefficient is exactly the displayed response
coefficient; no finite-width derivative has entered.

### 5.3 Removing the stopping and uniform integrability

Run the preceding induction at arbitrary finite moment order.  Entrywise
Gram and Schur-complement convergence, Weyl's inequality, and Markov's
inequality give, for every prescribed \(m\),

\[
 \mathbb P({\cal G}_t^c\cap{\cal G}_{t-1})
 \le C_{L,h,m}n^{-m}.                                   \tag{5.8}
\]

The stopped coefficient extensions converge in every finite \(L^P\), and
the union over the finite action list still has probability \(O(n^{-m})\).

It remains to control the raw network on this exceptional event.  Starting
with the normalized Euclidean norms of \(u^0,a^0,W_2^0/\sqrt n,\ldots,
W_L^0/\sqrt n\), define chronologically

\[
 \|H_\ell^s\|_{n,2}\le M_\phi(1+\|Z_\ell^s\|_{n,2}),
 \qquad \|C_L^s\|_{n,2}\le M_\phi\|a^s\|_{n,2},        \tag{5.9}
\]

use the forward/backward operator-norm inequalities, and use

\[
 \|W_\ell^{s+1}/\sqrt n\|_{\rm op}
 \le\|W_\ell^s/\sqrt n\|_{\rm op}
 +|h|\|C_\ell^s\|_{n,2}\|H_{\ell-1}^s\|_{n,2}.         \tag{5.10}
\]

For \(s=0,1,2,3\), perform the forward and backward substitutions and the
four parameter updates; at terminal time four perform only the forward
substitution.  This is a finite recursion, so every raw norm is bounded by
a polynomial with nonnegative coefficients in

\[
 1+M_\phi+\|u^0\|_{n,2}+\|a^0\|_{n,2}
 +\sum_{\ell=2}^L\|W_\ell^0/\sqrt n\|_{\rm op}.          \tag{5.11}
\]

Gaussian vector moments and the standard Gaussian matrix operator-norm
tail give uniform moments of every order for (5.11).  For \(p\ge2\),

\[
 \|x\|_{n,p}\le n^{1/2-1/p}\|x\|_{n,2},                \tag{5.12}
\]

while for \(p<2\), \(\|x\|_{n,p}\le\|x\|_{n,2}\).  Choose \(m\) in
(5.8) larger than the finite power of \(n\) in (5.12) and apply Hölder.
Every exceptional-event contribution to a field, ledger entry, and output
then vanishes.

Finally,

\[
 |f_{n,L}^s|\le\|a^s\|_{n,2}\|H_L^s\|_{n,2},            \tag{5.13}
\]

and the right side has a uniform \(L^{1+\delta}\) bound.  Hence the
terminal outputs are uniformly integrable.  We have proved separately at
each fixed nonzero admissible step that

\[
 \lim_{n\to\infty}\mathbb E f_{n,L}^4=F_{4,L}(h),
 \qquad
 \lim_{n\to\infty}\mathbb E f_{n,L}^2=F_{2,L}(h).       \tag{5.14}
\]

At \(h=0\), both identities hold directly.  The width limit is therefore
complete before any learning-rate differentiation.
