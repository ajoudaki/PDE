# Independent adversarial review

**Input:** `/tmp/proof-ef1cd41278f3/REPORT.md`

**Exact input SHA256:** `cd62425a6d8ae0ca7351bb6e71b31cd0b4eb7266263e53e377f976bab261e037`

**Reading coverage and sole-input compliance.** I read the entire input, from its title through the last sentence of “What remains unresolved,” including every displayed equation and both parts. The report was my sole mathematical input. I did not read skills, other files, previous versions, project notes, other reviews, websites, or other agents’ analyses. I performed no experiments and did not modify the input. The checks below are mathematical checks of the supplied text.

## Verdict

**FAIL as a completion or certification of the requested global trained-limit theorem.** The report supplies neither a positive sufficient cutoff `theta_*(delta,L)` nor a proof or disproof of a depth-independent cutoff. The missing conclusions and hypotheses are substantive and are listed below. This verdict does not assert that the requested theorem is false.

**PASS for the mathematical correctness of the explicitly stated partial results.** I found no substantive correctness error in the finite-width gradient-flow setup, initialization identification, sharp initialization theorem (A), normalized theorem (B), scalar asymptotics, or the conditional continuation theorem in Part II. In particular, I checked the conditional functional-analysis argument rather than treating it as an assumed black box. This limited PASS does not certify the unresolved global theorem. The report itself generally maintains this distinction clearly.

## Substantive completeness objections

1. **The principal requested conclusion is absent.** No strictly positive sufficient `theta_*(delta,L)` is established for the global canonical trained flow and the requested joint limits and dynamical properties. Proving positive definiteness for every positive mixture at initialization does not discharge this obligation.

2. **The depth-independent cutoff question remains open.** The decay of absolute initialized covariance and scalar regression gaps rules out a depth-uniform positive numerical margin. It does not rule out one positive mixture cutoff working for every separately fixed depth with depth-dependent constants. Conversely, normalized initialized coercivity does not prove that such a cutoff exists.

3. **Existence and boundedness of the auxiliary trained reference flows are hypotheses.** Part II assumes reference flows on each horizon and the uniform-in-cap primal bound (II.3). Neither is proved for the canonical references. The finite-width energy identity concerns the true gradient field; it does not by itself prove these assumptions for the auxiliary capped backward fields.

4. **The crucial source-tail condition remains unproved.** Condition (II.4) must hold uniformly over caps, times, layers, and samples. A raw second-moment bound does not imply it. The report’s own top-layer construction correctly demonstrates this failure. Curvature decay alone does not remove this missing obligation, as the differentiated-gate example with constant preactivation also correctly shows.

5. **The conditional Hilbert model is not identified as the canonical trained width limit.** Part II permits arbitrary bounded base actions and Hilbert–Schmidt increments. It does not construct the canonical Gaussian initialized action model, identify trained dependence structures, or prove that the finite-width trained networks converge to that model. The initialization covariance recursion cannot provide that identification after training starts.

6. **The requested trained approximation and observation conclusions are not proved.** The report does not establish the joint finite-width GF/GD trained path, kernel, and velocity limits, nor the required all-time trained-law nonaffinity and motion properties. A continuous population vector field and a conditional population solution do not automatically yield those separate conclusions.

7. **The global and depth quantifiers remain conditional.** The global gluing argument in Part II is valid if its compatible reference hypotheses are supplied on every finite horizon. Those hypotheses are not supplied. The initialization width limit also keeps depth fixed before width tends to infinity; its uniform deterministic bounds over integer depths do not establish a simultaneous depth/width limit.

These are incompleteness objections to the requested theorem, not hidden errors in a theorem that the report falsely claims to have proved. The report expressly acknowledges them.

## Full mathematical audit

### Finite model and initialization identification

The raw metric factors and gradient equations agree. Differentiating the predictions produces a factor `1/n`; the first block’s inverse metric supplies `n/d`, the intermediate blocks retain `1/n`, and the readout inverse metric removes `1/n`. This also gives exactly the displayed three types of prediction-kernel blocks.

The finite-width global GF argument is valid: energy dissipation bounds displacement in the positive-definite finite-dimensional raw norm and makes the path Cauchy at any finite proposed terminal time. Smooth local existence then continues it. Everywhere-defined finite GD updates give every finite node, without implying any width-limit statement.

The conditional Gaussian induction is sound, including singular limiting Grams. The bound on conditional product variance is `3 M^2`; conditional row independence supplies the `1/n` averaging factor. Covariance continuity follows from square-root coupling and the activation’s Lipschitz and linear-growth bounds.

The operator-norm net calculation is valid: the `1/4` nets have at most `9^n` points, bilinear approximation gives the factor two, and the displayed Gaussian union bound vanishes. Only square hidden matrices need this bound. The initialized backward norm is of order `1/n` in probability at fixed depth because the normalized readout second moment is `n^{-2}`. Consequently every hidden kernel block vanishes, while the readout block converges to `Q_L`.

### Part I.1: scalar bounds

The Gaussian integration-by-parts identities, Jensen lower bound on `c(q)`, and projection bound `q_+ >= q/4` are correct. The decrement bounds give the displayed reciprocal increments with constants `1/4` and `8`. Both variance estimates in (3) follow.

For (4), summing the lower decrement bound gives `sum q_k^2 <= 4/theta`; comparison with the integral of `(1+8 theta x)^{-2}` gives `sum q_k^2 >= L/(1+8 theta L)`. The additional inequality using the constant five is valid on both sides of `theta L = 4`.

### Part I.2–I.3: Hermite kernels and retained linear covariance

The Hermite normalization and correlated-pair identity are correct, including correlations `+1` and `-1`. The supplied completeness argument establishes the required density: the imaginary-argument generating series converges in Gaussian `L^2`, and the stated Gaussian-convolution argument proves Fourier uniqueness for the resulting integrable density. No unproved specialized Gaussian-kernel result is needed here.

The derivative identities follow by integration by parts and Parseval. Finite nonnegative derivative sums justify endpoint derivatives and continuity. The absence of even and constant coefficients is essential and is respected.

The residual projection bound is `(5/3) theta^2 q^3`. Since `c(q)^2 >= 1/4`, it gives the stated logarithmic first-chaos bound. Summability then yields the uniform consecutive-product lower bound `exp(-80/3)`. This bound is valid jointly in depth and mixture size.

### Part I.4: cubic lifting and lower constants

The tensor witnesses in (10) are unit vectors and annihilate the other two cubic tensors. Their retained inner products are at least `delta(2-delta)`. Summing the three coefficient estimates yields precisely the factor `1/3`. This argument does not require the original Gram to be invertible.

The cubic arctangent coefficient in (11), including its sign and normalization, is correct. Jensen under the probability measure weighted by `G^2` yields the bound `1/16`, hence `b_3(q)^2 >= q^3/384` and `w_3(q) >= theta^2 q^2/384`.

All discarded entrywise-power terms are positive semidefinite tensor Gram matrices. Iterating the linear retention plus cubic injection gives (13) and (14). Using `1+8 theta L <= 8(1+theta L)` produces exactly the lower constant `exp(-80/3)/73728` in (A).

### Part I.5: composition, upper constants, and strict example

The composed kernel has a nonnegative odd-degree expansion. The second-derivative estimate is `b_k <= 16 theta^2 q_k^2`, and odd degrees at least three give `d_k-1 <= b_k/3`. The derivative recursions and the exact formula for `B_L` are correct. They imply (17), with the stated factor `80 exp(128/3)`.

The planar example belongs to the strict admissible class for the whole stated range `0 < delta <= 1/4`. In particular, the last strict inequality remains positive at `delta = 1/4`; no closure-to-strictness argument is being silently used. Its original Gram is singular, and the test vector has squared norm at least three.

The expression for `E_n`, the identities at `c=1`, and its second derivative are correct. The bound `40 n^2-16 n+8 <= 54 n(n-1)` holds for every integer `n >= 3`. Taylor’s remainder and tensor-Gram positivity give the claimed quadratic bound. Dividing by the test-vector norm gives the factor `36 delta^2` in (20). Finally, `36 * 80 * 4 = 11520`, yielding exactly the upper constant in (A).

Removing the variance factor gives (B). Thus the proved joint order is indeed `delta^2 theta^2 L/(1+theta L)^2` in absolute scale and `delta^2 theta^2 L/(1+theta L)` in normalized scale, including `theta L` small, bounded, or large. The argument does not substitute a first-layer approximation at large depth.

### Part I.6–I.7: asymptotics, obstructions, and scope

The variance asymptotic follows from `D(q)/q^2 -> 2 theta` and averaging reciprocal increments. The arctangent remainder is controlled in Gaussian `L^2`; projecting the cubic term leaves `H_3`, whose squared norm is six. This proves the coefficient `2/3` in (22). At fixed positive mixture, the activation gap and its fraction of feature variance have the stated asymptotics `1/(12 theta ell^3)` and `1/(6 ell^2)`.

The normalized lower bound is compatible with vanishing per-layer regression gaps because the proof retains earlier covariance contributions. The absolute bound cannot remain uniformly positive over depths, since the diagonal itself tends to zero.

The affine equilateral obstruction is algebraically valid: the three inputs sum to zero, every bias-free linear network preserves that relation, and equal positive labels cannot be fitted. Zero readout gives the stated stationary affine field, and polynomial bounded-action dynamics have local uniqueness. This observation supplies no existence argument for the canonical positive-mixture dynamics.

The Gaussian mean is zero, so a positive constant-chaos lift cannot be inserted. The report correctly uses cubic lifting instead. Pairwise separation propagation is an initialization statement throughout the proof; no trained separation propagation is established or legitimately implied.

### Part II.1–II.2: state space and gates

The affine Hilbert state space is complete in the raw increment norm; the sum norm is equivalent at fixed finite depth. The first-block normalization matches the finite model. Bounded actions and their true Hilbert adjoints make the displayed forward and backward expressions well defined, and rank-one updates are Hilbert–Schmidt.

The proposed cutoff exists. The gate derivatives in (II.5) are correct, its incoming-field Lipschitz constant is at most one, and its preactivation Lipschitz constant is finite at every fixed cap. The sharper derivative bound for `N_R` integrates between absolute preactivations because both `N_R` and `g` are even and the latter is monotone in absolute value.

The global secant bound (II.6) is correct. The Rayleigh-quotient calculation yields the stated intermediate maximum and then the bound `1/s(bar z)`.

Importantly, (II.7) remains valid when the moved point clips but the reference point does not. One changes the incoming field at the moved point, compares the same cap between the two preactivations, and only then compares caps at the reference point. On the reference good event both caps agree there with the true gate; on the bad event the two nonlinear terms have total magnitude at most `2 |bar q|`. Only reference tails are required. Infinite caps obey the same argument.

### Part II.3: propagation and common constant

The forward bounds use the sum distance to absorb the telescoping contributions without a missing factor of depth. The backward recursion (II.9) has the correct operator-norm and adjoint factors. Downward substitution gives the deliberately loose (II.10).

The threshold `M` multiplies only forward discrepancies. It does not multiply an already accumulated backward discrepancy, so only one power of `M` occurs at any fixed depth.

I checked the common constant in (II.11). For a matrix block, inserting (II.8)–(II.10) bounds its discrepancy by

`B^(4L+1) [6(L+3)(1+theta M) d + 12 theta L T_M]`.

The first and readout blocks satisfy no larger common bound. Summing at most `L+1` blocks is safely below the displayed `100(L+1)^2 B^(4L+4)` for `B >= 1`, `L >= 1`. Thus the constant and its dependence are valid.

### Part II.4: convergence, directions, uniqueness, and continuation

The variable threshold is admissible while the stopped process remains below `A exp(-c)`, since `u >= A exp(-cR)` guarantees `M <= R`. It yields an Osgood differential inequality. Scalar comparison gives an upper bound for `u` itself with the right-hand side of (II.12); for sufficiently large caps this closes the stopping argument on every fixed finite horizon. The estimate is asymptotic in sufficiently large caps, not an unconditional finite-cap estimate for arbitrary horizons.

Taking `M=R/2` then proves uniform Cauchy convergence of directions, because a linear factor in `R` times the exponentially decreasing bound tends to zero. Uniform convergence of states and directions in the complete raw space identifies a strong `C^1` path by the integral equation.

The true gate is continuous on `L^2` pairs even though it need not be locally Lipschitz there: separate the incoming-field discrepancy and use bounded multiplier convergence in measure against a fixed square-integrable field. Subsequence dominated convergence gives norm continuity. Bounded operator composition and rank-one continuity complete the finite-depth argument. The reference-tail estimate also directly identifies the limiting direction with the true field.

The one-sided reference estimate supports comparison with every bounded-primal strong true-gate competitor. No tail assumption on that competitor is silently introduced. The limiting state’s exponentially small discrepancy from a cap reference at a reached time is enough to repeat the Osgood comparison, so continuation uniqueness is valid. Compatible constructions on finite horizons glue by uniqueness. This proves exactly the conditional global implication stated, with no necessary smallness coupling of mixture, depth, and horizon inside that implication.

### Part II.5 and the closing unresolved statement

The example `Z=Q` correctly makes the ratio tails vanish above one without forcing ordinary exponential tails. The explicit top-layer Hilbert–Schmidt modification is permissible and makes the chosen preactivation equal to one. Its weighted tail square is exactly `3/(sqrt(2) u)`, contradicting any exponential tail estimate with fixed positive exponent.

For the differentiated-gate example, `Q=J=U^(-1/3)` are both square integrable while their product is not square integrable. At constant `Z=1`, the curvature factor is nonzero and cannot help. The report correctly limits these examples to allowable states rather than asserting their reachability by training.

The final unresolved statement accurately describes the limitations of the proved results. No counterexample in the report, or in this audit, settles the positive-mixture global theorem or the depth-independent cutoff question.

## Certification boundary

The initialization theorems and the conditional continuation implication pass this audit. The full requested global trained theorem fails the completeness test because its central dynamical hypotheses and limit arguments remain unproved. No global theorem is certified by this review.
