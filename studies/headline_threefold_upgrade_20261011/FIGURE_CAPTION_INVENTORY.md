# Existing static figure inventory and caption suggestions

Scoped editorial inventory, 2026-10-11. Inputs were limited to top-level `paper/figures/` static figures and adjacent scripts/manifests, `paper/empirical_appendix.tex`, `paper/plot_figures.py`, `paper/scripts/figures.py`, `paper/scripts/README.md`, `paper/compact.tex`, and `docs/notation.qmd`. Required canonical-notation instructions and their neural-network reference were read. No other study or external generated-data path named in these sources was opened; no experiment or figure was regenerated.

There are **44 PDF stems** at the top level. Every top-level PNG/SVG has a same-stem PDF, so PNG/SVG representations add no further figure stem. Forty-three PDFs have one page; `experimental_gallery.pdf` has seven pages. Different stems frequently contain the same observations in different layouts, as recorded below. The interactive-explainer subtree is outside this inventory.

## Caption conventions and limits

Use the paper's closure-order symbol $q$ in captions; retained old artwork sometimes writes $P$. Here those order labels mean the same number of history modes. Define $f(\theta)$ as the plotted network prediction when describing the radial map $3+f(\theta)$. A plotted RMS is an empirical discrepancy from a dense predictor on the stated query set, unless the caption explicitly says training RMS. It is not an error against unknown labels, a spatial supremum, or a certificate between recorded times. An own-loss endpoint uses a different physical stopping time for each model. A learned correction's rank does not count retained dense initial matrices or establish equal total storage.

Three labels require special care:

- `compression_logarithmic.pdf` and the right panel of `compression_checks.pdf` use **Logarithmic for the earlier seeded finite-word decoder**, expressly separated from Taylor in `paper/empirical_appendix.tex:1` and `paper/scripts/README.md:161`.
- The three `sphere3_*` PDFs also print **Logarithmic**, but their adjacent current rendering scripts call that family **Taylor**, and the shared script guide says Taylor's saved key remains `logarithmic` (`paper/scripts/README.md:28`). They must not inherit the earlier decoder caption. Their historical PDF labels and current script labels differ; the allowed inputs do not include an output-hash manifest establishing that the current scripts generated these exact bytes.
- `learning_in_motion.pdf` and page 2 of `experimental_gallery.pdf` display the **older eight-time** observation set (`experimental_manifest.json:513`); `trajectory.pdf` and `trajectory_rms.pdf` use the **39-checkpoint** replay (`trajectory_capture_manifest.json:1`, `paper/scripts/README.md:419`). Do not describe the older plots as displaying 39 times.

The suggestions below are intentionally one or two sentences. “Support” identifies the exact allowed file/section supporting the caption; PDF text means labels extracted from the named existing PDF. Additional qualifiers are intended for nearby introduction text where they would make an individual caption too long.

## Conceptual illustrations

### 1. `mechanism.pdf`

Suggested caption: “Schematic of response-memory reconstruction: forward and residual-weighted backward histories use the same Legendre modes, and their paired moments reconstruct a learned correction while the initialized mixer remains fixed and retained. Orthogonality cancels mixed retained/omitted terms; a trajectory estimate additionally requires feedback stability.”

Support: the PDF's two panels; related explicit construction in `paper/figures/experimental_figures.py:215` and projection explanation at `:400`. This combines the content of `memory_mechanism.pdf` and `paired_projection.pdf` in a different layout. The printed $O_T(q^{-1})$ and $O_T(q^{-2})$ rates belong to the older finite-horizon schematic; do not identify them as the current global headline estimates. The exact producer for this compact PDF is not among the selected source files.

### 2. `memory_mechanism.pdf`

Suggested caption: “Single-sample schematic with three history modes: a fixed polynomial basis has evolving neuron-valued moment coefficients, whose paired outer products supply the learned connection. The initialized matrix is retained, and responses from the reconstructed network enter subsequent memory updates.”

Support: `paper/figures/experimental_figures.py:215`, `experimental_gallery.pdf` page 1. Same artwork is the first page of that gallery. Its symbols $m_1^{(k)}$ and $m_2^{(k)}$ are the forward and residual-weighted backward moments, respectively; its displayed normalization is the single-sample schematic, not a new general-$m$ model definition.

### 3. `paired_projection.pdf`

Suggested caption: “Both histories are projected orthogonally onto the same history space with the same integration measure, so the two mixed terms vanish and the interaction defect pairs the two omitted histories. Converting this algebraic identity into trajectory control requires separate regularity and feedback-stability estimates.”

Support: `paper/figures/experimental_figures.py:400`, `paper/plot_figures.py:110`, and `experimental_gallery.pdf` page 5. Duplicate conceptual content appears in `mechanism.pdf`; this is a mathematical diagram, not experimental evidence.

### 4. `clocks.pdf`

Suggested caption: “Illustrative four-mode Legendre fits of a normalized backward history in physical time, a residual-speed clock, and a joint clock. The printed RMS fit errors describe this particular illustration and do not establish a general ordering of clock accuracy.”

Support: the PDF labels: $b_1=r_1/\rho$, $q=4$, errors 0.107, 0.142, 0.003, and each horizontal coordinate rescaled to $[0,1]$. **Uncertainty:** the allowed source set does not identify this PDF's generating history or numerical protocol; do not call it a measured neural training experiment or borrow the distinct `learning_clocks.pdf` producer. Avoid adding initialization, seed, integration, or residual-history claims that are not printed.

### 5. `learning_clocks.pdf`

Suggested caption: “A constructed smooth response path is shown in physical time and in a joint clock that includes response motion; corresponding colored events remain the same. This schematic illustrates the change of coordinate and does not assert constant speed or improved low-order accuracy for a measured network trajectory.”

Support: `paper/figures/experimental_figures.py:359`, including the synthetic path construction and explicit footer qualifications, and `experimental_gallery.pdf` page 4. Distinct from the four-mode fits in `clocks.pdf`.

### 6. `moments.pdf`

Suggested caption: “Illustrative reconstruction of three neuron histories using one, two, and three Legendre coefficients, with coefficient distributions across 512 neurons shown below. The displayed median errors are normalized by each history's range; the older nonzero-readout example illustrates memory coordinates and does not validate the canonical initialization theorem.”

Support: PDF labels; `paper/plot_figures.py:68` and `:640`; `paper/scripts/README.md:49`. The cached-data path named by the sources was not opened. The present plotter supports the content and qualification, but is not asserted to have generated the exact older PDF layout.

## Circle fitted-function and order plots

### 7. `circle_deep.pdf`

Suggested caption: “Earlier five-task circle comparison for three tanh hidden layers of width 4096, with dense training and history orders $q=1,2,3$. Each curve is evaluated at its model's own training-MSE $10^{-3}$ endpoint, so the plots compare fitted functions rather than predictions at a shared physical time.”

Support: PDF task/order/endpoint labels; matching deep family described in `paper/scripts/README.md:263` and `paper/empirical_appendix.tex:215`. Cartesian alternative to `circle_deep_radial.pdf` and `circles_deep.pdf`; no per-pixel or hash identity is asserted across different renderers.

### 8. `circle_deep_radial.pdf`

Suggested caption: “Five fitted circle functions for three tanh hidden layers of width 4096 and orders $q=1,2,3$, each at its own training-MSE $10^{-3}$ endpoint. Angle is input direction, radius is $3+f(\theta)$, black points are labels, and printed discrepancies are RMS differences from dense predictions on 8192 circle queries.”

Support: `paper/scripts/README.md:263`, `paper/figures/radial_source_manifest.json:544`, and PDF labels. Same data family and matching printed RMS values as `circles_deep.pdf`; the latter is a more compact row layout. The fixed initialized matrices remain additional storage.

### 9. `circles_deep.pdf`

Suggested caption: “Compact radial view of five earlier circle tasks with three tanh hidden layers, width 4096, and orders $q=1,2,3$, evaluated at each model's own training-MSE $10^{-3}$ endpoint. Radius is $3+f(\theta)$ and the printed values are dense-versus-memory RMS discrepancies on 8192 circle queries.”

Support: existing full caption at `paper/empirical_appendix.tex:215`, matching PDF values, and `paper/plot_figures.py:101`. Duplicate dataset of entry 8 in a single-row layout; the orders do not improve monotonically on both alternating-label tasks.

### 10. `circle_shallow.pdf`

Suggested caption: “Earlier Cartesian circle predictions for two tanh hidden layers of width 2048 and history orders $q=1,3,7$, shown at each model's own training-MSE $10^{-3}$ endpoint. Black points mark training labels, and the memory implementation retains the dense initialized mixer.”

Support: PDF labels and `paper/scripts/README.md:281`. **Reference distinction:** the README explicitly says this older Cartesian shallow figure uses archived dense references for every task, unlike the selected references of the newer radial figures. It is therefore not an interchangeable rendering of entry 11 without this qualification.

### 11. `circle_shallow_radial.pdf`

Suggested caption: “Five fitted circle functions for two tanh hidden layers of width 2048 and orders $q=1,3,7$, at individual training-MSE $10^{-3}$ endpoints. Radius is $3+f(\theta)$, black points are labels, and printed RMS discrepancies use 8192 queries against the selected dense reference for each task.”

Support: `paper/scripts/README.md:263` and `:281`, `radial_source_manifest.json`, and PDF labels. Four fresh dense references and one refined archived reference are used. Same printed values and data family as `circles_shallow.pdf`; the smallest observed discrepancy may be below the observed refinement scale.

### 12. `circles_shallow.pdf`

Suggested caption: “Compact radial view of the five earlier two-hidden-layer tanh circle tasks at width 2048, with orders $q=1,3,7$ and separately fitted training-MSE $10^{-3}$ endpoints. The printed values measure RMS discrepancy from each selected dense reference over 8192 angles, with radius $3+f(\theta)$.”

Support: PDF values match entry 11; `paper/plot_figures.py:133`, `paper/scripts/README.md:263`. Duplicate layout of entry 11, not an additional experiment.

### 13. `order_decay.pdf`

Suggested caption: “Observed circle prediction discrepancy versus history order for the five displayed tasks. The inverse-order reference lines are visual comparisons, not fitted or certified convergence rates.”

Support: PDF labels (orders 1, 3, 7, five task names, $P^{-1}$ and $P^{-2}$ reference curves); `paper/scripts/README.md:59` identifies a separate historical producer. **Uncertainty:** that producer is outside the assigned source set; do not assume this PDF uses the newer selected dense references or copy their numbers into its caption.

### 14. `orders.pdf`

Suggested caption: “Earlier deep-circle endpoint discrepancies for orders $q=1,2,3$, shown alongside coarse/fine numerical sensitivity and the observed ranges of hidden-feature motion. These width-4096, three-hidden-layer tanh runs use individual training-MSE $10^{-3}$ endpoints; sensitivity ranges are diagnostics, not confidence intervals.”

Support: PDF task labels and exact activation ranges 0.35–0.65, 0.38–0.74, 0.46–0.68; corresponding source `paper/figures/experimental_figures.py:460` and `experimental_manifest.json:626`. Compact counterpart of `order_sensitivity.pdf`. State no universal monotonicity in order.

### 15. `order_sensitivity.pdf`

Suggested caption: “Five deep-circle tasks compare dense-versus-memory endpoint RMS, numerical sensitivity, and hidden-activation motion for three tanh hidden layers of width 4096. Each model stops at its own training-MSE $10^{-3}$ endpoint; order 2 is closer than order 3 on the two alternating-label tasks, and the sensitivity curves are empirical diagnostics.”

Support: `paper/figures/experimental_figures.py:460`, `experimental_manifest.json:626`, `experimental_gallery.pdf` page 7. RMS uses 8192 circle queries; activation ranges cover 20 fitted runs, including dense and the three orders. Duplicate data family of entry 14.

## Common-time trajectories

### 16. `trajectory.pdf`

Suggested caption: “Earlier paired-label circle trajectories for two tanh hidden layers of width 2048 and Legendre orders $q=1,3,7$, displayed at the same physical times 0, 5, 20, and 80. Radius is $3+f(\theta)$ and black points are training labels; the 39-checkpoint, two-tolerance Heun replay supplies discrete observations rather than a certificate between them.”

Support: existing caption `paper/empirical_appendix.tex:51`; `trajectory_capture_manifest.json:1`; `paper/scripts/README.md:419`. Spatial RMS, if discussed alongside this figure, uses 2048 queries, not the 8192 queries of fitted endpoint figures.

### 17. `trajectory_rms.pdf`

Suggested caption: “Prediction RMS discrepancy from the dense run for orders $q=1,3,7$ at the 38 positive common times of the width-2048 paired-label circle replay. Lines guide the eye, and the coarse/fine sensitivity scale is an empirical numerical diagnostic rather than a continuous-time error bound.”

Support: PDF labels; `paper/scripts/README.md:419`; `trajectory_capture_manifest.json:1` (39 total times including zero, 2048 queries, two tanh hidden layers, float64 adaptive Heun). Companion metric plot to entry 16.

### 18. `learning_in_motion.pdf`

Suggested caption: “Earlier eight-checkpoint paired-label circle comparison for two tanh hidden layers of width 2048 and orders $q=1,3,7$, with radial snapshots at times 0, 5, 20, and 80. The lower panel measures discrepancies on 2048 query angles; joins guide the eye and dotted coarse/fine sensitivities do not certify errors between observations.”

Support: `experimental_manifest.json:513`, `paper/figures/experimental_figures.py:283`, `experimental_gallery.pdf` page 2. Older observation set than entries 16–17; retaining both repeats snapshots but preserves different time sampling.

## Rank and frozen-kernel controls

### 19. `same_rank.pdf`

Suggested caption: “Selected fitted-circle comparisons of response memory and two seeds of directly trained factors with the same displayed correction-rank bound. The horizontal coordinate is RMS disagreement with dense training at individual training-MSE $10^{-3}$ endpoints; equal correction rank does not imply equal total storage or a comparison against every low-rank optimizer.”

Support: PDF rank/task labels; matching factor-memory and factor-direct records in `experimental_manifest.json:1`; detailed protocol at `paper/figures/experimental_figures.py:313` and `paper/scripts/README.md:532`. This is a selected summary of the broader rank sweep in entries 20–21, not a new dataset.

### 20. `factors.pdf`

Suggested caption: “Paired-label fitted functions and five-task correction-rank sweeps compare response memory with two seeds of directly trained factors in width-2048, two-hidden-layer tanh networks. RMS uses 8192 circle queries at each model's own training-MSE $10^{-3}$ endpoint; the comparison is specific to the displayed factor dynamics, with fixed mixers additional to moving state.”

Support: PDF labels; `paper/figures/experimental_figures.py:313`; `experimental_manifest.json:1`. Compact rendering of entry 21; the source records one capped factor run and limited numerical precision for some other points, so missing points are not successes and very small errors are not exact zeros.

### 21. `same_rank_dynamics.pdf`

Suggested caption: “Earlier fitted-circle control with two tanh hidden layers of width 2048: the paired-label example has correction-rank bound 24, and the lower panels retain the five-task rank sweep with two factor seeds. RMS uses 8192 queries at individual training-MSE $10^{-3}$ endpoints; hollow points have limited numerical precision and one capped run is omitted.”

Support: `paper/figures/experimental_figures.py:313`; `experimental_gallery.pdf` page 3; `experimental_manifest.json:500`. Despite the filename, the figure shows own-loss endpoints, not matched-time dynamics. The result does not compare with every possible factor method.

### 22. `same_rank_radial_preview.pdf`

Suggested caption: “Paired-label fitted functions compare dense training, order-3 response memory, and two factor seeds with correction-rank bound 24. All models reach training MSE $10^{-3}$ at their own times; RMS differences from dense are measured on 8192 angles and radius is $3+f(\theta)$.”

Support: `paper/scripts/README.md:434`; PDF labels; `experimental_manifest.json:503`. Enlarged counterpart of the top row of entries 20–21, not another experiment.

### 23. `frozen_ntk_radial_preview.pdf`

Suggested caption: “Paired-label fitted functions for the dense network, its full initialization-frozen empirical NTK, and order-3 response memory, using the same width-2048 initialization and canonical block mobilities. Each reaches training MSE $10^{-3}$ at its own time; RMS uses 8192 queries, and all panels use radius $30+f(\theta)$ to preserve the large signed NTK excursions.”

Support: `paper/scripts/README.md:451`; `frozen_ntk_manifest.json:1`; PDF labels. The control uses all parameter blocks, no ridge, and no discarded eigenmodes; this is not the zero-readout frozen kernel of the later compression suite or an infinite-width lazy-limit theorem.

### 24. `learning_controls_equal_mixed_odd.pdf`

Suggested caption: “Equally spaced mixed-label task: dense training, the full frozen initial NTK, two trained-factor seeds, and order-3 response memory are compared at their own training-MSE $10^{-3}$ endpoints. Correction-rank bound 12 uses the four-dimensional antipodal quotient; all panels share the output scale and RMS discrepancies use 8192 circle queries.”

Support: PDF labels; `paper/scripts/README.md:532`; `learning_controls_manifest.json` task `equal_mixed_odd`. All methods use the same width-2048, two-hidden-layer tanh initialization; rank equality does not count fixed dense matrices.

### 25. `learning_controls_quadrant_alternating.pdf`

Suggested caption: “Quadrant alternating-label task: dense training, the full frozen initial NTK, two rank-24 factor seeds, and order-3 response memory are evaluated at individual training-MSE $10^{-3}$ endpoints. RMS uses 8192 circle queries, and the explicitly marked NTK output scale is 100 times wider than the other panels.”

Support: PDF labels; `paper/scripts/README.md:532`; `learning_controls_manifest.json` task `quadrant_alternating`. Same width-2048 two-hidden-layer tanh control protocol as entry 24.

### 26. `learning_controls_quadrant_center_edges.pdf`

Suggested caption: “Quadrant center-versus-edges task compares dense training, the full frozen initial NTK, two rank-24 factor seeds, and order-3 response memory at their own training-MSE $10^{-3}$ endpoints. RMS uses 8192 circle queries; the NTK panel alone uses a 200-times-wider output scale, with signed ticks in original units.”

Support: PDF labels; `paper/scripts/README.md:532`; `learning_controls_manifest.json` task `quadrant_center_edges`. Same initialization and architecture as entry 24; the control's large excursion is not a generalization-error measurement.

### 27. `learning_controls_quadrant_pairs.pdf`

Suggested caption: “Quadrant paired-label task compares dense training, the full frozen initial NTK, two rank-24 factor seeds, and order-3 response memory at individual training-MSE $10^{-3}$ endpoints. RMS discrepancies use 8192 circle queries, and the NTK panel's explicitly marked output scale is ten times wider.”

Support: PDF labels; `paper/scripts/README.md:532`; `learning_controls_manifest.json` task `quadrant_pairs`. Reuses the task in entries 22–23 with a different panel scaling and an added control column.

### 28. `learning_controls_two_outliers_alternating.pdf`

Suggested caption: “Alternating-label task with two outliers compares dense training, the full frozen initial NTK, two rank-24 factor seeds, and order-3 response memory at their own training-MSE $10^{-3}$ endpoints. RMS uses 8192 circle queries; the NTK output scale is explicitly widened tenfold.”

Support: PDF labels; `paper/scripts/README.md:532`; `learning_controls_manifest.json` task `two_outliers_alternating`. Same initialization and architecture as entry 24.

### 29. `learning_controls_gallery.pdf`

Suggested caption: “All five earlier circle tasks compare dense training, the full frozen initial NTK, two factor seeds, and order-3 response memory at individual training-MSE $10^{-3}$ endpoints. RMS discrepancies use 8192 queries, correction-rank bounds are 24 except for the quotient task's 12, and each widened NTK output scale is marked.”

Support: `paper/scripts/README.md:516`; `learning_controls_manifest.json:1`; PDF labels. Exactly the five task rows in entries 24–28 combined onto one page; entries 30–31 split the same content for readability. Using all three gallery forms repeats these observations.

### 30. `learning_controls_gallery_a.pdf`

Suggested caption: “Three quadrant tasks from the four-method endpoint comparison, with identical width-2048 two-hidden-layer tanh initialization and two trained-factor seeds. Each method reaches training MSE $10^{-3}$ at its own time; RMS uses 8192 queries and the NTK scale multipliers are stated separately for each row.”

Support: `paper/scripts/README.md:516`; PDF labels. Contains paired labels, alternating labels, and center/edges: entries 27, 25, 26. These are the first three rows of entry 29.

### 31. `learning_controls_gallery_b.pdf`

Suggested caption: “The outlier and equally spaced mixed-label tasks complete the four-method endpoint comparison, using the same width-2048 two-hidden-layer tanh protocol. RMS uses 8192 queries at individual training-MSE $10^{-3}$ endpoints; correction-rank bounds are 24 and 12, and the outlier NTK scale is explicitly widened tenfold.”

Support: `paper/scripts/README.md:516`; PDF labels. Contains entries 28 and 24, the last two rows of entry 29.

## Earlier MNIST comparisons

### 32. `mnist.pdf`

Suggested caption: “Earlier MNIST 3-versus-8 fitted-function comparison with 100 training images, 1984 held-out images, two tanh hidden layers, and width 4096. The order-3 agreement plot and signed differences for orders 1–3 use each model's own training-MSE $10^{-3}$ endpoint; RMS measures disagreement with dense predictions rather than label error.”

Support: matching printed RMS values and panel design; `paper/figures/experimental_figures.py:431`, `experimental_manifest.json:540`. Compact layout of entry 33. This is not the 32-training-image PCA digits task in `compression_checks.pdf`.

### 33. `mnist_residuals.pdf`

Suggested caption: “Earlier MNIST 3-versus-8 predictions at individual training-MSE $10^{-3}$ endpoints, using 100 training and 1984 held-out images with two tanh hidden layers of width 4096. Signed memory-minus-dense differences share one vertical scale; their RMS values measure function agreement, and order 2 is slightly closer than order 3 in this run.”

Support: `paper/figures/experimental_figures.py:431`, `experimental_manifest.json:540`, `experimental_gallery.pdf` page 6. Same endpoint data as entry 32 and the primary endpoint in entries 34–35.

### 34. `mnist_rms.pdf`

Suggested caption: “Earlier MNIST validation discrepancies from dense predictions across history orders and the displayed individual training-loss endpoints. Bars show observed refinement margins rather than confidence intervals, and open markers identify failures of the numerical gate.”

Support: PDF labels explicitly list training MSE 0.1, 0.03, 0.01, 0.003, and primary 0.001. `experimental_manifest.json:540` supports only the primary endpoint's numerical-margin convention. **Uncertainty:** the selected allowed manifests do not reproduce all values at the other loss thresholds, so do not invent their exact scores or count gate failures from the primary-only manifest.

### 35. `mnist_scatter.pdf`

Suggested caption: “Earlier MNIST 3-versus-8 held-out predictions compare dense training with history orders $q=1,2,3$ at the primary training-MSE $10^{-3}$ endpoints. The printed RMS values quantify fitted-function agreement with dense predictions, not classification accuracy or error against labels.”

Support: PDF labels; matching values in `experimental_manifest.json:540` and setup in `paper/figures/experimental_figures.py:431`. Three-scatter alternative to entries 32–33; does not add an independent replicate.

## Sphere endpoint and later Taylor-family plots

### 36. `sphere_comparison.pdf`

Suggested caption: “Dense output, order-3 response-memory output, and their signed difference on complementary sphere views for four ReLU hidden layers of width 2048 and 64 training inputs. RMS uses 8192 equal-area queries at each model's own training-RMS 0.01 endpoint; this single-seed float32 Euler illustration has no continuous-flow refinement certificate.”

Support: `paper/scripts/README.md:297`, `sphere_source_manifest.json:1`, `paper/plot_figures.py:136`. Surface colors interpolate the saved queries; black dots are training locations, not labels. ReLU is outside the analytic activation theorem. Same data as entry 37; its producer is documented as unavailable, so replotting is not independent reproduction.

### 37. `sphere_orders.pdf`

Suggested caption: “Dense fitted output and signed order-1, order-2, and order-3 response-memory errors for four ReLU hidden layers of width 2048 and 64 sphere training inputs. Both hemispheres and a shared error color scale are shown; RMS uses 8192 equal-area queries at individual training-RMS 0.01 endpoints in a single-seed Euler run with step $1/128$.”

Support: `paper/scripts/README.md:297`, `sphere_source_manifest.json:1`, `paper/plot_figures.py:94`. ReLU scope and absent refinement/producer qualifications are the same as entry 36; the order trend is specific to these endpoints.

### 38. `sphere3_time.pdf`

Suggested caption: “Saved three-dimensional sphere comparisons show query RMS from a width-4096 dense reference over recorded positive training times for Legendre, Harmonic, and the finite-panel family historically labelled ‘Logarithmic’ in this export and now called Taylor by its plotting script. The smaller-dense curve is a geometric mean over three seeds and the dense-pair curve a geometric mean over two pairs; the 30 test inputs follow eight training inputs in the saved arrays.”

Support: `paper/figures/plot_sphere3_time.py:1` (width and purpose), `:18` (split), `:34` (reference and aggregations), `:42` (current Taylor label), PDF labels, and `paper/scripts/README.md:28`. **Qualification:** no current output-hash manifest was found in the assigned adjacent files; script/PDF label discrepancy is preserved explicitly. Only saved-time empirical fidelity is supported; do not claim continuous-time, confidence, or theorem validation. The script's external input directories were not opened.

### 39. `sphere3_tradeoff_endpoint.pdf`

Suggested caption: “Saved sphere-3 endpoint RMS versus moving parameter count for Legendre, Harmonic, smaller dense controls, and the family labelled ‘Logarithmic’ in this export but called Taylor by the adjacent script. Smaller-dense summaries are medians and observed ranges over three seeds, while the dotted line is the recorded independent width-4096 dense-pair discrepancy; fixed storage and source-construction costs are additional.”

Support: `paper/figures/plot_sphere3_tradeoff.py:19`, `:35`, `:48`, `:54`; PDF labels. The x-data for compression are the `moving` field, not total state. Same historical-label/provenance qualification as entry 38; curves describe tested saved points, not asymptotic laws.

### 40. `sphere3_tradeoff_max_time.pdf`

Suggested caption: “Saved sphere-3 maximum-recorded-time query RMS versus moving parameter count for the same selected methods and controls as the endpoint tradeoff. ‘Logarithmic’ is the historical export label for the family called Taylor in the adjacent script; smaller-dense shading is the full observed three-seed range, and fixed storage and offline setup are not included on the horizontal axis.”

Support: `paper/figures/plot_sphere3_tradeoff.py:24`, `:35`, `:48`, `:54`; `paper/scripts/README.md:123`; PDF labels. “Worst time” in the artwork must be qualified as worst recorded time. This is a different observable from entry 39 using the same saved comparison family.

## Earlier Harmonic and seeded-decoder validation

### 41. `compression_validation.pdf`

Suggested caption: “Earlier Harmonic circle confirmation compares maximum-recorded-time unseen-query RMS and retained model-tensor scalars across widths 1024, 2048, and 4096, with three held-out seeds at each width. The dense-pair, payload-matched small-network, and frozen-kernel controls use the stated empirical protocol; lines are medians and shading is the observed seed range, with offline source setup and query workspace additional.”

Support: `paper/empirical_appendix.tex:21`, `:66`, `:88`, `:107`; `paper/figures/capture_trajectory.py:3952`. The empirical factor-three rule is not the theoretical fluctuation quantile or a continuous-time guarantee; RMS-one labels need not obey the small-label theorem.

### 42. `compression_logarithmic.pdf`

Suggested caption: “Earlier dimension-five seeded-decoder confirmation, labelled ‘Logarithmic’ in the artwork, compares finite-program query fidelity and persistent numerical payload across three dense widths. This is not the finite-panel Taylor construction: medians and observed seed ranges describe the recorded cases, the dotted storage curve includes the query-workspace envelope, and the flat retained payload is not an asymptotic scaling estimate.”

Support: `paper/empirical_appendix.tex:1`, `:35`, `:66`, `:123`; `paper/figures/capture_trajectory.py:4003`. Seed 201 appears at all widths and three seeds at width 4096; the decoder uses a fixed ten-panel Euler program rather than an integration-convergence study, and source setup costs remain additional.

### 43. `compression_checks.pdf`

Suggested caption: “Additional earlier Harmonic dimension and embedded-digits checks, followed by seeded-decoder dimension checks labelled ‘Logarithmic,’ retain the small-network and frozen-kernel controls and the decoder's circle failure. Dimension checks use one seed except the three-seed dimension-five decoder summary, the Harmonic digits panel uses three seeds, and displayed ranges and the empirical factor-three threshold are not confidence statements.”

Support: `paper/empirical_appendix.tex:88`, `:170`, `:199`; `paper/figures/capture_trajectory.py:4049`. Decoder annotations count persistent payload, excluding query workspace. The digits panel is the PCA-based 32-training-image Harmonic experiment (261 held-out images), distinct from the older MNIST100 figures and the separate eight-training-image decoder failure reported only in prose.

## Composite gallery

### 44. `experimental_gallery.pdf`

Suggested caption: “Seven-page gallery of earlier response-memory schematics and saved comparisons: mechanism, eight-checkpoint trajectory, factor controls, illustrative clock, paired projection, MNIST residuals, and deep-circle order sensitivity. Its pages preserve the individual protocols and qualifications of their corresponding standalone figures.”

Support: `paper/figures/experimental_figures.py:490` and `:519`, and all seven PDF pages. This file contains no additional experiment beyond entries 2, 18, 21, 5, 3, 33, 15, in that order. Unlike the individual exports, it retains descriptive headings and footer qualifications. A plain `\includegraphics` shows only page 1 unless a page is specified; including the complete gallery requires all seven pages. If all standalone figures are included, omitting this duplicate composite loses no distinct figure content.

## Editorial uncertainties that remain without expanding scope

1. `clocks.pdf`, `order_decay.pdf`, and the nonprimary endpoints in `mnist_rms.pdf` lack their exact producer or complete numerical records in the assigned source set. Caption only their visible content and recorded qualifications.
2. The three `sphere3_*` exports retain the old “Logarithmic” label, while adjacent current scripts name Taylor. The supplied scripts support the intended family distinction; they do not establish the exact original artifact generation hash or a theorem-compliant empirical implementation.
3. Several compact PDFs (`mechanism`, `clocks`, `moments`, `orders`, `same_rank`, `factors`, `mnist`) have alternative producer layouts elsewhere. The report identifies content correspondence, not identical render hashes. Missing saved-data bundles mentioned by documentation were not fetched or reconstructed.
4. Historical empirical headings, placement recommendations, and figure numbers in `paper/scripts/README.md` refer to earlier editions, as that guide explicitly warns at line 61. They are not instructions to replace the compact paper's current theory or claim that these plots were run under its hypotheses.
5. The current compact abstract says it makes no empirical claim. An end-of-paper figure collection should explicitly introduce these as existing illustrations under their recorded protocols, separated from the headline theorem, rather than asserting that every plot validates the present Legendre/Harmonic/Taylor guarantees.
