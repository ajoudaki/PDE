# Independent mathematical referee report

**Verdict: PASS.** I found no unresolved mathematical correctness or completeness objection to Theorem M.1 after auditing the full manuscript, including the internal results on which the dynamics and observation arguments depend. This verdict is for the manuscript identified below and its stated quantifiers: a fixed admissible dataset, fixed selected activation, and each fixed finite physical horizon. It does not assert an interchange of infinite time and infinite width.

## Input isolation and reading coverage

The sole reading input was `/tmp/manuscript-9fe58d95d81c/REPORT.md`. I read no other file, skill, source note, review, project history, project state, or website. I did not communicate with other agents and performed no numerical experiment. The only written output is this review.

The manuscript contains **3,547 lines and 210,133 bytes**. Its SHA256, checked before and after the reading, is:

`fdbfa412195aedfbdae103b1e7e862dd42fffd5061e662dbda7dfe462eab0f7c`

I read the entire file in these contiguous, bounded, nontruncated chunks: lines 1–240, 241–480, 481–720, 721–960, 961–1200, 1201–1440, 1441–1680, 1681–1920, 1921–2160, 2161–2400, 2401–2640, 2641–2880, 2881–3120, 3121–3360, and 3361–3547. This covers all of Parts M, F, R, G, V, V.I, and N. No internal lemma was accepted merely because it had a label; its proof and subsequent uses were checked.

My principal perspective was training dynamics and limit theorems. I also audited the Gaussian foundation, controlled estimates, global argument, and initial-motion lower bounds because the principal conclusions depend on them.

## 1. Finite model, normalization, and theorem quantifiers

**Locations:** M.1–M.4; F.8–F.10; V.1 and V.9; N.6–N.7.

The readout is explicitly `n^{-1} C^T h^3`, and the loss is a sum over the three samples, not their average. With the metric (M.6), the first Euclidean gradient block has factor `1/n`, multiplied by inverse metric `n/d`; the two middle blocks keep their Euclidean `1/n`; and the readout's inverse metric cancels its Euclidean `1/n`. This gives precisely (M.7). The normalized rank-one action is `uv^T/n`, whose Frobenius norm equals the product of the two normalized vector norms. Thus the Hilbert–Schmidt population updates and their raw metric are the correct counterparts of the actual finite update.

The kernel factors in (M.15), (F.44), and (V.52) follow from that metric. In particular, the first block has `Gamma_ij`, without an additional factor of `d` or `n`, and the readout block is the feature Gram. The identity for the finite loss dissipation in (V.54) has the matching metric. Its finite-time length bound suffices to prevent finite-dimensional GF explosion; the manuscript supplies the endpoint/continuation argument. No energy-dissipation identity is incorrectly applied to the capped surrogate flow.

The actual finite random readout is retained. Its normalized squared norm has expectation `n^{-2}`, so comparison with a zero-readout auxiliary program is justified at fixed cap and fixed program. The subsequent same-width comparisons retain the actual initialization. The vanishing population readout is a limit conclusion, not a replacement of the finite training algorithm.

The raw GD update is simultaneous explicit Euler. Along its raw linear interpolation, fields are recomputed and its actual direction is the vector field at the preceding node. The velocity comparisons retain this distinction and accommodate the right-node/terminal-left convention. The prescribed step `n^{-2}` is used through a deterministic vanishing Euler defect; the argument does not invoke a Gaussian theorem for a program of length proportional to `n^2`.

The separation hypothesis permits singular `Gamma`. Its feasibility restriction and the data-dependent versus separation-dependent constants are consistently stated. The construction of `a_delta` and `e_delta` uses only delta through finite positive constant chains. Quantifiers in the theorem match those in the proof: compact physical-time convergence in probability along the full width sequence, without an assumption of independence across widths and without an infinite-time/width interchange.

**Assessment:** No normalization, initialization, or quantifier objection.

## 2. Gaussian conditioning, response terms, and singular queries

**Locations:** F.1–F.6, especially (F.6)–(F.14).

The conditional matrix law is derived from the two actual constraints `WV=Y` and `W^T U=Q`. The stated conditional mean satisfies both constraints by their compatibility relation; its orthogonality to the homogeneous constraint subspace gives the isotropic Gaussian projection formula. The induction justifying adaptive conditioning conditions on each query input after it is measurable from the transcript. It therefore does not require an adaptive input to have been independent of the matrix before conditioning.

In the new-query formula, removal of the finite-rank projection of fresh Gaussian noise has expected normalized square equal to rank divided by width. Under the provisional positive-definite limiting Grams, the remaining coefficients and variance converge. Conditional bounded-test and second-moment estimates supply joint empirical weak convergence and second-moment convergence, hence the required Wasserstein convergence.

The source-response derivation retains both matrix orientations. Gaussian integration by parts converts the conditional regression correction to expected formal derivatives. The cancellation involving old forward responses is explicit. Distinct oriented source groups may be independent even though their matrix answers are not: the opposite-orientation return terms carry the dependence. This distinction is respected later, including the current returns in R and V.I.

Singular Grams are handled by adding an independent fresh input perturbation at every query. For fixed perturbation amplitude, the new Schur complement is bounded below by its squared amplitude. The coupled finite-program discrepancy is bounded without inverse Gram estimates. Continuity of the finite scalar recursion is then proved through positive-semidefinite square roots and bounded formal derivatives. Consequently the width limit is taken at fixed perturbation, followed by perturbation removal; no continuity of a pseudoinverse at rank loss is assumed. The nullspace observation following (F.14) explains why separately named derivatives on singular supports have invariant contracted corrections.

Causal scalar feedback is reduced to deterministic limiting coefficients by a finite induction with inner-product and scalar-multiplication estimates. It does not differentiate residual feedback in a source derivative. This is exactly the form used by the Euler and controlled programs.

The operator-norm bound is obtained by a finite sphere net and Gaussian tails. The subsequent moment and trace-probe statements follow from that bound and an explicit conditional Gaussian quadratic-form variance. No random-matrix limit theorem is silently substituted for these calculations.

**Assessment:** The fixed-program theorem and its advertised singular and feedback extensions are proved in the required form. No omitted return term or rank-stability assumption was found.

## 3. Common spaces, adjoints, and differentiability

**Locations:** F.7–F.11; N.1.

The countable generated language supplies compatible finite-dimensional laws because every finite union is again a finite program. Limiting linearity and the inherited operator bound define actions on the generated span. The density argument extends them to the full generated `L^2` spaces. Passing the finite transpose identity on a dense span establishes actual Hilbert adjoints; reverse actions are not independently resampled operators.

The initialization consists of bounded actions, with only learned increments required to be Hilbert–Schmidt. The rank-one norm, adjoint, difference, and pairing identities used for those increments are proved and agree with normalized finite matrices. The construction does not require operator-norm convergence between unrelated matrices at different widths.

The distinction between a curve chain rule and a global `L^2` Nemytskii Fréchet derivative is handled correctly. Bounded multiplier continuity proves the strong chain rule along the constructed curves. For the scalar predictor and scalar feature energy, the weighted Taylor estimate splits the fixed `L^2` weight into bounded and small-tail parts. Applying it successively from the top layer down gives a scalar Fréchet remainder of the required order. Continuity of the gradients follows from the same multiplier and rank-one estimates. This justifies the raw gradient identity and later scalar energy expansion without requiring an unjustified second derivative of the activation map on all of `L^2`.

At fixed cap the gate is globally Lipschitz in its two scalar arguments, so the locally Lipschitz Hilbert-space vector field and its integral contraction construction are justified. Measurable controls yield absolutely continuous paths, while the autonomous physical capped flow is strongly `C^1`. These distinct regularity statements are used consistently.

**Assessment:** No functional-analytic gap in the state, adjoint, gradient, or chain-rule construction.

## 4. Controlled response bounds and their closure

**Locations:** R.1–R.9, with the affine hypothesis verified in G.3.

I checked the source system against exact rank-one unrolling. The learned forward and reverse contractions in (R.11)–(R.12) have the correct control weights and time ranges. Forward returns use strictly past reverse inputs; reverse returns include the current forward block. The construction order `A^2_k, A^3_k, B^3_k, B^2_k` matches the actual explicit schedule.

The affine raw stability bounds control both ordinary program perturbations and additive answer probes. The Gaussian probe uses an independent root reused with chosen deterministic signs. At fixed mesh and amplitude, its limiting pairing is identified first. The formal derivative coefficients are then passed as amplitude tends to zero, rather than exchanging a derivative and a width limit. A perturbation at a single past time carries that step size, which is essential for unequal meshes and a mesh-independent forward-row estimate. The conversion from scalar output-row sums to block-row sums is accounted for.

The nonlinear primal comparison uses the affine field's Lipschitz bound and a same-state perturbation bounded by a multiple of the amplitude. It does not import a cap-dependent nonlinear Lipschitz constant. It independently bounds all source variances and learned-moment discrepancies before response estimates are used, avoiding a circular variance premise.

On bounded coefficient prefixes, the coordinate moment recursions use maxima of deterministic `L^p` norms and Minkowski, not random time maxima or an `L^p` matrix-action bound. The derivative equations include the derivatives of the clips and the terminal incoming-field multiplier. Their exponential envelopes are integrable by convexity over the weighted time sum and the established one-time sub-Gaussian bounds; time-source independence is unnecessary.

The same-array affine derivative comparison is explicitly distinguished from comparison with the actual affine baseline. I checked the subtractions (R.59), (R.62), (R.65)–(R.66), and the coefficient recursions (R.69)–(R.87): the current rows enter only after their required predecessors have been bounded. The reverse-source perturbations preserve the individual step-size factor. The large constants absorb the displayed derivative and moment remainders, and the final finite-product bound controls the accumulated past row discrepancies.

The closure in R.9 is chronological. In particular, bounding the new middle forward row does not assume a bound for the as-yet-unconstructed current middle incoming field; the top reverse row is available before the current middle reverse row is estimated. The explicit formulas (R.93)–(R.94) retain both current returns. The positive amplitude in (R.90) is selected from previously specified finite constants. Although extremely small, it is mathematically positive and independent of mesh, cap, controls, and geometry beyond the stated parameters.

**Assessment:** The affine premise is not silently assumed globally; G.3 verifies it. I found no circular prefix estimate, missing current term, or unjustified moment/action estimate.

## 5. Uniform geometry, residual clock, and global uncut flow

**Locations:** G.1–G.6; V.2.

The augmented three-input Gram lower bound handles a mixed-sign coefficient vector by projection onto the singled-out input. The two-dimensional matrix has determinant `D^2` and trace at most 4, giving the stated `delta^2/4` lower bound. This covers degenerate input Grams.

The initial Gaussian feature projection uses the common marginal variance to obtain a common coefficient at least `a`. Its orthogonal residual Gram is positive semidefinite, producing the iterated readout coercivity. The positivity of the nonlinear regression margin follows from full Gaussian support, continuity over positive scales, and its strictly positive large-scale limit. Its stability under `L^2` perturbation includes a lower variance bound and a bounded optimal regression slope.

The control-clock estimates bound readout growth linearly in control time and hidden displacement quadratically. The same calculation applies to every positive Euler mesh, using the exact sum of `h_j s_j`; the first-overshoot argument addresses coarse meshes. Substituting the selected constants gives the strict slack claimed in (G.18)–(G.19), including the amount needed for readout coercivity and the nonlinear margin.

For capped physical dynamics, the residual equation uses the true prediction differential applied to the capped update directions. Its hidden contribution need not be positive or symmetric; the manuscript bounds its absolute operator norm and lets the readout Gram dominate it. This supplies exponential residual decay and a total residual clock at most `S/2`, excluding the clock stop with slack. Fixed-cap bounded states and speeds then give global continuation.

The response threshold is chosen at this one clock horizon. Fine physical Euler meshes produce deterministic effective controls and mesh sizes after the scalar limit, with total clock below `S`. The controlled estimates pass to fixed-cap flows by strong convergence and truncated moment bounds. Thus the incoming-field tails used for cap removal are uniform over physical horizons and caps.

The asymmetric gate comparison (V.10) is valid: truncate only the reference input in the change-of-preactivation term, while changing the other input through the uniformly bounded input derivative. Sequential substitution loses only one factor proportional to the reference cap. Gaussian reference tails therefore beat the Gronwall factor `exp(K_T R)`. This gives Cauchy raw paths, directions, and backward fields, hence a strong `C^1` uncut limit. The same reference-only comparison proves uniqueness against bounded-primal strong competitors without requiring tails for those competitors. It also proves unique continuation from a reached state.

**Assessment:** The global argument closes on one preselected activation; no dependence on an unknown trained trajectory or a changing physical horizon enters its selection.

## 6. Fixed-cap observations, unbounded products, and velocities

**Locations:** V.3–V.8; V.I.

The nonlinear source-row probe argument recomputes the actual finite residuals after a query perturbation. Its raw stability estimate therefore accounts for all three residual coefficients. In the limiting source derivative these coefficients remain frozen, as required by F. The continuity proof is finite and includes singular covariances. Expected response-row bounds are not confused with expectations of absolute derivative rows; V.4 proves the latter separately by causal inequalities.

The appended velocity queries have the actual chain-rule form: parameter-direction terms plus current matrix actions on lower feature velocities. Their feature multiplier is always the true activation derivative. Such products are not directly submitted to the bounded-derivative program theorem. The manuscript first truncates their incoming factor, proves the required derivative domination and moment bounds, and then removes clips in the stated nested order. The first appended action is established before its moment and derivative information is used for the second. New named forward sources keep their same-family covariances while having zero formal derivative in the independent transpose-source arguments.

For observational product convergence, bounded multiplier continuity and convergence of tail second moments suffice. The argument never requires finite-array fourth moments from empirical `W_2` convergence. Matrix-action continuity transfers the clipping discrepancy. The analogous true-backward chain in V.8 is established separately from capped update fields, with nested truncation and actual adjoints. Where source derivatives of those uncut initial observations are later needed, V.I supplies an additional dominated-derivative proof; its integrable envelopes and ordered clipping limits justify (V.I.1)–(V.I.3).

The deterministic velocity comparison (V.40) truncates only reference preactivation velocities. Its induction has a single factor of the truncation level because that factor multiplies an already-controlled forward-state discrepancy. Fixed-cap Euler node velocity moments are proved before they are used to obtain the continuum velocity bound. Cap-dependent moment constants are not subsequently multiplied by an uncontrolled cap-removal error.

**Assessment:** No unproved product closure, hidden `L^p` action assumption, or circular velocity-moment argument remains.

## 7. Finite algorithms, true kernels, path laws, and limit order

**Locations:** V.6–V.11.

At a fixed auxiliary mesh, the finite-program theorem identifies all required node tuples and update-length contractions. Exact rank unrolling bounds finite current operator norms; convergence of trained operator norms across widths is not assumed. This produces the primal ball and slack used in deterministic comparisons. The Euler defect is controlled on that ball with constants independent of width at fixed cap. First-exit comparisons justify existence/boundedness before using estimates over the complete horizon.

The fixed-cap limit takes width at fixed auxiliary mesh and fixed query clips, followed by mesh refinement. The growing number of raw GD steps contributes solely a deterministic defect. Fine Euler directions are compared at their actual preceding nodes. Neuron-index couplings and finite joint transcripts yield uniform-time field/velocity `W_2` convergence and finite collections of joint observation times.

The true-kernel observation proof includes all four blocks and all off-diagonal contractions. At capped states it explicitly distinguishes the true observed gradient kernel from the matrix governing surrogate residual dynamics. For actual uncut finite algorithms, reference-only gate estimates transfer states, raw directions, and backward fields from a fixed capped reference, then remove that cap. The common initialization allows the GF and GD conclusions to hold jointly by the same comparisons and a finite union of probability bounds.

For velocity cap removal, the uncut population velocity is already a continuous `L^2` path. Compactness of its time image supplies uniform tail control. The order is cap at fixed tail level, then removal of that level. The finite counterpart takes width first at fixed cap and level. This correctly avoids assuming cap-independent higher velocity moments.

The path-space assertion is supported by more than fixed-time distributions. The interpolation inequality (V.57) bounds squared supremum-norm path error by observation-grid size times integrated squared speed. The raw state/direction bounds give the required RMS speed bound for actual recomputed fields, and their integral representatives give continuous population versions and finite path-norm second moments. Joint node `W_2` convergence then passes through interpolation before the observation grid is refined. Uniform velocity `W_2` convergence separately supplies convergence of squared speeds and their integrals.

Fixed generated probes pass by a finite succession of Lipschitz coordinate operations, contractions, and bounded current or initialized actions in either orientation. The proof does not claim the same for a width-dependent growing probe expression. Full-sequence convergence in probability requires no cross-width initialization coupling.

**Assessment:** The limit orders support all observations stated in M.1. No unsupported upgrade from fixed-time laws to path laws, or from second moments to higher empirical moments, was found.

## 8. Nonzero initial motion and projected kernel expansion

**Locations:** N.1–N.7, using the fully checked V.I and F trace-probe results.

The top feature covariance is positive definite even when `Gamma` is singular, by the augmented-Gram argument. Thus the top initialized preactivation triple has full support. For positive nonlinearity, the continuity/full-support argument in (N.11) forces the top backward Gram to be positive definite: the first factor has no open zero set, and differentiating the second factor separately in each coordinate forces every coefficient to vanish.

The transpose formulas retain the return terms while giving independent fresh reverse source covariance. Conditioning on the relevant forward tuple therefore yields the positive conditional covariance bounds at the middle and bottom. These prove positivity of all three hidden parameter directions and every bottom sample, including geometries with vanishing affine bottom motion. The rank-one trace calculation for the matrix directions and the first-layer metric factor are correct.

I recomputed the affine upper-layer formulas. They give `U_j^2 = a^4[(gamma_j+m)I + gamma_j AA^*]Q` and the stated three-term operator for `U_j^3`. The finite proxies use limiting deterministic feature-Gram coefficients; the manuscript expressly justifies replacing empirical contractions by those coefficients rather than declaring finite equality.

For the middle lower bound, conditioning on the other matrix yields the exact mean and covariance of `B_n^T(am 1+B_n v_n)`, including the `v_n v_n^T/n` term. The trace moments `1,2` of the first Wishart factor give `(m+2 gamma_j)^2+gamma_j^2`. For the top bound, parity removes the cross term and row-sign/permutation invariance identifies the constant-vector quadratic form with the normalized trace in expectation. The supplied fourth-moment expansion gives the mixed trace values `1,1,2,2,3`; expansion and completion of the square yield (N.37). Fixed-program trace probes establish deterministic convergence, and operator moment bounds justify passage of expectations and products. Thus these are not merely expectation calculations being used as concentration claims.

The affine lower bounds are uniform over each individual sample and admissible binary-label configuration because `|m| >= 1/3`. The direct nonlinear perturbation bounds use the constant affine gate, so comparing it with the nonlinear gate needs only the uniform difference at most `e`. The rank-one and propagated sample-direction estimates have sufficient slack for the cutoff `(10^{10}a)^{-1}`; the chosen theorem cutoff is smaller. Consequently every upper preactivation direction remains nonzero, as does its feature direction because the activation derivative is at least `a`.

The physical time factors are consistent with `p=y/3`: `C'(0)=3H`, `b_i(t)/t -> 3 beta_i`, and `theta_h'(t)/t -> 9V`. Strong multiplier continuity and the chain rule establish the right initial second derivatives without assuming an ambient second Fréchet derivative. Integrating gives hidden displacement `(9/2)t^2 V + o(t^2)`.

Finally, the hidden part of the projected predictor gradient contributes `9t^2 ||V||^2` to the kernel. The scalar feature-energy differential contributes another `9t^2 ||V||^2` to the readout Gram term. Their sum is exactly the coefficient `18` in (M.20), with strictly positive hidden norm. No loss-average or readout normalization factor is missing.

**Assessment:** All stated initial-motion assertions and the projected actual-kernel expansion are supported.

## External results, severity, and repair requirements

I found no advanced external result whose missing proof or unchecked hypotheses block validation. The critical Gaussian program theorem, singular-query extension, action-space construction, cap-transfer estimate, trace identifications, product extensions, and path approximation are internal and proved in the manuscript. The remaining uses of basic integration, finite-dimensional linear algebra, Gaussian integration by parts, completeness, and elementary measure approximation are either derived or applied with the required hypotheses.

There are **no unresolved major or minor mathematical objections requiring repair** in this audit. The proof's strict limitations are material and should be preserved: fixed admissible data and activation, compact physical-time convergence, fixed finite generated probes, separate layer probability spaces, actual adjoints, and explicitly ordered cap/mesh/product limits. Under those stated limitations, the theorem is validated.
