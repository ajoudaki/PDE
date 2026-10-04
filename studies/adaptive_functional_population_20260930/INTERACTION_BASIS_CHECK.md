# Internal check of the corrected interaction-basis route

Date: 2026-09-30. **Internal mathematical check, not a promotion review.**

The reviewer read the entire candidate, Sections 1--10, after freezing its own independent route. This cross-route reading was explicitly authorized by the supervisor. No other scientific inputs were fetched, no computation was used as scientific evidence, and the candidate was not edited.

Checked file: `INTERACTION_BASIS_ROUTE.md`.

Exact checked SHA-256, verified before and after the check:

```text
adad55396cacb7e7d300701a0c23c48aa74ae33e6a6e07defdb00427c16878f6
```

## Verdict and required minor corrections

**Internally checked: the stated fixed-width analytic construction and conditional finite-horizon comparison pass, subject to the minor corrections below.** No substantive mathematical defect was found in the full candidate. This does not establish efficient width-uniform approximation or a universal integration algorithm for infinite input laws.

1. **Line 101, zero singular values.** The optional formula `e_k=v_k^T b/sigma_k` requires `sigma_k>0`. Retain only positive singular directions when `rank(B)<p`; extra null directions contribute nothing to `APB*` and need no stored atom. The actual ridge-sketch implementation already handles rank deficiency.
2. **Lines 312, 386, 439, 566, math delimiters.** Remove the backslash immediately before the closing dollar sign in the expressions for `Q(t,s)`, `p,lambda`, `pq`, and `||W_(1,0)||_op/sqrt(n)`, respectively.

Optional precision: (4.3) holds almost everywhere for arbitrary square-integrable factors and classically for the continuous factors used by the construction. The startup limits also use continuity, which those actual factors have.

These line references concern only the checked hash. Applying the corrections creates a new version; this report preserves the old version's provenance.

## Verification of the substantive claims

| Component | Check and conclusion |
|---|---|
| Canonical scaling and energy | Ordinary derivatives of `E=E_mu[(f-f_*)^2]` contain `2/n`. The metric inverse multiplies only the first-layer and readout blocks by `n`, giving exactly the displayed `F_1,H,G_l`. Thus `E_dot=-||theta_dot||^2` in (1.1), including both outer-block `1/n` norm weights. The path-radius bound is correct. |
| Cross-population factorization | `a=-2r delta/sqrt(n)` and `b=h/sqrt(n)` give `AB*=G` with the correct sign and scale. Equations (2.1), (2.2) estimate the interaction rather than individual field tails. |
| Ridge approximation | The stated trial `Z_0=Omega_1^dagger[I_k,0]V^T` is correct; no inverse of `Sigma_1` is missing. In singular coordinates its error blocks are `-Sigma_2 Omega_2 Omega_1^dagger` and `Sigma_2`. Their squared norms add. Conditional Gaussian expectation gives `||Sigma_2||_F^2 ||Omega_1^dagger||_F^2`; the reciprocal-distance argument yields `E||Omega_1^dagger||_F^2=k/(p-k-1)`. Hence (3.4), (3.6), and (10.2) have the stated constants. |
| Random source-path bound | The reference trajectory is independent of the additional sketches. Cauchy--Schwarz in time and Markov give (3.7). The proof does not incorrectly apply a fixed-matrix estimate to the adaptive surrogate trajectory. |
| Smooth factors and projected flow | Positive regularization gives a smooth inverse square root; the displayed differential bound is correct. The ridge projector satisfies `0<=P_lambda<=I`, so `<G,P_lambda G> >= ||P_lambda G||_F^2`, proving projected-flow dissipation. Constants may grow as regularization vanishes. |
| Exact Legendre pairing | With normalized coefficients `a_j=U_j/t`, `b_j=V_j/t`, Parseval gives `int_0^t AB^T=t sum_j a_j b_j^T=(1/t)sum_j U_j V_j^T`. The factor `1/t` and Frobenius convergence argument are correct. |
| Moment ODE and prefix sums | Differentiation of `s/t` gives the negative triangular term in (4.3). Integration by parts gives `D_jj=j` and `D_jk=sqrt((2j+1)(2k+1))` for `k<j`. The stated prefix-sum evaluation therefore removes the need for a dense `q by q` connection table. |
| Startup and autonomy | On a small parameter ball, projection contraction bounds the memory map by `t M_A M_B` and its path Lipschitz constant by a constant times `t`. This justifies the short-time contraction at the prescribed continuous startup. At positive time the stored moments and clock determine continuation without a past network. |
| Moving-frame transport | `partial_t Q=Omega_e Q` gives the term `U_j Omega_e^T`; differentiation with respect to past time gives `(A_dot-A Omega_e^T)Q^T`. Orthogonality cancels the paired transports. Normal frame motion is retained in the source. The actual implementation uses the smooth sketch rather than an unexplained functional frame. |

The time-tail constant merits an explicit check. Weighted Legendre derivative orthogonality gives

\[
\sum_{j\ge q}\|a_j\|_F^2\le
\frac{1}{q(q+1)}\int_0^1u(1-u)\|a'(u)\|_F^2du
\le\frac{t^2K_A^2}{6q(q+1)}.
\]

The analogous bound for `B`, their product square root, and the outer factor `t` give exactly `t^3 K_A K_B/[6q(q+1)]`. For scalar affine factors at `q=1`, the omitted covariance is `t^3 A_dot B_dot/12`, matching the constant. Only one derivative of each factor is required.

For the comparison proof, time projection has `L^2` norm one, so the difference of two reconstructions is bounded by

\[
(K_A^{\rm par}M_B+M_AK_B^{\rm par})\sqrt t
\left(\int_0^t\|z-z'\|^2ds\right)^{1/2}.
\]

After including exact-gradient blocks and the defects, the displayed scalar inequality squares to `e(t)^2 <= 2 epsilon^2 + 2 C^2 T int_0^t e(s)^2 ds`. Gronwall yields exactly the factor `sqrt(2) exp(C^2 T^2)` in (6.1), with no dependence on `q` introduced by projection. Time derivatives are used only along the reference path. Positive-margin continuation is valid: bounded factors also keep the finite stored moments bounded while the parameter reconstruction remains in the ball.

Thus fixed-`n,p,lambda`, `q -> infinity` convergence is to the projected flow, as stated. At `p=n`, the separate trial `Z_0=Omega^(-1)` gives the uniform source residual `sqrt(lambda)||Omega^(-1)||_F`; ordinary stability of the original vector field then justifies the stated iterated full-rank convergence. These arguments do not justify interchanging limits or asserting regularization-uniform factor derivatives.

## Entire-file checks beyond the central theorem

The constant-target obstruction is correctly normalized: `h_1(x_j)=e_j`, `h_2(x_j)=1`, `w_dot(0)=2 1`, and `delta_(2,dot)(0,x_j)=2e_j` give `G_(2,dot)(0)=4I/n^2`. The relative Frobenius rank calculation follows. Gaussian full support only transfers it to a possible, potentially extremely rare neighborhood. The candidate correctly excludes typical-Gaussian, width-uniform absolute-error, and output-error conclusions. Smooth input bumps do not give uniform density-regularity constants, as disclosed.

The quantization lemma is also correct. Conditional expectation onto cells gives forward residual Hilbert--Schmidt norm at most `L_b sqrt(Q_k+o(1))`. Its cross interaction has nuclear norm at most `M_A L_b sqrt(Q_k+o(1))`. Adding a rank-`k` approximation of this remainder to the rank-`k` projected interaction proves (10.1). The source factor `-2` is already in `a`, so no extra factor four is missing. Equation (10.3) includes both `1/sqrt(d)` and `1/sqrt(n)` correctly. Quantization cells are a proof device, not an uncounted algorithmic input.

## Resource and scope audit

No dense evolving hidden matrix, fitted prefix, canonical past network, or future trajectory drives the construction. Hidden actions use immutable initialization plus the stored factors. The two source products can be streamed with `np` accumulators and `p by p` algebra; the fully evolved first layer costs `nd`. Fixed dense initialization and input storage are expressly distinct from the learned-state bound. At full source rank storage can be quadratic, which is acknowledged.

For a finite dataset, repeated streaming passes implement the expectation products. For an infinite law, the candidate states an integration access assumption and a conditional error bound, not a general computable quadrature theorem. Equation (7.1) follows from projection contraction and expanding the two factor errors, provided those errors are controlled along visited states. Single-call Monte Carlo concentration does not supply that hypothesis. These explicit qualifications must stay attached to downstream claims.

The ridge startup delay `G=O(t)` versus `S=O(t^3/lambda)` is real and correctly charged to the population defect. The optional suppressed-prefix error is likewise charged explicitly. No exact trained prefix is used for initialization.

The candidate repeatedly retains dependence on width, the actual initialization, sketch norms, and regularization. Its source-tail exponent and `q^-2` reconstruction rate therefore do **not** become a width-uniform trajectory rate without further estimates. The unresolved joint control needed for `pq=o(n)` at fixed observable accuracy is stated accurately. This internal check upgrades no claim beyond the fixed-width, conditional scope above.
