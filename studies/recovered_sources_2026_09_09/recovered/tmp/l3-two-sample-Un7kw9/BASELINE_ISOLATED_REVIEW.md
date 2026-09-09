# Isolated adversarial review of the two-sample baseline lemmas

Date: 2026-09-05.

**Verdict: PASS for both candidates, within the exact scopes below.** I found no mathematical gap that blocks their stated baseline conclusions. This is not a certification of the nonlinear two-sample population/GF/exact-GD theorem or of one fixed nonlinear activation working for every angle.

## Reviewed versions and isolation

The candidate SHA256 hashes are:

| Candidate | SHA256 |
| --- | --- |
| `TWO_SAMPLE_SOURCE_BASELINE.md` | `a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f` |
| `SYMMETRY_RADIAL_CLOCK.md` | `40882fc19e44b4b9245156595bb1071bd4de6007d619fada54c9fce7c37903f4` |

Both candidates are in `/tmp/l3-two-sample-Un7kw9/` and were read completely. I personally read `/etc/codex/skills/solve-math-rigorously/SKILL.md` completely before the audit. I also read the complete `CONTRACT.md` and the relevant finite-program/common-space portion, lines 211–548, of `/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/L3_LOCAL_COMPLETE_PROOF.md`.

Dependency hashes:

- `CONTRACT.md`: `e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd`.
- `L3_LOCAL_COMPLETE_PROOF.md`: `f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4`.

The optional `OFFSET_ARCTAN_GLOBAL_THEOREM.md` was unnecessary and was not inspected. No other research, history, or reviews were inspected. No agents or numerical experiments were used. The candidates were not modified.

## Exact scope of the verdict

| Candidate | Verdict and certified scope |
| --- | --- |
| `TWO_SAMPLE_SOURCE_BASELINE.md` | **PASS.** Fixed finite-mesh source identification for its specified nonlinear-part clipped programs and for the uncut affine program; equations (26)–(29) conditional on P(B,S); conversion of a population Euler bound to P(B,S); and conversion of a bounded affine flow into such bounds for sufficiently fine meshes. Both label patterns and every fixed −1 ≤ ρ < 1 are included. |
| `SYMMETRY_RADIAL_CLOCK.md` | **PASS.** Equivariance of suitably symmetric clipped Euler programs, symmetry of their deterministic population limits, radial coercivity with the stated strong regularity and zero initial readout, conditional nonlinear continuation/clock statements, and unconditional construction of the affine scalar-feature baseline through any fixed target b > 1, with positive hidden variances and positive arctangent affine-approximation error. |

The first verdict does not turn a fixed-mesh theorem into a growing-mesh width limit. The second does not supply existence at arbitrary reached nonlinear population states: the candidate explicitly retains that hypothesis where continuation requires it.

## 1. Raw normalization, finite conditioning, and same-time sample slots

The raw first-layer metric gives

\[
w'=\frac1d\sum_b c_b\delta_b^{(1)}x_b,
\qquad (z_a^{(1)})'=\sum_b c_b\rho_{ab}\delta_b^{(1)},
\qquad c_b=y_b/2.
\]

Thus the candidate retains the required cross-sample geometry. There is no inversion of the input Gram matrix, including at ρ = −1. The four kernel blocks in source equation (3) and symmetry equations (21)–(22) are the corresponding parameter-gradient Gram blocks. In particular the first block has the factor ρ_ab, and the projected feature kernel is yᵀKy/4.

The relevant finite-program dependency is sufficiently general for this application. Its lines 299–377 cover deterministic scalar coefficients, independent Gaussian matrices reused in both orientations, independent iid root tuples with finite second moments, and globally Lipschitz C¹ coordinate instructions with bounded first derivatives. The proposed forward map and fixed-R backward map satisfy these conditions: the latter has partial derivatives bounded by 2eR and 1+e. For the affine case all coordinate maps after freezing contractions are affine. The root may contain both input projections, even when their covariance is singular.

Learned rank terms can be frozen causally because their contractions involve nodes already constructed. At a fixed transcript, bounded matrix norms, the rank-one difference estimate, and convergence of those contractions transfer the oracle law to the feedback program. This uses finite induction, not a mesh-uniform estimate. The dependency's independent query-input regularization and zero-noise continuity address singular Grams without convergence of pseudoinverses.

I checked the two-sample causal order in source lines 347–362 and the derivative equations (12)–(16). Both current forward sample queries precede both corresponding transpose queries. Correlation of current Gaussian sample sources is encoded in their covariance, not in a formal derivative of one source with respect to another. At the top, C_k depends only on earlier times, so

\[
D^{(3)}_{ka,kb}=\mathbf1_{a=b}\,\mathbb E p^{(3)}_{k,a}.
\]

Differentiating the middle backward instruction then gives exactly

\[
D^{(2)}_{ka,kb}
=\mathbf1_{a=b}\mathbb E p^{(2)}_{k,a}
 +D^{(3)}_{ka,kb}\mathbb E[v^{(2)}_{k,a}d^{(2)}_{k,b}].
\]

The return through the other matrix is included. Its current off-diagonal entries vanish for this Euler schedule; earlier-time blocks remain full. No sample-independence assumption is being made. At e = 0 both current backward response blocks vanish. The learned-rank coefficients have h_j c_b factors; the response coefficients correctly have no additional label factor.

## 2. Gaussian probe and off-support response identity

Source lines 629–739 provide a valid identification, rather than assuming a finite-network Jacobian trace formula.

Fix a mesh and deterministic slot weights α. Insert εα_ja g immediately after the chosen matrix-answer slots, with one independent standard Gaussian vector g in that population. The perturbed calculation is itself an admissible finite program. Its marginal scalar construction uses its own deterministic response/learned coefficients and source covariance parameters. Those parameters may change with ε. Its centered Gaussian source groups remain independent of the extra root G; the complete trained answers need not be independent of G.

For the affine model, after these deterministic parameters are fixed, every scalar coordinate is affine in its local Gaussian roots and source groups. If T_V,ja(ε) is the formal coefficient of the named source η_ja, the only explicit occurrences of G enter at exactly those source slots. Consequently

\[
V^\varepsilon=U^\varepsilon+
 \varepsilon\Big(\sum_{j,a}\alpha_{j,a}T_{V,ja}(\varepsilon)\Big)G,
\qquad U^\varepsilon\ \text{independent of }G.
\]

This proves equation (24), including its normalization. Differentiating with respect to G does not differentiate deterministic coefficients with respect to ε. Such a derivative is neither needed nor asserted.

At fixed ε, empirical second-moment convergence identifies the finite pairing with E[GV^ε]. At ε = 0 the pairing with the unperturbed output vanishes in probability: conditionally its variance is ||V_n^0||_n²/n. Finite-network stability and Cauchy–Schwarz therefore imply

\[
\left|\sum\alpha_{j,a}T_{V,ja}(\varepsilon)\right|\le C
\]

after taking width to infinity. Causal affine coefficient/second-moment recursion is continuous in ε, including at singular covariance; it contains no inverse covariance. Sending ε to zero proves (25). Taking α to be the deterministic signs of the unperturbed coefficients gives the absolute row sum.

This argument genuinely tests the declared off-support convention. If two unperturbed query answers coincide, their two inserted errors may nevertheless differ. The named expressions still contain two formal arguments, and the continuous perturbed coefficient recursion selects those arguments. It is not restricted to perturbations tangent to the unperturbed Gaussian support. An assertion of this kind would not follow merely from invariance of contracted responses, but the candidate supplies the additional probe argument required here.

## 3. Mesh-uniform estimates and the primal premise

I checked the constants against source equations (19)–(22). With b = 2B, the four affine vector-field component Lipschitz bounds are b², 2b², 3b², 3b² in the sum/max state norm, giving L = 9b² = 36B². The intermediate-answer forcing constants are respectively 2b, 1, 3b, 1 for middle forward, top forward, middle transpose, and bottom transpose forcing.

The bootstrap for the forced state is valid: the unforced state is bounded by B, ||g||_n ≤ 2 with probability tending to one, and a fixed sufficiently small ε makes the accumulated state difference less than B/2. Induction therefore keeps the forced trajectory within the ball where the estimate was proved. No bound on a perturbed primal trajectory is silently added to P(B,S).

Discrete Gronwall yields κSE|ε|||g||_n, with E = exp(36B²S). A perturbation at one past time enters the state update with h_j, giving κh_jE instead. The output Lipschitz constants then give exactly the four row bounds in (26):

\[
SE,\qquad 24B^2SE,\qquad 8B^2SE,\qquad SE.
\]

The indicated outputs have no direct current-source term. For (27), the extra 1 is precisely the direct current forward-source coefficient. Cauchy–Schwarz applied to the learned contractions gives (28)–(29), including the factor |c_b| = 1/2 for individual entries. A 2-by-2 block whose entries are bounded by A_*h_j has both row-sum norm and Euclidean operator norm at most 2A_*h_j. Thus the stated block constants are valid too.

These bounds are uniform over meshes satisfying P(B,S); neither a lower bound on step sizes nor covariance conditioning enters. Width convergence is used at each fixed mesh, as the candidate states.

The population-to-finite conversion in (31)–(32) also checks out. Unrolling learned matrices and using convergence of the finitely many update-factor norms gives initial bound 10 plus 2SB_0³ or 3SB_0³. This does not assume operator-norm convergence of trained matrices. The proposed B = 11+B_0+4SB_0³ supplies sufficient slack.

Finally, a bounded continuous affine flow supplies a uniform Euler bound only for sufficiently fine meshes. The local error 45b⁵h_j² is (1/2)(9b²)(10b³)h_j², and its Gronwall sum gives the candidate's mesh-error estimate. No arbitrary coarse-mesh conclusion is justified or claimed.

## 4. Symmetry without uncut uniqueness

The reflection Q exchanges the inputs because they have equal norm and ρ < 1; it remains defined at ρ = −1. Transforming the first weight block by Q and the readout by τ = y_1y_2 exchanges sample features and multiplies predictions, residuals, and backward fields by the stated signs. Substitution into the raw updates proves equivariance.

For clipped programs this conclusion requires the candidate's explicit conditions: sample-identical instructions, odd clips on sign-changing slots, and invariant additional norm cutoffs. It is not a claim for an arbitrary asymmetric clip. These conditions can be met by choosing an odd smooth clip for the nonlinear-part backward maps.

Finite initialization is invariant in law, which implies path-law invariance but not pathwise equality of the two finite predictions. Equation (8) correctly displays the obstruction to that stronger claim. Deterministic population contraction limits convert the law symmetry into f_a = y_a g. The common-space construction can be closed under the root reflection and sample exchange; its measure-preserving involutions intertwine the initial actions on dense query nodes and hence on their bounded extensions. Euler induction then preserves the stated identities.

Passing these identities to constructed strong limits uses continuity of fields/actions and of the relevant inner products. The argument does not use uniqueness of an unconstructed uncut equation and does not establish symmetry of every possible arbitrary uncut solution. This distinction is stated correctly in the candidate.

## 5. Radial regularity, continuation, and clock

The radial result retains C(0) = 0 from equation (12). With C ∈ C¹, C′ locally strongly absolutely continuous away from zero, and ⟨C,C″⟩ ≥ 0 almost everywhere, the displayed regularized-norm calculation proves convexity of sqrt(||C||²+ε²). Taking ε to zero gives convexity of ||C||. Zero initialization gives its right derivative h_0 = ||C′(0)||, yielding

\[
\|C(s)\|\ge sh_0,\qquad \|C'(s)\|\ge h_0.
\]

The second inequality follows from convexity and differentiation at nonzero C(s); when h_0 = 0 it is immediate. No compactness of Hilbert balls is used. Equation (14) should be read with the already stated zero initial readout, not as a replacement that discards it.

The application to bounded C¹ activation derivatives does not assume false Fréchet differentiability of a nonlinear superposition map L² → L². The candidate proves the needed strong path chain rule using bounded multipliers converging in probability and a fixed L²-factor truncation. The adjoint formula (20) is bounded in the raw Hilbert metric. The scalar gradient is norm continuous by the same multiplication argument, and integration along line segments proves scalar C¹ regularity. Along a constructed strong gradient path this is enough for

\[
C''=JJ^*C,\qquad g'=\|H\|^2+\|J^*C\|^2\ge\kappa_0.
\]

The energy increment identity makes a pre-target branch Cauchy at a finite endpoint. Norm continuity of the gradient gives a limiting velocity. Extending beyond that endpoint still requires local existence there. Symmetry lines 550–560 explicitly supply this as an additional hypothesis and correctly reject a general infinite-dimensional Peano inference.

Once a symmetric feature path is constructed to its first g = 1 state, its continuous kernel is bounded above and below on that compact interval. The upper bound gives divergence of ∫ds/[2(1−g(s))] at the target. The inverse clock is therefore global in physical time, with

\[
1-g(t)\le e^{-2\kappa_0t},\qquad L(t)\le e^{-4\kappa_0t}.
\]

The factor 2 follows from the contract's loss and c_a = y_a/2 convention. This proves a clock on the constructed feature path, not full-system uniqueness or a finite-width bridge.

## 6. Affine continuation and nondegeneracy, including ρ = −1

For the affine activation, the feature map is a finite sum of bounded multilinear expressions in the first field and HS matrix increments around bounded initial actions. Its scalar gradient is locally Lipschitz, with bounded derivatives on bounded balls. Thus the displayed contraction argument supplies local existence at every finite reached affine state.

The computed initial projected kernels are

\[
\kappa_0^{\rm same}=(7+\rho)/2,\qquad
\kappa_0^{\rm opp}=(1-\rho)/2.
\]

Both are positive for the allowed geometry. The energy bound while g < b and the radial lower bound prevent termination before the finite first hit S_b ≤ b/κ_0. Consequently the affine existence assertion through any fixed b > 1 is unconditional within the permitted common-action construction.

For opposite labels, equations (37) preserve the symmetry under (D_1,C) ↦ (−D_1,−C), leaving the common fields unchanged. Deterministic limiting laws imply zero contrast means and zero common–contrast covariance. If any D_ℓ vanished at a positive time, the identities D_2 = AD_1 and D_3 = BD_2 would imply g = 0, contradicting g ≥ κ_0s. Their initial norms are positive; strong continuity on [0,S_b] gives a positive minimum. This proves (39).

For same labels, the conditioning argument in (41)–(43) is essential and is correct. Scalar training is measurable with respect to F_n = σ(M_{1,0},A_0,B_0), while D_0 is an independent N(0,v_DI_n) vector. Therefore

\[
\mathbb E[\|T_nD_0\|_n^2\mid\mathscr F_n]
=\frac{v_D}{n}\|T_n\|_F^2.
\]

The learned differences A_s−A_0 and B_sA_s−B_0A_0 have bounded ordinary Frobenius norm on each fixed Euler prefix. Their action on D_0 consequently vanishes in normalized mean square on F_n-measurable bounded events. The separate conditional pairing estimate proves zero contrast mean and zero common–contrast covariance. Passing first through the fixed-program law and then through strong affine Euler convergence preserves the contrast fields and gives Var(z_a^(ℓ)(s)) ≥ v_D = (1−ρ)/2. Mere HS boundedness without conditional independence would not establish this conclusion; the candidate does not make that error.

At ρ = −1, v_M = 0 and v_D = 1. Neither label argument divides by v_M or by a Gram determinant. The same-label bound is at least 1 in every layer; the opposite-label positive-minimum argument also remains valid.

Finally, affine finite population programs are affine functions of their same-layer joint Gaussian roots/sources, with deterministic learned contractions. Strong L² Euler convergence preserves Gaussianity. Positive Gaussian variance implies strictly positive best affine approximation error for arctangent, because equality with an affine function almost surely would extend by positive Gaussian density and continuity to every real argument. Time continuity and compactness give η_b > 0. Equations (47)–(48) then correctly describe conditional transfer under a separately established uniform O(e) state comparison; they do not establish that comparison.

## Composition and remaining scope

The two baselines compose without a circular primal premise. Put R_b = b/√κ_0. The affine energy estimate bounds the displacement in the raw Hilbert metric by R_b. Initial first-layer projection norms are 1, initial action norms are at most 10, and C_0 = 0. Thus the continuous affine primal sizes are at most 10+R_b. Sufficiently fine population Euler meshes have, for example, bound B_0 = 11+R_b. Source equation (32) then supplies P(B,S_b), and the response bounds follow on that interval.

None of this supplies nonlinear response stability, cutoff removal, reached-state nonlinear existence, nonlinear state comparison, or the joint population/GF/exact-GD and observable conclusions in the contract. Constants and any conditional smallness threshold may depend on the fixed input pair. The ultimate quantifier remains one identical activation for all nonzero input angles. Initial contrast positivity for each fixed e > 0 and every ρ < 1, which the symmetry candidate proves, does not by itself meet that ultimate quantifier for the full flow theorem.

Those are explicit scope limits, not defects in these baseline lemmas. No candidate revision is required for the certified scope above.
