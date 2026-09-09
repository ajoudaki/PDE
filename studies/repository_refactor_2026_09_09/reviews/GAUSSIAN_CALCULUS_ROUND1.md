# Isolated adversarial mathematics audit

Verdict: **CLEAN**.

No required mathematical fix was found in the two supplied inputs. This verdict concerns the proofs and their stated scopes, including the fixed-program width identification. It does not certify the software implementation mentioned in Section 4 or any stronger limit theorem.

## Inputs, isolation, hashes, and read coverage

The only source material inspected was:

| Input | Complete read coverage | SHA-256 |
| --- | --- | --- |
| `/tmp/pde-calculus-full-review.YuzDVr/NOTATION.md` | Lines 1–98, all 98 lines | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `/tmp/pde-calculus-full-review.YuzDVr/gaussian_calculus.md` | Lines 1–1808, all 1808 lines | `7e2db79e59de2b52ae3a13e3013cced1086096648ca3313ecefde4c17a36d6fc` |

All 1,906 input lines were read. Chapter reading covered 1–260, 261–560, 561–860, 861–1180, 1181–1500, and 1501–1808. A combined display truncated part of the middle material; lines 1170–1517 were subsequently read in a separate, untruncated display. The notation file and chapter lines 1–260 were also reread with line numbers. No truncated passage was treated as read without recovery.

No repository, history, existing review, web source, agent, experiment, implementation file, or external instruction/reference file was consulted. No numerical or symbolic experiment was run. The inputs were not edited. All chapter line references below refer to this hashed version.

## Required fixes

None found. In particular, the strict-rank argument supplies the gap needed by the inverse estimates, and the stopping argument supplies the missing-event control needed to pass from conditional Gaussian actions to the original network and its terminal expectation. Neither step is being assumed as an external state-evolution theorem.

## End-to-end proof audit

### Gaussian reuse, empirical law, and finite conditioning

**Section 1, lines 11–93.** The rowwise orthogonal decomposition gives the stated conditional mean and covariance with the correct `1/n` normalization. Conditional on `y`, the transpose residual has covariance `sigma_n^2 P`; the finite coefficient is the random empirical `a_n`, not its expectation. The coupling bound (4) retains both the scale error and the removed constant-direction Gaussian component. Each tends to zero in probability. The ideal empirical Gaussian law has convergent second moments as well as weak convergence, so the use of quadratic Wasserstein convergence is justified; matching coordinates transfers it to the actual transpose output. The zero-variance case does not require division by the variance. The additional `C^1` and polynomial-growth hypotheses justify (5), including the vanishing boundary term. No row/column joint empirical law is inferred from this calculation.

**Section 2, lines 97–158.** The proposed mean satisfies both constraints using `U^T Y=R^T V`. Its orthogonality to the homogeneous constraint space establishes the Gaussian conditional mean, and the two-sided projection describes precisely the residual space. Formula (7) has the correct response coefficient and residual scale. Adaptive queries are allowed only through recorded independent roots and past answers. Discarding exactly dependent columns is an exact finite-dimensional statement; the text correctly does not use it to establish stability near singularity.

**Section 5.4, lines 528–631.** The induction is on the global chronology, which matters because queries can depend on other matrices' answers. Given the past, a new query is fixed and reveals a linear component of only the queried residual matrix. Its complementary Gaussian component remains independent of the other residual matrices. This preserves the product conditional law after interlaced forward and transpose calls. Both response formulas follow by projecting onto the previous query spans. The Moore–Penrose formulation also supplies an exact raw kernel when a finite Gram is singular. Scaling `M=sqrt(n) W_0` makes these precisely the initialization actions used in the network.

### Gradient calculus, Wick recurrence, and PSD validation

**Section 3, lines 162–191.** Differentiating `2<g,Hg>` contributes `2T[g,g,g]` and two Hessian-square terms totaling `4||Hg||^2`. Symmetry follows from the stated regularity. `C^3` suffices for the displayed third directional derivative. The change `theta=D^(1/2)q` gives velocity `D grad F` for a constant positive definite metric. The discussion explicitly retains the residual differentiation required for physical squared-loss time.

**Section 4, lines 195–251.** The Gaussian square-root representation proves integration by parts even for singular covariance. The recurrence has the correct diagonal subtraction, omits exactly the terms that could otherwise introduce negative powers, and lowers degree by two. Zero and odd degrees have the correct base values. Rational inputs lead to rational arithmetic. For the PSD test, the negative-pivot, zero-pivot/nonzero-row, and positive-pivot Schur-complement cases are exhaustive for a symmetric matrix. No inverse at a zero pivot is used. The mathematical algorithm is established here; the assertion that a particular API implements it is not a dependency of the proofs and was not independently checked.

### Exact model, normalization, and chronology

**Sections 5.1–5.3, lines 262–524; NOTATION.md, lines 16–42 and 70–88.** The theorem explicitly changes the stored readout initialization to independent `N(0,1)` entries. The output remains `a^T h/n`, and the cotangent remains `n` times the preactivation derivative. Consequently the middle stored update is `h delta h_previous^T/n`, while first-weight and readout updates have no additional width divisor.

The unscaled middle matrix satisfies `A=sqrt(n)W`, so `grad_A f=grad_W f/sqrt(n)`. A step `hn grad_A f` therefore changes the stored matrix by `h grad_W f`, exactly as claimed. The low-rank learned terms in (5.2.11)–(5.2.13) use normalized pairings and only strictly earlier updates. All blocks are updated simultaneously from the old network.

Each of the `N` training steps requires one forward and one backward sweep; the terminal evaluation requires only a forward sweep. This gives exactly `(2N+1)(L-1)` initialization-matrix actions. The listed query histories are correct before each direction, including the extra current feature column before a backward call. Queries are known before their own answers.

### Population construction and response cancellation

**Sections 5.5–5.6, lines 633–884.** Each field is measurable within its stated physical population. Covariances and response coefficients are deterministic population expectations. A new covariance is known before the corresponding source coordinate is adjoined: forward covariances come from already constructed lower-layer features; backward covariances come from already constructed upper-layer cotangents. This is a chronological construction, not an implicit distributional fixed point.

Only first derivatives with respect to Gaussian source coordinates are used. Holding deterministic covariance and response entries fixed is appropriate for Gaussian integration by parts. The chain rules require `phi'` and `phi''`, and the finite polynomial envelopes give integrable bounds. No unstated third activation derivative or Lipschitz bound on `phi''` is needed for the field coupling.

The cancellation can be checked directly from

`R = S Q + K P^T`, `v = K rho + S q`, and `omega = Q sigma + P k`.

The forward regression coefficient is `rho-P^T Q^{-1}q`, canceling the old forward action's cotangent component. The transpose coefficient is `sigma-S^T K^{-1}k`, canceling the old transpose action's feature component. The surviving Gaussian regressions have exactly the prescribed source covariances. The independent source blocks do not erase matrix reuse: that dependence is carried by these response terms. The later coupling estimates justify the population-limit interpretation of these algebraic identities.

### Strict rank, including exceptional branches

**Section 5.7, lines 886–1115.** The positive-conditional-variance criterion applies because the old variables are measurable before the chosen innovation. For a continuous nonconstant function, a Gaussian with nonzero variance cannot produce a constant value almost surely, since its density is positive everywhere.

At initialization, activation normalization makes all forward variances one. The top readout and then the descending Gaussian carriers center the time-zero response coefficients. Thus `K_{ell,00}=(E phi'(G)^2)^(L-ell+1)>0`. Nonconstancy and continuity of `phi'` provide a nonempty open set on which the derivative is nonzero.

At later forward times, a positive lower feature Gram supplies a strictly positive fresh forward variance. Older features and the response shift exclude that innovation. This proves the next feature Gram is positive and gives positive probability of a nonzero derivative.

For a nonconstant derivative, the top cotangent uses the current forward innovation. Its readout multiplier is measurable beforehand and is nonzero with positive probability: the preceding readout update itself has positive conditional variance because `h!=0`. For an affine activation `phi(x)=px+c`, `p!=0`, the correct innovation is instead the preceding forward innovation. Its coefficient in the new top cotangent is `h p^2 tau_{L,k-1}`, and all older top cotangents exclude it. This avoids falsely applying nonconstancy of `phi'` in the affine case.

Each descending cotangent then uses a fresh backward innovation multiplied by a derivative that is nonzero with positive probability. At layer one, the same innovation supplies both the next feature rank and the induction's nonzero-derivative event. Terminal forward ranks are included. Negative fixed `h` causes no failure: the relevant nonzero coefficients enter conditional variances through their squares.

The two separate boundary branches are also valid. If `phi` is constant, normalization forces `phi=+1` or `-1`, all cotangents vanish, and `E f_n^N=Nh` exactly. If `L=1`, there is no matrix conditioning; the displayed coordinate recursion is iid and exact at every width, with finite moments from linear growth and bounded derivative. The reused-matrix strict-rank proof is not improperly imposed on this branch.

### Empirical ledger, coupling, and moment tower

**Sections 5.8–5.9, lines 1117–1542.** The forward/backward cross-block distinction is essential and is handled: the enlarged backward block contains `v_<k^T h_k/n`, already formed for the forward action. Both new query overlaps, the new query norm, and both old Grams are available. No mixed-connector inverse is silently required.

The ideal copies are iid within a physical population while retaining their complete temporal dependence. Their Gaussian innovations can be shared action by action with the exact conditional raw kernels. Iterating these kernels gives the raw transcript its original joint law. Independence between ideal physical populations is therefore consistent with asymptotic field coupling; it is not asserted as exact independence of the finite raw populations.

The spectral tests are predictable and cumulative. A Gram is tested before its inverse is evaluated; its Schur variance is tested before the new answer is sampled. The minimum is over a finite strictly positive population list, including terminal forward innovations. Off the cumulative good event, deterministic population coefficients and the identity residual projection define extended actions. Exact raw actions still exist through the Moore–Penrose kernel.

The moment estimates close quantitatively:

1. The centered iid even-moment expansion eliminates singleton indices, leaving at most `nu/2` distinct indices and an `n^(-1/2)` bound after taking the `nu`-th root. Pair empirical moments consequently consume order `2nu`.
2. On the good event inverse factors are deterministically bounded. Replacing factors in a regression coefficient or Schur variance gives `C Z_n^2 delta_n`. There are at most two unbounded moment factors in that expression, in addition to the error.
3. In an action error the four terms are old-field error, coefficient error, scale error, and projected-noise error. For example, `Z_n^2 delta_n bar V` is bounded using orders `8nu`, `4nu`, and `2nu`, respectively. Freshness of the new Gaussian justifies conditioning in the projection estimate. The coefficient covariance there is `(V^T V/n)^{-1}/n`, giving the required `n^(-1/2)` factor. Thus order `8nu` is sufficient.
4. Coordinate bundles require at most two successive product estimates: a learned scalar-times-field term and a readout/backsignal times `phi'`. Lipschitz activation operations consume no further order. Order `4nu` suffices. The terminal readout-times-feature average also fits this budget by coordinate Cauchy–Schwarz and Holder.

Therefore the finite backward allocation `R_{j-1}=8R_j` covers the at most `3(2N+1)(L-1)+1` ledger entries. It is not necessary to assume the induction conclusion at all orders simultaneously. Choosing the terminal even order above both requested mixed exponents controls the mixed norm by probability-measure norm monotonicity.

At the first failed test, raw and extended histories still coincide. Eigenvalue perturbation and the Schur-error bound turn failure into a fixed-threshold empirical error. The arbitrary finite even moments and a finite union bound then give `P(stop)<=C_b n^(-b)` for each requested integer `b`. This avoids a circular argument requiring good raw inverse moments on the bad event.

### Removing stopping and taking expectations

**Section 5.10, lines 1544–1713.** The raw polynomial majorants use only first/readout RMS values and middle operator norms. The rank-one update bound has the correct normalization, and finite iteration preserves a fixed nonnegative-coefficient polynomial envelope. Initialization actions are bounded by the same envelope because the majorant for each middle matrix dominates its initial operator norm.

The Gaussian operator-norm proof supplies the needed uniform moments directly: a `1/4`-net has at most `9^n` points, the two-net bilinear estimate incurs factor two, and the union bound gives `2 exp(n log 81 - n y^2/8)`. The subsequent tail integration is uniform in width. Vector RMS moments follow from Jensen.

For a general coordinate exponent, the possible loss is only `n^(1/2-1/p)_+`. Taking `b=2nu`, with `nu>=max(p,P,2)`, overcomes it after Holder on the stopped event. Extended and ideal stopped pieces also vanish using their higher moments. Grams and raw cross-moments are controlled by products of RMS norms. Finally `|f_n^N|<=P(R_n)^2` supplies terminal uniform integrability independently of regression inverses. The coupled terminal product converges in `L^1`; its ideal empirical average has expectation exactly `F_{N,L}(h)`. This justifies the asserted expectation limit.

### Section 6 obstructions and exact limits of scope

**Lines 1737–1758.** Iterated same-space multiplication plus the `L^p` embedding uniformly bounds `||X||_{L^{kp}}`. Essential unboundedness contradicts this using positive tail probability at every level. Constants force a positive zeroth-order weight in a genuine derivative-sum norm. The argument does not rule out the finite order-consuming estimates used above.

**Lines 1760–1779.** Testing the ordinary-derivative shift and Leibniz product on the stated unit jets yields `j<=C_P C_S w_1`. For factorial-normalized jets the factor `j` moves from the product to the shift, leaving the same contradiction. The unrestricted positive coefficientwise setting is stated explicitly; arbitrary restricted expression classes are not ruled out.

**Lines 1781–1808.** Bounded real derivatives of `(1+u^2)^(-1)` and finite Gaussian moments justify differentiation under expectation to every finite order. The even Taylor coefficients are `(-1)^k(2k-1)!!`; their consecutive term ratios force radius zero. Nevertheless the displayed smooth autonomous two-dimensional ODE has the explicit unique global solution `(t,g(t))`, and its first velocity component is one. This proves the stated distinction between analyticity and smooth finite-dimensional realization without claiming a network closure.

The chapter proves a width limit for separately fixed finite `L,N` and fixed nonzero real `h`, under the stated normalized `C^2` activation assumptions and order-one stored readout. It does not prove physical loss-GD convergence, a continuous-time limit, a growing-depth or growing-action theorem, a uniform conditioning gap as `h` tends to zero, an infinite Taylor expansion, or a bounded population weight operator on an entire function space.

## Dependencies and classical hypotheses

All nonclassical ingredients needed for the width theorem are supplied within the chapter: the global adaptive Gaussian conditioning lemma, response identities, strict-rank induction, empirical concentration estimates, finite moment allocation, stopping, and raw-network bounds. The population construction and rank proof can be read together chronologically: each positive input Gram permits the next source extension, which then establishes the next rank. No full-rank result is used to construct an earlier unavailable query.

The remaining classical tools have their needed hypotheses: finite symmetric PSD matrices for Gaussian square roots; joint Gaussianity for orthogonal independence; integrable polynomial envelopes for Gaussian integration by parts and dominated differentiation; iid integrable variables for laws of large numbers; finite second moments for quadratic Wasserstein convergence; even finite moments and independence for the concentration expansion; positive spectral gaps for inverse and square-root estimates; and finite dimensions for projection, spectral perturbation, and sphere nets. Holder, Jensen, Cauchy–Schwarz, Markov, and union bounds are applied to finite moments or finite lists. The smooth ODE example is solved and shown unique directly.

## Optional clarifications

These are presentation improvements, not required proof repairs.

1. At lines 1299–1303, replace “Independently, generate the raw action” with wording explicitly saying that raw, extended, and ideal actions share the fresh Gaussian vector, while the raw action always uses its exact kernel. The common-noise construction is already specified at lines 1265–1273; “independently” could otherwise suggest separate noises on the good event.
2. At lines 1277–1278, remove “nonterminal” before “query Schur complements.” The minimum and the immediately following sentence correctly include terminal forward innovations.
3. At lines 1473–1487, mention the terminal readout-times-feature empirical average alongside the other product estimates. It obeys the same stated order budget, but the prose listing the “only nonlinear products” omits it.
4. At lines 1717–1718, write “Sections 5.2–5.10” instead of “Sections 2–10.”
