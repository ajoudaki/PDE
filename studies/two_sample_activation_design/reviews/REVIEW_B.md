# Isolated complete-proof review B

Verdict: **PASS for the stated Theorems A and B and the stated initial-motion conclusion.** I found no blocking mathematical error and require no repair. This verdict does not establish a moderate-amplitude global theorem, uniform width convergence over shapes/data/horizons, or one fixed positive amplitude for all separations. The candidate expressly leaves the moderate-amplitude problem open.

Reviewed on 2026-09-08. The reviewed main proof has SHA-256 `c36d92166c65affeb7974c5fe07ddfaa8697399b56d3c4322e89db51a02748ce`. I used the rigorous-math skill. I did not consult previous/sibling reviews, review-status files, README files, research ledgers, preparation notes, or historical temporary research artifacts. No experiment or delegated review was used. I changed no candidate or dependency file. Historical verdict language in mathematical source files was not treated as evidence.

## 1. Exact conclusions and quantifiers

Theorem A quantifies over each fixed `a in [1/2,1]`, each fixed `psi in A`, each admissible fixed dataset, and each positive `e <= c_dyn delta^(31/8)`. The universal coefficient depends on none of those objects. In particular A contains constants and affine functions; the dynamics proof does not need nonaffinity or a lower regression margin. The smallness conditions needed by the proof are all present in `c_dyn`.

Theorem B adds global nonaffinity and its separate shape-dependent coefficient. This dependence is necessary for the displayed uniform quantitative regression margin and is not imported into Theorem A. Every globally nonaffine C2 shape has nonconstant derivative, sufficient for initial hidden acceleration; that qualitative statement needs no additional eta cutoff. Neither theorem asserts nonzero hidden velocity at every later instant.

The finite initialization, raw metric, loss normalization, layer count, readout normalization and actual readout, simultaneous raw GD step, interpolation and node conventions agree with the stated equations. The population state is infinite dimensional, with bounded initialized actions and actual adjoints, and HS learned increments. The observable assertions are per-layer two-sample laws, with joint finite-time correlations and the stated path topology; they do not require pairing neurons from different layers.

## 2. Reconstruction of the symmetry and affine reference

The reflection exchanging the two equal-norm inputs exists because their sum and difference are orthogonal. After absorbing the first label in the readout, the transformation `(w,A,B,C) -> (Q_x w,A,B,tau C)` preserves both the feature objective and raw metric. It maps forward sample slots by P and backward slots by tau P. Its cap equivariance uses oddness of the clipping function, without requiring oddness of the activation. Invariant finite laws and deterministic limiting contractions establish prediction symmetry before uncut uniqueness is used.

I checked the two different sample bases explicitly. With `Q_f=QY`, `Q_b=Q`, the identities `Q_b^T Q_f=Y/2` and `Q_f Gamma (Y/2) Q_b^(-1)=diag(v,1-v)` give all update factors and the normalized equations. The deterministic forward-from-backward and backward-from-forward source blocks are intertwiners. Their typed conjugates are sector diagonal, whereas individual random gate matrices can mix sectors. For opposite labels one must not impose ordinary commutation with P in one common basis; the candidate does not do so. The backward current-return block has the correct type and is retained.

For the affine reference the normalized active problem is exactly gradient ascent of `<D,BAp>`. Its balances control the actions, and the radial identity gives `c >= t` and `F >= c^4/sqrt(2)`. Therefore the first hit of prediction 3/2 occurs before normalized time 2, with `c <= M` and original duration `S <= 2/lambda <= M^4`. Bounded polynomial fields and a strong finite endpoint rule out premature termination. Each dataset is stopped at its own endpoint.

The inactive-field freezing argument uses independence of the initial inactive Gaussian root and bounded Frobenius norms of finite learned increments. Conditional Gaussian estimates give vanishing normalized actions of those increments on the inactive root. This justifies the frozen fields and zero active/inactive covariance. The affine source recursion is linear in centered Gaussian arguments, so the actual affine marginal laws are centered Gaussian.

The variance estimates in SHAPE_SYMMETRY are consistent with the balances. With `R=||D||^2 < 5 v^(-1/4)`, expansion gives upper variances 6, 636, and 66780. The radial readout bound and `||B||^2 <=100+R` give `||Ap||^2 >= max{R(1+R),(100+R)^(-1)} >=1/101`. Including the gain factors yields the common standard-deviation interval `[1/sqrt(404),260]`. Neither endpoint of this interval depends on delta.

## 3. Raw perturbation and the precise exponent

The linear-growth extension is a real additional estimate: bounded shape values are not silently assumed. I checked the successive forward discrepancies `2eb`, `(9/2)eb^2`, `(61/8)eb^3`, the backward discrepancies `eb`, `(9/4)eb^2`, `(61/16)eb^3`, and the four raw forcing terms. Their sum is `375eb^3/16 <40eb^3`. These estimates require only `|psi(z)| <=1+|z|` and bounded first derivative, with the cap bound `|tau_R(q)| <=|q|`.

Only the affine field is differentiated. The raw radius-one tube therefore retains the integrated affine-Hessian estimate and the stated `C0 e lambda^(-3)` comparison. The normalized active first root is controlled by raw first-layer displacement; its bound is not inferred from small unnormalized sample projections. The direct forward expansion fits `Cz e lambda^(-7/2)`, and retaining lambda in the affine prediction comparison fits `Cg e lambda^(-11/4)`. The corresponding entries of `c_dyn` close the tube and preserve the endpoint margin uniformly in cap.

The original-time learned Gram discrepancies are computed directly in typed, unnormalized sample slots. Products with one discrepancy give the largest density `K e M^15 h_j`; summing strict time entries gives `K e M^19`. Thus the proof avoids the invalid inference `e/sqrt(delta) <= C e M^4` for intrinsic M when the inactive variance is small independently of the active variance. No inverse inactive variance is used by the replacement estimate.

The enlarged affine/beta certificate was checked through its actual source probes. The improvement `F >= z^2-100z` implies `(log sqrt(beta^2+z))' >= z-101 beta^2`. Integrating the radius-one Hessian retains coefficient three on the logarithm and gives the M-cubed propagator. The beta extension is only of size proportional to `M^(-2)`, supplied on the common continued interval. The independent Gaussian answer probes measure frozen formal derivatives by taking width at fixed nonzero probe amplitude before taking that amplitude to zero. They retain the single-source time-step factor and allow deterministic signs to measure full absolute rows. This includes the extra first-forward, top-backward, and reverse-top resolvent probes.

Original-time conversion yields active forward densities `M^(-5),M^(-3)`, backward rows `M^9,M^7`, resolvent rows `M^5`, and the strict U/FL/RF bounds needed by the sector argument. The positive beta derivative supplies the product bounds without incorrectly multiplying an arbitrary right row bound into a strict-density bound.

On the resulting box, the new linear-growth value equations have self-coefficients at most the displayed multiples of `e K^6 M^13`, `e K^6 M^11`, and `e K^6 M^8`. Absorption gives incoming Lp bounds with powers 15, 13 and 11 and factor sqrt(p). These prove subGaussian tails; they do not assume that a bounded L2 action preserves such tails.

The exact same-array derivative identities contain the full causal B rows, both gate perturbations, the curvature term, and the current return. Strict U preserves the source-step factor. Weighted Jensen controls the derivative exponential using individual-time subGaussian moments when `e K^22 M^19 <=1`. The subsequent expectation uses actual raw L2 incoming powers 3, 2 and 1. One explicit incoming factor occurs in each insertion, so Cauchy--Schwarz suffices; no unproved stronger raw Lp bound is needed. Forward defects have powers 13 and 11, backward rows 17 and 14, and the learned-moment row power 19 dominates them.

For the sector supersolution I checked the exact forced backward reconstruction and `|U Q V|_d <= S |U|_d |Q|_r |V|_d`. This permits arbitrary current diagonals and no minimum step. Active lower densities cost M^8 and the beta margin costs M^2; together with the M^2 sandwich this gives `q_def <= K^(-16) M^(-12)`. Separate active and inactive row radii are essential and are provided. Signed actual coefficients are bounded by the positive affine majorant; random gates are not diagonalized.

Consequently the complete required inequalities are implied by

`e M^31 <= (1/2) K^(-46)`.

Indeed `q_def <= K^30 e M^19 <= (1/2) K^(-16)M^(-12)` and `e K^22 M^19 <= (1/2) K^(-24)M^(-12)<1`. Since `M^31 <=24^(31/4) delta^(-31/8)`, the source entry of `c_dyn` has the correct direction, exponent and prefactor. Fixed-cap, fixed-mesh amplitude continuity and strict inner margins close the homotopy. No old, stronger amplitude restriction is needed by the mathematical lemmas actually imported here.

## 4. Full construction and every downstream bridge

The finite Gaussian-conditioning proof conditions each matrix on both query orientations. Gaussian projection and integration by parts give the full source derivative correction. Source covariances are full second moments, accommodating nonzero feature means. Independent query regularization and continuity of covariance square roots handle rank drops without convergence of pseudoinverses. The fixed-cap coordinate maps are globally Lipschitz C1 with bounded first derivatives for every psi in A; C3 is not needed. Frozen learned/residual contractions are transferred to actual finite feedback causally.

The countable generated-program construction supplies consistent deterministic same-layer laws. Finite initialized operator bounds pass to all rational combinations, then by density to bounded population actions. Exact finite transpose identities give actual adjoints. Rank-one updates remain HS. This construction does not infer convergence in operator norm between unrelated widths.

The asymmetric cap estimate has one linear factor in R, multiplied by state discrepancy, and a Gaussian tail only for the reference incoming fields. Its error is `C exp(CR-cR^2)`. Thus it constructs a C1 uncut autonomous feature path through the entire bounded reference interval, identifies its true gradient, and proves uniqueness against arbitrary bounded-primal strong competitors on the same spaces. Competitors need not have tails or sample symmetry. The same estimate with the reached-state initial discrepancy proves uniqueness after restart.

The first hit of g=1 occurs before the feature endpoint. Bounded g' gives divergence of the physical clock. Even a cap path need not be monotone for this first-hit argument. Hence the constructed physical paths exist on every finite physical horizon. The physical comparison retains both actual finite residuals. Its constants may depend on T, while its cap-independent reference tails came from the one fixed feature interval; no new activation smallness depending on T is introduced.

Finite matrix operator bounds come from initial bounds and exact rank-one unrolling of a fixed coarse program. Dimension-independent stopped Euler estimates remove its auxiliary mesh. Same-width comparison then removes caps. Raw GD is compared using the uncut field at its own preceding node against the cap reference at that node, leaving only the cap-reference local error proportional to `n^(-2)`. This avoids an uncut width-uniform Lipschitz assertion. The small finite readout is retained and removed only by fixed-program stability in the width limit. The convergence arguments use the full width sequence in probability.

The fixed-cap velocity bridge was read and checked in full. Nonlinear independent-root probes first bound actual expected source rows; an indexed causal inequality then bounds pathwise derivative rows and primary moments. The two extra forward velocity queries include both their source response and learned memories. Products `phi'(Z)P` are first truncated in P, their derivative rows are dominated, and truncations are removed in L2; the bounded-derivative source theorem is not applied directly to unbounded-derivative products.

For uncut velocities the deterministic comparison uses one reference-velocity truncation level. The uncut velocity is a continuous L2 path with compact time image and uniformly vanishing L2 tails. The order is population cap removal at fixed velocity truncation, then its removal; finite width is first taken at fixed cap and truncation. There is no uncontrolled use of a cap-dependent fourth-moment constant against a cap error. Right/terminal-left GD directions are the actual derivatives of the recomputed interpolated fields.

Finally the path approximation inequality `||x-I_h x||_infinity^2 <=4h integral |x'|^2`, the fixed-grid joint laws and speed bounds give the per-layer path-space Wasserstein conclusion. Same-layer L2 contractions give all four raw kernels, prediction and loss, while velocity laws give second moments and integrated squared speeds. These implications are separately justified and are not inferred from raw energy alone.

## 5. Nonaffinity, loss rate and initial motion

For a one-Lipschitz shape, the independent-copy covariance identity bounds every optimal regression slope in absolute value by one. Testing the optimizer of either coupled variable on the other gives the two-Lipschitz square-root regression estimate, including degenerate variables. Gaussian full support and compact-variance continuity establish `eta_psi>0` precisely for globally nonaffine shapes. The additional `c_NL` keeps coupled preactivation error at most `sqrt(eta_psi)/4`; absorbing the affine part yields the exact factor `e^2` and the claimed uniform margin.

Odd/even decomposition of any activation in the class has vanishing Gaussian cross terms, and the odd part has derivative at least `m=a-e>=1/4`. Iteration gives `kappa(0)>=m^6 delta/2>=delta/8192`. Strong radial coercivity requires only the established trajectory chain rule and adjunction. Thus `g_s'>=kappa(0)` and `dot L=-4g_s' L` prove the stated exponential loss bound.

The initial top beta Gram is positive definite because the feature combination vanishes on at most one point of each coordinate slice, while globally nonaffine C2 psi has nonconstant derivative. Full reused-transpose covariances and the deterministic derivative responses then give strictly positive lower conditional variances in the two lower layers. The HS trace identities give motion in every hidden block; forward adjunction and sample symmetry give every sample/layer acceleration. Bounded positive phi' transfers this to feature accelerations. The projected kernel expansion and physical-time factor four agree with the statement. No eta cutoff enters this argument.

## 6. Other new claims

- **AFFINE_POSITIVITY:** The source groups used by the affine lemma are independent, and affine Wick expectations and chronological source recursion give the needed entrywise positivity. Entrywise covariance lower bounds imply the claimed row bounds even for singular Gaussian source covariances. I checked every normalized transfer-table bound, including the identity `F B2=R1-I` in the FL estimate and the correct left-multiplication density inequality. The original-time orders follow from the gain/time factors. The wider beta interval is explicitly conditional on a primal bound; it is not asserted to have the old common continuation. The suggested `q M^6` nonlinear closure is marked provisional and is not used in Theorem A.
- **BOUNDED_ACTIVATION_ROUTE:** Direct integration gives the readout, top learned-kernel and both reverse-memory bounds, with the correct J powers and finite-readout adjustment. Raw physical energy supplies the stated finite-horizon constants. The selected Gaussian-column/sign construction produces a coordinate of order sqrt(n), and hence nonvanishing empirical second-moment tails despite bounded input and exchangeability. This is a counterexample to the general inference, not to the neural dynamics. The displayed two-control Lie bracket is correct; invertibility of the coordinate map and the two independent columns of Gamma force constant phi' for nonzero rho. Both obstructions have the stated limited scope.
- **RELATIVE_NONLINEARITY:** Independent-copy variance inequalities prove the distribution-independent bound. Gaussian sine orthogonalization gives the displayed residual variance and normalized nonlinear fraction. At omega=2, b=2/5 the monotonicity inequality holds and the fraction is approximately 6.4 percent. This coefficient is explicitly outside the global proof's certified regime.
- **SINE_INITIALIZATION:** The sine covariance identity, cancellation of the linear cross terms, strict contraction of interior correlations, fixed initialized variance and the top Gram/projected-kernel bounds all follow from the displayed formulas. Only initialization is claimed.

The two literature boundary statements were verified against primary sources: [Yang and Hu, Appendix A](https://proceedings.mlr.press/v139/yang21c/yang21c-supp.pdf) distinguishes the discrete width limit from the additional continuous-time well-posedness issue and the middle-matrix initialization; [Chen et al., Corollary 4.6](https://arxiv.org/html/2503.09565v2#S4) explicitly assumes weights cease changing after a finite time. Neither is needed as a mathematical premise of Theorem A or B.

## 7. Dependency coverage and superseded material

All seven candidate mathematical files were read in full. Every dependency file was hashed. The mathematical portions needed for this proof were reconstructed as follows; this records scope rather than claiming to certify every historical theorem in the dependency bundle.

| Dependency | Coverage used in this audit |
|---|---|
| `two_sample_odd_activation_theorem/PROOF.md` | Exact finite/population model and observable specifications; assembly checked against its actual companions. |
| `.../AFFINE_CORE.md` | Full file: active geometry, affine existence, frozen inactive fields, Gaussianity, clock and normalization. |
| `.../SOURCE_AND_LIMIT_BRIDGE.md` | Full file: exact source formulas and all cap, physical, finite-algorithm and observable interfaces; its old nonpolynomial response threshold is superseded. |
| `.../INITIAL_MOTION_AND_NORMALIZATION.md` | Full file: actual transpose covariance, all initial motion and kernel expansions; arctangent substitutions separately verified. |
| `.../sources/TWO_SAMPLE_SOURCE_BASELINE.md` | Sections 3–7 in full: two-sample source representation, current returns, raw answer perturbations, independent-root identity and source rows. Norm unrolling checked directly against the downstream bridge. |
| `.../sources/L3_LOCAL_COMPLETE_PROOF.md` | Fixed-mesh conditioning/source section and common-action construction through state/adjunction, lines 211–616. The old one-input bounded-arctangent response and special computational clock are not used. |
| `.../sources/FIXED_CAP_VELOCITY_BRIDGE.md` | Full file: every premise, independent-root probe, derivative row, velocity/product query, truncation, finite algorithm and time-uniform law step. |
| `.../sources/PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md` | Full file: asymmetric strong comparison, construction/restart, genuine physical residuals, actual GD, kernels, paths and ordered velocity limits. |
| `.../sources/SYMMETRY_RADIAL_CLOCK.md` | Sections 3–4: strong radial proof, trajectory chain rule, raw adjunction and all four kernel formulas. Old offset-specific symmetry/variance arguments are replaced by the candidate. |
| `.../sources/CONTRACT.md` | Full model/observable contract read; historical broader targets are not substituted for the candidate's explicit theorem. |
| `two_sample_odd_activation_quantitative/AFFINE_POLYNOMIAL_BOUNDS.md` | Full file: exact normalization/balances, bounded affine endpoint, integrated Hessian, raw tube, constants and absolute lower variances. Its arctangent margin is replaced by eta_psi. |
| `two_sample_odd_activation_power10/AFFINE_SOURCE_CERTIFICATE.md` | Sections 2–8: both-sector normalization, exact coefficients, beta enlargement, all probes, positivity/product derivatives, time conversion and explicit constants, including Ltop. |
| `.../NORMALIZED_GATES_AND_PRIMALS.md` | Full file inspected. Only exact equations are imported. Its global-delta moment inference is not used for intrinsic M; LINEAR_GROWTH replaces it. |
| `.../POSITIVE_SUPERSOLUTION.md` | Full file inspected, with exact map, typed applicability, signed chronological comparison, arbitrary backward row forcing, sandwiches and inactive construction checked. Its older exponents are replaced by power-four closure. |
| `.../REFINED_RESPONSE.md` | Source/transfer definitions and exact value/derivative identities checked; old power-43 estimates are superseded by the fully checked power-four response. |
| `two_sample_odd_activation_power4/PROOF.md` | Full assembly checked against companions and old model. |
| `.../AFFINE_PROPAGATOR.md` | Full file: all four gradient terms, integrated M-cubed bound, actual source probes, constants and products. |
| `.../PRIMAL_L2_RESPONSE.md` | Full file: source moments, strict/current derivative equations, envelope and actual-L2 forcing. |
| `.../SECTOR_SUPERSOLUTION.md` | Full file: both outer boxes, transfer persistence, exact forced supersolution, numerical ledger, homotopy. |

The remaining hashed dependencies are older assemblies or estimates not used as unresolved premises: `ANGLE_SPECIFIC_THEOREM_ASSEMBLY`, `INITIAL_FEATURE_LEARNING`, `NONLINEAR_RESPONSE_PERTURBATION`, `PREVIOUS_TWO_SAMPLE_PROOF`, `THREE_SAMPLE_CONTROLLED_RESPONSE_LEMMA`, quantitative `PROOF`, `POLYNOMIAL_RESPONSE_LEMMA`, `OLD_THRESHOLD_AND_NONAFFINITY`, and power-ten `PROOF`. Their relevant roles have the explicit replacements identified above: direct affine geometry, exact source conditioning/probes, power-four response/sector closure, the new shape symmetry/nonaffinity proof, and the fully checked strong/physical/velocity bridges. No historical review conclusion or unused old cutoff is an assumption in this acceptance.

## 8. Integrity record

All 36 candidate/dependency hashes matched their supplied manifests before the audit. After the audit all 36 still match both those manifests and the before record. Only this review was written in the candidate folder. The following table records the same full SHA-256 before and after for every audited artifact.

| Artifact | Before SHA-256 | After |
|---|---|---|
| `PROOF.md` | `c36d92166c65affeb7974c5fe07ddfaa8697399b56d3c4322e89db51a02748ce` | Identical |
| `SHAPE_SYMMETRY.md` | `58432555e59bc191e98cb7fda7e1063d22410933c2cb5816003f6e5bbe061540` | Identical |
| `LINEAR_GROWTH.md` | `5e06d3414959abef70cfbe569f1b393df689ad3826e31d391149d556ad861bd9` | Identical |
| `AFFINE_POSITIVITY.md` | `d87609ed88ed1d31ee3a9a32363e813ad4f30721b455737aa208db1c9bfaba81` | Identical |
| `BOUNDED_ACTIVATION_ROUTE.md` | `018e912b6b6e434c26eea0ea9a4c499952f9ffbff4c2cb4b235f18a2f61fa381` | Identical |
| `RELATIVE_NONLINEARITY.md` | `bcaa95026a90736f32cd4e2cdd8f2a662439afa20051abb9522918becab2070f` | Identical |
| `SINE_INITIALIZATION.md` | `55be13083cc6a61967e7e993a819c92a1e8ef981de858294a99e67e6fe335e72` | Identical |
| `DEPENDENCIES.json` | `3f5916ff969e28e8fb3b899d91813a654802ab00c346baff82f1dede2d38d012` | Identical |
| `../two_sample_odd_activation_theorem/PROOF.md` | `a4d6ed0ee99a1e111b5eba068f2219cf561a2281b1828b26227aca7a0a54a050` | Identical |
| `../two_sample_odd_activation_theorem/AFFINE_CORE.md` | `634dd3bbc35436e9d1760bee5c11cbf2124b3c42e8920a1bf3a4fcbb15039711` | Identical |
| `../two_sample_odd_activation_theorem/SOURCE_AND_LIMIT_BRIDGE.md` | `2a140f2a5a39f911b5c2ca51bc79102d20e9209f1450d38005360c88103f6e77` | Identical |
| `../two_sample_odd_activation_theorem/INITIAL_MOTION_AND_NORMALIZATION.md` | `c96316fdc481ef3f9e6fc402514ca9b45bcff12e199023505fbbb86d4e15bf24` | Identical |
| `../two_sample_odd_activation_theorem/sources/ANGLE_SPECIFIC_THEOREM_ASSEMBLY.md` | `27b2579f27ec14319dd39a93a4942d7b6463860648462d5ccb31b662c7725b75` | Identical |
| `../two_sample_odd_activation_theorem/sources/CONTRACT.md` | `e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd` | Identical |
| `../two_sample_odd_activation_theorem/sources/FIXED_CAP_VELOCITY_BRIDGE.md` | `a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0` | Identical |
| `../two_sample_odd_activation_theorem/sources/INITIAL_FEATURE_LEARNING.md` | `bd81de0a7ad0cb9bdd1f27f89961f4a3b7a7da6914456ae08596a882fa2ec351` | Identical |
| `../two_sample_odd_activation_theorem/sources/L3_LOCAL_COMPLETE_PROOF.md` | `f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4` | Identical |
| `../two_sample_odd_activation_theorem/sources/NONLINEAR_RESPONSE_PERTURBATION.md` | `ef0ea077406a27307bc84e045feebf5099f6f81883bdfed41508035fe4559568` | Identical |
| `../two_sample_odd_activation_theorem/sources/PREVIOUS_TWO_SAMPLE_PROOF.md` | `2891b892667396d64bd747689bcd59aa7ca3ffd224d3579fc3407bca0b623f9a` | Identical |
| `../two_sample_odd_activation_theorem/sources/PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md` | `99eb60a64df1bbf4d8b70f351198abced9ef7eaeacf9b39c3997da5700a8f066` | Identical |
| `../two_sample_odd_activation_theorem/sources/SYMMETRY_RADIAL_CLOCK.md` | `40882fc19e44b4b9245156595bb1071bd4de6007d619fada54c9fce7c37903f4` | Identical |
| `../two_sample_odd_activation_theorem/sources/THREE_SAMPLE_CONTROLLED_RESPONSE_LEMMA.md` | `49da0f68047b4f516d3ad3c94b7112259838bcebf68e2296a948364232842789` | Identical |
| `../two_sample_odd_activation_theorem/sources/TWO_SAMPLE_SOURCE_BASELINE.md` | `a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f` | Identical |
| `../two_sample_odd_activation_quantitative/PROOF.md` | `0a7dbd32cb9cc291e706813b59c0142394e6f9532244e52c21a5ab5d89ed4d02` | Identical |
| `../two_sample_odd_activation_quantitative/AFFINE_POLYNOMIAL_BOUNDS.md` | `8387e2f253063c139dacb282ca9f2372478521f54b33a9ef6c8dbd83f2b521ca` | Identical |
| `../two_sample_odd_activation_quantitative/POLYNOMIAL_RESPONSE_LEMMA.md` | `51b0f717b33ed618219e086d32b16a95ef4253892171597d1805dd9d37a64f7f` | Identical |
| `../two_sample_odd_activation_quantitative/OLD_THRESHOLD_AND_NONAFFINITY.md` | `c63753a83e832793c886b8ae8c122e30e0c01864b86a1a5dc9bee030852f9210` | Identical |
| `../two_sample_odd_activation_power10/PROOF.md` | `37b9e8a27135b95b8dffe05fe2b734229fadedc98bc1609259e365dbb2aeba37` | Identical |
| `../two_sample_odd_activation_power10/AFFINE_SOURCE_CERTIFICATE.md` | `bc55c0f8e25de1f3a4316fe36e86afa25c9486e014192f2eb818358909b048eb` | Identical |
| `../two_sample_odd_activation_power10/REFINED_RESPONSE.md` | `3622a0f903cd51b712d1d524a140d834471b5eb588611f059535c41f6efd2332` | Identical |
| `../two_sample_odd_activation_power10/POSITIVE_SUPERSOLUTION.md` | `e2be183521919ce69c7ae41b81f5cd78566c5430a78c2408687f52f1b6d86774` | Identical |
| `../two_sample_odd_activation_power10/NORMALIZED_GATES_AND_PRIMALS.md` | `8715de810f689037d2223712cd60bce15c3025bc53338a3a0fdeda6e07664dae` | Identical |
| `../two_sample_odd_activation_power4/PROOF.md` | `7e33899649b547e7dcac8a465f2d118518d9db9ef001a3d04d2b9da615aa9485` | Identical |
| `../two_sample_odd_activation_power4/AFFINE_PROPAGATOR.md` | `88a1bfbaf6fd1fc6fcfea56b25a4490932663090eb01710e9d96ba04d26fe460` | Identical |
| `../two_sample_odd_activation_power4/PRIMAL_L2_RESPONSE.md` | `cf313286d301aa9fe5fb121d0c1fa5351213efbeaa4c087656d205c3156e417a` | Identical |
| `../two_sample_odd_activation_power4/SECTOR_SUPERSOLUTION.md` | `e1ce9401b58bcd20384e1b2932d725844fda6904e9c9d70ef4a4f1af0f9ab68d` | Identical |
