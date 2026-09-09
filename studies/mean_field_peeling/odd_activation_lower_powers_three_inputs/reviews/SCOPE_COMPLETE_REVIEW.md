# Independent scope-complete mathematical review

Date: 2026-09-07.

## Verdict and exact scope

**No substantive mathematical defect was found in the assembled two-input theorem with the unchanged coefficient `c_poly` and sufficient amplitude `0<e<=c_poly delta^2`.** The `delta^3` choice follows with that same coefficient. The attached three-input note correctly establishes only its initialization, obstruction, necessary-displacement, and conditional symmetric-clock results; it does not establish the generic three-input global theorem.

This was an independent full-chain audit of the four candidate mathematical files and their applicable mathematical dependencies. I checked the original model and complete observable scope, the affine/primal/nonaffinity arguments, the new weighted transfer and positive closure arguments, the complete sector response calculation, and the downstream construction, uniqueness, restart, finite-GF/raw-GD, action/kernel, velocity/path, and initial-motion bridges. Earlier or sibling reviews, status/evidence ledgers, and review certificates were not used as mathematical evidence. No proof edit, experiment, delegation, or commit was performed.

The equation (6) editorial typo has been resolved: `Ce,qquad` was corrected to `Ce,\qquad`. I rechecked the corrected line and final assembly hash, and verified both complete manifests again. The correction does not change any mathematical claim or the verdict. No remaining issue was found in this audit.

## Reviewed versions and integrity

The four hashes below were checked against `CANDIDATE_HASHES.json`. All 30 entries of `DEPENDENCY_HASHES.json`, resolved relative to the parent `mean_field_peeling` directory, were independently recomputed and matched. Hash checking was an integrity check, not evidence of mathematical correctness.

| Candidate mathematical file | SHA-256 |
|---|---|
| `TWO_INPUT_PROOF.md` | `1ec4886b450deafb255c60a3e053d5c7c32ef3c02ad9a2aa41e50f0db7f98e7a` |
| `WEIGHTED_AFFINE_AND_CLOSURE.md` | `17d8bac86024c2dff6344f95d948c9783ad6f64b2fd12441ea5c953c08387076` |
| `SECTOR_RESPONSE.md` | `2f2e7e66f4d754fca842ebf9524e605ba846c5e2445fc9792e263c859f62d725` |
| `THREE_INPUT_ANALYSIS.md` | `87327edbd36e63fc40043e5e41783fa6a2e75a0be148af0e41d82337a5bbd2f9` |

This verdict concerns those exact versions. The dependency manifest includes historical mathematical source assemblies as well as the directly used lemmas; their obsolete thresholds are not new premises of this proof.

## 1. Model, normalization, and original theorem scope

The candidate retains the original three-hidden-layer bias-free raw model, all binary two-sample label choices, the independent Gaussian initialization, the small finite readout, and the metric

`(d/n)||dW1||_F^2 + ||dW2||_F^2 + ||dW3||_F^2 + ||dC||_n^2`.

Its matrix population increments have Hilbert–Schmidt norm, while initialized actions are bounded operators with actual adjoints. Finite raw GD is simultaneous Euler with step `n^-2`; hidden fields are recomputed from the raw parameter interpolation. No altered optimizer or readout reset has been introduced.

Odd label folding is an exact identity of the finite loss as a function of raw parameters, so it preserves both GF and raw GD. Exchange symmetry gives equal folded population predictions for the constructed fixed-cap programs and their strong limits. It is not imposed on finite-width trajectories or on nonsymmetric uniqueness competitors.

The intrinsic scale is used correctly:

`r=sqrt((1+y1*y2*rho)/2)`, `lambda=a^3 r`, `M^4=3/(sqrt(2) lambda)`.

Thus `S=T/lambda<=M^4` follows from `T<2`, and `M<=24^(1/4) delta^(-1/8)` follows from `a>=1/2` and `r>=sqrt(delta/2)`. Identities involving `r` use this intrinsic `M`, rather than incorrectly replacing it by the dataset-uniform upper envelope.

## 2. Affine geometry, primal comparison, and nonaffinity

I checked the affine balance identities and the sharpened propagator argument. For `z=||D||^2`, the four gradient terms give the stated lower polynomial for `F'`. Integrating with `z'=2F` yields its lower polynomial for `F^2`; combined with `F>=z^2/sqrt(2)`, it gives `F>=z^2-100z`. At scale `beta`, this yields

`(log w_beta)'>=||D_beta||^2-101 beta^2`.

Integration of the radius-one-tube Hessian, including the additive tube terms, therefore gives the two-time bound `exp(2100)[w(t)/w(u)]^3`. The first-layer inactive directions are annihilated by the affine objective, so the bound applies in the full raw metric used in the nonlinear comparison.

The old same-state cap-uniform forcing bound is proportional to `e w(u)^3`. Keeping the propagator's denominator inside variation of constants cancels this factor and gives `E(t)<=C(e/lambda)w(t)^3`. This is a bound on the actual capped raw program and precedes the response closure.

The existing independent primal threshold is `e<=c_* delta^(7/4)`. Since `delta^2<=delta^(7/4)` on `(0,1]` and `c_poly<=c_*`, the new theorem satisfies it without using an old source-response threshold. It supplies the strict radius-one margin, the endpoint prediction at least `5/4`, and the absolute trained activation-regression margin.

The nonaffinity argument itself is valid. Frozen inactive Gaussian fields and affine balance/radial lower bounds give sample preactivation variance at least `1/404`. The third-Hermite calculation supplies the positive absolute `eta_*`. The square root of the optimal arctangent regression error is 1-Lipschitz in `W_2`, since an optimal slope can be chosen in `[0,1]`. Thus the strong forward comparison preserves regression error at least `e^2 eta_*/4` on the full feature interval. No Gaussianity of the trained nonlinear fields is assumed.

## 3. Weighted source transfers and deterministic closure

The affine source estimates retain the exact independent-root probe interpretation. Injection costs are evaluated at the source time, output costs at the observation time, and every strict pulse retains its mesh factor. The probes are not replaced by an unidentified generic raw tangent.

The radial integral estimates for `w`, `w^2`, `w^4`, and the tail integral of `w^-2` follow by splitting at readout norm one and integrating `dt<=sqrt(2)c^-3 dc`. Their sufficiently fine positive-mesh forms require no minimum step.

The weighted product calculations are correct. In `F B3 V`, the derivative and learned-moment portions of `B3` produce respectively the integrands proportional to `w(q)` and `w(u)^-2 w(q)^5`. Reversing the latter integration and using the inverse-square tail bound yields the claimed `FL` weight. The analogous two integrands for `V B3 F` yield the claimed `RF` weight. In particular the learned-moment part of `B3` is not discarded.

The enlarged active backward row radius is legitimate: normalized excess is `O(r H^-100 M^3)`, and its weighted Neumann ratio is bounded by this quantity times `C log(exp(1)30M)`. The inactive integration row has size `O(M^4)` and is controlled by its separate `H^-100 M^-4` radius.

The final companion correctly limits nonlinear `R1,R2` claims to complete rows. Arbitrary backward row errors need not preserve their strict densities. The strict forward transfers `F,V` and the one-sided reverse-resolvent identity provide the actual estimates used later; the response proof requires no unsupported nonlinear strict-density estimate for `R1-I` or `R2-I`.

The supersolution retains all three required sandwiches, including `V J3 V`. The first-forward error gives the charge `M J2+`; the second-forward sandwich forces the larger charge `M^3 J3+`. Direct forward defects cost `M^10`. Reconstruction by `W*-W=a^2 L J3 R*` gives the stated backward interiority. The inactive comparison is triangular and includes current diagonals. Positivity belongs to the affine majorant and finite chronological map, not to the actual signed nonlinear coefficient arrays.

The resulting sufficient criterion is therefore the displayed one:

`D=M^10(E2+ + E3+) + M J2+ + M^3 J3+ + E2- + E3- + M^4(J2- + J3-) <= H^-200`.

## 4. Sector source calculation

The primitive covariance bounds concern the actual raw source laws. The active average of arctangent is bounded pointwise by the active preactivation. Together with the weighted raw comparison, this gives active feature discrepancies `Ce w^3`, `Ce w^4` and active feature norms `Crw`, `Crw^2`. The common readout makes the top backward contrast `O(e w)`; applying the true adjoint and next gate gives middle contrast `O(e w^2)`.

Consequently the inactive reverse Gaussian scales really are `CeM^2,CeM`, while the active forward Gaussian scales are `CM^-3,CM^-2`. No inverse covariance, covariance domination, or derivative of a covariance square root is needed. Solving the exact same-array value equations with these scales gives incoming subGaussian powers `M^10,M^9,M^7` for `q1,q2,C`.

The derivative identities retain `Lgate`, both linear bounded-gate/B terms, and the quadratic gate/B term. Deterministic coefficient blocks are sector diagonal by exchange equivariance; random gates remain full two-by-two matrices. In particular `P--` contains the large `B+` only through `DeltaV-+ B+ DeltaG+-`, with two amplitude factors.

The two-sector majorant is valid: with `K_u=diag(u,1) 11^T`, one has `K_u^2=(1+u)K_u`. Its exponential formula gives the displayed active-source and inactive-source cross-derivative bounds, including the direct inactive source identity and every past-source mesh factor. The causal running maximum is used only inside this pathwise estimate; the final moment bounds are suprema of individual-time norms, not moments of a random temporal supremum.

The derivative envelope is controlled under `e H^200 M^16<=1`. Its largest stochastic coefficient is `e H^175 M^14`; deterministic B terms are smaller. Weighted Jensen works for arbitrary time correlations. After these exponential moments are established, Hölder can use the actual raw `L^2` incoming powers `3,2,1` for single-curvature insertions. Cross returns use the higher source moments and preserve their two amplitude factors.

The decisive exponent calculations check:

| Forcing contribution | Power before amplitude reduction |
|---|---:|
| Active first-forward diagonal | `e M^(-10+4+9)=e M^3` |
| Active second-forward diagonal | `e M^(-6+4+7)=e M^5` |
| Active forward cross returns | `e^2 M^18`, `e^2 M^20` |
| Active middle/top backward rows | `e M^15`, `e M^12` |
| Inactive middle/top cross returns | `e^2 M^19`, `e^2 M^17` |

The `e H^200 M^16` condition converts the two-insertion prefactor `H^350` into `H^150` and removes sixteen powers of `M`. This gives exactly the claimed final sector table. The learned forward and backward moment estimates are smaller than the applicable final bounds; the inactive backward moments start quadratically in `e` because their affine counterparts vanish.

The numerical ledger tracks the delivered `H^40` transfer coefficients. Value products fit `H^81`; incoming scales fit `H^94`; the global exponential coefficient fits `H^175`; cross generation and return fit `H^350` before reduction. The final `H^200` forcing envelope therefore does not silently reuse a saturated single-H bound.

## 5. Unchanged numerical coefficient and delta-cubed inclusion

Inserting the source table into the closure criterion gives the eight powers

`13,15,16,15,13,11,7,5`.

Their maximum is 16, so `D<=8 H^200 e M^16`. Since `M^16<=24^4 delta^-2`, the stated coefficient gives

`D <= 8*24^4*10^-70 H^-200 < H^-200`.

The numerical factor `24^4` remains explicit; no additional H power is spent. The same choice also supplies `e H^200 M^16<1` and the old primal/nonaffinity threshold. Amplitude homotopy at each fixed cap and mesh therefore cannot reach the outer-box boundary.

Thus the proof really uses the old numerical `c_poly=min(1/4,c_*,10^-70 H^-400)`. It does not introduce an unspecified smaller constant. Since `delta^3<=delta^2`, the requested cubic-power amplitude is included with exactly this coefficient; so are the fourth-, tenth-, and eight-hundredth-power choices.

## 6. Downstream hypotheses and complete original conclusions

The completed source proof supplies bounded primal capped paths through the affine endpoint, uniform incoming subGaussian tails, and endpoint prediction exceeding one. These are the premises needed by the old downstream arguments; their old source-amplitude selections are replaced, not imposed again.

| Original conclusion | Checked bridge and necessary input |
|---|---|
| Autonomous uncut strong feature path | Asymmetric gate comparison has one linear cap factor; Gaussian reference tails dominate `exp(CR)`, giving uniform strong state and direction limits. Scalar differentiability and the strong chain rule identify the limit as the true raw gradient field. |
| Global physical population path | Equal folded predictions and an endpoint above one give a first hit of one; a bounded derivative makes the physical clock diverge there. Capped reference monotonicity is unnecessary. |
| Nonsymmetric uniqueness and reached-state restart | The physical asymmetric comparison retains each competitor's actual residuals and uses only reference tails. Restart errors still decay after the comparison exponential. |
| Finite GF and simultaneous raw GD | Fixed-program Gaussian laws are applied at fixed cap and auxiliary mesh; deterministic Euler estimates and rank-one unrolling supply the finite primal bounds. Width is taken first, then auxiliary mesh/cap limits. The GD defect is `C_(R,T)n^-2`; the actual finite random readout is retained. |
| Actions, adjoints, and full kernels | Common generated spaces use finite Gaussian operator bounds and exact transpose pairings. Strong rank-one increment comparison and convergent probe inputs retain both orientations; products of `L^2` fields give all off-diagonal as well as diagonal kernel entries. |
| Hidden velocity laws and moments | Product observations are first truncated to satisfy the fixed-program derivative hypotheses. Cap removal is performed at fixed reference-velocity truncation, followed by truncation removal using the compact continuous `L^2` image of the uncut velocity. No cap-growth bound on fourth-moment constants is presumed. |
| Same-layer path laws and integrated speeds | Fixed-grid joint laws combine with the interpolation bound `||x-I_hx||_infinity^2<=4h integral |x'|^2`. Raw-GD one-sided node directions are retained. |
| Nonaffinity and initial feature learning | The absolute regression margin passes through strong cap removal. Initial Gaussian support, full reused-transpose covariances/returns, adjunction, and exchange symmetry give nonzero hidden-block and every-sample/layer accelerations and changing projected kernel for every positive amplitude. |

The normalization variant also remains inside the proved gain/amplitude rectangle: for `0<r0<=c_poly delta^2`, dividing `z+r0 arctan z` by its Gaussian `L^2` norm gives gain in `[1/2,1]` and nonlinear coefficient at most `r0`. Literal nontrivial convex weights still have Gaussian energy less than one; the candidate makes no contrary assertion.

The conclusion concerns every fixed dataset and finite physical interval, along the full width sequence in probability. It does not establish a supremum over datasets, uniform convergence on the infinite half-line, exponents below two, optimality of exponent two, or a practical prefactor.

## 7. Separate three-input assessment

The corrected three-input note has no remaining substantive issue found. Its cubic tensor dual construction gives `Gamma^(circ 3)>=(delta(2-delta))^2 I/3` without a rank assumption. The nonzero third Hermite coefficient and subsequent Gaussian linear projections give the stated initialization Gram bounds. Its matching `Theta(e^2 delta^2)` statement is now correctly restricted to `d>=2`, `0<delta<=1/4`, `0<e<=1/2`; the unrestricted statement would fail at `delta=1`.

The equilateral equal-label affine population is exactly stationary at loss `3/2`. This is not a counterexample to the positive-amplitude theorem. The exact Gram-null feature-sum identities and bounded arctangent give the necessary fitted-state bound

`R >= (pi e)^(-1/3)-11`,

and, conditional on a true strong GF reaching the stated fitting criterion,

`T >= (2/3)[(pi e)^(-1/3)-11]_+^2`.

The scalar ascent lemma is correct under its explicit strong-existence and chain-rule premises. Monotonicity of `J/||C||` gives `J'>=||H0||^2`, a first-hit certificate at most `||H0||^-2`, and length at most `||H0||^-1` before hitting. The finite endpoint follows from the energy/Cauchy estimate, but local continuation is correctly not inferred for a merely continuous infinite-dimensional field. In the conditional symmetric equilateral case the physical scalar equation and the `Theta(e^-2)` certificate scale follow.

Substituting that growing clock into the current affine exponential smallness condition fails for all sufficiently small `e`. This is failure of that sufficient certificate, not a proof that fitting is impossible. The radial-clipping cancellation example and the lack of strong compactness from Galerkin energy bounds accurately identify limitations of the two suggested regularizations.

The note correctly leaves the generic three-input global construction, adequate source control, nonsymmetric uniqueness/restart, trained nonaffinity, and full finite-dynamics observable identification open. Neither initialization positivity nor the conditional symmetric scalar lemma supplies those missing hypotheses.
