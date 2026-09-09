# Isolated probability and functional-analysis review

**Verdict: PASS for the stated partial and conditional scope.** I found no substantive mathematical obstruction to Theorems 1 and 2. The two presentation corrections below should be made, including the missing addition signs in the displayed loss chain rule.

Manuscript reviewed: `CAPS_MANUSCRIPT.md`, read in full.

SHA256: `053e6f05a31095d3c2a84b8a40ad4e49cfe3e59156a60168170a25e0960abb4d`.

This review used only that manuscript. No other mathematical documents, prior discussions, agent reports, web sources, or experiments were consulted, and no review work was delegated.

## Scope and principal checks

1. **Population spaces and topology.** The boundedness assumption on `A0` supplies an actual operator between the stated Hilbert spaces and hence a genuine adjoint. Every backward product is an `L2` field multiplied by a bounded gate; the matrix updates are Hilbert–Schmidt rank-one operators. The inequality `||U||op <= ||U||HS` supplies the required operator control. The manuscript neither assumes nor silently uses that `A0` is Hilbert–Schmidt. Its applicability to a Gaussian-program action remains explicitly conditional on constructing that action on these spaces.

2. **Continuity and chain rule.** Equation (4) correctly proves strong continuity of the gate products without claiming local Lipschitzness for uncapped products. For a `C1` Hilbert-space curve, the Bochner integral and Fubini construction gives the requisite absolutely continuous scalar representatives. Bounded activation derivatives and (4) then give continuous `L2` derivatives of the activated paths. The subsequent operator product rule and genuine-adjoint pairing yield the sum of the three gradient pairings. No unproved Fréchet differentiability of the activation map is necessary.

3. **Unconditional approximation theorem.** The radial cap has the claimed Jacobian bounds, including at the origin where it is the identity. In the auxiliary extension, `|tau_M(C)| <= 2M` combines with `|phi''| <= 1/2` to give the coefficient `M` in (10). Likewise `|H_R(p)_i| <= 2R` gives the coefficient `R` in (12). The incoming-argument Lipschitz bound is one, so the two cap sizes are added rather than multiplied. The local Lipschitz constant can therefore grow linearly with `R` for fixed `T` and state ball. The extension's norm bound is independent of both caps because they decrease magnitudes.

4. **Dissipation and continuation.** The same nonnegative scalar `chi_R(P)` multiplies the entire first-row gradient, so (14) is valid even when the input vectors coincide or are linearly dependent. No inverse Gram matrix, separation assumption, or nonzero residual assumption is used. The energy inequality controls the path length on every finite horizon. The readout cap gives the pointwise bound needed to deactivate the auxiliary top cap. Bounded velocity and local existence then continue the extension through any finite proposed endpoint; the same pointwise bound also establishes uniqueness for every strong solution of the original capped equations.

5. **Tails, moments, and the readout.** Premise (15) gives exponential probability tails by dividing its squared tail norm by the squared threshold. Layer cake gives integer moment bounds linear in the moment order. Minkowski applies to the time-integrated capped readout, whose magnitude is bounded by the uncapped direction. Optimizing the integer moment in Markov's inequality yields an exponential readout probability tail, and the displayed truncated second-moment identity then yields (18), with a smaller rate if necessary. All constants may depend on the fixed horizon but remain uniform in cap and time. A zero horizon is trivial.

6. **One-sided Osgood estimate.** Equations (20) and (21) consistently place the difficult incoming fields on the reference side. Reference tails of `C` control the top gate, and reference tails of `P` control each residual-weighted `p_i`. The intervening bounded operator, residual, and rank-one estimates do not introduce a second cutoff factor. Consequently the modulus is proportional to `s log(B/s)`, not to `s log^2(B/s)`. Individual unweighted `q_i` need no exponential tail. This also covers times when some residual vanishes.

7. **Cap removal and uniqueness.** The defect estimate follows from the radial cap error and the factor `sqrt(3)` for the three first-row contributions. The scalar majorant starts strictly above zero, is locally governed by a smooth scalar equation away from zero, and gives a bound tending to zero on each fixed horizon. It establishes the uniform Cauchy property. Continuity then passes the integral equation and all the stated fields and kernels to the limit. Strong `L2` convergence and Fatou with a smaller threshold transfer the reference tails. Those tails belong only to the constructed reference solution; they are not required of a competitor. The resulting comparison proves uniqueness against bounded-state strong competitors and after restarting at any reached time. A continuous strong competitor is automatically bounded on each compact time interval on which it exists.

## Presentation corrections

- **Equation (5) is missing two plus signs.** As displayed, the adjacent gradient pairings denote a product, which is false. It must read `E' = <g_w, wdot> + <g_U, Udot>_HS + <g_C, Cdot>`. The accompanying derivation and (14) already use this sum, so this is an unambiguous typographical correction rather than a defect in the argument.

- **Clarify the compactness sentence after (26).** The parameter `R` ranges over all real numbers at least one, whereas the stated compactness justification explicitly concerns a sequence. The conclusion is valid without proving compactness of the entire continuously indexed family. For any sequence `R_n -> infinity`, the uniformly converging paths and their limit have compact union closure, so continuity gives uniform field convergence along that sequence. The sequential criterion then gives the asserted convergence as real `R -> infinity`. Equivalently, apply continuity uniformly near the compact image of the limit path. This supplies the brief missing explanation.

## Claim boundary

The manuscript does not establish premise (15) for the physical Gaussian approximations, and bounded `L2` state estimates alone would not establish it. It also does not construct the initialized Gaussian action or prove any finite-width GF/GD bridge. These omissions are expressly part of its claim boundary and are not contradictions of either stated theorem. This PASS does not certify the requested full Gaussian-initialized training limit.
