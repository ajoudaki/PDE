# Frozen gain theorem: adversarial geometry review

Date: 2026-09-08. Reviewer: `/root/three_depth_review_geometry`.

**Mathematical verdict: PASS for the complete frozen gain theorem below. Scope verdict: OUTSIDE THE USER'S ACCEPTED ACTIVATION CONSTRAINT.** The user subsequently rejected overall activation gain. This audit is retained as an assessment of the separately identified gain theorem; it is not a solution of the accepted near-identity/unit-sum problem. No gain sharpening or candidate editing was performed.

## Exact candidate checked

All five files were read, and their SHA-256 values agree with `CANDIDATE_HASHES.json`:

| File | Checked SHA-256 |
|---|---|
| `CONTRACT.md` | `219ea670b8e19a8d350ca74003fc9dc46933ce64563d199bbb4bef55fe644d90` |
| `PROOF.md` | `e8088b9554332c2d45250dec5e1b0004badb0252e5cfe63cefde0f8896e59f66` |
| `SOURCE_RESPONSE.md` | `c4dd77974660a1c7f556042f748c348af1fd3c2953d2e7220d508ee0960286f9` |
| `INITIAL_MOTION.md` | `dc4260ff571a3182362af01606706d7e0077d34d7552f0192ab340333a5fb12d` |
| `POPULATION_LIMITS.md` | `e7982d74e4004973ac3cdaa20715c9ad70fb9fd4ba04ad5b36e78fa8a222713c` |

The audited activation is exactly

\[
\phi_\delta(z)=a_\delta(z+\arctan z),\qquad
a_\delta=10^{10}/\lambda,\quad
\lambda=\delta^2/(324\pi e).
\]

The verdict covers every fixed finite hidden depth `L>=2`, all feasible three-input datasets satisfying the stated absolute angular separation, arbitrary binary labels, and every conclusion in PROOF.md's theorem. It does not cover a depth growing with width, uniform finite-width estimates in depth, an infinite-time/width interchange, a relative nonaffinity bound, or a unit-sum convex mixture. No experiment was run.

## Geometric and quantitative checks

1. **Singular input geometry.** Each unit tensor `R_i=u_i tensor v_ij tensor v_ik` annihilates the other two cubic input tensors. Its pairing with the i-th tensor is at least `delta(2-delta)`. Applying Cauchy--Schwarz separately for all three coefficients proves the exact lower bound `Gamma^(circ3) >= delta^2(2-delta)^2 I/3`. No positive definiteness or inverse of `Gamma` enters. In particular, planar triples with singular input Gram are included.

2. **The explicit cubic constant.** Gaussian integration by parts gives
   `E[atan(sigma G)H3(G)] = -2 sigma^3 E[G^2/(1+sigma^2 G^2)^2]`.
   The substitution `x=sigma G` removes the power of sigma. Restricting the resulting integral to `[-1,1]` and using `(1+x^2)^2<=4` gives `b3(sigma)^2 >= 1/(108 pi e)` for every `sigma>=1`. Projection onto cubic Gaussian chaos therefore proves `Q_1(0)>=lambda I`. The subsequent first-chaos projection has regression coefficient at least one in normalized coordinates, so the same lower bound survives every initialized layer.

3. **Raw normalization and control.** The rescaling of fields leaves the actual parameters and metric unchanged. `grad f_i=a^L grad F_i` produces exactly the physical time and accumulated residual-clock formulas in PROOF.md. The zero readout used in the population proof is justified by a separate fixed-cap comparison to the actual finite Gaussian readout; it is not substituted into either actual finite training algorithm.

4. **Primal estimates.** Until joint hidden displacement one, the adjacent norm bound four and activation Lipschitz bound two give the displayed `8^ell` forward bounds. Each hidden controlled block has speed at most `F ||C||`, with `F=8^L`; integrating `||C||<=3 F v` gives the claimed conservative bound `D<=3 sqrt(L)F^2 v^2`. Telescoping with the initialized actions yields the stated feature displacement, top Gram perturbation, and original-coordinate displacement. The inequalities in (19) hold uniformly for `L>=2` with `a=10^10/lambda`; the decreasing geometric sequences used there have substantial strict slack.

5. **Clipped fitting is not treated as GF.** The clipped hidden contribution `J_h U_h,R` need not be symmetric or positive. The proof uses its absolute operator bound, together with `Q_L>=3lambda I/4`, to get the residual decay. Integration gives a residual budget at most half the stopped control interval. This is a valid first-exit argument independent of a clipped energy identity. Endpoint continuation applies to the locally Lipschitz capped field.

6. **Original-coordinate absolute nonaffinity.** An optimal regression slope of `atan X` against `X` lies in `[0,1]`, by the independent-copy covariance identity. Hence the square root of the optimal squared residual is one-Lipschitz under an `L2` coupling. Every initialized raw Gaussian marginal has standard deviation at least one; the cubic bound applies at that actual scale. The original-coordinate displacement in (18)-(19) is less than `sqrt(eta0)/2`. This proves `R(z_i^ell(t))>=eta0/4`, and multiplying the nonlinear part by `a` gives the stated absolute gap. This is stronger than merely proving a normalized-coordinate or initialization-only regression gap.

## Initial motion and the kernel coefficient

The top backward Gram is positive definite: full support of the top Gaussian triple turns a zero quadratic form into the displayed functional identity; its nonconstant positive derivative forces every coefficient to vanish. At lower layers the genuine reused-transpose rule has a fresh Gaussian group of covariance `S_(ell+1)` plus the explicitly retained deterministic return. Conditioning on the local forward tuple proves strict backward Gram positivity even when the bottom tuple is singular. The bottom motion estimates and the positive trace formula then establish every hidden block's nonzero direction.

For each upper sample, formula (A) retains the additional same-matrix return in the recursion for `c^ell`. Regression of the newly appended forward source on the original three forward sources has variance exactly the squared distance in (B). The bottom conditional covariance supplies a strictly positive variance; the independent forward innovation and the derivative lower bound propagate it through all later layers. Independence is used only between the innovation and the original local forward/reverse variables, not between different added sample queries. The finite Gaussian-conditioning argument and ordered truncation justify these augmented queries without assuming globally bounded derivatives of untruncated velocity products.

The physical scaling is consistent: `C'(0)=3H`, `b_i^ell(t)/t -> 3 beta_i^ell`, and hidden velocity divided by t tends to `9V`. The readout-kernel contribution changes by `9 t^2 ||V||^2`; the hidden-gradient contribution is another `9 t^2 ||V||^2`. Thus the coefficient `18` is correct for the sum of all actual raw kernel blocks.

## Source construction and full population/algorithm bridge

The source lemma's Gaussian-part comparison is made at the same actual coefficient arrays. Resolvent elimination leaves a bounded arctangent remainder whose `1/K_ell` factor compensates the local curvature `K_ell`. The independently established actual `L2` scale controls the Gaussian part; it is not estimated from an assumed source radius. The Volterra derivative calculation retains the current backward return while strict forward time order prevents an algebraic loop. The resulting coefficient production inequalities strictly improve the displayed box in chronological order. The stated gain condition controls all the geometric depth factors, and yields cap-independent marginal Gaussian tails. No temporal independence or random time-maximum moment is substituted.

I also checked the underlying local finite-program construction in `../three_sample_self_contained/foundations.md` and the required chain, cap, observation and path arguments in that manuscript's `velocity.md`. Conditional Gaussian queries, their response corrections, singular-query perturbation, and countable common-space completion supply bounded initialized actions with genuine adjoints. The induction is over finitely many instructions and extends to the fixed finite list of adjacent matrices. The sharper initial norm input is correctly cited: Theorem 7.3.1 and Corollary 7.3.3 of [Vershynin's High-Dimensional Probability](https://anthonyhongxiao.github.io/pdfs/HDP-book.pdf) give the Gaussian expectation and tail bounds used for action norm at most two in the canonical limit and norm at most three with high finite-width probability.

The asymmetric cap comparison introduces a single factor of the cap: newly produced cap factors multiply forward discrepancies rather than previously produced backward cap terms. It needs tails only from the reference, so Gaussian reference tails defeat the comparison exponent and prove the strong cap limit, bounded-primal uniqueness, and reached-state restart. The strong chain rule and adjunction identify this limit with actual raw gradient flow.

For finite GF and raw GD, width is taken at a fixed cap and a fixed coarse program; width-independent raw Euler stability then handles the growing number of actual `n^-2` steps. Ordered observation truncation supplies genuine backward products and hidden velocities. The reference-tail comparisons transfer these to the uncut dynamics. Fixed-time joint laws and the integrated-speed interpolation estimate give path-space `W2` in the uniform path norm. The stated same-layer kernels, state/velocity laws, second moments, integrated squared speeds, and finite generated probes are consequently covered; no cross-width operator-norm convergence or limit-order interchange is required.

## Disposition

No mathematical blocker was found in the complete frozen gain theorem. No repair to that theorem is requested by this audit. Its activation constraint remains decisive: this PASS must not be used to mark the user's accepted near-identity or unit-sum activation target as proved. The later rejection of gain supersedes this candidate as a route to the user's requested result, without invalidating the separate mathematical theorem audited here.
