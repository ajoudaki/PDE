# Independent complete-proof audit

Verdict: **PASS** for the complete theorem, at the candidate hashes recorded below. No mathematical blocker remains in the argument needed for the claimed exponent-ten theorem.

This audit used the rigorous-math skill. I read CONTRACT.md, CANDIDATE_HASHES.json, and all four candidate mathematical files in full. I verified every candidate and dependency hash and inspected the original mathematical arguments needed for the affine estimates, Gaussian source identification, canonical actions, cap removal, physical conversion, uniqueness/restart, finite GF/raw-GD limits, velocities, path laws, nonaffinity, and initial motion. I did not read README files, review/status/evidence files, historical or sibling reviews, or the auxiliary NORMALIZED_GATES_AND_PRIMALS.md. The latter is not a premise of this verdict. No proof edits, trajectory experiments, delegation, or commits were performed by this reviewer.

The main assembly and response note received the explicitly identified presentation corrections during this audit. I checked those changes and the resulting final hashes. The verdict applies to the final versions, not to an earlier manifest.

## 1. Claim and quantifiers audited

The claim is the full original odd two-input L3 theorem for every

\[
0<\delta\le1,\qquad |\rho|\le1-\delta,\qquad
y_1,y_2\in\{-1,1\},\qquad \tfrac12\le a\le1,
\qquad 0<e\le c_{\rm poly}\delta^{10}.
\]

The coefficient is exactly the previous numerical prefactor

\[
c_{\rm poly}=\min\{1/4,c_*,10^{-70}H^{-400}\},
\qquad H=10^{30}(1+C_0+C_z+C_g+\exp(1410))^4.
\]

This yields the requested convex mixture with \(a=1-\theta\), \(e=\theta\), for every \(0<\theta\le c_{\rm poly}\delta^{10}\). The gain rectangle, all label choices, the actual raw metric, independent Gaussian initialization, finite random readout, simultaneous raw GD at step \(n^{-2}\), and original observables are preserved. Width convergence is along the full sequence in probability for each fixed dataset and each fixed finite physical interval. Neither uniformity over datasets nor uniformity over the infinite physical half-line is inferred. The same rectangle also retains the original Gaussian-energy-normalized family, since its nonlinear coefficient is smaller than its defining positive parameter and its gain lies in the rectangle.

## 2. Affine geometry and source certificate

I checked the actual scale

\[
v=(1+y_1y_2\rho)/2,\quad r=\sqrt v,\quad \lambda=a^3r,
\quad M^4=3/(\sqrt2\lambda).
\]

It satisfies \(M>1\), \(S\le2/\lambda\le M^4\), \(r=3M^{-4}/(\sqrt2a^3)\), and \(M\le24^{1/4}\delta^{-1/8}\). The certificate's lower-case \(m\) is this actual \(M\); its upper-case \(M\) is only the dataset-uniform envelope. The proof does not replace the actual \(r\) by a power of that upper envelope.

The original AFFINE_POLYNOMIAL_BOUNDS.md proves the normalized four-component gradient system, its operator balance identities, the bound \(F\ge\|D\|^4/\sqrt2\), its endpoint existence, and logarithmic integrated curvature. Its radius-one raw tube estimate differentiates the affine field and retains its factor \(\lambda\). This supplies the propagator \(CM^5\), raw discrepancy \(CeM^{12}\), preactivation discrepancy \(CeM^{14}\), and learned-moment density discrepancy \(CeM^{15}\). The last estimate uses a difference of two inner products, with actual feature/backward factors. Summing the learned backward moment errors pays the additional duration \(M^4\).

The joint sample/time normalization in AFFINE_SOURCE_CERTIFICATE.md was checked directly. With \(Q=\frac12\left(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\right)\), \(S_0=\operatorname{diag}(r,r_-)\), and \(\Delta t_j=\lambda h_j\), the four transformed learned moments have exactly the factor \(\Delta t_j\). In particular the original factor \(h_j/2\) becomes \(h_j\) after applying \(Q\) on both fields and \(Q^{-1}=2Q^T\) to the coefficient block. No missing factor two, variance factor, gain, or time derivative occurs in the normalized equations.

The inactive forward formulas and vanishing affine backward sector follow from the original conditional Gaussian freezing proof, not from an unjustified claim that bounded operators preserve Gaussian independence. The finite affine learned increments have bounded Frobenius norms and act negligibly, in normalized mean square, on the independent inactive root. Strong affine Euler limits preserve the resulting identities and Gaussian laws.

The response bounds are connected to actual formal coefficients by the fixed-program independent Gaussian probe identity in TWO_SAMPLE_SOURCE_BASELINE.md §§5–7. A perturbation at time \(j\) changes the next state with its factor \(h_j\); the original source law identifies the pairing with the independent probe at fixed amplitude and mesh, and amplitude continuity gives the formal derivative afterwards. The new first-preactivation and top-backward probes are admissible additive coordinate instructions. I checked their affected updates and their output costs, including the direct identity for each resolvent orientation and the absence of a direct term in the top forward transfer. Thus no width-limit derivative interchange or unsupported identification with a raw tangent is used.

Conversion back to original time supplies precisely the needed forward strict densities, backward rows, resolvent rows, and top strict transfer. Baseline coefficient blocks are sample diagonal, so their diagonal similarities do not introduce an input condition number. The explicit prefactor ledger allows every required affine input to have coefficient at most the old \(H\). Its largest stated numerical envelope, \(10^{25}\exp(1410)\), is below \(H\).

The intrinsic beta scales have gaps bounded below by \(H^{-1}M^{-2}\). Homogeneity, the original bounded-ball continuation interval, and the extended integrated Hessian bound put all these references on the same feature interval. Fixed-mesh Wick positivity and the unchanged integration operators justify differentiating with respect to beta at fixed mesh. Convexity of the nonnegative polynomials gives the beta-derivative bound throughout the required enlarged family.

## 3. Exact coefficient comparison and both sample sectors

The scaled affine equation is the additive equation

\[
\mathcal C_\beta=\beta^2\mathcal T_0(\mathcal C_\beta)+\mathcal M_\beta.
\]

The final assembly now displays that addition correctly, consistently with both companions. Differentiating its \(A_3\) equation yields

\[
\partial_\beta A_{3,\beta}
\ge2\beta^3a^2R_\beta F_\beta L_\beta.
\]

This gives the required bounds on \(F_\beta L_\beta\) and \(R_\beta F_\beta\) without multiplying separate coarse row/density bounds.

For arbitrary nonnegative causal row errors \(J_2,J_3\), including current diagonals, I checked the supersolution definitions and the identities

\[
R^*=(I-V_\beta J_3)^{-1}R_\beta,
\qquad W^*-W_\beta=a^2L_\beta J_3R^*,
\]
\[
F_\beta(B_2^*-B_{2,\beta})F_\beta
=F_\beta J_2F_\beta+
a^2(F_\beta L_\beta)J_3(R^*F_\beta).
\]

The backward inequalities are exact. The strict/row/strict inequality
\(|UQV|_d\le S|U|_d|Q|_r|V|_d\) follows by summing the middle row and preserving the final factor \(h_j\). It does not require a smallest-step bound. The first forward relative error has order \(M^{30}q\), which the \(M^{-2}\) beta margin absorbs at order \(q\le cM^{-32}\). The backward excess costs \(M^{22}q\); the complete outer radius \(M^{-12}\) therefore needs \(q\le cM^{-34}\). The numerical ledger verifies the sufficient threshold \(q\le H^{-16}M^{-34}\), including strict interior margins.

The inactive sector is not discarded. Since its affine backward equations vanish, its forced backward rows are \(O(q)\), and its forward added density is \(O(M^4q)\). The explicit \(u,w\) in the numerical ledger dominate both forward equations. The stated thresholds make these margins strict as well.

Exchange equivariance applies to each deterministic covariance, learned coefficient, and expected formal derivative by induction through the actual finite source program. Therefore the actual coefficient blocks commute with sample interchange and are diagonal in the mean/contrast basis. Individual random gates are not assumed diagonal; REFINED_RESPONSE keeps their full two-by-two actions. Physical nonsymmetric competitors are handled later by raw-state comparison, so the source-sector argument imposes no symmetry hypothesis on uniqueness.

For signed coefficients the finite causal polynomial bound \(|\mathcal T_0(\mathcal C)|\le\mathcal T_0(|\mathcal C|)\) is valid. The order \(A_{2,k},A_{3,k},B_{3,k},B_{2,k}\) is the original query order and handles the current middle return. It justifies comparison with the positive supersolution.

## 4. Same-array source values and exact derivative identity

I independently substituted \(\delta=aq+ed\), \(h=aZ+e\arctan Z\) into all three source populations. The three displayed value equations in REFINED_RESPONSE (D) are exact at the actual deterministic arrays. In particular the bottom and middle terms \((F/a)\zeta^1\), \((V/a)\zeta^2\), and their nonlinear factors \(F/a^2,V/a^2\) have the correct gains. The top equation includes both \(d_3\) and \(aEH_c\arctan Z_3\).

The Gaussian source standard deviations come independently from the primal bounds: orders \(1,M^2,M,M,M^2\) for the initial first root, \(\zeta^1,\xi^2,\zeta^2,\xi^3\). Arbitrary within-group correlations and singularities are allowed. The same-array resolvents give preactivation orders \(M^{11},M^{12},M^{13}\) and incoming orders \(M^{22},M^{21},M^{17}\), all times \(\sqrt p\). Only the supremum of deterministic \(L^p\) norms is used. The self-term coefficients have orders \(eM^{20},eM^{20},eM^{17}\) and can be absorbed uniformly in \(p\). The resulting subGaussian bounds do not assume that a merely bounded \(L^2\) action preserves Gaussian tails.

For the common local system, freeze the deterministic arrays and covariances, and put

\[
J=DZ,\quad R=(I-a^2KB)^{-1},\quad U=RK,
\quad L=(I-a^2BK)^{-1}=I+a^2BU.
\]

With \(G=aI+\Delta G\), \(V_{\rm gate}=aI+\Delta V\), and

\[
P=L_{\rm gate}+a\Delta VB+aB\Delta G+\Delta VB\Delta G,
\]

direct differentiation gives

\[
J-J_{\rm aff}=U(\Delta V I^\zeta+PJ),
\]
\[
\Delta(D\delta)
=\Delta V I^\zeta+PJ+a^2B(J-J_{\rm aff})
=L(\Delta V I^\zeta+PJ).
\]

This verifies the crucial cancellation exactly, including operator order and current time blocks. The argument uses the backward resolvent \(L\) directly. It does not bound \(B(J-J_{\rm aff})\) separately and lose extra powers of \(M\).

For one bottom/middle transpose source at \(j\), the direct preactivation derivative is zero through time \(j\), and all later forcing has the factor \(h_j\). For a full middle/top forward-source row, the current identity and all earlier slots are included in its row norm. Strictness of \(U\), the complete backward row bound, and a running deterministic causal majorant give the displayed derivative envelope. Its random exponent is a weighted time sum of \(Q_r\), not a random supremum.

For \((u,b,q)=(5,11,22),(7,9,21),(9,4,17)\), the stochastic integrated powers are \(31,32,30\); the deterministic integrated powers are \(20,20,17\). Weighted Jensen is valid with arbitrary source-time correlations, and the subGaussian estimate controls the required envelope moments. Hölder retains source-time and terminal incoming factors whenever they occur.

The forward defects have density powers

\[
2\cdot5+4+22=36,
\qquad 2\cdot7+4+21=39.
\]

The complete backward row defects have powers

\[
11+11+21=43\quad(B_2),
\qquad 11+11+17=39\quad(B_3).
\]

The current returns agree with the original exact source rules, including the \(B_{3,kk}\mathbb E[V_{2,k}G_{2,k}]\) term in \(B_{2,kk}\). The estimate of the complete expected derivative row follows from its expected absolute row. Learned backward moments add only \(eM^{19}\). Thus the claimed forcing is the full required forcing, not an estimate only for a selected response component.

The corrected outer-box statement expressly excludes backward strict-density persistence for arbitrary backward row errors. This is mathematically necessary: such errors may concentrate on arbitrarily small past steps. Only the forward strict densities and complete backward/resolvent rows are used in the subsequent proof, and these are preserved by the stated resolvent identities.

## 5. Numerical closure

The response ledger is sufficient with the unchanged numerical \(H\). Outer transfer bounds cost at most the stated \(H^2\) envelopes; the value inequalities and absorption give incoming \(L^p\) constants \(H^{10}\) and subGaussian constants \(H^{11}\). The derivative rate, duration, and subGaussian constants produce \(H^{18}\) before fixed-moment numerical factors. Hence \(eH^{22}M^{32}\le1\) supplies the required smallness and envelope moments. The forward defect products fit \(H^{20}\), feature defects fit \(H^{21}\), and backward products fit \(H^{19}\). Combining them with the independent learned-moment errors is safely bounded by

\[
q\le H^{30}eM^{43}.
\]

The final arithmetic uses

\[
M^{80}\le24^{20}\delta^{-10},\qquad 24^{20}<H,
\]
\[
eM^{80}\le10^{-70}H^{-399},
\qquad eH^{22}M^{32}\le10^{-70}H^{-377}<1,
\]
\[
qM^{34}\le H^{30}eM^{77}
\le10^{-70}H^{-369}<H^{-16}.
\]

The direction of each implication is correct because \(M>1\). The factor \(c_*\) also gives \(e\le c_*\delta^{7/4}\), since \(\delta^{10}\le\delta^{7/4}\). Thus the old primal tube, endpoint, and regression conditions hold without invoking the old source threshold.

At every fixed cap and sufficiently fine fixed mesh, amplitude continuity follows from the causal finite source construction and continuity of Gaussian covariance square roots, including rank drops. The zero-amplitude program lies strictly inside the outer box. At a proposed first exit the response estimate and numerical threshold apply, while the inner beta supersolution gives strict forward and backward margins in both sectors. This excludes exit. No probability theorem is applied to a transcript growing with width.

## 6. Complete theorem bridge

I checked the bridge against the actual original arguments, rather than importing the old exponent-800 theorem as a black-box threshold.

1. **Canonical state and actions.** The fixed-program Gaussian conditioning proof retains both matrices and orientations, uses full input second moments, and preserves distinct formal slots at singular covariance. Query-noise regularization is removed at fixed program length. Countable consistent programs, finite Gaussian operator bounds, and finite adjunction produce the common generated \(L^2\) action spaces and actual adjoints. The gain/offset change satisfies the same fixed-cap coordinate hypotheses.
2. **Cap removal and strong regularity.** The original asymmetric gate comparison has one factor \(R\) multiplying a forward-state discrepancy and Gaussian tails only from the reference incoming fields. The new bounded primal paths and subGaussian source bounds therefore give \(C\exp(C(1+eR)S-cR^2)\to0\). State and direction convergence yield an autonomous uncut strong \(C^1\) feature path, with the endpoint margin intact.
3. **Global physical population flow.** Exact population exchange symmetry gives the scalar folded prediction. The first hit of one precedes the feature endpoint. Bounded feature derivative implies divergence of \(\int ds/[2(1-g(s))]\) at that hit. This constructs all finite physical times on one trajectory. The capped clock requires no cap-gradient or monotonicity assertion. The original uncut radial calculation is also valid after strong construction, and retains the original initial projected-kernel lower bound and loss decay consequence.
4. **Nonsymmetric uniqueness and reached-state restart.** The physical asymmetric estimate keeps each competitor's two residuals and needs only its bounded primal sizes. No source tails or exchange symmetry are required of that competitor. Comparing to the capped reference and sending the cap to infinity proves uniqueness. Starting at a reached time includes the already controlled initial discrepancy and proves restart. Arbitrary-state existence outside the reached states is not asserted.
5. **Finite GF and prescribed raw GD.** Fixed-cap, fixed-mesh Gaussian identification uses the actual residual feedback and exact rank-one unrolling. Finite current operator bounds follow from update-factor norm sums, not trained operator-norm convergence. Width-independent stopped Euler estimates remove the auxiliary mesh. The same-width asymmetric comparison then removes the cap. The interpolated raw GD direction is the uncut field at its preceding node, so the extra fixed-cap comparison defect is \(C_{R,T}n^{-2}\). This preserves simultaneous raw updates and the initialized iid readout of variance \(n^{-2}\). These arguments establish the full width sequence jointly for GF and GD.
6. **Velocities, actions, kernels, and paths.** The original velocity proof first truncates the product queries, identifies their forward Gaussian sources and transpose responses, and removes that truncation at fixed cap. The deterministic hidden-velocity estimate uses one reference-velocity truncation factor. For cap removal the uncut velocity has a compact continuous \(L^2\) time image and therefore uniform tails. Width is taken first at fixed cap/truncation; the cap is removed at fixed truncation, and truncation is then removed. This yields the stipulated uniform-time and finite-collection same-layer joint \(\mathcal W_2\) velocity laws, second moments, and integrated squared speeds. Both action orientations and adjoints on generated probes survive. Products of converging \(L^2\) fields give every entry of all four raw kernels. The path interpolation bound \(\|x-I_hx\|_\infty^2\le4h\int|x'|^2\), followed by the speed bound and fixed-grid joint law, gives the original path-space \(\mathcal W_2\) conclusion. No cross-layer neuron pairing or continuous-path velocity law is added.
7. **Nonaffinity and initial motion.** The original affine balances and inactive freezing give absolute reference variance bounds; the explicit Hermite regression bound and the 1-Lipschitz square-root regression residual give \(e^2\eta_*/4>0\) throughout the feature interval and hence at every finite physical time. The original odd-family initial-motion proof uses full positive-definite transpose-source second moments, both reuse returns, actual adjoints, and exchange symmetry. It applies for every positive \(e\) in the gain rectangle, supplies every hidden-block/sample/layer acceleration, and gives the changing projected kernel. It imposes no additional amplitude threshold.

All hypotheses needed by these bridges are supplied by the audited candidate at \(e\le c_{\rm poly}\delta^{10}\). The result is consequently a complete theorem improvement, rather than a conditional source lemma.

## 7. Verified SHA-256 identities

Every candidate hash below matched CANDIDATE_HASHES.json at the final check:

| Candidate | SHA-256 |
|---|---|
| PROOF.md | `37b9e8a27135b95b8dffe05fe2b734229fadedc98bc1609259e365dbb2aeba37` |
| AFFINE_SOURCE_CERTIFICATE.md | `bc55c0f8e25de1f3a4316fe36e86afa25c9486e014192f2eb818358909b048eb` |
| REFINED_RESPONSE.md | `3622a0f903cd51b712d1d524a140d834471b5eb588611f059535c41f6efd2332` |
| POSITIVE_SUPERSOLUTION.md | `e2be183521919ce69c7ae41b81f5cd78566c5430a78c2408687f52f1b6d86774` |

All 19 dependency hashes matched DEPENDENCY_HASHES.json, resolved relative to the candidate directory's parent:

| Dependency | SHA-256 |
|---|---|
| two_sample_odd_activation_theorem/PROOF.md | `a4d6ed0ee99a1e111b5eba068f2219cf561a2281b1828b26227aca7a0a54a050` |
| two_sample_odd_activation_theorem/AFFINE_CORE.md | `634dd3bbc35436e9d1760bee5c11cbf2124b3c42e8920a1bf3a4fcbb15039711` |
| two_sample_odd_activation_theorem/SOURCE_AND_LIMIT_BRIDGE.md | `2a140f2a5a39f911b5c2ca51bc79102d20e9209f1450d38005360c88103f6e77` |
| two_sample_odd_activation_theorem/INITIAL_MOTION_AND_NORMALIZATION.md | `c96316fdc481ef3f9e6fc402514ca9b45bcff12e199023505fbbb86d4e15bf24` |
| two_sample_odd_activation_theorem/sources/ANGLE_SPECIFIC_THEOREM_ASSEMBLY.md | `27b2579f27ec14319dd39a93a4942d7b6463860648462d5ccb31b662c7725b75` |
| two_sample_odd_activation_theorem/sources/CONTRACT.md | `e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd` |
| two_sample_odd_activation_theorem/sources/FIXED_CAP_VELOCITY_BRIDGE.md | `a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0` |
| two_sample_odd_activation_theorem/sources/INITIAL_FEATURE_LEARNING.md | `bd81de0a7ad0cb9bdd1f27f89961f4a3b7a7da6914456ae08596a882fa2ec351` |
| two_sample_odd_activation_theorem/sources/L3_LOCAL_COMPLETE_PROOF.md | `f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4` |
| two_sample_odd_activation_theorem/sources/NONLINEAR_RESPONSE_PERTURBATION.md | `ef0ea077406a27307bc84e045feebf5099f6f81883bdfed41508035fe4559568` |
| two_sample_odd_activation_theorem/sources/PREVIOUS_TWO_SAMPLE_PROOF.md | `2891b892667396d64bd747689bcd59aa7ca3ffd224d3579fc3407bca0b623f9a` |
| two_sample_odd_activation_theorem/sources/PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md | `99eb60a64df1bbf4d8b70f351198abced9ef7eaeacf9b39c3997da5700a8f066` |
| two_sample_odd_activation_theorem/sources/SYMMETRY_RADIAL_CLOCK.md | `40882fc19e44b4b9245156595bb1071bd4de6007d619fada54c9fce7c37903f4` |
| two_sample_odd_activation_theorem/sources/THREE_SAMPLE_CONTROLLED_RESPONSE_LEMMA.md | `49da0f68047b4f516d3ad3c94b7112259838bcebf68e2296a948364232842789` |
| two_sample_odd_activation_theorem/sources/TWO_SAMPLE_SOURCE_BASELINE.md | `a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f` |
| two_sample_odd_activation_quantitative/PROOF.md | `0a7dbd32cb9cc291e706813b59c0142394e6f9532244e52c21a5ab5d89ed4d02` |
| two_sample_odd_activation_quantitative/AFFINE_POLYNOMIAL_BOUNDS.md | `8387e2f253063c139dacb282ca9f2372478521f54b33a9ef6c8dbd83f2b521ca` |
| two_sample_odd_activation_quantitative/POLYNOMIAL_RESPONSE_LEMMA.md | `51b0f717b33ed618219e086d32b16a95ef4253892171597d1805dd9d37a64f7f` |
| two_sample_odd_activation_quantitative/OLD_THRESHOLD_AND_NONAFFINITY.md | `c63753a83e832793c886b8ae8c122e30e0c01864b86a1a5dc9bee030852f9210` |

Final assessment: **PASS, complete theorem at the verified final hashes.** The exponent-ten conclusion uses the same explicit prefactor and all original model, initialization, optimizer, observable, uniqueness/restart, and limit quantifiers.
