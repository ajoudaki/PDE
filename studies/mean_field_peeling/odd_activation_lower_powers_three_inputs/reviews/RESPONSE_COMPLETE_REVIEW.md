# Independent complete mathematical review

Date: 2026-09-07.

## Verdict and exact scope

**PASS: the complete original odd two-input, three-hidden-layer population/GF/raw-GD theorem follows for every `0 < e <= c_poly delta^2`, with the unchanged explicit `c_poly`.** This includes the requested `c_poly delta^3` choice. This verdict covers the assembled theorem and its construction and observable bridges, not merely the response lemma.

**PASS: the explicitly limited three-input mathematical statements in `THREE_INPUT_ANALYSIS.md`. OPEN: the complete three-input odd-mixture global population/GF/raw-GD theorem.** The file correctly does not claim that theorem, and neither its initialization Gram nor its conditional scalar-clock argument closes it.

I found no blocking mathematical gap in the final four-file candidate. This review independently read all four mathematical candidate files, checked their contents against the actual source identities, and audited the required original mathematical portions of the affine, source, continuation, finite-program, velocity, nonaffinity, and initialization arguments. Historical reviews, review outcomes, evidence ledgers, and agent discussions were not used as mathematical premises. The explicitly hashed `AFFINE_SOURCE_CERTIFICATE.md` was inspected as original mathematical content about normalized source probes. No experiment, candidate edit, delegation, or commit was performed. The only output written by this review is this report.

The main-file editorial correction from `Ce,qquad` to `Ce,\qquad` was received during the audit. The final main hash below, rather than the initial main hash, identifies the reviewed version. All four candidate hashes and all 30 dependency hashes were rechecked after that correction and matched their manifests.

## 1. Model, quantifiers, and dependency architecture

The statement preserves the original normalized Gaussian initialization, including the finite random readout, the raw metric, simultaneous raw Euler/GD with step `n^-2`, and one identical activation at all three hidden layers. The population readout is zero as a limit; the finite readout is never silently reset. Absolute separation excludes both incompatible odd-network endpoints, and label folding handles every binary-label pair without changing the finite parameter trajectories.

The exact scale is

`r = sqrt((1+y1*y2*rho)/2)`, `lambda = a^3 r`,
`M = (3/(sqrt(2)lambda))^(1/4)`.

In particular `r = 3 M^-4/(sqrt(2)a^3)` is an identity for the intrinsic dataset scale. The envelope `M <= 24^(1/4) delta^-1/8` is used only for the final uniform choice. Substituting the uniform envelope into the identity for `r` would be invalid; the candidate does not do so. From `T<2` and `M^4=3/(sqrt(2)lambda)>2/lambda`, the duration bound `S<=M^4` is valid.

The proof has a noncircular order:

1. Construct fixed-cap paths and fixed finite programs; use the affine raw comparison to bound the actual paths and their actual L2 fields.
2. Use actual L2 field norms for primitive Gaussian covariances, while temporarily assuming the deterministic coefficient box.
3. On that box, solve the same-array value equations and obtain source moments; then obtain derivative defects.
4. Insert those defects into a deterministic positive supersolution and exclude first exit by amplitude homotopy at fixed cap and mesh.
5. Remove the auxiliary mesh and caps with the original bridges, construct the scalar physical clock, and transfer the full finite-width observables.

Neither the uncut theorem nor already-closed source tails are assumed to obtain the initial raw L2 bounds. The earlier fourth-power response restriction is replaced, rather than retained as an additional restriction that would prevent the claimed improvement.

## 2. Affine propagator, actual probes, and weighted products

I checked the power-four affine argument used here. Its four raw gradient terms give the integrated lower bound on the affine objective and hence `F>=z^2-100z`, where `z=||D||^2`. At enlarged beta scales this yields `(log w)' >= ||D||^2-101 beta^2`. The affine raw Hessian has three off-diagonal product terms per column in the raw component sum norm. The radius-one correction integrates as `6R+3`; it does not multiply the logarithmic coefficient by an extra fixed factor. The resulting two-time estimate `exp(2100)[w(t)/w(s)]^3` is valid on the whole enlarged interval and in the full raw geometry, including inactive first-layer variations.

The independent-root probes identify actual frozen formal source derivatives. At fixed nonzero probe amplitude one first takes the fixed-program width limit, pairs the output with the independent root, and only then sends the amplitude to zero. The source and covariance coefficients are frozen in the derivative. This is not an identification of an arbitrary raw tangent with a formal derivative. The old source rule also permits the added first-coordinate and top-backward probes, and retains their current identities.

Retaining local injection and output costs in these probes gives precisely the weights used by the candidate: unit/unit costs for `F,T`, `w(s)`/`w(t)` for `V,W`, `w(s)^2`/one for the first and backward-top resolvents, and one/`w(t)^2` for the forward-top resolvent. The top strict transfer has costs `w(s)^2` and `w(t)^2`. The learned `B3` term `w(t)w(s)` must be added and is present.

The radial integrals follow by splitting at `||D||=1` and using `dt <= C c^-3 dc` afterwards. This gives integrable `w`, logarithmic `w^2`, endpoint-square growth for the integral of `w^4`, and the crucial tail estimate `integral_s^T w^-2 <= C w(s)^-4`. The compact-interval Riemann-sum argument allows all sufficiently fine positive meshes and does not require a smallest step.

I expanded both triple products in `FL=F+FB3V` and `RF=F+VB3F`. For `FB3V`, the learned-moment contribution leaves `w(u)^-2 w(q)^5`; reversing the nonnegative integration order and applying the tail estimate reduces it to the bounded integral of `w(q)`. For `VB3F`, that contribution leaves `w(u)^-1 w(q)^4`; integrating in `q` first reduces it to the bounded integral of `w(u)`. Thus the claimed respective strict weights `w(t)^3/w(s)^2` and `w(t)^4/w(s)^3` are justified. No current identity or learned term has been omitted.

## 3. Outer boxes and deterministic closure

Deterministic source blocks are diagonal in the mean/contrast basis because exchange-equivariance applies to their full named-source formulas and covariance laws before expectation. This says nothing about the individual gates; their random off-diagonal terms remain in the response calculation.

The proposed active row radius `H^-100 M^3` is legitimate. Its normalized size is at most `2r H^-100 M^3`. Weighted causal resolvent identities give Neumann ratios controlled by this size times a fixed constant or `log(euler_number*30M)`. Since `r=O(M^-4)`, these ratios are uniformly tiny. The distinct inactive radius `H^-100 M^-4` pays for the inactive integration row of size `M^4`.

The treatment of arbitrary backward row errors is correctly typed. Such an error may have a current diagonal or concentrate on a very short past step. The proof claims weighted row bounds for perturbed resolvents, not an unjustified inherited strict density for every resolvent difference. The reverse-resolvent identity `L*=L_b+L_b J3_hat V*` has a strict right factor, so the particular strict estimate used there is justified. This distinction is essential to avoiding an implicit minimum-step assumption.

At the inner beta scale the positive supersolution keeps the forward arrays at the beta reference and reconstructs the backward arrays exactly. In particular `W*-W_b=a^2 L_b J3 R*` is in the correct orientation. Positivity of the finite chronological affine map dominates signed actual arrays after absolute values. Beta positivity concerns expected Wick expansions, not signs of individual initialized weights.

The weighted strict sandwiches yield the charges stated in the candidate. Conversion of an `F`-type normalized density costs `O(r^2)`. The `J2` sandwich therefore has original density `O(M^-9 J2+)`; the `J3` first-forward sandwich adds a logarithm. Dividing by the active `M^-8 h_j` lower bound and then paying the beta slack `M^-2` gives the advertised `M J2+` charge and the logarithmic first-forward `J3+` charge. Separately, `VJ3V` has endpoint power four and requires `M^2 log(M) J3+`; the sufficient `M^3 J3+` charge includes it. Omitting this last sandwich would be a real gap, but it is explicitly retained.

Backward reconstruction costs at most `H^55 J3+ M^4 log(euler_number*30M)`, which fits strictly inside the active radius under the typed criterion. The inactive construction is triangular because its top feedback vanishes. It charges `M^4(J2-+J3-)`, includes current diagonals, and stays below both its row radius and the added forward-density allowance.

Consequently the sufficient criterion

`D = M^10(E2+ + E3+) + M J2+ + M^3 J3+ + E2- + E3- + M^4(J2- + J3-) <= H^-200`

is supported, including strict interiority. The weighted companion's coarser delta-cubed discussion is a sufficient alternative route; the assembled square-power theorem uses the separately supplied and explicitly budgeted sector response, not that coarse discussion as a missing premise.

## 4. Actual raw L2 comparison, covariance scales, and learned moments

The same-state nonlinear forcing is `O(e w(u)^3)` in feature time. Applying only the affine tube propagator in normalized time cancels the source-time weight and proves `E(t)<=C(e/lambda)w(t)^3`. This argument remains valid for arbitrary nearby raw states; it does not require nonlinear inactive fields to freeze. The previous explicit condition `e<=c_* delta^(7/4)` already closes the tube and gives the endpoint and regression margins. It is implied by the new delta-squared choice.

The active forward estimate uses a substantive oddness cancellation:

`|[atan(P+Q)+atan(P-Q)]/2| <= |P|`.

The first active preactivation is exactly `r p_e`, and the second is obtained by the same bounded raw action on the active feature. Thus the two active feature differences are `O(e w^3)` and `O(e w^4)`, while their norms are `O(rw)` and `O(rw^2)`. This uses bounded actions on L2, not multiplication of two arbitrary unbounded L2 variables.

The actual incoming fields satisfy `||q1||2=O(w^3)`, `||q2||2=O(w^2)`, and `||C||2=O(w)`, directly from the raw bounded actions and capped gates. The common readout makes the top contrast `O(e w)`. Applying the actual adjoint and the next gate gives middle contrast `O(e w^2)`. These are actual source-output laws at each fixed program, established by the original Gaussian/action construction; no affine covariance domination is assumed.

The resulting actual primitive Gaussian scales are correctly identified: active bottom root `r`; reverse sources `(M^2,eM^2)` and `(M,eM)` in the two sectors; forward sources `(M^-3,1)` and `(M^-2,1)`. Full temporal covariance, singularity, and both matrix orientations survive. The proof never differentiates a covariance square root or assumes independent times.

Learned forward moments use the covariance difference inequality with one actual and one affine norm. The active density errors are `O(e)` and `O(eM^2)`; the inactive/full-sample sufficient errors `O(eM^7)` and `O(eM^8)` also follow. Backward moments pay one `lambda^-1` from the raw discrepancy and another from original-time integration. The radial integrals give top row `O(eM^11)` and middle row `O(eM^12 log(M))`, bounded by `O(eM^13)`. Inactive learned backward moments start at order `e^2`, because both affine contrast fields vanish. Their bounds `O(e^2M^7)` and `O(e^2M^5)` fit the final inactive forcing. The factor of the source-time step and all relevant row sums are accounted for.

## 5. Source moments and the exact two-sector derivative estimate

The same-array value identities separate each deterministic sector in the Gaussian linear part, then bound the genuinely nonlinear remainder in the full sample norm. Their leading preactivation powers are `(M,M^2,M^3)` and their self-interaction powers are `(M^13,M^11,M^8)`. Under `e H^200 M^16<=1`, the latter terms absorb for every individual Lp norm. Substituting into the incoming-field equations gives powers `(M^10,M^9,M^7)` with prefactor `H^94`.

These are suprema of individual-time norms. The even-moment expansion establishes subGaussian bounds without asserting a bound on a random time supremum or an Lp-preserving property of arbitrary L2 actions. Weighted Jensen then controls the derivative exponential through order eight. The largest stochastic integrated power is `4+10=14`; its coefficient is at most `e H^(81+94) M^14`. The stated smallness has spare `H^25 M^2`, including fixed sample and moment constants. The deterministic part inside the clock also fits.

I checked the exact local elimination. With `R=(I-a^2KB)^-1`, `U=RK`, `L=(I-a^2BK)^-1`, and deterministic coefficients frozen,

`J-Jaff=U[DeltaV I_zeta+P J]`,
`Ddelta-Ddelta_aff=L[DeltaV I_zeta+P J]`,
`P=Lgate+a DeltaV B+a B DeltaG+DeltaV B DeltaG`.

The second identity follows using `I+a^2BU=L` and retains the identity in the backward resolvent. The bounded gate terms with `B` have not been discarded. They determine, for example, the active middle-backward exponent fifteen.

In sample sectors the large active `B+` enters `P--` only through `DeltaV-+ B+ DeltaG+-`, hence with two nonlinear factors. A one-sector scalar replacement would lose this fact. The candidate instead uses the positive two-by-two majorant

`K_u = [[u,u],[1,1]]`, `K_u^2=(1+u)K_u`.

Its exact exponential bounds the finite chronological product after padding source histories and taking past running maxima. The strict `U` supplies the time step, whereas `B` may include its entire causal row and current diagonal. For an active transpose source the direct vector has sizes `(u+eu,e) h_j`; the exponential gives the claimed active size `u h_j E` and cross size `e h_j(1+u I)E`. For an inactive forward-source row it gives an inactive identity-scale base and active cross size `e u I E`. There is no discarded current source identity. The smaller `H^45` rate used for the cross-generation ledger is valid because the `H^40` backward coefficient is already inside `I`; charging it twice would be erroneous, and the candidate explicitly avoids doing so.

Only after the exponential moments have been controlled does the proof use the actual raw L2 bounds in `E[Q_r E_k]`. Cauchy--Schwarz applies for every pair of times, including the terminal time, without independence. Cross returns involve an extra clock factor and are instead handled with the established higher source moments and Hölder. The terminal-time maximum remains outside expectation for backward rows.

## 6. Forcing powers and explicit numerical closure

The forward active diagonal returns cost `e u^2 S(M^qraw+M^b)`, giving powers three and five. Their cross returns have powers eighteen and twenty with two factors of `e`; terminal feature gates and direct source terms fit as well. The inactive full-sample forward estimates give powers thirteen and eleven.

For active backward rows, the middle factors have powers `4+4+7=15`; the top factors have powers `3+5+4=12`. Inactive curvature returns use raw powers two and one. Their remaining cross returns have powers nineteen and seventeen, with two factors of `e`. Thus the complete table, including learned moments, is

| Defect | Active power of M | Inactive power of M |
|---|---:|---:|
| E2 | 3 | 13 |
| E3 | 5 | 11 |
| J2 | 15 | 3 |
| J3 | 12 | 1 |

Every entry is bounded by `H^200 e` times its listed power under the response smallness condition.

The numerical budget is consistent with the delivered `H^40` transfer envelope. Incoming source scales fit `H^94`; clock moments fit `H^96`; direct derivative bases fit `H^50`. One cross generation fits `H^196`, using the smaller rate. Returning it through one transfer and one incoming field fits below `H^350`. The reduction

`e^2 H^350 M^p <= e H^150 M^(p-16)`

is exactly what follows from `e H^200 M^16<=1`. Single-insertion products fit `H^140` before final rounding. There is ample room for the fixed sums and the smaller learned-moment terms below `H^200`; the proof does not silently multiply saturated `H^40` factors and rename the result `H`.

After the closure charges, the eight powers are `13,15,16,15,13,11,7,5`, respectively. Since `M>1`, their sum is bounded by `8H^200 eM^16`. The actual worst power is sixteen, from `M J2+`.

The final arithmetic uses exactly

`M^16 <= 24^4 delta^-2`,
`c_poly = min(1/4,c_*,10^-70 H^-400)`.

It gives

`D <= 8*24^4*10^-70 H^-200 < H^-200`.

The factor `24^4` is retained numerically, so there is no extra power of `H` charged against the fixed `H^-400` coefficient. The same choice implies the response-moment condition and the earlier primal/nonaffinity condition. At fixed cap and sufficiently fine fixed mesh, all amplitude-dependent source coefficients are continuous, including at singular Gaussian covariances by square-root continuity of the finite Gaussian laws. The strict supersolution margins therefore exclude every first exit. No cap-dependent or horizon-dependent activation choice is introduced.

## 7. Complete construction, uniqueness, finite algorithms, and observables

The resulting source tails and bounded primal feature interval are exactly the missing inputs for the original asymmetric cap comparison. Successive backward substitution has one linear cap loss `C(1+eR)` multiplying the state discrepancy, and Gaussian reference tails dominate `exp(CR)`. Both raw states and raw directions converge uniformly as caps are removed. The limit is a strong autonomous uncut feature gradient flow on the canonical spaces.

The endpoint prediction exceeds one. Exchange symmetry is established at the capped finite-program level and passes to the strong limit, so the scalar first-hit clock applies to the constructed population paths. A bounded derivative before the first hit makes the physical-time integral diverge there; capped paths do not need a gradient or monotonicity assertion for this argument. This constructs one path for every finite physical time. The nonlinear radial argument is used only after construction.

Physical uniqueness compares every bounded-primal strong competitor, including nonsymmetric ones, with the cap reference and retains both individual residuals. It requires tails only of the reference. Starting this comparison at a reached time proves restart there. The claim is neither arbitrary-state local existence for a continuous infinite-dimensional field nor uniqueness only within the symmetric ansatz.

The fixed finite Gaussian-program source rule, singular-query regularization, common generated probability spaces, and both actual adjoints have the needed hypotheses at fixed cap. The gain and offset changes only reduce the relevant bounded-derivative estimates. Source covariance is the full actual input Gram; finite-rank conditioning projections do not replace it by a residual covariance. Positive-semidefinite square-root continuity is used for law limits, never differentiation.

Width tends to infinity at fixed cap and auxiliary mesh. Rank-one unrolling and the initial operator bound supply a larger finite primal ball without cross-width trained operator-norm convergence. Deterministic raw Euler error removes the auxiliary mesh. The same-width asymmetric comparison then removes caps and handles the genuine raw-GD step through its `C_(R,T) n^-2` reference error. The original small random finite readout is retained and vanishes only in the limit. These are full-width-sequence convergence-in-probability arguments, and use no growing-transcript Gaussian assertion.

The velocity bridge first truncates the unbounded product queries `phi'(Z)P`, applies the fixed-program theorem, and removes those observational truncations in the appropriate order. In removing training caps it holds the reference-velocity truncation fixed, then removes that truncation. The uncut velocity has a compact continuous L2 time image, which supplies uniform reference tails without an estimate on cap-dependent fourth-moment growth. This yields the requested uniform-time same-layer field/velocity laws, fixed finite collections of times, second moments, and integrated squared speeds. The path interpolation estimate upgrades to the stated supremum-norm path-space W2 law. Both samples are paired within each layer; no cross-layer neuron pairing or continuous velocity-path law is added.

The four full kernel matrices, including off-diagonal entries, predictions and loss follow from the actual forward/backward L2 fields and their contractions. Both initialized and trained action orientations remain available on generated probes. The absolute affine regression margin from the quantitative proof transfers through the raw comparison and cap limit, giving strictly positive activation regression error `e^2 eta_*/4` at every finite physical time.

The initial-motion proof retains full reused-transpose Gaussian covariances and deterministic returns. Its positive backward Grams imply every hidden block moves to second order. Sample exchange proves each two-input upper-layer sample moves, while the bottom sample has its own conditional-variance proof. The physical time factors and projected kernel expansion are preserved. Positive `e`, not a new smallness restriction, is needed for these nonaffinity and initial-motion assertions. The normalized identity-plus-arctangent family has gain in `[1/2,1]` and nonlinear coefficient at most its original parameter, so its stated inclusion is also valid.

## 8. Limited three-input claims and the open boundary

The cubic-tensor witnesses have unit norm and annihilate the other two tensors. Summing the three Cauchy--Schwarz bounds gives `Gamma^(entrywise 3) >= s_delta^2 I/3`, without an input-Gram inverse. Gaussian integration by parts gives the nonzero third-chaos coefficient `b3=(1-2E(1+G^2)^-1)/sqrt(6)`; strict Jensen supplies its nonzero sign. Orthogonal projection onto that chaos gives the first-feature Gram bound. First-chaos regression at the next two Gaussian layers gives the factor `a^4`. The matching planar construction proves the stated worst-case scale only in the explicit small-separation range; the candidate correctly does not extrapolate it to `delta=1`. The imported algebraic initial-motion assertions retain their strong-solution/chain-rule qualification.

The affine obstruction is exact: affine predictions lie in `ran Gamma`, and a target component in `ker Gamma` cannot be fitted. The equal-label equilateral example is stationary at population affine initialization. This obstructs an affine comparison route and is not a counterexample for positive `e`.

The new raw-state identity for a Gram-null vector is exact at finite width and in population normalized L2 spaces. Bounded arctangent and bounded actions give the stated `e ||C|| [1+a||B||+a^2||B||||A||]` bound. The low-loss implication uses `sum f_i>=3/2`; raw Hilbert distance controls each learned action increment by its Hilbert--Schmidt norm. Therefore `R >= (pi e)^(-1/3)-11`, and the conditional energy identity gives the stated fitting-time lower bound. The argument does not assume successful fitting or prior uncut existence.

The general scalar ascent lemma is correct under its stated strong-existence and scalar chain-rule hypotheses. The quotient `J/||C||` is well-defined for positive time; differentiating it yields a sum of nonnegative terms. Its initial limit is `||H0||`, so `J'>=||H0||^2`. Ascent energy bounds the path length before a hit and gives a strong endpoint at a finite maximal endpoint. It does not give local existence from that endpoint for a merely continuous infinite-dimensional field. The physical exponential residual bound applies only to the symmetric strong trajectory for which the scalar reduction is valid. The resulting certificate has scale `e^-2` in the equilateral case.

Inserting that nonlinear clock into the old affine controlled-source threshold is not a valid closure: its exponential restriction becomes of the form `e exp(c/e^2)<=C`, which fails as `e` tends to zero. Generic triples also lack the required transitive symmetry. The two regularization discussions correctly distinguish energy bounds from local Lipschitzness and strong compactness. They do not claim a general impossibility theorem for alternative methods.

Accordingly the complete three-input construction, cap-uniform source control, nonsymmetric uniqueness/restart, trained-time nonaffinity, and full finite algorithm/observable limits remain **OPEN**. The candidate's explicit boundary is accurate.

## 9. Final SHA-256 binding

Candidate manifest SHA-256: `1f2c05ad0e37de101add136d4e3d284ed8b3c8bae77896f86e76e73a0977b469`.

Dependency manifest SHA-256: `0f2791cb302c2b330617041448929e587863a06e111f879f627b4106c9879523`.

All candidate paths below are relative to this study directory. All dependency paths are relative to its parent, `studies/mean_field_peeling`. Every listed digest matched the corresponding file on final verification.

### Candidate files: 4/4 match

```text
1ec4886b450deafb255c60a3e053d5c7c32ef3c02ad9a2aa41e50f0db7f98e7a  TWO_INPUT_PROOF.md
17d8bac86024c2dff6344f95d948c9783ad6f64b2fd12441ea5c953c08387076  WEIGHTED_AFFINE_AND_CLOSURE.md
2f2e7e66f4d754fca842ebf9524e605ba846c5e2445fc9792e263c859f62d725  SECTOR_RESPONSE.md
87327edbd36e63fc40043e5e41783fa6a2e75a0be148af0e41d82337a5bbd2f9  THREE_INPUT_ANALYSIS.md
```

### Mathematical dependencies: 30/30 match

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
37b9e8a27135b95b8dffe05fe2b734229fadedc98bc1609259e365dbb2aeba37  two_sample_odd_activation_power10/PROOF.md
bc55c0f8e25de1f3a4316fe36e86afa25c9486e014192f2eb818358909b048eb  two_sample_odd_activation_power10/AFFINE_SOURCE_CERTIFICATE.md
3622a0f903cd51b712d1d524a140d834471b5eb588611f059535c41f6efd2332  two_sample_odd_activation_power10/REFINED_RESPONSE.md
e2be183521919ce69c7ae41b81f5cd78566c5430a78c2408687f52f1b6d86774  two_sample_odd_activation_power10/POSITIVE_SUPERSOLUTION.md
7e33899649b547e7dcac8a465f2d118518d9db9ef001a3d04d2b9da615aa9485  two_sample_odd_activation_power4/PROOF.md
88a1bfbaf6fd1fc6fcfea56b25a4490932663090eb01710e9d96ba04d26fe460  two_sample_odd_activation_power4/AFFINE_PROPAGATOR.md
cf313286d301aa9fe5fb121d0c1fa5351213efbeaa4c087656d205c3156e417a  two_sample_odd_activation_power4/PRIMAL_L2_RESPONSE.md
e1ce9401b58bcd20384e1b2932d725844fda6904e9c9d70ef4a4f1af0f9ab68d  two_sample_odd_activation_power4/SECTOR_SUPERSOLUTION.md
5b5788fcf61ca350c31ca36868bbb0eed9d86f88dcafb36348632a443b8c45dc  odd_mixture_separation_quantitative/THREE_INPUT_GEOMETRY.md
43dcb3930747cb3ad00615d3eac93ec15e2eff85c1a8e56c30145f029b3360f3  odd_mixture_separation_quantitative/REPORT.md
e319166dbdd3c0c8b8ddfc7c588642bbac67f4cc5c870f0513b1bdddc6633300  three_sample_separated_angle_theorem/PROOF.md
```
