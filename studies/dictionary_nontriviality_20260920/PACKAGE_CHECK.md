# Scoped author-side check of PACKAGES.md

Date: 2026-09-20.

Status: internal design review only. This is neither an independent promotion review nor empirical validation. No experiments were run and neither reviewed design file was edited.

## Frozen inputs and scope

- Reviewed completely: `studies/dictionary_nontriviality_20260920/PACKAGES.md`.
  SHA-256: `806ef79fc6bd3ee7f299c8db9402dd0e559cfa4508027c9ac34cced619379eac`.
- Comparison design, read completely: `studies/dictionary_nontriviality_20260920/BASELINE_DESIGN.md`.
  SHA-256: `9adb4ac430dfd8c2545da24aae62a20ebd704ce9ab0daad22af5c357d008170b`.
- Other scientific input: the original scoped assignment and supervisor clarifications already incorporated into the baseline design.
- Process input: the required investigate-conjectures skill and its research-contract, decisive-experiments, and adversarial-audit references.

No other study files, maintained scientific sources, code, web sources, or generated data were read. In particular, this check does not independently verify the target's citations to C-H3, the maintained equations, or a future depth adapter. Those source and implementation checks remain outside this assignment. Line references below identify the hashed PACKAGES.md version.

## Overall assessment

The framework is substantially fair and addresses the central distinctions in the baseline design. It lets generic features, standard response/POD structure, and simpler practical models succeed. Its outcome rules do not require the existing dictionary to win. It correctly treats hierarchy convergence as different from efficient approximation and a future-snapshot reconstruction result as different from autonomous prediction.

Five clarifications should be incorporated before the execution manifest is frozen. None establishes a scientific failure of the proposed dictionary or of a competitor; no empirical claim can be assessed from this design alone.

## Actionable findings

### F1. Independent frozen random columns are a legitimate baseline

Location: line 235, C-N3.

The phrase “Independent resampling of dictionary columns ... are deliberately incorrect negative controls” is too broad. Independent columns drawn once and frozen form a legitimate random-feature dictionary and are already represented in C-N1. Independence can remove the candidate's designed correlations without making the alternative's own closure internally inconsistent.

Clarify that the deliberately incorrect operation is, for example, redrawing nominally frozen variables during a rollout, using inconsistent copies of one required shared mark in different equations, or failing to use the same operator and its transpose. A newly sampled frozen dictionary should remain an admissible competing model, with its own complete joint law, coefficient initialization, and charged costs. Merely changing the candidate's joint distribution can instead be a valid changed-construction ablation if implemented consistently and labeled accordingly.

Severity: conditional fairness issue. If read literally during baseline selection, the sentence could exclude a valid simple competitor; otherwise this is a wording repair.

### F2. Specify a common observable space for population-law metrics

Location: lines 110–119, especially “complete initial/current joint laws” at line 113.

Avoiding arbitrary pairings between different population clouds is correct. The design still needs to specify the common typed observable vector whose joint law is compared. Dictionary-specific features and descriptors can have different dimensions and meanings, so their raw laws are not automatically comparable. Requiring a generic dictionary to reproduce the candidate's feature coordinates would measure agreement with a representation choice rather than with dense training dynamics.

Before population execution, define the common physical initial/current quantities, input evaluations, layer identifiers, weights, and metric. Keep native dictionary metadata for provenance without silently inserting it into the co-primary fidelity metric. If some initialized mark is scientifically required, specify how every entrant obtains or reconstructs the same mark with its cost included. Report a finite collection of empirical law diagnostics as such; a sliced metric or Gram matrix does not establish equality of an unspecified complete joint law.

Severity: necessary metric specification for the population arm. The finite common-carrier paired-RMS arm already avoids this particular ambiguity. This is a pre-execution obligation rather than an observed invalid comparison.

### F3. Allocate the depth panel explicitly within the trajectory caps

Location: line 290 and stage table lines 326–327.

The opening proposes the L=2 anchor and an L=3 benchmark, but the broad-screen count of 72 equals six methods × three budgets × two seeds × two tasks at one depth. Its four dense trajectories likewise cover one depth. The twelve dense confirmation trajectories cover six seeds × two tasks at one depth. Running the stated panel in full at both depths exceeds those allocations.


Resolve this by declaring a primary depth for the full screen and confirmation, reserving a bounded L=3 adapter/stress check in another stage, or by explicitly splitting the existing cases across depths. Preserve the total caps. Do not silently treat uncounted depth runs as validation overhead. The current statement that breadth must shrink when validation needs more resources is appropriate; the manifest needs the actual allocation.

Severity: execution-plan ambiguity. It does not affect the conceptual baseline comparison, and the document already labels this envelope as awaiting instantiation.

### F4. Preserve the explicitly permitted burn-in initialization

Location: line 271, compared with the P_tau discussion in C-N2.

“Dense checkpoint resets belong only to defect tests” conflicts literally with the legitimate P_tau method, which initializes an autonomous reduced continuation once from the dense burn-in checkpoint. The earlier section correctly labels and charges this training-assisted construction.

Qualify the restart rule: own-state restarts are required for an existing autonomous rollout; dense resets during an initialization-only rollout are forbidden; one declared reset at the end of the charged P_tau acquisition interval is permitted as part of that method's initialization. Further dense resets must not be included in its reported autonomous continuation.

Severity: minor local inconsistency with a clear repair.

### F5. Separate native-ridge utility from a common-filter span comparison

Location: the common-finite construction in lines 42–48, spectra/cost reporting in lines 129–136, and the first C-N3 ablation.

The document correctly distinguishes a positive contraction from an orthogonal projector and gives a correct same-span invariance requirement. It also describes the finite experiment as isolating representation and filtering together. That is sufficient for a comparison of complete methods, but it does not yet specify a cross-dictionary test that attributes a gap to the approximation span rather than the native filter or coefficient metric. Equal raw rank and the same numerical ridge parameter do not imply equal contraction strength when feature scaling and Gram spectra differ. Reporting those spectra is valuable but does not itself remove the confounding.

Preserve the complete candidate with its native feature normalization and ridge schedule as one panel. For a separate labeled span/filter ablation, orthonormalize each numerically resolved span under the same population inner product, disclose numerical rank thresholds and any lost directions, and prescribe a common contraction-strength rule and coefficient metric across the resulting bases. For example, a common scalar contraction α_l times the orthogonal projector at each layer is a clear matched-filter target; the α_l rule must be frozen without future evaluation access. Other matched spectra require equally explicit ordering and matching rules. Count orthonormalization, filter construction, and all retained ranks and arrays.

This second panel defines a changed model family. Do not call it a native candidate run or a pure coordinate change: replacing its original contraction generally changes the initialized represented operator, and adopting a shared metric can also change its native dynamics. A genuine same-span invariance check instead transports the original operator, coefficients, and mobility and leaves the physical dynamics intact. Keep these two operations distinct in results and causal claims.

Severity: conditional attribution gap. It does not block reporting a complete native method's empirical error/cost advantage, but it blocks attributing that advantage specifically to its span while a filter/metric explanation remains unmatched. This clarification follows the supervisor's additional bounded audit question; no additional scientific source was read.

## Safeguards that are already present

| Audit topic | Assessment of the hashed design |
|---|---|
| Information access | I0/IX/IY/P_tau/O are separated, labels used for construction are distinguished from ordinary supervised training, donor/evaluation separation is required, and future POD is confined to oracle diagnostics. |
| Zero backward field | Correctly distinguishes the exact-zero population readout from the finite small random readout; synthetic nonzero readout/hidden probes and exact initial responses are labeled rather than called actual initial backpropagation. |
| Random span versus rotation | Distinguishes a changed random span and orthogonal-frequency construction from rotation of existing dictionary columns. |
| Ridge and mobility | Calls the native ridge embedding a positive contraction, requires transport of initialized operators and mobility under general reparameterization, and labels native re-whitening as a changed intervention. Cross-dictionary filter/metric matching still needs the separate panel specified in F5. |
| Forward/backward versus balanced POD | Explicitly requires a dynamical linearization and its actual adjoint for genuine balanced POD. |
| Reconstruction versus dynamics | Keeps offline projection, vector-field defect, and autonomous rollout separate, and does not convert oracle POD reconstruction into a nonlinear rollout lower bound. |
| Finite versus population carrier | Charges finite n×r tables and endpoint variables; requires an explicit replay/extension rule for a population entrant; rejects neuron-column matching as transfer. |
| Numerical and resource fairness | Accounts for construction, snapshots, stored dense operators, runtime, memory, and independent approximation axes; caps verification work inside the budget. |
| Simple models can win | C-N1 confirms the strongest screened generic competitor; C-N2 allows POD/low-rank explanations; C-N4 includes narrower networks and output-side models; decision rules explicitly include generic advantage and generic equivalence. |

## Manifest details to retain without expanding the study

These are implementation specifications already anticipated by the design, not requests for additional experiments:

- Freeze identical actual finite-network endpoint initializations in the common-finite arm, while retaining the canonical zero-readout population initialization as a separately labeled setting.
- Name the positive semidefinite kernel used by a Nyström entrant, the descriptor vector and scaling of mark features, and the domain/codomain and input dependence of every Krylov/adjoint application.
- Specify a common snapshot-family weighting and a probe distribution/count. Do not divide a zero backward column by its norm or replace it with unlabeled noise.
- State the hidden-motion error normalizations and zero-signal handling before applying the proposed 0.1 threshold. Preserve raw values and the prediction-error numerator/denominator.
- Distinguish an empirical minimum-cost point chosen from the entire evaluated rank grid from a rank-selection rule that could be deployed without access to a future dense reference. The existing “empirical frontier, not an automatic accuracy certificate” caveat is appropriate.
- Treat the two target functions as fixed tested tasks in any uncertainty statement; nested dictionary draws are not additional initialization replicates. The design already makes the latter point.

## Can a simple baseline genuinely win?

Yes, under the stated decision rules. A generic competitor can obtain the reverse cost advantage at the common accuracy threshold, or support replacement through the stated equivalence interval. A past-POD winner must retain its acquisition cost and access label; a future-POD winner remains a representation diagnostic. An inexpensive input-side predictor can make the closure unnecessary for the tested prediction task without claiming hidden-state fidelity.

One useful reporting refinement is to retain bounded-budget dominance when one method reaches the accuracy target and another never reaches it on the predeclared grid. An unknown extrapolated cost ratio may prevent the factor-of-two decision, but it should not erase the observed success/failure contrast. State that bounded-grid result separately and symmetrically for either winner. This is compatible with the existing rules on censoring, nonattainment, and avoiding unearned accuracy certificates.

## Scope of the conclusion

The design supplies a credible comparison framework after the listed clarifications and the already-required run-manifest specifications. This assessment gives no performance ranking, theorem validation, implementation approval, or promotion verdict. The highest-leverage design repairs are to separate native-method utility from common-filter/metric span attribution and to make the population observable contract explicit. The admissible random-column distinction, schedule, and restart wording are local repairs.

---

## Focused correction check: PACKAGES.md revision 2

Date: 2026-09-20. This section appends a correction check without changing the original findings above. It is an author-side design check, not launch approval, independent promotion review, implementation verification, or performance validation.

Read completely: revised `studies/dictionary_nontriviality_20260920/PACKAGES.md`, SHA-256 `03b564f38962794eb6de5e98f1c3ea47af63f621f48a2ff01d9cc4d4f4ff75fd`.

The preserved `PACKAGES_V1.md` has SHA-256 `806ef79fc6bd3ee7f299c8db9402dd0e559cfa4508027c9ac34cced619379eac`, matching the original review target. Its content was not needed again; only its hash was checked. The review report immediately before this append had SHA-256 `7954990881c18b328fd93ab7ead28220eced416729c72d5eae47d3b152476d39`.

| Finding | Revision-2 correction | Assessment |
|---|---|---|
| F1: independent frozen columns | C-N3 now explicitly admits columns drawn once and frozen, and consistent changes to the joint law. Incorrect controls are restricted to changing nominally frozen variables during rollout, inconsistent reuse, and broken transpose reuse. | Addressed. Valid random-feature competitors are no longer excluded by the wording. |
| F2: common population observable space | The metrics section defines layerwise physical tuples on a common input list, keeps initial/current pairs within each population, excludes candidate-specific dictionary coordinates, requires component scales and per-component errors, and limits claims based on finite law diagnostics. | Addressed at contract level. The listed manifest specifications remain necessary before numerical use. |
| F3: depth allocation | The full screen and confirmation now use exactly one primary depth, with a bounded L=2 anchor charged inside pilot allocations; an L=2-only fallback must be selected before screening if the L=3 adapter is unavailable. The text explicitly excludes a full two-depth grid. | Addressed. The stated method/seed/task counts no longer imply an uncounted second depth. |
| F4: burn-in checkpoint | C-N4 now distinguishes own-state restart, forbidden dense resets in initialization-only runs, one charged P_tau initialization, and separately labeled checkpoint diagnostics. | Addressed. The legitimate training-assisted continuation remains autonomous after its declared initialization. |
| F5: native filter versus matched span test | C-N3 preserves the native features/ridge schedule in one panel and defines a distinct common-filter panel with orthonormal resolved spans, Q_l=alpha_l Pi_l, shared alpha_l, a common coefficient metric, disclosed numerical rank losses, and charged preprocessing. It labels the changed initialization/dynamics and keeps that panel separate from operator/filter/metric-preserving invariance. | Addressed at contract level. Span attribution remains conditional on actually implementing the declared matching and the other common information/metric controls. |

The revision also incorporates two useful supporting clarifications: all finite-carrier entrants use the same actual finite endpoint initialization, and one-sided accuracy attainment on the fixed budget grid is reported symmetrically even when a cost ratio cannot be estimated. The explicit generic-advantage and generic-equivalence outcomes remain intact, so a simpler baseline can still win under the contract.

All five original findings are addressed in this revised design. No remaining correction is required within those five audited questions. This closes the wording and design-contract findings only: exact adapters, observable normalizations, numerical rank thresholds, commands, actual case allocations, tolerances, and all other already-required manifest choices remain to be specified and checked before execution. No experiment was performed, no target was edited, and no additional scientific sources or other studies were read.
