# Independent complete adversarial review A — frozen C.4.8 version 2

**Verdict: PASS for the entire frozen mathematical package.** I found no required correction, unresolved correctness objection, or missing scientific input. The source-response estimate supports the actual influence construction, and the sampling and finite-GF arguments establish the stated conclusions with their stated limit order. This verdict concerns the candidate and exact summary edits listed below; it does not assert any of the expressly excluded stronger conclusions.

Reviewer: `/root/review_v2_a`. Review completed on 2026-09-11 in `/home/amir/Codes/PDE`.

## 1. Isolation, ownership, and read completion

I started from the neutral assignment `studies/trained_prediction_sampling/review_packet_v2.md`. I am distinct from the listed authors/assemblers (`/root`, `source_response_route`, `statistical_route`, `weak_topology_route`), selector, and other reviewer. No author conversation, prior verdict, selector report, other candidate version, study README/history, other study, Git history, or other review was used. I did not communicate with the other reviewer or delegate any part of this personally required complete read. No external scientific source was needed or retrieved.

I personally read `solve-math-rigorously/SKILL.md` and `investigate-conjectures/SKILL.md` under `/etc/codex/skills/`, and the latter's `adversarial-audit.md`, `research-contract.md`, and `decisive-experiments.md` references. The computation was restricted to the two assigned deterministic identity checks and read-only consistency checks; no training experiment or sweep was run. The neutral packet's independent-review scope replaced ordinary author startup. No Git operation or established-source edit was performed.

Complete scientific read coverage:

| Input | Personally read scope |
|---|---|
| `proposal_C4_8_v2.md` | All 1–1552, in consecutive reads 1–400, 401–820, 821–1220, 1221–1552 |
| `promotion_edits_v2.json` | All 1–23 |
| `check_gaussian_calculus.py` | All 1–146 |
| `check_sampling_hoeffding.py` | All 1–368 |
| `docs/global_nonlinear.md` | All authorized 1840–2453; 2924–3440; 3836–4946; 5268–11436 |
| `docs/special_data_limits.md` | All authorized 3785–4286, including complete III.F.1–10 |
| `docs/finite_dynamics.md` | All authorized 1–227 |
| `docs/README.md` | All 1–284 |
| `docs/NOTATION.md` | All 1–98 |
| `AGENTS.md` | All 1–47 |
| `RESEARCH_WORKFLOW.md` | All 1–224, including complete promotion requirements |

The long global-nonlinear intervals were read consecutively: 3836–4380 / 4381–4946 and 5268–5900 / 5901–6550 / 6551–7200 / 7201–7900 / 7901–8600 / 8601–9300 / 9301–10000 / 10001–10700 / 10701–11436. There are no unread scientific gaps inside the authorized scopes. Unlisted complements of dependency files were not proof inputs.

Two output truncations were repaired. An early aggregate output truncated the combined README/notation/summary-edit read; I reread that entire combination with adequate output allowance. The 3785–4286 special-data output truncated within III.F.5; I reread 4020–4090, including the omitted regularization and zero-noise proof in full. No truncated proof was accepted as complete.

Writes are confined to this report and the assigned reviewer-A generated outputs. The two generated paths were first used by this review; the sampling program enforces fresh-directory creation.

## 2. Frozen-input integrity

I ran `sha256sum` on all eleven frozen inputs before substantive scientific reading and again after completing the reads and executing the checks. Every before hash matched the packet, and every after hash matched its before hash. The following values are **both the verified before and verified after hashes**:

| Input | SHA256 before = SHA256 after |
|---|---|
| `studies/trained_prediction_sampling/proposal_C4_8_v2.md` | `98fa7614b6449b58b07c65df047b68a3484bf0760b36a3a25052f67d72692928` |
| `studies/trained_prediction_sampling/promotion_edits_v2.json` | `50a95f4576c56c1438974a76da25a793ebe188e39c00e2f98f79bd79cb294f2c` |
| `studies/trained_prediction_sampling/check_gaussian_calculus.py` | `118b4d359f9c0e2dcfd42ab3b70df2c3e7970d940f9c1c463aaf96df13700cef` |
| `studies/trained_prediction_sampling/check_sampling_hoeffding.py` | `4a681e66870b25bccaed976cfc171bc29491a28ea235e15be0e64f9a0f5c807a` |
| `docs/global_nonlinear.md` | `9e758665ec842167b3fa49ab3b3e6f4539ced45b65a85cda081cc5969258c226` |
| `docs/special_data_limits.md` | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| `docs/finite_dynamics.md` | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| `docs/README.md` | `5dce185a68fafd4f5f366b491e4b367cdbb9d55443b8ac83eb8f5da3d417a19a` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `AGENTS.md` | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |

## 3. Contract and dependency audit

The target is the exact two-hidden-layer, bias-free tanh model with normalized circle input, bounded labels, stored Gaussian variances `(1, 1/n, 1/n²)`, output normalization `1/n`, mobilities `(n,1,n)`, unhalved integrated squared loss, and physical GF through 40. The first state block retains both first-row coordinates; the middle learned increment is Hilbert–Schmidt, and the initial action is the specified common Gaussian construction with its actual adjoint. These agree with the complete supplied notation, finite equations, C.4.1–3, and C.4.7 bodies.

The C.4.7 dependency actually supplies the needed finite-Euler source cap in a positive neighborhood. I checked its two distinct continuations: physical reference clock Euler is bounded through a fresh-root pulse argument, differentiated raw-to-clock defects transfer the bound to reference raw Euler, and the weighted same-passive-input comparison transfers that reference cap to nearby finite laws. Source masses remain attached to old pulses; duplicated reference atoms do not enlarge rows. The raw comparison uses the tail-bearing reference and does not assume the unknown changed-law trajectory's tails. The subsequent strong completion and finite proxy argument supply the actual map and finite-GF capture used here.

The authorized III.F bodies establish the finite source rule, singular-query regularization, common carrier, bounded actions, adjunction, and raw Hilbert–Schmidt convention. I checked the causal conditioning and response correction; independence of oriented *source groups* does not replace the reused matrix and its transpose by independent answers. The A.1–2 extensions cover the finite tanh backward products. The candidate uses those constructions, rather than an arbitrary operator of the same norm.

C.4.7 chooses its final radius inside the source-cap neighborhood. Consequently the candidate's nested radii (the requested quarter ball, response half ball, and larger three-quarter ball) have the margins needed for contaminations and approximation. No useful numerical radius or uniform failure probability over base laws is claimed. The population expectations are deterministic on this carrier, so the sampling limit does not conceal a random-environment Gaussian mixture.

## 4. Adversarial mathematical checks

### 4.1 Exact equations, feedback, and initialization — PASS

I differentiated S2 and S4 directly. S23–S27 include the derivative of the residual in `gamma`, both covariance derivatives, and the alpha/beta response derivatives. The explicit coordinate derivatives correctly have no derivative of a chosen Gaussian square root; law changes enter the expectation calculus S22. The construction is chronological: lower expressions use earlier reverse sources, their expectations determine current forward data, upper expressions determine current reverse data, and only then the raw lower update occurs. There is no same-node fixed-point assumption or supplied future forcing.

At the first Euler step, `w1=g`, `K1=0`, and `c1=2h Σ p_a y_a tanh(ξ_0a)`. Thus the first-step prediction is linear in masses and its mixed second mass derivative is zero. This verifies the loss factor, signs, and zero population readout against the written recursions. At finite width the original Gaussian readout is retained in P18–P20.

### 4.2 Unbounded multiplication and mesh-independent source jets — PASS

The main attempted obstruction was growth with the number of source slots, or an uncontrolled product of two merely L² quantities. S10 controls the time-weighted absolute Q sum by Jensen and the scalar Gaussian exponential moment without taking a maximum of Gaussian histories. S14 then has the correct highest-jet coefficient `2R0 D0 + 4R0 q_k`. Its random integrating factor has every separately fixed moment. Products of lower-order jets are controlled at larger finite moment orders. This proves S13 without assuming bounded multiplication on an ambient L² ball.

For the upper jets, the entrywise F bound retains `h_s p_a`, and the Volterra inequality S16–S17 has coefficients independent of source count. Repeated differentiation of one old source retains only its original mass factor: `∂_ξ^j(hp φ(ξ))=hp φ^(j)(ξ)`. The candidate explicitly avoids replacing that factor by `(hp)^j`. Its full absolute tensor sums also include repeated diagonals.

I checked S18 by differentiating the sum of lower raw increments, applying Minkowski before any input maximum of Q, and then using the integral formula for the feature difference. Each term has a jet of `w_k-w_b`, hence a factor equal to the interval length. The interpolation between row endpoints in that formula requires only their already bounded jets. The boundary lower expression depends exclusively on old reverse sources. This gives the crucial cancellation in S30–S31, including when the separately summed alpha index is old but one covariance index is new.

### 4.3 First and second mass-response absorption — PASS

The strongest attempted failure was an absorption length secretly depending on derivative history or on arbitrarily high moment orders. The first-response equations are linear in the unknown response. Splitting the explicit linear recursion into its current-forcing part and old-history part gives the separation claimed in S29: the current-E part has zero incoming derivative history and carries an interval sum, whereas old response moments enter only the additive constant. Hölder may require larger finite history moments, but these are obtained after absorption and never alter its coefficient.

The lower covariance new block costs `ell E` by S30–S31. S32–S33 then give the same factor in the entire forward covariance/row responses, even where they contract against old base coefficients of total mass bounded through T. Upper response propagation uses bounded upper jets and the F density; S34–S35 do not lose that small factor. S36 closes all deterministic components defining E. Only a finite list of low source orders and base moments determines `C_*`; the chosen interval need not make all higher-order constants small. A fixed finite number of groups covers T for every sufficiently fine mesh.

I differentiated the displayed second equations S37–S42 and checked the terms in S38. The mixed covariance term, both separate first-covariance/explicit-response terms, and the product of covariance derivatives with the fourth source tensor all occur with the correct factors. For alpha/beta these require base order five and first-response order three, both already furnished. Every mixed-second unknown has the same base linear coefficient as at first order. Products of first responses enter only the additive `C SR` forcing. Therefore S43 closes with a base absorption constant, and bilinearity preserves the two TV factors. No mass denominator or covariance-rank dependence is introduced.

### 4.4 Singular covariance, zero masses, and boundary directions — PASS

The proof of S19–S20 adds `eta I`, performs Gaussian integration by parts, and removes the regularization using uniform Gaussian moments and parameter-compact continuity. Passing the integrated identities and using the fundamental theorem supplies derivatives even on a rank-changing PSD family. It never differentiates a covariance square root or reconstructs named derivatives from a singular support.

At a fixed finite graph the coordinate expressions and required derivatives have polynomial envelopes, locally uniformly in mass parameters. Chronological Gaussian expectation formulas thus supply the finite mass derivatives before any uniform estimate. Continuous extension from positive masses handles unused atoms and one-sided admissible segments/rectangles. Constants do not depend on the minimum positive mass. Current duplicate queries have their one named diagonal coefficient; other current coefficients are zero. At zero initial readout the reverse covariance and response vanish, and the same formulas remain defined. Zero directions give zero response by linearity/bilinearity. None of these cases requires an inverse Gram matrix.

### 4.5 Actual Borel-law influence and centering — PASS

P8 has remainder `M epsilon² ||delta_z-lambda||TV²/2 ≤ 2M epsilon²`. Comparing derivatives to the same forward quotient and then sending the meshes to zero proves Cauchy convergence of the derivatives in the supremum output norm; value convergence alone is not incorrectly differentiated. The uniform quotient comparison passes to arbitrary laws by W1 density and continuity. It yields P9 and joint continuity of I on the compact half-ball times the compact observation space.

I checked centering through its two limit passages. On each finite simplex the weighted sum of atom directions is identically zero. Mesh convergence preserves this identity. Joint continuity makes the finite-law kernels converge uniformly in the atom, and weak convergence integrates a continuous Banach-valued function in norm by the finite partition-of-unity argument supplied in the candidate. This establishes the actual Bochner identity P10.

P11 follows by approximating both laws with a common finite discretization, preserving the TV upper bound; probability-preserving directions can be rescaled from an admissible positive segment. Interior segments and rectangles have the margins required for these approximations. P12 uses only four value limits, rather than assuming an unproved second derivative of the limiting flow. The resulting P13 is a specified evolution-and-limit procedure, with the complete source feedback, and is independent of meshes and admissible quantizations.

### 4.6 Localization and empirical remainder — PASS

The principal statistical obstruction is that nonatomic empirical laws generally do not approach the base law in TV. The proof never uses such convergence. It needs only W1 convergence for continuity of the first kernel, and TV-small single and double replacements.

I verified the finite continuous-test partition and the coupling constant `D/2` in R11. The cutoff support lies in the radius-half neighborhood, while the derivative estimates hold on a larger neighborhood. Its derivatives vanish at the cutoff boundary. The exact product identity R14 has the correct four coefficients. Subdivision of a general probability rectangle into cells inside the analytic region or the zero region preserves the mixed-difference bound by telescoping; cell area factors sum to one. The centered kernel remains bounded and agrees with I near the sampling law.

The centered log-mgf variance bound gives the stated `2N exp(-m b²/2)` exceptional probability. For the global calculation, I checked the conditional telescoping bias `≤2M_*/m`, the Hoeffding orthogonality, and the double-replacement factor four. Summing pairs gives `E||R_m^H||² ≤2M_*²/m²`, including m=1. The first projection R21 has error at most `4M_*/m`; continuity in the fixed `L²(mu;H)` norm and boundedness imply R22 without any quantitative modulus. The three orthogonal terms in R23 are exact; the first two contribute at most `6M_*²/m` after scaling. Thus the claimed mean-square little-o follows. A singleton observation space and a zero influence are explicitly harmless.

### 4.7 Covariance, CLT, and finite GF — PASS

The influence is bounded and continuous as a C(circle)-valued map, so the needed Bochner measurability, separability, centering, and second moment hold. The covariance is positive and self-adjoint, and Tonelli/Parseval give its finite trace. The finite-projection CLT proof has a uniform tail second-moment bound, closing the Hilbert limit. The continuous spatial kernel P16 follows from joint atom/input continuity and boundedness; the result concerns continuous linear spatial tests in H and does not infer an L² point-evaluation CLT. Rank-zero and other degenerate covariances are admitted. Cauchy–Schwarz with P4 proves the precise second-moment expansion P17.

P18 uses the ordinary finite Frobenius norm for the middle increment: `||Delta h^T/n||F` is the product of the two RMS norms. Its readout inequality first gives a finite exponential bound, then the middle and full first-row inequalities integrate to finite bounds. Local finite-dimensional smoothness consequently extends GF on every sample outcome, including laws outside UY. Smooth dependence supplies measurable H-valued statistics.

For fixed m and each realized law inside UY, C.4.7.NW1 applies with the unchanged independent initialization distribution. Conditional convergence in probability implies convergence of the bounded truncated error expectation; outer bounded convergence proves P19. This single coupling bounds all BL tests simultaneously. Outside UY their difference costs at most two, with exponentially small sampling probability. Taking width first, then m, proves P6. No width rate, joint fluctuation scaling, finite-width second-moment theorem, or finite-network tangent convergence at arbitrary base laws is inferred.

## 5. Executed checks and retained outputs

Working directory for both recipes: `/home/amir/Codes/PDE`. Runtime: Python **3.10.12**. Both programs were read completely before execution; both exited **0**.

```text
python studies/trained_prediction_sampling/check_gaussian_calculus.py --output data/generated/trained_prediction_sampling/review_v2_A/gaussian_report.json
python studies/trained_prediction_sampling/check_sampling_hoeffding.py --output-dir data/generated/trained_prediction_sampling/statistical_checks/review_v2_A
```

The Gaussian program passed all **six** exact polynomial identities: first derivatives in both parameters and the mixed second derivative for each of two observables. Its independent oracle substitutes `X=(G0+sG1,G0+tG1)` and integrates monomials using scalar Gaussian moments. The covariance determinant is `(s-t)²`, so the identities include the rank-one line. I checked the polynomial differentiation and expectation implementations and all displayed output.

The sampling program passed **748** exact assertions with 16 base states, six replacement pairs, and 64 configurations per pair. I inspected its entire generated JSON output. All Hoeffding orders 1–4 have positive energies. The direct higher-order second moment is `11044728/390625`; the pair-sum bound has strict positive slack `30270672/390625`. The direct and decomposed scaled remainder moments are both `548332/3125`, and all three contributing terms are nonzero. The fixture therefore tests the identities without collapsing to an additive or second-order-only statistic.

Retained output hashes:

| Output | SHA256 |
|---|---|
| `data/generated/trained_prediction_sampling/review_v2_A/gaussian_report.json` | `74379f1ba103d4dbb1f24ab221c3d38eb247ac3d364339b07a828f1378342e6c` |
| `data/generated/trained_prediction_sampling/statistical_checks/review_v2_A/report.json` | `4ba508009425f255fb1508c2b7d0509c97b505ff96a449ae159ef5e838bcee10` |

These are algebraic checks only. They do not certify the neural source estimate or asymptotic hypotheses; those received the separate proof audit above. No numerical training evidence is claimed by this package.

I also checked each exact summary replacement against its authorized target text. Each old string occurs exactly once (the global-nonlinear check was restricted to its authorized C.4 excerpt). The summaries state the same smaller-neighborhood, fixed-time, actual-influence, H-Gaussian, mean-square, and width-first conclusions. They introduce no GD, all-time, nondegeneracy, generalization-superiority, or finite-width rate claim.

## 6. Required corrections and final judgment

**Required corrections: none. Missing inputs: none. Unresolved objections: none.** No presentation suggestion is being treated as a proof condition.

All components pass: exact model and source provenance; mesh-uniform first and second finite-program mass responses; singular and zero-mass calculus; actual Borel influence and centering; local-to-global Hilbert sampling remainder; covariance and Hilbert CLT; actual finite-GF existence and width-first bridge; deterministic implementations; and exact summary scope.

The entire frozen version-2 package passes this independent complete adversarial mathematical review. The positive neighborhood and every separately fixed base law, horizon 40, H sampling topology, bounded exceptional-law extension, and width-before-sampling limit remain essential parts of the accepted statement.
