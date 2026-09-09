# Independent complete-theorem bridge review

Verdict: **PASS**. No substantive mathematical proof gap or quantifier gap remains for the theorem in the four-file candidate, with the scope stated in CONTRACT.md. The local cap-field scope correction requested during this review was checked in the final files.

Review date: 2026-09-07. This is an independent adversarial review of the candidate and its original mathematical dependencies. No sibling or historical review/status files were consulted. Historical status sentences appearing inside supplied mathematical sources were not used as premises. No proof file was edited, no agent was delegated, no numerical experiment was run, and no commit was made.

## Inspected version and source scope

CONTRACT.md, CANDIDATE_HASHES.json and all four candidate mathematical files were read in full. Each candidate SHA-256 agrees with CANDIDATE_HASHES.json:

| File | SHA-256 |
| --- | --- |
| PROOF.md | `a4d6ed0ee99a1e111b5eba068f2219cf561a2281b1828b26227aca7a0a54a050` |
| AFFINE_CORE.md | `634dd3bbc35436e9d1760bee5c11cbf2124b3c42e8920a1bf3a4fcbb15039711` |
| SOURCE_AND_LIMIT_BRIDGE.md | `2a140f2a5a39f911b5c2ca51bc79102d20e9209f1450d38005360c88103f6e77` |
| INITIAL_MOTION_AND_NORMALIZATION.md | `c96316fdc481ef3f9e6fc402514ca9b45bcff12e199023505fbbb86d4e15bf24` |

The original THREE_SAMPLE_CONTROLLED_RESPONSE_LEMMA.md, TWO_SAMPLE_SOURCE_BASELINE.md mathematical sections 1–9, NONLINEAR_RESPONSE_PERTURBATION.md mathematical sections 1–8, PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md, FIXED_CAP_VELOCITY_BRIDGE.md, PREVIOUS_TWO_SAMPLE_PROOF.md, and INITIAL_FEATURE_LEARNING.md were inspected substantively. For L3_LOCAL_COMPLETE_PROOF.md, the fixed-program conditioning, derivative-response identification, singular-query regularization, empirical-feedback identification, and countable common-action/adjunction construction were read directly. The original symmetry and strong radial/trajectory-chain-rule sections of SYMMETRY_RADIAL_CLOCK.md were also inspected. The old shifted affine coercivity and variance formulas were not substituted for the new odd-family arguments.

All eleven source files were independently hashed and agree with SOURCE_HASHES.json. Hash verification is distinct from the mathematical inspection scope just stated:

| Attached source | SHA-256 |
| --- | --- |
| ANGLE_SPECIFIC_THEOREM_ASSEMBLY.md | `27b2579f27ec14319dd39a93a4942d7b6463860648462d5ccb31b662c7725b75` |
| CONTRACT.md | `e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd` |
| FIXED_CAP_VELOCITY_BRIDGE.md | `a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0` |
| INITIAL_FEATURE_LEARNING.md | `bd81de0a7ad0cb9bdd1f27f89961f4a3b7a7da6914456ae08596a882fa2ec351` |
| L3_LOCAL_COMPLETE_PROOF.md | `f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4` |
| NONLINEAR_RESPONSE_PERTURBATION.md | `ef0ea077406a27307bc84e045feebf5099f6f81883bdfed41508035fe4559568` |
| PREVIOUS_TWO_SAMPLE_PROOF.md | `2891b892667396d64bd747689bcd59aa7ca3ffd224d3579fc3407bca0b623f9a` |
| PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md | `99eb60a64df1bbf4d8b70f351198abced9ef7eaeacf9b39c3997da5700a8f066` |
| SYMMETRY_RADIAL_CLOCK.md | `40882fc19e44b4b9245156595bb1071bd4de6007d619fada54c9fce7c37903f4` |
| THREE_SAMPLE_CONTROLLED_RESPONSE_LEMMA.md | `49da0f68047b4f516d3ad3c94b7112259838bcebf68e2296a948364232842789` |
| TWO_SAMPLE_SOURCE_BASELINE.md | `a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f` |

## Checked obligations

1. **Exact model, metric and raw GD.** Differentiation of the loss under the stated metric gives the factors 1/d, 1/n and 1 in the first, internal and readout updates. The four kernel blocks have the corresponding normalization. The proposed GD is simultaneous Euler in those raw coordinates at eta_n = n^-2. The finite readout has RMS order n^-1, and its treatment as a vanishing initial discrepancy does not replace the actual finite initialization by zero.

2. **Label sectors and population symmetry.** Oddness and evenness of the derivative give exact finite label folding, including backward fields and every update. The folded correlation is tau*rho. Reflection of the folded inputs and deterministic limiting contractions give equal folded predictions before any appeal to uncut uniqueness. Closing the generated probes under reflection realizes the symmetry on the common spaces. Thus all four binary label choices are covered. Finite trajectories are not assumed individually symmetric.

3. **Uniform affine reference.** The active/inactive equations in AFFINE_CORE.md (4) have the correct factors a, a^2, a^3 and v_u. The raw polynomial field is locally Lipschitz. From C'' = J J* C, convexity of ||C|| gives ||C'|| >= ||H(0)||. The energy identity, strong endpoint estimate, and local continuation therefore justify the first hit of g = 3/2, S <= 192/delta, and raw displacement <= 12 sqrt(2/delta). These estimates use only projected initial first-layer norms, not a false dimension-independent bound on the full initial raw norm.

4. **Inactive freezing and Gaussian nondegeneracy.** This part uses conditional independence in a finite affine program, rather than an arbitrary bounded-operator assertion. The independent inactive Gaussian root Q_0 has conditional covariance v_v I. Bounded Frobenius learned increments yield E[||T_n Q_0||_n^2 | F_n] = v_v ||T_n||_F^2/n, and the product increment B_s A_s - B_0 A_0 has the same boundedness property. Conditional scalar contractions also tend to zero. Fixed-program limits, then strong affine Euler limits, justify the exact frozen population fields and zero active/inactive covariance. The source programs remain linear in Gaussian coordinates with deterministic contractions. Consequently the affine scalar fields are centered Gaussian with variance at least delta/32 and standard deviation at most U^3. Both endpoint exclusions are used.

5. **Finite-array premise.** The response lemma requires an actual finite-array bound at each fixed sufficiently fine mesh, not merely population operator control. The candidate supplies precisely this: bounded population affine Euler fields, the initial finite Gaussian operator bound, and exact rank-one unrolling bound the finite trained operator norms. The conservative p = 11 + 2U + 4 S_delta (2U)^3 leaves slack. There is no implicit operator-norm convergence of trained matrices and no claim about arbitrary coarse affine Euler meshes or growing-transcript probabilities.

6. **Zero offset and uniform gain extension.** The conditioning hypotheses hold because phi and the fixed-cap D have bounded continuous first derivatives and linear growth. Removing the offset changes neither formal derivative paths nor learned-memory terms. With a <= 1, every positive gain factor in the affine update, probe, derivative, and Volterra upper bounds is dominated by its gain-one bound. The displayed same-state bounds give raw-field error at most 40 e b^3 and affine Lipschitz constant 9 b^2. Substituting b = 2p gives the stated sufficient restriction e <= [640 p^2 S exp(36 p^2 S)]^-1. Thus the extension constructs one finite K from fixed numerical upper bounds; it does not take an uncontrolled infimum of gain-dependent thresholds.

7. **Exact conditioning and return recurrences.** The original conditioning proof retains both orientations of both independent matrices. Projection onto the old query span followed by Gaussian integration by parts produces the full input second-moment Gaussian covariance and the expected formal-source derivative correction. The independent-query regularization handles zero reverse sources and other rank drops without a limiting Gram inverse. Learned rank terms have their h_j c_j factors; response derivatives have no extra label factor. Covariances, controls and deterministic coefficients are frozen only in these formal derivatives. The chronological order remains a_k^2, a_k^3, b_k^3, b_k^2. In particular the current blocks are

   b^3_{ki,kj} = 1_{i=j} E L^3_{k,i},

   b^2_{ki,kj} = 1_{i=j} E L^2_{k,i} + b^3_{ki,kj} E[V^2_{k,i} G^2_{k,j}].

   The second return is present. Formal slots remain distinct at singular covariance; correlated samples do not create off-support directional derivatives. The original affine recurrences and expanded difference inequalities preserve these facts after the gain change.

8. **Response closure and tails.** The single-transpose-source derivative keeps its h_j factor. Forward-source rows use sums of block norms, so the proof does not lose a factor proportional to the number of times. The backward-output derivative retains the current multiplier (1 + e Q_k), and the exponential envelope contains the past weighted sum of Q_r. The subGaussian coordinate estimates and convexity bound control every required envelope moment without a random time supremum. The four-stage induction only uses rows already constructed at its current stage and closes with E_k <= K e + K sum_{r<k} h_r E_r. This supplies the actual cap- and mesh-uniform incoming-field tails.

9. **One coefficient and nonaffinity.** All constants entering e_delta are functions of delta alone. Each dataset stops at its own affine S, with S_delta only an upper bound. The direct strong comparison has a strict primal margin, the forward comparison is at most J e, and the prediction comparison is at most O e < 1/4. The Gaussian regression minimum is positive on the explicit compact standard-deviation interval. The regression slope bound and L2 perturbation estimate correctly transfer it to the nonlinear law. Absorbing aZ gives the exact e^2 factor, and hence the positive uniform e^2 eta/4 margin on the complete feature interval.

10. **Cap removal and identification.** The asymmetric gate decomposition is algebraically correct. The incoming discrepancy is multiplied by at most 2, while only a forward-state discrepancy receives the O(eR) factor; backward substitution therefore produces a single linear R loss. Gaussian reference tails defeat exp(CR S). The common-space cap family is Cauchy in raw state and raw direction, including HS increments. Bounded continuous gates give continuity of the uncut raw field at the limit, identifying an autonomous strong C1 solution.

11. **Physical clock, uniqueness and restart.** The endpoint margin guarantees a first fitting hit for each cap and for the uncut path. Before the first hit, the clock is increasing; bounded g_R' makes its integral diverge at the hit even when g_R is not monotone. Physical cap references therefore exist for every finite horizon and inherit the uniform feature-interval primal/tail bounds. The physical asymmetric estimate retains the two individual residuals. Comparing a bounded-primal competitor against the cap reference requires tails only of that reference, so nonsymmetric competitors are included. Starting at a reached time adds an initial error already decaying like exp(-cR^2 + CR), still sufficient after the remaining Gronwall factor. No arbitrary-state existence is asserted. The uncut radial argument also gives the stated exponential loss bound with rate delta/32.

12. **Finite GF and the prescribed GD diagonal.** Fixed-cap, fixed-mesh conditioning identifies each actual residual and learned contraction. Rank-one unrolling supplies a larger finite primal ball with slack. The deterministic local Euler defect and stopped comparison have constants independent of width at fixed cap, permitting the auxiliary mesh to be removed. The same-width uncut-versus-cap estimate then removes caps after width. For GD the actual interpolant direction is the uncut field at its preceding node; comparison there to the cap reference adds C_{R,T} eta_n. Therefore eta_n = n^-2 is covered without identifying a Gaussian transcript of increasing length or requiring a width-uniform uncut Lipschitz constant.

13. **Velocity and path topologies.** The original fixed-cap proof first uses Gaussian probes to bound expected derivative rows, then an explicit causal estimate to bound absolute derivative rows. Its two appended forward velocity queries preserve source corrections and learned memories. The products phi'(Z) P are first smoothly truncated; L2 input convergence, bounded action norms and dominated convergence of the formal derivatives remove those truncations. The deterministic velocity comparison truncates only the reference P in a gate difference, with one factor M. Population cap velocities are compared first against the continuous uncut L2 velocity; compactness of its time image gives uniform vanishing L2 tails. Width, cap and velocity-truncation limits are then taken in the stated order. This avoids an unproved growth bound on cap-dependent moments. The interpolation inequality 4h integral |x'|^2 upgrades fixed-time joint laws to W2 on continuous feature/preactivation paths. Right-node and terminal-left raw-GD velocity conventions are retained. No continuous velocity-path law or cross-layer neuron coupling is claimed.

14. **Initial motion and normalization.** Full support and strict monotonicity make every initial feature Gram positive definite. Nonconstant phi' makes the full S_3 Gram positive definite, and the full-covariance reused-transpose innovations yield S_2 > 0 and the lower conditional variances used at layer one. The HS trace identities and adjunction certify all hidden blocks and aggregate upper-layer sample motion; reflection equates the two sample norms, proving each sample moves. Strong initial expansions use bounded-multiplier convergence, not Frechet differentiability of the feature Nemytskii map. The physical factors s'(0) = 2 and s''(0) = -4 kappa_0 give 4V and the stated kernel coefficients. The readout velocity and acceleration are also consistent. Both positive normalized coefficient families lie in the proved rectangle for sufficiently small parameters fixed from delta. A genuine convex mixture strictly contracts |G|, so its incompatibility with exact unit Gaussian energy is correctly stated.

## Revision checked and remaining gaps

PROOF.md (7) now asserts only the scalar prediction and loss identities for both capped and uncut constructed paths. The following sentences correctly distinguish dot Theta = 2(1-g) grad g for the uncut field from dot Theta_R = 2(1-g_R) V_R for an auxiliary cap. AFFINE_CORE.md section 1 now makes the same distinction and explicitly limits the gradient/kernel derivative identity to the uncut field. These statements match SOURCE_AND_LIMIT_BRIDGE.md section 4 and the actual first-hit clock proof.

The revised PROOF.md was reread in full, including the restored LaTeX separators. The revised AFFINE_CORE.md paragraphs were read and reversing precisely those paragraph changes reproduces its original inspected SHA-256, certifying the remainder is unchanged. The two unchanged companion hashes were rechecked, and all four final hashes match the refreshed CANDIDATE_HASHES.json. No remaining substantive gap or local cap-field scope defect was found.

## Final assessment

**PASS for the complete theorem at the inspected hashes.** No substantive remaining proof or quantifier gap was found. The theorem covers every fixed admissible two-input dataset and every finite physical horizon using a single positive e_delta for each delta, uniformly for a in [1/2,1]. The proof does not extend this to an endpoint, to a coefficient uniform as delta tends to zero, to uniform-in-dataset width convergence, to an infinite-horizon width limit, or to three inputs.
