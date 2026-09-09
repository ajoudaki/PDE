# Independent complete-proof audit: PASS

Date: 2026-09-07. Reviewer: `/root/ten_final_affine`.

Verdict: **PASS for the complete theorem at the four hashes below.** I found no remaining mathematical blocker. The certificate concerns the full condition `0<e<=c_poly delta^10`, with the unchanged explicit old prefactor, all gains `a in [1/2,1]`, all binary labels, and the original population/GF/raw-GD and observable conclusions. It is not merely a pass for a conditional affine lemma.

## 1. Independence, file identity, and scope

I read CONTRACT.md, CANDIDATE_HASHES.json, DEPENDENCY_HASHES.json, and the rigorous-math skill. I read all four candidate mathematical files in full. I did not use README, review status, evidence ledgers, historical or sibling reviews, or NORMALIZED_GATES_AND_PRIMALS.md. I ran no trajectory experiment, delegated no work, edited no proof, and made no commit.

Two changes were communicated during this audit: restoration of the printed addition in main equation (8), and qualification of the response outer-box assertion to exclude backward strict-density bounds. I independently re-read both resulting files in full and verified the final hashes. This verdict is attached only to the final versions:

| File | Verified SHA-256 |
|---|---|
| PROOF.md | `37b9e8a27135b95b8dffe05fe2b734229fadedc98bc1609259e365dbb2aeba37` |
| AFFINE_SOURCE_CERTIFICATE.md | `bc55c0f8e25de1f3a4316fe36e86afa25c9486e014192f2eb818358909b048eb` |
| REFINED_RESPONSE.md | `3622a0f903cd51b712d1d524a140d834471b5eb588611f059535c41f6efd2332` |
| POSITIVE_SUPERSOLUTION.md | `e2be183521919ce69c7ae41b81f5cd78566c5430a78c2408687f52f1b6d86774` |

I verified every one of the 19 dependency hashes, not just the four candidate hashes. Substantive dependency inspection included the original PROOF, AFFINE_CORE, SOURCE_AND_LIMIT_BRIDGE, INITIAL_MOTION_AND_NORMALIZATION, quantitative PROOF, AFFINE_POLYNOMIAL_BOUNDS, and POLYNOMIAL_RESPONSE_LEMMA in full; the original TWO_SAMPLE_SOURCE_BASELINE in full; the generic Gaussian conditioning/singular-query/common-action portions of L3_LOCAL_COMPLETE_PROOF; and the hypotheses, product-query justification, deterministic velocity comparison, strong-continuity, and finite-width portions of FIXED_CAP_VELOCITY_BRIDGE. Historical headers inside mathematical dependencies were not treated as premises.

## 2. Exact normalization and intrinsic scale: PASS

I checked the sample and time changes against the original raw source and update equations. Write `m` for the affine certificate's intrinsic scale and `M_delta` for its uniform upper envelope. Then

\[
\lambda=a^3r,\quad m^4=3/(\sqrt2\lambda),\quad
r={3\over\sqrt2a^3}m^{-4},\quad
m\le24^{1/4}\delta^{-1/8}.
\]

The last inequality is an upper envelope; the proof uses the exact preceding equality whenever it replaces powers of `r`. No step requires `r` comparable to a power of `M_delta`. Main PROOF and the other two companions use `M=m`; this translation is explicit.

For `Q=(1/2)[[1,1],[1,-1]]`, `Q^{-1}=2Q`, and `S0=diag(r,r_-)`, the transformed raw first update has coefficient

\[
S_0^{-1}S_0^2(a^3rS_0^{-1})/\lambda=I.
\]

The two matrix updates each have sector multiplier `(a^2r/s_i)(a s_i)/lambda=1`, and the readout update has `a^3r/lambda=1`. Thus the normalized ascent system is precisely the original raw system in different coordinates. It does not change the optimizer or first-layer metric.

The four coefficient transformations in affine equation (5) follow from the field transformations and agree with transformation of the actual frozen source derivatives. The learned-memory factor is also correct: `Q^{-1}=2Q^T` turns `(h_j/2)E[H_k H_j^T]` into `h_j E[(QH_k)(QH_j)^T]`; subsequent field and coefficient scaling gives `Delta t_j`, not a missing factor two.

At initialization scale beta, each initial-matrix return has the factor `beta^2`; the integration operators have no beta dependence. The exact affine source equation is the additive equation `C_beta=beta^2 T0(C_beta)+M_beta`. Inactive normalized entries are

\[
F_-=H,\quad A_{2,-}=2\beta^2H,\quad
V_-=2\beta^2H,\quad A_{3,-}=3\beta^4H.
\]

Their backward coefficients vanish. These formulas agree with the frozen inactive canonical Gaussian fields and remain regular if either sample-sector variance is small but positive.

## 3. Actual frozen formal derivatives and all added probes: PASS

The source bounds are connected to raw stability by a valid independent-root identity. They are not inferred directly from the raw tangent norm.

At a fixed finite program, insert a Gaussian root `G` in the population of the chosen instruction and output, using deterministic amplitudes `epsilon alpha_j`. The augmented program satisfies the same Gaussian conditioning hypotheses. After its deterministic contractions and covariance parameters are frozen, all affine coordinate instructions are linear in the roots and named Gaussian sources. Hence

\[
E[G V^\varepsilon]
=\varepsilon\sum_j\alpha_j T_{V,j}(\varepsilon).
\]

Here `T` is the formal transfer of that augmented program. The original source proof establishes independence of the named source innovations from the additional root and continuity of these finite-expression coefficients at zero amplitude, including singular source laws. Deterministic response bounds control the covariance on the left. Width is taken first at fixed mesh and nonzero amplitude, then amplitude tends to zero. The equivalent common-action argument is also available from the quantitative dependency. Neither method differentiates a covariance square root or interchanges a derivative with an uncontrolled width limit.

I checked the two newly required coordinate instructions specifically:

* **First preactivation.** Keep the integrated state separate and add the probe only to its forward query. The frozen equations are `p=xi1+H d1+epsilon alpha G`, `d1=zeta1+B2 p`. Therefore the transfer is exactly `R1=(I-HB2)^{-1}`. Its current term is identity. The pulse changes the A, B, and D updates at cost `C m^2`; future integrated-p output has cost one. This gives normalized row bound `C m^7`.
* **Top backward answer.** Keep D separate and add the probe to `d3=ED+epsilon alpha G`, with `ED=HP_+ x3`, `x3=xi3+A3 d3`. The x3 transfer is `U=(I-A3 HP_+)^{-1}A3`; the d3 transfer is `L3=(I-HP_+ A3)^{-1}`. U is strict and has no current direct output. L3 has current identity. The update injection cost is `C m^2`, while the x3 output cost is `C m^2` and the D output cost is one. These yield `|U|_d<=C m^9` and `|L3|_r<=C m^7` in normalized time.

The existing matrix-answer probes likewise give F, V, T, W and the remaining R/L orientations. Reusing one root with deterministic signs measures absolute expected rows, and a single pulse preserves the source-time step for strict densities. Fixed sample-block norm conversions cost only an absolute factor.

Reflection/evenness of amplitude-dependent parameters is compatible with this argument, but is not being used as a substitute for the finite-program identity. Continuity at zero already suffices. The top transfer is proved by the actual top probe, not by the insufficient inequality `T A3' T<=B3'`.

## 4. Returning to original time and the common numerical H: PASS

In the active sector, the original coefficient multipliers are respectively `r/a`, `ar`, `1/(ar)`, and `a/r`. Strict densities additionally multiply by `lambda=Delta t_j/h_j`; row norms do not. Consequently normalized F/V densities `m^5,m^7` give original densities `C r^2m^5,C r^2m^7`, whereas normalized T/W rows give `C m^5/r,C m^7/r`. These are bounded by the advertised `1,1,m^9,m^11` powers. The inactive original forward densities are bounded by `C r_-^2<=C`. U and the beta-controlled products transform like the relevant strict forward coefficient, giving the advertised sharpened `C m` densities. Baseline resolvent rows transform by diagonal similarity and have unchanged sector bounds.

The geometry dependency proves the normalized integrated radius-one-tube Hessian bound `1404+5 log m`. Its local extension by `1/[1000(200+m^2)]` and homogeneity give the common enlarged family. The scales

\[
b_j=1+{j\over10^6(200+m^2)},\qquad
b_{\rm far}=1+{1\over10^5(200+m^2)}
\]

are within that extension, and for `b<=b3` the remaining room is at least `1/(3*10^7 m^2)`. The beta derivative bound therefore holds uniformly at the inner and outer comparison scales, not only at one. The supersolution companion uses b3 as its third comparison scale; the affine certificate also provides the more distant scale needed to bound its derivative.

The explicit affine ledger is sufficient: component size `100m`, propagator `4 exp(1410)m^5`, injection/output costs at most `3(100m)^2`, fixed norm/Euler margins, beta derivative cost `3*10^7m^2`, and conversion `r^2<=288m^{-8}` leave a coefficient below `10^25 exp(1410)`. This is below the specified old

\[
H=10^{30}(1+C_0+C_z+C_g+e^{1410})^4.
\]

Thus the common coefficient is numerically certified, rather than selected retrospectively as an unspecified large constant. Products used subsequently are correctly charged additional powers of H.

## 5. Positive supersolution and sample sectors: PASS

Exchange equivariance applies to expected formal derivative blocks as well as learned covariance blocks, so every actual deterministic coefficient block is diagonal in the two-sector basis. This does not diagonalize random gates. The nonlinear response argument retains their full action. Physical uniqueness is supplied independently and does not impose symmetry on competing flows.

The active affine polynomial/Wick argument gives nonnegative coefficients and moments under beta scaling. Differentiating the A3 equation yields

\[
A'_{3,\beta}\ge2\beta^3a^2R_\beta F_\beta L_\beta.
\]

The beta gap gives the claimed `H^3 M^9` bounds on `F L` and `R F`. These products are essential: multiplying separate row and density bounds would not supply the stated closure exponent.

For arbitrary backward causal row forcing, including diagonal forcing, the concrete supersolution satisfies both backward inequalities exactly. Its resolvent identities give

\[
W^*-W_\beta=a^2L_\beta J_3R^*,
\]
\[
F_\beta(B_2^*-B_{2,\beta})F_\beta
=F_\beta J_2F_\beta
+a^2(F_\beta L_\beta)J_3(R^*F_\beta).
\]

The sandwich bound `|U Q V|_d<=S |U|_d |Q|_r |V|_d` preserves `h_j` even when forcing concentrates on an arbitrarily small step. Dividing by the positive active leading entries costs at most `H^2 M^8`, yielding relative first-forward error `H^12 M^30 q`. The beta slack is at least `H^{-1}M^{-2}`. Thus `q<=H^{-16}M^{-32}` suffices for forward domination. Reconstruction costs at most `H^4 M^22q` in backward row norm, so `q<=H^{-16}M^{-34}` gives the required strict interior margin for radius `H^{-10}M^{-12}`.

The inactive sector is separately controlled by its explicit triangular supersolution: backward rows are `O(q)` and added forward density is `O(M^4q)`. The numerical choices `u=H^3 M^4q`, `w=H^5 M^4q` suffice. The affine beta gap supplies a strict active forward entrywise margin at each fixed mesh. Chronological comparison in the actual A2/A3/B3/B2 call order is valid; no minimum step or inverse covariance enters.

## 6. Nonlinear same-array response and outer box: PASS

The revised response statement correctly retains only forward strict-density and causal row bounds on the outer box. Arbitrary backward row perturbations need not have bounded strict density. Inspection of the subsequent value, derivative, and forcing estimates shows that they use only backward row bounds. No lost backward-density assertion is needed.

The outer majorants preserve the required F and V densities by Neumann ratios at most `H^{-8}M^{-3}` and `H^{-8}M^{-1}`. R1, R2, L2 use their exact resolvent identities. The top transfers depend only on A3. The inactive top readout projection vanishes; its other inverse ratios are smaller. These facts justify the `H^2` outer envelope.

The primitive Gaussian scales are correctly obtained from raw primal matrix-input norms: first root 1, zeta1 `M^2`, xi2 and zeta2 `M`, xi3 `M^2`. This is not an assumption that bounded canonical L2 actions preserve Lp tails. Solving the actual value equations with their same-array affine resolvents and absorbing e-dependent self terms gives Z powers `11,12,13` and incoming-field powers `22,21,17`. Arbitrary source covariance singularities and time correlations are allowed.

For frozen coefficients and covariances, direct differentiation gives

\[
J-J_{\rm aff}=U(\Delta V I^\zeta+PJ),\qquad
\Delta(D\delta)=L(\Delta V I^\zeta+PJ).
\]

The second identity follows from `Delta(Ddelta)=DeltaV Izeta+PJ+a^2B(J-Jaff)` and `L=I+a^2BU`. It retains the current local multiplier and avoids an extra separately bounded B term.

Strict U gives the causal exponential with stochastic powers `31,32,30` after time integration. Deterministic time weights, weighted Jensen, and subGaussian marginal bounds control its fixed moments under `e H^22 M^32<=1`. There is no random supremum over source times. The single-transpose source factor `h_j` survives. The full forward-source row includes its direct current identity.

Forward derivative defects have powers `36,39`; complete backward row defects have powers `43,39`. In particular the middle backward row costs `M^11*M^11*M^21=M^43`. The diagonal formulas include both the direct middle local term and its return through the top current block. Learned moments contribute density `e M^15` and row norm `e M^19`. The numerical ledger bounds their total by `q<=H^30 e M^43`.

## 7. Amplitude homotopy and exact old prefactor: PASS

The coupled argument has no remaining conditional interface: the response companion proves its bound on precisely the box supplied by the supersolution companion, and both use the affine certificate proved here. At fixed cap and mesh coefficients are continuous in amplitude. At a first exit, the closed-box response bound and positive comparison put every component strictly inside; hence there is no exit. This establishes uniform estimates for all sufficiently fine fixed meshes and caps without a growing-transcript probability assertion.

The final arithmetic is

\[
eM^{80}\le10^{-70}H^{-400}24^{20}
\le10^{-70}H^{-399},
\]
\[
eH^{22}M^{32}\le10^{-70}H^{-377}<1,
\qquad qM^{34}\le H^{30}eM^{77}
\le10^{-70}H^{-369}<H^{-16}.
\]

It uses `M>1` and the correct direction of the upper-envelope inequality. The same `c_poly=min(1/4,c_*,10^{-70}H^{-400})` also implies all old primal, endpoint, and regression restrictions because `delta^10<=delta^{7/4}` on `(0,1]`. No additional angle-dependent threshold remains unverified.

## 8. Complete original conclusion and quantifiers: PASS

The inherited bridges require bounded primal feature paths, cap/mesh-uniform incoming subGaussian bounds, and endpoint prediction exceeding one. All are supplied with the new amplitude condition. The old restrictive source threshold is replaced by the new source proof; it is not invoked as a theorem on an amplitude interval where its hypotheses would fail.

The asymmetric cap estimate has a single linear cap factor in its stability exponent and Gaussian reference tails, so `exp(C(1+eR)S-cR^2)` tends to zero for each fixed dataset. It produces strong raw-state and raw-direction limits. The first-hit clock diverges because the prediction derivative is bounded on the compact feature interval. Capped references need not be gradients or monotone in prediction for this argument. The uncut path is the original autonomous gradient path; the physical comparison retains both individual residuals, proving uniqueness against bounded-primal nonsymmetric competitors and restart from reached states on the same canonical action spaces.

The finite proof takes width at fixed cap and auxiliary mesh, then removes the auxiliary mesh through width-independent fixed-cap Euler estimates, and then removes the cap. The prescribed simultaneous raw GD contributes `C_{R,T} n^{-2}`. Its initialized finite readout is retained and has the correct vanishing population limit. No operator-norm identification across widths or scalar symmetry of finite predictions is inserted.

The original velocity bridge first justifies product queries by smooth truncation. Cap removal fixes a reference-velocity truncation before sending the cap to infinity, then removes that truncation. The uncut velocity is continuous in L2; compactness of its time image gives uniform L2 tails. This proves the stipulated same-layer joint velocity laws, fixed finite collections of times, second moments, and integrated squared speeds. The interpolation inequality and these speed bounds give the original path-space W2 laws. Both samples, all four kernel matrices, initialized/trained action orientations and actual adjoints on generated probes remain within scope.

The original nonaffinity argument uses the absolute affine Gaussian margin and the W2-Lipschitz square-root regression residual. It transfers to at least `e^2 eta_*/4` along the whole feature interval and hence at every finite physical time. Initial motion uses nondegenerate initial two-sample Gaussian support, both full reused-transpose covariance matrices and their formal returns, and sample symmetry. It requires positive e, but no additional small angle-dependent e. All original hidden block/sample/layer motion and projected-kernel-change claims therefore persist. The unit-Gaussian-energy identity-perturbation family is also covered through the unchanged compact gain rectangle.

The theorem is for every fixed realizable two-input dataset with `|rho|<=1-delta`, every gain in `[1/2,1]`, and every fixed finite physical interval, along the full width sequence in probability. It does not assert uniform width convergence over datasets or infinite time, a common positive amplitude for all delta, arbitrary-state restart, a cross-layer neuron pairing, or a three-input extension. These limits and exclusions agree with the original theorem.

## 9. Verified immutable dependency hashes

Paths below are relative to the parent `studies/mean_field_peeling` directory. Every value matches DEPENDENCY_HASHES.json.

```text
two_sample_odd_activation_theorem/PROOF.md a4d6ed0ee99a1e111b5eba068f2219cf561a2281b1828b26227aca7a0a54a050
two_sample_odd_activation_theorem/AFFINE_CORE.md 634dd3bbc35436e9d1760bee5c11cbf2124b3c42e8920a1bf3a4fcbb15039711
two_sample_odd_activation_theorem/SOURCE_AND_LIMIT_BRIDGE.md 2a140f2a5a39f911b5c2ca51bc79102d20e9209f1450d38005360c88103f6e77
two_sample_odd_activation_theorem/INITIAL_MOTION_AND_NORMALIZATION.md c96316fdc481ef3f9e6fc402514ca9b45bcff12e199023505fbbb86d4e15bf24
two_sample_odd_activation_theorem/sources/ANGLE_SPECIFIC_THEOREM_ASSEMBLY.md 27b2579f27ec14319dd39a93a4942d7b6463860648462d5ccb31b662c7725b75
two_sample_odd_activation_theorem/sources/CONTRACT.md e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd
two_sample_odd_activation_theorem/sources/FIXED_CAP_VELOCITY_BRIDGE.md a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0
two_sample_odd_activation_theorem/sources/INITIAL_FEATURE_LEARNING.md bd81de0a7ad0cb9bdd1f27f89961f4a3b7a7da6914456ae08596a882fa2ec351
two_sample_odd_activation_theorem/sources/L3_LOCAL_COMPLETE_PROOF.md f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4
two_sample_odd_activation_theorem/sources/NONLINEAR_RESPONSE_PERTURBATION.md ef0ea077406a27307bc84e045feebf5099f6f81883bdfed41508035fe4559568
two_sample_odd_activation_theorem/sources/PREVIOUS_TWO_SAMPLE_PROOF.md 2891b892667396d64bd747689bcd59aa7ca3ffd224d3579fc3407bca0b623f9a
two_sample_odd_activation_theorem/sources/PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md 99eb60a64df1bbf4d8b70f351198abced9ef7eaeacf9b39c3997da5700a8f066
two_sample_odd_activation_theorem/sources/SYMMETRY_RADIAL_CLOCK.md 40882fc19e44b4b9245156595bb1071bd4de6007d619fada54c9fce7c37903f4
two_sample_odd_activation_theorem/sources/THREE_SAMPLE_CONTROLLED_RESPONSE_LEMMA.md 49da0f68047b4f516d3ad3c94b7112259838bcebf68e2296a948364232842789
two_sample_odd_activation_theorem/sources/TWO_SAMPLE_SOURCE_BASELINE.md a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f
two_sample_odd_activation_quantitative/PROOF.md 0a7dbd32cb9cc291e706813b59c0142394e6f9532244e52c21a5ab5d89ed4d02
two_sample_odd_activation_quantitative/AFFINE_POLYNOMIAL_BOUNDS.md 8387e2f253063c139dacb282ca9f2372478521f54b33a9ef6c8dbd83f2b521ca
two_sample_odd_activation_quantitative/POLYNOMIAL_RESPONSE_LEMMA.md 51b0f717b33ed618219e086d32b16a95ef4253892171597d1805dd9d37a64f7f
two_sample_odd_activation_quantitative/OLD_THRESHOLD_AND_NONAFFINITY.md c63753a83e832793c886b8ae8c122e30e0c01864b86a1a5dc9bee030852f9210
```

No further proof obligation was identified for the stated theorem at the reviewed hashes. Exponent optimality and improving the numerical prefactor are outside this verdict.
