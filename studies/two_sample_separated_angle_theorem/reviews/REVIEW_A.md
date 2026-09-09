# Independent adversarial complete-proof review A

Date: 2026-09-07.

**Verdict: PASS.** The entire separated-angle extension in `PROOF.md` follows from the attached mathematical lemmas with their hypotheses discharged. I found no required correction, open mathematical premise, hidden dependence of the activation threshold on the actual correlation or physical horizon, or weakening of the stated observable topology. This verdict concerns the theorem with a fixed positive separation; it does not assert a common positive threshold as the separation tends to zero.

## Review scope and independence

I read all 527 lines of the candidate. I used only the attached `sources/` files as mathematical dependencies, and the permitted rigorous-mathematics skill as procedural guidance. I did not inspect old or sibling reviews, status files, README files, ledgers, preparatory notes, or source-task history. Historical status statements inside the allowed source documents were not premises. I did not use agents, experiments, external mathematical sources, or modify the candidate.

The primary adversarial targets were the order of quantifiers, uniform selection from the separation alone, the antipodal endpoint, all four label patterns, the Gaussian minimum, each numerical bound in Sections 3–5, and the data-dependent stopping time. I also checked the construction, both matrix orientations, cap removal, physical dynamics, exact raw GD, velocities, path-space laws, uniqueness/restart, and initial nontriviality.

## Source integrity

The candidate SHA-256 at the start of review was

`2891b892667396d64bd747689bcd59aa7ca3ffd224d3579fc3407bca0b623f9a`.

It was rechecked after the substantive review and remained identical. Every attached source hash matched `SOURCE_HASHES.json`:

| Source | SHA-256 |
| --- | --- |
| `ANGLE_SPECIFIC_THEOREM_ASSEMBLY.md` | `27b2579f27ec14319dd39a93a4942d7b6463860648462d5ccb31b662c7725b75` |
| `CONTRACT.md` | `e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd` |
| `FIXED_CAP_VELOCITY_BRIDGE.md` | `a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0` |
| `INITIAL_FEATURE_LEARNING.md` | `bd81de0a7ad0cb9bdd1f27f89961f4a3b7a7da6914456ae08596a882fa2ec351` |
| `L3_LOCAL_COMPLETE_PROOF.md` | `f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4` |
| `NONLINEAR_RESPONSE_PERTURBATION.md` | `ef0ea077406a27307bc84e045feebf5099f6f81883bdfed41508035fe4559568` |
| `PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md` | `99eb60a64df1bbf4d8b70f351198abced9ef7eaeacf9b39c3997da5700a8f066` |
| `SYMMETRY_RADIAL_CLOCK.md` | `40882fc19e44b4b9245156595bb1071bd4de6007d619fada54c9fce7c37903f4` |
| `TWO_SAMPLE_SOURCE_BASELINE.md` | `a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f` |

The angle-specific assembly was hash-checked but not used as a premise. The candidate is established directly from the component mathematical lemmas.

## Coverage of supporting proofs

| Dependency | Proof coverage and checked use |
| --- | --- |
| `SYMMETRY_RADIAL_CLOCK.md` | Read the complete proof, including finite Euler equivariance, deterministic population symmetry, the strong radial lemma, the raw metric and chain rule, initial kernels, affine existence through the target margin, both common/contrast arguments, and Gaussianity. |
| `TWO_SAMPLE_SOURCE_BASELINE.md` | Read the complete proof. Checked the exact two-sample source program, frozen formal derivatives, current returns, affine primal estimates, Gaussian probe identity, response-row constants, and population-to-finite primal conversion. |
| `NONLINEAR_RESPONSE_PERTURBATION.md` | Read the complete proof. Checked primal comparison independently of response assumptions, the coefficient-prefix moment estimates, current-coordinate multiplier, same-coefficient derivative perturbation, causal deterministic stability, and the four-stage induction. |
| `PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md` | Read all four parts. Checked the explicit affine comparison constants, asymmetric cap estimate, reference-only tails, physical two-residual comparison, exact raw Euler comparison, uniqueness/restart, and ordered velocity/path-law limits. |
| `FIXED_CAP_VELOCITY_BRIDGE.md` | Read the complete proof, including nonlinear probes, all-index derivative estimates, both appended observational queries, product truncations, deterministic comparison (33), and the finite-width/time-uniform tail and velocity arguments. |
| `INITIAL_FEATURE_LEARNING.md` | Read the complete proof. Checked both initial transpose returns, the positive-definite Gram arguments at the endpoint, every hidden parameter block and sample feature, and the projected-kernel expansion. |
| `L3_LOCAL_COMPLETE_PROOF.md` | Read lines 211–455 (complete fixed-program conditioning and singular-query proof), 456–616 (common generated action spaces, boundedness and exact adjunction, with the surrounding setup), and 1748–1918 (gradient/HS/chain-rule argument). Only the general conditioning, action-space, adjunction and scalar-gradient ingredients were used; the one-sample local arctangent theorem was not substituted for the new theorem. |
| `CONTRACT.md` | Read fully to verify initialization, loss, raw metric, interpolation and observable conventions. Its historical research status was not used. |

## 1. Exact model, geometry and foundational identification

The finite equations match the stated loss and raw metric. The Euclidean first-weight loss gradient has factor \(1/n\), and multiplication by the inverse metric \(n/d\) gives the required \(1/d\). Blocks 2–3 retain \(1/n\), while the readout metric removes the \(1/n\) in its Euclidean gradient. Consequently the first projected kernel is \(\rho_{ab}\langle b_a^1,b_b^1\rangle\), with no missing factor of \(d\), \(n\), or 2. The projected feature objective \(g=y^Tf/2\) has physical conversion \(ds/dt=2(1-g)\).

The conditioning dependency is applicable to a fixed transcript with two interleaved independent Gaussian matrices, each used in both orientations, and the complete first-row Gaussian root tuple. For fixed \(d\), that tuple has the required moments. The first pair may be singular. The source proof treats singular query Grams by independent query-noise regularization at fixed transcript length, then a zero-noise limit controlled by bounded matrix actions and continuous finite source expressions. It does not require convergence of a pseudoinverse at a rank drop. Formal source arguments remain separately named; current returns are retained.

The common-space construction uses consistent finite joint laws on a countable coordinate collection. Its dense span and the Gaussian operator-norm estimate extend each orientation to a bounded \(L^2\) action, and finite adjunction passes to actual adjoints. Adding the fixed input-row tuple and the finitely or countably many desired programs preserves this construction. One fixed coefficient is chosen before constructing these spaces, so no uncountable simultaneous construction is needed.

Every label pair is covered by \(y=(\sigma,\sigma\tau)\), with \(\sigma,\tau\in\{-1,1\}\). The root reflection exchanging the two inputs exists at \(\rho=-1\) as well as in the interior. Symmetry is established by finite-program equivariance followed by deterministic population limits, rather than by assuming uncut uniqueness. The finite realization is not presumed symmetric. The small finite Gaussian readout is retained and has vanishing normalized size; only its population limit is zero.

## 2. Affine stopping interval and uniform primal constants

For same labels, \(\kappa_0=(7+\rho)/2\ge3\ge\delta/2\), since \(0<\delta\le2\). For opposite labels, \(\kappa_0=(1-\rho)/2\ge\delta/2\). These inequalities include \(\delta=2\), where the only admissible correlation is (-1).

The strong radial lemma gives both \(g'\ge\kappa_0\) and \(\|C'\|^2\ge\kappa_0\). Its proof uses strong Hilbert differentiation and convexity of \(\sqrt{\|C\|^2+\epsilon^2}\), with the correct regularity assumptions verified for the affine polynomial gradient. The energy identity gives, until and at the first hit \(g=3/2\),

\[
S\le \frac{3}{2\kappa_0}\le\frac3\delta,
\qquad
\|\Theta(s)-\Theta(0)\|_{\rm raw}
\le\sqrt{s g(s)}\le\frac{3}{2\sqrt{\kappa_0}}
\le\frac3{\sqrt{2\delta}}.
\]

The affine polynomial field is locally Lipschitz on the Hilbert state, and the energy bound gives a strong endpoint. Thus the hit exists without any nonlinear continuation premise. These are exactly the constants in (8)–(9).

Each first projection changes by at most the first raw displacement because \(\|x_a\|/\sqrt d=1\). Matrix operator changes are bounded by their HS changes. With initial projection norms 1 and initial action norms at most 10, \(U=11+R_\delta\) is valid. Although \(\sqrt d\|w_0\|_2=\sqrt d\), this quantity never enters activation selection. Bounds on the full first field may depend on the fixed dimension in the later convergence arguments, as the theorem permits.

The use of \(S_\delta\) does not extend an affine trajectory beyond its own first hit. The response theorem covers any family of meshes with duration at most its supplied upper bound and the specified primal bound. A family's endpoints may therefore be the particular \(S\le S_\delta\). Every time sum and exponential in the response proof uses only an upper duration bound. This disposes of the variable-stopping-time concern.

## 3. Uniform variance and Gaussian nonaffinity margin

For opposite labels, \(C'=\sigma D_3\). Thus radial coercivity bounds \(\|D_3\|^2\ge v_D\). The identities \(D_3=BD_2\), \(D_2=AD_1\) and action bounds give exactly

\[
\|D_2\|^2\ge v_D/U^2,\qquad
\|D_1\|^2\ge v_D/U^4.
\]

The contrast-root sign transformation leaves the common fields and the trained actions unchanged and flips each contrast field. It gives \(ED_\ell=E[M_\ell D_\ell]=0\), so these norm bounds are variance bounds.

For same labels, the supporting proof does more than invoke root independence. The finite affine training system is measurable with respect to the common root and the two initial matrices, whereas the contrast root is independent Gaussian. For a learned difference \(T_n\) of bounded ordinary Frobenius norm,

\[
E[\|T_nD_0\|_n^2\mid\mathscr F_n]
=v_D\|T_n\|_F^2/n\longrightarrow0.
\]

The corresponding conditional pairing calculation proves zero common/contrast covariance. Fixed-program passage and affine strong Euler convergence then freeze each population contrast. This is valid at \(\rho=-1\), where the common first root is zero. It does not incorrectly infer negligible contrast action from HS boundedness alone.

The common bound \(m^2=\delta/(2U^4)\) consequently holds in all layers and both sectors. Forward propagation gives the three bounds \(U,2U^2,3U^3=L\). Affine Gaussianity follows from the finite scalar recursion, which uses affine coordinate maps and deterministic contractions, followed by strong Euler convergence. Hence every relevant marginal lies in the parameter rectangle \(|\mu|\le L, m\le\sigma\le L\).

This rectangle is a nonempty compact subset of positive-variance Gaussian parameters. The regression formula (13) is continuous there by common-Gaussian \(L^2\) coupling and the denominator bound \(m^2\). At every point the regression error is strictly positive: a zero error would make arctangent affine on a full-support Gaussian law and then, by continuity, on all of \(\mathbb R\). Therefore the minimum \(\eta\) is attained and positive. This is an actual uniform margin, rather than an unjustified infimum over individually positive errors on varying trajectories.

The quantitative transfer also has the correct constants. Centering is an orthogonal projection, so the standard deviation can decrease by at most \(t=\|Z-Z_0\|_2\). If \(t\le m/2\), the regression slope for \(Z\) has magnitude at most \((\pi/2)/(m/2)=\pi/m\). Its affine predictor, reused for \(Z_0\), gives (16) by the triangle inequality and the 1-Lipschitz property of arctangent. This reasoning needs no Gaussian hypothesis on the perturbed \(Z\).

## 4. Response interface and all constants in the coefficient selection

The source baseline's population-to-finite conversion applies with \(B_0=2U\). The finite initial action bounds and the unrolled rank-one updates give upper bounds \(10+2S_\delta B_0^3\) and \(10+3S_\delta B_0^3\), while first-projection and readout norms converge at fixed meshes. Thus

\[
p=11+2U+4S_\delta(2U)^3
\]

has the required strict slack. A bounded affine flow supplies the \(2U\) Euler bound for sufficiently fine meshes by its explicit local defect estimate. No uniform-in-dataset probability limit is needed.

The response lemma's constants \(A_0,M_0\) in candidate lines 185–186 match its equation (4), including the extra factor 2 for the sum of block row norms. In equation (65) of that lemma, substituting \(B=p\), \(b=2p\), \(S=S_\delta\) gives

\[
\frac{B}{60b^3S e^{9b^2S}}
=\frac1{480p^2S_\delta e^{36p^2S_\delta}},
\]

as asserted in \(R\).

I checked the dependence of the remaining \(K\). The primal/source variance bounds use only the specified bound and duration; the coefficient-prefix moment estimates use \(A_0+1,M_0+1\); the exponential envelope retains its current-coordinate factor; its integrability uses weighted sums in time, not a random maximum over source coordinates. The four-stage construction bounds current \(a^2,a^3,b^3,b^2\) successively. In particular it does not assume the new backward row to prove that row's own bound. The only input-geometry norm needed is \(\|\Gamma\operatorname{diag}(y/2)\|_{\infty\to\infty}\le1\). No lower covariance eigenvalue, angle-specific compactness choice, dimension, or horizon enters this \(K\).

For the direct raw comparison, the bridge's same-state component differences are bounded by \(7,14,11,6\) times \(eb^3\); their sum is \(38eb^3\le40eb^3\). Its affine Lipschitz component constants sum to \(9b^2\). These estimates remain valid for first-field raw differences and matrix HS differences. Gronwall therefore gives the candidate's \(Q=40b^3S_\delta e^{9b^2S_\delta}\).

The forward size bounds \(4b,7b^2,10b^3\) are valid for \(b\ge1\) and \(e\le1\). The displayed second-layer expansion is bounded by \(5bE+(\pi/2)be\). The third-layer expansion is bounded by \(12b^2E+\pi b^2e\). This last bound also dominates the corresponding lower-layer bounds, giving exactly \(J=12b^2Q+\pi b^2\). Cauchy–Schwarz then gives \(O=10b^3Q+b(J+\pi/2)\) for the prediction difference. There is no missing factor from the two samples because their absolute projected-label coefficients sum to one.

Every entry in the minimum (19) is strictly positive and depends only on \(\delta\). Its extra factor \(1/2\) gives stronger slack than is used:

\[
Qe\le b/8,\qquad Oe\le1/8,\qquad
Je\le m/4,\qquad
Je\le\frac{\sqrt\eta}{4(1+\pi/m)}.
\]

The nonlinear flow consequently cannot leave the comparison ball; sufficiently fine nonlinear Euler prefixes have the same slack relative to their affine prefixes. The endpoint satisfies \(g_{e,R}(S)\ge11/8>5/4\), and the nonaffinity transfer is valid. Absorbing (1+Z) and rescaling the free affine coefficients proves the exact identity \(e^2\mathcal R(Z)\), yielding (22).

## 5. Cap removal, global time, uniqueness and exact finite dynamics

The response estimates are for the actual canonical nonlinear inputs \(C,q^2,q^1\), uniformly in cap and the admitted meshes. Their \(L^q\) bounds yield the Gaussian \(L^2\) tails required by the bridge. At fixed cap, bounded primal states and locally Lipschitz coordinate maps provide strong flows and Euler convergence. Hence the tail estimates pass to those flows.

The asymmetric cap identity retains the linear incoming-query difference and clips only the nonlinear part. On a bounded primal ball, its Lipschitz loss is linear in (1+eR); sequential backward substitution does not multiply three powers of \(R\). Only the reference requires a tail estimate. Therefore the quadratic tail exponent dominates the Gronwall factor, giving strong cap convergence of states, HS increments and raw directions and identifying an uncut autonomous strong gradient path through \(S\).

The inherited sample symmetry and endpoint margin give a first \(s_*<S\) with \(g=1\). The nonlinear initial kernel is positive in both sectors: the initial uncentered feature Gram calculation preserves strictly positive contrast at \(\rho=-1\), and the constant activation shift preserves the common sector. Radial coercivity is applied only after the uncut strong gradient path exists. Its strong chain rule is available; no global Fréchet differentiability assertion for the feature-valued Nemytskii map is needed.

Since (g') is continuous and bounded through \(s_*\), \(1-g(s)\le M(s_*-s)\). The physical-clock integral therefore diverges at \(s_*\). One feature path gives every finite physical horizon. Its nonaffinity bound on all of ([0,S]) persists on every such horizon without further shrinking \(e\).

The finite comparison uses the actual two residuals throughout. The finite systems do not use the population scalar clock. Fixed-cap finite identification proceeds by width first at a fixed finite program, then deterministic Euler estimates on a common bounded primal ball. The finite matrix bounds follow from initial norms and unrolled update lengths; trained matrix operator-norm convergence across widths is not assumed.

For the uncut finite systems, same-width comparison against a capped physical reference yields \(C_T\exp(C_TR-cR^2)\). For exact raw GD, evaluating its raw direction at the preceding node adds only \(C_{R,T}\eta_n\). Thus \(\eta_n=n^{-2}\) is covered without Gaussian identification for a growing transcript. All cap-dependent constants are fixed before the width limit. The final removal of \(R\) works for every fixed \(T\) and does not impose another smallness condition on \(e\).

The same reference-only asymmetric estimate applies to arbitrary bounded-primal strong competitors, including nonsymmetric competitors, and at a reached starting time. Gaussian decay absorbs the added linear-in-\(R\) Gronwall factor on every compact interval. This proves the asserted uniqueness and reached-state restart. It does not silently assert local existence from arbitrary states of the full \(L^2\) space.

## 6. Observable topology and nontriviality

The fixed-cap velocity bridge checks the coordinate-class issue explicitly. It does not apply the bounded-derivative fixed-program theorem directly to the unbounded-derivative product \(\phi'(Z)P\). It first truncates \(P\), identifies the two appended forward queries including their response rows, and removes the truncations by \(L^2\) estimates and expected-derivative domination. Its source-row and moment arguments use only bounded \(L^2\) actions, never an unsupported \(L^p\to L^p\) action bound.

The deterministic velocity comparison (33) costs a single truncation factor \(M\), plus reference preactivation-velocity tails. For removal of the training cap, population cap states and raw directions converge first. The uncut hidden velocities are continuous \(L^2\) paths and thus have compact time image with uniformly vanishing \(L^2\) tails. Fixing \(M\), removing the cap, then removing \(M\) proves convergence of population cap velocities. In the finite comparison the order is width first at fixed cap and \(M\), then cap removal at fixed \(M\), then \(M\to\infty\). This avoids any assumption that fixed-cap moment constants grow slowly in the cap.

These comparisons give uniform-in-time same-layer joint \(\mathcal W_2\) laws including both samples and velocities, and joint laws at any fixed finite collection of times. Strong \(L^2\) convergence controls all four kernel blocks and their off-diagonal entries. The raw-GD right-node and terminal-left direction conventions are preserved.

For the stronger path-space claim, the interpolation estimate

\[
\|x-I_hx\|_\infty^2\le4h\int_0^T|x'(t)|^2dt
\]

gives an empirical and population \(\mathcal W_2\) coupling bound. Bounded primal states and raw directions bound the integrated recomputed hidden speeds. At a fixed observation mesh the joint-node laws converge; subsequently taking the observation mesh to zero proves \(\mathcal W_2(C([0,T];\mathbb R^4))\) with the supremum norm. Thus the stated topology is not inferred merely from pointwise weak convergence. Uniform velocity second-moment convergence also gives integrated squared-speed convergence.

Finally, the initial-motion lemma applies for every fixed positive \(e\). The top feature Gram remains positive definite at the antipodal input because \(\phi(Z)=1+\psi(Z)\) and \(\phi(-Z)=1-\psi(Z)\) are linearly independent. The upper preactivation pairs consequently have full Gaussian support. The nonconstant derivative for \(e>0\) makes the top backward Gram positive definite. Each reused transpose retains a Gaussian source with the full input second-moment covariance and its response correction. These yield positive hidden matrix-block HS norms, positive first-block raw norm without an input-Gram inverse, and nonzero sample feature accelerations in every layer. Symmetry upgrades positivity of the sum of sample contributions to each sample where needed.

The strong initial expansions need only the constructed \(C^1\) path and bounded continuous gates. They give

\[
\kappa(s)=\kappa(0)+2s^2\|V\|_{\rm hidden}^2+o(s^2),
\qquad \|V\|_{\rm hidden}>0.
\]

Since \(s(t)=2t+o(t)\), the certificate applies in physical time. The theorem correctly confines this to initial acceleration and small-time kernel change; it does not claim perpetual nonzero velocity.

## Corrections and final logical extent

**Required corrections:** none.

**Optional corrections:** none needed for mathematical validity or the claimed quantifiers. The recursive finite constant \(K\) in the response interface is sufficient for an existence threshold; an optimized numerical coefficient is not a premise of this theorem.

The established order is

\[
\forall\delta\in(0,2]\ \exists e_\delta>0\quad
\forall e\in(0,e_\delta]\quad
\forall\text{ fixed admissible }(d,x_1,x_2,y_1,y_2)\quad
\forall T<\infty.
\]

All new uniformity claims and all downstream conclusions survive the adversarial checks above. No no-go counterexample, missing supremum/minimum argument, circular continuation step, or open dependency premise was found. **PASS for the complete stated extension.**
