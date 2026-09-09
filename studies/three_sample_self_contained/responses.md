# Part R. Controlled source responses for three samples

This part proves the response bound using only the fixed-program Gaussian and common-space Lemma F stated precisely below. A separate primal estimate supplies the affine boundedness hypothesis. The proof identifies the actual source equations, converts affine raw stability to formal response bounds by a Gaussian probe, bounds nonlinear source variances without assuming response estimates, controls coordinate and derivative moments on bounded prefixes, and closes those prefixes in the chronological order of the four query stages.

## R.1. Setup and the Gaussian-program input

Fix \(a\ge1,B\ge1,S>0\), and a positive semidefinite \(3\times3\) matrix \(\Gamma\) with unit diagonal. On any positive mesh \(0=s_0<\cdots<s_N\le S\), put \(h_j=s_{j+1}-s_j\). Choose deterministic controls \(c_j\in\mathbb R^3\) with \(\sum_i|c_{j,i}|\le1\), and set
\[
 P_j=\Gamma\operatorname{diag}(c_j),\qquad \mathbf1=(1,1,1)^T.
 \tag{R.1}
\]
Positive semidefiniteness of two-by-two principal minors gives \(|\Gamma_{im}|\le1\). Thus \(|P_j|\le1\), where, for rectangular matrices and finite rows of time blocks,
\[
 |T|=\max_i\sum_j|T_{ij}|,\qquad
 |T_{k\bullet}|_{\rm r}=\sum_j|T_{kj}|.
 \tag{R.2}
\]
These norms are submultiplicative, \(|I_3|=|\mathbf1|=1\), and \(|c_j^T|\le1\). For a random three-vector use \(\|X\|_p=(E|X|_\infty^p)^{1/p}\). Pad derivative rows by causal zero blocks when necessary.

For \(0\le\epsilon\le1\), take
\[
 \phi_\epsilon(z)=a(1+z)+\epsilon\arctan z,\quad g(z)=(1+z^2)^{-1},
 \quad D_{\epsilon,R}(z,q)=aq+\epsilon g(z)\tau_R(q).
 \tag{R.3}
\]
The finite cap \(R>0\) uses a smooth function satisfying \(|\tau_R(q)|\le\min\{|q|,2R\}\), \(|\tau_R'|\le1\), and \(\tau_R(q)=q\) on \([-R,R]\). Oddness can be imposed but is not used in these estimates. Since \(|g|,|g'|\le1\),
\[
 |D(z,q)|\le(a+1)|q|,\qquad |\phi_\epsilon(z)|\le a|z|+a+2.
 \tag{R.4}
\]
At fixed cap these coordinate instructions are continuously differentiable and globally Lipschitz: the two partial derivatives of \(D\) are bounded by \(2\epsilon R\) and \(a+\epsilon\).

Use normalized finite inner products \(\langle u,v\rangle_n=u^Tv/n\), independent initialized hidden matrices with entries \(N(0,1/n)\), and independent first-layer rows of joint law \(N(0,\Gamma)\). The controlled program in this part has \(C_0=0\). Its population has three separate neuron probability spaces; an expectation of layer-\(\ell\) variables is taken in that layer's space. Initial matrix actions have their actual adjoints, and learned increments are rank-one operators \(u\otimes v:q\mapsto u\langle v,q\rangle\). There is no pairing of coordinates across distinct layers.

The following is the exact version of internal Lemma F required here. For a fixed finite program with finitely many independent normalized Gaussian matrices used in both orientations, interleaved with \(C^1\) globally Lipschitz coordinate instructions with bounded derivatives, independent iid root tuples with finite second moments, and causal empirical inner products, the joint empirical coordinate laws and second moments have a canonical Gaussian-source limit. An initialized forward call on \(h\) has the representation
\[
 \xi_h+\sum_v u_v E\partial_{\zeta_v}h,
 \tag{R.5}
\]
where \(u_v\) are its previously queried reverse inputs. An initialized reverse call on \(u\) has the representation
\[
 \zeta_u+\sum_v h_v E\partial_{\xi_v}u,
 \tag{R.6}
\]
where \(h_v\) are its already queried forward inputs, including those earlier in the same time step. Forward and reverse source covariances are the full second moments of the corresponding matrix inputs. Distinct source groups and independent roots are independent in the canonical representation. Formal differentiation freezes all deterministic coefficients and covariance parameters and treats every named source slot separately, including at singular covariance. The lemma includes extra independent Gaussian roots and joint convergence of finitely many programs sharing initialized matrices and roots, on common action spaces.

This version of Lemma F is an input, not a conclusion about arbitrary bounded operators. Its applicability to empirical contractions is also elementary once its fixed-coefficient assertion is available. Freeze finitely many contractions at their causally constructed limits. Convergence of preceding nodes makes the error of each contraction tend to zero. A finite induction through Lipschitz coordinate instructions, bounded matrix actions, and the rank-one inequality transfers the limit to the actual contractions. The same induction identifies convergent causal scalar feedback values; no derivatives of that feedback enter (R.5)–(R.6).

The affine hypothesis is that, at each fixed mesh under consideration, the actual finite-width affine Euler arrays satisfy
\[
 \max_{k,i}\|Z^{1,0}_{k,i}\|_n\le B,\qquad
 \max_k\{\|W^0_{2,k}\|_{\rm op},\|W^0_{3,k}\|_{\rm op},\|C^0_k\|_n\}
 \le B
 \tag{R.7}
\]
on events of probability tending to one. One bound \(B\) works for the controls and meshes used in the application. An available bound may be enlarged to supply slack. A continuous-flow bound alone does not assert stability of arbitrary coarse Euler meshes.

We will construct explicit finite constants \(\epsilon_*(a,B,S)>0\), \(A,M,K\) such that every actual program with \(0\le\epsilon\le\epsilon_*\) satisfies
\[
 |A^\ell_{kj}|\le Ah_j\quad(j<k),\qquad
 |B^\ell_{k\bullet}|_{\rm r}\le M,\quad\ell=2,3,
 \tag{R.8}
\]
\[
 \sup_{k,R}\bigl(\|C_k\|_p+\|q^2_k\|_p+\|q^1_k\|_p\bigr)
 \le K\sqrt p\qquad(p\ge2).
 \tag{R.9}
\]
The constants are independent of \(\Gamma\), the cap, the mesh size and number of points, and variation of the controls.

## R.2. Deriving the source system

The forward calculation is \(H^\ell_{k,i}=\phi_\epsilon(Z^\ell_{k,i})\), \(Z^2_{k,i}=W_{2,k}H^1_{k,i}\), \(Z^3_{k,i}=W_{3,k}H^2_{k,i}\). The backward calculation is
\[
 \delta^3_{k,i}=D(Z^3_{k,i},C_k),\quad
 q^2_{k,i}=W_{3,k}^T\delta^3_{k,i},\quad
 \delta^2_{k,i}=D(Z^2_{k,i},q^2_{k,i}),
\]
\[
 q^1_{k,i}=W_{2,k}^T\delta^2_{k,i},\quad
 \delta^1_{k,i}=D(Z^1_{k,i},q^1_{k,i}).
\]
The controlled raw Euler updates are
\[
 Z^1_{k+1}=Z^1_k+h_kP_k\delta^1_k,
\]
\[
 W_{\ell,k+1}=W_{\ell,k}
 +h_k\sum_i c_{k,i}\delta^\ell_{k,i}\otimes_n H^{\ell-1}_{k,i},
 \quad \ell=2,3,\qquad
 C_{k+1}=C_k+h_kc_k^TH^3_k.
 \tag{R.10}
\]
For normalized inputs the first equation is exactly the projection of \(w_{k+1}=w_k+h_k\sum_i c_{k,i}\delta^1_{k,i}x_i/d\).

Unrolling the matrix update produces a learned forward addition
\[
 \sum_{j<k,m}h_jc_{j,m}\delta^\ell_{j,m}
       \langle H^{\ell-1}_{j,m},H^{\ell-1}_{k,i}\rangle_n
\]
and a learned reverse addition
\[
 \sum_{j<k,m}h_jc_{j,m}H^{\ell-1}_{j,m}
       \langle\delta^\ell_{j,m},\delta^\ell_{k,i}\rangle_n.
\]
Apply (R.5) and (R.6) to the remaining initialized matrix calls, and pass the displayed contractions to their expectations. Their sum gives
\[
 (A^\ell_{kj})_{im}
 =E\partial_{\zeta^{\ell-1}_{j,m}}H^{\ell-1}_{k,i}
 +h_jc_{j,m}E[H^{\ell-1}_{k,i}H^{\ell-1}_{j,m}],\quad j<k,
 \tag{R.11}
\]
\[
 (B^\ell_{kj})_{im}
 =E\partial_{\xi^\ell_{j,m}}\delta^\ell_{k,i}
 +\mathbf1_{j<k}h_jc_{j,m}E[\delta^\ell_{k,i}\delta^\ell_{j,m}],
 \quad j\le k.
 \tag{R.12}
\]
There is no extra control factor in the response term: controls already appear on its derivative paths through parameter updates.

The four centered Gaussian groups have covariances
\[
 E[\xi^\ell_{k,i}\xi^\ell_{j,m}]
   =E[H^{\ell-1}_{k,i}H^{\ell-1}_{j,m}],\qquad
 E[\zeta^{\ell-1}_{k,i}\zeta^{\ell-1}_{j,m}]
   =E[\delta^\ell_{k,i}\delta^\ell_{j,m}],\quad\ell=2,3.
 \tag{R.13}
\]
All time/sample correlations are retained, including singularities and nonzero feature means. The groups are independent as in Lemma F; coordinates within a group are not made independent. The complete source equations are
\[
 Z^1_k=Z^1_0+\sum_{r<k}h_rP_r\delta^1_r,\qquad
 q^1_k=\zeta^1_k+\sum_{v\le k}B^2_{kv}H^1_v,
 \tag{R.14}
\]
\[
 Z^2_k=\xi^2_k+\sum_{r<k}A^2_{kr}\delta^2_r,\qquad
 q^2_k=\zeta^2_k+\sum_{v\le k}B^3_{kv}H^2_v,
 \tag{R.15}
\]
\[
 Z^3_k=\xi^3_k+\sum_{r<k}A^3_{kr}\delta^3_r,\qquad
 C_k=\sum_{r<k}h_rc_r^TH^3_r,
 \tag{R.16}
\]
with \(Z^1_0\sim N(0,\Gamma)\), \(C_0=0\), and the coordinate maps already specified.

At each time compute all layer-2 forward calls, all layer-3 forward calls, all layer-3 reverse calls, then all layer-2 reverse calls, and finally update parameters. Thus the row construction order is
\[
                         A^2_k,\quad A^3_k,\quad B^3_k,\quad B^2_k.
 \tag{R.17}
\]
Samples within one stage are treated together. Every covariance and response coefficient uses quantities already available in this order. No covariance inverse or differentiation along the Gaussian support is involved.

If a physical population trajectory supplies \(c_k=-r_k/\|r_k\|_1\) and \(h_k=\Delta t_k\|r_k\|_1\), these are deterministic causal numbers. They are frozen in (R.11)–(R.12), and the affine comparator uses those identical numbers. At a zero residual the physical update is zero and the step is omitted. Thus the normalized residual is never differentiated.

## R.3. Raw affine stability and the Gaussian probe

Put
\[
 b=2B,\qquad Q=100a^3b^3,\qquad E_0=e^{QS},\qquad T_0=QSE_0.
 \tag{R.18}
\]
Use the raw distance
\[
 d(\theta,\widetilde\theta)
 =\max_i\|Z^1_i-\widetilde Z^1_i\|_2
 +\|W_2-\widetilde W_2\|_{\rm op}
 +\|W_3-\widetilde W_3\|_{\rm op}
 +\|C-\widetilde C\|_2,
 \tag{R.19}
\]
with normalized finite norms at finite width. On the ball where each primal size is at most \(b\), affine propagation gives
\[
 \|H^1_i\|\le2ab,\quad\|H^2_i\|\le3a^2b^2,\quad\|H^3_i\|\le4a^3b^3,
\]
\[
 \delta^3_i=aC,\qquad \delta^2_i=a^2W_3^TC,\qquad
 \delta^1_i=a^3W_2^TW_3^TC.
 \tag{R.20}
\]
For the four component differences \(u,v,w,t\) in (R.19), subtraction gives
\[
 \|\Delta H^1_i\|\le au,\quad
 \|\Delta H^2_i\|\le a^2b(u+2v),\quad
 \|\Delta H^3_i\|\le a^3b^2(u+2v+3w),
\]
\[
 \|\Delta\delta^3_i\|\le at,\quad
 \|\Delta\delta^2_i\|\le a^2b(w+t),\quad
 \|\Delta\delta^1_i\|\le a^3b^2(v+w+t).
 \tag{R.21}
\]
The rank-one inequality
\[
 \|u\otimes v-\widetilde u\otimes\widetilde v\|
 \le\|u-\widetilde u\|\|v\|+\|\widetilde u\|\|v-\widetilde v\|
 \tag{R.22}
\]
bounds the four update-component Lipschitz constants by \(a^3b^2,2a^3b^2,3a^3b^2,3a^3b^2\). Their sum is at most \(Q\). Every query norm and query Lipschitz constant used below is also at most \(Q\), by (R.20)–(R.21) and the two matrix applications defining the incoming fields.

Insert additive errors after one chosen matrix-answer type, recomputing subsequent calls and parameter updates. Errors with norm at most \(e_j\) in each sample at time \(j\) change the affine raw field at a fixed raw state by at most \(\kappa e_j\), with the following constants.

| Answer type | Affected updates | \(\kappa\) |
|---|---|---:|
| \(Z^2\) | \(W_3,C\) | \(2a^2b\) |
| \(Z^3\) | \(C\) | \(a\) |
| \(q^2\) | \(Z^1,W_2\) | \(3a^2b\) |
| \(q^1\) | \(Z^1\) | \(a\) |

A \(Z^2\) error changes \(H^2\) by \(a e_j\), and each of the \(W_3,C\) updates by at most \(a^2b e_j\). A \(q^2\) error changes \(\delta^2\) by \(a e_j\), contributes at most \(2a^2b e_j\) to the \(W_2\) update and \(a^2b e_j\) to the first-layer update. The two other entries follow directly from their affine gates. Each \(\kappa\le Q\).

Take an independent iid standard Gaussian vector \(g_n\) in the selected answer population, and insert \(\eta\alpha_{j,i}g_n\) with deterministic \(|\alpha_{j,i}|\le1\). The same vector is reused at the chosen times and sample slots. Finite iteration of the comparison recurrence gives
\[
 d(\theta_k^\eta,\theta_k^0)\le QSE_0|\eta|\|g_n\|_n.
 \tag{R.23}
\]
When only time \(j\) is perturbed, replace \(S\) by \(h_j\): the sole forcing in the state update carries \(h_j\), and later factors have product at most \(E_0\). On (R.7) and \(\|g_n\|_n\le2\), choose \(2T_0|\eta|<B/2\). Induction gives (R.23) at each next node and keeps the perturbed state strictly within the ball of radius \(b\).

Apply this to the four source/output pairs
\[
 (\zeta^1,H^1_i),\quad(\zeta^2,H^2_i),\quad
 (\xi^2,\delta^2_i),\quad(\xi^3,\delta^3_i).
 \tag{R.24}
\]
For affine gates the indicated output has no direct current dependence on that answer perturbation at fixed raw state, so its difference is at most \(Q\) times (R.23).

At a fixed probe amplitude Lemma F, with its extra independent root, gives
\[
 \langle g_n,V_n^\eta\rangle_n\longrightarrow E[GV^\eta],
 \tag{R.25}
\]
where \(G\sim N(0,1)\) is independent of the canonical source groups. Freeze the perturbed program's deterministic coefficients. Every affine coordinate is affine in the roots and sources. If \(D_{j,i}(\eta)=\partial_{\mathrm{source}_{j,i}}V^\eta\), the only explicit appearances of \(G\) are the inserted additions at those slots. Hence
\[
 \partial_GV^\eta=\eta\sum_{j,i}\alpha_{j,i}D_{j,i}(\eta),\qquad
 E[GV^\eta]=\eta\sum_{j,i}\alpha_{j,i}D_{j,i}(\eta).
 \tag{R.26}
\]
The second identity follows by writing \(V^\eta=U+tG\), with \(U\) independent of \(G\), and using \(EG=0,EG^2=1\).

At this fixed mesh \(D_{j,i}(\eta)\to D_{j,i}(0)\). Indeed affine coordinate coefficients are polynomial functions of preceding coefficients; their second moments are polynomial in these coefficients and covariance entries; expected formal derivatives are deterministic affine coefficients. Finite induction in order (R.17) proves continuity without inverting covariance matrices.

Conditionally on the unperturbed network, \(\langle g_n,V_n^0\rangle_n\) is centered Gaussian with variance \(\|V_n^0\|_n^2/n\), which tends to zero. Cauchy–Schwarz and (R.23) bound the pairing of the difference, divided by \(|\eta|\), by \(Q^2SE_0\|g_n\|_n^2\). First send width to infinity at fixed nonzero amplitude using (R.25)–(R.26), and then send amplitude to zero by the preceding continuity. This gives
\[
 \left|\sum_{j,i}\alpha_{j,i}D_{j,i}(0)\right|\le Q^2SE_0.
 \tag{R.27}
\]
Choose the signs of this deterministic finite derivative row to obtain its absolute row sum. Restricting signs to one time yields a block bound \(Q^2h_jE_0\). This applies even to coincident or zero-variance source slots, since errors were inserted at separately named finite answer slots. No derivative/width-limit interchange or trace identification is required.

The learned blocks in (R.11)–(R.12) have norm at most \(Q^2h_j\), by Cauchy–Schwarz and \(\sum_i|c_{j,i}|\le1\). Conversion of a maximum of three full scalar output-row sums to a sum of maximum block norms costs at most three. Therefore
\[
 A_0=3Q^2(E_0+1),\qquad M_0=3SQ^2(E_0+1)
 \tag{R.28}
\]
give
\[
 |A^{\ell,0}_{kj}|\le A_0h_j,\qquad
 |B^{\ell,0}_{k\bullet}|_{\rm r}\le M_0,\qquad\ell=2,3.
 \tag{R.29}
\]
The affine current blocks \(B^{\ell,0}_{kk}\) vanish because the corresponding two backward outputs in (R.24) have no direct current forward-source derivative.

## R.4. Nonlinear primal comparison and source variances

On the same raw ball, (R.4) gives
\[
 \|H^1_i\|\le3ab,\quad\|H^2_i\|\le4a^2b^2,\quad
 \|H^3_i\|\le5a^3b^3,
\]
\[
 \|\delta^3_i\|\le2ab,\quad\|q^2_i\|\le2ab^2,\quad
 \|\delta^2_i\|\le4a^2b^2,\quad
 \|q^1_i\|\le4a^2b^3,\quad\|\delta^1_i\|\le8a^3b^3.
 \tag{R.30}
\]
At an identical raw state, the nonlinear forward differences from affine queries are at most
\[
                   2\epsilon,\quad3ab\epsilon,\quad4a^2b^2\epsilon
 \tag{R.31}
\]
in layers 1, 2, 3. The intermediate exact upper bounds are \(2(1+ab)\epsilon\) and \(2(1+ab+a^2b^2)\epsilon\); use \(ab\ge2\). The backward differences in \(\delta^3,q^2,\delta^2,q^1,\delta^1\) are bounded, respectively, by
\[
 b\epsilon,\quad b^2\epsilon,\quad3ab^2\epsilon,\quad
 3ab^3\epsilon,\quad7a^2b^3\epsilon.
 \tag{R.32}
\]
For example \(|D(z,q)-aq|\le\epsilon|q|\), so the middle delta difference is at most \(a b^2\epsilon+2ab^2\epsilon\), using the nonlinear incoming norm in (R.30).

Substituting (R.30)–(R.32) in (R.22) bounds the sum of the four raw-field differences by \(30a^3b^3\epsilon\le Q\epsilon\). Affine raw-field Lipschitzness yields, for identical initialization and controls,
\[
 d_{k+1}\le(1+Qh_k)d_k+Q\epsilon h_k,\qquad d_k\le T_0\epsilon.
 \tag{R.33}
\]
If \(\epsilon\le B/(2T_0)\), stopped induction gives this bound at the next node and keeps the nonlinear path at distance at least \(B/2\) from the boundary. Neither a nonlinear-field Lipschitz constant nor a cap enters this comparison.

Define
\[
 \sigma=Q,\qquad D_0=Q(1+T_0),\qquad m_0=2QD_0.
 \tag{R.34}
\]
Every nonlinear and affine query has norm at most \(Q\). Its same-state difference from (R.31)–(R.32), followed by the affine query Lipschitz bound, gives an actual coupled query difference at most \(D_0\epsilon\). At fixed mesh and cap Lemma F passes these finite-array comparisons to the actual population programs sharing initialized matrices and roots. No comparison of square roots of growing source covariances is used.

Equation (R.13) therefore bounds every scalar source variance by \(\sigma^2\), without any response estimate. For each learned moment,
\[
 |E[UV]-E[U^0V^0]|
 \le\|U-U^0\|_2\|V\|_2+\|U^0\|_2\|V-V^0\|_2
 \le m_0\epsilon.
 \tag{R.35}
\]
Retaining the column control weights gives learned forward-block differences at most \(m_0\epsilon h_j\) and learned backward-row differences at most \(m_0S\epsilon\).


## R.5. Coordinate moments on bounded coefficient prefixes

Fix
\[
                     A=A_0+1,\qquad M=M_0+1,\qquad d_a=a+1.
 \tag{R.36}
\]
Initially assume only that the rows needed for a particular construction prefix satisfy (R.8). Section R.9 closes this assumption stage by stage.

A centered scalar Gaussian of variance at most \(\sigma^2\) satisfies \(\|G\|_p\le2\sigma\sqrt p\) for \(p\ge2\): its Gaussian integral gives \(Ee^{G^2/(4\sigma^2)}\le\sqrt2\), and maximizing \(x^pe^{-x^2/(4\sigma^2)}\) gives the norm bound. The maximum of three such variables consequently has \(L^p\) norm at most \(6\sigma\sqrt p\), regardless of their dependence. The first-layer root has this bound too.

Introduce explicit finite constants
\[
 k_0=a+2+6a\sigma,
\]
\[
 K_1=(k_0+6a d_a\sigma S)e^{a d_a MS},\qquad
 K_2=(k_0+6a d_a A\sigma S)e^{a d_a AMS},
\]
\[
 K_C=k_0S e^{a d_a AS^2},\qquad
 K_{q1}=6\sigma+MK_1,\quad K_{q2}=6\sigma+MK_2,
\]
\[
                         K_q=1+K_C+K_{q1}+K_{q2}.
 \tag{R.37}
\]
For \(U^1_k=\max_{v\le k}\|H^1_v\|_p\), (R.14) and (R.4) yield
\[
 \|q^1_r\|_p\le6\sigma\sqrt p+MU^1_r,\qquad
 U^1_k\le(k_0+6a d_a\sigma S)\sqrt p+a d_a M\sum_{r<k}h_rU^1_r.
 \tag{R.38}
\]
The maximum here is of deterministic norms, not a random maximum over times. For \(U^2_k=\max_{v\le k}\|H^2_v\|_p\), (R.15) yields
\[
 \|q^2_r\|_p\le6\sigma\sqrt p+MU^2_r,\qquad
 U^2_k\le(k_0+6a d_a A\sigma S)\sqrt p+a d_a AM\sum_{r<k}h_rU^2_r.
 \tag{R.39}
\]
At the top,
\(\|H^3_k\|_p\le k_0\sqrt p+a d_a A\sum_{r<k}h_r\|C_r\|_p\).
Substituting this into the readout sum, \(V_k=\max_{v\le k}\|C_v\|_p\) satisfies
\[
                    V_k\le k_0S\sqrt p+a d_a AS\sum_{r<k}h_rV_r.
 \tag{R.40}
\]
For nonnegative sequences, finite iteration of \(x_k\le f+L\sum_{r<k}h_rx_r\) gives \(x_k\le f\prod_{r<k}(1+Lh_r)\le f e^{LS}\). Applying this to (R.38)–(R.40) proves
\[
 \|H^1_k\|_p\le K_1\sqrt p,\quad\|H^2_k\|_p\le K_2\sqrt p,\quad
 \|C_k\|_p\le K_C\sqrt p,
\]
\[
                     \|q^1_k\|_p\le K_{q1}\sqrt p,\qquad
                     \|q^2_k\|_p\le K_{q2}\sqrt p.
 \tag{R.41}
\]
Equations (R.14)–(R.16) and (R.4) then bound all preactivations, top features, and deltas by finite multiples of \(\sqrt p\).

For each population separately let \(Q_k\) denote its incoming-field maximum, respectively \(|q^1_k|_\infty,|q^2_k|_\infty,|C_k|\). Then \(\|Q_k\|_p\le K_q\sqrt p\). Set
\[
                            L_q^2=8\exp(1)K_q^2.
 \tag{R.42}
\]
Expanding the exponential and using \(m!\ge(m/\exp(1))^m\) gives
\[
 Ee^{Q_k^2/L_q^2}
 \le \sum_{m\ge0}\frac{K_q^{2m}(2m)^m}{L_q^{2m}m!}
 \le\sum_{m\ge0}4^{-m}<2.
 \tag{R.43}
\]
The \(m=0\) summand is one. The factorial inequality follows by bounding \(\sum_{j=1}^m\log j\) below by \(\int_1^m\log x\,dx\).

## R.6. Exact nonlinear derivative equations and integrability

At each layer use its incoming \(q\), with \(q=C\mathbf1\) at the top, and define
\[
 G_k=aI+\epsilon\operatorname{diag}(g(Z_k)),
\]
\[
 V_k=aI+\epsilon\operatorname{diag}(g(Z_k)\tau_R'(q_k)),\qquad
 L_k=\epsilon\operatorname{diag}(g'(Z_k)\tau_R(q_k)).
 \tag{R.44}
\]
Then
\[
 |G_k|,|V_k|\le d_a,\quad |G_k-aI|,|V_k-aI|\le\epsilon,\qquad
 |L_k|\le\epsilon Q_k.
 \tag{R.45}
\]
The cap derivative is included explicitly in \(V_k\).

For a bottom reverse source at time \(j\), let
\(J^1_{k,j}=\partial_{\zeta^1_j}Z^1_k\), a \(3\times3\) matrix. Differentiating (R.14) at fixed coefficient arrays gives exactly
\[
 J^1_{k,j}=\sum_{r<k}h_rP_r\left[
 L^1_rJ^1_{r,j}+V^1_r\left(
 I\mathbf1_{r=j}+\sum_{v\le r}B^2_{rv}G^1_vJ^1_{v,j}\right)\right].
 \tag{R.46}
\]
For a middle forward source set \(I_k^\xi=I\mathbf1_{k=j},I_k^\zeta=0\); for a middle reverse source interchange these assignments. Equation (R.15) gives
\[
 J^2_{k,j}=I_k^\xi+\sum_{r<k}A^2_{kr}\left[
 L^2_rJ^2_{r,j}+V^2_r\left(
 I_r^\zeta+\sum_{v\le r}B^3_{rv}G^2_vJ^2_{v,j}\right)\right].
 \tag{R.47}
\]
In both equations the feature derivative is \(G_kJ_k\).
For a top forward source put \(J^3_{k,j}=\partial_{\xi^3_j}Z^3_k\) and \(T_{k,j}=\partial_{\xi^3_j}C_k\), the latter a \(1\times3\) row. The exact equations are
\[
 J^3_{k,j}=I\mathbf1_{k=j}+\sum_{r<k}A^3_{kr}
                 (L^3_rJ^3_{r,j}+V^3_r\mathbf1T_{r,j}),
\]
\[
                     T_{k,j}=\sum_{r<k}h_rc_r^TG^3_rJ^3_{r,j}.
 \tag{R.48}
\]
The backward outputs have derivatives
\[
 \partial_{\xi^2_j}\delta^2_k
   =L^2_kJ^2_{k,j}+V^2_k\sum_{v\le k}B^3_{kv}G^2_vJ^2_{v,j},
\]
\[
 \partial_{\xi^3_j}\delta^3_k
   =L^3_kJ^3_{k,j}+V^3_k\mathbf1T_{k,j}.
 \tag{R.49}
\]
These retain all current terms.

Let
\[
 H=10d_a^2(1+A)(1+M)(1+S),\qquad
 \mathcal E_k=\exp\left(Hs_k+H\epsilon\sum_{r<k}h_rQ_r\right).
 \tag{R.50}
\]
Each equation uses \(Q_r\) in its own population.
For one bottom reverse-source block (R.46) gives
\[
 |J^1_{k,j}|\le d_a h_j+
 \sum_{r<k}h_r(\epsilon Q_r+d_a^2M)\max_{v\le r}|J^1_{v,j}|.
 \tag{R.51}
\]
For a middle reverse-source block the forcing is \(d_a A h_j\) and the coefficient is \(A(\epsilon Q_r+d_a^2M)\). For the whole middle forward-source row, summing (R.47) in \(j\) gives forcing one and the same coefficient. For the top row norms \(u_k=|J^3_{k\bullet}|_{\rm r}\), \(t_k=|T_{k\bullet}|_{\rm r}\), (R.48) gives
\[
 t_k\le d_a\sum_{r<k}h_ru_r,\qquad
 u_k\le1+\sum_{r<k}h_r(A\epsilon Q_r+d_a^2AS)
                                    \max_{v\le r}u_v.
 \tag{R.52}
\]
In the second inequality the inner readout sum is bounded by \(S\max_{v\le r}u_v\).

For a recursion \(x_k\le f+\sum_{r<k}h_r\ell_r\max_{v\le r}x_v\), its equality majorant is increasing and equals \(f\prod_{r<k}(1+h_r\ell_r)\). Induction and \(1+t\le e^t\) bound the original recursion by that product. The definition of \(H\) dominates every forcing prefactor and feedback coefficient in (R.51)–(R.52). Hence
\[
 |J^1_{k,j}|,\ |J^{2,\zeta}_{k,j}|\le Hh_j\mathcal E_k,\qquad
 |J^{2,\xi}_{k\bullet}|_{\rm r},\ |J^3_{k\bullet}|_{\rm r}
                                      \le H\mathcal E_k,
\]
\[
                         |T_{k\bullet}|_{\rm r}\le H^2\mathcal E_k.
 \tag{R.53}
\]
Feature derivatives are bounded by \(H^2\) times the same envelope and source-step factor. Equation (R.49) gives
\[
 |\partial_{\xi^\ell_\bullet}\delta^\ell_k|_{\rm r}
                  \le H^3(1+\epsilon Q_k)\mathcal E_k.
 \tag{R.54}
\]
The terminal multiplier is necessary: \(Q_k\) is absent from the sum defining \(\mathcal E_k\).

Convexity, without independence across times, gives
\[
 \exp\left(\theta\sum_{r<k}h_rQ_r\right)
 \le1-s_k/S+\sum_{r<k}(h_r/S)e^{\theta SQ_r}\qquad(\theta\ge0).
 \tag{R.55}
\]
The scalar inequality \(uQ\le Q^2/L_q^2+u^2L_q^2/4\) and (R.43) imply \(Ee^{uQ}\le2e^{u^2L_q^2/4}\). Consequently, for every fixed finite \(p\ge1\),
\[
 E\mathcal E_k^p\le2\exp(pHS+p^2H^2S^2L_q^2/4).
 \tag{R.56}
\]
Hölder controls the current multiplier too. In particular the explicit constant
\[
                     X=2(1+2K_q)\exp(HS+H^2S^2L_q^2)
 \tag{R.57}
\]
satisfies
\[
                    E\mathcal E_k\le X,\qquad
                    E[(1+Q_k)\mathcal E_k]\le X.
 \tag{R.58}
\]
Indeed apply (R.56) with \(p=2\), and
\(\|1+Q_k\|_2\le1+\sqrt2K_q\). The same calculation at higher exponents gives every fixed finite moment of \(\mathcal E_k\) and \((1+Q_k)\mathcal E_k\). No random time supremum occurs.

## R.7. Same-array derivative perturbation

Keep the deterministic arrays \(A,B\) fixed throughout this section. A superscript \({\rm af}\) means replacing \(G,V,L\) in (R.46)–(R.49) by \(aI,aI,0\) at these same arrays. It does not mean evaluation at the actual affine baseline arrays. These affine derivative solutions are deterministic and need no source coupling.

Subtract the middle affine equation from (R.47). The affine feedback is
\(a^2\sum_{r<k}A^2_{kr}\sum_{v\le r}B^3_{rv}(J_v-J_v^{\rm af})\).
The complete forcing is
\[
 \sum_{r<k}A^2_{kr}\left[
 (V_r-aI)I_r^\zeta+L_rJ_r
 +(V_r-aI)\sum_{v\le r}B^3_{rv}G_vJ_v
 +a\sum_{v\le r}B^3_{rv}(G_v-aI)J_v\right].
 \tag{R.59}
\]
For the bottom subtraction replace \(A^2_{kr}\) by \(h_rP_r\), \(B^3\) by \(B^2\), and take \(I_r^\zeta=I\mathbf1_{r=j}\); these substitutions in the displayed formula specify every term of that subtraction.

Let \(f=h_j\) for one reverse-source block, and \(f=1\) for a full forward-source row. Define
\[
                         W_k=1+\sum_{r<k}h_r(1+Q_r)\mathcal E_r.
 \tag{R.60}
\]
This is increasing. In the reverse-source case the first term of (R.59) occurs only at \(r=j\), with bound \(A\epsilon h_j\). The remaining derivatives vanish through time \(j\), and thereafter carry \(h_j\) by (R.53). Thus every contribution retains \(f\) for arbitrary unequal meshes. Using (R.45), (R.53), and \(\mathcal E_v\le\mathcal E_r\) for \(v\le r\), the total forcing is at most \(4H^4\epsilon fW_k\). For example the three nondirect coefficients are bounded by \(AH\), \(AMd_a H\), and \(AaMH\), all absorbed in \(4H^4\). The bottom has smaller coefficients since \(|P_r|\le1\le A\).

The affine feedback is bounded by \(H\sum_{r<k}h_r\max_{v\le r}|J_v-J_v^{\rm af}|\). Iteration with increasing forcing gives
\[
                    |J_k-J_k^{\rm af}|
                    \le4H^4 e^{HS}\epsilon fW_k.
 \tag{R.61}
\]
The notation denotes the relevant block or time-row norm. Passing to a feature derivative adds \((G_k-aI)J_k\), whose norm is at most \(H\epsilon f\mathcal E_k\).

The top subtraction consists of the exact equations
\[
 \Delta J_k=\sum_{r<k}A^3_{kr}
 [a\mathbf1\Delta T_r+(V_r-aI)\mathbf1T_r+L_rJ_r],
\]
\[
                  \Delta T_k=\sum_{r<k}h_rc_r^T
                                  [a\Delta J_r+(G_r-aI)J_r].
 \tag{R.62}
\]
Substitution of the second into the first bounds affine feedback by
\(a^2AS\sum_{r<k}h_r\max_{v\le r}|\Delta J_v|_{\rm r}\), which is at most the feedback used in (R.61). The direct remainder is bounded by \(A\epsilon\sum h_r(H^2+HQ_r)\mathcal E_r\). The additional remainder from substituting \((G-aI)J\) is at most \(aAS H\epsilon\sum h_r\mathcal E_r\). Their sum is below \(4H^4\epsilon W_k\). Thus (R.61) holds for top \(\Delta J\), with \(f=1\), and the second equation of (R.62) bounds \(\Delta T\).

Set
\[
                             D_1=20H^8e^{HS}.
 \tag{R.63}
\]
Using \(aS\le H\), (R.61)–(R.62) and feature multiplication show that each relevant preactivation, feature, or readout derivative difference is bounded by
\[
                         D_1\epsilon f(W_k+\mathcal E_k).
 \tag{R.64}
\]
For the middle backward output the exact derivative difference is
\[
 L_kJ_k+(V_k-aI)\sum_{v\le k}B^3_{kv}G_vJ_v
 +a\sum_{v\le k}B^3_{kv}(G_v-aI)J_v
 +a^2\sum_{v\le k}B^3_{kv}(J_v-J_v^{\rm af}).
 \tag{R.65}
\]
For the top output it is
\[
                 L_kJ_k+(V_k-aI)\mathbf1T_k+a\mathbf1\Delta T_k.
 \tag{R.66}
\]
The first terms have norm at most \(H\epsilon Q_k\mathcal E_k\) and retain the current returns. The other two direct middle terms sum to at most \(2H^3\epsilon\mathcal E_k\); the final middle term is at most \(a^2MD_1\epsilon(W_k+\mathcal E_k)\). The top remainder is bounded by the same common bound. Therefore
\[
 |\partial_{\xi^\ell_\bullet}\delta^\ell_k
     -\partial_{\xi^\ell_\bullet}\delta^{\ell,{\rm af}}_k|_{\rm r}
 \le10H^3D_1\epsilon[W_k+(1+Q_k)\mathcal E_k].
 \tag{R.67}
\]
Since \(EW_k\le1+SX\), (R.58) proves the expected derivative remainders with an explicit coefficient ready to absorb the learned-moment errors:
\[
             R_0=200H^{11}e^{HS}[1+(S+1)X]+m_0(1+S).
 \tag{R.68}
\]
Specifically, an expected feature derivative differs from its same-array affine derivative by at most \(R_0\epsilon h_j\) for one reverse-source block. The expected norm of a full backward derivative-row difference is at most \(R_0\epsilon\). Adding the learned forward or backward moment errors from (R.35) preserves these respective bounds, because the first summand of (R.68) already dominates all derivative remainders and its second summand dominates all moment errors.


## R.8. Deterministic coefficient stability

At arbitrary fixed bounded arrays denote the affine derivative of \(H^1_k\) with respect to \(\zeta^1_j\) by \(F_{k,j}\), of \(H^2_k\) with respect to \(\zeta^2_j\) by \(V^{\rm f}_{k,j}\), and of \(H^2_k\) with respect to \(\xi^2_j\) by \(U_{k,j}\). Use \(T_{k,j}\) for the affine derivative of \(C_k\) with respect to \(\xi^3_j\). The superscript distinguishes \(V^{\rm f}\) from the local diagonal gate matrix. Specializing the exact random derivative equations gives
\[
 F_{k,j}=a^2h_jP_j\mathbf1_{j<k}
       +a^2\sum_{r<k}h_rP_r\sum_{v\le r}B^2_{rv}F_{v,j},
 \tag{R.69}
\]
\[
 V^{\rm f}_{k,j}=a^2A^2_{kj}\mathbf1_{j<k}
       +a^2\sum_{r<k}A^2_{kr}\sum_{v\le r}B^3_{rv}V^{\rm f}_{v,j},
 \tag{R.70}
\]
\[
 U_{k,j}=aI\mathbf1_{k=j}
       +a^2\sum_{r<k}A^2_{kr}\sum_{v\le r}B^3_{rv}U_{v,j},
 \tag{R.71}
\]
\[
 T_{k,j}=ah_jc_j^T\mathbf1_{j<k}
       +a^2\sum_{r<k}h_rc_r^T\sum_{v<r}A^3_{rv}\mathbf1T_{v,j}.
 \tag{R.72}
\]
The last equation follows by substituting the top preactivation derivative
\(I\mathbf1_{k=j}+a\sum_{v<k}A^3_{kv}\mathbf1T_{v,j}\)
into the readout sum. The two affine backward outputs are \(a\mathbf1T_{k,j}\) and
\[
                             W_{k,j}=a\sum_{v\le k}B^3_{kv}U_{v,j}.
 \tag{R.73}
\]
The coefficient matrix \(A^2\) and scalar gain square \(a^2\) are distinct throughout these formulas.

Finite iteration gives explicit constants
\[
 K_F=a^2e^{a^2MS},\quad K_V=a^2Ae^{a^2AMS},\quad
 K_U=ae^{a^2AMS},\quad K_T=aSe^{a^2AS^2},
 \tag{R.74}
\]
such that
\[
 |F_{k,j}|\le K_Fh_j,\quad |V^{\rm f}_{k,j}|\le K_Vh_j,\quad
 |U_{k\bullet}|_{\rm r}\le K_U,\quad |T_{k\bullet}|_{\rm r}\le K_T.
 \tag{R.75}
\]
For \(F,V^{\rm f}\), the forcing prefactors are \(a^2h_j,a^2Ah_j\) and feedback coefficients \(a^2M,a^2AM\). For \(U\), the time-row forcing is \(a\) and its feedback coefficient \(a^2AM\). For \(T\), exchange the finite time sums in (R.72) to obtain \(t_k\le aS+a^2AS\sum_{v<k}h_vt_v\). Applying the finite-product identity to these four displayed scalar recursions proves (R.74).

Put a superscript 0 on these same deterministic systems at the actual affine baseline arrays. Combining (R.11)–(R.12), the same-array derivative comparison, and the learned moment comparison gives exact difference identities
\[
 \Delta A^2_{kj}=F_{k,j}-F^0_{k,j}+\eta^2_{kj},\qquad
 \Delta A^3_{kj}=V^{\rm f}_{k,j}-V^{\rm f,0}_{k,j}+\eta^3_{kj},
\]
\[
 \Delta B^3_{kj}=a\mathbf1(T_{k,j}-T^0_{k,j})+\nu^3_{kj},\qquad
 \Delta B^2_{kj}=W_{k,j}-W^0_{k,j}+\nu^2_{kj},
 \tag{R.76}
\]
where the quantities already bounded in Sections R.4 and R.7 satisfy
\[
                |\eta^\ell_{kj}|\le R_0\epsilon h_j,\qquad
                |\nu^\ell_{k\bullet}|_{\rm r}\le R_0\epsilon.
 \tag{R.77}
\]
These are derived remainders rather than assumptions on coefficient stability.

Define
\[
 \alpha^\ell_k=\max_{j<k}\frac{|\Delta A^\ell_{kj}|}{h_j},\qquad
 \beta^\ell_k=|\Delta B^\ell_{k\bullet}|_{\rm r},
\]
\[
                     E_k=\beta^2_k+\beta^3_k,\qquad
                     I_k=\sum_{r<k}h_rE_r.
 \tag{R.78}
\]
An empty maximum is zero. Each \(I_k\) uses only completed past rows and is nondecreasing.

For \(f^j_k=|F_{k,j}-F^0_{k,j}|/h_j\), subtract (R.69) and expand
\(B^2F-B^{2,0}F^0=\Delta B^2F+B^{2,0}\Delta F\).
The direct terms cancel because controls and steps are identical. Thus
\[
 f^j_k\le a^2K_F I_k+
                 a^2M_0\sum_{r<k}h_r\max_{v\le r}f^j_v.
 \tag{R.79}
\]
Finite iteration bounds the first term times \(e^{a^2M_0S}\). Set
\[
                         D_2=R_0+a^2K_Fe^{a^2M_0S}.
 \tag{R.80}
\]
Equations (R.76)–(R.77) give \(\alpha^2_k\le D_2(\epsilon+I_k)\).

For \(v^j_k=|V^{\rm f}_{k,j}-V^{\rm f,0}_{k,j}|/h_j\), expand the three factors in (R.70) as
\[
 A^2B^3V^{\rm f}-A^{2,0}B^{3,0}V^{\rm f,0}
 =\Delta A^2B^3V^{\rm f}
  +A^{2,0}\Delta B^3V^{\rm f}
  +A^{2,0}B^{3,0}\Delta V^{\rm f}.
\]
Using \(|\Delta A^2_{kr}|\le\alpha^2_kh_r\) and (R.75) gives
\[
 v^j_k\le a^2(1+MSK_V)\alpha^2_k+a^2A_0K_VI_k
           +a^2A_0M_0\sum_{r<k}h_r\max_{v\le r}v^j_v.
 \tag{R.81}
\]
The first feedback term, for example, is at most
\(a^2\alpha^2_k\sum_{r<k}h_rMK_V\).
It is a forcing term containing a current row already bounded at the preceding stage. Define
\[
 C_V=[a^2(1+MSK_V)D_2+a^2A_0K_V]e^{a^2A_0M_0S},
 \qquad D_3=R_0+C_V.
 \tag{R.82}
\]
Since \(\epsilon+I_r\le\epsilon+I_k\) for \(r\le k\), product iteration of (R.81) and (R.76) gives
\(\alpha^3_k\le D_3(\epsilon+I_k)\).

For \(t_k=|T_{k\bullet}-T^0_{k\bullet}|_{\rm r}\), the direct forcing in (R.72) cancels. Expanding its two factors yields
\[
 t_k\le a^2SK_T\sum_{r<k}h_r\alpha^3_r
                  +a^2A_0S\sum_{v<k}h_vt_v.
 \tag{R.83}
\]
Indeed
\(\sum_{r<k}h_r\sum_{v<r}h_vt_v
=\sum_{v<k}h_vt_v\sum_{v<r<k}h_r\le S\sum_{v<k}h_vt_v\).
Put
\[
                 C_T=a^2S^2K_TD_3e^{a^2A_0S^2},\qquad E_3=R_0+aC_T.
 \tag{R.84}
\]
Use \(\sum_{r<k}h_r(\epsilon+I_r)\le S(\epsilon+I_k)\) and product iteration in (R.83). Equations (R.76)–(R.77) then give
\(\beta^3_k\le E_3(\epsilon+I_k)\).
There is no current \(\alpha^3_k\) in the affine equation (R.83). The nonlinear remainder uses that current row only after it was bounded in the preceding stage.

For \(u_k=|U_{k\bullet}-U^0_{k\bullet}|_{\rm r}\), expansion of all three factors in (R.71) gives
\[
 u_k\le a^2MSK_U\alpha^2_k+a^2A_0K_UI_k
           +a^2A_0M_0\sum_{r<k}h_r\max_{v\le r}u_v.
 \tag{R.85}
\]
The direct source terms cancel. Define
\[
                   C_U=[a^2MSK_UD_2+a^2A_0K_U]e^{a^2A_0M_0S}.
 \tag{R.86}
\]
Then \(u_k\le C_U(\epsilon+I_k)\). Finally the exact current-row product (R.73) has expansion
\(a\Delta B^3_k U+aB^{3,0}_k(U-U^0)\), so
\[
 |W_{k\bullet}-W^0_{k\bullet}|_{\rm r}
             \le aK_U\beta^3_k+aM_0\max_{v\le k}u_v.
 \tag{R.87}
\]
The current \(B^3_k\) was just bounded; current \(U_k\) uses current \(A^2_k\) and only past \(B^3\). Set
\[
 E_2=R_0+aK_UE_3+aM_0C_U,\qquad
                  K_*=2\max\{1,D_2,D_3,E_2,E_3\}.
 \tag{R.88}
\]
The four successive bounds are
\[
 \alpha^2_k,\alpha^3_k,\beta^2_k,\beta^3_k\le K_*(\epsilon+I_k),
 \qquad E_k\le K_*\epsilon+K_*\sum_{r<k}h_rE_r.
 \tag{R.89}
\]
Every constant is now a specified finite function of \((a,B,S)\).

## R.9. Chronological closure and explicit amplitude selection

Take
\[
 \epsilon_*(a,B,S)=
 \min\left\{1,\frac{B}{2T_0},
                  \frac{1}{2K_*\exp(K_*S)}\right\}.
 \tag{R.90}
\]
The finite constant chain is (R.18), (R.28), (R.34), (R.36)–(R.37), (R.42), (R.50), (R.57), (R.68), (R.74), and (R.80)–(R.88). Thus the number is positive and chosen before the mesh, controls, cap, or covariance.

The prefix assumptions close by induction through the actual query stages, rather than a simultaneous assumption on unknown current rows. Suppose all four coefficient rows at times \(r<k\) obey the bounds \((A,M)\) and
\[
                       E_r\le K_*\epsilon\prod_{v<r}(1+K_*h_v).
 \tag{R.91}
\]
The telescoping product identity gives
\[
 \epsilon+I_k
 \le\epsilon\left[1+\sum_{r<k}K_*h_r
                         \prod_{v<r}(1+K_*h_v)\right]
 =\epsilon\prod_{r<k}(1+K_*h_r)
 \le\epsilon e^{K_*S}.
 \tag{R.92}
\]

First construct \(A^2_k\). Its bottom coordinates and reverse-source derivative paths use only \(q^1_r,B^2_r\) with \(r<k\). Equations (R.38), (R.46), and (R.59) therefore establish its remainder before any bound on a new backward row is needed. Equations (R.79)–(R.80) and (R.90)–(R.92) give \(\alpha^2_k\le1/2\), so
\(|A^2_{kj}|\le(A_0+1/2)h_j<Ah_j\).

Next construct \(A^3_k\). The just-bounded \(A^2_k\) constructs \(Z^2_k,H^2_k\), and their reverse-source derivative paths use \(q^2_r,B^3_r\) only for \(r<k\). Equations (R.39), (R.47), and (R.59) give the remainder, and (R.81)–(R.82) yield \(\alpha^3_k\le1/2\). No bound on current \(q^2_k\) was used.

Then construct \(B^3_k\). The available \(C_k,Z^3_k\), their moments, and their derivative paths use \(A^3\) through the current time, now bounded, and no backward rows. Equations (R.40), (R.48), and (R.62), (R.66) provide this remainder; (R.83)–(R.84) give \(\beta^3_k\le1/2\). Hence its row norm is less than \(M\). This new row defines \(q^2_k\), which is bounded from its already constructed middle features by (R.39).

Finally construct \(B^2_k\). Current \(q^2_k,B^3_k\) now satisfy all bounds required for (R.49), (R.65). Equations (R.85)–(R.88) give \(\beta^2_k\le1/2\), hence its row norm is less than \(M\). Only now is current \(q^1_k\) defined and bounded by (R.38). The second inequality in (R.89), with (R.92), proves (R.91) at the new time. All learned moments at every stage were already bounded independently by Section R.4.

At \(k=0\) the forward rows are empty. Because \(C_0=0\), the top delta and its forward-source derivatives vanish; the source covariance of \(\zeta^2_0\) and the coefficient \(B^3_0\) are therefore zero. Thus \(q^2_0=\delta^2_0=0\), and the same computation gives \(B^2_0=0,q^1_0=0\). This starts the induction while retaining all separately named formal source arguments at zero variance.

For completeness the actual current-return blocks are
\[
                 (B^3_{kk})_{ij}=\mathbf1_{i=j}E(L^3_k)_{ii},
 \tag{R.93}
\]
\[
 (B^2_{kk})_{ij}=\mathbf1_{i=j}E(L^2_k)_{ii}
       +(B^3_{kk})_{ij}E[(V^2_k)_{ii}(G^2_k)_{jj}].
 \tag{R.94}
\]
Indeed \(\partial_{\xi^3_k}Z^3_k=I\) and \(\partial_{\xi^3_k}C_k=0\), giving (R.93). In the middle, \(\partial_{\xi^2_k}Z^2_k=I\) and \(\partial_{\xi^2_k}q^2_k=B^3_{kk}G^2_k\); the chain rule gives (R.94), including its column index \(j\) on \(G^2_k\). Equations (R.45) and (R.41) bound both current blocks by a constant times \(\epsilon\). They are diagonal for this explicit Euler schedule, while earlier blocks can be full. Their off-diagonal zeros are consequences of these formal derivatives, not consequences of sample independence. No current block was omitted or inverted.

The induction proves (R.8) and the quantitative stability estimate
\[
 \max_{\ell,k,j<k}\frac{|A^\ell_{kj}-A^{\ell,0}_{kj}|}{h_j}
 +\max_{\ell,k}|B^\ell_{k\bullet}-B^{\ell,0}_{k\bullet}|_{\rm r}
                  \le2K_*e^{K_*S}\epsilon.
 \tag{R.95}
\]
The coordinate argument now applies to the whole program. Thus (R.9) holds with \(K=K_q\). The same proof bounds all displayed forward fields and deltas by finite multiples of \(\sqrt p\). Equations (R.53)–(R.58) additionally give absolute expected response bounds
\[
 E|\partial_{\zeta^{\ell-1}_j}H^{\ell-1}_k|
       \le H^2Xh_j,\qquad
 E|\partial_{\xi^\ell_\bullet}\delta^\ell_k|_{\rm r}
       \le H^3X,\qquad\ell=2,3.
 \tag{R.96}
\]

The only advanced theorem used in this part is internal Lemma F, in the precise form stated in Section R.1. The remaining estimates use finite induction, elementary Gaussian integration, Cauchy–Schwarz, Hölder, the displayed rank-one inequality, finite products, and convexity. The affine hypothesis must be verified in the global-control argument. This part's conclusions concern every finite cap; their transfer to continuous trajectories and removal of caps belong to the subsequent dynamical argument.
