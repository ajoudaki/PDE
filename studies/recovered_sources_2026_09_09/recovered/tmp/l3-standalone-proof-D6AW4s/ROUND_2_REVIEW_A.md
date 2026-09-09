# Independent adversarial mathematical referee report

## Verdict: PASS

The full theorem is proved within its stated scope. I found no unresolved mathematical gap, counterexample, circular dependence, unjustified limit exchange, or imported specialized theorem requiring an additional proof. The presentation defects below are nonblocking: they do not leave an obligation of the theorem undischarged.

This verdict covers the particular activation, initialization, learning-rate sequence, observation class, and same-space uniqueness class in Section 1. It does not extend to other activations, arbitrary population initial states, infinite physical time, or operator-norm convergence between different widths.

## Identity, coverage, independence, and sources accessed

- Sole mathematical source: /tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md.
- Requested frozen SHA256: 293b34e5657f48991e8ff922c8e7648bf9400557e97cef1a314bb2af9203d5f1.
- Observed SHA256, both before reading and after the substantive audit: 293b34e5657f48991e8ff922c8e7648bf9400557e97cef1a314bb2af9203d5f1.
- Observed extent: 1,743 lines, 79,677 bytes.
- I read the entire document, lines 1–1743, including every displayed equation, the theorem, all twelve sections, and the final scope assertion. I subsequently reread the conditioning, source-response, singularity, common-space, and relevant notation passages.
- All line references below refer to that exact frozen document.
- Complete mathematical source-access list: the single proof document above. No other project or research file, previous review, audit-status file, conversation, agent report, external mathematical source, or skill file was consulted. No other agent was contacted. No simulations or numerical experiments were performed. Arithmetic checks were analytic checks of the displayed bounds.
- The proof was not edited. This report is the only file written, using apply_patch. The newly generated report was also inspected solely to validate its formatting; it was not used as mathematical evidence.

## 1. Model, normalizations, and elementary tools

**Locations:** Section 1, lines 20–161; Section 2, lines 163–254.

The finite model and backward definitions agree. The deltas exclude the residual; the factor of two comes from the squared loss. With vector variation norm squared equal to the ordinary squared Euclidean norm divided by \(n\), and ordinary Frobenius norm for matrix variations, the predictor gradients are the vector deltas, the matrix blocks \(\delta^{(\ell)}(h^{(\ell-1)})^T/n\), and the top feature vector. The updates, kernel normalizations, and later gradient interpretation therefore match.

The first-coordinate transformation is correct:
\[
F'(z)=10(1+z^2)=1/\phi'(z),\qquad
(F^{-1})'\le1/10,\qquad
\chi'(F(z))=(\phi'(z))^2\le1/100.
\]
The cubic \(F\) is supplied through the root pair \((G,F(G))\), whose fixed moments exist; it is not used as an unrestricted globally Lipschitz instruction. The activation and derivative bounds are valid. The sphere-net probability tends to zero because \(100/8>2\log9\), giving the required common bound for both initial matrices. The small readout has normalized \(L^2\) size \(O_{\mathbb P}(n^{-1})\).

The weak-convergence/second-moment argument supplies uniform square-tail control and finite-dimensional \(\mathcal W_2\) convergence. Continuous quadratic-growth tests are handled using those tails. The product assertion (2.4) has the necessary bounded multiplier and strong \(L^2\) convergence of its other factor. It does not assert false general Fréchet differentiability of nonlinear \(L^2\) maps. The finite-index coupling normalization and the discrete and continuous Gronwall comparisons are correct.

**Result:** discharged.

## 2. Exact conditioning under adaptive Gaussian reuse

**Locations:** Sections 3.1–3.2, lines 272–355, especially (3.1)–(3.4) and lines 316–320.

For nonzero independent \(h\), rowwise Gaussian projection gives (3.1). Applying its transpose to an already known, residual-independent \(u\) gives (3.2). Its Gaussian multiplier is \(\|u\|_2/\sqrt n\). Removing the one-dimensional projection costs only that multiplier squared times \(1/n\) in normalized mean squared norm. The innovation variance is the full second moment of \(u\); subtracting the response variance would be wrong.

I checked the general conditional mean and covariance. Write the first two terms of (3.3) as \(M\). Direct substitution gives \(MV=Y\), and compatibility gives
\[
U^TM=Q^TP_V+Q^TP_{V^\perp}=Q^T.
\]
The homogeneous constraint space consists exactly of matrices satisfying \(AV=0\) and \(A^TU=0\). Its orthogonal projection in entry space is \(A\mapsto P_{U^\perp}AP_{V^\perp}\), and the displayed mean is orthogonal to it. Isotropy of the vectorized Gaussian gives precisely (3.3). Applying this representation to the new input gives (3.4), including the normalization of \(\beta_n\). Interchanging the two sides gives the reverse formula.

Adaptation is handled by conditioning on the complete preceding transcript. The next input is then known. Its answer constrains only one remaining Gaussian matrix by a linear observation. Conditional independence of the other residual matrix is preserved. Coordinate operations and contractions of already observed vectors reveal no additional unobserved matrix randomness. This is the necessary sequential argument; it does not treat an adaptively selected input as independent.

After discarding the finite-rank Gaussian projection, conditional averaging is legitimate because the new scalar Gaussian coordinates are independent given the old transcript. The stated variances for bounded tests, the mean/Gaussian cross term, and the Gaussian-square average vanish at the correct normalized rates. Positive definite limiting Grams justify inverse convergence on this portion of the proof. Joint second-moment convergence supplies subsequent scalar contractions.

**Adversarial checks:** the document neither assumes iid coordinates after reuse nor replaces the transpose by an independent matrix. The single-query division formulas need a clearer local nonzero qualifier, listed below as a presentation issue; the actual zero-query obligation is separately discharged by Section 3.4.

**Result:** discharged in both directions and for interleaved use of both matrices.

## 3. Source-response rule and singular queries

**Locations:** Sections 3.3–3.4, lines 357–457; equations (3.5), (4.5), and (4.6).

The response formula is derived inside the document. For
\(h_\perp=h-\sum_r\alpha_rv_r\), orthogonality eliminates the old forward-input part of each reverse answer:
\[
\mathbb E[q_sh_\perp]=\mathbb E[\zeta_sh_\perp].
\]
Gaussian integration by parts therefore gives
\[
\beta=\mathbb E\nabla_\zeta h-\sum_r\alpha_r\mathbb E\nabla_\zeta v_r.
\]
Substitution into \(Y\alpha+U\beta\) cancels the old response coefficients. The surviving response is exactly \(\sum_su_s\mathbb E\partial_{\zeta_s}h\). The Gaussian part has covariance \(\mathbb E[hv_r]\) with each old forward source and variance \(\mathbb E[h^2]\). These are uncentered second moments. A new innovation is independent of all earlier groups and is combined only with its own group, preserving the asserted independence of distinct source groups.

Freezing deterministic coefficients and covariance parameters during source differentiation is appropriate to that calculation. The complete coordinate expression must still be differentiated through earlier matrix uses. In particular, the current return in (4.6),
\[
b^{(3)}_{kk}\mathbb E[(\phi'(Z^{(2)}_k))^2\tau'_R(q^{(2)}_k)],
\]
is present with the correct gate factors. Omitting it would change the law and undermine the response estimate.

The singular argument does not assume continuity of inverse Grams. A fresh independent \(\epsilon\)-Gaussian input perturbation adds \(\epsilon^2\) to the limiting Schur complement against the earlier same-direction inputs. For each fixed positive \(\epsilon\), the nonsingular argument applies.

The perturbed and unperturbed finite programs use the same matrices and original roots. On the common operator-bound event, a fixed finite number of Lipschitz instructions gives an \(O(\epsilon)\) normalized discrepancy independent of width. No mesh-uniform Gaussian-program estimate is claimed here.

The scalar response recursion also converges as \(\epsilon\to0\). It contains no inverse Gram. At each finite stage the previously constructed coefficients are bounded, so composition of the bounded-derivative maps bounds the next formal derivative. Covariances converge by strong \(L^2\) convergence of earlier expressions. Continuity of finite positive-semidefinite matrix square roots gives Gaussian couplings, and dominated convergence applies to the bounded continuous formal derivatives. The induction therefore remains valid at rank loss.

Formally distinct source slots are retained when their Gaussian values become dependent or zero. The null-space observation is correct: for \(\Gamma=\mathbb E[uu^T]\), a vector \(v\in\ker\Gamma\) satisfies \(u^Tv=0\) almost surely, so a coefficient change in that null space cannot affect the contracted response. The proof does not erase a formal source derivative solely because the source has zero variance.

**Adversarial checks:** zero queries, repeated queries, and limiting rank loss are covered. Neither pseudoinverse continuity nor persistent independent replacement noise is required. The perturbation argument is used only for fixed finite programs.

**Result:** discharged.

## 4. Clipped program and common population action spaces

**Locations:** Section 4, lines 459–590; Section 5, lines 592–647.

The clipped Euler program is explicitly an Euler discretization in the transformed first coordinate. Its rank-one forward and reverse corrections have the correct factors of \(\Delta/n\). The middle clip makes its coordinate map globally Lipschitz at fixed \(R\). The finite-program readout bound permits the stated smooth extension of the top product, preserving both values and derivatives on attained states.

Oracle contractions are selected causally. Restoring empirical feedback uses the displayed bilinear difference estimate, bounded initial operator norms, and convergent oracle second moments through a finite induction. It does not apply a fixed-program theorem to a number of instructions increasing with width. The scalar formulas (4.3)–(4.6) have the correct present-versus-past indexing.

The common-space construction supplies all the necessary additional structure:

1. A countable generating family is closed under the required finite operations and finite unions. Each finite union comes from the same finite initial matrices, giving consistent marginal laws.
2. The coordinate spaces are real Borel spaces. Countability and consistency give a probability measure on each layer's product space. Layers are treated separately, as required by the absence of cross-population neuron-index pairings.
3. Conditional expectations onto finite coordinate sets, truncation, regularity of finite-dimensional Borel probability laws, and the included dense smooth function family give density in each \(L^2\).
4. The finite inequality
   \[
   \|W_0u\|^2/n\le100\|u\|^2/n
   \]
   holds with probability tending to one and passes to deterministic limiting second moments. It gives (5.1). Zero \(L^2\) input difference therefore implies zero output difference. The map is well defined on equivalence classes; finite linear identities establish linearity. Density extends it to all \(L^2\), with norm at most ten.
5. Exact finite transpose pairings pass to limiting moments in the respective populations. Equation (5.2) extends by density, proving that the reverse action is the Hilbert adjoint on the whole space.

Real coefficients and additional Lipschitz probes are obtained by approximation and the operator bound. Bounded approximation and truncation control errors outside compact coordinate sets. The real-step Euler programs consequently live on these fixed spaces. Trained operators retain their accumulated rank-one updates.

**Adversarial checks:** consistency alone would not provide bounded operators or adjoints. The proof supplies density, the norm bound, equivalence-class well-definedness, linearity, and the pairing identity. No operator-norm comparison across widths is invoked.

**Result:** discharged.

## 5. Clipped flows and the quantitative response induction

**Locations:** Section 5, lines 649–757; Section 6, lines 759–945.

The primal bounds (5.5) hold for feature flows and positive-step Euler prefixes. Integrating readout, then top matrix, then middle matrix controls the first backward query without any coordinate supremum estimate. Zero initial readout and \(m<H^{(3)}<a\) give the pointwise reference bound (5.6).

The top-gate stability estimate requires a pointwise bound only on the reference readout. The other readout difference multiplies a bounded gate. The middle clipped gate gives the stated Lipschitz constant proportional to \(R\). Rank-one differences then control the whole vector field. The constrained continuous-path set is complete, the integral map preserves the readout constraint and enlarged primal bounds, and the contraction and Euler estimates apply. Constants are independent of width at fixed clipping.

I checked the response induction and constants:

- Initial backward response rows vanish for the stated reasons, while formal derivatives in degenerate reverse-source directions are retained.
- A single bottom reverse-source derivative enters the accumulated first coordinate with a factor \(\Delta\), giving (6.2) with coefficient less than \(A=3/2\).
- The direct middle forward source contributes one to the entire derivative row sum. The other terms give \(|q^{(2)}_r|/5+V_r/100\), as in (6.3). A single middle reverse-source derivative first contributes at most \(A\Delta/10\), as in (6.4).
- Jensen over time slots and marginal Gaussian exponential moments give the exponent
  \[
  219p/400+3969p^2/1280000.
  \]
  No independence across source times is used. The resulting envelope bounds give (6.6).
- The top derivative coefficient is \(1/100+a/5=73/300\), and its maximal exponent is \(657/800\). Including learned covariance terms gives
  \[
  V_k\le73/80+147/3200=3067/3200<1.
  \]
- This establishes the current top row before the current middle row. It gives \(Q=7/40+7/6=161/120\), and
  \[
  U_k\le3(Q/5+1/100)+SQ^2/100
      =2482563/2880000<9/10.
  \]

The induction is triangular, not circular. The current middle row is not assumed to establish either current bound.

The actual identified middle query is a centered Gaussian source of variance at most \((7/40)^2\) plus a shift bounded by \(7/6\). The exponential-square bound (6.11) follows from the squared-triangle inequality and the scalar Gaussian integral. Independence between that shift and its source is unnecessary.

**Result:** discharged, including uniformity in mesh and clipping.

## 6. Removing clipping, uniqueness, restart, and the finite feature limit

**Locations:** Sections 7–8, lines 947–1076.

The fixed-time Fatou argument transfers the exponential-square bound to each clipped flow. Different almost-everywhere subsequences at different times are harmless: the conclusion bounds each expectation by the same deterministic constant.

Identity (7.2) is exact. Its tail term uses only the reference query; it vanishes below the reference threshold. Consequently (7.3) requires no tail bound for the uncut competitor. The bump \(b_R\) has \(L^2\) size at most \(8e^{-R^2/256}\), which dominates every fixed exponential \(e^{CR}\) and the extra factor \(1+R\) needed for velocity convergence.

The clipped states are Cauchy in the complete continuous-path state space. Evaluation of the actual uncut vector field at the limit, followed by (7.3), gives uniform convergence of velocities. Passing the integral equations is therefore justified without passing an unbounded product through weak convergence.

The asymmetric comparison applies to any bounded-primal integral competitor. Its bounds only change the finite exponential comparison constant. At a reached restart state, the initial discrepancy with the clipped reference already has the required exponentially small form. This proves same-space uniqueness and reached-state restart without an unproved uncut local-Lipschitz assertion.

For finite width, the reference tail measurement is the continuous quadratic-growth function \(b_R^2\). Fixed-clip \(\mathcal W_2\) convergence and time-Lipschitzness of the query give uniform convergence of this measurement. Equation (8.2) restores the prescribed small readout using its normalized \(L^2\) size, without a pointwise bound on it. Width is taken to infinity at fixed clipping before clipping is removed. The separate estimate for \(\delta^{(2)}\) controls that unbounded gated field and then \(q^{(1)}\).

**Result:** discharged.

## 7. Gradient structure and all finite physical horizons

**Locations:** Section 9, lines 1078–1206.

The initial operators are not assumed Hilbert–Schmidt. Their increments are Hilbert–Schmidt because they are integrals of continuous rank-one fields with integrable Hilbert–Schmidt norms. Rank-one difference bounds identify the limits in both Hilbert–Schmidt and operator norms.

The scalar Fréchet derivative is properly justified by (9.2). Splitting a fixed \(L^2\) weight at level \(R\) gives a quadratic remainder on its bounded part and a small linear remainder on its tail. Forward differences are \(O(\|d\theta\|)\). Applying this estimate from the top downward gives (9.3), while mixed changes are quadratic. Formula (2.4) proves gradient continuity. This argument does not need Fréchet differentiability of the coordinatewise activation as a map \(L^2\to L^2\).

The feature flow has raw derivative \(\theta_s=\nabla f\). The Hilbert–Schmidt pairing gives \(f_s=\sum_\ell K^{(\ell)}\), with the announced normalizations. Since \(K^{(4)}\ge25/36\), a unique level-one time satisfies \(s_*\le36/25<3/2\).

The clock comparison has the correct sign. Boundedness of \(f_s\) gives \(1-f(s)\le B_*(s_*-s)\), hence logarithmic divergence of the clock integral. Its inverse exists at every finite physical time and stays below \(s_*\). The physical flow is precisely \(-\nabla(f-1)^2\), and the prediction and loss identities follow.

Raw-coordinate competitors are also covered. Their continuous backward fields and Hilbert–Schmidt increments allow the predictor derivative argument. The positive residual deficit cannot vanish on a finite interval. Coordinate absolute continuity and the scalar chain rule for \(F\) give (9.8); its right-hand side belongs to \(L^2\), proving transformed membership rather than assuming it. Feature-flow and scalar-clock uniqueness identify the competitor, including from every reached state.

**Result:** discharged.

## 8. Exact raw GD and the finite physical comparison

**Locations:** Section 10, lines 1208–1357.

Finite physical GF exists on every finite horizon: the residual identity bounds the residual, and successive integrations bound readout, top matrix, middle matrix, and first-coordinate motion. At each fixed width these prevent finite-dimensional escape. The finite feature clock stays inside the constructed interval on the stated high-probability event. Uniform predictor convergence and the scalar comparison identify its limit.

Raw GD is treated separately. The stopped clock uses positive steps \(\alpha_k=2\eta_n(1-f_{n,k})\). Bounds at good nodes give \(\alpha_k\le C\eta_n\), so the first stopped endpoint is still inside the feature interval and is included in all comparisons.

The cubic identity (10.1) is exact. Its norm estimate uses only \(\|q\|_2/\sqrt n\le C\) and
\[
\|q^2\|_2\le\|q\|_2^2,\qquad \|q^3\|_2\le\|q\|_2^3.
\]
Summation gives \(O(\eta_n\sqrt n+\eta_n^2n)=O(n^{-3/2}+n^{-3})\). No empirical fourth- or sixth-moment convergence is assumed.

Recursion (10.3) combines the asymmetric clipping comparison, the clipped local Euler defect, and that exact raw-coordinate defect. The random feature-time partition is harmless because (10.4) is a pathwise Riemann-sum estimate for a time-Lipschitz function. The stopped predictor comparison is therefore uniform over the actual width-dependent number of GD steps, while Gaussian-program convergence is used only for a fixed reference mesh.

The scalar-clock estimate and the positive population residual margin contradict both stopping conditions at the first bad endpoint, including the final interpolation node. Fractional use of the same cubic identity handles raw interpolation. Comparing GD and GF with the same finite clipped reference at their respective clocks proves (1.7).

The order of choosing clipping, then a fixed mesh, then all sufficiently large widths establishes full-sequence convergence in probability. A Gaussian-program theorem for \(O(n^2)\) instructions is not being assumed.

**Result:** discharged.

## 9. Probes, hidden velocities, integrated speeds, and whole paths

**Locations:** Section 11, lines 1359–1470.

Finite induction handles Lipschitz maps and bounded operator calls. Bounded gates multiplying unbounded backward or velocity fields are handled separately by truncation. Uniform square-tail control follows from the compact limiting \(L^2\) path and uniform \(\mathcal W_2\) convergence, and a later matrix call costs at most its operator norm. The four kernels are products of convergent expectations, not fourth-degree tests incorrectly admitted solely by \(\mathcal W_2\).

The velocity identities (11.1) follow from the product rule and curve chain rule. In particular, the factor \((\phi')^2q^{(1)}\) in the middle-layer equation is correct. The physical multiplier is \(2(1-f)\).

For actual raw GD interpolation, primal bounds control the recomputed hidden derivatives in normalized Euclidean norm. On one step each hidden coordinate changes by at most \(C\eta_n\sqrt n\), and the bounded derivative of the gate gives the same coordinate supremum estimate for its change. In (11.2), matrix and contraction errors are \(O(\eta_n)\), while the gate contribution is \(O(\eta_n\sqrt n)\). Propagation to layer three and feature derivatives gives \(O(n^{-3/2})\). This includes the prescribed terminal-left convention.

Continuous \(L^2\) velocities have measurable versions with finite integrated second moment. Integration and Fubini give absolutely continuous coordinate paths and integrable squared path suprema. Inequality (11.3) controls the entire path interpolation error by mesh size times integrated squared speed. Fixed-grid joint \(\mathcal W_2\) convergence and the triangle inequality then prove the claimed path-space convergence. The argument supplies the control that finite-dimensional marginals alone would lack.

**Result:** discharged.

## 10. Nonlinearity, second-order onset, kernel change, and no later freezing

**Locations:** Section 12, lines 1472–1736.

The initial variances retain full activation second moments, including the constant one. In the first transpose calculation the odd part of \(Z\phi(Z)\phi'(Z)\) has zero Gaussian expectation; the remaining integrand is positive off zero. Thus \(c_3>0\) and \(\sigma_3^2>0\). Independence of the transpose innovation from the middle preactivation yields (12.4).

The second transpose also has the required conditioning: given first-layer roots, the second preactivation, and the independent third matrix, its input is known without observing the second matrix's residual. This gives the positive \(c_2\) and \(\sigma_2^2\). Truncation of its unbounded gated input is justified by the already established joint \(\mathcal W_2\) law and operator bound. The proof does not claim false pointwise positivity of \(z\phi(z)\phi'(z)\) for negative \(z\).

Adjunction gives
\[
\mathbb E[B^{(2)}V^{(2)}]=\gamma_2+\gamma_1,\qquad
\mathbb E[B^{(3)}V^{(3)}]=\Gamma.
\]
All three movement coefficients are nonzero. Strong \(L^2\) continuity, reverse operator continuity, and (2.4) justify \(\delta^{(\ell)}(s)/s\to B^{(\ell)}\), then the derivative and integrated expansions (12.7). The remainder integration is controlled. The output kernel includes lower-layer motion:
\[
K^{(4)}(s)=m_3+\Gamma s^2+o(s^2),\qquad
\sum_\ell K^{(\ell)}(s)=m_3+2\Gamma s^2+o(s^2).
\]
Since \(s(t)=2t+o(t)\), the physical coefficients \(4\Gamma\) and \(8\Gamma\) in (12.8), and the integrated-speed coefficient \(16/3\), are correct.

For later-time nonaffinity, the top correction is uniformly bounded. The middle correction has a dominator depending only on its backward source group and independent of its forward source; independence of the actual correction is not needed. The bottom dominator is independent of the initial root. The constants \(63/160\), \(483/1600\), and \(1561/800\) and their Markov estimates agree with the earlier bounds. The resulting two-sided tails remain positive arbitrarily far out.

The weak-limit passage uses the correct direction for a closed half-line \(F\):
\[
\mu(F)\ge\limsup_j\mu_j(F).
\]
Unbounded support and strict monotonicity of the bounded activation rule out zero affine-regression error. The variance and minimized error are continuous and positive along the \(L^2\) path; each has a positive lower bound on every compact physical interval.

Finally, positive readout and gate give \(\delta^{(3)}\ne0\) at every positive reached feature time. Convergence of its squared norm supplies a positive middle backward-source variance in approximating programs. A bounded response cannot eliminate its unbounded support, proving \(\delta^{(2)}\ne0\). The same argument then proves \(\delta^{(1)}\ne0\). This is a sequential top-to-bottom argument. The positive pairings (12.13) exclude cancellation in the preactivation velocities, and strictly positive gates preserve nonzeroness. The positive physical clock multiplier yields nonzero hidden feature speed at every positive finite physical time.

**Result:** discharged for all nonlinearity and non-laziness claims.

## 11. Dependency and limit-exchange audit

No non-super-classic heavy theorem is imported without proof. The argument does not invoke an external mean-field limit, tensor-program theorem, adaptive random-matrix theorem, or infinite-dimensional continuation theorem.

The foundational facts have their necessary hypotheses:

- Laws of large numbers concern iid roots with the required integrable moments.
- Gaussian projection takes place in finite-dimensional Euclidean entry space. Adaptive use is justified by the transcript induction. Gaussian integration by parts has bounded formal derivatives and integrable roots, and singular covariances are reduced to standard Gaussian coordinates.
- Probability extension uses consistent finite marginals on a countable product of real Borel spaces. Finite-dimensional Borel probability measures have the regularity required for the density argument.
- Covariance square-root continuity uses finite symmetric positive-semidefinite matrices with spectra in a common compact interval and the continuous square-root function, including at zero.
- Completeness, orthogonal projections, Parseval, and bounded-operator extension apply to the stated Hilbert/Banach spaces. The layer \(L^2\) spaces are separable. Rank-one velocities are norm-continuous, legitimizing their operator and Hilbert–Schmidt integrals.
- Dominated convergence, Fatou, and Fubini are used with bounded derivatives, strong \(L^2\) control, nonnegative exponential moments, or integrable squared velocities. Closed-set weak-convergence inequalities have the correct direction.
- Contraction and Gronwall comparisons are proved by geometric or exponential iteration under the displayed hypotheses.

The dangerous limits are kept separate: fixed finite Gaussian programs; width limit at positive input perturbation and removal of perturbation; width at fixed clipping and reference mesh; mesh refinement; clipping removal using Gaussian tails; and a separate stopped comparison for raw GD. Infinite training time is not interchanged with infinite width.

**Unresolved specialized dependencies:** none.

## 12. Presentation defects, separated from mathematical gaps

These are editorial scope or notation issues. They require no new estimate, theorem change, or additional proof.

1. **Nonzero-query scope in the preliminary formulas.** At lines 274–294, (3.1)–(3.2) divide by \(\|h\|_2^2\), and the limiting coefficient divides by \(\mathbb E[H^2]\). Explicitly label this warm-up as the nonzero-input, positive-limiting-second-moment case. The displayed removed-projection expectation is \(1/n\) in that case; generally it is \(\operatorname{rank}(\operatorname{span}(h))/n\). This is not an unresolved zero-query case: Section 3.4 proves that case, and the direct Section 12 applications have features bounded below by \(m\).

2. **Wording of the finite gradient flow.** Lines 68–69 refer to discrete right-hand sides divided by \(\eta_n\). Precisely, the derivatives are the update increments divided by \(\eta_n\); the entire discrete right-hand side also contains the old parameter. Lines 107–108 also refer to “BOTH algorithms in (1.3),” although (1.3) displays GD and the flow is specified in adjacent prose. The later differential equations and Section 10 make the intended meaning unambiguous.

3. **Conditional-law equality notation.** Equations (3.3)–(3.4) use ordinary equality for a conditional Gaussian representation, whereas (3.1) explicitly uses equality in distribution. The surrounding prose states the conditional-law meaning. Consistent notation, with the transcript conditioning displayed, would improve inspectability.

4. **Scope of the generating maps.** Lines 594–600 refer to “the maps in Sections 2 and 4.” Section 2 also defines the non-Lipschitz cubic \(F\). Specify that the closure uses the permitted Lipschitz coordinate maps and includes \(F(G)\) only as the supplied root. Lines 190–193, 510–511, and 600 already establish that intended restriction. Arbitrary later applications of \(F\) are not used to invoke Section 3.

5. **Introduction of feature time.** Section 4's Euler equations omit the physical residual factor, while the “feature-time” description becomes explicit in Section 5 and the clock is constructed in Section 9. A sentence before (4.1) identifying auxiliary time \(s\) and the unit gradient-ascent field would improve first-pass readability. The actual equations and clock are consistent.

## Final determination

**PASS.** Every obligation of the full theorem is discharged by the frozen document with the allowed foundational facts. No mathematical repair remains. The five presentation items above do not constitute mathematical gaps.
