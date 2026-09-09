# Independent adversarial mathematical review — Round 2, reviewer B

## Verdict

**PASS.** I found no unresolved mathematical obligation of the theorem as stated, no invalid limit exchange on which it depends, and no imported specialized theorem whose missing proof is needed to complete the argument. In particular, the document proves the nonlinear uncut flow and its stated uniqueness class; it does not obtain those conclusions merely by identifying a finite Gaussian program.

The two presentation clarifications at the end of this report do not require a mathematical repair of the theorem. This verdict concerns the specified single activation, initialization, fixed finite physical horizons, common population spaces, and empirical/action-law topology. It does not extend to arbitrary initial population states, infinite physical time, or operator-norm comparison across different widths.

## Document identity, coverage, and sources

- Reviewed mathematical source: `/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md`.
- Expected SHA256: `293b34e5657f48991e8ff922c8e7648bf9400557e97cef1a314bb2af9203d5f1`.
- Observed SHA256 before reading: `293b34e5657f48991e8ff922c8e7648bf9400557e97cef1a314bb2af9203d5f1`.
- Observed SHA256 after the mathematical audit, immediately before writing this report: `293b34e5657f48991e8ff922c8e7648bf9400557e97cef1a314bb2af9203d5f1`.
- Size inspected: 1,743 lines, 79,677 bytes.
- **Entire-document confirmation:** I read all lines 1–1743, including every theorem assertion and Sections 2–12. A portion truncated in a combined tool response was read again in a separate, untruncated inspection. I also reread selected formulas and the theorem while checking their obligations.

Complete list of files/sources accessed for this review:

1. The exact proof file above: the **only mathematical source**.
2. `/etc/codex/skills/solve-math-rigorously/SKILL.md`: procedural instructions for conducting a rigorous mathematical audit, not mathematical evidence for this theorem.

No other project or research file, previous review, audit-status file, conversation, or agent report was inspected. No agent was contacted. No external mathematical source was accessed. No simulation or numerical experiment was run. The constant checks below are symbolic arithmetic and elementary inequalities. The proof was not edited. This report is the only output file written.

All line references below refer to the frozen proof file.

## Full-theorem obligation ledger

| Obligation | Principal locations | Assessment |
|---|---|---|
| Exact finite model, normalization, and raw gradient | 20–69; 1091–1179; 1210–1223 | Discharged |
| Adaptive Gaussian actions, both transposes, full covariances | 256–409 | Discharged |
| Singular and zero-variance query directions | 411–457 | Discharged |
| Actual finite clipped program, including empirical feedback | 459–590 | Discharged |
| Fixed common spaces, bounded actions, and genuine adjoints | 592–647 | Discharged |
| Fixed-cap flow construction and finite-width limit | 649–757 | Discharged |
| Mesh- and cap-uniform nonlinear response bootstrap | 759–945 | Discharged |
| Uncut existence and arbitrary bounded-primal competitor uniqueness | 947–1027 | Discharged |
| Prescribed small finite readout and uncut finite feature flow | 1029–1076 | Discharged |
| Raw Hilbert gradient structure, physical clocks, and raw restart uniqueness | 1078–1206 | Discharged |
| Exact raw GD, stopped comparison, and interpolation | 1208–1357 | Discharged |
| Probe laws, backward fields, physical velocities, and whole paths | 1359–1470 | Discharged |
| Initial nonzero motion coefficients and nonconstant kernel | 1472–1617 | Discharged |
| Uniform nonaffinity and nonzero hidden motion at every positive finite time | 1619–1736 | Discharged |

## Detailed mathematical audit

### 1. Setup, elementary estimates, and convergence tools

The activation estimates at 165–176 are sufficient for all subsequent bounds. The positive lower bound is essential, not cosmetic: it supplies the later feature-clock margin. The transformation satisfies

\[
F'(z)=10(1+z^2)=1/\phi'(z),\qquad
(\phi\circ F^{-1})'(F(z))=(\phi'(z))^2\le 1/100.
\]

The cubic transformation is correctly restricted to the initial root pair and to explicitly justified changes of coordinates. It is not silently used as a globally Lipschitz instruction.

The matrix norm bound at 178–190 has the correct net cardinality and scaling. A quarter-net gives the factor two in the bilinear supremum; a unit-vector bilinear form has variance exactly (1/n); and the resulting exponential union bound tends to zero. The initial readout has normalized squared norm of expectation (n^{-2}), giving the asserted (O_{\mathbb P}(n^{-1})) normalized norm.

Sections 2(a)–(c), 194–240, provide the relevant second-moment and truncation machinery. Weak convergence plus second-moment convergence yields squared-tail control, which justifies both the finite-dimensional Wasserstein conclusion and continuous quadratic-growth tests. The same-index coupling estimate has the correct normalization. In (2.4), the fixed limiting multiplier is truncated before passing to the limit; this avoids requiring an extra moment of the product. Its application to the curve chain rule is appropriate and does not assert unrestricted Fréchet differentiability of an (L^2\)-valued nonlinear map. The discrete and continuous Gronwall comparisons at 242–254 are valid.

### 2. Adaptive Gaussian calculations and singular queries

The conditional projection formula (3.3), 301–314, is correct. Its deterministic part satisfies both sets of observations because (U^TY=Q^TV), and its remaining Gaussian component lies in the simultaneous null directions. Formula (3.4) has the appropriate normalized Gram matrix and contraction in its reverse-response coefficient.

The adaptation argument at 316–320 conditions on the entire preceding transcript. The new input is then fixed, and the new constraint concerns only the matrix currently queried. Thus it does not assume unconditional independence between an adaptive input and the reused matrix. The two conditional residual matrices remain independent under the sequential conditioning described there.

The empirical induction at 330–355 controls the discarded projection in normalized (L^2), rather than declaring reused coordinates iid. At a fixed number of queries its rank is bounded. Conditional variance estimates for bounded tests, cross terms, and Gaussian squares then establish the necessary empirical convergence and second moments.

I checked the cancellation giving (3.5), 376–407. Orthogonality of (h_\perp) to prior forward inputs removes the old forward-response part of each reverse answer. Gaussian integration by parts supplies the expected source derivatives, and substituting the old forward decompositions cancels the projection coefficients. The new source covariance is the full input second moment. In particular, subtracting the response variance from the new Gaussian variance would be incorrect; the document does not do this.

The derivative convention at 370–374 is necessary and consistently used: deterministic response coefficients and covariance parameters are fixed while differentiating the explicit scalar expression. The argument includes dependence passing through earlier calls to the other matrix.

The singular-Gram argument at 411–457 does not assume convergence of inverses at a rank drop. Independent noise in each new query makes its limiting Schur complement positive at fixed noise level. The original finite program and its perturbed version are close using the original matrix norm bound and finitely many Lipschitz instructions. On the scalar side, causal response coefficients and their finite formal derivatives are bounded inductively; continuous covariance square roots give a coupling under which the coordinates and bounded derivatives converge. This is sufficient for the zero-noise passage. Formally distinct slots are retained even when their Gaussian law is singular. The kernel-of-covariance observation at 453–457 correctly explains why a null-direction coefficient change cannot alter the contracted response.

### 3. Actual clipped program and common population actions

The unrolling identities (4.2), 489–499, use the correct (1/n) factors for both orientations. The actual empirical feedback is restored at 513–525 by contraction differences and a finite instruction induction. This is a fixed-program argument; no claim of a Gaussian induction uniform in a growing number of GD steps is made or subsequently needed.

The fixed-cap coordinate instructions satisfy the hypotheses used in Section 3. The only potentially troublesome top product is extended outside the attained bounded readout interval. The middle product is capped, and (F(Z_0^{(1)})) is an initial root coordinate rather than a nonlinear instruction applied to arbitrary later states.

The causal order in (4.3)–(4.6) is correct. Forward matrix corrections use past reverse inputs; reverse corrections may include the current forward input. I explicitly checked the present middle return:

\[
b^{(2)}_{kk}
=\mathbb E[\phi''(Z^{(2)}_k)\tau_R(q^{(2)}_k)]
+b^{(3)}_{kk}\mathbb E[(\phi'(Z^{(2)}_k))^2\tau'_R(q^{(2)}_k)].
\]

The second term follows from differentiating the present (b^{(3)}_{kk}H^{(2)}_k) contribution to (q^{(2)}_k). It is present in the proof and in the later estimates.

The common-space construction at 594–647 is adequate. Consistency follows from finite unions of the same finite-width calculations. The coordinates form a countable real product, and the included finite-coordinate function family gives density in each resulting (L^2). Passing finite operator inequalities to limiting second moments makes each initial action well-defined on equivalence classes and bounded by ten. Passing finite transpose pairings then proves adjunction on a dense set and hence everywhere. These are actual bounded actions on fixed spaces; the construction does not replace a transpose by a new independent matrix. Approximation of real coefficients and fixed Lipschitz functions extends the countable construction to the finite probes and Euler programs needed later.

### 4. Fixed-cap flows and their uniform primal bounds

The coarse bounds (5.5), 671–689, follow in the required order: readout, third matrix, second matrix, and first-coordinate velocity. They use only bounded activation, bounded gates, the contraction property of the clip, and rank-one operator norms. Consequently they are independent of width and clipping, and apply to positive-step Euler prefixes as well as flows. The stronger pointwise readout bound follows from zero initial readout and the positive activation floor.

The asymmetric placement of the bounded reference readout in (5.7), 700–712, is valid. It does not impose an (L^\infty) condition on the competing readout. The capped middle gate estimate gives a state Lipschitz constant of order (1+R), uniformly in width.

At 729–741, the integral map is constructed on a closed set preserving the pointwise readout constraint. The velocity bounds allow a short invariant interval, and the fixed-cap Lipschitz bound supplies contraction. The coarse bounds allow restarts over the whole desired feature interval. At finite width, smoothness and bounded parameters likewise justify uncut continuation. The local Euler defect and discrete comparison in (5.8) are consequently available uniformly in width for fixed cap. The order “fixed mesh, width limit, mesh refinement” at 751–757 is legitimate.

### 5. The mesh- and cap-uniform response bootstrap

This is the main nonlinear estimate, and I checked its dependency order and constants throughout 759–945.

The zero-time backward rows really vanish because the zero readout is identically zero as an explicit expression. The proof correctly distinguishes this from erasing formal derivatives in a backward source direction merely because that source currently has zero variance.

Assume only (U_r,V_r\le1) for (r<k). The bottom-source calculation uses only these past rows and gives

\[
|a^{(2)}_{js}|\le\Delta\left(49/36+e^{S/100}/100\right)<(3/2)\Delta,
\qquad s<j\le k.
\]

The single-source forcing contains one factor of (Delta). The middle forward-source row in (6.3) has a single direct identity contribution, not one contribution for each earlier time slot. Its random envelope uses only past middle queries and past top response rows. The single middle-backward-source derivative in (6.4) also enters with a factor of (Delta).

The estimate of the envelope uses marginal Gaussian variances and Jensen over finitely many time slots. It neither assumes temporal independence nor bounds the maximum of a Gaussian process. With (A=S=3/2), the deterministic and Gaussian terms in the exponent are respectively

\[
219p/400,
\qquad 3969p^2/1280000.
\]

These give the stated (L^1) and (L^2) envelope bounds and hence (|a^{(3)}_{js}|<(3/2)\Delta).

The top derivative row includes both the derivative of the readout sum and the top gate. Their combined coefficient is ((73/300)S). The resulting exponential is bounded by (e^{657/800}<5/2). Adding the learned covariance contribution yields exactly

\[
V_k\le73/80+147/3200=3067/3200<1.
\]

This current top row is obtained before using any current (U_k). It gives (\|q^{(2)}_k\|_2\le161/120). The current middle row, including its current return through matrix 3, is then bounded by

\[
U_k\le3\left(\frac{161}{600}+\frac1{100}\right)
+\frac{3}{200}\left(\frac{161}{120}\right)^2
=\frac{2482563}{2880000}<9/10.
\]

Thus the simultaneous induction closes with strict margins. It is not a bootstrap that assumes its own current conclusion.

The identified query itself has a Gaussian source of variance at most ((7/40)^2) plus a bounded shift of absolute value at most (7/6). The exponential-square estimate (6.11) follows with its displayed constants even when source and shift are dependent. This supplies the actual cap-uniform tail input needed by the analytic flow argument.

### 6. Removing the cap and identifying arbitrary competitors

The passage from Euler queries to each fixed-cap flow in 949–958 is a strong (L^2) passage. Fatou is used at each fixed time; the resulting deterministic bound is uniform in time and cap. No common almost-sure subsequence for all times and caps is claimed.

The exact difference decomposition (7.2), 960–985, is correct. Its significant feature is that the tail is evaluated only on the capped reference. The first term uses the contraction property of the other clip, the second term has multiplier bounded by (2R), and the remaining discrepancy is supported outside the reference cap. Consequently an uncapped competitor, or a competitor with any larger cap, need not have its own exponential moments.

The tail estimate gives

\[
\varepsilon_R=8e^{-R^2/256},
\]

and the comparison error is bounded by a constant times (e^{C(1+R)S}\varepsilon_R). The quadratic decay in the exponent dominates every fixed linear exponent in (R). This proves a Cauchy property uniformly over all larger caps, rather than merely producing a subsequential weak limit.

At 1007–1015, the comparison is applied again with the limiting state as the uncapped state. Multiplication of the state error by (1+R) still tends to zero. This identifies the limiting velocities with the actual nonlinear vector field and passes the integral equations strongly. An unbounded product is not being passed through weak convergence.

The uniqueness argument at 1017–1027 applies to every continuous bounded-primal uncut integral competitor in the stated class. Such a competitor changes the finite comparison constant, but every such constant is absorbed by the same Gaussian tail. At a reached restart state, the initial error against the clipped reference is already of the form (e^{C_0R}\varepsilon_R), and another finite comparison interval only contributes another linear exponential. This also vanishes. There is no hidden assumption of local Lipschitzness of the uncut vector field on arbitrary (L^2) neighborhoods.

### 7. Uncut finite feature flows and the prescribed readout

The finite reference tail observable in (8.1), 1031–1049, is a continuous quadratic-growth measurement. Its uniform-in-time convergence follows from a finite time net and a query Lipschitz bound independent of width. This avoids assuming finite-width exponential moments or convergence of discontinuous tail indicators.

Equation (8.2) compares the actual uncut finite feature flow, with its prescribed random small readout, to the zero-readout capped reference. Only the reference requires a pointwise readout bound. The initial discrepancy vanishes at rate (O_{\mathbb P}(n^{-1})) in the normalized vector norm. Taking width first at fixed cap, then removing the cap, yields the full uncut feature-flow law. The additional middle-backward-field comparison at 1069–1075 is essential and is supplied; state convergence alone would not have justified this unbounded gated field.

### 8. Raw gradient structure, physical continuation, and raw uniqueness

At 1080–1089, trained matrix increments are Hilbert–Schmidt because they are integrals of continuous rank-one velocities. Their initial Gaussian actions need not be Hilbert–Schmidt. The distinction is maintained throughout the gradient argument.

The scalar weighted remainder (9.2), 1098–1110, proves the differentiability actually required. For fixed (B\in L^2), the bounded part of (B) gives a quadratic remainder and its tail gives a small multiple of (\|v\|_2). Expanding the predictor from the top down applies this with the old readout and the old reverse factors; all are in (L^2). Mixed matrix/activation increments are quadratic because an HS variation controls its operator norm. This establishes (9.3), and the HS rank-one pairing identifies the gradient in (9.4). The reverse continuity argument uses (2.4) with fixed limiting factors and proves continuity of that gradient.

The finite metric at 1210–1215 is also correct: normalized Euclidean squared norms for vector variations and ordinary Frobenius squared norms for matrices give precisely the raw updates (1.3). There is no missing factor of (n). The transformed coordinate is not confused with a Euclidean raw parameter: (X_s=q^{(1)}) corresponds to (Z_s^{(1)}=\phi'(Z^{(1)})q^{(1)}).

The feature derivative of the predictor is the sum of the four nonnegative kernel blocks, with (K^{(4)}\ge25/36). Continuity and boundedness on the constructed interval imply a unique level-one feature time

\[
0<s_*\le36/25<3/2.
\]

The upper bound on (f_s) is used in the correct direction in 1163–1169: it makes the physical time integral diverge at (s_*), and yields (s_*-s(t)\ge s_*e^{-2B_*t}). Thus every finite physical horizon fits strictly inside the constructed feature interval.

The additional raw-competitor argument at 1181–1204 is sufficient. Raw bounded-primal integral solutions have continuous backward fields; their rank-one equations give HS increments, so the gradient identity applies to their raw curves. Their deficit solves the displayed exponential equation and stays strictly positive at every finite time. Coordinate absolute continuity and the pointwise chain rule then establish (9.8). Its right side is (L^2), proving transformed membership rather than assuming it. Feature-time uniqueness and scalar-clock uniqueness identify the competitor, including at every reached restart. This discharges the stronger raw uniqueness assertion, not just uniqueness among preselected transformed solutions.

### 9. Exact raw GD, stopped clocks, and interpolation

Finite physical GF continuation at 1210–1223 uses the actual loss decrease and sequential bounds on the readout, matrix norms, and first raw vector. At fixed width these rule out finite-time parameter escape. On the high-probability initialization event, the finite feature predictor crosses one before (S=3/2); the threshold (-1/24) for its initial predictor is consistent with the minimum slope (25/36). The finite and population physical clocks then converge by a scalar Lipschitz comparison.

The raw GD argument does not identify raw GD with Euler in (X). The cubic identity (10.1) is exact. For the first raw step (z_+=z+\alpha\phi'(z)q), the nonlinear terms have normalized vector size at most

\[
C(\alpha^2\sqrt n+\alpha^3n).
\]

This follows from ordinary finite-dimensional norm inequalities and the bounded scalar coefficients, not from an assumed fourth or sixth empirical moment. On a positive prefix, (\max\alpha_k\le C\eta_n) and (\sum\alpha_k\le S), giving total defect

\[
O(\eta_n\sqrt n+\eta_n^2n)=O(n^{-3/2}+n^{-3}).
\]

The stopping construction at 1239–1261 is not circular. Before a bad node, the feature increments are positive, so the matrix and readout prefix bounds apply. These give the bound on the next increment. The step into the first bad endpoint is included and still lands below (S) for sufficiently large width.

The recurrence (10.3) includes all three required errors: the asymmetric tail forcing, the fixed-cap local Euler defect, and the raw-coordinate defect. The random partition in (10.4) is handled by a pathwise time-Lipschitz estimate for the reference tail observable. Hence no theorem for a growing adaptive Gaussian program is being invoked.

The stopped predictor error tends to zero in the correct order of limits. The scalar-clock comparison then gives (D_n\to0). At a candidate first bad endpoint, the strict margin

\[
36/25<147/100<3/2
\]

excludes the feature-time stop, and the positive deficit rho on the interval [0,T+1] excludes the prediction stop. The argument covers a first bad final interpolation node. Its constants are allowed to depend on the fixed horizon; it does not require a lower residual bound uniform over infinite physical time.

The fractional-step use of the same cubic identity at 1341–1346 controls the specified raw interpolation, including recomputed features. Comparing both finite algorithms to the same capped finite reference at their converging clocks proves the stated same-width distance (1.7). The cap/mesh/width order at 1353–1357 gives convergence along the full width sequence in probability.

### 10. Observables, actual velocities, and whole paths

Section 11 first supplies the missing unbounded-factor control instead of assuming that every observable is globally Lipschitz in the state. The middle backward field is handled by the asymmetric comparison, and subsequent bounded matrix actions preserve its controlled errors. For a bounded continuous gate times an unbounded field, truncating that field and using uniform squared tails gives the asserted joint laws. Compactness of the limiting (L^2) time path and uniform Wasserstein convergence supply the corresponding uniform finite tail control.

The kernel formulas have the correct normalization. Prediction and each norm or contraction are continuous quadratic-growth measurements of an appropriate finite same-layer list. Products of the resulting scalar expectations give the hidden matrix blocks of the kernel.

I differentiated the forward equations independently to check (11.1), 1385–1405. The lower propagated velocity in layer 2 is (W^{(2)}[(\phi'(Z^{(1)}))^2q^{(1)}]); the layer-3 propagation is (W^{(3)}[\phi'(Z^{(2)})(Z^{(2)})']). Both are correct. Physical velocities acquire the common multiplier (2(1-f)).

The between-node argument at 1407–1445 controls the velocities of the actual raw interpolant. Its preactivation velocities have bounded normalized (L^2) norm, so a step changes any coordinate by at most (C\eta_n\sqrt n). Bounded (phi'') therefore controls gate changes in coordinate supremum. In (11.2), the contraction and matrix errors are (O(\eta_n)), and the remaining gate error gives (O(\eta_n\sqrt n)). Propagating this through layer 3 and through feature gates gives a vanishing (O(n^{-3/2})) error. The left derivative at a terminal mesh node is covered by its adjacent step and the same vanishing time displacement. Thus the proof treats genuine interpolated velocities, not merely the vector field evaluated at GD nodes.

At 1447–1468, separable (L^2) and the finite time-energy bound give jointly measurable velocities and absolutely continuous scalar coordinate paths. The interpolation estimate (11.3) then controls the expected or empirical squared supremum error by a constant times mesh size and total squared speed. Fixed-grid joint Wasserstein convergence and a triangle inequality prove the whole-path Wasserstein limit. This includes its second-moment requirement in the supremum norm. Integrated squared velocities converge by the established uniform norm convergence on the finite physical interval.

### 11. Nonlinearity, initial onset, and absence of later freezing

The initial forward variances (12.1), 1476–1482, correctly retain the activation's nonzero mean contribution. The first transpose law in (12.3) uses the full second moment of (B^{(3)}) for its Gaussian innovation. The coefficient (c_3) is strictly positive only after the odd contribution has been averaged out; the document does not make the false pointwise sign claim for negative preactivations.

For the second transpose, 1520–1539 conditions on the entire independent third matrix as well as the observed second-layer preactivation. This makes the actual reverse input measurable without exposing the residual of the second matrix. The second use of the conditional formula is therefore justified. Its unbounded gated input is handled by truncation. These laws give strictly positive (gamma_1,gamma_2,gamma_3).

The adjoint identities in (12.6) are correct and show that each initial movement vector (V^{(\ell)}) is nonzero. The (L^2) expansions at 1561–1585 follow from the readout integral, bounded gates, operator continuity, and integration of an (o(s)) remainder. In particular the hidden motion starts at order (s^2), hence at order (t^2) in physical time. The kernel coefficients satisfy

\[
K^{(4)}(s)=m_3+\Gamma s^2+o(s^2),\qquad
\sum_{\ell=1}^4K^{(\ell)}(t)=m_3+8\Gamma t^2+o(t^2),
\]

with (Gamma>0). The propagated lower-layer motion is included in the coefficient. The squared physical-speed integral has the stated leading coefficient (16/3).

The support arguments at 1621–1675 are also valid in the presence of response dependence. At the top the correction is deterministically bounded. In the middle and bottom arguments, it is the dominating variable, not the actual nonlinear correction, that is independent of the relevant forward Gaussian or initial root. The constants (63/160), (483/1600), and (1561/800) agree with the displayed bounds. The passage of lower tail probabilities through closed half-lines uses the correct direction of the weak-convergence inequality.

The affine approximation minimum (12.12) is positive: zero error would force zero slope by bounded activation and unbounded support, and then force a constant preactivation by strict monotonicity. Its moment formula is continuous along the (L^2) path. Compactness therefore supplies a strictly positive minimum over every compact physical interval, and uniform moment convergence transfers this to finite empirical errors.

Finally, 1701–1736 proves nonzero motion at every positive finite time, not just near initialization. Positivity of the readout and gate makes (delta^{(3)}) nonzero. Its positive second moment provides a positive Gaussian source variance for the next backward query; a bounded response shift cannot destroy its unbounded support. Repeating this argument proves the two lower deltas are nonzero. The adjoint pairings in (12.13) then exclude cancellation of the propagated preactivation velocities. Strictly positive gates and the strictly positive physical clock multiplier preserve nonzero feature velocities. This completes the stronger “no later freezing” claim.

## Dependency audit

I found no unproved specialized mean-field, tensor-program, response-kernel, infinite-dimensional continuation, or numerical-convergence theorem used to bridge a missing step.

The foundational facts used without a full foundational reconstruction have their relevant hypotheses here:

- Laws of large numbers and conditional variance bounds: the initial tuples are iid with the required integrable moments; the conditional Gaussian innovations have the stated conditional independence; fixed-program norms are bounded in probability.
- Gaussian orthogonal projection and integration by parts: the matrix entries are finite-dimensional centered Gaussians; conditioning uses linear constraints after fixing the transcript; the source expressions have bounded formal derivatives. The singular case is explicitly reduced to standard Gaussians and handled by perturbation.
- Countable probability extension and finite-dimensional Borel regularity: the index family is countable, coordinate spaces are real standard Borel spaces, and consistency is supplied by finite unions. These are foundational measure-theoretic constructions, not a dynamical limit theorem.
- Hilbert projection, density, Parseval, and bounded-operator extension: all inputs lie in the specified (L^2) spaces; those spaces are separable under the countably generated construction; the required boundedness and pairings are proved before extension.
- Finite-dimensional spectral calculus and polynomial approximation: covariance matrices are positive semidefinite with spectra in a common compact interval for each fixed program. No derivative of a covariance square root is used.
- Dominated convergence, Fatou, Fubini, Cauchy–Schwarz, and Jensen: the proof supplies bounded derivatives, fixed-factor tail truncations, nonnegative exponential integrands, or finite time (L^2) bounds at the relevant applications.
- Elementary calculus and finite-dimensional local ODE theory: the finite vector fields are smooth, their compact-interval parameter bounds are established, and the fixed-cap population construction explicitly supplies contraction and restart estimates.

The Wasserstein approximation, Gronwall estimates, nonlinear comparison, and path interpolation arguments needed for the theorem are given in the document itself. None of the above foundational facts supplies an unproved substitute for the principal nonlinear analytic step.

## Presentation defects and clarifications

These are separate from mathematical gaps. Neither leaves a theorem obligation unresolved.

1. **Minor — implicit nonzero-input scope of the illustrative conditioning formulas.** At 274–294, (3.1)–(3.2) divide by (\|h\|_2^2), and the removed projection is assigned rank one, without first explicitly saying (h\ne0). The formulas should be introduced as the nonzero-input case. This is not an unresolved singular-query issue in the proof: Section 3.4 covers the degenerate programs, and the actual initial-transpose applications in Section 12 have activation inputs bounded below by (m), hence nonzero. I did not use these fractions at a zero input.

2. **Minor — imprecise algorithm cross-reference.** At 107–108, “BOTH algorithms in (1.3)” points to a display containing the GD updates only. GF is specified immediately afterward at 68–69 and treated explicitly later. Referring to “GD in (1.3) and the corresponding GF specified after it” would make the theorem's reference precise. The intended two algorithms are mathematically unambiguous.

## Final disposition

**PASS for the entire frozen document and the full theorem stated in Section 1.** No mathematical repair, missing specialized dependency, additional competitor-tail assumption, or unproved raw-GD interpolation obligation remains identified by this audit. The presentation items above are not conditions on this verdict.
