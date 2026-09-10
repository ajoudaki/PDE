# Independent complete mathematical audit B2

Verdict: **required model-scope correction**. The formal coefficient formulas in B require unit mobility multipliers, which B does not explicitly select from the shared convention. The identification of the initial raw kernel in D.1 needs the same clarification for the readout mobility. With that convention explicitly stated, I found no further required correction in A–E or in the complete supplied dependency proofs.

This verdict concerns the exact, unchanged inputs identified below. It does not certify a later revision.

## Required correction: declare the mobility convention in B and D.1

`FINAL_SCOPE_ADDITION.md` lines 263–264 specify mean square loss with the “shared raw mobilities.” However, `docs/NOTATION.md` lines 78–82 define those mobilities as

\[
n\kappa_1,\quad\kappa_2,\quad\kappa_3,\quad n\kappa_4,
\qquad \kappa_j>0,
\]

without setting the multipliers to one. The supplied finite-model dependency independently retains these multipliers in its exact updates and kernel: dependency lines 49–56 and 72–80. The independent-fragment convention at addition lines 3–9 does not transfer A's explicit unit-mobility assumption to B.

B's formulas nevertheless use unit multipliers. In particular:

- Lines 302–324 and 367–369 identify the first readout coefficient as \(C_1=\gamma h_y\), where \(h_y=\sum_a y_aH_3^a\). With the shared general convention it is instead \(\dot C(0)=\kappa_4\gamma h_y\).
- Lines 360–381 give unweighted hidden kernel coefficients and readout constant term \(Q_3\). The actual initial readout block is \(\kappa_4Q_3\).
- Lines 401–405 give a first Euler readout update and Gaussian scale without the readout multiplier.

For an explicit discrepancy, choose \(\kappa_4=2\), \(\kappa_1=\kappa_2=\kappa_3=1\), which the shared convention allows. B's formal initial total kernel is then \(2Q_3\), not \(Q_3\). Keeping B's definitions of \(R_j\) and

\[
M_1=G\circ R_1,\qquad M_2=Q_1\circ R_2,\qquad M_3=Q_2\circ R_3,
\]

the general-mobility hidden degree-two blocks are

\[
t^2\kappa_1\kappa_4^2M_1,\qquad
t^2\kappa_2\kappa_4^2M_2,\qquad
t^2\kappa_3\kappa_4^2M_3.
\]

The corresponding label quadratic-form identity is

\[
y^TK(t)y
=\kappa_4y^TQ_3y
+2\kappa_4^2t^2\sum_{j=1}^3\kappa_jy^TM_jy
+\text{formal terms of degree at least three}.
\]

Indeed each first backward coefficient acquires \(\kappa_4\); its raw kernel block acquires the additional \(\kappa_j\). The hidden acceleration in block \(j\) is \(\gamma^2\kappa_j\kappa_4J_{y,j}^*h_y\), and the readout kernel has its additional \(\kappa_4\), giving the same weighted degree-two contribution as the hidden blocks. Thus the missing convention affects exact constants, not just presentation.

Addition lines 729–759 likewise identify the initialized full raw kernel as \(K(0)=Q_3\). For the shared general metric it is \(K(0)=\kappa_4Q_3\), since only the readout gradient survives at zero readout. The bounds in lines 764–767 then carry the same scalar factor in both kernel blocks, although the displayed inverse-times-coupling ratio is unchanged.

The minimal correction is to state explicitly that B uses \(\kappa_1=\kappa_2=\kappa_3=\kappa_4=1\), and that D.1's initialized raw kernel uses unit readout mobility, or simply the unit-mobility product raw metric throughout that subsection. This preserves all displayed formulas and proofs. Retaining arbitrary multipliers would instead require the weighted formulas above. No input was edited during this audit.

## Complete A–E checks

### A: verified on its explicit order-one-readout, unit-mobility continuous flow

The metric and four kernel terms at lines 31–46 agree with the finite dependency. The initialization calculation at lines 85–114 uses a legitimate fixed finite Gaussian transcript: clip the independent centered readout, then the first reverse source; the response expectations vanish by independence and centering. Removing the clips uses already established joint second moments and bounded actions, and yields exactly \(s_3,s_2,s_1\) and \(K_0\).

Conditioning on hidden initialization leaves each initial reverse coordinate Gaussian linear in the readout. The column/operator bounds in lines 116–134 therefore prove the exponential-square empirical estimate and maximum bound without assuming independence of query coordinates. The signed feature flow has global finite-feature-time bounds by the ordered rank-one estimates. Its path-length bound (A.7) has the correct sign and normalization.

The Jensen calculation (A.8) is valid, including its zero case. The reverse difference splits always pair a new gate difference with an initial multiplier, so they introduce one \(\sqrt{s\log(e/s)}\) modulus, rather than repeated logarithms. Bounded actual and immutable action norms transfer that modulus through both reverse layers. The physical clock satisfies \(s(t)\le2t|r(0)|\). This proves the deterministic vanishing-time conclusions; for label zero the initial residual is \(O_{\mathbb P}(n^{-1/2})\), which transfers the same estimates to every fixed physical horizon.

Both coordinate balances (A.9) follow by differentiation with the stated \(1/n\) rank-one update. The increment-column bound and Minkowski give (A.10). The static concentration example is compatible with these bounds: at a coordinate with gate \(n^{-1/2}\), \(\Phi\) is of order \(\sqrt n\), while an ungated query of order \(\sqrt n\) retains order-one normalized square energy. This example is explicitly not promoted to a reachable trajectory. A supplies neither a nonzero-label positive-time tail theorem nor an exact-GD conclusion.

### B: verified coefficient geometry after the required mobility declaration

The trigonometric covariance identity (B.1), unit diagonals, and three Gaussian Gram recursions are correct. The tensor-power expansion and the interpolating polynomials at lines 284–295 prove strict positivity for distinct inputs even when the raw Gram is singular. The response derivatives give exactly \(J_3\) and \(J_2\). The lower reverse input needs a clip; its Gaussian-plus-bounded representation supplies the integrable derivative domination required to remove that clip.

The strict-positivity proof for \(R_3\) uses positive density of \(Z_3\) and nonzero trigonometric factors. The independent innovation covariance and tensor-product argument then prove \(R_2,R_1\succ0\) and \(G\circ R_1\succ0\). There is no implicit nonsingularity assumption on \(G\).

With unit multipliers, hidden velocity is zero initially and the readout first derivative is \(\gamma h_y\). Hidden acceleration is \(\gamma^2J_y^*h_y\); the readout block and the three hidden blocks each contribute \(t^2y^TMy\). Thus the factor two in (B.6) is correct as a formal coefficient identity. The text does not claim a remainder estimate or an existing sin-plus-cosine trajectory. The finite Gaussian sum formula and affine-regression value \(1-2/e\) are correct.

At the first zero-readout Euler node, \(\phi\phi'=\cos(2z)\). The reverse response vanishes and its source variance is \(4h^2E\cos^2(2G)=2h^2(1+e^{-8})\), under unit readout mobility. Sending \(h\) to zero at each fixed \(p\) contradicts a common bound for every Gaussian \(L^p\) norm. The rejected estimate is not used to claim failure of a continuous-time limit theorem.

### C: verified with its stated fitting conditions

The product Hilbert metric gives all four equations (C.1). Polynomial local Lipschitzness on bounded raw balls and the exact energy identity give a strong Cauchy endpoint at any hypothetical finite maximal time, proving global existence, uniqueness and reached-state restart for the given bounded initialized operators. The canonical initialized covariance (C.3) is a separate fresh-forward Gaussian fact.

The forward derivatives, raw kernel (C.4), and augmented-Gram bound (C.5) are correct; the bound includes \(q_1=0\) without a division by its norm. Each balance defect in (C.6) is exactly the fixed-offset term, and compression annihilates it. Three distinct unit inputs are affinely independent, including singular raw-Gram configurations. The stationary-predictor classification consequently gives precisely the stated possible binary-label loss levels.

For the conditional fitting result, \(R_u=-\|\theta_u\|^2\) gives (C.7). Entry below \(4/3-\epsilon_0\) supplies \(\|Pf\|\ge\nu\), hence \(\|q_1\|^2\ge\nu^2/[12(1+u)]\). The separately assumed \(G\succeq\lambda I\) supplies the kernel lower bound. Its integration bounds the entire residual-length clock by (C.8), makes the raw path converge strongly, and then supplies exponential decay in physical time. The text does not infer either entry below the barrier or positive raw-Gram margin from pairwise separation, and does not promote this reference calculation to the proposed nonlinear activation.

### D: verified causal lemma; D.1 needs the stated metric clarification

Both triangular resolvents exist as finite nilpotent sums. The running-maximum estimate for \(AB\) correctly allows concentrated old columns of \(B\); \(BA\) has the claimed column-density bound. This gives (D.6), including the individual-column estimate for \(U\). Exact elimination gives (D.7) with the actual coefficients and covariance.

The actual second-moment premises bound the standard deviations of the Gaussian parts. Minkowski, the Gaussian moment bound and discrete Gronwall give precisely (D.3)–(D.5), without independence between a Gaussian part and its remainder, a small \(\epsilon S\) assumption, or a minimum mesh step. Expanding the exponential from the \(C\sqrt p\) bound proves the asserted square-exponential tails. The lemma does not establish its own response or second-moment premises for a neural application.

In D.1, the two-coordinate-plane argument proves \(\lambda_2(G)\ge\delta\). Gaussian regression remains valid at singular covariance and yields (D.8); bounded residual trace and three-layer iteration give the positive correction bounded by \(9I\). Subject to the unit-readout declaration, (D.9)–(D.10) follow. Direct differentiation gives both equations in (D.11), including \(\dot L\). The orthogonal projection in (D.12) keeps the hidden-parameter-dependent offset and orthogonal component. These identities establish neither trained Schur positivity nor an autonomous scalar closure.

### E: verified actual positive-time obstruction on the constructed local flow

The replacement activation has all the explicit value, slope and curvature bounds used in the complete two-query induction II.B. Its transfer uses none of the same-label fitting or motion arguments of II.D. Fixed-cap coordinate instructions, the common action construction, and the asymmetric two-query comparison in II.C.1–II.C.2 therefore supply the claimed strong local uncut flow, actual adjoints and Hilbert–Schmidt increments. Both label configurations are covered. Sample exchange is used through deterministic limiting laws, not as a false samplewise finite-width identity.

The finite raw Euler bounds give the temporal \(L^2\) modulus of the top backward input, hence the same covariance modulus for its reverse Gaussian source. The dyadic Gaussian maximum proof applies to the finite interpolated source and to its orthogonal regression residual. The top readout has nonzero first derivative in \(L^2\) for either label mode; strict positivity of the gate then gives the positive terminal reverse-source variance for every sufficiently small positive time.

Conditioning on the reverse source controls its complete path and forces either query sign for every forward realization. Independent forward-source regression requires only its positive scalar variance. The terminal residual coordinate of that regression is zero, so the placement proof requires no bound on the remaining forward source. The displacement estimate, causal Lipschitz estimate and intermediate value theorem give an interval preimage of radius at least \(ce^{-C(R+1)}\), inside an interval of size \(C(R+1)\). Gaussian density bounds give the asserted joint lower tail. The closed inner event and the \(R+1\) query margin make both ordered limiting passages valid.

The first feature Gram is positive for all sufficiently small times, including \(\rho=-1\). Its dual feature \(B_a\) isolates one sample under the rank-one perturbation and has unit norm. Each chosen indicator direction is individually bounded, so its square is in \(L^2\). The second derivative at the last activation is a scalar pairing justified using bounded readout and strong multiplier continuity; it requires no \(L^4\) bound on the propagated direction. The second term of (22) is uniformly bounded over raw unit directions, whereas the first has both unbounded signs by the proved lower tails. The exact full-loss identity (24) is evaluated only after inserting the base-state residual relation. Since \(|g|<1/2\), it proves both signs of unbounded loss curvature and rules out local Lipschitzness of the raw gradient. The positive physical-time change is bounded as stated. The conclusion is local and does not contradict the separately proved strong existence or uniqueness.

## Dependency audit and read attestation

I personally read **every line** of all three scientific inputs: addition lines 1–1254, dependencies lines 1–4511, and notation lines 1–98, a total of **5,863 lines**. A small tool-output truncation near dependency lines 1931–1951 was resolved by explicitly rereading lines 1928–1956; those lines are included in this attestation.

The dependency audit included the complete finite model Sections 1–4; Part II.A's raw geometry and label-mode scope; every step and numerical bound of II.B's chronological response induction; all of II.C's construction, cap removal, physical-algorithm and observation arguments; and II.D's separation, nonaffinity, backward positivity and initial-motion proofs. It also included every supplied part of III: M's model and quantifiers; F's adaptive Gaussian conditioning, source identity, singular-query regularization, common action spaces, true adjoints and strong/scalar differentiation; S's controlled source bounds and chronological induction; G's geometry, clock and regression bounds; V's construction, finite-algorithm and ordered observation limits; N's backward/forward innovation and initial-acceleration proofs; and A's activation-class refinements and negative depth-uniform example. The larger gain and activation hypotheses of III.M were not imported into A, B, C, D or E merely because the general dependency packet contains that theorem.

I used only the three scientific inputs, `/etc/codex/skills/solve-math-rigorously/SKILL.md`, and checks for applicable ancestor `AGENTS.md` files; none of those instruction files was present on the checked ancestor paths. I read no project history, Git data, previous audit or verdict, other study, or external scientific source. I ran no experiment and delegated no part of this audit. The only written file is this review. This was fresh-context allowed-input isolation, not physical filesystem isolation.

Starting hashes matched the supplied values. A final hash check, after the full mathematical reading and checks and before writing this report, returned the same values:

| Input | Lines | Unchanged SHA-256 |
|---|---:|---|
| `studies/repository_refactor_2026_09_09/FINAL_SCOPE_ADDITION.md` | 1254 | `48a67ae44c8bf628d9cafe88f6d96a179e9ffca4b12440f3f68820212e76d877` |
| `studies/repository_refactor_2026_09_09/reviews/FINAL_SCOPE_DEPENDENCIES.md` | 4511 | `ec849bf098b9c48da4b10f3be63b92acc89ba1de3ff25412634948928769ec51` |
| `docs/NOTATION.md` | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
