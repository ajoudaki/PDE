# Independent mathematical review

**Verdict: PASS.** I found no unresolved mathematical correctness or completeness objection in the supplied manuscript. No required repair remains.

## Manuscript identity and isolation

- Input: `/tmp/report-ed1646d91004/REPORT.md`.
- SHA-256: `ad30e1e3ed36db9d1f36220859e3d40916aab4b26f892e478ccb850c9dbc7cd5`.
- Length: 3,826 lines; 223,246 bytes.
- The entire manuscript was read in the following consecutive, nontruncated chunks: 1–180, 181–440, 441–710, 711–1000, 1001–1280, 1281–1580, 1581–1900, 1901–2200, 2201–2500, 2501–2800, 2801–3110, 3111–3410, 3411–3700, and 3701–3826. There were no coverage gaps.
- The manuscript was the sole reading input. I did not read skills, AGENTS files, source notes, project state, other manuscripts, reviews, or agents' work; I did not browse or run numerical experiments. I did not edit the input. This review is the only output file I created.

## Findings and proof checks

### Model and theorem: Part M

The finite gradient factors agree with the displayed raw metric. In particular, the first block's Euclidean derivative is multiplied by `n/d`, the readout derivative by `n`, and the normalized rank-one hidden updates have the stated Frobenius/Hilbert–Schmidt interpretation. The finite readout variance and its vanishing normalized norm are consistent with a zero population initial readout, without changing the actual finite initialization.

The finite-dimensional gradient-flow continuation argument is valid: energy dissipation bounds the integral of squared raw speed, and Cauchy–Schwarz makes the path Cauchy at a finite endpoint. Local finite-dimensional existence then extends it. Global finite-step definability of raw GD does not require a descent assertion.

The theorem distinguishes the four required notions: global population existence, convergence on each fixed physical horizon, time-uniform nonaffinity of the population fields, and initial motion. It does not interchange infinite training time with width. Its law observables are correctly restricted to same-layer tuples, and its path laws concern continuous forward fields, while raw-GD velocities use the specified one-sided directions. The full first-weight norm's dimension dependence is explicitly accounted for rather than being used as a uniform activation-selection bound.

### Gaussian program and functional analysis: Part F

I checked the adaptive conditioning induction, including interleaved reuse of both matrices in both orientations. Conditioning on the existing transcript fixes each next query input; the new linear observation updates only the queried residual Gaussian matrix. This justifies the conditional product structure used in the induction.

The minimum-Frobenius-norm conditional mean in (F.6) satisfies both observed constraints by the compatibility identity. Its orthogonality to the homogeneous constraint space gives the stated residual Gaussian projection. Formula (F.7), the normalized variance factor, and the negligible finite-rank noise projection have the correct normalization. Conditional tests and second-moment estimates suffice for joint empirical Wasserstein convergence; no independence of trained coordinates is assumed.

The source rules retain response terms from the opposite orientation and all previously available derivative paths. Gaussian integration by parts is justified by the finite expression's bounded source derivatives and linear growth. Separate independent oriented source groups are compatible with dependent forward/reverse answers because the return terms are retained.

Singular query Grams are handled by a genuine two-limit argument. Fresh input noises make the relevant limiting Schur complements positive; finite coupled errors are bounded using initialized operator norms. The zero-noise scalar recursion is continuous through covariance square roots and bounded formal derivatives. No continuity of pseudoinverses, differentiation of covariance parameters, or rank-stability assumption is used. The singular-support invariance claim concerns the contracted correction, which is the quantity invariant under changes of formal expression.

The Gaussian operator norm bound, its moment extension, and the independent Gaussian trace-probe variance identity have valid constants and hypotheses. They support the later expectation limits for fixed polynomial observations.

The common-space construction includes a countable dense coordinate language and both action orientations. The finite operator inequalities pass to the generated span; density permits extension; finite adjunction passes to the actual Hilbert adjoints. This does not require operator-norm convergence of unidentified matrices across widths. The Hilbert–Schmidt identities and the finite normalized rank-one correspondence are correct.

The distinction between a curve chain rule and an ambient L2 Nemytskii Fréchet derivative is respected. The bounded-multiplier argument is valid. The weighted scalar Taylor estimate proves the scalar predictor's continuous Fréchet differentiability by successive top-down expansion, with all mixed parameter/field errors controlled. It supplies the true raw gradient and the four positive-semidefinite kernel blocks.

Fixed-cap local existence and Euler consistency follow from bounded first derivatives of the capped gate on a primal ball. Their constants are width independent on the specified initialized-operator event. The finite-program theorem is applied at fixed program size; the Euler estimate, rather than a growing-program claim, handles subsequent refinement.

### Controlled responses: Part R

I checked the response equations (R.11)–(R.16), their sample indices, learned rank-one terms, and chronological order. Current transpose returns are present, and the bottom transpose retains its derivative through the already constructed current middle return. Controls and residual-derived numerical coefficients are correctly frozen in source derivatives.

The affine comparison uses an explicitly stated finite-Euler primal hypothesis. Its raw-distance Lipschitz bounds and perturbation forcing constants dominate the relevant first-projection, operator, and readout changes. The Gaussian probe is applied at fixed nonzero amplitude and fixed mesh before amplitude tends to zero. It bounds absolute sums of expected derivatives by deterministic sign choices; it does not exchange a width limit with differentiation or confuse an expected derivative with the expectation of its absolute value. A single past insertion retains its mesh factor.

The nonlinear-to-affine primal comparison uses only the bounded nonlinear perturbation and affine Lipschitzness. It therefore supplies source variance and learned-moment bounds before a nonlinear response estimate is available. This prevents circular use of response coefficients to control the same variances needed to prove them.

The coordinate moment recursions use maxima of deterministic Lp norms and time-weighted sums, rather than unproved random time-supremum or Lp operator bounds. Their Gaussian inputs have variance bounds already obtained from the primal comparison. The exponential envelope estimate uses convexity and is valid for arbitrarily correlated time sources.

The differentiated equations include both partial derivatives of the capped gate, including the derivative of the clip. The terminal incoming-field multiplier is retained in the backward derivative bound. Its integrability is obtained by Hölder and the already established Gaussian-type moments. The same-array affine derivative comparison is separated from comparison with the actual affine baseline arrays.

I checked the deterministic difference recursions, the single-source-step factors for unequal meshes, and the coefficient chain through (R.90). The closure is chronological: bottom forward response, upper forward response, top transpose response, then lower transpose response. At each stage all current quantities needed by its remainder have already been bounded. The scalar product bound and the factor in the definition of K_* dominate the sum of the two backward-row errors. The base case at zero readout retains formal zero-variance source slots correctly. Thus the selected threshold is positive, finite, and uniform in cap, mesh length, mesh cardinality, controls, and admissible covariance.

### Geometry and global construction: Part G

The augmented-Gram bound handles singular input Grams. The mixed-sign reduction, determinant `D^2`, trace bound at most four, and comparison of coefficient norms give the claimed lower eigenvalue. The separation range and the example exhibiting quadratic dependence on separation are consistent.

The Gaussian affine projection in (G.3) is valid without parity assumptions and also with singular covariance. Its residual Gram is positive semidefinite. Iteration gives the initialized readout coercivity at the stated scale. The initialized scalar standard deviations lie in the stated finite interval.

The existence of an interval with positive affine-regression distance follows from continuity, overlap of intervals, and bounded nonconstancy. The Gaussian density lower bound on that interval gives the claimed margin. The perturbation of the regression margin is valid for arbitrary nearby L2 random variables: standard deviation is Lipschitz, the optimal slope is bounded by two, and the error is at most three times the L2 displacement. The activation margin is exactly e squared times this regression residual.

The controlled bounds apply to arbitrary positive Euler meshes as well as continuous controlled paths. The discrete identity involving the sum of `h_j s_j` prevents a first overshoot. The affine hypothesis used in Part R is consequently established at finite width on an initialized high-probability event, rather than inferred from a continuous population bound.

I checked the numerical inequalities in the selection of a, S, C_S, and D_S, including the displacement margin and readout-Gram perturbation. The large-gain requirements imply the displayed strict slacks. The capped hidden contribution to the prediction equation is treated as potentially nonsymmetric; its operator norm, not a gradient dissipation assertion for the surrogate, is what allows readout coercivity to dominate it.

The residual-clock argument is stopped before its assumptions could fail and proves an upper bound of S/2, excluding that stop. It supplies global capped existence and a single response threshold for every physical horizon. Transfer of the controlled moment bounds first uses sufficiently fine fixed-cap physical meshes on each horizon. The subsequent uncut construction invokes only the internal cap-transfer proof in Part V, whose hypotheses have been supplied.

### Actual finite algorithms, true kernels, and velocity laws: Part V

The asymmetric gate estimate compares the unrestricted or larger-cap state to a reference whose incoming fields alone need tails. Successive backward substitution produces a single factor linear in the reference cap; each cap-dependent factor multiplies a forward discrepancy, and all propagated incoming discrepancies are multiplied only by bounded gates and actions. The three residual coefficients are compared through the raw-state forward estimate. Gaussian reference tails beat the resulting exponential in cap.

This yields uniform strong convergence of cap states and raw directions. The limit solves the autonomous uncut equation and is C1. The same reference-only comparison proves uniqueness among bounded-primal strong competitors, including continuation from a reached state. No unproved local well-posedness theorem for arbitrary uncut L2 states is required.

The additional fixed-cap Gaussian-probe argument obtains source-row bounds with constants uniform in mesh. It recomputes finite residuals during perturbations while correctly freezing their deterministic limits in formal source derivatives. Its primal events follow from fixed-mesh observations and exact update lengths, independently of the source-row estimates. The later pathwise absolute derivative rows are obtained by an explicit causal recurrence, not by replacing absolute expectations with expectations of absolute derivatives.

The hidden velocities are actual chain-rule velocities. Their upper-layer formulas include the trained action applied to the lower feature velocity. The appended initialized-action queries retain all same-family source covariances and all relevant reverse response terms.

The use of the unbounded product `phi'(z) P` is justified in an appropriate order. Bottom product clipping gives integrable derivative domination from primary moments and derivative bounds before the first velocity action is identified. That first action supplies the moments and reverse-source derivative bounds for the second velocity action. The nested inner/outer clipping limits then establish the second response formula. Thus the argument does not invoke the bounded-derivative theorem directly for an unbounded-derivative product, and does not assume the velocity moment bounds it is establishing.

The deterministic velocity comparison truncates only a reference velocity. It has a single tail cutoff factor multiplying the already controlled forward-state difference. The population and finite Euler comparisons respect recomputation of hidden fields from raw interpolation; the fine algorithm's direction is evaluated at its actual preceding mesh node. Fixed-cap empirical tail control follows from Wasserstein convergence of finitely many coarse-node observations and subsequent refinement, not from an unsupported finite-width fourth-moment estimate.

The actual finite random readout is retained throughout both training algorithms and all same-width cap comparisons. Its vanishing discrepancy is used only to identify a fixed-program population initial condition. Finite reference operator bounds come from initialized norms plus sums of rank-one update lengths. Stopped same-width comparisons rule out finite-horizon exits with probability tending to one.

The true backward fields and the capped update fields are explicitly different. Section V.8 appends and truncates the true backward chain, passes its actual transpose actions, and obtains the full fixed-cap observed kernel. The subsequent uncut transfer can use capped update fields as direct references because the asymmetric estimate compares them to the true uncut fields. The four raw kernel blocks and their off-diagonal entries are all covered.

For actual raw GD, the comparison uses the field at the preceding GD node and a cap-reference within-step error. The only vanishing-step requirement is the deterministic Euler defect; there is no hidden appeal to a Gaussian theorem with a width-dependent transcript or to a width-independent uncut Lipschitz constant. This includes the stated step n^-2. The analogous actual finite GF comparison is valid, and both can use the same initialized reference.

The final velocity cap removal has the necessary tail order. Strong L2 continuity of the uncut velocity gives compact time images with uniformly vanishing tails. Cap velocities converge against that reference first; finite reference tails then pass at fixed cap and tail level. Taking cap to infinity before the final tail-level limit avoids multiplying a cap-dependent velocity moment constant by the cap-removal error.

The path-space argument is complete. Almost-everywhere absolutely continuous coordinate versions follow from the strong integral representation and Fubini. The observation-grid interpolation error is bounded in mean squared supremum norm by four times the mesh size times the integrated squared RMS speed. Joint node convergence followed by observation-grid refinement therefore gives the claimed path Wasserstein limit. Uniform-time velocity Wasserstein convergence gives uniform second-moment convergence and convergence of integrated squared speeds. Generated probes and both initialized/current action orientations pass by bounded-action continuity and finite Riemann approximation of learned increments.

The derivative-valid initialization extension V.I separately justifies the uncut backward response coefficients used in Part N. Its ordered truncations have integrable domination, and its Gaussian covariance passages use square roots rather than inverse covariances.

### Initial motion and projected-kernel variation: Part N

The functional `E = ||sum p_i h_i^3||^2/2` has the stated continuous scalar Fréchet derivative. The proof uses the weighted Taylor estimate with fixed backward weights and the quadratic forward difference term; its hidden raw gradient is exactly V.

Positive definiteness of the first two initialized feature Grams makes the top forward Gaussian full-support. The proof that S_3 is positive definite is valid for every nonconstant bounded C2 perturbation: the first factor in (N.11) has no open zero set, and the derivative of the second factor forces each coefficient to vanish because `psi''` is not identically zero. The exact reverse-source formulas then supply the conditional covariance lower bounds for S_2 and the bottom fields. They prove positivity of all hidden parameter blocks and every individual bottom sample even when the input Gram is singular.

I checked the exact affine expressions for the two upper sample directions. Their coefficients, powers of a, and dependence on each individual gamma_j are consistent with the affine feature Grams. The finite Gaussian covariance calculation for Q, the normalized trace identities, the even/odd cancellation in B, and the row-sign/permutation invariance argument are valid. The manuscript establishes deterministic trace limits and uniform integrability before passing the finite expectation inequalities to the population; fourth-moment expectation calculations alone are not being used as concentration.

The quadratic completions in (N.30) and (N.37) give the displayed positive lower bounds, using the binary-label fact `|sum p_i| >= 1/3`. The explicit nonlinear perturbation estimates compare constant affine gates to perturbed gates and require only the assumed derivative bounds. Their stated cutoff preserves more than half of both upper-sample affine lower bounds. No parity, analyticity, asymptotic limits, or monotonicity of the perturbation is needed.

The physical acceleration factors are correct: C'(0)=3H, the backward fields divided by t tend to 3 beta, the hidden raw velocities divided by t tend to 9V, and the hidden displacement is `(9/2)t^2 V + o(t^2)`. Strong multiplier continuity and operator continuity justify these limits with only C2 activation regularity. The induced preactivation and feature accelerations are nonzero for every sample and every hidden layer.

The projected total kernel is the squared full raw gradient of the projected predictor. Its hidden part contributes `9 t^2 ||V||^2`; the readout feature-energy change contributes another `9 t^2 ||V||^2`. This proves the coefficient 18 in the claimed expansion, for the actual total kernel along physical training.

### Uniform classes and examples: Part A

The shared interval-margin recipe follows from the same uniform derivative bounds and the interval density argument. The neighborhoods described are infinite dimensional and retain the stated regression margin by the Lipschitz property of distance to a closed affine subspace.

For functions with distinct limits at the two infinities, the limiting Gaussian regression residual is the squared half-gap times `1 - 2/pi`. Continuity on compact scale intervals and positivity at each scale give a positive infimum over scales at least one. The arctangent neighborhood construction preserves this lower bound by uniform perturbation, and the alternate quartic gain selection gives the required fixed displacement radius. The normalized example functions satisfy the stipulated bounds after scaling. The compact-support observation correctly explains why the general theorem uses a finite initialized variance range rather than a universal all-variance margin.

## Required repairs

None. The manuscript supplies the specialized hypotheses and arguments needed for its advanced constructions, separates its auxiliary objects from the actual raw algorithms and true kernels, and orders all width, mesh, cap, and product-truncation limits needed for the stated conclusions.
