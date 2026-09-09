# Independent complete-proof review B

Date: 2026-09-07.

**Verdict: PASS for the revised candidate identified below.** All conclusions in Section 1 of `PROOF.md`, with the observables and qualifications in Section 2, are supported by the supplied proof and the mathematical dependencies actually used. No required correction remains. This verdict includes the controlled response lemma, global population construction and uniqueness, finite GF and exact raw GD, all stated velocity/path topologies, uniform nonaffinity, and every asserted initial-motion certificate.

This was an independent adversarial proof review. I read the rigorous-mathematics skill. I did not inspect README/status files, ledgers, other reviews, sibling candidates, task history, or preparation notes. No experiment, delegation, or candidate edit was performed. Source files' status assertions and references to previous audits were not accepted as mathematical premises.

## Exact coverage

- `PROOF.md`: all 565 lines, including the theorem's quantifiers, raw normalization, canonical state, all constants, controlled-clock argument, cap removal, continuation, finite GF/GD comparisons, velocities and path laws, and both nontriviality requirements.
- `CONTROLLED_RESPONSE_LEMMA.md`: all 386 lines, including the expanded derivative and deterministic difference calculations in Section 7. I independently tracked all gain factors, sample/block norms, source-step factors, current terms, and causal dependencies.
- `GEOMETRY_AND_INITIAL_MOTION.md`: all 343 lines of the initially supplied version. The sole subsequent correction in Section 4 was checked directly and its exclusivity was verified by hashing the revised file after reverting that one line in memory. The resulting hash is exactly the initial geometry hash below.
- `CANDIDATE_HASHES.json` and `SOURCE_HASHES.json`: read and checked against actual file hashes at the beginning and end.
- `sources/L3_LOCAL_COMPLETE_PROOF.md`: lines 1–730, including the complete fixed-program Gaussian-conditioning proof, source-derivative identification, singular-query regularization and zero-noise proof, empirical-feedback identification, and complete common-action construction with bounded extensions and adjoints. Its later specialized one-sample local arctangent theorem is not imported into this candidate. The downstream response, comparison, and velocity arguments actually used here were read in their complete separate source files.
- `sources/TWO_SAMPLE_SOURCE_BASELINE.md`: all 950 lines. In particular, the finite-program extension, actual derivative conventions, Gaussian-probe identity, affine row bounds, and finite/population primal-premise transfer were checked.
- `sources/NONLINEAR_RESPONSE_PERTURBATION.md`: all 930 lines. The bounded-prefix moment estimates, derivative envelopes, same-array perturbation, four-stage deterministic closure, and both current returns were checked against the new gain/control version.
- `sources/PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md`: all 322 lines. The reference-only gate comparison, single linear cap loss, existence/uniqueness/restart argument, actual-residual finite comparisons, exact-GD comparison, ordered velocity limits, and path interpolation proof were checked.
- `sources/FIXED_CAP_VELOCITY_BRIDGE.md`: all 690 lines, including its nonlinear probes, absolute derivative rows, both appended action queries, product truncation and removal, deterministic velocity comparison, and finite GF/raw-GD node conventions.
- `sources/INITIAL_FEATURE_LEARNING.md`: all 197 lines, including both initial transpose laws, their smooth truncation justification, and the strong initial expansions.
- `sources/SYMMETRY_RADIAL_CLOCK.md`: all 908 lines. Its strong chain-rule and adjunction arguments were checked; its two-sample symmetry and scalar-clock conclusions were not used as three-sample premises.
- `sources/CONTRACT.md` and `sources/ANGLE_SPECIFIC_THEOREM_ASSEMBLY.md`: read in full for normalization and dependency scope. Their old theorem/status conclusions were not imported.

## Substantive checks

### Geometry, initialization, and constants

The mixed-sign reduction for the augmented Gram is valid, including zero coefficients and singular ordinary Grams. Its two-variable matrix has determinant (D^2), trace at most four for (D\in[\delta,2]), and hence minimum eigenvalue at least (\delta^2/4). Since ((\alpha_1+\alpha_2)^2\ge\alpha_1^2+\alpha_2^2), this proves the claimed bound in the original three-coordinate norm. The feasibility endpoint (\delta=3/2), empty class for larger separation, and the order-sharp example check out.

Projection onto the underlying independent Gaussian roots gives the stated initial feature-Gram inequality even at singular covariance. Common marginal variance makes the first-chaos coefficient common across samples, and its coefficient is at least (a). Thus the PSD remainder argument really gives (Q_3\succeq a^6\lambda I), rather than merely separate diagonal inequalities.

I checked the displayed forward/backward norm bounds, hidden speed sum, arbitrary positive-Euler-mesh displacement estimate, feature displacement inequalities, and Gram perturbation constant. The chosen (a_\delta) gives every strict inequality in (13). In particular, the top preactivation displacement is below (t_*), while the readout and hidden contributions leave the claimed coercivity margin. These estimates use the prescribed raw normalization; no factor of (d), (n), or number of samples is lost.

### Controlled Gaussian responses

The canonical source equations preserve full time/sample covariance and the independent named source groups. The original conditioning proof applies to three samples because they add finitely many calls with the same admissible coordinate instructions. Its independent query-noise argument handles singular input/query Grams without continuity of a pseudoinverse. Formal source slots remain separate when their realized Gaussian values coincide.

The gain modification is consistent. In particular, the affine derivative equations for (F,V,U) have the displayed (a^2) feedback factors, (U) has direct forcing (aI), the readout derivative has direct forcing (a h_jc_j^T), and the backward outputs are (a\mathbf1T) and (a\sum b^3U). The indexed response block (a^2_{kj}) is correctly distinguished from the scalar gain squared.

Arbitrary deterministic time-varying controls enter only through (\|c_j\|_1\le1) and (\|\Gamma\operatorname{diag}(c_j)\|_{\infty\to\infty}\le1). No difference or derivative of controls is used. The affine comparison and probes retain precisely the same frozen control and mesh sequence. The bounded affine primal premise is supplied uniformly by the short controlled interval, including finite arrays via exact update lengths.

The probe proof supplies actual formal-response bounds: it first takes width to infinity at a fixed nonzero probe amplitude, then sends that amplitude to zero using finite-transcript continuity. It does not identify formal derivatives with an unproved finite-network trace limit. Signs are chosen for the finite deterministic derivative row, and conversion to sums of three-sample block norms has the allowed factor three.

Primal nonlinear-affine comparison precedes and independently bounds the Gaussian source variances. Under a bounded coefficient prefix, Minkowski and discrete Volterra estimates give the (K\sqrt p) moments. The derivative envelopes retain the current backward multiplier ((1+eQ_k)), and their integrability follows from Gaussian-square moments, the convex weighted exponential inequality, and Hölder. There is no random supremum over an increasing number of source times.

The same-array derivative-error estimates retain (h_j) for a single transpose source, including nonuniform meshes. Equations (22)–(26) in the companion's expanded calculation correctly give the four-stage bounds: first (a^2_k) from past (b^2); then (a^3_k) from current (a^2_k) and past (b^3); then (b^3_k); finally (b^2_k). Current-row estimates are not assumed before construction. Both diagonal current returns in (13), including the return through the other matrix, are present. Discrete Gronwall and a single sufficiently small positive (e_*(a,B,S)) therefore close the entire program uniformly in mesh, cap, covariance, and control variation.

### Physical clock, global caps, and uncut uniqueness

For capped physical dynamics, the hidden prediction contribution need not be positive. The proof correctly estimates its absolute operator norm and lets the strictly positive readout Gram dominate it. The resulting residual differential inequality gives

\[
\|r(t)\|_2\le\sqrt3 e^{-\lambda a^6t/2},\qquad
\int_0^\infty\|r(t)\|_1dt\le S/2.
\]

This is first proved before a clock-budget exit and then excludes that exit with strict slack. It does not use a clipped loss-energy identity or two-sample symmetry. If the residual is zero, the physical field is zero. Normalized zero mesh steps can be omitted. For nonzero steps, (h_j=\Delta t_j\|r_j\|_1) and (c_j=-r_j/\|r_j\|_1) represent the physical Euler updates exactly. At a fixed cap and horizon their total duration is eventually below (S). Consequently freezing these causal deterministic contractions and passing through fixed-cap strong Euler convergence is a valid application of the controlled lemma; differentiating normalized residuals is unnecessary.

The asymmetric gate estimate requires tails only of the reference. Through the three backward substitutions, an incoming error receives bounded action/gate coefficients while a new forward-state error receives one (R) factor. Thus the comparison constant grows linearly in (R), not cubically. Gaussian reference tails defeat its exponential Gronwall cost on each finite physical interval. This supplies uniform strong state and raw-direction convergence, hence a strong (C^1) uncut solution.

The common generated action space contains the countable programs needed for all caps, meshes, and integer horizons, with actual adjoints and HS learned increments. Overlap agreement and bounded strong endpoints give the global trajectory. The same asymmetric reference-only argument applies to any bounded-primal strong competitor on these action spaces and to restarts at reached states; no tail assumption on the competitor or general infinite-dimensional Peano theorem is needed.

### Finite GF, exact GD, velocities, and path topology

At fixed cap and fixed auxiliary mesh, the generic finite-program law identifies all actual residual contractions. The finite random readout is retained and has vanishing RMS initial size. Initial operator bounds and exact rank-update lengths supply finite primal bounds with slack; trained operator-norm convergence is not assumed. Width-independent fixed-cap Euler stability then identifies finite cap GF.

The uncut finite algorithms are compared to their same-width cap reference. For raw GD the raw direction is evaluated at the preceding node; comparison at that node and the cap reference's time modulus give a vanishing (C_{R,T}n^{-2}) defect. This avoids any uniform Lipschitz assumption for the uncut field and any Gaussian identification of a growing training transcript. Width is taken first at fixed cap, then the cap is removed. The same reference gives joint convergence of GF and GD along the full width sequence in probability.

The complete fixed-cap velocity proof applies after replacing the two sample coordinates by three and the unit affine derivative by (a). Its bounded coordinate derivatives, nonlinear Gaussian-probe argument, absolute source rows, and both appended forward-action queries retain all relevant returns. Velocity products are first smoothly truncated; the supplied (L^2) and derivative arguments justify their removal. Only (L^2\to L^2) action bounds are invoked.

The cap-removal order for velocities is correct: first establish strong convergence of population cap velocities using the continuous uncut (L^2) velocity path as reference; its compact time image has uniformly vanishing (L^2) tails. For finite comparisons take width first at fixed cap and velocity truncation, then cap to infinity at fixed velocity truncation, then remove the latter. No uncontrolled product of a cap-dependent moment constant with a cap error is used. The actual right/terminal-left raw-GD directions are covered.

Products of strongly compared (L^2) fields yield the four full kernel blocks, predictions, and loss. Uniform-time velocity laws give second moments and integrated squared speeds. The observation-grid inequality

\[
\|x-I_hx\|_\infty^2\le4h\int_0^T|x'|^2
\]

provides the missing path-space approximation and, together with fixed joint-time laws, proves the asserted (\mathcal W_2(C([0,T];\mathbb R^6))) convergence. No cross-layer neuron pairing, cross-width operator identification, or convergence uniformly on the infinite time half-line is needed or claimed.

### Nonaffinity and every initial-motion assertion

The regression formula proves (\eta_*>0): the error is positive at each finite positive Gaussian scale and has the positive limit (\frac{\pi^2}{4}(1-2/\pi)) at infinite scale. Standard deviation is (L^2)-Lipschitz, and the optimal perturbed arctangent slope has magnitude at most (\pi) when the perturbed standard deviation is at least (1/2). Testing that predictor at the initial variable proves the stated error transfer. The uniform displacement bounds apply in all layers and times, so (21) is justified without Gaussianity of trained fields.

For positive (e), the initial top backward Gram is positive definite by full support and the nonconstant derivative. Each reused transpose preserves an independent Gaussian component with the stated full second-moment covariance. Conditional covariance then gives nonzero first-block and every bottom-sample acceleration, including singular ordinary Grams. Positive feature/backward Gram trace pairings prove both upper parameter blocks move.

I independently checked the gain-dependent affine upper-motion formulas (5)–(6), the conditional covariance of (Q=B^*H), and the Gaussian trace moments used for the upper bounds. The scalar quadratic minima give exactly the denominators five and fourteen. The perturbation induction's displayed coefficients and powers of (a) are consistent, and (e\le(10^{10}a)^{-1}) makes the common error smaller than half each upper-sample affine lower bound. This establishes each upper sample separately; no exchange symmetry is imported.

With (p=y/3), actual physical time gives (C(t)=3tH+o(t)) and hidden displacement (9t^2V/2+o(t^2)). The projected readout block and hidden blocks each contribute (9t^2\|V\|^2) at leading order, giving the stated coefficient eighteen for the total projected kernel. Bounded-gate strong path chain rules suffice; Fréchet differentiability of the entire feature map on unrestricted (L^2) is unnecessary.

## Correction received during this review

The parent reported one arithmetic correction to the illustrative scalar-clock counterexample in geometry Section 4. For diagonal (q), off-diagonal (c), and (y=(1,1,-1)), the correct product is

\[
Q_3y=(q,q,2c-q)^T.
\]

I checked that calculation and verified that replacing this line by the original line in memory recovers the original file hash exactly. Since (c>0), the corrected vector is still not parallel to (y); the example's conclusion is unchanged. This example is not used in the theorem's proof. The final verdict concerns the corrected version. No other candidate or source content changed during this review.

## Hash record

The following are actual SHA-256 hashes. Initial hashes were recorded before the mathematical review; final hashes were checked after the reported correction. Both manifests agree with the corresponding actual files.

| File | Initial hash | Final hash |
|---|---|---|
| `PROOF.md` | `e319166dbdd3c0c8b8ddfc7c588642bbac67f4cc5c870f0513b1bdddc6633300` | same |
| `CONTROLLED_RESPONSE_LEMMA.md` | `49da0f68047b4f516d3ad3c94b7112259838bcebf68e2296a948364232842789` | same |
| `GEOMETRY_AND_INITIAL_MOTION.md` | `f9e8547ec4037b574496643d931f80a7d99f70a0c33215e7f6f3c33d21499c74` | `e19c6c7f04d4e182ee1988dcc1aef10b91a0081ac7fd4f3504735f4c61fa1422` |
| `CANDIDATE_HASHES.json` | `d8a91214ca80a86f0fdfe1447bc3f2bb9f9129b64346afdd6a5841549b3153c0` | `48c3d3ea34b0a46344bef893963e53fb9bf011b7a21340fb388e3ae52eb16a27` |
| `SOURCE_HASHES.json` | `e36f1696924912c0af5d7f7aa90c856d7f9ff064c486f212cf26f2eaafbe9af1` | same |

All nine attached source hashes were unchanged:

| Source file | Initial and final SHA-256 |
|---|---|
| `ANGLE_SPECIFIC_THEOREM_ASSEMBLY.md` | `27b2579f27ec14319dd39a93a4942d7b6463860648462d5ccb31b662c7725b75` |
| `CONTRACT.md` | `e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd` |
| `FIXED_CAP_VELOCITY_BRIDGE.md` | `a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0` |
| `INITIAL_FEATURE_LEARNING.md` | `bd81de0a7ad0cb9bdd1f27f89961f4a3b7a7da6914456ae08596a882fa2ec351` |
| `L3_LOCAL_COMPLETE_PROOF.md` | `f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4` |
| `NONLINEAR_RESPONSE_PERTURBATION.md` | `ef0ea077406a27307bc84e045feebf5099f6f81883bdfed41508035fe4559568` |
| `PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md` | `99eb60a64df1bbf4d8b70f351198abced9ef7eaeacf9b39c3997da5700a8f066` |
| `SYMMETRY_RADIAL_CLOCK.md` | `40882fc19e44b4b9245156595bb1071bd4de6007d619fada54c9fce7c37903f4` |
| `TWO_SAMPLE_SOURCE_BASELINE.md` | `a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f` |

**Required findings:** none for the final hashes above.

**Optional findings:** none affecting the theorem or its proof. The large numerical constants and existential response threshold are conservative but valid for the stated existence theorem.
