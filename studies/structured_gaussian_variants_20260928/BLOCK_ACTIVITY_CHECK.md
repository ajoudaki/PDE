# Scoped check of the block activity theorem

Checked the complete frozen BLOCK_PARTICLE_RATE.md, with verification restricted to Sections 1–3. No other scientific files, experiments, or Git operations were used. This is a scoped mathematical check, not a fresh independent promotion review.

**Verdict:** the uniform finite-activity and fitting argument is valid under the stated block operator cap, initial Gram gap, and small-label condition (10). The constants in (9)–(12) are independent of \(B,k,q\). I found no substantive error in the training theorem. Two small specification/proof details should be made explicit below.

## Verified points

1. **Global learned updates and adjoints.** Under empirical \(\mu\), the pairing is
   \[
   \mathbb E_\mu\langle X,g\rangle_k
   =\frac1{Bk}\sum_{b=1}^B X_b^Tg_b.
   \]
   Thus each reconstructed summand is a global rank-one operator with denominator \(n=Bk\), and their sum is generally not block diagonal. Formula (4) is the adjoint of precisely this correction. The first-preactivation and readout equations have the canonical mobility factors.

2. **Exact passivity and defect.** The entries of \(D\) give \(D+D^T=-bb^T\) exactly. Differentiating \(\|Z\|_F^2\) gives (5), including its negative terminal energy and gain one. The identity \(De_0+b=e_0/2\) makes \(\sqrt\tau e_0h(0)\) the exact constant-prefix state, so (7) follows without an endpoint operator-norm estimate. Differentiating \(-2\kappa_\ell m^{-1}\sum_{a,j}Y_{a,j}\otimes X_{a,j}\) gives the three terms
   \[
   -\frac{2\kappa_\ell}{m}
   \sum_a\left[r_a\delta_a\otimes\widehat h_a+
   \rho\widehat U_a\otimes h_a-
   \rho\widehat U_a\otimes\widehat h_a\right].
   \]
   Adding and subtracting the ideal velocity gives exactly (8), with the displayed positive defect sign. No exact-gradient-flow kernel equation is used.

3. **Backward source induction.** The top source follows from the readout bound. Once the source at layer \(\ell\) is bounded, its memory obeys
   \[
   \sup_\omega\|Y_{\ell,a}\|_F/\sqrt k
   \le\sqrt{m/3}\,D_*S^{3/2},
   \]
   because \(\int_0^T\rho S(t)^2dt=S^3/3\). That memory and the already bounded forward memory control the adjoint correction for layer \(\ell-1\). Thus the downward induction is noncircular. Its correction norm is at most \(J S^{3/2}\); the chosen \(J\) even discards an available factor \(1/\sqrt3\).

4. **Time integration versus block supremum.** For \(W^{\rm corr}\dot h\), the uniform moment bounds leave \(\int_0^T\mathbb E_\mu\|\dot h\|_2/\sqrt k\,dt\), which is at most \(V_{\ell-1}\) by Tonelli and the definition of \(V_{\ell-1}\). No estimate of \(\int\sup_\omega\|\dot h\|\) is needed. For the defect, Cauchy–Schwarz in time gives
   \[
   \frac{2\kappa}{m}\sum_{a=1}^m
   \sqrt{mD_*^2S^3/3}\sqrt{S V_{\ell-1}^2}
   =K S^2V_{\ell-1}.
   \]
   The target feature is bounded by one in block RMS. Consequently (18) is valid. Iterating it gives the stated, deliberately loose \(C_V\).

5. **Integrated readout contraction.** The Gram perturbation is at most \(2mC_VS^2\) in operator norm. The readout contraction rate is therefore \(\gamma=\kappa_{L+1}\lambda/m\). The bound
   \[
   \int_0^T\|e(t)\|_2/\sqrt m\,dt
   \le2\kappa\sqrt m\,S V_L
   \]
   is valid using the sum of the integrated absolute sample errors; it does not require an interchange of a maximum and an integral. The five restrictions defining \(s_0\) respectively give \(S\le1\), \(JS^{3/2}\le1\), \(KS^2\le1\), the Gram gap, and absorption of the cubic error. Condition (10) then supplies the strict continuation margin \(S\le s_0/2\).

6. **Banach continuation and fitting.** For each fixed finite \(k,q\), use bounded measurable block fields with the supremum block-RMS norm, or \(L^\infty(\mu)\) with essential suprema. The unbounded fixed Gaussian first panel enters only through tanh and its bounded derivatives. On bounded state sets with \(\tau\ge1\), the vector field is bounded and Lipschitz with constants allowed to depend on \(k,q\). In particular, the norm in \(\rho\) is Lipschitz at zero, and (2) contains no division by \(\rho\). Once the first-preactivation increment bound below is included, no finite-time escape is possible. The velocity bound \(C_{k,q}\rho\) gives convergence in this Banach norm. Continuity of the prediction map and finite residual activity then force the residual limit to be zero.

## Details to make explicit

- **First-preactivation increments in the continuation paragraph.** Equation (16) displays the variation of \(h^{(1)}\), which alone would not control its preactivation. The same preceding calculation directly supplies the needed stronger estimate:
  \[
  \max_a\sup_\omega
  \int_0^T\|\dot u_a(t,\omega)\|_2/\sqrt k\,dt
  \le\kappa gD_*S^2.
  \]
  Hence \(\sup_\omega\|u_a(T,\omega)\|_2/\sqrt k\) has the same bound. Adding this one line makes the bounded-state continuation claim fully explicit.

- **Passive-input initialization.** Section 1 defines a mark using only the initial Gaussian *training* panel. A passive input outside the training-input span also needs its initial first-preactivation panel, jointly distributed with that training panel. Specify this extension of the mark law, or start from the full first matrix. Its increment is driven by
  \[
  \dot u_*=-\frac{2\kappa_1}{m}\sum_a r_a\delta_a^{(1)}G_{a*}.
  \]
  This introduces no feedback into training. With that initial field supplied, the passive recurrence (21) and endpoint convergence are valid. Training-panel marks alone do not determine this extra Gaussian component.

The verified conclusion concerns the stated capped initializer (or any supported empirical/population mark law with the gap). It establishes global existence, finite activity, state convergence, training fitting, and the specified passive conclusions. It does not establish a \(q\)-uniform physical-time tail, convergence as \(q\to\infty\), a uniform particle coupling, or transfer to uncapped/dense Gaussian initialization. Section 4's particle-rate theorem was read but is outside this check's verdict.


## Resolution note — 2026-09-29

Both requested clarifications are resolved in the checked source. Section 1 now specifies the joint initial Gaussian training/passive panel (lines 43–48), and the passive paragraph explicitly uses it (lines 450–453). The feature-variation proof now gives the raw first-preactivation increment bound (16a), together with its velocity derivation (lines 332–348); the continuation paragraph explicitly invokes that bound (lines 427–434). These additions are correct and sufficient. No comments remain open from this bounded Sections 1–3 check; its original verdict and scope are unchanged.

SHA256 of the final source checked, BLOCK_PARTICLE_RATE.md:

`f8cff667ec606feeb6dd38355ef11d7585049e4d980e0764ead956d091105f99`

The original review text above is preserved. This resolution does not extend the review to Section 4 or to the broader research program.
