# Independent adversarial audit

**Verdict: PASS.** Every asserted mathematical result in the supplied report is justified under its explicit assumptions. I found no unresolved objection requiring repair. The report proves an obstruction to a depth-uniform initialized kernel lower bound. It expressly does not prove or disprove the weaker global trained-dynamics statement at every separately fixed finite depth.

**Reviewed file:** `/tmp/convex_offset_final_20260908/manuscript.md`

**Exact SHA256:** `a6dae64cd54b9ab34520d2b493b78cefbbd4c868b5c222552e169982aff9f668`

**Full-read and isolation confirmation:** I read the entire report, from its title through the final sentence, and checked the hash directly. This report was my only mathematical input. I did not read other reports, reviews, project notes, conversations, or skills; I did not consult or spawn another agent; and I performed no numerical experiments. No specialized external theorem is used as an unproved premise: the Gaussian covariance differentiation, endpoint extension, and random-matrix norm estimate are all proved in the report and checked below. No external source retrieval was needed.

## 1. Activation, scaling, and initialized Gaussian recursion

The explicit class is a convex combination of the affine function `1+z` with a bounded shape. The arguments concern that convex combination; they do not require the activation to be convex as a function of its argument. With `alpha=1-epsilon` and `m=1-2 epsilon`, the stated shape assumptions imply

\[
m\le\phi_\varepsilon'(z)=\alpha+\varepsilon\psi'(z)\le1,
\qquad |\phi_\varepsilon(z)|\le\alpha |z|+1.
\]

Thus the activation is globally Lipschitz and has at most linear growth, with no unspecified gain factor.

The first preactivation covariance is exactly `Gamma` under the given first-layer variance. Conditional on the preceding features, each row of an independent higher-layer Gaussian weight matrix is a centered Gaussian tuple whose covariance is the preceding empirical **uncentered** feature Gram. This justifies the covariance, rather than centered-feature-covariance, recursion. The affine offset must remain in that Gram, and the report retains it.

The induction invoking a law of large numbers is valid, including for singular limiting covariances. To spell out the integrability detail: on any event where the preceding empirical covariance has bounded diagonal, conditional Gaussian fourth moments and the displayed linear-growth bound uniformly bound the second moments of the products of two new features. Conditional sample-average fluctuations consequently have variance `O(1/n)` on that event. The preceding covariance converges in probability and is therefore tight; the complement of such events can be made arbitrarily unlikely. The conditional expectations converge by continuity of Gaussian laws together with the same moment bounds. One may equivalently couple via continuous positive-semidefinite matrix square roots. This gives the asserted empirical-Gram convergence in probability by induction. The first layer is an ordinary independent-row law of large numbers.

Equal marginal input variances propagate. The lower bound on each subsequent standard deviation follows from

\[
E\phi_\varepsilon(\sigma G)\ge m,
\qquad \|\phi_\varepsilon(\sigma G)\|_2\ge
|E\phi_\varepsilon(\sigma G)|.
\]

The upper recursion `sigma_next <= alpha sigma + 1` preserves `[0,1/epsilon]`. The initial value `sigma_1=1` also satisfies both bounds. Equation (4) is therefore valid for every layer. In particular the lower bound used later concerns the feature second moment, whose square root is `sigma_(L+1)`, and the indexing is consistent.

## 2. Strict derivative bound and Gaussian comparison

The expectation in (5) is continuous on the compact interval of positive standard deviations by bounded convergence. It is at least `m^2`. If it were equal to one at any point, the pointwise interval `[m,1]` would force `phi'=1` Gaussian-almost surely. The positive Gaussian density and continuity imply this everywhere, hence `psi'=1` everywhere, contradicting boundedness. Compactness therefore gives exactly the claimed `0<kappa<1`. The constant may depend on the fixed activation; no uniform bound away from one over the entire shape class is asserted or needed.

I checked the covariance-density identity directly. With `D=sigma^4-c^2`, both `partial_c p_c / p_c` and `partial_x partial_y p_c / p_c` are

\[
\frac cD+
\frac{(\sigma^4+c^2)xy-\sigma^2c(x^2+y^2)}{D^2}.
\]

On every compact subinterval of nonsingular covariances the density and its relevant derivatives have uniform Gaussian decay times polynomial factors. The activation has linear growth and bounded first derivative, so differentiation under the integral and both integrations by parts are legitimate, with vanishing boundary terms. They yield

\[
F'(c)=E_c[\phi'(X)\phi'(Y)]\le
\sqrt{E\phi'(X)^2E\phi'(Y)^2}
=E\phi'(\sigma G)^2\le\kappa^2.
\]

The coupling given in the report has the required covariance and converges in `L^2` at each endpoint. Lipschitzness gives `L^2` convergence of its activated variables, and Cauchy--Schwarz gives continuity of their product expectations. Integrating to the upper endpoint and extending also to the lower endpoint is therefore justified. The identity

\[
E[(\phi(X)-\phi(Y))^2]=2(F(\sigma^2)-F(c)),
\qquad E[(X-Y)^2]=2(\sigma^2-c)
\]

then gives (6) with the correct constant and sign. No unstated restriction to nonnegative covariance is present.

## 3. Depth contraction and conditioning

At layer one the preactivation difference has second moment `2(1-Gamma_ij)`. At each subsequent layer its second moment equals the preceding feature difference second moment by the exact uncentered covariance recursion. Applying (6) at every layer gives (7), with exponent `2L` as written.

For distinct indices the coefficient vector `(e_i-e_j)/sqrt(2)` has unit norm and its Rayleigh quotient in `Q_L` is exactly `Delta_(L,ij)/2`. Thus (8) follows even when the Gram is singular. The argument does not require strict angular separation and remains valid for every admissible input triple.

Every activated marginal has mean at least `m`. Consequently testing `Q_L` against `1/sqrt(3)` times the all-ones vector and using the second-moment lower bound by squared mean gives `lambda_max(Q_L)>=3m^2`. In particular the normalized conditioning conclusion is stronger than a common shrinking scalar: explicitly,

\[
0\le\frac{\lambda_{\min}(Q_L)}{\lambda_{\max}(Q_L)}
\le\frac{1-\Gamma_{ij}}{3m^2}\kappa^{2L}.
\]

This is an exponential upper bound on the smallest-to-largest eigenvalue ratio. It does not assert an asymptotic equality or a positive lower bound on the smallest eigenvalue at fixed depth.

For the concrete shape `psi=arctan/4`, the stated bounds are correct: the supremum norm is `pi/8`, the derivative supremum is `1/4`, and the maximum magnitude of the second derivative is `3 sqrt(3)/32`, attained in magnitude at `|z|=1/sqrt(3)`. The resulting activation has derivative in `[3/4,13/16]`. Its global Lipschitz constant `13/16`, together with the same Gaussian second-moment recursion, proves (10) without the covariance-differentiation result.

## 4. Raw metric and the actual finite initialized kernel

For the predictor `f_i=C^T h_i^L/n`, the Euclidean readout derivative is `h_i^L/n`. Inverting its metric coefficient `1/n` gives the metric gradient `h_i^L`; pairing these gradients in that metric yields `h_i^T h_j/n`, as claimed.

With multiplication by `phi'(z)` understood componentwise, the backward fields are the usual chain-rule fields before the final predictor factor `1/n`. The Euclidean layer derivative is `b_i h_i^{previous,T}/n`. For higher layers the metric is the Frobenius metric, so the derivative pairing is

\[
\frac{(b_i^Tb_j)(h_i^Th_j)}{n^2}.
\]

For the first layer metric inversion supplies `n/d`, giving

\[
\frac nd\frac{(b_i^Tb_j)(x_i^Tx_j)}{n^2}
=\Gamma_{ij}\frac{b_i^Tb_j}{n}.
\]

These are precisely all the blocks in (12). No extra factor of `n` or `d` is missing.

The readout variance assumption gives `E||C||_n^2=n^{-2}` and hence `||C||_n=O_P(n^{-1})`. The matrix norm estimate is also correct. A maximal separated set gives a `1/4`-net with at most `9^n` points by the stated volume comparison. Approximating both arguments in the bilinear characterization of the operator norm gives the factor two. Every fixed bilinear form has Gaussian variance `1/n`; the threshold five tail is at most `2 exp(-25n/2)`. The union bound is therefore exactly the bound written in the report, and it tends to zero since `2 log 9 < 100/8`.

For any fixed finite depth a finite union controls all square weight matrices. The backward estimate then follows pathwise on this event from `|phi'|<=1`; it requires no false independence assumption between weights and backward fields. The first-layer rectangular matrix is not needed in the backward product. The forward Gram convergence gives `||h_i^ell||_n=O_P(1)`. Each hidden block is consequently `O_P(n^{-2})`, while the readout block converges to `Q_L`. Thus the actual finite random initialized **total** kernel converges to `Q_L` in probability, not merely the readout-only kernel of an artificially zeroed finite network.

The population statement `C=0` is consistent with this limiting initialization. It is not incorrectly imposed on the finite random readout. The proof explicitly takes width to infinity at separately fixed depth; it does not establish a joint limit with depth increasing with width.

## 5. Scope and final assessment

For every fixed allowed `epsilon` in `(0,1/2)` and every fixed allowed shape, the limiting initialized raw kernel cannot have a positive lower spectral bound independent of depth. A proof requiring such a bound cannot transfer unchanged to this normalized activation family. Changing the per-layer activation by a gain normalization changes both the forward covariance recursion and the backward fields under the fixed initialization and metric.

The report makes no unsupported inference from this obstruction to failure of global training at each finite depth. It does not establish positivity at every fixed depth either; its remark that a kernel *can* be positive at each finite depth while tending to degeneracy with depth is a valid logical explanation of the quantifier distinction. Its explicit unresolved obligations about all-time separation, incoming tails, and a fixed mixing threshold for trained three-input dynamics are not claimed results.

The trained-limit theorem is referred to as a target rather than specified and proved as a theorem in this standalone report. Accordingly this PASS certifies the actual initialization and conditioning results and their stated limited consequences. It does not certify a global trained-limit theorem. There is no required mathematical repair to the supplied report.
