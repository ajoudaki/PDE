# Independent adversarial mathematical review

## Verdict

**PASS.** The full theorem stated in Section 1 is proved for the specified activation, initialization, dynamics, observation class, and finite-physical-horizon quantifiers. I found no mathematical gap requiring repair, false asserted conclusion, consequentially ambiguous notation, or unproved specialized theorem on which the result depends. This verdict covers the entire proof, including the construction of the population actions, uniqueness and restart, exact raw GD, all convergence assertions, persistent strict nonlinearity, nonzero hidden velocities at every positive finite physical time, and the initial-motion and kernel expansions.

This is an independent audit of the supplied document. It does not use or infer any previous verdict, correction history, or other research state.

## Source identity, access, and complete reading coverage

The sole mathematical source was:

`/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md`

The exact SHA256 observed before reading was:

`bebbb70a8f8da8fd2fa5304fc7af08026e72aef73e20f77f046509f87e63954e`

A second hash observation after the substantive audit and a final hash check after writing the report returned the identical value. All three match the frozen hash supplied in the request. The observed document length was **1,789 lines and 81,999 bytes**.

I read the complete document, with line numbers, in these consecutive ranges: **1–300, 301–600, 601–900, 901–1200, 1201–1500, and 1501–1789**. All six reads returned their complete requested ranges without truncation. I additionally reread **311–475** and **815–958** to check the Gaussian response derivation, singular-covariance passage, and causal response induction. The line references below refer to this observed document.

The only other input file accessed was the mandatory procedural skill:

`/etc/codex/skills/solve-math-rigorously/SKILL.md`

That skill was read completely before mathematical review. Its use was disclosed in the task's progress message. It supplied procedural instructions about rigorous verification, hypotheses, quantifiers, and proof auditing; it supplied **no mathematical lemma, theorem, factual dependency, or evidence**. No linked skill resources were opened.

File accesses otherwise consisted of the proof's hash/length checks and creation/verification of this requested report. I did not inspect another project or research file, prior review, audit status, conversation, or agent report. I did not contact an agent, browse an external mathematical source, or run numerical experiments, simulations, or computer algebra. The calculations in this report are analytic reconstructions from the displayed definitions and arguments. The proof was not edited. This report is the sole file written, using `apply_patch`.

## Independent reconstruction of the dependency chain

The following is the dependency order I verified. Later claims are not being used to justify the earlier estimates on which they depend.

| Stage | Source locations | Required output and dependency check |
|---|---|---|
| Model and scope | 18–163 | Equations, normalization, interpolation, state spaces, observation class, and finite-time quantifiers are specified. |
| Elementary controls | 165–256 | Bounded positive activation, coordinate transformation, initial operator bounds, strong convergence tools, and Gronwall comparisons. |
| Fixed finite Gaussian programs | 258–475 | Conditional projections, adaptive reuse in both orientations, empirical second moments, response formula, and singular-Gram removal. No time-mesh-uniform program limit is assumed. |
| Actual clipped Euler programs | 477–619 | Rank-one unrolling, deterministic oracle coefficients, restoration of empirical contractions, and the complete causal scalar law. |
| Common actions and clipped flows | 621–790 | Fixed probability spaces; bounded initial actions with genuine adjoints; uniform primal bounds; fixed-cap existence, uniqueness, Euler approximation, and width convergence. |
| Uniform response estimate | 792–978 | Past-row induction bounds both current response rows without circularity and gives a cap- and mesh-uniform exponential-square moment for the actual middle query. |
| Uncut population flow | 980–1060 | Fatou passage, asymmetric comparison, Gaussian tail removal, strong state and velocity convergence, uniqueness, and restart on the constructed feature interval. |
| Uncut finite feature flow | 1062–1109 | Continuous tail measurements, zero-readout references, restoration of the prescribed small readout, and convergence of the unbounded backward fields. |
| Gradient structure and physical time | 1111–1239 | Hilbert–Schmidt increments, scalar predictor differentiability, the actual gradient, monotone feature predictor, clock nonattainment, and uniqueness for raw competitors. |
| Exact raw GD | 1241–1390 | Finite GF existence, physical clock convergence, exact cubic coordinate-change defect, stopped random-step comparison, exclusion of either stopping condition, and prescribed interpolation. |
| All observations and paths | 1392–1505 | Unbounded-factor truncation, joint probe laws, kernels, recomputed GD velocities, integrated squared velocities, and whole-path Wasserstein convergence. |
| Initial movement and kernel | 1509–1663 | Two initial transpose calculations, positive movement coefficients, strong second-order expansions, and the nonconstant total kernel. |
| Persistent strict nonlinearity | 1665–1743 | Uniform two-sided support tails, positive attained affine-approximation error, and compact-time uniform positivity. |
| Every positive finite time | 1745–1789 | Sequential positivity of all backward fields, adjoint identities excluding cancellation of hidden motion, and the strictly positive physical clock multiplier. |

In particular, the response estimate uses the already identified **fixed finite** scalar programs. Clipping is removed only after a response bound uniform in the number of mesh steps has been proved. Exact GD's growing number of steps is handled by comparison with a fixed-cap reference, not by extending the fixed-program theorem to a width-dependent program. The final nonlinearity arguments use source laws already constructed and limits already proved.

## Detailed audit of the mathematical steps

### 1. Definitions, normalization, and elementary analytic tools

**Locations: 18–256; equations (1.1)–(2.5).**

The residual is excluded from each delta, so the physical factor is exactly `-2r`. In the finite parameter metric subsequently specified at lines 1243–1247, vector squared norms carry `1/n`, whereas matrix variations use the ordinary squared Frobenius norm. Differentiating the displayed predictor in that metric gives precisely the four updates (1.3). A rank-one hidden gradient block `delta h^T/n` has squared Frobenius norm `||delta||² ||h||²/n²`, which agrees with (1.6). Thus neither a factor of `n` nor the factor of two from the squared loss is missing.

The scalar bounds are valid: `5/6 < phi < 7/6`, `0 < phi' <= 1/10`, and `|phi''| <= 1/5`. With `F'(z)=10(1+z²)=1/phi'(z)`, the inverse has derivative `phi'(F^{-1}(x))`, and `chi'(F(z))=(phi'(z))² <= 1/100`. The transformed velocity is consequently `q^(1)` in feature time, while the raw first-coordinate velocity is `delta^(1)`. The non-Lipschitz cubic `F` is introduced as part of a Gaussian root tuple with finite moments; it is not improperly admitted as a general globally Lipschitz program instruction.

The initial matrix bound follows from a `1/4`-net, two-vector approximation with factor two, and the Gaussian tail at threshold five. The exponent `100n/8` dominates `2n log 9`. Independence of the two initial matrices is sufficient for applying the resulting high-probability event to both. The initial readout's normalized squared norm has expectation `n^{-2}`, giving the asserted `O_P(n^{-1})` normalized norm.

The Wasserstein facts are used with finite-dimensional laws having finite second moments. Weak convergence plus convergence of second moments controls squared tails; finite cell coupling then gives Wasserstein convergence. Continuous tests of quadratic growth are treated with those tails, not merely with weak convergence. Compact images of continuous `L²` paths give the uniform integrability needed later. The product passage (2.4) is strong: the unbounded factor converges in `L²`, and the other factor is bounded and converges in probability. The stated proof by truncating the fixed limiting factor verifies the required hypotheses. Its application to curve derivatives does not assume unrestricted Fréchet differentiability of a Nemytskii map on `L²`.

The discrete and continuous comparisons are applied to bounded nonnegative error quantities and finite accumulated coefficients. The elementary Gronwall proofs therefore cover their later uses.

**Finding:** no defect.

### 2. Gaussian conditioning, adaptive reuse, and singular queries

**Locations: 258–475; equations (3.1)–(3.5).**

For the first transpose calculation, projecting a Gaussian row along the observed input gives (3.1). Transposing the residual gives a Gaussian vector with multiplier `||u||/sqrt(n)` and projection onto the complement of the original input. The removed projection has normalized expected squared norm `1/n`. In particular, the innovation variance is the **full** limiting second moment `E[U²]`; it is not reduced by subtracting the response contribution.

For the general formula, the first two terms of (3.3) satisfy both observations. Indeed `U^T Y=Q^T V` gives the overlapping component, and the second term supplies the remaining `P_{V^⊥}Q` component of the transpose constraint. The residual subspace consists exactly of matrices annihilating the old forward inputs and whose transpose annihilates the old reverse inputs. Projection of an isotropic Gaussian matrix onto this subspace has the displayed law. Adaptive inputs cause no extra nonlinear conditioning constraint: conditional on the preceding transcript, each next input is fixed. The argument that only the queried residual is updated also preserves conditional independence of the two matrix residuals.

The new-call formula (3.4) follows by splitting its input into its old-input projection and orthogonal remainder. On fixed finite programs the discarded Gaussian projection has bounded rank. Its normalized norm tends to zero in probability once the already established input second moments bound the multiplier. Positive-definite limiting Grams give convergence of the finite coefficients. Conditional averaging supplies both bounded-test convergence and second-moment convergence, including the cross-term variance estimate. This establishes joint empirical convergence without asserting iid coordinates after reuse.

I independently checked the source-response cancellation. For `h_perp` orthogonal in `L²` to the old forward inputs, the old reverse answers' response parts disappear from `E[q_s h_perp]`. Gaussian integration by parts then yields

`beta = E[nabla_zeta h] - sum_r alpha_r E[nabla_zeta v_r]`.

The second term cancels the old answers' corresponding response contribution in `Y alpha`. What remains is (3.5). The new centered source is the old same-orientation Gaussian combination plus a fresh independent innovation. Its covariance with each old source is the uncentered input pairing, and its variance is the full input second moment. Deterministic coefficient selection is held fixed in the coordinate derivatives, as required by this calculation. Sources belonging to other orientations and roots can be conditioned on in integration by parts. Bounded formal derivatives and integrable roots justify the integrals.

Section 3.4 does not interchange inverses with a singular covariance limit. Fresh independent input noise gives a positive Schur complement at each call. For a fixed program, its removal has an `O(epsilon)` same-matrix comparison on the initial norm event. The scalar limit is instead passed through the causal response recursion: preceding coefficients converge, bounded first derivatives control the next derivative, finite covariance square roots are continuous, and dominated convergence passes the expected derivatives. Finite induction justifies the compact coefficient bounds. At a rank drop, formally distinct slots retain their explicit derivative convention. A deterministic covariance-null vector contracts to zero against the reverse inputs because its squared `L²` norm is zero. This removes any concern about a spurious response in a zero-variance direction.

No specialized Gaussian-program theorem is being assumed in these steps; the operative conditioning and convergence argument is supplied in the document.

**Finding:** no defect.

### 3. The clipped program and the common operator realization

**Locations: 477–790; equations (4.1)–(5.8).**

The proposed clips have the asserted bounds and derivative bounds. Unrolling each trained matrix produces exactly the forward and transpose contractions in (4.2), including their `Delta/n` normalization. For fixed horizon, cap, and number of steps, the top readout is pointwise bounded and the middle delta is clipped. The coordinate products can therefore be extended smoothly with bounded derivatives without altering their values or derivatives on attained states. This verifies the program theorem's hypotheses.

Freezing contractions at their causal limiting expectations defines a legitimate deterministic-coefficient program. Their subsequent restoration is a finite induction using the displayed bilinear difference inequality and bounded initial matrix norms. This argument is expressly fixed-program; no hidden uniformity in the mesh is needed here.

The causal order in (4.3)–(4.6) is correct. Forward response terms use strict past indices. Reverse terms can include the present forward input. In particular, differentiating the current middle delta gives both

`E[phi''(Z2_k) tau_R(q2_k)]`

and

`b3_kk E[(phi'(Z2_k))² tau'_R(q2_k)]`.

The latter is the current return through matrix 3. It is present, and its contribution is also retained in the later response bounds.

The countable family of finite programs is closed under the operations needed to compare unions and rational linear combinations. Each finite joint law is the limit of the same underlying finite-width calculations, so the stated consistency is valid. Countable probability-measure extension applies on products of real lines. The coordinate-generated sigma field and the included dense bounded smooth cylinder functions give the claimed `L²` density, using truncation and regularity of finite-dimensional Borel probability measures.

Passing finite normalized second-moment inequalities gives a well-defined linear initial action with operator norm at most ten. Zero-norm differences are sent to zero, so extension to equivalence classes is justified. Passing finite transpose pairings and then using density proves (5.2) for all `L²` inputs. The resulting reverse action is the actual adjoint on the common spaces. These are fixed spaces and fixed operators; later meshes do not enlarge the dynamical state.

The primal bounds (5.5) are obtained in a noncircular order: readout, third matrix, second matrix, first-coordinate velocity. Their constants are independent of cap and width. Pointwise readout bounds (5.6) apply to the zero-readout references. The stability estimate places the potentially unbounded readout difference in `L²` and uses only the reference readout as the pointwise-bounded multiplier. For the middle gate, the factor `2R` gives a Lipschitz constant of order `1+R`. Rank-one differences have the required operator-norm estimate.

The integral contraction is carried out on a closed path set preserving the reference readout bounds; the velocity estimates preserve enlarged primal bounds for a sufficiently short interval. The a priori bounds allow finitely many restarts on each fixed feature horizon. The local Euler error is `O_R(Delta²)`, which gives a global `O_R(Delta)` comparison with constants independent of width. Fixed-program convergence, mesh refinement, and finite time nets then establish the fixed-cap uniform law. These steps do not require local Lipschitz continuity of the uncut infinite-dimensional field.

**Finding:** no defect.

### 4. Independent verification of the uniform response estimate

**Locations: 792–978; equations (6.1)–(6.11).**

This is the central quantitative dependency. I checked the induction and constants directly.

At index zero, the readout expression is identically zero, so both backward response rows vanish. The proof does not infer that all formal source derivatives vanish merely because a Gaussian slot has variance zero.

Assume only `U_r,V_r <= 1` for `r<k`. A single bottom backward source enters the first-coordinate sum once with coefficient `Delta`. The bound `chi' <= 1/100` then gives

`|partial H1_j / partial zeta1_s| <= (Delta/100) exp(S/100)`.

Consequently `|a2_js| < A Delta`, with `A=3/2`, using only past `U` rows. No pointwise bound on the realized bottom query is required.

For the middle forward-source row, summing source derivatives gives one direct-source contribution in total. The other terms are bounded by

`A Delta sum_{r<j} (|q2_r|/5 + V_r/100) max_{v<=r} R_v`.

This gives the envelope `E_j` in (6.3). A single middle backward source contributes at most `A Delta/10`, yielding (6.4). Only past `V` rows enter that envelope. Temporal correlation of the Gaussian sources does not impair the exponential-moment calculation: Jensen averages exponentials over time slots, and the remaining bounds use their marginal variances alone.

At `S=3/2`, the exponent is exactly bounded by

`219p/400 + 3969p²/1280000`.

For `p=1,2`, the resulting norms satisfy `||E_j||_1<4` and `||E_j||_2<3`. Thus `|a3_js| < A Delta` follows from `49/36+3/50<3/2` before the current top backward row is bounded.

The top derivative row has bound `(73/300) S max T`, and the forward recursion gives `max T <= exp(657/800)<5/2`. Adding the learned contraction terms yields

`V_k <= 73/80 + 147/3200 = 3067/3200 < 1`.

Only after this estimate is available does the proof use

`||q2_k||_2 <= 7/40+7/6 = 161/120 = Q`.

The complete current middle derivative row is bounded by `(|q2_k|/5+V_k/100)E_k`. Cauchy–Schwarz and the learned middle contraction give

`U_k <= 3(Q/5+1/100)+SQ²/100`

`<= 167/200+77763/2880000 = 2482563/2880000 < 9/10`.

Thus the simultaneous induction is genuinely causal: the current `U_k` is used in neither its own proof nor the proof of the current `V_k`. The complete current matrix-3 return is included in the `V_k/100` term.

Finally the actual middle query equals its centered Gaussian source plus a shift bounded by `7/6`; the source variance is at most `(7/40)²`. The elementary inequality `(u+v)²<=2u²+2v²` gives the displayed Gaussian square integral in (6.11), with parameters `49/288` and `49/6400`. Its bound by two is correct. Dependence between shift and source is immaterial to this pointwise inequality. This proves the required uniformity in cap, mesh, and time index without any source-path maximum estimate.

**Finding:** no defect.

### 5. Removing clipping, existence, uniqueness, and finite feature-flow convergence

**Locations: 980–1109; equations (7.1)–(8.2).**

For each fixed cap and time, the reference query converges strongly in `L²` under mesh refinement. An almost-everywhere subsequence and Fatou give (7.1). The same deterministic bound therefore holds at every time and every cap. The proof does not use a single almost-sure subsequence valid for an uncountable set of times.

The three-term identity (7.2) is exact. Its first two terms give a distance bound of order `1+R`; the last is measured solely on the reference query. It vanishes below the smaller cap and is at most `2|q_B|` elsewhere. Thus no tail or pointwise readout bound for the competing uncut state is silently needed. The continuous function `b_R` dominates the relevant tail and is suitable for later Wasserstein measurements.

From the exponential-square moment, the stated tail norm is bounded by

`epsilon_R = 8 exp(-R²/256)`.

Every comparison loss is of the form a polynomial in `R` times `exp(CR)`. Hence these errors tend to zero for every fixed finite comparison constant, including a constant associated with a competing bounded-primal solution.

The clipped states are Cauchy in the complete continuous-path Banach norm. The limit preserves the readout and primal bounds. Applying the asymmetric estimate to that limit and its references also makes the **computed uncut velocities** converge uniformly. Passing the integral equations therefore constructs a `C¹` uncut flow; no weak limit of an unbounded product is being identified as a strong limit. The same estimate forces any competitor to agree. For restart, the already small discrepancy at the restart time is multiplied by at most one further `exp(CR)`, still dominated by the Gaussian tail. This proves uniqueness from every reached feature state over the remaining constructed interval.

At finite width, `a_{n,R}` is a continuous quadratic-growth measurement of the reference query. The uniformly bounded reference state velocity and (5.7) give the needed time Lipschitz bound. A finite time net establishes uniform convergence of this tail measurement. Comparison (8.2) uses the prescribed readout only through its vanishing normalized `L²` norm; the zero-readout reference retains the necessary pointwise bound. Taking width to infinity at fixed cap, then removing the cap, is legitimate. The first inequality after (7.2) separately controls the middle delta, and adjoint bounds then control the bottom query. Those additional fields therefore have the required strong comparison and joint laws.

**Finding:** no defect.

### 6. Gradient structure, physical clock, and raw uniqueness

**Locations: 1111–1239; equations (9.1)–(9.8).**

The initial operators need only be bounded. The trained increments are integrals of rank-one operators and are Hilbert–Schmidt. The rank-one norm and difference identities verify convergence of the clipped integrals in that stronger norm. This justifies the affine Hilbert parameter space without incorrectly assuming the initial operators are Hilbert–Schmidt.

The scalar remainder estimate (9.2) is sufficient for Fréchet differentiability of the **predictor**. With a fixed old backward coefficient `B` in `L²`, its bounded part gives a quadratic remainder, and its tail gives an arbitrarily small multiple of `||v||_2`. Expanding from the top down applies this to the old readout and the two old reverse coefficients. Forward changes are `O(||dtheta||)`; terms containing both a matrix/readout change and a feature change are quadratic. The resulting derivative is exactly (9.3). Parseval gives the rank-one Hilbert–Schmidt pairing and hence the gradient (9.4). Gradient continuity follows in reverse order by (2.4) and operator-norm continuity. These arguments do not require a false unrestricted differentiability assertion for coordinatewise activation maps on `L²`.

The inverse-coordinate curve rule gives `(Z1)'=phi'(Z1)q1`. Thus the feature flow is indeed the raw gradient ascent flow of `f` in (9.1), and `f_s` is the sum of the four squared gradient blocks. The readout block is at least `m²=25/36`. Starting from `f(0)=0`, the predictor therefore reaches one exactly once at a feature time `s_*<=36/25<3/2`.

The kernel sum is continuous and bounded on the constructed interval. The estimate `1-f(s)<=B_*(s_*-s)` implies divergence of the physical clock integral at `s_*`. Its inverse exists for every finite physical time and obeys

`s_*-s(t) >= s_* exp(-2B_*t) > 0`.

The inequality direction is correct. It is the upper bound on `f_s` that proves nonattainment; the lower bound proves existence of the level-one feature time. Substitution gives exactly the physical gradient descent and loss identities in (9.7).

For a raw competing solution, continuity of its backward fields puts its matrix increments in the Hilbert–Schmidt affine class, so the predictor derivative and scalar deficit equation apply. Its bounded compact-time kernel keeps an initially positive deficit strictly positive. Scalar coordinate absolute continuity, Fubini, and the pointwise chain rule give (9.8); its right-hand side lies in `L²`. Thus transformed membership is proved for the competitor rather than assumed. The feature-clock comparison and nonattainment then identify it with the constructed solution. Reached states have the necessary initial transformed membership, so the same reasoning proves the stated restart claim.

**Finding:** no defect.

### 7. Exact raw GD and same-width comparison

**Locations: 1241–1390; equations (10.1)–(10.6).**

The finite raw gradient calculation yields a nonincreasing residual magnitude. Integrating the readout bound, then the two matrix bounds, then the first-coordinate velocity bounds all finite-dimensional coordinates on every finite physical interval. Local smooth ODE existence can therefore be continued. This also covers finite initializations outside the later high-probability comparison event.

On that event, the finite feature predictor has derivative at least `25/36`. The condition `f_n(0)>-1/24` ensures it reaches one before feature time `3/2`; the condition `f_n(0)<1` puts its physical clock on the increasing branch. Both hold with probability tending to one. Uniform feature-predictor convergence and a uniform Lipschitz bound give the finite physical-clock limit.

For GD, positivity of each feature increment is established on the stopped prefix. The primal bounds first bound the predictor and hence each increment by `C eta_n`. The incoming step to the first bad node is included: its feature endpoint is at most `147/100+C eta_n<3/2` for sufficiently large width. There is consequently no unexamined final step at the stopping boundary.

Expanding the actual cubic gives exactly

`F(z+alpha phi'(z)q)-F(z)`

`= alpha q + 10 alpha² z(phi'(z))² q² + (10/3)alpha³(phi'(z))³q³`.

The bounds `||q²||_2<=||q||_2²` and `||q³||_2<=||q||_2³` are valid finite Euclidean inequalities. With `||q||_2<=C sqrt(n)`, the normalized extra-vector bound is `C(alpha² sqrt(n)+alpha³ n)`. Summing over a bounded accumulated feature interval yields

`O(eta_n sqrt(n)+eta_n² n)=O(n^{-3/2}+n^{-3})`.

No fourth- or sixth-moment law is required.

The clipped local error, asymmetric comparison, and this exact defect give the recursion (10.3). For its random positive partition, the Riemann-sum tail estimate (10.4) is pathwise; it does not require deterministic steps or independence. Discrete Gronwall gives (10.5), and the prescribed order of cap choice, mesh choice, and width limit gives the stopped predictor error (10.6).

The population deficit minimum on `[0,T+1]` is strictly positive for every fixed `T`. Scalar clock comparison controls the entire stopped interpolation. At a proposed first bad endpoint, the estimates simultaneously place the feature clock below `147/100` and the predictor below `1-rho/2`, contradicting either stopping criterion. The extra unit of physical time correctly covers the terminal interpolation node.

Applying the same cubic identity to a fractional step compares the actual raw interpolation with transformed-node interpolation. The common clipped reference, evaluated at the two converging clocks, then gives the exact same-width distance (1.7) for GD and GF. No comparison of operators on different-width spaces is asserted or used. The final convergence is along the full width sequence in probability; Fatou subsequences used for a deterministic population moment bound do not restrict that sequence.

**Finding:** no defect.

### 8. Probes, velocities, and whole-path laws

**Locations: 1392–1505; equations (11.1)–(11.3).**

The state comparisons propagate through each fixed finite program of permitted Lipschitz maps, bounded products, and current matrix actions. The separately controlled middle delta and bottom query cover the named unbounded backward fields. To multiply an unbounded field by a bounded gate, the proof clips the unbounded factor, passes its bounded approximation, and then uses uniform squared tails. The limiting continuous `L²` path has compact image, and uniform Wasserstein convergence transfers the needed tail control to the finite laws. Bounded operator calls preserve these truncation comparisons. This verifies the extra measurement class without assuming unproved higher moments.

The three identities (11.1) follow by differentiating the forward equations, including the derivative of the lower-layer features. Their physical versions use the factor `2(1-f)`. Each term has the required `L²` integrability and strong continuity. Predictions and kernel blocks are quadratic-growth measurements or products of convergent scalar measurements, so their uniform convergence follows with the displayed normalization.

The treatment of GD velocities uses the derivative of the **recomputed** hidden preactivations along raw parameter interpolation. Primal bounds control each raw block velocity and then each recomputed preactivation velocity. A mesh step changes a preactivation by `O(eta_n)` in normalized Euclidean norm and hence by `O(eta_n sqrt(n))` in coordinate supremum. The resulting gate supremum bound multiplies an already bounded normalized velocity. Equation (11.2), followed by the same calculation in layer 3, therefore gives the asserted uniform `O(n^{-3/2})` discrepancy from the node formulas. The terminal-left convention is covered. This is sufficient for velocity laws, squared norms, and their time integrals.

Continuous paths into separable `L²` have the jointly measurable versions needed for coordinate integration. Cauchy–Schwarz in time gives finite expected squared path supremum. The interpolation estimate (11.3) controls the path-space transport cost by mesh size times the integrated squared velocity. On a fixed grid, the already proved joint Wasserstein convergence passes through linear interpolation. Taking width to infinity and then refining that grid proves the claimed `W_2(C([0,T]))` convergence. Finite-dimensional law convergence alone is not being mistaken for whole-path convergence.

**Finding:** no defect.

### 9. Initial transpose laws, movement, and kernel coefficients

**Locations: 1509–1663; equations (12.1)–(12.8).**

At initialization, Gaussian symmetry makes the odd contribution to `E[phi(Z)²]` vanish while retaining the constant contribution one. Thus the recursion for `m_ell` in (12.1) is correct and gives `m_ell>1`.

For matrix 3, the first-transpose identity gives a bounded response plus a Gaussian innovation of variance `E[(B3)²]>0`. The response coefficient is

`c3 = E[Z3 phi(Z3)phi'(Z3)]/m2`

`= E[Z3 arctan(Z3)/(1+Z3²)]/(100m2) > 0`.

Only the odd offset term vanishes; the sign is not obtained by asserting pointwise positivity of `z phi(z)phi'(z)`. The innovation is independent of the old layer-2 tuple, so (12.4) follows and is positive.

For matrix 2, conditioning on the first-layer roots, the initial second-layer preactivation, and the entire independent third matrix determines the actual reverse input without revealing the conditional residual of matrix 2. Hence the second use of (3.2) is legitimate. Its response coefficient is exactly (12.5), and its full innovation variance is `E[(B2)²]>0`. The Gaussian-plus-bounded field times a bounded gate is passed by truncation and its established second moments. Thus all three `gamma_ell` are strictly positive.

The adjoint calculations in (12.6) can be reconstructed as

`<B2,V2> = m1||B2||² + <(W2_0)*B2, phi'(Z1_0)B1>`

`= gamma2+gamma1`,

and

`<B3,V3> = gamma3+<B2,V2> = Gamma`.

They establish nonzero `V2,V3` without imposing a sign on individual matrix contributions. Strict positivity of the gate then gives a nonzero feature-motion coefficient in each layer.

For the expansions, the readout integral first gives `W4(s)/s -> H3_0` strongly in `L²`. Reverse-order use of bounded operators and the bounded-gate convergence lemma gives `delta_ell(s)/s -> B_ell`. Substitution in (11.1) yields `Z_ell'(s)=s V_ell+o(s)` in `L²`, and integration gives the preactivation expansion with coefficient `1/2`. The feature derivative expansion follows from the same gate lemma, and its integral has the same `1/2` factor. This establishes both derivative and integrated expansions; it does not differentiate an unspecified little-o remainder.

Rank-one velocity integration gives the Hilbert–Schmidt increment coefficient `(s²/2)B_ell tensor H_{ell-1,0}` and squared leading norm `gamma_ell s^4/4` for each hidden matrix.

The three hidden kernel blocks are `gamma_ell s²+o(s²)`. For the readout block, the feature expansion gives

`K4(s)=m3+s² <H3_0,phi'(Z3_0)V3>+o(s²)`

`=m3+Gamma s²+o(s²)`.

Using the separately proved velocity expansion gives `(K4)'(s)=2Gamma s+o(s)>0` at sufficiently small positive feature time. Lower-layer motion is included in `Gamma`. The total feature-time kernel is consequently `m3+2Gamma s²+o(s²)`.

Finally, `s_t(0)=2` gives `s(t)=2t+o(t)`, so

`H_ell(t)-H_{ell,0}=2t² phi'(Z_{ell,0})V_ell+o(t²)`,

`K4(t)=m3+4Gamma t²+o(t²)`,

`sum_ell K_ell(t)=m3+8Gamma t²+o(t²)`.

The velocity coefficients are `4t V_ell` and `4t phi'(Z_{ell,0})V_ell`. Squaring their `L²` norms and integrating gives exactly the factors `16/3` multiplying `T³` in the two energy expansions. Their coefficients are strictly positive. All time limits here are population small-time limits; finite-width consequences are taken at a sufficiently small fixed time using the convergence already proved.

**Finding:** no defect; the initial and kernel coefficients are correct.

### 10. Persistent strict nonlinearity and its uniform quantifiers

**Locations: 1665–1743; equations (12.9)–(12.12).**

The proof supplies more than an initial-time nonaffinity argument. Each finite scalar program has forward source variance between `m²` and `a²`. At the top, the response displacement is bounded pointwise by

`AaS²/10=63/160`.

A sufficiently large Gaussian source event therefore forces either tail of `Z3`, regardless of its dependence on the displacement.

At the middle layer, the actual displacement is dominated by a variable depending only on the middle backward source group. Its expectation is at most

`ASQ/10=483/1600`.

That **dominating variable**, rather than the actual correction, is independent of the forward source. Markov's inequality leaves probability at least `1117/1600` for it to be at most one. Intersecting this event with the independent source tail yields (12.10).

At the bottom, the transformed-coordinate displacement is dominated by a variable depending only on the bottom backward source group, independent of the initial root. Its expectation is at most

`S(Q/10+a)=1561/800<2`.

It is at most four with probability at least one half. The odd increasing cubic and its increasing inverse convert the independent Gaussian root event into precisely (12.11), for both signs. The activation need not be odd, and the proof does not treat it as odd.

These bounds are uniform in cap, mesh, and time index. For each fixed limit time, the half-lines used are closed, so their limiting probabilities are at least the limsup of the approximating probabilities. The direction of this passage is correct for retaining these lower bounds. No independence across times and no Gaussian path-supremum bound are used. Both tails of every hidden preactivation remain nonzero arbitrarily far out, at every reached time and at initialization.

For each such `Z`, the variance is positive, and least-squares minimization over intercept and slope gives (12.12) with an attained minimum. A zero minimum would give `phi(Z)=alpha Z+beta` almost surely. If `alpha` were nonzero, boundedness of `phi` would force bounded support for `Z`, contradicting the tails. If `alpha` were zero, strict monotonicity would force `Z` to be constant, again a contradiction. The minimum is therefore strictly positive.

All moments in this least-squares expression are continuous along the `L²` path. The denominator is positive at every time, so the expression is a continuous positive function on each compact physical interval. Compactness gives a positive lower bound, and the finite number of layers permits a common positive lower bound for all three. Uniform empirical moment convergence, with the limiting variance bounded away from zero, also justifies the asserted finite empirical lower bound with probability tending to one. This verifies the full compact-time claim, including time zero.

**Finding:** no defect; persistent and uniform strict nonlinearity is proved.

### 11. Non-lazy dynamics at every positive finite physical time

**Locations: 1745–1782; equation (12.13).**

Fix an arbitrary positive feature time reached at a finite physical time. The pointwise readout bound `W4(s)>=ms`, together with finite preactivations and strictly positive `phi'`, gives `delta3(s)>0` almost surely and `||delta3(s)||_2>0`.

The approximate middle backward Gaussian source has variance equal to the approximating `E[(delta3)²]`. Strong convergence makes these variances bounded below by a positive number once the cap is sufficiently large and its mesh sufficiently fine. The middle query differs from that source by a uniformly bounded shift. Each of its two tails therefore has a positive Gaussian lower bound that passes to the limit through a closed half-line. Consequently the limiting query is not zero; multiplication by the strictly positive middle gate cannot make the middle delta zero.

This reasoning then repeats for the bottom source, whose variance is the already established positive second moment of the middle delta. It gives a nonzero bottom delta. The implications proceed in the order `delta3 -> delta2 -> delta1`, so they do not assume a lower-layer positivity conclusion in order to prove its premise. A diagonal choice of sufficiently fine meshes for successively large caps is enough; no uniform positive variance over times approaching zero is required.

Positive backward fields alone could leave an apparent cancellation issue in the preactivation velocities. The document explicitly resolves it by adjunction:

`<delta2,Z2'> = K2+K1 > 0`,

`<delta3,Z3'> = K3+K2+K1 > 0`.

These identities follow by moving the current matrix action to its adjoint and substituting the delta definitions. Together with `Z1'=delta1`, they rule out zero preactivation velocity in any layer. A strictly positive bounded gate cannot annihilate a nonzero `L²` variable, so the feature velocities are also nonzero. Finally `2(1-f)>0` at every finite physical time by the clock nonattainment proof. Therefore every hidden physical feature velocity has nonzero `L²` norm at every `t>0` that is finite.

The quantifier is universal over such times: the argument starts with an arbitrary one. It is not merely an almost-everywhere-in-time or small-time statement. Exact vanishing at time zero is consistent with, and separately quantified by, the second-order onset calculation.

**Finding:** no defect; the full every-positive-finite-time claim is proved.

## Quantifier, convergence, and theorem-use checks

The finite-program law is used only for a fixed finite list of instructions. Mesh- and cap-uniformity are proved separately where needed. The limiting construction and width arguments follow the stated order: fixed cap and fixed reference mesh for the finite-program limit, mesh refinement for that cap, and cap removal using the explicit uniform response and tail bounds. For an arbitrary requested accuracy, these choices precede sufficiently large widths. This proves convergence in probability of the full sequence.

Time uniformity is obtained from norm-controlled comparisons and finite nets, and unbounded factors are handled by strong convergence and uniform squared tails. Whole-path convergence has its own integrated-velocity estimate. No passage from weak convergence alone to an unbounded quadratic measurement, product, or path-space second moment is required.

The physical horizon is fixed but arbitrary. Constants may depend on it. The proof does not require a positive deficit uniform as physical time tends to infinity, nor interchange infinite time with width. Restart is from every **reached** state on the constructed common spaces. No existence theorem for arbitrary population initial states is needed. The operator-norm comparisons occur on a common population space or at the same finite width; cross-width statements concern laws and actions.

The background results actually used are foundational classical facts in the domains permitted by the request: Gaussian orthogonal projection and elementary Gaussian integration, laws of large numbers with the stated integrability, conditional averaging, finite-dimensional spectral decomposition and polynomial approximation, finite Borel-measure regularity and countable product extension, Hilbert-space density/Parseval/adjoints, elementary integral contraction and Gronwall comparison, Fubini, dominated convergence, and Fatou. Their relevant hypotheses are met here. The document proves its operative Wasserstein, response, comparison, differentiation, clock, and path-estimate steps. I found no unproved non-classical mean-field, tensor-program, continuation, concentration, support, or infinite-dimensional ODE theorem hidden in the dependency chain.

## Notation audit and severity assessment

I found **no actual erroneous or consequentially ambiguous notation requiring correction**.

The main potentially sensitive conventions are resolved in the text: the readout is the rescaled `W^(4)`; deltas exclude the residual; finite transpose and population adjoint are distinguished; vector norms have their population or normalized finite meaning specified; operator and Hilbert–Schmidt norms are used for their respective purposes; feature time and physical time derivatives are distinguished; scalar-function primes have their ordinary scalar meaning; `A=3/2` differs from the activation upper bound `a=7/6`; and the initial moments `m_ell` differ from the activation floor `m`. The temporary omission of the middle clipping subscript is explicitly restricted to the scalar clipped programs. Source-slot derivatives at singular covariance are derivatives of the displayed expression with coefficients fixed, as stated.

Repeated expectation notation across layers is consequential only if a product mixes populations. Here the adjoint and rank-one formulas place each integrand on the indicated layer, and separate cross-layer moments are multiplied as scalars. The same-layer observation restriction avoids an unstated coordinate pairing between populations. The notation therefore does not alter or obscure a required mathematical assertion.

Optional presentational changes are not mathematical defects and are not grounds for withholding a pass. No such changes are required for this verdict.

| Severity | Number of findings | Required mathematical action |
|---|---:|---|
| Fatal false statement or counterexample | 0 | None |
| Major proof gap or missing hypothesis | 0 | None |
| Smaller mathematical error requiring repair | 0 | None |
| Erroneous or consequentially ambiguous notation | 0 | None |

**Final verdict: PASS. No required mathematical repair.**
