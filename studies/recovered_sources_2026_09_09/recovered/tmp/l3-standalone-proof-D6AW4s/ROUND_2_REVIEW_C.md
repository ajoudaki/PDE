# Independent adversarial mathematical review — Round 2, referee C

## Verdict: PASS

I find all obligations of the theorem in Section 1 discharged by the supplied document. I found no mathematical gap requiring repair, false theorem conclusion, unjustified limit interchange, or unproved specialized theorem dependency. The presentation defects listed below do not change this verdict.

This verdict applies to the precise stated scope: the specified activation and initialization, every fixed finite physical horizon, empirical/action-law convergence for each specified finite observation program, and uniqueness/restart on the constructed spaces from the initial or a reached state. It does not assert operator-norm convergence across widths, uniformity over all probe programs, arbitrary-initial-state population well-posedness, or an interchange with infinite training time.

## Source, integrity, and audit restrictions

- Sole mathematical source: `/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md`.
- Requested frozen SHA256: `293b34e5657f48991e8ff922c8e7648bf9400557e97cef1a314bb2af9203d5f1`.
- Observed SHA256, both before the audit and immediately before writing this report: `293b34e5657f48991e8ff922c8e7648bf9400557e97cef1a314bb2af9203d5f1`.
- The file has 1,743 lines and 79,677 bytes.
- I read the entire document, lines 1–1743, including all displayed formulas and the concluding claims. A range affected by output truncation was reread in full; no unread range was treated as verified.
- Complete list of files accessed for reading: (1) the proof file above; (2) `/etc/codex/skills/solve-math-rigorously/SKILL.md`, an operational instruction file, not a mathematical source or prior review. No other mathematical source was accessed.
- No project files, research files, previous reviews, audit-status file, other conversations, or other agents' reports were inspected. No agents were contacted. No browsing, simulations, numerical experiments, or external mathematical searches were performed. Numerical constants below were checked by direct arithmetic within the proof's arguments.
- The proof was not edited. The only file written is this report, using `apply_patch`.

All line references below refer to the frozen proof.

## 1. Independent reconstruction of the theorem's logical dependencies

The proof has a complete route from its finite random initialization to each conclusion:

1. The finite Gaussian conditional calculation establishes each fixed finite instruction program, with both orientations of each matrix and with adaptive reuse. Input perturbations remove singular-Gram restrictions; the formal derivative convention gives a continuous causal response representation.
2. Joint consistency of these finite laws and the finite matrix norm bound construct fixed separable neuron spaces with bounded initial actions and genuine adjoints. This is a construction of the operators used in the final equations.
3. On these spaces, each fixed-clip equation has a solution and a width-uniform Euler approximation estimate. The finite-program result is applied only after fixing its mesh and length.
4. The explicit response induction controls both backward response rows, uniformly in clipping and mesh, on feature time `[0,3/2]`. It gives an exponential-square moment bound for the actual middle backward query.
5. An asymmetric state comparison uses only the clipped reference's tail. Its Gaussian decay dominates the exponential dependence on clipping in the stability estimate. This constructs and uniquely identifies the uncut population feature flow, including restarts from reached feature states.
6. The same comparison proves the finite uncut feature-flow limit and restores the prescribed small finite initial readout.
7. The predictor is continuously Fréchet differentiable in the stated affine Hilbert parameter space. Along feature time it increases at least at rate `25/36`. The physical clock approaches its level-one feature time only at infinite physical time. Every finite physical interval therefore lies within the feature interval already constructed.
8. Exact raw GD is compared separately with the clipped reference, including its non-Euler first-coordinate defect and a stopped positive-clock argument. This gives full-sequence convergence and the same-width GD/GF state comparison.
9. Truncation of unbounded factors, explicit interpolation-velocity estimates, and a path interpolation inequality prove all the additional observation and path assertions.
10. Initial transpose laws give strictly positive second-order motion and kernel coefficients. Uniform tail lower bounds preserve nonaffinity. A separate positive-time backward-variance argument and adjoint energy identities exclude later freezing in every hidden layer.

I checked these implications rather than treating any of the mean-field, transpose-response, continuation, or non-laziness assertions as an imported research theorem.

## 2. Model, scaling, and elementary tools — lines 18–254

### Parameters and gradient normalization

The output normalization, the definitions of the residual-free deltas, the `1/n` matrix updates, and the vector updates are consistent. In particular, at finite width the parameter metric stated at lines 1210–1215 has vector norm squared `||v||²/n` and ordinary matrix Frobenius norm squared. In that metric the gradient of the predictor is

`(delta1, delta2 h1^T/n, delta3 h2^T/n, h3)`.

Its squared norm is exactly the sum of the four blocks in (1.6). Multiplication by `-2r` gives the stated physical GF, and an Euler step of size `eta_n` gives (1.3). Thus no extra `n` or residual factor is missing from the later gradient and kernel identities. The claim is about these expressly specified updates and metric.

The natural coordinate is also consistent: `F'(z)=10(1+z²)=1/phi'(z)`, `(F^{-1})'=phi'`, and `chi'(F(z))=(phi'(z))²`. The root pair `(G,F(G))` has finite moments of every order because `F` is a cubic polynomial; the proof does not process `F` as an unrestricted globally Lipschitz coordinate instruction.

### Bounds and limiting facts

The activation floor and ceiling follow from `pi<10/3`; the derivative bounds are valid globally. The initial matrix estimate uses two deterministic sphere nets, a bilinear Gaussian of variance `1/n`, and a union bound. The exponent `100/8` dominates `2 log 9`, so the exceptional probability tends to zero for both matrices. The initial readout has normalized squared norm expectation `n^{-2}`, giving the required `O_P(n^{-1})` normalized norm.

The finite-dimensional Wasserstein arguments provide the needed weak-convergence-plus-second-moment criterion and quadratic-growth tests. Subtracting a truncated second moment first controls the excess-square tail; replacing the cutoff by a smaller one controls the ordinary squared tail. This supplies the tail estimates later used for products with bounded gates.

The multiplication assertion (2.4) is valid with merely convergence in probability of its gate argument and strong `L²` convergence of its unbounded factor. It is not a claim that a nonlinear substitution operator on `L²` is generally Fréchet differentiable. Its curve-chain-rule consequence is sufficient for the preactivation and feature derivatives used later. The discrete and continuous comparisons in (2.5) have the stated nonnegative coefficients and bounded/integrable quantities whenever subsequently applied.

## 3. Gaussian reuse and singular queries — lines 256–457

### Conditional law and adaptation

For the nonzero-input case of (3.1)–(3.2), projecting a Gaussian matrix onto the observed input direction gives the displayed conditional law. The residual reverse answer has variance equal to the full normalized squared norm of the reverse input. There is no subtraction of the squared response mean from this innovation variance. The removed projection has normalized expected squared norm `1/n`.

For (3.3), the two deterministic terms satisfy both observation constraints. In particular, the compatibility identity `U^T Y=Q^T V` makes the transpose constraint work. The remaining matrix space is exactly the intersection of the two constraint nullspaces, with orthogonal projection `A -> P_{U-perp} A P_{V-perp}`. Gaussian orthogonality gives the independent residual.

Adaptive selection does not invalidate that projection: after conditioning on the existing transcript the next query vector is fixed, and the next answer adds a linear observation. Revealing a deterministic coordinate function adds no residual information. Repeating this argument also preserves independence of the two matrices' conditional residuals.

Equation (3.4) has the correct normalization. At fixed query count, a discarded residual projection has rank bounded independently of width. Its variance multiplier is bounded in probability by the input norms. The conditional averaging calculation establishes both bounded-Lipschitz tests and the new second moment. The cross term has the stated vanishing conditional variance, and Gaussian squares have variance `2 sigma_n^4/n`. Thus reused coordinates are never incorrectly declared iid.

### Source/response rule

The derivation of (3.5) uses exactly the orthogonality `E[v_r h_perp]=0`, so the old reverse response drops out of `E[q_s h_perp]`. Gaussian integration by parts then gives the coefficient multiplying the previous reverse inputs. Substitution of the old forward responses cancels the least-squares correction. The remaining source has covariance `E[h v_r]` with an old source and variance `E[h²]`.

The derivative convention is essential and is stated: preceding deterministic coefficients and covariance parameters are held fixed, but differentiation passes through the complete earlier coordinate expression, including uses of the other matrix. The coordinate maps have bounded first derivatives; for a fixed finite program this bounds the composed formal derivatives. The root integrability and the Gaussian moments justify the integration by parts. Singular Gaussian integration by parts is reduced to ordinary independent standard Gaussians.

### Removal of the Gram restriction

The fresh input perturbation contributes a strictly positive `epsilon²` to each limiting Gram Schur complement. Its independence from the preceding input span and the unperturbed current input justifies the vanishing cross contractions. On the initial operator-norm event, finite-program Lipschitz propagation bounds perturbation errors by `C epsilon`, with `C` independent of width and `epsilon<=1`.

The source recursion has a separate continuous limit as `epsilon` decreases. Its finite causal coefficient induction uses continuous coordinate derivatives, deterministic bounds for those derivatives, second-moment convergence of inputs, and continuity of finite-dimensional positive-semidefinite square roots. It does not take a limit of Gram inverses. The nullspace observation at lines 453–457 verifies that a formally redundant derivative direction cannot change the contracted response. Zero and repeated queries are consequently covered.

## 4. Actual Euler programs and fixed population spaces — lines 459–757

The clipping maps satisfy the required identity region, contraction bound, smoothness, and sign properties. Both forward and reverse terms in the unrolled rank-one update (4.2) have the correct normalization. Every contraction can be frozen causally when its inputs become available. At fixed mesh, bounded readout and clipped middle deltas permit the required globally Lipschitz coordinate extensions. Restoring empirical contractions is justified by the displayed Cauchy–Schwarz estimate and finite induction; this does not invoke a width-dependent-length Gaussian program theorem.

The source covariances in (4.4) are full second moments. The strictly past forward response and the present-inclusive reverse response in (4.5) match the call order. In particular, the second term in (4.6) is the actual return through the third matrix and has the correct factor `(phi')² tau_R'`. It is not omitted in the later estimates.

For the population spaces, finite-union consistency gives a countable consistent family of finite Borel laws. The countable measure extension principle applies. The generated sigma fields and the included coordinate-function closure provide dense spans in their `L²` spaces. Truncation, finite-dimensional measure regularity, and bounded continuous approximation justify the density argument; bounded clipping can keep these approximations controlled off compact sets.

Passing the finite operator estimate to each finite rational linear combination establishes (5.1). It also establishes linearity and independence of the representative chosen for an `L²` input. Extension by density gives bounded actions on the entire spaces. Passing finite transpose pairings and then using density proves (5.2), so the reverse action is the adjoint of the same initial operator. This construction does not presume an iid kernel representation or Hilbert–Schmidt initial operators.

The coarse primal bounds follow in the stated order: readout, matrix 3, matrix 2, first-coordinate velocity. They are independent of clip and width. From zero readout, positivity and boundedness of `phi` give the pointwise bound (5.6).

The stability estimate uses the bounded reference readout, not a bound on both readouts. The middle clipped gate then has Lipschitz constant of order `1+R`. These estimates hold in the state norm and in its normalized finite-width version. The constrained path set for Picard iteration is closed in that norm, its readout bound is preserved, and a sufficiently short interval gives a contraction. The coarse estimates permit continued construction on every fixed feature horizon for fixed clipping. The Lipschitz estimate and velocity bound also give a per-step Euler defect of order `Delta²` and (5.8).

The fixed-clip width limit has the permissible order: fix mesh and finite program, take width to infinity, then refine mesh using the common Euler estimate. Finite time nets give uniformity over each finite list of time arguments.

## 5. Quantitative response induction — lines 759–945

I checked the dependency order, all three differentiated recursions, and the numerical margins in this section.

- At time zero, the top delta is identically zero as an expression. The resulting zero reverse source and zero middle delta give `U_0=V_0=0`. This does not discard formal derivatives in a degenerate backward-source direction.
- The single bottom-source derivative has one forcing term of size `Delta`. With only preceding `U` rows bounded by one, it yields `|a2_js| <= Delta(a²+e^{S/100}/100) < (3/2)Delta`.
- In the middle forward derivative row, the direct source contributes a single one to the row sum. Differentiating the clipped gate contributes `|q2|/5`, and the complete reverse return contributes `V/100`. This gives the exponential envelope `E_j` in (6.3). A single middle reverse-source perturbation enters with size at most `(3/2)Delta/10`, giving (6.4).
- The middle reverse source variance is at most `(7/40)²`. Jensen's inequality over time slots requires no independence between those slots. Together with the Gaussian exponential bound, it gives the constants `219p/400` and `3969p²/1280000` in (6.5). The resulting bounds `||E_j||_1<4`, `||E_j||_2<3` imply `|a3_js|<(3/2)Delta`.
- The top derivative row has readout derivative contribution `Delta sum T_r/100` and gate derivative contribution `aS T_j/5`. Their combined coefficient is `(73/300)S`. The top forward recursion is strictly causal, giving `T_j<=e^{657/800}<5/2`.
- The current top backward row is consequently at most `73/80+147/3200=3067/3200<1`. This step uses no current `U_k` assumption.
- Then `||q2_k||_2 <= 7/40+7/6=161/120=:Q`. Cauchy–Schwarz applied to the current middle derivative row gives `U_k <= 3(Q/5+1/100)+S Q²/100 = 2482563/2880000 < 9/10`.

Thus the current rows are proved using only preceding rows and the expressly ordered current top computation. There is no circular bootstrap. Bounds for all meshes, caps, and indices with `M Delta<=3/2` follow by induction, including meshes with very few steps.

Equation (6.10) is a representation of the actual identified middle query. Its shift is bounded by `a` even if dependent on the source. The square inequality and the one-dimensional Gaussian integral give (6.11); the denominator `1-49/6400` is positive. Neither this argument nor the derivative-envelope estimate assumes a uniform Gaussian path maximum.

## 6. Uncut existence, uniqueness, and finite feature flows — lines 947–1076

For each fixed cap and time, the Euler query converges strongly in `L²`. A time-dependent choice of almost-sure subsequence followed by Fatou is sufficient to establish the deterministic bound (7.1) for every time. No simultaneous almost-sure assertion over an uncountable set is needed.

The decomposition (7.2) is algebraically exact. The only term containing a gate difference is multiplied by the bounded reference clip. The clip mismatch is zero on `|q_B|<=R` and is controlled elsewhere by a constant times `b_R(q_B)`. This proves (7.3) with constants independent of the larger clip and without a tail assumption on the competing state.

The exponential-square moment implies the displayed tail estimate, hence `epsilon_R=8 exp(-R²/256)` in (7.4). This decay dominates `exp(CR)` and any additional factor `1+R` for every fixed finite `C`. Accordingly (7.5) is a genuine Cauchy bound uniformly over `R'>=R`. The limiting state retains the primal and readout bounds. Applying (7.3) to that state verifies convergence to its own uncut vector field, rather than merely to an unidentified limit of clipped velocities. Passing the continuous integral equations gives a `C¹` uncut solution on the whole feature interval.

For uniqueness, any competing solution in the stated bounded-primal class can be compared against the same reference, with a possibly different but fixed finite constant `C`. The Gaussian tail still absorbs its stability exponent. At a restart, the initial reference discrepancy is already of order `exp(C_0 R)epsilon_R`; the further factor `exp(C_1 R)` still tends to zero. The proof therefore covers the declared uniqueness and reached-state restart class without presuming unrestricted local Lipschitzness of the uncut `L²` vector field.

At finite width, the tail observable is the continuous function `b_R`, and its squared empirical norm is a quadratic-growth measurement. Its time equicontinuity follows from the uniform reference query estimate. Thus (8.1) supplies a uniform tail estimate in probability at each fixed cap. The actual small readout is restored in (8.2); only the zero-readout reference needs a pointwise bound. Width is taken to infinity at fixed cap, and the cap is then removed. The additional middle-delta comparison and bounded adjoints give the claimed backward-field convergence as well as state comparisons.

## 7. Gradient structure, clocks, and the uniqueness class — lines 1078–1206

The initial operators need not be Hilbert–Schmidt. The trained increments are integrals of continuous rank-one Hilbert–Schmidt fields, and their norms and differences have the claimed bounds. The affine Hilbert space (9.1) is consequently the correct space for the gradient calculation.

The scalar Taylor estimate (9.2) is sufficient for continuous Fréchet differentiability of the predictor. On `|B|<=R` the remainder is bounded quadratically; on its complement the global Lipschitz bound and Cauchy–Schwarz give a linear remainder with arbitrarily small coefficient. One fixes `R`, lets the parameter increment vanish, and then removes `R`. Forward `L²` differences are of order the parameter variation. Expanding from the top downward uses successively fixed, square-integrable backward coefficients; terms containing two parameter changes are quadratic. This proves (9.3)–(9.4). Applying (2.4) in reverse order proves continuity of the gradient. No stronger substitution-operator differentiability is imported.

In feature time the raw first coordinate obeys `Z1_s=phi'(Z1)q1=delta1`, so the raw parameter velocity equals `grad f`. Its squared gradient norm is the sum in (9.5). The activation floor supplies `f_s>=25/36`, while the primal bounds give a finite upper bound. Starting from `f(0)=0`, there is a unique level-one feature time `s_*<=36/25<3/2`.

The bound `1-f(s)<=B_*(s_*-s)` gives divergence of the physical-time integral as `s` approaches `s_*`. It also gives the inequality in (9.6) with the correct direction: `s_*-s(t)>=s_* exp(-2B_*t)`. The physical multiplier remains strictly positive at every finite time. The stated residual and loss dissipation factors in (9.7) follow.

The raw uniqueness argument covers a potentially larger initial description of competitors. Its rank-one integral equations imply Hilbert–Schmidt increments. The scalar deficit equation applies and prevents a positive deficit from vanishing at finite time. Fubini supplies absolutely continuous coordinate versions of the first raw field. Their ordinary scalar chain rule proves (9.8), whose right side is in `L²`; membership of the transformed class is thus proved rather than assumed. Feature uniqueness and scalar-clock uniqueness identify the competitor. The same reasoning starts at any reached state, whose first transformed coordinate is already in `L²` and whose deficit is positive.

## 8. Exact raw GD and full-sequence limits — lines 1208–1357

Finite physical GF exists at every finite horizon. Residual dissipation bounds its readout, then its two matrix norms, then its first-coordinate velocity. At fixed width this prevents finite-time escape. For the high-probability feature-clock identification, `f_n(0)>-1/24` and `f_n(0)<1` ensure a level-one crossing before `3/2`, because `(25/36)(3/2)=25/24`. Uniform feature-predictor convergence and the scalar Lipschitz comparison identify the finite physical clock.

Exact raw GD is not silently equated with natural-coordinate Euler. Substituting `z_+=z+alpha phi'(z)q` into the cubic `F` gives exactly (10.1). With normalized `||q||_2` bounded, the deterministic inequalities `||q²||_2<=||q||_2²` and `||q³||_2<=||q||_2³` give the defect bound

`C(alpha² sqrt(n)+alpha³ n)`.

Summing uses `max alpha_k=O(eta_n)` and bounded accumulated feature time. For `eta_n=n^{-2}` the bound in (10.2) tends to zero. No empirical fourth or sixth moment is required.

The stopped-prefix construction is logically closed. Before a first bad endpoint its clock increments are positive; the coarse bounds control the step into that endpoint and keep it inside the constructed feature interval. Thus (10.3)–(10.5) apply through the endpoint used to contradict stopping. The random partition is handled pathwise by the time-Lipschitz reference tail function in (10.4), not by treating a random growing-length program as fixed.

The stopped predictor error tends to zero after the stated reference limits. The scalar clock comparison is valid up to the stopped endpoint. At that endpoint the margins `36/25<147/100` and the strictly positive deficit minimum on `[0,T+1]` contradict either stop condition with probability tending to one. The extra physical interval covers the last interpolation node, which may exceed `T` by less than one step.

The fractional-step version of (10.1) controls the prescribed raw interpolation. Finally both algorithms are compared with the same finite clipped reference at their respective clocks, proving the same-width state distance (1.7). This does not assert a norm comparison between operators on different-width spaces.

The final tolerance order is valid: choose the reference cap large, choose its mesh fine, and then take all sufficiently large widths. The intermediate almost-sure subsequences used for Fatou do not restrict the final width sequence. Each physical horizon is fixed before these choices; the proof never needs a positive residual bound uniform over infinite physical time.

## 9. Observations, velocities, and paths — lines 1359–1470

State comparison controls each fixed finite program of Lipschitz coordinate maps, bounded products, and bounded matrix actions. The separate middle-delta estimate controls the otherwise problematic unbounded gate product. For further bounded gates multiplying unbounded fields, truncation plus joint `W_2` convergence controls the error. Compactness of the limiting `L²` time image gives uniform squared tails; uniform law convergence supplies the corresponding finite empirical tails in probability. These arguments allow finite compositions and finite lists of time arguments, without claiming uniformity over all possible programs.

The kernel blocks are products of convergent quadratic-growth scalar measurements, with precisely the normalizations in (9.5). The forward differentiation in (11.1) gives the stated preactivation velocities; multiplying by the gate gives feature velocities. Curve differentiation uses (2.4), and bounded operators act on the correct layer spaces.

The actual GD interpolation is treated separately. On each step the raw block velocities are constant and uniformly bounded in the normalized vector/operator norms. Recomputed preactivations move by at most `C eta_n` in normalized vector norm, hence at most `C eta_n sqrt(n)` coordinatewise. Gate changes have the latter bound. Equation (11.2), followed by its layer-3 counterpart, therefore bounds the discrepancy from the left-node formula by `O(eta_n sqrt(n))=O(n^{-3/2})`. This argument does not require an independent coordinatewise bound on the velocity. The terminal-left convention is covered.

Measurable coordinate versions and finite expected squared path suprema follow from continuous `L²` velocities, time integration, Fubini, and Cauchy–Schwarz. The interpolation estimate (11.3) controls the population and empirical path errors by the mesh times the integrated squared velocity. Fixed-grid joint laws converge; interpolation of those grid values is a Lipschitz map into the continuous-path space. Taking width to infinity at fixed grid and then refining the grid proves the claimed path-space `W_2` convergence. Uniform squared-velocity convergence already supplies the integrated-velocity assertion.

## 10. Strict nonlinearity, expansions, and every positive time — lines 1472–1743

### Initial laws and coefficients

The initial forward variances in (12.1) retain the full activation second moment. Gaussian symmetry cancels the odd term and leaves `m_l>1`. The first reverse calculation has innovation variance `E[(B3)²]>0` and response

`c3 = E[Z3 arctan(Z3)/(1+Z3²)]/(100 m2) > 0`.

The cancellation of the odd offset term is valid; positivity is not incorrectly asserted pointwise for `z phi(z)phi'(z)` on negative `z`.

For the second transpose, conditioning on the first roots, the second-layer preactivation, and the entire independent third matrix fixes its reverse input without revealing the second matrix's conditional residual. Thus the second use of (3.2) is justified. The corresponding coefficient in (12.5) and variance in (12.4) are correct. The unbounded gated input is handled by truncation and second-moment convergence, not by assuming a globally Lipschitz unbounded product.

Adjunction gives exactly

`E[B2 V2]=gamma2+gamma1`,

`E[B3 V3]=gamma3+gamma2+gamma1=Gamma`.

All three `gamma` values are strictly positive, so each `V` is nonzero. A strictly positive gate cannot annihilate any of these nonzero `L²` fields.

### Initial expansions

Strong continuity and the readout integral give `W4(s)/s -> H3_0`. Bounded gates and operator-norm continuity successively give `delta_l(s)/s -> B_l` in `L²`. Substitution into (11.1) yields (12.7). Integrating an `o(s)` remainder in `L²` does give `o(s²)`. The matrix expansion holds in Hilbert–Schmidt norm by the continuous rank-one integral.

The three hidden kernel coefficients are `gamma_l`. The coefficient of the readout kernel is `E[H3_0 phi'(Z3_0)V3]=Gamma`, including all lower-layer motion. Consequently the feature-time total kernel is `m3+2 Gamma s²+o(s²)`. Since `s(t)=2t+o(t)`, the physical-time coefficients are exactly `4 Gamma` for the readout kernel and `8 Gamma` for the total kernel, as in (12.8).

The physical feature velocity is `4t phi'(Z_l0)V_l+o(t)` near zero. Its integrated squared norm has leading coefficient `16/3` times `||phi'(Z_l0)V_l||²`, with the analogous ungated formula for preactivations. Thus the second-order onset, nonzero small-time motion, and nonconstant total kernel follow with fixed strictly positive coefficients.

### Nonaffinity at every reached time

The top correction bound is `AaS²/10=63/160`. For the middle correction, the dominating variable depends only on the middle backward source group, which is independent of the middle forward Gaussian source; its expectation is at most `483/1600`. Markov's bound therefore gives the factor `1117/1600` in (12.10). For the bottom correction the dominator is independent of the first Gaussian root and has expectation at most `1561/800<2`. The threshold-four event has probability at least `1/2`; oddness and monotonicity of `F` give both signs of (12.11). Independence of the actual corrections is not assumed.

These estimates need only individual-time Gaussian marginals and source-group independence, not a bound on a Gaussian time supremum. Their closed-half-line passage has the correct Portmanteau direction: the limiting mass of a closed set is at least the limsup of the approximating masses. Thus both tails remain positive at arbitrarily large thresholds at every fixed reached time.

The affine least-squares formula (12.12) is valid because `Z` is square-integrable and has positive variance. If its attained minimum were zero, boundedness of `phi` on an unbounded support would force zero slope, and strict monotonicity would then force `Z` to be constant. This contradicts the tail bounds. All the moments in the formula are continuous along the `L²` path. Positive continuous variance and approximation error therefore have positive minima on each compact physical interval. There are only three layers, so their minima can be combined. Uniform empirical moment convergence transfers a smaller positive lower bound to the finite empirical errors with high probability.

### No later freezing

The argument at lines 1701–1736 proves a statement for every fixed positive feature time reached at finite physical time, independently of the initial expansion. The pointwise readout lower bound and positive gate imply `||delta3(s)||_2>0`. Approximating scalar programs therefore eventually have a reverse-source variance bounded away from zero. Their response shift is bounded by `a`, so Gaussian tail lower bounds survive passage to the limit and make `q2(s)` nonzero, in fact of unbounded support. Its positive gate gives `delta2(s)!=0`. Repeating the variance argument gives `delta1(s)!=0`. The order is top to middle to bottom, so this is not circular.

The adjoint identities (12.13) then give strictly positive pairings of the layer-2 and layer-3 preactivation velocities with their respective deltas; the first preactivation velocity is its delta. Cancellation between the direct and propagated parts of a preactivation velocity is consequently excluded. Strictly positive gates transfer this result to the feature velocities. Finally `2(1-f)>0` at each finite physical time transfers it from feature time to physical time. No uniform lower bound as time tends to infinity is claimed or needed.

## 11. Limit-order and quantifier audit

| Passage | Order and justification checked |
| --- | --- |
| Singular finite Gaussian program | Fix the finite program and positive perturbation; take width to infinity; remove perturbation using finite-program norm comparison and continuous source recursion. |
| Fixed-clip population/width flow | Fix cap and mesh; apply the finite program result; refine mesh using a norm estimate uniform in width. |
| Exponential moment for clipped flows | At each fixed cap and time, refine mesh, choose an almost-sure subsequence, and apply Fatou; the bound is independent of the cap and time. |
| Uncut population flow | Compare larger caps with a smaller capped reference; remove the cap using Gaussian tail decay against the stability exponent. |
| Finite uncut flow and exact GD | At fixed cap use uniform finite reference convergence; then remove the cap. For a prescribed final tolerance, select cap and mesh before taking all sufficiently large widths. |
| Physical time | Fix a finite physical horizon; scalar clock comparison stays strictly inside the already constructed feature interval. |
| Unbounded observations | Truncate the unbounded factor at a fixed level, use the joint law result, and remove the truncation by uniform squared-tail control. |
| Whole paths | First use a fixed finite time grid; take width to infinity; then refine the grid using integrated squared-velocity bounds. |
| Positive-time non-laziness | Fix any positive reached time; use a positive limiting upper-layer variance, then successively pass reverse tail bounds to lower layers. |

I found no use of a growing-query Gaussian theorem, no swap of infinite time with infinite width, no exchange of expectation with an uncontrolled supremum, and no inference of strong convergence for an unbounded product from weak convergence alone. The assertions are for every specified finite observation program, not one probability event uniform over an unrestricted collection of programs.

## 12. External dependency audit

No unresolved non-super-classic theorem dependency was found. In particular, the following specialized steps are proved within the document: adaptive Gaussian forward/transpose laws, response coefficients, singular-query removal, fixed-space bounded actions, the mesh/cap-uniform response estimate, uncut continuation and uniqueness, and exact raw-GD comparison.

The remaining background consists of foundational classical facts, used with the necessary hypotheses:

- Laws of large numbers and conditional variance bounds: finite root tuples have the required moments, and fresh residual Gaussian coordinates are conditionally independent where averaging is used.
- Gaussian projection and integration by parts: the relevant conditional constraints are finite linear observations; finite-program derivatives are bounded and roots integrable; singular Gaussian vectors are factored through standard Gaussians.
- Countable probability-measure extension: the index collection is countable, coordinates are real-valued, and finite laws are consistent under finite unions.
- Finite Borel probability regularity and `L²` density: the coordinate laws are finite-dimensional Borel probabilities, and the full sigma fields are generated by the countable coordinates.
- Finite-dimensional spectral decomposition and polynomial approximation: source covariance matrices are positive semidefinite and remain in a common bounded spectral interval for each fixed finite program.
- Cauchy–Schwarz, Jensen, Markov, Fatou, dominated convergence, Fubini, and compactness of a continuous image of a compact interval: all required moment, domination, or continuity conditions are supplied where used.
- Hilbert-space adjunction, Parseval, and Banach completeness: the neuron spaces are separable `L²` spaces, the actions are bounded, and trained increments are continuous Hilbert–Schmidt integrals.
- Contraction iteration, Gronwall comparison, scalar separation of variables, and ordinary scalar chain rules: the relevant restricted Lipschitz bounds, integrability, positive deficits, and absolutely continuous coordinate versions are established.
- Elementary Wasserstein coupling and metric facts: the finite-dimensional second-moment criterion is explained, and the path laws are on a separable continuous-path space with finite second moments.

## 13. Presentation defects and local clarifications

These are nonblocking editorial issues. None supplies a missing hypothesis for an application on the theorem's actual trajectory or requires a change to a mathematical conclusion.

1. **Stray closing parenthesis, line 1401.** The displayed feature-velocity formula ends with an extra `)` after `(Z^{(ell)})'`. Its intended identity is unambiguous from the immediately preceding formulas and the chain rule.
2. **Imprecise algorithm cross-reference, lines 107–108.** “BOTH algorithms in (1.3)” points to a display containing GD updates; GF is defined in the following prose at lines 68–69. A reference to “GD (1.3) and its associated GF” would identify the two algorithms more accurately.
3. **Local nonzero-input convention in the introductory transpose formula, lines 274–295.** The divisions in (3.1)–(3.2) require `h!=0`, and the limiting ratio requires a positive limiting input second moment. These conditions should be stated beside that illustrative formula. The actual initialization applications use `h=H` with `H>=m`, and the general zero/degenerate-query cases are separately handled in Section 3.4; there is no uncovered application here.
4. **Feature-time notation is introduced informally, lines 472–486 and 660–689.** The positive-step equations are eventually identified as feature-time dynamics in Section 9, but an explicit early sentence defining their independent time variable `s` and distinguishing primes in that variable from physical-time dots would make the notation easier to follow.
5. **Integrated-speed asymptotic convention, lines 1608–1611.** “Leading term” is mathematically clear from the preceding initial expansions. An explicit `+o(T^3)` and `T downarrow 0` would state the limiting regime directly and avoid any possible reading as an equality for arbitrary finite `T`.

## Final assessment

The proof meets the full finite-physical-horizon theorem as stated, including the autonomous bounded-action population formulation, uniqueness in the declared class and from reached states, full-sequence joint empirical/action-law convergence, exact raw-GD comparison, velocity and whole-path convergence, nonaffinity uniformly on compact intervals, strictly nonzero hidden feature velocity at every positive finite physical time, second-order initial motion, and a nonconstant total kernel.

**PASS. No mathematical repair or unresolved specialized dependency identified.**
