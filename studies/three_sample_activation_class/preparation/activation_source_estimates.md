# Transfer audit for Parts F, R, and V

Source read: `/home/amir/Codes/PDE/studies/three_sample_self_contained/MANUSCRIPT.md`, Parts F, R, and V, including V.I. No other study material was read; no experiment was run; the manuscript was not modified.

## Verdict and precise transfer statement

Let

\[
\phi_e(z)=a(1+z)+e\psi(z),\qquad
g(z)=\psi'(z),\qquad
D_{e,R}(z,q)=aq+eg(z)\tau_R(q),
\]

where \(a\ge1\), \(0\le e\le1\), \(\psi\in C^2(\mathbb R)\), and

\[
\|\psi\|_\infty\le2,\qquad
\|\psi'\|_\infty\le1,\qquad
\|\psi''\|_\infty\le1. \tag{T.1}
\]

Use the manuscript's clips, initialization, raw metric, source-derivative convention, and simultaneous Euler instruction order. Then:

1. Every assertion in Part F holds after the indicated activation/gate replacement. Its displayed numerical constants stay valid.
2. Under precisely the affine finite-Euler hypothesis (R.7), every assertion and every displayed numerical constant in Part R, including the complete constant chain and the threshold \(\epsilon_*(a,B,S)\) in (R.90), holds with \(\epsilon=e\). In particular the threshold is independent of the shape of \(\psi\).
3. Part V holds with the same conclusions provided its explicitly stated R-and-G input is supplied for the new activation: global capped population paths, uniform primal bounds, bounded directions on compact horizons, and (V.7). Its unspecified constants can be chosen using the common bounds (T.1), the stated primal/moment bounds, and the other parameters already allowed in Part V. There is no further activation-shape hypothesis in the GF/GD, source, true-kernel, hidden-velocity, or path-space transfer argument.

The proposed stronger normalization \(\psi\in C_b^3\), \(\|\psi^{(j)}\|_\infty\le1\) for \(j=0,1,2,3\), satisfies (T.1). Nonconstancy, oddness, monotonicity of \(\psi\), and the sign of \(g=\psi'\) are not needed in F/R/V. Nonconstancy and initial feature nonaffinity belong to the separate geometry argument. In particular this lemma alone does not establish Part G's hypotheses for arbitrary \(\psi\).

## 1. Complete local bound ledger

All activation-dependent analytic estimates used in these parts follow from

\[
|\phi_e(z)|\le a|z|+a+2,
\quad |\phi_e(z)-a(1+z)|\le2e,
\quad |\phi_e'(z)|\le a+e,
\quad |\phi_e'(z)-a|\le e,
\quad |\phi_e''(z)|\le e. \tag{T.2}
\]

At a finite cap,

\[
|D_{e,R}(z,q)|\le(a+e)|q|,
\quad |D_{e,R}(z,q)-aq|\le e|q|,
\]
\[
\partial_qD_{e,R}=a+eg(z)\tau_R'(q),
\qquad \partial_zD_{e,R}=eg'(z)\tau_R(q),
\]
\[
|\partial_qD_{e,R}|\le a+e,
\quad |\partial_qD_{e,R}-a|\le e,
\quad |\partial_zD_{e,R}|\le e\min(|q|,2R). \tag{T.3}
\]

These prove the global Lipschitz property needed for fixed finite programs. In particular (F.17)'s bound \(4eR\) and Section R.1's sharper \(2eR\) remain valid. Every inequality follows from absolute values; there is no use of \(g\ge0\).

For the diagonal matrices in (R.44), exactly the original inequalities hold:

\[
|G_k|,|V_k|\le a+1,
\quad |G_k-aI|,|V_k-aI|\le e,
\quad |L_k|\le eQ_k. \tag{T.4}
\]

The last inequality uses \(|\psi''|\le1\), not merely \(|\psi''|\le2\). This is the only normalization subtlety in the stated broader class; see Section 7 below.

For every \(R'\ge R\), including \(R'=\infty\), the exact reference-tail estimate is

\[
|D_{e,R'}(z,q)-D_{e,R}(\bar z,\bar q)|
\le(a+e)|q-\bar q|+2eR|z-\bar z|
+2e|\bar q|1_{|\bar q|>R}. \tag{T.5}
\]

To verify it, first change \(q\) to \(\bar q\) in \(D_{e,R'}\), costing \((a+e)|q-\bar q|\), and then write the remaining difference as

\[
e[g(z)-g(\bar z)]\tau_R(\bar q)
+eg(z)[\tau_{R'}(\bar q)-\tau_R(\bar q)].
\]

The first term is bounded by \(2eR|z-\bar z|\); the second is zero on \(|\bar q|\le R\) and otherwise bounded by \(2e|\bar q|\). Thus (V.10) holds with numerical constant \(c=2\), and (V.3) holds with a common \(c=2\). This proof allows either sign of \(g\).

## 2. Part F: exact source construction and functional analysis

**F.1–F.4.** Gaussian conditioning, source covariances, singular-query regularization, and source-response integration by parts are statements about fixed programs with \(C^1\) coordinate maps having bounded first derivatives. Equations (T.2)–(T.3) verify these hypotheses for every new activation and capped gate. At a fixed cap and transcript, all their scalar expressions have at most linear growth in finitely many roots/sources, and every formal first source derivative has a deterministic finite bound obtained by finitely composing the coordinate derivative bounds. This verifies the integration-by-parts integrability and the dominated-convergence premise in F.4; neither premise asks for a sign or special formula for \(g\).

The covariance entries remain the full moments \(E[uv]\). Nonodd \(\psi\) can change feature means, but none of the covariance formulas replaces \(E[uv]\) by centered input covariance. New matrix sources remain centered Gaussian with precisely these uncentered input Grams. Consequently nonzero feature means introduce no missing term.

For a parameterized fixed transcript, continuity of the new coordinate first derivatives follows from \(\psi\in C^2\). On a compact set of the finitely many earlier coefficient values, these derivatives have a common deterministic bound by (T.2)–(T.3). The existing covariance-square-root coupling therefore still passes expected first derivatives and input second moments at singular covariances. No extra derivative of a covariance, source law, or residual normalization is introduced.

**Sections F.6–F.8.** The scalar feedback comparison only uses Lipschitz maps, operator bounds, and Cauchy–Schwarz for contractions. Learned-action unrolling is an exact rank-one identity independent of activation shape. The common generated spaces, their dense node spans, the bound 10 for the initialized actions, and actual adjoints use finite-program convergence and the finite Gaussian matrix norm bound; the new activation satisfies their program hypotheses. HS rank-one norms and the raw metric are activation-independent.

**Sections F.9–F.11.** Strong bounded-multiplier continuity applies to \(b=\phi_e'\), which is continuous and bounded by \(a+e\). The strong curve chain rule needs only \(C^1\) and this bounded derivative. For the scalar Fréchet derivative use exactly the weighted Taylor proof (F.41), now with

\[
L_1\le a+e,\qquad L_2\le e.
\]

For fixed \(v,z\in L^2\), the remainder is bounded by both \(\tfrac12e|q|^2\) and \(2(a+e)|q|\); splitting at \(|v|=M\) gives the identical \(o(\|q\|_2)\) estimate. This verifies the scalar gradient, all four full Gram kernel blocks, and the true-flow loss identity. No lower bound on \(\phi_e'\) is used in these conclusions. Local capped existence/Euler approximation follows from (T.3) and the exact same raw rank-one estimates. Final uncapped product observations use bounded \(\phi_e'\), bounded \(\phi_e''\), and second-moment tails, so their closure also transfers.

## 3. Part R: numerical constant audit through R.90

This section specifies why the old constants suffice, rather than invoking an unspecified robustness principle.

| Manuscript step | Activation information used | Consequence under (T.1) |
|---|---|---|
| R.2, (R.11)–(R.17) | The F program hypotheses and exact matrix/rank unrolling | All coefficients, source covariances, causal zeros and four-stage order are unchanged in form. |
| R.3, (R.18)–(R.29) | Only the affine case \(e=0\) | The raw affine comparison, Gaussian probe, \(Q,E_0,T_0,A_0,M_0\) are numerically identical. |
| R.4, (R.30) | \(|\phi_e(z)|\le a|z|+a+2\), \(|D|\le(a+1)|q|\) | Every forward/backward primal norm bound is identical. |
| R.4, (R.31) | \(|\phi_e-\phi_0|\le2e\) | Forward perturbation bounds \(2e,3abe,4a^2b^2e\) remain valid. |
| R.4, (R.32) | \(|D-aq|\le e|q|\) and bounded actions | Backward bounds \(be,b^2e,3ab^2e,3ab^3e,7a^2b^3e\) remain valid. |
| R.4, (R.33)–(R.35) | Prior two rows, rank-one inequality, affine Lipschitz constant | The same raw-field discrepancy \(30a^3b^3e\le Qe\), stopped bound \(T_0e\), source variance \(\sigma^2=Q^2\), query discrepancy \(D_0e\), and moment error \(m_0e\) hold. |
| R.5, (R.36)–(R.43) | Primal/source bounds, (T.2)–(T.3), Minkowski | The constants \(K_1,K_2,K_C,K_{q1},K_{q2},K_q,L_q\) and exponential incoming-field estimate are identical. |
| R.6, (R.44)–(R.58) | Exactly (T.4) and first source chain rules | Same derivative recursions and \(H,\mathcal E_k,X\), including the terminal \((1+eQ_k)\) factor. |
| R.7, (R.59)–(R.68) | Exactly (T.4), derivative bounds, prior learned-moment error | Same \(D_1,R_0\) and expected derivative remainders. |
| R.8, (R.69)–(R.89) | Affine deterministic systems at fixed arrays and the preceding remainders | All \(K_F,K_V,K_U,K_T,D_2,D_3,C_V,C_T,E_3,C_U,E_2,K_*\) stay unchanged. |
| R.9, (R.90)–(R.96) | Previous constants, chronological induction, finite products | Exact same positive threshold and final response/moment estimates. |

Here are the nontrivial chain-rule and closure details behind the table. At frozen deterministic arrays,

\[
\partial H_k=G_k\partial Z_k,
\qquad \partial\delta_k=L_k\partial Z_k+V_k\partial q_k.
\]

Substituting the unrolled expressions for \(Z,q,C\) gives (R.46)–(R.49) term by term for the new activation. The substitution differentiates \(g\) once, producing \(g'=\psi''\); it never differentiates \(G,V,L\) a second time. The proof of (R.51)–(R.54) only takes norms of those exact equations and inserts (T.4). Thus it produces the identical nonnegative scalar recurrences and the identical envelope

\[
\mathcal E_k=\exp\{Hs_k+He\sum_{r<k}h_rQ_r\}.
\]

The sub-Gaussian moment/convexity estimates (R.43), (R.55)–(R.58) use no intertime independence and no property of \(g\). They remain valid for this envelope, including the indispensable current factor \(Q_k\).

For same-array derivative perturbation, replacing \(G,V,L\) by \(aI,aI,0\) and subtracting gives exactly the four terms in (R.59), the top equations (R.62), and the terminal terms (R.65)–(R.66). Each nonaffine term contains one of \(G-aI,V-aI,L\), bounded in (T.4). Consequently the old forcing bound \(4H^4efW_k\), iteration bound (R.61), \(D_1=20H^8e^{HS}\), and final coefficient

\[
R_0=200H^{11}e^{HS}[1+(S+1)X]+m_0(1+S)
\]

are unchanged. Signs of the factors or expected current-return coefficients never enter a lower bound; all these estimates use norms.

The deterministic comparison of the actual arrays with the affine baseline therefore receives precisely the same remainder inequalities (R.77), not merely remainders of an unspecified size. Its current dependence is still triangular: \(A^2_k\), then \(A^3_k\), then \(B^3_k\), then \(B^2_k\). At each stage the previously available derivative/moment estimates apply before estimating that new row. Thus the identical closure factor \(K_*e^{K_*S}\) applies, and the original formula

\[
e\le\epsilon_*(a,B,S)
=\min\left\{1,\frac{B}{2T_0},\frac1{2K_*e^{K_*S}}\right\}
\]

still gives a half-unit margin inside the coefficient bounds. The threshold's full dependency chain is exactly (R.18), (R.28), (R.34), (R.36)–(R.37), (R.42), (R.50), (R.57), (R.68), (R.74), and (R.80)–(R.88). No member depends on \(\psi\) after (T.1) is imposed.

For clarity, the signed current returns remain

\[
(B^3_{kk})_{ij}=1_{i=j}E[L^3_{k,ii}],
\]
\[
(B^2_{kk})_{ij}=1_{i=j}E[L^2_{k,ii}]
+(B^3_{kk})_{ij}E[V^2_{k,ii}G^2_{k,jj}].
\]

They can be positive or negative. Their diagonality comes from the separately named current-source derivatives and explicit schedule, and does not require sample independence, parity, or \(g\ge0\). At time zero all incoming fields are zero because \(C_0=0\) and \(\tau_R(0)=0\); this starts the same induction even when \(\psi(0)\ne0\).

## 4. Part V: cap removal and actual GF/GD

The activation-specific content of raw forward stability (V.8) is \(|\phi_e'|\le a+e\) and the linear-growth estimate in (T.2). Rank-one update comparison uses only its norm inequality. Substituting (T.5) through the backward gates gives (V.11) with the same structure

\[
K(1+eR)\|\theta-\bar\theta\|_{\mathcal X}
+Ke\sum_{Q\text{ in reference}}\|Q1_{|Q|>R}\|_2.
\]

There is only one factor \(R\), because each new such factor multiplies a forward discrepancy already controlled by (V.8); propagation of an earlier incoming discrepancy only multiplies it by bounded actions and \(a+e\). This reasoning is unchanged for signed \(g\).

Assuming (V.7), its elementary moment-to-Gaussian-tail derivation still gives \(Ke^{-cR^2}\). Gronwall then gives the existing \(K_Te^{K_TR-cR^2}\) cap-comparison bound. Therefore population cap removal, strong uncut construction, and uniqueness against a bounded-primal strong competitor transfer. Only reference tails are required, so no extra shape or incoming-tail assumption is imposed on a competitor.

At fixed cap, the new coordinate maps satisfy the same finite-program and bounded-derivative hypotheses. The nonlinear Gaussian probe in V.3 therefore has the same bounded first-derivative integration-by-parts justification. Its parameter-continuity step follows from the fixed-transcript argument in Section 2, and its raw perturbation estimate follows from (T.3). This gives the same strictly-past \(Kh_j\) and current \(K\) coefficient-row structure (V.21). Pointwise absolute first-derivative rows in V.4 follow by first chain rules, using \(|\partial_zD_R|\le2eR\), and yield the same scalar discrete Gronwall recursion. Primary moments follow using (T.2)–(T.3).

Raw Euler defects, same-width stopped comparisons, and the vanishing actual finite readout root do not differentiate \(\psi\) further. The actual finite GF remains a finite-dimensional gradient flow of the same loss and metric, and its energy identity supplies global finite-time nonescape. For raw GD the comparison still uses \(F_\infty\) at the preceding mesh node and a capped reference; no width-uniform uncut Lipschitz constant is needed. Thus V.7 and V.9 preserve the precise limit order and the conclusion for every deterministic step tending to zero, including the manuscript's \(n^{-2}\).

## 5. Hidden velocity source derivatives: no missing third derivative

The only new nonlinear product in V.5 is

\[
U=\phi_e'(Z)P.
\]

At a finite truncation its exact first source derivative is

\[
\partial_\eta[\phi_e'(Z)\tau_M(P)]
=e\psi''(Z)\tau_M(P)\partial_\eta Z
+\phi_e'(Z)\tau_M'(P)\partial_\eta P. \tag{T.6}
\]

The derivative uses \(\psi''\); there is no \(\psi'''\). With the primary derivative rows bounded by V.4, the bottom velocity row is dominated independently of \(M\) by \(K(1+|P^1|)\). Primary moments make that domination integrable. Thus dominated convergence passes the first appended action's expected source derivatives as its product clip is removed.

For the second action, the first appended action is represented as a new named forward source plus a deterministic-coefficient combination of primary deltas. In a derivative with respect to a primary transpose source, the new forward source and all coefficient values are frozen. Its derivative is therefore zero even if its covariance with earlier forward sources is nonzero or singular. The derivative of the remaining finite combination is bounded using the already established primary rows. Hence \(\partial_{\zeta^2}P^2\) is bounded and (T.6) gives domination \(K(1+|P^2|)\) for the second product. The first appended action's proved moments make this integrable. This is the exact reason no derivative of its response coefficient, and thus no hidden second source derivative, occurs.

The product's strong continuity also transfers quantitatively. For a fixed reference \(P\), split at \(|P|\le L\) to obtain

\[
\|[\phi_e'(Z_n)-\phi_e'(Z)]P\|_2
\le eL\|Z_n-Z\|_2
+2(a+e)\|P1_{|P|>L}\|_2.
\]

Together with \((a+e)\|P_n-P\|_2\), this proves (V.37). It passes empirical product clips using joint \(\mathcal W_2\) convergence and positive-part tails, then actual bounded action continuity. Keeping the first-action clip while truncating the second product gives the same nested order as V.5. No unproved derivative-limit interchange is needed.

For trajectory velocity comparison, the reference-factor truncation in (V.41) becomes

\[
\|[\phi_e'(z)-\phi_e'(\bar z)]\bar P\|_2
\le eM\|z-\bar z\|_2+2(a+e)\mathcal T_M(\bar P).
\]

Thus (V.40), fixed-cap velocity convergence, and ordered cap-then-velocity-tail removal all transfer with the same single-tail-level factor. Strong continuity on compact time intervals supplies compact \(L^2\) reference images and uniformly vanishing tails. None of this needs \(g''=\psi'''\), a quantitative modulus of continuity of \(\psi''\), or an \(L^p\)-operator bound for the Gaussian actions.

## 6. True backward kernels, V.I, and path laws

True backward observations use finite nested products \(\phi_e'(z)q\) and bounded transpose actions. The product continuity and empirical-tail bound just proved identify their joint \(\mathcal W_2\) laws, first at a fixed transcript and then along the capped/uncut comparisons. All four kernel blocks are full Gram matrices of raw gradients. Their entries, including off-diagonals, pass by Cauchy–Schwarz on coupled second moments; no derivative positivity is required for a Gram matrix to be positive semidefinite.

When an expected derivative formula is actually needed at initialization, V.I also transfers. Its first coefficient integrand becomes

\[
\tau_M'(H_0)p_j\phi_e'(Z_j^3)\phi_e'(Z_i^3)
+1_{i=j}\tau_M(H_0)e\psi''(Z_i^3),
\]

bounded uniformly in \(M\) by \(K(1+|H_0|)\). The initialized Gaussian inputs and (T.2) give every finite moment of \(H_0\). The second coefficient integrand has exactly the original form with \(\phi_e''=e\psi''\); at fixed outer clip its first limit has bounded domination, and its subsequent outer-clip removal is dominated by \(K(1+|q_i^2|)\). The first transpose source representation has already shown this integrability. The full source Gram square-root coupling and the ordered empirical clipping proof therefore remain valid. Again this uses only \(\psi''\), not \(\psi'''\).

The final path law proof uses strong curve chain rules, integrated squared speeds, the deterministic interpolation bound (V.57), and fixed-grid joint \(\mathcal W_2\) convergence. These have just been verified for the new activation. Integrated hidden and raw squared-speed conclusions are moment consequences of the same convergence and exact gradient identities. No additional shape property enters V.11.

## 7. Relation to the originally proposed bounds

For the broader initial class

\[
\|\psi\|_\infty\le2,\quad \|\psi'\|_\infty\le1,
\quad \|\psi''\|_\infty\le2,
\quad \|\psi'''\|_\infty\le6,
\]

F and V still apply directly; for example their finite-cap gate derivative is bounded by \(4eR\), and their unspecified constants absorb the curvature bound 2. The literal inequality \(|L_k|\le eQ_k\) in R.45 cannot be inferred from those assumptions: only \(|L_k|\le2eQ_k\) is guaranteed. Therefore one must either modify R's envelope/constant chain or renormalize before quoting its numeric threshold.

A rigorous way to preserve the complete existing constant chain is

\[
\rho=\psi/2,\qquad \eta=2e,
\]

so \(\phi_e=a(1+z)+\eta\rho\), \(D_{e,R}=aq+\eta\rho'\tau_R\), and \(\rho\) satisfies (T.1). The result above then applies whenever

\[
e\le\tfrac12\epsilon_*(a,B,S).
\]

The response/coefficient bounds (R.8), moment bound (R.9), and absolute derivative bounds (R.96) retain their old constants. The perturbation conclusion (R.95), expressed in the original amplitude, becomes at most \(4K_*e^{K_*S}e\). This is a sufficient threshold; no claim of optimality is intended.

With the parent's chosen normalization \(\|\psi^{(j)}\|_\infty\le1\) for \(j=0,1,2,3\), this renormalization is unnecessary: the original threshold and (R.95) coefficient \(2K_*e^{K_*S}\) hold literally.

## 8. Boundary of what was proved

There is no shape-dependent constant hidden inside Parts F/R/V once the stated norm bounds and their explicit input hypotheses are fixed. The special arctangent regression margin, its saturation limit, lower bounds for initialized Grams, and the selection of a global residual-clock horizon are separate obligations in Part G. The present transfer cannot replace them with derivative bounds alone. For instance a constant perturbation meets all boundedness hypotheses but has zero nonaffine regression residual. This does not obstruct F/R/V: it only demonstrates why the geometry input must be supplied separately.

No sign condition on \(g\) was used anywhere in this audit. Under the small amplitude ultimately selected one can separately obtain \(\phi_e'\ge a-e\), but positivity of this derivative is not a premise of any transfer step established here.
