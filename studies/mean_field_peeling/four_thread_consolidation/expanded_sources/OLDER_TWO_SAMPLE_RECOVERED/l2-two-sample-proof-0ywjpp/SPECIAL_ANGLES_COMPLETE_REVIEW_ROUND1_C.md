# Independent adversarial full-document review — Round 1 C

## Verdict and isolation record

**PASS at the stated scope:** two hidden layers, arctangent activations, loss SUM, the parameter metric (7), the physical step and interpolation in (6), and only input correlations 0 and −1. I found no required mathematical correction. The verdict includes the canonical population construction, both matrix orientations, actual Gaussian initialization, exact raw GD, all finite-horizon observable limits, persistent distributional nonaffinity, motion of both hidden layers, and change of the full kernel.

The only mathematical source read was `/tmp/l2-two-sample-proof-0ywjpp/L2_TWO_SAMPLE_SPECIAL_ANGLES_COMPLETE_PROOF.md`. I read all 1,935 lines (91,679 bytes). All line references below refer to that file. Its initial SHA-256 matched the requested value:

`5cd54a6125dfbf4b7d1bc86149760b842d7d2c1f9a44fe73fcf57f5d3d15f12e`

Final source-hash verification: **matched after writing this review**. The source still has SHA-256 `5cd54a6125dfbf4b7d1bc86149760b842d7d2c1f9a44fe73fcf57f5d3d15f12e`, identical to the initial and requested hashes. The source was not edited.

The rigorous-math skill was used procedurally. No other project documents, proofs, reviews, history, provenance snapshots, source agents, agents, experiments, or directory research were used. The four filenames at source lines 1920–1935 were read solely as text inside the permitted document and were not opened. No heavy external theorem was needed to fill an omitted argument; no external mathematical reference was consulted or assumed.

This verdict does not extend to intermediate correlations, other depths, ordinary Euclidean training of the displayed arrays, arbitrary width-dependent probes, operator-norm convergence of differently sized initial matrices, an infinite-time limit, or resetting the operator at restart. Those are outside the stated theorem.

## Required versus optional corrections

**Required corrections: none found.** In particular, I found no missing nondegeneracy assumption, unjustified inverse at the antiparallel rank drop, readout or clock normalization error, unsupported global response estimate, circular uniform integrability, or full-kernel cancellation.

The following are optional exposition improvements, not conditions on the PASS verdict:

1. **Specify the velocity fields explicitly.** At lines 194–197, “Every original hidden-field velocity” could be replaced by “The velocities of each hidden preactivation and activation field.” Equations (33), (73), Section 4.4, and lines 217–219 consistently specify those eight forward-field velocities. This avoids reading the isolated phrase as an additional assertion about time derivatives of every backward field in the preceding tuple list. The backward fields themselves are included in the path-law conclusion.
2. **Make the finite family in the velocity-tail argument explicit.** At lines 1383–1414, define the approximation by evaluating (73) at the left Euler node on each mesh interval. Then (75) applies to a finite collection at every fixed mesh. This follows from the existing comparisons, with no new assumption. A concrete derivation is given below.
3. **Clarify essential bounds and time quantifiers.** At lines 1179–1198, one may say explicitly that the representations hold almost surely at every deterministic finite time, while jointly measurable versions provide the product-almost-everywhere identities needed for integration. This suffices for every asserted law, norm, tail, and integral conclusion. No lower bound uniform over an unbounded time interval is asserted.
4. **Display the scalar reduction in (85).** At lines 1575–1578, multiplying `dot f=-2Kr` by `y^T/2` gives `dot f_1=(1-f_1)y^TKy`. This makes clear that the reduction uses the proved prediction symmetry and does not need an additional assumed kernel symmetry.

## Detailed coverage ledger

This ledger covers the entire document and every displayed equation (1)–(107). “Verified” means the calculation, hypotheses, and downstream use were checked. The sections following the ledger record independent derivations of the main potential failure points.

| Source lines and equations | Obligation checked | Assessment |
|---|---|---|
| 1–35; (1)–(3) | Scope, geometry, dimension restriction, opposite inputs at correlation −1, Gaussian variances, arctangent derivatives and bounds. | Verified. |
| 36–86; (4)–(7) | Forward/backward normalization, Euclidean gradients, inverse parameter metric, exact GD coefficients, and physical clock. | Verified: gradient factors become `2/d`, `2/n`, and `2`. |
| 88–144; (8)–(11) | Separate neuron spaces, actual matrix multiplication and transpose, rank scaling, HS/Frobenius identification, population dynamics. | Verified: a finite rank is `v h^T/n`; no further scaling enters either orientation. |
| 146–229; (12)–(14) | All theorem obligations: kernels, probe scope, joint paths, velocities, energies, increments, nonaffinity, motion, full-kernel change. | Matched to proofs below; optional velocity-wording clarification noted. |
| 233–251; (15) | Global transformed coordinate, inverse derivatives and Lipschitz bounds, square-integrable initial transformed root. | Verified: `E F(G)^2=14/3`. |
| 253–288; (16)–(18) | Special-angle cancellation, exact opposition, reduced control, row reconstruction, and first-matrix metric. | Verified: antiparallel control is `−4r_1`; only one independent first field is counted. |
| 290–370; (19)–(22) | All subtraction estimates, clipping on an open Banach ball, local contraction, control/feedback stability, differing initial operators. | Verified without a return-field supremum bound or an operator `L^p` bound for `p≠2`. |
| 372–392; (23) | Readout, rank, operator, and transformed-field action bounds; endpoint limit and continuation. | Verified, including the quadratic rank coefficient `1/2`. |
| 394–431; (24)–(26) | Curvewise chain rule, kernel differentiation, positivity, loss dissipation, action bound, global existence. | Verified: total squared parameter speed is `4r^TKr`. |
| 433–448; (27) | Original-class uniqueness and restart from every reached state. | Verified: the scalar chain rule puts every original solution in the transformed class. |
| 450–475; (28)–(29) | Euler defect, discrete stability, first-exit closure, width-independent constants. | Verified through the candidate exit node; no assumed global GD loss monotonicity. |
| 477–504; (30)–(31) | Exact cubic GD defect, accumulation at `η=n^{-2}`, raw interpolation, transformed velocities. | Verified: accumulated RMS defect `O(n^{-3/2})`. |
| 506–525; (32)–(33) | Original first and second velocities, gated products, energy and kernel errors. | Verified: hidden-velocity errors `O(n^{-1})` on the bounded event. |
| 527–547; (34)–(35) | Net cardinality, Gaussian matrix tail, readout maximum tail, high-probability initialization bounds. | Verified, including the exponents and threshold 8. |
| 551–640; (36)–(40) | Causal mesh/source recursion, covariances, learned responses, current reverse term, formal derivative convention. | Verified, including retained zero-variance slots and off-invariant auxiliary use. |
| 642–695; (41)–(42) | Fixed-program readout bound, smooth clipping for graph estimates, stored cubic root, graph derivatives and root dependence. | Verified, including the essential `n^{-1/2}` scalar derivative. |
| 696–740; (43)–(45) | Gaussian fluctuation inequality, conditional means via permutations, all finite coordinate moments. | Verified independently of the limiting law. |
| 742–804; (46)–(49) | Adaptive Gaussian conditioning, both constraints, projection removal, conditional concentration, polynomial-test tails. | Verified: fixed-rank projection empirical `p`th moments vanish. |
| 806–848; (50)–(51) | Source response identification by integration by parts and regression cancellation. | Verified: source covariance is the full input second moment. |
| 850–914; (52)–(53) | Query-noise regularization, positive Schur complements, finite coupling, higher moments, singular scalar continuity. | Verified at zero and redundant queries and in the rank-one geometry. |
| 915–947; (54) | Both learned rank actions, deterministic coefficient selection, empirical-feedback identification, Wasserstein coupling. | Verified. |
| 949–1018; (55) | Countable common space, Gaussian realization, bounded maps on dense spans, null relations, density with atoms, actual adjoint, canonicity. | Verified on the generated spaces. |
| 1020–1033; (56) | One global flow and all mesh programs using the same operator, common-space Euler convergence. | Verified; no width subsequence or new operator at each mesh. |
| 1035–1084; (57)–(59) | Mesh-uniform horizon bounds, actual fresh-root forcing, feedback-inclusive stability, later effects proportional to `h_s`. | Verified in both sample geometries. |
| 1086–1138; (60)–(62) | Root integration by parts, limit order, zero-variance slots, expected response bounds, learned terms and row sums. | Verified; supplies the essential global response estimate. |
| 1140–1161; (63)–(64) | Bounded response remainders, exact Gaussian variances, first-field independent Gaussian forcing, upper tails. | Verified. |
| 1163–1200; (65)–(66) | Cross-program isometries, common-space source limits, bounded remainders, Gaussian integrals and independence, measurability. | Verified for every deterministic finite time and for time integrals. |
| 1204–1220; (67) | Gated-product continuity and square-tail bound. | Verified without false joint `L^2` Lipschitzness of multiplication. |
| 1222–1296; (68)–(72) | Radial clipping, coordinate Lipschitz constants, path-supremum RMS bounds, delta/return derivatives, supremum moments, readout restoration. | Verified; no circular appeal to the width limit. |
| 1298–1354; (73) | Unbounded velocity queries by truncation, both orientations, fixed-mesh/time/width passage, actual Gaussian readout, general probe scope. | Verified. |
| 1356–1381; (74) | Path interpolation, derivative energy bounds, same-neuron Wasserstein path convergence, higher orders, uniform scalar outputs. | Verified. |
| 1383–1418; (75) | Original velocities, second-preactivation RMS comparison, square-tail transfer, final gate, uniform quadratic norms and integrated tests. | Verified; node-frozen approximation makes the finite-family step explicit. |
| 1420–1437; (76) | Parameter speeds, hidden energies, cross-time rank contractions, parameter-increment metrics. | Verified; no HS norm of the initial operator is asserted. |
| 1439–1451 | Transfer to raw GD, including all finite path-Wasserstein orders, velocities, kernels, and energies. | Verified using maximal coordinate errors tending to zero. |
| 1455–1511; (77)–(80) | Reflection, field signs, metric and dynamics equivariance, initialization symmetry, deterministic limiting prediction and norm identities. | Verified; orthogonal symmetry is a law symmetry, not a finite pathwise identity. |
| 1513–1544; (81)–(82) | First-layer two-sided tails, four orthogonal corners, positive-definite feature Gram, rank-one antiparallel alternative. | Verified using independence from the entire first row. |
| 1546–1568; (83), (14) | Positive second-source variance, tails with dependent remainder, closed affine span, positive nonaffinity distance. | Verified for all layers, samples, and finite times including zero. |
| 1570–1602; (84)–(87) | Label scalar equation, finite-time residual positivity, initial contrast kernel, positive progress, nonzero readout. | Verified. |
| 1604–1630; (88)–(89) | Nonzero deltas and return fields, individual first speeds, both hidden parameter speeds. | Verified for every physical `t>0`. |
| 1632–1666; (90) | Adjoint noncancellation identity, individual second speeds from exchange symmetry, readout speed, positive energies, zero hidden speeds initially. | Verified. |
| 1668–1744; (91)–(94) | Initial reused-transpose law, normalized finite projection, reduced inverse, Gaussian averaging, joint polynomial moments. | Verified with full delta-Gram noise covariance. |
| 1746–1764; (95) | Positive reverse variances, orthogonal covariance rank, antiparallel variance, gated return norm. | Verified. |
| 1766–1796; (96)–(98) | Feature time, feature equations, contrast gradient, strong readout/delta/return limits, product justification. | Verified without an `L^2` Fréchet second derivative. |
| 1798–1838; (99)–(102) | Leading orthogonal hidden velocities, rank normalization, strong limits, `d_*`, adjoint coefficient identity. | Verified, including all factors `1/2` and `1/4`. |
| 1841–1855; (103) | Antiparallel leading coefficients and absence of double-counting. | Verified. |
| 1857–1896; (104)–(107) | Hidden and readout kernel gains, addition to full kernel, return to physical time. | Verified: `κ(t)=κ(0)+32d_*t²+o(t²)`, `d_*>0`. |
| 1898–1918 | Assembly of the theorem and exclusion of intermediate correlations and broader claims. | Verified; the uncontrolled off-diagonal transformed ratio is correctly identified. |
| 1920–1935 | Provenance record and denial of external mathematical premises. | Read completely; none of the named snapshots was consulted or imported. |

## Independent checks of the principal failure points

### 1. Normalization, deterministic existence, and exact raw GD

The parameter metric weights are `d/n`, `1`, and `1/n`. Starting from the prediction factor `1/n`, the Euclidean loss gradients are `(2/n)Σ r_a δ_a^(1)x_a^T`, `(2/n)Σ r_a δ_a^(2)(h_a^(1))^T`, and `(2/n)Σ r_a h_a^(2)`. Inverting the metric gives precisely (6). The readout's large relative update is therefore correct and conceals no change of clock. Its initial coordinate scale is `n^{-1}`. Section 4.2 restores this actual Gaussian initialization by a quantitative stability comparison; it does not redefine the finite model to have zero readout.

Substituting the three parameter velocities into the prediction derivative gives `dot f=-2Kr`. The first contribution includes `C_ab`; the middle contribution is the product of normalized delta and feature Grams. Squaring the parameter-metric speeds gives `4r^TKr`, hence the displayed loss dissipation. At correlation −1, the deltas agree but features and first velocities are opposite. The control is `c_1-c_2=-4r_1`, and one independent first field gives the first-matrix metric. The document correctly avoids counting both opposite fields as independent parameter motion.

The transformed stability estimates are valid because the problematic first-layer gate disappears from `dot U`. For example, splitting the return difference gives `a e_3+Ma²e_a+M(aB+1)e_W`; splitting the rank difference gives `B e_3+M(Ba+1)e_a+MB²e_W`, exactly as in (20). Only `L^2` operator bounds and the bounded readout enter. The readout clipping construction yields a locally Lipschitz vector field on an open Banach ball, and the integral readout bound makes clipping inactive locally. Thus the proof addresses the nonopenness of an `L^∞` ball in `L^2`.

The curvewise chain rule establishes the energy identity before it is used to bound action. The action bounds give integrable drift and a limit at any candidate finite endpoint, permitting continuation. For original-class uniqueness, scalar absolute continuity and `F'(Z)φ'(Z)=1` give (27). Its right side is in `L^2`, so every original solution lies in the transformed uniqueness class. At every reached state the same equation establishes the necessary transformed integrability, and the readout and operator bounds persist. Restart retains the whole state and the same operator.

Expanding a raw first-coordinate update with `v=ηcφ'(z)q` gives exactly

`F(z+v)-F(z)=ηcq+η²c²zφ'(z)²q²+(η³/3)c³φ'(z)³q³`.

On the stopped state bounds, `||q||_n≤C`, `||q||_∞≤sqrt(n)C`, hence `||q²||_n≤sqrt(n)C²` and `||q³||_n≤nC³`. The per-step defect is at most `C(η²sqrt(n)+η³n)`; its accumulated size is `C_T(ηsqrt(n)+η²n)=O_T(n^{-3/2})`. The usual Euler error `O_T(η)=O_T(n^{-2})` is smaller. The first-exit comparison proves the required iterate bounds through the candidate exit, rather than assuming a discrete loss law that has not been proved.

The raw interpolation defect has the correct coefficients `(θ²−θ)zv²+(θ³−θ)v³/3`. Differentiation costs `η^{-1}` and still gives vanishing transformed velocity error. The original first gate costs at most `sqrt(n)` against an `O(n^{-3/2})` state error, giving `O(n^{-1})`. The second-layer product rule and final gate retain that order. The readout and rank velocities have the stronger state order. Norm-square and kernel estimates follow from bounded norms. These checks include interior and terminal node conventions because either adjacent discretized velocity has the proved vanishing error.

The probability bounds supplying those initial state constants are correct. A `1/4` net has at most `9^n` points; approximating both arguments of the bilinear form loses a factor at most two. The union bound is `2 exp(2n log 9−nt²/8)`, which tends to zero at threshold 8. The two readout maximum bounds in (35) follow by the same scalar Gaussian tail and a union bound.

### 2. Fixed Gaussian programs: moments, adaptive conditioning, singularity, feedback

The fixed-program moment proof is independent of the claimed limit. After ranks are unrolled, differentiating an initial-matrix action gives `(E/sqrt(n))Dx[v]+vx/sqrt(n)`. The second term has Euclidean norm at most `||v||_F||x||_n`. Differentiating a normalized contraction supplies `n^{-1/2}`, compensating for the Euclidean vector norm in scalar-times-vector instructions. This gives (42) with width-independent polynomial bounds. The readout can be smoothly clipped in graph estimates without changing program values; the cubic first root is stored as an iid tuple and is not differentiated in a Gaussian concentration argument.

For (43), the rotated Gaussian position and its orthogonal velocity are independent standard Gaussians. Integral Hölder and conditional Gaussian integration give the stated moment constant; conditional Jensen supplies centering. Matrix-norm moments follow by integrating (34). Conditional fluctuations alone would leave conditional means uncontrolled, but the document separately proves (44): permuting two neurons permutes their root coordinates and matrix indices, root Lipschitz dependence bounds the two conditional means' difference, and averaging bounds each mean by a polynomial in normalized root norms and its own root values. Hölder and the assumed root moments finish (45). No limiting Gaussian law is used to prove these bounds.

For (46), multiplying its conditional mean by `V` gives `Y`. Multiplying its transpose by `J` gives `P_VP+P_{V⊥}P=P`, using `J^TY=P^TV`. The Gaussian residual is precisely the map from `V⊥` to `J⊥`, the common null component of both sets of constraints. At each adaptive step the next query is measurable from the earlier transcript, so observing its answer imposes its linear constraint and no additional unexplained condition. Scalar contractions and coordinate operations reveal only functions of their already observed parents.

The projection-removal estimate is also correctly normalized: a projection of fixed rank `j` contributes at most `j E|N|^p σ_n^p/n` to the empirical `p`th moment for `p≥2`. The fixed-program moment bounds control `σ_n`, and lower orders follow from the probability-space norm inequality. After removal, coordinates of the new Gaussian contribution are conditionally independent. Conditional variance bounds, compact control of regression/noise coefficients, and the higher-moment tail inequality (49) identify continuous polynomial-growth tests.

The source-response cancellation can be checked directly. Write `h_⊥=h−Σλ_rh_r`. Each old reverse answer is its Gaussian source plus a linear combination of old forward inputs, so its inner product with `h_⊥` is `E[ζ_sh_⊥]`. Gaussian integration by parts gives

`Γ_v^{-1}E[ζh_⊥]=E[∇_ζh]−Σλ_rE[∇_ζh_r]`.

Substituting into the conditional forward answer cancels the old response terms and yields (50). The full source is its old-source projection plus a fresh Gaussian of variance `E h_⊥²`; its total variance is `E h²`. Subtracting a response variance again would be an error. The document uses the full second moment correctly, in both orientations of the same matrix.

Singular query Grams are handled by actual finite perturbations. A fresh root revealed immediately before each query is independent of the old input span and the unperturbed new input, giving Schur complement at least `ε²`. Fixed positive noise permits invertible Gaussian conditioning. Coupled graph subtraction gives a uniform RMS error proportional to `ε`; higher moments upgrade this to all finite moment orders. On the scalar side, (50) has no inverse covariance. Causal coefficient selection, bounded continuous formal first derivatives, continuous finite-dimensional covariance square roots, and moment domination give continuity through rank loss. This proves the zero-noise law while retaining formally distinct redundant and zero-variance slots, including the initial reverse slots.

Empirical feedback is not merely declared deterministic. First the limiting contractions define a causal deterministic-coefficient program. Its own empirical contractions converge by the program theorem. Coupling it to the actual-feedback program and subtracting the finitely many instructions bounds the difference by those contraction errors. Only after that comparison is the actual feedback identified. The moment bounds upgrade RMS comparisons and support the cell-matching proof of Wasserstein convergence. This order avoids assuming the limit in order to prove it.

### 3. The canonical bounded operator and actual adjoint

The common construction includes both orientations of queries, rational combinations, and a countable smooth cylinder family, with every instruction having finitely many parents. Each finite part therefore has the proved joint empirical law. Passing the finite matrix norm bound and exact adjoint identity to deterministic Gram limits gives (55). A zero-norm relation among inputs implies a zero-norm relation among answers, so the proposed linear map is well defined before completion.

The density argument concerns the full generated sigma fields, not just the initial roots. Finite-cylinder events approximate all events in those fields. One-sided smooth thresholds can approximate strict or non-strict rectangle indicators correctly even at atoms. Simple-function approximation and truncation give density in `L^2`. Both linear actions consequently extend boundedly; their inner-product identity proves that the reverse extension is the actual adjoint. There is no assertion that a pointwise iid continuum kernel defines this operator.

Every finite queried marginal has a unique full-sequence empirical limit. Thus different enumerations of the same family give the same joint law; additional fixed probes can be adjoined consistently. This is the claimed canonicity on generated spaces. The theorem does not quantify over arbitrary width-dependent directions or assert initial operator-norm convergence across dimensions.

Applying the deterministic flow construction to this one operator produces the global population solution. All included mesh programs satisfy Euler equations on the same spaces with the same operator. Equation (56) is therefore a strong common-space comparison, not just marginal convergence. That fact is used essentially when passing Gaussian source and response decompositions to continuous time.

### 4. Global responses and Gaussian remainders

A bounded `L^2` operator alone would not imply bounded pointwise return remainders. A fixed finite-program response formula alone would not imply mesh-uniform bounds. Sections 3.6–3.7 supply the additional estimates.

The deterministic readout recurrence bounds controls by constants times their step sizes and bounds their total absolute sum on a finite horizon. The rank equation bounds all operator norms. These bounds also hold for the forced programs because activations remain bounded. Subtracting complete state updates, including feedback, gives step stability `1+C_Th_k`. Retaining both sample coordinates makes the same argument work off the antiparallel invariant state for the auxiliary program; no raw-flow meaning is assigned there.

Injecting `εe` into one complete reverse answer changes only the immediate first update, by `O(h_s|ε|||e||_n)`. Later stability retains that factor. A forward injection can change the current delta, predictions, residuals, and return answer by order `|ε|`, but every later state effect carries `h_s`. The separate current-delta estimate and the later bounds (58)–(59) are therefore justified, including empirical feedback changes.

Fixing the mesh and nonzero forcing first, the joint finite-program theorem identifies the forced graph and its fresh root. In the local scalar expression the root is independent of the source family and occurs only in the injected source slot and its descendants. Selected covariances and coefficients may depend on `ε`, but are deterministic with respect to that local coordinate. Hence `∂_eX^ε=ε∂_slotX^ε`, and root Gaussian integration by parts gives `E[eX^ε]=εE[∂_slotX^ε]`. The unused root is independent of the unforced expression.

Passing the finite Cauchy–Schwarz inequality to the joint width limit bounds that expectation divided by `|ε|` by `C_Th_s`. Only then is forcing sent to zero, using the finite-program continuity already proved. This establishes exactly the expected formal derivatives in (38), including zero-variance initial slots. No derivative transverse to a singular Gaussian support is inferred merely from the unforced law. Feedback is included in the finite stability estimate; holding selected scalar values fixed is appropriate only for the subsequent local-root derivative.

The learned terms have the same `C_Th_s` bound because they include `γ_sb` and bounded second moments. Summation gives bounded absolute response row sums uniformly over mesh size. Each response input is pointwise bounded, so (63) has bounded remainders. Integrating the first-field equation gives (64), with its Gaussian term independent of the entire initial first row.

Cross-program covariance gives the Gaussian isometries (65). Sources therefore converge strongly with their inputs on the common space. Subtracting from convergent fields transfers the essential remainder bounds; an `L^2` limit of uniformly bounded variables is bounded. Gaussian Riemann sums converge in `L^2`, and characteristic functions preserve Gaussianity and independence from the first row. This proves (66) at every deterministic finite time, with jointly measurable representatives sufficient for Fubini in time. The all-time tails are thus deductions from the constructed flow, not extra premises or properties of a separately selected subsequential law.

### 5. Uniform integrability, paths, velocities, and energies

Ordinary `L^2` state stability alone would not control higher moments or multiplication by an unbounded return field. The document proves these separately. For the moment estimate, radial matrix clipping is 2-Lipschitz in operator norm and agrees with the original with probability tending to one. A change `D` in unscaled Gaussian entries changes the clipped operator by at most `2||D||_F/sqrt(n)`. State stability then makes each coordinate path-supremum functional Lipschitz with constant independent of width: the factor `sqrt(n)` for one coordinate cancels the normalized perturbation factor. The same cancellation applies to stored-root changes.

The path-supremum RMS bound (70) follows from pointwise absolute continuity and the integral triangle inequality. All derivatives used in (71) require bounded multipliers and `L^2` operator actions only. In particular, the readout factor in `dot δ^(2)` is bounded, and `dot Q` uses the actual bounded transpose. The Gaussian fluctuation inequality and conditional-mean permutation argument now apply to coordinate supremum functionals. They give every finite moment in (72), including the actual-readout comparison after auxiliary clipping. This proof does not assume the width-limit theorem it supports and does not assign an `L^p` norm to the matrix on arbitrary inputs.

The fixed-time passage has a correct order: choose a small fixed mesh, take width to infinity using the finite-program theorem, then refine the mesh. Same-index coupling bounds the finite outer error and the common-space coupling bounds the population outer error. Product truncation and (72) handle the first backward fields. The actual Gaussian readout is restored by stability with initial error `||W_n^(3)(0)||_n→0`. General probes are handled within the stated finite-program and verified-approximation scope in both orientations.

For paths, Cauchy–Schwarz on each observation interval proves (74); averaging gives the empirical transport estimate. The base fields have the required integrated squared derivatives. Grid convergence and this estimate establish joint path Wasserstein-2 convergence. The supremum moments upgrade it to every fixed finite order. The first backward product is a continuous map of the joint continuous-path tuple, with supremum bounded by the return-field supremum, so truncation justifies its path law as well. This step does not require an a priori derivative-energy estimate for that product.

The final second-activation gate merits a separate check because `W dot H^(1)` has no immediate higher-moment bound from an operator norm. Here is an explicit version of the source's compressed argument. At a fixed mesh, define `V_n^h(t)` by evaluating the second-preactivation velocity formula (73) at the left Euler node on the interval containing `t`. The transformed comparison and (67), with (72) for the first return field, imply that

`sup_{t≤T} ||dot z_n^(2)(t)−V_n^h(t)||_n`

tends to zero in the width-limsup followed by mesh-refinement limit. For fixed `h`, there are only finitely many fields `V_n^h(t)`. Their joint Wasserstein-2 convergence is supplied by the truncated-query argument. Their squares are consequently uniformly integrable in probability. Taking the maximum over that finite family in (75), then making `h` small, transfers the square-tail property to the actual GF velocity uniformly in time. The population velocity curve is continuous in `L^2`, and a finite cover by small `L^2` balls gives the same tail property there. Applying (67) now justifies the last gate. This establishes individual fixed-time velocity laws, uniform quadratic norms, and integrated tests without a circular moment argument.

For parameter speeds, row reconstruction gives the first metric, (76) gives the middle metric, and the readout metric is its field norm. Cross-time contractions of the rank integrand give the squared norm of any finite rank-integral sum. The integrand is continuous in HS norm with a width-independent modulus from state stability, so sums pass to the integral. This proves the parameter-increment statements while never taking an HS norm of the initial middle operator.

Raw GD inherits these conclusions from the deterministic comparisons. A normalized base-field error `O(n^{-3/2})` gives a maximal coordinate path error `O(n^{-1})`. The first backward product has normalized error `O(n^{-1})` by (32), hence maximal coordinate error `O(n^{-1/2})`. Both vanish. The resulting same-neuron coupling transfers every finite path-Wasserstein order using the GF moment bounds; velocity and energy estimates transfer the remaining observables. Thus the stated interpolation, not merely a transformed mesh, receives the theorem's limits.

### 6. Canonical symmetry, support, and persistent nonaffinity

The reflection (77) swaps the inputs and preserves the isotropic first-row law. Under (78), forward fields swap samples, while the readout and backward fields acquire the signs in (79). Opposite labels are essential for the residual sign. Checking all three updates shows that the first velocity is right-multiplied by the reflection, the middle velocity is unchanged, and the readout velocity changes sign. The parameter metric is preserved. The initial matrix/readout law is invariant both for auxiliary zero readout and for the actual independent symmetric Gaussian readout.

The full-sequence deterministic population limit therefore gives `f_2=-f_1` and equality of the two sample velocity norms. This does not turn orthogonal sample fields into pointwise opposites at finite width. At correlation −1, stronger opposition is already an exact raw-state identity. The source distinguishes these situations correctly. In particular, the equal second-velocity norms later used to exclude a stationary sample come from the canonical limit and are not assumed as an extra property of an arbitrary initial operator.

For the first-layer tails, (66) writes `F(Z_a)` as `F(G_a)` plus a Gaussian integral independent of the entire first row plus a bounded remainder. At a fixed time the joint Gaussian integrals have positive probability of lying in a sufficiently large bounded box. Independently, the initial row has positive probability of sufficiently large values with prescribed signs. The bounded remainder cannot defeat the resulting lower or upper bound on `F(Z_a)`. Every first field thus has both unbounded tails. At correlation zero, independence of `G_1,G_2` allows all four sign patterns, so the first-feature pair approaches all four corners of `[-B,B]^2` in support.

A linear combination that vanished almost surely would vanish at both limiting corners `(B,B)` and `(B,−B)`, forcing its two coefficients to zero. This proves positive definiteness of the uncentered first-feature Gram at each finite time. At correlation −1 it remains rank one, with a nonzero single feature. No two-column inverse is used.

Each second source has variance equal to the strictly positive first-feature second moment. If its bounded remainder is dependent on it, the event inclusion `ξ>R+C_T ⇒ Z^(2)>R` still holds, as does its negative-tail counterpart. Thus source/remainder dependence does not invalidate either tail. The proof uses independence only where supplied: between first-row roots and their Gaussian integral, not between second sources and remainders.

For each resulting `L^2` preactivation, `span{1,Z}` is closed because its Gram determinant is `Var(Z)>0`. A zero approximation infimum would therefore be attained as an exact affine identity. Since arctangent is bounded and the support is unbounded, the affine slope must be zero; since arctangent is strictly increasing, the field would then have to be constant. This contradiction proves the strictly positive distance in (14). The result is distributional nonaffinity, not just scalar nonlinearity of the activation, and holds for both layers and samples at every finite time, including zero.

### 7. Strict motion at every positive physical time

From prediction symmetry, `r=(f_1−1)y`. Applying `y^T/2` to the output equation gives `dot f_1=4(1−f_1)κ`. Kernel positivity and fixed-horizon bounds give the finite, strictly positive residual exponential in (85). The initial readout contrast is nonzero: initial second features are independent nonconstant centered variables at correlation zero and opposite nonzero variables at correlation −1. Thus `f_1` becomes positive immediately, stays positive by monotonicity, and remains below one at every finite time. The readout is consequently nonzero.

Since `φ'>0`, each second-layer delta is nonzero. Its squared norm is exactly the reverse-source variance. A nondegenerate Gaussian with a bounded remainder has unbounded tails, so every return field is nonzero. The special-angle first-velocity formulas have nonzero scalar coefficients and positive gates. Every first preactivation and activation speed is strictly positive, and reconstruction gives strict first-matrix speed.

For the middle matrix at correlation zero, apply the positive-definite first-feature Gram pointwise to `(y_a δ_a^(2))_a` and integrate. This gives (89) and strict positivity. At correlation −1 the reduced velocity is a rank-one operator with two nonzero factors. These are actual hidden-parameter speed statements, not conclusions merely about output motion.

Cancellation between `dot W^(2)H^(1)` and `W^(2)dot H^(1)` could otherwise leave a second preactivation stationary. Equation (90) excludes simultaneous cancellation: its first contribution is the squared HS middle speed, and its second is the squared first-matrix speed, with only one independent antiparallel first field. Their sum is positive. Therefore the two second preactivation speeds cannot both vanish; their independently proved equal norms make each nonzero. Positive gates give strict second activation speeds.

The readout velocity is a positive scalar multiple of the second-feature contrast. That contrast cannot vanish because its inner product with the readout equals `2f_1>0`. All speeds are continuous, so their energies are positive on every positive-duration interval in positive time. Initially hidden speeds vanish because the limiting readout and deltas vanish. No lower speed bound uniform as time tends to infinity is claimed.

### 8. Reused transpose and the full-kernel coefficient

Conditioning the initial matrix on its forward columns and then transposing gives exactly

`H Γ_n^{-1}(Z^T δhat/n) + P_{H⊥} G Σ_n^{1/2}`.

The normalized Grams and mixed contraction have the correct factors. Conditional on first features, the forward rows are independent Gaussians. The delta functions are bounded, while the mixed `Z` contraction uses finite Gaussian moments, as the source notes explicitly. Reduced Gram convergence justifies the inverse. Removing the fixed-rank projection has vanishing empirical moments and leaves noise covariance `E[δhat δhat^T]`, without subtracting the response variance.

At correlation zero, full initial two-dimensional Gaussian support and nonconstancy of `φ'` prove positive definiteness of that covariance. In the antiparallel reduction its single entry is positive. Conditional Gaussian variance given the first row then proves `||φ'(G_a)Qhat_a||_2>0`. Thus the initial first-layer learning coefficient is positive using the actual reused transpose, without assuming independence of its finite coordinates after reuse.

Feature time satisfies `ds/dt=4(1−f_1)` and `s=4t+o(t)`. The orthogonal first and middle equations have coefficients `y_a/2`; the reduced antiparallel equations have coefficient one. The readout feature-time derivative is `g=(H_1^(2)−H_2^(2))/2`, initially `What^(3)`.

Strong convergence of `W^(3)(s)/s` gives the delta and return limits through bounded-gate continuity and the bounded adjoint. Original hidden derivatives divided by `s` then have the strong limits (99)–(103). For example, the orthogonal rank contribution to the second-preactivation coefficient is

`(1/2)Σ_b y_b δhat_b E[φ(G_b)φ(G_a)]=(1/2)y_a m δhat_a`.

Moving the initial operator through its adjoint gives

`y_a E[δhat_a vhat_a^(2)]=(1/2)(m||δhat_a||_2²+||φ'(G_a)Qhat_a||_2²)`.

This verifies (101)–(102), including the factors `1/4` in `d_*`, and gives the one-field version (103) without double-counting. All relevant coefficients are strictly positive where asserted.

The hidden label-direction kernel equals the sum of squared hidden feature-time parameter speeds, so its leading gain is `d_*s²`. Differentiating the squared readout contrast gives (105). Dividing by `s` and using the preceding identity yields `2d_*`; integration gives a readout gain `d_*s²`. Hence

`κ(s)=κ(0)+2d_*s²+o(s²)`.

Returning to physical time yields

`κ(t)=κ(0)+32d_*t²+o(t²)`, with `d_*>0`.

The readout contribution has the same positive sign as the hidden contribution, so the full kernel cannot cancel back to its initial value at this order. This proves nonconstancy on every sufficiently short interval starting at zero. The derivation uses strong velocity limits and integration, not an unproved second Fréchet derivative of a nonlinear map on `L^2`.

## Limit exchanges and proof-dependency audit

| Potentially sensitive exchange | Controlling argument in the source |
|---|---|
| Differentiate nonlinear compositions | Bounded continuous scalar derivative and dominated squared difference quotients along the `L^2` curve; lines 394–402. |
| Adaptive query to empirical polynomial test | Conditional Gaussian independence after projection removal, conditional variance, fixed-program moments, and tails; lines 742–848. |
| Remove query noise at singular covariance | Uniform finite-graph coupling, higher-moment interpolation, inverse-free response recursion, continuous covariance roots; lines 850–914. |
| Restore empirical feedback | Causal finite-program subtraction using convergent deterministic-program contractions; lines 926–937. |
| Extract expected responses | Width limit at fixed mesh and nonzero forcing, independent-root integration by parts, then zero-forcing continuity; lines 1086–1128. |
| Pass Gaussian decompositions to the flow | Common-space convergence, source isometries, bounded remainders, Gaussian characteristic functions, and `L^2` Riemann sums; lines 1163–1200. |
| Width/time limit | Width-independent outer comparisons and the fixed-mesh theorem in the middle; lines 1322–1354. |
| Upgrade path laws and polynomial moments | Independently proved supremum moments, grid interpolation and truncation; lines 1222–1296 and 1356–1381. |
| Pass unbounded velocity queries and gates | Smooth truncation, bounded operator action, uniform RMS approximation, and square-tail transfer (75); lines 1298–1317 and 1383–1418. |
| Speed and increment integrals | Uniform norm convergence and boundedness; cross-time rank contractions and uniform rank-integrand modulus; lines 1420–1437. |
| Initial kernel expansion | Strong `L^2`/HS limits, bounded gates, Hilbert inner-product differentiation, integration of the derivative asymptotic; lines 1785–1892. |

The document proves the specialized results that otherwise would be substantial imports: adaptive Gaussian conditioning, the fixed-program law, singular-rank handling, the canonical bounded operator and adjoint, global response control, and the Gaussian fluctuation inequality. The remaining tools are foundational integration, Hilbert-space, finite-dimensional linear algebra, and probability facts: Fubini, dominated convergence, Hölder/Jensen/Cauchy–Schwarz, completeness, scalar Gaussian integration by parts, finite-dimensional positive-semidefinite square roots, and approximation of generated sigma fields. The displayed bounds, moments, or countability supply their needed hypotheses.

No unspecified tensor-program theorem, propagation-of-chaos theorem, spectral-limit theorem, external deep-network theorem, or mathematical result from a provenance snapshot is a premise. Consequently there was no heavy external theorem whose full primary statement, proof, or dependencies had to be retrieved. None was silently assumed.

## Final assessment

The entire document is sound at its stated two-angle scope. Global response control supports the tail and support conclusions; independent moment bounds support the observable and velocity limits; finite-law symmetry supports individual second-layer motion; and the expansion verifies positive full-kernel change in the original physical clock. The optional clarifications make compressed connections easier to inspect but do not supply missing mathematical premises or alter the theorem.
