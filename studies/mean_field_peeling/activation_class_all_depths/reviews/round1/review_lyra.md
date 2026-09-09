# Independent adversarial review

## Verdict

**UNVERIFIED AS WRITTEN, for an explicitly repairable notation defect in the quantitative source proof.** I found no counterexample and no unresolved substantive mathematical objection after independently reconstructing that calculation. The distinction matters: the supplied manuscript literally contains undefined expressions `exp(S.1)` and `sqrt(S.2)` in the argument supplying its crucial source moments. I cannot give the requested unconditional PASS to those expressions as written. The replacements and a complete validating calculation are below. A separate `o(N.1)` also needs correction.

Conditional on those explicitly specified editorial repairs, my audit validates the theorem and the appendix claims. I did not find another mathematical gap requiring an additional hypothesis or a change in a stated constant.

## Identity and scope

- File reviewed: `/tmp/hidden_depth_review_20260908/manuscript.md`.
- SHA256: `e61789c67fc6ea5ee918c50b82c7d5a233c0991e7222d32a003ca722f837606a`.
- Size: 2,864 lines; 22,013 words; 178,199 bytes.
- I read the entire file in order, including every section of Parts M, F, S, G, V, N and A, and then audited the dependencies and vulnerable calculations.
- I used no project files, other manuscripts, author notes, other reviews, chat mathematical context, or skill files. I neither communicated with other agents nor spawned any.
- No specialized external theorem is a premise of the supplied proof. I inspected its internal Gaussian conditioning, singular-query regularization, common-action construction, source estimates, and algorithm bridge. No external primary text was needed to discharge a specialized dependency.

## Required repairs

### 1. Undefined constants in S.3–S.4

Locations: line 945; lines 977–979; line 989; lines 998–999.

The manuscript writes `44+4/sqrt(S.2)`, `exp(S.1)`, and `sqrt(S.2)`. Here `(S.1)` and `(S.2)` are equation labels, not real numbers. The intended replacements are determined by the calculations:

- Replace every `exp(S.1)` in these lines by `exp(1)`.
- Replace every `sqrt(S.2)` in these lines by `sqrt(2)`.

This is not a proposed change to the perturbation parameter `e`. Writing `exp(1)` avoids confusing Euler's constant with that parameter.

I reconstructed the argument to check that the repaired expressions prove exactly the required quantitative bounds. If `||Z||_p <= M sqrt(p)` for every `p >= 2`, then, writing `e_E = exp(1)`,

\[
 E\exp\!\left(\frac{Z^2}{4e_E M^2}\right)
 \le 1+\sum_{k\ge1}
       \frac{M^{2k}(2k)^k}{(4e_E M^2)^k k!}
 \le 1+\sum_{k\ge1}2^{-k}=2.
\]

The last inequality uses `k! >= (k/e_E)^k`. Young's inequality gives even the stronger estimate

\[
 E e^{u|Z|}\le 2e^{e_E M^2u^2},
\]

so the manuscript's intended weaker coefficient `2 exp(1)` is valid. For

\[
 Z_k=\sum_{r<k}h_r K_\ell\max_i|q_{r,i}|,
 \qquad \|Z_k\|_p\le S W_\ell\sqrt p,
\]

its stated estimates follow:

\[
 E E_k\le 2\exp(4\alpha bS+2e_E\alpha^2S^2W_\ell^2)<4,
\]

\[
 \|E_k\|_2
 \le\sqrt2\exp(4\alpha bS+4e_E\alpha^2S^2W_\ell^2).
\]

Under `alpha S b <= 10^-9` and `alpha S W_l <= 10^-6`, Cauchy–Schwarz bounds the reverse response row by

\[
 \sqrt2(\sqrt2 W_\ell+4b)
 \exp(4\alpha bS+4e_E\alpha^2S^2W_\ell^2)
 <512(n_\ell+b),
\]

because `W_l = 60(n_l+b)`. Thus 512 remains valid, with substantial slack. The forward response constant 16 follows from `4 alpha h_j E E_k <= 16 alpha h_j`.

Similarly the S.3 forward moment calculation gives coefficients 42 on `alpha S Q_l` and `44+4/sqrt(p) <= 44+4/sqrt(2) < 50` on `alpha S b/K_l`. This validates its constant 50 after the same replacement.

No later constant or activation recipe needs changing.

### 2. Undefined asymptotic notation in N.4

Location: line 2262, the first paragraph of N.4.

Replace `o(N.1)` by `o_P(1)` (or explicitly “a quantity tending to zero in probability”). The accompanying proof is correct: there are finitely many coefficients, their differences tend to zero in probability, and the multiplying normalized vector norms are bounded in probability. Equation `(N.1)` is the inequality `0<e<a`; it cannot serve as the argument of this asymptotic notation.

## Adversarial tests of the theorem's quantifiers

**Singular input geometry.** The theorem does not need `Gamma` invertible. For three distinct unit inputs, the explicit two-variable reduction proves `Gamma + 11^T >= delta^2 I/4`. This covers antipodal pairs and rank-two configurations such as three unit vectors on a circle. The proof's one-sign case and mixed-sign case together exhaust coefficient vectors, including zeros. The use of three samples is material: I did not read this as an assertion for arbitrary sample count. In dimension one there is no admissible triple of three separated unit vectors, so that case is vacuous rather than a counterexample.

**Arbitrarily large fixed depth.** I checked the two essential mechanisms separately. The initialized Gram loses a summable amount, because integration by parts improves the expected derivative perturbation to `1/sigma_l`; replacing that estimate by the pointwise derivative bound would incorrectly give a depth-dependent loss. The training displacement shrinks exponentially with depth under the raw metric and the physical residual clock. All subsequent width limits fix depth first. The manuscript does not accidentally assert a joint width/depth limit.

**Very small nonlinearity.** The choice of `a` is independent of a fixed `e` in `(0,1]`. All stability estimates use upper bounds uniform in this interval. Strict positivity of the top backward Gram uses `phi''` not identically zero, which holds for every positive `e` and bounded nonconstant `psi`. There is no asserted lower bound on its smallest eigenvalue uniform as `e` decreases to zero. The nonaffinity bound includes the necessary factor `e^2`.

**Localized and oscillatory shapes.** No sign or monotonicity is imposed on `psi'` or `psi''`; only the full activation must remain increasing, which follows from `a>e`. A compactly supported perturbation makes the depth-uniform nonaffinity margin impossible already at initialization, exactly as A.3 states. Its finite-interval margin is nevertheless positive, and the potentially extremely large gain selected from that margin is allowed. Arbitrarily small local margins and distant support therefore do not contradict the quantified recipe. Oscillations do not invalidate either Gaussian integration by parts or the regression stability estimate.

**Uniform subclasses.** The common-gain conclusion fixes the function before taking the width limit. The stronger uniform-depth class uses a uniform Gaussian regression margin, not merely a common bounded `C^2` norm. The open ball around `(1/4) arctan` has this margin by the sup-norm stability estimate. Its members need not themselves have limits at infinity. The final disclaimer correctly excludes uniform width convergence over the function class and an `e`-independent positive margin.

## Detailed proof audit

### Model and normalization: Part M

The finite raw metric gives all three update factors in M.10. The first-coordinate change `w=sqrt(d) W^1` is an isometry of that block. Normalizing only the hidden fields gives `f_i=a^L F_i` while leaving the readout and raw metric unchanged, so every gradient block acquires exactly `a^L`. The physical raw backward field scaling and all raw kernel block powers in M.14/V.34 agree. The gradient-flow energy argument gives global finite-dimensional existence. The GD convention describes an actual raw Euler scheme with recomputed hidden fields; later comparisons retain its preceding-node direction.

### Foundations: Part F

I checked the Gaussian net bound, its operator-moment extension, and the conditional Gaussian projection formula. The induction on an adaptive transcript conditions only the queried residual matrix factor at a step; it does not assume that an adaptive query was independent of that matrix. The minimum-Frobenius-norm solution satisfies both forward and transpose constraints. The removed finite-rank Gaussian projection has normalized mean-square size `rank/n`.

The source-response identity is derived by cancellation of the regression correction using Gaussian integration by parts. It preserves opposite-orientation dependence in response terms; independence is asserted for primitive source groups, not matrix answers. The singular-query argument adds independent noise separately at every call, obtains positive limiting Schur complements, and removes the noise through bounded action estimates and continuity of finite covariance square roots. It does not use continuity of pseudoinverses at rank loss.

The countable generated language, density argument, norm inequality and adjunction identity yield common bounded actions with their actual adjoints. Arbitrary bounded substitute actions are not used. Only learned increments are Hilbert–Schmidt, matching the finite Frobenius metric. The multiplier-continuity and curve-chain-rule proofs use tails rather than an invalid Frechet derivative of the full `L^2` activation map. The scalar prediction's Frechet derivative is justified by the weighted remainder argument F.41; its weight is fixed at the expansion point. The feature-energy derivative uses the same valid argument.

### Controlled source calculation: Part S

The local equations retain the full current transpose return. The independent primal estimates close before any source estimates are invoked. The local Gaussian/remainder elimination uses the actual coefficient arrays; its remainder includes the activation offset at the required scale `1/K_l`. The marginal `L^p` argument uses no random time maximum and no temporal independence.

With the editorial repair above, the derivative Volterra estimate, moment generating function bound and response-production constants are valid. The explicit box arithmetic is consistent:

\[
 \alpha_\ell S b_\ell
 \le24576(67108864/a)^L64^{-\ell}T^2/a.
\]

The sufficient gain makes this at most its controlled `L=2` bound; using `sup T^2/(1+T)^3=4/27` yields the stated tiny bound. The estimate `W_l <= 61 b_l` follows from `n_l <= b_l/2048`. Both production inequalities are strictly inside their next radii. The forward chronological construction uses only strictly past reverse rows, while the reverse sweep uses a current incoming row already constructed at the preceding upper stage. I found no unknown-current-row circularity.

### Uniform geometry and residual clock: Part G

The initialization projection identity holds for singular Gaussian tuples. The product loss satisfies

\[
 \prod_{\ell\le L}(1-d_\ell)\ge1-\sum_{\ell\ge1}d_\ell
 =1-\frac1{a-2}\ge\frac12,
\]

so its square gives the claimed uniform Gram floor. The independent displacement bound produces exactly G.10's raw preactivation error and G.11's Gram perturbation power. The possibly nonsymmetric capped hidden contribution is controlled in operator norm, not treated as a positive kernel.

The physical residual estimate gives total control time at most `6/(lambda a^L)=S/2`, preventing first exit. The capped population paths and moment estimates are therefore available before cap removal. Step-function approximation of measurable controls is in `L^1`; the proof does not sample arbitrary measurable controls at Euler nodes.

The regression stability bound G.21 follows from the global bound one on every optimal regression slope, including the zero-variance case. The local interval density lower bound gives `c_psi/sigma`. The gain arithmetic in G.25/A.11 dominates raw displacement simultaneously for every fixed depth. No lower variance bound for a trained preactivation is needed.

### Population/algorithm/observation bridge: Part V

The cap comparison introduces one factor `R` multiplying a forward-state difference. Solving the downward backward recursion does not produce `R^L`. Reference incoming-field tails alone give `exp(CR-cR^2)`, hence strong path and raw-direction convergence and uniqueness against any bounded-primal uncut competitor. Restart uses the same comparison; it does not assume arbitrary-state local Lipschitzness for the uncut field.

The finite primal event is established at a fixed coarse transcript before the Gaussian probe estimates. At a fixed cap, the actual random readout is compared to zero only by a vanishing normalized-norm initialization discrepancy. The actual GF and GD algorithms themselves retain their original random readout.

The Gaussian probe proof bounds signed expectations of named derivatives by physical perturbations, then selects signs to bound absolute expected response rows. It does not interchange absolute values with expectations. The current-row recursion retains all current returns. The subsequent pointwise derivative-row estimates supply the stronger bounds needed for appended velocity queries.

The ascending velocity construction differentiates only the relevant primary reverse-source slots; the newly appended forward primitive source is a distinct slot. Its derivative-valid truncation uses an integrable envelope and removes previous inner caps while a new outer cap remains fixed. This avoids deriving source-derivative convergence merely from `W2` convergence. True backward observations have their own descending truncation argument and are not silently identified with capped update fields.

The deterministic velocity comparison also contains one tail threshold factor, with all new factors multiplying forward differences. Fixed-cap finite algorithms are compared against fixed coarse Euler programs. The fine step `n^-2` enters through its vanishing defect, and no growing transcript is passed directly to F.1. For uncut algorithms the order width, training cap, velocity tail threshold is maintained. Compact strong `L^2` time images supply tail removal without an uncontrolled cap-dependent fourth-moment constant.

The grid interpolation bound V.38 establishes path-law `W2` convergence from joint node laws and integrated squared speed bounds; pointwise laws alone are not used to claim path convergence. Contractions then give every true raw kernel block, integrated speeds and finite probe observations. The comparison arguments support full-sequence convergence in probability jointly for GF and GD.

### Initial motion, Gaussian innovation and coefficient 18: Part N

The top forward Gaussian has full three-dimensional support even for singular input `Gamma`, because the preceding feature Gram is positive definite. If a linear combination of top backward fields vanished, the product identity would force a linear combination of `phi'` to vanish identically. Differentiating separately in each coordinate and using `phi''` not identically zero proves positive definiteness of `S_L`.

The descending reverse sources have covariance `S_(l+1)` and are independent of that layer's forward tuple. Conditioning therefore gives the positive covariance lower bound even at a singular first-layer tuple. This proves every hidden raw block and every bottom sample direction is nonzero. The bottom metric factor `d` is accounted for.

For every upper sample, the added forward query has a regression remainder whose variance is the distance of its true input from the span of the three existing forward inputs. The regression correctly has no intercept because the source covariance uses the uncentered input Gram. At layer two, independent reverse variation makes that distance positive. At each later layer, the preceding primitive forward innovation remains independent of the current forward tuple and the separate reverse source group. Conditional variance then propagates a positive innovation. Its contribution cannot cancel the local backward combination. The proof makes no independence assumption between different samples' new innovations.

The coherent clipping program in N.4 uses the same clipped backward fields as reverse query inputs and as block contributions. Its source derivative is bounded independently of all caps, allowing the claimed ascending coefficient recurrence to survive cap removal with only `C^2` regularity.

Finally `C'(0)=3H`, `b_i^l(t)/t -> 3 beta_i^l`, and the raw hidden acceleration is `9V`. The curve chain rule gives acceleration `9U` and `9T` for every preactivation and feature. Genuine adjunction yields `<H,T>=||V||_hidden^2`. The readout part of the directional kernel contributes `9 t^2 ||V||^2`, and the hidden-gradient part contributes another `9 t^2 ||V||^2`, giving exactly 18. No derivative of an ambient `L^2` Nemytskii map or higher activation regularity is needed.

### Uniform activation subclasses: Part A

The interval regression formula, function and input stability inequalities, common-gain prescription and layerwise strengthened bound A.12 all check. The compact-support upper bound demonstrates the claimed obstruction to a broad depth-uniform margin. For distinct tail limits, the limiting regression residual is `b^2(1-2/pi)>0`; continuity and a compact interval give a positive infimum over all scales at least one. The derivatives and norms of `(1/4) arctan` are correct, including `3 sqrt(3)/32` for the second derivative norm. The sup-norm perturbation argument gives the claimed entire open ball. The disjoint compactly supported `C^2` translates establish infinitely many independent directions.

## Resolution needed for an unconditional PASS

Make the exact notation replacements specified above and supply that corrected manuscript for hash-specific certification. No change to M.4, M.15–M.18, any quantifier, or any substantive mathematical hypothesis is indicated by this review. My non-PASS status is limited to certifying the literal supplied file, whose source-estimate formulas currently contain undefined quantities; it is not evidence of a counterexample or an additional mathematical obstruction.
