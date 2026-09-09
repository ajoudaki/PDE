# Independent complete-proof adversarial review B

Date: 2026-09-07.

**Verdict: PASS for the full separated-input theorem stated in PROOF.md.**

The verdict covers the original finite model, the autonomous global population loss flow, full-sequence finite GF and raw-GD limits, every observable specified in Section 2, uniqueness and reached-state continuation, and both nontriviality certificates. It is not restricted to the new uniform coefficient calculation. I found no required mathematical repair and no additional unproved premise needed for the stated extension.

This certifies the quantifier with a fixed positive separation: for every delta in (0,2], one fixed positive coefficient threshold works for every allowed dataset and every finite physical horizon. It does not certify one positive coefficient for all correlations below 1 without a fixed separation, convergence uniform over datasets, or convergence uniform on the whole physical half-line. The candidate itself makes these distinctions.

## Independence, scope, and version control

I read all 527 lines of the candidate. I used only its supplied mathematical sources and the procedural solve-math-rigorously skill. I did not consult task history, README/status files, preparation notes, historical review files, sibling reviews, or other reviewers. I did not run experiments, delegate, edit the candidate, or edit any source.

I read the full affine/radial, two-sample source-baseline, nonlinear-response, primal/continuation, fixed-cap velocity, and initial-feature-learning proofs. Within L3_LOCAL_COMPLETE_PROOF.md I read the complete fixed-program Gaussian-conditioning proof, singular-query argument, common-action construction and fixed-cap flow discussion (lines 211–729), and the complete adjunction/gradient proof (lines 1748–1918). The original one-sample activation-specific bootstrap and transformed-coordinate GD arguments are not premises for this extension. CONTRACT.md fixes the model; ANGLE_SPECIFIC_THEOREM_ASSEMBLY.md was checked only for the dependency composition, not invoked as a theorem or an independent proof. Status language inside supplied sources was not used as mathematical evidence.

Candidate hash at the beginning and after the mathematical audit:

`2891b892667396d64bd747689bcd59aa7ca3ffd224d3579fc3407bca0b623f9a`

SOURCE_HASHES.json hash:

`e36f1696924912c0af5d7f7aa90c856d7f9ff064c486f212cf26f2eaafbe9af1`

All source hashes were independently checked against that manifest and checked again at the end of the mathematical audit:

| Source | SHA-256 |
| --- | --- |
| ANGLE_SPECIFIC_THEOREM_ASSEMBLY.md | `27b2579f27ec14319dd39a93a4942d7b6463860648462d5ccb31b662c7725b75` |
| CONTRACT.md | `e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd` |
| FIXED_CAP_VELOCITY_BRIDGE.md | `a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0` |
| INITIAL_FEATURE_LEARNING.md | `bd81de0a7ad0cb9bdd1f27f89961f4a3b7a7da6914456ae08596a882fa2ec351` |
| L3_LOCAL_COMPLETE_PROOF.md | `f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4` |
| NONLINEAR_RESPONSE_PERTURBATION.md | `ef0ea077406a27307bc84e045feebf5099f6f81883bdfed41508035fe4559568` |
| PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md | `99eb60a64df1bbf4d8b70f351198abced9ef7eaeacf9b39c3997da5700a8f066` |
| SYMMETRY_RADIAL_CLOCK.md | `40882fc19e44b4b9245156595bb1071bd4de6007d619fada54c9fce7c37903f4` |
| TWO_SAMPLE_SOURCE_BASELINE.md | `a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f` |

## Complete coverage and findings

### 1. Declared model, state, and observables: Sections 1–2

The raw metric gives exactly the displayed first-layer factor 1/d, the two hidden-matrix factors 1/n, and the readout update without an extra 1/n. Differentiating the loss (r_1 squared plus r_2 squared)/2 gives the two residual coefficients in (5). The four kernel blocks in (6) have the corresponding normalizations, including the first-layer input Gram factor and every off-diagonal entry. No one-sample coordinate transformation or learning-rate convention has been substituted.

The small finite readout has normalized size O_P(n^{-1}). The fixed-program comparison retains it, and the subsequent finite comparisons use the same finite initialization. The population readout zero is a limit, not a reset of finite parameters.

The first-layer full field is allowed to have raw initial size sqrt(d). Only normalized input projections and raw displacement enter activation selection. The velocity bridge can use a larger bound depending on fixed d; this changes convergence constants, not the coefficient threshold. The stated finite collection of fields and operators does not assert finite scalar dimension.

The initial Gaussian actions are obtained on generated spaces rather than postulated as arbitrary population initializations. In the fixed-program proof, conditioning retains both orientations of both matrices; the regression response is the expected formal source derivative. Independent query perturbations handle singular limiting query Grams without assuming convergence of pseudoinverses. The construction applies to a finite tuple of first-layer Gaussian coordinates, including the entire weight row and the singular projected pair at rho = -1. The nonlinear-part clipped gate has bounded first derivatives at each fixed cap, so it meets the fixed-program hypotheses.

The countable common-action construction includes bounded coordinate approximations and rational linear combinations. Its node span is dense in each generated L2 space. The finite Gaussian operator bound passes to these spans and extends both orientations continuously. The finite transpose identity then proves that the reverse actions are the actual adjoints. Rank-one training increments are Hilbert–Schmidt. This supplies the common state for strong cap/mesh comparisons without asserting cross-width operator-norm convergence of unrelated finite matrices.

### 2. Uniform affine interval: Section 3

The affine initial projected kernels are (7+rho)/2 and (1-rho)/2. Both are at least delta/2 on the declared range. The affine radial lemma gives both g' at least kappa_0 and the exact raw energy identity. Stopping at g = 3/2 gives S at most 3/(2 kappa_0), and Cauchy–Schwarz gives displacement at most 3/(2 sqrt(kappa_0)); these imply (8)–(9).

The affine existence proof is independent of nonlinear continuation. Its polynomial Hilbert-space field is Lipschitz on bounded balls; the energy estimate supplies a strong endpoint, from which the same local construction continues. It must therefore reach the target margin. Initial projected norms and action bounds yield U exactly as used. Replacing the duration by S_delta only bounds prefixes ending by each dataset's own S; it does not require extending an affine solution to S_delta after its target hit.

### 3. Nondegeneracy and regression stability: Section 4

For opposite labels, C' equals the signed top contrast. The radial lower bound on its norm, followed backward through D_3 = B D_2 and D_2 = A D_1 with action norms at most U, gives all three inequalities (10). Sign symmetry gives zero contrast mean and common/contrast covariance. For same labels, the supplied conditional finite-Gaussian calculation is sufficient: the contrast root is independent of the information driving scalar affine training, and bounded Frobenius learned increments act on that independent Gaussian root with vanishing normalized norm. The corresponding conditional pairing estimate gives zero common/contrast covariance. Thus the contrast variance stays v_D in each population. This is not an invalid inference from Hilbert–Schmidt boundedness alone.

These arguments give the uniform variance bound (11), including the antipodal endpoint. Forward propagation gives (12). Gaussianity is separately justified by the full affine source-program induction and strong L2 Euler convergence; positive variance alone is not used to infer nonaffinity.

The Gaussian parameter rectangle in (14) is compact, and every member is nondegenerate. The regression functional (13) is continuous there and strictly positive at each point by full support, so eta is positive. In (16), standard deviation is 1-Lipschitz in L2, and the optimal arctangent slope at Z is bounded by pi/m after the perturbation. Testing that affine approximation against Z_0 proves the displayed square-root error bound. This argument applies to the nonlinear, potentially non-Gaussian law.

### 4. One coefficient and every response premise: Section 5

The affine Euler bound 2U holds for sufficiently fine meshes by the bounded-ball Euler estimate. Source-baseline (32), with B_0 = 2U and duration bounded by S_delta, gives precisely the finite-array bound (18). The bound follows by unrolling rank updates and fixed-program convergence, not by an assumed trained operator-norm limit.

I checked the parameter dependence of the source and response proofs. The affine probe identities control both coefficient rows and individual past-source entries with their source-step factors. The nonlinear proof first establishes actual raw-state comparison and source-variance bounds, then controls coordinate moments and complete derivative rows. Its envelope retains the current multiplier. Its deterministic coefficient comparison closes successively through the first forward, second forward, top reverse, and middle reverse rows, retaining the current returns. The constants use only the affine primal bound, duration, and the displayed coefficient bounds. They use the input geometry through the bounded matrix Gamma diag(y/2); they do not introduce a covariance condition number, smallest mesh step, width, cap, or d-dependent initial full-field norm.

Substitution b = 2p into response equation (65) gives exactly the second entry of (R), 1/(480 p squared S_delta exp(36 p squared S_delta)). Thus (R) supplies a positive threshold depending only on the declared numerical arguments. The restriction to mesh families ending at their own S is consistent with the lemma's explicit hypothesis for the meshes under consideration.

The direct raw comparison has Lipschitz constant 9b squared for the affine field and same-state perturbation at most 40e b cubed. This yields Q in (17). The factor 1/2 in (19) leaves strict room in all stopping inequalities. Expanding the two forward actions gives the stated second- and third-layer preactivation bounds, hence J. The readout/prediction comparison gives O and preserves g_{e,R}(S) > 5/4. Every term in the minimum (19) is positive and determined before the data and physical horizon.

Finally (16) with the J bound gives arctangent regression error at least eta/4. Absorbing the affine part 1+Z gives exactly the factor e squared in (22). This transfers through strong cap removal and covers the whole constructed feature interval.

### 5. Autonomous physical flow and nonsymmetric competitors: Section 6

The asymmetric gate identity in the primal bridge has only one linear-in-R loss. At each backward layer the inherited incoming error is multiplied by a bounded action and bounded q derivative; the new R factor multiplies an already controlled forward-state difference. It does not generate a product of R factors across layers. The reference tail is enough; a competing path needs no tail assumption. Gaussian L2 tails therefore dominate the Gronwall factor and give strong state, Hilbert–Schmidt increment, and raw-direction convergence of the cap family.

The limit is an autonomous strong uncut gradient path. The forward chain rule and adjunction are valid along L2 paths using bounded gates and fixed-factor truncation; Fréchet differentiability of an arbitrary nonlinear L2-valued feature map is not assumed. The initial projected kernel is positive for the actual activation as well as for the affine reference. Constructed sample symmetry, the endpoint margin, and radial coercivity give the first hit s_* of g = 1. The clock (24) has exactly the factor needed for the stated physical loss, and bounded g' makes its integral diverge at s_*. One feature path therefore supplies all finite physical horizons.

For finite-cap physical references, monotonicity of their feature objective is not assumed: their first hit of 1 and bounded derivative suffice for the same divergent-clock construction. These physical references inherit cap-uniform primal and incoming-tail bounds from the bounded feature interval.

The physical comparison is written with both actual residuals. Its coefficient changes are locally Lipschitz on a primal ball and preserve the single linear-in-R loss. It therefore proves uniqueness against bounded-primal strong physical competitors even when they are nonsymmetric. At a reached time, the cap reference's initial discrepancy is already Gaussian-small in R; multiplying by a further finite-time exponential still sends it to zero. Existence after the reached state is supplied by the constructed global path. No unproved general Hilbert-space Peano theorem is needed.

For any fixed physical T, the removal cost has the form C_T exp(C_T R - cR squared). Its convergence requires no new smallness restriction on e depending on T.

### 6. Full width sequence, raw GD, and complete observable scope: Section 6

The finite reference construction takes width to infinity at each fixed cap and fixed auxiliary mesh. Its operator bounds come from the initialized action bound plus the finite sum of rank-update lengths. Population boundedness bounds the limiting sums uniformly over sufficiently fine meshes. Width-independent, stopped deterministic Euler estimates then remove the auxiliary mesh and identify fixed-cap finite GF.

The uncut finite GF is compared with that same-width reference by the asymmetric physical estimate. Fixed-cap uniform-time incoming tail convergence follows from the fixed-program laws and the fixed-cap time modulus. Taking width first and then cap size to infinity yields the stated full-sequence convergence in probability. Neither exact finite sample symmetry nor an increasing-transcript Gaussian limit is assumed.

For raw GD, the interpolation derivative is evaluated at its preceding GD node. Comparing there to the cap reference and then moving the latter to the current time adds C_{R,T} eta_n. This tends to zero for eta_n = n^{-2}. The argument does not require an n-independent Lipschitz constant for the uncut field and respects the right-node/terminal-left derivative conventions.

The fixed-cap velocity proof verifies the extra claims beyond state convergence. Nonlinear Gaussian probes bound the actual physical coefficient rows; the causal derivative estimate controls all source indices. The two appended forward-action velocity queries retain their Gaussian source and response terms. Their product instructions are justified by smooth truncations, L2 operator bounds, and convergence of expected derivatives, rather than being inserted into a theorem whose bounded-derivative hypotheses they fail.

The deterministic velocity comparison truncates the reference preactivation velocity and has error K[b + (1+M)a + reference tails]. In removing caps, population cap velocities first converge strongly using the uncut velocity as reference. The latter has a compact L2 time image and hence uniformly vanishing tails. For finite uncut versus finite cap paths, width tends to infinity at fixed R and M, then R tends to infinity at fixed M, and finally M tends to infinity. This avoids an unjustified product of cap-dependent velocity moment constants with cap-removal errors. It gives the uniform-time joint same-layer velocity laws, fixed finite-time joint laws, second moments, and integrated squared speeds asserted in Section 2.

All four kernel blocks and prediction/loss convergence follow from their actual strong-field comparisons and convergence of same-layer inner products. Both initialized and trained action orientations remain available on generated probes; no cross-layer coordinate pairing is introduced.

The path-space claim has its own valid step. Coordinate paths admit absolutely continuous versions with finite integrated mean-square speed. The observation-grid estimate bounds the averaged squared supremum interpolation error by 4h times that energy. Joint node W2 convergence at fixed grid, followed by h tending to zero, therefore proves W2 convergence on C([0,T]; R^4) for the paired preactivation/feature paths. Weak state convergence alone is not being used as a substitute.

### 7. Nontriviality and logical extent: Sections 6–7

The initial feature-learning lemma is applicable once the constructed C1 strong path exists. The shifted odd activation gives a positive-definite uncentered feature Gram even at rho = -1; the upper initial preactivation pairs are then nondegenerate. The beta_3 Gram is positive definite for every e > 0 because phi' is nonconstant. Both reused-transpose formulas retain the full Gaussian covariance and their response returns. Conditional covariance gives a positive beta_2 Gram and nonzero first-layer acceleration without an inverse input Gram.

The tensor Gram calculation proves strictly positive norm for each hidden matrix acceleration; the conditional lower bound proves the first-layer block acceleration. Forward differentiation and adjunction give a nonzero aggregate acceleration in each upper feature layer, and sample-reflection symmetry makes each sample's norm equal, hence positive. Bounded gates and fixed-factor L2 convergence justify the initial expansions under the actual strong regularity already constructed.

The projected kernel expansion has coefficient 2 times the squared hidden acceleration norm, as stated: one copy comes from the changing readout feature Gram and one from the hidden gradient blocks. Since s(t) = 2t + o(t), it certifies physical small-time kernel change and feature learning. It makes no unsupported claim of nonzero hidden velocity at every later instant. Combined with (22), it supplies every nontriviality conclusion in Section 1.

Section 7 states exactly the quantifiers proved by the construction. Constants for limiting comparisons may depend on the fixed dataset and T, while the selected activation coefficient depends only on delta. There is no stronger-than-source claim concealed in the final assembly.

## Required and optional findings

**Required findings: none.** No counterexample or missing proof obligation was found for the full stated theorem at the reviewed hashes.

**Optional findings: none needed for this certification.** The candidate already states the important scope boundaries, differentiability qualification, finite-readout convention, and ordered velocity/path limits explicitly.

**Final full-scope verdict: PASS**, under the model and quantifiers declared in Sections 1–2 and 7, with the supplied mathematical lemmas verified as above rather than accepted on the basis of review status.
