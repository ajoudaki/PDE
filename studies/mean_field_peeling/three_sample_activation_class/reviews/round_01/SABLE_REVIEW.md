# Independent mathematical review

**Verdict: PASS.** I find no remaining mathematical correctness or completeness objection to the claims as stated in this report. No repair is required for this verdict.

## Input, scope, and read coverage

- Sole substantive reading input: `/tmp/report-90a3cb5da6c3/REPORT.md`.
- Input size: 3,826 lines, 223,246 bytes.
- SHA256, checked before and after the read: `ad30e1e3ed36db9d1f36220859e3d40916aab4b26f892e478ccb850c9dbc7cd5`.
- I read the entire file in these consecutive, bounded, nontruncated chunks: 1–180, 181–400, 401–630, 631–870, 871–1100, 1101–1340, 1341–1570, 1571–1800, 1801–2030, 2031–2250, 2251–2470, 2471–2700, 2701–2930, 2931–3150, 3151–3370, 3371–3590, and 3591–3826. There are no gaps or unread appendices.
- I did not consult other files, skills, AGENTS instructions, author notes, source material, prior versions, other reviews, task-state records, the web, or other agents. I ran no numerical experiment. The input was not edited. This review is the only output file I wrote.

The audit concerns the precise three-input, three-hidden-layer theorem, its stated initialization and metric, the specified small positive perturbation of a large affine activation, all appended observations, and the subclass claims in Part A. I checked the internal arguments rather than accepting named internal lemmas without reviewing their proofs.

## 1. Statement, normalization, and raw equations

The factors in (M.7) are consistent with the predictor normalization and the metric (M.6). The Euclidean first-weight derivative has factor 1/n and the inverse metric supplies n/d. The two hidden matrix gradients have the stated 1/n rank-one factor. The readout inverse metric cancels the predictor's 1/n. Thus the finite equations, the normalized Hilbert–Schmidt interpretation, and the four kernel blocks describe the same gradient flow.

The distinction between raw parameter interpolation and recomputation of hidden fields is maintained in Part V. The actual random finite readout is not silently replaced by zero: its normalized norm tends to zero, and the zero-readout program is explicitly a comparator. The initial population first-weight norm and its dimension dependence are stated correctly; the activation selection uses projections and displacements, not a false dimension-free bound on the full first-weight norm.

Finite GF continuation follows from its exact energy identity and the finite-time Cauchy–Schwarz length bound. Local Lipschitzness holds at each finite width for the assumed C² activation. The argument does not mistakenly infer population local Lipschitzness of the uncut field from this finite-dimensional fact.

The realization restriction in (M.1) is explicit. The necessary bound δ ≤ 3/2 follows from the squared norm of the sum of three unit vectors. The theorem does not assume that realizable three-point geometries exist in every dimension.

## 2. Gaussian programs and canonical action spaces: Part F

I checked the conditioning calculation (F.5)–(F.8), including adaptivity and reuse of both orientations. Given the transcript, a new query is a linear observation of the appropriate remaining Gaussian factor. Sequential conditioning preserves the asserted product of residual laws. The proposed conditional mean satisfies both forward and reverse constraints, is orthogonal to the homogeneous solution subspace, and yields the correct noise normalization in (F.7). Removing the finite-rank output projection costs rank(U)/n in normalized mean square.

The positive-definite-query induction establishes both weak convergence and second-moment convergence. It does not assume independent trained coordinates. The conditional independent fresh Gaussian coordinates are used only at the step where they are available. The passage to W₂ and the same-index coupling estimate are valid.

The forward/reverse source rules include the required response terms. In particular, the integration-by-parts calculation (F.11)–(F.12) cancels the old forward projections exactly. Independence is asserted for oriented Gaussian source groups, not for the actual matrix answers. The formal derivative convention keeps deterministic coefficients fixed and retains paths through other previously computed answers. This is the convention the conditioning argument justifies.

The singular-query repair is adequate. Each fresh query perturbation contributes positive conditional squared distance at fixed perturbation size. The same-matrix finite comparison is uniform in width for a fixed program. At zero perturbation, continuity is proved using finite covariance square roots and bounded first derivatives, not continuity of pseudoinverses. The contracted correction is well defined on singular supports by (F.14). Thus singular query Grams are not an omitted hypothesis.

Causal scalar feedback is handled by an oracle construction followed by an induction on contraction and scalar-coefficient discrepancies. This does not differentiate empirical feedback or require an unjustified exchange between width and differentiation.

The common action-space construction has the needed ingredients: a countable generated language, joint finite-program consistency, density in the generated L² space, preservation of exact finite linear identities, and the high-probability matrix norm bound. The latter passes to deterministic limiting norm inequalities. Exact finite adjunction then extends by density, giving actual Hilbert adjoints. No comparison of unrelated matrices in operator norm across widths is used.

The norm estimate (F.4), the stronger tail estimate (F.4a), and the resulting uniform operator moments are valid. For t ≥ 10, the stated exponent comparison is sufficient. The independent Gaussian trace probe has variance at most 2||T_n||²/n, including for nonsymmetric matrices after symmetrization. Its later use with polynomial matrix expressions is supported by the proved moment bounds.

The Hilbert–Schmidt rank-one formulas and completeness argument are consistent with the finite normalized metric. The strong multiplier lemma and curve chain rule require only the stated bounded continuous multipliers. The scalar predictor's Fréchet differentiability is separately proved by the weighted Taylor estimate. It does not rely on the generally false assertion that the activation map is Fréchet differentiable from all of L² into L². The top-down scalar expansion and continuity of its raw gradient are valid.

## 3. Controlled response estimates and closure: Part R

I checked the four-stage order, source covariances, learned rank contributions, and source derivatives in (R.11)–(R.17). The sample indices and control factors are in the correct locations. Current forward queries precede the current reverse queries; forward returns therefore use strictly past times, while reverse returns retain the current time.

The affine raw comparison uses bounded primal norms and a deterministic control bound. The forward/backward affine expressions in (R.20) and their differences in (R.21) justify the stated common Lipschitz majorant. The four answer-insertion forcing constants correctly account for the update blocks affected by each inserted answer.

The Gaussian-probe argument is legitimate at fixed amplitude and fixed mesh. In the scalar law, the probe root is independent of the oriented source groups, and its explicit occurrences are precisely the inserted answer additions. Freezing the scalar coefficients is appropriate for integration by parts in that root. Continuity in the amplitude is established before taking the amplitude to zero. Choosing signs only after obtaining a deterministic limiting derivative row avoids a random-sign issue. This supplies affine response bounds without a singular covariance inverse or an interchange of derivative and width limits.

The nonlinear primal comparison uses affine Lipschitzness plus an explicit same-state perturbation bound. It does not use a cap-dependent nonlinear Lipschitz constant. Consequently the source variances and learned moment differences in R.4 are available before any response bootstrap. This removes a potential circularity in the moment argument.

The coordinate moment recursions in R.5 use maxima of deterministic Lᵖ norms, not random maxima over time. Minkowski's inequality therefore supplies the displayed estimates without temporal independence. The Gaussian exponential tail calculation follows from the √p moment bound.

The exact derivative equations (R.46)–(R.49) retain the cap derivative, signed derivatives of ψ, and all current returns. For reverse-source blocks the h_j factor is retained because the corresponding preactivation derivatives vanish through time j. The top derivative recursion carries the readout derivative as a separate causal variable. The terminal Q_k factor in (R.54) is necessary and is explicitly controlled; it is not incorrectly placed in the strictly-past envelope.

The same-array affine derivative comparison is distinct from comparison with the actual affine baseline. Equations (R.59), (R.62), (R.65), and (R.66) account for all the difference terms. Their expectation bounds use the exponential envelope and current-field moments already obtained on the appropriate prefix.

The deterministic coefficient perturbation equations are causal. In particular, A²_k uses past B² rows; A³_k uses the newly controlled A²_k and past B³ rows; B³_k uses the available top forward rows; and B²_k uses the newly controlled B³_k. The closure in R.9 follows this same order, so it does not assume bounds on all unknown current rows simultaneously. The zero-readout initialization starts the induction even though some source variances vanish. The current blocks (R.93)–(R.94), including the middle return through B³_kk, are correctly retained.

I found no unmet premise in applying this response result after G.3 verifies its affine finite-array hypothesis.

## 4. Geometry, nonaffinity, and global population dynamics: Part G

The augmented-Gram lower bound (G.1) is valid even for singular Γ. The mixed-sign reduction covers every remaining coefficient vector for three points. The displayed 2×2 matrix has determinant D² and trace D²−2D+4 ≤ 4 for D ∈ [δ,2], giving the claimed lower eigenvalue bound. The stated sharpness example satisfies the pairwise separation condition throughout its stated range and gives the displayed quotient.

The Gaussian projection in G.2 handles nonodd ψ. Its constant coefficient and linear coefficient may depend on the common marginal variance, but each is at least a−e. The residual is orthogonal to constants and all Gaussian linear functions, including in singular systems. Consequently the Loewner estimate (G.4) and its iteration to (G.5) are justified without an analyticity or kernel-positivity theorem.

The interval regression bound addresses the important generality issue correctly. A bounded nonconstant C² function must fail to be affine on some finite symmetric interval. The Gaussian density lower bound on that interval is c/σ for σ ≥ 1. Only the actual initialized standard deviations, lying in [1,5a²], are used. The proof does not claim a positive regression residual uniformly over all variances for arbitrary bounded perturbations.

The perturbation estimate (G.8) is valid for a possibly non-Gaussian trained variable: standard deviation is 1-Lipschitz under the stated L² coupling; the minimizing slope is bounded by 2; and using its affine predictor at the reference variable gives the required 3t_* error. No Gaussian law at positive training time is assumed.

The controlled bounds in G.3 apply to every positive Euler mesh of total control length at most S. The sum identity for h_j s_j gives the discrete version of the quadratic displacement estimate and rules out a first overshoot. This is sufficient for the affine-array hypothesis in R.7 and does not infer arbitrary-mesh Euler stability merely from a continuous affine flow.

The physical capped dynamics are not treated as gradient flow. Their exact residual equation has the possibly nonsymmetric term J_h U_h,R. Its operator norm is dominated by the positive readout Gram, which yields the residual decay and the strict S/2 residual-clock bound. The argument is stopped before the clock reaches S and then excludes that stop; the logic is not circular.

Fixed-cap local existence and continuation are justified by Lipschitz fields on bounded primal balls and bounded raw velocities. R's incoming moments pass through fixed-cap Euler approximation at each fixed horizon. Their constants are independent of cap and horizon because the effective control clock is bounded by the same S. Part V then provides the cap transfer actually invoked in G.6.

## 5. Finite algorithms, true kernels, velocities, and paths: Part V

The asymmetric gate inequality (V.10) is valid for every R′ ≥ R, including the true gate. It needs tails only of the reference incoming field. Sequential backward substitution creates a single linear factor in R: each new such factor multiplies an already controlled forward discrepancy, rather than another cap-dependent discrepancy. Residual coefficient comparison does not introduce another factor. This is the essential reason Gaussian tails beat the Gronwall loss.

The cap paths and their directions are uniformly Cauchy on compact time intervals. The limit integral equation yields a strong C¹ solution and identifies the true uncut field. Comparing an arbitrary bounded-primal strong competitor against the same capped references proves uniqueness without imposing moment tails on that competitor. The same estimate with the reached-state initial discrepancy proves the claimed unique continuation.

The fixed-cap source-row bounds in V.3 are proved by a fresh Gaussian probe, with actual recomputation of residual coefficients. The proof bounds absolute expected derivative rows, and V.4 separately establishes pointwise absolute derivative rows. These two quantities are not conflated. Their Volterra estimates have no same-time inversion.

The appended velocity calculations require more than simple W₂ closure because their derivatives are unbounded. V.5 supplies the needed argument. The bottom product is truncated first; its derivative row has an integrable envelope from primary moments. The first initialized action is then removed from its truncation and its moments established. The second action is handled with nested clips in the specified order. Its new named forward source has zero formal derivative in the relevant reverse-source group, even if the covariance is singular. Thus the second velocity moment bound is not assumed in order to prove itself.

The deterministic velocity comparison (V.40) truncates only reference velocity factors. The single M loss is justified by forward Lipschitz control and bounded operator actions. Its use with fixed-cap node moments proves a uniform L² velocity approximation; it does not require a matrix Lᵖ-to-Lᵖ bound.

The finite primary containment argument in V.7 uses exact update lengths and fixed-mesh contraction limits. This supplies the primal events needed for source-probe comparisons independently of the later derivative and velocity results. Fixed-cap GF and fine raw Euler are compared to fixed auxiliary meshes by dimension-independent raw estimates. F.1 is never applied directly to a transcript whose length grows with width.

The finite readout initialization is retained in all actual algorithms. Its O_P(n⁻¹) norm is removed only in a fixed-cap comparator justified by Lipschitz stability. For true finite GF, global existence is also proved directly from energy. For true raw GD, the comparison uses the actual preceding-node direction, adds the cap reference's within-step defect, and closes a first-exit bound. It does not require an unavailable width-independent Lipschitz bound for the uncut vector field.

V.8 distinguishes true backward observations from capped update fields. Its nested product truncations and bounded actions give the correct true backward tuple and all four full kernel blocks, including off-diagonals. Compact L² time images provide the uniform tails needed for observational trajectory comparison.

Velocity cap removal is ordered correctly. It first uses compact tails of the uncut population velocity and strong raw cap convergence, and only then transfers finite reference tails. It never multiplies an uncontrolled cap-dependent fourth-moment constant by a cap-removal error.

For path laws, (V.57) provides an actual supremum-path transport estimate from integrated squared coordinate speeds. Finite-dimensional joint time laws alone are not substituted for path-space convergence. The construction gives continuous coordinate path versions and finite second moments in the supremum norm. Uniform-time velocity W₂ convergence then proves convergence of squared speeds and their integrals. Generated probes use the two orientations and bounded same-width/common-space action comparisons; there is no unspecified cross-width operator identification.

The proof establishes full-sequence convergence in probability for each fixed dataset, activation, and finite horizon, jointly for the two algorithms under their common initialization. Its limit order agrees with Theorem M.1.

## 6. Initialization observations and nonzero motion: V.I and Part N

V.I supplies a separate derivative-valid extension for the unbounded initialization products. The top clip has an integrable envelope proportional to 1+|H₀|. After its removal, the returned middle field and its source derivatives are controlled before removing the second clip. Gram-square-root coupling handles all possible rank changes. The formulas retain the φ″ terms and all forward-source covariances.

The proof that S₃ is positive definite is valid for the full activation class. Q₂ is positive definite, so the top preactivation tuple has full support. The first factor in (N.11) has no open zero set because every p_i is nonzero and φ′ is strictly positive. Continuity then makes the second factor vanish everywhere. Differentiation in each separate coordinate forces v_i ψ″ to vanish identically. A bounded nonconstant C² function cannot have ψ″ identically zero. This proves strict positivity without requiring ψ″ to have one sign or to be nonzero everywhere.

The conditional reverse-source covariance arguments then give S₂ positive definite and a positive conditional bottom covariance. They correctly account for response terms instead of asserting that full returned fields are independent of forward features. The rank-one trace formula proves all hidden matrix directions nonzero. The Γ_jj = 1 term proves every bottom sample direction nonzero even when Γ is singular or its affine bottom direction vanishes.

I checked the exact affine formulas (N.20)–(N.23), including their powers of a and both contributions to each upper preactivation direction. The finite Gaussian calculation for B*H gives covariance (a²m²+||v||²)I+vvᵀ/n; the cubic cross terms vanish. The trace calculations yield τ(AA*)=1, τ((AA*)²)=2, and τ(S²)=τ(SR)=2, τ(R²)=3. The report proves deterministic trace limits and uniform integrability before using their expectation calculations; fourth-moment identities alone are not incorrectly treated as concentration proofs.

The completed squares (N.30), (N.33), and (N.37) give positive lower bounds for every upper sample. The binary three-label assumption is used explicitly through |m| ≥ 1/3. The nonlinear comparison is with the same initialized actions, and its derivative perturbation is bounded directly by e against the constant affine gate. It requires no unproved differentiability of the activation law in its variance.

The physical factors are consistent: C′(0)=3H, b_i(t)/t → 3β_i, hidden θ′_h(t)/t → 9V, and hidden displacement is (9/2)t²V+o(t²). The strong multiplier and curve product rules establish the actual right second derivatives of every hidden preactivation and feature. Finally the hidden kernel contribution is 9t²||V||² and the readout feature-energy contribution is another 9t²||V||². This gives exactly the coefficient 18 in (M.20)/(N.64).

## 7. Explicit constants and activation subclass claims

I checked the explicit constant selections and the inequalities on which their uses depend. In particular:

- The Gaussian net and tail constants in F.2–F.4c have the stated normalizations and sufficient exponents.
- The R.18 majorant dominates the affine field and query constants. The R.30–R.32 bounds give a same-state total perturbation below the claimed 30a³b³e. The affine response factor 3 and all control-weighted learned bounds are sufficient.
- The R.37 moment recursions, L_q²=8 exp(1)K_q², and the 4⁻ᵐ exponential series are consistent. R.50 dominates every derivative recursion coefficient. R.57 bounds both the exponential envelope and its terminal incoming-field product.
- R.63 and R.67 give the factor 200H¹¹ exp(HS) used in R.68. The latter also includes the learned-moment errors. R.74 and R.80–R.88 bound the four successive deterministic coefficient differences. K_* is twice the maximum needed to bound the sum of the two backward errors. Thus (R.90) leaves the claimed half-unit slack. All factors are finite and positive for the stated a,B,S.
- In G, the backward coefficient 968 is (2·11)²·2, and 968+44·6+2·70=1372<1400. Integrating gives 560000a⁶s². Substituting S gives the stated C_S and D_S. The gain bound a≥2000/√λ gives a⁶≥6.4·10¹⁹λ⁻³, sufficient for every inequality in (G.18).
- The feature-Gram perturbation is 7.2·10⁶a⁶D; the hidden residual contribution is below 6·10⁶a⁶C_S². Their stated slack yields the residual rate λa⁶/2. The integrated residual bound is 6/(λa⁶)=S/2.
- The cubic gain condition gives 615a²D_S/t_* ≤ 0.08856. The quartic alternative in A.4 gives 615a²D_S ≤ 0.08856t₀. The regression radii and margin factors consequently match the conclusions.
- The nonlinear motion comparison coefficients in N.41–N.50 agree with the displayed decompositions: in particular 6,985,680 and 143,416,183. The common 2·10⁸a⁷e bound is at most a⁶/50 under (N.52), strictly smaller than half of each affine lower bound. M.21 is smaller still.

Part A does not overstate the activation class. A.1 supplies a common interval residual for a whole C²-bounded neighborhood; its distance estimate is valid. A.2 separately assumes a uniform Gaussian regression margin across scales and proves the stronger separation-independent coefficient under that assumption. Distinct finite limits at ±∞ give the residual limit b²(1−2/π), and the arctangent neighborhood argument preserves a common positive margin. The normalized examples have the stated bounded derivatives.

I specifically checked the potentially adverse classes requested in this audit:

- **Localized/compactly supported perturbations:** the general theorem uses the finite variance range and c/σ estimate; Part A correctly records failure of the stronger uniform-in-variance condition in this case.
- **Oscillatory perturbations:** no limit at infinity is used in the general theorem, and all derivative estimates use absolute bounds. Nonconstancy supplies the finite interval residual and ψ″ not identically zero.
- **Nonodd perturbations:** the nonzero Gaussian mean contribution is retained in (G.3)–(G.4); no cancellation by oddness is assumed.
- **Sign-changing derivatives:** response formulas retain their signed expectations, while estimates use absolute bounds. The full activation's derivative remains positive because the affine slope dominates the bounded perturbation.
- **Singular input or query Grams:** the geometric proof, source regularization, formal derivative contraction, and reverse-covariance positivity each address the relevant singularity without assuming a nonexistent inverse.

## Objections and required repairs

**None.** I did not find a false claim, missing hypothesis, circular dependency, unjustified limiting interchange, incorrect decisive constant, or unproved internal/external invocation that leaves a needed obligation outstanding. The strict PASS verdict applies to the manuscript and SHA256 identified above.
