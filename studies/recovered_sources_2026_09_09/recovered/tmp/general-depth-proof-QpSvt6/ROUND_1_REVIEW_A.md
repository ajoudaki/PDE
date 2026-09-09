# Independent adversarial mathematical review — Round 1, reviewer A

## Verdict

**PASS.** I found no consequential gap, false implication, missing hypothesis, circular dependency, normalization error, or unresolved consequential notation issue in the stated theorem and its proof. This verdict covers the theorem as actually quantified: the specified single-input, single-target model, each fixed finite hidden depth \(L\ge3\), the fixed activation \(1+\arctan(z)/10\), the displayed parameter metric and updates, and every fixed finite physical horizon. It does not extend the result to other datasets, activations, step-size regimes, simultaneous depth/width limits, or infinite physical time.

The main potentially dangerous dependency in Section 6 closes. In particular, I checked \(L=4\) explicitly before extending the check to arbitrary fixed depth. The forward pass uses only strictly past backward rows and source variances. The current backward pass starts at the top and determines each source variance from an already bounded current upper delta before estimating the next response row. The current return through all upper layers is present. The numerical bounds leave positive margins.

There are no required mathematical repairs. Two optional presentation clarifications appear at the end; neither changes a proof dependency or theorem conclusion.

## Reviewed material, isolation, and reading attestation

- Sole mathematical source: `/tmp/general-depth-proof-QpSvt6/GENERAL_DEPTH_SELF_CONTAINED_PROOF.md`.
- Exact reviewed SHA256: `741331782e571a38ed11896fc342f2ce6291d63b057d456419d799757fe4327f`.
- Observed size: 1,727 lines, 79,533 bytes.
- **Full-document reading attestation:** I read the complete document, consecutively from line 1 through line 1727, including the theorem, all twelve sections and their subsections, every displayed formula, and the closing scope statements. The initial complete reading used line ranges 1–300, 301–620, 621–930, 931–1230, 1231–1530, and 1531–1727. This review is not based on selected sections or a supplied prior verdict.
- Procedural material also read: `/home/amir/.codex/skills/review-ai-paper/SKILL.md` and its `references/severity-rubric.md`. These supplied review procedure and severity terminology only. I imported no mathematical assumption, estimate, theorem, or conclusion from them. The user's isolation and sole-write-target requirements took precedence over the skill's generic instructions to inventory other materials, retrieve sources, or create separate evidence files.
- I did not read any other project file, historical proof, audit report, coordinator message, or agent output. I did not search the project, browse external mathematical sources, spawn agents, or conduct experiments. The numerical checks below are direct arithmetic and inequalities applied to the document. Shell use was limited to reading the authorized material and obtaining the proof's hash and size. This report was written with `apply_patch`; the proof was not modified.

Line references below refer to this exact reviewed version.

## 1. Model, normalization, and elementary tools

### Section 1: theorem and exact equations, lines 16–143

The parameter counts and population types agree: one first-layer field, \(L-1\) hidden operators, and one readout field give \(L+1\) current objects on \(L\) neuron spaces. Adjacent expectations and the rank-one convention \(U\otimes V:B\mapsto U\mathbb E[VB]\) are consistently typed. No comparison requires pairing coordinates from different populations.

The finite metric is essential and is explicitly specified in Section 10, lines 1200–1205. With vector squared norms \(n^{-1}\|v\|_2^2\) and ordinary matrix Frobenius squared norms, direct differentiation gives

\[
 \nabla f_n=
 \left(\delta^{(1)},
       (\delta^{(\ell)}(h^{(\ell-1)})^T/n)_{\ell=2}^L,
       h^{(L)}\right).
\]

Thus the displayed GD updates are precisely the gradient steps for that metric. Their squared gradient blocks are exactly (1.6). In particular, the two vector blocks and the matrix blocks have different coordinate normalizations, and the proof does not silently replace one by the other. On normalized finite neuron spaces, the operator Hilbert–Schmidt norm of a matrix is its ordinary Frobenius norm, so the finite and population metric conventions agree.

The transformation also has the correct normalization:

\[
 F'(z)=10(1+z^2)=1/\phi'(z),\qquad
 (\phi\circ F^{-1})'=(\phi'\circ F^{-1})^2\le1/100.
\]

Consequently the raw first-coordinate feature velocity is \(\delta^{(1)}\), while the transformed velocity is \(q^{(1)}\). Equations (1.5) and (9.3) are compatible; the proof does not assert that the transformed coordinates carry the same constant Hilbert metric as the raw coordinates.

### Section 2: elementary bounds and limiting tools, lines 145–236

The bounds \(5/6<\phi<7/6\), \(0<\phi'\le1/10\), and \(|\phi''|\le1/5\) are valid. The \(1/4\)-net argument gives a factor two in the bilinear-form approximation, Gaussian threshold five when the operator threshold is ten, and hence the exponent \(100n/8\) in (2.2). The resulting probability tends to zero even after the \(9^{2n}\) union bound. The normalized initial readout second moment is \(n^{-2}\), as stated.

The finite-dimensional \(\mathcal W_2\) criterion, the passage to continuous quadratic-growth tests, the index coupling bound, and the discrete/continuous Gronwall comparisons are sufficient for their later uses. The bounded-gate/unbounded-factor argument (2.4) is correct: its tail is taken on the fixed limiting \(L^2\) factor. It supports the curve chain rule without asserting unrestricted Fréchet differentiability of the activation map on \(L^2\). The initial pair \((G,F(G))\) is separately admitted as a root with all finite moments; later cubic operations are not included in the Lipschitz probe class.

## 2. Gaussian identification and construction of the fixed spaces

### Section 3: adaptive matrix reuse, lines 238–455

I checked the conditioning formulas and the source/response derivation rather than assuming a tensor-program result.

For one forward call, (3.1) is the rowwise Gaussian projection conditioned on \(Wh=y\). Applying the transpose gives (3.2), with innovation variance \(\|u\|_2^2/n\). The projection removed from the fresh Gaussian has normalized expected squared norm \(1/n\). This justifies the **full uncentered input second moment** as the source variance. Subtracting the squared response contribution would be an error; the document does not do so.

For multiple calls, the first two terms of (3.3) satisfy both sets of constraints because \(U^TY=Q^TV\), and the remaining Gaussian matrix acts between the two orthogonal complements. Adaptive queries cause no additional nonlinear conditioning on unexplored residuals: each input is measurable before the new linear observation. Induction preserves the conditional independence of residuals for different matrices.

In (3.4), all quantities in the regression coefficients are empirical contractions of already available same-population tuples. Positive limiting Grams therefore justify coefficient convergence. The conditional averaging argument controls both bounded Lipschitz tests and second moments, including the cross-term and Gaussian-square variances. Discarded fixed-rank projections have vanishing normalized \(L^2\) norm. These facts establish joint empirical \(\mathcal W_2\) convergence for each fixed finite program.

The non-classic step (3.5) follows from the displayed calculation. Write \(h_\perp=h-\sum_r\alpha_rv_r\). Its orthogonality to the old forward inputs removes the response part of each old reverse answer from \(\mathbb E[q_sh_\perp]\). Gaussian integration by parts then gives

\[
 \beta=\mathbb E\nabla_\zeta h
            -\sum_r\alpha_r\mathbb E\nabla_\zeta v_r.
\]

Substitution into the conditional regression cancels the old response coefficients. The new Gaussian source is a linear combination of old sources in the same orientation plus a new independent Gaussian, with covariance exactly the uncentered second moments of the forward inputs. This also explains independence between distinct source groups. Derivatives must differentiate the complete explicit expression while holding deterministic selected coefficients and covariance parameters fixed; that is the convention subsequently used in Sections 4 and 6.

Section 3.4 handles singular Grams without assuming inverse convergence. Fresh input jitter supplies a strictly positive Gram Schur complement at each fixed program call. The finite perturbed/unperturbed comparison uses the bounded initial matrix actions and a finite Lipschitz induction, with a constant independent of width and of \(0<\epsilon\le1\). In the scalar recursion, coefficients and formal derivatives can be bounded successively because every instruction depends on previously constructed quantities. Continuous covariance square roots supply a Gaussian coupling even at a rank drop; bounded continuous formal derivatives permit dominated convergence. Null covariance directions annihilate the associated input combination, so they cannot change the contracted response. No vanishing formal derivative is inferred merely from a zero-variance source slot.

### Section 4: actual clipped Euler law, lines 457–588

The clip has the stated monotonicity and Lipschitz properties. The readout bound makes the top product a legitimate bounded-derivative instruction after extension; each interior clipped product has bounded derivatives as well. The initial non-Lipschitz cubic appears only in the authorized root pair.

Unrolling the trained matrices produces precisely the two normalized rank memories in (4.2). Freezing contractions gives a causal fixed finite program. Restoring actual contractions uses the displayed bilinear difference estimate and a finite instruction induction, not a claim uniform in the number of time steps. Later width limits respect that restriction.

Equations (4.3)–(4.5) include both initial-matrix responses and trained rank memories. Forward memories are strictly past-time; backward memories include the current time. In particular (4.6) correctly differentiates the current feature appearing in the current upper response. This term is indispensable and is retained at every interior layer.

### Section 5: common spaces and fixed-clip flows, lines 590–755

The countable program construction is consistent under finite unions because every finite union has the joint limit of the same finite-width calculations. The included coordinate functions generate the sigma field, and the finite-coordinate approximation argument establishes their dense span in \(L^2\).

Passing finite operator bounds and transpose pairings to limiting second moments gives (5.1) on the countable rational domain. In particular a zero input difference has zero output difference. Density then gives bounded operators on equivalence classes, and the pairing proves that the reverse actions are their actual adjoints. This is enough for the subsequent state-space construction; it is not operator-norm convergence across different widths.

The primal bounds (5.4) are triangular. The bounded readout velocity controls the top delta, which controls the top matrix increment. Descending in depth then controls the next delta and matrix in turn. No bound for a lower matrix is needed to obtain its own upper query bound. These constants can be large with depth, but remain finite at each fixed depth and horizon.

The estimates (5.6)–(5.8) give linear cap dependence for the field (5.3). At each backward step, the previous backward error is multiplied by a cap-independent operator/gate constant; the new \(R\)-dependent term multiplies a forward difference already controlled by (5.6). Thus repeated descent does not introduce powers \(R^{L-2}\). The asymmetric readout estimate (5.7) correctly requires a pointwise bound only on the reference readout.

The closed path set with bounded readout is suitable for the stated contraction construction. The primal bounds allow continuation at each fixed cap. The local Euler defect and the global estimate (5.9) have constants independent of width on the initial norm event. Taking width first for a fixed mesh and then refining it establishes the fixed-clip limit without applying the finite-program result to an increasing number of instructions.

## 3. Section 6: explicit depth-four audit and all constants

Locations: lines 757–939, especially (6.2)–(6.9).

### The current returns at \(L=4\)

Suppress the time index \(k\) in the following deterministic scalars, and set

\[
 e_\ell=\mathbb E[\phi''(Z_k^{(\ell)})\tau_R(q_k^{(\ell)})],
 \qquad
 g_\ell=\mathbb E[(\phi'(Z_k^{(\ell)}))^2\tau_R'(q_k^{(\ell)})].
\]

Then (4.6) gives

\[
 b^{(4)}_{kk}=\mathbb E[W^{(5)}_k\phi''(Z^{(4)}_k)],
 \quad b^{(3)}_{kk}=e_3+g_3b^{(4)}_{kk},
\]
\[
 b^{(2)}_{kk}=e_2+g_2e_3+g_2g_3b^{(4)}_{kk}.
\]

Thus the return through layer 4 occurs in both lower responses. The row-sum estimates control the past response slots as well, not just these diagonals. Since \(0\le g_\ell\le1/100\), the current return is bounded by the \(B_{\ell+1,k}/100\) term used in (6.9).

### The actual induction order

At time zero, the top readout makes its delta and forward-source derivatives zero. Descending gives zero backward rows and zero delta laws. Reverse-source formal derivatives at such a zero-variance slot need not vanish; the proof preserves them in the later forward calculation.

Assume the stated bounds for all rows and deltas strictly before time \(k\).

1. The bottom transformed recurrence bounds \(a^{(2)}_{jr}\) for \(j\le k\) using only \(b^{(2)}_{uv}\) with \(u<j\le k\).
2. At layer 2, the derivative of \(Z^{(2)}_j\) involves only \(\delta^{(2)}_u\) for \(u<j\). Its envelope therefore needs only past \(q^{(2)}_u\), past \(B_{3,u}\), and past variance \(\|\delta^{(3)}_u\|_2^2\). This establishes the current \(a^{(3)}\).
3. The identical argument at layer 3 uses past \(B_{4,u}\) and past \(\|\delta^{(4)}_u\|_2^2\), establishing the current \(a^{(4)}\).
4. The top calculation bounds the current \(\delta^{(4)}_k\) and \(B_{4,k}\).
5. These give the current source variance \(\operatorname{Var}(\zeta^{(3)}_k)=\|\delta^{(4)}_k\|_2^2\), then a bound for \(q^{(3)}_k\), then \(\delta^{(3)}_k\), then \(B_{3,k}\).
6. The just obtained \(\delta^{(3)}_k\) and \(B_{3,k}\) supply the current layer-2 source variance and response bound in exactly the same order. The bottom query then uses \(\delta^{(2)}_k\) and \(B_{2,k}\).

There is no use of an unproved current lower row to bound a current upper row. The same local forward step and local backward step can be repeated any finite number of times. This supplies the arbitrary-fixed-depth induction after the explicit \(L=4\) check.

### Derivative rows and exponential envelopes

For an interior forward-source derivative, the only dependence of \(q_u^{(\ell)}\) on that source group is through its explicit feature history. Hence (6.3) follows by summing absolute derivatives and applying the scalar Gronwall comparison. The direct derivative of the present forward source contributes exactly one. For a single reverse source, the additional direct query derivative occurs once, yielding the forcing \(A\Delta/10\) for \(Z\) and \(A\Delta/100\) for \(H\).

The estimate for \(E_{\ell,j}\) uses only past bounds. Jensen's inequality over the time slots, followed by the one-dimensional Gaussian exponential estimate, does not require temporal independence. Cauchy–Schwarz in the current row estimate does not require independence between the current query and the envelope.

At the top, differentiating the readout sum produces the \(\Delta\sum T_u/100\) term. Differentiating the top gate produces \(aST_j/5\). Their sum is bounded by \((73/300)S\max T_v\). The top recursion is strictly past-time, so its Gronwall bound is valid without a current response assumption.

### Arithmetic check

All bounds below use \(A=S=3/2\), \(a=7/6\), and \(Q=7/40+7/6=161/120\). Bounds at smaller \(S\) are no larger.

| Quantity or location | Checked value or sufficient bound |
|---|---|
| Bottom forward coefficient, (6.2) | \(a^2+1/50=1243/900<3/2\) |
| Linear exponent in (6.5) | \(AS(a/5+1/100)=219/400\) |
| Quadratic exponent in (6.5) | \(\tfrac12(AS/5)^2(7/40)^2=3969/1280000\) |
| Envelope moments | The exponent after the \(p\)-th root is below \(3/5\) for \(p=1,2\); hence \(\|E\|_1<4\), \(\|E\|_2<2\sqrt2<3\) |
| Interior forward coefficient, (6.6) | \(a^2+4A/100=1279/900<3/2\) |
| Top derivative-row exponent | \(A(73/300)S^2=657/800\) |
| Top derivative-row envelope | \(e^{657/800}<5/2\), using \(3^5 2^6=15552<15625=5^6\) |
| Top delta norm | \(aS/10=7/40\) |
| Top derivative contribution to \(B_L\) | \((73/300)S(5/2)=73/80\) |
| Top learned covariance contribution | \(a^2S^3/100=147/3200\) |
| Total top row, (6.7) | \(3067/3200<1\) |
| Interior delta norm, (6.8) | \(Q/10=161/1200<7/40\) |
| Interior derivative contribution | \(3(Q/5+1/100)=167/200\) |
| Interior learned covariance contribution | \(SQ^2/100=77763/2880000\) |
| Total interior row, (6.9) | \(2482563/2880000<9/10\) |

The current source variance bound in (6.8) is established from the upper delta before being used. The learned covariance row is bounded by the sum of products of \(L^2\) delta norms, with the correct factor \(\Delta\) and total length at most \(S\).

Finally, every query, including the bottom query, is a centered Gaussian source of variance at most \((7/40)^2\) plus a shift bounded by \(a\). The shift may depend on the source, but

\[
 q^2/16\le\zeta^2/8+a^2/8
\]

is pointwise. The Gaussian integral in (6.10) therefore has the correct factors \(49/288\) and \(1-49/6400\), and is below two. This is a uniform one-time exponential moment, not a claim about a Gaussian path supremum.

## 4. Clip removal, uniqueness, and all finite physical times

### Sections 7–8: lines 941–1075

The passage from fixed-cap Euler queries to fixed-cap flow queries uses \(L^2\) convergence at each specified time, followed by an almost-everywhere subsequence and Fatou. It does not need one almost-sure subsequence valid simultaneously at all times.

The decomposition (7.2) is algebraically exact even though the two states use different recursively clipped upper deltas. Its reference tail and forward error terms have the stated coefficients. Descending through finitely many layers yields (7.3) with a constant independent of both caps and only linear growth in the smaller cap. No competitor tail estimate or pointwise competitor readout bound is assumed.

The Gaussian-tail calculation gives

\[
 \|(|q|-R/2)_+\|_2\le8e^{-R^2/256}.
\]

Thus the comparison factor \(e^{C(1+R)S}\), and also an additional factor \(1+R\) when comparing velocities, are dominated by the tail decay for every fixed finite \(C\). This proves a Cauchy sequence of clipped paths in the complete stated state space. Applying the same comparison to the limiting state identifies its actual uncut backward fields and velocities, so the limiting integral equation is the desired one.

For uniqueness, the competitor's compact-interval primal bounds merely change \(C\); the Gaussian decay still dominates. A restart contributes the already controlled initial discrepancy at the restart time and another finite exponential factor. Accordingly, uniqueness is not inferred from a nonexistent uncut local-Lipschitz estimate on arbitrary \(L^2\) balls.

At finite width, the tail statistic in (8.1) is a continuous quadratic-growth observation. Its uniform convergence follows from fixed-cap time-Lipschitz bounds and a time net. This avoids assuming uniform finite-width exponential moments. The actual \(O_{\mathbb P}(n^{-1})\) readout is compared to the zero-readout reference through the asymmetric estimate. The order of limits is fixed cap, width, then cap removal, as required.

### Section 9: lines 1077–1196

The rank-one velocity has the same product norm in HS and operator norms, and its difference bound also holds in HS norm. Hence the trained increments belong to HS even though the initial actions need not.

The scalar Fréchet differentiability proof is sufficient. For a fixed \(L^2\) pairing factor \(B\), (9.2) splits the nonlinear remainder into a bounded-factor quadratic term and a tail term linear in the perturbation. Taking perturbation size to zero before removing the tail proves the needed little-oh estimate. Expanding the scalar output down through the layers only requires finitely many such fixed old reverse factors. Terms containing two varying factors have quadratic size. Gradient continuity follows by bounded-gate multiplication and operator-norm continuity. This justifies (9.3) and the raw Hilbert gradient structure without an invalid \(L^2\)-Nemytskii differentiability assumption.

The feature-time identity \(f_s=\sum K^{(\ell)}\) includes all blocks, and the readout block gives \(f_s\ge25/36\). Starting from \(f(0)=0\), the level-one point satisfies

\[
 0<s_*\le36/25<3/2.
\]

The upper bound on \(f_s\), not just this lower bound, is used to prove divergence of the physical-clock integral as \(s\uparrow s_*\). Its inequality direction is correct: \(1-f(s)\le B_*(s_*-s)\) gives a logarithmic lower bound on \(t(s)\). Thus every finite physical horizon is covered by the one constructed feature interval.

Raw uniqueness is also addressed, rather than assumed from transformed uniqueness. A competing raw curve has continuous \(L^2\) backward fields and HS matrix increments, so its deficit obeys the scalar exponential identity. Its coordinatewise absolutely continuous version permits the ordinary scalar chain rule for the cubic \(F\). Equation (9.7) then proves transformed \(L^2\) membership from the integral of \(q^{(1)}\). The positive deficit gives an increasing feature clock, and feature uniqueness plus clock uniqueness identifies the competitor, including restarts from reached states.

## 5. Exact GD, probes, velocities, and whole paths

### Section 10: lines 1198–1347

The finite GF existence argument controls the readout first and then the hidden matrices downward, using nonincrease of the residual magnitude. At each fixed width these bounds prevent finite-time escape. The finite feature clock has its level-one point before \(S=3/2\) when \(f_n(0)>-1/24\), since \((25/36)(3/2)=25/24\). The required initial event has probability tending to one.

Raw GD is handled separately from transformed Euler. Direct expansion of the cubic gives exactly (10.1). From \(\|q^{(1)}\|_2\le C\sqrt n\),

\[
 \|q^2\|_2/\sqrt n\le C^2\sqrt n,
 \qquad \|q^3\|_2/\sqrt n\le C^3n.
\]

The summed transformed-coordinate defect is therefore

\[
 O(\eta_n\sqrt n+\eta_n^2n)=O(n^{-3/2}+n^{-3}).
\]

No empirical fourth- or sixth-moment hypothesis is needed. The positive-prefix primal bound justifies the bounded increments used in this summation, including the step into the first potentially bad endpoint.

The recurrence (10.3) applies the asymmetric clip comparison to the actual raw-GD nodes and the exact finite clipped reference. The random partition creates no law-of-large-numbers issue: (10.4) is a pathwise quadrature estimate using the reference tail statistic's fixed-cap time-Lipschitz bound. Gronwall yields the stopped comparison without invoking Section 3 for the width-dependent number of GD steps.

The stopping argument has real margins. The population feature clock lies below \(36/25=1.44\), whereas the stop threshold is \(147/100=1.47\), below the constructed endpoint (1.5). The deficit minimum on \([0,T+1]\) is positive for each fixed \(T\). Uniform predictor and clock errors contradict both possible first-exit conditions, including an exit at the final interpolation node. The constants are allowed to depend on \(T\), so this does not claim an infinite-time interchange.

Fractional use of the same cubic identity covers raw interpolation between nodes. Comparing both finite GF and raw GD to the same finite clipped reference proves the same-width state-distance assertion. The selection order—cap, fixed mesh, then all sufficiently large widths—establishes full-sequence convergence in probability, not merely a subsequence result.

### Section 11: lines 1349–1458

The ordinary probe class is controlled by bounded operator actions and Lipschitz coordinate operations. Backward fields are additionally controlled by (7.3). Bounded continuous gates multiplying unbounded \(L^2\) factors are handled by truncating those factors first. Uniform quadratic tails follow from the compact limiting \(L^2\) paths and uniform \(\mathcal W_2\) convergence. This makes the extension to all stated finite probe lists and finite joint time arguments legitimate.

The velocity formula (11.1) differentiates both the trained matrix and its input feature. Its first term has coefficient \(\mathbb E[(H^{(\ell-1)})^2]\), exactly as required by the rank-one update. Physical velocities have the common multiplier \(2(1-f)\).

For raw GD interpolation, each parameter velocity is constant on the step, but recomputed hidden velocities are not. The document accounts for that distinction. Normalized hidden preactivation changes are \(O(\eta_n)\); their coordinate supremum is at most \(O(\eta_n\sqrt n)\). Bounded \(\phi''\) converts this into a uniform gate change. The finite layer induction in (11.2) then bounds the discrepancy between actual recomputed velocities and node formulas by \(O(\eta_n\sqrt n)=O(n^{-3/2})\). The estimate covers the stated endpoint derivative convention and needs no additional coordinate moment assumption.

The measurable-version and integration argument produces absolutely continuous population coordinate paths. The interpolation bound (11.3), together with the established integrated squared-velocity bounds and fixed-grid joint \(\mathcal W_2\) convergence, proves \(\mathcal W_2(C([0,T]))\) convergence. This is stronger than finite-dimensional convergence alone, and the additional argument needed for it is present.

## 6. Every nonlinear and non-lazy obligation

### Section 12.1: initial transpose induction, lines 1462–1552

The initial forward laws and moments in (12.1) retain the constant activation offset. Gaussian symmetry removes the cross term, giving \(m_\ell>1\).

The top transpose coefficient is

\[
 \frac{\mathbb E[Z^{(L)}_0H^{(L)}_0\phi'(Z^{(L)}_0)]}{m_{L-1}}
 =\frac1{100m_{L-1}}
   \mathbb E\frac{Z^{(L)}_0\arctan Z^{(L)}_0}{1+(Z^{(L)}_0)^2}>0.
\]

At each lower transpose, conditioning on the forward answer and the independent upper matrices makes the reverse input measurable without exposing that matrix's residual. Thus the one-forward/one-transpose calculation remains applicable. The preceding independent Gaussian term has zero contribution to the coefficient pairing. Equations (12.3)–(12.4) therefore use the correct positive coefficients and the full input second moments for their variances. The bounded-gate truncation argument justifies the unbounded reverse inputs.

Adjunction proves (12.5): pairing the matrix term in \(V^{(\ell)}\) with \(B^{(\ell)}\) gives precisely the preceding layer's pairing. Hence every leading hidden velocity \(V^{(\ell)}\), and its product with the strictly positive gate, is nonzero.

### Section 12.2: onset and kernel change, lines 1554–1615

The readout integral yields \(W^{(L+1)}(s)/s\to H^{(L)}_0\). Bounded-gate multiplication and bounded operator continuity then justify the downward limits \(\delta^{(\ell)}(s)/s\to B^{(\ell)}\). Applying (11.1) upward gives the \(L^2\) expansions (12.6). Their integrals and rank-one HS expansions have the asserted orders.

In feature time, the hidden kernel sum contributes \(\Gamma s^2\), and the readout kernel contributes \(m_L+\Gamma s^2\). Since \(s(t)=2t+o(t)\), the total physical kernel is

\[
 m_L+8\Gamma t^2+o(t^2),\qquad \Gamma>0.
\]

The factors in (12.7) and the integrated squared-velocity coefficient \(16/3\) are correct. Every trained hidden block has a nonzero second-order leading displacement, and the readout has nonzero first-order displacement. These are fixed-depth population effects, not effects that vanish with width or with an auxiliary activation parameter.

### Section 12.3: non-affinity throughout each finite horizon, lines 1617–1684

The top forward correction is bounded by \(AaS^2/10=63/160\). For an interior layer, the correction is dominated by a variable depending only on the reverse source group, with expectation at most \(ASQ/10=483/1600\). That dominator is independent of the layer's forward Gaussian source. Markov's inequality therefore supplies the factor \(1117/1600\) in the positive-tail bounds (12.9), even though the actual correction need not be independent of the source.

At the bottom, \(\mathbb E R_{1,k}\le S(Q/10+a)=1561/800<2\); independence from the initial root and the threshold four give (12.10). The positive lower tails pass to the flows using the closed-half-line direction of the weak-convergence inequality, which is the correct direction here.

Consequently each hidden law has unbounded support in both directions at every reached time. A bounded strictly increasing activation cannot agree almost surely with an affine function on such a law: a nonzero slope contradicts boundedness, and zero slope contradicts strict monotonicity and nondegeneracy. The regression formula (12.11) is valid with finite second moments and positive variance. Continuity of its moments and compactness in time then give a strictly positive minimum on each compact physical interval. The uniform empirical statement follows from the established moment convergence.

### Section 12.4: no later freezing, lines 1686–1720

This argument proves the stronger every-positive-finite-time assertion; it does not merely reuse the small-time expansion.

At a chosen \(s>0\), the pointwise positive readout and gate imply a nonzero top delta. Convergence of the approximating backward laws bounds the current reverse-source variance away from zero. A Gaussian source with such a variance plus a uniformly bounded, possibly dependent shift has positive tails at arbitrarily large fixed thresholds. Closed-half-line passage proves that the limiting next query is nonzero, and the strictly positive gate gives a nonzero next delta. Repeating downward proves this for all layers, including the bottom.

Equation (12.12) then follows by actual adjunction and (11.1). Its positive pairing excludes cancellation that could otherwise make a hidden preactivation velocity zero despite a nonzero local update. Strictly positive gates preserve nonzero feature velocities, and the positive physical-clock multiplier preserves them at every finite \(t>0\). This completes the nonfreezing obligation separately from the initial non-lazy expansion.

## Claim-level assessment and dependency check

| Central claim | Controlling proof components | Assessment |
|---|---|---|
| Self-contained adaptive Gaussian limits and fixed bounded actions with actual adjoints | Sections 3–5 | Sound for the specified programs and their stated extensions |
| Cap-independent response and source-variance bounds at every fixed depth | Section 6, with (4.3)–(4.6) | Sound; explicitly checked at \(L=4\), then by the repeated local induction |
| Uncut population flow, uniqueness, restart, and all finite physical horizons | Sections 7–9 | Sound; linear cap growth is dominated by the proved Gaussian tails |
| Full-sequence joint MF/GF/exact-GD convergence, velocities, kernels, and path laws | Sections 8, 10–11 | Sound; raw-GD defects and between-node velocities are separately controlled |
| Persistent non-affinity, movement of all trained blocks, nonconstant kernel, and no later hidden freezing | Section 12 | Sound; each obligation has an independent sufficient argument |

No claim above rests on an unavailable non-classic citation, a presumed earlier PASS, an experiment, or an unverified external result. No major or fatal concern was found. The result's plausibility and the validity of this supplied proof were assessed separately; the PASS is based on the checked internal derivations.

## Optional exposition, not required repairs

1. **Lines 43–58 and 1200–1205:** bringing the finite metric convention forward to the first display of raw GD would help readers who otherwise initially interpret “GD” as Euclidean GD in every displayed coordinate. The later metric specification already resolves this, and the equations and kernel normalizations agree.
2. **Lines 1622–1628:** explicitly writing \(u>0\) alongside the top tail bound (12.8), as is done for the interior bound at line 1639, would clarify its use. The variance-lower-bound argument is being used for positive tail thresholds; all support and non-affinity conclusions require only those thresholds. No negative-threshold estimate is needed anywhere in the proof.

**Final assessment:** the stated theorem passes this isolated full-document mathematical review. No consequential issue remains outstanding.
