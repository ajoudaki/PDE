# Isolated adversarial modular audit

2026-09-07. **MODULAR PASS, with the scope below.** No blocking mathematical gap was found in the stated fixed-program identification, supported response estimates, support induction, or physical-coefficient memory obstruction. This verdict includes an audit of the specialized cutoff/initialization bridge; it is not inherited merely from the softplus lemma.

The mathematical reference for this verdict is the rescaled finite-width Euler system (2), with residual feedback and initialization (3). The four supplied files do not specify the original unrescaled network parameterization sufficiently to independently reconstruct its change of variables and physical time normalization. Thus “physical” here means the reference system (2) stipulated in the candidate. This is **not** certification of its provenance from an otherwise unspecified raw network, convergence along the original width-dependent learning rate \(\eta=n^{-2}\), a population differential equation, or global MF. The candidate expressly excludes those limit claims. No missing global theorem is being counted as a defect in this modular submission.

## Inputs and isolation

I personally read all four files in full, including all of the supplied finite-program proof. No other mathematical files, project/history material, reviews, snapshots, diffs, agent outputs, external imports, or experiments were used. References to further documents inside these four files were not followed. Source files were not edited.

| Source | Lines | SHA-256 |
|---|---:|---|
| `/tmp/l2-two-sample-proof-0ywjpp/FROZEN_MASK_CANONICAL_MEMORY_TEST.md` | 1012 | `7af67979a2734b4b2955e644a5a17b54497e6892c775d53cc175c990db494c3a` |
| `/tmp/l2-two-sample-proof-0ywjpp/FROZEN_MASK_UNIFORM_GAUSSIAN_RESPONSE_GAP.md` | 263 | `a05a83e0ee5ea13d02a3ef51bb8967d1d3ddb7fd6eed601b4f1fdb4cea85c65a` |
| `/tmp/l2-two-sample-proof-0ywjpp/HARMONIC_COVARIANCE_RESPONSE_TEST.md` | 651 | `cb1ccec3a4431815b17ef6a8268c168a5feb5f6fe55b0a7c4a6b155ba7c69fb5` |
| `/tmp/l3-two-sample-proof-DLuelg/SOFTPLUS_FIXED_PROGRAM_IDENTIFICATION.md` | 862 | `875fe50be7d9eb859810504649020ae0005be5f47109ef4f98c0c288cbf5d603` |

The requested candidate hash matches. Equation and section numbers below refer to that candidate unless a dependency is named.

## 1. Residual feedback and order of limits

The sample-exchange transformation is valid at finite width **in distribution**, including the independent centered Gaussian readout: exchange the first-layer sample coordinates and negate \(w_0\). In (2), \(f_a,c_a,\delta_a,q_a\) transform to their negative exchanged values; each hidden update contains the sign-invariant product \(c_b\delta_b\), and the readout update changes sign. Once deterministic empirical limits are established, this forces
\[
f_{k2}=-f_{k1},\qquad c_{kb}=2r_ky_b,\qquad
r_k=1-f_{k1},\qquad \lambda_k=2hr_k.
\]
It does not give sample antisymmetry on an individual finite-width realization. Predictions are computed before their residual coefficients enter the next update, so feedback is causal.

All width limits in Section 4 fix \(h,N\), and any cutoff used at that stage. Subsequent \(h\downarrow0\) or \(h=T/N\) limits concern the resulting deterministic population programs. Constants in the identification comparison may depend on \(N,h\); they cannot be used to identify \(N=N(n)\). Constant label forcing is not substituted for physical residuals. In particular the first two coefficients really are
\[
\lambda_0=\lambda=2h,\qquad
\lambda_1=\mu=\lambda(1-\lambda v_0).
\]

## 2. Specialized finite-program bridge: hypotheses and removal steps

The softplus lemma's literal activation-specific statement is insufficient by itself. Its supplied proof, however, proves the needed finite-graph machinery under the following checked hypotheses.

* **Fixed graph and admissible maps.** Unroll the sole trained matrix into initial-matrix actions in both orientations and finitely many rank terms. Features \(\phi_1,\arctan\) are smooth and globally Lipschitz. Choose the bottom cap to be a smooth bounded cap of the type explicitly constructed in the softplus dependency: \(|\tau_Q|\le\min(|q|,2Q)\), equal to the identity on \([-Q,Q]\), with uniformly bounded first derivative. Then \(\psi(z)\tau_Q(q)\) has bounded first partial derivatives for fixed \(Q\).
* **Readout localization.** Equations (11) follow from \(|f_a|\le L\|w\|_{n,2}\), \(\sum_a|c_a|\le4(1+L\|w\|_{n,2})\), and the normalized rank-one operator bound. Iteration gives (12), and bounded feature increments give (13). With \(W_*=1+4TL(1+LR_T)\), choose a smooth readout cap equal to the identity on \([-W_*,W_*]\) and satisfying \(|\chi(w)|\le|w|\). The map \(\chi(w)p(z)\) is globally Lipschitz. Its own RMS estimates reproduce (11)–(13), so on the stated initial event this extension agrees with the intended cutoff program throughout the prefix. This makes the localization noncircular.
* **Initialization, moments, and symmetry.** There is one iid Gaussian matrix, independent iid Gaussian bottom pairs, and an independent readout; independent permutations of the two neuron populations preserve the graph. The dependency's operator-tail proof, Gaussian gradient-moment inequality, and graph derivative induction therefore apply with one matrix instead of two. For fixed caps they provide the all-order moments needed for its conditional empirical averaging and projection removal. This uses the bounded partial derivatives just checked, not an unproved moment theorem for \(\psi(z)q\).
* **Scalar feedback.** Predictions and learned coefficients use normalized quadratic contractions, followed by affine/polynomial scalar arithmetic and scalar-times-vector operations. In particular \(c=-2(f-y)\) is allowed. The oracle replacement argument in the dependency's Section 7 applies instruction by instruction; a current residual creates no implicit equation.
* **Singular queries and responses.** The dependency proves both-orientation conditioning, finite-rank projection removal, and auxiliary-query-noise removal. Its source/response formulas and final scalar coupling contain no inverse covariance. Their hypotheses are met by the capped maps above, including the startup zero and duplicate queries. The generic conditioning derivation does not require softplus, three layers, or a positive gate.

The actual readout is restored correctly. Indeed
\[
\mathbb E\|w_0\|_{n,2}^2=n^{-2},\qquad
\Pr(\|w_0\|_\infty>\varepsilon)\le2n e^{-n^2\varepsilon^2/2}.
\]
Together with the supplied matrix tail, the bounded initial event has probability tending to one. Coupling capped actual and zero-readout graphs gives, for fixed caps and graph, RMS discrepancies bounded by a finite constant times \(\|w_0\|_{n,2}\), through matrix actions, Lipschitz maps, contractions, and scalar arithmetic. Thus the limiting root is zero. Finite-width backward fields at time zero need not vanish. No uniform-in-mesh initialization claim follows.

The uncapping step also closes; the needed details are these. Construct the scalar law in causal order. Bottom features are bounded, and every reverse query has the form
\[
q_j^Q=\zeta_j^Q+\sum_l B_{jl}^Q H_l^Q.
\]
On compact sets of preceding coefficients, expressions and their formal first derivatives are bounded by fixed polynomials in the finite Gaussian tuple, uniformly in large \(Q\). This follows from \(|\tau_Q(q)|\le|q|\), bounded \(\tau'_Q\), bounded activation derivatives, and finite chain-rule induction. Moreover \(\tau_Q(q)\to q\) and \(\tau'_Q(q)\to1\) locally. Square-root coupling and dominated convergence pass both query second moments and expected first derivatives through the next instruction, even at a rank drop. The next selected coefficients then converge and are bounded. This is a causal induction, not an assumption that all coefficients are already uniformly bounded. No second derivative of the cap is needed for these first-response limits.

Consequently, for all sufficiently large \(Q\), the finitely many bottom reverse sources have uniformly bounded Gaussian variances and the feature shifts have uniformly bounded absolute values. Their RMS tails are bounded by \(C e^{-cK^2}\) for large \(K\); independence between the shift and its source is unnecessary.

For the finite-width uncapping comparison, let \(\Delta_{n,Q}\) collect the finitely many RMS state and scalar discrepancies. The split estimate (15), the rank-update difference estimate, and the other bounded-map estimates give constants \(C,d\), independent of \(K,Q,n\) on the bounded initial event, such that
\[
\Delta_{n,Q}\le C(1+K)^d\sum_j\left(
\|q_j^Q\mathbf1_{|q_j^Q|>K}\|_{n,2}
+\|q_j^Q\mathbf1_{|q_j^Q|>Q}\|_{n,2}\right),
\]
with an additional vanishing initial-discrepancy term if the zero-root comparison is combined with this one. The polynomial degree is finite because the graph is fixed. In particular, the large derivative of the bottom map costs a factor proportional to \(K\), not an uncontrolled dependence on \(Q\). The fixed-cutoff empirical theorem controls the tails using continuous majorants of the indicators. Taking width first, then \(Q\to\infty\), bounds the right side by \(C'(1+K)^d e^{-cK^2}\); finally \(K\to\infty\) removes it. This is a valid order of limits.

Bounded RMS norms and
\[
|\langle x,y\rangle_n-\langle\widetilde x,\widetilde y\rangle_n|
\le\|x-\widetilde x\|_{n,2}\|y\|_{n,2}
+\|\widetilde x\|_{n,2}\|y-\widetilde y\|_{n,2}
\]
transfer the displayed mixed second moments, including those of the first backward fields. The argument does not assert all-order raw finite-width moment convergence or empirical convergence of parameter Jacobians. The formal derivative convergence used to construct the scalar response coefficients was separately justified above.

## 3. Sources, complete memories, and the frozen-mask estimate

The unrolled forward and reverse rank terms give exactly \(M_A,M_B\) in (7), including the historical residual coefficient in each column. The supplied conditioning derivation generates a new source as a deterministic combination of previous sources in the same orientation plus an independent innovation. Thus \(G,\zeta^{(1)},\xi^{(2)}\) may be independent Gaussian groups in their separate population realization. This is not independence of evolved fields or an assertion about cross-population coordinate pairings.

Equations (8)–(9) correctly differentiate the entire explicit expressions with \(f,c,\lambda,A,B,\Gamma,\Sigma\) frozen. In particular the readout-history derivative is retained, the current \(D\) block is diagonal in formal sample slots, and no \(-2h\partial f\) term belongs here. The possibly nonzero \(S_{1a,0b}\) is consistent with \(\zeta_0=0\); neither that slot nor the formally distinct duplicate \(\xi_0,\xi_1\) slots may be discarded.

On the Gaussian-independent event \(\mathcal F\), both gates remain zero for every formal reverse source, so the frozen contribution to \(\mathbb E[Z(v^TH)]\) vanishes. Gaussian integration by parts and masked Cauchy–Schwarz give
\[
S\Sigma S^T\preceq\alpha\mathbb E[\mathbf1_{\mathcal F^c}HH^T]
\preceq\alpha\Gamma,\qquad D\Gamma D^T\preceq\Sigma.
\]
The derivative integrability follows from the preceding finite polynomial bounds. The raw query second moments, rather than centered feature covariances, are the correct Grams. Kernel annihilation gives the range inclusions; square-root conjugation gives (26). The constant is uniform in history length because \(\alpha\le4R/\sqrt{2\pi}<1\). No positivity of residuals is needed here: use step \(h\ge0\) and signed coefficients \(c_{kb}\) in the mask dependency. These estimates do not control mean-square sensitivities, statistical-selection derivatives, a variation of the zero readout root, or the complete feedback inverse.

## 4. Entire physical Euler segments and positive residuals

The segment calculation reevaluates features at interpolated parameters, as required. Norm convexity preserves \(R_T,B_T\) throughout the segment, and
\(\|\delta_a^{(1)}(u)\|_{n,2}\le mB_TR_T\) requires only an operator bound, not a coordinate bound on the reverse query.

Differentiating \(f_a=n^{-1}w^T\phi_2(W\phi_1(z_a^{(1)}))\) along the three updates in (2) gives precisely the three terms in (18). The middle term has two normalized pairings; the bottom term retains \(C_{ab}\). They form a Gram pairing of the correspondingly scaled gradient blocks, including the sample input vectors. Hence
\[
|\mathcal K_{ab}(u,k)|\le G_T^2
=L^2+(\beta^2+m^2B_T^2)R_T^2
\]
on the whole segment. Positivity of the mixed kernel or a Hessian estimate is not needed. Endpoint convergence alone transfers (20). For (21), fixed-\(u\) reevaluations are admissible appended finite graphs; compact-parameter Gaussian coupling gives continuous scalar contractions. The common bound on a high-probability event permits integration of truncated expected errors, followed by Fubini and Markov. Thus pointwise-in-\(u\) convergence suffices; no unproved uniform empirical convergence is invoked.

Exchange symmetry now gives \(|r_{k+1}-r_k|\le4hG_T^2|r_k|\). Starting from \(r_0=1\), with \(4hG_T^2\le1/2\),
\[
r_k\ge(1-4hG_T^2)^k\ge e^{-8G_T^2T}>0
\quad(kh\le T).
\]
The constants do not depend on the mesh or width; the width-first identification used to reach this inequality still does. This distinction is sound.

## 5. Support induction and ordinary-output bounds

For \(-1<\rho<1\), positive probability of all saturated sign quadrants implies \(K=\mathbb E[FF^T]>0\). Also \(J=\mathbb E[gg^T]>0\): a zero quadratic form would force \(c_1p(x_1)+c_2p(x_2)=0\) off the diagonal, hence everywhere by continuity, which forces \(c=0\). Startup gives only the prescribed relations \(H_1=H_0\), \(\delta_0=0\).

The alternating induction excludes further linear relations. Conditional on the past bottom sources and root, a positive reverse innovation enters the next bottom preactivation with matrix \(\lambda_{k-1}CY\operatorname{diag}\psi\). There is positive probability that both gates are positive: start strictly inside the bump and choose the finitely many preceding reverse innovations near the values cancelling their reverse answers. Conditional Gaussian full support and continuity give positive mass to this event. The displayed matrix is invertible there. Since no nonzero linear combination of two coordinatewise \(\phi_1\) outputs is constant on all of \(\mathbb R^2\), the new feature block has positive Schur complement relative to all past features.

The corresponding new top source has full conditional density. Its readout is \(\lambda_0d\) at time one and \((\lambda_0+\lambda_1)d\) at time two. At later times the newest arctan difference has a nonzero coefficient and, conditional on earlier sources and the other current coordinate, is strictly monotone. Thus the readout is nonzero almost surely. Nonconstancy of \(c_1p(z_1)+c_2p(z_2)\) then gives a positive backward Schur complement. These are conditional-variation arguments and exclude relations with the entire past, not just dependence within the new pair.

Accordingly (28) is valid under (27), with the stated separate condition for \(N=1\). The extra condition \(\lambda_0+\lambda_1\ne0\) is essential: the two coarse-step examples in Section 6 are correct. Fine-mesh residual positivity supplies all these conditions. On those supports, \((M_Au)_0=(M_Au)_1=0\) and \((M_Bv)_0=0\), proving preservation. The harmonic dependency's different-activation, \(\rho=-1\) leakage example does not contradict this result.

Equations (30)–(33) also check. In particular
\(2\sum_r|\lambda_r|a_r=a_k^2-\sum_r|\lambda_r|^2\le a_k^2\),
and \(|u_j|\le\sqrt{\Sigma_{jj}}\|u\|_\Sigma\) yields the memory row bounds. The sum has \(2(N+1)\) output coordinates, giving \(\sqrt{2(T+h)}\). These control ordinary weighted Euclidean outputs, not the covariance-output constants in (34).

## 6. Exact two-update Schur transfer

The startup derivative blocks are \(D_{10}=\lambda PY\), \(D_{11}=\lambda\operatorname{diag}(t)\); their learned terms vanish because \(\delta_0=0\). With \(\tau=\lambda\mu\), the resulting bottom increment is exactly (38), and Taylor expansion gives
\[
H_2^{(1)}=F+\tau L^{(1)}+O_{L^p}(\tau^2).
\]
All finite \(p\) are legitimate here because the finitely many Gaussian variables have all moments and the activation derivatives are bounded. Gaussian regression with the nonsingular root block \(K\), followed by square-root coupling of the conditional covariance, gives the scaled source pair \((X,E)\) and \(V_1>0\). Positivity follows from the independent \(V\) term on the two-positive-gate event.

The formal derivative is \(S_{21}=\mu J^{(1)}Y+O(\mu\tau)\); adding the learned term gives \(A_{21}=\mu(J^{(1)}+K)Y+O(\mu\tau)\). Hence (41) retains both contributions. Crucially \(\mathsf W_2=s d\) exactly, where \(s=\lambda+\mu\), so
\[
\delta_2-\frac{s}{\lambda}\delta_1
=s\tau L^{(2)}+o_{L^p}(s\tau),\qquad
\frac{s}{\lambda}=2-\lambda v_0.
\]
Subtracting only \(2\delta_1\) would leave the larger term \(-\lambda^2v_0g\). The candidate uses the correct subtraction. Conditional on \(X\), the innovation covariance in \(L^{(2)}\) is
\(\operatorname{diag}(dp'(X))V_1\operatorname{diag}(dp'(X))\), positive definite almost surely; thus \(V_2>0\).

A destination vector with zero early blocks has squared covariance norm determined by the inverse destination Schur complement. Prescribing the input block at time one costs minimally \(u_1^T(\lambda^2J)^{-1}u_1\) or \(v_1^TK^{-1}v_1\), with later blocks supplied by covariance regression. This proves (44), including the duplicate feature block and all supported extensions. Schur complements are unchanged by deterministic regression subtractions, so
\[
V_{1,h}/\tau^2\to V_1,\quad
V_{2,h}/(s\tau)^2\to V_2,\quad
\Sigma_{21}/(s\lambda)\to J.
\]
The prefactors cancel because \(\tau=\lambda\mu\). Both finite, strictly positive limits in (46) follow. No factor of two or residual-feedback term is missing.

## 7. Quantitative audit of the \(361/220\) constant

At \(\rho=0\), \(K=kI\). Every numerical inequality used in Section 9 is valid analytically:

* \(p_0<1/5\), \(a<1/35\), \(q_4<1/250\), \(k<1/100\), \(\beta^2<5k/4\), and \(b=a+k<1/25\) follow from the stated Gaussian density, saturation, and exponential bounds.
* The centered independent arctan remainders contribute at most \(\sqrt{60}k^{3/2}/3\) to the approximation of \(e_+^Tg\). The gate remainder contributes \(\sqrt{24}k^{3/2}\), since \(\mathbb E[(X_1-X_2)^2(X_1^2+X_2^2)^2]=48k^3\). Their sum is less than \((15/2)k^{3/2}\). Thus \(\sqrt{j_+}>(2-15k/2)\sqrt k>1.9\sqrt k\), proving (48).
* \(1-4k\le a_0\le1\) makes all absolute entries of \(T_0\) at most one. Independence of \(V,G\) removes the \(V\) cross term; evenness of the gate and oddness of the features remove the weighted \(F_1F_2\) term. Hence \(\mathbb E|L^{(1)}|^2\le2q_4(3k+\beta^2)<17k/500\), proving (49). The covariance of the centered Gaussian \(E\) is indeed this raw Gram.
* Regressing each \(E_a\) onto independent \(X_-,X_+\) gives the three variance multipliers \(36k^2,12k^2,8k^2\) under the weight \(2X_-^2(X_-^2+X_+^2)\); cross terms vanish by parity. Thus (50) holds without assuming \(E\) independent of \(X\). The \(E\) contribution to \(e_+^TL^{(2)}\) has norm at most \(\sqrt{306/125}\,k^{3/2}\).
* \((p'p)'=(-2+10x^2)/(1+x^2)^4\) has absolute value at most two. The remaining contribution has norm at most \(\sqrt{240}\,b k^{3/2}\), using \(\mathbb E(X_1-X_2)^6=120k^3\). Finally \(\sqrt{306/125}<157/100\) and \(\sqrt{240}/25<63/100\), so their sum is strictly below \(11/5\).

The norm test is the generalized Rayleigh quotient
\[
\|V_2^{-1/2}JYK^{1/2}\|^2
\ge\frac{e_+^TJYKYJe_+}{e_+^TV_2e_+}
\ge\frac{k j_+^2}{\mathbb E(e_+^TL^{(2)})^2}.
\]
Here the numerator is \(k j_+^2\) because \(K=kI\), \(Y^2=I\), and exchange symmetry makes \(e_+\) an eigenvector of \(J\). Equations (48) and (51) give the strict lower bound \(361/220>1.64\), hence eventually \(8/5\), as claimed.

## 8. Fixed-horizon consequence and fixes

For \(h=T/N\), sufficiently large \(N\) gives whole-history support preservation. Padding a destination test for the first three times with zeros leaves both the numerator \(z^TM_B\Gamma M_B^Tz\) and denominator \(z^T\Sigma z\) equal to their prefix values: causality prevents later input columns from entering those rows, and the prefix law is unchanged by extending the program. Therefore the whole-history norm dominates the prefix norm and (53) follows.

This is a lower bound exceeding one for the learned reverse memory. It rules out its contraction and a fine-mesh bound vanishing with a short physical horizon. It proves neither divergence nor failure of larger finite covariance-norm bounds, and says nothing decisive about cancellations in the complete feedback product or its inverse.

**Required fixes for the stated modular result:** none. The scope qualification at the start of this review is essential: an original-raw-GD or simultaneous-limit theorem would require additional inputs and proofs and does not receive PASS here.

**Optional presentation improvements:** explicitly require the proof cap to be bounded by \(2Q\), as in the supplied cap construction; display the finite-degree stability inequality from Section 2 of this review; and spell out the conditional-variation argument against relations with all past blocks in the support proof. These make already valid steps easier to audit. They are not substitutes for the checks above and are not additional theorem hypotheses.
