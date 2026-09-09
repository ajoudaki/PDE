# Isolated adversarial audit: Part III

**Verdict: CLEAN within the assigned mathematical scope.** No required mathematical correction was found. One optional notation correction is recorded below. This verdict concerns the supplied proof, including its internal probability, response, continuation, algorithm, observation, and initial-motion arguments; it does not certify the separate proofs of Parts I or II.

## Source identity, isolation, and read coverage

The only mathematical sources consulted were:

| Source | SHA-256 | Size |
|---|---|---|
| `/tmp/pde-special-reviewed-input.CM1FuJ/special_data_limits.md` | `94ad0b6a9ba39e937e1f90626c74c6b9d1f652fe20523dcdf1cdbf780bdfeda0` | 349,239 bytes; 6,397 lines |
| `/tmp/pde-special-reviewed-input.CM1FuJ/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` | 5,110 bytes; 98 lines |

Both hashes were checked before and after the mathematical reading and were identical. Neither input was edited. No repository content, history, previous review, web source, other agent, experiment, or numerical simulation was consulted. The mathematical-solution skill was read as procedural guidance only; it supplied no mathematical premise.

Read coverage was as follows. Ranges are inclusive.

| Source section | Lines | Coverage |
|---|---:|---|
| Opening and conventions | 1–126 | Complete |
| III opening and III.M | 3499–3776 | Complete, all statements and definitions |
| III.F.1–11 | 3777–4318 | Complete, all proofs and ancillary arguments |
| III.S.1–7 | 4319–4575 | Complete, including coefficient production and chronological induction |
| III.G.1–4 | 4576–4983 | Complete, including numerical gain checks |
| III.V.1–12 | 4984–5444 | Complete, including nested observation truncations and actual GD interpolation |
| III.N.0–5 | 5445–6011 | Complete, including all capped source recurrences |
| III.A.1–5 | 6012–6375 | Complete, including the open-ball construction and obstruction |
| Final scope | 6376–6397 | Complete through chapter EOF |
| NOTATION.md | 1–98 | Complete through EOF |

Thus 3,025 chapter lines and all 98 notation lines were read in full. One long display of III.V was truncated in transit; lines 5249–5298 were subsequently reread in full, covering the omitted passage. A heading-only locator was also read. No mathematical argument from chapter lines 127–3498 was used. All dependencies needed for Part III are within the fully read material above. Statements summarizing Parts I and II in the opening/final scope were read as scope statements, not independently validated against those unassigned proofs.

## Required and optional issues

**Required issues: none found.** In particular, the audit did not find a missing specialized theorem, an unsupported growing-transcript limit, an invalid population restart, or an unjustified passage from second moments to unbounded response derivatives.

**Optional O1 — undefined matrix alias, line 5692.** The base return calculation writes `A_2 T_j^1`, although the initialized action in this section is denoted `W^(2)`. Replace `A_2` by `W^(2)` (or explicitly declare the alias). The adjacent text, the query schedule at lines 5772 onward, and the ensuing calculation uniquely identify the intended action. This is a local notation defect, not a missing mathematical argument or a different initialization.

The qualifications about absolute nonaffinity, fixed depth, fixed positive amplitude, reached-state restart, and population versus finite-time approximation are essential parts of the result, not optional caveats. They are correctly present in the supplied text.

## What the proof actually establishes

Fix admissible three-sample data, a normalized bounded nonconstant shape with two bounded continuous derivatives, and separation parameter `delta`. The displayed gain depends on `delta` and the shape witness, and is selected before depth, width, physical horizon, and the particular admissible data configuration. Fix any one `e` in `(0,1]`. For every separately fixed finite `L >= 2`, the proof establishes:

1. A global strong autonomous population gradient flow on the canonical generated action spaces, unique among bounded-primal strong competitors, including continuation from every reached state.
2. The stated population Gram floor and exponential fitting estimates, with a bound on total control time independent of the physical observation horizon.
3. Full-sequence, in-probability compact-physical-time limits for actual finite GF and simultaneous raw GD with step `n^(-2)`, retaining their small random initialized readout.
4. The listed predictions, loss, every true raw kernel block, same-layer joint field/velocity laws, finite joint-time laws, hidden path laws in supremum-norm Wasserstein-2, second moments, integrated speeds, and fixed generated probes.
5. Persistent positive absolute affine-regression residuals; nonzero initial hidden-block and every-sample hidden-field accelerations; and the stated positive quadratic kernel variation.
6. A common gain for the stated shape classes, an infinite-dimensional open class with a positive absolute margin uniform in depth, and a compact-support obstruction for the broad class.

This is not a simultaneous depth/width theorem, uniform finite-width convergence over an infinite activation class, an infinite-time finite-optimizer theorem, a lower bound independent of `e`, or a claim that every hidden velocity stays nonzero at every positive time.

## Detailed check reasoning

### 1. Conventions, exact algorithms, and quantifiers

**Opening, NOTATION, III.M.1–2.** The storage conversion is linear: `w = W^(1) = sqrt(d) V^(1)`. Its metric identity is exact, so first-row mobility changes consistently under storage conversion. Differentiating `f_i = Wout^T h_i^L/n` gives `partial f_i / partial z_i^ell = delta_i^ell/n`. For half-sum loss, multiplying by the inverse metric gives exactly

\[
\dot V^{(1)}=-d^{-1}\sum_i r_i\delta_i^1x_i^T,
\quad \dot W^{(\ell)}=-n^{-1}\sum_i r_i\delta_i^\ell(h_i^{\ell-1})^T,
\quad \dot W^{(L+1)}=-\sum_i r_i h_i^L.
\]

There is no missing sample factor. More generally `L_c = cm L_mean`, hence the clock and step identities in C.5. For Part III, `cm = 3/2`, not one. Raw GD and recomputation along raw linear interpolation respect the linear storage conversion.

The hidden normalization also checks exactly:

\[
f_i=a^L F_i,\qquad
\delta_i^\ell=a^{L-\ell+1}d_i^\ell,
\qquad H_i^{\ell-1}=a^{\ell-1}X_i^{\ell-1}.
\]

Thus every predictor-gradient block has the same overall factor `a^L`, and every true kernel block has factor `a^(2L)`. In particular the first block has `G_ij`, not `d G_ij`, and the middle blocks acquire their factor by multiplying both the backward and forward scalings. Normalizing hidden fields has not normalized the stored readout, raw metric, or physical step.

The finite rank-one matrix is `uv^T/n`; its ordinary Frobenius norm is `(||u||/sqrt(n))(||v||/sqrt(n))`. This matches the population Hilbert–Schmidt rank-one norm. Pairings always contract within the appropriate layer; no cross-layer neuron pairing is needed.

Finite GF continuation uses the correct finite-dimensional hypotheses: the finite vector field is locally Lipschitz, its exact gradient energy identity controls integrated squared raw speed, and

\[
\|\theta(t)-\theta(s)\|_{\rm raw,n}
\le \sqrt{|t-s|\,\mathcal L_n(0)}
\]

gives a Cauchy endpoint at any finite putative maximal time. Local continuation then contradicts maximality. This does not assume population local Lipschitzness. Finite GD is everywhere defined algebraically; its useful finite-horizon bounds are established separately in III.V.

**III.M.3 and final scope.** The theorem consistently fixes the activation, data, finite depth, and physical horizon before width. `T_0 = 12/lambda` in gain selection is not the physical observation horizon. Constants in the finite algorithm bridge may grow with `L`, `a`, and the physical horizon; none is fed back into the depth-independent gain recipe. The restart domain is the reached canonical state space, not an arbitrary Hilbert-space initialization.

### 2. Gaussian foundations: III.F.1–11

**III.F.1: empirical-law topology.** The root law needs only finite second moment. Truncation proves the required scalar laws of large numbers. The finite-dimensional transport argument establishes weak convergence plus second-moment convergence implies Wasserstein-2 convergence, including its in-probability version. Same-index coupling controls later approximation errors without claiming trained rows are independent.

**III.F.2: operator bounds and trace corollary.** The `1/4`-net has at most `9^n` points, and the two-sided net error is at most half the operator norm. A fixed bilinear form is `N(0,1/n)`. Threshold five therefore yields exactly `2 * 9^(2n) * exp(-100n/8)` for operator norm exceeding ten. For thresholds at least ten, `2 log 9 <= t^2/16`, validating the stated tail simplification and uniform fixed moments. The independent Gaussian trace probe has variance `2 ||sym(T_n)||_F^2/n^2 <= 2 ||T_n||_op^2/n`; its independence and moment hypotheses are explicit. The trace corollary depends on F.1, but it is not used to prove F.1, so there is no circularity.

**III.F.3: adaptive conditioning.** Conditioning is performed successively on the transcript, under which the next input is fixed. A call adds a linear observation of exactly one residual Gaussian matrix, preserving the product conditional law of the remaining residual factors. This addresses adaptive reuse directly. The proposed conditional mean satisfies both constraints using `U^T Y = Q^T V`; the homogeneous subspace is `P_Uperp K P_Vperp`. Its orthogonality to the mean proves the Gaussian projection formula. The output correction and innovation have the correct factors of `n`. The discarded Gaussian projection costs rank divided by width in squared RMS; rank is bounded by the fixed transcript length. Coefficient convergence here is used only under positive definite limiting query Grams.

The conditional innovation supplies the required empirical bounded-test concentration and second moments. Its cross term has vanishing conditional variance because the old RMS norms are bounded in probability. This proves the induction rather than substituting an independence assertion for trained rows.

**III.F.4: source responses.** Input Grams are uncentered second moments, whereas the sources themselves are centered. Subtracting the old forward-query regression makes the remaining input orthogonal to every old forward input. Gaussian integration by parts then converts its pairing with an old reverse answer into the full reverse-input Gram times expected named derivatives. Substitution cancels the regression derivatives and gives precisely the source correction. The functions have linear growth and bounded source derivatives at a fixed instruction, so Gaussian boundary terms and integrability are justified, including conditioning on independent finite-second-moment roots.

Only the primitive source groups are independent. Outputs in opposite orientations retain their response dependence. Freezing coefficients and covariances in named derivatives is therefore necessary and is used consistently later.

**III.F.5: singular queries.** Each query receives its own fresh input noise. Conditional projection onto the complement of earlier inputs leaves asymptotic squared distance at least `epsilon^2`; the mixed noise term vanishes and the normalized projected-noise norm tends to one. Thus the perturbed query Grams are positive definite without assuming rank stability for the original program. The finite same-array error is `O(epsilon)` on the fixed operator/noise event.

The second half of the argument is needed and is supplied: response coefficients and derivatives, not just values, converge under finite covariance-square-root coupling. Their continuity follows inductively from bounded derivatives of the coordinate instructions and a compact neighborhood of the already converging coefficient list. Finite-second-moment roots dominate node values, and bounded source derivatives dominate coefficient expectations. No continuity of a pseudoinverse at changing rank is used. On singular supports, ambiguity in individual derivative coefficients lies in the covariance kernel and disappears after contraction with the associated input tuple.

**III.F.6: scalar feedback.** The oracle replacement is causal. Inner-product and scalar-times-vector errors are controlled by the displayed RMS inequalities. Local Lipschitzness suffices near the deterministic limiting arguments, with a stated fallback outside the domain if necessary. The physical algorithms require no divisions. Feedback coefficients can multiply unbounded nodes because their RMS norms are already controlled.

**III.F.7: common spaces and actual adjoints.** The countable program language yields compatible finite marginal laws because unused finite-width computations change no vector. Cylinder approximation, bounded smooth approximants, and truncation give density in the generated layer `L^2` spaces. The norm-ten inequality passes to every generated rational combination, so equal `L^2` inputs have equal answers and the maps extend boundedly to completion. Passing the finite transpose pairing to this dense set identifies the reverse extension as the genuine Hilbert-space adjoint. Extension to arbitrary fixed Lipschitz probes uses a common linear-growth envelope and second-moment tails, not an unsupported uniform approximation on all of Euclidean space.

**III.F.8: raw Hilbert space.** Parseval verifies the Hilbert–Schmidt norm, rank-one identities, and pairing formula. With normalized finite layer pairings the orthonormal basis is `sqrt(n)e_j`, which indeed gives the ordinary Frobenius norm. Only learned increments are Hilbert–Schmidt. The stated strong integrals are legitimate in these separable complete spaces; continuous rank-one factors give continuous Hilbert–Schmidt velocities and preserve adjunction.

**III.F.9: multiplication and curve differentiation.** Bounded continuous multipliers times a convergent `L^2` factor converge in `L^2`: truncation is applied to the fixed limiting factor, not to an uncontrolled sequence of products. The integral scalar difference quotient proves the curve chain rule. It does not assert that a nonlinear Nemytskii map is Fréchet differentiable from all of `L^2` to itself. The operator product rule uses norm-continuous bounded operators and strong derivatives, which are the available hypotheses.

**III.F.10: scalar Fréchet derivatives.** This stronger scalar conclusion has its own proof. For fixed incoming weight `v`, splitting its Taylor remainder at `|v| <= M` gives a term `O(M ||q||_2^2)` plus a tail multiple of `||q||_2`. Sending the increment to zero before `M` to infinity gives a uniform directional remainder, hence a Fréchet remainder. Forward increments are `O(||Delta theta||_raw)`; downward weighted expansion and genuine adjunction identify every gradient block. Multiplier continuity then gives continuity of the scalar gradient. The feature-energy derivative has the same weighted expansion. The true loss dissipation and kernel identities consequently hold along a strong uncut solution without assuming its existence in this lemma.

**III.F.11: capped existence and Euler.** At fixed cap the actual backward coordinate map has bounded first derivatives. On a primal ball the raw field is locally Lipschitz with width-independent bounds, using operator norm at most Hilbert–Schmidt increment norm and the rank-one difference inequality. Picard contraction applies on a ball/time interval where both invariance and contraction inequalities hold. The Euler defect `L_0 M_0 h^2/2` and its iterated discrepancy bound are correct. They are later used against a fixed auxiliary transcript, not as a Gaussian theorem for a transcript with `n^2` steps. The final paragraph correctly requires second-moment tails before removing an observational product cap.

### 3. Controlled source estimates: III.S.1–7

**III.S.1: local equations.** Unrolling the learned rank-one increments and applying the two source rules yields the displayed `Acal` and `Bcal` arrays, with strict past dependence for `Acal` and current returns included in `Bcal`. Bottom coefficients carry the input Gram, and the top readout is a past integrator. The induced block infinity norms and sums over blocks accommodate all three sample indices; no sign cancellation is used in their estimates.

**III.S.2: independent primal control.** Before the hidden-displacement stop, current operator norms are at most eleven, normalized features obey `||X_i^ell|| <= 32^ell`, and the readout is bounded by `3 F s`. Backward amplification is at most `22 <= 32` per layer. Each hidden block speed is bounded by `F ||Wout||`, hence joint displacement is at most `3 sqrt(L) F^2 s^2`. For Euler, `sum h_j s_j <= s_k^2/2` bounds even the first proposed exit node using earlier states. The selected gain makes this less than `1/4` and gives `Q_l < 1/2`. These facts precede, and do not rely on, the response estimates.

**III.S.3: same-array Gaussian part.** The eliminations of `X = Y + u` and `d = q + v` are exact at the actual frozen coefficient arrays. In particular

\[
Y-Y_G=Uv+UBu,\qquad q-q_G=BUv+(I-BA)^{-1}Bu.
\]

The Gaussian comparison uses the same sources and coefficients, not an affine-network law or a substituted covariance. Row bounds give a `2r ||q||_p` error that is absorbed with `r <= 1/8`. The offset contributes `b/K_l`; multiplication by the curvature scale `K_l` removes its apparent growth. The resulting marginal `sqrt(p)` bounds are valid for each finite prefix before absorption because fixed-cap finite programs are Lipschitz Gaussian expressions. No moment of a random maximum over all mesh times is required.

**III.S.4: derivatives and production.** Differentiating the local equations gives `J = I_xi + A[NJ + V(I_zeta + BGJ)]`. Strictness of `A` ensures every propagated derivative term comes from an earlier time even though `B` has a current diagonal. Discrete Gronwall gives the exponential envelope in the text; a single reverse-source insertion carries its own `h_j` factor. Minkowski controls the weighted sum of curvature variables in the exponent using marginal subGaussian moments. The exponential-square series and Young inequality supply integrable exponential envelopes without temporal independence. Cauchy–Schwarz then bounds the reverse expected derivative row and yields the conservative production constants 16 and 512. Expected absolute envelopes are available here; this is stronger than merely bounding absolute expected derivatives.

**III.S.5: gain arithmetic.** Direct substitution gives

\[
\alpha_l S b_l
\le 24576(67108864/a)^L64^{-l}T^2/a,
\quad n_l\le B_0\le b_l/2048.
\]

The condition `a >= 10^12(1+T)` makes the claimed smallness estimates valid for every finite `L >= 2`; the worst-case depth in these geometric bounds is two. The production radii have strict slack: `17 alpha_l < 32 alpha_l` and `514 b_l < 2048 b_l`. Their dependence does not require selecting gain after depth.

**III.S.6: chronological closure.** The induction starts with zero top readout and zero current reverse responses. In the forward sweep a new `Acal` row depends on backward fields only at strictly earlier times, so its estimate does not assume the unconstructed current `Bcal` row. In the reverse sweep the current forward row is already built, and the incoming current reverse row comes from the preceding higher layer. Thus the local estimates are used only on prefixes for which all hypotheses are established. This closes the potential current-row bootstrap loophole.

**III.S.7: output and limitations.** The uniform marginal moments imply Gaussian second-moment tails. Fixed-cap controlled Euler limits transfer them to population controls, with the measurable-control passage explicitly supplied in III.G.3. The actual finite random readout is removed only in a fixed-cap width comparison; it is retained in the actual algorithms. Observation derivatives and velocity/path limits are not treated as automatic consequences of S and are proved separately in V.

### 4. Global geometry and persistent nonaffinity: III.G.1–4

**III.G.1: three-input geometry.** For mixed-sign coefficients, writing the sum as two positive weights against one negative weight reduces the quadratic form to `(A-b)^2 + ((1-D)A-b)^2`, with `D in [delta,2]`. Its matrix has determinant `D^2` and trace at most four. The smaller eigenvalue is therefore at least `delta^2/4`; also `A^2+b^2` dominates the original coefficient norm squared. The one-sign case follows from the constant coordinate. This uses the three-sample structure and does not assume an invertible input Gram.

The initialized activation projection has orthogonal constant, Gaussian-linear, and residual parts. Gaussian regression is valid for singular tuples because each marginal variance is positive. Bounded shape and integration by parts improve the average derivative error to `1/sigma_l`, so the normalized Gram losses are summable with depth. The product bound `prod(1-d_l) >= 1-sum d_l`, with sum `1/(a-2)`, proves the uniform initialized floor `lambda I`. A mere per-layer lower derivative bound would not prove this depth-uniform conclusion; the supplied improvement is essential and valid.

**III.G.2: scales and movement.** The forward perturbation recurrence has ratio `20/32`, giving the stated normalized movement bound. Restoring raw preactivation scale yields

\[
d_L=3\sqrt L\,T_0^2\,32768^L/a^{L+1}.
\]

Entrywise Gram perturbations and a three-row norm bound give `6 F_*^2 D`. Both true normalized hidden differentials and capped hidden direction maps are bounded, so their product norm is controlled even though it need not be symmetric. The numerical gain bound makes both this product and the Gram perturbation smaller than `lambda/4`. The resulting current top Gram floor is `3 lambda/4`. There is no invocation of positivity for the capped hidden contribution.

**III.G.3: physical control clock and global capped paths.** The exact physical equation has residual matrix `-a^(2L)(Q_L + J_h U_h,R)`. Its possibly nonsymmetric hidden part is controlled in absolute operator norm, yielding

\[
\frac d{dt}\|r\|^2\le-\lambda a^{2L}\|r\|^2.
\]

With `r(0)=-y`, integrating `a^L ||r||_1` gives at most `6/(lambda a^L)=S/2`, excluding a first exit at control time `S`. Zero residual produces a stationary capped continuation; no division at zero is needed. Primal and speed bounds then give finite endpoint continuation in raw space. General measurable controls are approximated in `L^1` by bounded interval step controls, rather than sampled at arbitrary Euler nodes. Fixed-cap stability and Fatou pass the source moment estimates. This order avoids a circular appeal to an unconstructed uncut path.

**III.G.4: nonaffinity.** For a 1-Lipschitz shape, the optimal regression slope has absolute value at most one by the independent-copy covariance identity. Testing the two optimal affine fits on a common coupling gives the claimed square-root-residual Lipschitz constant two, even at zero variance. A bounded nonconstant continuous shape must fail to be affine on some finite interval, yielding a positive `J_psi`. Gaussian density on that interval bounds its residual below by `c_psi/sigma`. The variance upper bound gives initialized residual at least `c_psi/(4a^(L-1))`.

The displacement-to-square-root-margin ratio is bounded by the displayed geometric expression, and the second gain condition reduces it to at most `3/4`. Thus the movement cannot remove the initial regression residual. Absorbing the affine part and scaling the remainder gives exactly `e^2 c_psi/(16a^(L-1))`. This is an absolute residual, with no division by the affine gain or feature energy.

### 5. Population restart, exact GF/GD, and every observation: III.V.1–12

**III.V.1–2: dependencies, one-cap comparison, and restart.** Forward differences and residual differences are bounded first by raw state differences. At a backward gate the split is asymmetric: change the incoming value with a bounded gate derivative, then split the forward-coordinate perturbation at the reference cap. Every new factor `R` multiplies a forward discrepancy; it does not multiply an already accumulated backward error. Descending the finite number of layers therefore gives `C(1+R) alpha + C sum Tail_l`, not an unsupported `R^L` Lipschitz estimate.

All tails belong to the capped reference. Its `sqrt(p)` moments imply `C exp(-cR^2)` second-moment tails, which dominate the `exp(C_T R)` comparison amplification for each physical horizon. The resulting state and raw-derivative Cauchy bounds construct a strong `C^1` uncut path and identify its uncut vector field. An arbitrary bounded-primal strong competitor needs no moment or tail hypothesis of its own. At a reached time, the inherited discrepancy from the original capped reference has the same Gaussian decay; one more finite-horizon exponential factor still tends to zero. This proves the claimed autonomous uniqueness and restart without reinitializing matrices or Gaussian sources and without claiming arbitrary-state well-posedness.

**III.V.3: finite primal events precede probes.** Fixed-cap Euler convergence follows from deterministic raw stability. At a fixed mesh, all primary contractions have finite-program limits. Rank-one unrolling bounds the current finite operator norms by their initial norms plus a finite sum of converging products. An enlarged primal ball with slack therefore contains the finite coarse arrays with probability tending to one. The actual readout has RMS `O_P(n^(-1))`; stopped fixed-cap stability propagates this vanishing discrepancy from the zero-readout auxiliary program. This supplies the finite primal event before the probe argument uses it.

**III.V.4: expected response rows from probes.** A fresh independent Gaussian root inserted at selected answer slots is admissible in a fixed finite program. Its effect on subsequent raw updates is weighted by the corresponding physical step; single past insertions therefore cost `h_j`, while current answers retain a direct term. The stability comparison recomputes residuals and updates, rather than freezing them in the finite dynamics. In the scalar law, integration by parts in the added root holds with deterministic limiting coefficients frozen; its explicit occurrences are exactly the selected answer insertions. Finite covariance-square-root continuity then permits the perturbation to vanish. Choosing signs bounds sums of absolute expected derivatives, not expectations of absolute derivative sums. The text makes this distinction and supplies the latter kind of control separately in V.5. The current reverse-row recursion includes its curvature term and higher current return, with zero current readout-integrator term as base.

**III.V.5: pointwise derivatives and primary moments.** Substitution of the established response-density bounds into the differentiated local equations gives the displayed Volterra recurrence for full derivative rows. Same-time reverse terms involve already constructed forward values; there is no same-time algebraic loop. The nested past sum is bounded by `T sum h_j U_j`, closing discrete Gronwall uniformly over sufficiently fine meshes. Repeating the recurrence for `L^p` norms with Gaussian forcing gives marginal `C_(R,T) sqrt(p)` bounds. This uses neither an `L^p` operator bound for initialized matrices nor temporal independence.

**III.V.6: derivative-valid velocity queries.** Preactivation velocities contain an action on the preceding feature velocity, and the feature velocity uses the true gate `g_l`, even under capped updates. Appending actions in ascending layer order ensures their preceding opposite-orientation inputs are exactly the primary update-backward fields. The response formula retains the current reverse input and the strictly past learned increment.

The induction differentiates only the primary reverse-source coordinates needed for the next action. A new forward primitive source has zero formal derivative in these separate slots; its covariance need not be nonsingular. Hence the preactivation-velocity derivative row is bounded, while the feature-velocity row has integrable envelope `C(1+|P_l|)`. The new source variance is the already known incoming velocity second moment. This gives the next layer's response row and marginal moments without assuming a future estimate.

The unbounded products are not directly fed to F.1. The text first uses `g(Y) tau_M(P)`, proves its exact derivative formula, removes earlier inner caps at fixed new outer cap, and then removes that outer cap using the established envelope. The convergence of source derivatives is justified from explicit coefficient/source expressions, not inferred from Wasserstein convergence. Empirical cap removal uses the incoming second-moment tails and bounded actions. These steps close both the derivative and empirical-law obligations.

**III.V.7: velocity continuity and mesh passage.** Expanding `P_l = v_W X + W U` gives the stated upward error recursion. Splitting the multiplier difference against the reference velocity at threshold `M` gives `C M` times the forward discrepancy and a positive-part tail. Again each threshold factor multiplies an independent forward-state error, so the finite recurrence contains one `M`. Fourth moments of the coarse population reference give tail `O(1/M)`; taking `M = |pi|^(-1/2)` yields the asserted fixed-cap velocity error. Strong curve differentiation supplies the actual population velocities, and Fatou transfers their marginal moments. The resulting time modulus concerns `L^2` velocities, not a random coordinate-path maximum.

**III.V.8: actual finite capped GF and GD.** The finite coarse transcript is fixed before width. Deterministic defects compare its raw interpolation to finite GF or fine raw Euler; slack excludes exit. In GD the direction remains the field at the preceding fine node, while hidden quantities and their derivatives are evaluated at interpolated parameters. Its direction error against a coarse-node reference still vanishes by within-step displacement and fixed-cap raw Lipschitzness.

At fixed mesh and tail threshold, only finitely many velocity laws/tails are passed through the Gaussian theorem. Taking width first and then refining the mesh yields uniform-time same-layer joint Wasserstein-2 laws via the three-term inequality V.32. No empirical fourth-moment bound is asserted or needed. The positive-part tail functional is 1-Lipschitz in Wasserstein-2, giving the required uniform-in-time empirical second-moment tail conclusions.

**III.V.9: true backward observations and kernels.** Capped update fields are not silently identified with true predictor derivatives. The latter are appended in a separate descending chain. At each product, known inner caps are removed while the next outer cap is fixed; then that outer cap is removed using the newly established incoming second-moment tail. Initialized adjoints and learned rank-one increments pass these `L^2` errors using bounded action norms. The induction supplies actual action laws, without claiming an unneeded unbounded source-derivative formula.

For time passage, the true backward map is strongly continuous by the bounded multiplier lemma and bounded action continuity. Its image along a compact time interval is compact in `L^2`; a finite covering proves uniform tail removal on that compact image. The downward comparison thus permits width, mesh, and threshold limits in the stated order. Pairwise contraction continuity yields every off-diagonal and diagonal kernel entry, with the correct factor `a^(2L)` in each block.

**III.V.10: actual uncut finite algorithms.** Same-width capped references retain the same nonzero initial readout. Their empirical tails pass uniformly at fixed cap; `|q| 1_(|q|>R) <= 2(|q|-R/2)_+` converts these to the required reference tails. The asymmetric comparison yields width-limit state and direction error `C_T exp(C_T R-cR^2)`, and first-exit slack makes the bounds valid with probability tending to one. For GD, comparison is made at its preceding node, followed by the capped reference's within-step variation. The displayed integral recurrence therefore needs no width-independent local Lipschitz bound for the uncut field. This is a limit for exact raw GD, not transformed Euler or a control-clock optimizer.

**III.V.11: removing velocity caps in the correct order.** Uncut population velocities are continuous in `L^2`, hence have compact time images and uniformly removable second-moment tails. Comparing capped velocities against that uncut reference gives uniform strong velocity convergence without controlling the growth of fixed-cap fourth-moment constants. Finite reference tails pass at fixed training cap and threshold. The sequence is then width, training cap at fixed threshold, and finally threshold to infinity. This avoids multiplying an uncontrolled cap-dependent velocity moment by a cap error. The right-node and terminal-left direction conventions are retained.

**III.V.12: path laws, energies, and probes.** The path interpolation inequality

\[
\|x-I_hx\|_\infty^2\le4h\int_0^T|x'(s)|^2\,ds
\]

uses absolutely continuous coordinate paths, supplied by the strong integral/chain construction. Uniform RMS speed bounds and initial second moments imply finite second moments of the path supremum. Averaging the inequality gives Wasserstein interpolation costs, and finite-grid joint laws then prove the full hidden path law in supremum-norm Wasserstein-2. Fixed-time laws alone would not suffice; the needed path estimate is supplied.

Uniform-time velocity second moments give integrated hidden speeds and cross-products. Raw block speeds follow from residuals paired with the corresponding true kernel block; in GD these are evaluated at its preceding node. Fixed generated probes are handled by finite instruction induction, retaining both initialized action orientations and comparing current actions only at the same width or on common population spaces. Learned-increment contractions have finite rank unrollings and then controlled time approximation. No cross-width operator identification is claimed.

### 6. Initial activity and kernel change: III.N.0–5

**III.N.0–1: scope and forward positivity.** The initial argument needs only `a > e > 0`, finite depth, the bounded `C^2` shape, and a canonical strong flow for its dynamical interpretation. Constant/linear Gaussian projection proves `Q_1 >= (a-e)^2(G+11^T)` and propagates strict positivity to every forward feature Gram. The direct three-vector geometry also covers singular input Gram. Thus every upper initialized preactivation tuple has full three-dimensional Gaussian support; the bottom tuple need not.

**III.N.2: top and lower backward Grams.** If a linear combination of top `beta_i` vanished, full support would force the product of the label-feature sum and a derivative combination to vanish identically. The first factor has no open zero set because each label coefficient is nonzero and `phi' > 0`. Continuity therefore makes the derivative combination identically zero. Differentiating coordinatewise forces each coefficient to vanish since bounded nonconstant `psi` cannot have `psi''` identically zero. This proves the top backward Gram is positive definite.

The exact reverse formulas include both curvature and current return terms. Conditional on the forward tuple, the independent reverse source contributes covariance `diag(D) S_next diag(D)`, bounded below by `(a-e)^2 lambda_min(S_next) I`. This proves every lower backward Gram positive even at singular bottom input covariance. The bottom block and each sample's bottom motion inherit a positive variance because `||u_i||=1`, `G_jj=1`, and `p_j` is nonzero. Matrix-block positivity follows by pairing two positive Grams through `diag(p)`; no sign assumption on their off-diagonal entries is needed.

**III.N.3: upper sample motion.** Block motion alone would not exclude cancellation of the two terms in a sample preactivation derivative. The added-forward-query argument supplies the stronger fact. The exact source recursion keeps the return `c^(ell-1) E[D_j D_i]` in addition to the direct block term. Regressing the new primitive Gaussian source on the three old forward sources uses the uncentered input Gram and no intercept. At layer two its residual variance is bounded below by conditional variance over the independent bottom reverse source. At each higher layer, the preceding independent innovation survives multiplication by a derivative bounded below by `a-e`; conditioning on the local forward/reverse pair cannot erase it. The new innovation is independent of the terms with which it might otherwise cancel. This establishes positive motion for every individual sample at every hidden layer.

**III.N.4: unbounded products and actual query schedule.** The finite schedule is forward initialization, descending backward queries, and then ascending added-forward queries. This supplies exactly the opposite-orientation input lists used in the formulas. At the top, clipping the label-feature sum yields a derivative bounded by `C(1+|H|)`; at each lower backward gate the derivative is bounded by `C(1+|q|)`. The source representation already gives the needed moments before each next gate is removed.

For added forward queries, the proof uses one coherent capped backward chain in both the reverse calls and the block contributions. Its exact derivative contains the two clip derivatives in N.22. These are bounded by one, so the deterministic coefficient recursion gives a bound uniform in all observation caps. Backward caps are removed first in dependency order, then forward caps in ascending order. Source covariance coupling and bounded derivative envelopes pass the expected responses; bounded initialized actions and multiplier continuity identify the same limits as actual uncut answers. The empirical passage uses second-moment tails after each incoming law is known. Hence the positive innovations and return formulas used earlier are proved, not merely asserted for inadmissible unbounded coordinate instructions. Only two derivatives of the shape are required.

**III.N.5: strong accelerations and coefficient 18.** At zero readout, all hidden first derivatives vanish and `Wout'(0)=3H`. Strong multiplier and action continuity imply `delta_i^ell(t)/t -> 3 beta_i^ell`; substituting the physical update gives `theta_h'(t)/t -> 9 V`. Thus the hidden state has expansion `(9/2)t^2 V + o(t^2)`. The curve chain/product rules give the corresponding `9 U_j^ell` and `9 T_j^ell` right second derivatives, without requiring an ambient twice Fréchet differentiable hidden-field map.

Adjunction telescopes the hidden feature-energy pairing to `||V||_hidden^2`, including the first-block factor `d`. The readout kernel contribution therefore changes by `9 t^2 ||V||^2 + o(t^2)`. The hidden predictor-gradient norm contributes another `9 t^2 ||V||^2 + o(t^2)`. Their sum is exactly the stated coefficient 18 for half-sum loss and `p=y/3`. Every hidden block contributes positively. This proves initial activity and a changing kernel, not every-positive-time velocity positivity.

### 7. Uniform classes and the obstruction: III.A.1–5

**III.A.1: regression stability.** Completion of squares handles positive variance; the constant-variable case is explicitly separated. The independent-copy identity bounds optimal slopes by one. Changing the input gives the square-root-residual bound with constant two; changing the function gives a bound by its uniform difference. The exact identity `R_phi = e^2 R_psi` absorbs the affine part into free regression coefficients. No variance lower bound is hidden in these steps.

**III.A.2: common finite-interval margin.** Orthogonality of `1` and `x` on `[-r,r]` gives the exact coefficient `3/(2r^3)` in the regression formula. Continuity and overlapping intervals ensure a positive witness for every bounded nonconstant shape. The Gaussian density estimate gives `c_psi/sigma`. The initialized variance bounds and the gain arithmetic compare raw movement against this margin simultaneously at every finite depth. The improved layerwise lower bound `e^2 c_psi/(16a^(ell-1))` follows. A class with a common interval witness, or merely a common positive lower bound on its witness constants, has a common gain. The open-neighborhood argument uses the interval `L^2` norm of the perturbation and strict norm slack, not compactness of an infinite-dimensional class.

**III.A.3: failure for the broad class.** A nonzero compactly supported `C^2` bump is admissible after normalization. Testing the zero affine fit bounds its Gaussian residual by `||psi||_(L^2(dx))^2/(sigma sqrt(2 pi))`. At fixed gain and amplitude, initialized scales tend to infinity with layer index because `a-e > 1` under the stated gain regime. Hence this single admissible shape has absolute initialized residual tending to zero with depth. A positive bound uniform in depth and all times is already impossible at time zero. This is stronger than the simpler observation that the broad class allows shapes arbitrarily close to constants.

**III.A.4: positive depth-uniform class.** Under a common positive Gaussian-scale residual floor, the movement estimate directly preserves a common absolute margin at every depth. Existence of such a class is actually proved. For a bounded continuous shape with distinct limits at the two infinities, the regression residual is positive at each finite scale, continuous in scale, and tends to `b^2(1-2/pi)>0` at infinite scale. Dominated convergence applies with bounded integrands and an integrable `|G|` weight. A positive minimum on a compact remaining scale interval completes the argument.

For the center `arctan(x)/4`, the stated function and derivative norms check, including `||psi_0''||_infty = 3 sqrt(3)/32`. Uniform regression stability transfers its Gaussian-scale margin to the entire displayed open `C_b^2` ball. The radius leaves strict room below the unit norm bound. Disjoint translates of the explicitly given `C^2` bump supply arbitrarily many independent perturbation directions. Membership in the ball need not preserve the center's tail limits or oddness; the transfer uses uniform closeness, so oscillatory perturbations cause no gap.

**III.A.5 and final scope: honest uniformity.** The common constants apply to each fixed class member and each fixed finite depth. They do not give a supremum-over-class finite-width theorem. The lower bounds scale with `e^2`; fixing positive `e` is indispensable. The compact-support obstruction concerns a proposed depth-uniform absolute margin and does not claim sharpness of the numerical lower bound proved in the broad theorem.

## Adversarial conclusions and limits of this verdict

The main potential failure routes were checked against their proofs:

- Singular adaptive queries are regularized before inverse-Gram limits, and derivative continuity is proved separately.
- Gaussian source independence is never substituted for independence of opposite-orientation matrix answers.
- Population existence and restart use capped reference tails, not a nonexistent general `L^2` local Lipschitz theorem for the uncut gates.
- The control clock bounds total population travel, while actual finite GF/GD remain in physical time with their original initialization and metric.
- Fixed finite Gaussian programs are combined with deterministic mesh comparison; no theorem is applied to a growing GD transcript.
- Unbounded response derivatives receive explicit domination; value products receive ordered tail removal; empirical Wasserstein convergence is not used as a substitute for derivative convergence.
- Uniform path laws have their own interpolation-energy argument, and velocity cap removal avoids uncontrolled cap-dependent moment constants.
- Every upper sample's initial motion has an independent-innovation proof, so nonzero parameter blocks alone are not used to rule out samplewise cancellation.
- Nonaffinity is absolute. Indeed the affine competitor `a(1+z)` always gives `R_phi(Z) <= e^2`; a positive absolute lower bound therefore says nothing comparable about its fraction of a large feature energy. The supplied all-time hidden-displacement bound can also be very small as gain or depth grows. The theorem makes no contrary quantitative relative-motion claim.

All specialized dependencies needed for these conclusions are proved within the assigned Part III. The remaining tools are elementary Gaussian integration and conditioning, finite-dimensional spectral/regression algebra, truncation and transport coupling, dominated/Fatou convergence, Hilbert-space completion and integration, and explicitly checked contraction/Gronwall arguments. No unprovided specialized result was accepted as a premise.

**Final assessment: CLEAN for the assigned Part III proof and its conventions/scope, with no required issues and the single optional alias correction O1.**
