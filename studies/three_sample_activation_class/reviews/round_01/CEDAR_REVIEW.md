# Independent mathematical referee report

**Verdict: PASS.** I find no remaining mathematical correctness or completeness objection in this manuscript. This verdict covers the entire manuscript, including the finite-program construction, controlled-response estimates, all observation limits, initial-motion calculations, and activation subclasses.

## Input identity, independence, and reading coverage

- Sole mathematical reading input: `/tmp/report-e42cddb32cea/REPORT.md`.
- Manuscript size: 3,826 lines, 223,246 bytes.
- SHA256: `ad30e1e3ed36db9d1f36220859e3d40916aab4b26f892e478ccb850c9dbc7cd5`.
- The hash was checked before and after the reading and was unchanged.
- I read the complete file in these bounded, nontruncated chunks: lines 1–280, 281–560, 561–840, 841–1120, 1121–1420, 1421–1720, 1721–2020, 2021–2320, 2321–2620, 2621–2920, 2921–3220, 3221–3520, and 3521–3826. This covers every line, including every table and the final activation examples. I subsequently obtained section line numbers from the same input file.
- I did not read any other file, skill, project instruction, source note, prior manuscript, review, or project state. I did not use the web, numerical experiments, another agent's reasoning, or additional mathematical context. The calculations below are an independent analytical audit of the supplied manuscript.
- I did not modify the manuscript. This report is the only file I wrote.

## Objections and required repairs

**Substantive objections: none. Required mathematical repairs: none.**

In particular, I did not treat the stated internal lemmas as external assumptions: I checked their proofs in Parts F, R, G, V, and N. I also checked that later invocations stay within the hypotheses actually established. The distinctions between finite programs and growing meshes, capped update fields and true backward fields, formal source derivatives and covariance derivatives, and same-space comparisons and cross-width operator assertions are maintained where they matter.

## Detailed audit

### 1. Model, normalization, scope, and parameter selection — lines 3–365

The raw metric and gradient factors agree. The first Euclidean weight derivative has factor (1/n), which becomes (1/d) after applying the inverse first-block metric; the hidden matrix blocks retain (1/n), and the readout factor cancels. The Hilbert–Schmidt rank-one convention subsequently used is precisely (uv^T/n) at finite width. The four kernel blocks are the corresponding gradient Grams.

The realizability restriction is legitimate: positivity of the squared sum of the three normalized inputs gives (9-6\delta\ge0). No argument assumes positive definiteness of the original input Gram. The initial first projections have variance one, and the finite readout has normalized mean-square norm (n^{-2}), consistent with the limiting zero readout. The latter is an auxiliary population limit and is not substituted into the actual finite algorithms.

The finite-dimensional global GF argument is valid: the energy identity bounds raw displacement on a finite interval and makes the path Cauchy at a finite endpoint; local existence then extends it. GD is defined at all finite iterates regardless of whether a deterministic global bound is available.

The theorem's convergence quantifiers are compact-time, fixed-data, full-sequence convergence in probability. Its uniform activation selection does not purport to give uniform convergence over all datasets or an interchange of infinite width and infinite time. The definition of a generated probe is finite and layer-typed. The GD directions are the actual directions of the recomputed hidden fields along the raw parameter interpolation.

The constants in (M.21) are finite and strictly positive. The dependence on the shape through the interval regression constant is sufficient; the subsequent response threshold uses only the displayed uniform bounds on the shape and its first two derivatives. The dimension-dependent norm of the full initialized first weight is acknowledged, and the selection uses normalized projections and displacements instead.

### 2. Fixed Gaussian programs, conditioning, and singular cases — lines 366–745

**Elementary probability and operator bounds.** The operator-net proof has the correct normalization and exponent. For (t\ge10), the strengthened tail bound in (F.4a) follows from (2\log9\le t^2/16). Tail integration yields the uniform operator moments subsequently needed in Part N. The conditional quadratic-form variance in (F.4c) correctly uses the symmetric part, and the upper bound is (2\|T_n\|_{\rm op}^2/n). Thus the trace probe does not rely on an unproved concentration assertion. Empirical second moments, weak convergence, and their conversion to Wasserstein convergence use the required finite second moments; no independence of trained coordinates is asserted.

**Adaptive conditioning.** The transcript argument in Section 3 is sound. Conditional on the past, an adaptive input is fixed, and the next answer is a linear observation of only the queried matrix. Conditioning therefore preserves the product structure of the remaining conditional matrix factors. This is a successive-conditioning argument, not conditioning a fresh Gaussian on constraints whose adaptive origin is ignored.

The compatibility identity (U^TY=Q^TV), the minimum-Frobenius-norm mean in (F.6), and the homogeneous subspace (P_{U^\perp}KP_{V^\perp}) are correct. In (F.7), the reverse coefficient has exactly the required normalization ((U^TU/n)^{-1}(Q^Th_\perp/n)). The removed projection of the fresh Gaussian has mean normalized squared norm at most the finite query rank divided by (n). Positive definite limiting query Grams justify the provisional inverse operations on events whose probabilities tend to one. The conditional test-function and second-moment arguments then establish the induction.

**Source rule.** In Section 4, orthogonality to previous forward inputs removes the old forward-response contributions from (E[q_sh_\perp]). Gaussian integration by parts gives (G_U E\nabla_\zeta h_\perp), and substitution into the conditional mean cancels the old forward coefficients with the correct sign. The resulting forward-source covariance is the *uncentered* input Gram. Independence concerns the centered source groups, while dependence between actual forward and reverse answers remains in the return terms.

The derivative convention freezes deterministic coefficients and covariances and retains each named slot. The hypotheses for integration by parts hold: finite-program scalar expressions have at most linear growth and bounded first source derivatives at fixed coefficients. Conditioning on independent roots and other source groups is allowed. No derivative through a covariance representation is introduced.

**Rank loss.** Section 5 correctly adds a distinct independent Gaussian perturbation to every query input. Each new limiting squared distance to the preceding query span is at least the perturbation variance. The finite-program perturbation error is uniformly (O(\varepsilon)) at fixed instruction count on the bounded-operator and bounded-noise events. Continuity of the finite source recursion is proved through positive-semidefinite square roots and bounded derivatives, rather than by claiming continuity of a pseudoinverse. Root second moments supply the required dominator for scalar values, and derivative boundedness supplies domination for their expectations. The resulting limit order proves the original program's full-sequence law even at singular Grams. The kernel-invariance observation (F.14) correctly shows that contracted corrections are independent of nonunique derivative coordinates on a singular support.

**Feedback and network unrolling.** The oracle comparison for causal scalar contractions is causal and uses local Lipschitzness only near the deterministic limiting arguments. Coefficient errors multiply bounded-in-probability normalized vector norms. The forward and backward learned terms in (F.21)–(F.22) have the right sample placement, control factors, and time inequalities. The current third-layer return can enter the current second-layer return; the manuscript retains that derivative path. The vanishing readout comparison is valid at fixed cap and fixed program length.

### 3. Common action spaces, actual adjoints, and differentiation — lines 746–990

The countable language is closed under the needed operations and admits consistent finite-dimensional limiting laws. Retaining each layer's generated sigma-field gives separable (L^2) spaces. The stated density argument is adequate: cylinder functions are dense, bounded continuous functions approximate finite-dimensional Borel functions in (L^2), and the included smooth family approximates those functions with tail control.

The finite operator inequalities pass to deterministic limiting norms. They ensure that an action is independent of the expression used to represent its input and extends continuously from the dense generated span. Crucially, the reverse assignments are proved to be the actual Hilbert adjoints by passing the finite inner-product identity and using density. Arbitrary bounded operators are never substituted for this construction. Approximation of additional fixed real-coefficient and Lipschitz probes uses the same bounded actions and finite second-moment tail control.

The Hilbert–Schmidt identities (F.28)–(F.31), including the normalized finite realization, are correct. Only learned increments are required to be Hilbert–Schmidt. Strong integrals of rank-one velocities therefore give legitimate increments and adjoints on these spaces.

The bounded-multiplier lemma and strong curve chain rule are valid under their stated hypotheses. In particular, they avoid a false assertion that a nonlinear Nemytskii map is Fréchet differentiable on all of (L^2). The scalar weighted Taylor estimate (F.41) does yield an (o(\|q\|_2)) remainder against a fixed (L^2) weight: first fix the truncation level, take the small-increment limit, then remove the weight truncation. Repeated top-down use produces the displayed scalar predictor derivative and its continuous raw gradient. The gradient-flow and kernel identities consequently hold for the constructed strong uncut path.

The local capped field is locally Lipschitz on raw balls, and its contraction and Euler arguments apply with width-independent constants on the prescribed primal balls. Measurable controls are appropriately assigned absolutely continuous solutions rather than automatically (C^1) ones. The final product-observation truncation is used only for values and laws; it is not presented as an unrestricted unbounded-derivative source theorem.

### 4. Controlled response theorem — lines 991–1811

I checked the entire constant chain and chronological argument, including the current blocks.

- The matrix block row norms, (|\Gamma_{ij}|\le1), and the control condition give the asserted submultiplicative estimates. (R.11)–(R.16) follow from exact rank unrolling and the source rule. In particular, there is no spurious control factor in the response derivative term.
- The affine propagation and differences in (R.20)–(R.22) give update Lipschitz bounds dominated by (Q=100a^3b^3). The four answer-perturbation forcing constants in the table have the claimed affected updates and sizes. The Gaussian probe yields signed *expected* derivative sums, and choosing their deterministic signs produces absolute coefficient sums. It does not equate (|E\partial V|) with (E|\partial V|). The factor three used in passing scalar output-row estimates to block rows is supplied in (R.28). A single-time forcing keeps its (h_j) factor, including at zero-variance source slots.
- The same-state nonlinear/affine query bounds and raw-field estimate (R.33) are independent of the cap. The stopped comparison keeps the nonlinear path inside the larger ball. Query variances and the learned-moment errors are consequently bounded *before* response estimates are assumed; this removes a possible circular moment premise.
- On bounded coefficient prefixes, the moment inequalities use Minkowski and deterministic maxima of norms, not a random maximum over an increasing number of times. The discrete Volterra bounds in (R.38)–(R.40) give the specified (K\sqrt p) constants. The exponential-moment estimate uses (m!\ge(m/\exp(1))^m) with the correct scale.
- The exact derivative equations (R.46)–(R.49) retain the cap derivative, current forward dependence, and middle derivative through the current third-layer return. Reverse-source blocks vanish through their insertion time and then carry the source step (h_j). The full forward rows have unit direct forcing. The envelope arguments keep the terminal multiplier (1+\varepsilon Q_k), which cannot be absorbed into a sum containing only past (Q_r). Convexity in (R.55) supplies integrability without time independence.
- The same-array affine derivative comparison in Section R.7 is distinct from comparison with the actual affine baseline. The subtraction formulas list the nonlinear forcing terms, retain the unequal-mesh source factor, and give the remainders in (R.68). The coefficient (200H^{11}e^{HS}) dominates the stated (10H^3D_1) backward remainder, and (m_0(1+S)) covers the learned-moment errors.
- The deterministic recursions (R.69)–(R.87) and their time factors agree. In particular, the affine top readout derivative has no dependence on the current (A^3_k), while the middle output product has the current (B^3_k), already bounded at its preceding stage. The four error constants and (K_*=2\max\{1,D_2,D_3,E_2,E_3\}) dominate both individual errors and their required sum.
- Section R.9 closes the prefixes in the actual order (A^2_k,A^3_k,B^3_k,B^2_k). The proof of each remainder uses only previously bounded rows and the current rows already completed in this order. The product identity yields the half-unit slack at (R.90). The zero-readout initial row starts the induction even with zero source variance. (R.93)–(R.94) include both current returns and the correct sample column on the middle forward gate.

The conclusion is genuinely uniform in mesh count, positive step sizes with bounded total clock, cap, and control variation, subject to the explicitly stated affine finite-array hypothesis. That hypothesis is subsequently verified in G.3 rather than inferred from continuous-flow stability on arbitrary coarse meshes.

### 5. Geometry, nonlinear regression margin, and global clock — lines 1812–2284

The augmented-Gram proof handles all coefficient sign patterns for three samples. Its two-by-two matrix has determinant (D^2) and trace at most four for (D\in[\delta,2]), so the claimed lower bound follows. The example establishing the δ-squared scale has the asserted pairwise inner products and quotient.

The initial Gaussian projection uses integration by parts without an inverse of a singular covariance. The projected constant and slope are each at least (a/2); the residual Gram is positive semidefinite. Iteration gives (G.5) with λ equal to δ-squared divided by 256. The marginal standard-deviation bounds (1\le\sigma_\ell\le5a^2) are sufficient for the later argument.

The interval distance (J_r) must be positive for some finite integer (r), because otherwise the compatible affine representatives would make the bounded shape constant. The Gaussian density lower bound on that interval gives (\mathcal R(\sigma G)\ge c_\psi/\sigma). The perturbation estimate (G.8) is valid for non-Gaussian trained variables: standard deviation remains at least one half, the optimal slope has absolute value at most two, and the two regression residual norms differ by at most (3t_*). Thus the lower bound is not based on a Gaussianity assumption during training.

The raw controlled speed constants and the quadratic displacement bound follow from the displayed forward and backward norm bounds. The Euler summation identity also excludes a first discrete overshoot. The choices in (M.21) imply (G.18). In particular, the leading gain bound gives (a^6\ge6.4\cdot10^{19}\lambda^{-3}), and the cubic bound gives (615a^2D_S/t_*\le0.08856). The affine finite-array hypothesis of Part R holds with (B=12) on the initialized norm event, for every admitted positive control mesh.

The feature-Gram perturbation is at most (7.2\cdot10^6a^6D). The true hidden differential and the capped update map have product norm at most (6\cdot10^6a^6C_S^2). Although that product need not be positive or symmetric, its absolute quadratic-form contribution is bounded, which is enough for the residual estimate. The resulting residual clock is at most (6/(\lambda a^6)=S/2), with strict slack against the stopping clock (S). This is a valid argument for capped physical dynamics and does not wrongly assign them a gradient-flow energy identity.

Fixed-cap Euler convergence and this clock bound justify the effective physical meshes used in G.5. Their coefficients are deterministic population feedback values frozen in formal source derivatives. Part R's moment bounds pass at fixed cap and then hold uniformly in physical time and cap. They supply precisely the reference tails required for the cap transfer.

### 6. Cap transfer, finite algorithms, kernels, velocities, and paths — lines 2285–2991

**Raw stability and uniqueness.** The asymmetric gate estimate (V.10) is correct, including (R'=\infty). Comparing each incoming argument first, and introducing each capped forward multiplier afterward, produces only a single linear cap loss. Sequential substitution and rank-one differences give (V.11), including actual residual feedback, with tails only from the reference path. The Gaussian tail dominates the ensuing exponential-in-cap stability loss on every fixed horizon. Thus cap states and directions converge strongly in the raw space, their limit solves the true equation, and the same reference-only bound proves uniqueness against any bounded-primal strong competitor. The reached-state continuation argument also preserves this decay after its additional stability factor.

**Fixed-cap derivatives and velocities.** The nonlinear Gaussian probe in V.3 recomputes the residuals at finite width and then freezes the limiting scalar coefficients in source derivatives. At fixed mesh its derivative expectations are continuous by the stated square-root coupling and bounded-derivative domination. The primary finite primal event used here is supplied independently by update-length bounds in V.7. The pointwise derivative-row estimates in V.4 are proved after the expected coefficient estimates; the two estimates are not conflated. Their current terms are triangular and require no same-time inverse.

The appended velocity formulas have the correct raw chain-rule terms and learned rank contributions. Their initial-matrix calls are ordered after the primary transcript, and future-source derivatives vanish. The new forward source is held as a separate named argument when differentiating in primary transpose sources; its possibly singular covariance does not authorize an additional derivative through a representation of that covariance. Nested clipping is necessary here and is provided. The first action obtains its derivative domination from primary moments; the second action uses the already established first-action moments. This ordering avoids assuming the desired untruncated velocity moments in order to prove them.

**Finite-cap algorithm limits.** The Euler defects and stopped comparisons in V.6–V.7 are uniform in width at fixed cap. The comparisons explicitly retain the actual finite readout; its vanishing discrepancy is established through a same-matrix zero-readout auxiliary program only at fixed transcript. The finite primal ball is obtained using exact update lengths and fixed-program contraction limits, rather than convergence of current finite operator norms to a population operator norm. Primary and velocity laws are transferred by same-neuron couplings, with width taken before auxiliary mesh refinement. Tail convergence follows from Wasserstein convergence and the Lipschitz positive-part tail functional, not from an unproved empirical fourth-moment estimate.

**True kernels.** Section V.8 separately closes the true backward observation chain at capped states using nested product truncations and bounded actual transpose actions. It then proves the trajectory comparison using compact (L^2) time images for reference tails. Consequently all four true gradient-kernel blocks, including their off-diagonals, have the asserted uniform-time limits. The manuscript correctly distinguishes this observed kernel from the nonsymmetric coefficient matrix governing a capped trajectory's own predictions.

**Uncut finite algorithms.** V.9 applies the same-width asymmetric comparison at fixed cap and takes the width limit before removing that cap. The raw GD direction is evaluated at the preceding GD node throughout; the extra defect is a fixed-cap reference variation of order (\eta_n). There is no use of a width-independent Lipschitz constant for the uncut finite field. First-exit estimates supply the required high-probability finite-horizon bounds. Joint convergence of GF and GD follows from their common initialized reference.

**Velocity and path limits.** In (V.40), truncation is on the reference preactivation speed, and each new multiplier cutoff acts on a forward state discrepancy. The single cutoff loss is therefore correct. Population uncut velocities have continuous (L^2) paths, whose compact images have uniformly vanishing second-moment tails. This permits velocity cap removal without an assumed growth bound on cap-dependent higher-moment constants. The finite comparison takes width, then cap, then the velocity-tail level in the stated order. Joint laws at finitely many times are obtained from the whole coarse transcript, not separate marginal convergence.

The interpolation estimate (V.57) is valid for each absolutely continuous neuron path. After averaging, it supplies a path-space Wasserstein error controlled by the integrated RMS speed, and also establishes finite second moments in the path supremum norm. This is enough to promote joint observation-grid laws to the asserted full path law. Uniform velocity second moments yield the integrated squared-speed statements. The raw-block speed identities use the true preceding-node residual and kernel for GD. Generated probes and both action orientations pass using actual operator bounds and HS differences, without identifying unrelated finite matrices across widths.

**Initialization observation lemma.** V.I verifies the additional derivative formulas actually needed in Part N. The top expected derivative has an integrable envelope (K(1+|H_0|)). After the first transpose passage, its derivative in each middle forward source is the deterministic return coefficient times the corresponding gate. The second gate is handled by the stated inner-then-outer truncation order, with envelope (K(1+|q_i^2|)) after the first limit. The complete reverse-source Grams, current return terms, and independence from the respective forward families are all retained. Thus (V.I.1)–(V.I.3) do not rely on directly applying F.1 to an unbounded-derivative product.

### 7. Initial hidden motion and changing projected kernel — lines 2992–3645

The feature-energy differential (N.9) follows from the same scalar weighted Taylor argument used for the predictor and has raw gradient (V). Its use later requires only first scalar Fréchet differentiability, which is proved.

The initial feature Grams (Q_1,Q_2) are positive definite even when the input Gram is singular. Therefore the top preactivation tuple has full Gaussian support. If (v^TS_3v=0), the product identity (N.11) holds everywhere by continuity. The first factor has no open zero set because every (p_i\phi'(z_i)) is nonzero. The second factor must then vanish everywhere, and differentiating it shows every (v_i=0), since (e\psi''\not\equiv0). This proves positive definiteness of the top backward Gram for every positive admitted amplitude.

The fresh reverse-source covariances then give the conditional covariance bounds (N.15)–(N.16). The return shifts remain present but do not change those conditional covariances. These bounds imply nonzero motion of every hidden parameter block and every bottom sample. The rank-one trace identity and positive-definite trace lower bound in (N.18) are valid even with mixed signs in (p). The bottom-sample argument needs only the unit diagonal of the possibly singular input Gram.

I independently expanded the affine upper-layer formulas. With (Q=B^*H), the middle direction is (a^4[(\gamma_j+m)I+\gamma_jAA^*]Q). The top direct term has coefficient (a^5[\gamma_j+(1+a^{-2})m]), and the two propagated terms give exactly (N.23).

The finite Gaussian calculations in N.4 have the correct scaling. In particular:

- (E_BQ_n=v_n), and its covariance is ((a^2m^2+\|v_n\|_n^2)I+v_nv_n^T/n); the mixed linear/quadratic covariance is zero by centered cubic moments.
- The Gaussian fourth-moment expansion gives limiting traces (\tau(AA^*)=1), (\tau((AA^*)^2)=2).
- For (S=BB^*) and (R=BAA^*B^*), the required limiting traces are (1,1,2,2,3) for (S,R,S^2,SR,R^2), respectively. The conditional formula (N.35) has both terms and the correct (1+1/n) factor.
- Consequently (\tau(L_j^2)=(m+2\gamma_j)^2+\gamma_j^2), and the completed square for (\tau(T_j^2)) has remainder ((6+8a^{-2}+5a^{-4})m^2/14).

These are deterministic population inequalities because F.1 and the independent Gaussian trace probe establish deterministic limits, and the proved operator moments give uniform integrability. Finite expectation computations alone are not used as a substitute for this passage. The symmetry argument eliminating the top cross term and the orthogonal-invariance argument relating its constant-vector norm to a normalized trace are valid at fixed (A_n).

The nonlinear perturbation tables and their scalar derivations have the displayed powers and coefficients. In particular, the two final direction-error coefficients are (6{,}985{,}680a^6e) and (143{,}416{,}183a^7e), each dominated by the stated common bound. The cutoff (e\le(10^{10}a)^{-1}) leaves more than half of both affine lower bounds for every upper sample. It is included in the activation rule.

For physical time, (C'(0)=3H), (b_i^\ell(t)/t\to3\beta_i^\ell), and the hidden raw equation consequently gives (\theta_h'(t)/t\to9V). Bounded multiplier continuity and the actual action adjoints suffice for all these strong limits. The resulting right second derivatives of preactivations and features are (9U_j^\ell) and (9\phi'(Z_j^\ell)U_j^\ell); no ambient second Fréchet derivative is assumed. Finally, the hidden part of the projected kernel contributes (9t^2\|V\|^2), and the scalar feature-energy differential contributes another (9t^2\|V\|^2). Thus the coefficient 18 in (M.20)/(N.64) is correct and strictly positive.

### 8. Uniform shape classes and examples — lines 3646–3826

The interval-distance lower bound gives the common recipe and margin in A.1, with no unsupported uniform-in-function probabilistic convergence claim. The distance-to-subspace Lipschitz estimate gives the asserted infinite-dimensional neighborhoods within the normalized (C_b^2) bounds.

Under (A.3), the replacement margin radius is independent of the gain, and the quartic gain selection in (A.4) gives (615a_\delta^2D_S\le0.08856t_0), as needed. For distinct finite limits at infinity, projection onto (\operatorname{span}\{1,G\}), bounded convergence, and (E|G|=\sqrt{2/\pi}) give the positive limiting residual. Continuity on bounded positive scale intervals then gives a positive infimum over all scales at least one. The arctangent neighborhood inherits a common margin through the uniform perturbation bound; the sine and cosine perturbation statements are compatible with that construction.

The concrete functions in (A.8) have the claimed bounded first two derivatives after normalization. The compact-support example correctly shows why a scale-uniform Gaussian regression margin cannot be assumed for the full class. The final scope restriction to the selected affine-plus-small-perturbation activations is consistent with what was proved.

## Final assessment

All parts were read and checked, and the emphasized issues were also checked independently of the theorem's stated conclusions. The manuscript supplies the needed adaptive-conditioning argument, rank-loss treatment, common action construction with genuine adjoints, derivative-valid observational extensions, and ordered dynamical limit transfers. The remaining algebraic and analytical assertions, including the explicit constant selections and all initial-motion statements, are supported by the supplied proofs. **PASS; no mathematical repair is required.**
