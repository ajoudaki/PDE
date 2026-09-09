# Independent complete-proof review C

Verdict: **PASS** for the final candidate hashes recorded below. There are no outstanding required mathematical changes. This verdict concerns the complete three-input theorem in PROOF.md, including its global population construction, strong uniqueness, exact raw-GD/GF limits, stated observables, all-time nonaffinity, and motion of every hidden block and every sample in every layer. It is not a verdict restricted to the initial-motion companion.

## Scope and independence

I read all three candidate documents and both hash manifests. I checked their arguments against the needed proofs in the attached sources: the finite-program Gaussian-conditioning, singular-query regularization, common-action construction, scalar predictor differentiability and strong multiplier/chain-rule portions of L3_LOCAL_COMPLETE_PROOF.md; the source representation, current returns, affine primal comparison and Gaussian-probe proof in TWO_SAMPLE_SOURCE_BASELINE.md; the primal, moment, derivative-envelope and four-stage coefficient proofs in NONLINEAR_RESPONSE_PERTURBATION.md; the full PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md and FIXED_CAP_VELOCITY_BRIDGE.md; and INITIAL_FEATURE_LEARNING.md. The old symmetry/radial-clock theorem is not a premise of this verdict. In particular, its sample-exchange step is not used to infer individual upper-sample motion.

I used solve-math-rigorously. I did not inspect status files, ledgers, other reviews, sibling tasks or preparation notes; I did not conduct experiments, delegate, or edit the candidate. The only candidate change during this review was made by the parent after I reported the nonblocking arithmetic error described below. I verified its exact extent by reversing the textual replacement and reproducing the original SHA-256 digest.

## 1. Geometry, normalization and the gain bootstrap

The raw metric and finite gradients have the stated factors: the first block is divided by d, matrix updates by n, and the readout update has no n divisor. Thus the displayed four kernel blocks have the correct normalizations, including the input Gram factor in K1. The loss is half the sum of three squared residuals.

The augmented-Gram proof is valid for every feasible triple, including singular ordinary Grams. In the mixed-sign case the projected two-variable quadratic has determinant D² and trace D²−2D+4≤4 for D∈[δ,2]. Its smaller eigenvalue is at least D²/trace≥δ²/4. The comparison A²+b²≥α1²+α2²+b² completes the lower bound without an inverse of Γ. The same-sign case and the feasibility bound δ≤3/2 are valid. The example demonstrating the order δ² is valid throughout its specified range.

At initialization, the constant and first Gaussian-chaos projections of a+az+e arctan(z) are orthogonal to the remaining chaos. Equal marginal variances ensure that the linear coefficient is the same for all three coordinates in a layer and is at least a. This gives Qℓ≽a²J+a²Qℓ−1, including singular Γ, and hence Q3≽λa6 I with λ=δ²/4. No pairwise-correlation entrywise argument is substituted for a positive-semidefinite matrix inequality.

I checked the controlled bounds and their numerical slack. On D≤1 the forward bounds 6a, 70a², 800a³ and backward bounds 2a‖C‖, 44a²‖C‖, 968a³‖C‖ follow from action norm 11 and gate norm 2a. The three hidden speeds sum to at most 1372a³‖C‖≤1400a³‖C‖. Integrating C′ first therefore gives the stated 560000a6s² bound, and its enlargement to D_S. The discrete inequality Σh_js_j≤s_k²/2 preserves this argument on arbitrary positive meshes. Consequently the affine finite-array premise really is available with B=12 and uniform slack; trained operator-norm convergence is not being assumed.

The choice of a makes all four inequalities (13) strict. In particular, a6≥6.4·10^19λ−3 gives D_S≤2.25·10−12λ, while the other lower bound on a4 gives 615a²D_S≤0.08856t*. The forward-displacement constants and three-column Gram perturbation bound in (14)–(15) are sufficient. The hidden cap contribution need not be positive, but its operator norm is bounded by 3(1400)²a6‖C‖²≤6·10^6a6C_S². Thus the symmetric part of the full residual operator is bounded below by λa6/2. The resulting residual decay and ∫‖r‖1≤6/(λa6)=S/2 close the stopped argument with slack. This proves global capped physical existence without a clipped energy identity or scalar sample symmetry.

## 2. Source-response extension and its causal closure

The fixed-program extension from two to three samples is legitimate: the conditioning argument is for a fixed finite transcript of reusable Gaussian matrix calls, not specifically for two sample coordinates. Both orientations and all sample/time cross moments are retained. The independent-query-noise proof passes to zero noise through finite covariance square roots and bounded-derivative coordinate expressions. It does not presume continuity of a pseudoinverse at a rank drop. The countable generated-space construction then supplies actual bounded actions and adjoints from finite norm and transpose identities.

I checked the response equations against rank-one unrolling. The explicit h_v c_v,j factors occur only in learned-rank additions; the response derivative itself has no extra such factor. Formal source slots remain distinct at singular covariance. Freezing deterministic controls, mesh and all population contractions is appropriate for the source derivatives. For the physical population Euler program, h_j=Δt_j‖r_j‖1 and c_j=−r_j/‖r_j‖1 reproduce the physical update exactly; zero-residual steps may be omitted. Fixed-cap Euler convergence and the strict clock slack place those meshes inside the one fixed budget S on every finite physical horizon.

The affine probe argument genuinely bounds response rows, rather than inferring such bounds from primal norms alone. It inserts a single independent root with chosen signs into the relevant answer slots, applies finite-dimensional raw stability before the width limit, and then uses Gaussian integration by parts and finite-transcript continuity. The single-time perturbation retains h_j; conversion to time sums of three-by-three block norms costs only a fixed sample factor. Gain a changes finite constants, not this argument. The nonlinear comparator uses precisely the same frozen controls as its affine comparator.

The cap-independent primal perturbation uses the same-state bounds |φ_e−φ_0|≤πe/2 and |D_e,R−aq|≤e|q|; it does not use an uncontrolled gate difference times an incoming field. This supplies variance and learned-moment bounds before response bootstrapping. Under bounded coefficient prefixes, the three explicit Volterra moment estimates give K√p without a random supremum over times.

The derivative calculation retains G−aI, V−aI and L, with |L|≤eQ. Its past-time exponential envelope alone would not control a backward output, but the document includes the necessary current factor (1+eQ_k). The convexity estimate for exp(θΣhQ) and the already proved sub-Gaussian one-time moments give the needed integrability of this factor. The same-array derivative subtraction preserves h_j for an individual reverse source.

I checked the affine recursions (11) and the expanded differences (22)–(26), including all powers of a and the order of block multiplication. The four stages are genuinely causal: a2_k uses past b2, a3_k uses current a2_k and past b3, b3_k is then available, and b2_k may finally use current b3_k. The second current transpose return in (13) is retained. No same-time inverse or simultaneous assumption on an unconstructed row is used. The resulting discrete Gronwall estimate selects a positive e*(a,B,S) uniformly in cap, mesh, controls and Γ. This discharges the response-tail premise for the actual physical reference paths with one coefficient independent of physical horizon.

## 3. Cap removal, uniqueness and the finite algorithms

The asymmetric gate estimate (18) is sufficient on bounded primal sets with a tail assumption only on the reference. Recursive backward substitution has one linear factor in R: each new R multiplies a forward-state discrepancy, while incoming discrepancies acquire only bounded gate and action constants. Lipschitz dependence of the physical residual contractions adds only bounded constants. Gaussian reference tails therefore dominate the Gronwall cost exp(C_T R), giving strong state and raw-direction errors tending to zero.

The cap limit is a strong C1 solution in the raw affine Hilbert space, with Hilbert–Schmidt matrix increments. Bounded continuous multipliers acting on a fixed L2 factor justify the forward and backward passage and the trajectory chain rule. The scalar predictor has the derivative required for the gradient interpretation by the fixed-backward-factor truncation argument; full L2-to-L2 Fréchet differentiability of a nonlinear activation is unnecessary.

The same asymmetric comparison applies to any bounded-primal strong competitor on the same action spaces without imposing that competitor's own tail hypothesis. The cap reference's error at a reached time is still Gaussian-small, so propagation from that time proves unique continuation. This establishes the stated autonomous uniqueness class and restart property, not just uniqueness inside a symmetric family.

At fixed cap and fixed auxiliary physical mesh, the generic source result identifies every causal residual contraction. The initial finite random readout remains in the finite algorithms; its RMS norm is O_P(n−1), and the fixed-transcript comparison sends it to zero only in the population limit. The rank-one length bounds supply the required larger finite primal ball. Width-independent fixed-cap Euler estimates and stopped comparisons then identify finite cap GF.

The uncut finite GF and the prescribed raw GD are compared to a same-width cap reference, keeping all three residuals. For raw GD the actual direction is evaluated at its preceding raw node; the comparison adds a fixed-cap error of order n−2. This argument neither assumes a width-independent Lipschitz constant for the uncut field nor applies a Gaussian theorem to a growing transcript. The width-first, cap-second limits give the claimed full-sequence convergence in probability, jointly for both algorithms.

## 4. Velocity, path and contraction observables

The fixed-cap velocity source proof extends by replacing the bounded two-sample coefficient sums with bounded three-sample sums and the unit gate constant with a. Its nonlinear Gaussian probes establish expected response rows, while its separate all-index causal recursion bounds absolute derivative rows. Those are different claims and are not conflated. The two additional forward-action velocity queries include their response corrections.

The unbounded derivative of the product φ′(Z)P is handled by first clipping P in an observational query. Its coefficient derivatives are dominated using the established absolute rows and moments, then the clip is removed in L2 with bounded action norms. No Lp operator bound for a Gaussian matrix is assumed. The strong trajectory chain rule gives continuous L2 population velocities.

For the final cap removal, the deterministic comparison has the stated single factor (1+M) on the state error. The order of limits is sound: compare population cap velocities to the uncut continuous L2 velocity path, whose compact time image has uniformly vanishing L2 tails; then use fixed-cap finite tail convergence, send width to infinity, remove the cap at fixed M, and finally send M to infinity. This avoids multiplying an uncontrolled cap-dependent moment constant by the cap-removal error. The node conventions are compatible with the actual raw interpolation.

Products of two converging L2 fields give every displayed kernel entry, predictions, loss and second-moment contraction. The interpolation inequality sup|x−I_hx|²≤4h∫|x′|² supplies path-space W2 convergence from joint observation-grid laws and speed bounds. Uniform-time velocity second-moment convergence gives the integrated squared speeds. Thus the proof supplies all the topologies listed in Section 2, rather than only fixed-time feature laws.

## 5. Every sample and layer moves; physical kernel changes

The nonlinear argument for the bottom layer is valid even where affine motion vanishes. Q1 is positive definite, so the upper initialized Gaussian preactivation vectors have full support. If a linear combination of β3_i=Hφ′(Z3_i) vanishes, continuity gives an identity on R3. H has no open zero set because every coordinate derivative p_iφ′ is nonzero. Differentiating the second factor then forces every coefficient to vanish when e>0. Thus S3 is positive definite. The complete first transpose return has an independent Gaussian component with covariance S3; conditional multiplication by gates at least a gives S2≽a²λ_min(S3)I. The next transpose independently supplies the required bottom noise. For each sample j, the j-th Gram diagonal term alone yields the strictly positive conditional variance in (4). The first parameter block is positive by the corresponding vector conditional covariance; both matrix blocks are positive by the positive-definite Gram trace pairing.

I independently reconstructed the affine upper-sample formulas. With u=m1+z_p, V2=a³Q⊗u and U1_j=a³c_jA*Q. These give U2_j=a4[(c_j+m)I+c_jAA*]Q. The second feature Gram contraction is a4c_j+(a²+a4)m, and propagation through B gives exactly the displayed T_j and U3_j=a5T_jH.

For the first upper bound, conditional Gaussian fourth moments give E_B Q=v and Cov_B(Q)=(a²m²+‖v‖_n²)I+vvᵀ/n, including the noncentral am Bᵀ1 contribution. The trace factor is (m+2c_j)²+c_j², whose exact minimum is m²/5. The asserted norm of v and the resulting gain powers in (7) are consistent.

For the top bound, T is even in B and Bv is odd, so the cross term vanishes in the deterministic polynomial limit. Orthogonal output-row invariance supplies the trace lower bound. The necessary Wick moments are τ(S)=τ(R)=1, τ(S²)=τ(SR)=2 and τ(R²)=3. In particular the stated finite identity for E_A tr(AA* M AA* M)/n is correct, including its 1/n term. Expanding τ(T²) gives [3c+(2+t)m]²+(2c+m)²+c²; minimizing in c gives (6+8t+5t²)m²/14. These arguments are valid for every c_j and do not require exchangeable sample geometry. The finite fixed-degree Gaussian contractions have converging second moments, as used in passing the conditional estimates to their deterministic population values.

All explicit perturbation constants in Section 5 check out. The three forward differences, three backward differences, rank-one differences and the two acceleration product rules yield respectively the stated coefficients 655, 15210, 325300, 65060, 32807, 6985680 and 143416183. The common constant 2·10^8a7 and e≤(10^10a)−1 imply an error at most a6/50, below half each affine lower bound a7/(9√5) and a6√(3/7)/9. Since |m|≥1/3 for three binary labels, this is one geometry-independent cutoff. The final eδ has additional slack and also meets the response cutoff.

In physical time, C(t)/t→3H, hidden velocity/t→9V, and hidden displacement/t²→9V/2. Writing J for the hidden linearization of H and V=J*H, the top readout kernel contributes 9t²‖V‖², while the three hidden kernel blocks together contribute another 9t²‖V‖². Therefore the coefficient 18 in (24) is correct without a scalar clock. The strict positivity of V proves a changing total kernel near zero. Bounded gates and strong fixed-factor convergence justify these expansions on the constructed C1 path.

## 6. Uniform nonaffinity

Every initialized scalar standard deviation is at least one. The arctangent regression error is positive at each positive Gaussian variance, continuous in its scale, and has the positive displayed limit as the scale tends to infinity. Thus η*>0. If an L2 perturbation has size at most t*, its standard deviation stays at least 1/2, and its optimal arctangent regression slope is at most π in absolute value. Testing that affine predictor at the original Gaussian gives the claimed error lower bound η*/4. The controlled preactivation displacement estimate is uniform over all physical times and passes through cap removal. Consequently the final activation has the stated uniform error e²η*/4, with e fixed independently of width and horizon; trained Gaussianity is not assumed.

## Required changes and optional clarifications

Required changes remaining: **none**.

One nonblocking arithmetic error was reported during review and corrected by the parent: in the orthogonal-input example, if Q3 has diagonal q and off-diagonal c, then Q3(1,1,−1)ᵀ=(q,q,2c−q)ᵀ. The original displayed vector used the convention Q3=qI+cJ instead. The corrected expression still proves failure of the scalar-clock symmetry. This example is not a premise of the global proof. The exact replacement and updated manifest were verified by hashes, as detailed below.

Optional presentation improvements only: the Wick-concentration sentence could include an explicit variance estimate for the finite polynomial contractions; and the initial-motion companion could define V1,V2,V3 together before its first use. Their definitions and the required moment/strong-limit arguments are already available from the displayed raw equations and attached source, so neither is a missing theorem obligation.

## Exact version record

The following tables record the SHA-256 values measured before reading the proof and after the parent's one-line correction. Every unchanged source digest was also verified against SOURCE_HASHES.json. Reversing only the corrected vector in the final geometry file reproduces its original digest; replacing only that digest in the final candidate manifest reproduces the original manifest digest. All other reviewed files are byte-for-byte unchanged.

| File | Before SHA-256 | After SHA-256 |
| --- | --- | --- |
| PROOF.md | `e319166dbdd3c0c8b8ddfc7c588642bbac67f4cc5c870f0513b1bdddc6633300` | `e319166dbdd3c0c8b8ddfc7c588642bbac67f4cc5c870f0513b1bdddc6633300` |
| CONTROLLED_RESPONSE_LEMMA.md | `49da0f68047b4f516d3ad3c94b7112259838bcebf68e2296a948364232842789` | `49da0f68047b4f516d3ad3c94b7112259838bcebf68e2296a948364232842789` |
| GEOMETRY_AND_INITIAL_MOTION.md | `f9e8547ec4037b574496643d931f80a7d99f70a0c33215e7f6f3c33d21499c74` | `e19c6c7f04d4e182ee1988dcc1aef10b91a0081ac7fd4f3504735f4c61fa1422` |
| CANDIDATE_HASHES.json | `d8a91214ca80a86f0fdfe1447bc3f2bb9f9129b64346afdd6a5841549b3153c0` | `48c3d3ea34b0a46344bef893963e53fb9bf011b7a21340fb388e3ae52eb16a27` |
| SOURCE_HASHES.json | `e36f1696924912c0af5d7f7aa90c856d7f9ff064c486f212cf26f2eaafbe9af1` | `e36f1696924912c0af5d7f7aa90c856d7f9ff064c486f212cf26f2eaafbe9af1` |
| sources/ANGLE_SPECIFIC_THEOREM_ASSEMBLY.md | `27b2579f27ec14319dd39a93a4942d7b6463860648462d5ccb31b662c7725b75` | `27b2579f27ec14319dd39a93a4942d7b6463860648462d5ccb31b662c7725b75` |
| sources/CONTRACT.md | `e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd` | `e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd` |
| sources/FIXED_CAP_VELOCITY_BRIDGE.md | `a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0` | `a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0` |
| sources/INITIAL_FEATURE_LEARNING.md | `bd81de0a7ad0cb9bdd1f27f89961f4a3b7a7da6914456ae08596a882fa2ec351` | `bd81de0a7ad0cb9bdd1f27f89961f4a3b7a7da6914456ae08596a882fa2ec351` |
| sources/L3_LOCAL_COMPLETE_PROOF.md | `f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4` | `f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4` |
| sources/NONLINEAR_RESPONSE_PERTURBATION.md | `ef0ea077406a27307bc84e045feebf5099f6f81883bdfed41508035fe4559568` | `ef0ea077406a27307bc84e045feebf5099f6f81883bdfed41508035fe4559568` |
| sources/PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md | `99eb60a64df1bbf4d8b70f351198abced9ef7eaeacf9b39c3997da5700a8f066` | `99eb60a64df1bbf4d8b70f351198abced9ef7eaeacf9b39c3997da5700a8f066` |
| sources/SYMMETRY_RADIAL_CLOCK.md | `40882fc19e44b4b9245156595bb1071bd4de6007d619fada54c9fce7c37903f4` | `40882fc19e44b4b9245156595bb1071bd4de6007d619fada54c9fce7c37903f4` |
| sources/TWO_SAMPLE_SOURCE_BASELINE.md | `a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f` | `a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f` |

PASS applies to the after hashes. No review outcome, status stamp or source-status assertion was used as a mathematical premise.
