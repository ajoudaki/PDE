# Independent adversarial review: final manuscript

**Verdict: PASS.** I find Theorem M.1, including its exact finite algorithms and all stated observation limits, justified by the manuscript's internal argument. I find no unresolved mathematical objection requiring a repair. The additional assertions in Part A are also justified with their stated quantifiers.

## Isolation and full-read confirmation

- Sole mathematical source: `/tmp/hidden_depth_final_20260908/manuscript.md`.
- SHA256 independently checked: `efa3c2b1e592a469d8aa7900e95f0a8a43a4a1865b9c4c3f69f3bacfcb613e4a`.
- Size checked: 2,864 lines, 178,181 bytes.
- I read every line, in contiguous ranges 1–360, 361–720, 721–1080, 1081–1440, 1441–1800, 1801–2160, 2161–2520, and 2521–2864. Thus Parts M, F, S, G, V, N, and A were all read in full.
- I used no other manuscript, report, conversation, author note, skill, reviewer, or subagent as mathematical context. No numerical experiments were performed.
- No specialized external theorem was needed as an unproved premise. Accordingly, no external text was retrieved. The Gaussian conditioning, singular-query extension, common action construction, derivative facts, and approximation bridges are proved internally.

## Obligation audit

### 1. The declared raw metric, GF, and actual GD are preserved — PASS

The first-layer Euclidean derivative of a predictor is `b x^T/n`; inversion of the metric coefficient `d/n` gives the displayed `b x^T/d` update. Higher matrices retain their `1/n` update, and the readout metric cancels its Euclidean `1/n`. This verifies (M.9)–(M.10), rather than merely checking a rescaled surrogate algorithm.

The coordinate substitution `w = sqrt(d) W^1` is an isometry because `||Delta w||_n^2 = (d/n)||Delta W^1||_F^2`. Its bottom field is `w dot u_i`, and its raw direction is the claimed sum of `b_i u_i`.

Part F.8 correctly identifies the Hilbert–Schmidt norm at finite width with the ordinary Frobenius matrix norm when both vector spaces have normalized inner products. In particular the rank-one operator is `v h^T/n`, not `v h^T`.

GD is consistently the simultaneous Euler scheme for this same raw GF, with physical step `n^-2`. V.8 and V.10 keep its actual preceding-node direction, and V.11 evaluates hidden derivatives at the interpolated raw state in that direction. The proof does not substitute the field at the interpolated state for the actual GD direction.

Finite GF global existence follows from its exact energy identity and the resulting finite-horizon length bound. This is legitimate in finite-dimensional raw parameter space. GD is an everywhere-defined finite composition, while its necessary high-probability horizon bounds are proved separately by comparison.

### 2. Hidden normalization and true observation scalings — PASS

Direct substitution gives `Y_l = A_l X_(l-1)` and `X_l = chi_l(Y_l)`, with `chi_l' = 1 + (e/a) psi'(a^(l-1) Y_l)`. The original readout is unchanged and `f_i = a^L F_i`. Hence the factor `a^L` multiplies the raw scalar differential in every block, not just one block.

The backward induction gives exactly `b_raw,l = a^(L-l+1) d_l`. Multiplying this by the original preceding feature scaling gives `a^L` for every raw hidden gradient. Consequently all kernel blocks in V.34 have the common factor `a^(2L)`. I checked the bottom block's additional input Gram and the readout block independently.

The large physical factors are fixed constants in the width limit. Neither a changed learning rate nor a changed readout metric is hidden in the normalization.

### 3. Fixed finite Gaussian programs and reused transposes — PASS

F.3 conditions successively on the actual adaptive transcript. At a matrix query the input is transcript measurable, so the additional observation constrains only that matrix's remaining conditional Gaussian factor. The product structure of the other residual factors is preserved. This supplies the needed justification for adaptive queries; the proof does not assume unconditional input/matrix independence.

The conditional mean in F.6 satisfies both forward and transpose constraints and is orthogonal to their homogeneous solution space. The remaining Gaussian projection has normalized squared mean `rank(U)/n`, which vanishes for a fixed transcript. This validates the nonsingular-query induction and its empirical second moments.

The source-response calculation correctly cancels the forward regression's derivative terms by Gaussian integration by parts. Sources in opposite orientations are independent primitive groups; actual answers remain dependent through their response corrections. The full uncentered input Gram is used as each centered source covariance.

F.4 regularizes every query with a fresh independent input noise. At fixed positive noise the query Grams have positive Schur complements. The same-width error is `O(epsilon)` on the bounded operator event. The limiting source recursion is then continuous through covariance square roots and bounded first derivatives. This avoids a rank-stability or pseudoinverse-continuity assumption. Keeping named slots distinct at singular covariance is supported by F.14's nullspace cancellation.

The scalar-feedback extension is causal: the oracle coefficients are built from prior deterministic limits, and same-width norm estimates transfer them to actual coefficients. There is no implicit fixed point in this step.

### 4. Common spaces, bounded actions, and actual adjoints — PASS

The countable generated language has consistent finite marginals, because finite unions are covered by the finite program theorem. The high-probability finite operator bound transfers to every generated input and then to the dense span. Completion therefore produces bounded initialized actions with norm at most 10. Finite transpose identities pass first on the generated span and then by density, proving that the reverse actions are genuine Hilbert adjoints.

Only learned increments are required to be Hilbert–Schmidt. The initialized operators themselves are not incorrectly required to lie in that class. The rank-one integral estimates give actual Hilbert–Schmidt increments and preserve adjunction through time.

The density/approximation argument also covers additional fixed Lipschitz coordinate instructions and real coefficients. No cross-width identification of operators is asserted or needed.

### 5. Strong derivatives and the scalar raw gradient — PASS

F.5's multiplier statement uses a tail split on the fixed limiting `L2` multiplier input. This is sufficient for its claimed strong convergence. F.6 is a chain rule along strongly differentiable curves, and does not make the false stronger claim that an arbitrary nonlinear Nemytskii map is Fréchet differentiable from all of `L2` to `L2`.

F.7 proves the needed *scalar* Fréchet derivative separately. The weighted Taylor remainder is split between a bounded part of the fixed incoming weight and its `L2` tail. Forward increments are `O(eta)`, and the downward weighted expansion has finitely many `o(eta)` remainders and `O(eta^2)` mixed action terms. This gives the displayed gradient blocks. Multiplier continuity proves continuity of those scalar gradients.

It follows that an uncut strong solution is truly the raw gradient flow of the declared loss, with the true kernel and energy identities. Existence of that solution is not circularly assumed in this differentiation argument.

### 6. Independent primal bounds and depth-uniform source estimates — PASS

S.2 establishes primal bounds before using source estimates. On the hidden displacement stop, current operator norms are at most 11, forward norms are bounded by `32^l`, backward growth by `32^(L-l)`, and every hidden block speed by `32^L ||C||`. Integration gives the stated `3 sqrt(L) 32^(2L) s^2` bound. For Euler, only past states enter the proposed update, so the strict bound excludes a first overshooting node as claimed.

S.3 uses the actual coefficient arrays in its triangular elimination. The bounded activation offset contributes at scale `1/K_l`, while the possible derivative growth is at scale `K_l`; the factors cancel in the moment production. The Gaussian part is bounded using its actual covariance and the independent primal `L2` bound. The absorption uses `2r < 1`, and the constants 20 and 50 exceed the resulting coefficients.

The exponential derivative envelope in S.4 is controlled by marginal subGaussian moments and Minkowski for the weighted time sum. It does not require temporal independence or a moment bound for a random maximum over all times. The conversion from `||Z||_p <= M sqrt(p)` to the exponential moment is justified by the displayed series/factorial estimate.

I checked the box arithmetic in S.5. In particular

`alpha_l S b_l <= 24576 (67108864/a)^L 64^(-l) T^2/a`,

and `n_l <= B0 <= b_l/2048`. Therefore `W_l <= 61 b_l`, and the selected depth-independent lower bound on `a` supplies the small gain conditions uniformly for every finite `L >= 2`. The forward and reverse production inequalities lie strictly inside the next boxes.

### 7. Chronological closure, including current reverse rows — PASS

This is a central dependency check. In S.6, the forward construction at time `k` uses `q_l,r` and the incoming reverse rows only for `r < k`. Strict lower triangularity of the forward row is exactly what makes that statement true. Consequently its derivative envelope and forward production estimate are already available from the completed prefix.

After all current forward rows are known, the current top incoming row is the readout integrator. The reverse sweep then produces the next incoming row before it is needed at the following lower layer. At each such step the complete local prefix has both its forward and incoming reverse rows bounded.

Thus neither sweep assumes the bound of an unknown current row in order to produce that same bound. The zero-readout base stage also closes: current backward values and their forward-source derivatives vanish at time zero, even though distinct zero-variance slots remain formal slots.

### 8. Gram geometry, total control clock, and all-time bounds — PASS

The three-input augmented Gram bound is valid even for singular input Gram matrices. In the mixed-sign case its two-variable matrix has determinant `D^2` and trace at most 4 for `D in [delta,2]`; its least eigenvalue is therefore at least `delta^2/4`. The one-sign case also satisfies the claimed lower bound.

The Gaussian constant/linear projection leaves a positive semidefinite residual Gram. Crucially, boundedness of `psi` gives `|E psi'(sigma G)| <= 1/sigma`, so the losses in the normalized linear coefficients are summable in depth. This yields the initialized floor `lambda = delta^2/16` without accumulating a fixed factor at each layer.

The perturbation recurrences G.9–G.12 follow from bounded initialized actions and raw displacement. I checked the principal bound `54 * 2^40 T0^2/a^4 < lambda/4`; it follows from the selected `a` and `T0 = 12/lambda`. The displacement stop has strict slack as well.

For capped physical paths, the hidden residual coefficient need not be symmetric. G.17–G.18 use its absolute operator bound, while the readout contribution retains the positive Gram. This is sufficient to obtain `d||r||^2/dt <= -lambda a^(2L)||r||^2`. Its residual clock is at most `6/(lambda a^L) = S/2`, excluding a first exit at `S`.

The transfer of controlled moment estimates to capped physical paths is justified by step-control approximation in `L1` and fixed-cap stability. It does not sample an arbitrary measurable control at Euler nodes. Capped paths and their residual controls are deterministic population objects, so this use of the controlled estimates is legitimate.

### 9. Population cap removal, uniqueness, and continuation — PASS

V.7's gate comparison places all tails on the capped reference. In its downward recursion each new factor of `R` multiplies a forward state discrepancy already bounded directly by raw distance. It never multiplies the preceding backward discrepancy. The resulting Lipschitz factor is `C(1+R)`, rather than `R^L`.

The uniform source moments give Gaussian-decaying reference tails. Gronwall therefore produces `C_T exp(C_T R - cR^2)` for both states and raw derivatives. This is sufficient for a strong `C1` uncut limit and identification of its equation.

The same one-reference comparison applies to a bounded-primal strong uncut competitor without demanding tails of that competitor. At a reached state the small mismatch with the capped reference remains small after the additional exponential factor. This proves precisely the stated uniqueness and restart class. The argument does not claim arbitrary-state local Lipschitzness of the uncut infinite-dimensional field.

### 10. Actual random readout and finite GF/GD bridge — PASS

The actual finite readout has normalized RMS `O_P(n^-1)`. It is retained in both algorithms and in same-width comparisons. It is compared with the zero-readout auxiliary program only at a fixed cap and fixed transcript, where Lipschitz stability is valid. Thus the zero population initialization is a proved limit, not an algorithmic reset.

V.3 obtains the finite primal events from fixed-mesh primary laws and explicit rank-one unrolling before using Gaussian probe estimates. V.8 compares actual capped GF and fine Euler to that fixed auxiliary mesh using width-independent fixed-cap constants. This avoids applying F.1 to `O(n^2)` training steps.

For actual uncut GF and GD, V.10 uses the capped reference's uniformly converging incoming tails, the same-width version of the one-cap-factor estimate, and strict primal slack. For GD, V.36 correctly bounds the preceding-node discrepancy by the running supremum, and includes the reference's within-step variation. No width-independent Lipschitz estimate of the uncut vector field is assumed.

The order is fixed cap, width limit after its auxiliary-mesh bridge, and then cap removal. Every fixed-program result is full-sequence convergence in probability; subsequent deterministic error bounds preserve that mode. Coupling both actual algorithms through their common initialization gives their joint conclusion.

### 11. Fixed-cap response probes and velocity products — PASS

V.4's Gaussian forcing is inserted into actual answer slots, with all subsequent raw updates and residuals recomputed. Its stability bound includes that feedback. At the scalar limit the coefficients are deterministic, so Gaussian integration by parts legitimately freezes them. Choosing signs after taking the unperturbed expected derivatives bounds absolute expected derivative rows. This does not substitute `E|partial V|` for `|E partial V|`.

The explicit descending formula V.18 retains the current return at every layer. V.19–V.20 then bound pointwise source rows without a same-time algebraic loop.

The appended velocity schedule is ascending in layer. At each new action, the relevant opposite-orientation inputs are primary backward fields already known. The new Gaussian source variance is the already bounded input velocity norm. The response row is controlled by the lower-layer derivative invariant, giving the needed marginal moment estimate before advancing to the next layer.

The unbounded gate products are not directly fed into F.1. V.27 gives their exact clipped derivatives. At a new layer the previous inner observation caps are removed while the outer cap stays fixed, then the outer cap is removed using the established integrable envelope. The argument therefore establishes derivative convergence rather than inferring it from `W2` convergence alone.

### 12. True backward observations and true raw kernels — PASS

V.9 closes the true backward chain independently from capped training gates. Each product is first clipped, its finite law is obtained, and its input tails are removed before the next actual adjoint action is applied. Bounded action norms and positive-part tail convergence suffice for this finite observation induction.

The uniform-time passage uses compact `L2` time images of the true backward map. Compactness yields uniformly vanishing tails, so no unproved high-moment bound for the uncut true chain is required.

All off-diagonal sample contractions are included in the same-layer joint laws. Their continuity under `L2` couplings gives every entry of every raw kernel block. The manuscript explicitly distinguishes this observed true gradient kernel from the generally nonsymmetric coefficient matrix governing capped dynamics.

### 13. Velocity cap removal and complete limit order — PASS

V.29 is an upward recurrence with one factor of the velocity tail threshold `M`; each new `M` multiplies a forward discrepancy, rather than a preceding velocity discrepancy.

For population cap removal the reference is the uncut path, whose continuous `L2` velocity image is compact. Taking training cap to infinity at fixed `M`, followed by `M` to infinity, proves uniform strong velocity convergence and transfers tail compactness to large caps.

The finite comparison V.37 then uses width at fixed cap and `M`, cap removal at fixed `M`, and finally `M` removal. It does not multiply the cap-removal error by a potentially uncontrolled fixed-cap fourth-moment constant. This resolves the most delicate order-of-limits issue in the velocity claim.

### 14. Full path `W2`, integrated speeds, and probes — PASS

Joint laws at finite time lists alone would not establish the path claim. V.38 supplies the additional ingredient: the supremum interpolation error squared is bounded by `4h` times the integrated squared coordinate speed. RMS speeds are bounded on the common no-exit primal/direction event, and corresponding population paths have finite supremum second moment.

The already proved joint-grid `W2` laws pass through the finite interpolation map. The triangle inequality with the interpolation costs, first width and then observation-grid refinement, proves the full path `W2` assertion in the supremum norm.

Uniform-time velocity `W2` convergence gives squared RMS speeds and within-layer cross second moments, hence their time integrals. GD's endpoint conventions affect neither the comparison nor the integrals. Its blockwise raw direction identity is correctly evaluated at the preceding node.

Fixed generated probes are closed under their finite typed instruction graphs by bounded-derivative coordinate continuity, contractions, and bounded current/initialized actions in both orientations. Strong approximation and finite time nets cover the claimed finite lists and joint-time observations.

### 15. Nonaffinity and the activation selection — PASS

The regression stability estimate uses the optimal affine slope bound `|c_X| <= 1`, which follows from the independent-copy covariance formula and the Lipschitz constant of `psi`. Thus it needs no variance lower bound and also covers constant random variables.

A bounded nonconstant `psi` has positive affine residual on some finite interval. Restricting the Gaussian regression integral to that interval gives `c_psi/sigma`, and the initialized marginal variance bounds give the depth-dependent initial margin.

I checked the comparison of raw displacement with that margin. With `q = 32768/sqrt(a)`, the worst finite depth is controlled by the `L=2` geometric estimate, and the second condition in M.4 makes the G.25 ratio at most `3/4`. Regression stability therefore gives M.17 for all samples, layers, and times. Adding the affine part of the activation and multiplying its perturbation by `e` has exactly the asserted regression effect.

### 16. All hidden blocks, all samples/layers, and kernel coefficient 18 — PASS

N.1 proves positive definiteness of every feature Gram from the constant and linear Gaussian projections, including singular bottom input Gram. The top preactivation tuple has full support because `L >= 2`.

The top backward Gram is positive definite: vanishing of a linear combination of the top backward fields gives a product of two continuous functions vanishing everywhere. The signed feature sum has no open zero set because each of its coordinate derivatives is nonzero. Therefore the derivative combination vanishes identically, and nontrivial `phi''` forces each coefficient to vanish. Bounded nonconstant `psi` ensures `phi''` is not identically zero.

The descending backward source formula includes the curvature term and the next-layer return. Its independent Gaussian reverse component has the full uncentered incoming Gram. Conditional covariance therefore propagates strict positivity through every lower backward Gram, proving positivity of each hidden parameter block and each bottom sample motion.

For upper samples, N.14 is derived with the exact transpose response. The variance in N.15 is the distance of the actual added forward-query input from the span of the three original forward inputs, with no incorrect centering/intercept. At the first upper layer this distance is positive by the bottom reverse conditional variance. At later layers the previous independent innovation survives multiplication by a derivative bounded below, proving the next positive innovation. The new forward remainder is independent of the displayed original forward tuple and the separate reverse group, so it cannot cancel the other terms in the sample acceleration.

N.4 gives a coherent clipped program for these extra forward queries and their reverse inputs. Its bounded derivative formula N.22 and coefficient recurrence N.23 justify the untruncated source recursions with only `C2` regularity.

Finally, the strong right derivative calculation gives `C(t)/t -> 3H`, `b_i^l(t)/t -> 3 beta_i^l`, and hidden parameter acceleration `9V`. Strong chain rules give the corresponding `9U` and `9T` for every sample/layer. Genuine adjunction yields `<H,T> = ||V||_hidden^2`. The readout-gradient Gram contributes `9 t^2 ||V||^2`, and the hidden-gradient Gram contributes another `9 t^2 ||V||^2`, giving exactly 18 in M.18. Every hidden block of `V` is strictly positive.

### 17. Additional activation classes in Part A — PASS

The function perturbation and variable perturbation estimates are correct distances to the affine subspace. A common interval residual supplies a common gain with the stated arithmetic; the stronger layer-specific bound A.12 is consistent with the main theorem's weaker depth bound.

For a compactly supported nonzero perturbation, the initialized residual is at most a constant divided by its increasing marginal standard deviation. Thus the claimed obstruction to a positive margin uniform over all depths already holds at initialization.

For a bounded continuous function with distinct tail limits, A.17 is the exact Gaussian affine-regression formula. Its limit is `b^2(1-2/pi)>0`, and positivity at each fixed scale plus continuity on a compact interval yields a strictly positive infimum over all scales at least one. The normalized arctangent example, its derivative norms, the open-ball margin, and the disjoint-support bump construction are correct. No compactness of the infinite-dimensional function class is assumed.

## Quantifier check and final assessment

The proof establishes one selected activation gain and perturbation amplitude for all separately fixed finite depths. Its width, mesh, cap, and observation constants may depend on the fixed depth and horizon, as the theorem expressly allows. It makes no simultaneous increasing-depth width claim, no exchange of infinite time and infinite width, and no uniform width convergence over an infinite activation class. The weaker nonaffinity margin for the broad class and stronger margin for the special class are kept distinct.

**Final result: PASS. No theorem repair is required by this audit.**
