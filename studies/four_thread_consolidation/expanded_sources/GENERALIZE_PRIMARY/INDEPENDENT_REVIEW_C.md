# Independent mathematical review C

Verdict: **PASS** for the stated fixed-depth, short-time theorem and its stated two-hidden-layer activity corollary. I found no major or minor mathematical gap requiring correction in the investigated obligations. This verdict does not assert an all-time result, a depth-uniform time interval, or activity beyond the separately stated Gaussian-initialization, zero-readout, two-layer setting.

I read the solve-math-rigorously skill and independently checked the supplied proofs. The supplied activity audit was treated as a collection of claims to verify, not as evidence that its verdict was correct. No other reviewer was contacted.

## Reviewed versions

SHA-256 hashes, including the newly inserted activation examples:

- `GENERAL_POPULATION_GF_PROOF.md`: `792dbd8eca426dc8fd5434d67b183826025a7a301f42fd579d6332fa458005e2`
- `GENERAL_DEPTH_RESPONSE_PROOF.md`: `3dfb63e3cac21ee15573af7f4107287f58dc2013db7e4a11083c90472bf8995b`
- `ACTIVITY_SOURCE_AUDIT.md`: `3d91ef619477525519a7faacd293418b15e7f2f24699ed871df6eef11b194421`
- `/tmp/GENERAL_ACTIVATION_ACTIVITY.md`: `c6bfa76ac200ce59f91109b31a40d22d668ec678e2ea60386f93f7d7604b4e89`

The first three paths are relative to `/tmp/pde-gf-supervisor-worktree`.

## Primary-source verification

I directly checked [Tensor Programs III](https://arxiv.org/pdf/2009.10685), Setup 2.2, Box 1, Theorem 2.10, and Remarks 2.11–2.12. Its fixed-program hypotheses permit the stated Gaussian matrices, jointly Gaussian initial vector slots, polynomially bounded coordinate operations and measurements, and covariance degeneracy. Its formal derivatives follow the written program; they do not differentiate deterministic expectation coefficients. The opposite matrix orientations have independent Gaussian slot families but retain the stated response corrections. This source is being used only for fixed computations.

I also checked [Tensor Programs IVb](https://arxiv.org/pdf/2308.01814), Definition 2.6.7 and Propositions 2.6.8–2.6.9: the cited operator interpretation, boundedness, and adjoint statements are accurately described. The main proof also gives its own operator-norm passage from finite matrices, so these propositions are corroboration rather than a replacement for the construction.

## Exact response and sensitivity obligations

The depth note's equations (6)–(11) pass. Expand the trained matrix into its initial matrix plus the accumulated rank-one updates. In a forward call at time k, the initial matrix's opposite-direction source slots can only be earlier backward calls, hence s<k. In a backward call, current forward calls have already been constructed, hence s<=k. This gives precisely the two summation ranges. The training term in F uses the H/H contraction, whereas the training term in D uses the delta/delta contraction. Both have factor -2 kappa Delta omega_b r_b,s, with no additional initialization variance. The variance multiplies only the initial-matrix response coefficients and Gaussian covariances.

The same input's current backward quantity can depend on other current input slots through the higher response. These derivatives are retained in the full row sum (23)–(25); no diagonal-only approximation has been made. Singular covariance does not invalidate the formal-slot differentiation: the written program is retained, and a null-direction change has zero resulting source combination in L2.

The bounds (24)–(28) close without taking a maximum of random backward fields. For every target derivative row, the memory bound is entrywise in the source input and time. Taking the maximum of derivative row sums therefore leaves the weighted scalar sum Delta sum_u sum_b omega_b |P_b,u| in (26). This is exactly the quantity controlled by Jensen in (14).

The single backward-slot calculation (29)–(32) also passes. Its direct derivative is the one indicator at (b,s); insertion into the first-layer update or the lower forward memory produces a source pulse proportional to Delta omega_b. Every subsequent term multiplies the same derivative maximum by a weighted time sum. Thus the factor Delta omega_b survives Gronwall. There is no hidden inverse weight, unweighted input count, or maximum-over-history Gaussian estimate.

## Noncircular field and tail bounds

The preliminary RMS/operator ball is independent of the response analysis. It bounds each Gaussian slot's variance through its source second moment, so the constant K in (18)–(21) can indeed be chosen before the response caps.

At a fixed mesh, finite causal magnitude recursions give finite subGaussian norms: activations have linear growth and the backward activation derivative is bounded. This observation does not establish uniformity, but it legitimately makes the subsequent induction available.

The cap order (33)–(35) is noncircular. First choose the C caps from their zero-time prefactors, which depend only on lower C caps. Then choose the A caps downward from the top layer, matching B_P,ell + d_ell = (4K+1)(1+a_ell+1) below the top. All remaining occurrences of the opposing caps are multiplied by T or T squared in the exponents. A sufficiently small positive T consequently improves every response bound by a factor of two.

The literal construction order supplies the hypotheses at the step where each estimate is used: current forward C coefficients use past backward fields and already constructed lower forward coefficients; current backward A coefficients use already constructed upper backward quantities. The initial step starts with no forward response memory and the prescribed readout root, including nonzero-mean and unbounded subGaussian readouts.

The moment-to-exponential estimate (13) has the stated constants: its r-th nonconstant series term is at most 4^(-r). Jensen (14) needs only marginal bounds, not temporal independence. The resulting Gaussian cutoff tail follows after reducing its exponential constant. The variable-step extension correctly retains the source step length and uses only total elapsed time; appending a fractional final update therefore controls a recomputed interpolation-time field.

## Existence and convergence bridges

The common realization and operator construction pass. Joint fixed-program laws for finite unions are consistent; the countable generated family and its L2 closure provide a common domain for comparing Euler meshes. Finite operator inequalities pass to the generated span by second-moment convergence. Passing the finite adjunction identity identifies the two extended maps as adjoints. No convergence in operator norm between a finite matrix and a population operator is asserted or needed.

The localization estimate has linear cutoff growth, C(1+R), rather than a power R to the depth. A new derivative-difference cutoff is added at each backward layer; previously accumulated differences are multiplied only by bounded derivatives and operators. The resulting factor exp(CRT) is dominated by the reference tail exp(-cR squared). Therefore the two-mesh estimate makes Euler paths Cauchy with the stated order of limits.

Continuity of the bounded-multiplier product on L2 is sufficient for the strong integral equation. The fixed-factor truncation argument establishes it without claiming Frechet differentiability of the activation map on L2. Fatou transfers the marginal exponential bound to the constructed flow. The one-sided reference estimate then proves uniqueness against an arbitrary competing strong solution on the same initial state, without assuming tails for that competitor.

The finite oracle/proxy comparison passes. At a fixed coarse mesh, only finitely many scalar contractions differ between prescribed oracle matrix actions and recomputed proxy actions. Their errors vanish, and multiplying them by bounded RMS source vectors preserves this conclusion. Backpropagation can be transferred downward using oracle reference tails; higher moments of actual GD are unnecessary. The proxy's assigned grid velocity is consequently consistent with its recomputed vector field. Comparing assigned fine- and coarse-grid velocities gives (12), with the additional O(eta_n+Delta) time discretization error. The stated limit order removes this error for every eta_n tending to zero.

The extra observables are supported by the same estimates. After state stability, parameter velocities converge and the recursive hidden-velocity formula is continuous in state and velocity. Its compact population range has uniformly integrable squared tails. Fixed-mesh oracle cutoff moments transfer the bounded-multiplier steps, establishing integrated squared-speed convergence. Separately, the uniform RMS speed bound gives the stated O(epsilon) squared error for time-grid reconstruction. Joint fixed-time Wasserstein-2 convergence plus this reconstruction proves Wasserstein-2 convergence for the uniform path norm. Lipschitz activations transfer the conclusion to hidden activation paths. The restrictions on probe products suffice for the same cutoff induction.

The kernel normalizations and loss identity (13) agree with the stored learning rates and the normalized loss. The block products use two normalized contractions for middle matrices. The first block additionally carries G, and the readout block has a single hidden contraction.

## C1,1 and initialization scope

The mollification estimates are correct and preserve bounded first and second derivatives uniformly. The value at zero remains uniformly controlled by the original bounds for smoothing scales at most one. Comparisons across smoothings add an error of order (1+R)(epsilon+epsilon'), so the ordered limits construct and uniquely identify the original C1,1 flow and its finite-width limit. The added exact GELU and SiLU derivative formulas are correct; the quadratic-smoothed ReLU has continuous, bounded, 1-Lipschitz derivative and fails second differentiability only at the stated junctions.

Scalar subGaussian root encoding passes: the quantile of a subGaussian law at Phi(g) is linearly bounded in |g| using the Gaussian lower tail bound. Atomic/asymmetric laws cause no problem. Encoding fixed-dimensional first-weight rows coordinatewise preserves their independence, and centered independent subGaussian projections have the claimed dimension-free marginal bound. No derivative through these initial transforms is used. This establishes the stated first-weight/readout extension, not non-Gaussian middle-matrix universality.

## Strict two-layer activity and weighted constants

I independently verified the activity argument and its weighted translation. Put p_a=omega_a y_a in the onset fields and the tested kernel direction, while keeping the physical kernel blocks unchanged. Then the readout starts at 2 kappa_3 t S, both backward fields start at 2 kappa_3 t times their stated U/B fields, and the hidden displacements have the stated 2 kappa_3 t squared factors, including kappa_1 in the first layer. The total-kernel quadratic-form coefficient is 8 kappa_3 squared (kappa_1 A_1+kappa_2 A_2), and -dot L(0)=4 kappa_3 E S squared.

The finite-difference ridge argument establishes Q positive definite for bounded nonconstant activations. Differentiating a putative ridge relation extends it to nonaffine C1 activations with bounded derivative. The argument for V uses full support and continuity through the zero set of S; it remains valid when activation derivatives vanish on intervals. Nonzero labels mean every p_a is nonzero.

The reused-transpose law has the full Gaussian covariance sigma_2 squared V, together with its deterministic response. Conditioning the next forward call on the earlier forward and adjoint calls yields the stated fresh variance sigma_2 squared E[(A_a perpendicular) squared]. Removing finitely many output directions does not remove this normalized-coordinate variance. The conditional-variance bound gives E[(A_a perpendicular) squared]>0, because its diagonal source coefficient p_a(phi_1'(Z_0,a)) squared is nonzero with positive probability. The learned-matrix contribution cannot cancel the independent fresh Gaussian term.

This also verifies actual activation motion: A_a is nonzero in L2, and multiplying the second-layer fresh component by phi_2'(Y_a) leaves positive variance. Directional L2 chain rules give the corresponding positive order-t RMS speeds. The positive-definite Schur products establish the first two kernel blocks; full support establishes the initial readout block. The positive weighted-label coefficient prevents cancellation in the total kernel. Gaussian support and nonaffinity give strictly positive initial affine-fit errors, which persist by L2 continuity.

These strict conclusions use Gaussian first weights as explicitly declared in the main theorem's initialization discussion. Arbitrary subGaussian first roots need not meet their support/nondegeneracy requirements. No general subGaussian, nonzero-readout, or arbitrary-depth strict-activity conclusion has been inferred.

## Required revisions

None for the investigated mathematical obligations in the versions identified above.
