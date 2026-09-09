# Independent adversarial audit

**Verdict: PASS within the expressly stated initialization-only scope.**

I read `/home/amir/Codes/PDE/studies/mean_field_peeling/CALIBRATED_NEAR_IDENTITY_INITIALIZATION.md` in full, from its title through the last sentence of Section 6. The SHA256 of the audited input is:

`f55df0156da98d67a655b27280a005d148df0bb206b783a454dfed379bc99211`

The input was not edited. No other files, skills, reviewers, subagents, web sources, or numerical experiments were used. This report is based on direct symbolic checking of the supplied note.

## Checks

1. **Calibration and Gaussian normalization.** The chosen constant cancels the degree-one Gaussian component: `2 c exp(-2) = exp(-1/2)`. The variance is positive because the bounded continuous shape is nonzero. Oddness and the cancellation give the stated mean, orthogonality, and unit normalization. Consequently the population variance remains exactly one at every layer for each fixed activation parameter.

2. **Ordinary finite-depth network identification.** For fixed finite depth, the conditional Gaussian row law has exactly the preceding empirical uncentered Gram as covariance. Bounded preceding diagonals give uniform conditional fourth-moment bounds for next-layer feature products. Conditional Chebyshev and induction therefore establish concentration. Positive-square-root Gaussian coupling, the Lipschitz activation, and bounded second moments justify expectation continuity even at singular covariances. This argument establishes the claimed width-first limit for each finite depth; it does not require, and the note does not claim, an estimate uniform in depth.

3. **Correlation map and coefficient signs.** The mixed linear/nonlinear terms vanish for every Gaussian correlation, including both endpoints. Expansion of the exact sine kernel yields coefficient numerator `1 - 2^m + 4^(m-1) = (2^(m-1)-1)^2`. Its linear coefficient vanishes, its cubic coefficient is `3/(2N)`, and all retained coefficients are positive. Normalization at correlation one makes their sum one. The correlation contraction and separation preservation follow.

4. **Worst-case three-input geometry.** Each tensor test vector has unit norm, annihilates the other two cubic tensor features, and pairs with its own feature by `sqrt(1-C_ij^2) sqrt(1-C_ik^2)`, which is at least `delta(2-delta)`. Summing the three elementary Cauchy–Schwarz inequalities gives exactly the factor `1/3` in (7), including singular input Grams and all admissible signs. Positive semidefiniteness of the remaining tensor powers then gives (8). Iteration and the binomial inequality give both bounds in (9). No hidden dependence of the activation shape or total depth parameter on the separation parameter is introduced.

5. **Population depth limit and nonlinear witness.** The modified Euler step differs from the ordinary time step by a second-order amount. The smooth vector field has an invariant correlation interval, and the displayed error recursion gives convergence for fixed total depth. The limiting covariance remains positive semidefinite. For the equilateral triple, positivity of the scalar magnitude follows from its differential lower bound; the reciprocal-square differential inequality and the two covariance eigenvalues give (12). The resulting positive smallest eigenvalue cannot arise from scalar rescaling of the initially singular Gram.

6. **Near-identity estimates and local variance stability.** The weighted value bound, derivative bound, and second-derivative estimate follow directly from bounded shape derivatives and the scalar denominator. The variance cross term is `q a(q)` by Gaussian integration by parts. The derivative `a'(1)` has the stated negative sign and coefficient. Differentiability of the bounded-shape variance term supplies the stated expansion of `V_h'(1)`. Continuity then proves local attraction for sufficiently small positive `h`; no uniform attraction neighborhood or joint width/depth stability is inferred.

7. **Derivative moments and scope.** Gaussian integration by parts removes the linear derivative term, and the exponential product bound follows from the scalar second moment. It supplies neither an operator norm estimate for Jacobian products nor a trained-adjoint estimate. The note explicitly preserves this distinction. Its conclusions concern initialized population feature covariances and their sequential limits; all training, response-history, finite-width/growing-depth, and fitting claims are explicitly left open.

## Unresolved objections

None within the stated scope. In particular, I found no quantifier switch from finite-depth width limits to a joint limit, no use of trained fields as Gaussian, and no promotion of covariance or scalar gate estimates into neuronwise or trained backward-field bounds.
