# Independent audit of the cavity expansion

Reviewed frozen input: `/tmp/mfp_cavity_review_20261011/MFP_CAVITY_PROOF.md`, revision c2, complete lines 1–566. The substantive audit is of Sections 2–4 and the one/two-site reconstruction in Section 6. I also read the prescribed mathematical presentation skills and neural reference, `docs/notation.qmd`, and the relevant established primitive-program, source-response, and raw-moment passages in `docs/02-gaussian-reuse.qmd` (within lines 252–580). I did not read the linked referee report, blueprint, study histories, or another reviewer's findings. This report does not certify Section 5's source-response identification or the derivative compilation in Section 7.

**Finding:** the raw-moment estimate, external-history expansion, dependent-history substitution, scalar estimates, Gaussian quadratic-form step, and one/two-site reconstruction are sound within the stated finite smooth Gaussian grammar. I found one literally false independence sentence, at lines 169–170, whose correction does not affect the proof: the cavity is a function only of retained initialization, but is generally statistically dependent on the actual external histories. The estimates correctly avoid requiring that false independence.

## 1. Raw moments and old-cavity Jacobians

The simultaneous induction over instruction number, all finite moment orders, and all fixed raw-entry derivative orders is well founded (lines 72–112). At a matrix node, derivatives on the linear matrix factor create at most \(k\) earlier-node derivatives. For an even moment \(m\), fix an index pattern with \(b\) distinct labels, \(s\) of which occur once. The nonsingleton product \(M_0\) does not contain the singleton raw coordinates. Consequently repeated Gaussian integration by parts gives exactly

\[
\mathbb E\!\left[\left(\prod_{u\in S}w_u\right)M_0Z\right]
=\left(\prod_{u\in S}\operatorname{Var}(w_u)\right)
\mathbb E[M_0\partial_SZ].
\]

All reuse dependence belongs to \(Z\), so no factorization of weights from the input is used. The earlier-node induction controls \(\partial_SZ\), including the extra derivative orders created by integration by parts. Its product-rule expansion has a number of terms depending on \(m,k\), not \(n\). Thus the absolute contribution is at most

\[
C n^{-s}n^{-(m-s)/2}=C n^{-(m+s)/2}\le Cn^{-b},
\]

because \(m\ge 2b-s\). Summing at most \(n^b\) labelings per fixed pattern closes the induction. Singular root covariances and zero matrix-entry variances do not disturb this calculation. Fixed-width polynomial growth supplies the necessary integrability before the uniform estimate. This supports (M), lines 114–122.

The matrix norm bound in lines 124–132 is adequate. The displayed two-net tail, integrated above a fixed sufficiently large threshold, gives moments bounded uniformly in width. The notation \(O_*(n^a)\) deliberately allows arbitrarily small exponent losses. Uniform coordinate moments of every order imply that the maximum of \(O(n)\) polynomial derivative coefficients is \(O_*(1)\), as asserted in lines 134–140.

The weighted norm in lines 172–192 is correctly normalized. A scalar perturbation has norm \(\sqrt n|\delta s|\); broadcasting it through a coefficient vector \(a\) has operator norm \(\|a\|_2/\sqrt n\). A normalized average has the same weighted operator bound in the reverse direction. Finite composition therefore yields retained-initialization-measurable matrices \(A\) with \(\|A\|_{\rm op}=O_*(1)\), scalar response columns \(B\) with \(\|B\|_2=O_*(\sqrt n)\), and scalar response rows with Euclidean norm \(O_*(n^{-1/2})\). These estimates require no empirical law.

## 2. Exact external histories and the Taylor remainder

Deleting one or two neurons of a single type is essential (lines 144–163). Distinct matrix endpoint types mean a named matrix loses rows or columns, never an intersecting corner block. Every omitted port is therefore an independent \(N(0,I/n)\) vector, independent of the retained initialization. At an action away from the deleted type, the exact missing summand is \(g_{W,i}x_{q,i}\); at a deleted-type average it is \(\beta_b/n\). Substitution of the actual histories is an exact chronological identity even though those histories are themselves functions of the omitted ports.

The first variation (L), lines 182–208, is a finite decomposition into old-cavity responses with the actual \(x,\beta\) substituted after differentiation. For a retained-initialization-measurable \(A\), conditioning gives coordinate variance at most \(\|A\|_{\rm op}^2/n\) for \(Ag\). A high fixed moment and a union bound over \(O(n)\) coordinates give

\[
\|Ag\|_\infty=O_*(n^{-1/2}),\qquad
\|Ag\|_2=O_*(1).
\]

A scalar response row \(a\) has \(\|a\|_2=O_*(n^{-1/2})\), so \(a g=O_*(n^{-1})\). Scalar injections contribute a vector norm at most \(O_*(n^{-1/2})\), hence also that bound for their coordinate maximum. Multiplying these finitely many basis responses by the actual \(x,\beta\) preserves all the stated exponents by Hölder and their all-order moment bounds. This justifies (LB) without claiming that the substituted first variation is Gaussian.

For the nonlinear remainder, the induction at lines 210–239 closes with exactly the advertised rates. Assuming the parent remainder bounds, \(\Delta u=L_u+R_u\) satisfies

\[
\|\Delta u\|_2=O_*(1),\quad
\|\Delta u\|_\infty=O_*(n^{-1/2}),\quad
|\Delta s|=O_*(n^{-1}).
\]

All second derivatives on each coordinatewise segment between the actual and cavity parent arguments have an \(O_*(1)\) cap: every point on such a segment is bounded by the two endpoint magnitudes, both already covered by (M). The vector Taylor remainder is bounded by the displayed product in lines 222–223 and is therefore \(O_*(n^{-1/2})\) in Euclidean norm. For an average, multiplying by \(\sqrt n\) gives the bound in lines 228–229, again \(O_*(n^{-1/2})\). The old linear derivative propagates earlier remainders with weighted norm \(O_*(1)\). At matrix and average instructions the external forcing cancels exactly against its first variation. Roots have zero remainder. This proves (R).

In particular, this is not a global controlled-trajectory Taylor argument with an unproved moment estimate along an artificial trajectory. It uses local Taylor formulas between actual and cavity parent values. Dependence of the substituted histories creates no missing derivative term, because they are external parameters of the retained execution being expanded.

## 3. Quadratic forms, scalar feedback, and two probes

In lines 243–275 the reconstructed deleted output has two error terms bounded by

\[
\frac{|\beta_b|}{n}\|g\|_2\|B_{h_r,b}\|_2=O_*(n^{-1/2}),\qquad
\|g\|_2\|R_{h_r}\|_2=O_*(n^{-1/2}).
\]

No independence is needed for these estimates. Conditional on retained initialization, the remaining quadratic forms have mean \(\operatorname{tr}(A)/n\) in the same-port case and zero in the independent-port case. Their variance is at most \(2\|A\|_F^2/n^2\le 2\|A\|_{\rm op}^2/n\), or the analogous independent bilinear-form bound. Choosing an exponent loss smaller than \(1/2\) makes their unconditional second moments vanish. The actual coefficients \(x\) are tight, so multiplying by them preserves convergence in probability even when they depend on the quadratic forms. Thus (C) follows.

The same omitted Gaussian port occurs precisely for the same deleted site and the opposite orientation of the same named matrix (lines 268–285). Cross-site terms vanish by the independent-port calculation. Conditional on retained initialization, all source variables are linear functions of the omitted Gaussian ports with deterministic coefficients \(h_r^0\). Their covariance is exactly \(\langle h_r^0,h_t^0\rangle/n\), and the lists for two deleted sites are conditionally independent. They are also independent of the deleted root tuples. These are conditional statements; shared random retained covariances may create finite-width unconditional dependence.

The scalar-feedback observation at lines 288–294 is valid. Expand a physical Jacobian into the finitely many instruction-level paths. Every path traversing a scalar node factors through a one-dimensional space and therefore has rank at most one. Its operator norm between vector endpoints is \(O_*(1)\) under the weighted norms. Its trace divided by \(n\) is consequently \(O_*(1/n)\). The sum contains finitely many paths because graph size is fixed. Scalar values still remain in the coefficients.

Assuming the deterministic trace limits supplied separately by Section 5, the one/two-site reconstruction in lines 386–428 is complete. The earlier-stage theorem supplies deterministic limits for cavity Grams and all preceding scalar values. The conditional Gaussian characteristic function then converges to that of one source list, or two independent source lists, including joint convergence with deleted roots. Slutsky and chronological continuous substitution into (C) give one-site convergence and two-site convergence to independent copies. Uniform moments ensure uniform integrability for continuous polynomial-growth tests and their pairwise products. Exchangeability then gives the variance identity in lines 420–423; higher moment bounds upgrade the resulting \(L^2\) empirical convergence to every finite \(L^p\). No quantitative propagation-of-chaos assumption or covariance inverse is hidden here.

## 4. Required wording correction

Lines 169–170 say the zero-injection cavity is “independent of both g and these external values.” Statistical independence from the actual histories is false in an admitted program. Let \(u\in\mathbb R^n_\sigma\) have iid standard Gaussian coordinates, let \(W:\tau\to\sigma\), form \(y=W^Tu\), and then form \(Wy\). Delete coordinate \(i\) of type \(\tau\). The history used in the second action is \(x=y_i=g^Tu\); the cavity contains \(u\). But

\[
\mathbb E[x^2\mid u]=\|u\|_2^2/n,
\]

which is nonconstant. Thus \(x\) is statistically dependent on the cavity initialization.

Replace that sentence with: “Setting all additive injections to zero gives the old cavity, which is measurable with respect to the retained initialization, independent of the omitted Gaussian ports, and does not use the external parameters.” This preserves precisely the properties used later. Lines 200–208 and 264–266 already handle history dependence correctly, so this is a repairable statement of dependence, not a failure of the cavity argument or a counterexample to the theorem.
