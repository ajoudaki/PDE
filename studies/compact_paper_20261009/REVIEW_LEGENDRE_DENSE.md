# Scoped cross-review: dense fitting, Legendre, and dense lower transfer

## Scope and verdict

Read completely: `paper/compact.tex`, `paper/compact_fitting.tex`, and `paper/compact_legendre.tex`. Also read the source interfaces `cp:source`, `cp:finite-time`, and `cp:carrier` in `paper/compact_foundations.tex`, including the finite-time/carrier corollary proof to check their precise range and normalization. No author notes, other review reports, study history, or original proof were used in this review.

No theorem-blocking mathematical defect was found in the assigned fitting, Legendre, lower-transfer, or assembly arguments. This verdict is conditional on the source interfaces being established: the long probabilistic source proof was outside this review's assigned scope. The checks below rederived the identities and coefficient dependencies, rather than treating agreement with the original appendix as evidence.

## Minor actionable clarification

At `paper/compact_legendre.tex:12`, explicitly declare the supplied order to be an integer `q >= 1`. The projection lemma contains `1/(q(q+1))`, and the comparison uses `log q`; the phrase “every finite order” in `cp:legendre-fit` should mean every positive finite order. The prescribed headline order already satisfies this, so this is a domain clarification rather than a theorem correction.

## Verified points

1. **Dense normalization and fitting.** In mobility coordinates `(W^(1)/sqrt(n), W^(2), ..., W^(L), w/sqrt(n))`, the displayed flow is exactly minus the gradient of the mean squared residual. Its readout block gives `-d(rho^2)/dt >= lambda rho^2` when the normalized top Gram is at least `lambda/4`. The path-length bound, hidden displacement recursion, Gram singular-value margin, and uniform endpoint bound have the stated normalization. The initialization proof covers singular intermediate covariance matrices and fixed-dimensional sphere queries; cavity initial conditions are transferred uniformly from a maximal-coordinate bound, not an unjustified union of merely asymptotic probabilities.

2. **Signed perturbation.** Direct subtraction gives the negative term `-2 ||r-r'||_m^2`; the remaining two Taylor terms have coefficient `K(rho' + 3 rho)`. Regularization of the parameter norm handles zero discrepancy. This avoids an ambient Lipschitz exponential in physical time.

3. **Legendre moments and defect.** Differentiating `P_j(2 xi/A - 1)` on a growing interval gives precisely the stored moment coefficients `j` and `2i+1`. The initialized forward prefix is constant and the backward prefix zero. Differentiating the projected bilinear pairing gives the full endpoint product minus the product of endpoint errors, with the sign and factor `2 rho/(mn)` in the reconstructed-matrix defect. The endpoint kernel, weighted tail bound, and growing-interval error identity are consistent with the unnormalized interval measure.

4. **All-order fitting.** The apparently order-growing backward endpoint bound is multiplied by the forward integrated projection tail; `(q+1)/q <= 2` removes the order from the energy bootstrap. The sharper endpoint kernel bound then gives the stated pointwise defect. Applying the output Jacobian to that defect costs at most `lambda rho/4`, preserving residual decay at rate `lambda/4`. The weighted gradient-energy argument gives finite path length, while integrable residuals and bounded moments give convergent stored state. No division by a residual is present in the actual autonomous equations.

5. **Comparison and absorption.** The signed comparison uses only the actual dense training carrier bound, with coefficient additive in its maximum. The backward comparison history uses the closure's normalized residual but the dense response; this distinction is necessary for the derivative estimate and is correctly retained. Freezing after `2 log(q)/kappa` cancels the inverse activity-clock speed using the remaining-clock bound. The integrated defect is a product of two projection tails; its closure-discrepancy term is absorbed once `q >= q_abs`. This cutoff is subpolynomial at fixed problem parameters and is eventually below the prescribed order.

6. **Exact logarithmic/exponential rate.** With `X=beta^L`, the ledger gives an exponent at most `1 + sqrt(log(en))`, because `X^36 (Y/lambda)^2 <= 1`. The forward error is at most `C Y (1+lambda^(-1))^6 exp(sqrt(log(en))) sqrt(log(en) log(eq))/q^2`. Squaring the prescribed order cancels exactly this exponential, and `log(eq)=O(log(en))` gives `C Y/(sqrt(n) log(en)^3)`. No hidden sample/gap factor enters the exponential. The moving-state count includes the first matrix and readout only after taking the fixed-problem eventual width threshold; the dense initialized mixers remain separately charged.

7. **Dense lower bound.** The innovation lemma's squared-area identity and two eigenvalue lower bounds give a deterministic training index with positive scalar variance. Conditional on preceding layers, the two last-layer groups are independent. Their centered third moments are uniformly bounded on bounded covariance sets, so the conditional characteristic-function argument yields a Gaussian law of variance `8 v_*/m^2`. The preceding layers contribute an arbitrary conditional mean shift; the Gaussian maximal-interval argument correctly controls it instead of assuming it disappears. The degree-N Chebyshev truncation and endpoint Markov bound have the stated physical-time factor. Taking `N` proportional to `log n` on the `1/(lambda sqrt(log n))` interval yields the claimed `Y sqrt(gamma)/(sqrt(n) log(en)^(5/2))` fluctuation at a positive training time.

8. **Headline assembly.** The witness lies at a training input, so both query domains inherit the same lower bound. A union bound, not an independence assumption between approximation and variability, is used. The strict confidence margin permits an eventual finite-width statement. Letting the auxiliary confidence budget tend to zero proves convergence in probability. The lower bound is explicitly not an endpoint lower bound.

## Limitations

This was a mathematical source review, not numerical experimentation or a second full audit of the probabilistic source engine. No TeX was changed by this review. The sole requested clarification does not affect the current positive-order headline construction.

## Resolution addendum

Verified the local revision at `paper/compact_legendre.tex:11`: “Fix an integer order q >= 1.” This explicitly supplies the positive-integer domain used by the projection and comparison formulas and resolves the sole requested clarification. No outstanding finding remains within this review's stated scope. This was a local resolution check, not an additional full review.
