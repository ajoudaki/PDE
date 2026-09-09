# Independent adversarial proof audit

## Verdict

**NOT CLEAN AS WRITTEN: one required notation correction, with no substantive mathematical gap found.**

The mathematical proofs support the two candidate claims: the one-sample, small-stored-readout L2 joint limit on every fixed finite physical interval under \(\eta_n\sqrt n\to0\), and the corresponding L3 joint limit with \(\eta_n=n^{-2}\) on the explicitly stated local interval. All six embedded L3 proof stages discharge their mathematical premises. The sole required correction is the undefined norm in §4, detailed below; its intended inequality is valid and is also established in standard notation in §6. This finding does **not** invalidate either limit theorem.

No additional initialization, covariance-rank, evolving fourth-moment, competing-solution tail, uncut Lipschitz, or continuation hypothesis is needed for the claims actually stated. No global L3 result, continuation past the constructed endpoint, or restart beyond that endpoint is certified here.

## Inputs, isolation, and full-read coverage

The only input contents used were these two files. References to line numbers below refer to this exact `arctan_limits.md`, unless `NOTATION.md` is expressly named.

| Input | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| `/tmp/pde-established-arctan-review.L0FZTB/NOTATION.md` | 98 | 5,110 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `/tmp/pde-established-arctan-review.L0FZTB/arctan_limits.md` | 3,117 | 143,021 | `c067db75cba14b345dd86f69bc4d240e76cdb631bb7985bb5bc73ff75f238c34` |

`NOTATION.md` was read completely, including its population-space, normalization, clock, and scope requirements. The complete chapter was read in order through these coverage intervals:

| Chapter lines | Coverage |
|---|---|
| 1–800 | Complete. An initially truncated combined display was repaired by reading lines 285–550 in full before proceeding. |
| 801–1100 | Complete |
| 1101–1420 | Complete |
| 1421–1750 | Complete |
| 1751–2070 | Complete |
| 2071–2390 | Complete |
| 2391–2720 | Complete |
| 2721–3117 | Complete through EOF |

Targeted rereads subsequently checked notation and several delicate estimates. Those searches supplemented the full reading. No source history, rest of the repository, previous review, other agent, external paper, browsing, Git operation, or code experiment was used. No input was edited. `REVIEW.md` is the only output written.

Both input hashes were checked again after writing the review and were unchanged.

## Required fix

### R1 — Replace the undefined population norm in §4

**Location:** lines 1409–1412, immediately before the fixed-clipping Lipschitz argument.

The expression

\[
|W^{(4)}\phi'(Z^{(3)})-\widetilde W^{(4)}\phi'(\widetilde Z^{(3)})|_{2,3}
\]

uses a norm symbol defined in neither allowed input. It is an accidental notation remnant. `NOTATION.md`, lines 59–63, specifies the population norm notation. Replace this expression by

\[
\big\|W^{(4)}\phi'(Z^{(3)})
 -\widetilde W^{(4)}\phi'(\widetilde Z^{(3)})
\big\|_{L^2(\Omega_3)}.
\]

The resulting displayed inequality is correct. Indeed, writing the difference as

\[
\phi'(Z^{(3)})(W^{(4)}-\widetilde W^{(4)})
+\widetilde W^{(4)}
 [\phi'(Z^{(3)})-\phi'(\widetilde Z^{(3)})]
\]

and using \(|\phi'|\le1\), \(\operatorname{Lip}(\phi')\le2\), and
\(\|\widetilde W^{(4)}\|_\infty\le aS\) gives exactly the claimed right-hand side. With initial readout bounded by one, the stated replacement coefficient \(2(1+aS)\) is sufficient. Lines 1960–1973 independently give this argument with standard norms and explain the asymmetric use of the reference readout bound.

**Severity:** required for a literally self-contained, notation-compliant manuscript; no theorem-level mathematical repair. No additional required fix was identified.

## L2 audit

### Model, Gaussian conditioning, and common actions

The initialization, residual, loss, and mobilities in lines 56–84 agree with the notation contract. In particular, stored readout variance is \(n^{-2}\), not standard deviation \(n^{-2}\), and its normalized Euclidean size is \(O_{\mathbb P}(n^{-1})\). The residual is absent from each \(\delta\) and enters the updates as \(-2r\). The three kernel normalizations in lines 415–421 agree with the parameter metric.

The two conditional examples (L2.8)–(L2.9) retain the forward/transpose overlap. Their denominators are nonzero almost surely under the prescribed initialization and \(\Delta>0\). In the general conditional formula (L2.12), the compatibility identity \(U^TY=R^TV\) ensures that its deterministic part satisfies both observed matrix equations. The remaining matrix is projected in both directions. Consequently the transpose is never replaced by a fresh independent matrix.

The fixed-program proof in lines 227–300 is sufficient for the stated Lipschitz measurement class:

- The net bound controls the ordinary operator norm, with a fixed sufficiently large constant and probability tending to one.
- The new input jitter is independent of the existing history. Its Schur complement has limiting squared size at least \(\varepsilon^2\); the cross-term variance and fixed-rank correction are correctly scaled.
- Fresh output projections have normalized squared mean \(\operatorname{rank}(U)/n\). Conditional averaging yields joint weak convergence and convergence of second moments.
- The coupling bound (L2.16) removes jitter at fixed program size. It does not require convergence of an unperturbed Gram inverse or pseudoinverse.

The consistent finite laws in lines 304–337 generate actual layer probability spaces. Bounded finite-coordinate functions give the required dense subspaces of their \(L^2\) spaces. The finite operator bound makes the matrix assignment independent of its representative and extends it continuously. Passing the finite bilinear identity proves adjunction. There is no assumption that the initial action is Hilbert–Schmidt, nor an operator-norm identification across widths.

### Global existence and the two discretizations

The transformed flow (L2.20) is locally Lipschitz in (L2.21) on the stated operator- and readout-bounded sets. The pointwise bound on the reference readout is precisely what makes the top backward product Lipschitz. The complete closed path set used for integral iteration preserves this bound.

The output chain rule and adjunction give

\[
\dot f=-2rK,\qquad \dot{\mathcal L}=-4r^2K,\qquad K\ge0.
\]

Thus \(|r|\) cannot increase. The readout supremum grows at most linearly on each fixed physical interval; the matrix and transformed-coordinate bounds in (L2.25) then exclude finite-time blow-up. The continuation argument uses only reached states with these inherited bounds. The same reasoning justifies the flow-side constants in the stopped Euler comparison. The separate readout-supremum argument at lines 459–464 closes the component not controlled by the state metric.

The oracle construction freezes only finitely many deterministic population contractions. Its stored matrix memory and its declared preactivation are correctly distinguished in (L2.30). Their discrepancy is exactly an empirical-minus-population contraction sum. Consequently (L2.31) transfers the fixed-program result to empirical-feedback Euler without applying Gaussian conditioning to an unjustified deterministic treatment of random coefficients.

The proof-mesh order in (L2.32) is valid: fix \(\Delta\), take width to infinity, then decrease \(\Delta\). The constants may depend on this fixed mesh. This is separate from the actual GD step condition.

For raw GD, the identity

\[
F(z+\eta\phi'(z)b)-F(z)
=\eta b+\eta^2z\phi'(z)^2b^2
+\frac{\eta^3}{3}\phi'(z)^3b^3
\]

is exact. If \(\|b\|_2/\sqrt n\le C\), then
\(\|b\|_\infty\le C\sqrt n\); hence the normalized quadratic and cubic defects are bounded by \(C(\eta^2\sqrt n+\eta^3n)\). Summing over physical time gives (L2.34). All three terms \(\eta\), \(\eta\sqrt n\), and \(\eta^2n\) vanish under the stated assumption. The fractional-step identity also covers the transform of the specified raw linear interpolant. No exact transformed-Euler interpretation of raw GD is used.

### Measurements, velocities, paths, and initial motion

The backward measurement \(P=(W^{(2)})^*\delta^{(2)}\) is covered before multiplication by an unbounded varying factor is allowed. Uniform \(\mathcal W_2\) convergence and compactness of its continuous population \(L^2\) path supply the uniform squared tails in (L2.35). This legitimizes the later gate products and matrix calls, including (L2.36). A uniform fourth moment is unnecessary.

At GD endpoints the raw parameter slopes equal the finite gradient vector field. Between endpoints the product rule for recomputed hidden coordinates introduces changed gates. The bounded-part/tail decomposition at line 590 controls these terms, including their squared speeds. Lines 611–626 apply the same reasoning to feature velocities. The polygonal path estimate (L2.38), together with joint grid laws, proves the stated \(\mathcal W_2\) convergence for the supremum path metric, including its second moments.

The expansions (L2.42)–(L2.43) have the correct factors. In particular, with the variables defined in lines 630–645,

\[
E_2[US_0]=\mu_1\nu+\gamma_1>0,
\qquad
K(t)=k_3+8(\mu_1\nu+\gamma_1)t^2+o(t^2).
\]

The independent Gaussian innovation in (L2.40) makes \(\gamma_1>0\), and the displayed pairing makes \(S_0\ne0\). The nonaffinity argument uses positive initial Gaussian variance and continuity of the actual regression moments; it does not require preservation of Gaussianity at positive times.

The restart argument at line 540 is also valid for the measured state: joint laws preserve norms and inner products of generated probes; the induced isometry intertwines the action, adjoint, coordinate operations, and rank-one updates. The future integral iteration stays in those generated spaces. A finite list of fields and operators is not being mistaken for a finite-dimensional scalar state.

## L3: audit of all six embedded stages

### 1. §3 — Source identification, rank changes, and exact derivatives

**Premises discharged:** fixed finite program; independent original Gaussian matrices; queries measurable before their answers; bounded first derivatives of the coordinate instructions; root tuples with finite second moments. The Gaussian root \((Z_0^{(1)},F(Z_0^{(1)}))\) meets the last condition because its required sixth moment is finite. Global Lipschitz continuity of \(F\) is not assumed.

Conditional residual independence survives interleaving the two matrices: once the current transcript is fixed, a new query constrains only the selected matrix. Coordinate calculations are functions of the transcript and add no separate constraint. The conditioning formula (S.1) therefore applies successively to both orientations of both matrices.

The identification of the response coefficient in (S.3) is an actual calculation. If \(H_\perp=H-\sum_r\alpha_rV_r\), then the old forward-input response in \(Q_s\) pairs to zero with \(H_\perp\). Gaussian integration by parts gives

\[
E[\zeta H_\perp]=\Gamma_U E\nabla_\zeta H_\perp.
\]

For positive definite \(\Gamma_U\), inserting this into (S.2) cancels the old response derivatives carried by \(Y\alpha\). The result is exactly

\[
W_0^{(\ell)}H
=\xi_H+\sum_s U_s E\partial_{\zeta_s}H.
\]

The fresh Gaussian covariance is \(E[HH']\) for the corresponding inputs; it is not the covariance of an incorrectly independent matrix answer. Independence of the Gaussian source groups is compatible with dependent forward and reverse **actions**, because the response terms retain their overlaps.

Lines 1114–1140 correctly handle singular limits in two separate steps. Input jitter first proves empirical convergence using positive limiting Gram matrices. The explicit scalar derivative recursion is then passed to zero jitter by finite causal induction, continuous covariance square roots, and bounded-derivative domination. This second step is essential: law convergence alone would not identify derivatives at singular support. It is present here. For a singular covariance \(\Gamma\), if the vector of transpose inputs has second-moment matrix \(\Gamma\), then every vector in \(\ker\Gamma\) contracts to zero almost surely. Thus the correction is independent of an irrelevant null-space coefficient, while individual formal coefficients may depend on the stated off-support extension.

The distinction between an exact coefficient and an entire collapsed chain derivative is respected. In particular,

\[
b^{(3)}_{kk}=E_3[W_k^{(4)}\phi''(Z_k^{(3)})],
\]

whereas

\[
b^{(2)}_{kk}
=E_2[\phi''(Z_k^{(2)})\tau_R(Q_k^{(2)})]
+b^{(3)}_{kk}E_2[\phi'(Z_k^{(2)})^2\tau_R'(Q_k^{(2)})].
\]

The second term is necessary and is included. The readout's earlier-source dependence contributes to earlier \(b^{(3)}_{ks}\), not to a derivative of deterministic coefficient selection or of a covariance factorization.

An explicit singular-time check illustrates the distinction. At the first nonzero top backward step, on the zero-jitter population support, let \(Z=Z_0^{(3)}\). Then

\[
b^{(3)}_{10}=\Delta E_3[\phi'(Z)^2],\qquad
b^{(3)}_{11}=\Delta E_3[\phi(Z)\phi''(Z)].
\]

Although the two forward source coordinates coincide almost surely at this stage, their formal derivatives are distinct. Since \(H_1^{(2)}=H_0^{(2)}\), their contracted sum is

\[
\Delta E_3[(\phi\phi')'(Z)]H_0^{(2)}
=\Delta\frac{E_3[Z\phi(Z)\phi'(Z)]}{\mu_2}H_0^{(2)}.
\]

This agrees with the direct transpose-conditioning coefficient. Replacing the diagonal coefficient alone by the whole derivative would double-count an earlier-source contribution. The manuscript does not do that.

The rank-one learned terms and empirical-feedback oracle comparison at lines 1154–1205 are consistent with this source construction. Their coefficients are available in causal order. The small nonzero finite readout is removed by a fixed-step comparison; no estimate uniform in program length is claimed at this stage.

### 2. §4 — Common spaces, adjoints, and fixed-clipping flows

**Premises discharged:** consistent finite joint laws from §3; a countable generating collection; deterministic population operator bound; clipping with the displayed contraction and identity properties.

The construction supplies full generated \(L^2(\Omega_\ell)\) spaces, not just unrelated finite-dimensional distributions. The norm bound (A.1) makes the action well defined on equivalence classes. Density extends it; (A.2) establishes the actual adjoint. Arbitrary fixed real coefficients and the required Lipschitz operations can be recovered by approximation of the finite calculations. This suffices to place every fixed clipped Euler calculation on the same spaces.

The clipping-independent estimates (A.8)–(A.9) have the correct powers and factors:

\[
\|W^{(3)}(s)\|_{\rm op}\le10+\frac{a^2s^2}{2},
\quad
\|W^{(2)}(s)\|_{\rm op}
\le10+5a^2s^2+\frac{a^4s^4}{8}.
\]

They follow successively from \(|W^{(4)}|\le as\), \(|\delta^{(3)}|\le as\), and
\(\|\delta_R^{(2)}\|_2\le\|W^{(3)}\|_{\rm op}\|\delta^{(3)}\|_2\).
They do not use a gradient identity for the clipped field.

After R1's notation correction, the Lipschitz estimate has constant \(C_S(1+R)\), independent of width. The common pointwise readout bound defines a closed path set and is preserved by the integral update. The primal estimates permit continuation of each **fixed-clipping** flow to every finite feature time. This is not continuation of the uncut L3 flow. The fixed-clipping width limit follows by a fixed proof mesh followed by mesh removal.

### 3. §5 — Mesh-uniform response bootstrap and tails

**Premises discharged:** precisely the scalar source equations established in §3 and realized in §4. Neither an unproved response rule nor a covariance derivative is inserted into the bootstrap.

The closure is causal. Assuming earlier \(U_r,V_r\le1\):

1. The bottom source derivative first enters through \(\Delta\), yielding \(|a^{(2)}_{js}|\le A\Delta\).
2. The middle derivative row satisfies a discrete Volterra inequality with coefficient \(A\Delta(2|Q_r^{(2)}|+V_r)\). Its envelope is (B.2); a single backward source has the additional forcing \(A\Delta\), giving (B.3).
3. The bound on each marginal variance of \(\zeta_r^{(2)}\), followed by Jensen over time indices, gives (B.4). Time independence is not used. Correlation between the source and its bounded response shift is harmless.
4. Taking the envelope's first moment gives \(|a^{(3)}_{js}|\le A_3\Delta\). The top derivative row is then bounded pointwise by \(\exp((1+2a)A_3S^2)\).
5. This bounds the **current** top response row by \(V_k\le C_3S\), before bounding \(Q_k^{(2)}\). Cauchy–Schwarz with the envelope's second moment then gives \(U_k\le C_2S\).

The learned terms are accounted for: the top contribution is at most \(a^2S^3\), and the middle contribution is at most \(Q^2S^3\le Q^2S\). The choice of \(S_0\) makes the bounds at a putative first exit at most \(1/2\). Applying the same causal estimates to each earlier index justifies the maximum used in (B.9). There is no circular reliance on the current bottom response row.

The conclusion is a marginal Gaussian variable plus a deterministically bounded shift:

\[
\operatorname{Var}(\zeta_k^{(2)})\le a^2S^2,
\qquad |\beta_k^{(2)}|\le aC_3S.
\]

This proves (B.10) uniformly in time index, proof mesh, and clipping. It does not assert a Gaussian bound for the maximum over all time indices. Such a bound is not needed later.

For example, the deterministic choice

\[
K^2=16a^2S_0^2(1+C_3^2)
\]

is sufficient for (C.2): use \((\zeta+\beta)^2\le2\zeta^2+2\beta^2\) and the centered scalar Gaussian square-exponential integral. The resulting expectation is at most \(e^{1/8}(3/4)^{-1/2}<2\). Thus the exponential-moment premise of §6 follows from the displayed bootstrap constants without an extra hypothesis.

### 4. §6 — Cap removal, uniqueness, raw GD, clocks, and velocities

**Premises discharged:** common spaces and fixed-clipping limits; uniform primal bounds; the proved population exponential moment. No tail condition on an arbitrary competing uncut solution is assumed.

The decomposition (C.8) is algebraically exact. It puts the large-cutoff or uncut input difference in a 1-Lipschitz clipping difference, the changed gate beside the **reference** bounded clipped field, and the cutoff mismatch entirely at the reference state. The resulting bound

\[
\|\mathcal V_{R'}(A)-\mathcal V_R(B)\|
\le C(1+R)\rho(A,B)+C\|b_R(Q_B^{(2)})\|_2
\]

has a constant independent of \(R'\), including \(R'=\infty\). The top product estimate likewise needs a pointwise bound only on the reference readout. A competitor's bounded mean-square and operator norms suffice.

Fatou passes the Euler exponential moment to the exact clipped flow at every time with the same constant. It yields

\[
\varepsilon_R=2K e^{-R^2/(16K^2)}.
\]

The Gronwall factor grows only as \(e^{C(1+R)S}\), so (C.12) is Cauchy uniformly in \(R'\ge R\). Its rate also makes the velocity error \((1+R)\rho+\varepsilon_R\) vanish, which justifies the unbounded product and the integral-equation limit. The uncut solution is continuously differentiable in the stated Banach state norm.

This directly supplies the uniqueness needed in place of an uncut local-Lipschitz theorem. The sometimes-used Osgood formulation is unnecessary: the stronger explicit comparison \(e^{CR}\varepsilon_R\to0\) is already proved. Comparing any bounded-primal competitor against the same clipped references identifies it with the limit. The restart discrepancy at a reached time is itself exponentially small in \(R^2\); multiplication by the additional remaining-interval Gronwall factor still tends to zero. This proves restart uniqueness only inside the constructed interval.

The finite tail transfer (C.13) uses a continuous 1-Lipschitz tail function. Fixed-clipping \(\mathcal W_2\) convergence gives its norm convergence; the reference state's uniform time Lipschitz bound supplies the finite time net. No finite-width exponential moment or discontinuous-indicator limit is assumed. Consequently the asymmetric comparison also handles finite uncut flow with its small nonzero readout.

For actual GD, the local positive-clock induction is valid including the last interpolation endpoint. On the stated initialization event,

\[
|f_{n,k}|\le\frac38,
\qquad \frac54\eta\le\alpha_k=2\eta(1-f_{n,k})\le\frac{11}{4}\eta<3\eta.
\]

Since \(T_0=\bar S/4\) and \(\eta\le\bar S/24\), the last required feature-clock endpoint is at most \(7\bar S/8\). The primal bounds for positive steps apply to the matrix and readout updates regardless of the transformed first-coordinate defect.

The defect (C.15) is the same exact cubic calculation as in L2, with \(\alpha_k\) in place of the step. Its total normalized size is at most

\[
C_S(\eta\sqrt n+\eta^2n).
\]

With \(\eta=n^{-2}\), these terms are \(n^{-3/2}\) and \(n^{-3}\). The reference-flow Euler error also tends to zero at each fixed cutoff. Equation (C.18) is a pathwise Riemann-sum bound valid for **any** positive partition with the specified maximum step. Thus the state-dependent random clock causes no independence or optional-sampling gap.

The physical clock comparison uses a Lipschitz predictor along the feature path, positive clock speed, and a strict margin before \(\bar S\). The finite GD and flow are compared to the same finite clipped reference before removing the cutoff. This proves (C.21) in a common finite space; it does not infer a same-width norm comparison merely from equality of limiting laws.

The competing raw-solution argument is also valid. Coordinate absolute continuity gives the scalar chain rule for \(F\); its derivative cancels \(\phi'\). The resulting integral has an \(L^2\) right-hand side, so transformed-coordinate membership follows even when not initially stipulated for the competitor. The positive-clock estimate then transfers feature-time uniqueness back to physical time, with the stated endpoint restriction.

Finally, the three velocities (C.22) contain all product-rule terms. Their gate products are obtained by successive fixed truncations and uniform squared-tail removal. At GD endpoints these formulas agree with the actual raw slopes. Between endpoints, bounded matrix slopes and normalized hidden speeds give \(O(\eta)\) movement; a changed gate times a velocity has bounded-part error \(O(A\eta)\) and tail error controlled by the already established endpoint velocity laws. The layer-by-layer induction is therefore not circular. It proves the uniform joint velocity laws, integrated preactivation and feature squared speeds, kernel limits, and path-law claims, with the prescribed one-sided mesh-node convention.

### 5. §7 — Gradient geometry and differentiability

**Premises discharged:** the uncut integral solution and continuous rank-one velocities from §6; bounded initial actions with actual adjoints.

The initial actions need not be Hilbert–Schmidt. Their trained increments are integrals of continuous rank-one Hilbert–Schmidt velocities. The cutoff comparison controls these velocities in Hilbert–Schmidt norm as well as operator norm, so the cutoff limit has the claimed parameter geometry.

The weighted remainder (G.3) proves differentiability of the **scalar predictor**. For fixed \(B\in L^2\), it gives a remainder bounded by

\[
CR\|e\|_2^2+2\|B\mathbf1_{|B|>R}\|_2\|e\|_2,
\]

which is \(o(\|e\|_2)\) after first fixing \(R\). Expanding the scalar predictor from the top downward pairs each nonlinear remainder with a fixed backward coefficient in the correct layer. Matrix-change/activation-change products and the readout cross term are quadratic in the parameter perturbation norm. This verifies a Fréchet derivative in (G.2), not merely a formal directional derivative, without asserting Fréchet differentiability of the coordinatewise nonlinearity from all of \(L^2\) to \(L^2\).

The gradient in (G.5) is continuous by the bounded-multiplier argument and reverse operator bounds. The physical factor is \(-2r\), so the loss derivative is \(-4r^2K\). All four blocks in (G.8) agree with the finite metric, including both activation-norm factors in the hidden matrix blocks. The present state determines the evolution; response coefficients are proof quantities rather than extra prescribed state inputs.

### 6. §8 — Initial Gaussian responses, feature motion, and kernel change

**Premises discharged:** continuous local solution, bounded actual adjoints, and initial finite Gaussian conditioning. No differentiability of an unrestricted nonlinear \(L^2\) map is needed.

The multiplier lemma (F.8) and the curve chain rule justify the strong limits in (F.6)–(F.7). The gate multiplication operators need only converge strongly on fixed \(L^2\) vectors. The operators in (F.9) are uniformly bounded, so this suffices when their inputs also converge strongly. There is no unjustified operator-norm convergence of a varying gate.

The direct transpose-conditioning innovation variance in (F.10) is \(E[u^2]\). Subtracting the squared response component from it would be wrong. The displayed formulas correctly retain the response and the full innovation variance. In the second application, conditioning on the entire independent upper matrix leaves the lower conditional residual untouched; \(B_2\) is then a permitted transpose input.

In particular,

\[
c_2=\frac{c_3}{\mu_1}E_2[Z_0^{(2)}\phi'(Z_0^{(2)})\phi(Z_0^{(2)})]>0
\]

retains the return through the upper matrix. The positive independent innovations imply \(B_2\ne0\) and \(P_1\ne0\). The inequalities
\(\mathcal A_0^{(2)}\succeq\mu_1I\) and
\(\mathcal A_0^{(3)}\succeq\mu_2I\), together with \(\phi'(z)>0\), give nonzero preactivation and feature leading fields in every layer. No uniform positive lower bound for \(\phi'\) is claimed or needed.

The feature-time displacement coefficient is \(s^2/2\); since \(s(t)=2t+o(t)\), the physical displacement coefficient is \(2t^2\), and the physical speed coefficient is \(4t\). Thus each squared-speed integral has its stated \(16/3\) coefficient. The adjoint pairing gives

\[
\langle\beta_3,\mathcal A_0^{(3)}\beta_3\rangle
=\gamma_1+\gamma_2+\gamma_3,
\]

so both the top readout kernel change and the sum of hidden kernel blocks have this same \(s^2\) coefficient. The total physical-time kernel expansion is correctly

\[
K(t)=\mu_3+8(\gamma_1+\gamma_2+\gamma_3)t^2+o(t^2).
\]

The regression formula (F.20) has positive denominator initially. Equality in its residual error would force arctangent to agree everywhere with an affine function under a full-support Gaussian law and continuity. Continuity of the first and second moments preserves both positive variance and positive error on a common initial interval. This establishes nonaffinity separately from motion and kernel change.

## Classical dependencies and their hypotheses

These are the classical facts needed by the audit; no research-paper theorem or unnamed network-limit theorem is required.

1. **Finite-dimensional Gaussian projection.** Orthogonal components of a centered isotropic Gaussian vector are independent. Vectorizing a finite Gaussian matrix and conditioning on compatible linear observations therefore gives a projected Gaussian residual. Adaptive queries are covered by conditioning successively on the prior transcript, so each new query is fixed before its answer is revealed. Both conditional formulas in this chapter satisfy these hypotheses.

2. **Gaussian integration by parts, including singular covariance.** If \(g\) is a standard finite Gaussian vector and a \(C^1\) function has bounded first derivatives and integrable growth, integration by parts against its density gives \(E[g_i h(g)]=E[\partial_i h(g)]\). Writing \(\zeta=Ag\) gives \(E[\zeta h(\zeta)]=AA^T E\nabla h(\zeta)\), also when \(A\) is singular. Independent roots may be conditioned on first. Fixed-program source expressions here have bounded first derivatives and finite second moments. Continuous positive-semidefinite square roots provide the finite-dimensional Gaussian coupling used in jitter removal.

3. **Averaging and Wasserstein convergence.** For iid finite-dimensional roots with finite second moment, the law of large numbers gives empirical weak convergence and convergence of second moments. For conditionally independent Gaussian innovations added to an existing coordinate tuple, bounded-test empirical variance is \(O(n^{-1})\); the conditional square-norm variance is \(O((1+\|m\|_2^2/n)/n)\), with \(m\) the conditional mean vector. These are the induction estimates used here. On a Euclidean space, weak convergence plus second-moment convergence is equivalent to \(\mathcal W_2\) convergence. The space of probability laws with finite second moment over a complete separable metric space is complete under \(\mathcal W_2\). The Euclidean node spaces and the continuous-path spaces with supremum metric meet these conditions.

4. **Countable probability-space construction and density.** Consistent finite-dimensional Borel probability laws on a countable product of real coordinate spaces define a probability measure on that product. Conditional expectations onto the first finitely many generated coordinates approximate every generated \(L^2\) variable. Bounded continuous functions are dense in \(L^2\) of a finite-dimensional Borel probability law; compact approximation then permits the included countable Lipschitz families. These facts provide exactly the density needed for the common actions.

5. **Contraction, integration, and Gronwall.** A contraction on a complete closed path set has a unique fixed point. Continuous Banach-valued paths on a compact interval have bounded, separable range and a Bochner integral; this remains true when the ambient operator space is not separable. If \(e(t)\le e_0+\int_0^t(Le(u)+a(u))du\), then \(e(t)\le e^{Lt}(e_0+\int_0^t a(u)du)\). For positive variable steps, the corresponding discrete bound follows from \(\prod_j(1+L\alpha_j)\le e^{L\sum_j\alpha_j}\). The chapter provides the closed sets, bounds, and positive steps before using these results.

6. **Tails, multipliers, and paths.** If a family is compact in \(\mathcal W_2\), its squared tails are uniformly integrable. The coupling inequality displayed in lines 572–576 transfers that property to uniformly convergent empirical laws. A bounded continuous multiplier converging in probability acts continuously on a fixed \(L^2\) variable by truncation; this proves the curve chain rules used here. For an absolutely continuous scalar path, Cauchy–Schwarz bounds its squared polygonal-interpolation error by \(4|\pi|\int|\dot z|^2\). The population velocities are continuous \(L^2\) paths; their integral representatives have absolutely continuous scalar sample paths by Fubini. These hypotheses support both the integrated-speed and supremum-path conclusions.

## Optional notes, not additional proof obligations

- **Describe the initial actions more literally.** Lines 2763–2765 say “independent Gaussian initial actions.” In the common-space construction the actions are fixed bounded operators encoding limits from independent finite Gaussian matrices. “Initial actions induced by the independent Gaussian matrices” would avoid suggesting that the bounded operators themselves are newly sampled independent Gaussian operator-valued variables. The surrounding construction resolves the intended meaning.
- **Avoid reusing the scalar bound \(Q\).** The explicit bootstrap uses \(Q=a(1+C_3)\), whereas (C.4) locally declares \(Q=aS\), later enlarged to \(1+aS\). The latter declaration is explicit and is used consistently as a readout bound, so it causes no algebraic error. A distinct symbol for that readout bound would make the section easier to check.
- **Use one dummy variable for the clipping assumption.** At line 911, \(\tau_R(q)\) is paired with \(\tau_R'(Q)\). Replacing the latter dummy argument by \(q\) would remove an unnecessary capitalization switch. The later quantified clipping conditions are unambiguous.

No optional note above requires changing a theorem, adding a hypothesis, extending a horizon, altering the proof's limit order, or recomputing a response coefficient.
