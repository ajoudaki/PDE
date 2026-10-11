# Independent scientific promotion review B — frozen version 5

**Verdict: PASS for the stated theory and exact-real algorithm-complexity addition.** No required scientific correction or missing proof input remains in this review. This verdict does not authorize integration, certify finite precision, or replace the separate integration review.

## Identity, isolation, and input integrity

Reviewer: `/root/promotion_science_b_v5`, distinct from the three named authors/assemblers and the selector. I received the neutral assignment in a fresh context, not author discussion, previous reviews, or study history. I read no other study, no author source notes, and no archived book. The scientific inputs were exactly the frozen chapter, index, notation, diff, and manifest specified by `PROMOTION_REVIEW_ASSIGNMENT_V5.md`. The manifest names additional files; those names were provenance only and were not treated as permission to retrieve their contents. I did not solicit author explanations.

I read and applied `solve-math-rigorously`, `explain-with-canonical-notation`, its complete neural-response-memory reference, and the research/promotion workflow. Mathematical arguments below use the chapter's normalization, residual sign, and stored readout. The zero readout is an explicit chapter-specific initialization, compatible with the global contract's requirement to distinguish models.

SHA-256 values obtained by `sha256sum`:

| Frozen input | SHA-256 |
|---|---|
| `docs/08b-trajectory-compression.qmd` | `7363ea5815ed592ce33b0b4b2185539358348f21f3e3b264caa68620a2d5f460` |
| `docs/index.qmd` | `8246e044093b241d51b5eb964d65932dbe5d4e7f97a61f1389c9f16eb5402a68` |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `chapter.diff` | `76f17ece3582b944a78c9e6e1282f56d99194e1460074ac7dc1aad8e6e506816` |
| `inputs.sha256.json` | `c6c5c124dafb8f42f61beba15e527226f9abaa7862acfcdb78361b93b15bc483` |
| neutral assignment | `ba74aee8bacdc9fa591a0816fc3fbcd085b368b04bea1b088ff873faec9e52cd` |

The chapter matches the manifest's **proposed** chapter entry. The different unprefixed chapter hash in that manifest records the established baseline; it is not the proposed input identity. Index and notation match their manifest entries. The diff introduces the width and setup sections and corresponding interface prose; unchanged arguments were read as dependencies, not accepted on reputation.

A final repeat of `sha256sum` after writing this report returned identical values for all five frozen packet files. The inputs remained unchanged throughout the review.

## Complete read coverage and commands

The chapter was read with consecutive `sed -n` ranges `1,700`, `701,1400`, `1401,2100`, `2101,2800`, `2801,3500`, `3501,4200`, `4201,4900`, `4901,5600`, `5601,6300`, `6301,7000`, `7001,7700`, and `7701,8050`. `wc -l` verified its actual end at line 7954. Each of these chapter reads returned its complete requested contents without truncation. This includes the complete unchanged cavity, fitting, Legendre, selected-model, harmonic, Taylor, and nonlinear-learning proofs.

The initial combined process/index/notation read exceeded the orchestration output budget. I repaired it with workflow ranges `1,170` and `170,350` (287 actual lines), index ranges `1,170` and `171,260`, and a separate complete `cat` of notation (98 lines). One combined second index read was truncated again; its `171,260` range was reread alone successfully. The initial manifest read was truncated and was replaced with complete `1,121`. The first diff read was also truncated by the outer budget, so `1,1050` was repeated with an explicit larger outer budget, followed by complete `1051,2050` and `2051,3007`. There is no unread complement in the assigned scientific packet.

Operational checks were `git status --short --untracked-files=no`, `git rev-parse HEAD`, and `git diff --cached --name-only`. HEAD was `ef8362764b4eb8144d7af8d6f8db080fdaaf82ca`; the index was empty. Unrelated modified paths were observed as metadata only and left untouched. No Git mutation was performed. The only writes are this report and the assigned scratch script.

An independent deterministic algebra script was created with `apply_patch` and run as:

```sh
python data/generated/headline_threefold_upgrade_20261011/review_b_v5/check_algebra.py
```

Exit status was zero. It checks all ranks for matrix sizes 1, 2, 5, and 9, metric inversion/isometry, positive quadrature through its exact polynomial degree for orders 1 through 32, grouped endpoint factors, and the fixed-parameter exponent comparisons. These are finite algebra checks, not statistical evidence or a training campaign. Its outcomes were:

```text
Gaussian conditional-mean/update identities: maximum error 1.3003210510503555e-15
Metric inverse/isometry identities: maximum error 2.50287954702156e-14
Fejer positivity/mass/exactness: maximum error 1.2858637765678083e-15
Grouped endpoint coefficient identity: error 6.051002940156751e-16
Operation/memory and Legendre ratio exponents: PASS
```

The general arguments, rather than these floating-point instances, determine the verdict.

## Model and dependency audit

The comparison is to an actual width-n dense gradient flow with independent Gaussian first/hidden matrices and exactly zero readout. Its loss is the mean squared residual, and the block mobilities are `(n,1,...,1,n)`. In mobility coordinates the velocity is `-2/m` times the sum of residual-weighted output gradients. This recovers every width factor in the numerical field and in the source response `D_Theta z grad_Theta(n f)`.

The assumptions retained throughout are fixed depth, fixed deterministic normalized inputs, a strictly positive final population feature Gram gap, strip-holomorphic activations with bounded first derivative, and `0<Y<=lambda X^-30`, where `lambda=gamma/m<=1` and `X=beta^L`. Linear activation growth is used; bounded activation values are not silently required. No full rank of the input Gram is needed. Constant activations cannot meet the final gap for m>=2; affine activations satisfying the gap are permitted by the compression and setup results. The additional nonaffinity assumptions belong only to the separately scoped feature-learning certificate.

The dense fitting proof controls the readout contribution to dissipation, then uses the integrated residual to close the operator/feature/Gram tube with strict margins. Cauchy--Schwarz applied to `(-d rho^2)/rho` gives parameter tail length `2 rho/sqrt(lambda)`. This proves actual convergence and uniform output tails, not merely an infimum of loss. The selected fitting proof has its own exact energy identity despite not being a gradient flow of the corrected predictor. The positivity comes from its explicitly prescribed sum-of-Grams deficit equation. These facts justify both fitted endpoints used later.

I checked the four cavity trace types, the normalized Schatten estimates, the negative-Gram propagator treatment on real and imaginary segments, the nonlinear joining-strip remainder gate, and the separate singleton/common-cavity corrections. Conditional Gaussian statements are made with frozen controls and retained-measurable stops; substituting adaptive controls uses the uniform event. In particular, the chapter does not assert that an adaptive variation remains centered Gaussian. The finite refinement supplies the extra common-prefix endpoint grid needed when the successful full prefix is random.

There is no missing cross-chapter proof dependency. The Chapter 7 link is an explicitly different background benchmark. The standard elementary analytic and Gaussian ingredients actually needed here have their relevant calculations in the frozen chapter. The unchanged nonlinear-learning section was also read completely: its finite forward/reverse conditioning, initial acceleration identities, adjoint telescoping, and cubic prediction certificate are not used to infer the new polynomial width threshold.

## Polynomial width: reconstruction and attacks

**Finite initialization.** For a Gaussian Lipschitz norm, the difference between its mean and RMS is at most its Lipschitz constant. This gives the displayed concentration inequality once the tolerance exceeds twice that constant. Polarization transfers concentration of the plus/minus feature norms to covariance entries. I checked the potentially singular covariance step by first shrinking both Gaussian pairs to common marginal deviations: the scaling error costs `2sK_0 Delta`; differentiating correlation at fixed marginals costs `s^2` times covariance error plus `2s^2R_0 Delta`. Thus the stated `D_0^cov` encloses all terms without dividing by a variance. The layer recurrences sum to the claimed initial gap, and the sphere-net cardinality enters logarithmically as `d log(1+2/h_0)`, not exponentially in the width threshold.

**Finite source probability.** The normalization by `S=16Y/lambda` removes inverse label factors from the retained force derivatives. I checked that the first-layer incoming row is handled as a scalar control: it has order-S-squared motion, not the interior-row extra inverse-square-root-width factor. The common map envelope `C=X^1000 chi^2` and `A=C^4(N+d+u+1)^8` leaves positive exponent margins in the entropy and remainder bounds. At `log n>=40000 log(A/rho)`, the logarithm of `A ell^16` is at most `17 log(A/rho)`, below `log n/1000`. The control-net logarithm is below `n^.627`, the union logarithm below `n^.65`, while quadratic-form tails have exponent at least `n^.78`. The nonlinear remainder has largest displayed power `n^-.07875`, strictly below the `n^-.04` stop. These comparisons use explicit gates rather than an unspecified eventual absorption.

For moments, main common-cavity references use fixed exponents; only the tiny singleton-to-common corrections need order proportional to `u`. Collision tuples contribute the displayed exponential factor involving `choose(u,2) W_n/(16n)`. The confidence order is logarithmic in `mL/rho`. Budget failure is bounded by `emL(64e^2)^-u`, and the simultaneous domain allocation is strictly less than rho: the shared initialization allowance is rho/4, and twice the other three allowances sums to 3rho/4, with strict bounds on the constituents. I specifically checked that confidence does not multiply the panel-count coefficient.

**Capped geometry.** The function `h(t)=log(1+2 K r_n exp(nu t))/(2 K)` has derivative at most `nu/(2K)<=1/8`. Its disks fit the flaring domain, and its retractions are Lipschitz and commute with the real anchors. The additional cap controls both the imaginary-time base propagator and the Gaussian correction moments. On vertical pieces, freezing the real symmetric generator gives a unitary base; the remaining norm growth is bounded by an integrated generator difference. Complex positivity is never invoked. Splitting the panel-count integral where `2 K r_n exp(nu t)=1` gives the inverse-radius and logarithmic terms. Expanding the reciprocal cap produces a term proportional to `S^2 b_n^(3/2)`; `b_n^(3/2)<=4 sqrt(ell)` restores the required squared-label factor. This is the essential reason the cap preserves the headline retained count.

**Actual dense lower bound.** With final-layer conditional covariance bounded below by `gamma/2`, the squared-area identity yields a coordinate product variance at least `Y^2 gamma^4/(256X^16)`. Conditional sixth-moment bounds give third centered moment at most `8m^3Y^3X^24`. I independently expanded the characteristic function of `V-V'`: below frequency `3 sigma^2/(8M_3)` its modulus is bounded by `exp(-sigma^2 t^2/4)`. Integrating against the Gaussian interval majorant proves the shift-uniform finite small-ball bound. Conditioning on the whole second run makes that run only a shift; no independence between the derivative and source events is needed. The random maximizing training coordinate is measurable in the conditioning field, and the source event covers all training coordinates.

The derivative-to-trajectory transfer contributes `r/(2K^2)` with `r` proportional to `ell^-1/2` and `K=O(ell)`, hence `ell^-5/2`. The analytic tail is order `Y/(lambda n^2)` and is absorbed by the explicit third lower-width gate. The witness lies at positive time because both initial predictions vanish. Both fitted training outputs equal their label, so no endpoint separation is inferred. This is a lower estimate for the actual denominator in the promised norm.

**Improved Legendre order.** I reconstructed the argument after subtracting the accumulated physical feature defect. The resulting history g has first clock derivative equal to the ordinary normalized feature velocity, and second derivative `dot a/rho_hat`. The weight `xi(A-xi)` in the Legendre operator cancels the terminal inverse residual through `(A-tau)/rho_hat<=4/lambda`. Its derivative has no prefix jump because the initial readout is zero. Two integrations by parts then supply a forward tail of order `q^-2`, while the frozen backward history contributes `q^-1`. The product in the exact physical defect is therefore order `q^-3`, with the additional linear defect term absorbed by `q>=4P^3 ell`.

The bootstrap `D<=Y/sqrt n` converts known dense carrier/response maxima into closure coordinate bounds without an extra width loss in differentiated curvature products. The signed comparison contributes at most `P n^(1/64)`, since the label cap makes its square-root-log coefficient small. With `q>=n^(1/4)`, the resulting error exponent is `-3/4+1/64=-47/64`; dividing by the dense lower bound gives `-15/64`. Absorbing `ell^(9/2)` by `n^(7/64)` leaves `n^-1/8`. This verifies polynomial inverse-error dependence, which would not follow from the older logarithmic relative error alone. The explicit `N_Leg` also enforces `q<=sqrt n` and improves the bootstrap by a factor two. Whole-sphere prediction subtraction uses real operator bounds; a new complex whole-sphere probability event is unnecessary.

**Taylor width/count compatibility.** The exact-metric transfer needs only source values and exact initialized-image pairing, not matched derivatives at source-panel boundaries. The polynomial source lemma supplies these on the capped disks. The finite tail gate is label-independent after cancellation of Y. The count gate controls the additional `log(1/Y)` in the coefficient degree, giving `K+1<=8ell`. Squaring the panel rank retains `(Y/lambda)^4 ell^3` and the separate `lambda^-2 ell^2 log(e+ell)^2` term. Only the latter count simplification requires an inverse-label width gate. The final maxima contain fixed powers and logarithms of exposed parameters, with no hidden exponential in inverse tolerance, sample count, confidence, or gap.

## Efficient setup: reconstruction and attacks

**Signed numerical stability.** Expanding the difference of the two residual-gradient fields gives a negative output-error square. Maximizing `-2a^2+2(C^r+J^r)a E^2` produces `(C^r+J^r)^2 E^4/2`, so division by E yields exactly the cubic term of the displayed error inequality. The integrating-factor exponent is `2J^r int rho<=4J^rY/lambda=A_n`. The supplied two small-defect conditions close the first-exit argument at `2 exp(A_n) E_0`. This avoids a time-length exponential Lipschitz estimate that could change the claimed setup powers.

**Activation backend and restarts.** The moving parameter balls preserve a strict scalar strip by `sqrt(n) P_* b_n<=a/16` and preserve carrier maxima by the separate kappa constraint. The inner Chebyshev ellipse contains the necessary Cauchy disks; the outer ellipse stays strictly inside the half-strip. Fourier tail plus discrete alias bounds give value error, and Cauchy gives the first two derivatives without activation derivative calls. The field substitution error is uniformly controlled on the complex balls. The restart map has contraction factor at most one quarter, and its fixed point remains inside the smaller ball. Taylor truncation plus activation error gives integrated defect at most `e_d`; signed stability then supplies the next anchor hypothesis. Thus finite induction covers all of `[0,T]` without querying or testing a trained exact trajectory.

For source error I checked all four terms: source Taylor tail, activation substitution along the local polynomial-field solution, parameter truncation error transferred through the original source, and the accumulated real-path error. The chosen orders allocate at most `epsilon_v/64` to each. Passive backward responses use a conservative `n`-Lipschitz coordinate bound and the corresponding Euclidean tolerance; the width factor is paid in logarithmic accuracy, not omitted. At fixed parameters `J,D=O(ell^(3/2))` and `K=O(ell)` follow directly from the explicit radii and tolerances.

**Taylor sources.** Chebyshev-root interpolation reproduces a degree-K_s Taylor approximation, while its operator norm is bounded by `2K_s+1`. The doubled logarithmic degree pays that norm. Exact initialized images of the numerical nodes ensure exact pairing by linearity. The source rank uses all source panels, separately from numerical integration panels. I checked the stronger numerical degree against the original polynomial count gate: the displayed logarithm is at most `(9/4)ell+log 8`, so `K_s+1<=8ell` at the supplied gate. The same capped domain therefore supports width and setup claims jointly, without invoking the old eventual uncapped-panel event.

**Harmonic sources.** The coefficient quadrature uses positive one-dimensional rules, with the normalized spherical Jacobian included in the integrand. Complex angular rotations consume at most half the certified query radius. The time and angular orders pay the integrand growth of retained harmonics. Telescoping d rule errors gives at most half the coefficient tolerance, and the approximate-node error pays the other half. Coefficients are accumulated globally rather than retained separately per numerical panel. Taking exact initialized images of base coefficients preserves pairing. The original anisotropic mode set retains its inverse-time-radius factor proportional to `(Y/lambda)^2`, and hence the squared-label factor in storage survives. The two-point d=1 case has no spatial integration or degeneracy problem.

**Adaptive Gaussian execution.** I independently derived the conditional affine mean `A=Y V^T+U R^T(I-VV^T)`. Compatibility makes `AV=Y` and `A^T U=R`; the orthogonal residual subspace is exactly `(I-UU^T) B (I-VV^T)`. A new forward or transpose direction splits this residual into independent Gaussian components because the covariance between the observed direction and the remaining orthogonal complement vanishes. This proves the induction with adaptive directions and across layers. Zero/dependent directions add no information; full opposite rank gives zero innovation. These cases were included in the algebra check. Completion yields one ordinary joint Gaussian reference whose past replies all agree pathwise, rather than separate marginally correct matrix actions.

**Matrix access and complexity.** The four enumerated initialized-matrix request classes cover exact initialized training passes, all constant-anchor coefficient actions, completed source images, and final source-basis images. Selection uses the generated vectors and cannot query an uncounted hidden matrix norm or entry. The last basis-image class is needed even when existing paired images do not span it. Replacing random actual rank in the deterministic query budget by `min(n,R)` makes the sampler's bounded-transcript assumption valid.

The endpoint coefficient sum groups into mK rank-one factors per layer/panel. Caching inner contractions reduces current-panel action work to `O(m b K^2(n+K))`; accumulated earlier factors separately cost the `J(J-1)K(K+1)` term. No rank approximation to the exact trained matrix is presumed. Streaming uses one anchor, current jets, global sources, and in the implicit case the factored numerical history and Gaussian transcript. Selection costs `O(L n r^3)` and is explicitly retained.

Substituting the actual orders gives supplied Taylor work `O(n^2 ell^(5/2))` and implicit Taylor work `O(n ell^5)`; sampler, trained factors, and activation composition all reach the latter exponent. Harmonic has `R,Q=O(ell^(3d/2+1))`; its selector dominates implicit work at `O(n ell^(9d/2+3))`. The supplied Harmonic leading term is `O(n^2 ell^(3d/2+1))`. Peak storage is respectively quadratic for supplied matrices and `O(n ell^(3d/2+1))`, `O(n ell^(5/2))` for implicit Harmonic and Taylor. Scalar geometry, quadrature, coefficient accumulation, exact initial features, input reduction, and final metric solves are included in the full ledgers. Fixed-parameter absorption of lower terms is not claimed uniformly in growing dimension or data size.

## Component verdicts and completion

| Component | Verdict |
|---|---|
| Shared fitting, source, projection, selection and endpoint dependencies | PASS |
| Finite initialization/source probability and capped geometry | PASS |
| Finite actual dense-trajectory lower bound | PASS |
| Legendre third-order defect and polynomial sufficient width | PASS |
| Taylor polynomial width, label-sensitive count, and exact pairing | PASS |
| Numerical source routine, scalar activation backend, restart induction | PASS |
| Harmonic supplied dense setup | PASS |
| Taylor supplied dense setup | PASS |
| Harmonic fresh implicit Gaussian setup | PASS |
| Taylor fresh implicit Gaussian setup | PASS |
| Whole-sphere/panel domains, all-time norm, retained inventories, computational primitives | PASS |

Unresolved objections: **none**. Required corrections: **none**. Missing scientific inputs: **none**. No external specialized theorem was imported to complete a missing step. This is a completed review of the whole frozen scientific packet, not a spot check or endorsement based on previous verdicts.

The scope limitations remain material: the width exponents and activation constants are enormous; Harmonic's width onset remains eventual; setup costs are exact-real costs with separately fixed parameters and supplied certificates; implicit initialization is a fresh coupled Gaussian reference, not conversion of an arbitrary supplied matrix; the disposable rollout reaches `T=32 log(en)/lambda` in physical time; retained coordinate counts are not bit bounds; finite precision, population capture, generalization, and comparisons with every dense solver are outside the addition.
