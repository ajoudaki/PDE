# Independent mathematical review

**Verdict: PASS.** I found no unresolved substantive mathematical objection to Theorem M.1 or to the additional claims in Part A. This verdict concerns the stated, separately fixed finite-depth and finite-horizon limits; it does not extend them to simultaneous depth/width limits or uniformity over an infinite activation class.

Manuscript: `/tmp/hidden_depth_review_20260908/manuscript.md`

Full SHA256: `e61789c67fc6ea5ee918c50b82c7d5a233c0991e7222d32a003ca722f837606a`

Scope read: all 2,864 lines, 178,199 bytes, including all definitions, proofs, intermediate estimates, qualifications, and Part A. I read the manuscript in consecutive, complete ranges 1–420, 421–780, 781–1160, 1161–1545, 1546–1910, 1911–2300, 2301–2670, and 2671–2864. I then rechecked relevant locations within that same manuscript. I read no project files, other manuscripts, preparation material, skills, or other reviewers' reports, and did not consult or delegate to another reviewer.

There are several evident reference-substitution/typesetting errors, detailed below. Their intended numerical quantities can be recovered and the affected estimates proved directly. I do not regard these as unresolved theorem obligations.

## 1. Dependency audit and external invocations

The operative dependency chain is:

1. Part F proves the finite Gaussian program theorem, the singular-query extension, the common action construction, scalar differentiability, and fixed-cap local existence/Euler stability.
2. Part S proves controlled, cap- and mesh-independent population source/moment estimates on the short normalized control interval. Its primal bounds precede its source induction.
3. Part G proves depth-uniform initialization geometry, uniformly small controlled displacement, global capped physical paths, and a uniformly bounded total control clock. This transfers S's estimates to the actual capped population paths.
4. Part V removes training caps, proves uncut uniqueness/restart, establishes actual finite GF/GD convergence by fixed auxiliary transcripts, and separately justifies velocity, true-backward, and path observations.
5. Part N establishes positive initial directions and their physical interpretation using a finite augmented initialization transcript and a separate derivative-valid clipping argument.
6. Part A proves its additional regression and activation-class assertions from the established displacement estimate.

I found no circular dependence in this chain. In particular, Part F's capped local existence does not use source moment estimates; S's stopped primal estimates do not use the coefficient box; G obtains global capped paths before the cap-removal step; and V obtains finite primal events before its Gaussian-probe response bounds.

**No specialized external theorem is used as an unproved premise.** Consequently there was no specialized primary text/proof to retrieve. The nontrivial Gaussian-program result is actually proved in F rather than merely invoked by name. Gaussian conditioning, Gaussian integration by parts, the finite net norm bound, finite-dimensional Wasserstein convergence, and the necessary clipping mechanisms are supplied internally. Remaining background facts are elementary real/functional analysis and probability: orthogonal projection in finite-dimensional Gaussian space, diagonalization/Parseval, Cauchy–Schwarz/Hölder/Minkowski, Fubini/Tonelli, dominated convergence/Fatou, elementary measure approximation/monotone classes, completeness of Hilbert spaces, and contraction/iterated-integral arguments. The manuscript either proves the relevant application or uses these at their ordinary foundational level. No random-matrix spectral-limit theorem, tensor-program theorem, propagation-of-chaos theorem, or abstract mean-field training theorem is needed.

## 2. Model, metric, and normalization

I checked all raw metric factors. With the finite readout convention `f = n^{-1} C^T h`, the inverse first-block metric multiplies its Euclidean derivative by `n/d`, the upper matrix metric leaves its Euclidean `1/n` factor, and the readout inverse metric multiplies by `n`. This gives precisely (M.10).

The substitution `w = sqrt(d) W^1` is an isometry for the first block: `(d/n)||Delta W^1||_F^2 = ||Delta w||_n^2`. It gives the first-layer projection `w dot u_i` with variance one and introduces no alternative training metric.

The feature normalization has the exact identity

`phi(a^(l-1)Y)/a^l = Y + [1+(e/a)psi(a^(l-1)Y)]/a^(l-1)`.

Consequently the physical backward variable has factor `a^(L-l+1)`, while multiplication by the incoming physical feature restores `a^L` in every hidden gradient block. The readout block also has factor `a^L`. Thus `grad_raw f_i = a^L grad_raw F_i` in every block, and every normalized representation of a raw kernel block in (V.34) has the common factor `a^(2L)`. I found no dropped depth-dependent time or metric factor.

The finite random readout is not silently replaced in either actual algorithm. The zero-readout auxiliary program is compared at fixed cap using its `O_P(n^{-1})` normalized norm discrepancy. The actual readout initialization remains shared by the finite algorithm and its same-width references.

The finite GF continuation argument is valid: the exact energy identity bounds raw path length on each finite time interval, yielding a Cauchy finite endpoint in a finite-dimensional complete parameter space. GD is a finite composition at every finite step. Its interpretation as recomputed hidden fields along raw parameter interpolation is preserved in V.

## 3. Foundational probability: adaptive reuse and singular laws

### Adaptive Gaussian conditioning, F.3

The conditional Gaussian argument is genuinely chronological. A query input is measurable from the already conditioned transcript; the new answer is then a linear observation of only the queried residual matrix. At that point it is legitimate to hold the input fixed. Conditioning the current product of residual laws on this answer updates only that factor. This avoids the false assertion that an adaptive input was independent of its matrix before the transcript was fixed.

For constraints `WV=Y`, `W^T U=Q`, I checked that the displayed mean satisfies both constraints by `U^T Y=Q^T V`, and that its two summands are orthogonal to the homogeneous space `P_(U-perp) K P_(V-perp)`. The residual covariance is therefore exactly the projected isotropic Gaussian covariance. The scaling of beta in (F.7) agrees with the normalized inner products.

The omitted fresh-noise projection has conditional squared normalized norm `rank(U)/n`. The rank is fixed by the transcript length. Boundedness in probability of the multiplying variance suffices to remove it; the proof does not require uniform independence of trained neuron coordinates. Conditional empirical-test variance and the explicit second-moment expansion then prove the asserted finite-dimensional W2 limit under positive limiting query Grams.

### Source-response rule, F.4

The response derivation retains all opposite-orientation observations and all derivative paths in the input expression. Orthogonality of `h_perp` to old forward inputs removes the old reverse response terms from `E[q_s h_perp]`. Gaussian integration by parts gives the remaining coefficient, and substitution cancels the derivatives of the forward regression projection. The primitive forward source has variance `E[h^2]` and cross-covariance `E[h v_r]`, i.e. the full uncentered input Gram.

Independence is asserted for primitive oriented Gaussian groups, not for the actual matrix answers or for answers and later adaptive inputs. The latter retain their return terms. Interleaving different matrices is covered by the conditional-product induction.

### Singular queries, F.5

The regularization is at each actual query input, with a distinct fresh Gaussian root for that call. Its limiting Schur complement is at least `epsilon^2`; prior query inputs and the old part of the current input do not use that fresh root. Thus the nonsingular theorem applies at every fixed positive epsilon.

The same-matrix coupling gives a deterministic `C epsilon` node error on the common high-probability operator/noise-norm event. This estimate uses the fixed instruction count and bounded coordinate Lipschitz constants, and is independent of the rank of the original limiting Gram.

The scalar zero-noise limit is justified through covariance square roots and bounded continuous formal derivatives. It does not take a limit of inverse Grams or pseudoinverses. Coefficient continuity closes causally: prior coefficients lie in a compact set, expressions have uniform linear-growth/derivative bounds, covariance entries converge by L2 convergence, and the next expected derivative converges by bounded convergence.

The invariant meaning of singular-support derivative contractions is also correct. If a difference of two formal expressions vanishes on the source support, Gaussian integration by parts puts the difference of their expected derivative vectors in the covariance kernel. A reverse input vector with that Gram annihilates this kernel almost surely. Individual formal coefficients need not be invariant; the response contraction is.

The causal scalar-feedback extension compares to a deterministic oracle instruction by instruction. Its error estimates are adequate even when coefficients multiply unbounded vector nodes, because only their normalized L2 norms enter.

## 4. Common bounded actions and strong differentiation

The countable generated-language construction gives compatible finite-dimensional laws. The finite norm inequality passes to deterministic limiting squared norms for every generated input. It makes each answer assignment well-defined on L2 equivalence classes, linear, and bounded by 10. Generated cylinder functions are dense, so completion defines a single bounded action on the entire generated Hilbert space.

The finite adjunction identity is passed first on the dense generated domain and then by continuity. Thus the reversed maps are genuine Hilbert adjoints of those same forward actions. Independent reverse resampling is not used. Arbitrary real coefficients and admissible coordinate maps can be represented by finite generated approximations with controlled L2 errors.

The Hilbert–Schmidt norm agrees with finite Frobenius norm under the normalized layer inner products: an orthonormal finite basis is `sqrt(n)e_j`. In particular `u tensor v` is the finite matrix `uv^T/n`. This validates both the population raw metric and the learned rank-one integrals. Only learned increments need be Hilbert–Schmidt; the initialized action itself does not.

F.5–F.7 handle a real infinite-dimensional issue correctly. The proof uses strong bounded-multiplier continuity and a curve chain rule; it does not claim that the nonlinear L2-to-L2 feature map is generally Fréchet differentiable. Scalar prediction differentiability is instead proved by the weighted Taylor remainder (F.41). At a fixed incoming L2 weight, its tail makes the linear-growth remainder `o(||q||_2)` uniformly over small increments. Downward weighted expansion then proves the scalar Fréchet derivative and continuity of its gradient. This is sufficient for the exact energy/kernel identities.

Fixed-cap vector fields are locally Lipschitz on bounded primal balls: the capped backward coordinate map has bounded first derivatives, and the remaining operations are bounded actions, scalar contractions, and continuous rank-one bilinear maps. This supports the stated contraction and Euler arguments without invoking differentiability of an uncut L2 product.

## 5. Part S: moment estimates and chronological coefficient closure

I checked the local source equations and the placement of current versus strict-past returns. Forward learned/response rows are strict in time; reverse rows include the current diagonal. The diagonal is retained in the derivative recurrence.

The independent primal bootstrap is valid. Before hidden displacement 1, adjacent action norms are at most 11, the first three projection norms are bounded, and forward/backward norm induction gives `F=32^L` and `||q_l||_2 <= 32^(L-l) 3FS`. Every hidden block speed is bounded by `F ||C||_2`. Integration gives the stated, deliberately loose, `3 sqrt(L) F^2 s^2` displacement bound. The same preceding-node estimate excludes an Euler overshoot.

The same-array Gaussian elimination is algebraically exact:

`Y-Y_G = U v + U B u`,

`q-q_G = B U v + Lloc B u`.

The small parameter is `r = alpha S b`. The absorption uses a moment which is already finite for a fixed capped finite transcript. The Gaussian part's variance is bounded using the independent actual L2 primal estimate; it is not borrowed from a comparison covariance. The bounded offset contributes `b/K_l`, which is essential when multiplied by the curvature scale `K_l`.

The pointwise Jacobian recurrence has strict time causality. Its exponential envelope depends on the weighted sum of marginal `K_l max_i |q_i|` values, not on a random time maximum. Minkowski plus marginal subGaussian moments controls that weighted sum without temporal independence.

I independently checked the numerical gain algebra:

`alpha_l S <= 3(32768/a)^L T`,

`alpha_l S b_l <= 24576 (67108864/a)^L 64^(-l) T^2/a`.

For `a >= 10^12(1+T)`, the latter is bounded by its L=2 case and is less than `2.57*10^(-19)`, using `sup T^2/(1+T)^3 = 4/27`. Since `W_l <= 61 b_l`, the exponential-envelope smallness has ample slack. The produced forward and reverse bounds lie strictly inside the respective next radii.

Most importantly, S.6 closes the actual coefficient arrays chronologically. Current forward production uses only completed past reverse rows because its local forward row is strict. Current reverse production starts from the known top readout integrator and descends after the current forward rows have been constructed. There is no use of an unknown current reverse row to prove that same row's bound.

This proves the cap- and mesh-independent marginal moment/tail input actually needed later. The passage from step controls to arbitrary bounded measurable deterministic controls uses L1 approximation and fixed-cap stability rather than unjustified point sampling.

## 6. Uniform depth geometry and global cap removal

The three-input augmented Gram proof works for singular input Grams and for the stated one-sided separation. The two-variable projected quadratic form has determinant `D^2`, trace at most 4, and hence minimum eigenvalue at least `delta^2/4`. Its coefficient norm dominates the original three-coefficient norm.

The initialized constant/linear Gaussian projection is valid even at singular covariance. The improvement `|E psi'(sigma G)| <= 1/sigma` uses bounded psi and Gaussian integration by parts. Together with the lower variance growth, it makes the successive normalized linear-projection losses summable. The product bound gives `Q_L(0) >= lambda I` uniformly in finite L.

I checked the powers in the controlled displacement and Gram perturbation estimates. In particular `F_*^4=2^(20L)` and the largest perturbation is bounded by `54*2^40*T_0^2/a^4`, which is strictly below `lambda/4` under the stated gain. The possibly nonsymmetric capped hidden prediction term is bounded in operator norm; it is not mistakenly treated as a positive kernel.

Thus the capped physical residual equation has coercive symmetric part at least `lambda/2` while its clock is inside the prescribed interval. Its residual bound integrates to total control time at most `6/(lambda a^L)=S/2`, excluding a first clock exit. Capped paths are global before cap removal is attempted.

V.2's cap comparison has exactly one multiplicative reference-cap factor. Each backward recurrence introduces `R` only against a forward state discrepancy already bounded by the raw state error. It does not multiply the preceding backward error by R. All tail terms belong to the capped reference. Therefore the reference subGaussian tail beats `exp(C_T R)` and gives uniform strong convergence of raw states and raw derivatives.

The same comparison proves uniqueness against an arbitrary bounded-primal strong uncut competitor without requiring its tails or its source representation. At a reached-time restart, the initial capped-reference error is already of order `exp(CR-cR^2)`; another linear-in-R exponential leaves it vanishing. This is sufficient for the stated continuation uniqueness.

The nonaffinity proof is quantitative and correctly scaled. The optimal regression slope has absolute value at most one, so the square-root residual is 2-Lipschitz under an L2 coupling without a variance lower bound. The fixed interval yields `c_psi/sigma`; the raw displacement ratio to one quarter of the initialized margin is at most `3/4` under the second gain condition. The affine part of phi is absorbed exactly into the fitted affine function. This gives (M.17).

## 7. Actual GF/GD and observation limits

The finite-program theorem is only applied to fixed auxiliary meshes, fixed appended probe lists, and fixed observation caps. Fine GF/GD is compared to these by width-independent fixed-cap estimates on a primal ball. No Gaussian-program theorem for a transcript whose length grows with width is assumed.

V.3 derives the finite primal event from finite primary contractions and rank-one unrolling before using source-row or velocity estimates. The readout discrepancy is handled on the same fixed-cap stability scale.

V.4's Gaussian-probe step supplies bounds on sums of absolute expected source derivatives. A fresh independent Gaussian vector is inserted additively at selected answer slots. Recomputed residual feedback is included in the perturbation stability estimate. A single past insertion changes later raw states by `O(h_j epsilon)`; bounded insertions at all times give `O(epsilon)`. Integration by parts differentiates only the explicit inserted Gaussian variable, with scalar population coefficients frozen. At a fixed transcript, continuity of coefficients, covariance square roots, and bounded formal derivatives validates the epsilon limit. Choosing signs after the expectations are determined yields the absolute row bound. This does not confuse `|E derivative|` with `E |derivative|`.

V.5 then obtains genuine pointwise derivative-row bounds from those coefficient bounds by a separate causal recurrence. This separation is necessary and is present.

The ascending velocity observation induction in V.6 has the needed derivative-valid truncation. At each new action, the prior velocity already has its law, moments, and its relevant primary-transpose-source derivative bound. The derivative of `g(Y) tau_M(P)` has the envelope `C(1+|P|)`. Inner observation caps are removed before the new outer cap. In the next layer's relevant reverse-source differentiation, the newly introduced primitive forward source has derivative zero as a distinct named coordinate, even at singular covariance. This gives the stated induction without requiring psi''' or inferring derivative convergence merely from W2 convergence.

The deterministic velocity comparison (V.29) has one tail threshold factor M for the same reason as the backward cap comparison: it multiplies only forward state error. It treats the actual direction as a separate input. Consequently it applies to the preceding-node GD direction evaluated through the chain rule at the interpolated state.

True backward observations are separately appended in descending order in V.9. Bounded multipliers, positive-part L2 tails, and bounded current adjoints remove their clips. The proof does not need an untruncated derivative formula for this observational closure. Uniformity in time is supplied by compact L2 images of the population reference path and the deterministic backward comparison. This suffices for every true raw kernel entry, including off-diagonal entries.

For the actual uncut finite algorithms, V.8/V.10 first take width at a fixed training cap and compare on the same initialization. Reference tails, rather than unproved finite high moments, bound the uncapped error. The no-exit argument uses fixed slack. The GD error includes its preceding-node evaluation and its `n^{-2}` within-step term. For each fixed depth and activation the latter tends to zero, irrespective of the possibly large fixed physical-time constants.

The order of velocity cap removal in V.11 is also appropriate: first obtain population capped-to-uncut strong velocity convergence using the compact uncut reference; next take width at fixed training cap and tail threshold; then remove the training cap at a fixed threshold; finally remove the threshold. This avoids needing any growth bound on cap-dependent velocity fourth-moment constants.

For path-space W2 convergence, (V.38) explicitly controls the squared supremum interpolation error by `4h` times integrated squared coordinate speed. The established RMS speed bound therefore supplies path tightness and second moments. Fixed-grid joint laws then suffice. These path conclusions are stronger than fixed-time convergence alone, and the needed extra argument is present.

Uniform-time velocity W2 convergence gives squared speeds and their time integrals. Fixed finite generated probe graphs preserve the controlled L2 approximation errors under bounded coordinate maps, scalar contractions, and either initialized/current action orientation. I found no observation claimed in M.1 that falls outside these arguments.

## 8. Initial motion and kernel coefficient

For L at least 2, the initial top forward Gaussian tuple has full three-dimensional support because the previous uncentered feature Gram is positive definite. If the top backward Gram had a null vector v, the continuous product `H(z) sum_i v_i phi'(z_i)` would vanish everywhere. The nonzero set of H is dense since every partial derivative `p_i phi'(z_i)` is nonzero. Hence the second factor vanishes everywhere, and differentiation in each coordinate forces `v_i phi''` to vanish. Since a bounded nonconstant psi cannot have identically zero second derivative, v is zero.

The initialized reverse source formula retains both curvature and next-layer return terms. Its primitive source is independent of the relevant forward tuple and has covariance equal to the full next-layer backward Gram. Conditional covariance then propagates strict positivity downward, including through singular first-layer projections. The raw bottom metric factor d and each internal Hilbert–Schmidt block norm are correctly included in the positivity bounds.

For individual upper samples, (N.14) retains the exact deterministic return coefficients. The variance of the fresh forward innovation is the distance of the actual query input to the span of the three prior forward inputs, using their uncentered Gram and no intercept. At the bottom this distance is positive by conditional reverse-source variance. At each upper step the independent innovation survives multiplication by a derivative bounded below by `a-e`. Thus it cannot cancel the remaining return expression. This proves nonzero preactivation and feature directions for every sample at every layer.

N.4 supplies a coherent finite capped program for all of these otherwise unbounded products. Backward caps are removed in descending dependency order; added forward caps are removed in ascending order. The explicit response derivative (N.22) is bounded independently of all caps. Source covariance convergence and bounded action continuity then identify the actual uncapped action answers. This closes the source-rule dependency of the positivity proof.

Finally, `C(t)/t -> 3H`, followed by bounded-multiplier/action continuity, gives physical backward fields divided by t converging to `3 beta`. The exact hidden updates therefore give acceleration `9V`. The same curve product and chain rules yield sample accelerations `9U` and `9T`; no ambient second derivative of an L2 feature map is assumed.

I independently checked the coefficient 18. The readout-gradient contribution changes by `9 t^2 ||V||_hidden^2`, using the adjoint telescoping identity `<H,T>=||V||_hidden^2`. The hidden-gradient contribution is another `9 t^2 ||V||_hidden^2`, because its gradient divided by t tends to `3V`. Their sum is precisely (M.18), with every hidden block strictly positive.

## 9. Part A

The regression stability and fixed-function distance estimates are valid as distances to the closed span of `1,X`. The finite-interval formula and density lower bound are correct. The stronger layer-specific bound in (A.12) follows from the same displacement arithmetic.

The compact-support counterexample correctly rules out a positive all-depth margin for the entire admissible class already at initialization: its squared Gaussian regression residual is at most an integrable compact-support mass divided by sigma, and sigma grows geometrically.

The positive depth-uniform subclass construction is also valid. A bounded function with different limits at the two ends has limiting Gaussian regression residual `b^2(1-2/pi)>0`. Strict positivity and continuity at each finite positive scale supply a positive infimum on scales at least one. The displayed arctan center has the stated derivative norms. Sup-norm regression stability gives a common margin on the entire open C_b^2 ball, even for members without tail limits. Disjointly supported C_b^2 translates establish infinitely many independent directions. These conclusions do not imply unclaimed width convergence uniform over the class.

## 10. Editorial corrections, with resolved mathematical content

These should be corrected in the manuscript, but none leaves a substantive estimate undetermined:

1. **Lines 945, 989, 998:** `sqrt(S.2)` should be `sqrt(2)`.
2. **Lines 977–999:** `exp(S.1)` should be `exp(1)`, Euler's number, not the activation amplitude e. For example, from `||Z||_p <= M sqrt(p)` one obtains

   `E exp(Z^2/(4 exp(1) M^2)) <= 2`

   by expanding in powers and using `k! >= (k/exp(1))^k`. Young's inequality then yields the manuscript's loose bound `E exp(u|Z|) <= 2 exp(2 exp(1) M^2 u^2)`. Applying it with `u=2 alpha` gives the displayed square-root second moment of the envelope with `sqrt(2) exp(4 alpha b S + 4 exp(1) alpha^2 S^2 W_l^2)`. The subsequent constants 512 and 514 have ample slack.
3. **Line 2262:** `o(N.1)` should be `o_P(1)` for the stated finite-array norm error (or `o(1)` with the convergence-in-probability convention made explicit).

I have treated these as identifiable reference-renumbering artifacts, not as new definitions. The direct calculations above verify the exact numerical content that the affected arguments require.

**Final assessment:** the manuscript supplies the necessary adaptive-Gaussian, singular-law, common-adjoint, global-existence, true-algorithm, observation, and motion arguments. I found no missing specialized external premise and no unresolved substantive gap in the complete claimed theorem after checking its dependencies and constants. The mathematical verdict is **PASS**.
