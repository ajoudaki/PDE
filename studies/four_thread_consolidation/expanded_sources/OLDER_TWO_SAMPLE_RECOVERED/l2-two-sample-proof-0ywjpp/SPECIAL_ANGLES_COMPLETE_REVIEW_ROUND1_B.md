# Independent adversarial full-document review — Round 1 B

## Verdict

**PASS, for the special-angle theorem actually stated: fixed input dimension, two samples, two hidden layers, arctangent activations, correlation 0 or -1, the parameter metric (7), the physical step size n^-2, and convergence on each fixed finite time horizon.**

I found no required mathematical correction. In particular, I found no missing heavy theorem, unresolved rank assumption, circular response estimate, incorrect time factor, or unjustified replacement of the actual finite Gaussian readout by zero. The deterministic existence/uniqueness argument and the probability/mesh comparisons close under the stated assumptions.

This verdict does not assert a general-angle theorem, ordinary Euclidean GD on the displayed arrays, operator-norm convergence across widths, convergence uniform on the half-line, convergence in expectation, or a restart with a newly sampled operator. None of those is proved or claimed here.

The phrase “every original hidden-field velocity” could be made more explicit. Section 4.4 directly treats the preactivation and activation velocities. Below I also check the broader reading that includes derivatives of the backward fields, using (71), (53), (67), (72), and (75). That reading does not require an additional assumption or an external theorem. Making those formulas explicit is an optional presentation improvement, not an unresolved obligation in this audit.

## Isolation, scope, and integrity record

- Sole mathematical source read: `/tmp/l2-two-sample-proof-0ywjpp/L2_TWO_SAMPLE_SPECIAL_ANGLES_COMPLETE_PROOF.md`.
- All 1,935 lines were read, in order, before judgment. This includes the scope qualification and the provenance-only list at the end.
- Expected SHA-256: `5cd54a6125dfbf4b7d1bc86149760b842d7d2c1f9a44fe73fcf57f5d3d15f12e`.
- Initial SHA-256: exact match.
- A second hash check after the analytical audit, before writing this review: exact match.
- The final post-write source hash check is recorded at the end of this review.
- Procedural skill read: `/etc/codex/skills/solve-math-rigorously/SKILL.md`.
- No other mathematical document, project document, prior review, history, source agent, or directory listing was consulted. In particular, none of the four files named at source lines 1923–1930 was opened.
- No agents, experiments, simulations, numerical checks, or mathematical reference searches were used.
- No heavy external theorem is invoked as a premise of this proof. There is consequently no external-theorem access blocker to report. Elementary Gaussian projection, integration by parts, probability inequalities, and finite-dimensional linear algebra are checked below in the forms used.
- The source was not edited. This review was created with `apply_patch` at the requested output path.

All line and equation references below refer to the supplied source, not to this review.

## Full coverage ledger

“Verified” means the mathematical implication was checked, including the relevant hypotheses, factors, and limiting order; it does not mean merely that the section was read.

| Source coverage | Equations | Result and principal checks |
| --- | --- | --- |
| Lines 1–86; §1.1 | (1)–(7) | Verified input normalization, shapes, readout variance, Euclidean gradients, inverse metric, loss-SUM factors, and the raw physical clock. |
| Lines 88–144; §1.2 | (8)–(11) | Verified normalized adjoints, rank-one action, finite Frobenius/HS identification, population state types, forward/backward definitions, and autonomous equations. |
| Lines 146–229; §1.3 | (12)–(14) | Audited every claimed observable class against §§2–5: paths, moments, probes, kernels, velocities, parameter metrics, increments, nonaffinity, positive speeds, and kernel change. |
| Lines 231–288; §2.1 | (15)–(18) | Verified inverse-coordinate derivatives, the Gaussian moment 14/3, exact cancellation at correlation 0, the factor-four antiparallel reduction, and first-row reconstruction. |
| Lines 290–370; §2.2 | (19)–(22) | Verified every subtraction estimate, clipping construction in an open Banach-space neighborhood, contraction, control stability, feedback stability, and comparison of different initial operators. |
| Lines 372–448; §2.3 | (23)–(27) | Verified a priori action bounds, endpoint extension, the along-curve chain rule, prediction/energy identities, global feedback control, original-class uniqueness, and autonomous restart. |
| Lines 450–547; §2.4 | (28)–(35) | Verified Euler consistency, first-exit closure, exact raw cubic defect, interpolation and velocity errors, all normalization factors, and high-probability initialization bounds. |
| Lines 549–640; §3.1 | (36)–(40) | Verified causal scheduling, scalar recursion, learned-rank terms, uncentered source covariances, current reverse response, and formal derivatives at singular covariance. |
| Lines 642–740; §3.2 | (41)–(45) | Verified bounded readout, Lipschitz replacement, graph norm/derivative induction, Gaussian rotation inequality, conditional-mean argument, and all-order fixed-program moments. |
| Lines 742–848; §3.3 | (46)–(51) | Verified adaptive conditioning, both projection orientations, negligible finite-rank corrections, conditional empirical averaging, Gaussian integration by parts, and the full-variance source representation. |
| Lines 850–947; §3.4 | (52)–(54), and singular-limit arguments | Verified input-noise regularization, positive Schur complements, finite-graph comparison, interpolation to all moments, covariance-square-root continuity, retention of null slots, empirical feedback, and Wasserstein convergence. |
| Lines 949–1033; §3.5 | (55)–(56) | Verified countable construction, well-defined bounded actions, density, the actual adjoint, observable canonicity, and the common-space Euler comparison. |
| Lines 1035–1138; §3.6 | (57)–(62) | Verified horizon-uniform bounds, actual fresh-root perturbations, feedback dependence, off-invariant antiparallel comparison, integration by parts in the new root, and the width/forcing order of limits. |
| Lines 1140–1200; §3.7 | (63)–(66) | Verified bounded response remainders, Gaussian upper tails, source isometries, passage on the common space, Gaussian integrals, and independence from the complete first row. |
| Lines 1202–1296; §4.1 | (67)–(72) | Verified product continuity, auxiliary radial clipping, supremum Lipschitz estimates, pathwise integral bounds, conditional concentration, all-order supremum moments, and removal of auxiliary clipping in probability. |
| Lines 1298–1354; §4.2 | (73) | Verified unbounded-query truncation, both operator orientations, fixed-time width/mesh limits, actual-readout restoration, and the exact admissible-probe scope. |
| Lines 1356–1381; §4.3 | (74) | Verified path transport through observation grids, backward-field path products, every finite Wasserstein order, and uniform prediction/loss/kernel convergence. |
| Lines 1383–1451; §4.4 | (75)–(76), reuse of (31)–(33) | Verified original velocity comparisons, noncircular UI for the second preactivation velocity, uniform quadratic norms, integrated energies, increment metrics, and transfer to raw GD. The broader backward-velocity interpretation is checked separately below. |
| Lines 1453–1511; §5.1 | (77)–(80) | Verified the input reflection, all field signs, metric/loss preservation, commutation with GF/GD, deterministic-limit symmetry, and equality of sample velocity norms. |
| Lines 1513–1568; §5.2 | (81)–(83), use of (14) | Verified both first-layer tails, four-corner support at correlation 0, the rank-one alternative at -1, both second-layer tails, and strict positive distance from affine functions. |
| Lines 1570–1666; §5.3 | (84)–(90) | Verified residual direction, exponential residual formula, strictly positive prediction progress, every stated positive-time speed, the adjoint no-cancellation identity, and the zero-time hidden-speed statement. |
| Lines 1668–1764; §5.4 | (91)–(95) | Verified initial reverse conditioning, every factor of n and m, the unreduced Gaussian variance, singular reduction, and strict positivity of the leading first-layer coefficient. |
| Lines 1766–1896; §5.5 | (96)–(107) | Verified feature-time conversion, all leading velocity coefficients, both geometric cases, hidden/readout contributions, and the positive physical coefficient 32 d_*. |
| Lines 1898–1935; §5.6 | General-angle display and scope record | Verified the stated obstruction away from the two angles and that the provenance list supplies no imported mathematical premise. |

## Detailed findings and re-derivations

### 1. Metric, transpose, physical time, and singular geometry

At finite width, differentiation of the prediction contributes one factor 1/n to each Euclidean parameter gradient. Thus the three Euclidean loss gradients are exactly those at lines 80–83. The inverse metric weights are n/d, 1, and n. Their products with the Euclidean gradients give respectively 2/d, 2/n, and 2, exactly as in (6). There is no missing loss-average factor or additional readout rescaling.

The readout variance in (2) is n^-2, hence its standard deviation is n^-1. Its normalized squared norm has expectation n^-2. Consequently its population limit is zero, but the actual finite readout is not identically zero; §§2.4 and 4.2 correctly keep that distinction.

For the two copies of the normalized finite neuron space,

`<Wu,v>_n = <u,W^T v>_n`.

The adjoint is therefore the ordinary transpose. Using the normalized orthonormal bases `sqrt(n) e_i` in both spaces leaves the matrix entries of the linear map unchanged. Its Hilbert–Schmidt norm is the ordinary Frobenius norm. The rank-one map is `v h^T/n`, whose Frobenius norm is `||v||_n ||h||_n`. These observations verify (8)–(9) and the normalizations in (12), (13), (54), (76), and (94).

For correlation 0 the two inputs are orthogonal, each with squared norm d. For correlation -1, equality in Cauchy–Schwarz forces `x_2=-x_1`; odd activations and even derivatives then give every identity in (17), including equality, rather than opposition, of the two backward deltas. The effective control is

`c_1-c_2 = -2 r_1 + 2 r_2 = -4 r_1`.

This factor appears consistently in the state equations, first-row reconstruction, energy identity, strict-motion proof, and feature-time expansion. In particular, the antiparallel first-parameter energy is counted once, not twice.

For (18), taking the scalar product with an independent input returns exactly the corresponding changed preactivation. The orthogonal complement of the input span is unchanged by the raw first-parameter equation. Moreover,

`d E |dot W^(1)|^2 = sum_{a=1}^{m_rho} ||dot Z_a^(1)||_2^2`.

No first-parameter degree of freedom or metric contribution is lost at reconstruction.

### 2. Deterministic existence and original-class restart uniqueness

The coordinate map satisfies `F'(z)=1+z^2=1/phi'(z)`. Therefore `(F^-1)'=phi'` and `(phi o F^-1)'=phi'^2`, each bounded by one. The transformed first equation is exact in the two allowed geometries. The initial transformed field is in L2 because

`E F(G)^2 = E G^2 + (2/3) E G^4 + (1/9) E G^6 = 14/3`.

I checked all six inequalities in (20). In particular, the potentially dangerous backward product is handled before the first-layer gate is reapplied. Splitting the second-layer delta gives

`||delta_2 - tilde delta_2||_2 <= e_3 + M (a_0' e_a + B e_W)`.

Applying the bounded operator and bounding the remaining operator difference against `||tilde delta_2||_2 <= M` gives exactly

`||Q - tilde Q||_2 <= a_0' e_3 + M(a_0')^2 e_a + M(a_0' B+1)e_W`.

The rank difference is the sum of two rank-one terms; its HS estimate has the same constants as the operator estimate. No L-infinity bound on Q, and no Lp boundedness of the operator for p other than 2, is used here.

The clipping construction at lines 328–347 resolves the non-openness of an L-infinity readout ball in L2. After clipping the readout inside predictions and deltas, the vector field is locally Lipschitz on an actual open Banach-space neighborhood. The integral-map contraction is valid in the complete continuous-path space. The readout update itself has bounded coordinates, so a sufficiently short interval keeps it inside the clipping range. This constructs a solution of the original equations, not a permanently clipped equation.

The action estimates in (23) are correctly normalized. For example,

`||dot W^(2)||_p <= B (sum |c_a|) (b_2+B S)`,

whose integral is `B b_2 S + B^2 S^2/2`. Multiplying the resulting operator bound by the readout L2 bound gives the stated integral bound for U. These bounds also make the state Cauchy at a finite endpoint of finite action. The separate L-infinity Cauchy estimate for the readout supplies the hypothesis needed to restart the local construction at that endpoint.

The along-curve chain rule at lines 394–402 is sufficient for differentiating all forward fields. The proof uses a fixed tangent direction and dominated convergence of squared scalar difference quotients. It does not assume Frechet differentiability of a general nonlinear composition map on L2.

Differentiating the prediction and using the actual adjoint gives the three blocks of (12). In particular, the first contribution is

`E_1[delta_a^(1) dot Z_a^(1)] = -2 sum_b C_ab r_b E_1[delta_a^(1) delta_b^(1)]`.

The other contributions give K^(2) and K^(3). Hence `dot f=-2Kr` and `dot L=-4 r^T K r`. Each block is a Gram matrix in the stated parameter metric. The squared parameter speed is exactly `4 r^T K r`, including the one-field antiparallel reduction. This verifies (24)–(25), not just monotonicity of the loss.

The residual bound closes the action bound: `sum |c_a| <= 2 sqrt(2) ||r||`, and the reduced control has the same bound. Thus there is no finite-time action blowup. This gives global existence on every finite horizon and the constants in (26).

The uniqueness claim is not restricted to solutions initially postulated in transformed coordinates. For an ordinary L2 solution of the original integral equations with a reached initial state:

1. Its residuals are continuous; the readout integral inherits a local essential bound from the bounded activation and the bounded initial readout.
2. The first preactivation equation has integrable L2 forcing `c Q` multiplied by the bounded gate.
3. Fubini supplies scalar absolutely continuous representatives.
4. Each scalar trajectory has compact range on a compact time interval, so applying the ordinary scalar chain rule to the smooth, possibly unbounded F is legitimate.
5. The result is exactly (27). Its right side is in L2 because the reached initial transformed field and the forcing integral are in L2.

The solution therefore lies in the transformed class, where (22) gives uniqueness. The reached state retains its operator, readout, first row, and unchanged orthogonal component. The antiparallel relation persists under the original integral equations. Concatenation proves the claimed autonomous restart; no resampling or omitted history variable is involved.

### 3. Raw GD is not silently identified with transformed Euler

The local transformed Euler error (28) follows from a bounded Lipschitz drift along the exact solution. The recurrence in (29) has a summable local error and yields a uniform finite-horizon estimate. The stopping argument checks the candidate exit node: the old residual bound controls the entire next update, and the error estimate then rules out a residual excursion. It does not presuppose stability of the untruncated iterates.

At a raw node, expansion of the cubic gives precisely

`F(z+v)-F(z) = (1+z^2)v + z v^2 + v^3/3`,

with `v=eta c phi'(z) q`. The linear term is `eta c q`, so (30) is exact. The bounds

`||q^2||_n <= ||q||_infty ||q||_n <= sqrt(n) C_T^2`

and

`||q^3||_n <= ||q||_infty^2 ||q||_n <= n C_T^3`

give the displayed defect. Multiplying by the number of steps gives an accumulated bound of order `eta sqrt(n) + eta^2 n`; at `eta=n^-2` this is `O_T(n^-3/2)`. The ordinary Euler error `O_T(n^-2)` is smaller. The other two transformed coordinates have no coordinate-change defect.

For interpolation, directly subtracting the linear interpolation of the endpoint F-values from `F(z+theta v)` gives the expression at lines 499–501. Dividing its derivative by the step length gives the stated `eta sqrt(n)+eta^2 n` velocity error. Thus the result applies to linear interpolation of the raw arrays with recomputed fields, as required by lines 67–70.

The normalized first-velocity error becomes `O_T(n^-1)` after applying (32), because the available deterministic finite-width supremum bound is `sqrt(n) C_T`. The same accounting in (33) gives that order for both second-layer forward velocities. Rank and readout velocity errors retain order `n^-3/2`. Uniform speed bounds convert these estimates to squared norms and integrated energies. No discrete loss dissipation identity is asserted or needed.

The 1/4-net argument yields a factor two in the bilinear norm comparison; a fixed bilinear form has variance 1/n. Union over the two nets gives exactly (34). At threshold eight its exponent is strictly negative uniformly in width. The two readout bounds in (35) use standard deviation 1/n and are correct. On these events, the initial residual norm is bounded independently of width because the readout supremum is at most one. All constants used in the raw-versus-flow comparison are consequently uniform on events of probability tending to one; there is no additional bound on the initial first-row coordinates hidden in the estimate.

### 4. Fixed-program law, singular ranks, and the reused transpose

The recursion (37)–(40) is causal. At a node, first-layer fields are already known; both forward queries occur before either reverse query; the current second-layer deltas depend on the existing readout; the updates occur last. In particular, the current reverse derivative is exactly the diagonal term at (40). Formal covariance-degenerate sample slots remain distinct, as they must.

The readout bound (41) follows from `|f_a|<=B ||W^(3)||_infty` and the two summands in the update. It remains valid under the described query perturbations. A smooth bounded readout replacement can therefore be used for the finite graph estimates without altering the program values. Storing F(G) as part of an iid root tuple is legitimate and avoids differentiating the cubic as a globally Lipschitz root map.

In (42), the direct matrix differential is `v x/sqrt(n)`. Its ordinary Euclidean norm is at most `||v||_F ||x||_n`. For a normalized contraction, differentiation introduces the compensating `n^-1/2` factor. This factor cancels the `sqrt(n)` norm of a vector at scalar-times-vector nodes. The resulting derivative and polynomial norm bounds are dimension independent.

The Gaussian rotation proof of (43) is valid for p at least one. The rotated position and velocity are independent standard Gaussians. Integral Holder gives the power of pi/2; conditional integration of the directional Gaussian gives `E|N|^p`; conditional Jensen centers the variable. The matrix-norm tail bound supplies all moments needed for the polynomial derivative bounds.

The conditional-mean argument is also necessary and valid: the stored roots are not all Gaussian linear coordinates. Permuting two neurons in one population, with the corresponding matrix rows or columns, identifies the difference of the two conditional means with a root-array perturbation. Averaging that difference and using the normalized RMS bound gives (44). Holder and the root moments then prove (45). No assertion about arbitrary Lp operator inputs is substituted for this random-program estimate.

For (46), the mean satisfies both constraints, using `J^T Y=P^T V`. The remaining matrix lies in the common orthogonal null space of those constraints. Gaussian orthogonal projection gives its independent residual law. Adaptivity is harmless here because each new query is measurable before its answer is exposed; inductively the newly observed information is exactly the next linear constraint.

The forward answer from that formula is `Y lambda + J nu + sigma P_{J-perp} e`, with precisely the normalized coefficients at lines 763–765. The diagonal projection calculation in (47) is correct: the sum of diagonal entries is the fixed rank, and each entry lies between zero and one. All moments of sigma are bounded by the already established input moments. The removed projection therefore vanishes in every fixed empirical Lp norm.

After removing that projection, coordinates of the new Gaussian innovation are conditionally independent. Localizing the regression and variance coefficients to a bounded set gives (48); convergence of the empirical Gram entries makes that localization exhaustive. The Gaussian-integrated test is continuous with polynomial growth on those coefficient sets. The higher-moment tail estimate (49) justifies the expectation limit and the restoration of the small projection. This proves the finite-program induction, including the relevant polynomial tests rather than merely bounded tests.

The calculation leading to (50) retains the old forward projection and the old reverse responses. Integration by parts gives

`nu = E grad_zeta h - sum_r lambda_r E grad_zeta h_r`.

Substitution of the old forward answers cancels the second term. Crucially, the full new Gaussian source is the old source projection plus the independent residual innovation. Its variance is the full uncentered input second moment. It is not reduced by an Onsager-response variance. The reverse calculation is the same conditioning of the same matrix, with the populations exchanged.

For singular query Grams, the fresh input noise in §3.4 is independent both of the old same-direction input span and of the unperturbed new input. The limiting Schur complement is at least epsilon squared. For each fixed positive epsilon the finite conditioning theorem applies; no uniform inverse-Gram bound as epsilon tends to zero is assumed.

The actual finite noisy and noiseless programs are coupled before passing to a scalar law. Their L2 difference is bounded by epsilon times a polynomial of variables with uniformly bounded moments. Equation (53) and (45) upgrade this to every fixed finite empirical Lp order. On the scalar side the response formula has no covariance inverse; induction, bounded first source derivatives, and continuity of positive semidefinite square roots give continuity at zero noise. The square-root argument works also at zero eigenvalues: any subsequential positive semidefinite limit is the unique nonnegative square root of the limiting matrix.

The limit order is width first at fixed positive noise, then noise to zero. This covers exactly zero queries, redundant queries, the initial zero reverse fields, and the antiparallel rank defect. Retaining formal null slots is consistent with the fact that a coefficient change along a null input relation has zero contracted response.

Finally, the learned-rank formulas (54) are exact operator identities. Selecting contractions causally in the scalar program and comparing that deterministic-coefficient program with the actual empirical-feedback graph is legitimate: at each step only already identified scalar contraction errors are introduced. Finite induction using (52) closes the comparison. The moment bounds and (53) then restore all polynomial tests. The cell-coupling and tail construction at lines 939–947 proves Wasserstein convergence in probability, not merely weak convergence.

### 5. Canonical operator and global response bounds

The countable construction uses finite parents at every stage and covers every fixed finite subprogram. Input Gram matrices specify consistent Gaussian source covariances. Zero conditional variance requires no new random draw. The elementary binary-digit construction suffices to realize the countable roots and innovations; a continuum iid kernel is neither claimed nor used.

The finite matrix norm bound and convergence of the relevant Gram entries force every inequality in (55). A nonzero violation would be an inequality between deterministic limiting numbers and would contradict the high-probability finite inequality. Zero-norm input relations therefore produce zero-norm output relations. This proves well-definedness, not just boundedness, of the proposed linear maps.

The supplied cylinder-density argument covers atoms: one-sided smooth threshold approximations can represent either choice of endpoint. Finite-cylinder events generate the countable sigma field, and truncation/simple-function approximation gives density in L2. Extending the two maps by continuity and then passing the finite duality identity to the completions makes the reverse map the actual Hilbert adjoint. Observable canonicity follows because any common finite marginal is the full-sequence limit of the same finite program. This is the appropriate generated-space meaning of canonicity.

The common operator is constructed before taking the mesh limit. Every constructed mesh program solves its Euler equations on those same spaces, so (56) is an ordinary deterministic comparison to the unique global flow. It is not a width-subsequence definition of that flow.

For §3.6, (41) gives (57) uniformly over the allowed partitions. The bound on the sum of the absolute update coefficients and the rank equation give a common operator bound. Subtracting one auxiliary step gives a factor `1+C_T h_k`. Retaining both first coordinates makes this estimate valid also off the antiparallel invariant state; this auxiliary comparison is not asserted to be raw GF there.

Injecting epsilon times a new first-population root into a complete reverse answer changes the next state only through an update weighted by h_s. This proves (58) after multiplying the later stability factors. Injecting a new second-population root into a complete forward answer can change current deltas by order epsilon, but every subsequent state change carries h_s. That proves (59). Residual and learned-rank changes are included in these estimates; feedback has not been frozen at finite width.

At a fixed nonzero forcing amplitude, the finite-program theorem identifies the forced run, the unforced run, and the new root jointly. In the relevant local scalar expression, that root appears through the designated source slot plus epsilon times the root. The Gaussian sources are independent of the local root. The selected expectations and covariance parameters can depend on epsilon, but are deterministic with respect to this local coordinate. Thus (60) differentiates exactly the right expression. Gaussian integration by parts in the fresh root extracts the expected source derivative without differentiating a singular-support extension.

The finite Cauchy–Schwarz bound passes to that joint limit. Dividing by the fixed nonzero epsilon bounds the expected derivative by `C_T h_s`. Only then is epsilon sent to zero, using the coefficient/derivative continuity already proved in §3.4. This establishes (61), including slots with zero unforced variance. Adding the explicit learned terms gives (62). The constants are uniform in the number of mesh nodes. This is a global finite-horizon estimate, not a local response bootstrap or an assumption inferred from the desired representation.

The bounded activations and bounded readout turn the row-sum bounds into (63). Integrating the first transformed equation gives (64). The Gaussian part has bounded variance by the sum of absolute coefficients times the individual standard deviations, and is independent of the full first row. Independence between the Gaussian part and the bounded remainder is not used or asserted.

For passage to the common-space flow, the cross-program covariance identities make the source maps isometries. Linearity on the input spans follows as well: the squared norm of any linear relation between the sources equals the squared norm of the corresponding input relation. Equation (56) therefore gives convergence of the Gaussian sources in L2 along with their inputs. Bounded remainders remain essentially bounded under L2 limits. The first-layer sums converge to Gaussian L2 integrals; their joint characteristic functions preserve Gaussianity and independence from the first row. These facts verify every assertion of (66). Joint measurability and Fubini suffice; no unproved sample-path regularity theorem for a Gaussian process is needed.

### 6. Paths, products, velocities, kernels, and probability quantifiers

The product estimate (67) is correctly used where L2 multiplication is not Lipschitz. The field with an unbounded magnitude is truncated; the bounded gate difference is handled in L2. The remaining square tail is controlled by uniform integrability. This avoids an invalid use of an L2 operator as an Lp operator.

The radial cap (68) is 2-Lipschitz in operator norm. Perturbing unscaled Gaussian entries by E consequently changes the capped operator by at most `2 ||E||_F/sqrt(n)`. Stability of the transformed flow, including comparison of different initial operators, cancels that square-root factor when bounding a single output coordinate. The same cancellation holds for perturbations of stored root arrays. Thus each coordinate supremum functional used for (72) has a dimension-independent Lipschitz constant.

Equation (70) is stronger than a supremum of L2 norms: it bounds the L2 norm of the pointwise time supremum. The pointwise integral inequality and Minkowski give its first step. The derivatives of the fields in (69) are bounded in L2 using (16), (23), (33), and (71); every operator action in this calculation is an L2 action. The conditional Gaussian inequality and the permutation/conditional-mean argument then apply to the supremum functional itself. This proves all-order supremum moments, not just fixed-time moments.

The Euler version follows with products of the factors `1+C_T h_k` and sums of increments. The additional readout clipping used only in this moment proof has uniformly bounded iid root moments and agrees with the actual readout with probability tending to one. Both auxiliary modifications can therefore be removed for convergence in probability. More explicitly, for q>p the probability that an empirical p-tail exceeds a given tolerance is bounded, on the agreement event, by a constant times `R^(p-q)`; the probability of disagreement tends to zero. No moment assertion on an exceptional event is needed for the stated probability mode of convergence.

For an unbounded first-velocity query, truncating Q makes the instruction globally Lipschitz. The L2 input tail is uniformly negligible by (72); the bounded operator controls the output error. The fixed-program theorem then applies jointly to all requested truncated probes. This validates (73), and the same reasoning works for the transpose and for the stated L2 closure of admissible probes.

For a fixed horizon T and a typical velocity V, the operative finite comparison has the form

`lim_{h down to 0} limsup_{n to infinity} P(sup_{t<=T} ||V_n^GF(t)-V_n^h(t)||_n > epsilon) = 0`.

The corresponding population comparison tends to zero in the common-space L2 norm, uniformly in time. At each fixed comparison mesh, only finitely many endpoint probes are required, and their joint law converges in probability. Stepwise evaluations at those endpoints suffice for this argument. These are the appropriate iterated limits: a tolerance is fixed, then a mesh, and only then a sufficiently large width. No width-dependent regression inverse or simultaneous growing-program limit is introduced.

Restoring the actual initial readout uses the same two Gaussian matrices and first roots in the auxiliary and actual finite flows. Equation (22) gives a transformed-state error bounded by `C_T ||W_n^(3)(0)||_n`, which tends to zero in probability. The uniform integrability estimates transfer the original fields and velocities. Raw GD is subsequently compared with the actual-readout GF. Thus neither comparison silently changes the model initialization.

For path laws, (74) follows by comparing a scalar absolutely continuous path to the endpoints of each observation interval and applying Cauchy–Schwarz. Its empirical or population average is an explicit squared transport bound. Applying it to the base tuple using (70)–(71), then letting the observation grid refine, proves Wasserstein-2 convergence on continuous-path space. The delta^(1) path is a continuous bounded-gate product of already included paths, with path norm dominated by that of Q. Higher supremum moments from (72) upgrade the path convergence to every fixed finite Wasserstein order. The first row is recovered by (18). No pairing between different neuron populations is needed.

The scalar predictions and kernel blocks are contractions of these fields. Blocks 2 and 3 are directly controlled in L2 on the state bounds. Block 1 additionally uses the Q supremum tails in (67). Fixed-mesh endpoint contractions converge jointly; the time modulus and mesh comparison control the whole interval. This verifies uniform convergence in probability of all three blocks separately, and of the prediction and loss.

For original forward velocities, the potentially difficult order is correct:

1. The transformed velocity and state converge by the Lipschitz estimates.
2. Equation (67) and Q supremum moments give the first preactivation and activation velocity comparisons.
3. Rank and readout velocities are Lipschitz on the state bounds.
4. The second preactivation velocity is the sum of an operator-velocity action and an operator action on the first activation velocity. Subtraction gives a uniform L2 comparison without multiplying by the second gate.
5. Its fixed-mesh law is identified by the already justified query approximation.
6. Equation (75) transfers square-tail integrability from finitely many fixed-mesh probes to the second preactivation velocity in the iterated limit.
7. Only after that step is the second activation gate multiplied in using (67).

Thus the UI needed for the final gate is obtained before using it; there is no circular argument. On the population space, compactness of a continuous L2 velocity curve gives the corresponding finite-cover argument. The comparisons give fixed-time joint Wasserstein-2 laws, uniform-in-time convergence of squared norms, and integrated mean-square comparisons under the stated approximations. They do not claim a continuous-path law for a discontinuous mesh velocity.

The first parameter metric is (18); the middle squared speed is exactly (76); the readout squared speed is its normalized L2 norm. Uniform norm convergence gives convergence of their time integrals and the individual forward hidden-velocity energies. For the operator increment, the rank integrand is continuous in HS norm with a uniform time modulus. The squared norm of a Riemann sum is a finite double sum of cross-time field contractions. Those contractions have already been identified, and the Riemann error is uniformly small. No HS norm of the initial operator is taken.

Finally, the raw-versus-GF estimates apply to the specified raw interpolation, including the one-sided convention at nodes. For base fields, a normalized error of order n^-3/2 gives a maximum coordinate path error of order n^-1. For delta^(1), the order n^-1 normalized error gives maximum coordinate error of order n^-1/2. Both vanish, so the same-neuron couplings transfer every fixed finite path Wasserstein order from GF to raw GD. Velocity norm and energy transfer use the already verified estimates (31)–(33).

The quantifier is each fixed finite T and each fixed finite family of tests or probes, with convergence in probability along the full width sequence. Exceptional initialization events are removed by their probabilities. The construction and all mesh limits use the same population flow on larger horizons. Nothing in this argument exchanges T tending to infinity with width or mesh limits.

### 7. Broader reading of “hidden-field velocity”: backward derivatives

For completeness, I checked that the existing estimates also support derivatives of the original backward fields in (5)/(10), if the wording at lines 194–197 is read that broadly. The essential formulas are

`dot delta_a^(2) = dot W^(3) phi'(Z_a^(2)) + W^(3) phi''(Z_a^(2)) dot Z_a^(2)`,

`dot Q_a^(1) = dot W^(2)* delta_a^(2) + W^(2)* dot delta_a^(2)`,

and, for an independent first coordinate with `dot Z_a^(1)=c_a phi'(Z_a^(1)) Q_a^(1)`,

`dot delta_a^(1) = c_a phi''(Z_a^(1)) phi'(Z_a^(1)) (Q_a^(1))^2 + phi'(Z_a^(1)) dot Q_a^(1)`.

The first two formulas are already (71). In the antiparallel reduction the coefficient in the last formula is the reduced control, and the two sample deltas and their derivatives agree.

The first formula uses bounded multipliers and the already established square UI of `dot Z^(2)`. Thus (67) gives its uniform L2 comparison. Applying the actual transpose in the second formula is legitimate after L2 truncation of its input; the same bounded-operator argument used in §4.2 identifies the query. Its square tails can be transferred from fixed-mesh approximations by (75), exactly as for `dot Z^(2)`.

For the last formula, Q squared needs L2 control, hence Q needs L4 control. This is available: (72) supplies arbitrary higher supremum moments, and the interpolation inequality (53) upgrades the uniform L2 Q comparisons to L4 comparisons in probability. At population level the same interpolation gives L4 continuity of Q. The original first equation is then a C1 L4 curve, and the along-curve chain-rule proof works with fourth powers as well. Holder justifies multiplying its differentiated gate by Q to obtain an L2 derivative. The bounded coefficient times Q squared has square tails controlled by higher Q moments; the other term uses the just-established square UI of `dot Q`. Equations (67) and (75) therefore give the same joint Wasserstein-2 and quadratic-energy conclusions.

Transfer of these derivatives from GF to raw interpolation also follows without a new scaling assumption. The maximum coordinate errors of the base fields tend to zero. The forward velocity errors from (32)–(33) give the comparisons in the first two displayed formulas. For `dot delta^(1)`, use its exact product-rule form on the raw interpolation, `phi''(z) dot z q + phi'(z) dot q`. For example, the term containing the first-velocity error is bounded by its maximum coordinate error times `||q||_n`; that maximum error is at most `sqrt(n) O_T(n^-1)=O_T(n^-1/2)`. The terms containing gate differences are controlled by the vanishing maximum base-field error and the GF higher moments. All such errors tend to zero in probability, uniformly in time. Their squared norms and integrated energies follow as before.

These deductions use the document's existing moment, interpolation, product, and probe lemmas. They do not require bounded L4 action of W, and do not assert the particular deterministic O(n^-1) rate for backward derivatives that §2.4 establishes for the forward velocities. The strict-speed and zero-time statements at lines 217–219 concern the explicitly listed forward hidden fields and parameter speeds; they should not be extended to backward-field derivatives, which can already be nonzero at zero.

### 8. Exchange symmetry, tails, nonaffinity, and persistent motion

The reflection (77) swaps the inputs because their norms agree. Under (78), forward sample fields are exchanged, readout signs are reversed, and every backward field is both exchanged and negated. The residual sign uses the antisymmetric labels. The loss and parameter metric are invariant, and the raw update equations commute with this transformation. The initialized finite law is invariant, including the actual symmetric Gaussian readout law.

A finite distributional symmetry alone would not impose an almost-sure antisymmetry on a finite run at correlation 0. The proof correctly passes through convergence in probability to deterministic scalar population observables. It consequently obtains `f_2=-f_1` and equality of the sample speed norms. At correlation -1 the stronger pointwise identities follow directly from the inputs. No finite pathwise identity at correlation 0 is assumed.

The first-layer tail proof uses an event on which the Gaussian integral is bounded, independent of the initial first row, and then a sufficiently far Gaussian tail of G. The bounded remainder cannot defeat that event. At correlation 0 the same construction works for every sign combination of the independent G_1 and G_2, giving support arbitrarily near all four activation corners. A nonzero linear functional cannot vanish at both `(B,B)` and `(B,-B)`, so the uncentered feature Gram is positive definite. At correlation -1 only the one-dimensional nonzero feature is needed; no inverse of the singular two-sample Gram is used.

Each second-layer Gaussian source has positive variance equal to the first-feature squared norm. The inclusions in (83) give both unbounded tails even if the remainder depends on the source. Thus all four preactivation distributions have positive variance and both unbounded tails at every finite time.

The affine span of 1 and Z is closed because its Gram determinant is `Var(Z)>0`. Consequently a zero approximation infimum in (14) would be attained. Boundedness of arctangent and an unbounded tail force the slope to vanish; strict monotonicity then forces Z to be constant. This contradiction gives a strictly positive infimum, rather than merely the absence of one arbitrarily selected affine representation.

Using the contrast `(f_1-f_2)/2=f_1`, rather than assuming an unstated kernel entry identity, (24) gives

`dot f_1 = (1-f_1) y^T K y = 4(1-f_1) kappa`.

The finite-horizon kernel bounds justify the exponential solution (85). The initial second-layer sources have covariance mI in the orthogonal case and the stated rank-one covariance in the antiparallel case. The initial readout-contrast feature is nonzero, so kappa is initially strictly positive. Monotonicity then gives `0<f_1(t)<1` for every positive finite time, and forces a nonzero readout.

Because the gates are strictly positive, every second-layer delta is nonzero. Its reverse Gaussian source is therefore nondegenerate; a bounded remainder cannot cancel its tails. The first-layer velocities in (88) are nonzero, as are their activation velocities and the first-parameter speed. For the middle parameter, (89) is the integrated pointwise positive-definite Gram inequality. At correlation -1 the reduced rank-one velocity has two nonzero factors.

I checked (90) independently. The first part of `dot Z^(2)` produces the HS inner product of `dot W^(2)` with itself. Moving the second part through the actual adjoint produces `sum_a c_a E[delta_a^(1) dot Z_a^(1)]`. It is the sum of the independent first-coordinate squared speeds. At correlation -1 it reduces to `(c_1-c_2) E[delta_1^(1) dot Z_1^(1)]`, with no extra factor two. The positive right side rules out simultaneous cancellation of both second-layer velocities. Exchange equality of the norms then rules out either one vanishing. The positive gates give the activation statement.

Finally, a zero readout velocity would make the second-layer contrast feature zero; its inner product with the readout would then contradict `f_1>0`. Continuity makes the energy on every positive-length positive-time interval strictly positive. At time zero, the stated forward hidden and hidden-parameter velocities vanish because the limiting readout and backward fields vanish.

### 9. Initial reverse law and the full-kernel coefficient

In (94), the factors `Gamma_n^-1` and `Z^T delta/n` exactly undo `H^T H=n Gamma_n`. The independent residual reverse matrix has row covariance `Sigma_n=delta^T delta/n`. Removing its projection onto the fixed-dimensional first-feature span costs a vanishing empirical moment by (47). It does not subtract a nonvanishing covariance from the limiting coordinate Gaussian.

Conditional on the first features, the initial second-layer rows are independent Gaussians with covariance Gamma_n. Their Gram converges to mI, or to the scalar m in the reduction. The row deltas are bounded, while the cross contraction with Z uses Gaussian moments. This gives precisely (92)–(93). The only inverse is that of the nonsingular reduced feature Gram. The full two-sample antiparallel Gram is never inverted.

The diagonal residual variances are positive. In the orthogonal case a linear relation between the two deltas would imply `lambda_1 phi'(u)+lambda_2 phi'(v)=0` off the diagonal for a full-support Gaussian pair. Varying one coordinate proves both coefficients zero. In the antiparallel case `phi(Z) phi'(Z)` is nonzero except on a null set. The conditional Gaussian component of the reverse field is independent of the initial first row and has positive variance, establishing (95).

The feature clock satisfies `ds/dt=4(1-f_1)>0` and `s(t)=4t+o(t)`. Dividing the physical equations by this derivative gives exactly (97), or coefficient one in the reduced antiparallel system. No raw time convention is changed.

The readout integral gives `W^(3)(s)/s -> widehat W^(3)` in L2. Bounded gates, continuity in measure, and operator-norm continuity then give (98). The initial orthogonal first-feature Gram is mI, so the two contributions to `Z_a^(2)'/s` are exactly

`(y_a/2) m widehat delta_a^(2)`

and

`(y_a/2) W^(2)(0) [phi'(G_a)^2 widehat Q_a^(1)]`.

These verify all coefficients in (99)–(100). The independent first-coordinate metric and the rank-one HS norm give (101). The adjoint evaluates the inner product in (102) as the sum of the nonnegative m-delta term and the squared gated reverse field. Equations (103) correctly remove both factors 1/2 and keep only one independent first coordinate in the antiparallel case.

The hidden part of kappa is the squared hidden parameter speed in feature time, so its leading coefficient is d_*. If `A=(H_1^(2)-H_2^(2))/2`, the readout part is `||A||_2^2`. Its derivative is exactly (105). Dividing by s gives

`sum_a y_a E[widehat delta_a^(2) widehat v_a^(2)] = 2 d_*`,

in both geometries. Integration yields a readout contribution `d_* s^2`, in addition to the hidden contribution `d_* s^2`. Thus

`kappa(s) = kappa(0) + 2 d_* s^2 + o(s^2)`

and

`kappa(t) = kappa(0) + 32 d_* t^2 + o(t^2)`.

The coefficient is strictly positive. The proof has therefore checked the full kernel, including a readout contribution that could not simply have been ignored; a positive hidden block alone would not have sufficed. The argument only uses strong first-order limits along curves and does not import a second Frechet derivative of the L2 nonlinear map.

For an intermediate nonzero correlation, differentiating F instead gives the ratio displayed at lines 1912–1913. It is not generally a bounded L2 multiplier. The stated exclusion of those angles is mathematically consistent with the actual argument.

## Required corrections

**None found.** The substantive estimates and limit arguments support the claims on the stated special-angle, fixed-finite-horizon scope. The independent checks above do not add a model assumption, a missing external theorem, or a numerical premise.

## Optional corrections and concrete clarifications

1. **Make the velocity list explicit — lines 194–204, 1259–1267, and 1383–1418; (71), (73).** The proof directly organizes §4.4 around preactivation/activation velocities. For the narrower intended terminology, replace “Every original hidden-field velocity” by “Each preactivation and activation velocity in (73).” For the broader reading including backward fields, add the displayed backward-derivative formulas and the L4 interpolation paragraph from this review's §7. Either version makes the scope easier to audit. The existing estimates support the broader version; no new Lp operator hypothesis is needed.

2. **State the range of the Gaussian moment inequality — lines 696–713; (43).** Add “for p>=1 and finite right-hand side.” This is the range used in the proof. The rotation/Jensen argument should not be read as a claim for arbitrary p between zero and one.

3. **Name the variance localization in the empirical induction — lines 784–804; (48).** Write “on a bounded event for the regression coefficients and sigma_n.” The coefficient sigma_n is tight by convergence of the input Gram. Including it explicitly makes the constant in (48) immediate and avoids making a reader infer that it is included in the existing bounded-coefficient event.

4. **Display the double-limit velocity quantifier — lines 194–197 and 1383–1418.** Add the uniform-in-time finite comparison formula given in §6 of this review and its population counterpart. This would make “integrated mean square under the approximations used below” precise at the theorem statement without suggesting an unstated direct identification of finite and infinite neuron labels.

5. **Specify fixed-program conventions near the probe definition — lines 179–192.** It would be useful to say explicitly that the finite instruction list, deterministic coefficients, and laws of added iid roots are fixed as width varies, apart from the expressly specified initialization and approximation limits. This is the convention actually used by the fixed-program proof and is consistent with the exclusion of arbitrary width-dependent directions.

These are presentation/scope clarifications. None changes the metric, physical clock, initialization, allowed angles, or mathematical conclusion audited here.

## Final source-integrity check

Post-write SHA-256 verification: `5cd54a6125dfbf4b7d1bc86149760b842d7d2c1f9a44fe73fcf57f5d3d15f12e`, an exact match to the supplied and initial hashes. The reviewed source is unchanged.
