# Fixed-cap empirical hidden-velocity bridge

Status: proved under the compact-interval primal bounds and the fixed-program/common-action and raw-Hilbert local-Lipschitz premises specified below. Constants depend on the fixed cap. This proves neither cap removal nor an all-angle activation theorem.

The solve-math-rigorously skill was read in full. The three requested documents were read in full. The finite Gaussian conditioning and common-action sections, and the hidden-velocity discussion, of `L3_LOCAL_COMPLETE_PROOF.md` were also inspected. No experiment, agent, or modification of an existing file is used.

## 1. Statement, assumptions, and proof structure

Fix \(T<\infty\), \(R>0\), and \(0\le e\le1\). The same argument works for any fixed finite \(e\ge0\), with \(1+e\) replacing the bound 2. Set

\[
 \phi(z)=1+z+e\arctan z,\qquad
 d(z)=\phi'(z),\qquad
 D(z,q)=q+e(1+z^2)^{-1}\tau_R(q).
 \tag{1}
\]

Use precisely the smooth clip in `TWO_SAMPLE_SOURCE_BASELINE.md`:

\[
 |\tau_R(q)|\le\min(|q|,2R),\quad |\tau_R'|\le1,
 \quad \tau_R(q)=q\quad (|q|\le R).
\]

In particular, for a numerical constant \(c\),

\[
 |\phi(z)|\le c+2|z|,\quad |d|\le2,\quad |d'|\le c,
 \quad |D(z,q)|\le2|q|,\quad
 |D_z|\le2eR,\quad |D_q|\le2.                 \tag{2}
\]

All coordinate derivatives used below are continuous. Only the displayed first-derivative bounds on \(D\) are needed.

The state is \(\theta=(w,W_2,W_3,C)\), with matrix increments measured in Hilbert--Schmidt norm around their bounded initial actions. Its difference norm is

\[
 \|\Delta\theta\|_{\mathcal X}
 =\sqrt d\,\|\Delta w\|_2+
   \|\Delta W_2\|_{\rm HS}+\|\Delta W_3\|_{\rm HS}
   +\|\Delta C\|_2.                              \tag{3}
\]

At width \(n\), the first term is \(\sqrt{d/n}\|\Delta W^{(1)}\|_F\), the two matrix terms are ordinary Frobenius norms, and vector norms are \(\|v\|_n=(n^{-1}\sum_i v_i^2)^{1/2}\). A rank-one action is \(u\otimes_n v=uv^T/n\). Population expectations and norms always belong to the indicated neuron population; populations are never paired coordinatewise.

We use the two-sample **physical** vector field \(F_R\). Write

\[
 p_a(\theta)=y_a-f_a(\theta),\qquad f_a=\langle C,H^3_a\rangle,
 \quad \rho_{ab}=x_a^Tx_b/d.
\]

Its four components are

\[
 F_w=\sum_b p_b\delta^1_b x_b/d,\qquad
 F_{W_\ell}=\sum_b p_b\delta^\ell_b\otimes H^{\ell-1}_b
 \quad(\ell=2,3),\qquad
 F_C=\sum_b p_b H^3_b,                            \tag{4}
\]

where \(Z^1_a=w\cdot x_a\), \(Z^\ell_a=W_\ell H^{\ell-1}_a\), \(H^\ell_a=\phi(Z^\ell_a)\), and

\[
 \delta^3_a=D(Z^3_a,C),\quad
 q^2_a=W_3^*\delta^3_a,\quad \delta^2_a=D(Z^2_a,q^2_a),\quad
 q^1_a=W_2^*\delta^2_a,\quad \delta^1_a=D(Z^1_a,q^1_a).
 \tag{5}
\]

Thus the two finite residuals are recomputed, individually, at every raw Euler node. No finite scalar clock or sample symmetry is assumed. “Fixed-cap GF” below means the flow of (4); with the auxiliary caps it need not be the gradient of the original loss.

The premises supplied in the question are used in the following exact form.

1. The population flow of (4) exists on \([0,T]\), on the common generated action spaces, with a finite bound on \(\sqrt d\|w\|_2,\|W_2\|_{\rm op},\|W_3\|_{\rm op},\|C\|_2\). Alternatively, a uniformly bounded population Euler family and its strong raw-state limit suffice. Initial roots and normalizations are those of the contract, so the population \(C_0\) is zero.
2. On a larger primal ball the raw field is bounded and Lipschitz in (3), with constants independent of width, at this fixed \(R\). These facts also follow from (2), the bounded actions, and rank-one norm inequalities. The corresponding statement with additive errors at intermediate matrix answers holds by the same finite composition of Lipschitz maps.
3. At every fixed finite mesh, the joint empirical \(\mathcal W_2\) law and formal source rule of Section 3 of `TWO_SAMPLE_SOURCE_BASELINE.md` hold, including deterministic feedback contractions, additional independent roots, singular Gaussian covariances, both matrices, and both orientations. The initial actions are bounded on the common generated \(L^2\) spaces. We use **only** their \(L^2\to L^2\) bound.

The fixed-program premise concerns bounded-derivative coordinate instructions. Section 5 explicitly extends it to the velocity queries needed here; it is not assumed for those unbounded-derivative products.

Let \(B\ge1\) bound the supplied population primal sizes. Here and below \(K\) denotes a finite constant depending on \(B,R,e,T,d,x_1,x_2,y_1,y_2\), enlarged a finite number of times. It never depends on a mesh, its smallest step, width, a source covariance condition number, or a moment exponent. Primal constants can be enlarged before choosing sufficiently fine meshes.

Under these premises:

- Population Euler node fields and hidden preactivation/feature velocities satisfy \(\sup_{\pi,k,a}\|X^\pi_{k,a}\|_{L^p}\le K\sqrt p\), \(p\ge2\), for every field \(X\) in (5), every forward field, \(C\), and each hidden velocity. The same bound holds with \(\sup_{t\le T}\) for the population flow.
- Fixed-cap finite GF, and raw Euler with any deterministic step tending to zero (in particular \(n^{-2}\)), have the same limiting joint empirical laws of these fields and velocities. Marginal \(\mathcal W_2\) convergence is uniform in physical time; joint laws at any fixed finite collection of times converge in \(\mathcal W_2\), retaining both samples in each layer.
- For \(\mathcal T_u(X)=\|(|X|-u)_+\|_2\), the corresponding empirical tail norms converge uniformly in time to the population tail norms, for each fixed \(u\ge0\). In particular the squared velocity tails are uniformly integrable in the width-limit sense made precise in Section 8. Squared speeds and their integrals converge.

The proof first bounds expected source rows by nonlinear Gaussian probes. An indexed causal estimate then gives pathwise derivative bounds and population moments. Two additional forward queries give the hidden-velocity moments. Finally an asymmetric, deterministic velocity comparison transfers raw-state Euler error to hidden velocities using only reference tails.

## 2. Nonlinear probes and the actual coefficient bounds

Let \(0=t_0<\cdots<t_N=T\), \(h_j=t_{j+1}-t_j\). Freeze all scalar population contractions causally, including \(p_{j,b}=y_b-f_b(\theta_j)\). The source representation is the baseline representation with \(c_b\) replaced in every learned update by \(p_{j,b}\):

\[
 Z^1_{k,a}=Z^1_{0,a}+\sum_{j<k,b}h_jp_{j,b}\rho_{ab}\delta^1_{j,b},
 \qquad C_k=\sum_{j<k,b}h_jp_{j,b}H^3_{j,b},        \tag{6}
\]
\[
 Z^\ell_{k,a}=\xi^\ell_{k,a}
       +\sum_{j<k,b}A^\ell_{ka,jb}\delta^\ell_{j,b},\qquad
 q^{\ell-1}_{k,a}=\zeta^{\ell-1}_{k,a}
       +\sum_{j\le k,b}D^\ell_{ka,jb}H^{\ell-1}_{j,b},
 \quad \ell=2,3,                                 \tag{7}
\]
\[
 A^\ell_{ka,jb}
 =E_{\ell-1}\partial_{\zeta^{\ell-1}_{j,b}}H^{\ell-1}_{k,a}
   +h_jp_{j,b}E_{\ell-1}[H^{\ell-1}_{k,a}H^{\ell-1}_{j,b}],
 \quad j<k,                                      \tag{8}
\]
\[
 D^\ell_{ka,jb}
 =E_\ell\partial_{\xi^\ell_{j,b}}\delta^\ell_{k,a}
   +\mathbf1_{j<k}h_jp_{j,b}E_\ell[\delta^\ell_{k,a}\delta^\ell_{j,b}].
 \tag{9}
\]

Derivatives mean partial derivatives of the displayed finite scalar expressions, with **all** scalar contractions, response coefficients, and covariance parameters held fixed. Their named arguments are distinct even at a singular covariance. The four source groups, and the roots, have the independence and full cross-sample/time covariances stated in the baseline. In particular each source variance is the squared \(L^2\) norm of its actual matrix input. The primal bound and (2) bound these variances by \(K\), and bound \(\sum_b|p_{j,b}|\) by \(K\).

Here is a probe proof for the nonlinear coefficients, including their past-time step factors. Choose one of the four answer/source groups and a new iid standard Gaussian vector \(g\) in that answer's population, independent of the original network. At the selected answer \((j,b)\), insert \(\varepsilon\alpha_{j,b}g\), \( |\alpha_{j,b}|\le1\). Both residuals and every subsequent state update are recomputed in this perturbed finite program.

On the primal ball, a simultaneous error at the two answer slots of a time changes the evaluated raw field by at most \(K|\varepsilon|\|g\|_n\). Lipschitz stability therefore gives, for the state discrepancy,

\[
 e_{k+1}\le(1+Kh_k)e_k+Kh_k|\varepsilon|\|g\|_n.
 \tag{10}
\]

If only time \(j\) is forced, the inhomogeneous term occurs only at \(j\), so \(e_k\le Kh_j|\varepsilon|\|g\|_n\) for \(k>j\). With all times forced, \(e_k\le K|\varepsilon|\|g\|_n\). Every primary query \(V_k\) is Lipschitz as a function of state and the current answer errors. Consequently its discrepancy obeys the same all-time bound; an individual strictly past answer gives the sharper \(Kh_j|\varepsilon|\|g\|_n\). A current answer gives \(K|\varepsilon|\|g\|_n\). These constants include the residual feedback. A fixed sufficiently small \(|\varepsilon|\), on \(\|g\|_n\le2\), keeps the perturbed program inside a larger ball by first-exit induction in (10).

At fixed mesh and fixed \(\varepsilon\), the finite-program law with this additional root gives

\[
 \langle g,V_n^\varepsilon\rangle_n\longrightarrow E[G V^\varepsilon].
 \tag{11}
\]

In its scalar description \(G\sim N(0,1)\) is independent of all Gaussian source groups and the original roots. Coefficients and covariances depend on \(\varepsilon\), but are deterministic. The only explicit appearances of \(G\) are the inserted answer additions. With that coefficient list fixed, the chain rule gives

\[
 \partial_G V^\varepsilon
 =\varepsilon\sum_{j,b}\alpha_{j,b}
                  \partial_{\eta_{j,b}}V^\varepsilon,
 \qquad
 E[G V^\varepsilon]
 =\varepsilon\sum_{j,b}\alpha_{j,b}
                  E\partial_{\eta_{j,b}}V^\varepsilon.       \tag{12}
\]

For the second identity, condition on all other sources and roots and integrate against the one-dimensional Gaussian density. A fixed finite primary scalar expression is Lipschitz with a deterministic constant after its coefficients are frozen. Thus it has at most linear growth in \(G\), its derivative is bounded, and the boundary term in integration by parts vanishes. Integrability permits averaging over the other variables. Affinity of the coordinate instructions is unnecessary.

At this fixed mesh,

\[
 E\partial_{\eta_{j,b}}V^\varepsilon
       \longrightarrow E\partial_{\eta_{j,b}}V^0.          \tag{13}
\]

To justify (13), induct in the finite chronological query order. Covariances are second moments of already constructed inputs, so vary continuously when those inputs converge in \(L^2\). Realize the finite Gaussian tuples through their positive-semidefinite covariance square roots; continuity of these square roots includes rank drops. Each next frozen scalar expression and its first derivatives are continuous functions of the earlier coefficient list and Gaussian arguments. On a small compact neighborhood of that finite coefficient list, the bounded coordinate derivatives give a deterministic bound for each of its finitely many formal first derivatives. Dominated convergence passes the expected derivatives; linear growth and Gaussian second moments pass the next covariances and learned contractions. Physical residuals are continuous second-moment contractions of existing forward/readout fields. No covariance derivative or covariance inverse occurs in this induction.

Conditioned on the original network, \(\langle g,V_n^0\rangle_n\) is centered Gaussian of variance \(\|V_n^0\|_n^2/n\), hence tends to zero in probability. Apply Cauchy--Schwarz to the finite discrepancy estimate following (10), use (11)--(12), take \(n\to\infty\) first, and then use (13) to send \(\varepsilon\to0\). This proves

\[
 \left|\sum_{j,b}\alpha_{j,b}E\partial_{\eta_{j,b}}V_k\right|\le K.
 \tag{14}
\]

Selecting the deterministic signs of the expected derivatives bounds the sum of their absolute expectations. Selecting a single strictly past source gives \(Kh_j\). Selecting a current source gives \(K\). This argument applies separately to every output/source population pairing needed in (8)--(9); an unrelated population is never paired with \(g\).

Cauchy--Schwarz bounds the learned contractions in (8)--(9). Therefore, for both \(\ell=2,3\), both samples \(a,b\in\{1,2\}\), every mesh, and every admissible index,

\[
 |A^\ell_{ka,jb}|\le Kh_j\quad(j<k),\qquad
 |D^\ell_{ka,jb}|\le Kh_j\quad(j<k),\qquad
 |D^\ell_{ka,kb}|\le K.                           \tag{15}
\]

For completeness, the actual current blocks remain those in the baseline. With \(a^\ell_{k,a}=D_z(Z^\ell_{k,a},m^\ell_{k,a})\), \(v^\ell_{k,a}=D_q(Z^\ell_{k,a},m^\ell_{k,a})\), and \(m^1=q^1,m^2=q^2,m^3=C\),

\[
 D^3_{ka,kb}=\mathbf1_{a=b}E a^3_{k,a},\qquad
 D^2_{ka,kb}=\mathbf1_{a=b}E a^2_{k,a}
       +D^3_{ka,kb}E[v^2_{k,a}d(Z^2_{k,b})].       \tag{16}
\]

Indeed \(C_k\) and each forward learned correction use strictly earlier times; each current forward preactivation contains only its own current forward source. This gives (16) by differentiating the two current backward gates in order. Physical residuals are frozen scalars and do not alter it. In particular no current block is incorrectly treated as zero, and no invertibility assumption on the two-sample covariance is used.

## 3. An all-index causal estimate

This section upgrades (15) to pathwise derivative bounds and primary moments. It does **not** equate \(|E\partial V|\) with \(E|\partial V|\).

For a scalar field in population \(l\), let

\[
 \mathcal R(F)=\sum_{\eta\text{ in population }l}|\partial_\eta F|,
 \tag{17}
\]

where the finite sum includes every named primary Gaussian source through \(N\) in that population:

\[
 l=1:\ \zeta^1;\qquad l=2:\ (\xi^2,\zeta^2);\qquad l=3:\ \xi^3.
\]

Future derivatives vanish. Initial-root derivatives need not be included; including them merely changes the constant term below. All deterministic coefficients are fixed in (17). The seminorm obeys subadditivity, \(\mathcal R(H^l)\le2\mathcal R(Z^l)\), and

\[
 \mathcal R(\delta^l)\le 2eR\,\mathcal R(Z^l)+2\mathcal R(m^l).
 \tag{18}
\]

To see every time and sample index in the estimate, set \(z^l_{k,a}=\mathcal R(Z^l_{k,a})\), \(u^l_{k,a}=\mathcal R(H^l_{k,a})\), \(b^l_{k,a}=\mathcal R(\delta^l_{k,a})\), \(v^i_{k,a}=\mathcal R(q^i_{k,a})\), and \(c_k=\mathcal R(C_k)\). Equations (6)--(7) and (15) give the following deterministic inequalities, pointwise on the scalar probability space:

\[
\begin{aligned}
 z^1_{k,a}&\le K\sum_{j<k}h_j\sum_b b^1_{j,b},\\
 z^2_{k,a}&\le1+K\sum_{j<k}h_j\sum_b b^2_{j,b},\\
 z^3_{k,a}&\le1+K\sum_{j<k}h_j\sum_b b^3_{j,b},\\
 c_k&\le K\sum_{j<k}h_j\sum_b u^3_{j,b},\\
 u^l_{k,a}&\le2z^l_{k,a},\\
 v^i_{k,a}&\le1+K\sum_bu^i_{k,b}
                    +K\sum_{j<k}h_j\sum_bu^i_{j,b}quad(i=1,2),\\
 b^i_{k,a}&\le2eR z^i_{k,a}+2v^i_{k,a}\quad(i=1,2),\\
 b^3_{k,a}&\le2eR z^3_{k,a}+2c_k.
\end{aligned}                                                   \tag{19}
\]

All quantities at a fixed time on the right of a current transpose bound are **forward** fields already determined at that time. There is no same-time implicit system to invert.

Here is the scalar reduction proving that (19) is mesh-uniform. Let \(U_k\) be the maximum of \(c_k\) and the six \(z^l_{k,a}\). The last four lines bound every \(u,v,b\) at time \(k\) by

\[
 K\left(1+U_k+\sum_{j<k}h_jU_j\right).
\]

Insert this into the first four lines. The double sum obeys

\[
 \sum_{j<k}h_j\sum_{i<j}h_iU_i
 =\sum_{i<k}h_iU_i\sum_{i<j<k}h_j
 \le T\sum_{i<k}h_iU_i.
\]

It follows that \(U_k\le K+K\sum_{j<k}h_jU_j\), after incorporating \(1+T\) into \(K\). For this last inequality, induction gives

\[
 U_k\le K\prod_{j<k}(1+Kh_j)\le K e^{KT}.
\]

Returning to all the lines of (19) proves the pathwise bound

\[
 \mathcal R(F_{k,a})\le K                         \tag{20}
\]

for every primary scalar field and \(C\), simultaneously in the finite indices. In particular (20) bounds \(E\sum|\partial F|\), not only a signed expected row.

Exactly the same indexed estimate proves primary moment bounds. For \(p\ge2\), substitute \(\|F\|_{L^p}\) for each derivative seminorm in (19). The root \(Z^1_{0,a}\) and each Gaussian source have \(L^p\) norm at most \(K\sqrt p\), since their variances are bounded by the primal assumption. Replace each direct 1 by \(K\sqrt p\), use \(\|H\|_p\le c+2\|Z\|_p\), and use \(\|\delta^l\|_p\le2\|m^l\|_p\). The latter is stronger than the corresponding inequality in (19). The same scalar reduction gives

\[
 \sup_{\pi,k,a}\|F^\pi_{k,a}\|_{L^p}\le K\sqrt p,
 \qquad p\ge2,                                  \tag{21}
\]

for all primary fields. This uses source representations of the actual inputs and Minkowski's inequality for finite sums. It contains no \(L^p\to L^p\) assertion about a Gaussian matrix action.

## 4. The two hidden-velocity queries and their response rows

At a population Euler node define the *instantaneous* physical preactivation and feature velocities by evaluating the chain rule in direction \(F_R(\theta_k)\):

\[
\begin{aligned}
 P^1_{k,a}&=\sum_b p_{k,b}\rho_{ab}\delta^1_{k,b},
 &U^1_{k,a}&=d(Z^1_{k,a})P^1_{k,a},\\
 P^2_{k,a}&=\sum_b p_{k,b}\delta^2_{k,b}
                       E_1[H^1_{k,b}H^1_{k,a}]+J^2_{k,a},
 &J^2_{k,a}&=W_{2,k}U^1_{k,a},\\
 U^2_{k,a}&=d(Z^2_{k,a})P^2_{k,a},\\
 P^3_{k,a}&=\sum_b p_{k,b}\delta^3_{k,b}
                       E_2[H^2_{k,b}H^2_{k,a}]+J^3_{k,a},
 &J^3_{k,a}&=W_{3,k}U^2_{k,a},\\
 U^3_{k,a}&=d(Z^3_{k,a})P^3_{k,a}.
\end{aligned}                                                    \tag{22}
\]

Here \(P^l=\dot Z^l\) and \(U^l=\dot H^l\) at a flow state. The derivatives of the forward activation in (22) are the actual \(d=\phi'\), not a capped backward gate.

Append these observational queries **after the complete primary training transcript**: first all \(W_{2,0}U^1_{k,a}\) queries, and then all \(W_{3,0}U^2_{k,a}\) queries, with the learned rank increments added explicitly. They never feed back into training. Source derivatives with respect to times later than \(k\) vanish, so the initial-matrix response correction only contains \(j\le k\), even in this appended order. No primary coefficient is altered by adjoining an unused observation.

The initial-action source rule and exact rank unrolling give

\[
 J^\ell_{k,a}=\gamma^\ell_{k,a}
      +\sum_{j\le k,b}E^\ell_{ka,jb}\delta^\ell_{j,b},
 \quad \ell=2,3,                                \tag{23}
\]
\[
 E^\ell_{ka,jb}
 =E_{\ell-1}\partial_{\zeta^{\ell-1}_{j,b}}U^{\ell-1}_{k,a}
   +\mathbf1_{j<k}h_jp_{j,b}
                         E_{\ell-1}[H^{\ell-1}_{j,b}U^{\ell-1}_{k,a}].
 \tag{24}
\]

The centered Gaussian \(\gamma^\ell_{k,a}\) belongs to the forward source group of matrix \(\ell\). Its variance is \(E_{\ell-1}|U^{\ell-1}_{k,a}|^2\); its covariance with another forward query is the second moment of their two inputs. It is formally a new forward-source argument, independent of the opposite source group. It need not be independent of old sources in its own forward group. Section 5 verifies (23)--(24) for these products from the bounded-derivative finite-program premise.

For the bottom query, (20) and (22), with \(p_{k,b}\) held fixed, imply

\[
 \mathcal R(P^1_{k,a})\le K,\qquad
 \mathcal R(U^1_{k,a})
 \le c|P^1_{k,a}|\mathcal R(Z^1_{k,a})+2\mathcal R(P^1_{k,a})
 \le K\left(1+\sum_b|q^1_{k,b}|\right).           \tag{25}
\]

Thus the absolute response row in (24) for \(\ell=2\) is at most \(K\), by \(\sum|E\partial U|\le E\mathcal R(U)\) and (21) at \(p=2\). The learned row is at most \(K\sum_{j<k}h_j\le K\), by Cauchy--Schwarz and the primal/velocity \(L^2\) bounds. Also \(\|U^1\|_p\le K\sqrt p\). Consequently (23), (21), and the Gaussian variance formula give

\[
 \sum_{j\le k,b}|E^2_{ka,jb}|\le K,
 \quad \|J^2_{k,a}\|_p+\|P^2_{k,a}\|_p+\|U^2_{k,a}\|_p
 \le K\sqrt p.                                  \tag{26}
\]

For the second new query, differentiate (23) for \(J^2\) only with respect to the primary population-2 transpose sources \(\zeta^2\). With coefficients and the new forward source \(\gamma^2\) fixed, (20) and the coefficient row in (26) yield

\[
 \sum_{j,b}|\partial_{\zeta^2_{j,b}}J^2_{k,a}|\le K,
 \qquad
 \sum_{j,b}|\partial_{\zeta^2_{j,b}}P^2_{k,a}|\le K.
 \tag{27}
\]

The other term in \(P^2\) is a bounded deterministic linear combination of the current \(\delta^2\) fields, so its derivative is covered by (20). Therefore

\[
 \sum_{j,b}|\partial_{\zeta^2_{j,b}}U^2_{k,a}|
 \le K(1+|P^2_{k,a}|).                           \tag{28}
\]

Equations (24), (26), and (28) bound the response and learned rows for \(\ell=3\) by \(K\). A second application of (23) gives

\[
 \sum_{j\le k,b}|E^3_{ka,jb}|\le K,\qquad
 \sup_{\pi,k,a,l}
    \bigl(\|P^l_{k,a}\|_p+\|U^l_{k,a}\|_p\bigr)\le K\sqrt p.
 \tag{29}
\]

In particular the reference node fourth moments are uniformly bounded at fixed cap. Both reused forward actions have been identified with their Gaussian sources **and** their expected-response-weighted old transpose inputs.

## 5. Justification of the appended product queries

The map \((z,P)\mapsto d(z)P\) is continuous of linear growth, but not globally Lipschitz. The fixed-program theorem must not be applied directly to it.

First use \(U_M=d(Z)\tau_M(P)\), with a smooth clip having the properties in (1) at level \(M\). For fixed \(M\), this coordinate instruction is globally Lipschitz with bounded continuous first derivatives. It is admissible in the supplied finite-program rule.

For the bottom query, the primary joint empirical \(\mathcal W_2\) limit gives the joint limit of \((Z^1,P^1,U^1)\): if \((z_n,p_n)\to(z,p)\) in \(L^2\) under a coupling, then

\[
 \|d(z_n)p_n-d(z)p\|_2
 \le2\|p_n-p\|_2+\|(d(z_n)-d(z))p\|_2\longrightarrow0.
 \tag{30}
\]

The last limit follows by truncating the fixed \(L^2\) variable \(p\), using boundedness of \(d\) on the discarded part, and its Lipschitz bound on the bounded part. This proves the asserted preservation of \(\mathcal W_2\) without a higher empirical moment assumption. The continuous linear-growth tail function \(|P|\mathbf1_{|P|>M}\) can be bounded using \(2(|P|-M/2)_+\), so primary \(\mathcal W_2\) convergence also gives

\[
 \lim_{M\to\infty}\limsup_{n\to\infty}
  \mathbb P(\|U^1_{n,M}-U^1_n\|_n>\varepsilon)=0
 \quad(\varepsilon>0).                          \tag{31}
\]

Here and throughout the width limit is at a fixed finite mesh. A bounded matrix action in normalized \(L^2\) transfers (31) to \(W_{2,k}U^1_{n,M}\). The same \(L^2\to L^2\) bound gives convergence of the population actions as \(M\to\infty\).

It remains to identify the limit of the coefficients, not merely the action. Differentiating the truncated expression gives

\[
 \partial_\eta[d(Z)\tau_M(P)]
 =d'(Z)\tau_M(P)\partial_\eta Z
      +d(Z)\tau_M'(P)\partial_\eta P.             \tag{32}
\]

The sum of the absolute derivatives in (32) is dominated by

\[
 c|P|\mathcal R(Z)+2\mathcal R(P).
\]

For the bottom query this has finite expectation by (20)--(21); for the middle query the required \(\zeta^2\) rows are bounded by (20), (26)--(27). At a fixed mesh, \(\tau_M(P)\to P\) and \(\tau_M'(P)\to1\) pointwise. Dominated convergence proves convergence of every expected source derivative in (24), including at degenerate source laws. Learned contractions converge by \(L^2\) convergence. The new Gaussian source covariances converge because their input second moments do; finite covariance square-root coupling then passes the full scalar formula to (23).

This argument also justifies the second appended query rigorously in order. After the bottom query has been adjoined, its joint law with the entire primary transcript converges in \(\mathcal W_2\). Thus \(P^2\), a sum of that query and primary fields with converging scalar contractions, has a joint \(\mathcal W_2\) limit. For a fixed outer clip \(M\), \((Z^2,P^2)\mapsto d(Z^2)\tau_M(P^2)\) is Lipschitz. One may first truncate the bottom query, apply the original finite-program theorem, and then remove that inner truncation in \(L^2\). The derivative formula (23) for \(J^2\) shows that its \(\zeta^2\) derivative rows converge and stay bounded as the inner truncation is removed: its coefficients converge, its primary delta derivatives obey (20), and its new forward source has formal \(\zeta^2\) derivative zero. Formula (32) then permits removal of the outer truncation. This proves (23)--(24) for both actions, and their joint empirical \(\mathcal W_2\) laws, without a circular assumption about velocity moments.

All finitely many time/sample observations may be treated together. Covariances of their added sources use the full input cross moments. Truncation never identifies sources that merely happen to agree on the support of a singular Gaussian law.

## 6. A deterministic velocity comparison using reference tails

This estimate is valid in a finite normalized space or a population space. Let \(\theta,\bar\theta\) be two states in a primal ball with the same initial actions. Let \(v,\bar v\) be two raw directions of bounded \(\mathcal X\) norm. Denote their state and direction discrepancies by

\[
 a=\|\theta-\bar\theta\|_{\mathcal X},\qquad
 b=\|v-\bar v\|_{\mathcal X}.
\]

Evaluate forward fields at their respective states and define \(P^l(\theta,v),U^l(\theta,v)\) by

\[
 P^1_a=v_w\cdot x_a,\qquad U^1_a=d(Z^1_a)P^1_a,\qquad
 P^l_a=v_{W_l}H^{l-1}_a+W_lU^{l-1}_a,\qquad
 U^l_a=d(Z^l_a)P^l_a\quad(l=2,3).
\]

Use a bar for the second evaluation. All these \(L^2\) norms are bounded by a primal/direction-dependent constant. Let

\[
 \mathcal T_M(X)=\|(|X|-M)_+\|_2 .
\]

For every \(M\ge1\), every sample, and every layer,

\[
 \sum_{l,a}\bigl(\|P^l_a-\bar P^l_a\|_2+
                       \|U^l_a-\bar U^l_a\|_2\bigr)
 \le K\left[b+(1+M)a+\sum_{l,a}\mathcal T_M(\bar P^l_a)\right].
 \tag{33}
\]

Here \(K\) depends on the primal/direction bound and on (2), not on \(M\).

To prove (33), let \(c_M(P)=\operatorname{sgn}(P)\min(|P|,M)\). Then

\[
 \|(d(Z)-d(\bar Z))\bar P\|_2
 \le cM\|Z-\bar Z\|_2+4\|\bar P-c_M(\bar P)\|_2
 =cM\|Z-\bar Z\|_2+4\mathcal T_M(\bar P).
 \tag{34}
\]

Forward propagation with the bounded actions and Lipschitz \(\phi\) gives \(\|Z^l_a-\bar Z^l_a\|_2+\|H^l_a-\bar H^l_a\|_2\le Ka\). The first preactivation velocity discrepancy is at most \(b\), since \(\|x_a\|/\sqrt d=1\). For \(l=2,3\), expand

\[
\begin{aligned}
 P^l_a-\bar P^l_a={}&
 (v_{W_l}-\bar v_{W_l})H^{l-1}_a
 +\bar v_{W_l}(H^{l-1}_a-\bar H^{l-1}_a)\\
 &+(W_l-\bar W_l)\bar U^{l-1}_a
 +W_l(U^{l-1}_a-\bar U^{l-1}_a).
\end{aligned}
\]

The operator norm is bounded by the HS norm for the two differences and for the raw matrix direction. Hence

\[
 \|P^l_a-\bar P^l_a\|_2
 \le K\bigl(a+b+\|U^{l-1}_a-\bar U^{l-1}_a\|_2\bigr).
\]

Also, by (34),

\[
 \|U^l_a-\bar U^l_a\|_2
 \le2\|P^l_a-\bar P^l_a\|_2+cKM a+
                              4\mathcal T_M(\bar P^l_a).
\]

Inducting through the three layers and summing the two samples proves (33). In particular there is a single factor \(M\), not a product of three truncation levels.

If the reference preactivation velocities have \(L^4\) norms at most \(K\), then

\[
 \mathcal T_M(\bar P)\le
 \|\bar P\,\mathbf1_{|\bar P|>M}\|_2
 \le \|\bar P\|_4^2/M.
 \tag{35}
\]

Thus, when \(a,b\le K\varepsilon\), choosing \(M=\varepsilon^{-1/2}\) for \(0<\varepsilon\le1\) gives a \(K\sqrt\varepsilon\) velocity error. When the reference is finite empirical, (33) still holds exactly, and only its finitely many reference tail norms need to converge. An empirical fourth-moment bound is unnecessary.

## 7. Population continuity, moment bounds, and raw-state approximation

First, the population hidden velocities in (22) exist and are continuous \(L^2\) paths. This fact requires a chain rule along the trajectory, not Fréchet differentiability of the activation Nemytskii map on all of \(L^2\).

Indeed \(Z^1\) is a \(C^1\) \(L^2\) path. From its integral representation, Fubini gives coordinate paths that are absolutely continuous for almost every neuron. The scalar chain rule gives derivative \(d(Z^1)P^1\). This product is \(L^2\)-continuous: for \(t\to s\), split its difference into a bounded multiplier times \(P^1(t)-P^1(s)\), and a bounded gate difference times the fixed \(L^2\) variable \(P^1(s)\); the latter tends to zero by truncation as in (30). The coordinate integral identity therefore holds in \(L^2\), with a continuous \(L^2\) integrand. It follows that \(H^1\) is \(C^1\) in \(L^2\) with that derivative. Each \(W_l\) is \(C^1\) in operator norm, since its increment is \(C^1\) in HS norm. The product rule for the continuous bilinear action gives \(P^2\), and repeating the same argument gives \(U^2,P^3,U^3\). All are bounded in \(L^2\) on the interval by the primal and raw-direction bounds.

Here is the precise raw Euler estimate being used. On a fixed larger ball suppose \(\|F_R\|_{\mathcal X}\le M_0\) and its Lipschitz constant is \(L_0\). A flow step has local Euler defect at most \(L_0M_0h_j^2/2\), obtained by integrating

\[
 \|F_R(\theta(t_j+s))-F_R(\theta(t_j))\|_{\mathcal X}
 \le L_0M_0s .
\]

The error recurrence gives node error at most

\[
 \tfrac12 L_0M_0 T e^{L_0T}|\pi|,
 \qquad |\pi|=\max_jh_j.
 \tag{36}
\]

Linear interpolation adds at most \(2M_0|\pi|\). Choosing sufficiently small mesh so that this bound is less than the slack to the larger ball justifies the estimate by first-exit induction. All constants are dimension independent. The same proof applies on the common population space.

Let \(X^\pi_{\lfloor t\rfloor}\) denote a population Euler node field or instantaneous node velocity, with \(\lfloor t\rfloor\) the preceding mesh node. At \(T\), use the preceding interval when needed for the terminal-left convention. Its state differs from the flow state at \(t\) by \(K|\pi|\), and the two raw directions differ by \(K|\pi|\). Applying (33) with this Euler node as reference and (29), (35), gives

\[
 \sup_{t\le T}\sum_{l,a}
  \left(\|P^l_a(t)-P^{l,\pi}_{\lfloor t\rfloor,a}\|_2+
        \|U^l_a(t)-U^{l,\pi}_{\lfloor t\rfloor,a}\|_2\right)
 \le K\sqrt{|\pi|}.
 \tag{37}
\]

The primary fields have the stronger \(K|\pi|\) bound by their fixed-cap Lipschitz estimates. No continuity of the velocity as a Lipschitz function on the full raw state ball was assumed.

For each \(t\), the strong \(L^2\) convergence in (37) has an almost surely convergent subsequence. Fatou's lemma and (21), (29) therefore give, for every \(p\ge2\),

\[
 \sup_{t\le T}\|X(t)\|_{L^p}\le K\sqrt p
 \tag{38}
\]

for every primary field and hidden velocity under consideration. The constant is independent of \(p\), \(t\), and the approximating mesh. This statement is \(\sup_t\|X(t)\|_p\); it does not assert \(\|\sup_t|X(t)|\|_p\) for velocities. Applying (33) between two flow times, and then (35), also gives the useful mean-square time modulus

\[
 \sum_{l,a}\bigl(\|P^l_a(t)-P^l_a(s)\|_2+
                         \|U^l_a(t)-U^l_a(s)\|_2\bigr)
 \le K|t-s|^{1/2}\qquad (|t-s|\le1).
 \tag{39}
\]

Primary fields are \(L^2\)-Lipschitz in time at fixed cap.

One need not additionally assume operator-norm convergence of the finite trained matrices to use these estimates. At a fixed mesh their exact unrolling gives

\[
 \max_k\|W^{(n)}_{l,k}\|_{\rm op}
 \le \|W^{(n)}_{l,0}\|_{\rm op}
    +\sum_{j<N,b}h_j|p^{(n)}_{j,b}|
              \|\delta^{l,(n)}_{j,b}\|_n\|H^{l-1,(n)}_{j,b}\|_n .
 \tag{40}
\]

The initial norms are at most 10 with probability tending to one, as in the supplied common-action construction. At the fixed mesh, every term in the finite sum converges by the primary finite-program law. The limit of the sum is bounded by \(KT\), uniformly over all sufficiently fine population meshes. The finite first-layer and readout norms at the finitely many nodes also converge to their bounded population counterparts. Thus a single deterministic, enlarged finite primal ball, with slack, contains every node and raw linear interpolant with probability tending to one, for each fixed sufficiently fine mesh. This probability statement takes width first at that mesh; it is not a uniform estimate over growing transcripts.

The derivation of Sections 2--5 used exactly these fixed-mesh finite primal bounds (or the assumed bounds directly). Hence it is not circular to obtain (40) from the primary fixed-program law: that law is a premise, and its finite-mesh validity requires no mesh-uniform derivative or velocity bound.

## 8. The finite-width GF/raw-GD velocity bridge

Let \(\theta_n(t)\) be either the finite flow of (4), or the raw linear interpolation of its exact Euler updates with deterministic step \(\eta_n\to0\). All hidden fields are recomputed from this raw interpolation. In the Euler case its raw direction on an interval is \(F_R(\theta_n(k\eta_n))\); it is not replaced by \(F_R(\theta_n(t))\).

Fix an auxiliary coarse mesh \(\pi\), independent of \(n\), sufficiently fine for the slack in Section 7. Let \(\theta^\pi_n\) be the same-width, same-initialization raw Euler reference. Its node fields and instantaneous node velocities are those of the finite program of Sections 2--5. Denote an instantaneous hidden velocity tuple by \(V^\pi_{n,k}=(P^{l,\pi}_{n,k,a},U^{l,\pi}_{n,k,a})_{l,a}\), with norms summed by layer and sample as in (33). Each pairing or empirical law below is taken separately within a layer.

On the high-probability event supplied by (40), deterministic stopped Euler comparison yields

\[
 \sup_{t\le T}\|\theta_n(t)-\theta^\pi_n(t)\|_{\mathcal X}
 \le K(|\pi|+\eta_n)
 \tag{41}
\]

for raw Euler, and \(K|\pi|\) for GF. For clarity, (41) can be proved without presupposing global finite-flow existence. The coarse interpolation has a defect bounded by \(L_0M_0|\pi|\) in its raw differential equation. Until exit from the larger ball, a fine interpolation has defect bounded by \(L_0M_0\eta_n\), and a flow has defect zero. Integral Gronwall bounds their difference by the right-hand side of (41). Take \(|\pi|\) small and then \(n\) large so the difference is below the ball's fixed slack. No exit can occur, and finite-dimensional local existence continues the GF through \(T\). The same argument keeps the fine Euler nodes in the ball. This proves (41) and existence on the full interval on events of probability tending to one.

For each \(t\), compare the actual raw direction of \(\theta_n(t)\) to \(F_R(\theta^\pi_n(t_k))\), where \(t_k=\lfloor t\rfloor\). Their difference is at most \(K(|\pi|+\eta_n)\): use (41), the bounded displacement over a coarse interval, and, for raw Euler, the bounded displacement from \(t\) to its own preceding fine node. The same bound holds for their state discrepancy. Apply (33) with the *coarse node* as reference to obtain the pathwise estimate

\[
 \sup_{t\le T}\|V_n(t)-V^\pi_{n,\lfloor t\rfloor}\|_{\rm sum,2}
 \le K\left[(1+M)(|\pi|+\eta_n)
       +\max_k\sum_{l,a}\mathcal T_{M,n}(P^{l,\pi}_{n,k,a})\right],
 \tag{42}
\]

where \(\mathcal T_{M,n}(v)=\|(|v|-M)_+\|_n\), and \(\eta_n=0\) denotes GF. This equation treats the actual derivative of every recomputed hidden feature along the raw interpolant.

At fixed \(\pi,M\), Sections 4--5 give joint empirical \(\mathcal W_2\) convergence of all finitely many reference velocities. The map \(v\mapsto (|v|-M)_+\) is 1-Lipschitz, so

\[
 \max_{k,l,a}
  |\mathcal T_{M,n}(P^{l,\pi}_{n,k,a})
       -\mathcal T_M(P^{l,\pi}_{k,a})|
 \longrightarrow0 \quad\hbox{in probability}.             \tag{43}
\]

By the population fourth-moment bound (29), every limiting norm here is at most \(K/M\). In particular, for every \(\varepsilon>0\),

\[
 \lim_{n\to\infty}\mathbb P\left(
 \sup_{t\le T}\|V_n(t)-V^\pi_{n,\lfloor t\rfloor}\|_{\rm sum,2}
 >K\{(1+M)|\pi|+M^{-1}\}+\varepsilon\right)=0 .
 \tag{44}
\]

The norm in (44) compares vectors in the same finite network. Its constant is independent of \(\pi,M,n\). Choosing \(M=|\pi|^{-1/2}\) gives a \(K\sqrt{|\pi|}\) error in this precise width-limit sense. The limits in the argument are fixed \(\pi,M\), then \(n\to\infty\), then \(|\pi|\to0\); no Gaussian identification for a growing transcript is invoked.

Now let \(X_{n,l}(t)\) be the vector, at a single neuron of layer \(l\), containing both samples of all desired primary fields and hidden velocities. Include the shared \(C\) only in population 3. Let \(\mu_{n,l}(t)\) be its empirical probability measure and \(\mu_l(t)\) its population law. Coupling the actual and coarse finite vectors by their common neuron indices costs at most their normalized \(L^2\) discrepancy. The triangle inequality gives

\[
\begin{aligned}
 \sup_{t\le T}\mathcal W_2(\mu_{n,l}(t),\mu_l(t))
 \le{}&
 \sup_t\|X_{n,l}(t)-X^\pi_{n,l,\lfloor t\rfloor}\|_{n}\\
 &+\max_k\mathcal W_2(\mu^\pi_{n,l,k},\mu^\pi_{l,k})\\
 &+\sup_t\|X^\pi_{l,\lfloor t\rfloor}-X_l(t)\|_{L^2(\Omega_l)} .
\end{aligned}                                                    \tag{45}
\]

The first term tends to at most \(K\sqrt{|\pi|}\) in the sense of (44), with primary-field error \(K|\pi|\). The second tends to zero at fixed mesh by the proved finite-program velocity law. The last is bounded by \(K\sqrt{|\pi|}\) by (37). Taking the stated limits proves

\[
 \sup_{t\le T}\mathcal W_2(\mu_{n,l}(t),\mu_l(t))
       \longrightarrow0\quad\hbox{in probability}.         \tag{46}
\]

For a fixed finite collection of times, use the same neuron coupling for the concatenated tuple at those times and the fixed-program law for the entire coarse transcript. The squared coupling cost is the sum of the costs at those finitely many times. The same argument proves joint \(\mathcal W_2\) convergence, preserving all sample/time correlations within the layer.

There is also empirical mean-square equicontinuity in the precise form

\[
 \lim_{\delta\downarrow0}\limsup_{n\to\infty}
 \mathbb P\!\left(
  \sup_{|t-s|\le\delta}\|X_{n,l}(t)-X_{n,l}(s)\|_n
       >\varepsilon\right)=0
 \quad(\varepsilon>0).                            \tag{47}
\]

To verify (47), choose auxiliary uniform meshes of size \(h\). The discrepancy from the frozen coarse observations has width-limit bound \(K\sqrt h\) by (44). For \(|t-s|\le h\), their coarse indices are equal or adjacent. At a fixed mesh the finitely many normalized norms of adjacent reference differences converge, by their joint \(\mathcal W_2\) law, to the corresponding population norms. These are at most \(K\sqrt h\), by (37) and (39). Thus the width-limit bound on the supremum for \(\delta\le h\) is \(K\sqrt h\). First choose \(h\) small for the prescribed \(\varepsilon\), then let \(\delta\le h\) decrease. This proves (47), including raw-GD velocity jumps.

The tail functional is 1-Lipschitz with respect to \(\mathcal W_2\): under any coupling,

\[
 |\mathcal T_u(X)-\mathcal T_u(Y)|
 \le\|(|X|-u)_+-(|Y|-u)_+\|_2\le\|X-Y\|_2 .
\]

Consequently (46) gives, for every fixed \(u\ge0\) and every individual field/velocity \(X\),

\[
 \sup_{t\le T}|\mathcal T_{u,n}(X_n(t))-\mathcal T_u(X(t))|
        \longrightarrow0\quad\hbox{in probability}.       \tag{48}
\]

The moment bounds (21), (29), (38) imply cap-dependent Gaussian second-moment tails: there exist \(K,c,u_0>0\) such that

\[
 \sup_{\pi,k}\|X^\pi_k\mathbf1_{|X^\pi_k|>u}\|_2
 +\sup_{t\le T}\|X(t)\mathbf1_{|X(t)|>u}\|_2
       \le K e^{-cu^2}\quad(u\ge u_0).                    \tag{49}
\]

For an explicit derivation, \(\|X\|_p\le K_0\sqrt p\) gives
\(E[X^2\mathbf1_{|X|>u}]\le u^2(K_0\sqrt p/u)^p\) for \(p\ge2\). Choose \(p=(u/(3K_0))^2\ge2\); then the right-hand side is \(u^2 3^{-p}\). Absorb \(u^2\) into a slightly smaller Gaussian exponent and take square roots to obtain (49).

Since \(|x|\mathbf1_{|x|>2u}\le2(|x|-u)_+\), (48)--(49) imply

\[
 \lim_{n\to\infty}\mathbb P\!\left(
   \sup_{t\le T}\|X_n(t)\mathbf1_{|X_n(t)|>2u}\|_n
                  >2K e^{-cu^2}+\varepsilon\right)=0
 \quad(u\ge u_0,\ \varepsilon>0).                       \tag{50}
\]

This is the required uniform-time empirical tail control. In particular,

\[
 \lim_{u\to\infty}\limsup_{n\to\infty}
 \mathbb P\!\left(
  \sup_{t\le T}\frac1n\sum_i
       |X_{n,i}(t)|^2\mathbf1_{|X_{n,i}(t)|>u}
                   >\varepsilon\right)=0 .
 \tag{51}
\]

The assertion is an asymptotic empirical second-moment statement, not a uniform-in-\(n\) exponential moment estimate. No empirical fourth-moment convergence is asserted or needed.

Finally, (46) and the uniform \(L^2\) bounds imply uniform convergence of the squared norms and all within-layer cross second moments of the velocity tuple. For example use

\[
 |\|x\|_2^2-\|y\|_2^2|
 \le(\|x\|_2+\|y\|_2)\|x-y\|_2
\]

under a coupling, and apply the same identity to sums of two coordinates for cross moments. Integration over \([0,T]\) therefore gives convergence of integrated squared preactivation and feature speeds, and of their cross products.

At raw-GD nodes the right-hand raw direction is used; at a terminal node the left-hand direction is used. The state and direction discrepancy estimates preceding (42) apply to these one-sided choices as well. Node values have no effect on any integrated quantity.

## 9. Scope of the completed bridge

The fixed-cap task is closed under the supplied primal, local-Lipschitz, and fixed-program/common-action premises. The key new estimates are the nonlinear probe bound (14)--(15), the pathwise causal derivative bound (19)--(20), the two velocity response formulas (23)--(29), and the empirical raw-state-to-hidden-velocity comparison (42)--(48).

Every occurrence of \(p_{k,a}\) is the actual two-residual physical coefficient, or its causal deterministic population limit. The proof retains all sample indices, the current transpose returns, both matrix orientations, and the degenerate antipodal input case. It uses the initial actions only as bounded \(L^2\) operators.

Constants in (15), (20)--(21), (29), (38), and (49)--(50) may grow with \(R\). Nothing here supplies cap-independent tails, removes \(R\), proves global primal bounds, or selects one activation for every angle. A separate cap-removal argument may use (33) once it has supplied the needed raw-state/raw-direction comparison; that separate comparison is not proved here.
