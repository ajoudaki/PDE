# Final independent supersolution and complete-theorem audit

Date: 2026-09-07.

**Verdict: PASS for the final candidate hashes recorded below. No mathematical blocker remains.** The four mathematical files together establish the complete original two-input theorem for \(1/2\le a\le1\) and \(0<e\le c_{\rm poly}\delta^{10}\), with the same explicit numerical prefactor as the exponent-800 result.

## Scope and independence

I read CONTRACT.md, both hash manifests, and all four candidate mathematical files in full. I applied the solve-math-rigorously skill. I did not read README/status/evidence files, sibling or historical reviews, or NORMALIZED_GATES_AND_PRIMALS.md. That excluded auxiliary file is not a premise. I performed no trajectory experiment, delegation, proof edit, or commit. Hash computation and read-only source inspection are the only computational checks.

I read the original theorem's PROOF.md, AFFINE_CORE.md, SOURCE_AND_LIMIT_BRIDGE.md, and INITIAL_MOTION_AND_NORMALIZATION.md in full; the quantitative PROOF.md and AFFINE_POLYNOMIAL_BOUNDS.md; the positive-scaling and source-response argument in POLYNOMIAL_RESPONSE_LEMMA.md; the original TWO_SAMPLE_SOURCE_BASELINE.md; the conditioning, singular-query and common-action portions of L3_LOCAL_COMPLETE_PROOF.md; the original primal comparison and continuation bridge; the fixed-cap velocity bridge; and the necessary original nonlinear learned-moment comparison. Every entry of both hash manifests was independently checked, including dependencies not needed as separate premises.

Two presentation issues found during this audit were reported to the assembler and corrected there: the missing additive sign in main equation (8), and the overly broad assertion that backward strict densities persist under arbitrary backward row errors. I inspected the corrections and recomputed the final hashes. The final response proof explicitly uses only backward row bounds on that box. The main source display's local field notation was also changed from H to h. These corrections change neither the supersolution nor the numerical conclusion.

## 1. Exact target and unchanged dynamics: PASS

The candidate retains deterministic RMS-unit inputs, all binary labels, the two-sided condition \(|\rho|\le1-\delta\), all three hidden layers, the original independent Gaussian initial matrices and finite readout, the raw metric, and simultaneous raw GD with step \(n^{-2}\). The auxiliary change \(t=\lambda s\) is converted back to the original feature-time mesh before closure; it does not rescale the optimizer.

Label folding is exact by oddness and the even derivative. Both label sectors have folded controls \((1/2,1/2)\) and active variance \(v=(1+y_1y_2\rho)/2\). The actual endpoint scale satisfies
\[
M^4=\frac{3}{\sqrt2\,a^3\sqrt v},\qquad
M>1,\qquad S\le2/\lambda\le M^4,\qquad
M\le24^{1/4}\delta^{-1/8}.
\]
The proof distinguishes M from its dataset-uniform upper envelope. It does not substitute that envelope into \(\sqrt v\asymp M^{-4}\).

Since \(c_{\rm poly}\le c_*\) and \(\delta^{10}\le\delta^{7/4}\), the original quantitative primal tube, endpoint and absolute Gaussian-regression conditions hold. This applies the original estimates' proofs, not the exponent-800 theorem at an unsupported amplitude.

## 2. Affine source certificate and numerical inputs: PASS

The normalization in AFFINE_SOURCE_CERTIFICATE.md §§2–3 retains every gain and variance factor. Learned coefficients acquire exactly \(\Delta t_j=\lambda h_j\), while initialized-matrix returns acquire \(\beta^2\). Inactive freezing and Gaussianity follow from the canonical finite-array conditional argument in AFFINE_CORE.md; no assertion that arbitrary bounded actions preserve independence or tails is used.

The affine balances and integrated radius-one Hessian bound give propagator \(CM^5\). Enlarged beta paths exist on the same original interval because their time dilation fits inside the explicit extension \(1/(1000(200+M^2))\). Strong Euler approximation supplies margins at sufficiently fine fixed meshes.

The actual additive independent Gaussian probes identify each required formal source transfer by the original finite-difference identity. Width identification is at fixed program and probe amplitude; amplitude then tends to zero. Current direct identities are retained for \(R_1,R,L,R_3,L_3\). The top backward-answer probe identifies \(R_3A_3\), rather than replacing it by an unproved positivity shortcut. Both action orientations are present.

Conversion to original time gives the safe coefficient powers \(5,7,9,11\), all required resolvent rows, and top strict-transfer power 9. The numerical input ledger is sufficient: primary size \(100M\), propagator \(4e^{1410}M^5\), injection/output costs at most \(3(100M)^2\), beta derivative factor at most \(3\cdot10^7M^2\), and the displayed gain/sample conversions are dominated by \(10^{25}e^{1410}<H\). Later products correctly pay additional powers of H.

## 3. Actual deterministic sample-sector symmetry: PASS

The reduction concerns deterministic expected coefficients. At fixed cap and mesh, simultaneous sample interchange preserves the roots, Gaussian covariances, coordinate program and scalar readout. The chain rule conjugates every formal derivative block by the interchange matrix, with arrays and covariances frozen. Expectation and chronological construction preserve this invariance, so every actual deterministic coefficient block is diagonal in the mean/contrast basis.

Individual random gates can mix those sectors. REFINED_RESPONSE.md retains their full two-by-two action in all moment and derivative bounds. Only after obtaining deterministic coefficient defects are the scalar temporal comparisons used. Arbitrary externally forced off-diagonal sample blocks are not needed. Nonsymmetric physical competitors are handled by the independent asymmetric comparison.

## 4. Beta positivity and scale slack: PASS

At fixed affine mesh, active raw-coordinate expansions use additions, products and positive step sizes. Wick contractions contribute nonnegative variance weights. Hence active learned moments and chronological coefficients are polynomials in beta with nonnegative coefficients.

The scaled equation is exactly
\[
\mathcal C_\beta=\beta^2\mathcal T_0(\mathcal C_\beta)+\mathcal M_\beta.
\]
Differentiation retains
\[
A'_{3,\beta}\ge\beta^2a^2R_\beta A'_{2,\beta}L_\beta
\ge2\beta^3a^2R_\beta F_\beta L_\beta.
\]
Convexity gives \(f'(\beta)\le f(b)/(b-\beta)\). The explicit beta gaps of order \(M^{-2}\), the affine A3 bound, and \(R,L\ge I\) therefore give
\[
|F_\beta L_\beta|_d,\ |R_\beta F_\beta|_d\le H^3M^9.
\]
This does not multiply two crude resolvent norms.

The safe lower entries \(F_{kj},V_{kj}\ge H^{-2}M^{-8}h_j\) hold. The main text's stronger \(H^{-1}\) lower bound also follows from the exact gain/variance constants and the size of H. Integrating the beta derivative gives the active inner/outer gap \(H^{-3}M^{-10}h_j\). It is strict on every fixed positive mesh without a minimum-step assumption.

## 5. Exact active supersolution and signed comparison: PASS

For arbitrary nonnegative causal row errors \(J_3,J_2\), the construction
\[
B_3^*=B_{3,\beta}+J_3,\qquad
B_2^*=B_{2,\beta}+W^*-W_\beta+J_2
\]
dominates both backward equations exactly. Enlarged-beta learned moments dominate unit-beta learned moments.

The noncommuting temporal identities have the correct order:
\[
R^*=(I-V_\beta J_3)^{-1}R_\beta,\qquad
W^*-W_\beta=a^2L_\beta J_3R^*.
\]
Consequently
\[
F_\beta(B_2^*-B_{2,\beta})F_\beta
=F_\beta J_2F_\beta+
a^2(F_\beta L_\beta)J_3(R^*F_\beta).
\]
The strict/row/strict sandwich bound retains \(h_j\), including when a J has a current diagonal or is concentrated on a very small past step.

Division by the positive leading entry yields \(\eta\le H^{11}M^{30}q\). Positive left multiplication proves inductively
\[
(F_\beta D_B)^nF_\beta\le\eta^nF_\beta,
\]
justifying the entrywise geometric comparison. The V sandwich costs \(M^{26}q\). Direct strict forcing and both forward errors fit within \(\beta^2-1\gtrsim H^{-1}M^{-2}\) under \(q\le H^{-16}M^{-32}\).

The inverses are finite causal polynomials, so
\[
|\mathcal T_0(\mathcal C)|\le\mathcal T_0(|\mathcal C|)
\]
for signed actual coefficients. The actual chronological order A2, A3, B3, B2 resolves all dependencies, including B2's current dependence on the already constructed B3 block. Finite induction supplies the claimed comparison; no unsupported implicit fixed-point argument is used.

## 6. Inactive sector and two-scale first exit: PASS

In the affine inactive sector K3 and both backward coefficients/moments vanish. The explicit forced majorant takes \(B_3^*=J_3\), \(B_2^*=a^2J_3R^*+J_2\). Its forward additions have density \(O((1+S)q)\), and backward rows are \(O(q)\). Numerically \(u=H^3M^4q\), \(w=H^5M^4q\) suffice. As explicitly specified in the note, the forward assertion is an absolute-value majorant, not two-sided closeness inferred from one-sided domination.

On the outer box, forward transfer densities and causal row bounds persist by the exact resolvent identities. Backward strict densities are neither supplied nor needed. Inactive Neumann ratios are smaller. Individual versus summed backward radii do not create a loss: together the two excesses are at most \(2H^{-12}M^{-12}<r_0/2\).

The strengthened criterion
\[
q\le H^{-16}M^{-34},\qquad r_0=H^{-10}M^{-12}
\]
puts backward rows strictly inside the outer radius. Active forward bounds lie below beta-out by the explicit gap; inactive additions lie below the fixed density margin. Source coefficients depend continuously on amplitude at fixed cap and mesh, including singular covariance cases by the original finite construction. The affine start is interior. Thus first exit is contradicted on the closed box, uniformly in cap and sufficiently fine mesh.

## 7. Nonlinear gates, moments, current returns and forcing: PASS

The source Gaussian scales \(1,M^2,M,M,M^2\) follow independently from primal L2 bounds. Exact same-array resolvents in the value equations give incoming Lp powers \(22,21,17\) for \(q^1,q^2,C\), with prefactor \(H^{10}\), after absorption. These are deterministic sums of Lp norms, not random time suprema or unsupported Lp bounds for arbitrary bounded actions.

With all arrays and covariances frozen, put
\[
P=L_{\rm gate}+a\Delta V B+aB\Delta G+\Delta V B\Delta G.
\]
Direct subtraction gives the exact equations
\[
J-J_{\rm aff}=U[\Delta V I^\zeta+PJ],\qquad
D\delta-D\delta_{\rm aff}=L[\Delta V I^\zeta+PJ].
\]
The second follows by substituting the first into the output difference and using \(L=I+a^2BU\). It justifies the improved backward power count.

All feedback in J passes through a strict U kernel. A single transpose-source derivative vanishes through its source time and retains its initial \(h_j\) factor. A complete forward-source row retains its current identity. The causal product bound produces an exponential with rate proportional to e and deterministic weights \(h_r(Q_r+M^b)\). Its stochastic integrated powers are \(31,32,30\); its deterministic powers are \(20,20,17\). Weighted Jensen and the proved subGaussian moments control the required fixed moments under \(eH^{22}M^{32}\le1\), with arbitrary time correlations.

Complete backward rows include current returns. In particular the current B2 equation retains propagation through the current B3 block. In the exact L identity, the current identity of L retains the terminal \(Q_k\) factor; Hölder controls it with the envelope.

The forward density defects have powers \(36,39\), and backward row defects have powers \(43,39\). The largest is \(eM^{11}M^{11}M^{21}\). Independent learned-moment errors cost \(eM^{15}h_j\), or \(eM^{19}\) after row summation. The numerical ledger dominates all these products, so the complete forcing is
\[
q\le H^{30}eM^{43}.
\]

## 8. Explicit prefactor and exponent arithmetic: PASS

H is exactly the original \(C_B\), and \(24^{20}<H\). Thus
\[
e\le c_{\rm poly}\delta^{10}
\quad\Longrightarrow\quad
eM^{80}\le10^{-70}H^{-399}.
\]
Consequently
\[
eH^{22}M^{32}\le10^{-70}H^{-377}<1,\qquad
qM^{34}\le H^{30}eM^{77}\le10^{-70}H^{-369}<H^{-16}.
\]
The forward closure costs 32 powers and the complete backward outer margin costs 34. The combined forcing/closure exponent is \(43+34=77<80\). The original primal/nonaffinity condition is already implied. No unspecified constant is used to enlarge the numerical prefactor.

## 9. Complete original theorem and limit conclusions: PASS

The candidate supplies exactly the three downstream premises: bounded cap-uniform primal paths, cap/mesh-uniform subGaussian incoming fields, and endpoint prediction exceeding one.

The asymmetric cap estimate uses reference tails and a stability exponent linear in the cap. Gaussian decay removes the cap with strong raw-state and direction convergence. The first-hit clock diverges for both capped and uncut references; capped prediction monotonicity is not assumed. The resulting autonomous physical flow is global. The original radial lower bound also retains the original loss decay estimate.

Physical comparison retains both actual residuals and requires neither symmetry nor tails of the bounded-primal strong competitor. Uniqueness on the same canonical spaces and restart from reached states therefore remain valid.

Finite identification takes width at fixed cap and auxiliary mesh. Deterministic Euler estimates remove the mesh and compare actual raw GD with error \(C_{R,T}n^{-2}\). The finite initialized readout is retained. No source theorem is applied to a growing transcript, and trained operator-norm convergence is not assumed.

The fixed-cap velocity proof uses truncated product queries. For cap removal it first fixes the reference-velocity truncation, then sends the cap to infinity, then removes the truncation using the compact L2 time image of the uncut velocity. This retains uniform-time and finite-time joint same-layer velocity laws, second moments, squared speeds and integrated squared speeds. The path interpolation estimate gives the required same-layer path-space W2 laws. All four raw kernels, off-diagonal entries, both action orientations and actual adjoints on generated probes remain covered.

The absolute regression margin survives strong limits and is multiplied by \(e^2>0\). The original odd-family motion argument uses positive initial Grams and full reused-transpose second-moment covariances. It applies to every positive e in the rectangle without another angle-dependent threshold, retaining nonzero hidden-block and every sample/layer acceleration, readout motion and projected kernel change.

The original Gaussian-unit-energy family also remains covered by its coefficient conversion into this rectangle. There is no claim of trained variance conservation.

The convergence quantifiers remain: each fixed dataset, each fixed finite physical interval, and the full width sequence. There is no uniformity over datasets or the infinite time half-line, no three-input extension, no arbitrary-state restart, and no reduction of the original observable scope.

## Verified final SHA-256 hashes

Candidate paths are relative to this directory:

```text
37b9e8a27135b95b8dffe05fe2b734229fadedc98bc1609259e365dbb2aeba37  PROOF.md
bc55c0f8e25de1f3a4316fe36e86afa25c9486e014192f2eb818358909b048eb  AFFINE_SOURCE_CERTIFICATE.md
3622a0f903cd51b712d1d524a140d834471b5eb588611f059535c41f6efd2332  REFINED_RESPONSE.md
e2be183521919ce69c7ae41b81f5cd78566c5430a78c2408687f52f1b6d86774  POSITIVE_SUPERSOLUTION.md
```

Dependency paths are relative to the parent directory. All 19 entries match:

```text
a4d6ed0ee99a1e111b5eba068f2219cf561a2281b1828b26227aca7a0a54a050  two_sample_odd_activation_theorem/PROOF.md
634dd3bbc35436e9d1760bee5c11cbf2124b3c42e8920a1bf3a4fcbb15039711  two_sample_odd_activation_theorem/AFFINE_CORE.md
2a140f2a5a39f911b5c2ca51bc79102d20e9209f1450d38005360c88103f6e77  two_sample_odd_activation_theorem/SOURCE_AND_LIMIT_BRIDGE.md
c96316fdc481ef3f9e6fc402514ca9b45bcff12e199023505fbbb86d4e15bf24  two_sample_odd_activation_theorem/INITIAL_MOTION_AND_NORMALIZATION.md
27b2579f27ec14319dd39a93a4942d7b6463860648462d5ccb31b662c7725b75  two_sample_odd_activation_theorem/sources/ANGLE_SPECIFIC_THEOREM_ASSEMBLY.md
e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd  two_sample_odd_activation_theorem/sources/CONTRACT.md
a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0  two_sample_odd_activation_theorem/sources/FIXED_CAP_VELOCITY_BRIDGE.md
bd81de0a7ad0cb9bdd1f27f89961f4a3b7a7da6914456ae08596a882fa2ec351  two_sample_odd_activation_theorem/sources/INITIAL_FEATURE_LEARNING.md
f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4  two_sample_odd_activation_theorem/sources/L3_LOCAL_COMPLETE_PROOF.md
ef0ea077406a27307bc84e045feebf5099f6f81883bdfed41508035fe4559568  two_sample_odd_activation_theorem/sources/NONLINEAR_RESPONSE_PERTURBATION.md
2891b892667396d64bd747689bcd59aa7ca3ffd224d3579fc3407bca0b623f9a  two_sample_odd_activation_theorem/sources/PREVIOUS_TWO_SAMPLE_PROOF.md
99eb60a64df1bbf4d8b70f351198abced9ef7eaeacf9b39c3997da5700a8f066  two_sample_odd_activation_theorem/sources/PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md
40882fc19e44b4b9245156595bb1071bd4de6007d619fada54c9fce7c37903f4  two_sample_odd_activation_theorem/sources/SYMMETRY_RADIAL_CLOCK.md
49da0f68047b4f516d3ad3c94b7112259838bcebf68e2296a948364232842789  two_sample_odd_activation_theorem/sources/THREE_SAMPLE_CONTROLLED_RESPONSE_LEMMA.md
a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f  two_sample_odd_activation_theorem/sources/TWO_SAMPLE_SOURCE_BASELINE.md
0a7dbd32cb9cc291e706813b59c0142394e6f9532244e52c21a5ab5d89ed4d02  two_sample_odd_activation_quantitative/PROOF.md
8387e2f253063c139dacb282ca9f2372478521f54b33a9ef6c8dbd83f2b521ca  two_sample_odd_activation_quantitative/AFFINE_POLYNOMIAL_BOUNDS.md
51b0f717b33ed618219e086d32b16a95ef4253892171597d1805dd9d37a64f7f  two_sample_odd_activation_quantitative/POLYNOMIAL_RESPONSE_LEMMA.md
c63753a83e832793c886b8ae8c122e30e0c01864b86a1a5dc9bee030852f9210  two_sample_odd_activation_quantitative/OLD_THRESHOLD_AND_NONAFFINITY.md
```

**Final decision: PASS.** This is a complete-theorem verdict on the recorded final candidate, not merely a conditional supersolution verdict.

