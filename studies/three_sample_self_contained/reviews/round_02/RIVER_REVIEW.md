# Independent adversarial mathematical review

**Verdict: PASS.** I found no remaining mathematical correctness or proof-completeness objection after reading and auditing the entire manuscript. In particular, the adaptive Gaussian argument is proved within the manuscript, its singular-covariance passage does not rely on continuity of a pseudoinverse, and the transpose actions used in the dynamics are justified as actual Hilbert adjoints. The subsequent estimates respect the restrictions of that finite-program argument.

## Scope, isolation, and reading coverage

- Sole reading input: `/tmp/manuscript-5e73c4891e4c/REPORT.md`.
- Manuscript size: 3,547 lines, 210,133 bytes.
- Manuscript SHA256: `fdbfa412195aedfbdae103b1e7e862dd42fffd5061e662dbda7dfe462eab0f7c`.
- I read all lines, in the following bounded, nontruncated chunks: 1–220, 221–440, 441–670, 671–900, 901–1130, 1131–1355, 1356–1585, 1586–1810, 1811–2040, 2041–2280, 2281–2510, 2511–2750, 2751–2970, 2971–3190, 3191–3420, and 3421–3547.
- I read no other files, skills, project state, source notes, history, reviews, or websites. I did not communicate with other agents, consult external results, or perform numerical experiments. The only written artifact is this review; the manuscript was not edited.
- The audit covered Theorem M.1 and the supporting arguments in Parts F, R, G, V, V.I, and N, including the explicit activation-selection constants and the claimed initial accelerations and kernel expansion.

There are no major or minor correctness findings requiring repair. The remainder records the substantive obligations checked and why the apparent failure modes do not invalidate the proof.

## 1. Finite model, metric, and theorem interpretation

**Locations:** M.1–M.4, (M.3)–(M.18), F.8, (F.39)–(F.44), V.9.

The finite metric gives exactly the factors in (M.7). In particular, the first-block Euclidean derivative has the factor (1/n), and the inverse metric changes this to (1/d); the readout metric cancels the prediction's (1/n). For normalized neuron spaces, the rank-one action is (uv^T/n) and its Hilbert–Schmidt norm is its ordinary finite Frobenius norm. Consequently the population raw metric and all four kernel blocks are the correct counterparts of the finite dynamics.

The finite-GF continuation argument uses the gradient energy identity to bound raw path length on every finite interval. In finite dimension, this supplies a finite endpoint from which local existence restarts. It does not incorrectly infer a uniform-in-width parameter bound from that argument. GD is the stated simultaneous raw Euler method, with hidden fields recomputed along raw interpolation; the subsequent velocity proof uses that convention.

The theorem quantifies over realizable separated triples. The restriction δ ≤ 3/2 follows from the Gram geometry, and no proof subsequently assumes that Γ itself is invertible. The width assertions concern deterministic population laws and identified observables, rather than norm convergence between unassociated operators at different widths. The finite random readout is retained in both actual algorithms; the zero-readout comparisons are auxiliary fixed-program comparisons.

## 2. Adaptive Gaussian conditioning

**Locations:** F.3, (F.5)–(F.8), Theorem F.1.

This is a genuine conditioning proof rather than an appeal to an unnamed tensor-program theorem. The key adaptive step is valid: conditional on the existing transcript, a next query input is fixed, and the answer is a linear observation of the selected residual matrix. Starting from independent Gaussian matrix factors, successive conditioning preserves the product form of their conditional residual laws. Observations involving other matrices therefore do not expose additional unaccounted randomness in the selected matrix. This is stronger and more appropriate than claiming an adaptive input is independent of the original matrix.

The conditional mean in (F.6) satisfies both constraints, by (U^TY=Q^TV). Its two summands are orthogonal to the homogeneous solution space (P_{U^⊥}KP_{V^⊥}). Isotropic Gaussian projection therefore yields precisely the residual in (F.6), and applying it to the new input gives (F.7) with the stated normalized variance.

The removed projection of the fresh Gaussian has expected normalized squared norm (rankU)/n. Since each transcript is fixed and finite, this vanishes. Conditional variance estimates for bounded tests and the explicit second-moment expansion establish empirical weak convergence and convergence of second moments. They do not presuppose that trained neuron coordinates are independent. The conversion to W₂ convergence and the same-index comparison (F.3) supply the required mode of convergence.

The provisional positive-definiteness assumption is used only where fixed-dimensional Gram inversion is continuous. Its removal is a separate proved step, discussed below.

## 3. Source corrections, orientation dependence, and singular covariance

**Locations:** F.4–F.6, Lemmas F.3–F.4, (F.9)–(F.23), R.2, (R.93)–(R.94), V.3, V.I.

In the source-rule proof, each old reverse answer is its reverse source plus a deterministic combination of old forward inputs. Orthogonality of the new forward-input residual to those inputs makes (F.11) valid. Gaussian integration by parts then converts its pairing with the reverse sources into their input Gram times the expected formal derivative. Substitution in (F.7) cancels exactly the corrections already contained in old forward answers. The resulting new forward source has covariance equal to the full input second moments, including feature means. The reverse calculation has the same structure.

The independence of distinct *source groups* is maintained by adjoining a fresh independent Gaussian to the appropriate group. This does not assert independence of an answer from a later adaptive input, or independence of a transpose answer from its same-layer features. Those dependencies remain in the explicit return terms.

Singular queries are handled by adding a distinct fresh Gaussian input perturbation at each call. At fixed nonzero perturbation, the new input has a limiting squared distance of at least the perturbation variance from the old same-orientation query span. Thus the nonsingular induction actually applies. The high-probability operator bound propagates the finite-array perturbation error with a constant depending only on the fixed program. The scalar recursion is separately continuous as the perturbation vanishes: coefficient limits, covariance-square-root coupling, linear-growth bounds, and bounded continuous first derivatives close a finite induction. No inverse empirical Gram or pseudoinverse is passed through a rank drop.

The formal derivative convention at singular covariance is also coherent. Derivative vectors may change by a covariance-null direction when smooth extensions agree on the Gaussian support, but contraction with the associated input tuple removes that direction, as in (F.14). The proof never treats individual off-support derivative coefficients as uniquely intrinsic quantities.

The network source equations retain both learned matrix terms and all allowed transpose returns. Forward responses use strictly past backward queries; reverse responses include current forward queries. In particular, the current middle reverse coefficient retains the derivative through the already computed top reverse answer. The explicit formulas (R.93)–(R.94) and (V.22) agree with this order. They do not discard or invert a current return, and singular sample covariance is not confused with sample independence.

For physical scalar feedback, the finite oracle construction is causal. Moment contractions and residual coefficients converge using normalized (L^2) comparison, while formal derivatives freeze the resulting deterministic coefficients. The response calculations do not differentiate a normalized residual at zero.

## 4. Common generated spaces and actual adjoints

**Locations:** F.7–F.8, (F.24)–(F.33).

The countable language has a finite-prefix causal enumeration. Every finite union of programs has the limiting same-layer law established above, and unused instructions do not alter the exact finite vectors. This gives the needed consistent law of countably many coordinates.

The generated nodes are dense in the (L^2) space of their own generated sigma-field: finite-coordinate functions are dense by the cylinder-set approximation, and bounded smooth coordinate approximants are dense for each finite-dimensional law. The construction does not assert density in a larger arbitrary probability space.

The finite high-probability inequality (∥A_nu_n∥_n ≤ 10∥u_n∥_n) passes to deterministic limiting squared norms on the generated span. This proves that a zero (L^2) input has a zero answer, that different expressions for the same input agree, and that the assignments extend as bounded linear maps. Finite linearity passes by the same argument.

Most importantly, the exact finite transpose identity passes to limiting pairwise contractions on dense generated subspaces and then to their completions. The reverse maps are therefore the actual Hilbert adjoints in (F.27). This is sufficient for all later raw-gradient and kernel identities; no unrelated reverse Gaussian operator is substituted.

Arbitrary fixed real coefficients and Lipschitz coordinate instructions are recovered by approximation of fixed programs and bounded-action continuity. Learned increments are integrals of rank-one Hilbert–Schmidt operators. The argument needs neither a Hilbert–Schmidt initialized action nor convergence of initialized matrices in an operator topology across widths.

## 5. Hilbert-space differentiation and local capped dynamics

**Locations:** F.9–F.11, Theorem F.7, (N.6)–(N.9), V.6.

The manuscript correctly avoids claiming that every bounded-derivative scalar nonlinearity defines a Fréchet differentiable (L^2)-to-(L^2) Nemytskii map. The bounded multiplier lemma proves continuity when the other factor converges strongly in (L^2). It gives the strong chain rule along curves and the backward-field continuity actually needed.

The scalar predictor differentiability proof has a separate valid weighted Taylor estimate. With a fixed (L^2) weight, truncate the weight to use the quadratic remainder on its bounded part and the linear remainder on its (L^2) tail. This is (o(∥q∥_2). Successive adjunction then produces the raw Fréchet derivative of the scalar prediction. Rank-one estimates prove continuity of its gradient. The same argument establishes the hidden feature-energy differential used in Part N.

At fixed cap, both partial derivatives of the backward gate are bounded. Forward Lipschitzness, bounded actions, and rank-one estimates therefore give a locally Lipschitz field on a raw primal ball. The supplied integral-contraction and Euler-defect arguments establish local existence, uniqueness, and fixed-cap approximation without requiring an unproved smoothness theorem for the uncut infinite-dimensional field.

## 6. Uniform controlled response estimates

**Locations:** R.1–R.9, especially (R.7), (R.23)–(R.29), (R.33)–(R.35), (R.46)–(R.90).

The affine hypothesis is explicitly a finite-array, positive-mesh hypothesis, rather than a conclusion silently inferred from a continuous affine flow. Part G subsequently verifies it with slack for all the meshes admitted in Part R.

The affine Gaussian-probe argument is valid. One fresh independent Gaussian is inserted with deterministic signs into separately named answer slots, and the finite raw comparison bounds the resulting output pairing. At a fixed perturbation amplitude, the finite-program theorem identifies the pairing. With scalar coefficients frozen, its derivative with respect to the probe is precisely the signed sum of the relevant source derivatives. Continuity at fixed mesh justifies sending the amplitude to zero *after* the width limit. This avoids interchanging a derivative with a width limit. A single past-time insertion retains its factor (h_j). Taking signs bounds the absolute row of deterministic expected coefficients, with the sample/block norm conversion accounted for.

The nonlinear same-state comparison uses (|D(z,q)-aq|≤ε|q|) and bounded nonlinear forward remainders. Comparison with the affine field yields (R.33) without a cap-dependent nonlinear Lipschitz constant. This establishes query norms, source variances, and learned-moment differences *before* response-row closure, removing a potential circularity.

Given bounded coefficient prefixes, the (L^p) estimates use Minkowski and discrete Gronwall; their time maxima are maxima of deterministic norms, not random suprema. All source correlations are retained. The exponential derivative envelope is integrable by convexity over mesh weights and the marginal incoming subgaussian bounds; no time independence is used. The terminal incoming multiplier in (R.54) is present and is controlled separately in (R.58).

The differentiated source equations (R.46)–(R.49) contain the gate derivatives in both arguments, including the clip derivative. Their nonlinear-to-affine comparison is first at the *same deterministic arrays*, and only subsequently at the actual affine baseline arrays. This distinction is essential and is observed in (R.59)–(R.77).

The deterministic stability equations retain current dependencies in the order (A^2_k,A^3_k,B^3_k,B^2_k). The first two stages require only past backward rows. The top reverse row is then bounded before the middle reverse row uses it. The integral quantity (I_k) contains only completed past rows. Equations (R.79)–(R.89) and the product identity (R.92) therefore close an actual chronological induction; they are not a simultaneous bootstrap on unknown current rows.

I checked the gain and step factors in these recursions and the domination chain defining ε_*. All constants are finite functions of the fixed numerical arguments. The chosen amplitude makes the row discrepancies smaller than the available unit slack, uniformly in cap, covariance, number of steps, and mesh irregularity.

## 7. Geometry, residual control, and global construction

**Locations:** G.1–G.6, (M.21), V.2.

The augmented-Gram lower bound is valid even for singular Γ. For a mixed-sign three-vector, the displayed two-by-two quadratic form has determinant (D^2), trace at most four, and (D≥δ). Also (A^2+b^2) dominates the original coefficient norm. This proves the uniform δ^2/4 bound actually used.

Initial Gaussian linear projection gives (a^2(11^T+Q)) as a lower bound on each feature Gram. Common marginal variances make its linear coefficient common across samples. Iteration gives the readout lower bound λ a^6 I without assuming a full-rank input Gram.

The stopped controlled estimates bound hidden displacement by (10^6a^6s^2) and readout norm by (800a^3s), with identical estimates for arbitrary positive Euler meshes. The identity for ∑ h_js_j rules out a discrete overshoot as well as a continuous exit. The numerical lower bounds on (a) imply the stated slack in (G.18) and the preactivation displacement bound (G.19).

The capped dynamics need not be a gradient flow. The proof instead derives their actual residual equation with the possibly nonsymmetric hidden contribution (J_hU_{h,R}), bounds its norm, and lets the readout coercivity dominate it. This gives exponential residual decay and a total residual clock at most (S/2), excluding the stopped clock endpoint (S). It verifies the affine hypothesis with (B=12) and gives one response threshold for every physical horizon.

The passage of controlled response moments to capped physical flows first freezes their deterministic effective controls and uses sufficiently fine meshes with total effective duration less than (S). Thus it does not require random-control or growing-transcript versions of Part F.

Cap removal uses the valid asymmetric gate comparison (V.10). Only the lower-cap reference needs tails. In the backward substitutions, each new factor (R) multiplies a forward discrepancy, while preceding backward discrepancies encounter only bounded actions and bounded derivatives in the incoming argument. Hence the loss is linear in (R), not an unproved product of cap factors. The subgaussian reference tail wins against the ensuing exp(C_TR). States and raw directions are uniformly Cauchy, so the limit is strong (C^1) and satisfies the uncut equations.

The same reference-only comparison proves uniqueness against any bounded-primal strong competitor, and works from a reached state with the small initial discrepancy from its cap reference. Existence and uniqueness are not inferred from a nonexistent general local-Lipschitz theorem for uncut (L^2) states.

The nonlinear margin argument is also complete. R(σ G) is positive for every finite positive σ, continuous, and has a positive limit at infinity. The regression-slope bound makes R stable in the asserted (L^2) neighborhood. The controlled displacement stays inside that neighborhood for all times, proving (M.19).

## 8. Finite algorithms, true kernels, velocities, and path laws

**Locations:** V.3–V.11.

The fixed-cap nonlinear Gaussian probes are justified by fixed-transcript integration by parts and continuity of expected derivatives. Their stability comparison recomputes all residuals, so it does not omit scalar feedback effects. The expected source-row bound is kept distinct from the pointwise absolute derivative-row bound, which is established separately by (V.24)–(V.25).

Velocity products cannot be inserted directly into Part F because their coordinate derivatives are unbounded. Section V.5 explicitly truncates them. The first appended action has an integrable derivative-row bound (K(1+|P^1|)); only after its coefficients, source covariances, actual action, and moments are identified is the second action treated. Nested truncations and the stated limit order justify both source formulas. No (L^p)-operator bound for initialized matrices is assumed.

The deterministic velocity comparison truncates only the reference factor of bounded multiplier products. The upper-layer recursion produces one truncation factor (M), since it multiplies a forward discrepancy. Fixed-cap Euler nodes have the required fourth moments by the preceding velocity argument. After cap removal, compactness of a continuous (L^2) velocity path supplies uniform tails instead; the proof does not multiply the cap-removal error by an uncontrolled cap-dependent fourth-moment constant.

At a fixed auxiliary mesh, exact update lengths bound finite action norms and supply a primal ball with slack. Fixed-cap Euler defects then compare actual finite GF and arbitrarily fine raw Euler to the coarse reference with width-independent constants at that cap. The small initialized readout is handled by a same-width comparison, and is never erased from actual training. Only fixed transcripts are identified probabilistically.

True backward observations at capped states are distinguished from capped update fields. Their appended transpose/gate chain has its own nested-truncation argument. Consequently the four full true kernel blocks, including off-diagonals, are identified without misusing the capped residual equation as a true-kernel equation.

The same-width uncut comparisons use empirical tails of the finite cap reference, passed from its fixed-cap W₂ convergence. First-exit estimates provide the required finite-horizon containment. For raw GD, the comparison uses its actual preceding-node field, with a separate cap-reference within-step error. No width-independent Lipschitz constant for the uncut finite field or Gaussian theorem for (n^2T) instructions is invoked. The two algorithms share a reference and therefore have joint convergence to the same limits.

Uniform-time and finite-joint-time field/velocity laws follow by same-neuron couplings and the ordered width/mesh/cap/truncation limits. The path-space assertion has an additional necessary argument: the observation-grid interpolation error is bounded by (4h) times integrated squared speed. This yields W₂ convergence in the path supremum norm and finite second moments there. Integrated squared-speed and same-layer cross-moment convergence follow from uniform-time second-moment convergence. Generated probes pass through bounded action and adjoint comparisons in the same limits.

## 9. Initial acceleration and actual kernel variation

**Locations:** V.I, N.1–N.7.

The initialization observational extension proves the expected derivative formulas by truncation before using them. In particular, the return coefficients in (N.13)–(N.14) include the derivatives of both the gate and the incoming field. The reverse source covariances are full input Grams and are independent of the appropriate forward sources, rather than the complete returned inputs being assumed independent.

The augmented feature Gram makes the top initialized Gaussian tuple nondegenerate. If the top backward Gram had a null vector, continuity and full support would give (N.11) everywhere. The first factor has no open zero set because each relevant partial derivative is nonzero; differentiating the remaining identically zero factor then forces every coefficient to vanish when (e>0). Thus (S_3) is positive definite. Conditional covariance propagates positivity to (S_2) and the bottom fields. This proves nonzero hidden parameter blocks and every bottom sample, including singular input geometries.

The affine upper-layer formulas (N.22)–(N.23) have the correct gain factors. The finite Gaussian calculation for (B^TH) includes the mean (v), the isotropic covariance, and the (vv^T/n) term. Trace concentration is not inferred from expectation calculations alone: independent Gaussian trace probes, the finite-program limit, and uniform operator moments supply deterministic trace limits and uniform integrability. The resulting traces (1,2) and (1,1,2,2,3) give the completed-square lower bounds (N.33) and (N.38). Sign symmetry in the top calculation legitimately removes the cross term.

The perturbation estimates in N.5 compare the nonlinear derivative gate with the constant affine gate, so they need no unproved (L^∞) control on preactivation differences. The displayed norm and difference arithmetic bounds both upper preactivation directions by a common perturbation error (2·10^8a^7e). Under the specified cutoff this is less than half each affine lower bound. Positivity is therefore established for every sample in every layer.

Finally, (C(t)/t→3H) and bounded-multiplier continuity give (b_i^ℓ(t)/t→3β_i^ℓ). The actual physical equations then give hidden acceleration (9V), displacement (9/2)t^2V+o(t^2), and the stated field accelerations. These are valid right derivatives at the initial endpoint, without a second ambient Fréchet derivative of the activation map.

For the projected kernel, the hidden gradient contributes (9t^2∥V∥^2), and the scalar feature-energy differential contributes the same amount through the readout block. Their sum is the coefficient (18) in (M.20). Since the hidden directions have already been shown nonzero, this proves variation of the actual total projected kernel.

## Final assessment

The theorem's proof obligations are met within the supplied manuscript. I found no theoretical counterexample under its stated assumptions, no unsupported nonclassical external invocation, and no remaining gap in the conditioning, singularity handling, operator construction, response closure, cap transfer, finite-algorithm limits, or nontriviality arguments. **No repair is required by this review.**
