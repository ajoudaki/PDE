# Independent adversarial review A

Verdict: **PASS** for the written local, fixed-depth theorem and its necessary response lemma. I found no fatal, major, or remaining substantive minor mathematical objection. This verdict concerns the stated fixed positive interval, fixed dataset and input dimension, Gaussian middle matrices, and every sequence of positive GD step sizes tending to zero. It does not certify an all-time theorem, a growing-depth or growing-dataset limit, non-Gaussian middle-matrix universality, or arbitrary-depth strict activity.

I read the two proof files without relying on prior-review claims and checked the relevant primary-source statements directly. Reviewed versions:

- `GENERAL_POPULATION_GF_PROOF.md`, 524 lines, SHA-256 `792dbd8eca426dc8fd5434d67b183826025a7a301f42fd579d6332fa458005e2`.
- `GENERAL_DEPTH_RESPONSE_PROOF.md`, 540 lines, SHA-256 `3dfb63e3cac21ee15573af7f4107287f58dc2013db7e4a11083c90472bf8995b`.

The activity companion was also read as a scope and consistency check. The verdict does not use its statement that earlier checks passed. The activation-example paragraph added during review was checked separately: its softplus, exact-GELU, and SiLU derivatives and its piecewise-quadratic C1,1 example are correct. Line references below use the final versions identified above.

## 1. External input and exact response representation

The finite-computation use of [Tensor Programs III, Setup 2.2, Box 1, Theorem 2.10, and Remarks 2.11–2.12](https://arxiv.org/pdf/2009.10685), printed pages 6–9, is valid. The source permits polynomially bounded measurable coordinate maps and measurements, Gaussian matrix reuse in both orientations, and singular limiting covariances. Its derivative rule uses the literal symbolic expression in Gaussian innovation slots. The proof correctly freezes deterministic expectations, coefficients, and covariance laws in those derivatives.

In the response file, lines 96–177, the forward correction at layer ell sums previous backward sources; the backward correction sums current and previous forward sources. These are exactly the opposite-orientation calls that have already occurred in the forward-then-backward program. The learned rank-one terms have their own coefficients and do not acquire an erroneous sigma-squared factor. Different orientation families are independent at the innovation level; the response terms retain the dependence caused by matrix reuse. Correlated or duplicate slots must remain separate formal arguments, as they do here.

For C2 activations the needed slot derivatives involve only bounded first and second activation derivatives and finitely many polynomially bounded fields. The non-smooth quantile transforms are independent root operations and are never differentiated in a matrix-innovation derivative.

## 2. Weighted sensitivity and noncircular caps

The substantive uniform estimate is proved, rather than obtained from the fixed-program theorem. I checked the two distinct derivative arguments in the response file, lines 290–423.

For a full forward-slot derivative row, the current backward response contributes at most its deterministic absolute row sum times the maximum preactivation derivative row. Differentiating delta adds the pointwise factor |P| through phi''. The forward memory then multiplies each source by at most f_ell Delta omega_b. Consequently the growth term is the weighted average sum_b omega_b |P_b,u| in equation (26). The maximum over derivative rows does not introduce a maximum over the random P fields.

For one backward-slot derivative, the direct derivative is a single Kronecker pulse. Its first contribution to a preactivation carries Delta omega_b, including in the first-layer update with the Gram factor. Every subsequent contribution remains inside the weighted memory sum. Equation (31) therefore preserves this source factor, and equation (32) introduces neither dataset-size dependence nor an inverse small weight.

Jensen's inequality in equation (14) controls the exponential of the weighted time integral using only marginal subGaussian bounds. It requires no independence across inputs or times. The exponents in equations (28) and (32) vanish with T once their caps have been selected.

The cap order in lines 425–487 is noncircular: c caps are selected bottom-up using prefactors that contain no a cap, a caps are then selected top-down, and T is chosen last. At each time, current forward responses use already constructed lower forward fields and past backward histories. Current backward responses use already constructed higher backward responses. No current coefficient needs itself to have already been bounded. At time zero the top-down construction begins with the given readout root; zero or centered readout is unnecessary.

The variable-step argument at lines 503–514 also correctly covers fields recomputed at affine parameter interpolation times by appending a partial final Euler update.

## 3. Initial tails and the preliminary ball

Population-proof lines 166–182 give an admissible exact encoding of the stated scalar subGaussian initial laws. A subGaussian quantile composed with the standard Gaussian distribution function is bounded in magnitude by C(1+|g|), including for atomic laws. Independent centered first-weight entries give subGaussian input projections with a bound depending on B_in X, rather than on d. The scalar quantile representation is used only for a fixed computation; its number of roots can depend on the fixed d without affecting the marginal tail estimates used for the time interval.

The preliminary operator/RMS bounds at lines 214–240 use only bounded activation derivatives and linear activation growth. The forward recursion, backward recursion, residual bound, and rank-one operator norm give width-independent bounded parameter velocities on a larger ball. The first-exit argument therefore supplies the interval required by the response lemma without presupposing its tails. Initial concentration is required only for the fixed finite dataset.

## 4. Common operator realization

Population-proof lines 184–203 give a valid common realization through finite unions of the countable program family and their generated operations. Consistency follows from the same finite initial arrays. On the generated span, simultaneous second-moment convergence transfers the finite matrix norm bound to the limiting action. It also makes that action well-defined on L2 equivalence classes. Completion extends the action continuously. The finite adjunction identity transfers for every generated pair and then extends by density.

The cited [Tensor Programs IVb, Definition 2.6.7 and Propositions 2.6.8–2.6.9](https://arxiv.org/pdf/2308.01814), printed page 21, explicitly supports initial-operator boundedness and the identification of transpose with adjoint. Here the proof additionally specifies the countable common construction needed for mesh comparisons. No norm comparison between an n-by-n matrix and a population operator is used.

## 5. Existence, uniqueness, and arbitrary vanishing-step comparison

The localization at population-proof lines 274–303 is correct. Each downward backward recursion multiplies an existing difference only by bounded operators and bounded activation derivatives; the new cutoff error is added. Thus the Lipschitz coefficient grows linearly with R, not as R to the depth. The Gaussian cutoff error beats the resulting Gronwall factor. The completeness and bounded-multiplier continuity argument at lines 305–330 then give a strong flow and uniqueness against any competing strong solution on the same initial state. Only the constructed reference needs subGaussian tails.

The proxy in lines 342–398 is an actual finite parameter state built from oracle nodes. Its forward and transpose actions differ from the prescribed oracle actions by fixed-mesh contraction errors. Downward localization against oracle P fields establishes consistency of recomputed proxy backpropagation even for an unbounded readout. The stated elementary tail-transfer inequality passes the reference cutoff estimate to these recomputed proxy fields.

Comparing assigned grid velocities is the correct way to account for the fine and coarse interpolants. Their preceding grid states are within their current distance plus C(eta_n+Delta); no derivative of the interpolation is silently replaced by the vector field at its current state. Equation (12) consequently has the required ordered-limit form. Sending n to infinity at fixed R and Delta, then Delta to zero, then R to infinity establishes the assertion for every eta_n tending to zero. No estimate for an increasing number of actual-GD tensor-program instructions is needed.

## 6. Observables and C1,1 smoothing

Forward observables are Lipschitz on the state ball; the same localized backward comparison controls the kernel contractions. The displayed kernel scaling agrees with the stated stored-parameter learning rates.

For the hidden-speed argument, the additional products contain bounded activation derivatives and L2 reference velocity fields. Uniform convergence of the population Euler states and their vector-field values makes those reference velocities a uniformly integrable L2 family. Fixed-mesh oracle cutoff convergence and a subsequent cutoff limit suffice after state stability; a new Gronwall tail estimate for speeds is unnecessary. The integrated-speed bound gives the claimed mean-square uniform-path grid reconstruction error, hence the path-law Wasserstein-2 passage.

The mollification estimates at lines 456–474 are valid globally despite unbounded activation values. All response bounds and the common time interval depend only on the value-at-zero and first-two-derivative bounds, which remain uniform under smoothing. The additional activation and derivative errors in the localized comparison vanish in the stated ordered limits. The argument therefore covers globally Lipschitz C1,1 activations and appropriately excludes ReLU.

The optional activity corollary remains restricted to two hidden layers, zero limiting readout, Gaussian first weights, and its stated nondegeneracy conditions. Its weighted-label replacement, leading orders, and positivity arguments are consistent with the strong-flow theorem and do not enter the arbitrary-depth existence proof.
