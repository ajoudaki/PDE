# Round 1 — Independent adversarial mathematical review B

## Verdict: PASS

The document establishes the full theorem as stated, including existence and uniqueness in the stated class, restart from every reached state, the removal of clipping, the exact raw-GD limit with its physical clock and prescribed interpolation, hidden velocity and whole-path convergence, and the nonlinear/non-lazy conclusions. I found no fatal gap, repairable mathematical proof omission, false mathematical assertion affecting the theorem, or counterexample. No mathematical repair is outstanding.

This verdict concerns the theorem's actual scope: fixed finite physical horizons; the constructed, common neuron spaces and initial operators; uniqueness among the specified integral solutions; the specified finite probe programs; and empirical/action-law convergence across widths. It does not assert existence from arbitrary population initial states, an infinite-time/width interchange, or an operator-norm comparison between different widths. Those extensions are expressly excluded by the document.

## Input integrity, full reading, and sources

- Sole mathematical source accessed: `/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md`.
- Required SHA256: `cca2fb10f658125f6ba5727be9c59655e050dedcce0552922cf23470ddab4ee7`.
- Observed SHA256, both before reading and after completing the audit: `cca2fb10f658125f6ba5727be9c59655e050dedcce0552922cf23470ddab4ee7`.
- Input size checked: 1,743 lines, 79,674 bytes.
- I read the entire document, including its theorem, all proof sections, and its concluding assertions. The numbered reading covered lines 1–220, 221–440, 441–660, 661–900, 901–1140, 1141–1380, 1381–1600, and 1601–1743, without an omitted interval.
- Source-access operations were read-only `sha256sum`, `wc`, and numbered `nl`/`sed` reads of that single input. The only file created was this report, using `apply_patch`.
- I accessed no other project file, research file, prior review, skill file, external publication, or web source. I did not search the project, contact another agent, edit the proof, or run a numerical experiment. No prior conversation or research lemma was used as mathematical input.

The checks below are analytic. Classical facts used in assessing the arguments include finite-dimensional Gaussian conditioning, Gaussian integration by parts, the law of large numbers, elementary measure convergence, conditional expectation and Hilbert-space projection, the countable probability-extension principle on real coordinate spaces, completeness, and the contraction principle. The document supplies the problem-specific Gaussian reuse, response, clipping, clock, and discretization arguments; I have not treated those as available external theorems.

## Obligation ledger

| Theorem obligation | Main locations | Audit result |
|---|---|---|
| Correct finite scaling, raw updates, kernels, and physical time | §1; §§9–10 | Established; the vector and matrix metric normalizations agree with the displayed updates. |
| Adaptive Gaussian calls in both directions, including singular Grams | §§3.1–3.4 | Established by conditional projection, empirical induction, the source rule, and vanishing input perturbations. |
| Identification of the actual feedback program | §4 | Established; empirical contractions are restored after the fixed deterministic-coefficient calculation. |
| Fixed common probability spaces and bounded initial actions with true adjoints | §5, (5.1)–(5.2) | Established; consistency, density, norm bounds, and transpose pairings provide the construction. |
| Fixed-clip existence, continuation, and mesh approximation | §5, (5.4)–(5.8) | Established on the bounded-readout path class used for the reference flows. |
| Mesh- and cap-uniform response control | §6, (6.1)–(6.11) | Established; the induction is causal and its arithmetic closes strictly below the bootstrap threshold. |
| Uncut population existence and uniqueness | §7 | Established through the asymmetric comparison and a Gaussian tail that dominates the comparison factor. |
| Restart from a reached state | §7; §9, (9.8) | Established, including competitors not assumed to satisfy a response estimate. |
| Uncut finite feature-flow limit and restoration of the small readout | §8 | Established; only the zero-readout reference requires a pointwise bound or tail estimate. |
| Actual gradient structure and all finite physical horizons | §9; beginning of §10 | Established; the predictor differentiability argument and the nonattaining scalar clock have the required hypotheses. |
| Exact raw GD, positive stopped clock, and removal of the stop | §10, (10.1)–(10.6) | Established, including the first stopped endpoint and the last interpolation node. |
| Same-width GD/GF state comparison | (1.7); end of §10 | Established by comparison with the same finite clipped reference at converging clocks. |
| Finite probes, unbounded gated fields, and quadratic observations | §§8, 11 | Established by norm comparison, truncation, and uniform second-moment control. |
| Recomputed hidden velocities for the specified raw interpolation | §11, (11.1)–(11.2) | Established; the within-step error is controlled at the stated step size. |
| Whole-path Wasserstein convergence and integrated squared velocities | §11, (11.3) | Established by finite-grid convergence and the energy bound on interpolation error. |
| Positive second-order motion and nonconstant kernel | §§12.1–12.2 | Established; the transpose innovation variances and expansion coefficients are correct. |
| Persistent nonaffinity of all hidden laws | §12.3 | Established by two-sided support bounds and continuity of the affine-fit error. |
| Nonzero hidden feature velocities at every positive finite physical time | §12.4 | Established by sequential backward nondegeneracy and adjoint identities. |

## Detailed audit

### 1. Setup, normalization, and elementary tools

**§1, lines 18–161; equations (1.1)–(1.7).** The backward fields correctly omit the residual. With vector squared norm divided by `n` and ordinary matrix Frobenius squared norm, the gradient of the finite predictor has vector entries `delta^(1)` and `h^(3)`, and matrix entries `delta^(ell) (h^(ell-1))^T/n`. Multiplication by `-2r` gives exactly (1.3) per physical-time unit. The four squared gradient contributions are precisely (1.6). Thus the relative layer scaling, the factors of `n`, and the factor two from the squared loss are consistent.

The coordinate transformation is also consistent: `F'(z)=10(1+z^2)=1/phi'(z)`. It changes the first continuous equation to `X_s=q^(1)` in feature time, but does not turn a raw finite GD step into an exact Euler step in `X`. The document explicitly preserves that distinction and later estimates its error.

The theorem's cross-width assertion is a law/action assertion, whereas (1.7) compares two algorithms on the same finite-dimensional parameter space. The proof does not conflate these two notions of convergence.

**§2, lines 163–190.** The activation floor and ceiling follow from the stated bound on pi. The derivatives of `phi`, the bound on `phi''`, the inverse Lipschitz constant, and (2.1) are correct. Treating `(G,F(G))` as an initial root tuple is essential and legitimate: it has finite moments of every order, although `F` is not globally Lipschitz.

The two-sided net argument gives the factor two in the operator bound. Each fixed bilinear form has variance `1/n`; the union bound therefore gives (2.2). Its exponential exponent dominates the net cardinality. Passing to both independent initial matrices requires only a union bound. The initial readout estimate is correct: its normalized squared norm has expectation `n^(-2)` and its normalized norm is `O_P(n^(-1))`.

**§2(a)–(b), lines 194–219.** Weak convergence plus convergence of second moments gives uniformly small squared tails, and the bounded-cell coupling argument yields finite-dimensional Wasserstein convergence. In extracting a usual squared-tail bound from the excess above a truncated second moment, one can use a larger cutoff; this is an elementary inequality, not an additional moment hypothesis. The passage to continuous quadratic-growth tests is valid after truncation. Compactness of a continuous `L^2` image supplies the uniform integrability later used along a time interval.

**§2(c), lines 221–240.** The index coupling in (2.3) is valid. Smooth saturation of bounded factors gives the required globally Lipschitz product instructions. The bounded-multiplier convergence assertion (2.4) is correct: split off the strongly convergent factor, truncate the remaining fixed `L^2` factor, and use convergence in probability on the bounded part. Its use for a differentiable `L^2` curve is legitimate and does not assert the false general Fréchet differentiability of a nonlinear `L^2`-valued Nemytskii map.

**§2(d), lines 242–254.** Both discrete and continuous comparison statements are valid for the nonnegative coefficients/forcings to which they are applied. In particular, the discrete estimate can be applied pathwise to the later random positive partition; probabilistic independence of its steps is unnecessary.

### 2. Gaussian reuse and singular queries

**§3.1, lines 272–297; (3.1)–(3.2).** The conditioning formula is the Gaussian orthogonal projection onto the observation `Wh=y`. The transpose residual is a projected standard Gaussian multiplied by `||u||/sqrt(n)`. The removed component has fixed rank and vanishing normalized squared size. The innovation variance is the full second moment of the reverse input, as stated; subtracting the response variance here would be erroneous. The displayed division assumes a nonzero input; the zero/singular cases of the general program are subsequently covered by §3.4, so this is not an uncovered theorem case.

**§3.2, lines 299–355; (3.3)–(3.4).** The first two terms of (3.3) satisfy both observations, using `U^T Y=Q^T V`, and the residual is orthogonal to both constraint spaces. Adaptivity does not permit an independent resampling of the used matrix, but it does permit this conditional residual representation: the next query is determined by the already revealed transcript. Revealing it adds only the new linear constraint on the queried residual. This also preserves conditional independence of the residuals of the two different matrices.

For (3.4), the deterministic mean and the Gaussian residual have the stated coefficients. With a fixed number of queries and positive definite limiting input Grams, inverse continuity and second-moment convergence justify the coefficient limits. The discarded output-space projection has fixed rank; its normalized error vanishes with the required bounded-in-probability variance multiplier.

The empirical induction is sufficient for joint laws, not just single-coordinate distributions. After dropping the negligible projection, the conditional Gaussian coordinates are independent given the transcript. The conditional variance bound for bounded tests tends to zero, and their integrated conditional expectations are tests of the previous tuple. The displayed bounds on Gaussian cross terms and centered squares establish convergence of second moments. This closes the induction in Wasserstein distance and also justifies the scalar contractions.

**§3.3, lines 357–409; (3.5).** The response rule is derived rather than assumed. In particular, the component of an old reverse answer along old forward inputs disappears when paired with `h_perp`. Gaussian integration by parts then gives the product of the reverse-input Gram and the expected formal source derivative. Substitution cancels the derivative contributions from the old forward projection. The new forward Gaussian source has the stated uncentered covariances because the innovation variance is the squared norm of the input projection residual.

Holding earlier deterministic coefficients and covariance parameters fixed is the correct derivative convention for this calculation. The differentiation is of the coordinate expression, not of the procedure selecting its law. Derivatives through uses of the other matrix remain present. Bounded first derivatives and integrable roots suffice for the conditioning and integration by parts used here. The singular Gaussian integration-by-parts identity itself follows from the stated factorization into standard Gaussians.

**§3.4, lines 411–457.** Fresh input perturbations make each limiting Gram Schur complement strictly positive. At fixed program length, operator-norm control and Lipschitz propagation give an `O(epsilon)` comparison with the original program, uniformly in width on events of probability tending to one. No estimate uniform over a diverging number of queries is inferred from this argument.

The scalar zero-perturbation limit does not require convergence of Gram inverses. It uses the causal response formula instead. At each of finitely many instructions, bounds on earlier coefficients bound the new formal derivatives and hence the new expected derivative coefficients. Continuity of covariance square roots, coupled Gaussian inputs, and continuity and boundedness of the coordinate derivatives give the next limit. This is a finite induction and is not an assumed uniform control near singular inverse matrices.

Keeping formal slots at a rank drop is consistent. If a coefficient change lies in the null space of the source Gram, its contraction with the corresponding reverse-input tuple is zero almost surely. The width limit and the perturbation limit can therefore be combined in the order given. This covers degenerate and repeated queries, including the zero backward fields at initialization.

### 3. Actual clipped program and common spaces

**§4, lines 459–590; (4.1)–(4.6).** The proposed smooth clipping construction has all the displayed properties. Only the middle backward query is clipped, and the forward activations and top readout remain those of the actual program.

Unrolling the rank-one updates yields (4.2), with the correct normalized finite contractions. At a fixed mesh and clip, the oracle instructions meet §3's hypotheses. The bounded top readout permits the stated smooth extension of its gated product; the middle product has bounded first derivatives because its query is clipped. The initial transformed field is supplied as a root, rather than passed through an impermissible globally Lipschitz use of `F`.

Restoring empirical contractions is a finite causal induction. The pairing difference inequality has the correct norm factors, and only fixed-program norm bounds and contraction errors are used. Hence the argument identifies the actual finite program, not just an oracle with externally fixed coefficients.

The source covariance formulas retain full second moments. The forward corrections use only past backward inputs, whereas reverse corrections may include the current forward input. Formula (4.6) correctly includes the present return through matrix 3 in the current matrix-2 response. This term is also retained in the subsequent derivative estimates; it is not silently discarded after being written down.

**§5, lines 592–647; (5.1)–(5.2).** Finite unions of programs have limiting same-layer laws because they are finite calculations using the same finite initialization. Their marginal consistency is thus justified. A countable family of such laws on real coordinate slots has the required probability extension. Separate neuron spaces are appropriate, since no cross-population coordinate pairing is claimed.

The generated fields are dense in each layer's `L^2`: conditional expectations reduce to finitely many slots, truncation reduces to bounded functions, regularity of a finite-dimensional Borel probability law permits continuous approximation, and the included countable function family supplies the remaining approximation. The needed identities for derived coordinate slots follow from their joint finite program laws.

The high-probability finite operator bound passes to each deterministic limiting squared-norm inequality. It also identifies zero-equivalent inputs, so it defines an action on `L^2` equivalence classes. Density gives a bounded extension. The finite transpose identity passes using joint second moments and extends by continuity, making the reverse action the adjoint of this same operator. This is stronger than merely specifying two actions with matching marginal distributions.

Real coefficients and fixed Lipschitz probes can be included by approximation and the bounded action estimates. The trained operator stores its full rank-one increment. Neither the state space nor the number of state objects grows when the mesh is refined.

### 4. Fixed-clipping analytic existence and stability

**§5, lines 649–690; (5.3)–(5.6).** The state norm is a Banach norm, and its finite counterpart matches (1.7). The coarse estimates follow in the order readout, matrix 3, matrix 2, first coordinate. They only use bounded activations, bounded gates, the rank-one norm identity, and contraction of the clip. They are consequently uniform in clipping and width. They also apply to positive Euler prefixes of bounded total feature time. With zero initial readout, the stronger pointwise bound (5.6) follows directly by integrating the positive bounded top activation.

**§5, lines 692–727; (5.7).** The forward difference estimate uses the correct `1/100` Lipschitz constant for `chi`. At the top gate, placing the reference readout against the gate difference is the important asymmetric choice: the other readout needs only an `L^2` bound. The resulting query difference is controlled in `L^2` by the state distance. The middle gate difference costs a factor proportional to `R`, because the reference clipped query is bounded. Reverse actions and rank-one differences then give the stated `C_S(1+R)` bound. The normalized finite-width versions have the same constants.

**§5, lines 729–757; (5.8).** The fixed-point construction is performed on the appropriate closed path set with the bounded pointwise readout constraint. It does not assert local Lipschitzness on an unrestricted `L^2` neighborhood of readouts. The integral map preserves the readout bounds; a short interval preserves the enlarged primal bounds and makes it a contraction. The prior uniform bounds allow continuation by finitely many intervals on any fixed feature horizon.

At finite width, smoothness and the corresponding boundedness give the uncut feature flow as well. For fixed clipping, the local Euler defect and the resulting global `O(Delta)` state error follow from the Lipschitz field and the velocity bound. In the width-limit application, the pointwise-bounded, zero-readout references are the ones being approximated. Fixed-program convergence followed by mesh refinement is therefore legitimate. Finite time nets and the stated norm continuity yield uniform convergence for finite probe/time lists without applying §3 to a diverging program.

### 5. Response bootstrap and its constants

**§6, lines 759–945; (6.1)–(6.11).** This is the main quantitative argument. I checked both its derivative recursions and its numerical inequalities analytically.

The initialization of the row sums is valid even with degenerate backward sources. A formally nonzero derivative in a zero-variance backward direction is not equated to zero merely because the source vanishes. What vanishes in the initial reverse-response rows is the relevant derivative of the initially zero gated readout/backward field.

Under the past-row bootstrap, a single bottom-source derivative enters the `X` recursion with one factor of `Delta`. The discrete comparison gives (6.2). Thus there is no missing factor of the number of source slots in the bound on `a^(2)`.

For the middle forward derivative row, the direct source contributes one, while all older derivatives enter through the past update sum. The query derivative contains the complete matrix-3 return. Bounding it by the row sum `V_r` yields (6.3). For a single middle reverse source there is only one direct forcing contribution, of size at most `A Delta/10`, giving (6.4). The strictly past-time forward recursion prevents a hidden current-source equation.

The envelope estimate uses marginal Gaussian moments and Jensen over the time slots. It does not require independence between times, independence of the response shift from its source, or a bound on a path supremum. With `A=S=3/2` and `a=7/6`, the constants in (6.5) are exactly

```
A S (a/5 + 1/100) = 219/400,
(1/2) (A S/5)^2 (a S/10)^2 = 3969/1280000.
```

For `p=1,2`, the resulting estimates imply `||E_j||_1<4` and `||E_j||_2<3`. The two bounds on the forward coefficient are strict:

```
49/36 + 1/50 < 3/2,
49/36 + 3/50 < 3/2.
```

For the top derivative row, the readout-derivative term and the top-gate term sum to `(73/300) S` times the preceding derivative-row maximum. Together with the forward coefficient estimate this gives exponent `657/800`. The document's elementary comparison with `5/2` is valid: `657/800<5/6` and `3^5 2^6<5^6`.

The current top row consequently satisfies

```
(73/300)(3/2)(5/2) + (49/36)(3/2)^3/100
    = 73/80 + 147/3200
    = 3067/3200 < 1.
```

Only after obtaining this current top-row bound does the proof bound the current middle query. Its coarse norm bound is `Q=7/40+7/6=161/120`. The current middle response then obeys

```
3(Q/5 + 1/100) + (3/2) Q^2/100
    = 167/200 + 77763/2880000
    = 2482563/2880000 < 9/10.
```

This closes the simultaneous induction without using the current `U_k` as an assumption. The bound on `a^(3)` used for the current top row depends only on earlier rows through the middle envelope. That dependency is also causal.

Finally, the response shift of the actual query is bounded by `a`, and its Gaussian source variance is at most `(7/40)^2`. The exponent and Gaussian-square integral in (6.11) are correct:

```
2 a^2/16 = 49/288,
1 - 2(7/40)^2/8 = 1 - 49/6400.
```

The displayed upper bound is strictly less than two. This supplies a cap-, mesh-, and time-uniform exponential-square moment of the identified query itself. It is the estimate required for clipping removal, rather than an assumed tail estimate for an unconstructed uncut process.

### 6. Clipping removal, unrestricted competing solutions, and restart

**§7, lines 947–958; (7.1).** Fixed-cap state convergence implies strong convergence of the computed middle query using (5.7). An almost-everywhere convergent subsequence and Fatou transfer the exponential-square bound. The subsequence may depend on the fixed time and cap: the conclusion is a deterministic moment bound at every time, and therefore a bound on their supremum. No simultaneous almost-sure convergence over uncountably many times is needed.

**§7, lines 960–998; (7.2)–(7.4).** The asymmetric identity (7.2) is algebraically exact. Its last bracket is zero inside the reference cutoff and is bounded by twice the query magnitude outside. Both the field comparison and the middle-backward-field comparison depend on the tail of the reference state only. There is no hidden tail assumption on the uncut or larger-cap competitor.

The soft-tail function is continuous and Lipschitz, which is important when it is later measured at finite width. The exponential-square moment gives the stated tail bound. With `K=4`, the usable norm error is

```
epsilon_R = 8 exp(-R^2/256).
```

It dominates every fixed comparison factor `exp(CR)` and every extra polynomial factor in `R`.

**§7, lines 999–1015; (7.5).** The larger-cap versus smaller-cap estimate makes the family Cauchy in the complete uniform Banach path norm. Applying the same comparison to the limiting state and a capped reference shows convergence to the actual uncut vector field. The extra factor `1+R` still tends to zero when multiplied by the error bound. Thus the passage through the unbounded middle product is strong and quantitative. Uniform convergence of the continuous capped velocities supplies a continuous limiting velocity, and the integral equation gives a continuously differentiable solution on all of `[0,3/2]`.

**§7, lines 1017–1027.** Uniqueness is proved against an arbitrary bounded-primal continuous uncut integral solution on the same spaces. Its own bounds enter only the finite comparison constant. It need not possess Gaussian tails, a source representation, or the response bounds of §6. Since the tail error wins against every fixed such constant, the comparison identifies the competitor.

The restart argument also addresses the mismatch between the reached uncut state and the state of the original capped reference at the restart time. That mismatch is already exponentially small in the squared cap. Multiplication by the new comparison factor on the remaining interval still makes it vanish. The proof therefore establishes restart uniqueness from each reached state without falsely assuming that a freshly restarted clipped system has a new Gaussian initialization law.

### 7. Finite uncut feature flow and small initial readout

**§8, lines 1029–1076; (8.1)–(8.2).** For each fixed cap, the soft-tail squared measurement is a continuous quadratic-growth test, and its square root is also continuous. The state speed bound and the asymmetric query estimate make the reference query uniformly Lipschitz in time in normalized vector norm. The soft-tail measurement inherits that property, giving the uniform-in-time statement (8.1) by a finite net.

The finite uncut flow is compared with a zero-readout finite capped flow using identical hidden initialization. This permits an `L^2`-small initial readout without imposing a width-uniform pointwise bound on that readout. The forcing in (8.2) uses only the reference's soft tail. First taking width to infinity at fixed cap, then letting the cap increase, closes the comparison. No finite-width exponential-moment estimate is presumed.

The separate middle-backward-field estimate is necessary and is supplied. It controls `delta^(2)` despite its unbounded query factor; bounded reverse operators then control `q^(1)`. This is sufficient for the later gated observations and velocities and is not merely state convergence being misapplied to an unbounded multiplication map.

### 8. Gradient structure, physical existence, and the raw uniqueness class

**§9, lines 1078–1136; (9.1)–(9.4).** Initial Gaussian actions are allowed to be non-Hilbert–Schmidt. Their trained increments are integrals of continuous rank-one Hilbert–Schmidt velocities. The rank-one difference bound also holds in Hilbert–Schmidt norm, so the limiting increment is the same one previously obtained in operator norm. This justifies the affine Hilbert parameter space used for the gradient statement.

The predictor differentiability proof addresses the correct scalar functional. For each fixed `B` in `L^2`, (9.2) gives a small scalar Taylor remainder by truncating `B`, first sending the variation to zero and then the truncation to infinity. Forward variations are of the size of the parameter variation in `L^2`. Expanding from the top down places fixed old backward coefficients against each activation remainder. They belong to `L^2`. Terms involving two parameter/feature variations are quadratic. This proves (9.3), rather than appealing to an unavailable `L^2`-valued Fréchet chain rule.

The Hilbert–Schmidt pairing identity gives the stated gradient. Gradient continuity follows by strong convergence of matrix actions and the bounded-multiplier result with fixed old factors in reverse order. Thus the chain rule along the actual raw Hilbert-space curve is justified.

**§9, lines 1138–1179; (9.5)–(9.7).** The inverse-coordinate curve chain rule converts the feature flow into `theta_s=grad f`. Consequently `f_s` is the sum of the four nonnegative kernel blocks. The readout block is bounded below by `25/36`, while all blocks are continuous and bounded on the constructed feature interval.

The strictly increasing predictor has exactly one level-one point, with `0<s_*<=36/25<3/2`. Its bounded derivative supplies the upper estimate on `1-f(s)` needed for the logarithmic divergence of the physical-time integral. The inverse clock exists for every finite physical time. The direction of the bound in (9.6) is correct: `s_*-s(t)` has the displayed positive lower bound on each finite interval. The loss, residual, and physical gradient identities follow with the correct factors and signs.

**§9, lines 1181–1206; (9.8).** The raw uniqueness argument covers competitors not already assumed to lie in the transformed coordinate class. Their backward fields are continuous in `L^2` by bounded-multiplier convergence, and their rank-one integral equations yield Hilbert–Schmidt increments. The scalar predictor chain rule therefore applies to them. The bounded kernel gives the exponential deficit identity, so a reached positive deficit cannot vanish at a finite competing time.

Choosing absolutely continuous scalar representatives and applying the pointwise chain rule to `F` is legitimate. The right side of (9.8) belongs to `L^2`, since the initial reached transformed state belongs to `L^2`, the scalar multiplier is bounded on the compact interval, and `q^(1)` is bounded there in `L^2`. This establishes transformed membership instead of assuming it. The strictly increasing clock then allows application of the feature uniqueness result. Nonattainment of `s_*` excludes a finite physical exit from the part of the feature curve already identified. The same argument applies at every reached restart state.

This establishes the stated autonomous solution and restart class. The Gaussian coefficients in the proof are not extra state variables or external forcing in the resulting differential equation.

### 9. Exact raw GD and the stopped physical clock

**§10, lines 1208–1237.** Finite physical GF has a nonincreasing residual magnitude. Successive integration of the readout, matrix-3, matrix-2, and first-vector bounds prevents finite-dimensional finite-time escape. The gradient normalization is the one checked above. For the finite feature flow, `f_n(0)>-1/24` implies

```
f_n(3/2) >= f_n(0) + (25/36)(3/2) > 1.
```

Together with `f_n(0)<1`, this puts its level-one point inside the available feature interval. The finite physical clock is nonattaining as in §9. Uniform feature-predictor convergence and a Lipschitz scalar comparison give convergence of the clocks on every fixed physical horizon.

**§10, lines 1239–1261.** The GD stopping construction uses a strictly positive population deficit on `[0,T+1]`, not a positive lower bound uniform over infinite time. Before the first bad node, feature increments are positive. Bounded accumulated feature time bounds readout and operator norms and hence the predictor; this bounds each increment by a constant times `eta_n`. The step into a first bad node is included and lands before `3/2` for all sufficiently large widths. This avoids using an estimate beyond its established stopped domain.

**§10, lines 1263–1282; (10.1)–(10.2).** The cubic identity has the correct quadratic and cubic coefficients. The norm bounds require only the normalized Euclidean norm of `q^(1)`. In particular,

```
||q^2||_2 <= ||q||_2^2,
||q^3||_2 <= ||q||_2^3
```

are valid finite-dimensional inequalities. They give a normalized error bounded by `C(alpha_k^2 sqrt(n)+alpha_k^3 n)`. Summing a positive prefix with bounded total length gives `C_S(eta_n sqrt(n)+eta_n^2 n)`, which is `O(n^(-3/2)+n^(-3))` at the prescribed step size. No fourth- or sixth-moment assumption is concealed in this estimate.

**§10, lines 1284–1317; (10.3)–(10.6).** The reference-flow Euler defect, the asymmetric field comparison, and the raw-coordinate defect yield the stated recursion. All terms are valid through the first stopped endpoint. The Riemann-sum comparison for the soft-tail forcing is pathwise and uses the already established uniform time Lipschitz bound. Thus a random adaptive clock does not require an independence hypothesis. Discrete comparison yields (10.5). Taking width first at fixed cap and then removing the cap establishes the stopped predictor error uniformly over the prefix.

**§10, lines 1319–1339.** On each physical mesh cell the interpolated clock has exactly the stated slope. Comparing it with the population scalar clock produces the displayed integral error inequality; the node-to-cell difference costs only `O(eta_n)`. At a putative bad endpoint, clock convergence leaves a strictly positive margin between `36/25` and `147/100`, while predictor convergence leaves a strictly positive margin to `1-rho/2`. Both stop conditions are contradicted with probability tending to one. The use of `[0,T+1]` covers the ceiling node beyond `T` and a first bad endpoint at that node.

**§10, lines 1341–1357.** Applying the raw cubic identity to a fractional step controls the discrepancy between transforming the raw linear interpolation and linearly interpolating transformed nodes. The other blocks are already linear. GD and GF can then be compared with the same finite capped reference at their converging clocks. Its bounded speed controls the time shift, proving (1.7).

The limit order is valid for a full-sequence convergence-in-probability result: choose a cap, choose a fixed reference mesh, and then take all sufficiently large widths. The source-law theorem is never applied to the width-dependent number of GD steps. The earlier subsequences used for Fatou do not select the eventual width limit.

### 10. Observables, recomputed velocities, and whole paths

**§11, lines 1359–1405; (11.1).** Bounded operators and Lipschitz coordinate instructions propagate strong same-width comparison errors. The separately proved control of the middle backward field supplies the exceptional unbounded input. A bounded continuous gate times an unbounded `L^2` field is handled by truncating that field. Compactness of the limiting `L^2` trajectory and uniform Wasserstein convergence supply uniform squared-tail control in probability for the finite fields. This validates the successive gated products and subsequent matrix calls; it does not assume boundedness of the backward fields themselves.

Prediction and each kernel block are continuous quadratic-growth averages or finite products of such averages. The feature-time velocity formulas in (11.1) follow directly from the rank-one equations and the valid curve chain rule. The lower-layer gate is squared in the matrix-2 forward-velocity term, as required. The physical multiplier is `2(1-f)`. These formulas are covered by the preceding truncation and action comparisons, including joint finite time lists.

**§11, lines 1407–1445; (11.2).** The document separately treats the velocities of recomputed preactivations inside raw GD interpolation cells. Each raw parameter-block velocity is constant on the cell and has the required normalized vector or operator bound. Differentiating the forward equations gives bounded normalized hidden preactivation speeds. A cellwise normalized change of order `eta_n` gives a coordinate-supremum change of order `eta_n sqrt(n)` by the deterministic Euclidean inequality. Hence all gate changes have that same supremum bound.

Equation (11.2) is the exact derivative of the prescribed interpolation. Its contraction and matrix changes cost `O(eta_n)`; its changing gate multiplies a bounded normalized old velocity and costs `O(eta_n sqrt(n))`. The layer-3 recursion includes the already controlled layer-2 velocity change. Multiplication by the final feature gate has the same bound. Thus the discrepancy from the node velocity formulas is uniformly `O(n^(-3/2))` at the chosen step size. This argument does not need a uniform pointwise bound on the velocities. It also covers the terminal-left convention by comparison with the preceding node and continuity of the limiting velocity.

Uniform convergence of the velocity laws and squared norms therefore applies to the actual raw interpolation, and integrating the uniform squared-norm convergence proves the energy assertion.

**§11, lines 1447–1470; (11.3).** Continuous `L^2` velocities on the separable layer spaces have jointly measurable versions. Integrating them and using Fubini gives absolutely continuous scalar representatives of the population paths. Their squared supremum norms are integrable by the initial second moment and Cauchy–Schwarz in time.

The interpolation bound (11.3) is valid for an absolutely continuous scalar path. It bounds the maximum error on the whole interval by the mesh length times the full derivative energy; it does not incorrectly replace an expectation of a supremum by a supremum of expectations. It can be averaged over finite neuron paths or over the population.

On a fixed time grid, linear interpolation is a Lipschitz map from the finite tuple of values into the space of continuous paths with the supremum norm. Joint grid-law convergence therefore controls the interpolated path laws. The energy bound controls both interpolation errors, uniformly in width in probability. Taking width to infinity and then the grid mesh to zero proves the stated path-space Wasserstein convergence. The Lipschitz activation transfers it to feature paths.

### 11. Nonlinearity and non-lazy learning

**§12.1, lines 1472–1557; (12.1)–(12.6).** Initial Gaussian symmetry yields the displayed full second moments, which are strictly above one. The initial top backward direction is positive and square-integrable. Applying the one-forward/one-reverse conditioning formula gives the full, strictly positive innovation variance `E[(B^(3))^2]` for the first transpose law. The expression for `c_3` is correct: the odd contribution integrates to zero, and the remaining integrand is positive off zero. No pointwise sign claim for the discarded odd term is needed.

For the second transpose, conditioning on the independent third matrix and the second-layer forward observation leaves the residual of the second matrix unobserved. The new backward input is therefore admissible for the same conditional formula. Its second moment and contraction converge by the preceding joint law and truncation. This gives the stated `c_2` and full innovation variance. Both coefficients and all three `gamma` constants are strictly positive. The adjoint pairings in (12.6) correctly include the bottom-layer contribution; they imply that every leading hidden motion direction is nonzero.

**§12.2, lines 1559–1617; (12.7)–(12.8).** The readout integral first gives `W^(4)(s)/s -> H^(3)_0`. Bounded-gate convergence and operator continuity propagate the corresponding first-order backward limits down the network. Substitution into the velocity formulas gives (12.7) in `L^2`; integration of its norm-small remainder justifies the second-order displacement expansion. The rank-one expansion also holds in Hilbert–Schmidt norm.

The three hidden kernel coefficients are `gamma_ell`, while the readout kernel coefficient is `Gamma`, by the verified adjoint identity. Therefore the total feature-time kernel coefficient is `2 Gamma`. With `s(t)=2t+o(t)`, the physical-time coefficients in (12.8) are correctly `4 Gamma` for the readout block and `8 Gamma` for the total kernel. The leading physical feature velocity is four times `t` times its leading gated direction, giving the stated `16/3` coefficient for the integrated squared speed. These are positive fixed population coefficients, establishing the claimed non-lazy motion and nonconstant kernel.

**§12.3, lines 1619–1697; (12.9)–(12.12).** The top forward correction is uniformly bounded by `63/160`. For the middle correction, the dominating variable depends only on the backward source group, which is independent of the relevant forward Gaussian group. The actual correction need not be independent. Its expectation is bounded by `483/1600`, so Markov gives the stated `1117/1600` event probability. The bottom dominating variable is independent of the initial root; its expectation is `1561/800<2`, yielding the indicated probability at cutoff four. The oddness and monotonicity of `F` give the two bottom tail events with the correct signs.

The tail passage through mesh refinement and cap removal uses closed half-lines in the correct direction of the weak-convergence inequality. The resulting support is unbounded on both sides at every time; no density, joint almost-sure source limit, or Gaussian time-supremum estimate is assumed.

For a nonconstant square-integrable preactivation, minimizing over an affine function gives (12.12). If its error were zero, the bounded activation and unbounded support would force zero slope; strict monotonicity would then force a constant preactivation, contradicting the tails. All moments in the formula are continuous along the `L^2` path. The positive variance and positive error consequently have positive minima on each compact time interval. Uniform second-moment convergence transfers a smaller lower bound to the finite empirical errors. This proves persistent nonaffinity, not merely nonaffinity at initialization.

**§12.4, lines 1699–1736; (12.13).** At a reached positive feature time, the pointwise readout lower bound and strict positivity of the gate make the top backward field nonzero. In approximating scalar programs the corresponding Gaussian innovation variances then have a positive lower bound, while the response shifts remain bounded. Closed-half-line passage therefore gives unbounded support of the next backward query. Its strictly positive gate makes the middle backward field nonzero. Repeating this argument yields the bottom backward nondegeneracy. The reasoning is sequential from top to bottom and does not presuppose the lower-layer conclusion.

The adjoint identities (12.13) have the correct kernel terms. Positive pairings exclude zero middle and top preactivation velocities, while the first preactivation velocity is its nonzero backward field. Strictly positive gates cannot annihilate these nonzero `L^2` fields. Finally, the physical clock multiplier is strictly positive at every finite physical time. Thus every hidden feature velocity is nonzero at every positive finite physical time, while the zero initial hidden velocities and their second-order onset agree with the earlier expansions.

## Findings and required action

**Fatal gaps:** none.

**Repairable mathematical proof omissions:** none.

**Counterexamples to the stated theorem or its supporting mathematical assertions:** none found.

**Presentation only:** equation (6.4), line 838, contains `E_j,quad` where a LaTeX `\quad` separator was intended. The plain `sup` in line 1163 and `min` in line 1243 can likewise be typeset as mathematical operators. These are formatting defects with unambiguous mathematical readings; correcting the markup discharges them. They require no change to an estimate, hypothesis, quantifier, or proof argument and do not qualify the PASS verdict.

No nonclassical outside lemma is needed to fill a missing step. In particular, the key specialized obligations—adaptive Gaussian reuse, singular queries, response bounds, cap removal, uniqueness against arbitrary stated competitors, the raw-GD coordinate defect and stopped clock, and within-step velocity control—are discharged inside the submitted document.
