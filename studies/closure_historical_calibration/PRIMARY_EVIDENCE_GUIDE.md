# Primary evidence guide

This is a source packet for a report-and-theorem assessment. It contains no new
experiment, proof, literature comparison, significance rating, or recommendation.
The coordinator controls its release. Statements below locate what the sources
assert; packet preparation did not repeat their proofs, numerical runs, or audits.

The frozen root is
`data/generated/closure_historical_calibration/primary_packet/frozen/`.
Paths below are relative to that root unless explicitly described as original.
The frozen tree preserves repository-relative paths for `docs/`, `code/`,
`studies/`, and the copied parts of `data/generated/`. Original large arrays and
checkpoints remain in their existing namespaces; this packet is not a standalone
training reproduction bundle.

## Packet identity and reading boundaries

The freeze contains 3,227 copied files, with 61,204,232 source bytes. The exact
freeze timestamp and per-file SHA256 values are in `../MANIFEST.json` relative to
the frozen root. The recorded Git HEAD is metadata only: several primary sources
were uncommitted, so source bytes and hashes identify this packet.

- `SOURCE_MAP.tsv` and `MANIFEST.json` map every copied source to its frozen copy,
  original hash, copied hash, size, and whether text changed.
- `REPORT_LOCATIONS.json` gives the original one-based line of every heading in
  the copied study reports and plans. Line numbers are preserved in the copies.
- `REFERENCED_ARTIFACTS.json` resolves report links, identifies copied results,
  and records original locations and hashes of referenced compact NPZ/CSV files
  where needed. No linked artifact within the seven authorized generated-data
  namespaces was missing at the freeze.
- `OMISSIONS.json` records excluded files and the reason for exclusion. Large
  state files are inventory entries, not newly hashed numerical evidence.
- `SANITIZATION.json` gives the exact source and line range of every text edit.
  There is one edit: `studies/first_order_dimension_mnist/PLAN.md:66`, replacing
  an administrative reference to other research milestones with “or extend the
  scope beyond this study.” Its scientific configuration and provenance text
  are unchanged.

`docs/README.md` is excluded in full because it contains strategic roadmap and
contextual assessment prose. It was used as a locator only. The complete nine
other canonical Markdown files are retained, including proof bodies and their
cross-chapter dependencies. Scientific code, tests, scripts, validation plans,
and `code/README.md` are retained; the PDF-export tooling and caches are omitted.

All `NOVELTY*` files and prior assessment/debate directories are excluded.
`first_order_dimension_mnist/README.md`, including archived copies bearing that
name, was not opened and is excluded in full. Whole-file exclusions have no
invented line range: they mean every line. The other experimental READMEs are
retained as primary records, with their numerical limitations and correction
history. Scientific implementation/consistency audits such as `REVIEW_RUNNER.md`
and `SYNTHESIS_AUDIT.md` are retained; their correctness or numerical-criterion
labels are not significance grades. No prior novelty reports, significance grades,
or debate records were opened.

The permitted `closure_feature_geometry` folder contains only a planning README
and no generated files. Its planning text is omitted; this folder supplies no
completed scientific result to the packet. No other study was used as an input.
Historical links and source-hash metadata may mention old locations. They do not
authorize reading another study or an excluded document. In particular, older
links to `docs/README.md` should be replaced by the theorem locations below.

## Common model, normalization, and observables

The notation contract is `docs/NOTATION.md`, in full. The common finite model is
the bias-free network with two tanh hidden layers and scalar output:

\[
u=x/\sqrt d,\quad h^1=\tanh(W_1u),\quad
h^2=\tanh(W_2h^1),\quad f_n=c^Th^2/n.
\]

The stored independent Gaussian entry variances are `(1,1/n,1/n²)`; loss is
the probability-weighted, unhalved squared residual; gradient-flow block
mobilities are `(n,1,n)`. The finite network keeps its random initial readout.
The corresponding population closure begins with zero readout. Numerical Heun
steps approximate this physical gradient flow; they are not literal raw-GD
updates. The input dimension, horizon, and law in any theorem remain explicit.

The finite observable closure retains two complete joint mark populations and
one evolving coefficient matrix `M`; its reverse action uses the actual
transpose. In `docs/global_nonlinear.md:13431–13521`, equations (H3.N1)–(H3.N6)
specify the retained marks, ridge, forward/backward fields, dynamics, observables,
and limit order. The evolving state is `(w,c,M)`; the initialization is
`w=g,c=0,M=D`. Population-node quadrature `P`, coefficient/Gram quadrature `Q`,
closure order `N`, time step, arithmetic precision, and network width are
different parameters.

For circle experiments, `d=2`, `u=(cos θ,sin θ)`, and `x=√2u`.
An activation Gram entry is the within-layer average of the product of two
activations, not a weight Gram or centered correlation. Reports distinguish
absolute matrix RMS `||G−Gref||F/m` from relative Frobenius error
`||G−Gref||F/||Gref||F`. They also distinguish raw activation RMS, paired
initial/current motion, and `G(t)−G(0)`. Mean network loss usually means the
mean of the individual losses, not the loss of the mean prediction.

Circle output errors compare saved functions on stated finite panels with
actual-network seed means or individual seeds. Without a separately specified
off-training target law, those are function-agreement/extrapolation comparisons.
They are not off-training teacher-risk measurements. A finite saved panel or
time grid is not a certified continuous-input/time supremum.

## Canonical theorem and implementation locations

The complete chapters are supplied to preserve dependencies. The table is a
locator, not a replacement for hypotheses and proof bodies.

| Source location | Statement and scope to inspect |
|---|---|
| `docs/special_data_limits.md:3789`, theorem at `3820`; source equations at `3954–3966` | III.F.1 and following sections: fixed finite Gaussian programs, reused action/adjoint laws, regularization and common-space construction. C.4.7.9 explicitly lists III.F.1–10 among its dependencies. |
| `docs/global_nonlinear.md:3836–3981` | C.4: model, local two-hidden-tanh training-law theorem and observation conventions. |
| `docs/global_nonlinear.md:8989–9170` | C.4.7.1: changed-law model, theorem and observation contract; ensuing C.4.7.2–7 provide the complete estimates and actual finite-GF identification. |
| `docs/global_nonlinear.md:11441–12083` | C.4.7.8: current bounded-probe hierarchy; theorem at `11493`, initialized observation alphabet, exact weak evolution, invariance and reached restart. |
| `docs/global_nonlinear.md:12084–12554` | C.4.7.9: finite autonomous population closure; theorem at `12101`. At separately fixed law in its stated neighborhood and `T=1/200`, nested feature spans converge in whole-circle/time predictions and specified same-layer joint observations in W2. No numerical rate or resource rate is asserted. |
| `docs/global_nonlinear.md:12555–13160` | C.4.7.10 A: short-time canonical population flow and actual finite-GF identification. Proposition at `12607` treats the stated bounded-label circle laws through `T=1/200`. The executable numerical family is stated separately in part A. |
| `docs/global_nonlinear.md:13161–13430` | C.4.7.10 B: compatible initialized-word/Chebyshev hierarchy, density, action orientations and odd-degree enrichments. |
| `docs/global_nonlinear.md:13431–13981` | C.4.7.10 C: finite numerical theorem at `13481`, equations and complete arithmetic/integration proofs. Refinement order is precision, time steps, input quadrature, population quadrature, initializer quadrature, source regularization, then closure order. No arbitrary simultaneous refinement or tolerance selector follows. |
| `docs/global_nonlinear.md:13982–15736` | C.4.7.10 D: time-40 construction, its full proof, closure and numerical limits. The fixed supported radius is `ρ=2^(−E10)`, with `E0=8192`, `E(j+1)=2^Ej`; laws lie near the two orthogonal reference axes. D.1 defines the represented rational-endpoint family; D.3 states the population law class, and D.4 gives numerical limits. Wider resolved arcs, sparse-circle tests, and MNIST are outside this stated time-40 family. |
| `code/pde/observable_initialization.py:105,305` | Dictionary construction and joint initialized features; all source and dependent arithmetic/compiler modules are retained. |
| `code/pde/observable_solver.py:113,157,168,204,225,265,318` | State, initializer, fields, vector field, Heun evolution, paired observations and restart. |
| `code/pde/observable_laws.py`, `code/README.md` | Exact supported-law representation, numerical radius collapse, resource allowances, operational validation and limitations. |

The time-40 numerical examples may collapse the positive supported radius at
their declared precision; that operational limitation is part of the sources.
Neither this freeze nor an empirical comparison enlarges a theorem's law family,
horizon, dimensional scope, or limit order.

## General-dimensional first-order construction and MNIST records

All locations in this section are under `studies/first_order_dimension_mnist/`.
`INITIALIZATION_THEORY.md:11–171` states and derives the general-d first-order
coefficient target; `:172–203` gives exact antithetic folding and its conditions;
`:204` onward records precommitted checks and their outcomes. These are
study-owned construction identities, not a general-d trained-network convergence
theorem. `MODEL_SCOPE_CHECK.md:15–112` records the metric, initialization, state
counts, folding interpretation, and reporting qualifications.

The full dictionary has dimensions `(2d+1,d+1)`, with the reverse-response term
retained and ridge `1/4096`. The initialized coordinate blocks do not constrain
the subsequent full learned `M`. Numerical scalar/two-dimensional Gaussian
quadrature on a truncated interval computes the coefficients; it is not an
exact-integral certificate. Nominal even `P` represents `P/2` independent base
draws and their negatives in each population. Consequently `P=n` does not equate
independent sample counts or approximation errors. Moving-state storage is
`O(Pd+d²)`, with fixed marks, caches, integration stages, checkpoints and data
additional. `MODEL_SCOPE_CHECK.md:55–112` includes those array counts and limits.

Implementation sources are `P1_INITIALIZATION.py` (coefficient routine at line
77, initializer at 145), `P1_ENGINE.py` (engine at 36), and `NETWORK_ENGINE.py`
(engine at 12). `COMPUTE_REPORT.md`, `ENGINE_CHECK.py`, `REPLAY.py`, and
`REVIEW_RUNNER.md` retain algebraic checks, runner corrections, raw-IDX checks,
checkpoint replay and the limits of those checks. The numerical configurations
are in `PLAN.md`, `PCA_PLAN.md`, per-run `config.json`, and producer snapshots.

| Recorded comparison | Configuration and result locations |
|---|---|
| Original 784-coordinate MNIST 3 versus 5 | 10,552 training, 1,000 validation and 1,902 official-test images; per-image division by 255 and Euclidean normalization; seeds 1729/2718/3141. Width/nominal P 2048 and later 4096; fixed order p=1. Float32, TF32 disabled, full-batch Heun, network step .25 and closure step .125. Validation-based continuation reaches at most T600. `REPORT.md:84–162` records the 2048 campaign; `:53–82` records the later full 4096 campaign. |
| 4096 equal-time validation outputs | At T600, relative RMS of each closure against the three-network mean is 5.32–5.48%; `REPORT.md:53–82`, `FULL_4096_CHECK.md`. This includes all seed pairs, worst errors, half-step controls and finite-seed qualifications. |
| 4096 matched training loss | Nearest saved closure snapshots at T380/370/370 match the mean network terminal loss approximately; relative RMS becomes 4.45–4.61%. Worst individual error and sign disagreement do not uniformly improve. `REPORT.md:13–51`, `MATCHED_LOSS_PLAN.md`, `MATCHED_LOSS_CHECK.md`. This is saved-output postprocessing. |
| PCA98 representation | Centered PCA fitted only on the training split retains 240 components and 98.00167% of centered variance, without whitening or renormalization. It retains 53.05% of original uncentered energy. `PCA_REPORT.md:17–42`, `PCA_DATA_CHECK.md`. |
| PCA common-loss outputs | One attainable MSE, .011080311898, is used across all twelve original/PCA runs, with nearest saved training-loss selection. PCA closure versus PCA network relative RMS is 4.09–4.62%; versus the original-input network it is 10.41–11.23%. `PCA_REPORT.md:83–137` retains equal-time, own-reference and common-loss comparisons separately. |
| Computation | Crossed RTX3090 timing repetitions use common T100, the same steps and both device assignments. PCA closure versus PCA network integration speed ratios are 3.75–3.96, with 80.20% less peak live allocated training memory. These are fixed-horizon implementation measurements, not time-to-matched-loss or asymptotic rates. `PCA_REPORT.md:44–81`, `PCA_SPEED_CHECK.md`, and the earlier `SPEED_4096.md`/`SPEED_4096_CHECK.md` retain all repetitions. |

The copied reports retain failed coarse-step pilots, the correction from an
unbalanced pilot validation subset, all final numerical controls, PCA's change
to the learned representation, and absent full-horizon float64 checks. Validation
participates in stopping. No higher-order MNIST comparison was executed.
`REPORT.md` explicitly retains historical 2048 text after the later 4096 sections;
its old deferral statement does not erase the subsequent completed 4096 campaign.

Numerical provenance is under original/frozen `data/generated/first_order_dimension_mnist/`:
`validation_analysis_002/`, `validation4096_001/`, `width_comparison_001/`,
`matched_loss4096_001/`, `pca_analysis_001/`, `pca_benchmark_analysis_003/`,
the `main*`, `controls*`, `pca4096/`, `pca_controls/` configuration/summary trees,
and dedicated replay/check folders. CSV per-image exports are copied. NPZ
predictions, prepared data and full states have original-path provenance in the
artifact map/inventory; report-linked compact prediction archives are hashed.

## Circle numerical campaigns, including adverse outcomes

All reports/plans in each listed study are copied in full. This table identifies
the experimental configurations and qualifications, rather than selecting one
reported outcome for assessment.

| Study and report locations | Recorded configurations and qualifications |
|---|---|
| `wide_network_closure_comparison/WIDE_GPU_20260914_REPORT.md:9–111` and matching plan | T40, axis and radius-1/20 arc laws; widths 2048/8192, seeds 11/29/47; 16 network and eight closure trajectories. Orders 1/3/5, base Q1024/P512, with N3 quadrature doubling. Network step .01, closure .005; matched controls. Raw RMS and paired motion are separate. The complete numerical agreement criterion remains inconclusive because the N3 quadrature diagnostic exceeds its cutoff and is not an N5 bound. |
| `wide_network_closure_comparison/GRAM_20260914_REPORT.md`, matching plan | Original trajectories replayed with full training/circle Grams at 206 saved times; 24 replays plus two time-step controls. Complete order, layer and panel tables remain in the report. Quadrature sensitivity is retained. |
| `wide_network_closure_comparison/ARC30_20260914_REPORT.md:18–202`, matching plan | Sixteen training inputs spanning ±30° around two axes; eight networks and eight closures through T40. N5 Q/P refinements reach 4096/2048. Different layers have different order trends; several Gram controls remain above the .002 diagnostic cutoff. |
| `wide_network_closure_comparison/LONG_20260914_REPORT.md`, original plan and later `LONG_20260914_SANITY_SCOPE.md` | Same sixteen configurations continued/replayed through T640, later main step .05 and control .025. The strict original settling test fails 314/416 conditions; quadrature remains unresolved. Four just-launched T1280 workers were cancelled before saved observations. Reports retain the later mild stopping scope and original test separately. |
| `xor_network_closure/REPORT.md:15–126`, `EXPERIMENT_PLAN.md`, `RADIAL_NTK_PLAN.md`, `MATCHED_NTK_PLAN.md`, README | Shifted four-pole sixteen-input law with centers 0°,90°,150°,240°, signs +,−,+,−; T100, widths 2048/8192 and three seeds. Eight networks and eight closures, base Q2048/P1024 with doubled quadrature and time controls. The full network and frozen-readout baseline differ in loss; closure whole-trajectory agreement fails and all three quadrature checks remain unresolved. The later full initial NTK/matched-loss results are retained separately from the initial readout-only control. |
| `quadrant_network_closure/README.md:23–118,149–183`, `EXPERIMENT_PLAN.md`, `NTK_PLAN.md` | Sixteen first-quadrant inputs in four alternating-label clusters; T100, widths 2048/8192, seeds 11/29/47, step .01; Q2048/P1024, doubled controls, orders 1/3/5. The output and Gram metrics differ. All three quadrature controls fail their gates. The later full initial NTK is compared at matched per-seed training loss, with very different physical times. The loss-slider interpolation uses another explicitly stated ensemble-loss convention. |
| `closure_endpoint_discrimination/README.md:11–154`, all plans, `PAIR_ENDPOINT_SCOPE.md` and `PAIR_FOLLOWUP.md` | Twenty-four inputs near six fixed centers, six prespecified label stages. First finite-time separation case is stage 5. Main Q8192/P4096, two quadrature refinements; width8192 network seeds 11/29/47, width/precision/step controls; main step .02. Last complete common comparison is T1000. None of eighteen trajectories meets the frozen plateau rule; N5 last quadrature and network half-step controls also miss thresholds. T1100 is incomplete, with storage-limit interruption and retained failure/recovery records. |
| `closure_circle_spectral_mechanism/PLAN.md`, `INSIGHT.md`, `THEORY.md`, `NTK_THEORY.md`, `SYNTHESIS_AUDIT.md` | Initial 75 trajectories cover fifteen two-/three-/four-point laws, primary orders 1/3/5 and specified N2 diagnostics, through mildly settled T100–120. Two of thirteen quadrature checks fail; amplitude/rotation cases and some geometries lack matched controls. Exact representability/parity/kernel identities are separated from empirical reached trajectories. N is mark-polynomial order, not an angular Fourier cutoff. |
| `closure_circle_spectral_mechanism/NET_COMPARISON.md:9–103`, `NET_PLAN.md`, `NET_VERIFY.md` | Twenty actual-network trajectories: pair separations 15°/30°/90°, widths 1024/4096, three seeds plus two controls, T100. N1→N3 output-error improvement is observed in all three cases; N3→N5 is geometry dependent. Matched control coverage is incomplete, closure quadrature affects smaller differences, and the conditional 8192-width branch was not launched because of storage reserve. Tanh–sine fitting describes saved functions, not a label-only predictor or an endpoint-selection theorem. |
| `closure_circle_spectral_mechanism/MULTI_NET_COMPARISON.md:17–125`, `MULTI_NET_PLAN.md` | Forty-eight actual-network runs: six three-/four-point laws, widths 1024/4096, seeds 1729/2718/3141, .02 main and .01 controls, through T120. Primary comparison uses common T100. N3 has less measured error than N1 in all six; N5 has less than N3 in three and more in three. Only the four-point 30° case passes all available order-improvement control checks. Other cases retain failed/missing closure quadrature qualifications. |

The circle algebra in `closure_circle_spectral_mechanism/THEORY.md` is
study-owned: exact input oddness starts at line 90, conditional N2 redundancy
at 127, the evolving-kernel identity at 168, and the representability versus
reachability distinction is explicit. `NTK_THEORY.md:27–193` supplies the
initial-kernel scaling, weighted physical-time solution, and balanced-pair
formula. `SYNTHESIS_AUDIT.md` preserves sparse-data Fourier coupling and
amplitude/frequency limits. These sources do not establish general monotone
order accuracy, a selected endpoint formula, or long-time hierarchy convergence.

## Numerical result provenance and omissions

The original and frozen generated-data prefix is `data/generated/<study>/`.
Complete compact summaries, per-run configurations, producer Python snapshots,
execution/failure logs, hash/verification records, CSVs and PDF reports are copied.
The principal result roots are:

| Study | Generated result roots |
|---|---|
| wide_network_closure_comparison | `WIDE_GPU_20260914_202109Z/`, `GRAM_20260914_v1/`, `ARC30_20260914_v1/`, `ARC30_20260914_frozen_baseline_v1/`, `LONG_20260914_v1/` |
| xor_network_closure | `run_001/`, `radial_output_001/`, `radial_output_002/`, `radial_ntk_001/`, `radial_ntk_matched_001/` |
| quadrant_network_closure | `run_001/`, `ntk_001/`, `loss_explorer_001/` |
| closure_endpoint_discrimination | `campaign_001/`, including all six screen stages and stage_05 `analysis_1000.json`, `focused_1000.json`, `final_audit_1000.json`, `verification_1000.json`; partial T1100 and checkpoint-retirement records remain identified. |
| closure_circle_spectral_mechanism | `campaign_001/analysis_final/`, `verification_final/`, `network_comparison_001/analysis_final/`, `network_verification_main/`, `network_comparison_multi_001/analysis_final/` and `verification_final/` |

Where a report cites a raw array that is not copied, the original path is
recorded, and its preexisting producer/analysis record supplies used-source and
output digests. `REFERENCED_ARTIFACTS.json` additionally hashes directly linked
NPZ/CSV files up to 10 MiB. Large NPY/NPZ/PT/JSON checkpoints, image duplicates,
compiled viewers, historical non-code source snapshots, and caches are not
duplicated. Historical retired state bytes remain unavailable exactly as their
retention reports disclose. Metadata about an original artifact is not a claim
that its contents were reread or its entire historical run reproduced.

The packet retains the complete numerical reports rather than favorable
extracts. Its limits are those documented in the reports plus the bounded
copying policy above. No external scientific source was retrieved; cited external
papers/data URLs are references in the primary source, not newly inspected inputs.
The copied source/hash checks verify this freeze's identity, not the truth of
every theorem or experimental conclusion.
