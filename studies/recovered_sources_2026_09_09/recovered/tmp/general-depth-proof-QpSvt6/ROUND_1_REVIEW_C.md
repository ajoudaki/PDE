# Independent adversarial mathematical review — Round 1, reviewer C

**Verdict: PASS.** I found no consequential gap, false implication, missing hypothesis, quantifier weakening, circular argument, normalization error, or unresolved consequential notation issue in the stated theorem and its proof. This verdict concerns the precise model, metric, initialization, step size, observation class, and fixed-depth quantifiers in this document.

Reviewed document: `/tmp/general-depth-proof-QpSvt6/GENERAL_DEPTH_SELF_CONTAINED_PROOF.md`.

Exact reviewed SHA256:

`741331782e571a38ed11896fc342f2ce6291d63b057d456419d799757fe4327f`

The hash was checked directly and matches the supplied hash. Locations below are inclusive line numbers in that document, supplemented by equation or section numbers.

## Reading and isolation attestation

I read the entire document, lines 1–1727, including every theorem assertion, displayed calculation, proof paragraph, and final qualification. I reread the Gaussian conditioning/source-rule passage to ensure that output truncation did not omit any part of the reading.

My only mathematical input was the reviewed document. I did not read another project file, historical proof, audit report, coordinator message, or agent output; search the project; consult external mathematical sources; spawn agents; or run experiments. I read `/home/amir/.codex/skills/solve-math-rigorously/SKILL.md` as procedural instructions for checking mathematical arguments. It supplied no mathematical assumptions or results to this review. The proof was not modified. This review is my only write target.

The checks below include independent verification of the non-classical arguments from the proofs supplied here. I did not assume a previous PASS or treat an asserted intermediate lemma as established without checking its argument.

## Findings by section

### 1. Exact model, theorem, and quantifiers — lines 16–143

The statement fixes \(L\ge3\) before taking the width limit, fixes the activation and the physical GD step \(\eta_n=n^{-2}\), and specifies the raw updates and interpolation. Subsequent estimates may depend on \(L\) and on the finite physical horizon. This is consistent with the theorem; no uniform limit as depth or physical time tends to infinity is substituted for a fixed-depth, finite-horizon assertion.

The normalized vector norms and ordinary matrix Frobenius metric explain the different factors in the vector and matrix updates. They are also consistent with the finite kernel blocks. In particular, the ordinary coordinate derivative of \(f_n\) in the first vector is \(\delta^{(1)}/n\); the vector metric multiplies it by \(n\). For an interior matrix the derivative is \(\delta^{(\ell)}(h^{(\ell-1)})^T/n\), with no further metric factor. Thus (1.3), (1.6), and the metric later specified in Sections 9–10 agree. Reading “raw GD” as the explicitly defined dynamics, rather than imposing an additional Euclidean metric contrary to the text, leaves no normalization discrepancy.

The population theorem concerns bounded actions and same-population empirical/action laws. It does not assert convergence in operator norm between different widths, nor a coordinate coupling between different layers. Its stronger same-width GD/GF distance is separately proved.

### 2. Elementary bounds and convergence tools — lines 145–236

The activation bounds, derivatives, inverse-coordinate transformation, and bound \(\chi'\le1/100\) are correct. Treating \((G,F(G))\) as an initial root tuple avoids applying a later Lipschitz-program theorem to the cubic map \(F\).

The net argument gives the claimed high-probability operator bound: the bilinear threshold is \(5\), its Gaussian tail exponent is \(-25n/2\), and multiplication by \(9^{2n}\) still tends to zero. The readout norm estimate has the claimed order.

The weak-convergence/second-moment criterion, quadratic-growth test passage, neuron-index coupling bound, bounded-gate product lemma, curve chain rule, and discrete/continuous Gronwall comparisons are sufficient for their uses. In particular, the product lemma requires strong convergence of the unbounded factor, which subsequent applications obtain. The text does not incorrectly assert Fréchet differentiability of a general nonlinear map from \(L^2\) to \(L^2\).

### 3. Adaptive Gaussian reuse and singular Grams — lines 238–455

I checked both the conditional matrix formula and its use with adaptive queries. The mean in (3.3) satisfies both old constraints because \(U^TY=Q^TV\). The residual is the Gaussian component on the orthogonal complement of those constraints. Conditioning successively on predictable queries retains this description: after the transcript is fixed, the new constraint concerns only the queried matrix. This also justifies the conditional independence of the unexplored residuals of distinct matrices.

In (3.4), the coefficient of \(U\) has the correct normalization. Removing the fixed-rank Gaussian projection costs vanishing normalized squared norm. Conditional averaging of a bounded test has variance \(O(1/n)\); the separately displayed cross-term and Gaussian-square calculations provide second-moment convergence. Thus this is a proof of joint empirical \(\mathcal W_2\) convergence, not an unsupported independence claim about reused coordinates.

The source/response derivation in Section 3.3 checks out. Orthogonality of \(h_\perp\) to all old forward inputs removes the non-source part of each old reverse answer from its contraction with \(h_\perp\). Gaussian integration by parts then gives

\[
\beta=\mathbb E\nabla_\zeta h-\sum_r\alpha_r\mathbb E\nabla_\zeta v_r.
\]

Substitution cancels the old response terms and leaves (3.5). The new source covariance is the full uncentered input second moment. Subtracting the squared response from that covariance would be incorrect; the document does not do so. Differentiation of the explicit expression, with selected scalar coefficients fixed, is the appropriate convention for the frozen finite program.

Section 3.4 removes an otherwise consequential rank-stability assumption. Fresh input jitter gives positive limiting Gram Schur complements. The finite calculation is uniformly close to its unperturbed counterpart by the initial operator bound and finite Lipschitz induction. On the scalar side, continuity follows through the causal response formula: previous coefficients and formal derivatives are bounded by finite induction, covariance square roots vary continuously even at rank loss, and the bounded continuous derivatives permit passage to the next response coefficient. Thus no inverse-Gram limit is silently taken at a singular covariance. Distinct formal slots at singularity are consistently retained; the null-space observation addresses the contracted answer.

### 4. Clipped Euler program and identification — lines 457–588

The clipping scheme matches the transformed vector field: every interior reverse query is clipped, the bottom transformed query is not, and the top readout is handled using its pointwise bound. The learned forward and reverse terms in (4.2) have the correct factors \(\Delta/n\).

For a fixed program, the bounded readout and clipped deltas permit globally Lipschitz \(C^1\) extensions of its coordinate instructions. Oracle contractions can be selected causally and then replaced by empirical contractions using the displayed inner-product difference estimate. This argument is explicitly restricted to fixed programs; it is not later misused for the width-dependent number of GD iterations.

The resulting scalar recursions (4.3)–(4.5) retain both learned memories and Gaussian reuse responses. Their time ordering is consistent: forward memories are strictly past, while reverse memories include the present forward query. In particular, the second term in the interior identity (4.6) is the current return from the next layer. It is included in the later response estimates.

### 5. Fixed spaces, actual adjoints, primal bounds, and fixed-cap flows — lines 590–755

The countable-program construction supplies consistent laws because finite unions arise as limits of the same finite-width calculations. The coordinate family is dense in each generated \(L^2\) space. Passing the finite norm bound and transpose pairing to limiting second moments establishes bounded, well-defined linear actions on that dense family. Their extensions are actual adjoints by (5.1). This supplies fixed spaces and operators without resampling transposes or adding operators as time advances.

The descending primal bounds (5.4) are valid for both positive-step Euler prefixes and feature flows. They use the bounded readout velocity first, then bounded gates, the next matrix norm, and the rank-one norm identity. Their independence from clipping is justified by \(|\tau_R(q)|\le|q|\). No pointwise bound on a competing readout is needed for these bounds.

The stability argument has the claimed dependence on the cap. Forward discrepancies are controlled independently of \(R\). The top backward comparison uses the bounded reference readout. At an interior layer the already accumulated backward discrepancy is multiplied by a bounded operator norm and \(1/10\); the factor \(R\) multiplies only a forward discrepancy. Summing the finitely many resulting contributions therefore gives \(C(1+R)d\), rather than an iterated power of \(R\).

The fixed-cap contraction construction is legitimate on the closed bounded-readout path set. The integral equations preserve the readout bounds, and the primal bounds permit continuation over every fixed feature interval. Integrating the Lipschitz velocity gives the stated local Euler defect and global fixed-cap mesh error. The fixed-mesh width limit followed by mesh refinement and finite time nets establishes the fixed-cap convergence assertions.

### 6. Depth-independent response estimate — lines 757–939

I checked the causal dependencies and numerical inequalities in this section. The induction assumes backward row and delta bounds only at strictly earlier times. Its forward pass then constructs current \(a\)-coefficients from bottom to top before the current backward pass starts.

At the bottom, \(\chi'\le1/100\) yields (6.2). At an interior layer, differentiating the complete scalar expression yields the row inequality (6.3). A single reverse-source derivative contributes only one direct forcing of size at most \(A\Delta/10\); its propagation gives (6.4). There is no current reverse-source dependence in the current forward preactivation.

For the envelope, the past row bound gives \(|q_u|\le|\zeta_u|+a\), and the upper delta bound controls the source variance. Jensen over the time slots needs no independence across time. The exponent in (6.5) is correctly

\[
219p/400+3969p^2/1280000.
\]

It gives the stated \(L^1\) and \(L^2\) envelope bounds. Consequently the forward coefficient bound closes with \(49/36+3/50<3/2\).

At the top, the derivative row is controlled by \((73/300)S\) times the forward-row envelope. The bound \(e^{657/800}<5/2\), together with the learned covariance row, gives \(3067/3200<1\). Downward, the current upper bounds give \(\|q_k\|_2\le Q=161/120\) before the current lower row is estimated. Cauchy–Schwarz then gives the row bound

\[
3(Q/5+1/100)+(3/2)Q^2/100
=2482563/2880000<9/10.
\]

This order avoids a current-time circularity. The preceding backward error is never multiplied by a cap in this induction either. The same constants can indeed be repeated through each additional fixed layer. Finally, the bounded response shift and Gaussian source variance give (6.10) with the displayed constants, without assuming the shift is independent of its source or claiming a Gaussian supremum bound for an entire path.

### 7. Multiple-cap asymmetric stability, removal, and restart — lines 941–1030

The three-term identity (7.2) is exact with each state's own recursively computed queries. Its first term propagates the query discrepancy with a cap-independent Lipschitz factor. Its second term uses only the reference cap times a forward discrepancy. Its third term is supported on the reference query tail. Applying the query difference estimate downward therefore proves (7.3) with linear dependence on the reference cap, independent of the competitor cap, including an uncut competitor.

The single-time exponential moment passes from the identified programs to fixed-cap flows by strong \(L^2\) approximation and Fatou. It gives the uniform tail norm \(\varepsilon_R=8e^{-R^2/256}\). This defeats \(e^{CR}\), and also any additional factor \(1+R\), for every fixed comparison constant. Thus the cap paths are Cauchy in the complete state norm, and evaluation of (7.3) against their limit identifies the actual uncut vector field and all backward fields. This is a strong passage of the integral equations; it does not rely on a weak limit of an unbounded product.

The uniqueness comparison requires tails only from the constructed reference. A competing bounded-primal solution may have a different finite primal constant and no pointwise readout bound. Its new Gronwall constant is still defeated by the same Gaussian tail. For restart from a reached feature state, the initial discrepancy to the reference path has the same exponentially small form, which survives the additional comparison interval. This proves the stated reached-state uniqueness without assuming local Lipschitzness on an arbitrary uncut \(L^2\) neighborhood.

### 8. Finite uncut feature flow — lines 1032–1075

The empirical tail observable in (8.1) is controlled by \(\mathcal W_2\) convergence and fixed-cap time continuity. It does not require finite-width exponential moments. Comparison to the same-width, zero-readout clipped reference accommodates the actual random initial readout through its vanishing normalized \(L^2\) norm. The bounded reference, rather than the competitor, supplies the pointwise readout hypothesis.

The order “fixed cap, width limit, cap removal” is sufficient. The backward/query terms of (7.3) provide the additional field convergence, with their extra cap factors still absorbed by the tail. No unproved uniform-in-width concentration estimate for a growing Gaussian program is used.

### 9. Raw gradient structure, global physical existence, and raw uniqueness — lines 1077–1196

The trained increments are Hilbert–Schmidt because their rank-one velocities are continuous in HS norm and integrable. This does not incorrectly impose HS regularity on the initial actions.

The scalar Fréchet differentiability argument is valid. Inequality (9.2) controls the activation remainder paired with any fixed old \(L^2\) backward factor. Forward differences are \(O(\|d\theta\|)\), and expansion from the top down leaves only finitely many such remainders and quadratic cross terms. This proves the scalar derivative even though the full nonlinear coordinate map need not be Fréchet differentiable on \(L^2\). The HS rank-one pairing gives (9.3), and bounded-gate continuity proves gradient continuity.

The raw feature curve is gradient ascent of the predictor. Hence \(f_s=\sum K^{(\ell)}\ge25/36\), while that derivative is bounded on the constructed feature interval. Starting from \(f(0)=0\), there is one level-one point \(s_*\le36/25<3/2\). Boundedness of \(f_s\) gives logarithmic divergence of the physical clock at \(s_*\). Every finite physical horizon therefore lies inside the single feature interval already constructed. No continuation premise beyond that interval is needed.

Raw uniqueness is separately justified. For a raw competitor, the continuous backward fields make its matrix curve an HS integral curve, so the scalar gradient identity applies. Its positive deficit cannot vanish in finite time. Pointwise absolutely continuous representatives and the ordinary scalar chain rule give (9.7); its right-hand side is in \(L^2\), establishing transformed membership rather than assuming it. The positive clock then permits the feature uniqueness comparison. The same reasoning applies at every reached state and proves the claimed physical restart property.

### 10. Exact raw GD and finite physical comparison — lines 1198–1347

Finite GF has no finite-time escape: the residual bound first controls the readout, then integration of matrix bounds from the top down and the first-vector velocity controls all finite-dimensional parameters. The finite feature clock is also valid on the high-probability initialization event, and its convergence follows from uniform predictor convergence and scalar Lipschitz comparison.

The raw-GD argument does not identify GD with transformed Euler. The exact cubic expansion (10.1) includes both additional terms. From the normalized \(L^2\) bound on the bottom query and the deterministic Euclidean inequalities for \(q^2\) and \(q^3\), its accumulated defect is

\[
O(\eta_n\sqrt n+\eta_n^2n)=O(n^{-3/2}+n^{-3}).
\]

No fourth- or sixth-moment assumption is required. The raw matrix and readout updates give the necessary primal bounds on every positive stopped prefix, including the step into a proposed first bad node.

The comparison recurrence (10.3) includes the asymmetric cap error, reference Euler defect, and both raw-transform defects. The random partition causes no difficulty because (10.4) is a pathwise estimate using the fixed-cap reference's time modulus. The resulting stopped predictor estimate and scalar clock comparison include the endpoint of the first proposed exit. The strict margins \(36/25<147/100<3/2\) and the positive finite-horizon deficit contradict both stopping conditions. This does not assume in advance that GD remains below the target.

The fractional-step cubic identity controls the specified raw interpolation. Comparing GD and GF with the same finite reference at their respective converging clocks proves the stronger same-width distance (1.7). The sequential choices of cap, fixed reference mesh, and sufficiently large width establish convergence of the full width sequence in probability, rather than only a selected subsequence.

### 11. Observation class, exact interpolated velocities, and path laws — lines 1349–1458

The extension from Lipschitz instructions to bounded gates multiplying unbounded fields is justified by clipping the unbounded field first. Uniform \(\mathcal W_2\) convergence and compactness of the limiting \(L^2\) path control the discarded squared tails; subsequent bounded operator calls preserve that control. This covers the backward fields and the finite recursive velocity formulas without adding a moment hypothesis.

The preactivation velocity identity (11.1) has the correct rank-one contraction, including the full feature second moment. Physical velocities acquire the common factor \(2(1-f)\).

For actual raw GD interpolation, all raw block velocities are constant on a step, while hidden fields are recomputed. The normalized Euclidean velocity bounds imply a coordinate supremum change \(O(\eta_n\sqrt n)\) in each preactivation and gate. In (11.2), the contraction and matrix changes contribute \(O(\eta_n)\); the gate change contributes \(O(\eta_n\sqrt n)\). Induction through the finitely many layers controls the additional lower-layer velocity discrepancy. Thus the claimed error for every recomputed hidden velocity is \(O(n^{-3/2})\). The prescribed right-node and terminal-left conventions are compatible with this estimate and continuity of the limiting velocities.

The measurable-version and Fubini argument supplies actual absolutely continuous population coordinate paths. Inequality (11.3) controls interpolation error in squared supremum norm by mesh size times integrated squared velocity. Fixed-grid joint \(\mathcal W_2\) convergence, followed by grid refinement, therefore proves the stated \(\mathcal W_2(C([0,T]))\) convergence. The kinetic-energy bounds used in that argument are supplied by the preceding velocity result.

### 12. Strict nonlinear learning in every hidden layer — lines 1460–1727

**Initial reverse fields and onset.** The initial Gaussian forward laws use the full uncentered feature moments. In the initial transpose induction, conditioning on the lower initialization, the matrix's forward answer, and the independent upper matrices makes its reverse input measurable without revealing its remaining Gaussian residual. Thus (3.2) is applicable at each successive matrix. The coefficient \(\kappa_\ell\) is positive because the odd contribution vanishes and \(z\arctan z/(1+z^2)>0\) off zero. The innovation uses the full second moment in (12.4). This proves nonzero backward fields at every depth.

Adjunction in (12.5) gives a strictly positive pairing at each layer, so the forward motion terms cannot cancel completely. Strong \(L^2\) convergence of \(\delta^{(\ell)}(s)/s\), followed by the velocity recursion, gives all second-order hidden-motion expansions. The readout kernel receives the coefficient \(\Gamma\), and the hidden kernel blocks together receive another \(\Gamma\). With \(s(t)=2t+o(t)\), the total coefficient \(8\Gamma t^2\) in (12.7) is correct. Thus the kernel is nonconstant and every hidden layer exhibits strictly positive feature learning at small fixed positive times; this is not inferred solely from readout training.

**Strict non-affinity at all reached times.** The top correction is uniformly bounded. At an interior layer the correction is dominated by a random variable depending only on the reverse source group, which is independent of the forward source used for the lower-tail event. At the bottom the corresponding dominator is independent of the Gaussian root. The argument needs independence of those dominators, not independence of the actual corrections. Their expectations and Markov constants in (12.8)–(12.10) are consistent with the Section 6 bounds.

The direction of the closed-half-line passage is correct: the limiting mass of a closed set is at least the limsup of the approximating masses. Consequently both unbounded tails persist after mesh and cap removal. An attained zero affine-fit error would force a bounded strictly monotone activation to agree almost surely with an affine function on an unbounded support; boundedness forces slope zero, and strict monotonicity then forces a constant preactivation, a contradiction. Continuity of the moments gives a positive minimum of the error on each compact physical interval, including initialization. Uniform empirical second-moment convergence supplies the asserted finite-width consequence.

**No later freezing.** At every reached \(s>0\), the readout is at least \(ms\), so the top delta has positive squared norm. Approximating programs then have reverse-source variance bounded away from zero. Their uniformly bounded response shifts imply nontrivial tails in the next query. Passing those tails to the uncut limit and using the strictly positive gate gives a nonzero next delta. Repeating downward establishes each layer before using it for the next; there is no circular dependence among the nonzero-variance claims.

Finally, (12.12) follows from the velocity recursion and the actual adjoint relation. Its positive right-hand side rules out cancellation of each preactivation velocity. Strictly positive gates preserve nonzero feature velocity, and the physical multiplier stays positive at every finite physical time. Thus the proof establishes the all-positive-time nonfreezing assertion, in addition to the separate second-order onset calculation.

## Required repairs and optional exposition

No required repair was identified. I found no outstanding consequential notation issue. The finite normalized norms, population \(L^2\) norms, operator/HS norms, feature and physical time derivatives, singular-slot derivative convention, and interpolation velocity conventions are sufficiently specified for the arguments that use them.

The conclusions are proved for the stated one-input, one-target model and the explicitly specified raw metric and step size. No extra data, activation, depth-uniform observable bound, or simultaneous depth/width theorem is needed to justify the PASS.
