# Independent adversarial mathematical audit

**Verdict: PASS.**

I found no unresolved mathematical correctness or completeness objection to Theorem M.1 after reading the entire manuscript and auditing its proof dependencies. In particular, I found no circularity in the response bootstrap, the passage from a bounded residual clock to cap-uniform moments, or the reference-tail uniqueness argument. No repair is required by this review.

## Input isolation and reading coverage

- Sole mathematical reading input: /tmp/manuscript-766d3a3d78ba/REPORT.md.
- Manuscript SHA256: fdbfa412195aedfbdae103b1e7e862dd42fffd5061e662dbda7dfe462eab0f7c.
- Manuscript size: 3,547 lines; 210,133 bytes.
- I read the entire manuscript in these bounded, nontruncated chunks: lines 1–260, 261–520, 521–780, 781–1040, 1041–1300, 1301–1560, 1561–1820, 1821–2080, 2081–2340, 2341–2600, 2601–2860, 2861–3120, 3121–3380, and 3381–3547. I subsequently searched only that same manuscript to identify locations.
- I read no other files, skills, source notes, project state, history, other reviews, or websites. I did not contact other agents. I performed no numerical experiments and made no changes to the manuscript. The only file written for this task is this review.

The perspective of this audit was deliberately skeptical of estimates on nonlinear maps in L², source-response constants, mesh uniformity, unbounded incoming multipliers, and uniqueness claims beyond a constructed class. The discussion below records the checks that resolved those concerns.

## 1. Statement, scaling, and quantifiers

**Locations:** M.1–M.4, lines 5–320; F.8–F.10, lines 751–929; V.1, lines 2198–2277.

The physical parameter metric and all four update factors agree. For the first block, the Euclidean gradient has the factor 1/n, while the inverse metric contributes n/d; this gives 1/d. For each hidden matrix the Euclidean gradient is already the normalized rank-one action bhᵀ/n. The readout inverse metric cancels the Euclidean 1/n. The population rank-one action has exactly the finite Frobenius norm when both finite neuron spaces carry normalized inner products. The population first-block norm also agrees with the finite raw norm.

The finite readout is nonzero and is kept in both actual algorithms. Its vanishing normalized size is used only in comparator arguments at a fixed cap and a fixed finite transcript. It is not silently set to zero in finite training.

The theorem distinguishes compact-time, full-sequence width convergence from global population existence. It does not interchange the infinite-width and infinite-time limits. The activation parameters depend only on separation. Subsequent convergence constants are explicitly permitted to depend on the fixed dataset, dimension, activation, and observation horizon. The large full initial first-weight norm, √d, is acknowledged, and the dimension-independent activation choice uses only the three normalized projections and displacement estimates.

The common actions are the constructed Gaussian actions, not arbitrary operators with norm at most 10. This restriction is essential to both the source arguments and the initial-motion calculations, and the statement imposes it. The admissible geometry qualification also correctly handles dimensions in which no separated triple exists.

## 2. Gaussian conditioning and source-response identities

**Locations:** F.1–F.5, lines 339–603, especially (F.5)–(F.14).

The adaptive conditioning argument is valid. At a matrix call, its input is measurable with respect to the already revealed transcript. Conditioning that call imposes a linear observation on only the queried residual Gaussian matrix. Successive conditioning preserves the product structure of the residual factors. This is sufficient even though the query input was not independent of the original matrix before conditioning.

The conditional mean in (F.6) satisfies both forward and reverse constraints by the compatibility relation UᵀY = QᵀV. Its Frobenius orthogonality to the homogeneous constraint space identifies the Gaussian conditional law. Applying this law to a new input gives the coefficients in (F.7), including the normalized reverse-input Gram and the response projection. The removed Gaussian projection has normalized mean square equal to a fixed rank divided by n, so it disappears at fixed transcript length.

The empirical-law induction checks both weak tests and second moments. Its conditional variance estimates require boundedness in probability of the old normalized norms, which the preceding induction supplies. Lipschitz coordinate instructions preserve the resulting Wasserstein convergence.

The source correction is not inferred from independence of forward and transpose answers. In (F.11)–(F.12), orthogonality of the new residual input to earlier forward inputs removes the old reverse-response terms. Gaussian integration by parts then produces the expected formal derivative. Substitution cancels the response contribution inherited through the old forward regression. This yields the claimed new source covariance and correction. Independent source groups are consistent with dependent answers because the response terms retain their shared dependence.

The formal derivative convention is necessary at singular covariance and is consistently used. Derivatives are taken in named arguments with deterministic coefficients frozen. The kernel-of-covariance observation (F.14) explains why different smooth extensions on a singular support give the same contracted correction, without claiming equality of individual derivative coefficients.

## 3. Singular queries, feedback, and common action spaces

**Locations:** F.5–F.8, lines 559–801.

The singular-query argument does not assume stable rank. Each fresh independent input perturbation gives a strictly positive limiting Schur complement at fixed perturbation size. The same-array finite comparison is an instruction-by-instruction L² estimate on the bounded initial-operator event, and its constant depends only on the fixed program.

The subsequent zero-perturbation passage avoids pseudoinverse continuity. At each finite stage, the source covariance square root is continuous, node values have uniform linear-growth bounds, and the formal derivatives have uniform deterministic bounds on a compact coefficient neighborhood. These properties give convergence of node second moments and expected derivatives and close the finite induction. The triangle argument consequently identifies the original, possibly singular program along the full width sequence.

Causal scalar feedback is handled by an oracle program whose coefficients are determined from prior limiting contractions. The inner-product and scalar-multiplication estimates in F.6 transfer that oracle to actual finite feedback. There is no implicit fixed-point assumption here. The normalized residual controls used later are explicitly frozen and are not differentiated at zero residual.

The countable construction in F.7 supplies consistent finite joint laws: a finite family of expressions is identified by its finite union, and adding unused instructions changes no finite vectors. The limiting operator inequalities transfer from the finite norm event to deterministic limiting norms. They make the actions well-defined on L² equivalence classes and on the span of generated nodes. Density of that span follows from the cylinder approximation and included smooth coordinate functions. The two transpose identities pass by the same contractions and density, giving actual Hilbert adjoints. No cross-width operator-norm identification is required.

The explicit initial Gaussian norm bound has a negative exponential rate, and its extension to fixed operator moments is sufficient for the trace probes in Part N. The trace-probe variance bound in (F.4c) applies also to nonsymmetric matrices by taking their symmetric part. Its independence requirement is met by the additional Gaussian probe used there.

## 4. L² nonlinear analysis and the raw gradient

**Locations:** F.9–F.11, lines 802–950; N.1, lines 2902–2993.

The manuscript does not rely on a false Fréchet differentiability assertion for a nonlinear Nemytskii map from all of L² to L². The bounded multiplier lemma splits the fixed incoming factor into a bounded part and an L² tail. This proves strong multiplier continuity, which is precisely what the curve chain rule requires.

The scalar predictor is proved Fréchet differentiable using a weighted Taylor remainder. Its two bounds, quadratic in the increment and linear in the increment, permit truncation of the fixed weight. Forward differences are O(η) in L², so each weighted remainder is o(η), while action-increment cross products are O(η²). Moving the fixed actions through adjoints gives the stated gradient blocks. The same bounded multiplier and rank-one arguments prove continuity of the gradient.

The feature-energy functional in N.1 uses this scalar method again, rather than requiring a second derivative of the ambient activation map. Its derivative is the hidden vector V. Both this derivative and the raw predictor gradient are sufficient for the later energy and kernel identities.

Fixed-cap local existence and Euler approximation use a genuinely locally Lipschitz field on a bounded primal ball: the two partial derivatives of the capped gate are bounded, the forward map is Lipschitz there, and learned products are controlled in Hilbert–Schmidt norm. The stated integral contraction and defect recurrence are valid in the complete raw space.

## 5. Exact response system and the affine probe

**Locations:** R.1–R.3, lines 957–1214; equations (R.10)–(R.29).

Unrolling the learned matrices gives the displayed forward and reverse moment terms with the correct control position h_j c_{j,m}. The source correction has no additional control factor: that control is already on the derivative path. The query order is causal, and reverse corrections include current forward calls.

The raw affine Lipschitz estimates use the distance in first-projection norms, current operator norms, and readout norm. These suffice for all queries and rank-one update estimates. The conservative constant Q = 100a³b³ dominates the displayed component estimates and answer-perturbation forcing constants. A perturbation at a single time changes subsequent raw states with its own factor h_j, regardless of the other mesh sizes.

The affine Gaussian probe avoids interchanging a width limit and a derivative. At fixed nonzero amplitude, the finite program identifies the pairing with the new Gaussian root. With the program coefficients frozen, the affine scalar expression is affine in that root; Gaussian integration by parts identifies the pairing with the signed formal derivative row. The unperturbed pairing tends to zero, and the finite same-array comparison bounds the perturbed pairing. Only afterwards is the amplitude sent to zero, using finite chronological continuity. Choosing deterministic signs is legitimate for the deterministic limiting derivative coefficients.

The conversion from scalar row bounds to a sum of time-block norms incurs a factor at most three, which is included in A₀ and M₀. The learned moment contributions have the asserted h_j bounds. The affine current backward blocks vanish for the stated residual-free outputs and explicit schedule.

## 6. Independent primal comparison and the response constant chain

**Locations:** R.4–R.7, lines 1215–1538; (R.30)–(R.68).

The nonlinear-to-affine primal comparison is independent of response estimates and cap size. At the same state, the gate difference from aq is bounded by ε|q|, and the activation perturbation is uniformly bounded by a constant times ε. Backward substitution and the rank-one inequality give the stated raw forcing bound. Only the affine field's Lipschitz constant enters the comparison recurrence. The first-exit estimate therefore establishes the nonlinear primal bound before any response bootstrap is invoked.

In particular, the actual source variances are bounded by actual input L² norms before coefficient-prefix estimates are used. The learned moment differences are compared on the same finite arrays and then passed to the population. They are not obtained by a comparison of square roots of covariance matrices whose dimension grows with the mesh.

On a bounded coefficient prefix, the moment recursions use maxima of deterministic Lᵖ norms and sums of positive mesh lengths. Minkowski and the finite-product identity suffice; no random time supremum or time independence is assumed. The constants in (R.37) give the claimed √p growth. The factorial estimate in (R.43) turns that into a uniform exponential square moment.

The exact derivative equations include all three local derivatives: G = φ′, V = ∂qD, and L = ∂zD. In particular V contains the cap derivative τ′_R, and L is bounded by εQ_k, not by a cap-dependent deterministic factor. Current backward derivative outputs in (R.49) are retained.

The pathwise derivative envelopes follow by causal finite-product iteration. The envelope excludes the terminal time, so the extra factor 1 + εQ_k in the backward-output bound is necessary and is present. Jensen's weighted exponential inequality and Hölder control both the envelope and this terminal factor without independence across times.

In the same-array perturbation of R.7, replacing the gate matrices by aI, aI, and 0 really does leave the deterministic coefficient arrays fixed. The exact subtraction in (R.59) includes the direct reverse-source term, the LJ term, and both gate differences in the returned product. A reverse-source perturbation retains its factor h_j; later propagation does not introduce a quotient involving another time step. The top subtraction separately tracks the readout derivative. The output differences (R.65)–(R.66) keep their current multipliers.

The coefficient in (R.68) is large enough for the displayed remainders: 10H³D₁ = 200H¹¹ exp(HS), and the expected envelope combination is bounded by 1 + (S+1)X. The added m₀(1+S) covers both learned moment errors. Every constant in the chain is a finite function of a, B, and S only.

## 7. Deterministic coefficient stability and chronological closure

**Locations:** R.8–R.9, lines 1539–1769; (R.69)–(R.96).

The deterministic affine derivative systems at fixed arrays are correctly obtained from the random derivative equations. Their roles are kept distinct from evaluation at the actual affine baseline arrays. Subtracting these systems yields the differences used in (R.76); the nonlinear and learned-moment remainders have already been controlled.

The expansions in (R.79), (R.81), (R.83), and (R.85) retain every changed factor. Current-row dependence is treated as forcing only when that row has been bounded at the preceding stage. The time sums in the top readout estimate are bounded by S after an explicit exchange of finite sums. No minimum mesh size or quasi-uniformity assumption appears.

The last middle backward product in (R.87) uses the just-constructed current B³ row. Its remaining U difference depends on the current A² row and past B³ rows, so it does not introduce a same-time circular equation. With K_* twice the maximum of the four component constants, both component bounds and the bound on the sum E_k follow.

The closure order A²_k, A³_k, B³_k, B²_k is essential and is correctly followed:

1. The bottom feature derivatives for A²_k require only past bottom backward rows.
2. A³_k uses the newly bounded middle forward row and only past middle backward rows.
3. B³_k uses the available top forward row and the readout; it then defines the current middle incoming field.
4. B²_k can consequently use that current middle incoming field and current B³_k.

The initial zero-readout stage starts this induction. The explicit current-return formulas (R.93)–(R.94) confirm that the potentially problematic current third-layer return into the middle derivative is present. No current return is inverted or discarded.

Finally, the positive-product identity in (R.92) and the threshold 1/[2K_* exp(K_*S)] give strict slack for each new row. This proves the prefix hypothesis instead of assuming it. The threshold also includes the independent primal-comparison condition B/(2T₀). The full estimate is uniform over arbitrary positive meshes, number of mesh points, control variation, sample covariance, and finite cap.

## 8. Separation, nonlinear margin, and all positive controlled meshes

**Locations:** G.1–G.3, lines 1773–2013; (G.1)–(G.20).

The augmented input Gram lower bound is valid even for singular Γ. In the mixed-sign case the two-dimensional quadratic form has determinant D² and trace D² − 2D + 4 ≤ 4. Its smaller eigenvalue is therefore at least δ²/4, and replacing the two positive coefficients by their sum only enlarges their squared norm. The one-sign case is simpler. No inverse of Γ is used.

The Gaussian projection of each feature onto constants and Gaussian linear functions yields a common slope at a fixed layer because the marginal variances agree. Its residual Gram is positive semidefinite, giving the initial readout Gram lower bound. The argument remains valid at singular lower-layer covariance.

The strict positivity of η_* follows from positivity at every finite positive scale, continuity, and a strictly positive large-scale limit. The regression stability argument also checks a positive lower bound on the perturbed standard deviation before bounding its optimal slope. It does not assume that the trained preactivation remains Gaussian.

The controlled primal estimates are independent of caps and response constants. On the stopping ball, the hidden speed sum is bounded by 1400a³‖C‖, and readout speed by 800a³. The resulting quadratic hidden displacement estimate holds for Euler on every positive mesh through the exact identity for the sum of h_j s_j in terms of s_k² and the sum of h_j². This excludes a first discrete overshoot rather than relying on a continuous-flow argument for coarse Euler.

The stated a-selection makes D_S and C_S satisfy all three required kinds of slack: containment in the primal ball, persistence of readout coercivity, and preactivation displacement smaller than t_*. In particular, the factor 615a²D_S is bounded by 0.08856t_* by the second lower bound on a. These estimates verify the finite affine-array hypothesis of Part R with B = 12, including arbitrary positive controlled meshes.

## 9. Global residual clock and horizon-independent amplitude choice

**Locations:** G.4–G.6, lines 2014–2187.

The capped dynamics are not incorrectly treated as a gradient flow. The exact residual equation uses the true hidden prediction differential composed with the capped hidden update map. That product can be nonsymmetric. Bounding its operator norm, rather than asserting positivity, controls its quadratic contribution.

The feature displacement estimate gives K⁴ ≥ (3/4)λa⁶I. The hidden contribution has norm at most (1/4)λa⁶. Consequently the residual norm decays at rate at least λa⁶/2, and its total ℓ¹ clock is at most 6/(λa⁶) = S/2.

This clock argument is initially stopped before S, so its use of the controlled estimates is justified. The strict S/2 conclusion excludes the stop. Fixed-cap local existence, bounded primal quantities, and bounded raw speed then continue each capped path globally. No cap-uniform moment premise is needed for this part.

Only after this global capped construction does G.5 apply the response theorem. At a fixed horizon, sufficiently fine physical Euler meshes have effective total residual-clock length less than S. Their frozen controls have ℓ¹ norm at most one and their affine comparators use the identical numerical steps and controls. Fixed-cap Euler convergence then passes the response moments to each physical cap path. Since the same numerical a, B, and S work for all horizons, the resulting moment constant and amplitude threshold are independent of physical time.

This resolves the potentially circular implication: the residual clock is established from deterministic primal and readout estimates, and the clock subsequently supplies the domain on which the response theorem yields uniform tails.

## 10. Uncapping, strong existence, and uniqueness

**Locations:** V.2, lines 2278–2337; G.6, lines 2134–2187.

The asymmetric gate estimate is valid for every larger cap and for the true uncut gate. Changing the incoming field first uses the uniform q-Lipschitz constant. The forward discrepancy uses only the smaller reference cap, and the remaining clip difference is supported where the reference incoming field exceeds that cap.

Sequential backward substitution incurs a single factor proportional to the reference cap. Each new such factor multiplies a forward discrepancy already bounded directly in raw state distance; incoming discrepancies are multiplied only by bounded actions and gate slopes. Residual coefficient differences are controlled separately by the primal forward estimate. They do not create an additional cap factor.

The incoming moment estimate gives Gaussian L² tails. Therefore the linear-exponential stability loss is dominated by the quadratic-exponential tail decay, yielding a uniform raw-state, backward-field, and raw-direction Cauchy estimate on each fixed time interval. Completeness and convergence of the integral equations give a strong C¹ limit; applying the same asymmetric inequality with the limit on the uncut side identifies its vector field.

The uniqueness claim is supported in the stated broad class. An arbitrary bounded-primal strong competitor requires no tail estimate of its own: only the canonical cap reference appears in the tail term. Its different primal bounds merely change the coefficient of the linear exponential. Comparison still forces its distance to the cap reference to tend to zero. At a reached time, the cap reference's initial discrepancy already has a quadratic-exponential smallness that survives a further linear-exponential stability factor. This proves uniqueness of continuation from reached states without invoking local well-posedness for arbitrary uncut L² states.

## 11. Finite algorithms and the order of limits

**Locations:** V.3, V.6–V.9, lines 2338–2413 and 2541–2741; F.11, lines 930–950.

The finite Gaussian theorem is applied only to fixed programs. A fixed coarse capped Euler mesh is first identified; deterministic raw Euler estimates then compare fine Euler or capped flow to that same-width coarse reference. The matrix bound in (V.44) uses exact rank-one update lengths, not convergence of trained operator norms. These lengths have bounded deterministic limits over sufficiently fine population meshes. They supply the finite primal event used in the later comparisons.

The fixed-cap nonlinear Gaussian probes used for source rows have bounded coordinate derivatives at each fixed transcript. Their integration by parts is justified at fixed amplitude, and derivative continuity follows by finite covariance-square-root and coefficient induction. The primary finite-program law and rank-one update bounds establish their primal event independently of those source-row estimates, so the V.3/V.7 cross-reference is not circular.

The actual readout norm of order 1/n in probability is propagated from a zero-root comparator at fixed cap and transcript, with first-exit slack. Subsequent same-width comparisons retain the original readout in both paths.

For uncut finite GF, the raw energy identity separately guarantees global finite-dimensional existence. Its comparison to the cap flow uses reference incoming tails obtained from fixed-cap empirical Wasserstein convergence. For raw GD, the field is evaluated at the preceding raw node, exactly as prescribed by simultaneous Euler. Equation (V.55) controls that node discrepancy by the running state-error supremum and treats only the cap reference's within-step variation as an Euler defect. It does not assume an uncut width-independent Lipschitz constant.

At each fixed cap the raw step tends to zero and the deterministic defect vanishes. Cap removal comes afterwards. This supports the specified step n⁻², and the manuscript's stronger observation about any deterministic vanishing raw step is consistent with the argument. Both algorithms may use the same initialization and cap reference, giving joint convergence by the same finite collection of probability estimates.

## 12. True kernels, velocities, probes, and path laws

**Locations:** V.4–V.11, lines 2414–2827.

The primary pointwise derivative rows are bounded by a causal Volterra recurrence at fixed cap. The current transpose terms involve already determined forward fields. This gives primary moments without an Lᵖ operator theorem for the initialized matrices.

The appended velocity inputs contain bounded multipliers times unbounded velocities, so they cannot be submitted directly to the original bounded-derivative program theorem. V.5 supplies the required nested truncations. The bottom input's formal derivative row has an integrable primary-moment envelope. Its first initialized action therefore has controlled response coefficients and moments before the second velocity input is treated. The second input's transpose-source derivative holds its new forward source fixed, as required by the source convention. The ordered inner and outer clip limits avoid assuming the upper velocity moments that are being proved.

The deterministic velocity comparison has a single truncation-level loss: multiplier differences are split using the reference velocity, and every new such loss multiplies a forward state discrepancy. This compares the actual chain-rule velocities, including those of recomputed hidden fields along linearly interpolated raw GD parameters. It does not replace them by derivatives of linearly interpolated hidden fields.

True backward fields observed at a capped state are handled separately from the capped update fields. V.8 identifies their joint laws through nested bounded-gate observations and current actions. It uses action continuity and uniform second-moment tails, without claiming a derivative source formula for arbitrary untruncated products. The four true kernel blocks are then within-layer second-moment contractions, including off-diagonal sample entries.

For velocity cap removal, the uncut strong curve already has continuous L² preactivation velocities. Their compact time images have uniformly vanishing L² tails. Population cap velocity convergence is proved with a fixed tail level first. The finite comparison then takes width at fixed cap and level, cap removal at fixed level, and finally the tail level to infinity. It never multiplies an uncontrolled cap-dependent higher-moment constant by the cap-removal error.

Uniform-time field/velocity Wasserstein convergence and the neuron-index coupling also yield the joint laws at finitely many times. Full path laws are not inferred from these alone: (V.57) supplies a direct supremum-path interpolation cost bounded by mesh size times integrated squared speed. Fixed observation-grid convergence followed by grid refinement proves the path-space assertion. Initial moments and the same speed bound ensure that the path laws have finite second moments.

The squared-speed integrals and raw block speeds follow from the actual velocity norm and kernel identities, respectively. The one-sided node conventions for GD are compatible with these comparisons and do not affect time integrals. Fixed generated probes pass through finite instruction induction, same-width/current-action bounds, and common-space L² continuity in both orientations.

## 13. Initialization observations and all nonzero initial motions

**Locations:** V.I, lines 2828–2895; N.1–N.6, lines 2902–3503.

The initialization transpose formulas needed in Part N receive a separate derivative-valid proof. Truncating H₀φ′(Z³_i) gives bounded-derivative programs whose expected derivatives are dominated by K(1+|H₀|). The first reverse coefficients and input Grams consequently converge. The second gate is then handled by an inner-limit/outer-limit order with an integrable K(1+|q²_i|) envelope. This justifies the current-return terms and full reverse source covariances used in N.2.

The upper initialized forward covariance is positive definite by the augmented-Gram bound, even when the original input Gram is singular. Full support and nonconstancy of φ′ then prove S₃ positive definite. Conditioning on independent fresh reverse Gaussian sources propagates positive definiteness to S₂ and the conditional bottom covariance. The lower bounds for each hidden parameter block and every bottom sample follow without a false lower bound on Γ itself. In particular, the bottom sample bound uses its diagonal entry Γ_jj = 1.

For the two upper samples, the affine formulas (N.22)–(N.23) correctly retain both the direct learned-weight direction and the propagated lower-layer direction. They permit cancellation and therefore require the quantitative calculation in N.4. I checked that calculation:

- Conditional on the first matrix and roots, Q = B*(am1 + Bv) has mean v and covariance (a²m² + ‖v‖²_n)I + vvᵀ/n. This gives (N.27), including its 1+1/n factor.
- The needed trace limits for AA* are 1 and 2. Uniform operator moments plus the independent trace probe justify deterministic limits and expectation passage; fourth-moment expectation calculations alone are not used as concentration.
- For S = BB* and R = BAA*B*, the required limiting moments are τ(S) = τ(R) = 1, τ(S²) = τ(SR) = 2, and τ(R²) = 3. The finite formula (N.35) has the correct two trace-square terms.
- The resulting quadratic forms are (m + 2γ_j)² + γ_j² in layer two and [3γ_j + (2+a⁻²)m]² + (2γ_j+m)² + γ_j² in layer three. Their completed-square remainders are strictly positive because three binary labels give |m| ≥ 1/3.

These prove the stated uniform affine lower bounds for each upper sample. The nonlinear perturbation compares gates to the constant affine gate, so it does not need a bound on the change of preactivation inside a derivative. The forward, backward, rank-one, and preactivation difference decompositions in N.5 have the correct factors. The common bound 2·10⁸a⁷e, combined with e ≤ (10¹⁰a)⁻¹, is smaller than half each affine lower bound. Thus all upper sample directions remain nonzero.

The time factors are also correct. At zero readout, hidden first velocities vanish while C′(0) = 3H. Strong bounded-multiplier and action continuity give b_i^ℓ(t)/t → 3β_i^ℓ. The residual tends to −3p_i, giving θ′_h(t)/t → 9V, hence hidden displacement (9/2)t²V + o(t²). Applying the strong forward chain rule gives right second derivatives 9U_j^ℓ and 9φ′(Z_j^ℓ)U_j^ℓ. Their asserted nonvanishing follows from the preceding lower bounds.

## 14. Projected kernel coefficient

**Locations:** N.7, lines 3504–3547.

The projected full kernel is the squared norm of the hidden gradient of f_p plus the readout-gradient squared norm ‖H(θ_h)‖². From b/t → 3β, the hidden term contributes 9t²‖V‖²_hidden + o(t²). The scalar feature-energy differential applied to hidden displacement (9/2)t²V + o(t²) gives an additional 9t²‖V‖²_hidden + o(t²) in ‖H‖². Thus the total coefficient is exactly 18, as stated. This argument needs only the scalar first derivative already proved, not a second ambient Fréchet derivative.

## 15. External-theorem and dependency audit

No missing nonclassical external theorem is needed to complete the argument as written. The potentially substantial Gaussian-program result is proved internally, including adaptive reuse, both orientations, singular queries, feedback, and the common actions. The response theorem is reduced to its displayed recurrences, elementary Gaussian integration, moment inequalities, and finite-product estimates. Cap transfer, broad uniqueness, product observations, and path-space convergence likewise receive internal arguments rather than references to unnamed limit theorems.

The remaining standard functional-analytic and measure-theoretic ingredients—Hilbert-space completeness, elementary Gaussian projection, density of cylinder functions, finite-dimensional Gaussian square roots, basic integral and dominated-convergence arguments, and the weak-plus-second-moment characterization of Wasserstein convergence—are either derived at the point of use or used with their relevant hypotheses supplied.

The dependency direction is consistent: fixed Gaussian programs and local capped analysis; independent controlled primal bounds; response control on the resulting bounded clock; global capped moments; uncapping and reference-tail uniqueness; finite algorithm and observation limits; then initial-motion consequences. Cross-references to later detailed sections do not require their conclusions before their independent premises are established.

**Final assessment:** PASS. No severity-rated mathematical defect, unresolved verification obligation, or required repair remains from this audit.
