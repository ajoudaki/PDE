# Focused reconstruction of the restricted terminal candidate

Input: the complete frozen `TERMINAL_APPROXIMATION.md` and the supervisor's assignment only, together with required proof/notation instructions. This check does not inspect other routes, prior reports, code, or experiments. It checks the displayed restricted construction, not the requested general deep-network theorem.

## Actual proved scope

The candidate proves a deterministic numerical approximation to the population endpoint for one hidden layer, one training example, zero initial readout, independent Gaussian first weights, and a fixed effectively computable nonconstant activation satisfying
\(0<a\le\phi\le b\) on the real line and the stated strip derivative bound. Both parameter blocks follow their prescribed gradient-flow updates. For a deterministic query whose orthogonal component relative to the training direction is at least \(\tau_0>0\), the candidate compares its predictor with the random dense endpoint in ensemble mean square. The constants are uniform over the stated bounded query domain, and summing the squared bounds gives the corresponding result for a fixed finite panel.

At fixed problem constants, it retains \(O(d+(\log n)^3)\) working numbers, with \(O(\log n+\log d)\) bits per working number, and has \(O(d+(\log n)^3)\) arithmetic operations per query. Its error is eventually at most the actual ensemble RMS discrepancy between two independent dense endpoints. This is neither a comparison to one realized pair nor a fixed-confidence or pathwise guarantee. It does not establish a general sample-count, depth, activation-class, or feature-gap theorem.

## Four checks

**Exact feature clock.** For \(u_0=x_0/\sqrt d\) with \(\|u_0\|_2=1\), the first-layer velocity is parallel to \(u_0\). Substituting

\[
\partial_s z_s=w_s\phi'(z_s),\qquad
\partial_s w_s=\phi(z_s),\qquad
\dot s=2(y-F_n(s))
\]

into the physical equations gives their exact factors and initial conditions. The identity

\[
\partial_s[w_s\phi(z_s)]
=\phi(z_s)^2+w_s^2\phi'(z_s)^2\ge a^2
\]

makes the empirical root unique and gives exponential decay of the physical training residual. The uniform bounds on \(w_s\) and \(z_s-g\) rule out finite feature-time escape. The independent orthogonal Gaussian component of each initial row then gives the claimed exact query formula. These steps correctly identify the finite dense endpoint, not merely a proposed limiting model.

**Mean bias.** With \(\Delta=s_n-s_*\), the inverse-slope bound gives \(\mathbb E\Delta^2=O(n^{-1})\). In the empirical-root Taylor identity, the empirical value error has mean zero, while the product of empirical derivative error and \(\Delta\) is \(O(n^{-1})\) by Cauchy–Schwarz. The bounded second derivative supplies the same order for the remainder; thus \(\mathbb E\Delta=O(n^{-1})\). Applying the same expansion to the query average yields

\[
|\mathbb E f_n^\infty(x)-K(\rho,\tau)|\le C_b/n.
\]

All differentiated quantities are uniformly bounded on the stated feature interval. The formulas for \(\psi_s''\), \(z_s''\), and \(k_s''\), and the constants in (15)–(19), are consistent. The argument does not incorrectly assume independence of the empirical clock and the particles.

**Actual variance.** Conditional on all training Gaussian coordinates, the orthogonal query Gaussians remain independent. A bounded nonconstant continuous activation has strictly positive variance under every full-support Gaussian with positive variance. Continuity and the compact rectangle in (20) therefore give \(v_0>0\). For each row with \(|G_i|\le B_0\), its conditional contribution is at least \((ay/b^2)^2v_0/n^2\). Taking expectations and summing gives

\[
\operatorname{Var}(f_n^\infty(x))\ge
\frac{a^2p_0v_0}{b^4}\frac{y^2}{n}.
\]

This proof remains valid although the empirical stopping clock depends on all training coordinates. The lower bound is deliberately unavailable at the training point. Together with the deterministic bias bound, the exact bias–variance identity proves (32); its lower ratio bound is \(1/2\), so the stated RMS ratio limit \(1/\sqrt2\) also follows.

**Numerical count and precision.** Gaussian truncation needs \(B=O(\sqrt{\log(1/\varepsilon)})\). The truncated integrand is bounded and holomorphic in a query-parameter tube of width \(h=\Theta((B+C_0)^{-1})\), at fixed constants. The mapped product ellipses fit inside that tube, and the coefficient bound and summed tail in (25)–(27) are correct. Hence

\[
p=O((\log(1/\varepsilon))^{3/2}),\qquad
(p+1)^2=O((\log(1/\varepsilon))^3).
\]

The explicit compact quadrature, scalar root search, and two-dimensional ODE integrations make the coefficients computable to the requested accuracies. Their effective derivative bounds are available from the stated activation bounds and variational equations. No expectation remains in the retained evaluator. Coefficient errors sum over \((p+1)^2\) terms. Recurrence error \(O(p^2\delta)\) per Chebyshev factor, argument sensitivity \(O(p^2)\), and the finite coefficient sum require only a fixed polynomial loss in \(p\), so \(O(\log(1/\varepsilon)+\log p)\) fractional bits suffice, with the stated data and dimensional guards. The separation \(\tau\ge\tau_0\) controls the square-root sensitivity. Setting \(\varepsilon=1/n\) gives the reported retained bit and arithmetic orders.

## Corrections and qualifications

1. Replace “the tangent feature lower bound ... is \(\gamma=a^2\)” with “the one-sample initial feature Gram is \(\gamma=\mathbb E\phi(G)^2\ge a^2\).” The constant \(a^2\) is a certified lower bound. Along feature time, the training derivative includes the additional nonnegative term \(w_s^2\phi'(z_s)^2\); it is not generally equal to the initial feature Gram.
2. Section 6, step 4 concerns normalized coefficients \(c_{jk}\). Its error conclusion should say that the *resulting prediction error after multiplication by \(y\)* is at most \(y\varepsilon/8\), or that the sum of normalized coefficient errors is at most \(\varepsilon/8\). The displayed clock tolerance is sufficient: the cosine coefficient normalization contributes at most a factor four, so its summed prediction effect is at most \(y\varepsilon/32\). This is a wording/unit correction, not a failed bound.
3. The requested coefficient accuracy must cover quadrature and ODE evaluation jointly; numerical clock approximation and storage rounding must also remain in their separately allocated budgets. The displayed constants leave sufficient slack for this allocation. The setup claim is a polynomial count of the specified quadrature/ODE arithmetic operations at fixed data, with activation evaluation cost additional, exactly as its later caveat says. Effective computability alone would not establish polynomial total bit running time.

No further substantive error was found in these four arguments. This is a successful restricted constructive lemma with the qualifications above. Its endpoint-variance argument and two-coordinate approximation do not settle the general theorem or supply polynomial control of the nondegeneracy constant in a general feature gap.
