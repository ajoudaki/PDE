# Three samples: a large-gain global route and the controlled source-response lemma

This note concerns only the three-sample extension. It uses the supplied two-sample proof and its attached source/baseline/bridge lemmas, read directly. It uses no experiments, sibling materials, or modifications of the original study. The rigorous-mathematics skill was read.

The route proves a global population construction for a **modified near-affine family**

\[
 \phi_{a,e}(z)=a(1+z)+e\arctan z,\qquad a\ge1,
\]

with one sufficiently large gain \(a=a_\delta\) and one sufficiently small positive \(e=e_\delta\). It does not establish the same conclusion for the restricted unit-gain family \(1+z+e\arctan z\). All parameters remain trainable with the original raw metric and normalization. No width-dependent parameter is introduced.

The main additional ingredient is proved below: the supplied nonlinear response argument extends to three samples and arbitrary deterministic time-varying control coefficients of bounded \(\ell^1\) norm. Its constants are independent of the variation of those controls. This makes a bounded cumulative residual clock sufficient; no scalar residual symmetry or fixed residual direction is required.

## 1. Uniform initial feature coercivity

Let \(\Gamma=(x_a^Tx_b/d)_{a,b=1}^3\), and assume its diagonal is one and \(\Gamma_{ab}\le1-\delta\) for distinct samples. The compact set of such positive-semidefinite matrices is denoted \(\mathcal G_\delta\). If it is empty the requested universal statement is vacuous; otherwise set

\[
 \lambda_\delta=\min_{\Gamma\in\mathcal G_\delta}
           \lambda_{\min}(\Gamma+\mathbf1\mathbf1^T)>0.
 \tag{1}
\]

To prove strict positivity, realize \(\Gamma\) by unit vectors \(v_1,v_2,v_3\) in \(\mathbb R^3\). A null vector \(q\) of the augmented Gram obeys \(\sum q_a=0\), \(\sum q_av_a=0\). A nonzero such vector would make the three distinct sphere points collinear: solve for one point as an affine combination of the other two. A line intersects the unit sphere in at most two points. Hence the augmented Gram is positive definite. Eigenvalue continuity and compactness prove (1). No dimension-dependent inverse is involved.

For centered jointly Gaussian \(Z\) with common marginal variance \(v>0\), write \(\psi(z)=az+e\arctan z\). With
\(b_v=E[Z_1\arctan Z_1]/v>0\), Gaussian conditioning gives

\[
 E[Z_i\arctan Z_j]=b_v\operatorname{Cov}(Z_i,Z_j).
\]

Therefore

\[
 E[\psi(Z)\psi(Z)^T]
   =(a^2+2ae b_v)\operatorname{Cov}(Z)
          +e^2E[\arctan(Z)\arctan(Z)^T]
   \succeq a^2\operatorname{Cov}(Z).
\]

The centered odd term has mean zero, so the feature Gram at each initialized layer satisfies
\(Q_\ell\succeq a^2\mathbf1\mathbf1^T+a^2Q_{\ell-1}\), with \(Q_0=\Gamma\). All initialized marginal variances are equal, as required above. Thus

\[
 K^4(0)=Q_3\succeq
 a^6\Gamma+(a^6+a^4+a^2)\mathbf1\mathbf1^T
 \succeq a^6\lambda_\delta I_3.
 \tag{2}
\]

## 2. All controlled paths on one short interval are bounded

Use the actual population state \((w,A,B,C)\), with initial action norms at most 10 and \(\|z^1_{a,0}\|_2=1\). Put

\[
 D=\sqrt d\|w-w_0\|_2+\|A-A_0\|_{HS}+\|B-B_0\|_{HS}.
\]

Consider either the affine activation (\(e=0\)) or the nonlinear activation with any \(0\le e\le1\), and any nonlinear-part backward cap

\[
 \mathcal D_{e,R}(z,q)=a q+e(1+z^2)^{-1}\tau_R(q).
 \tag{3}
\]

The controlled equations replace each loss coefficient \(-r_a\) by an arbitrary measurable coefficient \(c_a(s)\), with
\(\sum_a|c_a(s)|\le1\). The first-layer update is still
\(w'=d^{-1}\sum_a c_a\delta_a^1x_a\); both matrix updates and the readout use the same coefficients. These are nonautonomous equations unless the controls are specified by feedback.

On \(D\le1\), the first projections are at most 2 and the current action norms at most 11. Since
\(|\phi_{a,e}(z)|\le a(3+|z|)\), \(|\phi'_{a,e}|\le2a\), and \(|\mathcal D_{e,R}(z,q)|\le2a|q|\), direct propagation gives the convenient loose bounds

\[
 \|h_a^1\|\le6a,\quad \|h_a^2\|\le70a^2,
 \quad\|h_a^3\|\le800a^3,
\]
\[
 \|\delta_a^3\|\le2a\|C\|,
 \quad\|\delta_a^2\|\le44a^2\|C\|,
 \quad\|\delta_a^1\|\le968a^3\|C\|.
\]

The three hidden raw block speeds consequently sum to at most
\(1400a^3\|C\|\), and \(\|C'\|\le800a^3\). Starting at \(C_0=0\),

\[
 \|C(s)\|\le800a^3s,\qquad
 D(s)\le560000a^6s^2\le10^6a^6s^2.
 \tag{4}
\]

The same proof works for arbitrary positive Euler meshes and arbitrary coefficients \(c_k\) of \(\ell^1\) norm at most one: use \(\|C_k\|\le800a^3s_k\) and
\(\sum_{j<k}h_js_j\le s_k^2/2\). A first-exit induction closes the estimates if the right side of (4) at the final budget is strictly below one. It requires no control regularity and no mesh-size lower bound. Finite-width initial events with projection norms at most 2 and initial action norms at most 10 have probability tending to one; an arbitrarily small extra margin covers the nonzero finite initial readout. The same source constructions can alternatively use zero affine comparator readout and transfer the actual vanishing readout at each fixed transcript.

Set \(\lambda=\lambda_\delta\) and

\[
 S=\frac{12}{\lambda a^6}.
 \tag{5}
\]

Choose \(a\) large enough that all inequalities below hold. Their right sides depend only on \(\lambda\), so this choice precedes the dataset, label vector, cap, and physical horizon. In particular require

\[
 D_S:=10^6a^6S^2<\min\{1/2,\lambda/(3\cdot10^7)\},
 \quad C_S:=800a^3S\le1,
 \quad 6\cdot10^6 C_S^2\le\lambda/4.
 \tag{6}
\]

Each left side decreases to zero as \(a\to\infty\); the last is expressed after division by \(a^6\). Thus (6) is a finite explicit selection procedure.

## 3. The source-response lemma with three time-varying coefficients

**Lemma.** Fix finite \(a\ge1,B\ge1,S>0\). Take any finite positive mesh of duration at most \(S\), and any deterministic coefficient sequence \(c_k\in\mathbb R^3\) with \(\|c_k\|_1\le1\). Suppose the corresponding actual affine Euler arrays have projected first-layer, action-operator, and readout norms bounded by \(B\), with uniform slack, on finite-width events whose probabilities tend to one. Then there exist \(e_*(a,B,S)>0\) and \(K(a,B,S)<\infty\), independent of the mesh, coefficients, cap and \(\Gamma\), such that the canonical nonlinear programs with activation \(\phi_{a,e}\) and gate (3), for \(0\le e\le e_*\), have uniformly bounded response coefficients and

\[
 \sup_{k,R}\big(\|C_k\|_{L^p}+\|q_k^2\|_{L^p}
                   +\|q_k^1\|_{L^p}\big)\le K\sqrt p,
 \qquad p\ge2.
 \tag{7}
\]

For the pair norm in the source proof, use the maximum of the three sample coordinates. All source groups retain full time/sample covariance, including singular covariance. The lemma applies to the bounded controlled paths of Section 2 with, for example, one fixed sufficiently generous numerical \(B\).

### 3.1 Exact source representation and what is frozen

Write \(P_k=\Gamma\operatorname{diag}(c_k)\); then
\(|P_k|_{\infty\to\infty}\le1\). The exact source equations are

\[
 Z^1_k=Z^1_0+\sum_{r<k}h_rP_r\delta_r^1,
 \quad q^1_k=\zeta^1_k+\sum_{v\le k}b^2_{kv}H^1_v,
\]
\[
 Z^\ell_k=\xi^\ell_k+\sum_{r<k}a^\ell_{kr}\delta_r^\ell,
 \quad\ell=2,3,
 \qquad q^2_k=\zeta^2_k+\sum_{v\le k}b^3_{kv}H^2_v,
\]
\[
 C_k=\sum_{r<k}h_rc_r^TH^3_r.
 \tag{8}
\]

The coefficient rules are, with \(i,j\) now sample indices in the displayed entries,

\[
 a^\ell_{ki,vj}
 =E\partial_{\zeta^{\ell-1}_{v,j}}H^{\ell-1}_{k,i}
       +h_vc_{v,j}E[H^{\ell-1}_{k,i}H^{\ell-1}_{v,j}],\quad v<k,
\]
\[
 b^\ell_{ki,vj}
 =E\partial_{\xi^\ell_{v,j}}\delta^\ell_{k,i}
       +\mathbf1_{v<k}h_vc_{v,j}E[\delta^\ell_{k,i}\delta^\ell_{v,j}],
       \quad v\le k.
 \tag{9}
\]

The four Gaussian covariance groups are exactly those in the supplied baseline, with three samples: forward covariance is the second moment of the corresponding preceding feature, reverse covariance the second moment of the corresponding delta. The groups and first root are independent in the canonical source representation. No neuron pairing between layers is imposed.

To derive (8)--(9), unroll each trained matrix into its initial matrix plus the rank-one updates with coefficient \(h_vc_{v,j}\). Apply the supplied finite-program Gaussian-conditioning rule to each initial matrix call in both orientations, and add the learned terms. At fixed cap, the coordinate maps are globally Lipschitz with bounded first derivatives. Three samples add only finitely many queries. All formal derivatives freeze the deterministic arrays, covariance parameters, mesh and control coefficients; formal source slots remain separate at singular covariance. The conditioning proof never differentiates scalar population feedback.

If the controls arose from the actual population residual, their numerical values are deterministic causal contractions. Freezing those values is the same scalar-feedback identification used for the learned moments. At any fixed finite transcript, convergence of all previous contractions identifies those values, and finite induction transfers the frozen program to the actual feedback program. For normalized controls at a zero residual, use \(c=0,h=0\) and omit the zero step; the physical update is exactly zero. There is no need to differentiate \(r/\|r\|_1\) or a covariance square root. For the perturbative affine comparator, use **the same frozen nonlinear control sequence and mesh**, not the affine model's own residual sequence.

### 3.2 Affine response bounds remain valid

On a raw primal ball of radius \(b=2B\), all affine query norms, their Lipschitz constants, and the Lipschitz constant of the controlled raw affine field are bounded by a finite \(Q=Q(a,b)\). For example taking a sufficiently enlarged universal multiple of \(a^3b^3\) suffices: affine forward norms have orders \(ab,a^2b^2,a^3b^3\), affine backward norms orders \(ab,a^2b^2,a^3b^3\), and every raw update is a product of the same factors as in the supplied baseline. Inserting bounded additive errors immediately after any one of the four matrix-answer types changes the raw update and the four relevant response outputs by at most another such \(Q\) times the error norm. Every use of control coefficients is bounded by \(\sum|c_{k,a}|\le1\), or \(|P_k|\le1\); no difference or derivative of controls occurs.

For an independent Gaussian probe \(g\), inserted with signed coefficients \(\alpha_{k,a}\) at the chosen answer slots, the bounded-ball affine comparison gives

\[
 \|\Theta^\varepsilon_k-\Theta^0_k\|
 \le QSe^{QS}|\varepsilon|\|g\|;
\]

if only time \(j\) is perturbed, replace the first \(S\) by \(h_j\). The coefficients \(c_k\) are held identical in both programs. Strict ball slack closes this comparison for small fixed probe amplitude.

At a fixed transcript the affine source expression is affine in the new Gaussian root \(G\), with coefficient
\(\varepsilon\sum_{j,b}\alpha_{j,b}\partial_{\eta_{j,b}}V\). Hence

\[
 E[GV^\varepsilon]
 =\varepsilon\sum_{j,b}\alpha_{j,b}
                 \partial_{\eta_{j,b}}V^\varepsilon.
\]

The finite-program induction makes its deterministic coefficients continuous in the probe amplitude, including at singular covariance. Taking the width limit at a fixed probe amplitude and then the amplitude to zero, the norm comparison bounds the absolute sum of the formal derivative row by \(Q^2Se^{QS}\), and an individual past-time source contribution by \(Q^2h_je^{QS}\). Choose signs after taking that finite deterministic row. This is exactly the probe argument in the supplied baseline; time-varying deterministic controls are simply fixed numerical coefficients in every affine expression. No matrix-to-response implication has been assumed.

Adding the learned moment terms in (9), and converting per-output row bounds to the time sum of maximum block row norms, costs only the fixed sample factor 3. Therefore there are \(A_0,M_0<\infty\), depending only on \((a,B,S)\), with

\[
 |a^{\ell,0}_{kj}|\le A_0h_j,
 \qquad \sum_{j\le k}|b^{\ell,0}_{kj}|\le M_0,
 \quad \ell=2,3.
 \tag{10}
\]

For instance one may enlarge \(Q\) above and take
\(A_0=3Q^2(e^{QS}+1)\), \(M_0=3SQ^2(e^{QS}+1)\). These constants do not depend on the particular control sequence.

### 3.3 Primal perturbation and Gaussian source variances

At the same raw state, the forward activation changes by at most \(\pi e/2\), and the backward gate differs from \(aq\) by at most \(e|q|\), independently of the cap. Forward propagation, reverse propagation, and the rank-one difference inequality thus give

\[
 \|V_{e,R,c}(\Theta)-V_{0,c}(\Theta)\|\le Q_1e,
 \qquad \operatorname{Lip}(V_{0,c})\le Q_1
\]

on the common ball, uniformly in \(c\). Discrete Gronwall bounds the nonlinear-affine raw difference by \(Q_1Se^{Q_1S}e\). Choose \(e\) so that this is less than half the affine slack. It closes by induction without any nonlinear-field Lipschitz constant or tail assumption. The forward and backward queries then differ in \(L^2\) by \(Q_2e\), so every learned moment in (9) differs by at most \(Q_3e\). Its forward coefficient contribution has the factor \(h_j\), and the full backward-row contribution is at most \(Q_3Se\). Common fixed-program construction couples the two actual programs; no growing covariance square roots are compared. The source covariance rules now bound every scalar source variance by one \(\sigma^2(a,B,S)\).

### 3.4 Bounded coefficient prefixes imply moments and derivative envelopes

Fix \(A=A_0+1\) and \(M=M_0+1\), and consider the required, already constructed coefficient rows bounded by
\(|a_{kr}|\le Ah_r\), \(\sum_{v\le k}|b_{kv}|\le M\). Since \(|\mathcal D|\le(a+1)|q|\), \(|\phi(z)|\le a(1+|z|)+\pi/2\), the three source recursions (8) give deterministic-norm Volterra inequalities. For example, for middle-layer feature norms \(U_k=\max_{v\le k}\|H^2_v\|_p\),

\[
 \|q_r^2\|_p\le K\sqrt p+MU_r,
 \quad U_k\le K\sqrt p+KaA\sum_{r<k}h_rU_r.
\]

Enlarging \(K\) to absorb the preceding \((a+1)\) and source terms is legitimate because \(a,A,M,S,\sigma\) are fixed. Bottom recursions use \(|P_r|\le1\). Top recursions have an extra nested readout sum, bounded using \(\sum h\le S\). Finite product iteration gives \(K\sqrt p\) for every relevant coordinate on such a prefix. Replacing two sample coordinates by three costs at most a factor three in bounding their maximum; correlations are unrestricted.

Set \(g(z)=(1+z^2)^{-1}\). The local derivative matrices are

\[
 G=aI+e\operatorname{diag}(g(Z)),\quad
 V=aI+e\operatorname{diag}(g(Z)\tau_R'(q)),\quad
 L=e\operatorname{diag}(g'(Z)\tau_R(q)).
\]

They obey \(|G-aI|,|V-aI|\le e\) and \(|L|\le eQ_r\), with \(Q_r\) the appropriate incoming-field maximum. Differentiating (8) gives precisely the derivative recursions of the supplied nonlinear response proof, with \(P\) replaced by \(P_r\), \(c\) by \(c_r\), and each affine identity gate by \(aI\). Submultiplicativity therefore bounds each single transpose-source derivative by
\(Kh_j\mathcal E_k\), and each forward-source derivative row by \(K\mathcal E_k\), where

\[
 \mathcal E_k=\exp\{Ks_k+Ke\sum_{r<k}h_rQ_r\}.
\]

Backward-output derivatives require the additional current factor
\(K(1+eQ_k)\mathcal E_k\). It must not be dropped. The moment bound gives a uniform \(E e^{cQ_r^2}<\infty\). Convexity gives

\[
 e^{\theta\sum_{r<k}h_rQ_r}
 \le1-s_k/S+\sum_{r<k}(h_r/S)e^{\theta SQ_r}.
\]

Thus \(\mathcal E_k\) and \((1+Q_k)\mathcal E_k\) have every fixed finite moment uniformly in mesh and cap. No random time supremum is used.

Subtracting the same-array affine derivative equations leaves affine Volterra feedback plus terms containing \(G-aI,V-aI,L\). The preceding envelope bounds their expectations by \(Ke h_j\) for one transpose source and by \(Ke\) for a full forward-source row. This conclusion retains the single source-step factor: before its source time the derivative vanishes, its direct injection at that time carries \(h_j\), and every subsequent term carries the derivative it feeds. Current \(L_kJ_k\) terms are controlled by \(eE[Q_k\mathcal E_k]\), also \(O(e)\).

### 3.5 Exact affine recursions and causal closure

Here are the recursions needed to verify that there is no new current-row feedback or control derivative. Let \(F,V,U\) denote affine derivatives of \(H^1,H^2,H^2\) with respect to bottom reverse, middle reverse, middle forward sources, respectively, evaluated at arbitrary fixed response arrays; let \(T\) be the top forward-source derivative of \(C\). Then

\[
 F_{k,j}=a^2h_jP_j\mathbf1_{j<k}
       +a^2\sum_{r<k}h_rP_r\sum_{v\le r}b^2_{rv}F_{v,j},
\]
\[
 V_{k,j}=a^2a^2_{kj}\mathbf1_{j<k}
       +a^2\sum_{r<k}a^2_{kr}\sum_{v\le r}b^3_{rv}V_{v,j},
\]
\[
 U_{k,j}=aI\mathbf1_{k=j}
       +a^2\sum_{r<k}a^2_{kr}\sum_{v\le r}b^3_{rv}U_{v,j},
\]
\[
 T_{k,j}=a h_jc_j^T\mathbf1_{j<k}
       +a^2\sum_{r<k}h_rc_r^T\sum_{v<r}a^3_{rv}\mathbf1 T_{v,j}.
 \tag{11}
\]

Here \(a^2_{kj}\) with indices is the layer-2 forward response block; the unindexed \(a^2\) is the square of the activation gain. The affine backward derivative outputs are
\(a\mathbf1T\) and \(W_{k,j}=a\sum_{v\le k}b^3_{kv}U_{v,j}\).

Under bounded prefix coefficients, finite Volterra iteration in (11) gives
\(|F_{k,j}|,|V_{k,j}|\le Kh_j\), and bounded time-row norms for \(U,T\). The same-array perturbative derivative estimate and learned-moment estimate give exact difference identities

\[
 \Delta a^2=\Delta F+\eta^2,\quad
 \Delta a^3=\Delta V+\eta^3,
\quad \Delta b^3=a\mathbf1\Delta T+\nu^3,
\quad \Delta b^2=\Delta W+\nu^2,
\]

with \(|\eta_{kj}|\le Ke h_j\), \(\sum_j|\nu_{kj}|\le Ke\). Define
\(\alpha_k^\ell=\max_{j<k}|\Delta a^\ell_{kj}|/h_j\),
\(\beta_k^\ell=\sum_{j\le k}|\Delta b^\ell_{kj}|\), and
\(I_k=\sum_{r<k}h_r(\beta_r^2+\beta_r^3)\).
Subtracting (11) in the chronological order gives

\[
 \alpha_k^2\le K(e+I_k),\quad
 \alpha_k^3\le K(e+I_k),\quad
 \beta_k^3\le K(e+I_k),\quad
 \beta_k^2\le K(e+I_k).
 \tag{12}
\]

For explicit dependency checking: the first recursion uses only past \(b^2\); the second uses the newly bounded current \(a^2_k\) and past \(b^3\). The top \(T_k\) uses only \(a^3_r\) with \(r<k\), while its nonlinear remainder uses the current \(a^3_k\), already bounded. Finally \(U_k\) uses current \(a^2_k\) and past \(b^3\), and \(W_k\) is allowed to use current \(b^3_k\), just bounded. In each subtraction the forcing is bounded by \(K(e+I_k)\); the remaining unknown is inside a strictly past \(K\sum h_r\max_{v\le r}\) sum, so finite product iteration proves the claimed inequality. The factors \(a\) and \(a^2\) only enlarge \(K\). The direct terms containing \(P_j,c_j\) cancel because the comparator uses the same controls.

Thus \(E_k:=\beta_k^2+\beta_k^3\) satisfies
\(E_k\le Ke+K\sum_{r<k}h_rE_r\). Choosing
\(e_*\le(2Ke^{KS})^{-1}\), and also satisfying the primal comparison restriction above, proves each new row lies within one half of its affine bound plus unit slack. A literal induction through the four stages in (12) closes every prefix; no simultaneous assumption on unconstructed current rows occurs.

The nonlinear current blocks remain

\[
 (b^3_{kk})_{ij}=\mathbf1_{i=j}E L^3_{k,i},
\]
\[
 (b^2_{kk})_{ij}=\mathbf1_{i=j}E L^2_{k,i}
       +(b^3_{kk})_{ij}E[V^2_{k,i}G^2_{k,j}].
 \tag{13}
\]

They are \(O(e)\); all earlier blocks can be full. No current return has been discarded or inverted. The moment argument in Section 3.4 now applies to the full program and proves (7). This completes the controlled source-response lemma.

## 4. Kernel domination gives global capped physical flows

The cap is not a gradient modification, so its hidden prediction contribution need not be positive semidefinite. We bound its absolute size instead.

For every state reached by a controlled path of duration at most \(S\), forward Lipschitz propagation from its own initialized state gives

\[
 \|h_a^3-h_{a,0}^3\|_2\le1500a^3D.
\]

Indeed first-layer feature difference is at most \(2aD\), middle preactivation difference at most \(26aD\), middle feature difference at most \(52a^2D\), top preactivation difference at most \(615a^2D\), and top feature difference at most \(1230a^3D\). The loose constant above suffices. Hence

\[
 \|K^4-K^4(0)\|_{op}\le7.2\cdot10^6a^6D,
 \qquad K^4\succeq(3/4)\lambda a^6I
 \tag{14}
\]

under (6).

Let \(J_{hid}\) be the true hidden prediction Jacobian and \(U_{hid,R}\) the map from sample coefficients to capped hidden raw directions. The previous bounds give
\(\|J_{hid}\|,\|U_{hid,R}\|\le\sqrt3\,1400a^3\|C\|\). Therefore

\[
 \|J_{hid}U_{hid,R}\|_{op}
       \le6\cdot10^6a^6\|C\|^2
       \le\lambda a^6/4.
\]

For the physical cap flow, \(\dot r=-[K^4+J_{hid}U_{hid,R}]r\), so

\[
 \frac d{dt}\|r\|_2\le-\frac{\lambda a^6}{2}\|r\|_2
 \quad\text{whenever }r\ne0.
 \tag{15}
\]

At a zero residual the entire physical vector field is zero. With binary labels and initial population readout zero,

\[
 \|r(t)\|_2\le\sqrt3 e^{-\lambda a^6t/2},
 \qquad \int_0^\infty\|r(t)\|_1dt
       \le\frac6{\lambda a^6}=S/2.
 \tag{16}
\]

These bounds first hold before any putative exit or clock-budget hit. Define \(s(t)=\int_0^t\|r(v)\|_1dv\), and wherever residual is nonzero use controls \(c=-r/\|r\|_1\). Section 2 then bounds the state until \(s=S\). Equation (16) prevents that clock hit, with strict margin. A fixed-cap physical vector field is locally Lipschitz on the raw Hilbert state, and bounded on the attained ball. A finite maximal physical endpoint would consequently have a strong state limit and admit continuation. This proves global existence of every cap flow, with the same cap-independent bounds. It does not presuppose uncut existence.

## 5. Cap removal and all-time population existence

Fix \(a\) by (6), and choose one positive \(e\le e_*(a,B,S)\) from Section 3. All these choices depend only on \(\delta\).

On every fixed finite physical horizon, Euler approximations to a fixed-cap physical path eventually have accumulated control budget at most \(S\), because their limiting cap path has budget at most \(S/2\). Apply the controlled response lemma to their deterministic population coefficient sequence and effective mesh \(h_j=\Delta t_j\|r_j\|_1\). This gives the same subGaussian bound independent of that physical horizon and cap. Fixed-cap mesh convergence passes it to every actual cap flow. Neither \(e\) nor the response constants are chosen anew as the physical horizon grows.

The asymmetric gate comparison in the supplied bridge becomes

\[
 |\mathcal D_{e,R'}(z_A,q_A)-\mathcal D_{e,R}(z_B,q_B)|
 \le(a+e)|q_A-q_B|+C eR|z_A-z_B|
            +2e|q_B|\mathbf1_{|q_B|>R}.
\]

Forward propagation and rank-one products consequently give the same raw strong comparison with only a linear loss in \(R\). On a fixed physical horizon \([0,T]\), the cap difference is bounded by
\(C_T\exp(C_TR-cR^2)\), which vanishes as \(R\to\infty\). The population states, trained HS increments and directions converge strongly on that interval to one uncut \(C^1\) physical solution. The constants in this last comparison may depend on \(T\); the activation coefficient does not.

Repeat on integer horizons on one canonical action construction containing their countable cap/mesh programs. Uniqueness follows from the same asymmetric comparison against the cap reference; only the reference needs tails. Hence the restrictions agree and define a single global autonomous physical solution, unique against bounded-primal strong competitors and uniquely continuable from its reached states. Limits preserve (4), (14), and (16). In particular the requested cumulative Euclidean residual time is finite:

\[
 \tau_\infty=\int_0^\infty\|r(t)\|_2dt
              \le\frac{2\sqrt3}{\lambda_\delta a_\delta^6}.
\]

The existing finite GF/raw-GD/velocity/path-space bridge now applies with three samples: it uses finitely many sample slots, exact residual feedback, bounded primal/reference tails, and the same asymmetric cap comparison. It does not require two-sample symmetry once global cap references have been supplied as above. Extra sample indices only alter constants. The finite initial readout is retained in this physical bridge, as in the supplied proof.

## 6. Optional all-time nonaffinity transfer

This route has a simple uniform initial reference for strict nonaffinity. Each initialized scalar preactivation is centered Gaussian with standard deviation at least one. Define

\[
 \eta_*=\inf_{\sigma\ge1}\mathcal R(\sigma G)>0,
 \quad \mathcal R(Z)=\inf_{\alpha,\beta}E[\arctan Z-\alpha-\beta Z]^2.
\]

Positivity on finite compact \(\sigma\)-intervals follows from full Gaussian support. At infinity, bounded convergence gives

\[
 \mathcal R(\sigma G)
   =E[\arctan(\sigma G)^2]-(E[G\arctan(\sigma G)])^2
   \longrightarrow\frac{\pi^2}{4}(1-2/\pi)>0.
\]

Thus the half-line infimum is positive. The proof's regression stability estimate applies with \(m=1\). In addition to (6), enlarge \(a\) so that

\[
 615a^2D_S\le
 \min\{1/2,\sqrt{\eta_*}/[2(1+\pi)]\}.
\]

Its left side is \(O(\lambda^{-2}a^{-4})\), so this is feasible before choosing \(e\). Every actual preactivation stays this close in \(L^2\) to its own initialized Gaussian field, uniformly over all time and caps. Therefore
\(\mathcal R(z_a^\ell(t))\ge\eta_*/4\). Absorbing \(a(1+Z)\) into the affine approximant gives exact nonaffinity error
\(e^2\mathcal R(Z)\ge e^2\eta_*/4>0\).

This proves all-time strict nonaffinity for the modified gain family. Initial hidden acceleration and changing-kernel certificates should be checked separately for three samples; this note does not substitute a two-sample initial-motion lemma for that task.

## 7. Expanded response inequalities for independent audit

This section makes the norm estimates behind Sections 3.4–3.5 explicit. It is redundant with their architecture but records every feedback factor needed to verify the extension.

All matrix norms below are maximum absolute row sums. Time-row norms sum those block norms. These norms are submultiplicative for the 3-by-3 source blocks, the 1-by-3 readout blocks, and the 3-by-1 vector \(\mathbf1\). In particular \(|I_3|=|\mathbf1|=1\), \(|c_r^T|\le1\), \(|P_r|\le1\). Only conversion from a maximum of three scalar coordinate norms or three output derivative rows costs the numerical factor three already allowed above.

Write \(d_a=a+1\). On a bounded coefficient prefix, let \(J\) be a preactivation derivative and \(T\) a readout derivative. The exact random derivative equations are:

\[
 J^1_{k,j}=\sum_{r<k}h_rP_r\left[
 L^1_rJ^1_{r,j}+V^1_r\left(I\mathbf1_{r=j}
             +\sum_{v\le r}b^2_{rv}G^1_vJ^1_{v,j}\right)\right],
\]
\[
 J^2_k=I_k^\xi+\sum_{r<k}a^2_{kr}\left[
 L^2_rJ^2_r+V^2_r\left(I_r^\zeta
             +\sum_{v\le r}b^3_{rv}G^2_vJ^2_v\right)\right],
\]
\[
 J^3_{k,j}=I\mathbf1_{k=j}+\sum_{r<k}a^3_{kr}
        (V^3_r\mathbf1 T_{r,j}+L^3_rJ^3_{r,j}),
 \qquad T_{k,j}=\sum_{r<k}h_rc_r^TG^3_rJ^3_{r,j}.
 \tag{17}
\]

For a single bottom transpose source,

\[
 |J^1_{k,j}|\le d_a h_j
       +\sum_{r<k}h_r(eQ_r+d_a^2M)
                    \max_{v\le r}|J^1_{v,j}|.
\]

For a single middle transpose source, replace the forcing by \(d_aAh_j\) and the feedback coefficient by \(A(eQ_r+d_a^2M)\). For the full middle forward-source row \(u_k\), the forcing is one and that same feedback applies. For top forward-source row norms \(u_k,t_k\),

\[
 t_k\le d_a\sum_{r<k}h_ru_r,
\qquad
 u_k\le1+\sum_{r<k}h_r(d_a^2AS+eAQ_r)
                              \max_{v\le r}u_v.
 \tag{18}
\]

These follow by summing (17) over the named formal source slots; rows can be padded by zeros, so their length never appears. A nonnegative recursion
\(x_k\le f+\sum_{r<k}h_r\ell_r\max_{v\le r}x_v\)
is bounded by \(f\prod_{r<k}(1+h_r\ell_r)\le f e^{\sum h_r\ell_r}\). This proves the derivative envelopes quoted in Section 3.4, with constants depending only on \(a,A,M,S\).

For the coordinate moments themselves, put \(U_k=\max_{v\le k}\|H^2_v\|_p\). With one source constant \(K_0\), the exact norm inequalities are

\[
 \|q_r^2\|_p\le K_0\sqrt p+MU_r,
\]
\[
 U_k\le K_0(1+ad_aAS)\sqrt p
          +ad_aAM\sum_{r<k}h_rU_r.
 \tag{19}
\]

Here the harmless constant term \(a+e\pi/2\) is absorbed into \(K_0\sqrt p\). At the bottom,

\[
 \max_{v\le k}\|H^1_v\|_p
 \le K_0(1+ad_aS)\sqrt p
       +ad_aM\sum_{r<k}h_r\max_{v\le r}\|H^1_v\|_p.
\]

At the top, for \(V_k=\max_{v\le k}\|C_v\|_p\),

\[
 V_k\le K_0S\sqrt p+ad_aAS\sum_{r<k}h_rV_r.
\]

Finite product iteration proves (7) under the stated prefix assumption; then (8) gives all remaining forward and backward field moments. All source variances have already been bounded independently of these coefficient-prefix moments.

For clarity about the same-array perturbation, subtracting the affine middle equation from (17) leaves affine feedback
\(a^2\sum a^2_{kr}\sum b^3_{rv}(J_v-J_v^0)\)
and forcing

\[
 \sum_{r<k}a^2_{kr}\left[
 (V_r-aI)I_r^\zeta+L_rJ_r
 +(V_r-aI)\sum_{v\le r}b^3_{rv}G_vJ_v
 +a\sum_{v\le r}b^3_{rv}(G_v-aI)J_v\right].
 \tag{20}
\]

For the bottom, replace \(a^2_{kr}\) by \(h_rP_r\). For a single transpose source, this forcing is bounded by
\(Ke h_j[1+\sum_{r<k}h_r(1+Q_r)\mathcal E_r]\); for a full forward-source row replace \(h_j\) by one. The deterministic affine feedback and finite product iteration preserve those bounds up to a constant. Their expected values are respectively \(Ke h_j\) and \(Ke\), by the exponential-integrability argument in Section 3.4.

The top subtraction is

\[
 \Delta J_k=\sum_{r<k}a^3_{kr}
       [a\mathbf1\Delta T_r+(V_r-aI)\mathbf1T_r+L_rJ_r],
\qquad
 \Delta T_k=\sum_{r<k}h_rc_r^T
       [a\Delta J_r+(G_r-aI)J_r].
\]

Substituting the second equation into the first bounds affine feedback by
\(a^2AS\sum_{r<k}h_r\max_{v\le r}|\Delta J_v|\); the remainder obeys (20)'s row bound. At the backward outputs the additional middle forcing is

\[
 L_kJ_k+(V_k-aI)\sum_{v\le k}b^3_{kv}G_vJ_v
        +a\sum_{v\le k}b^3_{kv}(G_v-aI)J_v,
\]

and the top forcing is \(L_kJ_k+(V_k-aI)\mathbf1T_k\). Their expected row norms are \(O(e)\), including the current terms. This proves the derivative-error remainders used in (12) without omitting a cap derivative.

Finally the deterministic four-row difference calculation can be checked with explicit scalar inequalities. Let \(A,M\) be the enlarged coefficient bounds and \(A_0,M_0\) the affine bounds. At arbitrary such arrays, (11) gives

\[
 K_F=a^2e^{a^2MS},\quad
 K_V=a^2A e^{a^2AMS},\quad
 K_U=a e^{a^2AMS},\quad
 K_T=aS e^{a^2AS^2}
 \tag{21}
\]

as admissible bounds on \(|F_{k,j}|/h_j\), \(|V_{k,j}|/h_j\), and the row norms of \(U,T\). Let
\(f^j_k=|F_{k,j}-F^0_{k,j}|/h_j\),
\(v^j_k=|V_{k,j}-V^0_{k,j}|/h_j\),
\(u_k=|U_{k\bullet}-U^0_{k\bullet}|_{r}\), and
\(t_k=|T_{k\bullet}-T^0_{k\bullet}|_{r}\). Causal zero entries are taken to be zero in all maxima. Product expansion gives

\[
 f^j_k\le a^2K_F\sum_{r<k}h_r\beta_r^2
       +a^2M_0\sum_{r<k}h_r\max_{v\le r}f^j_v,
 \tag{22}
\]
\[
 v^j_k\le a^2(1+MSK_V)\alpha_k^2
       +a^2A_0K_V\sum_{r<k}h_r\beta_r^3
       +a^2A_0M_0\sum_{r<k}h_r\max_{v\le r}v^j_v,
 \tag{23}
\]
\[
 t_k\le a^2SK_T\sum_{r<k}h_r\alpha_r^3
               +a^2A_0S\sum_{v<k}h_vt_v,
 \tag{24}
\]
\[
 u_k\le a^2MSK_U\alpha_k^2
       +a^2A_0K_U\sum_{r<k}h_r\beta_r^3
       +a^2A_0M_0\sum_{r<k}h_r\max_{v\le r}u_v,
 \tag{25}
\]
\[
 |W_{k\bullet}-W^0_{k\bullet}|_r
       \le aK_U\beta_k^3+aM_0\max_{v\le k}u_v.
 \tag{26}
\]

For (23), expand \(a^2_{kr}b^3_{rv}V_{v,j}\) into the difference of its first, second and third factors in that order; the first difference contributes at most \(MSK_V\alpha_k^2\), the second the displayed \(\sum h\beta^3\), and the third the past-feedback term. The same expansion gives (25). Equation (24) follows by exchanging the two finite nonnegative time sums, using \(\sum_{r>v}h_r\le S\). Equation (26) is the exact current-row product with the already constructed \(b^3_k\). These computations use \(P_r,c_r\) only through their bounded norms; their direct source terms cancel identically.

Iterating (22) and adding \(\eta^2\) first proves \(\alpha_k^2\le K(e+I_k)\). Inserting that bound into (23), iterating, and adding \(\eta^3\) proves the second bound in (12). Next (24) and \(\nu^3\) prove the third, using \(\sum_{r<k}h_r I_r\le S I_k\). Finally (25), (26) and \(\nu^2\) prove the fourth. This gives the literal four-stage induction described in Section 3.5, uniformly for every allowed mesh and deterministic time-varying control sequence.
