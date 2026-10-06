# Independent compact-section audit

Date: 2026-10-06.

## Status and scope

**Amended compact section: PASS, conditional on the stated source event and dense initialization/fitting theorem.** The frozen compact draft has one missing construction definition, described below. The explicitly authorized insertion in `RESULT.md`, lines 1583–1638, resolves it. No false inequality or additional mathematical obstruction was found in the requested deterministic compact implication. This is an isolated mathematical review, not promotion approval and not an effective confidence-to-width theorem.

The complete frozen compact section, complete source section, complete analytic-tail note and notation contract were read. From the dense section, the complete model/initialization/fitting statements and corresponding proofs were read; its independent-run concentration and lower-bound arguments are outside this audit. The source probability theorem is accepted as a stated input. Its finite-deletion proof and qualitative stochastic onset are not independently certified by this verdict.

Only the assigned packet, shared instructions, required skills and the subsequently authorized source-space insertion in `RESULT.md` were used. No other study, prior review, research history or linked component note was read. The required canonical-notation skill at `/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` returned permission denied; a filename search in the accessible skill roots found no replacement. `solve-math-rigorously` and the available notation contract were read and applied. This access limitation is recorded explicitly rather than claiming that the unavailable skill was read.

## Input identity

SHA256 values were checked on arrival and again before writing this report.

| Input | SHA256 |
|---|---|
| `INTEGRATED_COMPACT_SECTION.md` | `ecdd4ef9d66f5c9405aa68d3703b8a90fef78f695d604c7f1d74bc2103b8d985` |
| `INTEGRATED_SOURCE_SECTION.md` | `ddef8fdef8232f4a0352353ea1b3670f1af8f3b9fea5d47629924323055e459f` |
| `INTEGRATED_DENSE_SECTION.md` | `099e3dd8019c6737c7be215b666a2ac7f3ab8007f96b9ba6e85e26705b320341` |
| `ANALYTIC_TAIL_EXTENSION.md` | `70ec072f0e83c74364f068d61f04148bf110771fd06b4b2b874bb3c5d8dfc349` |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |

The authorized repair insertion was read at `RESULT.md` whole-file SHA256 `6491e6ed5a4d619c6f2507c77c4ccb9b0daa8fa6ca81108a61b37744e2f4b36b`. That records the version containing the inspected insertion; it is not a claim to have reviewed the other sections of that assembled file. Final-artifact binding, if requested, is recorded separately below.

## Finding and resolution

The frozen compact draft uses the source spaces in its initialization at lines 159–174, invokes membership in `E_j` at lines 796–799, and counts four source families at lines 620–621 and 1538, without explicitly defining those spaces or naming the four families. The supplied source section establishes the needed source estimates but does not supply this omitted definition. Consequently the frozen draft's claim of a complete deterministic construction requires a local repair.

For each layer, the missing families are the dense feature, its initialized forward image from the preceding layer, the passive-query dense response, and the initialized transpose image of the next response:

\[
h_n^{(j)}(t,v),\qquad
W_0^{(j)}h_n^{(j-1)}(t,v)\quad(j\ge2),\qquad
\delta_n^{(j)}(t,v),\qquad
W_0^{(j+1)T}\delta_n^{(j+1)}(t,v)\quad(j<L).
\]

Here the passive-query response uses the ordinary dense backward recursion with top carrier `w_n(t)`. Its query contributes no training force. The coefficient span must include the constant, every initialized training feature, its initialized forward image where present, and the first-weight columns at layer one. Paired coefficient computation must use identical linear quadrature, cutoff and jet operations in the two spaces.

**Resolved in the inspected insertion.** `RESULT.md` lines 1583–1638 give all these definitions, the endpoint omissions, the exact additions and their counts, and the exact paired memberships with separate coordinate errors. In particular the additions have dimension at most `m+d+1` at layer one and `2m+1` later; `B=2m+d+1` covers both. The insertion introduces no fifth source family. Thus it supports `B+4N` for `d>=2`, `B+8N_1` for `d=1`, and the paired-action defect used later. The frozen file itself was not edited.

## Mathematical checks

The following checks use the draft's proof abbreviations `lambda=gamma/m`, `z=Y/lambda`, `alpha=Y/sqrt(lambda)` and `S=16z`; the global gap remains the unweighted `gamma`.

1. **Harmonic and temporal count.** The tangent-average multiplier proves spherical-degree decay without assuming convergence of a harmonic series at complex points. The Pochhammer estimate, projector bound, Fourier contour shift and two exponential half-tails give the stated `eta/16` tail. The weighted-simplex cube argument gives

   \[
   N(T,\eta)\le
   \frac{2[H(T,\eta)+\alpha_T+(d-1)r_q]^d}
        {d!\alpha_T r_q^{d-1}}.
   \]

   For `d=1`, the two real queries require two temporal expansions per possible source family, explaining `8N_1`. Neither count hides a sample-count multiplier.

2. **Finite initial jets and exact pairing.** The explicit disk map sends zero to time zero, reaches all of `[0,T]` on a compact real interval inside the disk, and stays inside the source rectangle. The Cauchy remainder tends to zero for a finite Taylor degree at every positive tolerance. Finite quadrature can be made uniformly accurate across the finitely many retained coefficients and source coordinates. Applying the same scalar linear operations to an image pair preserves its exact initialized-matrix identity. This is finite real-arithmetic setup; no setup-efficiency or bounded-precision result follows.

3. **Selection and metric.** The supplied barrier proof gives at most `9r` selected coordinates, with spectrum between one and four after rescaling. The lower-potential argument is valid: with its displayed `D`, one obtains `sum L >= 1-Phi_l >= 2/3`, matching the upper bound on `sum U`. The metric formula has eigenvalues in `[1/4,1]` relative to the diagonal metric and satisfies `P^T M P=I`. The constant source vector supplies its exact unit mass. Multiplication by a diagonal gate has norm at most twice the coordinate maximum, without a minimum-selected-weight factor.

4. **Exact initialization and independent fitting.** The initialized feature/image additions preserve the complete training forward pass and initial top Gram. The compact energy identity follows by expanding the given velocities; it does not require the gates to be self-adjoint or the optimizer to be the gradient of the corrected predictor. The corrected readout has norm below `5alpha`. The hidden displacement bound obeys

   \[
   20F_cY^2/\lambda^{3/2}
   \le \frac{5\sqrt\lambda}{64H_c^2}
   <\frac1{8H_c},
   \]

   using exactly the stated compact label allowance and `sqrt(lambda)<=H_c`. This closes the operator, feature and Gram stops, gives global continuation and convergence, and justifies both the baseline and endpoint bounds.

5. **Source action and energy transfer.** The norm and pairing transfers follow from exact source isometry and diagonal mass at most four. Paired initialization errors cost `18eta`; the learned action errors are bounded without differentiating a source approximation. Integrating feature approximants gives a readout approximant with coordinate error `4eta z`. Together with `eta<=Y` this establishes `int nu<=2alpha` and `||w_R||<=3alpha`. The selected-response bound uses `sqrt(lambda)<=H_c`; it does not impose `lambda<=1`.

6. **Readout/deficit cancellation.** For `e=(c_C-c_n)/sqrt(m)`, `p=T_C e` and `zeta=w_C-w_R+p`, the identity `T_C Q_C=V_C` cancels the raw-readout term exactly. The potentially non-dissipative hidden contribution satisfies

   \[
   200z^2F_c\,\|e\|_2^2
   \le\frac{25}{32H_c^2}\|e\|_2^2,
   \]

   leaving at least `39/32` of the negative lifted-deficit term. Regularizing the norm of `p` justifies its integrated damping estimate, including `p=0`. Factoring the Gram difference retains the actual selected-readout velocity `nu`, and the displayed scalar inequality integrates to exactly `B_n`. Both source-error terms `eta` and `eta/sqrt(lambda)` are retained. Inserting the resulting estimate into the query bound gives exactly the stated `A_n`.

7. **All finite horizons on one event.** The late dense path length is at most `2alpha exp(-lambda t/2)`. The fixed parameter ball about `T_0` preserves operator and activation-strip margins. Radial complex continuation and `4 K r_t<=log 2` give the stated residual and parameter bounds; the additional gate keeps every continuation in the same fixed ball. Local analytic ODE existence and uniqueness then extend and glue the solutions. The carrier subtraction recurrence has the stated factor `n`, covered by its separate deterministic gate. Both new gates are eventual and independent of the selected budget, horizon and accuracy. This argument does not require new horizon-dependent Gaussian events.

8. **Explicit constants on the full label interval.** The source allowance implies the displayed inequalities for `zK_1`, `zF` and `z^2 K_1 K_src`; the stronger fourth-root source entry is used where required. The compact runtime allowance gives `400z^2F_c<=25/(16H_c^2)`. These verify `B_n<=44+64sqrt(log(en))`. The positive source recurrences support the stated beta-power envelopes, numerical prefactor and tail estimates. The rank-envelope arithmetic yields denominator `32768` before the factor-nine conversion and hence `294912` in the headline negative exponential rate. The optional smaller cap is used only for its separately labeled original-tolerance refinement.

9. **Every-budget and inverse interfaces.** The variable-rank calculation has the correct factors four and eight, and `lambda^{-1} c_t^{-1}=1024(U/a)z^2`. Under `T=T_0+4u/lambda`, `eta=eta_0 exp(-u)`, the resulting rank is at most `B_*+C_d(h_0+u)^(d+1)` and the error is `E_1 exp(-u)`. If that rank is at most `q/9`, its integer dimension is at most `floor(q/9)`; no premature ceiling is needed. The baseline branch covers `q>=9B` before analytic improvement becomes available. The headline `18B_*` domain, loose-target branch, sharper discrete count and full-width fallback are mutually consistent. The prescription inverts sufficient certificates and does not assert minimal possible width. Exact retention makes the compact equations identical to the dense equations, including the `1/n` hidden-update normalization.

10. **Storage.** The learned-coordinate count is exact for the displayed state. The corrected readout is derived, not an additional learned vector. Summing the explicitly listed optional copies and caches gives the displayed inventory. With `q_j<=9R` and `m,d<=R`, its quadratic coefficient is at most `441L-102`, below the stated allowance. In the genuinely compressed budget branch, `q<n` and `q>=9B` imply `n>d`, so the first-weight rank argument used here applies. The analytic dimension bound `R=B+4N` or `B+8N_1` also has `R>=m,d` directly. Substituting actual rank at most `q/9` gives `1020/81<13`. The full-width learned count is the ordinary dense count plus the compact deficit state and any deliberately retained caches. Counts are real-coordinate counts and exclude discarded setup arrays, bit precision and a numerical solver's chosen workspace, exactly as stated.

## Claim boundary

The result is a deterministic compact-construction implication on the inherited event. Its error coefficients, source counts, supplied-budget prescription and inverse prescription are explicit. The onset of the source probability event remains qualitative, as stated throughout the packet. This review neither converts that onset into a numerical confidence-certified initialization width nor audits the independent dense upper/lower comparison. It establishes no test-risk guarantee, optimal compression rate, efficient preprocessing or ordinary-gradient interpretation of the compact optimizer.

The inspected repair resolves the only construction omission found. No candidate files or Git state were changed by this audit.

## Final artifact binding

The final assembled `RESULT.md` was verified at SHA256 `e24e2f519bd597159f1745ce46e9f9ad27c8772e9ef80807907b63557401c562`. Its compact statement occupies lines 1492–2021 and its compact proof/provenance occupies lines 4698–5934. Direct diffs against the complete frozen compact section confirm that the only changes are the inspected source-space insertion, heading/anchor organization, two integral-spacing corrections, and an explicit local redefinition `X=beta^L` in the activation-only budget calculation. No other compact mathematical formula changed.

**Final outcome: PASS for that final artifact's compact statement and proof, relative to its stated source and dense-fitting inputs, with the claim boundary above unchanged.** This hash binds the reviewed section; it is not a verdict on the assembled file's other mathematical sections or audit appendix. The initial frozen hashes remain the record of the packet even if its temporary section files are subsequently removed after assembly.
