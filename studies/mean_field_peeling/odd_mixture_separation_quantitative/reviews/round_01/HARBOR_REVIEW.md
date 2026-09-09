# Independent adversarial mathematical review

**Verdict: PASS.** No substantive objection or required mathematical repair remains after reading the entire manuscript and checking its internal dependencies. This verdict concerns the results actually stated: the global odd-mixture theorem for two inputs, the three-input initialization results and explicitly conditional motion conclusions, and the separately stated shifted-activation theorem reproduced in Appendix C. It does not certify an unproved global theorem for generic three-input odd-mixture training.

## Input identity, complete coverage, and isolation

- Input: `/tmp/report-83c5f4e8d603/REPORT.md`.
- SHA256: `daa5a57856db4edc58e58f5f9efff12fbe6e0b442b503e1ef731eecfd444ae7b`.
- Size: 302,359 bytes; 5,743 lines.
- The hash was checked before reading and again immediately before saving this review; it was unchanged.
- Complete sequential reading used these bounded, nontruncated line intervals: 1–280, 281–560, 561–840, 841–1120, 1121–1400, 1401–1680, 1681–1960, 1961–2240, 2241–2520, 2521–2800, 2801–3080, 3081–3360, 3361–3640, 3641–3920, 3921–4200, 4201–4480, 4481–4760, 4761–5040, 5041–5320, 5321–5600, and 5601–5743. Every appendix, including all of Appendix C's Parts M, F, R, G, V, V.I, and N, was read. A subsequent heading search on the same input supplied locations for this review.
- Isolation complied with the assignment: no skills, AGENTS files, directory listings, other manuscripts, previous reviews, task history, web or external mathematical sources were consulted. No communication with other agents occurred. No numerical experiment was conducted. The manuscript was not edited. The sole written artifact is this review.
- All references below are to the reviewed input's line locations, named sections, or equation labels. Numerical inequalities were checked algebraically; no experimental result is being substituted for a proof.

## 1. Scope and principal conclusion

Theorem T.1 begins at line 90. Its quantifiers are appropriately restricted to realizable fixed datasets with absolute angular separation, one coefficient fixed before width and horizon, and limits on each fixed finite physical interval. It does not claim uniform convergence over all geometries or all physical time, and it does not interchange the infinite-width and infinite-time limits.

The distinction between the odd-mixture result and Appendix C's shifted-activation theorem is maintained. The odd-mixture proof uses the latter manuscript's intermediate results after checking changed hypotheses; it does not simply invoke Theorem M.1 with a different activation. The three-input chapter beginning at line 1633 explicitly leaves the global odd-mixture extension open. The singular affine obstruction identified there is an obstruction to the affine-reference route, not a purported counterexample to the positive-mixture theorem.

The finite raw metric gives exactly the stated first-layer factor 1/d, matrix factor 1/n, and readout factor one. The population rank-one operators have precisely the Hilbert–Schmidt normalization corresponding to ordinary finite Frobenius norm. The four kernels are the Gram blocks of the actual raw prediction gradients. No metric or transpose normalization discrepancy was found.

## 2. Specialized foundational dependencies

### Fixed Gaussian programs, including singular queries

Part F begins at line 2524. Its hypotheses are fixed finite instruction count, globally Lipschitz C1 coordinate instructions with bounded first derivatives, independent iid root tuples with finite second moments, and finitely many Gaussian matrices reused in both orientations. The primary fixed-cap network instructions satisfy these hypotheses. The activation has bounded derivative and linear growth; the clipped backward gate has bounded partial derivatives at every fixed cap.

The adaptive conditioning argument conditions sequentially on the transcript. It preserves independent residual matrix factors, rather than incorrectly treating adaptively chosen inputs as unconditionally independent. The conditional mean in F.6 satisfies both forward and reverse constraints, and the remaining Gaussian lives on the doubly projected homogeneous subspace. The removed finite-rank projection has normalized expected squared length rank/n, which is sufficient for its disappearance at fixed transcript length.

The source rule F.9–F.10 is checked against that conditional law. Gaussian integration by parts produces the response, and the old-forward regression terms cancel as asserted. The resulting Gaussian source covariance is the full uncentered input Gram. Replacing it by a residual covariance after feature regression would give a different, incorrect rule; the report does not make that replacement.

F.4 regularizes each query input with its own fresh Gaussian root. This gives positive limiting Schur complements at fixed regularization. Its comparison to the original program uses bounded matrix actions and fixed coordinate Lipschitz constants. Removal of regularization uses continuous positive-semidefinite square roots and bounded source derivatives, not continuity of a pseudoinverse at rank loss. The distinction between formal source coordinates and Gaussian-support coordinates is correctly retained. F.14 explains why the contracted correction is invariant even where its individual coefficients are not.

The causal scalar-feedback extension is separately proved by comparison with frozen limiting contractions. The functions used for actual residual feedback are locally Lipschitz on the relevant scalar sets. Normalized residual controls are frozen only after their numerical values are obtained; there is no attempted differentiation of the normalization at zero.

### Common action spaces and scalar differentiation

The countable construction at line 2904 closes the language under coordinate approximation and both orientations of initialized actions. The density argument, limiting norm inequality, and limiting adjunction identity supply actual bounded linear actions and their actual Hilbert adjoints on the generated L2 spaces. This avoids assuming an independently resampled reverse action or operator-norm convergence across different widths. Real coefficients and additional fixed probes are admitted by approximation and bounded-action continuity.

F.5–F.7 supply the correct differentiability statements. The bounded-multiplier lemma proves strong continuity on each fixed L2 factor. The trajectory chain rule follows for C1 L2 curves. The scalar prediction's Fréchet derivative is established by a weighted Taylor remainder, successively moved through actual adjoints; it is not inferred from a false ambient L2-to-L2 Fréchet derivative of a nonlinear Nemytskii map. The same weighted argument supports the scalar feature-energy differential in N.6–N.9.

At fixed cap the raw field is locally Lipschitz on primal balls. Forward Lipschitzness, bounded gate partial derivatives, and the rank-one inequality give the claimed local flow and Euler estimates with constants independent of width. These facts do not assert uncut local Lipschitzness, and the later proof does not need it.

## 3. Two-input reference, explicit coefficient, and nonaffinity

Appendix A, beginning at line 1067, proves exact odd label folding and the invariance of both finite vector fields under that folding. Reflection symmetry of finite programs, together with deterministic limiting contractions, gives the population scalar prediction identity. It is not incorrectly imposed on each finite random realization, and its construction precedes uncut uniqueness.

For the affine comparator at the same gain, the active equations A.4 close without the inactive root. The independence used in A.10 is available: the inactive first-layer Gaussian projection is independent of the entire active initialized transcript. The ordinary Frobenius norms of learned increments remain bounded at each fixed prefix by rank-one unrolling. Their normalized action on that independent root therefore disappears. The argument also applies to the composed increment BA−B0A0. This proves the inactive-field freezing; an operator bound alone would not have done so.

The covariance calculation A.13 removes the active/inactive cross term. Finite affine source expressions are linear in jointly Gaussian source coordinates after scalar contractions have deterministic limits, so the Gaussian marginal assertion survives strong affine Euler convergence. Each sample variance is consequently at least δ/32 throughout its own stopped affine reference interval.

The affine energy argument is valid. C''=JJ* C follows from the trajectory chain rule and the actual adjoint gradient. Convexity of the regularized radial norm, followed by its zero-regularization limit, gives the initial radial slope lower bound and g'≥δ/128. Energy and Cauchy–Schwarz supply a strong endpoint if a finite maximal interval ended below g=3/2. Local polynomial-field continuation then forces the hit. The proof stops each comparator at its own hit; it does not extrapolate its boundedness to the larger numerical duration Sδ.

The sharper constants in the main text, line 211 onward, were checked against their stated norm conventions. The affine forcing table has the correct affected components. The response probe is inserted at separately named answer slots, and width is taken before its amplitude tends to zero. Choosing signs bounds the absolute row; converting scalar output rows into block-row norms incurs the displayed two-sample factor. The learned forward and backward moments are covered by T.17. T.18 supplies the required finite affine-array premise through fixed-mesh contraction limits and exact update lengths, without assuming trained finite operator norms converge.

The explicit Gaussian margin Q.1–Q.4 follows from the third Hermite component, one integration by parts, the Laplace representation, and Jensen against the probability density t exp(−t). The resulting function of variance is increasing. Q.5 is also valid for degenerate variables: the optimal arctangent regression slope lies in [0,1], with slope zero available for a constant variable. The coupling estimate therefore has no hidden inverse-variance loss. Absorbing the affine part gives Q.7 exactly. The final constant in T.9 is the Gaussian margin divided by four and multiplied by e².

The cutoff recipe is genuinely finite and explicit. The gain-one substitution is an upper estimate while the comparator retains its actual gain a=1−e. Removing the activation offset does not remove derivative paths or current returns. The coordinate and forcing inequalities needed from Part R are dominated by the displayed numerical-gain-one constants. Q.11 retains the factor e in the exponential envelope; the added Q.12 condition makes Q.13 valid. The chronological remainder constants are then unchanged. The reciprocal terms in Q.18 have the asserted monotonicity, including the simplified P/(2T0) and b/(4Q) terms. Its limit zero follows from b/(4Q), independently of any necessity claim.

The exponential-tower accounting is consistent: the improved primitive response constants are at most single exponential in a constant times δ^(−6); K* is at most double exponential; exp(K*S) contributes the third. The report correctly treats this as a very conservative sufficient amplitude, not sharp admissibility or proof of a polynomial allowance. The discussion of E_max avoids deriving interior necessity from incompatible exact endpoints.

## 4. Controlled response closure

Part R, beginning at line 3149, provides the needed cap- and mesh-independent incoming moments. The proof is not merely a declaration of response regularity.

R.11–R.17 retain both learned rank-one terms, both action orientations, uncentered input moments, and current transpose returns. Their chronological construction is A2, A3, B3, B2. Forward inputs use only strictly past backward answers, whereas reverse calls may use the current forward tuple.

R.23–R.29 turn raw affine stability into formal response bounds through a Gaussian probe. The argument takes the width limit at fixed nonzero amplitude, then uses finite affine coefficient continuity as amplitude tends to zero. Thus singular source directions are tested without differentiating along a singular support or interchanging a derivative with a width limit.

The nonlinear primal comparison and query-variance bounds precede the response bootstrap. R.33 depends on affine Lipschitzness and same-state perturbations, so it does not presuppose a nonlinear response bound. R.38–R.43 then obtain sub-Gaussian moment growth from bounded coefficient prefixes and Gaussian source variances. Their maxima are maxima of deterministic Lp norms; no unproved random time-supremum estimate is inserted.

The exact derivative equations R.46–R.49 retain the terminal LkJk factors. R.50–R.58 control both the accumulated exponential envelope and its current incoming-field multiplier, using convexity rather than time independence. R.59–R.77 compare nonlinear derivatives to affine derivatives at the same coefficient arrays before comparison to the actual affine baseline. This separation is necessary and is performed correctly.

R.79–R.89 then compare the deterministic coefficient systems. The new forward row depends on already controlled previous rows; the top backward row is established before the middle backward row uses it. R.91–R.94 make this induction explicit and include both current-return formulas. The finite-product inequality closes the prefix with strict slack under the chosen coefficient. No circular same-time inverse, omitted current term, or unsupported response assumption remained in this check.

## 5. Global raw flow, clocks, and nonsymmetric uniqueness

The main cap-removal argument begins at line 317 and is fully supplied again in V.2, beginning at line 4474. The asymmetric gate splitting T.24/V.10 is correct for arbitrary admissible clips, including R'=infinity. Its last term is supported where the reference incoming field exceeds R. Successive backward substitution multiplies incoming discrepancies by bounded gates and actions; each new R multiplies a forward-state discrepancy already controlled independently. Consequently the loss is linear in R, rather than a product of three cap factors.

The cap-independent incoming moments give Gaussian L2 tails. Gronwall therefore bounds cap discrepancies by an exponential linear in R times an exponential negative quadratic in R. The same estimate bounds raw directions. Completeness of the raw increment space gives a uniform C1 limit, and the estimate with the true gate on the left identifies its autonomous field. The scalar differential from F.7 identifies it as the raw Hilbert gradient field.

For the uncut two-input feature path, the radial argument remains valid after construction because only the strong trajectory chain rule and adjunction are required. Thus g crosses one before the endpoint with g(S)≥5/4. The physical clock is increasing before that first hit. A bounded feature derivative gives 1−g(s)≤M(s*−s), so physical time diverges at the hit. This produces every finite physical time and the stated loss rate, with the factor four in the loss derivative checked.

For each cap, existence of a first hit and divergence of its clock require continuity and the bounded derivative, not monotonicity of its prediction or a gradient-flow energy identity. The report correctly makes this distinction. The same bounded feature intervals supply uniform primal and incoming-tail bounds for their entire physical trajectories.

Against a nonsymmetric uncut competitor, the physical comparison keeps all actual residual components and uses only the reference's tails. Bounded competitor primal quantities merely change the deterministic comparison constant. No scalar reduction of the competitor is assumed. At a reached state, the cap's exponentially small initial discrepancy can withstand an additional exponential linear in R. The reference-only comparison therefore proves uniqueness and unique continuation in the stated class, without claiming existence from arbitrary ambient uncut states.

Appendix C's own shifted theorem was also checked, rather than treated as a free dependency. G.1 proves the augmented-Gram lower bound, G.3 supplies a bounded controlled interval and the finite affine-array premise on all admitted meshes, and G.21–G.23 show readout coercivity dominates the possibly nonsymmetric capped hidden term. G.24 gives strict residual-clock slack. The resulting cap references and tails provide exactly the inputs required by Part V. These shifted-activation estimates are distinct from the two-input scalar-clock argument.

## 6. Actual finite GF, raw GD, true kernels, and generated probes

V.6–V.9, lines 4737–4937, establish the relevant finite-algorithm bridges. At a fixed auxiliary mesh, primary fixed-program laws and update-factor contractions bound current finite operators by exact rank unrolling. The enlarged ball is obtained with slack and does not require cross-width operator convergence. Width-independent fixed-cap Euler defects then let the width tend to infinity before the auxiliary mesh is refined.

The actual finite readout has normalized size O_P(n^(−1)). Only a same-width auxiliary fixed-program comparator sets it to zero. Stopped finite-step comparison propagates its disappearance in the limiting law; actual finite GF, GD, and same-width cap comparisons retain the specified random initialization.

Actual uncut finite GF is globally defined by its finite-dimensional raw energy identity. Compact-time identification is then supplied by the cap reference. For raw GD the direction is the uncut field at the preceding node, not at the interpolated state. V.55 adds the cap reference's within-step defect K_(R,T) eta_n. At fixed cap this vanishes for eta_n=n^(−2). The argument never applies a fixed-program theorem to a transcript whose length grows with width. Stopping is removed through strict slack, including for the discrete algorithm.

True kernels at capped states receive a separate proof in V.8. The true backward chain is appended with nested gate truncations. Bounded-multiplier L2 continuity, second-moment tails, and bounded current actions identify the actual observations after removing the truncations. Its uniform-time upgrade uses compact L2 time images of the true incoming fields. This correctly distinguishes true backward observations from capped update fields. For the final uncut comparison, V.11 directly compares capped update fields with the true uncut backward fields. Products of the resulting L2 observations give all kernel entries, including off-diagonals.

Generated probes remain fixed finite expressions. Their instruction class has bounded coordinate derivatives and same-layer contractions, and every initialized or trained action is used with its correct domain and orientation. The comparison of action outputs uses same-width or common-population operator differences controlled by Hilbert–Schmidt increment errors. This supplies the claimed probe limits without inventing a cross-layer neuron pairing.

## 7. Appended velocities, derivative validity, and path laws

The velocity proofs at lines 4534–4864 are substantive and were checked separately from raw-state convergence. V.3 derives expected primary source rows by nonlinear Gaussian probes, including recomputation of residual feedback. Source differentiation freezes the actual deterministic coefficients. A single past insertion supplies the mesh-step factor; current return coefficients retain their separate bounded contribution. V.4 then derives pointwise absolute derivative rows and primary moments by triangular recurrences. It does not replace E|derivative| by |E derivative|.

The appended velocity inputs d_phi(z)P have unbounded coordinate derivatives and are not fed directly into F.1. V.36 truncates the incoming velocity. At the first appended action, the derivative dominator K(1+|P1|) is integrable from primary estimates. Only after the first action's coefficient and moment bounds are established is the second action treated with an inner and outer truncation. A new forward Gaussian source is held as a distinct formal argument when differentiating in the opposite source family; its possible correlation with old sources of the same forward family is retained. This justifies V.30–V.35 without an arbitrary operator Lp bound or circular velocity-moment premise.

The deterministic comparison V.40 is valid: the gate mismatch is multiplied only by a truncated reference velocity, and propagation through the three layers introduces a single tail level M. For population cap removal, the uncut reference velocities already exist as continuous L2 paths by the trajectory chain rule. Their compact time images have uniformly vanishing tails. Thus cap removal is performed at fixed M, followed by M tending to infinity. For finite velocities the order is width at fixed cap and M, cap at fixed M, then M tending to infinity. This avoids multiplying a cap-removal error by uncontrolled cap-dependent fourth moments.

At fixed cap, the fourth-moment bound is legitimately used only with that cap fixed, to upgrade auxiliary-mesh approximation and obtain uniform-time empirical laws. Full finite-time concatenations preserve same-layer correlations. The specified one-sided GD directions are covered by preceding-node comparison and continuity of the reference direction.

For path laws, V.57 supplies the missing passage from finite grids to the supremum path norm. Its squared interpolation error is bounded by 4h times integrated squared speed. Bounded raw directions, bounded actions, and bounded activation derivative give the required normalized speed bound; initial second moments and that bound place the path laws in P2. Fixed-grid joint W2 limits followed by grid refinement therefore prove the stated path-space W2 convergence. Uniform-time velocity W2 convergence controls squared norms, cross moments, and integrated speeds. No random supremum-moment estimate is silently substituted for a supremum of Lp norms.

## 8. Initial motion and three-input geometry

For two inputs, Appendix B beginning at line 1444 proves positive initial forward Grams from full Gaussian support and strict monotonicity. The top beta Gram uses the fact that phi'' is not identically zero. V.I supplies the derivative-valid transpose identities with full reverse covariance and the required current feature responses. Conditional covariance then proves the lower beta Grams are positive.

The hidden block norms are positive trace pairings of positive definite Grams; the bottom block and each bottom sample also have direct conditional-variance lower bounds. The upper-layer adjunction identities prove at least one nonzero sample direction, and the valid two-sample reflection transfers equal squared norms to the other sample in both label sectors. The expansion is in the actual raw direction, and the physical clock multiplies the hidden acceleration by four and the projected kernel coefficient by four, yielding the stated 8||V||² coefficient. The readout starts with nonzero velocity. Weighted scalar remainders or bounded directional chain rules justify the second-order energy expansion without ambient second Fréchet differentiation.

For three separated lines, the tensor test R_i in equation (1) kills both other cubic tensors and has pairing at least delta(2−delta) with its own. Summing the three coefficient inequalities proves the claimed cubic Gram lower bound, including singular input Grams. The third Hermite projection has coefficient e b3 with b3 nonzero by strict Jensen. Its residual is orthogonal to the entire cubic tuple, yielding the nonlinear Gram bound. The first-chaos projection propagates positive definiteness through the next two initial layers.

The sharpness construction cancels the linear activation exactly in the input-Gram kernel direction. The second-difference estimate for arctangent gives the stated O(e²delta²) Rayleigh quotient. Both the closed and strictly separated configurations satisfy the displayed angular inequalities in the claimed range. The least-eigenvalue statement is correctly distinguished from a bound in every binary-label direction.

The new per-sample upper-layer argument at equations (8)–(11) is sound. The first additional forward input retains positive conditional variance from the fresh lower reverse Gaussian. After regression on old forward sources, a positive independent forward remainder remains, independent also of the opposite source family. The middle beta tuple depends only on the older variables, so it cannot cancel that remainder. The same argument applies at the top. The finite conditioning explanation confirms the normalized finite-rank projection cannot erase the innovation. The finite added queries have the stated truncation and derivative domination; no growing-transcript conclusion is extracted from them.

These directions become accelerations only conditional on a canonical strong solution with the chain rule. The factor nine in the three-input hidden acceleration and coefficient 18||V||² in the projected kernel expansion follow directly from initial residuals −y and do not require equal residuals or a scalar clock. The manuscript explicitly preserves this conditional status.

Appendix C's Part N was read through its final line. Its affine upper-sample estimates use deterministic fixed-program limits together with operator moments and independent trace probes; the finite fourth-moment identities are not used alone as a concentration argument. The expansions of the relevant Wishart trace moments and the squares in N.30 and N.37 agree with the displayed lower bounds. The direct nonlinear perturbation estimates preserve those lower bounds at the stated shifted-theorem amplitude. N.54–N.64 then justify the physical initial derivatives and kernel expansion using the proved multiplier and scalar-energy arguments.

## 9. Counterexample and overclaim attempts

The following potential failures were actively tested against the full proof and did not leave an objection:

1. **Exact antipodal/duplicate obstructions.** They explain excluded endpoints but cannot refute an interior theorem or prove necessity of the sufficient cutoff's decay. The report respects both distinctions.
2. **Singular three-input Gram and affine label incompatibility.** These produce the stated failed affine clock and stationary equilateral affine example. They do not contradict the positive-mixture initialization claims, and the report does not call them a global existence proof.
3. **Lost transpose dependence.** A reused Gaussian matrix requires return terms and full input second moments. Both are present, including the current middle return induced by the top return.
4. **Degenerate Gaussian source supports.** Independent input regularization and formal-source derivatives resolve this; no unstable covariance inverse is required in a limit.
5. **Uncut L2 non-Lipschitzness.** The proof constructs capped flows first and obtains uncut uniqueness through reference-only tails. It does not use an invalid uncut Picard argument.
6. **A nonsymmetric competing solution.** The physical comparison retains its actual residuals and only borrows tails from the cap reference.
7. **A cap-dependent velocity-moment explosion.** The final velocity comparison uses compact uncut L2 tails and an explicit fixed-M limit order, so no uniform-in-cap fourth moment is needed.
8. **Finite GD evaluated at the wrong state.** Its preceding-node field and the extra reference defect are explicitly retained.
9. **Fixed-time laws mistaken for path laws.** The observation-grid interpolation estimate and integrated-speed bound supply the additional step.
10. **Uniform-in-time nonaffinity inferred from a compact-time limit alone.** It instead comes from comparison on one bounded feature interval containing every physical time, so the all-time infimum is justified.

## Substantive objections and required repairs

None remaining. The detailed checks above support PASS for the manuscript's stated scope. In particular, no repair is requested that would turn the explicitly open generic three-input global problem into a purported established theorem.

## Cosmetic and clarity suggestions, separate from the verdict

- The title “An odd convex activation” can be read as asserting that the activation is a convex function. For e>0 its second derivative changes sign, as the report itself computes. “An odd convex-mixture activation” or “An odd activation formed by a convex mixture” would describe the intended meaning more precisely. No proof in the manuscript uses global convexity of this scalar function.
- Appendix A has several initial-time expressions such as C(A.0) and Theta(A.0). Ordinary C(0) and Theta(0) would avoid the appearance of an equation label used as a time coordinate.
- The quantitative chapter begins its numbered sections at 2. Renumbering is optional and has no mathematical effect.
