# REVIEW — CLEAN

Verdict: **CLEAN** for the theorem as stated: each separately fixed finite hidden depth `L >= 3`, the specified one-input/label-one model and initialization, and convergence on each fixed finite physical-time interval. I found no proof gap requiring a mathematical correction. This verdict does not extend the result to a joint depth/width limit, an increasing sequence of physical horizons, or convergence of finite optimizers at infinite time.

## Scope and exact input manifest

I read all 98 lines of the notation contract and all 1,796 lines of the chapter, including every displayed calculation and the final activity argument. The review used only these two inputs. No history, repository material, other reviews, web sources, agents, experiments, or external mathematical results beyond the chapter's stated classical background were consulted. Neither input was edited.

SHA-256 hashes below identify the exact inspected bytes; byte and line counts are from `wc -c` and `wc -l`.

| Input | Bytes | Lines | SHA-256 |
| --- | ---: | ---: | --- |
| [NOTATION.md](/tmp/pde-global-round1.NdaWhM/NOTATION.md:1) | 5,110 | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| [global_nonlinear.md](/tmp/pde-global-round1.NdaWhM/global_nonlinear.md:1) | 83,472 | 1,796 | `becfba469f81bc4573275bc679aa3ee102f2e553c03c00357c3268792a556c95` |

All chapter line references below refer to this hashed version.

## Required fixes

None found. In particular, the population construction, finite-width approximation, exact raw-GD comparison, nonaffinity, and persistent hidden activity have separate arguments; the later conclusions are not obtained merely by asserting that existence or loss decay implies them.

## Optional clarifications

1. **Distinguish formal zero from almost-sure zero in the initialization of the response induction** (lines 832–836). The top delta is identically zero as a formal expression. An interior delta at initialization need only vanish under its degenerate source law. For example, with the upper response row zero, its expression is `phi'(xi_0) tau_R(zeta_0)`, where `zeta_0 = 0` almost surely, but its formal derivative with respect to `zeta_0` is `phi'(xi_0)`, not zero. The sentence “Downward induction gives the same for all deltas and rows” could explicitly make this distinction. This is not a required correction: the stated formal-derivative convention and the subsequent derivative recurrences retain precisely this derivative, and the forward-source response row at time zero still vanishes.
2. **Define or replace “MF”** at line 1406. “Population/GF/GD convergence” would avoid the otherwise undefined acronym. This has no mathematical effect.

## Proof coverage

“Pass” means I checked the obligation against the contained argument and found no necessary missing step. It is an assessment of the proof provided, not an extension of its quantifiers.

| Obligation | Location | Assessment |
| --- | --- | --- |
| One input, label one, fixed common activation, tiny stored readout, exact mobility and loss factors | Notation; §1, lines 30–170 | Pass. The model, raw updates, kernel normalization, and time factor agree. |
| Bounds, elementary probability and convergence tools | §2, lines 181–275 | Pass. Constants and normalization are consistent; the continuity tools accommodate bounded gates multiplying unbounded `L^2` factors. |
| Adaptive Gaussian reuse and true transposes | §§3.1–3.2, lines 293–392 | Pass. Conditional projection is for the same matrix; fresh randomness is only its unobserved Gaussian residual. |
| Joint empirical laws and second moments | §3.2, lines 374–392 | Pass. Conditional averaging is applied to new innovations, not to falsely independent reused coordinates. |
| Gaussian source/response rule | §3.3, lines 394–451 | Pass. The response coefficient is derived from regression and integration by parts, with the full input second moment as source covariance. |
| Singular limiting Grams and formal derivative convention | §3.4, lines 453–499 | Pass. Fixed-program input perturbation, a width-uniform finite comparison, and causal scalar continuity remove the need to take limits of singular inverses. |
| Actual empirical feedback, not just an oracle | §4, lines 501–636 | Pass. Fixed-program contraction errors are restored by a finite Lipschitz induction. Current reverse responses are included. |
| Common probability spaces, bounded initial actions, actual adjoints | §5, lines 640–685 | Pass. Consistent finite laws, a dense generated domain, and inherited norm/pairing identities provide one fixed operator realization. |
| Primal bounds, fixed-clip existence and mesh comparison | §5, lines 687–810 | Pass. Bounds are independent of width and cap where claimed; fixed-cap local Lipschitz estimates suffice for construction and Euler comparison. |
| Response control uniform in mesh, cap, and depth | §6, lines 812–994 | Pass. The forward/time/backward induction closes with the displayed constants. It needs no temporal independence. |
| Clip removal, uncut existence, uniqueness, reached-state restart | §7, lines 996–1085 | Pass. Linear cap dependence in stability is dominated by the Gaussian tail bound, including a restarted initial discrepancy. |
| Finite uncut feature-flow convergence with actual readout initialization | §8, lines 1087–1130 | Pass. The bounded reference readout and continuous tail statistic handle the small unbounded competitor readout. |
| Hilbert gradient structure, physical clock, loss decay, raw uniqueness | §9, lines 1132–1258 | Pass. Scalar Fréchet differentiability is justified without asserting unrestricted `L^2` Nemytskii differentiability. The clock reaches every finite physical time. |
| Finite physical GF and exact raw GD | §10, lines 1260–1411 | Pass. Finite GF continuation, the cubic defect, stopped positive-step comparison, clock comparison, and removal of the stopping conditions are all supplied. |
| All specified probes, kernel blocks, hidden velocities and paths | §11, lines 1413–1525 | Pass. The argument supplies tail truncation, actual interpolated-GD velocity control, joint time laws, and the path interpolation estimate. |
| Initial movement and a nonconstant total kernel | §§12.1–12.2, lines 1529–1684 | Pass. The initial transpose induction and adjoint pairings exclude cancellation and give positive leading coefficients. |
| Persistent nonaffinity, including initialization | §12.3, lines 1686–1753 | Pass. Uniform lower-tail estimates survive the limits and imply a strictly positive affine regression error on compact intervals. |
| Persistent activity of every hidden layer | §12.4, lines 1755–1789 | Pass. Nonzero backward fields propagate downward, and a positive cumulative-kernel pairing excludes zero hidden velocities. |
| No forbidden endpoint or depth interchange | §§7–12; lines 1407–1411 and 1791–1796 | Pass. The order of approximation is explicit, and all final width statements are compact-time statements at fixed depth. |

## Detailed checks of the main potential failure points

### 1. Scaling and the claimed model

The finite definitions give `delta^(ell) = n partial f_n / partial z^(ell)`. With loss `(f_n-1)^2` and block mobilities `n,1,...,1,n`, the resulting raw increments are exactly (1.3). The hidden-matrix increment contains `1/n`; the readout and first-vector increments do not. The stored readout has variance `n^-2`, so its RMS is `O_P(n^-1)` and the population readout starts at zero.

The finite metric in §10 and population metric (9.1) also match the claimed kernel blocks. In particular, the finite Frobenius norm of `delta h^T/n` is the product of the two RMS norms. There is no missing factor of `n`, no residual embedded in the backward fields, and no half-loss convention silently changing the physical clock or decay rate.

The same `phi(z)=1+atan(z)/10` is used at every layer. Its positive floor `5/6`, upper bound `7/6`, and derivative bounds are valid. `F'=1/phi'` and `(phi composed with F^-1)' <= 1/100` are the appropriate identities for this activation. The initial cubic coordinate is included as a root with finite moments; it is not passed through a theorem requiring a globally Lipschitz cubic map.

### 2. Gaussian reuse, joint empirical limits, and rank loss

The conditional mean in (3.3) satisfies both constraints because `U^T Y = Q^T V`. Its remaining Gaussian component is projected in both matrix directions. Adaptive inputs are measurable with respect to the preceding transcript, so the next observation adds a linear constraint to the conditional Gaussian residual. This also explains why different matrix residuals remain conditionally independent. The argument does not condition on a later input before accounting for how that input was obtained.

For a new answer, the Gaussian projection discarded in (3.4) has normalized squared size of order fixed-rank divided by width. The remaining innovation has conditionally independent coordinates. The conditional test variance, mean-square cross term, and Gaussian-square variance in lines 374–390 establish both weak empirical convergence and second-moment convergence. They therefore establish the required joint `W_2` law, including old coordinates and quadratic contractions; a marginal Gaussian description alone would not have sufficed.

The source/response calculation uses orthogonality to the old forward-input span to replace `E[q_s h_perp]` by `E[zeta_s h_perp]`. Gaussian integration by parts then produces the derivative coefficients, and substitution cancels the old forward response terms. Consequently the new source covariance is the uncentered input second moment. In particular, (3.2) and (12.3) correctly retain the full reverse-input second moment as innovation variance rather than subtracting the response contribution.

For singular Grams, the perturbation is made to each query input using a new independent root, giving a positive limiting Schur complement at fixed perturbation size. The subsequent finite comparison uses original coupled matrices and their operator bounds, not a possibly ill-conditioned regression inverse. The perturbation constant is allowed to depend on the fixed finite program; it is not used as a uniform-in-mesh constant later.

The scalar removal argument is causal: at each new instruction, earlier derivative coefficients are already bounded and convergent; finitely many bounded-derivative compositions give the next bound. Covariance square-root continuity and bounded continuous formal derivatives then give the next limiting law and response coefficient. This avoids an inverse-continuity assertion at rank loss. The nullspace argument in lines 495–499 also checks that a covariance-null change of derivative coefficients cannot change the contracted answer. Degenerate Gaussian source slots must remain formally distinct, as the chapter specifies.

### 3. The common action spaces are sufficient

The countable family is closed under finite unions, so consistency is inherited from actual finite computations, not merely from separately specified marginals. The coordinate product has the generated sigma field, and the included finite-coordinate approximating functions have dense span in its `L^2` space. Passing the finite operator bound and transpose identity to limiting second moments makes an initial action well-defined on equivalence classes and bounded on this dense span. Its extension and the reverse extension are adjoints by the pairing identity.

This supplies one set of initial operators for all subsequent reference programs and their limits. Real coefficients and fixed Lipschitz maps can be obtained by approximation using the same bounded actions. The theorem does not require operator-norm convergence across widths or assert that the initial actions are Hilbert–Schmidt. Only the trained rank-one integrals need the latter property, and §9 supplies it.

### 4. The mesh-uniform response induction closes

The order of dependencies in §6 is valid. The bottom derivative estimate uses only earlier response rows. Each interior forward pass uses the already established forward coefficients at that layer and earlier upper-layer rows and delta norms. The backward pass then starts at the top and descends using the just-established current upper row. The current reverse return, displayed separately in (4.6), is included in these estimates.

I checked the numerical margins. The forward bounds are

- `49/36 + 1/50 < 3/2` at the bottom;
- `49/36 + 3/50 < 3/2` at an interior layer.

The envelope estimate (6.5) gives the asserted `L^1` and `L^2` bounds. Jensen is applied across time slots to exponentials of Gaussian absolute values, so correlated or singular temporal Gaussian laws are allowed. At the top, the derivative estimate and the learned covariance row give `3067/3200 < 1`. At an interior layer, `Q=161/120` gives a delta norm at most `Q/10 < 7/40`, and the row estimate is `2482563/2880000 < 9/10`. These are sufficient strict margins to close the same induction at every additional fixed layer.

The consequence `q = zeta + beta`, with `|beta| <= 7/6` and Gaussian variance at most `(7/40)^2`, yields (6.10) even though the shift may depend on the source. This is a bound at each time, not an unsupported Gaussian path-supremum estimate.

### 5. Uncut dynamics and uniqueness are not assumed locally Lipschitz

The cap dependence in (7.3) is genuinely linear. At an interior backward step, the preceding backward error is multiplied by a bounded operator norm and a gate bounded by `1/10`; the additional factor of `R` multiplies a forward-state difference. Repeating the backward induction therefore adds linear-cap terms instead of producing a power of the cap at each layer.

The top comparison uses only the pointwise bound of the reference readout. Thus neither the finite small random readout nor an arbitrary competing bounded-primal solution needs an extra pointwise hypothesis. The tail error `8 exp(-R^2/256)` beats every finite Gronwall factor of the form `exp(CR)`, and it still does so after multiplying by `1+R` to compare backward fields and velocities.

The resulting uniform state and velocity limits justify the uncut integral equation. Uniqueness is obtained by comparison to the clipped reference, not by claiming local Lipschitzness of the uncut field on an arbitrary `L^2` neighborhood. At a reached-state restart, the initial discrepancy itself already has a Gaussian-decaying bound times a finite exponential; another finite exponential for the restarted comparison leaves it vanishing.

### 6. Physical time and the raw gradient class

The weighted Taylor estimate (9.2) is sufficient for scalar Fréchet differentiability: truncate the fixed old backward factor, take the small variation limit at fixed truncation, then remove the truncation. Forward variations are `O(||dtheta||)` in `L^2`, and bilinear cross terms are quadratic because the matrix variation's operator norm is bounded by its Hilbert–Schmidt norm. The continuous-gradient argument uses bounded gates and convergence in probability against fixed `L^2` factors; it does not assume an unavailable general chain rule for Fréchet derivatives of Nemytskii maps on `L^2`.

The resulting feature-time equation gives `f_s = sum K^(ell) >= 25/36`. Hence the first level-one point is unique and lies at `s_* <= 36/25 < 3/2`. Boundedness of `f_s` gives `1-f(s) <= B_*(s_*-s)`, so the physical clock integral diverges at `s_*`. Its inverse therefore covers every finite physical time, while remaining strictly below that feature endpoint. The loss inequality is then exactly `L_t <= -(25/9)L`.

For raw competitors, the deficit equation prevents finite-time attainment of the label. Fubini supplies absolutely continuous scalar versions, and the pointwise chain rule yields (9.7). Its right side is in `L^2`, so membership in the transformed class is proved rather than assumed. This closes raw uniqueness and restart in the theorem's stated class.

### 7. Finite GF and exact raw GD

Finite physical GF continuation is separately justified by residual monotonicity and successive operator/vector bounds. For raw GD, the identity (10.1) contains the quadratic and cubic defects of the `F` transformation. The elementary finite inequalities used to bound them require only a bounded query RMS, not fourth or sixth empirical moments. Their cumulative normalized size is

`O(eta_n sqrt(n) + eta_n^2 n) = O(n^-3/2 + n^-3)`.

The comparison is with a fixed-cap finite reference. The random, variable feature-step partition is controlled by a pathwise time-Lipschitz bound on the continuous tail statistic; a finite-program Gaussian theorem is not applied to the growing number of GD steps.

The stopping argument includes the first potentially bad endpoint. The gap between `36/25` and `147/100`, and the positive population deficit minimum on `[0,T+1]`, exclude both stopping conditions once the predictor and clock errors are small. The extra physical interval handles the final interpolation node. Fractional use of (10.1) then treats the actual raw-parameter interpolation. Comparing GD and GF to the same finite reference establishes the stronger same-width distance (1.7), not merely agreement of their limiting predictions.

### 8. Observables, velocities, and whole paths

For bounded continuous gates multiplying unbounded fields, §11 clips the unbounded factor and controls the discarded `L^2` tail. Uniform `W_2` convergence to a compact family of limiting laws supplies the corresponding uniform finite tail control. Bounded operator calls propagate the same errors. This covers the additional backward and velocity programs as well as the explicitly Lipschitz probe class.

Formula (11.1) has both terms of the differentiated hidden preactivation: the current parameter velocity acting on the current feature, and the current matrix acting on the preceding feature velocity. Raw GD needs further work between nodes, and receives it. The recomputed preactivation increment is `O(eta_n)` in RMS and therefore `O(eta_n sqrt(n))` in coordinate supremum. Bounded `phi''` gives that same order for the gate change, which suffices to compare actual interpolated velocities with their node formulas. This includes the stated one-sided conventions.

The whole-path statement follows from joint grid-value convergence and (11.3), with bounded integrated squared velocities controlling the empirical and population supremum-norm interpolation errors. It is therefore stronger than a mere collection of one-time marginal laws. No extra coordinatewise moment or path-supremum Gaussian hypothesis is needed.

### 9. Nonaffinity and activity persist

The initial transpose induction in §12.1 conditions without revealing the current matrix's residual. Its response coefficient is positive by Gaussian symmetry and positivity of `z atan(z)` away from zero, and its innovation uses the full input second moment. Consequently all the `B` fields have positive squared norms. The adjoint identity (12.5) excludes cancellation in each initial preactivation-motion coefficient.

These facts yield the second-order hidden onset and the strictly positive `Gamma` in the kernel expansion. The total physical-time kernel is `nu_L + 8 Gamma t^2 + o(t^2)`, so the nonconstant-kernel conclusion is justified without asserting later monotonicity.

For persistent nonaffinity, the top correction is uniformly bounded. Interior corrections are dominated by a function of the opposite source group, independent of the relevant forward source; the bottom correction has a dominator independent of the initial root. The Markov/Gaussian lower bounds thus do not assume independence of the corrections themselves. Lower bounds on closed half-lines pass to a weak limit in the direction used in lines 1729–1732. Every limiting hidden law has unbounded support, finite variance, and strictly positive variance. A zero affine regression error would force a zero slope by boundedness of `phi`, and then a constant preactivation by strict monotonicity. Continuity gives the asserted compact-time positive minimum, including initialization.

Persistent activity is separately proved. The positive readout makes the top backward field nonzero for every positive feature time. A positive limiting reverse-input second moment gives a positive Gaussian source variance along sufficiently accurate approximations. A uniformly bounded response cannot eliminate its unbounded tails. Repeating this argument downward proves all backward fields nonzero. Finally, (12.12) pairs a hidden velocity with its backward field to obtain a strictly positive sum of kernel blocks, ruling out cancellation of that velocity. Strictly positive gates and the strictly positive finite-time physical multiplier preserve nonzero feature velocities.

## Classical inputs and their hypotheses

The specialized Gaussian-program limit, response estimate, clipping comparison, and raw-GD comparison are derived in the chapter. I found no nonclassical heavy result left as an external black box. The classical inputs used have the necessary hypotheses here:

| Classical input | Hypotheses supplied in this proof |
| --- | --- |
| Law of large numbers and conditional second-moment bounds | Iid finite-dimensional root tuples with finite second moments; the Gaussian/root constructions here have the stated higher moments where mentioned. New innovation coordinates are conditionally independent. |
| Gaussian conditioning and integration by parts | Finite Gaussian matrices/vectors; transcript-measurable linear queries; compatible constraints; bounded formal derivatives for fixed programs. Singular Gaussian integration by parts is reduced to standard Gaussians. |
| Finite-dimensional spectral calculus | Symmetric positive-semidefinite covariance matrices in a bounded spectral interval; polynomial approximation establishes square-root continuity including at zero eigenvalues. |
| Countable probability extension and conditional distributions | Consistent finite laws on finite-dimensional Euclidean coordinate spaces, hence standard Borel spaces; the coordinate index set is countable. |
| Density in `L^2`, regularity of finite Borel measures, Hilbert adjunction and Parseval | Generated countable sigma fields; finite Borel probability laws on Euclidean spaces; dense domains and bounded actions before extension. The resulting `L^2` spaces are separable. |
| Contraction, Gronwall, and finite-dimensional continuation | Fixed-cap Lipschitz bounds on the invariant bounded sets; complete path spaces; bounded intervalwise velocities. For uncut finite-dimensional flow, smoothness and the separate primal bounds prevent finite-time escape. |
| Fubini, Fatou, dominated convergence, and closed-set weak convergence | Jointly measurable `L^2` paths or finite coordinate laws; nonnegative exponential quantities for Fatou; bounded derivative/gate domination or explicit `L^2` truncation where required. |

## Limit order and endpoint audit

For a specified accuracy, depth and physical horizon are fixed first. One chooses a sufficiently large clipping level, then a sufficiently fine fixed reference mesh, and only then takes all sufficiently large widths. Query perturbations are removed at the fixed-program stage. The subsequences used for Fatou or almost-everywhere convergence do not select a final width subsequence.

The endpoint `s_*` is approached only as physical time tends to infinity. Every finite physical interval stays within the already constructed feature interval. The asymptotic population loss statement is a consequence of the population differential inequality; it is not an interchange with an infinite-time finite-width or finite-GD limit. Similarly, the depth-uniform response constants are not used to assert a joint infinite-depth limit. These distinctions are respected throughout the theorem and its proof.
