# Internal check of the frozen-history weak nonlinear remainder

2026-10-01. Scoped independent internal mathematical audit, not promotion review.

Scientific inputs: the complete `WEIGHTED_REMAINDER_ROUTE.md`, the corrected complete `RESOLUTION_UPPER_ROUTE.md`, and the previously assigned complete `BIAS_CAVITY_ROUTE.md`, `FITTING_AND_THRESHOLD.md`, and `CONCENTRATION_ROUTE.md`. The repository instructions were reread and the solve-math-rigorously skill was applied. No sibling lower/interpolation report, other study, manuscript, experiment, or Git history was read. This report is the only file written for this audit.

**Verdict: PASS for theorem (5) with its stated frozen scalar histories, cavity event, near-cap hypothesis (4), and envelope \(|\eta_a|\le2s^c\).** The ordinary remainder energy, weighted scalar inequality, conditional moment estimates, exact graph propagation, and terminal-time supremum all have the required width factors. No independent nonlinear propagator or Gaussian nonlinear increment is assumed.

One scope qualification is required: the statement that this envelope automatically includes the actual full-system row history is not justified with the literal constant 2 and the cavity activity. The full-system bound is \(|d_{ai}|\le2s^{\rm full}\). The same proof extends to any fixed envelope \(C_\eta s^c\), and activity comparability supplies such an envelope on a full/cavity fitting event. This qualification does not affect (5) as precisely stated. Restoring the empirical scalar histories remains outside its conclusion.

## 1. The deterministic graph really has bounded ordinary operators

With \((r,\rho,\tau,K,V)\) frozen, every non-activation operation in (1)–(2) is affine or linear in the dynamic state and the external forcing \(\omega\eta\). The maps are built from \(W,W^T\), finitely many fixed sample vectors, and the fixed scalar arrays \(K,V\). Their ordinary Euclidean/Frobenius operator norms are bounded independently of n. Stacking or duplicating the fixed number of sample blocks costs only a constant depending on m and d.

The post-gate map \(F(x,p)=C_M(p\psi(x))\) has global Lipschitz constants \((2M,1)\), even for unbounded p. Thus the complete state vector field has Lipschitz coefficient \(C\rho(t)\) in ordinary norm, globally in U. The forcing \(\omega\eta_a\) enters additively in p and contributes no state derivative containing \(\omega\). These facts verify the claim in Section 3 and permit shifted states \(U^c+T\) outside the fitting tube.

The same facts give global Caratheodory solutions for every finite row vector and measurable bounded history. Gaussian rows need no norm cutoff in theorem (5). The Gaussian tails of large rows are handled by moment estimates, not by an unmentioned localization event.

At zero row, all occurrences of eta vanish and the frozen coefficients are the actual cavity coefficients, so the base trajectory is exactly \(U^c\). The first tangent holds eta fixed as a prescribed function of time. It does not differentiate the selection rule \(\eta(\omega)\).

## 2. The local Taylor inequalities are valid without a carrier bound

For \(D=|u|+|v|\), the global Lipschitz bound gives \(|q_F|\le C_M D\). This proves the smooth part of (7) when D exceeds a fixed positive cutoff, because \(D\le C\min(D^2,D)\) on that range.

For smaller D, the logarithmic derivative bound on \(\psi\) implies

\[
 e^{-2|u|}\psi(x)\le\psi(x+u)\le e^{2|u|}\psi(x).
\]

If \(|p\psi(x)|>2M\), choosing the cutoff sufficiently small makes both endpoint carriers saturate on the same side, with zero base derivative; the defect is zero. Otherwise \(|p\psi(x)|\le2M\), and relative first/second derivative bounds give

\[
 (p+v)\psi(x+u)-p\psi(x)
 =p\psi'(x)u+\psi(x)v+e,
 \qquad |e|\le C_M D^2.
\]

All constants depend on M but not on p. The carrier increment is at most \(C_M D\); applying the scalar hard-clip remainder inequality to that increment gives (7). This checks the potentially dangerous dependence on the uncut transpose carrier.

The energy-to-weight inequality (21) is also valid for all nonnegative a,t,e, without a smallness assumption. For \(h(x)=\min(x^2,x)\),

\[
 h(t+e)\le2h(t)+2h(e),\qquad
 a h(t)\le at^2,\qquad a h(e)\le e^2+a^3.
\]

The last bound follows by splitting into \(a\le1\), \(a>1,e\ge a\), and \(a>1,e<a\). For the corner term, the larger of t and e determines which of \(d_X\le2Ct\) and \(d_X\le2Ce\) must hold. On the latter event,

\[
 ae\mathbf1_{\{d_X\le2Ce\}}
 \le e^2+a^2\mathbf1_{\{d_X\le2Ca\}}.
\]

This proves the displayed bound. Crucially, the nonlinear input error contributes \(e^2\) without a random weight. Consequently its squared ordinary norm, rather than its ordinary norm, is the needed quantity.

The near-cap bound implies zero probability of a base carrier equaling a corner at each fixed time on \(\mathcal C\). Fubini on bounded intervals and a countable union give a time-null corner set for almost every good cavity, simultaneously for the finitely many base coordinates at each width. The upper base gate has strict separation from its caps. The base variational equation therefore uses actual derivatives almost everywhere; defining a bounded selector arbitrarily on the remaining null time set has no effect on its solution.

## 3. Adaptive tangents have coordinate envelopes, not Gaussian laws

The tangent equation has cavity-measurable matrices \(L,B_b\), with

\[
 \|L(t)\|_{\rm op}\le C\rho(t),\qquad
 \|B_b(t)\|_{\rm op}\le C,\qquad
 \|P(t,s)\|_{\rm op}\le e^{CS_*}.
\]

Its Duhamel representation is valid for each realized history held fixed. For a state coordinate j, take absolute values inside that representation before using \(|\eta_b(s)|\le2s^c(s)\). Every resulting integrand is an absolute Gaussian projection with a cavity-measurable coefficient vector of bounded norm. Conditional Minkowski gives an envelope of conditional \(L^p\) norm \(C\sqrt p/\sqrt n\), uniformly over all eta.

The same statement for an algebraic tangent input needs a direct use of the representation, rather than an inference solely from individual state-coordinate bounds. Explicitly, a scalar algebraic tangent input has the form

\[
 q(t)^T T(t)+\sum_b c_b(t)\eta_b(t)\omega_j,
 \qquad \|q(t)\|_2+\sum_b|c_b(t)|\le C,
\]

or the corresponding bounded fixed-coordinate linear map of omega. Insert the Duhamel formula into the first term: each coefficient
\(q(t)^TP(t,s)B_b(s)\) has bounded row norm, so the same conditional Gaussian estimate applies. This supplies the claim in Section 3 without a hidden sum over n state coordinates. Only a fixed-time bound is needed for internal algebraic nodes.

For state-coordinate terminal-time suprema, the fundamental theorem for P gives

\[
 \sup_{t\ge s}|e_j^TP(t,s)B_b(s)\omega|
 \le |e_j^TB_b(s)\omega|
 +\int_s^\infty|e_j^TL(t)P(t,s)B_b(s)\omega|\,dt.
\]

The conditional \(L^p\) norm is again \(C\sqrt p/\sqrt n\), since \(\int\rho\le S_*\). No source-time selector or eta is differentiated. These bounds give the claimed conditional sub-Gaussian envelope tails, including for adaptive eta. The tangent itself need not be Gaussian under such adaptivity.

## 4. One-point density gives the stated ordinary energy

Let V be a tangent-input envelope at a fixed coordinate and time. Conditional on the cavity, its fourth moment is O(n^{-2}) and its tail is bounded by \(C\exp(-cnv^2)\). With cavity-measurable distance d,

\[
 \mathbb E_\omega[V^2\mathbf1_{\{d\le CV\}}\mid\mathcal A]
 \le (\mathbb E_\omega V^4)^{1/2}
       \mathbb P_\omega(V\ge d/C)^{1/2}
 \le Cn^{-1}e^{-cnd^2}.
\]

The localized one-point hypothesis (4) gives

\[
 \mathbb E[\mathbf1_{\mathcal C}e^{-cnd^2}]
 =\int_0^\infty2cnu e^{-cnu^2}
          \mathbb P(\mathcal C\cap\{d\le u\})\,du
 \le Cn^{-1/2}.
\]

This uses neither conditional density given the cavity nor independence between coordinates. It uses Gaussian integration conditional on the cavity first, and the unconditional localized small-ball bound second. The event is cavity-measurable, so these operations are consistent.

The squared defect per lower coordinate is therefore O(n^{-3/2}). Upper-gate distances are at least M/2, so their corner contributions are exponentially small and their smooth contributions O(n^{-2}); tanh also contributes O(n^{-2}). There are O(n) coordinates and only finitely many activation types. Thus

\[
 \mathbb E_{\mathcal C}\|q^{\rm tan}(t)\|_2^2\le Cn^{-1/2}
\]

in ordinary, unnormalized norm.

The shifted-state graph comparison is sound: at a linear node propagate its input errors by a bounded linear map; at an activation node add and subtract the value at the pure tangent input, propagating previous errors by its global Lipschitz bound and adding its own pure-tangent defect. The vector graph has fixed depth and a fixed number of vector operations, so this introduces no width factor.

Subtract the tangent equation, compare the true state with the shifted state, and use the complete vector field's global Lipschitz bound. Gronwall yields

\[
 \sup_t\|R(t)\|_2
 \le C\int_0^\infty\rho(t)\sum_v\|q_v^{\rm tan}(t)\|_2\,dt.
\]

Replacing rho by its deterministic integrable envelope on \(\mathcal C\), then applying Minkowski, proves (19). The argument does not take a supremum of cap events over time.

For an actual algebraic input minus its base and tangent inputs, compare its evaluation first with the shifted-state graph and then with the linearized graph. Its error E is bounded by \(C\|R\|_2\) plus a fixed sum of preceding pure-tangent defects. This proves (20) in ordinary norm at each fixed time, again with no delocalization assumption on E.

## 5. Weighted local defects have exactly the root-width scaling

Take a coordinate weight a with the conditional \(C\sqrt p/\sqrt n\) moment bound, and a tangent-input envelope t with the same bound. Arbitrary dependence between them is allowed. Conditional Hölder gives

\[
 \mathbb E_\omega(at^2+a^3\mid\mathcal A)\le Cn^{-3/2}.
\]

Conditional Cauchy–Schwarz and the respective tail of t or a give

\[
 \mathbb E_\omega[
 at\mathbf1_{\{d\le Ct\}}+
 a^2\mathbf1_{\{d\le Ca\}}\mid\mathcal A]
 \le Cn^{-1}e^{-cnd^2}.
\]

After integration over the good cavity this is O(n^{-3/2}) per lower coordinate. Summing O(n) such terms gives O(n^{-1/2}). The remaining term from (21) is \(\sum_j e_j^2\); each activation has at most two scalar inputs, so that sum is bounded by a fixed multiple of the squared norm of its algebraic input errors, already O(n^{-1/2}) in expectation by (20). This establishes (25).

The use of the energy is essential and justified. A direct bound by \(\|\omega\|_2\|R\|_2\) would give only n^{-1/4}; that bound is not used at the decisive step. Nor is any Gaussian claim made about R or the actual input increments.

## 6. Exact adjoint propagation and all-time output

The alternative graph expansion in (26) is exact. At each activation, its actual increment equals its base derivative applied to its actual input increment plus its own local defect. Expanding this identity through the affine graph expresses the total vector field increment as the full base Jacobian applied to the state/input increment plus a sum of local defects multiplied by products of base derivatives and fixed linear maps.

Subtracting the tangent equation leaves

\[
 \dot R=LR+\rho\sum_vM_vq_v.
\]

Every \(M_v\) is cavity-measurable and has bounded ordinary operator norm. The factors \(r_a/\rho\) are bounded; the zero-rate convention is harmless. This representation does not linearize an unknown nonlinear propagator or assert that such a propagator is independent of omega. All row dependence beyond the linear part remains in the explicit defects q.

For a fixed source time and local-defect coordinate, its left weight is a Gaussian projection with coefficient built from \(M_v(s)\), \(P(t,s)\), and the output derivative \(DH_a(U^c(t))\). The terminal-time derivative of P has integrable operator norm. Also,

\[
 \|\partial_t DH_a(U^c(t))\|_{\rm op}\le C\rho(t),
\]

because each row of the clipped A velocity is O(rho), uniformly in width. Consequently the absolute terminal-time supremum of that weight has conditional \(L^p\) norm \(C\sqrt p/\sqrt n\). Source-time selectors are held fixed, so no unjustified variation estimate for them is needed.

Take the terminal-time supremum outside the Duhamel expression by its absolute integral. At each source time, use the weighted local estimate (25) with these supremum weights. Integrating against the deterministic rho envelope gives (31).

For the direct output tanh defect, the cap-free scalar inequality gives at each time a sum of an ordinary squared error and Gaussian/tangent cubic terms. Take the supremum of the **sum** of squared errors before bounding it by \(C\sup_t\|R_A(t)\|_F^2\); no sum of coordinatewise error suprema is needed. The tangent terms may use the coordinatewise supremum envelopes because their moments have already been checked. Their expected sum is n times O(n^{-3/2}), hence O(n^{-1/2}). This closes (5) with the required temporal supremum.

The adaptive linear estimate (32) follows from the same terminal-time variation argument and the stated Gaussian quadratic-form variance identity. Its adaptive trace target can remain random. This estimate is consistent with the earlier checked linear lemma.

## 7. Exact scope and the full-path envelope qualification

The proved object is the forced lower-feature flow with \(\theta=(r,\rho,\tau,K,V)=\theta^c\). It retains the original initialized matrix and its transpose, the exact post-gate hard clip, and arbitrary bounded row-dependent eta. It is not yet the full finite system's lower-feature trajectory: recovering that trajectory also requires replacing \(\theta^c\) by the realized full histories \(\theta^n(\omega)\).

There are two distinct issues in saying the theorem “includes the actual causal path.”

1. A causal row equation driven with the frozen cavity residual satisfies \(|\eta|\le2s^c\), and is included directly.
2. The actual full-system backward row satisfies \(|\eta|\le2s^{\rm full}\). Comparability of full and cavity activities gives \(|\eta|\le C_\eta s^c\) on a suitable joint fitting event, not necessarily the literal envelope \(2s^c\). All estimates above extend to a fixed \(C_\eta\) with changed constants. To use full-row histories on a norm-ball event while preserving Gaussian integration, extend or truncate eta outside that event to respect the chosen envelope; do not condition the Gaussian row on the event. This is a straightforward scope extension of the proof, but it must be stated rather than attributed to the literal envelope automatically.

Even after this envelope adjustment, evaluating the frozen-history functional at the full row path does not restore the empirical scalar histories. Mixed row/history nonlinear errors and comparison of the finite covariance/response law with the own population law are not bounded by (5). The report correctly leaves these tasks open.

The common-cavity near-cap input applies at M=1 by the checked upper-route result with its sufficiently large operator cutoff. The theorem at other fixed caps remains conditional on establishing its displayed hypothesis (4) at that cap; the report states that restriction.

## 8. The RMS counterexample is valid but has its stated limited role

In (33), every summand is nonnegative. On \(0<U\le1/(2\sqrt n)\) and \(-2\le G_j\le-1\), its value is at least \(1/(2n)\) for sufficiently large n. With probability at least one half, at least \(np_0/2\) independent coordinates meet the latter condition. Independence from U then gives a probability of order n^{-1/2} that \(Z_n\ge p_0/4\), establishing \(\mathbb E Z_n^2\ge c n^{-1/2}\).

The upper first-moment estimate follows from
\(Z_n\le\sum_j\omega_j^2\mathbf1_{\{U\le|\omega_j|\}}\) and the bound \(\mathbb P(U\le v)\le4v\). It gives \(\mathbb E Z_n\le Cn^{-1/2}\). Thus one-point density permits the claimed L1 rate while failing to force a root-width L2 rate. This is a valid logical counterexample, not a reachable-state or prediction lower bound.

No blocking proof gap was found in the precisely stated frozen-history L1 theorem. Its remaining limits are the envelope qualification above and the explicitly unproved restoration/population comparison steps.

## Final amendment: inspected scope corrections

2026-10-01. I checked the author's narrow revisions to the path envelope and the algebraic tangent moment argument. The theorem now allows any fixed \(C_\eta<\infty\) with \(|\eta_a(t)|\le C_\eta s^c(t)\), and permits its constant to depend on \(C_\eta\). It explicitly derives the full-row envelope on a simultaneous fitting event, extends the path outside that event by clipping, and preserves unconditional Gaussian integration before restricting the nonnegative estimate. The scalar histories remain frozen at cavity values throughout. This resolves the envelope qualification in the original verdict and Section 7 above.

The revised bounded-map argument inserts \(Q(t)\) directly into the tangent Duhamel kernels \(e_j^TQ(t)P(t,s)B_b(s)\) before applying conditional Gaussian projection estimates. This correctly establishes the coordinate moment bound without summing coordinate envelopes through an operator norm.

**Final verdict: PASS for the corrected frozen-history theorem (5), uniformly over the stated fixed-multiple adaptive path class.** Quantitative restoration of the scalar histories and population-law comparison remain outside the theorem. This amendment checks only the requested revisions; it does not reopen the completed proof audit. The current repository mathematical-communication instructions and their canonical-notation skill, including its neural-network reference, were read for this amendment.
