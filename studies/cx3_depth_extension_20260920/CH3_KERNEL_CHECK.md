# Author-side check of the fixed-depth kernel corollary

2026-09-20. Scoped author cross-check, not an isolated independent review or
promotion review. Verdict: **PASS within the stated local finite-data,
unit-mobility scope.** No mathematical defect was found.

Checked `CH3_KERNEL_COROLLARY.md` in full, SHA-256:

    a0f6b5de8671a094274d0742a428c2b7740c85885f74f8a143f48e6b8e88aceb

Its activity input is the unchanged frozen `CH3_ACTIVITY_PROOF.md`, SHA-256:

    4858e2d8b3d41eafab3070277799ebcf5441e3f2a0b86491eb162d0e1f2dba23

The other scientific inputs were the already assigned and fully read
maintained C.1–C.3, including C.3's weighted-loss correction. No new reading
of `CH3_LOCAL_PROOF.md`, other study drafts, or other studies was performed.
The reference to local-proof equation (29) was checked through the kernel
formulas already stated in maintained C.1; no claim is made here about the
separate local proof. No experiments or Git operations were performed.

## Checked mathematical steps

1. **Strict block coefficients.** For every positive-semidefinite Q and
   positive-definite D, the displayed decomposition proves
   Q circ D >= lambda_min(D) diag(Q_aa). Applying it to G,D_1 and to
   Q_(ell-1),D_ell gives strictly positive J_ell even when G is singular.
   Each p_a=omega_a y_a is nonzero under the stated assumptions, so
   E_star=sum_ell p^T J_ell p>0.
2. **Hidden kernel expansions.** The established limits
   Delta_ell(t)/t -> 2B_ell and H_ell(t) -> H_ell in L2 give exactly
   K^ell(t)=4t^2 J_ell+o(t^2). Products of contractions converge by
   Cauchy–Schwarz; finite sample count upgrades entrywise convergence to
   matrix-norm convergence. Strict positivity for sufficiently small t>0
   and nonconstancy of every hidden block follow. The readout block starts
   at Q_L>0 and stays strictly positive by continuity.
3. **The telescope.** For ell>=2, the learned term contributes
   p^T(Q_(ell-1) circ D_ell)p. Actual adjunction transfers the propagated
   term to the preceding layer because
   B_(ell-1,a)=d_(ell-1,a) A_ell^* B_(ell,a). Iterating ends at
   p^T(G circ D_1)p. Thus the displayed sum at the top equals E_star.
   The calculation neither removes response terms nor assumes individual
   terms have a sign.
4. **Readout and total-kernel constants.** With
   S_t=S+2t^2 sum_a p_a E_(L,a)+o_L2(t^2), expanding its squared norm gives
   4t^2 sum_a p_a <S,d_(L,a)R_(L,a)>=4E_star t^2. Adding the hidden blocks'
   4E_star t^2 gives the total coefficient 8E_star. Therefore both kernels
   are nonconstant in the weighted direction p, with the constants and
   direction agreeing with unit-mobility maintained C.3 at L=2.
5. **Learned-action motion.** For each edge ell=2,...,L and fixed input a,
   the learned-increment limit applied to H_(ell-1,a) is exactly the stated
   2t^2 sum_b p_b Q_(ell-1),ba B_(ell,b). Its coefficient vector is nonzero
   because its a-th entry is p_a Q_(ell-1),aa. Positive definiteness of
   D_ell proves strictly nonzero L2 displacement. This concerns the learned
   increment K_ell, distinct from the kernel block K^ell.
6. **Loss descent.** The unhalved weighted loss has exact derivative
   -4(Omega r)^T K(Omega r). Since r(0)=-y and K(0)=Q_L,
   -loss'(0)=4p^T Q_L p=4||S||_2^2>0. Continuity supplies the stated lower
   bound 2||S||_2^2 on a common smaller positive interval.

Intersecting these finitely many intervals with the activity proof's motion,
variance and nonaffinity intervals is valid. No bound uniform in depth or
degenerating data is needed or asserted. The corollary supplies the remaining
strict local finite-data C.3 conclusions; it does not establish substantial
training, broad-law completeness, numerical convergence, or promotion status.
