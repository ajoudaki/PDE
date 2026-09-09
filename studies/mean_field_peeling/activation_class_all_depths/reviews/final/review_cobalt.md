# Independent whole-manuscript audit — cobalt

**Verdict: PASS.** I found no unresolved mathematical objection to the complete statement of Theorem M.1, with its stated fixed-depth, fixed-horizon, and full-width-sequence quantifiers. This is a proof audit, not a claim of a machine-checked formal proof.

## Audited artifact and isolation

- Sole mathematical input: `/tmp/hidden_depth_final_20260908/manuscript.md`.
- Exact SHA256, independently computed: `efa3c2b1e592a469d8aa7900e95f0a8a43a4a1865b9c4c3f69f3bacfcb613e4a`.
- I read the entire manuscript, including every proof and appendix, rather than limiting the review to the principal theorem or selected bottlenecks.
- Complete read coverage: Part M, M.1–M.3; Part F, Sections 1–11; Part S, S.1–S.7; Part G, G.1–G.4; Part V, V.1–V.12; Part N, its statement and N.1–N.5; Part A, A.1–A.5. To avoid any omission from a truncated initial display, I subsequently read complete, nontruncated blocks covering lines 1–368, 369–654, 654–1068, 1069–1476, 1477–1735, 1735–1937, 1938–2199, 2199–2501, and 2502 through the end.
- I did not read other manuscripts, author notes, skills, reviews, or chat history, did not consult or spawn another agent, and did not run numerical experiments.
- No specialized external theorem is invoked as a premise. The manuscript supplies its own finite Gaussian program theorem, singular extension, common-action construction, source estimates, and algorithm bridge. I did not substitute a remembered tensor-program, dynamical-mean-field, or propagation-of-chaos theorem for any of these proofs. The elementary Gaussian, Hilbert-space, and integration arguments are checked below.

## Theorem-obligation ledger

| Obligation | Finding |
|---|---|
| Exact raw initialization, metric, and physical GF/GD scaling | Verified in M and F. |
| Fixed finite Gaussian programs with adaptively reused transposes | Verified by the sequential conditional-law induction and source-rule algebra in F. |
| Singular query Grams without rank stability | Verified by fresh input-noise regularization, same-array stability, and covariance-square-root continuity. |
| One common population action space with genuine adjoints | Verified by the countable generated language, norm transfer, density, and finite adjunction identity. |
| Scalar Fréchet derivative and strong field chain rules at only (C^2) activation regularity | Verified; no invalid ambient (L^2\to L^2) Fréchet derivative is used. |
| Cap- and mesh-uniform controlled source moments | Verified by S's independent primal bounds, actual-array Gaussian decomposition, Volterra derivative bounds, and chronological construction. |
| One gain valid at all separately fixed finite depths | Verified, including S's coefficient boxes, G's perturbation estimates, and the nonaffinity arithmetic. |
| Global strong population uncut GF, uniqueness, and restart | Verified by the capped residual clock and one-reference-cap comparison. |
| Original finite GF and simultaneous original raw GD | Verified by fixed-cap same-width comparisons, retention of the actual random readout, and ordered removal of the training cap. |
| Uniform true kernels, fields, and velocities | Verified, including separate treatment of true backward observations and actual GD interpolation directions. |
| Whole-path (\mathcal W_2), joint-time laws, second moments, and integrated speeds | Verified using the explicit path interpolation estimate and the uniform velocity laws. |
| Fixed finite generated probes and both action orientations | Verified by finite-program approximation and bounded-action propagation. |
| Persistent nonlinear regression residual | Verified by the bounded optimal-slope argument and Gaussian finite-interval margin. |
| Every hidden block and every sample/layer has nonzero initial acceleration; coefficient 18 | Verified by N's backward covariance floors, forward innovations, derivative-valid clips, and exact telescoping identity. |
| Appendix's class-uniform and depth-uniform refinements | Verified with the restrictions and quantifiers stated in A.5. |

## 1. Raw equations, normalization, and differentiation

The inverse first-layer metric converts the Euclidean derivative's factor (1/n) into (1/d), whereas the higher matrices retain (1/n) and the readout loses it. Thus (M.10) is precisely the gradient flow of the displayed finite loss under (M.9). Setting (w=\sqrt d W^1) is an isometry, and the bottom preactivation becomes (w\cdot u_i). For normalized hidden fields, the identity

\[
\chi_\ell(v)=\phi(a^{\ell-1}v)/a^\ell,
\qquad f_i=a^LF_i
\]

holds exactly. Consequently all raw gradient blocks have the same factor (a^L). The backward scaling (b_i^\ell=a^{L-\ell+1}d_i^\ell), the rank-one action (vh^T/n), and all three kinds of kernel block in (M.14)/(V.34) agree with that metric. There is no concealed change of learning rate or readout variable.

The proof of scalar Fréchet differentiability in F.7 is adequate despite the familiar obstruction to general (L^2)-valued Nemytskii differentiability. Formula (F.41) tests the nonlinear remainder against a *fixed* incoming (L^2) weight, first bounds the weight on a truncation, then removes its tail. Every forward field difference is (O(\eta)), so the finitely many weighted remainders are (o(\eta)). Genuine adjunction gives the stated gradient blocks. Their continuity follows from bounded multiplier continuity, not from an unwarranted local Lipschitz assertion for the uncut backward map.

The strong curve chain rule likewise uses a bounded multiplier converging in probability against an (L^2)-convergent difference quotient. The operator product rule is valid because the learned action increment is differentiable in Hilbert–Schmidt norm, which controls operator norm. These arguments need only the stated bounded first and second activation derivatives. Finite uncut GF global existence follows from the finite-dimensional energy identity and the Cauchy endpoint argument; no bounded global vector-field hypothesis is being silently used.

## 2. Adaptive conditioning and singular sources

I checked the conditional independence argument in F.3 at its adaptive step. Conditional on the *whole current transcript*, a query input is fixed. The new answer is a linear observation of one residual matrix factor only. Starting from independent factors, successive conditioning therefore retains the product form for the residual factors of the other matrices. This is the correct filtration argument; it does not incorrectly assert unconditional independence of a query and its reused matrix.

In (F.6), the compatibility identity (U^TY=Q^TV) proves both constraints for (M). The homogeneous subspace is exactly (P_{U^\perp}KP_{V^\perp}); (M) is orthogonal to it. Isotropic Gaussian projection therefore gives the conditional law. The formula (F.7), including its factors of (n), follows from this decomposition. The removed fresh-noise projection has normalized mean square (operatorname{rank}(U)/n), so fixed transcript length is sufficient. Conditional variance estimates for tests and second moments then give the claimed empirical (\mathcal W_2) convergence.

For the source rule, the orthogonality of (h_\perp) to all old forward inputs removes the deterministic return terms of the old reverse answers. Gaussian integration by parts supplies (G_U E\nabla h_\perp). Substitution of the old forward source decompositions cancels the derivatives of the regression projection. The remaining source has covariance (E[hv_r]) and variance (E[h^2]), as required. Distinct orientation groups can be independent while actual answers remain dependent through their return terms. The proof preserves this distinction.

F.4 genuinely handles a singular limit. Each call receives a distinct fresh Gaussian input perturbation, whose limiting squared distance from the earlier same-orientation query span is at least (\varepsilon^2). At fixed (\varepsilon), the nonsingular proof applies. The same initialized matrices and roots yield a deterministic (C\varepsilon) normalized-array comparison on events of probability tending to one. Scalar node values and first named-source derivatives are continuous under covariance-square-root coupling and compact coefficient control. The proof does not differentiate a covariance and does not pass a pseudoinverse through a rank change. It also keeps zero-variance named slots, as needed later. The kernel-of-covariance identity (F.14) correctly explains invariance of contracted responses even when separate formal derivative coefficients are representation dependent.

The iid-root and Gaussian norm estimates suffice for all the finite-program uses here. The trace variance in (F.4c) has the correct factor (2/n^2), and the operator-moment bound justifies the stated polynomial-in-actions trace applications.

## 3. Common actions and true adjoints

The countable generated-language construction avoids an unjustified identification of operators on different finite widths. Finite unions of programs have consistent joint laws because unused instructions change no finite-array vector. On rational spans, the finite initialized norm event transfers (|Au|\le10|u|) to the deterministic limits. It also transfers linearity and shows that two expressions equal in (L^2) have the same answer.

The generated span is dense in the layer (L^2) space: finite-coordinate functions approximate arbitrary generated measurable functions, and the included bounded smooth functions approximate finite-coordinate functions after controlling tails. Thus both orientations extend as bounded operators. Passing the finite identity

\[
\langle v_n,A_nu_n\rangle_n=\langle A_n^Tv_n,u_n\rangle_n
\]

and then using density proves *genuine* adjunction on the whole space. All later learned increments are actual Hilbert–Schmidt rank-one integrals, with their genuine adjoints. Only these increments, rather than the initialized actions themselves, are required to be Hilbert–Schmidt.

Approximating arbitrary fixed Lipschitz coordinate instructions on large compact sets with a common linear envelope is sufficient for their inclusion in the same action spaces. The propagation uses the target instruction's Lipschitz constant and the bounded initialized action, rather than an unproved uniform derivative approximation.

## 4. Uniform source induction and gain constants

I checked S independently of the later bridge. Its primal stop uses only initialized action norms, the three unit-variance bottom projections, and raw displacement. In particular, no dimension-independent estimate of (|w_0|_2=\sqrt d) enters the gain. With (F=32^L), the bounds (|X_\ell|_2\le32^\ell), (|C(s)|_2\le3Fs), and (|q_\ell|_2\le32^{L-\ell}3FS) give the stated displacement (3\sqrt L F^2s^2). Positive Euler meshes satisfy the same estimate, including a proposed first overshooting node.

The decomposition in S.3 is on the actual coefficient arrays and actual covariance, which is essential. Writing (X=Y+u), (d=q+v), with (|u|\le2/K_\ell) and (|v|\le|q|), exact elimination gives the displayed (Y-Y_G) and (q-q_G). The row norm bounds for the triangular inverses follow from (alpha Sb\le1/8). Combining the independent (L^2) bound on actual (q) with Gaussian moments of (q_G) closes the (L^p) absorption. The (b/K_\ell) term explicitly retains the offset and cancels its possible curvature scale. The constants 20 and 60 are sufficient for (S.1)–(S.2).

The Jacobian recurrence retains the current reverse diagonal. Strictness of the forward array gives a Volterra recurrence rather than a same-time implicit loop. The bounds on a single reverse-source response include the needed (h_j), and the full forward-source row admits the stated exponential envelope. Minkowski controls the weighted time sum by (SW_\ell\sqrt p); no independence over times or moment of a random time maximum is assumed. The exponential estimate follows from the even-moment series and the factorial lower bound. These facts support both production bounds in (S.5).

The numerical box arithmetic is consistent:

\[
\alpha_\ell S\le3(32768/a)^LT,
\quad
\alpha_\ell S b_\ell
\le24576(2^{26}/a)^L64^{-\ell}T^2/a,
\quad W_\ell\le61b_\ell.
\]

The condition (a\ge10^{12}(1+T)), (L\ge2), gives substantially more than the quoted smallness. For example the largest resulting second-product bound is bounded by its (L=2,\ell=1) expression and (T^2/(1+T)^3\le4/27). The production radii have genuine slack: (17\alpha_\ell<32\alpha_\ell) and (514b_\ell<2048b_\ell).

S.6 resolves the important causal issue. Current forward production uses only completed past reverse rows and past (q)'s, through strict forward causality. Once the current forward sweep is complete, the top incoming row is known. Each downward step then uses the current incoming row already produced at the higher layer. Thus it never bounds an unknown current reverse row using a hypothesis that already requires that row. This supports mesh- and cap-uniform marginal source tails.

## 5. Geometry, global clock, uniqueness, and nonaffinity

For three samples, the augmented Gram lower bound is valid even with a singular input Gram. In the mixed-sign case the two-dimensional quadratic form has determinant (D^2), trace at most 4, and (D\ge\delta). The one-sign case is immediate from the constant component. This proves (G.1).

The Gaussian constant and linear projections are orthogonal also to the other coordinates of a singular Gaussian tuple. Boundedness of (\psi), through (|E\psi'(\sigma G)|\le1/\sigma), produces a summable loss (d_\ell=a^{-1}(2/a)^{\ell-1}), rather than a fixed per-layer loss. Therefore (Q_L(0)\succeq\lambda I) uniformly over all finite (L).

The controlled perturbation recurrence in (G.9) uses initialized norm 10 and gate norm 2, giving the ratio (20/32). It implies both the raw preactivation displacement (G.10) and Gram perturbation (G.11). The hidden differential/update product in (G.12) is bounded in absolute operator norm; no symmetry or positivity of the capped hidden term is presumed. The shared bound (54\,2^{40}T_0^2/a^4<\lambda/4) is valid under (M.4), and so are the displacement stop and source-box conditions.

The exact capped physical residual equation then gives the claimed exponential decay until the clock exit. Its integral yields (v(t)\le6/(\lambda a^L)=S/2), ruling out that exit. This gives global capped paths with cap-independent primal bounds. Passing S's source moments first for step controls and then by (L^1) approximation for measurable controls avoids invalid sampling of arbitrary measurable controls at Euler nodes. The autonomous population control is deterministic, so these estimates apply to it.

The comparison (V.7) uses only a tail of the capped reference. Each cap factor multiplies a forward state difference; downward substitution does not raise the cap to the depth. Consequently (e^{C_TR-cR^2}) defeats both the comparison Gronwall factor and the additional factor needed for restart. This establishes a strong (C^1) uncut limit and uniqueness against every bounded-primal strong competitor in the stated class. It does not require a general local Lipschitz theorem for the uncut (L^2) field.

For regression, optimal affine slopes of a 1-Lipschitz function lie in ([-1,1]), including a valid zero-slope choice for constant random variables. Thus the square root of the regression residual is 2-Lipschitz under an (L^2) coupling without any variance lower bound. The finite-interval residual is positive for some finite integer interval because a bounded globally affine function is constant. The Gaussian density bound gives (c_\psi/\sigma), with (1\le\sigma_\ell\le4a^{\ell-1}). The arithmetic in (G.25) reduces the displacement-to-margin ratio to at most (3/4); (A.11) gives an even sharper sufficient estimate. Absorbing the affine component and scaling by (e^2) proves (M.17).

## 6. Original finite algorithms and observation limits

The finite-program theorem is applied only to fixed auxiliary transcripts. Fixed-cap raw Lipschitz and Euler-defect constants are width independent on the prescribed primal ball. Rank-one unrolling gives finite primal events from primary coarse-node laws before the probe estimates use these events. The actual finite readout is retained: its (O_P(n^{-1})) normalized norm is removed by fixed-cap stability, not by changing either actual algorithm's initialization.

The Gaussian probe argument in V.4 perturbs actual answer slots and recomputes subsequent finite residuals and updates. A single past insertion produces an (h_j)-scaled later state effect, whereas a current query retains its direct forcing. Gaussian integration by parts after the fixed-program limit differentiates the explicit source expression with scalar feedback coefficients frozen, which is exactly the needed named-source derivative convention. Covariance-square-root continuity justifies the subsequent small-perturbation limit. Choosing deterministic signs bounds absolute *expected* response rows; the text correctly does not equate this with an expectation of the absolute derivative. V.5 subsequently derives the separate pointwise derivative-row bounds.

For velocity observations, the ascending action schedule is correct: the only opposite-orientation inputs of the new initialized action are its primary reverse inputs. New same-orientation sources retain all input covariances. The induction bounds derivatives only in the primary reverse sources relevant to the *next* action. Differentiating (g(Y)P) gives an integrable envelope (C(1+|P|)), and the actual response formula makes the relevant derivative row of (P) bounded. The coherent nested truncation order proves the derivative formula and empirical law before the unbounded product is used. This is stronger than, and does not incorrectly follow merely from, (\mathcal W_2) convergence.

The deterministic comparison (V.29) has one observation threshold factor, multiplying the already bounded forward discrepancy. At fixed cap, coarse-node fourth moments bound the reference positive-part tails, giving the mesh limit without needing finite-width fourth-moment convergence. Same-index coupling then gives uniform-time joint laws, and finite concatenation retains joint-time correlations.

True backward observations have a separate descending clipping argument in V.9. It uses bounded genuine adjoints and known incoming second-moment tails and makes no unproved claim about untruncated expected derivatives. Strong continuity of the true backward map makes the cap-flow time image compact in (L^2); its tails are uniformly removable. This supports every true raw kernel block, including off-diagonal entries and the bottom input-Gram factor.

For actual finite uncut GF, same-width comparison uses only the finite capped reference tails, whose width-limit bounds are supplied by the population source estimates. The same proof applies to original simultaneous raw GD: its direction is evaluated at its preceding fine node, and the capped within-step variation is the additional vanishing (\eta_n=n^{-2}) error. First-exit slack establishes the required finite-horizon bounds in probability. No width-independent Lipschitz estimate for the uncut field and no Gaussian theorem for a transcript growing with width are assumed.

Velocity cap removal uses the necessary order: width at fixed training cap and tail threshold, then training-cap removal at fixed threshold, then removal of that threshold. Uniform strong convergence of population cap velocities follows from compact tails of the uncut time image, so no uncontrolled dependence of fixed-cap high moments is multiplied by a cap-removal error. The actual GD field derivative is evaluated at its interpolated parameter state with its actual piecewise constant raw direction. The right-node and terminal-left conventions are consistent with the proof.

For whole paths, (V.38) is a direct pointwise estimate and provides a genuine (L^2) cost in the supremum path norm. The integrated RMS speed bounds and joint observation-grid laws therefore suffice for path (\mathcal W_2), rather than merely fixed-time weak convergence. Uniform velocity (\mathcal W_2) gives squared speed and cross-moment convergence, hence integrated speeds. Additional fixed generated probes are propagated by finite-program approximation and bounded actions/adjoints. All the limit orders preserve full-sequence convergence in probability and permit shared references for GF and GD.

## 7. Initial motion and kernel coefficient

The forward Grams in N.1 are strictly positive by the same augmented-input geometry and positive linear projection coefficient. At the top, (S_L\succ0) follows from full three-dimensional Gaussian support, the dense nonzero set of (H), and the fact that bounded nonconstant (\psi) has (\psi''\not\equiv0). This argument needs (L\ge2), as correctly stipulated.

The reverse source formulas (N.8)–(N.9) keep both the current curvature and next-layer return. Their covariance floor conditional on the forward tuple proves (S_\ell\succ0) down to the possibly singular bottom layer. Summing coordinatewise conditional variance bounds gives nonzero bottom raw motion even when the input Gram is singular. The Hilbert–Schmidt trace identity proves every higher matrix block is nonzero.

Nonzero sample fields at upper layers are not inferred solely from nonzero parameter blocks. N.3 supplies the separate primitive forward innovation. Its variance is regression of the *input* (T_j^{\ell-1}) on the feature span using uncentered input Grams. Conditional variances prove strict positivity at layer 2 and propagate it upward. The innovation is independent of the original forward tuple and the separate local reverse source group; its retained positive variance therefore cannot be canceled by the response terms. This proves every (U_j^\ell\ne0), and strict positivity of (\phi') then gives every (T_j^\ell\ne0).

N.4 supplies a coherent fixed-cap program for both backward and added forward queries. Its derivative (N.22) has a deterministic cap-independent bound (B^2C_{ji}^\ell). Removing backward caps in descending dependency order and forward caps in ascending order establishes the actual uncapped source recurrences and their derivatives. Bounded actions and positive-part tail convergence identify these formulas with the true uncut finite-array queries. Thus the initial-motion calculation does not invoke the bounded-derivative finite-program theorem directly on an unbounded product.

Finally, (C'(0)=3H), (b_i^\ell(t)/t\to3\beta_i^\ell), and the exact raw updates give (\theta_h'(t)/t\to9V). The strong chain and operator product rules yield the advertised field accelerations. Genuine adjunction gives (\langle H,T\rangle=\|V\|_{\rm hidden}^2), with the correct factor (d) in the original first block. The readout-gradient norm contributes (9t^2\|V\|^2), and the hidden-gradient norm contributes another (9t^2\|V\|^2). Their sum is exactly the coefficient 18 in (M.18).

## 8. Appendix and scope

The finite-interval class result uses a common positive margin and therefore a common gain without requiring compactness of an infinite-dimensional class. Compactly supported perturbations have initialized regression residual at most a constant times (1/\sigma_\ell), proving that the broad activation class cannot possess a positive lower margin uniform in depth.

The stronger class condition (A.14) is sufficient with the modified gain (A.15). For the displayed arctangent center, the regression residual is continuous and positive on finite positive scale intervals and has a positive limit (b^2(1-2/\pi)) at infinite scale. The uniform-norm regression stability estimate extends the resulting positive infimum to the stated open (C_b^2) ball. The derivative bounds of the center and the disjoint supported translates used to establish infinitely many independent directions are correct. Members need not preserve the center's tail limits or oddness.

The manuscript correctly limits its conclusions to each separately fixed finite depth and each fixed observation horizon before width tends to infinity. Sharing gain constants does not establish uniform convergence over an infinite activation class, a simultaneous width/depth limit, a time/width interchange, or a margin uniform as (e\downarrow0); none of those extra claims is made.

## Final disposition

**PASS for the exact audited hash.** The entire stated theorem, including its singular-input case, original finite algorithms, true kernels, velocities, whole paths, generated probes, all-layer/sample initial motion, and appendix refinements, is supported by the internal proof chain. I have no unresolved objection requiring a mathematical repair.
