# Independent complete mathematical audit A1

Audit date: 2026-09-10.

**Verdict: the five separately stated mathematical scopes A–E are supported by the supplied proofs and dependencies. No theorem-level correction or missing operative dependency was found. One sentence in D needs a minor correction: its row-norm assertion must refer only to the two inverse operators, not also to the operator \(U\) defined immediately before it.** The displayed conclusions of D already use the correct bound and are unaffected.

This verdict does not promote initialization identities, formal coefficients, conditional estimates, or local trajectories to stronger training theorems.

## Input identity and complete-read record

Only the following three project files were used as scientific inputs. No other project document, source, study, review, history, Git information, or chat was consulted. The rigorous mathematics skill at /etc/codex/skills/solve-math-rigorously/SKILL.md was read as procedural instructions. No external specialized theorem was assumed, no web research or experiment was performed, and no audit work was delegated. The only additional computation was bounded deterministic arithmetic on constants already present in these inputs.

| Input | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| studies/repository_refactor_2026_09_09/FINAL_SCOPE_ADDITION.md | 1253 | 57382 | 7454e66b690d39f0a7acfa20903b59f07342ff3af159aa98eccee6595306abcf |
| studies/repository_refactor_2026_09_09/reviews/FINAL_SCOPE_DEPENDENCIES.md | 4511 | 254883 | ec849bf098b9c48da4b10f3be63b92acc89ba1de3ff25412634948928769ec51 |
| docs/NOTATION.md | 98 | 5110 | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |

All 5,862 lines were read in full, including proofs and scope qualifications:

- NOTATION.md: lines 1–98.
- Candidate: lines 1–450, 451–900, and 901–1253.
- Dependencies: lines 1–550, 551–1100, 1101–1650, 1651–2200, 2201–2600, 2601–3000, 3001–3450, 3451–3950, and 3951–4511. A display truncation within the 1651–2200 read was repaired by rereading lines 1920–2040, including the complete affected operator-moment and trace discussion. No displayed omission was treated as read.

Targeted rereads followed the full reads, solely within the same permitted inputs. The three input hashes were checked again after the mathematical checks and were unchanged. The only project write in this audit is this report.

## Required correction: D's inverse row bounds

**Location:** candidate lines 650–653, immediately before the proof of (D.6).

The text defines
\[
\mathcal R=(I-a^2AB)^{-1},\qquad
\mathcal T=(I-a^2BA)^{-1},\qquad U=\mathcal RA,
\]
and then says, “Their complete block-row norms are at most \(E\).” As written, this can include all three operators. The bound is valid for \(\mathcal R,\mathcal T\), but not generally for \(U\).

For an explicit admissible example, take two nodes \(t_0=0,t_1=S=1\), three-dimensional blocks, \(A_{10}=2I_3\), all other \(A\) blocks zero, and \(B=0\). Choose \(\alpha=2,b=0,\varepsilon=1/2\). Then \(E=1\), \(\mathcal R=\mathcal T=I\), and \(U=A\) has complete row norm 2. Zero Gaussian arrays give zero actual fields and satisfy the moment premises. Even if positive bound constants are desired, choose \(b=1\) while retaining \(B=0\): then \(E=e^{1/2}<2=\|U\|_{\rm row}\).

Replace that sentence by:

> The complete block-row norms of \(\mathcal R\) and \(\mathcal T\) are at most \(E\). Consequently \(\|U\|_{\rm row}\le\alpha SE\).

The stronger per-column estimate actually used below is already correct:
\[
\|U_{kj}\|_\infty\le\alpha Eh_j.
\]
Summing it gives the corrected row estimate. Equations (D.6), (D.7), and the constants in (D.3)–(D.5) consistently retain the necessary \(\alpha S\) factor. This is a local wording correction, not a failure of the lemma.

## Model, metric, initialization, and time

The notation contract's first stored matrix and the dependency packet's \(V^{(1)}\) agree through \(W^{(1)}=\sqrt d\,V^{(1)}\). Their first-block metrics agree because \(d\|\Delta V^{(1)}\|_F^2/n=\|\Delta W^{(1)}\|_F^2/n\). The expectation rank-one operator corresponds to \(uv^T/n\), with ordinary finite Frobenius norm equal to its Hilbert–Schmidt norm in the normalized finite coordinate spaces. Each transpose remains the reverse of the same matrix; its population counterpart is the actual adjoint.

The finite derivative formulas, all kernel factors, and dissipation identities in dependency Sections 1–4 check directly. Residuals never enter the backward fields or kernel definition. Nonnegative loss bounds raw path length on every finite interval, making a hypothetical finite endpoint Cauchy and allowing continuation. The bounded-derivative forward/backward RMS induction is width-uniform at fixed depth, but supplies no nonlinear multiplier-tail conclusion by itself.

| Scope | Initialization and loss | Clock or conclusion |
|---|---|---|
| A | Order-one stored readout; one sample; full square loss | \(\dot r=-2K_nr\), signed feature flow, \(s(t)=2\int_0^t|r_n|\) |
| B | Stored readout variance \(n^{-2}\); full mean square loss | Initial coefficient factor \(\gamma=2/m\); no constructed positive-time trajectory |
| C | Given-space affine model; canonical zero readout; half-sum loss | \(\dot r=-Kr\); residual-length clock only in conditional fitting |
| D | Same-array Gaussian implication and separate initialization calculations | Flow identities explicitly assume \(\dot r=-Kr\); no inferred optimizer theorem |
| E | Zero population readout arising from stored variance \(n^{-2}\); two-sample sum loss | \(\theta_s=\nabla g\), \(ds/dt=4(1-g)\) on the constructed population path |

Neither A's initial kernel nor its stationary zero-label limit is borrowed from the tiny-readout model. B's tiny finite readout is used only through its zero limiting initialization. E's scalar clock is established after deterministic population symmetry; it is not assigned samplewise to finite networks.

## A: tanh short-time continuity and zero-label stationarity

**Status: supported within its stated continuous-flow scope.**

The four terms of (A.1) are the exact raw gradient squares. Conditioning on the initialized hidden weights makes the initial prediction a centered readout Gaussian of variance at most \(1/n\). This remains true with order-one stored readout because the predictor includes \(1/n\).

For (A.5), the three forward-only Gaussian calls give the stated \(q_j\). With an odd bounded smooth readout truncation, the first reverse source coefficient is zero by independence and centering. The next coefficient vanishes after an odd clip of its independent centered Gaussian query. Joint \(\mathcal W_2\) convergence removes query clips using square tails, and bounded gates/actions propagate the errors. The backward recursion is linear in the readout, justifying removal of its truncation using Gaussian square tails. This yields exactly \(s_3,s_2,s_1\) and
\[
K_0=q_3+s_3q_2+s_2q_1+s_1.
\]
No unbounded coordinate instruction is directly assigned bounded derivatives.

The conditional variances in (A.6) are bounded by the displayed column/action norms. One sufficiently large deterministic \(L\), on the high-probability initialized norm event, controls the exponential-square empirical averages. Independence of different query coordinates is unnecessary for Markov's inequality or the union bound.

Bounded features control the signed-feature readout, then the upper action, lower action, and bottom velocity on compact feature intervals. These estimates exclude feature-time escape. The alternative length bound (A.7) also has the correct sign and constants: the increase of \(\sigma f\) is \(\int K\), while the endpoint prediction difference is at most \(2\|W^{(4)}(0)\|_2/\sqrt n+s\).

The entropy estimate (A.8) follows from Jensen with \(p_i=w_i^2/(nu)\). Tanh gate differences have magnitude at most one, meeting its hypothesis. Every new reverse gate is paired with a fixed initialized multiplier, so the recurrence carries a single \(\sqrt{s\log(e/s)}\) modulus; it does not iterate the logarithm. Bounded action differences transfer the result to actual and immutable queries. The column bound gives (A.3).

The physical clock is bounded by \(2t|r_n(0)|\), with tight initial residual. For \(y=0\), residual monotonicity gives \(s(T)=O_{\mathbb P}(n^{-1/2})\), allowing the two-limit short-clock estimate on every fixed physical horizon. This proves the stationary limit (A.4), not a nonzero-label feature-learning limit.

Both identities in (A.9) differentiate correctly. The uniform coordinate bound on \(\sqrt n\|p_j\|\), integrated immutable-query RMS bound, and Gaussian integrability of \(\Phi(G)^2\) prove (A.10). The static concentration example correctly shows why bounded inverse-gate RMS does not imply square-tail control of an ungated query. No canonical reachability or raw-Euler balance assertion is made.

## B: initialized covariance and formal coefficient geometry

**Status: supported as initialization and formal coefficient statements only.**

For standard Gaussian marginals, both products in (B.1) reduce in expectation to \(\cos(X-Y)\); simultaneous-sign-odd sine terms vanish. The covariance recursion (B.2), including unit diagonals, follows. Strict positivity holds even at singular input Gram: the tensor-power expansion gives all polynomial tests, and the interpolation polynomial isolates each distinct input. Positive definite later Grams admit distinct vector realizations, so the argument repeats.

Differentiating \(C_1\phi'(Z_3^\mu)\) gives both terms of \(J_3\). Differentiating the next gated source gives \(J_2\), including its negative diagonal term. Each primitive reverse covariance is the full input second moment \(R_j\), not a response-subtracted covariance. Independent primitive Gaussian groups coexist with the response terms and are not substituted independent matrices.

The positivity argument for \(R_3\) is valid for the binary labels in the supplied model: \(a=\gamma y\ne0\), both trigonometric factors have dense open nonzero sets, and \(Q_2\) gives full Gaussian support. The tensor-vector proof of strict Hadamard-product positivity only needs positive diagonal in the other Gram. Thus \(G\circ R_1\succ0\) does not require \(G\succ0\).

The unbounded middle product is handled in the correct order. Its Gaussian-plus-bounded input has integrable value and derivative envelopes. At fixed smooth query clip, III.F applies; dominated convergence passes expected derivatives, and joint \(\mathcal W_2\) tails plus action bounds identify the uncut answer.

The factor 2 in (B.6) is correct. With \(h_y=\sum y_aH_3^a\), hidden acceleration is \(\gamma^2J_y^*h_y\). The three hidden blocks contribute \(t^2y^TMy\), and the readout-feature Gram contributes another \(t^2y^TMy\). Initial hidden velocity is zero. The higher-degree notation is expressly formal, not an analytic remainder or an application of III.M's different activation theorem.

The complex-exponential formula has the correct \(2^{-k/2}\) normalization and phase. The affine regression residual is \(1-2/e>0\). The rejected first-Euler-node estimate fails for the stated reason: its reverse source has variance \(2h^2(1+e^{-8})\), while the proposed \(Kh e^{Khp}\) bound would give a common bound for all Gaussian \(L^p\) norms after \(h\downarrow0\) at each fixed \(p\). This does not disprove a separate local construction.

## C: affine global flow and conditional fitting

**Status: supported, with the fitting implication remaining conditional.**

On the affine Hilbert space, (C.1) is a locally Lipschitz polynomial vector field. The \(W:V\to\mathcal H_1\) block is Hilbert–Schmidt because \(V\) is finite dimensional. The loss identity and Cauchy–Schwarz give (C.2), including initial loss \(3/2\) for zero readout and three binary labels. Completeness supplies the endpoint used to prove global continuation from every finite initial state.

The canonical covariance (C.3) uses fresh centered initialized forward calls and the fixed constant offsets. Differentiating features gives (C.4). For (C.5), put \(h=Wd+se_1\). Then \(s^2\le2\|h\|^2+2\|W\|^2\|d\|^2\), while \(\|q_1\|\le\|A\|\|q_2\|\). These imply the displayed denominator and include \(q_1=0\) without division.

The offset defects (C.6) have the correct signs and layer types. Compression by \(I-e_\ell\otimes e_\ell\) kills each defect, but does not restore a full homogeneous balance. Training an augmented offset column would change the equations.

Three distinct unit vectors are affinely independent because a line meets the sphere at at most two points. The stationary classification follows from \(H_2r=0\), then \(\sum r_i=0\), and, when \(q_1\ne0\), \(Xr=0\). When \(q_1=0\), the expanded predictor is constant. The possible stationary binary losses and initial decrease are correct. An initial derivative alone does not prove crossing the mixed-label level \(4/3\).

For conditional fitting, \(R_u=-\|\theta_u\|_{\rm raw}^2\) bounds total squared clock-speed by \(\sqrt3\). Entry below \(4/3-\epsilon_0\) gives the positive nonconstant-prediction margin \(\nu\). Displacement gives \(\|W\|^2\le4(1+u)\), hence \(\|q_1\|^2\ge\nu^2/[12(1+u)]\). The separately assumed \(G\succeq\lambda I\) then gives (C.8) by integrating a logarithmic kernel lower bound. Finite residual-length clock yields a bounded strong endpoint and a uniformly positive kernel, giving exponential physical fitting. Earlier zero residual is stationary and is included. No unconditional entry argument or nonlinear perturbation theorem is inferred.

## D: same-array value bounds and initialized geometry

**Status: the lemma and separate identities are supported, with the wording correction above.**

The causal inverse bounds concern the actual deterministic arrays. For \(\mathcal R\), running maxima correctly avoid a nonexistent column-density bound for \(AB\). For \(BA\), the block bound \(b\alpha h_j\) does hold. This proves (D.6), including \(\|U\|_{\rm row}\le\alpha SE\).

Eliminating the exact equations gives (D.7). Its Gaussian parts are centered combinations of the actual sources even when the forward/reverse groups are correlated. In particular,
\[
\|(q_G)_{ki}\|_2
\le Q+\varepsilon a b\alpha ESQ+\varepsilon(\pi/2)bE=V.
\]
The Gaussian moment bound and strict causal recurrence give \(M=(4V+d_0)e^{k_0S}\). The forward estimate uses \(\|U\|_{\rm row}\le\alpha ES\) and \(\|UB\|_{\rm row}\le\alpha bES\), yielding exactly \(V_Z\) and (D.5). Neither independence from the nonlinear remainder nor small \(\varepsilon S\) is needed. The moment expansion gives Gaussian value tails. Actual response bounds and actual second moments remain premises, particularly for nongradient caps.

The three-input eigenvalue argument proves \(\lambda_2(G)\ge\delta\). Gaussian regression at singular covariance gives (D.8)'s orthogonality. The contraction \(|az+\varepsilon\arctan z|\le|z|\) bounds initialized variances, while \(a>0\) keeps them positive. Three residual Grams of trace at most 3 give \(0\preceq R\preceq9I\) in (D.9). Zero readout is essential to its identification with the full initial kernel. The coupling bounds (D.10) are only initialized bounds.

Substitution verifies (D.11), including \(\dot L-L\sigma\). Formula (D.12) is orthogonal projection under its stated invertibility premise. Neither closes an autonomous scalar system or proves a trained positive Schur complement.

## E: reached-state tails and unbounded full-loss curvature

**Status: supported for the actual local population trajectory at every fixed positive feature time specified.**

The new activation satisfies \(5/6<\phi<7/6\), \(0<\phi'\le1/10\), and \(|\phi''|\le1/5\). II.B's complete numerical induction uses precisely these bounds, the readout integral bound, and \(|G_{ab}|\le1\). It uses no arctangent coordinate transform, same-label readout positivity, or special higher jet. Thus (E.2) and both query envelopes transfer for either label mode.

II.C.1–II.C.2 provide the local construction: cap-independent primal bounds; fixed-cap III.F programs after harmless readout truncation; a two-query comparison with a single \(1+R\) factor; and strong state/velocity cap removal at rate \(e^{CR-R^2/256}\). Rank-one integration supplies Hilbert–Schmidt increments. These establish feature-flow uniqueness and reached-state restart. After the population clock is identified, the physical asymmetric comparison described in II.C.3 also gives local physical uniqueness without requiring a competitor to have sample symmetry.

The sign/exchange argument proves \(f_a=y_ag\) for deterministic population predictions. It respects the singular first-layer metric at \(\rho=-1\), and uses only symmetry in law at finite width. The sum-loss clock is therefore \(ds/dt=4(1-g)\).

The lower-tail proof obtains its required uniformity from primal finite-Euler estimates: the top backward inputs have an \(L^2\)-Lipschitz temporal modulus, giving the same covariance metric for the reverse Gaussian source. Linear interpolation preserves it. The dyadic finite-Gaussian estimate (9) uses a union bound rather than independence among increments, and still holds after scalar Gaussian projection.

Initially the first feature Gram is positive definite even at \(\rho=-1\), where its features are \(1+b(G)\) and \(1-b(G)\) with nonconstant odd \(b\). The later Gaussian feature Grams are positive definite. Thus \(V_0=\frac12\sum y_aH_a^3(0)\ne0\), and \(W^{(4)}(S)/S\to V_0\) ensures positive top-backward second moment at all sufficiently small positive \(S\). The reverse scalar regression denominator is consequently bounded below uniformly in sufficiently late cap/mesh approximations.

A large terminal reverse Gaussian value and a bounded independent residual path give a whole-source bound \(C(R+1)\), at cost \(ce^{-C(R+1)^2}\). The actual middle query differs from that source by at most \(7/6\), for every forward-source realization. Regression of the independent forward group gives a terminal residual identically zero and a scalar variance at least \((5/6)^2\). The map \(x\mapsto Z_{M,a}(x)\) stays within \(D_R=O(R+1)\) of \(x\) and has Lipschitz constant at most \(Ce^{C(R+1)}\). Its continuous range and a Gaussian density bound place the terminal preactivation inside any interval with the claimed extra Gaussian cost. No measurable root selection is needed: the measurable preimage contains a sufficiently long interval.

The terminal event is closed and strictly inside the desired event. The closed-set inequality passes its lower probability bound in the correct direction, first as the fixed-cap mesh vanishes and then as the cap is removed. Constants are uniform in both limits. Thus (E.1) is a statement about the reached uncut law.

For curvature, the dual first-feature direction \(B_a\) is a unit vector isolating one sample; the rank-one \(W^{(2)}\) direction has raw norm one. Each indicator direction \(v\) is individually bounded, so \(v^2\in L^2\) and the adjoint pairing in (22) is legitimate. Bounded reached readout makes \(L^2\) convergence sufficient for the final scalar second derivative; no \(L^4\) bound on its propagated first variation is needed. The Taylor cross term retains its required \(|t|\).

The first term of (22) has both unbounded signs by (E.1) on an interval where \(|\phi''|\) is bounded below. The other term is uniformly bounded by (23). Scalar first derivative norms are bounded. Differentiating the full sum loss before substituting the base-state residuals gives exactly
\[
-D^2\mathcal L[v,v]
=4(1-g)D^2g[v,v]-2\sum_a(Df_a[v])^2.
\]
Therefore both signs of full-loss curvature are unbounded on raw unit directions. A locally Lipschitz gradient would bound every such second derivative by its common Lipschitz constant, a contradiction.

Finally \(|g|<1/2\) implies \(S/6\le t(S)\le S/2\). The obstruction is at actual deterministic positive physical times and does not contradict the constructed local existence, uniqueness, or restart. No fixed-positive-time finite-width Hessian limit or opposite-label global continuation follows.

## Complete dependency audit and closure

The following checks cover the remainder of the supplied packet as well as the operative portions above.

| Portion | Audit result |
|---|---|
| Finite Sections 1–4, lines 8–214 | Derivatives, metric, kernel, global GF, Gaussian initial event, and fixed-depth RMS bounds check. Their distinction from adaptive multiplier tails is maintained. |
| II.A, lines 277–471 | Raw first-field metric, singular endpoint, exchange isometry, symmetry in law, deterministic population identity, and sum-loss clock agree. |
| II.B, lines 473–789 | The response induction never uses an unknown current row. Both sample contributions retain their factor \(1/2\). Fixed-cap coordinate hypotheses and retained zero-variance source slots are correct. |
| II.C, lines 791–1288 | Common spaces, both-cap comparison, strong/raw identification, same-label fitting clock, finite off-mode control, stopping, and ordered observation limits check. |
| II.D, lines 1292–1629 | Pair separation, marginal support, regression residual, backward pair positivity, motion, initialized transpose closure, and quadratic kernel coefficients check for their same-label shifted-arctan model. Its gate-ratio proof is not transferred into E. |
| III.M, lines 1646–1911 | Gain-selected model, raw normalization, half-sum clock, fixed finite-depth quantifiers, and observations are consistent. Its activation theorem is different from A, B, D, and E. |
| III.F, lines 1913–2453 | Adaptive conditioning, negligible finite-rank projected noise, source integration by parts, full input covariance, singular-query perturbation, feedback, common-space completion, and genuine adjoints close internally. Scalar Fréchet differentiability does not assume an \(L^2\)-valued activation derivative. |
| III.S, lines 2455–2710 | Actual coefficients, independent primal stop bounds, same-array elimination, expected derivative production, explicit gain boxes, and chronological induction close. Nongradient caps do not borrow gradient dissipation. |
| III.G, lines 2712–3118 | Augmented input geometry, summable initialized derivative loss, displacement, Gram floor, nonsymmetric capped residual estimate, total control clock, and nonaffinity stability check. Measurable controls are approximated in \(L^1\), not sampled arbitrarily. |
| III.V, lines 3120–3579 | One-cap-factor comparison, physical cap removal, primal events, response probes, derivative-valid velocities, true backward observations, same-width GF/GD comparison, and final tail order check. Path convergence uses the interpolation bound. |
| III.N, lines 3581–4146 | Forward/backward positivity, true-return recursion, regression innovations, coherent clipping, physical accelerations, and coefficient 18 check with the original metric. |
| III.A, lines 4148–4511 | Regression stability, finite-interval witness, gain selection, compact-support obstruction to a depth-uniform margin, and the open \(C_b^2\) ball with positive all-scale margin check. Uniform constants are not promoted to uniform width convergence over the class. |

The foundational conditioning argument preserves the product law of residual matrix factors one query at a time. Integration by parts recovers the actual opposite-orientation response. Input-noise regularization removes singular query Grams using covariance square roots rather than pseudoinverse continuity. Common generated spaces are completed only after finite norm and transpose identities pass to the limit. These supply the operative closure for A, B, C's canonical initialization, and E.

The bounded deterministic arithmetic check verified
\[
\frac72\left(\frac{Q_*}{5}+\frac{V_*}{100}\right)
+\frac3{200}Q_*^2
=\frac{71063018523}{73728000000}
\approx0.9638538754<0.97,
\]
with \(V_*=3067/3200\) and \(Q_*=24829/19200\). It also checked \(49/36+3/25=1333/900<3/2\), preceding exponent margins, and the integer inequalities bounding exponential constants. The query-envelope upper bound is approximately \(1.19004<2\); the packet also supplies elementary strict bounds, so its conclusion does not depend on floating-point arithmetic.

The supported outcomes are exactly A's short-time continuity and stationary zero-label limit; B's initialization and formal coefficient identities; C's global affine flow and conditional fitting implication; D's auxiliary same-array implication and separate initialized/residual identities; and E's local reached-state failure of raw-gradient local Lipschitzness. The sole correction above changes none of these conclusions.

