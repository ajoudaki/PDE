# Operator-task evidence audit

Read-only research-state consolidation, 8 September 2026. This document records the final claims and their actual scope in **both** Operator MFP tasks. It is not a new proof search, a rerun of the historical experiments, or a new independent certification of every mathematical argument. Original studies and session files were preserved.

## 1. Coverage and evidence

The complete local primary session rollouts were recovered, including the terminal reviews absent from the ten-turn exports:

| Task | Primary chronology | Coverage |
|---|---|---|
| Operator MFP L=2, general t (`01a03544-ddce-77a1-b5af-44df07c54f4b`) | `/home/codex-b/.codex/sessions/2026/08/24/rollout-2026-08-24T21-35-00-01a03544-ddce-77a1-b5af-44df07c54f4b.jsonl` | 36,944 records; 458 user/assistant messages; 52 final answers; terminal PDE review round included |
| Operator MFP L=2, general t (2) (`01a044b8-39b5-7240-8406-c08a614deaa8`) | `/home/codex-b/.codex/sessions/2026/08/27/rollout-2026-08-27T21-35-19-01a044b8-39b5-7240-8406-c08a614deaa8.jsonl` | 34,738 records; 428 user/assistant messages; 50 final answers; 4 September correction included |

The second task contains the first task's shared history through the initial arbitrary-distinct-data claim, then follows a different audit branch. It is not an independent confirmation of every inherited result. Some inherited records have the fork time as their timestamp; chronology below therefore uses original rollout line numbers. `O1:35611`, for example, means record 35,611 of the first primary rollout, not a line in a derived text file.

Plaintext exports preserve the complete user/assistant message chronology and all late agent reviews:

- [O1 chronology](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR1_CHRONOLOGY.txt), [O2 chronology](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR2_CHRONOLOGY.txt).
- [O1 final answers](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR1_FINALS.txt), [O2 final answers](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR2_FINALS.txt).
- [O1 review messages](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR1_REVIEWS.txt), [O2 review messages](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR2_REVIEWS.txt).
- [Source manifest, complete SHA-256 values and preservation copies](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR_SOURCE_MANIFEST.json).

The full final deep-linear theorem, its audit record, the final PDE boundary proof, the full global L2 arctangent proof, both final narrowed L3 reports, and the substantive quadratic/ReLU final proofs and scope audits were read. The long canonical quadratic covariant-Schur proof was read through all 3,342 lines. Earlier finite-step studies were followed through their final corrections; their subsidiary combinatorial programs were not rerun. External research theorems were assessed through the historical source-audit records and the recovered proof appendices; this pass did not repeat the historical external-paper audit.

No required terminal operator manuscript was missing. Three originally temporary manuscripts were found in `/tmp` and copied verbatim into this directory, with matching hashes. The terminal PDE task was interrupted **after** three final isolated auditors had returned CLEAN on the frozen artifact; the lack of a final assistant answer does not erase those completed reviews.

## 2. Results that must be added to a consolidation

| Result | Exact status and horizon | Important boundary |
|---|---|---|
| L=3-hidden deep-linear finite-contraction ODE no-go | Proved, frozen-hash CLEAN | Uniformly bounded number/degree of scalar contraction coordinates, state-universal closure; not arbitrary encodings |
| Its bounded-contraction local PDE extension | Proved, three final frozen-hash CLEAN reviews | Fixed finite field count, finite differential/readout order, uniformly bounded contraction degree; not every finite-field PDE |
| Same deep-linear model: autonomous operator population/GF/exact-GD limit | Global on every fixed compact interval | One fixed infinite-dimensional noncommutative source plus one evolving trace-class kernel and residual; arbitrary normalized GD mesh tending to zero |
| L2 one-sample arctangent: population/GF/exact-GD joint limit | Global on every fixed compact interval | Tiny initial readout; canonical current action state; hidden path laws and velocity energies included |
| Old quadratic model: width-first loss Euler initial layer | No continuous initialized compact-time scalar limit | Order-one rescaled readout, L2, one sample; terminal positive-time convergence is a different question |
| Old quadratic finite GF and sufficiently resolved GD diagonals | Same initialized-continuity obstruction | Does not establish failure for every under-resolved full-network diagonal |
| Quadratic frozen-bottom auxiliary model | Initial layer for **every** deterministic mesh tending to zero | Bottom layer is frozen; this quantifier does not transfer to the fully trained network |
| Hard ReLU classical GF | Fixed-derivative-at-zero ODE can fail to continue | Finite-width attracting-gate event; not a generalized Euler no-go |
| Hard ReLU actual Euler scalar paths | Tight in C[0,T0] for **every** deterministic mesh tending to zero | Continuous initialized subsequential predictor/loss limits; uniqueness, determinism and full state remain unproved |
| L3 sin+cos general-distinct-data claims in these tasks | Full joint theorem withdrawn; finite-step DAG and initial geometry survive | Latest report proves neither the full theorem nor its negation; newer all-depth theorem must be audited separately |

Here and below `L` counts **hidden** layers, so the deep-linear no-go has four trainable factors. A statement on all `[0,T]`, for each fixed finite T, is global existence plus compact-time convergence, not a uniform-in-infinite-time approximation theorem.

## 3. The missing deep-linear ODE no-go

Primary artifact: [JOINT_DEEP_LINEAR_THEOREM.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_joint_audit/JOINT_DEEP_LINEAR_THEOREM.md), especially Theorem 1 and Sections 2–3. Frozen SHA-256:

`ca3407d83f19faa857307c976d680b4c5b97f90901fd5faf48920d2f9e20d799`.

[AUDIT_RECORD.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_joint_audit/AUDIT_RECORD.md) records three isolated final CLEAN reviews of that exact artifact: algebra/closure scope; Gaussian source/Fock/global flow; and compact-time/exact-GD identification. Earlier incomplete annihilator wording and missing explicit real form were corrected before freezing. The final answer is O1:36450.

### Model and quantifiers

There is one scalar input and one real label y, identity activation at three hidden layers, and

\[
f_n=a^\top RBx,\qquad a,x\in\mathbb R^n,\quad B,R\in\mathbb R^{n\times n}.
\]

All entries of the four initial factors are independent N(0,1/n). The loss is `(y-f_n)^2`. Physical mobility η is a fixed strictly positive constant. With `e=y-f`, the physical vector field is `2ηe` times the feature derivation D defined by

\[
Da=RBx,\quad DR=a(Bx)^\top,\quad DB=(R^\top a)x^\top,
\quad Dx=B^\top R^\top a.
\]

Equivalently, four raw standard-Gaussian factors are divided by √n, giving raw output `n^{-2} a_raw^T R_raw B_raw x_raw`, with common raw mobility `nη`.

**No-go:** there are no fixed integers k,D, independent of width, and no fixed polynomial vector field V, for which a k-coordinate state `g_n` contains f and satisfies `Dg_n=V(g_n)` for all parameter states and all sufficiently large n, when every coordinate is uniformly a finite linear combination of typed same-time complete-contraction graphs of tensor degree at most D. The same obstruction holds for analytic-germ V when equality is required on a full state neighborhood of zero. This is an exact state-universal closure theorem, not a claim restricted to a chosen Gaussian trajectory.

The algebraic obstruction is an unbounded family of **connected** graph types. With `A=RB` and `C=A^T A`, the odd derivative `D^{2m-1}f` contains the path

\[
4^{m-1}x^\top(B^\top R^\top RB)^m x,
\]

of degree `4m+2`, with positive coefficient. Products of a finite list of contraction coordinates can only make disjoint unions of the finitely many connected types already present. Stable graph independence for sufficiently large widths prevents the new path from being represented that way. The analytic argument compares homogeneous tensor degree. The later PDE manuscript gives the careful auxiliary quotient-closure proof of stable graph independence, including the potential high-valence identification issue.

This does **not** mean that deep linear nets have no global flow, that a numerical norm cannot contract, that no closure exists at a specified finite n, or that every conceivable finite scalar encoding is impossible. It excludes the named natural contraction-coordinate class. An orbit-fitted output ODE, an arbitrary/nonlocal encoding, or a fixed number of infinite-dimensional fields lies outside the theorem.

## 4. Stronger terminal result: the precise PDE closure boundary

Primary: [PDE_CLOSURE_BOUNDARY.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_pde_no_go/PDE_CLOSURE_BOUNDARY.md). Frozen and current SHA-256:

`cc8b6fa5c8084ed69d56c794214edb5c14d8208801e47aab2fb4a5d5715bcd2e`.

The same network and feature derivation are used. Fix a spatial domain Ω in R^d, field count q, spatial differential order r, readout jet order ρ, and contraction degree D, all independent of n. Each field is encoded by a finite sum

\[
U_{\alpha,n}(\zeta;\theta)
=\sum_{\deg G\le D}c_{\alpha,G,n}(\zeta)P_G^{(n)}(\theta).
\]

The coefficients are smooth spatial functions and **may depend on n**. The proposed evolution is a fixed local differential-polynomial PDE, with smooth spatial coefficients and all mixed partial derivatives through order r allowed. The output must be a finite-jet polynomial readout at finitely many spatial points, using derivatives through order ρ. The identity must hold on a nonempty open set of full parameter states for all sufficiently large n.

**Theorem:** such an exact closure is impossible. The conclusion also holds for analytic differential-expression/readout germs on a full neighborhood of the prescribed zero-field jet basepoints. It further holds for the physical loss derivation `2η(y-f)D` for **every real y**, including zero, with η>0.

Spatial differentiation changes coefficient functions, not the finite connected graph alphabet. Repeated time differentiation of the readout produces finite spatial-jet expressions and therefore cannot generate the unbounded connected path ladder. For y≠0, the lowest homogeneous part of the kth physical derivative is `(2ηy)^k D^k f`. For y=0, the positive contraction expansion contains the same new connected path alongside powers of f. Thus the zero-label case is covered algebraically even though the selected limiting Gaussian orbit with y=0 is stationary.

The quantitative necessity statement says that, under width-uniform locally finite graph support at every fixed spatial-jet cutoff, representing the derivative of order `2m-1` forces a jet of order at most `ρ+(2m-1)r` to contain the path of degree `4m+2`. Consequently a universal fixed contraction-degree cap cannot work.

The manuscript **also disproves the unrestricted wording** “no fixed finite-field PDE.” The translation PDE `U_t=U_s` can encode the feature-time local germ `U(θ)(s)=f(Φ^sθ)`. For physical loss flow, the corresponding entire forward output profile on the fixed half-line yields a global translation-semigroup realization. These are exact autonomous, restartable output encodings, but preload the future trajectory; they are not a constructive compression under a nonoracle representation requirement. They establish why the bounded-contraction hypothesis is necessary.

Review provenance is unusually important here. Earlier reviews demanded η>0, full analytic neighborhoods, and correct stable-independence handling. After repairs, round-two reviewers returned CLEAN at O1:36884, 36891 and 36896. On the final frozen hash, `/root/pde_final_dynamics` returned “CLEAN — SHA256 verified exactly” at O1:36926, `/root/pde_final_logic` returned CLEAN at 36933, and `/root/pde_final_algebra` returned CLEAN at 36940. The user interruption is O1:36944, after all three results. These messages are preserved in OPERATOR1_REVIEWS.txt.

## 5. The positive deep-linear theorem: global autonomous population/GF/GD

The same frozen [joint theorem](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_joint_audit/JOINT_DEEP_LINEAR_THEOREM.md) proves a positive infinite-dimensional closure alongside the scalar no-go.

On one fixed real separable Fock Hilbert space, build a bounded, explicit source C0 from six creation/annihilation colors. The evolving state is a trace-class kernel Q plus scalar residual e:

\[
\dot Q=2\eta e(C_0^*+Q^*)^3,
\quad K=\operatorname{Tr}\big[(C_0+Q)^3(C_0^*+Q^*)^3\big],
\quad\dot e=-2\eta eK,
\]

\[
Q(0)=0,\quad e(0)=y,\quad
f=\tfrac14\operatorname{Tr}(C_0+Q)^4=y-e,
\quad\mathcal L=e^2.
\]

The flow is globally defined, unique, autonomous and restartable on its named trace-class state class. In particular `||Q(T)||_1 ≤ 2|y|√(ηT)`, which prevents finite-time escape. The source is immutable but is part of the representation, not a record of the evolving trajectory's history. One field on an infinite domain has infinitely many scalar degrees of freedom and is compatible with the contraction ODE/PDE no-go.

For every fixed finite T, the exact finite-width GF and exact simultaneous parameter-GD interpolations converge in probability uniformly on `[0,T]` to f, K and loss, and to every fixed finite family of the stated current rooted-word/finite-rank observables. **Every deterministic normalized physical mesh δ_n→0 is allowed.** If one separately insists that the raw parameter multiplier itself tend to zero, impose `δ_n=o(1/n)`; this optional extra condition is not needed for normalized-coordinate joint convergence. Do not promote the listed observable theorem into a generic W2 path-law/velocity-energy theorem for all nonlinear probes.

An equivalent free-Wishart description uses two vector fields z,p, one scalar h, one current kernel S, and fixed noncommuting positive source operators X,Y. Its feature-time equations are

\[
z'=(I+X+hI+S)p,\quad p'=(I+Y+hI+S)z,
\quad h'=2\langle z,p\rangle,\quad
S'=|z\rangle\langle p|+|p\rangle\langle z|.
\]

Physical time adds the factor `2ηe`. This is a genuine fixed-domain IDE representation. It gives f→y and loss→0 when y≠0; the selected y=0 population path is stationary. Noncommutative mixed words remain necessary: e.g. `τ(X²Y²)=4` while `τ(XYXY)=3`. Spectral marginal data alone do not determine the relevant kernels; the manuscript supplies finite-state witnesses as well.

The Gaussian source input ultimately has a self-contained proof using finite Wick words, conditional Gaussian-root concentration and operator-norm nets. The manuscript audits recent external random-matrix results but does not depend on them in its final proof. The continuous-time bridge uses fixed finite word/Picard approximants followed by a dimension-free factorial tail and a dimension-free Euler estimate; it does not apply a fixed-program theorem to a growing program.

## 6. One-sample L2 arctangent global theorem, with final audit provenance

Primary preservation copy: [OPERATOR_L2_FULL_AUDITED_PROOF.md](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR_L2_FULL_AUDITED_PROOF.md), copied verbatim from `/tmp/L2_FULL_AUDITED_PROOF.md`. SHA-256:

`e9f963cde5061f4f5b4d8d3913a62ccd013af451334e46356134f624759d42fb`.

This is the final authoritative proof in O1, not the initially rejected short proposal. It is a two-hidden-layer, bias-free, one-sample `(x,y)=(1,1)` network with φ=atan and loss `(f-1)^2`. The first weights A_i are iid N(0,1); connector B_ji iid N(0,1/n); raw readout c_j iid N(0,n^-4); all blocks independent. Put C=nc, so `Var(C_j(0))=n^-2`. Raw mobilities are `(n,1,1/n)`, with displayed physical step `η_n=n^-2` and time `kη_n`.

On fixed canonical right/left L2 action spaces, use

\[
X=A+A^3/3,\quad A=J(X),\quad H=\arctan A,
\quad S=BH,\quad D=C/(1+S^2),\quad e=f-1.
\]

The closed equations are

\[
\dot X=-2e B^*D,\qquad
\dot B=-2eD\otimes H,\qquad
\dot C=-2e\arctan S.
\]

The current cyclic probe representation records actual operator actions and actual adjoints on a saturated typed grammar. The construction uses bounded/Lipschitz coordinate maps and controlled truncations, not arbitrary multiplication on an L2 algebra. It has a unique global solution in the stated bounded-operator and bounded-C class on every finite interval and is autonomous/restartable from the current cyclic state.

For each fixed finite T, the theorem jointly identifies population flow, actual finite-width GF and exact parameter GD. Its observable scope includes uniform output, loss and all three NTK blocks; the named bounded/Lipschitz or truncated gated action records; empirical hidden-preactivation path laws for A and S in W2(C[0,T]); and both hidden velocity integrated-square energies. Actual parameter interpolations are used, with hidden fields recomputed from them. The same-width GD proof gives the displayed error `C_T(η+η√n+η²n)`, so the estimate supports meshes with `η√n→0`; the stated theorem fixes the concrete `n^-2` choice.

Strict nonaffinity, positive hidden variances, activity of all three parameter blocks, kernel movement and loss descent are established on one common sufficiently small positive interval. These activity conclusions should not be silently strengthened to uniform strict bounds for all t≥0. The existence/convergence theorem itself is global on every fixed compact time interval.

The complete final proof repairs the earlier incomplete probability-space realization, current-action topology, nested probe induction, source tail control and W2 path argument. Final source review at O1:35595 and final continuum/exact-GD review at O1:35588 returned CLEAN; O1:35611 records the frozen hash and final release. Earlier O1:34813, 34834, 34841, 35349 and 35519 are **rejected intermediate rounds**, not contradictory terminal conclusions.

The only nonclassical external input is the exact fixed-finite-program specialization of Tensor Programs III, Theorem 2.10. The primary-source reviewer read its full relevant proof, including singular covariance and reused-transpose clauses, and the final appendix records six printed-proof corrections. The actual argument uses deterministic-coefficient finite programs at fixed mesh, then separately handles empirical feedback, width-dependent tiny readout, and mesh removal. It does not claim that the source theorem itself supplies the time-uniform bridge.

This modern tiny-readout model differs from the older order-one-readout quadratic/ReLU model below. An old failure cannot be transferred merely because both networks have L2 and one sample.

## 7. Quadratic activation: several different negative statements

### 7.1 Original model

The original model is

\[
f_n=\frac1n\sum_i a_i\phi\!\left(\frac1{\sqrt n}\sum_jW_{ij}\phi(u_j)\right),
\]

with all a_i,u_j,W_ij iid standard Gaussian, `q=1`, two hidden layers and one sample y=1. The rescaled readout a is **order one** at initialization. For half-square loss, `g=n∇f`, GF is `θdot=(1-f)g`, Euler is `θ^+=θ+h(1-f)g`, and physical time is kh. Quadratic means φ(x)=x²/√3 unless an explicitly stated unnormalized coordinate change is used.

### 7.2 Feature-ascent finite-step uniform-remainder no-go

Primary: [UNIFORM_NO_GO_THEOREM.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_quadratic_l2_order5/UNIFORM_NO_GO_THEOREM.md), with [fixed-h polynomial width bridge](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_quadratic_l2_order5/FIXED_H_QUADRATIC_WIDTH_LEMMA.md) and [final audit](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_quadratic_l2_order5/FINAL_NO_GO_RELEASE_AUDIT.md).

For φ(x)=px+qx², `p²+3q²=1`, q≠0, let F_N(h) be the expected-output width limit of pure feature ascent at fixed finite N,h. Then for **every** ρ>0,

`F_{2t}(ρ/t)-F_t(2ρ/t)→+∞` as t→∞.

No fixed polynomial-in-t factor multiplying h^5 can uniformly bound the cubic-subtracted exact nonzero-step remainder on `0<h≤ρ/t`. The proof uses positive-polynomial step-doubling and a frozen-bottom lower branch, followed by Gaussian factorial growth of a surviving order that itself grows exponentially in t. Signs are removed by exact orthogonal conjugacies. The literal fifth jet remains O(t^4); no contradiction exists because the obstruction is in much higher orders.

For polynomial degree d≥2, the corresponding **full-network** theorem covers sign-coherent polynomials, including appropriate sign/reflection conjugates and the separately handled shifted powers. An arbitrary-sign polynomial theorem is proved only for the frozen scalar block. The actual full signed network remains open: bottom-update deletion is not coefficientwise monotone and maximal sectors can cancel after Gaussian contraction. See [final polynomial scope](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_polynomial_uniform_no_go/FINAL_POLYNOMIAL_SCOPE.md) and [hostile signed-bridge audit](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_polynomial_uniform_no_go/FULL_SIGNED_BRIDGE_AUDIT.md). These auxiliary ascent results are not themselves loss-GF conclusions.

### 7.3 Width-first loss Euler has an initialized layer

Primary: [FULL_RESOLUTION_AND_JOINT_SCALING.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_loss_mesh_resolution/FULL_RESOLUTION_AND_JOINT_SCALING.md), [FINAL_X2_RELU_MESH_VERDICT.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_loss_mesh_resolution/FINAL_X2_RELU_MESH_VERDICT.md), [independent audit](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_loss_mesh_resolution/INDEPENDENT_AUDIT.md).

For every fixed output threshold δ in (0,1), the width-first loss-Euler path reaches δ at physical times tending to zero as h→0. Until that hit, every adaptive feature step is at least `(1-δ)h`; deterministic-schedule positive-polynomial monotonicity and the all-order divergence force the hit. Thus predictor and loss cannot converge compact-uniformly to a continuous path with initialized trace f(0)=0, loss(0)=1/2. The initialized continuity failure persists even though loss feedback restrains later output.

This does **not** resolve a positive-terminal-time paired loss discrepancy after the layer, nor establish that every possible joint width–mesh diagonal fails. The proof orders width first at every fixed mesh.

### 7.4 Exact finite GF and sufficiently resolved joint GD

The underlying exact finite-width loss GF is global at every finite n. Its **width limit** nevertheless has an initialized concentration obstruction. The final source is [CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md), replacing the earlier invalid full-state susceptibility versions.

In its unnormalized φ=x² coordinates, set G=W/√n, X=u², Z=GX, B=A⊙Z, R=G^TB and f=<A,Z²>_n. The feature equations are `A'=Z²`, `X'=8X⊙R`, `G'=2B X^T/n`. The theorem forces a fixed nonzero output change by feature time `(0.09+o(1))/√log n`, with high probability. Positive label y_* and physical mobility bounded below retain a comparable loss-time clock until the small fixed output stop. Normalized quadratic activation transfers by its constant coordinate/time rescaling.

The proof uses covariant ordered Schur elimination, endpoint cancellations and a source-space collective perturbation argument, not a bound on the full Hessian. It separates the extreme-column pole from the row pole using an archived integer-arithmetic certificate, then uses leave-two-out conditional Gaussian/coarea bounds, unique-leader spacing and a release argument to convert the extreme into fixed output action. This pass read that final proof but did not rerun its numerical certificate. Its header certifies a **proof-body** hash `be9d0d95...`; the whole-file hash, including that header, is `a1eb606a...` in the manifest. These hashes should not be falsely treated as a mismatch.

The joint scaling note [JOINT_SCALING_VERDICT.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_joint_width_mesh_quadratic/JOINT_SCALING_VERDICT.md) gives explicit sufficiently resolved GD diagonals that shadow GF through the initial layer; for example a sufficient class is

`h_n n^14 exp(6·10^11 n^9/√log n)→0`,

and `h_n=exp(-10^12 n^9)` satisfies it. Such diagonals also fail continuous initialized compact-time convergence. The proposed much weaker release-scale condition `h=o((log n)^{1/4}/√n)` is diagnostic, not proved sufficient in the full system.

Dividing the optimizer by the tangent kernel creates a different algorithm with scalar equation `fdot=1-f`; this is not a rescue theorem for the original optimizer or the full state. Similarly, sufficiently vanishing common mobility gives a trivial frozen limit, not the originally requested nontrivial feature-learning flow.

### 7.5 Auxiliary all-diagonal theorem does not transfer

The final [ARBITRARY_DIAGONAL_FROZEN_THEOREM_AND_FULL_GAP.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_joint_width_mesh_quadratic/ARBITRARY_DIAGONAL_FROZEN_THEOREM_AND_FULL_GAP.md) proves the initial layer for **every deterministic h_n→0** when the bottom features are frozen. Conditional on their Gram Q_n→1, a favorable positive Gaussian top-row block satisfies a scalar Riccati lower recursion. All negative rows have a uniform integrable lower contribution; no width-versus-mesh rate is needed.

The same theorem for the fully trained quadratic network is not proved. Explicit width-one examples disprove both tempting pathwise shortcuts: fine-versus-coarse feature monotonicity and monotonicity under freezing the bottom layer. Exact discrete reused-adjoint updates have nonperturbative second-/third-order source terms on under-resolved extremes. The note carefully leaves arbitrary full-network diagonals open. Its primary proof is available, but unlike the frozen-hash deep-linear/L2 releases, this consolidation did not find a separate final hash-specific reviewer certificate for this auxiliary note; retain that evidence-level distinction.

## 8. ReLU: classical failure and actual Euler compactness coexist

Use the original order-one-readout model of Section 7.1, φ(x)=√2 x_+, half-square loss and any fixed bounded gate convention `|φ'(0)|≤√2`.

The [final mesh verdict](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_loss_mesh_resolution/FINAL_X2_RELU_MESH_VERDICT.md), [joint-width audit](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_loss_time_doubling/RELU_JOINT_WIDTH_MESH_AUDIT.md), and [continuous-limit test](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_loss_time_doubling/RELU_NO_CONTINUOUS_LIMIT_TEST.md) must be read together.

**Negative:** a width-two construction reaches an attracting gate with side normal velocities p>0>q. The displayed witness has f=1/4, residual 3/4 and velocities `p=3/8`, `q=-21/8`. Small adjustments cover a proposed fixed gate derivative. There is no absolutely continuous continuation of the resulting classical fixed-convention ODE through that gate. An open upstream flow tube has positive Gaussian probability. The proof does not supply a width-uniform lower probability of macroscopic gate hitting.

**Positive:** for **every** deterministic h_n↓0, linearly interpolated actual Euler predictors F_n and corresponding losses are tight in C([0,T0]), where

`T0=1/(384·6^4)`.

Every subsequential limit is continuous and has F(0)=0 and loss(0)=1/2. The finite-width proof uses `R=max(1,||a||_n,||u||_n,||W/√n||op)`, the pathwise update `R^+≤R+6hR^5`, the high-probability initialization bound R0≤6, and a common bound R≤12 on the explicit interval. ReLU Lipschitzness then bounds each predictor increment by `60·12^7 h`. No smooth gate approximation, classical ODE continuation or loss dissipation is assumed.

This is scalar compactness and existence of continuous subsequential limits, not a deterministic unique generalized OMFP state, a full hidden-state/velocity limit, or a global-in-time theorem. It directly blocks the stronger claim that every joint ReLU mesh lacks even a continuous initialized scalar limit.

At one frozen attracting gate, hard Euler selects occupation `λ=p/(p-q)`, with counting error less than one sample per finite window. The binary gate Young measure has every positive moment equal to λ. Replacing it by a deterministic derivative λ changes its square to λ²; full kernel/cotangent readouts can distinguish these. Smooth softplus selection can therefore differ from hard Euler. Marginal occupations also do not determine products of multiple gates: relative phases matter. The notes exhibit that logical distinction but do not prove an actual-network pair of mesh subsequences with distinct macroscopic losses. Initialization gate-count regimes n h_n→0/finite/infinite are not themselves convergence criteria.

The independent mesh-resolution audit certifies the quadratic initial-layer and ReLU gate calculations. The later scalar compactness proof is a self-contained primary result; no separate frozen-hash final review certificate was located in this pass. The exact hard-ReLU/leaky-ReLU uniform feature-ascent remainder classification remains open; a smooth counterexample below is not a theorem about the hard kink.

## 9. Multisample claims, obstructions and their later retractions

### 9.1 Duplicate contradiction is an activity obstruction

O1:22838, 22923 and 23376 (O2 lines one larger in the shared segment) use duplicate inputs with opposite binary labels. Every deterministic network predicts the same value on the two samples; their summed squared loss is already minimized at the common initial prediction zero. Thus no universal theorem can demand strict loss decrease/nontrivial learning for **every arbitrary input-label configuration**, under any allowed activation/scaling. This does not prove that an autonomous limit fails to exist; a stationary limit is compatible with it.

Once inputs are required to be pairwise distinct, this exact obstruction disappears. Arbitrarily close opposite-label pairs still rule out dataset-uniform positive conditioning/activity constants. Constants and usable time windows may depend on the fixed dataset. Positive-definite initialization Gram matrices and strictly positive small-time formal coefficients were obtained, but those facts alone do not supply the joint limit.

### 9.2 L2 sin+cos claims must retain their review history

The shared final answer O1:31382/O2:31383 claims a universal fixed-dataset L2 construction with `φ=sin+cos`. O2:31923 explicitly withdraws that compact-time theorem after three audit rounds: fixed-program convergence had been promoted to a growing-horizon state theorem without a proved uniform bridge. O2:32603 makes a renewed affirmative claim using an all-source bootstrap, local `T=1/(1536p)` and an extremely small displayed GD mesh. The next request concerns L3, and the terminal L3 manuscript does not supply a separately frozen, complete L2 proof of that renewed claim. Consequently this operator audit does not treat the renewed short answer alone as an independently certified final theorem. The broader later all-depth theorem being consolidated elsewhere should supply the current result, after its own exact hypotheses are checked.

### 9.3 L3 sin+cos: complete corrected scope

Two full narrowed reports were recovered:

- [O1 L3 report](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR1_L3_AUDITED_REPORT.md), original `/tmp/L3_AUDITED_REPORT.md`, final O1:34294 after failed blind proof audits.
- [O2 final L3 report](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OPERATOR2_L3_AUDITED_REPORT.md), original `/tmp/l3_joint_limit_audited_report.md`, final O2:34735 on 4 September after two audit rounds and two final PASS reviews of the corrected scope.

Model: three hidden layers, fixed finite p samples with pairwise-distinct RMS-normalized inputs `||x_a||²/d=1`, binary labels, φ=sin+cos, first-layer iid N(0,1/d), independent middle iid N(0,1/n), raw readout iid N(0,n^-4), raw mobilities `(n/d,1,1,1/n)`, and proposed vanishing mesh with nη_n→0. The terminal report proves exact finite-width normalized dynamics, all four NTK blocks, every fixed finite-step Gaussian DAG including reused-transpose responses, and strict positive-definiteness of the initial activation Grams and first nonzero hidden NTK coefficients. It gives explicit Gaussian formulas and conditional/formal small-time feature activity.

The formal O(t³) notation in its small-time formulas is **coefficient notation only**. It does not assert an analytic remainder or the existence of the proposed continuous trajectory. The report expressly leaves the full uncut joint population/GF/exact-GD action theorem unproved; it does not disprove that theorem.

The 4 September report adds a concrete counterexample to the proposed all-source estimate. For m=d=1 and x=y=1, one small population Euler step h gives a reused-transpose source P_2 with `P_2/h` tending in law to a nondegenerate Gaussian, variance `2(1+exp(-8))`. Thus an estimate of the form `||P(t)||_q≤KT exp(KTq)` with K independent of q cannot hold for all q and arbitrarily small T: first let T=h→0 at fixed q, then q→∞. This refutes that estimate, not the population-flow conjecture.

Other audited gaps include cancellation of purported factorial gains, omitted higher Malliavin/source branches, a cutoff that was not actually the identity on its core, and the distinction between singular redundant coefficient masses and an actual observable law. An adaptive bounded test can align with a reused Gaussian column and create a √n coordinate, so unproved uniform square-tail transfer is substantive.

The corrected report derives a sound finite-width cutoff Lipschitz estimate in **independent coordinates**, then states the missing uniform uncut transpose tail theorem and the remaining completion/restartability obligations explicitly. Even a completed fixed-cutoff law would still need cutoff removal and uniform integrability for uncut kernels and velocity energies. Neither fixed-program Tensor Programs IV nor the checked fixed-discrete-time feature-richness theorem supplies that growing-horizon argument.

Any later all-depth C1,1 result may supersede the **open status of the underlying existence problem** for covered activations/datasets. It does not retroactively validate the false all-source estimate or the withdrawn proof. No such later result was independently recertified by this operator-only pass.

## 10. Earlier finite-step material: retain only the final distinctions

These stages are relevant because several later false conclusions arose by promoting their results beyond their quantifiers.

1. **Exact finite-step Gaussian chronology.** The one-hidden-layer scalar neuron recursion, and later reused-operator DAGs at fixed depth and fixed finite step count, are positive results. At L2, early cubic-remainder claims were withdrawn at O1:1798 and 2997, then repaired in fixed-h/fixed-t form, with the final fixed-t release at O1:7264 reporting five independent hostile passes. O1:8660 gives the general fixed finite `(L,t)` extension under the weighted C12 derivative envelope. Its constants may depend strongly on t. This does not establish a continuous-time joint limit.

2. **Uniform t^4 remainder.** O1:9817 retains the theorem for L1 under RMS normalization, at-most-linear activation growth and uniformly bounded derivatives through order 12. It is a feature-ascent expected-output bound on `|h|≤cφ/t`, with activation-only constants. [UNIFORM_L1.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/UNIFORM_L1.md) and [its PASS audit](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/AUDIT_UNIFORM_L1.md) contain the exact scalar recursion and Gaussian-integrable tangent estimates. The identity-activation extension at every fixed depth is retained in O1:10922. These are not global nonlinear state theorems.

3. **The fifth jet is always polynomial in t.** O1:12741 and [FIFTH_JET_POLYNOMIAL_THEOREM.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_near_identity_omfp/FIFTH_JET_POLYNOMIAL_THEOREM.md) show the fifth coefficient of the equal-time Euler discrepancy has degree at most four in t when the fixed-order jet exists. Leading fifth-degree Euler chronology cancels. This cannot control the full nonzero-h remainder uniformly in t.

4. **A different norm no-go.** [FINAL_RESOLUTION.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_uniform_near_identity_l2/FINAL_RESOLUTION.md) and [its audit](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_uniform_near_identity_l2/FINAL_RESOLUTION_AUDIT.md), released O1:13588, reject the prescribed single all-source Banach algebra containing an unbounded Gaussian-like atom. A norm with positive zeroth-order weight and bounded multiplication on the whole same space would bound all powers geometrically; Gaussian Lq growth contradicts this. The normalized near-identity analytic class does not avoid the obstruction. Radius-losing scales and typed reachable product modules are not excluded. This is **not** the deep-linear finite-contraction ODE/PDE no-go and does not refute the scalar remainder conjecture.

5. **Bounded-slope smooth counterexamples.** [SUPER_T5_EFFECTIVE_REMAINDER.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_linear_growth_uniform_counterexample/SUPER_T5_EFFECTIVE_REMAINDER.md) constructs a single RMS-normalized C∞ activation with positive bounded slope and at-most-linear growth for which the best cubic-subtracted exact remainder exceeds `(3/5)N^{N+6}-2` at every integer N≥2 on `0<h≤ρ/N`. Every fixed-schedule width-first output exists. The [independent audit](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_linear_growth_uniform_counterexample/SUPER_T5_EFFECTIVE_REMAINDER_INDEPENDENT_AUDIT.md) accepts it relative to the already established **marked source-aware generated-core intertwining**, while correcting the false claim that the flattened E6 zero-margin ledger was empty. The true grouped quadratic principal contribution cancels in that sector. Do not erase this declared dependency.

6. **Smooth ReLU-like variant.** [SMOOTH_RELU_LADDER.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_linear_growth_uniform_counterexample/SMOOTH_RELU_LADDER.md) and [its audit](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_linear_growth_uniform_counterexample/SMOOTH_RELU_LADDER_AUDIT.md) put the same remote, increasingly narrow bumps in an exact affine tail of a fixed smooth ReLU/leaky-ReLU base. The counterexample can be arbitrarily close in weighted C1, with remainder ≥N^N. Higher derivatives have no fixed global envelope. This neither classifies hard ReLU nor ordinary softplus nor a uniform C1,1 activation class.

7. **Scalar mesh criteria are weaker than a restartable state limit.** The final [dyadic audit](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/AUDIT_DYADIC_CONVERGENCE.md) proves convergence of scalar equal-time output functions under summability `Σ_j B_{2^j}/2^{5j}<∞`, using the exact substitution h=T/(2m). Uniformly summable discrepancies are sufficient on the corresponding bounded time interval; O(t^4) is one sufficient growth rate, not necessary. It does not prove partition independence, operator-state convergence, autonomy, uniqueness or unbounded kernel readouts. [CONTINUOUS_TIME_MINIMAL_BRIDGE.md](/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_depth_time_doubling/CONTINUOUS_TIME_MINIMAL_BRIDGE.md) makes the extra requirements explicit: state-level forced-trajectory stability, summable local defects, generator consistency, restart-stable uniqueness and separate finite-width mesh removal/uniform integrability.

8. **Changing from feature ascent to loss descent changes the discrepancy.** O1:19694 correctly identifies a generic order-h² fine/coarse loss discrepancy for half-square loss. It is ordinary first-order Euler behavior and neither proves nor disproves a continuous-time limit. The all-order quadratic initial-layer proof, rather than a finite loss jet, is what resolves the negative model.

9. **Initialization and optimizer changes matter.** O1:21025 explains that a coherent neuron-embedded/nested kernel initialization is a different ensemble from the iid Gaussian connector. O1:21206 distinguishes an already proved arctangent finite-GF width limit and an auxiliary Euler scheme from the original raw width-first Euler claim. The later tiny-readout theorem supplies its own exact-GD bridge. These statements should not be collapsed into an activation-only yes/no table.

## 11. Supersession map and final use

The current operator evidence supports the following precise replacements:

- Replace a vague “bounded ODE contractions are impossible” sentence by the state-universal finite-contraction ODE theorem and its stronger finite-order bounded-contraction PDE extension. Keep their positive global operator IDE alongside them.
- Replace “the interrupted last operator turn did not finish” by “its final PDE manuscript and all three final frozen-hash reviews completed before interruption.”
- Replace the early rejected L2 arctangent outline by the hash-matched final 46 KB global proof and its final source/continuum reviews.
- Replace blanket quadratic statements by three separate quantifiers: width-first loss Euler; exact GF/sufficiently resolved full-network joint diagonals; every diagonal only in the frozen-bottom model. Keep the old order-one readout explicit.
- Replace “ReLU has no continuous limit” by classical fixed-gate-derivative noncontinuation **and** actual-Euler scalar local compactness for every mesh tending to zero. A unique deterministic generalized full-state limit remains a separate question.
- Replace the late sin+cos claims in these two tasks by their corrected finite-step/initial-geometry scope. Later all-depth results may settle the underlying problem on their own hypotheses; they do not repair the old estimate.
- Retain the duplicate-opposite-label example only as a universal strict-activity/nontrivial-learning obstruction. It is compatible with a stationary autonomous limit.

Global existence, an absolute positive local window, scalar output convergence, hidden W2 path convergence, velocity-energy convergence, and autonomous restartability are separate axes. The recovered operator results materially populate all of these axes, and their distinctions survive later supersession.
