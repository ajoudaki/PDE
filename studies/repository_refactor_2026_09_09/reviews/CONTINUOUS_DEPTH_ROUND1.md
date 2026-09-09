# Isolated adversarial mathematical review

**Verdict: CLEAN within the explicitly stated scope.** No required mathematical fixes were found. The global characteristic theorem, compact-time joint width/depth estimate, kernel and loss identities, activation class, and stated obstruction to universal fixed linear-moment closure follow under their declared hypotheses. This verdict does not certify a dense-matrix model, a gradient-descent limit, eventual fitting, or a stronger nonclosure assertion.

## Inputs, hashes, and read coverage

Only these two inputs were read, both in full:

| Input in `/tmp/pde-established-depth-review.Rthh2y/` | Bytes | Lines read | SHA-256 |
| --- | ---: | --- | --- |
| `NOTATION.md` | 5,110 | 1–98, complete | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `continuous_depth.md` | 54,128 | 1–1490, complete | `0930e1b2a4c219749cd1994ffb657093aea0a103b2d4a414c21bd697604d5362` |

The chapter was read in consecutive ranges 1–360, 361–730, 731–1100, and 1101–1490, with no gaps or truncated read output. All thirteen sections, Theorem 4.1, Proposition 12.1, and the conditional example outside A1–A2 were included in the audit. References below are to `continuous_depth.md` unless expressly identified otherwise.

No project files, source history, other reviews, internet sources, agents, or numerical experiments were used. No input was edited. This review does not use a previous PASS as evidence. `REVIEW.md` is the sole output file.

## Required fixes

None. In particular, the audit did not find a missing extra moment assumption, parameter-support bound, depth/width rate relation, positive discrete-sensitivity assumption, second classical derivative assumption on the feature, or measurable optimal-coupling selection needed to complete the stated proofs.

## Proof audit

### 1. Assumptions, architecture, and notation

The feature is explicitly a scalar residual particle feature, with raw parameter in Euclidean space, rather than the dense network's coordinatewise activation. A1 supplies a parameter-uniform affine growth bound in the state and a global state Lipschitz constant. A2 supplies bounded parameter gradients and joint Lipschitz bounds for both first derivatives on every bounded state strip. Together with the explicitly assumed joint `C^1` regularity, these are sufficient for the uses of the chain rule, local ODE uniqueness, transport comparison, and first-order Taylor remainders below. No change of raw parameterization is silently treated as preserving these properties.

The fixed finite scalar batch, arbitrary labels, positive fixed mobility, half mean squared loss, constant population initialization in depth, and finite first moment of the initial law are explicit (lines 30–102, 129–139, 344–390). General-profile existence and restart are separately stated on the depth-integrable first-moment space. The joint limit concerns deterministic sequences with both width and depth tending to infinity, in probability, uniformly on each fixed finite training interval.

The notation contract is respected. Finite hidden states are lower-case and population states are capitalized. The auxiliary particle feature, parameter dimension, sensitivities, architectural mesh, and coefficient fields are typed where introduced. Most importantly, `r=f-y` is consistently the residual; neither finite `p` nor population `P` contains it. The architecture and loss/mobility conventions are explicitly distinguished from the dense-network defaults in `NOTATION.md`. There is no residual/adjoint substitution in any gradient or kernel formula.

### 2. Exact finite gradients and global finite flow

Equations (2.4)–(2.6) have the correct downstream index. A parameter in layer `ell` changes the next state, so its output derivative is `p_(ell+1) grad_theta Phi/(nL)`. Consequently `grad_theta L=q/(nL)`, and mobility `kappa nL` gives exactly `theta_dot=-kappa q`.

The normalization of (2.7) also checks: multiplying the Gram matrix of these output gradients by `nL` leaves the layer/particle average `1/(nL)`. Substitution gives (2.8), and squaring `grad L=q/(nL)` gives precisely the factor `-kappa/(nL)` in (2.9). Positive semidefiniteness follows from a finite Euclidean Gram expression. These identities make no independence assumption after training.

The forward recursion yields the uniform bound `Z_*=exp(c1)(x_*+c0)`. The product of absolute sensitivity factors is bounded by `(1+c1/L)^L <= exp(c1)`, even when some factors are zero or negative. Thus no condition `L>c1` is being used. On this state strip each particle velocity is bounded by

`kappa (Z_*+y_*) P_* C_(Z_*)`.

The full finite vector field is locally Lipschitz: the forward recursion is `C^1`, while A2 makes the sensitivity and feature-gradient compositions locally Lipschitz. For each fixed finite system, bounded coordinate velocities rule out a finite escape time. The Cauchy-at-the-endpoint and local-restart argument at lines 467–477 therefore proves unique global exact gradient flow. It does not rely on an unproved coercivity or fitting property.

### 3. Forward and backward readouts for Borel profiles

For a fixed state, integration against the Borel probability kernel is measurable in depth. The forward right-hand side is globally `c1`-Lipschitz in state and uniformly bounded at zero. Its integral map acts on continuous paths and contracts on sufficiently short depth intervals. The uniform growth estimate extends the resulting absolutely continuous solution to the whole depth interval.

The exponential formula (5.5) solves the backward equation with terminal value one. Its exponent is bounded in absolute value by `c1`, giving both upper and strictly positive lower bounds for the continuous sensitivity. The integral equations determine unique continuous readouts even when the profile itself has no continuous representative.

The coupling bound (5.6) is valid for the scalar and vector functions used. Integrating the parameter gradient along a segment proves (5.7); A2 and bounded gradient factors also prove the Lipschitz estimates for the kernel's gradient products. All relevant parameter integrands on the state strip are bounded. No second parameter moment is needed.

### 4. Discrete population comparison and existence

The recursions (6.5) and (6.6) follow by separating state and law changes, using the parameter coupling bound, and retaining the absolute bound on each discrete backward factor. Summing their local forcing with weight `h` yields the maximum state and sensitivity errors in terms of the average law distance `d_L`. A single layer's law error is not required to be small.

Substitution in the velocity gives (6.7); comparison of bounded gradient products gives (6.8). Transporting finitely many initial layer couplings and averaging (6.10) closes a Gronwall inequality because `d_L <= h sum H_ell`. This proves (6.11) with a constant independent of depth.

The characteristic fixed-point construction of Section 7 applies to the finite product with this metric and the same uniform velocity bounds. Empirical atoms follow the very same characteristic ODE by (2.6) and (6.3), so identification with the empirical population solution is valid in the characteristic class. It does not infer characteristic uniqueness merely from weak PDE uniqueness.

### 5. Completeness, measurability, and the characteristic fixed point

The completeness proof at lines 641–683 is correct. Summably close successive laws can be coupled on one countable product using Borel disintegration on Euclidean spaces. Summable expected increments give an almost-sure limit with an integrable displacement from the first variable, and convergence in expected distance. This proves completeness of the Wasserstein space; finite rational quantization proves separability. The stated disintegration fact and countable probability-kernel construction are applicable to precisely the Borel Euclidean spaces in use.

For the profile space, the summable-subsequence argument gives a Borel, almost-everywhere pointwise limit in that complete Wasserstein space. The integrated tail estimate (7.1) gives convergence in the profile metric and finite integrated first moment. Quotienting by almost-everywhere equality therefore produces a complete metric space. Completeness of continuous curves in its uniform metric follows by taking uniform limits.

Equations (7.2)–(7.4) correctly control all continuous readouts and the velocity by the integrated profile distance. The additional observation (7.5) is essential and valid: the depth derivatives of the readouts are uniformly bounded even for discontinuous profiles. As a result the velocity itself has a jointly continuous, uniformly Lipschitz representative in depth and parameter. Null-set changes in the law profile do not alter this representative.

A continuous trial curve in the profile metric thus produces a velocity continuous in training time in the uniform norm. Boundedness and uniform parameter Lipschitzness give global characteristics jointly continuous in time, depth, and initial parameter. The Picard iteration has uniform bounds on its increments despite the unbounded initial-parameter domain.

The pushforward profile is Borel. The kernel integration argument gives weak measurability, and the explicit finite-grid approximations at lines 768–775 upgrade it to measurability in the Wasserstein topology. Their error is controlled by a vanishing mesh error and the first-moment tail at each depth. Bounded characteristic displacement proves both membership in the profile space and time Lipschitzness in its metric.

The common-initial-parameter coupling gives exactly the contraction factor `C tau exp(C tau)` in (7.8). The fixed-point map returns curves starting at the prescribed profile, and its estimates hold uniformly over that profile. The contraction can therefore be iterated over all finite training intervals. Differentiating compactly supported `C^1` tests is justified by the bounded velocity and proves the displayed continuity equation in its specified weak sense.

Finally, (7.10) takes an infimum over initial couplings separately at each depth only after deriving a bound valid for every such coupling. The resulting inequality involves measurable Wasserstein distances, which can then be integrated. There is no unproved measurable selection of optimal couplings. A second Gronwall estimate yields stability on all of the profile space. Autonomy and characteristic uniqueness justify the semigroup and exact restart statement. Uniqueness is explicitly restricted to the characteristic class, as proved.

### 6. Canonical representative and first-order depth consistency

With constant initial law, characteristics at two depths can be coupled using the same initial parameter. The velocity's uniform depth Lipschitz bound gives (8.1), and hence a Wasserstein-Lipschitz law profile on each compact training interval. It is a representative of the previously constructed equivalence class at every training time. A continuous distance function that is zero almost everywhere on `[0,1]` is zero everywhere, including at the endpoints; this proves uniqueness of the representative used for grid evaluation.

This regularity makes both forward and backward depth coefficients Lipschitz. The forward quadrature defect is `O_T(h^2)`. In the backward defect, freezing the sensitivity at the right endpoint and its coefficient at the left endpoint also costs `O_T(h^2)` by the bounded, Lipschitz product estimate. Thus (8.5) matches the exact discrete sensitivity convention.

Forward and backward discrete Gronwall estimates give (8.7). Comparing the velocities requires the additional shift from `P_(ell+1)` to `P(s_ell)`, and that `O(h)` term is explicitly retained. The common-law characteristic coupling then gives `E_L <= H_L` and the closed inequality (8.10), proving (8.11).

The continuous kernel integrand is bounded and depth-Lipschitz by the same gradient-product estimate. Its discrete comparison includes the sensitivity shift, and the Riemann-sum error (8.12) is bounded by half the Lipschitz constant times `h`. Hence (8.13) follows. This argument uses deterministic population solutions from the constant initial law; it assumes no depth regularity of the random empirical initial profile.

### 7. Width error, arbitrary joint rates, and observables

Equation (9.1) follows directly from discrete population stability and the readout estimates, with initial discrepancy equal to the averaged empirical Wasserstein error. Combining it with the deterministic depth estimate proves the entire pathwise bound (4.2), including maximum hidden-state and sensitivity errors and every kernel entry. Its constants are independent of both discretization sizes and of realized initial parameters.

The first-moment initialization proof is sufficient as written. Projection onto a fixed ball costs the first-moment tail twice. On that ball, finite quantization costs at most `2 epsilon`, and unmatched mass can be transported over diameter `2R`. Independence within a layer gives the displayed empirical-frequency variance estimate. Taking the limits in the order `n`, quantization mesh, then radius proves `alpha_n -> 0` without an extra tail assumption or an asserted algebraic rate.

Linearity of expectation gives `E epsilon_(n,L)=alpha_n` for every depth. The probability bound is consequently `C_T(alpha_n+1/L)/epsilon`; it imposes no relation between width and depth and does not require independence between layer errors. The random compact-time supremum is measurable: the finite ODE and readouts depend continuously on initial parameters, and time continuity permits taking the supremum over a countable dense set of times.

Outputs and residuals are terminal-state readouts. The bounded-residual calculation in (9.7) gives the claimed uniform loss convergence with the correct half-mean normalization. The piecewise-constant empirical-profile statement follows by integrating the canonical representative's depth Lipschitz bound over each cell. Every convergence statement remains on a fixed compact interval of exact gradient-flow time.

### 8. Differentiable outputs, kernels, and dissipation

The continuum kernel is positive semidefinite by the squared-norm expression (10.1). The output differentiation argument is rigorous under A1–A2, including unbounded initial parameter support. Specifically, (7.4) and the time displacement bound imply uniformly in depth and initial parameter that

`|v[rho_u](s,Theta_u)-v[rho_t](s,Theta_t)| <= C |u-t|`.

The characteristic difference quotient therefore converges uniformly to its velocity. The forward-state time increment is also uniformly `O(|u-t|)`. Since both first derivatives of the feature are Lipschitz on the state strip, the Taylor remainder divided by the time increment is uniformly `O(|u-t|)`. Subtracting the candidate linear Volterra equation and applying Gronwall proves uniform convergence of the state quotient to the solution of (10.3). This supplies an actual time derivative, not merely a formal variation. At initial time the right derivative is the appropriate one.

Multiplication by the absolutely continuous sensitivity cancels the `B_a P_a U_a` terms. The terminal and initial boundary values then give (10.5), with coefficient `-kappa/m`. Differentiating the half mean squared loss gives `-kappa r^T K r/m^2`, identical to `-kappa` times the integral of `|Q|^2` in (10.6).

For general initial profiles, the same uniform bounds dominate integration against the depth-dependent initial probability kernel. No smooth density, continuous initial depth representative, or additional moment is needed for these readouts. The text correctly requires positive full dissipation energy for a negative loss derivative and correctly allows batch cancellations. The admissible zero feature is a valid counterexample to inferring eventual fitting from A1–A2.

### 9. Concrete activation class and possible motion

All derivatives in (11.2) are correct. Bounded `A`, `U`, and `B`, together with bounded `sigma'`, give A1 globally. On a bounded state strip the argument `U(omega)z+B(beta)` is bounded and jointly Lipschitz. Every factor in (11.2) is then bounded and Lipschitz by the specified `C_b^(1,1)` conditions and the conditions on `sigma'`. Product differences prove A2; boundedness of `sigma` on the entire real line is not required.

The listed examples satisfy these conditions. In particular, softsign has a continuous derivative `(1+|u|)^(-2)` with global Lipschitz constant at most two; no second derivative at zero is needed. Softplus has logistic first derivative. For exact GELU the first and second derivatives stated at lines 1245–1246 are correct and bounded. The bounded smooth examples, affine functions, and stated rescalings also fit the declared class.

The initial-motion construction is valid. At the chosen atomic law and input, the nonzero parameter gradient persists on a positive interval of depths by continuity of the initial forward state. The scalar residual is chosen nonzero, and the continuous sensitivity has a positive lower bound. Thus the initial dissipation integral is strictly positive. This proves the claimed possibility of motion without asserting it for every initialization. The exclusions of exact ReLU and uncontrolled superlinear/raw-weight regimes are consistent with the assumptions.

### 10. Fixed linear-moment obstruction

Proposition 12.1 is correct for any finite list, including an empty or linearly dependent list. If every finite relation between the vectors `(1,psi_1,...,psi_J)` annihilates the feature, (12.2) defines a well-defined linear functional on their finite-dimensional span. Extending a basis represents this functional by coefficients, proving the span conclusion. Its contrapositive yields (12.3).

The constant coordinate forces the coefficients in that relation to sum to zero. Their positive and negative masses are equal and strictly positive; normalizing them yields two finitely supported probability laws with equal declared moments and different feature integrals. Repeated support points do not invalidate the construction. The converse is immediate by integration of the linear combination. With finite support, the moments here are finite sums of the stated finite real values.

An infinite-dimensional family of feature functions cannot be contained in the span of a fixed finite list of moments and the constant function. The stated obstruction therefore follows for universal exact forward-coefficient recovery over all finitely supported laws and the specified continuum of states. It does not assert impossibility for an arbitrary nonlinear encoding, a restricted reachable orbit, or a fixed finite set of state values.

### 11. Analytic nondegeneracy and generalized Vandermonde proof

The nondegeneracy hypotheses at lines 1338–1345 are sufficient and explicit: a nonzero amplitude on a parameter slice, an attained fixed bias, a slope range containing a neighborhood of zero, and analyticity with infinitely many nonzero Taylor coefficients at that bias. For any finite choice of states, the neighborhood of slope zero can be reduced so all Taylor expansions are valid simultaneously. No uniform analytic radius over the entire state interval is needed.

The interval permits arbitrarily many distinct states of the same nonzero sign. A function identity on the parameter slice gives (12.5) by extracting any chosen nonzero Taylor orders. Gaps between those orders cause no problem.

The generalized Vandermonde argument is valid. For a combination with `N` nonzero monomial terms and increasing real exponents on the positive half-line, division by its smallest power preserves its positive zeros. If it had `N` distinct zeros, Rolle's theorem would give at least `N-1` distinct zeros of the derivative. That derivative has `N-1` nonzero terms with distinct real exponents, so induction bounds its zeros by `N-2`. The one-term case starts the induction; zero coefficients can simply be omitted. A singular square evaluation matrix would give a nonzero row combination violating this zero bound, so the matrix is invertible. For negative states the exponents used are integer Taylor orders, and each row differs from the positive-state matrix by the nonzero factor `(-1)^k`. This proves independence for every finite size and hence the infinite-dimensional span assertion.

The fixed-slope/bias example correctly has forward feature span at most one. Thus the activation name or nonaffinity alone is not being used to infer nonclosure.

### 12. Moment dynamics and the example outside the theorem

For `C^1` moment functions and finitely supported characteristic laws, (12.6) follows by differentiating finite sums with preserved atom masses. For general laws, the explicitly added initial integrability and integrable supremum of the transported moment gradient give domination by the bounded velocity; they justify the same derivative formula. These extra hypotheses are necessary for this extension and are actually stated, rather than inferred from a first moment alone.

The generator-invariance and sensitivity/kernel-readout requirements are appropriately conditional on universal recovery and the ability to isolate the relevant state contributions. Applying the proposition to each required integrand gives the stated necessary conditions. The text expressly avoids imposing each separate generator on a single fixed trajectory whose combinations may cancel.

For the quadratic-parameter example, direct differentiation gives the linear characteristic velocity `-b theta`. Its exponential characteristic yields `M2(t)=M2(0) exp(-2 integral b)` at each depth, which gives (12.10) wherever the stipulated solution and integrability conditions hold. The displayed kernel follows from `partial_theta Phi=theta chi(z)`. The example is explicitly conditional and outside the global theorem. A nonzero derivative of `chi` violates A1; if `chi` is a nonzero constant, the value at state zero violates A1 instead. A2 fails on a strip containing a point where `chi` is nonzero. No existence, joint-limit, or fitting conclusion is silently imported into this example.

### 13. Scope of the conclusion

The conclusions in Section 13 match what is proved. The state is a measure field with determined forward/backward readouts, and atom-based representations still consist of depth fields. A fixed count of field types is never equated with a finite-dimensional scalar state. Architectural Euler consistency is not presented as a training-time Euler/GD result. Nonincreasing loss is not promoted to fitting or minimizer convergence. The dense Gaussian-matrix architecture is expressly excluded throughout.

## Optional remarks

These are exposition suggestions only; neither is needed for the CLEAN verdict.

1. At lines 1138–1142, displaying the uniform velocity-increment estimate used in audit item 8 would make the uniformity over unbounded initial parameter support immediately visible. The existing estimates already imply it, so this is not a missing hypothesis or proof gap.
2. In Proposition 12.1, explicitly calling the finite-support integrals “finite sums” would clarify why no global measurability or regularity condition on the arbitrary functions `psi_j` is needed for that algebraic statement. The later differentiated-moment statement correctly adds its own `C^1` and integrability requirements.
