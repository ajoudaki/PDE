# Independent adversarial mathematical review

**Verdict: PASS, restricted to the proved and explicitly conditional scopes asserted in the report.**

Input: `/tmp/proof-735e1a9531d4/REPORT.md`

Input SHA256: `cd62425a6d8ae0ca7351bb6e71b31cd0b4eb7266263e53e377f976bab261e037`

I found no substantive correctness or completeness objection to the finite-width existence statement, the initialization identification, the sharp joint-order initialization theorem, the ancillary initialized-law results, or the conditional continuation theorem with its stated additional hypotheses. This PASS does **not** certify the global canonical trained limit, any sufficient positive training threshold, any depth-independent sufficient training threshold, or any of the other claims explicitly left unresolved.

## Input isolation and reading coverage

The report was my sole mathematical input. I read all 643 lines, including all formulas, both parts, the introductory model and initialization lemma, and the final unresolved-scope discussion. The initial whole-file display had a truncation; I subsequently read the complete numbered ranges 1–220, 221–460, and 461–643, which supplied the omitted passage and ensured complete coverage. I read no skills, project files, notes, earlier versions or reviews, other agents' analyses, or websites. I performed no experiments and did not modify the report.

| Coverage | Audit result |
|---|---|
| Lines 1–18: activation, scope, summary scale | Consistent with the later proved theorem and its parameter range. |
| Lines 20–75: finite model, metric, GF/GD, initialization identification | Valid at separately fixed finite depth and fixed input dimension. |
| Lines 77–115: definitions and theorems (A), (B) | Both comparisons follow with universal constants and a strict admissible example in every dimension at least two. |
| Lines 117–169: scalar variance estimates | All inequalities, telescoping estimates, and constants checked. |
| Lines 171–221: Hermite foundations, correlation and endpoint identities | Complete for the functions and degenerate Gaussian pairs used here. |
| Lines 223–310: first-chaos retention and cubic injection | Valid, including singular starting Gram matrices. |
| Lines 312–397: composition curvature and strict upper example | Derivatives, example geometry, Rayleigh quotient, and final constants checked. |
| Lines 399–443: asymptotics, affine obstruction, scope limits | Correct in their stated initialized or affine scopes. |
| Lines 445–496: conditional state space and theorem | The extra assumptions are explicit and adequate for the implication proved. |
| Lines 498–533: capped gates and asymmetric comparison | Valid, including an infinite cap and clipping at the moved point. |
| Lines 535–581: depth propagation and common constant | The dependence is linear in the comparison threshold; the displayed constant has sufficient slack. |
| Lines 583–604: convergence, direction convergence, uniqueness, continuation | The variable-threshold argument closes for every fixed horizon under the assumptions. |
| Lines 606–630: failures of tail and differentiated-product implications | Both counterexamples are valid and correctly distinguished from reachability claims. |
| Lines 632–643: unresolved matters | Consistent with the proved scopes; no unresolved training theorem is silently claimed. |

## Checks of the initialization results

The inverse metric gives the stated first-layer factor (1/d), hidden-layer factor (1/n), and readout factor one. The prediction-kernel blocks follow with precisely those normalizations. The finite-dimensional field is smooth everywhere. Its loss identity controls displacement on every finite interval, makes increments approaching a finite endpoint Cauchy, and therefore excludes finite-time escape. The GD statement only asserts that each finite update is defined and needs no stability assumption.

The conditional Gaussian induction does not assume independence between layers after conditioning. At a layer with empirical diagonal bounded by (M), Gaussian fourth moments give conditional product variance at most (3M^2). The induction makes this event have probability tending to one for a fixed sufficiently large (M). Positive-square-root coupling establishes the required covariance-map continuity even at singular covariance matrices. All layer and entry unions are finite.

The square-matrix operator-norm estimate is adequate: a (1/4)-net can have at most (9^n) points; the bilinear net estimate has factor two; and the displayed Gaussian union-bound exponent is negative after including both nets. This is needed only for the square hidden matrices. Combining it with (E\|C(0)\|_n^2=n^{-2}) gives backward norms (O_{\mathbb P}(n^{-1})), so every hidden kernel block vanishes. No independence between the backward fields and forward features is needed for this last bound.

For scalar variance, the projection coefficient and Jensen lower bound give (q_+\ge q/4). The decrement inequality gives both reciprocal increments and the useful telescoping estimate

\[
\sum_{k<L}q_k^2\le \frac4\theta(1-q_L)\le\frac4\theta.
\]

The lower sum estimate is the integral of ((1+8\theta x)^{-2}), namely (L/(1+8\theta L)). The interpolation bound with coefficient five is valid in both cases \(\theta L\le4\) and \(\theta L\ge4\).

The Hermite completeness argument is not circular. Orthogonality is obtained first. The imaginary-argument generating series then converges in Gaussian (L^2) because its squared coefficient norms are summable; its pointwise sum identifies the limit. A function orthogonal to all polynomials consequently has a Gaussian-weighted integrable density with zero Fourier transform. The Gaussian convolution and approximate-identity argument supplied in the report proves that density is zero. The correlated-pair identity extends by (L^2) approximation and Cauchy–Schwarz without requiring a nonsingular joint density, so correlations (\pm1) are included.

The first two derivative coefficient identities have vanishing Gaussian boundary terms: the activation has at most linear growth and its first two derivatives are bounded. Parseval therefore supplies the finite first and second coefficient moments. Termwise derivatives inside the correlation interval, followed by dominated or monotone convergence, give actual one-sided derivatives and their continuity at one, not merely formal coefficient sums. Those endpoint properties also justify the subsequent finite-depth chain rules.

The first-chaos logarithmic loss is at most ((20/3)\theta^2q^2). Its sum is at most (80/3), uniformly over the full allowed depth and mixture range. The cubic Hermite coefficient has the stated sign and coefficient (-\sqrt{2/3}\,q^{3/2}). Jensen under the Gaussian measure weighted by (G^2) yields its squared lower bound (q^3/384).

The tensor witnesses in the cubic lift need not be symmetric tensors. They have norm one, annihilate the other two cubic tensors, and pair with the selected one by at least (\delta(2-\delta)). Summing the three scalar estimates proves (10). Positivity of every tensor-power Gram and the nonnegative Hermite coefficients then permits the matrix inequality and its iteration, even when the input Gram is singular.

For the upper bound, composition preserves the probability distribution on positive odd degrees. The estimate (d_k-1\le b_k/3) follows degree by degree from (n\ge3). The exact formula for composed second derivatives and the resulting curvature bound are valid. The planar example is strictly admissible throughout (0<\delta\le1/4), including the upper endpoint. Its test vector has squared norm at least three, and its degree-one quadratic form is identically zero. Direct differentiation gives the stated (E_n''); the bound (40n^2-16n+8\le54n(n-1)) holds for every integer (n\ge3). Taylor's remainder and positive-semidefiniteness give the two-sided bound on (E_n).

The final constants reproduce exactly:

\[
1152\cdot64=73728,\qquad 36\cdot80\cdot4=11520.
\]

Thus the constants in (A) are sufficient and independent of dimension, geometry, depth, and mixture in the stated parameter range. Omitting the scalar variance factor gives (B). The asymptotic reciprocal variance increment is (2\theta); the regression residual is (-q^{3/2}H_3/3+O_{L^2}(q^{5/2})). These give the stated constants (1/(12\theta\ell^3)) and (1/(6\ell^2)) at fixed positive mixture. The equilateral affine obstruction uses the exact zero feature sum and zero readout, and does not extend that obstruction to positive mixture.

## Checks of the conditional continuation theorem

The affine product space is complete in the raw increment norm. Hilbert–Schmidt increments control operator differences, and all rank-one directions are in the declared tangent space. The conditional hypotheses impose operator bounds on the actions; they do not need to impose Hilbert–Schmidt bounds on the fixed base actions. For fixed finite cap, the scalar gate is globally Lipschitz, which makes the induced (L^2) gates Lipschitz and the state field locally Lipschitz on bounded primal sets. The theorem additionally assumes reference existence on the entire observation interval.

The gate estimates preserve the needed curvature factor. In particular, after replacing the incoming field by the reference incoming field, the difference between two capped nonlinear terms at the same reference preactivation vanishes on the good event. The remaining moved-preactivation difference is controlled by the secant estimate for (g(z)=(1+z^2)^{-1}). On the bad event, bounding both nonlinear terms by the absolute reference incoming field is sufficient. This proves (II.7) without assuming that the moved point is unclipped or has a tail bound.

The forward discrepancy bound uses the sum of parameter differences, which absorbs the sum over layers without an extra layer factor. In the backward induction, the threshold multiplies only forward discrepancies; propagation of previous backward discrepancies has coefficient bounded by the action norm. The bound (II.10) and the linear threshold dependence in (II.11) therefore hold at every fixed depth. Substitution into the residual and rank-one differences gives powers and coefficients below the common (100(L+1)^2B^{4L+4}).

For the variable threshold, (u=d+Ae^{-cR}) guarantees that (M=c^{-1}\log(A/u)) is at most the smaller cap, while the stopping condition guarantees (M\ge1). The differential inequality becomes an Osgood inequality with modulus (u\log(eA/u)). Its solution bound actually controls (u), so choosing the smaller cap sufficiently large keeps the path below the stopping threshold for the whole fixed interval. This validates the stopping argument behind (II.12), regardless of the finite horizon or the positive value of (c).

The resulting exponential-in-cap state bound, followed by (M=R/2), makes the directions uniformly Cauchy as well. Completeness and the integral equations give a (C^1) limit. The true gate is continuous in the (L^2\times L^2\to L^2) topology by a bounded multiplier argument against a fixed square-integrable incoming field; differentiability of this Nemytskii map is not assumed. Applying (II.11) directly against a finite-cap reference identifies the limit direction with the true field.

The comparison remains valid for any bounded-primal strong true-gate competitor because only the reference needs the weighted tail estimate. Enlarging the primal bound changes constants but leaves positive exponential decay in the cap. The same argument allows an exponentially small initial discrepancy at a reached time, proving continuation uniqueness. Under consistent reference hypotheses on all finite horizons, overlap uniqueness gives the claimed global conditional solution.

Finally, the tail counterexample has a permissible rank-one Hilbert–Schmidt increment, sends the selected feature to the constant one, and gives the exact squared tail norm (3/(\sqrt2u)). The differentiated-product example has square-integrable factors and a nonsquare-integrable product at a preactivation where curvature is nonzero. Both demonstrate genuine logical gaps between raw second-moment bounds and the additional control required; neither is incorrectly represented as a reachable trained law.

## Objections and limits of certification

**Substantive correctness/completeness objections: none found in the asserted scopes.** Standard background results invoked in these scopes have the needed hypotheses: finite-dimensional local ODE existence applies to the smooth finite field; covariance square roots are used only for finite positive semidefinite matrices; Fourier uniqueness is supplied by an explicit integrable-density argument; and the limit construction takes place in a complete affine Hilbert product space with continuous directions.

The report expressly leaves the canonical reference bounds, finite-width trained approximations and velocity observations, global trained-law nonaffinity, and sufficient training thresholds unresolved. Their absence is a limitation of what this report establishes, not a missing premise hidden inside either theorem certified above.
