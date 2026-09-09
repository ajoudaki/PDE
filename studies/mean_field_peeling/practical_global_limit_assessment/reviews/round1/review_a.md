# Isolated adversarial audit

Input: `/home/amir/Codes/PDE/studies/mean_field_peeling/practical_global_limit_assessment/ASSESSMENT.md`, read in full. No other document, chat, skill, agent assessment, or external source was consulted. Cited existing results were treated only as attributed premises.

## Verdict

The substantive new initialization calculations, finite-dimensional energy argument, and depth comparisons pass. One explicit parameter qualification is needed to make the relative-nonlinearity paragraph valid as a standalone statement: its claimed denominator bound is not valid for unrestricted `e`. State `0 <= e <= 1` in that paragraph, as is evidently intended by the surrounding discussion of `e=1`, together with the normalized-shape bounds `||psi||_infinity <= 1` and `||psi'||_infinity <= 1`. Alternatively, condition the denominator bound on `a >= |e|`, and use `a >= 2|e|` for its direct deduction of the displayed relative bound.

No claimed initialization-to-training or energy-to-population implication was found. The document consistently labels the population continuation, physical-tail estimate, trained-depth limit, and fixed moderate activation theorem as unresolved.

## Exact necessary correction

The paragraph beginning “An absolute positive nonaffinity margin” currently claims

    E phi(Z)^2 >= (a-e)^2 sigma^2

and attributes it to projection and Gaussian integration by parts. Projection actually gives

    E phi(Z)^2 >= sigma^2 (a + e E psi'(Z))^2.

With `||psi'||_infinity <= 1`, this implies the stated lower bound when `a >= e >= 0`, but squaring a negative lower estimate `a-e` is not permissible. The document does not explicitly specify an upper bound on `e` in this paragraph. For example, with `psi(z)=sin(z)`, `a=2`, `e=10`, and `sigma=2`, the actual denominator is

    20 + 160 exp(-2) + 50(1-exp(-8)) < 93,

whereas the asserted lower bound is `256`. This example has bounded shape and derivative, each of norm one.

A minimal replacement is:

> For `0 <= e <= 1`, `a >= 2`, centered Gaussian `Z` of standard deviation `sigma >= 1`, and normalized shape bounds `||psi||_infinity <= 1` and `||psi'||_infinity <= 1`, the numerator is at most `e^2`, while the denominator is at least `(a-e)^2 sigma^2`, by projection onto `Z` and Gaussian integration by parts. The relative regression fraction is therefore at most `4e^2/a^2`.

If the original source's term “normalized shape class” already includes the two shape bounds, they need not be repeated; the amplitude qualification is still needed somewhere in this document. The final relative-fraction upper bound alone can actually be extended to arbitrary nonnegative `e`: for `a >= 2e` use projection, and for `a < 2e` use the trivial fraction bound `1 <= 4e^2/a^2`. That observation does not repair the unrestricted denominator claim.

## Checks of the new elementary arguments

### Gain and regression observations

For fixed positive shape constant, the two displayed gain requirements scale respectively as `delta^(-2)` and `delta^(-8/5)`, so their maximum is of order `delta^(-2)` as asserted. The first requirement gives reciprocal gains approximately `5.20806e-17` and `5.20833e-21` at the two stated separations, consistent with both numerical inequalities.

The affine-regression residual identity is exact because adding an affine function does not change distance to the affine subspace, and scalar multiplication scales the squared distance by `e^2`. Three distinct points on one sphere are affinely independent: affine dependence of three distinct points would put them on a line, and a line intersects a sphere in at most two points.

### Energy and continuation boundaries

For an existing raw-metric gradient flow of a nonnegative differentiable loss, integration of `dE/dt=-||dot Theta||_raw^2` gives the displayed energy bound. Cauchy–Schwarz gives the displacement bound. At each fixed finite width, a finite-dimensional raw ball is compact; smooth local dynamics then exclude finite-time escape and give continuation. This reasoning supplies no compactness or local Lipschitz assertion for the infinite-dimensional population space, and the document explicitly says so.

The identity for a capped direction is algebraically correct. Uniform vanishing of `||G-G_R||` on the relevant stopped solutions would give approximate energy control by Young's inequality. A tail of size `exp(-cR^2)` dominates a reference stability loss `exp(CR)` for every fixed pair of constants. Whether the proposed incoming-field estimate actually supplies all gradient-error and bridge estimates depends on definitions and results not reproduced here; the document presents this as an unproved sufficient proof route, not a proved theorem. There is no elementary contradiction in that conditional route.

The scalar ascent example satisfies all three displayed equations: the first two derivatives are `sec(s) tan(s)`, and the third is `sec(s)^2`. Its finite-time blow-up is real and does not contradict squared-loss dissipation.

### True residual composition

For nonnegative `beta`, submultiplicativity gives the stated Jacobian product bound. The scalar formula follows from `(sinh h)'=beta sinh h`. Its derivative is `exp(beta)` at zero and tends to one at either infinity; for `beta>0` it is nonaffine. The bounded Lipschitz field `beta tanh` gives ordinary Euler convergence. The text correctly confines this example to forward composition.

### Gaussian `1/L` normalized-geometry cancellation

For centered jointly Gaussian preactivations of common variance `q`, Gaussian integration by parts gives `E[Z_i psi(Z_j)]=Q_ij a(q)`. Expanding the next preactivation second-moment kernel after fresh centered Gaussian mixing therefore yields exactly

    Q^+ = (1+2e a(q))Q + e^2 B,
    q^+ = (1+2e a(q))q + e^2 b,
    C^+-C = e^2(B-bC)/q^+.

The use of this second moment as the covariance of the next centered Gaussian preactivation is consistent with the fresh mixing architecture; it should not be read as the centered covariance of the generally noncentered activated features themselves.

For `0 <= e <= 1/2` and `||psi'||_infinity <= 1`, projection onto the unit Gaussian gives

    q^+ >= q(1+e a(q))^2 >= (1-e)^2 q.

The triangle inequality in `L2` gives the stated upper variance recursion. With `e=beta/L`, `beta>=0`, and `L>=2beta`, the inequality `log(1-e)>=-2e` gives `q_l>=exp(-4beta)` for every `l<=L`; the upper bound follows by summing the square-root recursion. The document's stated condition `e<=1/2` already contains the required eventual restriction on `L`. Explicitly declaring `beta>=0` would remove a minor implicit sign convention.

Because `|B_ij|<=||psi||_infinity^2`, `b<=||psi||_infinity^2`, and `|C_ij|<=1`, each normalized increment is bounded by `2e^2||psi||_infinity^2 exp(4beta)`. Summing `L` increments proves precisely the displayed `O(1/L)` bound, with its stated constant. The affine-offset recursion also checks exactly: each fresh centered mixing step adds `(beta b/L)^2 11^T`, giving the displayed final covariance after `L` steps.

### Variance-calibrated `1/sqrt(L)` candidate

Gaussian integration by parts gives `a0=E[1/(1+G^2)]`. Thus `r` is odd, globally Lipschitz, has at most linear growth, and is orthogonal to `G`. Its positive-order derivatives are bounded. Its squared norm `v` is strictly positive because `atan` is not linear. The text correctly acknowledges that `r` itself is unbounded.

The variance normalization is exact. Joint Gaussian integration by parts kills both cross terms at every correlation, including the endpoints, and gives exactly

    c^+ = (c+e_L^2 R(c))/(1+e_L^2 v).

For interior correlations, Gaussian covariance differentiation gives `R'(c)=E[r'(G_1)r'(G_2)]`, bounded in absolute value by `||r'||_infinity^2`. Linear growth and Lipschitz continuity of `r` justify continuous extension to the endpoints through a coupled Gaussian representation. This supplies a globally Lipschitz `R` on `[-1,1]`.

Writing `e_L^2=beta^2/L`, the exact increment is

    (beta^2/L)(R(c)-vc)/(1+beta^2 v/L).

Since `|R(c)|<=v`, its difference from the displayed Euler step is uniformly `O(L^(-2))`. Standard discrete error propagation for the Lipschitz vector field gives convergence uniformly in depth, with error `O(1/L)` under the usual piecewise constant or linear interpolation. Endpoints satisfy `R(1)=v` and `R(-1)=-v`; the ODE preserves the correlation interval, as do all discrete feature correlations.

Oddness and orthogonality give `R(0)=0` and `R'(0)=(E r'(G))^2=0`, while `R(1)=v>0`. Consequently `R`, and the generator `beta^2(R(c)-vc)` for `beta != 0`, are nonaffine. Even the positive-depth solution map is nonaffine: it fixes both endpoints, while its derivative at zero is `exp(-s beta^2 v)<1` for positive depth and nonzero `beta`. Choosing `beta` with `beta^2 v` of order one is consistent with every layer tending to identity as `L` grows.

The document explicitly restricts these statements to initialized covariance geometry. It does not use them to assert a trained global flow or a joint width-depth limit.

### Training normalization and literature

Under the stated uniform sensitivity bounds, branch parameter derivatives scaled by `1/L` contribute at most `O(L^-2)` per independently parameterized branch to the kernel; summing `L` branches gives `O(L^-1)`. A metric or learning-rate normalization is therefore relevant to a nonvanishing branch-training limit. The document appropriately treats it as an additional model choice.

No independent certification of the cited manuscripts or the literature theorem is supplied by this audit. Their attributed statements are not used here to close any population-existence or trained-depth gap.
