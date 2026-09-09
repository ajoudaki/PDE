# Audited status of the proposed nonlinear L=3 joint limit

## Verdict

The proposed theorem is **not proved by the available argument**.  The fixed-width scaling, every finite-mesh width limit, and the explicit initialization/activity calculation are valid, but the passage from fixed finite Gaussian programs to compact continuous time has a load-bearing gap.  The status is *open*, not false: the audit below disproves the supplied proof and two natural repairs, not the existence of the claimed limit.

## Candidate model and the parts that do hold

For fixed pairwise distinct \(x_a\in\mathbb R^d\), \(\|x_a\|^2=d\), labels \(y_a\in\{\pm1\}\), and \(\phi(u)=\sin u+\cos u\), set
\[
U_i^a=w_i^\top x_a,\quad S^a=BH_1^a,\quad T^a=AH_2^a,\quad
H_\ell^a=\phi(Z_\ell^a),\quad f_a=\langle C,H_3^a\rangle_n,
\]
with \((Z_1,Z_2,Z_3)=(U,S,T)\), \(C=nc\), and \(\langle u,v\rangle_n=n^{-1}u^\top v\).  Initialize
\[
w_{ir}\sim N(0,d^{-1}),\quad A_{kj},B_{ji}\sim N(0,n^{-1}),
\quad c_k\sim N(0,n^{-4}),
\]
and use raw mobilities \(n/d,1,1,1/n\) for \(w,B,A,c\).  With
\[
D_3^a=C\phi'(T^a),\quad P_2^a=A^\top D_3^a,\quad
D_2^a=\phi'(S^a)P_2^a,\quad P_1^a=B^\top D_2^a,
\]
the normalized gradient-flow equations are exactly
\[
\begin{aligned}
\dot U^a&=-\gamma\sum_bR_{ab}e_b\phi'(U^b)P_1^b,\\
\dot B&=-\gamma\sum_be_bD_2^b\otimes_nH_1^b,\\
\dot A&=-\gamma\sum_be_bD_3^b\otimes_nH_2^b,\\
\dot C&=-\gamma\sum_be_bH_3^b,
\end{aligned}
\qquad \gamma=2/p,\quad R_{ab}=d^{-1}x_a^\top x_b. \tag{1}
\]
The corresponding four kernel blocks and the identities
\(\dot f=-\gamma Ke\), \(\dot{\mathcal L}=-\gamma^2e^\top Ke\) are also exact.

For every **fixed finite** Euler mesh and number of steps, first form a deterministic *population oracle*: set its initial readout coordinate to \(C_0=0\), and, in the unrolled rank-one updates, replace each empirical residual and overlap scalar by the population expectation recursively supplied by preceding oracle nodes.  That oracle is a parameterless NETSOR\(^{\top}\) program, so Yang's Master Theorem (arXiv:2009.10685v3, Theorem 2.10) applies to it.  Its exact scope is a fixed finite program; it allows singular initial Gaussian covariance and arbitrary finite reuse of a matrix and its transpose.  Theorem A.2 supplies mean convergence for quadratically bounded tests when the oracle's coordinate maps are linearly bounded.  Couple the actual and oracle programs with the same \(A_0,B_0,U_0\).  Since the actual \(C_{0,i}\sim N(0,n^{-2})\), \(\|C_0\|_n=o_{\mathbb P}(1)\), while \(\|A_0\|_{\mathrm{op}}+\|B_0\|_{\mathrm{op}}=O_{\mathbb P}(1)\).  A finite node-by-node Hölder/moment induction (using the Master Theorem for the finitely many polynomial moments required at that fixed depth) then shows that every empirical feedback scalar differs by \(o_{\mathbb P}(1)\) and every vector differs by \(o_{\mathbb P}(1)\) in normalized \(\ell^2\).  Thus the actual network, including its quadratic kernel observables, is identified **in probability** for each fixed finite number of steps.  No growing-time or actual-network \(L^1\) assertion is made.  Neither theorem, nor this finite induction, is uniform when the program length tends to infinity.  Directly treating the empirical feedback as parameterized NETSOR\(^{\top+}\) would require its separate hypotheses and is not being invoked here.

Conditional on a compact-time action-law limit with the required strong \(L^2\) continuity, the initialization calculation is valid.  The uppercase backpropagated fields vanish at \(t=0\); the lowercase variables below are their right-hand first coefficients, defined by
\[
\frac{D_3^a(t)}{\gamma t}\to d_a^3,\quad
\frac{P_2^a(t)}{\gamma t}\to p_a^2,\quad
\frac{D_2^a(t)}{\gamma t}\to d_a^2,\quad
\frac{P_1^a(t)}{\gamma t}\to p_a^1
\quad\text{strongly in }L^2. \tag{2a}
\]
Define
\[
Q_1=e^{-1+R},\qquad Q_2=e^{-1+Q_1},\qquad Q_3=e^{-1+Q_2}
\]
entrywise.  The distinct-input Gaussian-RBF argument gives \(Q_1\succ0\), and Schur powers give \(Q_2,Q_3\succ0\).  If
\[
g(T)=\sum_cy_c\phi(T_c),\qquad d_a^3=g(T)\phi'(T_a),
\quad G^3_{ab}=\mathbb E[d_a^3d_b^3],
\]
then the two exact reused-adjoint laws at initialization are
\[
p_a^2=\zeta_a^2+\sum_cM^3_{ac}\phi(S_c),
\quad M^3_{ac}=y_cQ_{3,ac}-\delta_{ac}(Q_3y)_a,
\quad \zeta^2\sim N(0,G^3),
\]
and, with \(d_a^2=\phi'(S_a)p_a^2\), \(G^2=\mathbb E[d^2d^{2\top}]\),
\[
p_a^1=\zeta_a^1+\sum_cM^2_{ac}\phi(U_c),
\quad M^2_{ac}=Q_{2,ac}M^3_{ac}
-\delta_{ac}\sum_kQ_{2,ak}M^3_{ak},
\quad \zeta^1\sim N(0,G^2).
\]
The innovations are independent of the preceding layer.  The matrices
\(G^3,G^2,G^1\), where \(G^1=\mathbb E[q^1q^{1\top}]\) and
\(q_a^1=\phi'(U_a)p_a^1\), are positive definite.  Hence
\[
L_1=R\circ G^1,\qquad L_2=Q_1\circ G^2,
\qquad L_3=Q_2\circ G^3
\]
are positive definite, including when \(R\) is singular.  The resulting formal small-time coefficients are
\[
K^U(t)=\gamma^2t^2L_1+o(t^2),\quad
K^B(t)=\gamma^2t^2L_2+o(t^2),\quad
K^A(t)=\gamma^2t^2L_3+o(t^2),
\]
and
\[
y^\top K(t)y=y^\top Q_3y
+2\gamma^2t^2\sum_{r=1}^3y^\top L_ry+o(t^2),
\qquad \mathcal L'(0+)=-\gamma^2y^\top Q_3y<0. \tag{2}
\]
These are conditional width-limit jets; they do not establish compact-time existence.

## The fatal gap

The candidate proof attempted to establish, uniformly for \(k h\le T\),
\[
\|P_{1,k}^a\|_{\psi_2}+\|P_{2,k}^a\|_{\psi_2}\le C T. \tag{3}
\]
It defined \(I_q(X)=\|\partial X/\partial\widehat Z_q\|_2\).  This is a deterministic number, but the subsequent recurrence treated its aggregate \(J_k\) as a random variable and wrote a pointwise inequality containing random \(|P_{r,k}|\), followed by \(\mathbb EJ_k^2\).  Thus the lemma is ill-typed.

Changing to pointwise derivatives does not repair it.  A current call of \(A_0\) or \(B_0\) has response terms from every preceding opposite-orientation call.  The proof did not enumerate the forward responses, adjoint responses, learned-rank paths, error/overlap paths, and product branches.  In a dense history, Gaussian source Grams are singular or nearly singular.  The total response vector is invariant, but an \(\ell^1\) mass of coefficients in a redundant source list is not: if \(Y_0=\phi(Z)\) and \(Y_h=\phi(Z+hX)\), the bounded response \((Y_h-Y_0)/h\) has coefficient mass \(2/h\).  Higher differences have masses \(h^{-m}\).  The fixed-program core-set theorem gives no uniform bound on these masses as \(h\downarrow0\).  Therefore (3), its exponential tail consequence, and cutoff removal were not proved.

This is not a cosmetic demand.  Normalized \(L^2\) and matrix operator-norm bounds do not imply an adaptive-adjoint tail bound.  If \(G_{ij}\sim N(0,1/n)\) and \(v_i=\operatorname{sign}(G_{i1})\), then \(|v_i|=1\), while
\[
(G^\top v)_1=\sum_i|G_{i1}|\asymp\sqrt n.
\]
Its one exceptional coordinate contributes order one to the normalized squared norm, so fixed-level \(L^2\) tails do not vanish.  Reachability restrictions may rule out this particular \(v\), but proving precisely such a restriction is the missing all-history theorem.

Nor does the trigonometric identity by itself close the gap.  With \(H=\sin+\cos\), \(G=H'=\cos-\sin\), one has \((H,G)'=J(H,G)\), but the gate \(D_2=G(S)\odot P_2\), viewed as a map of the two independent state inputs \((S,P_2)\), has the partial derivative
\[
 D_S\big|_{P_2}[D_2]\,\xi=-H(S)\odot P_2\odot\xi. \tag{4}
\]
Already at the first positive population-oracle Euler node,
\(P_{2,1}/(\gamma h)=p^2\) contains the nondegenerate Gaussian innovation \(\zeta^2\) in the displayed initialization law.  Multiplication by \(-H(S)P_{2,1}\) is therefore an unbounded, and not uniformly one-sided-bounded, operator on \(L^2\).  Rotation preserves one trajectory's radius, not the distance between two trajectories.  Thus the proposed **nodewise globally Lipschitz \(L^2\)** stability repair fails.  Equation (4) does not rule out a different, genuinely coupled cancellation mechanism; none is supplied by the candidate proof.

## Consequences

Without (3), the manuscript has no valid proof of:

1. a mesh-uniform limit as the number of reused-matrix calls tends to infinity;
2. removal of the adjoint cutoff;
3. uniform integrability of kernels and squared velocities;
4. \(W_2(C([0,T]))\) convergence of the hidden paths;
5. uniqueness of an abstract GNS action-law solution; or
6. autonomy and restartability of that solution.

The GNS construction itself also needs a complete state space and vector field; fixed-probe adjoint identities alone do not prove uniqueness or a semigroup.

## Minimal missing theorem package

A successful proof needs a representation-invariant, causal aggregate-adjoint theory for the entire dense history.  Its central a-priori estimate could take the following form: construct a covariance-quotient/isonormal source space and prove, for some \(c,C,T_0>0\),
\[
\sup_{0<h\le T\le T_0}\ \sup_{kh\le T}\ \sup_{a,r}
\mathbb E\exp\{c|P_{r,k}^a|^2/T^2\}\le C, \tag{5}
\]
together with full-state mesh tightness and equicontinuity, Euler consistency and identification in a complete covariance-quotient state, two-history stability/uniqueness, convergence of the response operators as \(h\downarrow0\), and a restart/semigroup theorem.  The proof must include both orientations of both reused matrices and must remain valid at singular covariance.  Alternatively, a direct Osgood/monotonicity mechanism strong enough to replace this package would suffice.  No theorem cited in the candidate proof asserts these results.

Accordingly, a clean proof of the L=3 compact-time joint mean-field/gradient-flow theorem cannot presently be output.  The exact finite-step and initialization calculations above survive, but the full theorem remains unresolved.
