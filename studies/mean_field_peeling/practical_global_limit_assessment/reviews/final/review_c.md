# Isolated adversarial audit of the practical global-limit assessment

**Verdict: PASS.** I found no necessary mathematical correction to the new elementary derivations or to the assessment's stated claim levels. This verdict applies to the conditional Gaussian population calculations and strategic assessment actually presented. It expressly does **not** establish a new global trained theorem, a finite-width Gaussian recursion, a uniform trained nonlinearity result, or a joint width–depth training limit.

## Isolation and scope

I read all 153 lines of `/home/amir/Codes/PDE/studies/mean_field_peeling/practical_global_limit_assessment/reviews/final/ASSESSMENT.md`. I did not read another mathematical file, conversation, skill, review, source, or agent's work, and did not delegate. Existing cited results and descriptions of manuscripts/literature were treated as attributed premises rather than independently certified theorems. The input was not edited.

The checks below concern the algebra, elementary analytic arguments, assumptions, quantifiers, and the distinction between demonstrated initialization facts and open training statements.

## 1. Existing constants and relative nonlinearity

The displayed gain rule has the stated asymptotics when the shape and its positive constant `c_psi` are fixed. Since `T0 = 192/delta^2`, its first term is of order `delta^(-2)` and its second is of order `delta^(-8/5)`. The first therefore determines the asymptotic maximum as `delta` tends to zero. For `e=1`, the first requirement alone gives

- at `delta=0.1`, `1/a <= 1/(10^12 * 19201)`, approximately `5.2081e-17`;
- at `delta=0.001`, `1/a <= 1/(10^12 * 192000001)`, approximately `5.2083e-21`.

Both strict numerical upper bounds in the assessment are valid. Their interpretation as sufficient and potentially nonoptimal is appropriate. The earlier sufficient cutoff and its derivation remain attributed premises.

For `phi(z)=a(1+z)+e psi(z)`, subtracting an arbitrary affine function and changing its two coefficients proves the exact affine-regression identity for `e != 0`; the identity also holds trivially for `e=0`.

Write `Z = sigma G` and `m = E psi'(Z)`. Gaussian integration by parts gives

`E[phi(Z) Z] = sigma^2 (a + e m)`.

Projection onto the one-dimensional span of `Z` then gives

`E phi(Z)^2 >= sigma^2 (a + e m)^2 >= sigma^2 (a-e)^2`.

The last inequality uses `|m| <= 1` and `a-e > 0`. The regression numerator is at most `e^2 E psi(Z)^2 <= e^2`. Since `sigma >= 1` and `a-e >= a/2` under the stated assumptions, the normalized fraction is at most `4 e^2/a^2`. No hidden centering assumption on `phi` or `psi` is needed: the denominator is the uncentered second moment, and the regression numerator allows an intercept.

The three-point observation is correct. A line intersects a sphere in at most two distinct points, so three distinct sphere points are not collinear and hence are affinely independent. Any three scalar target values on them admit an affine interpolant. Thus fitting those observations alone cannot certify function-level nonaffinity.

## 2. Physical energy, continuation, and the proposed tail obligation

For a true gradient flow in a fixed positive-definite raw metric,

`dE_n/dt = -||dot Theta_n||_raw^2`.

Integrating and using nonnegativity proves the displayed energy inequality. The displacement estimate follows from integrating velocity and Cauchy–Schwarz. At each fixed finite width, these estimates keep a solution inside a finite-dimensional bounded ball for any finite interval. A smooth vector field defined on the whole parameter space then permits continuation. No kernel lower bound or separation enters this argument. The claimed initial-loss limit is treated as an initialization premise; it is consistent with the usual half-sum squared loss and three binary labels with vanishing initial predictions.

The distinction between finite-dimensional continuation and a canonical population flow is essential and is preserved. Bounded energy does not supply strong compactness in an infinite-dimensional Hilbert space. Likewise, an `L2` bound on a multiplying field alone does not give the `L2 -> L2` multiplication bound needed for an ambient-ball Lipschitz argument. The assessment does not mistake either observation for a counterexample on reached states.

The proposed tail lemma remains explicitly unproved and sufficient rather than necessary. Conditional on the stated cap comparison and on converting these tails into cap-gradient errors, a Gaussian tail dominates an exponential-in-cap stability factor: `exp(C R) exp(-c R^2)` tends to zero. This elementary comparison is correct. Whether the particular incoming-field estimates deliver all required gradient and observable bounds is still a proof obligation, as the assessment acknowledges; I do not certify the cited cap construction from this input alone.

The approximate energy identity is algebraically exact wherever its chain rule is justified:

`-<G,G_R> = -||G_R||^2 - <G-G_R,G_R>`.

It genuinely can remove a stopping condition without assuming dissipation of the capped field. For example, if the stopped gradient error is bounded by `epsilon_R` uniformly up to time `T`, Young's inequality gives

`dE/dt <= -(1/2)||G_R||^2 + (1/2)epsilon_R^2`,

and therefore

`integral_0^T ||G_R||^2 dt <= 2 E(0) + T epsilon_R^2`.

The corresponding displacement is at most `sqrt(2 T E(0) + T^2 epsilon_R^2)`. One may first fix a ball radius larger than the limiting bound, including the initial norm if the ball is centered at the origin, and then take the cap large. Constants depending on that fixed radius cause no circularity when the errors vanish as the cap increases. This is conditional reasoning, not a proof that the requisite gradient-error estimate or population chain rule already holds.

The affine ascent example is exact: differentiating `w=A=sec(s)` and `C=tan(s)` verifies all three displayed equations, with initial values `(1,1,0)` and finite-time divergence at `pi/2`. The prescribed coefficient is the bounded constant one. It is correctly used to reject a claim about arbitrary bounded ascent controls, not to contradict physical squared-loss dissipation.

## 3. Residual forward composition

Under the displayed uniform derivative bound, submultiplicativity gives the Jacobian product estimate `(1+beta M/L)^L <= exp(beta M)`.

For the scalar ODE, `d(sinh h)/ds = beta sinh h`, which proves the displayed solution. Its derivative with respect to the initial condition is

`exp(beta) cosh(h0) / sqrt(1 + exp(2 beta) sinh(h0)^2)`.

It equals `exp(beta)` at zero and tends to one as `|h0|` grows. Thus the time-one map is nonaffine for every fixed positive `beta`. The bounded, globally Lipschitz field `beta tanh(h)` supplies the elementary Euler convergence asserted. This is solely a forward-composition example.

The dense-layer Jacobian retains the fresh Gaussian matrix when the activation tends to the identity. It consequently does not become a residual Jacobian of the form `I+O(1/L)` merely from that activation scaling.

## 4. Gaussian `1/L` calculation

These formulas concern the Gaussian covariance/feature-moment recursion, which is the population initialization map relevant after the fixed-depth width limit. They are not an assertion that all hidden layers of a finite-width Gaussian-weight network are jointly Gaussian unconditionally. That distinction is consistent with the final fixed-`L` width-first instruction and with the Gaussian-input assumptions stated for the calculation.

For `Q=qC`, with `q>0`, diagonal entries of `C` equal to one, and centered jointly Gaussian coordinates, Gaussian integration by parts gives

`E[Z_i psi(Z_j)] = Q_ij E psi'(sqrt(q) G)`.

The same formula holds at singular covariances. Conditional regression onto `Z_j` reduces it to the one-dimensional identity; zero covariance and coincident/opposite coordinates cause no problem. Both cross terms in the activation product are therefore proportional to `Q`, so

`Q^+ = (1+2e a(q))Q + e^2 B`.

All diagonal entries of `B` are the same because all marginal variances are `q`. Writing

`q^+ = (1+2e a(q))q + e^2 b`

and subtracting `C` after normalization proves the displayed increment exactly. Here `Q^+` is the next centered Gaussian preactivation covariance obtained from the uncentered feature second moment; it must not instead be read as the centered covariance of `phi_e(Z)` itself when `psi` has nonzero mean.

For `K=||psi||_infinity`, projection onto `G` and the derivative bound yield

`q^+ >= q(1+e E psi'(sqrt(q)G))^2 >= (1-e)^2 q`.

The last inequality is used only for `0<=e<=1/2`. Minkowski's inequality gives `sqrt(q^+) <= sqrt(q)+eK`. Consequently, for `e=beta/L`, `q_0=1`, and `0<=l<=L`,

`q_l >= (1-e)^(2l) >= exp(-4 e l) >= exp(-4 beta)`,

`q_l <= (1+l e K)^2 <= (1+beta K)^2`.

The lower exponential estimate uses `log(1-e) >= -2e` on `[0,1/2]`. Thus this displayed form of the constants is conditional on `L>=2 beta` and `||psi'||_infinity<=1`, just as the preceding hypotheses require. Every fixed `beta` satisfies the depth restriction eventually.

Since `|C_ij|<=1`, `|B_ij|<=K^2`, and `0<=b<=K^2`, the increment has magnitude at most `2 e^2 K^2 exp(4 beta)`. Summing `L` increments yields exactly the stated `2 beta^2 K^2 exp(4 beta)/L` bound. The conclusion concerns disappearance of new normalized initialization geometry; it says nothing about a trained time interval.

For an affine offset `d=beta b/L`, the cross terms vanish under each fresh centered Gaussian mixing step and the covariance increment is `d^2 11^T`. After `L` steps this gives `Gamma+(beta^2 b^2/L)11^T`. The absence of a coherent first-order offset is correct.

## 5. Calibrated `1/sqrt(L)` candidate

The proposed residual `r` has all stated properties. In particular, `0<a0<1`, `r` is odd, has at most linear growth, has bounded positive-order derivatives, and obeys `E[G r(G)]=0`. Its nonzero linear part at infinity means it is unbounded in value. The document expressly acknowledges the change of activation class.

The constant `v` is strictly positive: if it vanished, continuity and full Gaussian support would imply `atan(z)=a0 z` for every real `z`, which is false. Oddness supplies zero mean. Expanding the squared activation then gives the unit variance identity exactly.

For standard Gaussian coordinates with correlation `c`, each mixed term is zero by Gaussian regression and `E[G r(G)]=0`. Thus

`c^+ = (c+e_L^2 R(c))/(1+e_L^2 v)`

is exact for the Gaussian feature map. Cauchy–Schwarz gives `|R(c)|<=v`, uniformly including the endpoints.

The covariance differentiation identity is justified here by the available bounded derivatives and Gaussian integrability. More explicitly, put `Y_c=cX+sqrt(1-c^2)Y` for independent standard Gaussians. Differentiate `E r(X)r(Y_c)` in the interior and integrate by parts in `X` and `Y`. The terms containing `r''` cancel, leaving

`R'(c)=E[r'(X)r'(Y_c)]`.

This has absolute value at most `||r'||_infinity^2`. The Lipschitz property of `r` gives continuity of `R` at both endpoints through this same coupling. Hence the claimed Lipschitz bound extends to all of `[-1,1]`.

Writing `F(c)=beta^2(R(c)-vc)`, the exact update is

`c^+ = c + (1/L) F(c)/(1+beta^2 v/L)`.

Its difference from the Euler step `c+F(c)/L` is uniformly `O(L^(-2))`, since `|R(c)-vc|<=2v`. The usual elementary error recursion for a Lipschitz vector field then gives convergence uniformly across the depth grid, and across `[0,1]` with the usual piecewise constant or linear interpolation. The interval is preserved: each discrete map is a unit-variance feature correlation; also `F(1)=F(-1)=0`, so the limiting ODE cannot leave the interval.

The nonaffinity argument is valid: independence and oddness give `R(0)=0`, integration by parts gives `E r'(G)=0`, hence `R'(0)=0`, whereas `R(1)=v>0`. Thus `R`, and therefore `F`, is nonaffine. This also really produces a nonaffine time-one correlation map for every `beta>0`: its endpoints are fixed, while its derivative at zero is `exp(-beta^2 v)<1`, incompatible with an affine map fixing both endpoints.

The cumulative coefficient `L e_L^2 v = beta^2 v` is independent of the separation parameter. Choosing it to be of order one is legitimate because `v>0` is fixed and `beta` is fixed as `L` grows. This coefficient is not a claim of a uniform lower bound on nonlinear geometry for every possible dataset; correlations initially equal to zero or either endpoint are equilibria. Nor does it measure trained nonlinearity. The assessment makes neither stronger claim.

## 6. Training scaling and overall quantifiers

With uniform bounds on the relevant state and parameter sensitivities, a residual branch multiplier `1/L` gives a parameter derivative of size `O(1/L)` per independently parameterized branch. Squaring and summing over `L` branches in an unaveraged sum metric gives an `O(1/L)` branch-kernel contribution. This is an upper-order statement; no positive matching lower bound follows from the stated upper bounds. The assessment's use of “of order” should be read in that sense. Its qualification concerning a nontrivial branch-training limit and separate treatment of the readout is correct.

The central fixed-depth objective has the appropriate quantifiers: one activation is chosen independently of both horizon and width; constants may subsequently depend on each finite horizon and fixed depth. Uniqueness, continuation from reached states, finite-width identification, and specified joint observable topologies remain obligations. No fitting-rate or all-time kernel-floor assertion is silently substituted for them.

A separate theorem at every fixed depth does not by itself imply convergence along a depth growing with width. The document explicitly preserves this distinction. It also keeps the residual architecture, metric changes, literature methodology, and original dense Gaussian model separate.

## Final conclusion

PASS: the new elementary computations are sound under their stated conditional assumptions, and the assessment consistently labels the global trained-flow objective as open. The only precision reminders are already implicit in those assumptions: the Gaussian recursion is the population Gaussian map, the displayed `1/L` constants require `L>=2 beta` and the unit derivative bound, and the residual kernel estimate supplies an upper bound rather than a lower bound. None changes the strategic conclusion or requires a mathematical correction. This audit does not claim a new global trained theorem.
