# Internal adversarial check of RESULT.md

This is an internal check after an independent route was frozen. It is not a blind independent promotion review and does not authorize promotion. The checker read the complete candidate and its own independent route, with the required mathematical and conjecture-audit skills. No other study, experiment, maintained scientific source, or external paper was read for this check. External citation attribution was therefore not independently verified; the mathematical arguments supplied in the candidate were checked directly.

Candidate: `studies/input_geometry_response_fields_20260930/RESULT.md`

SHA256 of the final checked candidate:

`44c94275d490c119d0c85c155cd16b9924f260cc1f2c79c238f03b9d7abfb3d0`

Read provenance: the entire original candidate was read at SHA256 `79437c3d291403de1e4234e9f3a6cc2c0c69587c14ba94b83993f30b391a490e`. The revised introduction and complete Sections 3, 6, and 8 were then checked at `73f2a8dde68df8e55ee7551d2029bee3a7cde52a7785068d17fb9398d0fdb679`; the complete final Sections 6 and 7 and the added integer-order clause were checked at the final hash above. The supervisor identified these as the complete intervening substantive changes. The check of Section 7 covers its stated comparison and scope, not the proof of the new cross-reference to `FIELD_ROUTE.md`, which was outside this check's assigned inputs.

## Verdict

**Internal mathematical PASS for the stated fixed-width, finite-horizon approximation theorem and the exact polynomial-data reduction.** No contradiction or missing mathematical bridge was found in the sample-uniform temporal estimate, its combination with analytic cubature, or the exact polynomial example. The result constitutes a meaningful data-count-independent approximation statement within that scope. It does not establish width-uniformity or all-time accuracy for tanh, favorable preprocessing conditioning, or a generic effective continuum-cubature algorithm under a second-moment assumption alone.

All four presentation objections below have been resolved in the final checked candidate. The continuum-access and finite-precision limitations remain substantive limits of the result and should be preserved when it is summarized. They do not invalidate existence of a finite autonomous ODE with the asserted error, or the constructive empirical-data algorithm supplied.

## 1. Objections and precise fixes

### A. Continuum existence is stronger than a mere closure statement, but weaker than a general effective construction

**Classification: implementation-scope qualification; not a mathematical counterexample.**

The proof establishes that an integrable feature vector has an exact finite positive moment representation. Its supporting-hyperplane reduction and convex-combination argument do not, by themselves, give a numerical algorithm that selects the nodes and weights from an arbitrary abstract probability law. A second-moment bound alone cannot make that law effectively accessible.

The original Section 3 acknowledged the need for “integration/selection access.” The final version explicitly requires certified moments and a supplied or computable positive cubature and states that integrability alone does not give a node-selection algorithm. Thus this objection is resolved. Retain that qualification in any interpretation: for every continuum law the theorem gives a finite autonomous witness; an effective continuum implementation additionally requires a specified method to compute or approximate the finite moments and find a corresponding positive representation. This source-data access is entirely different from a forbidden trajectory oracle, but it is still a real input-access assumption.

**Suggested sentence:** “For empirical data the summary is constructed by finite elimination; for a continuum law the finite witness exists, and an effective implementation additionally requires computable moment and positive-cubature access, or an explicitly bounded approximation to them.”

No empirical implementation or floating-point validation is established by the current mathematical construction. The candidate correctly says this in Section 9.

### B. Arithmetic state counts do not bound numerical precision

**Classification: material numerical limitation already partly disclosed; no failure of the stated arithmetic bounds.**

The mathematical constants avoid minimum atom weights and maximum individual labels. Nevertheless, exact cubature can retain extremely small weights paired with very large labels. Exact arithmetic stores these quantities as scalars, while a practical representation may require substantial precision. Individual unweighted memory coordinates may also be large when an atom has small weight, even though every weighted norm used in the proof stays bounded.

The final Section 6 now explicitly distinguishes arithmetic and real-coordinate counts from bit complexity and preprocessing conditioning. It also adds the exact square-root-weight representation checked in Section 6 below; that representation avoids large runtime label coefficients and reciprocal weights. Thus the presentation objection is resolved. Do not promote the result to a numerical-conditioning bound for the cubature construction. A certified finite-precision implementation still needs moment residual bounds and ODE-error control. No such extra result is required for the continuous-time theorem as currently scoped.

**Suggested sentence:** “These are arithmetic and state-dimension counts; they do not bound bit precision or conditioning uniformly over arbitrarily small atom weights.”

### C. Specify the approximation orders explicitly

**Classification: minor precision.**

The Legendre tail bound and the rate require `q` to be a positive integer, while `p` can be a nonnegative integer. The final introduction now states this explicitly; this objection is resolved.

**Fix:** state `q ∈ {1,2,…}` and `p ∈ {0,1,…}` near the headline result.

### D. Polynomial pairings need “at most,” not “precisely”

**Classification: minor wording.**

Section 8 correctly derives upper bounds on input degree. The original word “precisely” could falsely suggest that every architecture or parameter choice attains the maximal degree. Cancellations, zero weights, lower-degree activations, and degenerate parameterizations can reduce the required degree. The final candidate uses “at most” and specifies `b≥1`; this objection is resolved.

**Fix:** use “require moments of degree at most 2D_* and D_*.” State that the common polynomial degree `b` is a positive integer if the displayed geometric degree formulas are used without a separate constant-activation convention.

## 2. Positive cubature and continuum support

Let `J=(p+1)^s`. The feature map has `2J+1` coordinates: `ψ`, `yψ`, and `y²`. Since one coordinate is constantly one, its affine dimension is at most `2J`. Thus a convex-combination reduction to at most `2J+1` atoms is correct. There is no missing extra atom from the final `y²` statistic.

The noncompact-label proof is valid under the given second-moment hypothesis. Each `ψ_i` is bounded on the cube, so `ψ_i`, `yψ_i`, and `y²` are integrable. An expectation belongs to the closed convex hull of any full-measure feature range by separation. If it lies on a proper supporting hyperplane, the nonnegative slack has zero expectation and hence vanishes almost surely. Finite repetition reduces affine dimension. In the remaining affine hull, a relative-interior point of the closed convex hull lies in the convex hull: choose a small surrounding simplex in the relative interior, approximate its vertices by points in the convex hull, and preserve containment of the point under sufficiently small perturbations. Expanding those convex-hull vertices produces a finite combination of actual feature values.

The resulting points may be chosen in any preselected full-measure subset on which the map is defined, intersected with the support. The cube times the real line is a usual Euclidean measurable space, so its probability law has a full-measure support. There is no hidden compact-support assumption on labels.

The elimination algorithm preserves positivity and every retained feature: the constant row forces a nonzero null vector to have both signs, and the prescribed step removes at least one positive coefficient without making another negative. Keeping at most `2J+2` columns before elimination is sufficient. The `O(mJ³)` arithmetic work and `O(J²+Jd)` storage claims are conservative under the stated fixed structural dimensions.

## 3. Analytic approximation and the parameter region

The canonical energy identity is correct for the block mobility `D` with norm `n`:

\[
\frac{d\mathcal L}{dt}=-\dot\theta^TD^{-1}\dot\theta,
\qquad
\int_0^T\|\dot\theta\|^2dt\le n\mathcal L(0).
\]

Both original and cubature losses initially have square root at most `F₀+Y`, because the cubature preserves the label second moment. Cauchy–Schwarz therefore puts both dense flows in the displayed parameter ball. The same finite-energy estimate makes a putative finite-time trajectory Cauchy at its endpoint, so local existence extends it. This closes the finite-time-escape loophole.

For real parameters in a compact ball, real tanh preactivations form compact sets away from the complex poles. A finite layer-by-layer continuity argument provides a common complex neighborhood of the real input cube for every parameter in the ball. Shrinking it supplies a common closed product Bernstein ellipse and uniform bounds for the differentiated expressions. Thus the analytic radius need not be assumed from the initial snapshot, and it is independent of the number of examples or cubature atoms. Its possible deterioration with width, depth, horizon, and initialization is correctly retained in the constants.

The tensor Chebyshev tail bound (11) has the correct geometric factor. The coefficient estimate is `2^s M b^{-|α|₁}`; a union bound over the coordinate whose index exceeds `p` gives

\[
\sum_{\exists j:\alpha_j>p}b^{-|\alpha|_1}
\le s\,b^{-(p+1)}(1-b^{-1})^{-s}.
\]

Using vector norms in the contour-integral estimate is legitimate. It is unnecessary to introduce a dimension factor for each parameter coordinate; the bounded vector norm already carries the permitted width dependence.

Both unlabeled measures have mass one and both signed label measures have total variation at most `Y`. Polynomial moment matching therefore gives exactly the factor `4n(1+Y)` in (12). The Hessian calculation in (13) is also correct. It controls feedback uniformly over the entire parameter ball, rather than only on the reference trajectory. Consequently (14) is a valid whole-trajectory estimate.

The temporal closure need not stay in this particular dense-flow ball. Its separate bounds in Section 5 provide another fixed compact region; taking a containing ball is enough for the final predictor Lipschitz estimate. This does not introduce `p`, `q`, or `K` dependence.

## 4. Detailed check of the temporal theorem

### Moment representation and reconstruction

The triangular moment equations agree with unnormalized shifted-Legendre moments on `[0,τ]`. The constant forward prefix on `[0,1]` has zeroth moment equal to the initial activation and every higher moment zero. The zero backward prefix has every moment zero. The prefactor `(2k+1)/τ` in (16) is therefore the correct projection normalization.

The label-affine identity `B=A−yC` is exact because all three equations use the same scalar damping coefficients and zero backward initialization. It does not assume smooth labels. The actual finite-node implementation stores `B`, not separate `A,C`, so the memory count of two families is consistent with the three-field interpretation in Section 2.

### Uniform physical bounds

The readout obeys `dot w=−2 E[rh]`. Since `wᵀh=nf`,

\[
\frac{d}{dt}\|w\|^2
=-4n\mathbb E[(f-y)f]
=n\mathbb Ey^2-4n\mathbb E(f-y/2)^2.
\]

This remains true for the closure, because the readout evolves by its canonical equation even though the internal matrices have a defect. It supplies the stated `B_w`, residual bound, and upper bound `A₀` on the clock.

If `||δ_ℓ||≤β_ℓ`, then, at every positive-residual time,

\[
\mathbb E_j\|b_j\|^2
=\mathbb E_j\frac{r_j^2\|\delta_j\|^2}{\rho^2}
\le\beta_\ell^2.
\]

Projection contraction and data/time Cauchy–Schwarz give the internal matrix bound in (18). The top-down induction is not circular: bound the readout, then `δ_L`, then `W_L`, then `δ_(L−1)`, continuing downward. The first matrix has a direct integral bound once `β₁` is available. Every physical bound is independent of `q,K`, and individual atom weights. Individual memory coordinates are bounded for every fixed finite weighted problem, which suffices for its continuation; they need not obey a weight-independent unweighted bound.

### Endpoint residual identity and its sign

At fixed history coordinate, actual past values remain fixed, while the differentiated projected history stays a polynomial of degree below `q`. Orthogonality therefore eliminates its interior pairing with the residual. Differentiating the growing integral gives exactly

\[
\dot D_u=\rho\|u(\tau)-(\Pi_qu)(\tau)\|^2.
\]

The same argument for a cross residual gives its derivative as `ρ(b−b*)(h−h*)ᵀ`. Moreover,

\[
\int bh^T-\int(\Pi_qb)(\Pi_qh)^T
=\int(b-\Pi_qb)(h-\Pi_qh)^T.
\]

The reconstructed update is minus `2/n` times the projected pairing; its own exact gradient accumulator is minus `2/n` times the unprojected pairing. Reconstruction minus accumulator is consequently **plus** `2/n` times the cross residual. This verifies the sign, matrix ordering, and product structure of (20). Equation (21) then follows by Cauchy–Schwarz in time and the probability-weighted data index.

### The cancellation that removes `q` from the depth bound

The endpoint norm on polynomials of degree below `q` is `q/√τ` because `Σ_(k<q)(2k+1)=q²`. Since the backward history is zero on the prefix,

\[
\mathbb E\|b^*\|^2
\le\frac{q^2}{\tau}\mathbb E\int_0^\tau\|b\|^2
\le q^2\beta_\ell^2.
\]

The triangle inequality in the weighted data `L²` norm yields `E||b−b*||²≤(q+1)²β_ℓ²`; no factor `K` or reciprocal atom weight enters.

The Legendre spectral bound (22) has the correct factor `τ²/[4q(q+1)]`. It only needs the forward history to be absolutely continuous with square-integrable clock derivative. No backward-history derivative estimate is used or silently assumed.

Combining the preceding inequalities gives

\[
\begin{aligned}
\int_0^T\rho\|E_\ell/\rho\|_F^2dt
&\le\frac{4(q+1)^2\beta_\ell^2}{n^2}
\mathbb E D_{h,\ell-1}(T)\\
&\le\frac{\beta_\ell^2A_0^2}{n^2}
\frac{q+1}{q}Z_{\ell-1}
\le\frac{2\beta_\ell^2A_0^2}{n^2}Z_{\ell-1}.
\end{aligned}
\]

This confirms (23), including its constant and the absence of `K`. The first-layer estimate is `Z₁≤S(v₁X)²`. Applying the three-term squared-norm bound to the later forward derivatives gives (24) exactly. Induction over depth therefore bounds every needed `Z_ℓ` independently of `q`.

Finally `E D_b≤Sβ_ℓ²` and (22) inserted in (21) give a total physical defect of order `1/√[q(q+1)]`. The canonical vector field is Lipschitz on the common physical parameter region with label dependence controlled by `E|y|≤Y`. Its comparison with the perturbed flow thus gives (17) without a hidden `K` constant.

### Zero residual and local uniqueness

For every fixed finite positive-weight problem, the displayed closure RHS is locally Lipschitz on `τ>0`: the residual RMS is a finite weighted Euclidean norm and no denominator contains `ρ`. If `ρ=0`, positivity of the weights implies all residuals vanish. Every memory derivative, the clock derivative, and the first/readout derivatives then vanish, so the entire autonomous state is an equilibrium.

A nonstationary locally unique solution cannot reach that equilibrium at a finite regular time, by uniqueness of the reversed autonomous ODE from that point. Thus a nonstationary solution has positive `ρ` throughout every finite interval under consideration. The clock-coordinate manipulations are justified there; the stationary case is separate and exact. No unjustified division by zero remains.

## 5. Polynomial example

For common polynomial activation degree `b≥1`, the hidden activation at depth `ℓ` has input degree at most `b^ℓ`. Backpropagation contains derivative factors from layers `ℓ` through `L`, giving total degree

\[
\sum_{j=\ell}^L(b-1)b^{j-1}=b^L-b^{\ell-1}.
\]

This verifies the candidate's degree for `δ_ℓ`. Multiplication by the output adds at most `D_*=b^L`, giving degree at most `2D_*−b^(ℓ−1)` for the `A_ℓ` drive; `C_ℓ` has degree at most `D_*−b^(ℓ−1)`. Shared scalar damping and time integration do not increase input degree. Pairing with `H_(ℓ−1)`, of degree at most `b^(ℓ−1)`, needs at most degrees `2D_*` and `D_*`, respectively.

The residual clock uses the same moments through the loss identity, plus `Ey²`. Therefore matched moments determine the entire polynomial coefficient closure, not merely the dense gradient field at one time. The equality of the order-`q` closures on their common existence interval is justified. The final wording avoids overstating the degree bounds as necessary in every instance.

The revised count is also correct: there are `binom(s+2b^L,s)` unlabeled monomials, `binom(s+b^L,s)` label-weighted monomials, and the one `y²` statistic. The constant coordinate reduces affine dimension by one, giving at most the displayed sum plus one atoms. This one cubature works simultaneously for every width, initialization, and finite order `q`, because those choices change coefficient values but not the necessary input degrees. Polynomial canonical gradient flows exist globally by the same nonnegative-loss energy argument and local smoothness, so the exact dense-data reduction is valid for all time. This does not assert global existence of polynomial temporal closures or width-uniform compression of their learned matrices.

## 6. State, cost, observables, and scope

The two moment families for `L−1` internal matrices give `2(L−1)nqK` evolving coordinates. First-layer weights, readout, and clock add `nd+n+1`. Static initialized dense matrices remain present and are applied exactly. The stated RHS cost accounts for their dense applications, the low-rank learned updates acting on all `K` response vectors, and prefix-sum moment updates. No omitted `q²` cost is required for the triangular operator.

The predictor at an unseen input is evaluated from the current reconstructed weights; no new history is necessary for that point. Thus the uniform prediction observable in (1) matches the represented state. The RMSE comparison follows from the reverse triangle inequality and does not claim statistical generalization.

The final square-root-weight runtime formulation is algebraically exact. Setting `γ_j=√a_j`, `β_j=γ_j y_j`, `U=γH`, `V=γB`, and `e_j=γ_jf_j−β_j=γ_jr_j` gives `ρ²=Σe_j²`, backward drive `e_jδ_j`, forward drive `γ_jρh_j`, and pairing `VUᵀ=a_jBHᵀ`. The first-layer and readout drives use `γ_je_j=a_jr_j`, as required by their canonical weighted equations. Also `Σβ_j²=Σa_jy_j²≤Y²`, so every stored label coefficient is bounded by `Y`. No selected raw label or reciprocal atom weight is needed at runtime. The state dimension is unchanged. This removes the specific large-label/tiny-denominator runtime problem without making a new claim about preprocessing conditioning.

The proof combines two separate comparisons: original dense flow versus cubature dense flow, then cubature dense flow versus cubature temporal closure. It does **not** require the normalized backward field `rδ/ρ` to have a uniform analytic input radius or smooth labels. This separation avoids a potentially serious false implication that could otherwise have entered a direct field-quadrature proof.

The theorem allows `K` and `q` to grow with accuracy and horizon. It does not assert exact finite closure for tanh, fixed complexity for all accuracies, or uniformity in width. Its low-rank learned matrices are consequences of the chosen approximation, rather than hypotheses about the exact learned matrices. The candidate states these distinctions adequately.

## Closing assessment

The final checked candidate supplies both a small source-error estimate and an error-propagation argument for each approximation axis. In particular, the sample-uniform temporal theorem closes the potentially decisive gap between data moment compression and a small autonomous response-memory state. The exact polynomial-data reduction supplies a separate, stronger statement in its own architecture class. With the final candidate's explicit continuum-access and numerical-precision qualifications, these stated mathematical results survive this internal adversarial check.
