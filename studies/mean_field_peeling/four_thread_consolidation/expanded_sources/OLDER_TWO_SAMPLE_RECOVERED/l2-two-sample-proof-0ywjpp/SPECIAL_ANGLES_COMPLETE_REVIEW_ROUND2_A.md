# Independent isolated mathematical review — round 2, referee A

## Verdict and exact scope

**PASS for the theorem actually stated: two inputs, two hidden layers of equal width, both activations arctangent, labels `(1,-1)`, correlations `rho=0` or `rho=-1`, the initialization (2), the parameter metric (7), and the raw updates (6) with `eta_n=n^{-2}`.**

I found no required mathematical correction or unresolved proof obligation in the complete document. This verdict includes the deterministic global finite-time solution and restart assertion, the canonical initial operator and its actual adjoint, the full-sequence finite-width limits, the specified raw-GD interpolation, every stated observable and convergence mode, persistent nonaffinity and positive-time motion, and the positive quadratic change of the full kernel. The detailed checks below explain the verdict; it is not based on a selected lemma.

The verdict makes **no all-angle inference**, no assertion for other depths or activations, no interchange with an infinite-time limit, and no assertion of operator-norm convergence of matrices of different dimensions. “Global” here means existence of one solution for every finite physical time, with estimates allowed to depend on the chosen finite horizon.

Required corrections: **none found**. Two optional clarity edits are recorded at the end. They do not alter the theorem or supply missing mathematical premises.

## Source identity and isolation record

- Sole mathematical source: `/tmp/l2-two-sample-proof-0ywjpp/L2_TWO_SAMPLE_SPECIAL_ANGLES_COMPLETE_PROOF.md`.
- Source size read: **1,977 lines, 94,653 bytes**. I personally read the entire document, including its scope discussion and provenance-only final lines. A portion truncated in one combined display was separately reread so that no source interval remained unread.
- Expected SHA-256 supplied by the user: `830ca8830edddd5acf351664e71a346a702dd8c73e9191775458fec8b6df71e0`.
- Observed source SHA-256 before the audit: `830ca8830edddd5acf351664e71a346a702dd8c73e9191775458fec8b6df71e0`.
- Observed source SHA-256 after the complete mathematical audit, also rechecked after writing this report: `830ca8830edddd5acf351664e71a346a702dd8c73e9191775458fec8b6df71e0`.
- The source was not edited. The sole output file created or edited for this review is this report, using `apply_patch`.
- The only additional file read was the procedural skill `/etc/codex/skills/solve-math-rigorously/SKILL.md`. It supplied audit procedure, not mathematical context for this theorem.
- No project files, ledgers, earlier reviews, snapshots, dependency notes, other tasks, or prior mathematical conversations were consulted. In particular, none of the four snapshots named in the source's provenance record was opened or used.
- No agents, numerical experiments, symbolic-computation experiments, or source edits were used. File reads, line/byte counting, and cryptographic hashing were the only diagnostic operations.
- No external mathematical source was consulted. The document does not rely on an essential specialized external theorem: the Gaussian-program identification, singular-covariance passage, operator construction, and response estimate are proved within it. The external-result audit below distinguishes the elementary background facts from those substantive internal arguments.

Line references below refer to the verified source, not to this report.

## Complete obligation inventory

The following inventory covers every numbered equation and every source subsection. The later sections give the substantive checks behind these results.

| Source location | Equations | Obligation audited | Result |
| --- | --- | --- | --- |
| §1.1, lines 12–86 | (1)–(7) | Geometry, variances, loss normalization, parameter metric, exact raw updates and physical clock | Satisfied |
| §1.2, lines 88–145 | (8)–(11) | Separate neuron spaces, empirical normalization, rank operators, adjoints, population state and equations | Satisfied |
| §1.3, lines 147–235 | (12)–(14) | Full theorem scope, kernel blocks, probe restrictions, velocity/energy metrics, nonaffinity and strict motion | Discharged by the subsequent arguments |
| §2.1, lines 239–294 | (15)–(18) | Special-angle transformation, antiparallel reduction, reconstruction of the complete first row | Satisfied |
| §2.2, lines 296–376 | (19)–(22) | Ordinary-L2 local construction, stability, feedback, and comparison of differing initial operators | Satisfied |
| §2.3, lines 378–454 | (23)–(27) | Global extension, chain rules, exact energy identity, uniqueness in the original class, autonomous restart | Satisfied |
| §2.4, lines 456–553 | (28)–(35) | Untruncated Euler, exact raw-GD defect, interpolation and velocity errors, high-probability uniform bounds | Satisfied |
| §3.1, lines 557–646 | (36)–(40) | Causal scalar program, full source covariances, learned responses, formal derivative convention | Satisfied |
| §3.2, lines 648–747 | (41)–(45) | Width-uniform all-order moments for each fixed graph | Satisfied |
| §3.3, lines 749–859 | (46)–(51) | Adaptive Gaussian conditioning, projection removal, empirical induction, source-response identification | Satisfied |
| §3.4, lines 861–958 | (52)–(54) | Singular Grams, vanishing query noise, feedback replacement, all polynomial tests and finite-dimensional Wasserstein convergence | Satisfied |
| §3.5, lines 960–1044 | (55)–(56) | One common countably generated space, bounded initial operator, actual adjoint, canonicity, common-space Euler limit | Satisfied |
| §3.6, lines 1046–1149 | (57)–(62) | Mesh-uniform expected response bounds from actual fresh-root forcing | Satisfied |
| §3.7, lines 1151–1215 | (63)–(66) | Bounded Gaussian remainders, source isometries, passage to the existing continuous flow, measurability | Satisfied |
| §4.1, lines 1219–1311 | (67)–(72) | Product continuity and uniform integrability, including path suprema and actual initial readout | Satisfied |
| §4.2, lines 1313–1369 | (73) | Fixed-time width/time passage, both query orientations, unbounded velocity probes, readout restoration | Satisfied |
| §4.3, lines 1371–1396 | (74) | Same-neuron path laws in every finite Wasserstein order; uniform predictions, loss and kernels | Satisfied |
| §4.4, lines 1398–1491 | (75)–(76) | All original velocities, uniform squared norms, integrated comparisons, parameter speeds and increments, transfer to raw GD | Satisfied |
| §5.1, lines 1495–1551 | (77)–(80) | Finite exchange symmetry and its passage to deterministic limiting values | Satisfied |
| §5.2, lines 1553–1608 | (81)–(83) | Two-sided tails, positive definite first-feature Gram at `rho=0`, positive nonaffinity infima | Satisfied |
| §5.3, lines 1610–1708 | (84)–(90) | Positive progress, nonvanishing residual, every individual positive-time hidden speed and all parameter speeds | Satisfied |
| §5.4, lines 1710–1806 | (91)–(95) | Correct reused-transpose initial law and positivity of its Gaussian variances | Satisfied |
| §5.5, lines 1808–1938 | (96)–(107) | Strong initial limits, both kernel contributions, antiparallel factors, physical-time quadratic coefficient | Satisfied |
| §5.6, lines 1940–1977 | Final scope/provenance | No unsupported extension or dependence on the named snapshots | Satisfied |

## 1. Model, normalization, and exact identities

### 1.1 Initialization and the optimization metric

The entries in (2) have variances `1/d`, `1/n`, and `n^{-2}` respectively; the readout standard deviation is therefore `n^{-1}`. The prediction contains the displayed factor `1/n` and no additional implicit readout rescaling.

Differentiating the loss **sum** gives the three Euclidean gradients stated at lines 80–83. Applying the inverse blocks of (7), namely `n/d`, `1`, and `n`, gives exactly the three directions in (6). In particular:

- The first direction is `-(2/d) sum_a r_a delta_a^(1) x_a^T`.
- The second direction is `-(2/n) sum_a r_a delta_a^(2) (h_a^(1))^T`.
- The readout direction is `-2 sum_a r_a h_a^(2)`.

Thus division by `eta_n` gives the specified gradient flow in the physical variable `t=k eta_n`. The theorem would be a different statement for ordinary Euclidean descent on all three arrays; the document explicitly prevents that interpretation.

### 1.2 Empirical spaces, ranks, and quadratic metrics

Both finite neuron spaces have inner product `v^T w/n`. Consequently the adjoint of ordinary multiplication by the middle matrix is its actual transpose, and the operator norm is its usual Euclidean operator norm. The rank operator `v tensor h` has matrix `v h^T/n`. Its Hilbert–Schmidt norm equals its ordinary Frobenius norm and equals `||v||_n ||h||_n`, where `||v||_n=||v||_ell2/sqrt(n)`.

This verifies all factors in (9), the middle update, and both middle-layer kernel factors. It also explains why the initial middle matrix itself is not assigned a limiting Hilbert–Schmidt norm. Only its learned increment is measured in that norm.

Differentiation of the prediction gives the three blocks (12). Their Gram representations are valid, including the first block with input vectors `x_a/sqrt(d)`. Thus each block is positive semidefinite, not merely their sum.

For reference, the metric-to-limit correspondence is:

| Finite quantity | Population quantity |
| --- | --- |
| `(d/n) ||dot W_n^(1)||_F^2` | `d E_1 |dot W^(1)|^2`, equal to the sum of squared independent first-preactivation speeds |
| `||dot W_n^(2)||_F^2` | `||dot W^(2)||_HS^2` |
| `(1/n) ||dot W_n^(3)||_ell2^2` | `||dot W^(3)||_L2^2` |
| `W_n^(2) h` | `W^(2) h`, with no additional empirical factor in the action |
| `v h^T/n` | `v tensor h` |

The same correspondences apply to parameter increments. No norm in this table silently changes between a speed and an increment.

## 2. Deterministic global wellposedness and restart

### 2.1 The transformation works at both stated geometries

For `F(z)=z+z^3/3`, `F'(z)=1+z^2=1/phi'(z)`. Therefore `F^{-1}` is globally 1-Lipschitz, and the derivative of `phi(F^{-1}(u))` is `phi'(F^{-1}(u))^2`, bounded by one. The initial transformed field is in L2: the Gaussian moment calculation gives `E F(G)^2=14/3`.

At `rho=0`, the first-preactivation equation is diagonal in the sample index, so multiplication by `F'` gives exactly `dot U_a=c_a Q_a^(1)`. No ratio of two different sample gates remains.

At `rho=-1`, opposite inputs and odd activations give opposite forward fields and predictions, while even derivatives give equal backward fields, including for the actual nonzero finite readout. Hence the reduced control is `c_1-c_2=-4r_1`. The one-field equation and the rank and readout equations all have this same reduced control. The loss sum is responsible for the factor four.

Equation (18) retains the orthogonal component of the initial first row. At orthogonal inputs there are two independent projection coordinates; at antiparallel inputs there is one. It follows exactly that `d E|dot W^(1)|^2` counts the independent first-preactivation motions once each. This avoids doubling the antiparallel first-matrix energy.

### 2.2 The L2 stability argument closes without an unavailable multiplier estimate

I checked every inequality in (20). The first two follow from the Lipschitz scalar maps and the operator bound. The delta estimate uses a bounded readout to control the difference of gates. The reverse estimate is obtained by adding and subtracting one operator action. The rank estimate uses two rank-one differences and the norm identity (9). The prediction estimate is Cauchy–Schwarz with bounded features and readout.

For example, the reverse estimate has exactly the necessary terms

`a_0' e_3 + M(a_0')^2 e_a + M(a_0' B+1)e_W`.

The extra `M e_W` is the changed-adjoint contribution; it is present. The rank estimate likewise contains both the changed delta and the changed first feature.

The transformed first drift uses `Q`, not `phi'(Z)Q`. This is the decisive point: local Lipschitz continuity of this vector field requires no L-infinity bound on `Q` and no bounded action of the middle operator on Lp for `p != 2`.

The clipping construction addresses the fact that an L-infinity ball is not open in L2. With the readout clipped in predictions and deltas, the vector field is locally Lipschitz on an actual Banach-space ball. The stated contraction argument supplies existence and uniqueness there. The readout integral subsequently keeps the solution inside the unclipped region for a sufficiently short interval. For integrable prescribed controls, using their accumulated absolute integral in the contraction estimate is valid.

Equation (22) is the correct Gronwall estimate for controlled trajectories. For physical feedback the prediction inequality in (20) controls the difference of the controls themselves, yielding ordinary local Lipschitz stability. When the initial operators differ, separating their operator-norm difference from the Hilbert–Schmidt difference of the learned increments is sufficient; an unjustified initial Hilbert–Schmidt comparison is not made.

### 2.3 Global extension is established before the probabilistic limit

The bounds (23) follow directly from the readout and rank integrals. In particular, integrating `B(b_2+Bv)` against action gives

`B b_2 S + (B^2/2) S^2`.

The transformed first displacement is bounded by integrating the product of the operator bound and readout L2 bound against the same action. All these bounds are independent of the pointwise size of the first preactivation.

A finite endpoint with finite action is not a blow-up obstruction: the state derivative has an integrable scalar majorant in the relevant Banach norm, so the state converges there; the readout also converges in L-infinity. The local construction applies at that endpoint.

For physical feedback, the chain rule used to establish (24) is valid along the actual L2 curves. The proof at lines 400–408 uses scalar difference quotients and dominated convergence against a fixed L2 direction; it does not assert false general Fréchet differentiability of the composition map on L2.

Using the actual adjoint in the prediction derivative gives

`dot f=-2Kr`, and `dot L=-4 r^T K r`.

The latter equals the negative sum of squared parameter speeds in the stated metric. This verifies both the signs and the factor four. Consequently the residual norm stays at most `R_0`, and the total action is at most `2 sqrt(2) R_0 t`. In the antiparallel reduction the same bound follows from `|r_1|=R/sqrt(2)` and the reduced control `-4r_1`.

Thus the action is finite on every finite horizon, so the local solution extends globally in physical time. For zero population readout the explicit consequences `S<=4t`, `||W^(3)||_infty<=4Bt`, and `||W^(2)||_op<=8+8B^2t^2` are correct.

### 2.4 Uniqueness covers original L2 solutions and reached states

The original-equation uniqueness argument is substantive and sufficient. A solution of the original integral equations has continuous residuals and a locally bounded readout from its readout integral. Its first-preactivation equation has the scalar form `dot Z=c phi'(Z)Q`, with `cQ` integrable in L2. Fubini gives absolutely continuous scalar trajectories almost everywhere. Applying the scalar chain rule for `F` along each such trajectory yields (27).

Although `F` is not a globally Lipschitz L2 composition map, this step is legitimate: each scalar absolutely continuous trajectory has bounded range on its compact time interval, and the resulting right-hand side of (27) is an L2 integral. It therefore proves that the original solution belongs to the transformed class, rather than assuming that membership.

The hypotheses are preserved at every reached state. The complete initial operator plus learned increment, the current readout, the current first fields, and the unchanged orthogonal first-row component are all retained. At antiparallel inputs the sum of the two original first derivatives is zero, preserving the required invariant relation. Local uniqueness and concatenation consequently prove the claimed autonomous restart. No fresh Gaussian sampling or reconstruction from only marginal field laws is used at restart.

## 3. Exact raw-GD comparison and all rates

### 3.1 Euler control does not assume discrete loss monotonicity

The bounded transformed drift and its Lipschitz constant give local truncation error `O_T(h^2)` in (28). Iterating the displayed recurrence yields (29), including the accumulated defects.

The first-exit argument is valid for the untruncated iterates. Before a candidate residual exit, the accumulated discrete action is bounded. The readout and rank updates provide state bounds through that candidate update, with the stated one-half coefficient from the exact discrete double-sum identity. The comparison then puts the candidate residual within one-half of the exact residual, contradicting an exit beyond `R_0+1`. This is not an appeal to an unproved descent property of raw GD.

### 3.2 The raw-to-transformed defect is exact

For a raw first-coordinate increment `v=eta c phi'(z)q`, expanding the cubic gives exactly

`F(z+v)-F(z)=eta c q + eta^2 c^2 z phi'(z)^2 q^2 + (eta^3/3)c^3 phi'(z)^3 q^3`.

On the stopped bounds, `||q||_n<=C_T` and `||q||_infty<=sqrt(n) C_T`. Thus

`||q^2||_n<=sqrt(n) C_T^2`, and `||q^3||_n<=n C_T^3`.

Together with `|z|phi'(z)^2<=1`, these imply the stated one-step defect `O_T(eta^2 sqrt(n)+eta^3 n)`. Accumulating over `O_T(eta^{-1})` steps gives

`O_T(eta sqrt(n)+eta^2 n)=O_T(n^{-3/2})`

when `eta=n^{-2}`. The ordinary Euler error `O_T(n^{-2})` is smaller. The other two parameter coordinates have no transformation defect. Equation (31) therefore has the correct scale.

The polynomial discrepancy between raw linear interpolation and linear interpolation of its transformed endpoints is also exact. Differentiating it divides its scale by `eta`, giving `O_T(eta sqrt(n)+eta^2 n)=O_T(n^{-3/2})` for transformed velocities. Its derivative uses the stipulated one-sided conventions at nodes.

### 3.3 Products and original velocities

The finite product bound (32) legitimately loses a factor `sqrt(n)` and no more. Combining it with the transformed comparison yields `O_T(n^{-1})` for the first original preactivation and activation velocities. Applying the product rule (33), the bounded middle operator, and the same finite multiplier estimate yields the same rate for the second-layer original velocities. The final activation product uses an L-infinity estimate for a finite vector whose normalized L2 norm is bounded; this again costs only `sqrt(n)` against the `n^{-3/2}` state error.

The verified rates, on events whose probability tends to one, are:

| Compared raw-GD and same-initialization finite-GF quantity | Uniform finite-horizon error |
| --- | --- |
| Transformed state and transformed velocities | `O_T(n^{-3/2})` |
| Middle-parameter and readout velocities | `O_T(n^{-3/2})` |
| Original hidden preactivation and activation velocities | `O_T(n^{-1})` |
| First kernel block | `O_T(n^{-1})` |
| Second and third kernel blocks | `O_T(n^{-3/2})` |

The squared-norm inequality at lines 527–529 transfers these errors to speeds and energies because the normalized norms are bounded on the same event. The proof correctly reserves the exact energy identity for GF.

### 3.4 Probability bounds and the actual readout

The `1/4`-net has at most `9^n` points, and approximation of both arguments of the bilinear form gives the factor two in the norm bound. A fixed bilinear form has variance `1/n`, so the union bound gives exactly (34), with exponent `2n log 9 - n t^2/8`. At threshold eight this probability tends to zero exponentially.

The readout union bounds (35) follow from its standard deviation `1/n`. In particular the thresholds one and `sqrt(6 log n)/n` give the probabilities stated. These events make the constants in the raw comparison uniform in width. The theorem does not require deterministic control on their complements.

## 4. Finite Gaussian programs and the canonical operator

### 4.1 Causality and formal source derivatives

In (37)–(40), both forward answers precede the reverse answers at each node, and updates follow all those answers. A current forward response uses only earlier reverse inputs. A current reverse response may involve the current forward source, as recorded in the last line of (40). The readout derivative through all earlier activations is also present.

All source covariances are the uncentered second moments of the corresponding query inputs. They retain sample, time, and cross-run covariances. The formal derivatives hold selected scalar quantities fixed. This convention is justified later by the deterministic-coefficient comparison and by actual forcing; it is not used as an unsupported differentiation of empirical feedback.

At `rho=-1`, the unforced mesh preserves the invariant state. The off-invariant transformed program used for forcing is expressly an auxiliary program. Its use does not assert an incorrect equivalence to raw GF away from that invariant state.

### 4.2 Fixed-program moment estimates

The readout recursion (41) follows from bounded arctangent features, including under the specified query perturbations. It permits a smooth bounded extension of the readout-times-gate map that is globally Lipschitz without changing any program value. Storing the cubic Gaussian coordinate as part of the iid root tuple is legitimate: its moments are finite and it is not differentiated as an underlying Gaussian coordinate.

I checked the normalization in the graph derivative estimates (42). Differentiating `W x` with respect to the unscaled Gaussian entries produces `W partial x + n^{-1/2} v x`; its second term is bounded by the normalized norm of `x` times `||v||_F`. Differentiating an empirical contraction produces the `n^{-1/2}` factor stated. This factor cancels the ordinary `sqrt(n)` vector norm in scalar-times-vector instructions. Fixed graph depth therefore gives a polynomial bound independent of width.

The rotation proof of (43) is valid: at each rotation angle the Gaussian velocity is independent of the rotated Gaussian position, and conditional integration of its scalar product with the gradient gives the one-dimensional Gaussian moment. Integral Hölder and then conditional Jensen give the displayed constant.

The conditional-mean argument (44) is also needed and is supplied. Exchange of two neurons in the output population preserves the Gaussian matrix law; the stored-root Lipschitz bound controls the difference of their conditional means. Averaging over the other neuron and using the normalized norm bound controls the mean of a single coordinate. This avoids treating the cubic stored roots as Gaussian inputs to (43). Hölder and their all-order moments then prove (45), including the stated uniformity over query-noise sizes in `[0,1]`.

### 4.3 Adaptive Gaussian conditioning and response terms

The conditional mean in (46) satisfies both `WV=Y` and `W^T J=P`. For the second constraint, compatibility `J^T Y=P^T V` supplies the component along the old forward-input span, and the second term supplies its orthogonal complement. The residual is exactly `P_{J^perp} tilde W P_{V^perp}`. Vectorized Gaussian orthogonal projection proves the formula. Adaptivity adds no extra constraint because each new query is measurable from the already conditioned transcript.

The new-answer formula has innovation standard deviation `||h_perp||_ell2/sqrt(n)`. In (47), the diagonal entries of a rank-at-most-j orthogonal projection lie in `[0,1]` and sum to at most j, so its normalized p-moment contribution is `O(j/n)` for each fixed p at least two. Its removal is justified by (45); smaller p follow from L2.

After removal, conditional independent Gaussian coordinates give the conditional variance bound (48). Regression coefficients are controlled by convergence to nonsingular limiting Grams. For unbounded inputs, the innovation variance is tight by its normalized L2 bound and the moment estimates. The continuous polynomial-growth tests are then handled by compact truncation and (49). This establishes the nonsingular empirical induction, rather than merely identifying a candidate covariance.

The calculation leading to (50) includes the required reused-matrix response. After projecting `h` off old forward inputs, the old reverse-answer inner products reduce to `E[zeta h_perp]`. Gaussian integration by parts gives (51); substitution into the regression coefficient cancels the old-forward projection responses. The source covariance is the **full input Gram**, not a Gram reduced by a response covariance. The reverse orientation uses the identical matrix and the same argument. This is consistent with the separate explicit initial return law in §5.4.

### 4.4 Singular Grams and empirical feedback

Independent query-input noise makes the new limiting Schur complement at least `epsilon^2`, including for a query that was exactly zero or redundant. It is crucial that the noise is fresh before that query. The finite Gram is nonsingular almost surely once width exceeds the number of prior queries.

The finite perturbed and unperturbed graphs are coupled using the same original matrix and roots. Their RMS difference is `epsilon` times a polynomially controlled quantity. Interpolation (53), using all-order moments from (45), extends this to every finite empirical Lp norm in probability. The polynomial-test passage follows from the explicit truncation estimate.

On the scalar side, the source-response rule contains no inverse covariance. The causal expressions and their formal first derivatives depend continuously on the selected coefficients, with the required domination for a fixed finite graph. Continuity of finite-dimensional positive semidefinite square roots permits a common Gaussian coupling even at rank drops. Dominated convergence therefore establishes both coordinate-moment and expected-derivative continuity as noise vanishes.

The order of limits is legitimate: positive noise gives the width theorem; finite uniform approximation and scalar continuity then allow noise to vanish. Formal zero-variance or redundant slots are retained. A null-direction ambiguity changes no contracted response because the corresponding linear combination of reverse inputs has zero L2 norm. There is no unsupported use of an inverse singular Gram.

For feedback, the deterministic-coefficient program is selected in causal order from the already identified laws. Its finitely many empirical contraction errors vanish. The same-matrix finite comparison controls the actual-feedback program by those errors on bounded graph-norm events; moment bounds remove the events' complements and upgrade RMS control. This supplies the missing justification that would otherwise be needed for freezing scalar feedback in formal derivatives.

The finite-dimensional Wasserstein conclusion is proved by a concrete coupling: match mass in small bounded cells, couple unmatched bounded mass, and use higher moments to control tails. The result is convergence in probability, in each fixed finite order.

### 4.5 The common-space operator and its adjoint

The enumeration includes the relevant finite meshes, both orientations applied to generated nodes, constants, rational combinations, and a dense collection of bounded smooth cylinder functions. Every finite subcollection is covered by the finite-program result, including joint programs sharing the same matrix.

Equation (55) is inherited from exact finite bilinear identities and the high-probability operator bound. Because the limiting Gram entries are deterministic, a strict violation of either norm inequality or the adjoint identity would contradict finite convergence. Zero-norm input relations therefore give zero-norm output relations, so these are well-defined linear maps.

The cylinder approximation argument establishes density in the generated L2 spaces; it does not assume that the trajectory fields alone are dense. Extending both maps by their bounds gives a bounded operator and its actual Hilbert adjoint, on separate neuron spaces. The norm bound eight is sufficient throughout; no sharp random-matrix spectral theorem is required.

The countable source construction is consistent and explicit. Adding unused queries leaves earlier marginal laws unchanged because they are already full-sequence limits of the same finite observables. This proves the stated canonicity under enumeration. The construction is not a continuum kernel with independent entries.

The common operator then supports the deterministic flow of §2. Each enumerated scalar mesh is an Euler scheme for that same operator and adjoint, and (56) follows from the deterministic comparison. Thus the population flow is not selected by extracting a width subsequence, and the operator is not resampled as the mesh changes.

## 5. Global response bounds and Gaussian remainders

### 5.1 Fresh-root forcing establishes the expected derivatives actually used

This is an essential global step, and I checked it independently of the subsequent nontriviality deductions.

Equation (41) gives (57) uniformly over the number of mesh steps on a fixed horizon. The total absolute sum of the controls is consequently bounded. The learned ranks bound the operators, and the stepwise stability factor is `1+C_T h_k`. These estimates hold for the auxiliary off-invariant two-sample program as well, since the transformed update is linear in its reverse answers and `||C||<=2`.

Inserting `epsilon e` into a complete reverse answer changes the immediately subsequent first-state update by `O_T(h_s |epsilon| ||e||_n)`. The other state updates at that node do not directly use that reverse answer. Propagating the later stability factors proves (58).

Inserting noise into a complete forward answer changes the current gate, delta, prediction, and residual by `O_T(|epsilon| ||e||_n)`; the transpose bounds the current reverse-answer change. Every changed state update carries `h_s`, so all later delta discrepancies have the scale in (59). At the current node, only the designated sample delta has a direct change, bounded by `M_T |epsilon| ||e||_n`.

For a fixed mesh and fixed nonzero noise, the joint forced/unforced finite-program theorem applies. In the local scalar expression, the fresh root appears through the designated source slot plus `epsilon e`. All selected covariances, responses, and feedback values are deterministic with respect to this local coordinate; the source family is independent of that root. Hence the chain rule and one-dimensional Gaussian integration by parts give exactly (60).

Passing the finite Cauchy–Schwarz bound to this joint limit and dividing by `|epsilon|` bounds the expected slot derivative. Only then is noise sent to zero, using the fixed-mesh derivative continuity already proved. This proves (61), including zero-variance initial slots and the diagonal current-node beta term. It does not infer derivatives transverse to a singular Gaussian support from an unforced law alone.

Adding the learned rank coefficients gives (62): past coefficients are `O_T(h_s)` and the only possible current coefficient is uniformly bounded. Their row sums remain bounded as the mesh is refined. Feedback changes were included in the finite estimates; holding selected scalar values fixed in the later local derivative is therefore justified.

### 5.2 Remainders and passage to continuous time

The response-row bounds multiply bounded first features or bounded second deltas. Thus (63) gives genuinely essentially bounded remainders, not merely L2 remainders. The transformed first field is its cubic Gaussian root plus a Gaussian linear combination of reverse sources and a bounded remainder, as in (64). The Gaussian part is independent of the first-row roots; it need not be independent of its bounded remainder.

The cross-program covariance rule makes the source assignments L2 isometries (65). State convergence therefore makes the sources converge on the existing common space. Subtracting them from the convergent fields preserves the essential remainder bounds. Riemann sums converge in L2, and the limits of Gaussian linear combinations remain Gaussian; independence from the roots passes through joint characteristic functions.

The resulting (66) holds at each deterministic finite time. The stated measurable representatives and Fubini argument suffice for the time integrals. A single pointwise exceptional set valid for every real time is not needed for the theorem's distributional tail and positivity arguments.

This closes the global representation argument. No assumption about a bounded Lp action of the initial operator, and no unproved long-time response bootstrap, has entered it.

## 6. Every claimed mode of convergence

### 6.1 Product estimates and path-supremum moments

Equation (67) is the correct replacement for a false joint-L2 Lipschitz assertion about a gate times an unbounded field. Splitting at `|b|=R` gives the displayed terms. Its two-product variant and its fixed-field specialization justify the population product continuity used throughout.

For finite uniform integrability, the operator clipping (68) is used only in moment estimates. Its operator-norm Lipschitz constant at most two is valid, including when only one argument is outside the ball. A change in unscaled Gaussian entries therefore changes the clipped operator by at most `2||E||_F/sqrt(n)`.

The deterministic stability estimate converts this to a normalized field change. Multiplying by `sqrt(n)` to control an individual coordinate cancels this factor, yielding a dimension-independent Lipschitz constant for each coordinate's path supremum. The same reasoning applies to stored-root changes.

The derivative estimates behind (70) are sufficient for every base field in (69). In particular (71) differentiates the second delta and the first reverse field using bounded readout/gate multipliers and bounded L2 operator actions. It never requires differentiating `delta^(1)` with an unbounded multiplier. Pointwise absolutely continuous representatives follow from the L2 integrals and Fubini.

The conditional Gaussian rotation inequality and the root-permutation conditional-mean argument therefore apply to these supremum functionals. This proves the all-order bound (72), uniformly over the relevant meshes. Clipping the actual initial readout to `[-1,1]` for this estimate gives uniformly bounded iid roots; (35) removes that clipping with probability tending to one. These are moment-estimate devices, not changes to the asserted dynamics.

### 6.2 Fixed-time fields and admissible probes

For a fixed mesh, §3 identifies all base fields and their contractions. Products such as the first delta are continuous polynomial-growth tests of known tuples. To query the matrix on an unbounded velocity input, smoothly truncating `Q^(1)` makes the query a permitted Lipschitz instruction. The L2 input error vanishes by (45) or the time-uniform bound (72), and either operator orientation multiplies that error by a bounded factor. This establishes the promised unbounded velocity probes rather than assuming them admissible.

The fixed-time width/time passage has the correct triangle order: choose a mesh so that both deterministic finite-flow/mesh and population-flow/mesh discrepancies are small, then let width tend to infinity for that fixed program. The finite same-neuron coupling and the population common-space coupling supply the respective Wasserstein bounds. No width subsequence is extracted.

The actual finite readout is restored by a same-initial-matrices comparison with the auxiliary zero-readout flow. Its normalized L2 size tends to zero, and its supremum is bounded on events tending to probability one. Stability and product integrability transfer the observables. The zero population readout is thus the proved limit of the actual initialization.

The general probe scope is limited to the fixed programs and L2 approximations explicitly defined in §1.3. That restriction rules out amplification of the vanishing readout or arbitrary width-dependent directions. The proof covers both the forward and reverse actions within this scope.

### 6.3 Path laws and uniform scalar outputs

The polygonal approximation estimate (74) follows from Cauchy–Schwarz on each observation interval and is sufficient after averaging over neurons. The base fields have the required integrated squared derivatives by (70)–(71). Thus fixed-grid convergence, followed by grid refinement, gives joint Wasserstein-2 path convergence with the supremum metric.

For the first delta, continuous multiplication on scalar continuous-path space and the domination by the path supremum of `Q^(1)` justify the extension. Higher supremum moments in (72) upgrade the joint path convergence to every fixed finite Wasserstein order. The full first row follows from (18) and the unchanged Gaussian orthogonal component.

Predictions and kernel blocks two and three have uniform state-continuity estimates. Block one uses (67) with the uniformly integrable squared path suprema of `Q^(1)`. At each fixed comparison mesh there are only finitely many endpoint contractions, and the uniform state modulus controls the intervening times. This proves uniform-in-time convergence in probability of predictions, loss, and all three kernel blocks.

### 6.4 Original velocities, including the final second-layer gate

The transformed vector field is controlled by (20). The first original preactivation and activation velocities require (67) and the `Q^(1)` supremum-tail control. Rank and readout velocities are Lipschitz in the state. Subtracting the operator and input separately in the second-preactivation identity of (73) then gives its uniform L2 comparison.

The finitely many left-node comparison velocities suffice: replacing an interpolated comparison state by its left node has vanishing error by the transformed state modulus and the same product estimates. The explicit quantifiers at lines 1419–1434 correctly state a width-limsup, mesh-to-zero comparison in probability, uniformly in time. They do not claim a canonical labeling of finite neurons by population points.

The second activation requires a further step, and it is supplied. For a fixed mesh, Wasserstein-2 convergence of its finitely many second-preactivation velocity evaluations gives uniform integrability of their squares in probability. Inequality (75) transfers this property to the L2-close continuous-flow velocities. Choosing the fixed mesh first and the tail cutoff second is sufficient; no uniform high-moment estimate for arbitrary operator images is required. The population version follows from compactness of a continuous L2 velocity curve and the same inequality. Equation (67) then justifies multiplication by the final second-layer gate.

These comparisons give fixed-time joint Wasserstein-2 velocity convergence, convergence of squared normalized velocity norms uniformly in time in probability, and the specified integrated mean-square comparisons. Multiplying the squared uniform comparison bound by `T` gives the integrated bound. This is an in-probability statement about the finite comparison errors, not an unasserted convergence in expectation over initialization.

### 6.5 Parameter speeds, energies, increments, and transfer to raw GD

The first speed uses the independent-coordinate metric identity (18). The middle squared speed is exactly the contraction formula (76), with the factor four and both empirical normalizations. The readout speed is its normalized field norm. Their contractions converge, so their uniform quadratic limits and finite-horizon integrals follow.

For increments, the first and readout coordinates follow from the field/path limits. The middle increment is approximated by a finite sum of ranks. Its integrand has a width-independent Hilbert–Schmidt continuity modulus by (20), and the squared norm of each finite sum is a cross-time contraction already covered by the joint observation laws. The initial middle operator's divergent Frobenius scale is never included.

Finally, (31)–(33) transfer the GF statements to the stipulated raw parameter interpolation. For base fields, the normalized uniform error `O_T(n^{-3/2})` implies maximal same-neuron path error `O_T(n^{-1})`. For the first delta, the `O_T(n^{-1})` normalized product error still gives a vanishing maximal coordinate error after multiplication by `sqrt(n)`. Thus every fixed path Wasserstein order transfers without requiring extra raw-GD moment bounds on rare bad events. Probe limits transfer through their fixed Lipschitz instructions and stated L2 approximations.

The convergence assertions are therefore mutually consistent:

| Observable | Proved mode |
| --- | --- |
| Listed joint same-neuron field paths, separately in each population | Every fixed finite Wasserstein order on continuous-path space, in probability |
| Finite time/field tuples and continuous polynomial-growth tests | Joint convergence in probability, with the needed moments |
| Predictions, loss, and three kernel blocks | Uniform in physical time on each fixed finite horizon, in probability |
| Fixed admissible probe collections in either orientation | Joint Wasserstein-2 field-law convergence |
| Listed scalar-neuron velocities | Fixed-time joint Wasserstein-2 convergence and the stated integrated mean-square comparisons |
| Squared normalized velocity norms and parameter speeds | Uniform in time in probability, with convergent finite-horizon integrals |
| Parameter increment sizes | Convergence in the corresponding quadratic metrics, middle increment only |

There is no asserted continuous-path law for discontinuous mesh velocities, no cross-population artificial pairing, and no dimension-changing operator-norm convergence.

## 7. Nonaffinity, strict motion, and the full-kernel expansion

### 7.1 Exchange symmetry is justified at finite width

The reflection (77) swaps the two equal-norm inputs, including the antiparallel case. Under (78), forward fields swap samples while the readout, predictions, residuals, and backward fields transform with the signs in (79). The opposite labels are essential for the residual identity.

The transformation preserves both loss and metric and commutes with the displayed finite updates and GF. Gaussian first-row isotropy and independent symmetric readout initialization preserve its law. Passing this finite law symmetry to deterministic limiting scalar values proves `f_2=-f_1` and equal sample speed norms. The orthogonal case is only a law symmetry; the proof does not incorrectly promote it to a finite pathwise identity. The antiparallel case has the stronger exact identities from its geometry.

### 7.2 All-time tails and positive nonaffinity infima

In (81), the Gaussian integral is independent of the initial first row and the error is bounded. A bounded event for that integral of positive probability can therefore be combined with either sufficiently extreme Gaussian root tail. This proves both unbounded tails for each first preactivation at any fixed finite time.

For orthogonal inputs, independent first Gaussian coordinates permit all four extreme sign patterns simultaneously with that bounded-integral event. Hence the first-feature support approaches all four corners. A linear relation holding almost surely must vanish at the two independent corners used in the proof, so the uncentered first-feature Gram is positive definite. At antiparallel inputs it is correctly treated as rank one, with positive reduced feature norm.

The second forward Gaussian source has variance equal to the corresponding first-feature squared norm and is therefore nondegenerate. A bounded remainder cannot eliminate either Gaussian tail. No independence of that source from its remainder is needed.

For an L2 variable with these tails, the span of `1,Z` is closed; the determinant of its two-by-two Gram is its positive variance. If the nonaffinity infimum were zero, an affine representation would be attained. Boundedness of arctangent and an unbounded tail force its slope to vanish, while strict monotonicity rules out a constant representation. This proves the strictly positive infimum, not merely failure of a particular affine fit.

### 7.3 All individual positive-time speeds

With `kappa=y^T K y/4`, symmetry gives `r=(f_1-1)y`. Multiplication of the prediction equation by `y^T/2` yields `dot f_1=4(1-f_1)kappa`, exactly as in (85). The kernel bounds keep its integral finite on finite horizons, so the exponential residual formula is valid and gives `f_1<1`.

The initial readout block has a nonzero contrast: independent nonconstant centered second features at orthogonal inputs, and opposite nonzero features at antiparallel inputs. Thus `kappa(0)>0`. Continuity gives initial positive progress, and nonnegativity of kappa preserves it, proving `0<f_1(t)<1` for every positive time.

The nonzero prediction forces the readout to be nonzero. Strictly positive gates then make each second delta nonzero. Its reverse Gaussian source has positive variance, so its bounded-remainder representation makes each `Q_a^(1)` nonzero. The nonvanishing scalar control and positive gates give every first preactivation and activation speed, and therefore the first-matrix speed, strictly positive.

At orthogonal inputs, applying the positive definite first-feature Gram pointwise to `(y_a delta_a^(2))_a` proves (89) and strict middle-matrix speed. At antiparallel inputs the single reduced rank is nonzero.

The identity (90) is the correct way to rule out total cancellation in second-preactivation motion. Its rank part is the squared Hilbert–Schmidt speed, and its first-layer part becomes the sum of independent first-coordinate squared speeds after using the actual adjoint. In the antiparallel case the difference of controls gives precisely one such squared norm. Its right side is positive; equal sample speed norms from (80) then imply that each second-preactivation speed is positive. Positive gates give each second activation speed.

If the readout speed vanished, the second-feature contrast would vanish, contradicting the already positive prediction. This proves the remaining parameter speed. Continuity gives positive energies on every nonempty positive-time interval. The zero-time hidden speeds vanish because the population readout and backward fields are zero.

### 7.4 The initial reused-transpose law

In (94), the finite regression factor is `H Gamma_n^{-1}(Z^T delta_hat/n)`. This has the right normalization because `Gamma_n=H^T H/n`. The residual transpose term has conditional covariance `Sigma_n=delta_hat^T delta_hat/n`, projected off the first-feature span. It is the full delta second moment, not a conditional residual variance with the signal subtracted.

Conditional row averaging gives the limiting Grams and cross-moments. The reduced limiting Gram is invertible in both geometries. The cross-moment involving the unbounded Gaussian forward coordinate is controlled by Gaussian moments; the document expressly does not claim that coordinate is bounded. The finite-rank projection error vanishes by (47). These steps establish (92)–(93), jointly with the initial first row, inside the canonical space.

At orthogonal inputs the common contrast factor is nonzero off the diagonal, and a vanishing linear combination of the two gate factors on full Gaussian support would force both coefficients to be zero. Thus its covariance is positive definite. The antiparallel scalar variance is also positive. Conditional Gaussian variance given the first row then proves (95), even after multiplication by the strictly positive first gate.

### 7.5 Every coefficient in the kernel expansion

The temporary feature time satisfies `ds/dt=4(1-f_1)>0` and `s(t)=4t+o(t)`. It is used only for the local calculation; the raw-GD clock remains physical time. Dividing the physical equations by this factor gives the one-half coefficients in (97) at orthogonal inputs and coefficient one in the antiparallel reduction.

The readout integral gives the strong limit `W^(3)(s)/s -> W_hat^(3)`. Bounded gates and operator-norm continuity then give both strong limits (98). The product arguments use the fixed-field bounded-multiplier lemma, so no unproved second Fréchet derivative on L2 is needed.

I checked the rank and first-layer contributions to each second-preactivation leading velocity in (99). The initial Gram `mI` yields the term `y_a m delta_hat_a/2`; the other term is `y_a W_0(phi'(G_a)^2 Q_hat_a)/2`. Thus (100) and the one-quarter coefficient in (101) are correct. Moving through the actual adjoint gives (102) with its one-half factor.

For antiparallel inputs, the reduced first and middle leading velocities have coefficient one, and `d_*` is the sum in (103), with no duplication of the opposite sample. In both geometries `d_*>0` by the verified initial return law and the positive delta norms.

The hidden label-direction kernel equals the sum of squared feature-time hidden-parameter speeds. It therefore contributes `d_* s^2+o(s^2)`. Differentiating the readout contrast norm in (104) gives (105). Dividing by s, the orthogonal identity (102) sums to `2d_*`; the two equal antiparallel contributions give the same result. Integration adds another `d_* s^2+o(s^2)` from the readout block. Hence

`kappa(s)=kappa(0)+2d_* s^2+o(s^2)`.

Returning to physical time multiplies the quadratic coefficient by sixteen, so

`kappa(t)=kappa(0)+32d_* t^2+o(t^2)`, with `d_*>0`.

The first-order change is zero, and both quadratic contributions are positive. This proves that the **full** kernel changes near zero; it does not merely show that a hidden block changes while leaving open cancellation by the readout block.

## 8. External-result and hidden-assumption audit

No essential nonclassic theorem is imported without its proof. The items that could otherwise have been substantive external dependencies are established internally:

- The Gaussian concentration/moment inequality has its rotation proof in §3.2.
- Adaptive Gaussian matrix conditioning and finite-rank projection removal are proved in §3.3.
- The response/source law is derived by explicit Gaussian integration by parts and regression cancellation in §3.3.
- Singular query Grams and actual empirical feedback are handled in §3.4, rather than delegated to a general program theorem.
- The common bounded operator and actual adjoint are constructed in §3.5 from finite identities and density.
- Global expected-response bounds are proved by actual fresh-root programs in §3.6.
- The special initial reverse law is additionally proved directly in §5.4.

The remaining background facts are classical elementary tools: completeness of the relevant Banach and L2 spaces, finite-dimensional spectral diagonalization, Gaussian orthogonal projection, scalar Gaussian integration by parts, Cauchy–Schwarz/Hölder/Jensen, Markov/Chebyshev, Fubini, dominated convergence, and elementary measure approximation. Their relevant conditions are supplied by the bounded gates/readout, fixed-graph moment bounds, continuous L2 curves, and finite-action estimates. The local contraction, Gronwall, chain-rule, square-root continuity, and Wasserstein approximation arguments are spelled out in the document as well.

The adversarial checks that mattered most were whether a singular source support was being differentiated without justification, whether a bounded L2 operator was silently assumed to act on higher Lp spaces, whether discrete loss monotonicity was assumed, whether the antiparallel motion was double-counted, whether field convergence was mistaken for path or velocity convergence, whether the small initial readout was erased from raw GD, and whether the hidden kernel change could cancel in the full kernel. The document addresses each of these points with the arguments reviewed above.

## 9. Optional clarity edits; no required corrections

1. **Line 1211: “uniform in the horizon.”** The formulas consistently use a constant `C_T`, so the supported meaning is “uniform over time on each fixed finite horizon.” That wording would avoid suggesting a bound independent of T. The surrounding equations and the explicit finite-horizon scope make this an editorial ambiguity, not a mathematical gap.

2. **Sample-index conventions in error sums such as (31) and (56).** At `rho=-1`, an error sum over both opposite samples is twice the corresponding one-independent-coordinate error, whereas the exact first-parameter metric counts the independent coordinate once. Both error bounds are correct because their constants absorb this fixed factor. Stating the summation convention there would improve readability. The exact metric and energy identities already use the correct convention, so no scaling correction is needed.

The PASS verdict applies only to the stated `rho=0,-1`, `L=2` theorem. The document itself explains why its transformed L2 argument does not establish an intermediate-angle theorem: the cross-sample gate ratio in the final scope discussion is not a bounded L2 multiplier in general.
