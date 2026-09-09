# Seven-action fixed-step width identification

## Result and scope

This note closes the finite-width extension from the five actions used for
the two-step output to the seven actions needed for the three-step output.
It uses the exact network, normalization, and adaptive Gaussian-conditioning
lemma proved in the preceding two-step proof.  Nothing below differentiates
a finite-width network or lets the step size depend on the width.

Fix a nonzero step size (h).  Let the population three-time feature and
cotangent Grams produced by the Gaussian recursion below be

$$
Q^{[2]}=(Q_{rs})_{0\le r,s\le2},
\qquad
K^{[2]}=(K_{rs})_{0\le r,s\le2}.
$$

Assume

$$
Q^{[2]}>0,\qquad K^{[2]}>0. \tag{0.1}
$$

Then, as (n\to\infty) at this fixed (h), every field in the actual
seven-action network converges in normalized (L^p), for every finite
(p), to the corresponding field of the Gaussian recursion, every raw
empirical Gram and cross-moment used by adaptive conditioning converges in
every finite (L^p), and

$$
\lim_{n\to\infty}\mathbb E f_n^3=F_3(h).
\tag{0.2}
$$

The terminal feature innovation at time (3) may have zero variance.  No
invertibility of (Q^{[3]}) is used.  Thus (0.1) is exactly the additional
rank condition needed beyond the five-action proof.  A quantitative
small-(h) theorem must establish (0.1) on its claimed punctured interval
by a separate activation-defined rank lemma.

This is the nonconstant case.  If

$$
d=\mathbb E[\phi'(G)^2]=0,
$$

continuity and full support of the Gaussian law give
\(\phi'\equiv0\).  The normalization \(\mathbb E[\phi(G)^2]=1\) then
gives \(\phi\equiv1\) or \(\phi\equiv-1\).  All \(C^s\) vanish, only the
readout update acts, and direct substitution into the finite-width network
gives \(F_{k,n}(h)=kh\) for every \(n\).  In particular
\(F_3(h)-F_1(3h)=0\) identically.  No inverse Gram is needed in that case.

## 1. Exact chronology

With (W=W^0), define the raw source-matrix actions

$$
Y^s=WH^s/\sqrt n,
\qquad
D^s=W^TC^s/\sqrt n.
$$

The simultaneous ascent update gives, exactly,

$$
W^s=W+\frac h{\sqrt n}\sum_{r<s}C^r(H^r)^T,
$$

and hence

$$
z^s=Y^s+h\sum_{r<s}Q_{rs}^{(n)}C^r,
\qquad
b^s=D^s+h\sum_{r<s}K_{rs}^{(n)}H^r. \tag{1.1}
$$

In particular,

$$
b^2=D^2+hK_{02}^{(n)}H^0+hK_{12}^{(n)}H^1,
\tag{1.2}
$$

$$
z^3=Y^3+hQ_{03}^{(n)}C^0+hQ_{13}^{(n)}C^1
             +hQ_{23}^{(n)}C^2. \tag{1.3}
$$

There is no (K_{22}^{(n)}H^2) in (1.2), and no
(Q_{33}^{(n)}C^3) in (1.3), because the current update has not yet been
made when the current gradient is evaluated.

The source matrix is revealed in the order

$$
Y^0, D^0, Y^1, D^1, Y^2, D^2, Y^3. \tag{1.4}
$$

This order is predictable.  Initially (H^0) is external to (W).
After (Y^s), equations (1.1) and the scalar top update determine
(z^s,a^s,C^s), so (C^s) is measurable before (D^s).  After (D^s),
(1.1) and the scalar lower update determine (b^s,u^{s+1},H^{s+1}), so
(H^{s+1}) is measurable before (Y^{s+1}).  In particular, the
dependence of (H^1) on the reused column action (D^0) is in the revealed
filtration; it is not replaced by an independent copy.  The adaptive
row/column conditioning theorem therefore applies at all seven actions.

## 2. Population recursion

Use one jointly Gaussian feature source block
((\xi_0,\xi_1,\xi_2,\xi_3)), whose covariance is the feature Gram, and
one jointly Gaussian cotangent source block
((\chi_0,\chi_1,\chi_2)), whose covariance is the cotangent Gram.  The
two source blocks, (A), and (U) are mutually independent.  The blocks
are generated chronologically; this sentence does not assert that their
time coordinates are independent.

Set (u_0=U), (H_s=\phi(u_s)), and, for (s=0,1,2), define

$$
\sigma_{sr}=\mathbb E[\partial_{\xi_r}C_s],\qquad 0\le r\le s,
$$

$$
b_s=\chi_s+\sum_{r\le s}\sigma_{sr}H_r
       +h\sum_{r<s}K_{rs}H_r, \tag{2.1}
$$

$$
u_{s+1}=u_s+h b_s\phi'(u_s),
\qquad H_{s+1}=\phi(u_{s+1}). \tag{2.2}
$$

For (s=0,1,2,3), define

$$
\rho_{sr}=\mathbb E[\partial_{\chi_r}H_s],\qquad 0\le r<s,
$$

$$
z_s=\xi_s+\sum_{r<s}(\rho_{sr}+hQ_{rs})C_r, \tag{2.3}
$$

$$
a_s=A+h\sum_{r<s}\phi(z_r),
\qquad C_s=a_s\phi'(z_s). \tag{2.4}
$$

Here (Q_{rs}=\mathbb E[H_rH_s]) and
(K_{rs}=\mathbb E[C_rC_s]).  Centering of (A) gives
(\sigma_{00}=0).  The limiting terminal output is

$$
F_3(h)=\mathbb E[a_3\phi(z_3)]. \tag{2.5}
$$

The response derivatives at the two new stages are genuine derivatives of
the finite-dimensional population integrands.  For example, with
(\partial_r=\partial_{\xi_r}),

$$
\partial_r a_2
=h\sum_{t<2}\phi'(z_t)\partial_r z_t,
$$

$$
\partial_r z_2
=\mathbf 1_{\{r=2\}}+\sum_{t<2}(\rho_{2t}+hQ_{t2})\partial_r C_t,
$$

$$
\partial_r C_2
=(\partial_r a_2)\phi'(z_2)
 +a_2\phi''(z_2)\partial_r z_2. \tag{2.6}
$$

Thus (\sigma_{2r}=\mathbb E[\partial_rC_2]).  Likewise, with
(\partial_r=\partial_{\chi_r}),

$$
\partial_r b_2
=\mathbf1_{\{r=2\}}
 +\sum_{t\le2}\sigma_{2t}\partial_rH_t
 +h\sum_{t<2}K_{t2}\partial_rH_t,
$$

$$
\partial_r u_3
=\partial_r u_2
+h\bigl[(\partial_r b_2)\phi'(u_2)
       +b_2\phi''(u_2)\partial_r u_2\bigr],
$$

$$
\partial_rH_3=\phi'(u_3)\partial_r u_3. \tag{2.7}
$$

Thus (\rho_{3r}=\mathbb E[\partial_rH_3]).  Under the stated activation
envelope, all fields and all derivatives in (2.6)--(2.7) have polynomial
growth in finitely many Gaussian marks.  They are integrable, so every
Gaussian integration by parts below is justified.

## 3. Complete action ledger

At an action, (q,k,r,v,R) have the meanings in the adaptive
row/column-conditioning formulas.  The following table lists every new raw
empirical observable.  Previously constructed entries are not relisted.

| action | predictable query | new Grams and cross-moments | rank status |
|---|---|---|---|
| (Y^0) | (H^0) | (Q_{00}^{(n)}) | (Q_{00}=1) |
| (D^0) | (C^0) | (K_{00}^{(n)},(Y^0)^TC^0/n) | (K_{00}=d>0) |
| (Y^1) | (H^1) | (Q_{01}^{(n)},Q_{11}^{(n)},(D^0)^TH^1/n) | new (Q)-Schur (>0) |
| (D^1) | (C^1) | (K_{01}^{(n)},K_{11}^{(n)},(Y^{0:1})^TC^1/n) | new (K)-Schur (>0) |
| (Y^2) | (H^2) | (Q_{02}^{(n)},Q_{12}^{(n)},Q_{22}^{(n)},(D^{0:1})^TH^2/n) | new (Q)-Schur (>0) |
| (D^2) | (C^2) | (K_{02}^{(n)},K_{12}^{(n)},K_{22}^{(n)},(Y^{0:2})^TC^2/n) | new (K)-Schur (>0) |
| (Y^3) | (H^3) | (Q_{03}^{(n)},Q_{13}^{(n)},Q_{23}^{(n)},Q_{33}^{(n)},(D^{0:2})^TH^3/n) | terminal Schur may vanish |

At each line the conditioning formula also uses the old cross block

$$
R^{(n)}=(C^{\mathrm{old}})^TY^{\mathrm{old}}/n
       =(D^{\mathrm{old}})^TH^{\mathrm{old}}/n. \tag{3.1}
$$

The equality in (3.1) is exact, since both sides equal
((C^{\mathrm{old}})^TWH^{\mathrm{old}}/n^{3/2}).  Entries involving the
new query are precisely the cross-moments displayed in the table.  Thus the
table omits no input to either regression formula.

The nonterminal innovation variances, in chronological order, are

$$
K_{00},\quad
Q_{11}-Q_{01}^2/Q_{00},\quad
K_{11}-K_{01}^2/K_{00},
$$

$$
Q_{22}-Q_{2,0:1}(Q^{[1]})^{-1}Q_{0:1,2},
$$

$$
K_{22}-K_{2,0:1}(K^{[1]})^{-1}K_{0:1,2}. \tag{3.2}
$$

They are positive exactly when the relevant leading principal extensions
are positive definite.  Hence (0.1), together with (Q_{00}=1), supplies
every inverse and every nonterminal square-root lower bound used in the
seven actions.  The new feature Schur at (Y^3) is terminal and is not in
(3.2).

## 4. Reused-column cancellation at (D^2)

This is the first new action.  At one representative coordinate, write

$$
h=(H_0,H_1,H_2)^T,\quad
c=(C_0,C_1)^T,
$$

$$
y=(Y^0,Y^1,Y^2)^T,\quad
d=(D^0,D^1)^T.
$$

The already identified five actions have the block form

$$
y=\xi+Pc,
\qquad
d=\chi+Sh, \tag{4.1}
$$

where

$$
P=
\begin{pmatrix}
0&0\\
\rho_{10}&0\\
\rho_{20}&\rho_{21}
\end{pmatrix},
\qquad
S=
\begin{pmatrix}
0&0&0\\
\sigma_{10}&\sigma_{11}&0
\end{pmatrix}. \tag{4.2}
$$

Let

$$
Q=\mathbb E[hh^T],\quad K=\mathbb E[cc^T],\quad
k=\mathbb E[cC_2],
$$

and let

$$
\sigma_2=(\sigma_{20},\sigma_{21},\sigma_{22})^T.
$$

Gaussian integration by parts in the joint (\xi)-block gives

$$
\mathbb E[c\xi^T]=SQ,
$$

because (S_{sr}=\mathbb E[\partial_{\xi_r}C_s]) for
(s=0,1).  Consequently the old cross block is

$$
R:=\mathbb E[cy^T]=SQ+KP^T. \tag{4.3}
$$

The new row-action overlap is

$$
r:=\mathbb E[yC_2]
=Q\sigma_2+Pk. \tag{4.4}
$$

The population column-conditioning formula reads

$$
D^2
=d^TK^{-1}k
+h^TQ^{-1}(r-R^TK^{-1}k)
 +\text{orthogonal Gaussian innovation}. \tag{4.5}
$$

Using (4.3)--(4.4),

$$
Q^{-1}(r-R^TK^{-1}k)
=\sigma_2-S^TK^{-1}k. \tag{4.6}
$$

On the other hand, the first term in (4.5), together with (4.1), is

$$
d^TK^{-1}k
=\chi^TK^{-1}k+h^TS^TK^{-1}k. \tag{4.7}
$$

The last term in (4.7) cancels the negative term from (4.6) exactly.
The remaining Gaussian regression

$$
\chi^TK^{-1}k
+\sqrt{K_{22}-k^TK^{-1}k}\,G_2
$$

has variance (K_{22}) and covariance (k) with (\chi); it is therefore
the next coordinate (\chi_2) of the same joint Gaussian block.  The
finite-dimensional projection of (G_2) onto the old (H)-span vanishes
in normalized (L^p), as proved in the projector estimate.  Thus

$$
D^2\longrightarrow
\chi_2+\sigma_{20}H_0+\sigma_{21}H_1+\sigma_{22}H_2. \tag{4.8}
$$

Adding the two exact learned-matrix terms in (1.2) gives exactly (2.1) for
(b_2).  Equations (4.3)--(4.7) retain all earlier (W/W^T) responses;
none was discarded as an independence approximation.

## 5. Reused-row cancellation at (Y^3)

After (D^2), use three-time blocks

$$
h=(H_0,H_1,H_2)^T,\quad c=(C_0,C_1,C_2)^T,
$$

$$
y=(Y^0,Y^1,Y^2)^T,\quad d=(D^0,D^1,D^2)^T.
$$

They obey

$$
y=\xi+Pc,\qquad d=\chi+Sh, \tag{5.1}
$$

where now

$$
P_{sr}=\mathbf1_{\{r<s\}}\rho_{sr},
\qquad
S_{sr}=\mathbf1_{\{r\le s\}}\sigma_{sr},
\qquad 0\le r,s\le2. \tag{5.2}
$$

In particular (P) is strictly lower triangular and
(S_{00}=\sigma_{00}=0).  Put

$$
Q=\mathbb E[hh^T],\quad K=\mathbb E[cc^T],
\quad q=\mathbb E[hH_3],
$$

$$
\rho_3=(\rho_{30},\rho_{31},\rho_{32})^T.
$$

As before,

$$
R:=\mathbb E[cy^T]=SQ+KP^T. \tag{5.3}
$$

Gaussian integration by parts in the (\chi)-block gives

$$
\mathbb E[\chi H_3]=K\rho_3.
$$

Therefore

$$
v:=\mathbb E[dH_3]=K\rho_3+Sq. \tag{5.4}
$$

The population row-conditioning formula is

$$
Y^3
=y^TQ^{-1}q
+c^TK^{-1}(v-RQ^{-1}q)
+\text{orthogonal Gaussian innovation}. \tag{5.5}
$$

Equations (5.3)--(5.4) give

$$
K^{-1}(v-RQ^{-1}q)
=\rho_3-P^TQ^{-1}q. \tag{5.6}
$$

The response part of the first term in (5.5) is, by (5.1),

$$
c^TP^TQ^{-1}q,
$$

which cancels the second term in (5.6).  The remaining Gaussian regression
and terminal innovation form (\xi_3), jointly Gaussian with
((\xi_0,\xi_1,\xi_2)) and with covariance (Q^{[3]}).  If its Schur
variance is zero, the innovation is simply zero.  Hence

$$
Y^3\longrightarrow
\xi_3+\rho_{30}C_0+\rho_{31}C_1+\rho_{32}C_2. \tag{5.7}
$$

Adding (1.3) yields (2.3) at (s=3).

## 6. Concentration and uniform integrability

We now verify that the two population cancellations just computed identify
the actual network, rather than merely a formal Gaussian program.

### 6.1 Coupled ideal arrays

Use iid column marks

$$
(U_j,g_{0j},g_{1j},g_{2j})\sim N(0,I_4)
$$

and iid row marks

$$
(A_i,e_{0i},e_{1i},e_{2i},e_{3i})\sim N(0,I_5),
$$

the two arrays being independent.  Generate every Gaussian time block by
the ordinary finite Gram--Schmidt regression on its earlier coordinates.
At a positive Schur variance, use the next fresh mark; at the terminal
(\xi_3) use zero if its Schur variance is zero.  Conditional on the
deterministic population moments, row coordinates are iid copies of the
row recursion and column coordinates are iid copies of the column
recursion.  Use the same fresh mark for the corresponding orthogonal
innovation in the adaptive conditioning representation of the actual
matrix.  This is one chronological coupling, not separate incompatible
couplings for the seven queries.

### 6.2 Good event and the (D^2) stage

Let (\gamma(h)>0) be smaller than half the minimum of the five positive
quantities in (3.2) and the minimum eigenvalues of all old blocks inverted
in the seven actions.  The first five coupled actions have already been
proved with arbitrarily high moment order.  Because the (Y^2) innovation
is now nonterminal and its population Schur variance is positive, its
coupling error is (O(n^{-1/2})), rather than the weaker terminal
zero-variance rate.

The query (C^2) is a polynomial-Lipschitz coordinate function of the
fields available after (Y^2).  Bounded activation derivatives and the
linear-growth bound for (\phi) imply, for every finite (P),

$$
\|C_n^2-\bar C^2\|_{L^P(\Omega;\|\cdot\|_{n,P})}
=O(n^{-1/2}), \tag{6.1}
$$

and all actual stopped and ideal fields have uniform moments of every fixed
order.  Applying Rosenthal to the iid ideal row coordinates, and using
(6.1) plus Hölder for the actual-to-ideal difference, proves (L^P)
convergence of

$$
K_{02}^{(n)},K_{12}^{(n)},K_{22}^{(n)},
\qquad (Y^{0:2})^TC^2/n, \tag{6.2}
$$

and the entries of the old block (R^{(n)}) needed at (D^2).

Intersect the old good event with the events that the empirical
(Q^{[2]}) and (K^{[1]}) have minimum eigenvalue at least
(\gamma(h)), and that the empirical new-(C^2) Schur variance is at least
(\gamma(h)).  All defining quantities are measurable before revealing
(D^2).  The inverse identity, Weyl's inequality, and the fact that a
square root is Lipschitz away from zero show that every stopped regression
coefficient and innovation scale at (D^2) converges in every finite
(L^P).  Running (6.2) at arbitrarily high moment order and applying
Markov gives, for every (M<\infty),

$$
\mathbb P(\text{first failure at }D^2)\le C_{M,h}n^{-M}. \tag{6.3}
$$

The adaptive projector estimate for a fixed three-dimensional old query
span is

$$
\left\|\|P_Hg\|_{n,P}\right\|_{L^S(g\mid H)}
\le C_{P,S,h}n^{-1/2}\sum_{r=0}^2\|H^r\|_{n,P}. \tag{6.4}
$$

Combining (6.2)--(6.4), using the same (g_2) in the actual and ideal
innovations, proves normalized (L^P) convergence of (D^2) to (4.8).
The exact learned terms then give (b^2).  The maps in (2.2) give
normalized (L^P) convergence of (u^3,H^3).

### 6.3 The (Y^3) stage

The ideal column coordinates are iid.  Rosenthal and the just-proved field
coupling therefore give convergence in every finite (L^P) of

$$
Q_{03}^{(n)},Q_{13}^{(n)},Q_{23}^{(n)},Q_{33}^{(n)},
\qquad (D^{0:2})^TH^3/n, \tag{6.5}
$$

as well as the full old block (R^{(n)}).  The empirical (Q^{[2]}) and
(K^{[2]}) are within (\gamma(h)) of their positive-definite population
limits outside an event of probability (O(n^{-M})) for every (M).
Thus every conditional-mean coefficient at (Y^3) converges in every
finite (L^P).

No lower bound is imposed on the new-(H^3) Schur variance.  Its empirical
version converges to the nonnegative population value.  For its innovation
standard deviation use

$$
|\sqrt{x}-\sqrt y|\le\sqrt{|x-y|},\qquad x,y\ge0. \tag{6.6}
$$

The resulting terminal innovation, and hence (Y^3), converges in
normalized (L^P); when the population variance is zero, the rate supplied
by (6.6) may be (O(n^{-1/4})), which is sufficient because no later
regression uses (Y^3).  Equation (1.3) then gives convergence of (z^3).

### 6.4 Removing stopping and passing to the expected output

For (|h|\le1), extend the raw-energy recursion from the five-action proof
through (s=2):

$$
\mathsf h_s=M_\phi(1+\mathsf u_s),\quad
\mathsf z_s=\mathsf w_s\mathsf h_s,\quad
\mathsf c_s=M_\phi\mathsf a_s,\quad
\mathsf b_s=\mathsf w_s\mathsf c_s,
$$

$$
\mathsf a_{s+1}=\mathsf a_s+M_\phi(1+\mathsf z_s),\quad
\mathsf u_{s+1}=\mathsf u_s+M_\phi\mathsf b_s,
$$

$$
\mathsf w_{s+1}=\mathsf w_s+\mathsf c_s\mathsf h_s,
\qquad s=0,1,2. \tag{6.7}
$$

Then form (\mathsf h_3,\mathsf z_3) by the first two rules.  Every
majorant in (6.7) is a fixed polynomial with nonnegative coefficients in

$$
M_\phi,\quad \|U\|_{n,2},\quad \|A\|_{n,2},\quad
\|W\|_{\rm op}/\sqrt n,
$$

whose moments of all fixed orders are uniform in (n).  Traversing the
finite expression tree also gives polynomial-in-(n) bounds for every
normalized (L^P) field and raw empirical product on the complement of the
good event.  Choose (M) in (6.3) larger than this finite polynomial power.
Hölder then removes stopping from every actual field, Gram, and raw
cross-moment in the ledger.

Finally,

$$
|f_n^3|
\le \|a^3\|_{n,2}\|\phi(z^3)\|_{n,2}
\le M_\phi\mathsf a_3(1+\mathsf z_3). \tag{6.8}
$$

The right side has a uniform (L^{1+\delta}) bound for every fixed
(\delta>0).  Thus the terminal empirical output is uniformly integrable.
Its empirical average converges in probability and in (L^1) to (2.5),
which proves (0.2).

The inverse-Gram regression coefficients are proof coordinates, not network
parameters.  On the good event their stopped versions converge in every
(L^P) and are uniformly integrable; on the negligible complement the
proof reverts to the raw network and (6.7).  No claim about untruncated
inverse-Gram coefficients is needed or made.  Every actual raw empirical
Gram, cross-moment, and output in the identification is untruncated and has
the convergence and uniform integrability just proved.

## 7. Adversarial audit

The fixed-(h) width bridge has the following status.

| obligation | status | reason |
|---|---|---|
| exact finite-width update and chronology | closed | (1.1)--(1.4) |
| predictability despite reused (W,W^T) | closed | filtration argument after (1.4) |
| dependence of (H^1) on (D^0) | closed in inherited five-action proof | it is retained in the old blocks (P,S,R) |
| all new empirical inputs at (D^2,Y^3) | closed | ledger (3.1) and (6.2), (6.5) |
| new reused-column response | closed | exact cancellation (4.3)--(4.8) |
| new reused-row response | closed | exact cancellation (5.3)--(5.7) |
| concentration of raw Grams and cross-moments | closed | finite high-moment coupling in Section 6 |
| terminal output uniform integrability | closed | (6.7)--(6.8) |
| terminal zero innovation | closed | (6.6), with no later inverse |
| rank needed by the bridge | exactly isolated | (Q^{[2]}>0,K^{[2]}>0) |

There is no remaining gap in the seven-action identification conditional on
(0.1).  There is one boundary on what this note proves: it does not itself
certify a numerical activation-defined radius on which (0.1) holds.  A
claim valid for every (0<|h|\le h_\phi) is unconditional only after the
separate desingularized-Gram lemma supplies that radius.  An argument that
merely cites continuity of (Q^{[2]},K^{[2]}), or gives unnamed
(o(1)) forward-difference remainders, does not meet the requested
quantitative qualification.
