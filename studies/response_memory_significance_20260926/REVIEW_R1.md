# Round 1 isolated counter-review of `CANDIDATE_V1`

## Overall determination

The revision resolves the central mathematical and resource-accounting objections. I re-audited both clock proofs rather than inferring soundness from the abstract or the author response. For positive initial residual, I find the ordinary-clock and response-clock arguments sound at the stated fixed finite width, depth, data, initialization, and compact horizon. The response-clock proof is now self-contained: it obtains an order-independent coarse defect and path-variation estimate before bounding the clock, controls the normalized response map on a residual tube, derives the joint Legendre tail, closes the physical/residual stops, and handles the fixed-order Gram continuation. The corrected Variant-B state count, retained-operator cost, crossover inequalities, and adverse empirical facts are also stated plainly.

The defensible significance claim is therefore a **strong specialized theory result**: an autonomous response-history moment family approximates the complete parameter path of a fixed finite deep nonlinear gradient flow, with an exact product-of-projection-errors mechanism and compact-horizon rates. The frozen evidence does not support an unqualified “breakthrough” in memory-efficient training, runtime, empirical validation, or unrestricted priority. V1 largely stops making those broader claims. Its remaining defects are localized: one materially relevant local population-closure precedent is still omitted; the response-clock zero-residual branch is asserted without defining its normalized response state; the factor baseline omits a consequential initialization qualification; the frozen TeX bundle is not independently build-complete; and the definition of “scalar ODE” contradicts the table's usage. None invalidates the positive-residual trajectory theorems.

**Current disposition:** limited revision. There is no remaining fatal or major theorem flaw. O4 retains a moderate significance-positioning issue; O5, O6, O8, and O9 retain minor defects. O1, O2, O3, and O7 are resolved.

## Resolution of Round 0 objections

### O1 — **Resolved; current severity: none**

V1 corrects the Variant-B state count everywhere that matters. The abstract now says that the closure evolves “`2(H-1)mnP` history scalars and a shared symmetric `P x P` Gram matrix” and gives the complete moving-state scaling `O(Hmn epsilon^{-1/2}+epsilon^{-1})` (V1 lines 59–62). Table `tab:complexity` counts the symmetry-packed Gram as `P(P+1)/2`, distinguishes the implementation's full `P^2` storage, and gives learned rank at most `m(P+1)` because of the matching prefix (lines 872–897). Equation `eq:new-state-epsilon` and its following sentence state that the Gram term eventually dominates at fixed `H,m,n` (lines 942–958).

This agrees with `RESPONSE_CLOCK_UNCONDITIONAL_BOUND.md`, where the weighted projection requires an evolving `P x P` Gram, and with the packet's direct state formulas. The previous `O(Hmn epsilon^{-1/2})` complete-state claim has been withdrawn; it is now used only for the history factors. No V2 repair is required for O1.

### O2 — **Resolved; current severity: none**

V1 now separates learned-history state, complete moving state, and restartable total storage. The abstract says, exactly, “This is a representation theorem for learned increments, not a net model-memory or runtime compression theorem” (lines 64–68). The action count includes both the `O(nmP)` correction action and the retained `O(n^2)` `W_0`/transpose action, hence `O(n^2+nmP)` per vector and `O(mn^2+nm^2P)` per batch per link and direction (lines 899–912). It also includes the response-clock Gram factorization, solves, dilation, and directional passes.

The crossover statements are now exact:

- history factors beat dense moving internal matrices iff `2mP<n`, equation `eq:history-crossover` (lines 914–919);
- complete Variant A moving state requires `2(H-1)mnP+1<(H-1)n^2` (lines 920–924);
- symmetry-packed Variant B requires `2(H-1)mnP+P(P+1)/2+1<(H-1)n^2`, equation `eq:new-crossover` (lines 925–928).

V1 explicitly says that the theorem does not put its sufficient order below these crossovers and that total restartable storage is strictly larger than minimal dense storage after `W_0`, Variant-B prefix factors, and the Gram are included (lines 929–940). The MNIST figures—158.78127/165.03127/171.28128 MiB versus 152.53125 MiB, and 139.89330/149.92219/152.26930 seconds versus 102.97555 seconds—match `MNIST100_RESULTS.md` and are reported at lines 1132–1140.

This resolves the correctness objection. It also fixes the interpretation: the elapsed-time-independent state replaces the literal growing integral-history representation in `eq:exact-history`; dense gradient flow itself already has a fixed-size current-weight state. Thus this is learned-increment model reduction, not removal of a temporal-memory burden from the standard dense training algorithm.

### O3 — **Resolved; current severity: none**

The HiPPO and NTH comparisons now meet the required contract.

For HiPPO, V1 lines 123–136 credit online time-dependent polynomial projection, scaled Legendre modes, and triangular dilation dynamics as direct ingredients, and lines 283–289 credit the precise Legendre identity used in the closure. This matches HiPPO Definition 1, Theorem 2, Propositions 3–6, and Appendix D.3 equation (29). The claimed mismatch is accurate: HiPPO approximates a supplied signal; it does not supply feedback-coupled forward/backward neural histories, learned-matrix reconstruction, or a fixed-width complete-parameter trajectory theorem.

For NTH, V1 lines 138–166 correctly distinguish the exact finite-width output/kernel hierarchy in equations (2.1)–(2.2) from the autonomous top-kernel freezing in equation (2.7). An order-`q` training kernel has up to `m^q` sample-indexed values, so a direct hierarchy through order `q` is dominated by `O(m^q)` values before symmetry reduction; V1 uses `p` for this order and explicitly labels the count as reviewer-derived rather than a source complexity theorem (lines 142–145). The translation of Theorem 2.6's regime, width-dependent horizon, and output error at lines 146–160 is consistent with the source. The equation (2.11) test-point construction adds up to `O(m^(q-1))` values per test point (V1 lines 161–163). The supplied NTH paper demonstrates no executable truncated-hierarchy solver or direct truncation experiment, and its guarantee concerns wide/NTK-scaled outputs and kernels, not the complete parameter trajectory of one fixed finite network. Table `tab:prior-contract` preserves these distinctions (lines 211–231).

No V2 repair is required for O3.

### O4 — **Partially resolved; current severity: moderate**

The broad external positioning is much better. V1 now compares Tensor Programs IV, feature-learning and finite-width DMFT, multilayer mean field, Neural Feature Flow, shallow mean-field limits, lazy limits, initialization theories, and Mori–Zwanzig at the level of regime, object, state type, horizon, and implementation (lines 168–231). It limits its conclusion to the “reviewed, nonexhaustive source set” and makes “no unrestricted priority claim” (lines 233–238). Those are valid corrections.

One close frozen precedent remains absent: `BOOK_OBSERVABLE_CLOSURE.qmd`, Section C.4.7.9, theorem anchor `thm-docs-global-nonlinear-l12101`. That theorem constructs an increasing sequence of finite-type autonomous population systems, each well posed and restartable from saved current state, with uniform-in-time whole-circle prediction convergence and convergence of declared joint observations on a fixed positive interval. Its proof evolves two current population laws and a finite matrix of action contractions and compares directly with canonical nonlinear population gradient flow. It does **not** displace V1's theorem: its state contains probability laws and therefore infinitely many scalar degrees of freedom; its target is a specific two-hidden-layer population flow rather than one fixed finite network's full parameter path; it gives no `P^{-1}`/`P^{-2}` resource rate; and it does not retain and approximate the exact finite realization. But it is closer than the generic multilayer-mean-field row to the paper's autonomous/restartable nonlinear-closure claim and belongs in the contract table.

The author response says it “removed the earlier extended companion operator/no-go discussion rather than using it as evidence.” Removal does not answer this positive autonomous-closure precedent. The omission weakens only the novelty/significance positioning; it does not affect either proof.

**Required V2 repair:** add a short paragraph and one row to `tab:prior-contract` for Section C.4.7.9. State: fixed finite-type population closure; probability-law plus finite-matrix state; restartable; uniform compact-time whole-circle/observation convergence; no finite-scalar fixed-network parameter theorem or quantitative state/error rate. Keep the present bounded, nonexhaustive priority language.

### O5 — **Partially resolved; current severity: minor formal defect**

The original major missing-proof-detail objection is resolved for `rho(0)>0`.

For Variant A, I checked:

1. the scaled Legendre tail and rescaling, Lemma `lem:legendre` (lines 380–407);
2. exact equivalence between the moment ODE and the closure's own history integrals (lines 328–332);
3. the projection-energy identity and product-of-errors defect, equations `eq:projection-energy`–`eq:defect-energy` (lines 450–476);
4. the proof-only accumulator showing an accumulated absolute velocity defect (lines 478–488);
5. the nonvanishing-residual change of coordinate, the endpoint-evaluation cancellation, and the depth-stable `P`-independent forward-history recursion (lines 490–541); and
6. the accumulated `O(P^{-1})` defect, Gronwall comparison, first-exit exclusion, and continuation (lines 543–608).

I found no invalid step in that chain. In particular, the endpoint factor `P+1` in lines 511–520 is canceled by the Legendre tail in `eq:e-square`, so the depth induction does not silently lose a power of `P`.

For Variant B, I checked:

1. the weighted moment/Gram equations and exact mixed-term cancellation, `eq:new-recon`–`eq:new-defect` (lines 632–664);
2. the dense residual lower bound and stopped physical/residual tube (lines 685–705);
3. differentiation of `G^{-1}` and the weighted projection energy (lines 706–723);
4. the raw-energy coarse defect and total-variation bound before any clock cap (lines 725–742);
5. the normalized-residual projector, `D Psi` bound, and unconditional clock estimate (lines 744–768);
6. the joint unit-speed Legendre comparison using `d mu <= d xi` and the resulting `1/[P(P+1)]` defect (lines 770–796);
7. Gronwall, explicit order conditions, and exclusion of both stops (lines 797–812); and
8. fixed-`P` prefix-Gram positivity and compact continuation (lines 814–827).

This matches the detailed structure in `RESPONSE_CLOCK_UNCONDITIONAL_BOUND.md` and `DEEP_ACTIVATION_ERROR_THEOREM.md`. I found no circular use of the sharp approximation estimate to obtain the clock bound, and the manuscript correctly says that the Gram lower bound need not be uniform in `P`.

The remaining formal issue is the zero-residual sentence. The construction defines `b=(r/rho) delta` only for `rho>0` (V1 line 298), and Variant B initializes `U` with `b(0)` and defines `Psi` using `b` (lines 615–653). Theorem 4.1 then says, “If `rho(0)=0`, both flows are stationary” (line 680) without defining `b`, `U`, `C`, or the response-clock ODE on that branch. The physical conclusion is true, but the displayed autonomous state is undefined at `0/0`.

**Required V2 repair:** either restrict Theorem 4.1 and the Variant-B ODE to `rho(0)>0` and state the zero-loss physical trajectory separately, or define the stationary branch explicitly, for example `b=0`, `U=0`, `C=0`, constant physical variables and `L=1`. Then state uniqueness only in the selected branch. This is a localized definition repair and does not alter the positive-residual theorem.

### O6 — **Partially resolved; current severity: minor empirical-disclosure defect**

The evidence-availability objection is resolved. The newly frozen `MOMENT_RESULTS.md`, protocol, independent check, metrics, and summary support the shallow-circle table at V1 lines 1064–1085, including the stated limited resolution of the smallest `P=7` discrepancies. The newly frozen `FACTOR_CONTROL_RESULTS.md`, protocol, independent check, and metrics support the claims at lines 1001–1013: 29 valid factor-seed comparisons, 28 at least twofold, one unresolved hard-outlier cell, 58 threshold hits among 60 two-resolution trajectories, and the hard-outlier rank-56 values 0.00466307 versus 0.516210 and 0.251026. The unsupported old dictionary numbers have been removed.

One baseline qualification present in the frozen evidence is absent from V1. `FACTOR_CONTROL_RESULTS.md`, “What was compared,” and `FACTOR_CONTROL_CHECK.md`, “Completed engine checks,” state that the factor model uses `A(0)=0` and independent `B_ij(0)~N(0,1/r)`. It exactly matches the initial physical network, but its induced middle-matrix velocity matches the dense initial velocity only **in expectation** over `B`, not for either realized seed. Response memory, by construction, has the exact physical initial velocity. V1 identifies Euclidean factor flow and fixed seeds but does not disclose this asymmetry at lines 1001–1013. The numerical comparison remains correct, and V1 already limits it to “this factor metric,” but the missing fact matters when interpreting the result as evidence for a superior learned-increment representation.

**Required V2 repair:** add one sentence after line 1004: “With `A(0)=0` and `B_ij(0)~N(0,1/r)`, the control matches the initialized network exactly and matches the dense initial middle-matrix velocity only in expectation, not for each realized factor seed.” Retain the present statement that QR/SVD truncation and other trainable low-rank methods were not tested.

### O7 — **Resolved; current severity: none (the empirical limitation remains substantive)**

V1 now says exactly what the experiments test. Lines 1018–1027 identify separate matched-loss stopping, generally one initialization, endpoint predictor agreement rather than same-time physical trajectories, absence of an order-rate slope, and the non-certified status of solver refinements. Lines 1029–1050 report the adverse response-clock facts from `response_clock_metrics.csv` and its frozen reports: the step-sensitive GELU depth-three case through `P=5`, the approximately 330.9 maximum main-panel Gram condition, the 1.79–3.99 new/old runtime ratios, strict-fit denominators 79/70/67/66 in the 82-case sweep, the fitted-pair medians and maxima, and 17 cases with a miss. Lines 1087–1127 disclose nonmonotone deep-circle and MNIST order trends. The complete storage/runtime figures appear at lines 1132–1151.

The author did not perform the requested same-time, multi-initialization rate campaign because this revision froze existing evidence. That leaves the empirical validation narrow, but V1 no longer claims that the panels validate either theorem's rate or complete parameter trajectory. The missing campaign is open work, not a remaining reporting defect. No V2 experiment is required to sustain the theorem; a future empirical rate claim would require same-time parameter and prediction errors, adequate solver refinement, multiple orders, and multiple initializations.

### O8 — **Partially resolved; current severity: minor reproducibility defect**

The scientific source identities are repaired. `REFERENCES_V1.bib` correctly identifies arXiv:1902.06720 as Lee et al., *Wide Neural Networks of Any Depth Evolve as Linear Models Under Gradient Descent*, and arXiv:1805.01053 as Sirignano and Spiliopoulos, *Mean Field Analysis of Neural Networks: A Law of Large Numbers*. The unsupported Celentano attribution is gone. V1's related-work statements now use the supplied primary sources, and lines 233–238 explicitly bound the priority claim.

The frozen versioned source is still not build-complete on its own. `CANDIDATE_V1.tex` ends with `\bibliography{references}` (line 1196), while the supplied versioned bibliography is `REFERENCES_V1.bib`; it also references `figures/circle_shallow.pdf`, `figures/circle_deep.pdf`, `figures/mnist_scatter.pdf`, and `figures/mnist_rms.pdf` without those versioned build inputs being part of the frozen V1 source bundle. The supplied `CANDIDATE_V1.pdf` is rendered correctly, so this is reproducibility rather than content failure. The author response's statement that live `paper/main.tex` compiles cannot substitute for a build of the frozen review object, which this assignment forbids me to inspect.

**Required V2 repair:** freeze a self-contained source bundle whose bibliography and figure paths resolve without consulting live paper files, and record the exact build command/tool versions. Renaming or copying `REFERENCES_V2.bib` to the name used by the TeX and including the four figure assets is sufficient.

### O9 — **Partially resolved; current severity: minor terminology defect**

The concrete V0 presentation problems are otherwise fixed. `Psi` is now an unambiguous nested concatenation with one `[a;b]` block per link/sample (lines 615–621); passive observables are described as forward activations and predictions (lines 360–362); the mass, clock length, theoretical packed Gram, and implementation Gram are distinguished; and the operation table includes the retained initialized action. The V1 formula is correct regardless of the author response's disagreement about whether V0 visually duplicated the pair.

One internal contradiction remains. The state-class definition says that a “scalar ODE” has dimension “independent of width” (lines 107–113). Table `tab:prior-contract` then defines “finite scalar” to mean finite at fixed width and order and says it “need not be width independent” (lines 211–215). The paper's own state has dimension proportional to `HmnP`, so it is excluded by the first definition and included by the second.

**Required V2 repair:** replace lines 109–110 with: “A finite-scalar ODE evolves finitely many real coordinates at each fixed `n,m,H,P`; its dimension may depend on these parameters but not on elapsed training time.” If a width-independent aggregate class is needed, define it separately. This also makes the comparison with the probability-law state in the missing local precedent precise.

## Direct answer to the scientific-significance defense

### (a) Theorem novelty and significance

The positive-residual theorems are nontrivial, and within the frozen nonexhaustive source set I found no prior result satisfying their complete contract: one fixed finite deep nonlinear network; exact retention of initialized operators; finite scalar response-history state at fixed order; autonomous restart; learned-increment reconstruction; and uniform approximation of the complete physical parameter path on every prescribed finite horizon. The exact cancellation of both mixed projection terms and the resulting product of forward/backward projection errors is the key new mechanism. The response-clock bootstrap is also substantive: it makes the joint path unit speed without assuming the clock bound that the sharp approximation needs.

This supports “strong specialized theory contribution.” It does not support a field-wide or unrestricted breakthrough claim. Online Legendre memory is inherited from HiPPO; autonomous hierarchy truncation has NTH precedent; nonlinear feature-learning population/field dynamics have extensive precedent; and the local C.4.7.9 theorem already supplies a finite-type autonomous restartable population closure with compact-time observable convergence. V1's fixed-finite-width, full-parameter statement and proof mechanism remain distinct after those credits.

### (b) Learned-increment compression

The learned-increment compression claim is mathematically real. Variant A represents each internal correction with rank at most `mP`; Variant B has rank at most `m(P+1)` because of the fixed prefix. The history state does not grow with elapsed time, and convergence follows as order grows. When `2mP<n`, the two history-factor arrays are smaller than a dense moving internal matrix.

Its practical scope is narrower. The theorem does not ensure that an accuracy-sufficient `P` satisfies `2mP<n` or either complete-moving-state crossover. At fixed dimensions, sufficiently large `P` eventually loses the count advantage. Dense gradient flow already evolves a fixed-size current state; the growing object is the exact integral-history representation, not the standard dense algorithm. These facts materially reduce a broad “compression breakthrough” interpretation but do not reduce the theorem to bookkeeping: the difficult point is closing an endogenous feedback-coupled history while controlling the resulting physical path.

### (c) Total storage and runtime

There is no positive total-resource result. Every `W_0` and transpose action remains; Variant B adds prefix factors and a Gram; the current implementation stores the full `P^2` Gram; total restartable storage is larger than minimal dense storage; and the large reported closures are slower. The exact per-vector action remains `O(n^2+nmP)`, not subquadratic in `n` while `W_0` is dense. This decisively prevents the current work from being characterized as a systems or efficient-training breakthrough. V1 now says so accurately.

### (d) Empirical validation

The evidence supports executability and selected low-order endpoint-predictor fidelity. It also supports the exact rank-matched factor-control comparison under its specified Euclidean factor metric. It does not validate either compact-horizon trajectory rate, parameter-path accuracy, robustness across initialization, or practical superiority of the response clock. The step-sensitive Variant-B case, fit failures, nonmonotone order trends, larger storage, and slower runtime materially weaken an empirical-breakthrough interpretation. Because V1 discloses these facts, they limit significance rather than contradict the revised claims.

### (e) Unrestricted priority

No unrestricted priority conclusion is justified. The packet is explicitly nonexhaustive, and I did not browse beyond it. V1 correctly limits its conclusion to that reviewed set. After adding the omitted local C.4.7.9 comparison, the defensible statement is that the complete contract was not found in the supplied source set—not that no earlier or concurrent work establishes it under different terminology.

## Exact V2 repair list

1. **O4 / moderate:** compare `BOOK_OBSERVABLE_CLOSURE.qmd` Section C.4.7.9, theorem `thm-docs-global-nonlinear-l12101`, in prose and `tab:prior-contract`, with the precise population-law/fixed-finite-network mismatch.
2. **O5 / minor:** define or remove the `rho(0)=0` Variant-B branch so that `b`, `U`, `C`, `Psi`, and uniqueness are not left at `0/0`.
3. **O6 / minor:** disclose that the random factor control matches the dense initial matrix velocity only in expectation, not for either realized seed.
4. **O8 / minor:** make the frozen versioned TeX bundle independently build-complete, including the correctly named bibliography and four figure assets.
5. **O9 / minor:** make the finite-scalar state definition permit dependence on fixed `n,m,H,P`, consistently with the contract table and the proposed closure.

No new theorem, new experiment, or runtime claim is required for V2. The missing same-time rate campaign and initialized-operator compression should remain clearly identified as open work.

## Reading and verification coverage

I read `CANDIDATE_V1.tex` end to end and checked the 21-page `CANDIDATE_V1.pdf`, including rendered equations, both state tables, and all three figure panels. I read `REFERENCES_V1.bib`, `REVIEW_R0.md`, `AUTHOR_RESPONSE_R0.md`, `DIFF_V0_V1.patch`, `NEUTRAL_ASSIGNMENT.md`, and `LITERATURE_PACKET.md`. I rechecked all theorem evidence enumerated in the packet, the deep-circle, MNIST, and response-clock reports/tables, the added shallow-moment and factor-control protocols/results/checks/metrics, and the exact primary-source anchors relevant to the disputed comparisons. For the primary literature, Round 1 focused on the packet-listed theorem/equation/section anchors rather than rereading every nondisputed page.

I performed algebraic proof checking and consistency checks against frozen metrics. I did not run new training, rerun supplied code, browse, inspect live paper files, inspect unrelated studies, use Git history, or read another advocate/reviewer report. I did not verify unrestricted priority beyond the frozen packet. The frozen source-bundle build gap described in O8 prevented an independent rebuild of the exact V1 PDF without consulting forbidden live assets.

## Round 1 factual claim ledger

1. **F1-R1.** V1 correctly counts Variant B's complete moving state as history factors plus a symmetric Gram and clock, yielding `O(Hmn epsilon^{-1/2}+epsilon^{-1})` before common outer blocks.
2. **F2-R1.** The history-only crossover is exactly `2mP<n`; neither convergence theorem guarantees that its sufficient order lies below this or the complete-state crossover.
3. **F3-R1.** Total restartable closure storage includes dense initialized `W_0`; Variant B additionally includes prefix data and Gram storage, and the reported large closures use more total storage and time than dense flow.
4. **F4-R1.** HiPPO supplies the online scaled-Legendre projection/dilation ingredient but not the neural feedback-coupled reconstruction or fixed-width full-trajectory theorem.
5. **F5-R1.** An order-`q` NTH training hierarchy has a direct `O(m^q)` sample-index count before symmetry reductions; Theorem 2.6 has a width-dependent regime/horizon/error, equation (2.11) adds up to `O(m^(q-1))` test-point values, and the supplied paper demonstrates no truncated solver.
6. **F6-R1.** The ordinary-clock proof contains a complete projection-tail, product-error, depth-induction, feedback, and continuation argument; I found no fatal or major defect.
7. **F7-R1.** For `rho(0)>0`, the response-clock proof obtains its coarse defect and clock bound before the sharp tail and closes physical, residual, Gram, and continuation stops without circularity.
8. **F8-R1.** Variant B's displayed state is undefined at `rho(0)=0` unless a separate convention is supplied for `b=r delta/rho` and its prefix moments.
9. **F9-R1.** The frozen shallow and factor-control evidence supports the numerical values retained in V1, including 29 valid factor-seed comparisons and one excluded two-resolution capped cell.
10. **F10-R1.** The factor control matches the exact initial network but matches dense initial middle-matrix velocity only in expectation over its random factor, not for each realized seed.
11. **F11-R1.** The experiments are predominantly separately stopped matched-loss comparisons and do not measure same-time full-parameter errors or either theorem's order-rate slope.
12. **F12-R1.** `BOOK_OBSERVABLE_CLOSURE.qmd` C.4.7.9 proves a restartable finite-type autonomous population closure with compact-time prediction/observation convergence, but its probability-law state and population target do not meet V1's fixed-finite-network finite-scalar contract.
13. **F13-R1.** V1 disclaims unrestricted priority and limits its literature conclusion to a reviewed nonexhaustive set.
14. **F14-R1.** The frozen TeX points to unversioned bibliography and figure paths and therefore is not independently build-complete from the permitted V1 files.
15. **F15-R1.** V1's definition of scalar ODE as width-independent conflicts with its table's finite-at-fixed-width definition and with its own `O(HmnP)` state.

## Round 1 evaluative claim ledger

1. **E1-R1.** The central positive-residual compact-horizon trajectory theorems survive Round 1 and constitute a nontrivial specialized theory contribution.
2. **E2-R1.** The learned-increment representation is genuinely compressed only in a conditional state-count sense; no proved useful-order crossover, total-memory reduction, or runtime acceleration follows.
3. **E3-R1.** Retained dense `W_0` actions and unfavorable measured total resources rule out a current efficient-training or systems-breakthrough interpretation.
4. **E4-R1.** The product-of-projection-errors identity and response-clock bootstrap are the strongest sources of mathematical significance after known HiPPO, hierarchy, and population-dynamics ingredients are credited.
5. **E5-R1.** Omitting the local C.4.7.9 autonomous population theorem materially weakens the current significance positioning but does not displace the fixed-finite-width full-parameter theorem.
6. **E6-R1.** The experiments support implementation and selected matched-loss predictor fidelity; they do not validate trajectory rates, robust low-order behavior, or practical response-clock superiority.
7. **E7-R1.** The factor-control result is valid for its stated metric, but the realized initial-velocity mismatch should be disclosed before drawing mechanism-level conclusions.
8. **E8-R1.** No unrestricted priority or field-wide breakthrough conclusion is supportable from the frozen nonexhaustive packet.
9. **E9-R1.** After the five localized V2 repairs above, the manuscript can credibly present a strong specialized theorem about finite-width response-history model reduction without implying net resource compression or empirical rate validation.
