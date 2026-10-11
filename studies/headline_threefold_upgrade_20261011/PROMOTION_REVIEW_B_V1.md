# Independent scientific review B — frozen promotion v1

**Status: PARTIAL / NOT COMPLETE — version 1 withdrawn.** The coordinator withdrew this packet before acceptance and instructed this reviewer to stop, citing new `@proof-*` references being parsed as citations and requiring a corrected frozen version. I did not inspect any build or other review report. I had finished the scientific reading and written the substantive findings below when that instruction arrived, but have stopped without a final acceptance verdict or final report/input revalidation. No scientific objection had been found in the work performed. This is an interrupted review record, not a completed promotion review or permission to integrate.

## Role, isolation and input identity

Reviewer: `/root/promotion_science_b_v1`, distinct from the three authors/assemblers and relevance selector named in the neutral assignment. I began with that assignment and the shared repository instructions, without author discussion, study history or another review. I did not consult the study README, source notes, selection report, prior verdicts, author agents, other reviewers, other studies, the archived book, or live scientific source files. Communication of findings is through this report. I edited only this report and my assigned generated scratch.

The scientific packet root was `data/generated/headline_threefold_upgrade_20261011/promotion_v1/`. SHA-256 values actually calculated are:

| Input | SHA-256 |
|---|---|
| `docs/08b-trajectory-compression.qmd` | `44248693994249cba7fcee35486bb3419981425930371be0776710778a71c59f` |
| `docs/index.qmd` | `8246e044093b241d51b5eb964d65932dbe5d4e7f97a61f1389c9f16eb5402a68` |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `chapter.diff` | `a743327c32d9da0f80a46624fe776e7d06db3d10102d6504987f2ffe8c1d5e38` |
| `inputs.sha256.json` | `c1f7a872afa95154ef5794e74f82dc7c53ec74d830aa2db8f21dfa947a0c65b3` |
| neutral assignment | `8e1a97a05be7d09ae2be784b1466d4329d0fd0f6f7a5766aba6713e19d34cce8` |

The manifest's `docs/08b-trajectory-compression.qmd` key records the pre-addition source; its `proposed/docs/08b-trajectory-compression.qmd` key records the supplied candidate. The candidate matches the latter. I did not mistake the source hash for the reviewed hash. Other packet filenames, sizes and hashes appeared in metadata output; I did not read their scientific contents.

Required process instructions read: `RESEARCH_WORKFLOW.md`, including all of Part 2; `solve-math-rigorously`; `explain-with-canonical-notation` and its complete neural-response-memory reference. No external scientific source was used. The chapter's Chapter 7 comparison is explicitly background rather than a dependency. The contextual references in the index are likewise not imported to complete these proofs.

## Complete coverage and verification record

I read all 7,954 lines of the candidate Chapter 9, including unchanged proof bodies, all 260 lines of its frozen index, and all 98 lines of its frozen notation contract. The chapter read intervals were 1–1000, 1001–2000, 2001–2750, 2751–3550, 3551–4350, 4351–5150, 5151–5950, 5951–6750, 6751–7550 and 7551–7954. The tool output for 1001–2000 lost part of the trace paragraph to its outer output limit; I repaired it by reading 1450–1525 and then 1515–1555. An initial combined process/index read was also truncated: I separately reread workflow Part 2 through its end and index lines 1–160 and 161–260. No scientific part of the assigned inputs remains unread.

I inspected every diff hunk header and removed passage. To avoid treating the 2,915 already-read added lines as a different input, I mechanically matched every added/context target line in the complete 3,007-line diff against its exact candidate line number. All 2,974 target lines matched. Thus the diff's scientific additions were read in the full chapter, together with their surrounding dependencies; its deletions and provenance were separately inspected.

The executable verification record is `data/generated/headline_threefold_upgrade_20261011/review_b_v1/checks.py`. Executed command:

```text
python data/generated/headline_threefold_upgrade_20261011/review_b_v1/checks.py
```

It exited 0 and verified the three scientific hashes, all diff target lines, exact rational Gaussian posterior-update identities, 27 log-domain instances of the Legendre structural gates, and the maximum used in the capped-panel logarithm estimate. The rational test uses nonaligned left/right observed directions and verifies compatibility, the updated conditional mean, and the vanishing cross-covariance direction. The structural-gate test uses three values each of the activation/depth envelope and gap, at the gate and larger widths; it does not materialize astronomical widths. These checks supplement the derivations below; they are not probabilistic evidence or substitutes for the proofs. I did not run training experiments, claim a maintained implementation, or audit unassigned producer code.

## Setup and unchanged dependencies

**Provisional findings.** The compared dense system has first weights of variance one, hidden weights of variance (1/n), exactly zero stored readout, loss (m^{-1}\sum_a r_a^2), and mobilities ((n,1,\ldots,1,n)). Its parameter norm places (1/n) on the squared first-weight and readout norms and no extra normalization on hidden Frobenius norms. Substitution of the displayed gradients recovers the flow, its tangent Gram and its dissipation identity. This is not the small random readout model from other chapters.

The assumptions retain (m\ge2), (L\ge2), normalized correlated inputs, positive final population Gram gap (\gamma), (\lambda=\gamma/m\le1), and (0<Y\le\lambda\beta^{-30L}). Analyticity plus bounded strip derivative allows unbounded activation values of linear growth. The proofs use that growth, rather than silently replacing it with bounded activations. Degenerate intermediate covariance matrices are allowed. Their square roots are continuous and the covariance calculations never invert the input Gram.

In lines 242–532 I checked the initialization net, conditional Gram propagation, cavity comparison, fitting stop and signed estimate. The readout contribution gives (-\partial_t\rho^2\ge\lambda\rho^2); integrating the weighted energy gives parameter tail length (2\rho(t)/\sqrt\lambda). Small labels close the hidden-displacement and singular-value margins. Finite length gives actual parameter endpoints and uniform prediction tails, not merely a convergent loss. In the signed comparison, the negative residual-difference square survives exact subtraction and the remaining coefficient is proportional to integrated residual activity.

In lines 533–2326 I checked the full source proof used by the additions: independently stopped cavities, root-independent coefficient extensions, the differentiated port equations, nonlinear remainder terms, uniform frozen-control Gaussian tests, trace absorption, complete-path moments, and the three domain verifications. The reverse port affects the gradient but not the forward residual; the top deletion has a separate residual offset. The first-layer incoming-row motion is not incorrectly charged a hidden-row (n^{-1/2}) factor. It enters scalar controls, with no nonexistent retained reverse port below layer one. The four noncentered contractions are retained; adaptive substitution follows the uniform event and is not asserted to preserve Gaussianity. The negative-Gram propagator is contractive only on real segments. On vertical segments the proof freezes a real symmetric generator to get unitary evolution and bounds the change. These distinctions prevent the principal independence and complex-positivity shortcuts I tested.

Lines 2327–3210 provide the Legendre identities and original dense lower bound. The growing-projection identity integrates squared endpoint errors into the final squared history tail. The zero backward prefix makes the relevant join continuous. Legendre fitting is order-independent and precedes error comparison. The original lower bound uses a last-layer innovation at a training query and transfers its initial derivative to a positive-time difference. It does not assert an endpoint difference where both runs fit the same labels.

Lines 4589–5892 supply the complete selection, dynamics, compiler and source-space dependencies. The barrier construction selects at most nine times the rank. Its metric satisfies exact source isometry and (D/4\preceq M\preceq D); coordinate gates consequently cost a factor at most two. The prescribed optimizer is not falsely identified with ordinary gradient flow in a metric where those gates need not be self-adjoint. The independent fitting proof and corrected readout preserve the training Gram gap. In the comparison proof, the (2V_Ce) term cancels with the differentiated residual correction; retaining this cancellation avoids a physical-time exponential loss. Source approximation errors are used as value errors and are never differentiated. The initialized-jet compiler remains a finite provenance construction without a work claim.

I also read and checked the unchanged nonlinear-learning section, lines 7385–7906. Its extra nonaffinity/nonparallel-input assumptions are local. Positive Hermite coefficient support, the four-input affine annihilator, one-pass Gaussian conditioning, the adjoint acceleration identity and the cubic kernel departure support the stated fixed-small-time conclusions. The inverse Gram there is an already positive hidden feature Gram, never the possibly singular input Gram. The nonlinear increment argument uses second-moment tail truncation. None of these stronger learning certificates is silently given polynomial onset by the new width theorem.

## Polynomial source probability and width claims

**Provisional findings: lines 3211–4225.** I reconstructed the finite argument rather than using eventual convergence as a quantitative premise.

1. The initialization calculation propagates marginal RMS errors separately from covariance errors. Shrinking to common marginal deviations and differentiating in the correlation gives the stated covariance modulus without a reciprocal marginal variance. Polarization of Gaussian-Lipschitz RMS concentration yields the entry estimate. The sphere net contributes (d\log(1+2/h_0)), not the net's cardinality outside a logarithm. Thus the initialized fitting width is polynomial in the exposed parameters, also for singular input covariance and (m>d).
2. In the finite source calculation (S=16Y/\lambda) scales the readout and hidden displacement. Zero initial readout removes inverse (S) from the effective derivatives. The fixed coefficient recurrences retain at most the displayed powers of (X=\beta^L) and (\chi=1+\lambda^{-1}). The map, control-modulus and derivative envelopes are polynomial; their homogeneous layer propagation is bounded once rather than costing a width power at every layer.
3. With (A=X^{4000}\chi^8(N+d+u+1)^8), the gate (n\ge(A/\rho)^{40000}) pays (A\ell_n^{16}\le n^{1/1000}) and the stated smaller powers for (u) and (\ell_n). The control entropy has power below (0.627), endpoint/deletion union below (0.65), and Gaussian exponent (0.78). The remaining (0.7) failure exponent therefore leaves a strict margin. The nonlinear remainder exponent (-0.07875) is strictly smaller than the bootstrap exponent (-0.04). These are numerical powers of width, not hidden problem-dependent powers.
4. The endpoint mesh uses a cavity's own stopped domain when conditioning on an omitted root. Only after all tests does it approximate a possibly adaptive full-network prefix. I specifically tested the failure mode of conditioning a Gaussian root on full-network survival: the displayed prefix-grid and retraction construction avoids it. Common-cavity weights are independent conditional on their common cavity; singleton-to-common corrections need only Hölder bounds, not independence. Repeated indices are charged through the partition count and (W_n). The confidence moment order (u_\rho) is logarithmic in (mL/\rho), and the label allowance does not shrink with that order.
5. The capped panel radius controls the complete-path complex correction at fixed exponential orders even when the original time radius is very large. The confidence order is spent only on the small singleton/common-cavity correction. The reciprocal cap produces a term (\lambda^{-1}B_n\sqrt{b_n}); (b_n^{3/2}\le4\sqrt{\ell_n}) converts its (S^2) part into the existing label-dependent term. This is why the cap does not add a new storage logarithm or confidence factor to the panel count.

The probability allocation is valid: shared initialization costs less than (\rho/4), and twice the other three allowances costs less than (3\rho/4). Real fitting extends the carrier and response controls beyond the finite source horizon, with exponentially small parameter tails. There is no residual (n^{-1}\le Y) gate in this normalized finite argument.

For the finite dense lower bound, conditioning on the first run through layer (L-1) and the whole second run makes the latter an arbitrary measurable shift. The squared-area argument supplies some measurable training coordinate with conditional variance at least (Y^2\gamma^4/(256X^{16})). Its third centered moment is at most (8m^3Y^3X^{24}). I derived the small-ball estimate by symmetrizing the characteristic function, using its quadratic decay up to (3\sigma^2/(8M_3)), and integrating a Gaussian majorant of the interval indicator. With (h=\tau\sigma_0/24), the stated width controls the exponential remainder uniformly over that shift. The analytic ellipse transfer contributes (r/(2K^2)), hence the displayed (\ell_n^{-5/2}) and the weaker finite coefficient (a_\tau). The last width gate pays the (n^{-2}) analytic tail. This is a lower bound for two actual independent dense trajectories, not for a certificate or a substituted reference.

## Legendre improvement and final quantitative assembly

**Provisional findings: lines 4227–4587.** On the bootstrap (D_{T_0}\le Y/\sqrt n), one RMS-to-coordinate conversion transfers the true dense carrier/response bounds to the reconstructed Legendre path. Differentiation includes the closure's physical defect. Products with changed gates use a bounded reference coordinate carrier or response; no unjustified coordinate bound on the feature speed or extra (\sqrt n\|\mathcal E\|) enters.

Subtracting the integrated feature defect gives a history (g) with (\partial_\tau g=a). The initial readout is zero, so this first derivative vanishes at the constant-prefix join. In

\[
\mathscr D_Ag=-\partial_\xi[\xi(A-\xi)\partial_\xi g],
\]

the possible inverse clock speed in (g''\) is canceled by ((A-\tau)/\widehat\rho\le4/\lambda). Both endpoint fluxes and the join term vanish. Applying the Legendre eigenvalues (j(j+1)) therefore gives a forward tail of order (YP\ell_n/q^2+Pd_{T_0}). The backward freezing estimate gives (YP\ell_n/q+P\ell_nD_{T_0}). Multiplying these tails with the exact projection-growth identity, and absorbing the linear defect term, yields the stated (q^{-3}) bound.

The signed amplification is at most (Pn^{1/64}), since the small-label coefficient of (\sqrt{\ell_n}) is at most (X^{-24}). The structural gate ensures (q\le\sqrt n), (q\ge4P^3\ell_n), and (8P^4\ell_n^2\le n^{15/64}). Consequently the bootstrap improves to (Y/(2\sqrt n)). The estimate is uniform in the arbitrary finite horizon and passes to the existing fitted limits. Its (n^{-47/64}) numerator, divided by the finite (n^{-1/2}\ell_n^{-5/2}) lower bound, gives (\ell_n^{9/2}n^{-15/64}); absorbing the logarithm leaves (n^{-1/8}). This proves polynomial inverse-tolerance onset. Using only the old logarithmic relative bound would not have done so.

For Taylor, the capped count is squared before simplification. It gives exactly the two terms ((Y/\lambda)^4\ell_n^3) and (\lambda^{-2}\ell_n^2\log(e+\ell_n)^2). The source degree has its explicit (\log(1/Y)) before the inverse-label count gate is imposed. The gate implies degree at most (8\ell_n); the (Y^{-1}) dependence is therefore disclosed rather than absorbed into an activation-only constant. The finite-time error is (Y/(2n)), and the explicit fitting-tail gate gives the other half. Input-span reduction preserves original normalization and first-row law. The final maxima contain only fixed powers of (X,m,d,p,\gamma^{-1},\delta^{-1},\varepsilon^{-1}), and (Y^{-1}) for Taylor. Legendre does not need (Y^{-1}). Neither conclusion quantifies Harmonic onset or the separate nonlinear-learning certificates.

## Numerical source computation and transfer

**Provisional findings: lines 5893–6744.** I checked the construction as an actual finite algorithm from initialization, including the scalar evaluator and restart argument.

The real stability estimate retains the negative prediction-difference square. Maximizing the remaining quadratic expression yields

\[
E'\le2J^{\rm r}\rho E+
\tfrac12(C^{\rm r}+J^{\rm r})^2E^3+\|d_u\|.
\]

Thus its amplification involves (A_n=4J^{\rm r}Y/\lambda=O(\sqrt{\ell_n})), not a generic exponential in the physical horizon times a width-dependent global Lipschitz constant. The two explicit restrictions on total defect close the cubic bootstrap. Passive backward fields are allowed a worse coordinate envelope; the resulting source sensitivity is explicitly (C_{\rm src}nE), and the later tolerances pay that factor.

Complex restart balls stay within the half-strip by forward subtraction from the certified true trajectory. Carrier subtraction gives (M_c+1) and makes the local Lipschitz estimate pairwise on the ball. The approximation of the activation is built from finitely many real values on a Chebyshev grid. I checked the outer and inner ellipses, their positive separation, geometric coefficient tails, discrete aliases, and Cauchy disks for the first two derivatives. Linear growth bounds the ellipse values. No high original activation derivative or complex activation oracle is a hidden primitive.

For polynomial-field restarts the integral map has contraction factor at most (1/4), stays inside its specified ball, and yields a true local holomorphic solution. Truncating it at half radius controls both parameter and derivative tails. Its piecewise polynomial rollout is continuous at the numerical anchors, so its defect can be integrated over the full interval. The global signed estimate verifies the next anchor's accuracy inductively; the algorithm never tests an inaccessible true error or samples an externally supplied trained trajectory. The four-term source-error decomposition separately pays truncation, activation substitution, polynomial-parameter tail and accumulated path error. Its Euclidean error budgets sum to the claimed (\varepsilon_v/16).

For Taylor, real Chebyshev source nodes span the local interpolant. Its norm bound (2K_s+1), analytic Taylor tail and the numerical nodal error give the source contract with room to spare. Initialized images are formed by the actual fixed matrix, so interpolation commutes exactly with that matrix and its transpose. The numerical source panels and the flaring analytic panels are different and are both charged. The calculation of (K_s\), including its factor two, still gives (K_s+1\le8\ell_n) at the original polynomial count gate. The capped-domain source event is exactly the quantitative event already reviewed; no additional qualitative Taylor source event is invoked.

For Harmonic, the retained global mode set is unchanged. I checked the normalized angular Jacobian, positive Fejér weights (including order one), periodic trapezoid error, polar ellipse error, and product-rule telescoping. Successive complex angular rotations stay within the certified quadric tube. The harmonic basis and normalization recurrence require only finite arithmetic and square roots. The source quadrature errors are first controlled separately for an analytic base and its analytic image; only then are approximate global coefficients paired by exact matrix application. This avoids an invalid coordinate-error-to-matrix-error step. Coefficients are accumulated globally across numerical panels, so the number of panels does not multiply the retained Harmonic rank. The two-point (d=1) case is handled separately and agrees with the stated exponent.

Both source spaces include exact original initialized training features, their required images, the constant, and the first-layer columns. Polynomial surrogate features do not replace these additions. The exact source metric, initial selected arrays, prescribed nonlinear optimizer and endpoint transfer therefore apply unchanged. Disposable preprocessing covers the full (T=32\ell_n/\lambda) physical interval; the compressed dynamics subsequently start at time zero.

## Gaussian law, matrix access and complexity

**Provisional findings: lines 6746–7383.** With orthonormal observed right/left directions (V,U), replies (Y=WV,R=W^\top U), and compatibility (U^\top Y=R^\top V), the conditional mean is

\[
A=YV^\top+UR^\top(I-VV^\top).
\]

Its residual is ((I-UU^\top)G(I-VV^\top)). This is the orthogonal Gaussian conditional kernel. Splitting off a new direction gives precisely the sampler's displayed mean and projected innovation; orthogonality kills cross-covariance with the remaining matrix. A transpose query gives the transposed construction. Dependent queries return their already determined value. Zero queries, full opposite rank, singular innovation covariance, and alternating directions therefore cause no inverse-query-Gram problem. Interleaving layers preserves a product of conditional kernels because every query choice is already transcript-measurable. Completing the matrices at the bounded stop proves the ordinary independent dense law and simultaneous pathwise agreement with all previous replies. The exact rational scratch check verifies the nonaligned-direction mean-update algebra independently.

I checked every source of initialized hidden-matrix information: exact initial training actions, constant-anchor actions for numerical source coefficients, initialized source images, and final basis images. No hidden matrix entry, norm, singular value or uncharged full-matrix test is needed. Previous numerical increments are grouped into (mK) outer products per panel. Their accumulated actions cost the explicit factor-history term; they are not treated as free low-rank updates. Causal convolution caching costs (O(mb'K^2(n+K))), and does not require (K) dense matrix coefficients.

The supplied and implicit computations can use identical deterministic ordering and tie rules. Under completion, coefficient induction followed by panel induction gives identical actual generator lists, ranks, selectors, metrics and initialized mixers. Hence their final arrays and entire autonomous future agree pathwise. This is a fresh Gaussian reference contract, not a subquadratic conversion of an arbitrary supplied matrix or seed.

The full ledgers include input-span construction, first-matrix handling, activation coefficient preparation and composition, both sets of panels/nodes, spherical geometry and harmonic basis evaluation, coefficient projection, source orthogonalization, all final initialized basis actions, metric/Gram inversions, initial copies and simultaneous scratch. In particular the selector's (O(Lnr^3)) cost is present. Exact rank decisions are made on the actual computed generators and do not require an accidental exact-source rank deficiency to survive approximation.

At fixed parameters I independently substituted (J,D=O(\ell_n^{3/2})), (K=O(\ell_n)). Taylor has source rank (O(\ell_n^{3/2})), but query count (O(\ell_n^{5/2})). Its sampler, factor-history and activation composition each cost (O(n\ell_n^5)); its selector costs only (O(n\ell_n^{9/2})). Harmonic has rank and query bound (O(\ell_n^{3d/2+1})); the selector dominates its width-linear work at (O(n\ell_n^{9d/2+3})). The online activation scratch (nDK) fits the advertised implicit memory, including the minimal (d=1) exponent. In supplied execution the terms with one factor of width and larger logarithmic powers are eventually dominated by the stated (n^2) terms. The four headline rows follow with their explicitly fixed-parameter constants. These substitutions do not assert polynomial onset for the computational asymptotics.

## Adversarial boundary cases and limits

The following attacks were included in the derivations rather than postponed as optional checks:

- (Y\downarrow0): the finite training-source and Legendre gates stay free of inverse (Y); Taylor exposes its separate count gate. At (Y=0) the stationary predictor is outside the nonzero-ratio hypothesis and explicitly distinguished.
- Singular input/intermediate covariance, (m>d), and antipodal inputs: initialization uses continuous square roots and correlation continuity. Only the positive final gap is required for compression; incompatible duplicate labels cannot satisfy that gap. Additional nonparallel restrictions belong only to the nonlinear-learning theorem.
- Unbounded analytic activations of linear growth: RMS and scalar approximation envelopes retain the constant and linear terms. No bounded-value hypothesis is added.
- Small gap: its powers are retained before logarithmic absorption. The Legendre signed exponent does not acquire a repeated reciprocal-gap factor; the finite lower coefficient exposes its weaker gap dependence.
- Arbitrarily high confidence: finite moment order enters the polynomial source gate; it does not enter the label allowance or capped-panel count.
- Residual zero and (t=\infty): stationary continuation or uniqueness handles divisions in proof histories, while stored equations do not divide by residuals. Finite path lengths and explicit tails provide fitted endpoints for the complete-trajectory norm.
- New passive inputs after initialization: Taylor offers no guarantee for them. Harmonic and Legendre retain the whole-sphere claim.
- Adaptive, repeated, zero and full-rank Gaussian query directions: the exact sampler handles each without a nonsingular query Gram, and without conditioning on later source success.
- Rank perturbation and finite precision: the rank bound is a generator bound; exact-real selection is legitimate. Neither coordinate count nor arithmetic count is claimed as a bit bound or a stable floating-point algorithm.

No attack performed before withdrawal produced a counterexample to an input claim. The dependence, cancellation, source geometry, probability allocation and execution steps discussed above were supported by the inspected proof bodies. No scientific objection or missing scientific input had been identified at the stop. This observation is not a final verdict on the withdrawn package.

## Component status at withdrawal

| Component | Provisional observation |
|---|---|
| Complete unchanged dependencies used by additions | No objection found before stop |
| Finite source probability and dense lower comparison | No objection found before stop |
| Third-order Legendre error and polynomial sufficient width | No objection found before stop |
| Capped Taylor width, source rank and retained count | No objection found before stop |
| Numerical source routine and exact pairing/endpoint transfer | No objection found before stop |
| Harmonic supplied and fresh implicit setup claims | No objection found before stop |
| Taylor supplied and fresh implicit setup claims | No objection found before stop |
| Adaptive two-direction Gaussian coupling and exhaustive cost ledgers | No objection found before stop |
| Compatibility of Taylor setup with its polynomial source/count gates | No objection found before stop |

The read coverage and executed checks above are the actual work completed before the stop. No candidate file was modified. Final review revalidation and acceptance were not performed after withdrawal. Overall status: **PARTIAL / NOT COMPLETE (withdrawn v1)**. A fresh review of the corrected frozen packet is required; this report cannot serve as an acceptance verdict for it.
