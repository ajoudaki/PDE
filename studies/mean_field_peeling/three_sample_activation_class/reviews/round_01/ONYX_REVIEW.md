# Independent mathematical review

**Verdict: PASS.** I found no remaining mathematical correctness or proof-completeness objection in the supplied manuscript. The verdict applies to the precise statements and quantifiers in this version, including its fixed-function, fixed-dataset, compact-time convergence assertions.

## Input, reading coverage, and isolation

- Sole reading input: `/tmp/report-a18efe65b35a/REPORT.md`.
- Input size: 3,826 lines; 223,246 bytes.
- SHA256, checked before reading and again after the complete reading: `ad30e1e3ed36db9d1f36220859e3d40916aab4b26f892e478ccb850c9dbc7cd5`.
- Complete reading coverage, in bounded, nontruncated chunks: lines 1–260, 261–520, 521–780, 781–1040, 1041–1300, 1301–1560, 1561–1820, 1821–2080, 2081–2340, 2341–2600, 2601–2860, 2861–3120, 3121–3380, 3381–3640, and 3641–3826. These intervals cover the entire manuscript without a gap.
- I read no other files, including skills, project instructions, authoring notes, other manuscripts, or other reviews. I used no web sources, conversation-history retrieval, other agents, or numerical experiments. The manuscript was not modified. This review is my sole file output.

## Objections

None.

## Required repairs

None.

## Mathematical audit

### 1. Model, metric, and theorem quantifiers — Part M

The finite forward/backward normalization and all four physical gradient factors agree with the raw metric in (M.6). In particular, the first weight block has the factor (1/d), the two square matrix blocks have (1/n), and the readout update has no remaining (1/n). The population Hilbert–Schmidt rank-one convention reproduces the finite Frobenius metric.

The finite GF continuation argument is valid: the gradient identity bounds integrated squared raw speed; Cauchy–Schwarz makes the path Cauchy at a finite endpoint; finite-dimensional local existence then continues it. The claim about GD is only that its finite iterates are defined, with the later estimates supplying the requisite finite-horizon bounds. No general infinite-time GD boundedness is asserted.

The theorem distinguishes the three neuron probability spaces, fixed same-layer probe laws, and raw parameter comparisons on identified spaces. It does not require cross-width operator convergence. Its activation parameters depend on separation and the selected perturbation function, while convergence constants may depend on the fixed data and horizon. Neither uniform convergence in an infinite function class nor an exchange of infinite time and infinite width is asserted.

### 2. Finite Gaussian programs and canonical actions — Part F

The adaptive conditioning argument conditions successively on each revealed answer. This justifies the conditional product structure of the remaining Gaussian matrix factors despite adaptive inputs. Formula (F.6) is the Gaussian orthogonal projection onto the affine matrix constraint space: its compatibility relation, particular solution, and homogeneous two-sided projection are correct. The normalized variance and projection-error factors in (F.7)–(F.8) are consistent.

The source-response derivation retains all previous opposite-orientation inputs and unrolls derivatives through other previously computed calls. The cancellation in (F.11)–(F.12) gives the displayed signed response coefficient. Independence is asserted for the oriented source groups, not for the actual forward and transpose answers. The input second moments, including nonzero means, are used as source covariances.

Singular queries are treated by independent perturbations of query inputs. At fixed perturbation size, every new same-orientation query has a strictly positive limiting innovation norm. The finite-program error estimate uses bounded matrix norms and Lipschitz instructions, while the scalar passage uses covariance square-root continuity and bounded formal derivatives. This avoids a rank-stability premise or continuity of Gram pseudoinverses. The subsequent singular-support invariance argument concerns contracted response corrections and does not incorrectly claim uniqueness of individual derivative coefficients.

The countable-language construction supplies dense generated subspaces. Finite operator inequalities and finite adjunction identities pass to those subspaces and extend by completion. Thus the initialized reverse actions are actual Hilbert adjoints. The argument does not replace the specified Gaussian initialization by arbitrary bounded operators.

The distinction between a strong curve chain rule and Fréchet differentiability of an (L^2)-valued activation map is maintained. The weighted scalar Taylor estimate (F.41), followed by top-down adjunction, establishes the scalar predictor's continuously Fréchet differentiable raw gradient. Its assumptions use only the stated bounded first and second activation derivatives. The fixed-cap local flow and Euler results use genuinely Lipschitz capped gates on bounded primal sets.

### 3. Response bounds and chronological closure — Part R

The raw controlled Euler updates, learned rank terms, and response coefficients in (R.10)–(R.16) have consistent signs, controls, and sample positions. Forward rows use strictly past reverse inputs, while reverse rows include available current forward sources. The construction order in (R.17) is sufficient for the formulas.

The affine Gaussian-probe argument establishes formal derivative row bounds without exchanging a derivative with the width limit. The same inserted Gaussian root can test an arbitrary deterministic signed row. Taking width first and probe amplitude second, with deterministic coefficient continuity, yields the row estimate. A single past insertion retains its actual step length (h_j); no lower bound on mesh ratios is used. The comparison also avoids equating an absolute expected derivative with the expectation of an absolute derivative.

The nonlinear raw comparison in R.4 uses the affine field's Lipschitz bound and a same-state perturbation estimate. It supplies query norms, source variances, and learned-moment differences before response bounds are assumed. Consequently the source-variance estimate is not circular. The displayed coefficients in the forward and backward perturbation bounds are sufficient under (age1), (b=2Bge2).

On a bounded coefficient prefix, R.5 establishes (L^p) bounds by Minkowski and deterministic discrete Gronwall. It uses a maximum of deterministic time-indexed norms, not an unjustified moment bound on a random time supremum. R.6 controls the formal derivative equations with the actual (psi''	au_R(q)) term and includes the current incoming multiplier absent from the past-time exponential envelope. Convexity in time, rather than independence across times, justifies (R.55)–(R.58).

The same-array affine derivative comparison is kept distinct from comparison with the actual affine baseline. Equations (R.69)–(R.87) then propagate coefficient discrepancies using completed past rows or already constructed current rows. In particular, the construction of (B^2_k) uses the newly bounded (B^3_k), and the current terms (R.93)–(R.94) are retained. I find no implicit current-row inversion or omitted derivative path in this closure.

The constant chain ending in (R.90) is finite and depends only on ((a,B,S)). All divisors are strictly positive. Its threshold is selected before the mesh, cap, controls, or input covariance. The product estimate (R.92) closes the prefix induction with strict slack.

### 4. Geometry, generalized activations, and global bounds — Part G

The geometric bound (G.1) is valid for the one-sided separation condition, including singular input Grams. For mixed-sign coefficients, the displayed two-dimensional matrix has determinant (D^2) and trace at most four for (D\in[\delta,2]); this supplies the claimed uniform bound. The example following the lemma satisfies the separation constraint and gives the stated order (\delta^2).

The Gaussian projection in (G.3)–(G.4) does not use oddness or monotonicity of (psi). Its common mean and linear coefficient are at least (a-e); Gaussian integration by parts is justified by the bounded function and derivative. The residual Gram is positive semidefinite even for singular Gaussian covariance. Iteration gives the initialized readout Gram lower bound (G.5), with the stated normalization.

The interval regression certificate is positive for some finite interval because a bounded nonconstant continuous function cannot be affine on every nested interval. The formula for the interval projection in (G.6a) has the correct coefficients. The Gaussian density lower bound yields (c_psi/\sigma), which is appropriate for perturbations whose regression residual can vanish at large variance. The initialized standard deviations lie in the specified range ([1,5a^2]).

The transfer estimate (G.8) is valid for non-Gaussian perturbed variables. Standard deviation is 1-Lipschitz after centering, and the minimizing slope is bounded by two when the perturbed standard deviation is at least (1/2). Testing that affine fit against the initial variable gives the stated loss of at most (3t_*) in the square root of the regression residual.

The gain and amplitude selections are noncircular. The controlled primal estimates require only (e\le1), bounded gates, and the initialized operator event. They control every positive Euler mesh by summing update lengths, including a possible first discrete overshoot. They verify the affine hypothesis of Part R with (B=12). The inequalities (G.18)–(G.19) follow from the gain selections in (M.21); in particular the cubic lower bound compensates for the radius (t_*=\tau_\psi/a).

The capped physical residual equation correctly uses the generally nonsymmetric hidden contribution (J_hU_{h,R}). Its operator norm is dominated by the readout coercivity, so the proof of residual decay does not assume capped dynamics are a gradient flow. The stopped residual-clock estimate gives the strict budget (S/2), excluding an exit at (S) and yielding global capped existence before the response-tail theorem is used.

The passage of response moments to each fixed-cap flow uses fixed meshes first and then refinement. It yields one cap- and time-independent incoming-field tail estimate. The final regression inequality follows from uniform raw hidden displacement and from absorbing the affine part of the activation into the regression fit.

### 5. Cap removal, uniqueness, and the finite algorithms — Part V

The asymmetric gate estimate (V.10) is correct. It requires tails only for the capped reference. In its successive backward use, a new cap factor multiplies a forward discrepancy; the incoming discrepancy is multiplied by bounded actions and (a+e). Consequently (V.11) has one linear cap loss rather than a product of cap losses across depth.

The Gaussian reference tails dominate the resulting Gronwall exponential on every finite horizon. The cap states and raw directions are uniformly Cauchy, giving a strong (C^1) uncut limit and its actual equations. Comparison with a bounded-primal competitor uses only reference tails, proving the stated uniqueness without postulating local Lipschitzness of the uncut vector field on all (L^2) states. The same estimate handles continuation from reached states, including the initial cap-reference discrepancy at the reached time.

The fixed-cap primary derivative and moment arguments use only fixed finite transcripts. The appended velocity queries in V.5 have separate nested truncation arguments because their product maps do not have globally bounded derivatives. The first appended action establishes the moment and derivative domination needed for the second. Named appended forward sources are held fixed when differentiating in the relevant opposite-orientation primary sources; their possible same-family correlations are preserved.

The deterministic velocity comparison (V.40) has a single truncation loss and references only the preactivation-velocity tails. The fixed-cap mesh estimates and their empirical passage establish uniform-time field/velocity laws without requiring finite-width fourth-moment estimates. The true backward observations in V.8 are identified separately from capped update fields. Thus the full true kernels, including off-diagonal entries, are covered.

The actual finite random readout is retained. Its vanishing normalized norm is used only in a same-width auxiliary fixed-program comparison. The same-width comparisons for true GF and raw GD subsequently retain their common nonzero initialization. For GD, the direction is correctly evaluated at the preceding raw node, and its additional defect tends to zero with the step size. The proof does not apply the Gaussian finite-program theorem directly to a transcript whose length grows with width.

Population and finite velocity cap removal use the ordered tail limits stated in V.10; no uncontrolled growth of fixed-cap moment constants is multiplied by a cap-removal error. The interpolation inequality (V.57), together with integrated RMS speed bounds, supplies the missing tightness in the path supremum norm. This establishes path-space (mathcal W_2) convergence in addition to finite-time joint laws. Uniform velocity second moments also justify the integrated squared-speed assertions. The finite generated-probe closure uses bounded actions, Lipschitz coordinate maps, and converging contractions in both orientations.

### 6. Initial accelerations and the projected kernel — Part N and V.I

Lemma V.I supplies the derivative-valid source formulas needed for the initial uncut products. Its expected derivative limits have explicit integrable domination, and its matrix-input passages use second-moment truncation and bounded actions. Thus the initial positivity argument does not misuse the bounded-derivative finite-program theorem.

The top backward Gram is positive definite for every positive (e): (Z^3) has full Gaussian support, the factor (\sum p_i\phi(z_i)) has no open zero set, and a vanishing linear combination of the derivative fields would force every coefficient to vanish because (\psi''\not\equiv0). Independent reverse source covariances then give the strictly positive conditional lower bounds for the lower backward Grams. These prove positivity of every hidden parameter block and every bottom sample direction, including when the affine bottom direction vanishes or the input Gram is singular.

The affine formulas for each upper sample in (N.22)–(N.23) are consistent with the affine feature Grams. The finite Gaussian conditional covariance (N.26), the fourth-moment trace identities (N.28), and the conditional trace calculation (N.35) yield the stated limits. Concentration and passage of expectations are not inferred from these expectation identities alone: Part F's independent trace probe and operator moment bounds supply those steps. The resulting quadratic forms in (N.30) and (N.37) are strictly positive with the displayed lower bounds.

The nonlinear perturbation estimates in N.5 use only bounded actions and the normalized function bounds. Their powers of (a), difference decompositions, and displayed numerical coefficients are consistent. The cutoff (e\le(10^{10}a)^{-1}) preserves both upper-sample lower bounds and is included with slack in (M.21).

The initial acceleration argument requires only the established strong solution, bounded-multiplier continuity, and the first-order behavior of the readout. It correctly obtains hidden velocity divided by (t) tending to (9V), hence the right initial second derivatives. The scalar feature-energy differential justifies the readout-kernel contribution without a second Fréchet derivative of the activation map. The two contributions to the projected kernel are each (9t^2\|V\|^2+o(t^2)), giving the factor 18 in the theorem.

### 7. Uniform function classes and examples — Part A

The interval-certified class has a common parameter recipe because the response and dynamical constants use only the normalized function bounds after the regression certificate is fixed. The asserted uniformity is in the deterministic activation selection and population margin, with convergence still for each fixed function. The (C_b^2) neighborhood argument uses the 1-Lipschitz distance to the affine subspace and preserves all three norm constraints.

For the stronger class, the hypothesis (A.3) gives a scale-independent initial regression certificate. The quartic gain choice in (A.4) correctly preserves a fixed radius (t_0). The distinct-limit argument has the stated limiting residual (b^2(1-2/\pi)); positivity at finite scale, continuity, and the positive limiting value prove a positive infimum. The small (C_b^2) neighborhood of the scaled arctangent retains a common margin even for nonodd, nonmonotone, or oscillating perturbation functions. This does not claim that the full activation loses monotonicity: its large affine slope remains positive.

All listed concrete functions satisfy the stated normalization requirements. The discussion of compactly supported functions correctly explains why the main theorem uses a bounded initialized variance range rather than assuming a positive regression margin over all Gaussian scales.

## Optional editorial suggestions

- Part F, §6 uses the valid but looser bounds (|g'|\le2) and (|\partial_zD_R|\le4eR), whereas Parts R and G use the sharper normalized bounds (|g'|\le1) and (2eR). Using one convention throughout would make constant checking slightly easier. This is not a mathematical error and requires no repair for the verdict.

