# Independent adversarial mathematical review

**Verdict: PASS.** I identified no remaining mathematical correctness or proof-completeness objection in the supplied manuscript after reading its entire contents and checking the obligations described below.

## Input, isolation, and reading coverage

- Sole mathematical reading input: `/tmp/manuscript-a8abf0b79445/REPORT.md`.
- Input SHA256: `d4ab2401e4659ab4a7aef66f83ad40ab14b2db99984df8185cfa7770965304a5`.
- Input size: 3,547 lines, 210,132 bytes.
- Full reading coverage, in consecutive bounded, nontruncated tool outputs: lines 1–220, 221–440, 441–660, 661–880, 881–1100, 1101–1320, 1321–1540, 1541–1760, 1761–1980, 1981–2200, 2201–2420, 2421–2640, 2641–2860, 2861–3080, 3081–3300, and 3301–3547. These cover every line, including all proofs in Parts M, F, R, G, V, V.I, and N.
- I did not read other files, skills, project state, source notes, prior reviews, or history; did not browse or consult outside sources; did not contact other agents; and performed no numerical experiments. File-size and SHA256 commands inspected only the permitted manuscript. This review is my only written output file.

The audit emphasized exact finite algorithms, limit orders, readout initialization, products and appended matrix observations, path and velocity convergence, and initial-motion calculations. I also audited the Gaussian foundation, response bootstrap, global construction, and theorem quantifiers.

## 1. Exact model, normalization, and theorem scope

The factors in (M.7), (M.12), and the four kernel blocks are consistent with the stated metrics. A raw first-weight Euclidean derivative has factor (1/n), while the inverse metric contributes (n/d). A hidden matrix rank-one direction is (uv^T/n), whose Frobenius norm is the product of the two normalized RMS norms. The readout metric contributes the missing factor (n). This verifies, in particular, the factor (Gamma_{ij}) in (K^1) and the absence of additional powers of width in the other blocks.

The finite global-GF argument is valid: dissipation bounds the squared raw speed integral, hence the displacement and all increments approaching a finite endpoint. At a fixed width this prevents finite-time escape in the finite-dimensional parameter space and gives a limit from which local smooth existence continues. This argument is not incorrectly applied to the capped system. Finite GD requires no existence theorem beyond its everywhere-defined finite update formulas.

The theorem keeps (a,e) fixed before width or time limits. Its convergence assertions are for each fixed dataset and finite deterministic horizon. The proof does not establish, or silently use, interchange of infinite time with infinite width. Dimension dependence in bounds involving the full first-weight norm is separated from the dimension-free activation choice, which uses normalized projections and displacement. The realizability qualification handles dimensions in which no admissible input triple exists.

The GD velocities are the derivatives of recomputed hidden fields along linear raw-parameter interpolation. The proof consistently uses the vector field at the preceding raw GD node for the actual raw direction. It does not replace that direction by the vector field at the interpolated raw state. The stated one-sided conventions are covered by the same comparison and affect no integrated-speed assertion.

## 2. Gaussian foundation and common action spaces

I found the finite-program proof in Part F sufficient for the uses made later.

The adaptive conditioning argument conditions successively on the transcript. At a query, its input is already measurable; conditioning the queried Gaussian residual factor on its new linear observation leaves the other residual factors unchanged. This is the needed justification for adaptivity. The minimum-Frobenius-norm solution in (F.6) satisfies both constraints using (U^TY=Q^TV), and its orthogonal complement is precisely the doubly projected homogeneous matrix space. Thus (F.7) follows with the correct normalized innovation variance. The removed noise projection has normalized expected squared norm at most the finite query count divided by width.

For positive limiting query Grams, coefficient convergence, conditional concentration of bounded tests, and the explicit second-moment calculation give empirical (mathcal W_2) convergence. The source-response derivation uses the full old input orthogonality to remove the old forward-input portion of a reverse answer. Gaussian integration by parts then produces (F.9)–(F.10). The covariance of a source is the uncentered input second moment, not its centered covariance. Independent oriented source groups do not imply independent matrix answers; the return terms retain this dependence.

The singular-Gram argument avoids the dangerous step of passing a pseudoinverse through a rank change. Each perturbed query receives fresh independent input noise, giving a positive Schur complement. At fixed program length the finite same-matrix coupling error is bounded by a constant times the noise amplitude. Separately, the scalar source recursion is continuous through positive-semidefinite square-root coupling and bounded, continuous formal first derivatives. This allows width first and regularization removal second. The formal derivative convention remains meaningful at zero variance because null covariance directions disappear after contraction with the associated input fields, as (F.14) shows.

The extension to causal empirical contractions is an oracle comparison of two actual finite computations, using (F.15). It does not take derivatives of random contraction coefficients. The common-space construction uses a countable generated language, density of bounded continuous cylinder functions, and limiting finite operator inequalities. The resulting initialized actions are well-defined on the dense generated span and extend boundedly to (L^2). Passing the exact finite adjunction identity through dense generated inputs proves that the reverse actions are actual Hilbert adjoints. No operator-norm convergence between unidentified finite-width matrices is asserted or needed.

The Hilbert–Schmidt increment normalization matches finite Frobenius norm, and the rank-one continuity estimate supports all the later strong increment limits. The bounded multiplier lemma and the strong curve chain rule are valid with (L^2) inputs. The weighted scalar Taylor estimate proves the scalar predictor is continuously Fréchet differentiable without claiming that the activation Nemytskii map is Fréchet differentiable on all of (L^2). This distinction is used correctly in the energy and kernel identities.

## 3. Response estimates and chronological closure

I checked the indexing, causal order, and nonlinear perturbation structure of Part R. The forward response coefficients contain strictly past reverse inputs, while backward responses include current forward inputs. The learned terms have the correct column control (h_jc_{j,m}). In particular, the middle current return through the already computed top reverse answer is retained in (R.49), (R.65), and (R.94).

The affine Gaussian-probe argument in R.3 does not exchange a width limit with a derivative. It first perturbs actual answer slots with a fresh reused Gaussian vector at fixed amplitude and mesh. Raw affine stability bounds the finite pairing. The fixed-program theorem identifies its limit, Gaussian integration by parts identifies the expected formal derivative contraction, and finite-transcript coefficient continuity permits amplitude removal. Signs are selected for deterministic derivative coefficients after this passage. This yields the required absolute expected row bounds, including singular source slots. The proof does not substitute an expectation of an absolute derivative for the absolute expected derivative.

The nonlinear primal comparison in R.4 uses affine Lipschitzness and a same-state nonlinear/affine field difference. Its constants are cap-independent because |D(z,q)-aq| is at most ε|q|. It supplies source variances before any response bootstrap, so the moment argument is not circular. Learned moment differences use actual coupled queries on common action spaces, rather than an unjustified comparison of growing source covariance square roots.

On a bounded coefficient prefix, the coordinate moment recurrences yield (L^p) bounds proportional to (sqrt p) by deterministic Minkowski and discrete Gronwall estimates. These bounds concern a maximum of deterministic timewise norms, not a random supremum over time. The derivative envelope retains the current incoming factor (1+ε Q_k), which is outside the past-time exponential. Convexity in (R.55) controls the exponential without time independence. The stated constants in (R.57)–(R.68) absorb the terminal factor and the learned moment errors.

The same-array affine derivative comparison is correctly distinguished from the actual affine comparator. The deterministic difference equations (R.69)–(R.87) then bridge those two objects. Their source block factors (h_j) are retained for unequal meshes. The current forward coefficient row depends on previously controlled rows, and the middle current backward row is controlled only after the top current backward row.

The closure in R.9 respects precisely the order (A^2_k,A^3_k,B^3_k,B^2_k). Consequently no unknown current row is assumed bounded to prove its own bound. The telescoping product estimate gives the stated (epsilon_*>0) from a finite chain of constants. The constants may be extremely large or the resulting amplitude extremely small, but this is not an existence or quantifier defect.

## 4. Uniform geometry and global population dynamics

The augmented-Gram bound (G.1) holds also for singular (Gamma). In the mixed-sign case the displayed (2\times2) matrix has determinant (D^2) and trace at most four, and (A^2+b^2) dominates the squared coefficient norm. The example following the lemma has the claimed separation and quotient, so the sharpness observation is also consistent.

The initialized feature Gram lower bound uses a common marginal variance within each layer, which the initialization supplies. Projection onto constants and Gaussian linear functions gives (a+b_vZ_i) with (b_v\ge a); the remaining Gram is positive semidefinite. Iteration yields the (a^6(Gamma+mathbf1mathbf1^T)) contribution needed for uniform readout coercivity.

The positive arctangent regression margin is established both on finite positive variance intervals and at infinite variance. The limit in (G.7) is positive. The stability estimate for a nearby non-Gaussian variable uses its own regression slope, bounded through its standard deviation, and is a valid one-sided test of the initialized regression problem. It requires no persistence of Gaussianity during training.

The controlled displacement estimates apply to all positive Euler meshes as well as controlled continuous paths; the explicit ∑ (h_js_j) identity prevents a first discrete overshoot. They verify the finite affine hypothesis (R.7), rather than inferring arbitrary-mesh Euler stability from a continuous-flow bound. The displayed activation selection gives the required strict displacement, readout, kernel, and regression slacks.

For the capped physical flow, (J_hU_{h,R}) is not presumed positive or symmetric. Its operator norm is bounded by the product of the true hidden differential and capped update-map bounds, while (K^4) remains coercive. This proves the residual decay estimate despite the surrogate hidden direction. Reparametrization is used only before the residual clock can reach (S), and its resulting (S/2) estimate excludes that stop. At zero residual the fixed-cap field vanishes, so the omitted normalized control is unnecessary.

The physical Euler effective clock consists of deterministic population causal coefficients; Part R permits these values with the same frozen affine comparator. Fine fixed-cap physical Euler approximation and the strict clock slack justify applying the response theorem before passing its moments to continuous cap paths. The resulting tail bound is uniform in cap and physical time.

## 5. Cap removal and uniqueness

The asymmetric gate inequality (V.10) is valid also for (R'=∞). Splitting through the lower-cap gate leaves a lower-cap Lipschitz forward term and a tail depending only on the reference incoming field. Descending the three backward levels multiplies incoming errors by bounded actions and bounded (q)-derivatives; it does not multiply the cap factors together. Thus (V.11) has a single factor linear in (R).

The Gaussian reference tail dominates the resulting (\exp(K_TR)) stability loss. Cap paths and their raw derivatives are uniformly Cauchy on each compact horizon. Passing their integral equations gives a strong (C^1) limit, and the same asymmetric estimate identifies its uncut vector field. The argument also compares any bounded-primal strong competitor with the reference cap path without assuming tails for the competitor. At a reached state the existing cap discrepancy remains vanishing after another finite-time stability factor. These facts justify the stated uniqueness and continuation class; the manuscript does not invoke unproved local Lipschitzness of the uncut vector field on arbitrary (L^2) states.

## 6. Finite GF/GD, actual initialization, and limit order

The actual readout has (E\|C_0^{(n)}\|_n^2=n^{-2}), hence RMS size (O_{\Pr}(n^{-1})). Its zero-readout comparator is used only to identify a fixed capped transcript, where Lipschitz comparison propagates the vanishing discrepancy. The actual finite algorithms and their same-width cap comparisons retain the nonzero random readout. This is sufficient; a direct uncapped, growing-transcript initialization comparison is not presumed.

At a fixed auxiliary mesh, the initialized matrix bound and exact rank-update lengths yield finite primal bounds with slack. Uniform deterministic fixed-cap Euler estimates then compare finite GF or fine raw Euler with that same-width coarse program. Only the coarse program is subjected to Gaussian identification. The fine raw step contributes its deterministic interpolation defect, which tends to zero at the stipulated (n^{-2}) step. The proof therefore never applies F.1 to a program whose instruction count grows with width.

The finite uncut comparisons use the same finite cap reference and its empirical positive-part tails. Width is taken with cap fixed, where the established capped laws give those tail limits. A first-exit argument closes the bounded primal event, after which cap removal transfers the fields and kernels. The raw-GD inequality (V.55) correctly compares its preceding-node raw direction to the cap reference and includes the cap within-step defect. This avoids any width-independent uncut Lipschitz premise. Using a common initialization and reference makes the two algorithm convergence assertions joint without requiring independence between widths.

## 7. Products, true kernels, velocities, and path \mathcal W_2

The appended velocity products and true backward products do not satisfy the original bounded-coordinate-derivative hypothesis. The manuscript explicitly repairs this in two different ways appropriate to their uses.

For velocity source formulas, V.5 first truncates the bottom product. The primary absolute derivative rows provide an integrable envelope independent of the product truncation. This identifies the first appended action and its moments before using those moments for the next appended action. The next action uses nested truncations in a fixed order. Its new forward Gaussian source has zero formal derivative in the opposite source family, even when same-family covariances are singular. The argument establishes the needed expected derivative identities without an (L^p)-bounded matrix-action theorem or a circular velocity moment assumption.

For true backward observations on capped trajectories, V.8 uses bounded multiplier continuity, joint (mathcal W_2) tail control, and bounded actual transpose actions; no source derivative formula is required there. V.I separately proves derivative-valid formulas at initialization through nested truncation and integrable Gaussian-linear envelopes. Thus the kernels throughout the theorem use the actual backward fields, not silently the capped update fields.

The deterministic velocity comparison has a single truncation level factor multiplying the raw state discrepancy. Each higher-layer multiplier error uses its own already controlled forward discrepancy. Population fixed-cap node velocity moments justify mesh refinement. For cap removal, V.10 instead uses compact (L^2) time images of the uncut velocities and orders cap removal at a fixed tail level before tail removal. It does not multiply an uncontrolled cap-dependent moment constant by the cap error.

Uniform-time same-layer joint (mathcal W_2) convergence controls second moments and all contractions needed for the four kernel blocks. Finite-time concatenation retains temporal correlations. For path laws, the explicit interpolation inequality (V.57) bounds expected squared supremum error by the mesh size times integrated RMS squared speed. Initial second moments and this speed bound provide finite path-space second moments and continuous coordinate versions. This supplies the missing implication that fixed-time laws alone could not supply. The integrated squared-speed convergence then follows from uniform-time norm convergence; it concerns actual coordinate speeds, not marginal-law metric derivatives.

Fixed finite generated probes remain within the established closure under Lipschitz coordinate functions, contractions, and both orientations of initialized/current actions. The probe instruction count is fixed before width, and no unidentified cross-width operator comparison is used.

## 8. Initial motion, Gaussian moments, and nontriviality

The positivity argument for (S_3) uses nondegeneracy of the initialized top Gaussian tuple, which follows from the augmented input Gram and the first two feature Grams. Full support turns a zero squared norm into an everywhere functional identity. Since the weighted feature sum has no open zero set and (phi'') is not identically zero for (e>0), all coefficients of the proposed null vector vanish. The fresh reverse covariance in V.I then makes (S_2) positive definite and supplies the conditional covariance bound at the bottom. This proves positivity of all hidden parameter blocks and every bottom sample without inverting (Gamma).

The affine upper-layer formulas (N.22)–(N.23) have the correct powers of (a), with (V^2=a^3Q\otimes k) and (V^3=H\otimes v). I checked the finite conditional moment calculation (N.26): the linear term has covariance (a^2m^2I), the quadratic term has covariance (|v_n|_n^2I+v_nv_n^T/n), and the cross covariance vanishes by the centered cubic Gaussian identity. This gives the exact (1+1/n) factor in (N.27).

The trace calculations use the correct real Gaussian fourth pairings. They yield (	au(AA^*)=1,	au((AA^*)^2)=2), and the upper pair of matrices has (	au(S)=	au(R)=1,	au(S^2)=	au(SR)=2,	au(R^2)=3). The conditional formula (N.35), including its (	au_n(M_n)^2) term, is correct. Deterministic trace limits are not inferred from expectations alone: independent Gaussian trace probes, F.1, operator moment bounds, and uniform integrability justify each passage. The same moment control justifies the vector-norm expectation limits and products of random factors used in (N.32).

Both square completions, (N.30)/(N.33) and (N.37)/(N.38), give the claimed positive affine lower bounds uniformly in sample geometry. The binary three-label assumption supplies (|m|\ge1/3), which is essential and available. The explicit nonlinear perturbation calculation compares the gate with the constant affine gate, so its bound does not require uniform control of a preactivation-dependent gate difference. The numerical coefficient arithmetic in (N.41)–(N.50) and the amplitude cutoff preserve both upper-sample lower bounds. Consequently all hidden preactivation and feature directions are nonzero.

Finally (C'(0)=3H), hence (b_i^ell(t)/t\to3\beta_i^ell), and the hidden physical direction divided by time tends to (9V). The raw displacement is therefore ((9/2)t^2V+o(t^2)). The chain rule yields the claimed right second derivatives (9U_j^ell) and (9d_j^ell U_j^ell). For the projected kernel, its hidden-gradient norm contributes (9t^2\|V\|^2); the scalar feature-energy differential contributes another (9t^2\|V\|^2) to its readout block. Their sum is exactly the coefficient 18 in (M.20)/(N.64). This is a change of the true total projected kernel.

## External theorem and completeness audit

I found no external nonclassical lemma left unproved and no advanced external result carrying an unchecked hypothesis. The potentially substantial inputs are internal: the adaptive Gaussian program theorem is proved in Part F; the mesh/cap-uniform response theorem is proved in Part R; the cap-transfer and velocity/product arguments are proved in Part V; and the initialization derivative extension is proved in V.I.

The remaining standard foundational tools include finite-dimensional Gaussian factorization and orthogonal diagonalization, the law of large numbers proved by truncation here, dominated convergence, Fatou, Fubini/Tonelli, Cauchy–Schwarz/Hölder, Parseval, elementary probability regularity/monotone-class approximation, and contraction or Gronwall iteration. Their relevant integrability, separability, boundedness, and causality requirements are supplied in the applications. None conceals a growing-transcript theorem, an arbitrary (L^p) matrix bound, or a differentiability theorem for general nonlinear (L^2) maps.

There are no mathematical repair requests from this audit.
