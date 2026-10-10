# Promotion selection: response compression and fixed-order learning

Date: 2026-10-10. Selector: Codex subagent `/root/promotion_screen`.
Baseline HEAD: `1dba30ab2b1f728247b9b93b93a4df9f772886c4`.
Role: independent relevance and placement selector; I did not author or
assemble these results. This is Gate 1, **acceptance for candidate assembly**,
not scientific acceptance or permission to change established files.

## Decision and book placement

The candidate contains one substantial new approximation message and several
distinct learning results. Accept the scoped components below for assembly.
Use one new Part II chapter and additions to existing Part III chapters.
Do not add a new Part or a separate historical-results chapter.

| Component | Decision, distinct value, and exact scope | Smallest destination |
|---|---|---|
| Complete compact theorem and its four proof files | **Accept.** Quantitative prediction compression of a coupled finite dense network over the complete trajectory, including its fitted limit. Legendre retains history moments and fixed dense mixers; Harmonic and Taylor retain selected coordinates, exact source metrics and a corrected optimizer. This adds all-time prediction comparison and explicit coordinate counts to the book's qualitative current-observable closure and iterated numerical convergence. | New Part II chapter, immediately after `08-autonomous-computation.qmd`, titled **Complete-trajectory compression**, with stable `ch-complete-trajectory-compression` identifier. A filename such as `08a-complete-trajectory-compression.qmd` avoids renaming existing paths. |
| Architectural floor and absence of suboptimal local minima | **Merge.** The signed-input grouping floor and exact population landscape theorem explain expressivity separately from dynamics. Keep order one on the stated odd sphere sector in dimension at least two; keep full order-two/order-three circle spaces, including their constant coordinates. Preserve arbitrary real labels, physical product topology and small-population-set variations. | Part III, `09-trainability.qmd`, new coherent section **Landscape and architectural loss floors of fixed-order closures**. |
| Lower-layer trainability with rank-one upper features | **Merge.** The constructed three-input state shows why a singular readout Gram does not imply singular full prediction differential. Keep the bounded-displacement odd class and explicit construction; do not assert initialized reachability or a uniform singular-value bound. | Same Chapter 9 section, after the landscape/Gram distinction; refer to the Chapter 7 fixed-order model. |
| Protected reflected/antipodal pairs and arbitrary-pair small labels | **Merge.** Global fitting, finite length, state convergence and strict terminal contrast gain for exact canonical symmetries; a separate local-basin result treats arbitrary orientations with sufficiently small labels. Existing Chapter 10 treats different dense/population activation families and does not subsume these fixed-order tanh results. | Part III, `10-correlated-pairs.qmd`, section **Protected geometry in the first-order tanh closure**. Share the scalar-clock proof with the triple and plateau applications. |
| Uniform canonical cyclic triples | **Merge.** A positive uniform rate over every canonical coordinate-cyclic three-input orbit, including compatible collapsed and planar endpoints, supplies a fixed-order nonlinear fitting family distinct from Chapter 12's specially designed activation/depth results. Retain equal weights, the coordinate action and permitted simultaneous input/label sign flips. | Part III, `12-three-sample-learning.qmd`, section **Cyclic triples in the first-order tanh closure**. |
| Initialized positive plateau at the architectural floor | **Merge.** This is an actual initialized trajectory with persistent hidden motion, convergence and terminal asymptotics; it reaches an unavoidable odd-predictor floor. It is distinct from Chapter 9's smooth plateau-activation confinement results. Do not call it failed optimization on realizable data. | Chapter 9, following the floor/landscape material, with a cross-reference from Chapter 12. |
| Initialized feature independence and free passive values | **Merge.** For the exact first-order circle closure, finite nonantipodal feature families are independent and fitting readouts can assign an arbitrary additional query value. This cleanly separates interpolation freedom from flow-selected prediction. Chapter 13 already has related feature-independence arguments for a different trained population state; reuse the explanatory connection, not its model assumptions. | Part III, `13-predictor-selection.qmd`, an opening section **Fitting does not determine the passive predictor**. |

The compact theorem's restrictions belong beside its headline: fixed data,
input dimension and depth; strip-holomorphic activations with the stated
derivative bounds; a positive initialized population feature-Gram gap; the
explicit very small label condition; and **exactly zero finite readout**.
The book's small random finite readout is a different initialization.
Preserve whole-sphere queries for Legendre/Harmonic and the panel declared
before initialization for Taylor. The denominator is whole-trajectory
variability between independent dense runs, witnessed at transient times;
this is not an endpoint fluctuation theorem. Coordinate counts do not imply
bit complexity or practical preprocessing. These restrictions make the result
useful and nonvacuous without replacing the book's broader dense-GD objective.

Use the new chapter for the complete compact proof chain, including fitting,
analytic sources, moment projection, selection and the variability argument.
Splitting these dependencies across Parts I–III would increase maintenance
and obscure the common hypotheses. Cross-reference established conventions,
but retain locally complete model definitions and proof hypotheses.

## Duplication, proportion and maintenance

Chapter 7 already defines initialized observable dictionaries, actual paired
matrix actions, finite autonomous closures and general-dimensional first-order
coefficients. Chapter 8 already contains polynomial dictionary construction,
numerical realizations and convergence with separate initializer/population
quadratures. Merge the older candidate's common model and canonical constants
into references to those precise sections; do not publish a second dictionary
definition with historical notation. Add only genuinely necessary missing
lemmas or an explicit convenient equivalent coordinate representation there.

The older learning results do **not** establish general initialized convergence
from absence of bad minima, arbitrary-orientation unit-label pair fitting,
all-time dense-network fidelity of fixed-order closures, or generalization.
No Chapter 14 theorem addition is selected. The compact prediction norm is
also not a population test-risk guarantee.

Maintenance cost is substantial for the compact analytic proof and moderate
for the older package: several invariant sectors, two initialization
conventions and a shared scalar-clock argument must remain visibly distinct.
Keep a short model/scope comparison and one common proof for each reused
lemma. Introduce native Quarto statement/equation identifiers and complete
proofs; historical filenames, source-line references and prior verdicts are
provenance only. Update the reading guide/navigation and affected chapter
introductions proportionately; do not duplicate the whole assembled narrative.

## Reusable implementation selection

| Component | Decision and overlap control | Destination |
|---|---|---|
| `compression_core.py` | **Accept, with a narrow numerical contract.** Direct Legendre moments and shared corrected Selected dynamics are new. Dense duplicates some maintained finite algebra but adds arbitrary-depth optional Torch execution, six activations and zero-readout coupling; keep it as this module's explicit reference and use maintained finite equations as an independent validation oracle. Do not replace the existing NumPy or weighted two-layer engines. | `code/pde/compression.py`; an opt-in Torch module, accompanying guide, `code/tests/test_compression.py`. |
| Harmonic rollout sources and Taylor rollout/origin jets | **Accept as numerical source builders; decline theorem-certified-runtime branding.** Dense-rollout setup and order-two origin jets do not implement the theorem's initialization-only analytic continuation/compiler. Harmonic runtime supports dimensions two and three; Taylor guarantees no undeclared-query accuracy. No practical source-error or asymptotic-storage certificate is selected. | Same module and guide, clearly named source modes and limitations. |
| `dictionary_core.py` | **Accept as an adapter.** Finite initialized carriers, matched Gaussian/orthogonal controls, orders one through nine and diagnostics add a useful comparison API. Reuse `observable_initialization.build_dictionary` and `observable_torch_p1.ClosureEngine`; do not copy their solvers. The general-dimensional first-order convenience wrapper adds no new mathematics. | `code/pde/observable_dictionaries.py`; reuse `GENERAL_P1.md` for shared engine semantics and add a short dictionary guide/tests. |
| Endpoint/error helpers | **Narrow/merge.** Keep threshold stopping and chord interpolation, including failure status, as explicitly finite numerical comparison tools. Existing `closure_comparison` already provides prediction metrics and saved-loss matching; avoid presenting these different stopping rules as interchangeable or duplicating generic metrics without reason. | Dictionary adapter for engine-dependent stopping; reuse or cross-reference `code/pde/closure_comparison.py` for common comparison contracts. |
| `data_core.py` | **Accept.** Small deterministic toy tasks and an optional official-split binary-MNIST loader fill a maintained-input gap. Preserve normalized rows, train-only label scaling, split-qualified IDs, explicit cache root/download option and provenance. Optional TorchVision loads only on request. | `code/pde/compression_data.py`, guide and deterministic fixture tests. |
| `visual_core.py` | **Accept.** Array-only circle/sphere plots and simple offline viewers are reusable and absent from the current maintained API. Keep sampled discrepancies distinct from continuum errors. NumPy remains the core dependency; Matplotlib is needed only for static plots. | `code/pde/prediction_views.py`, guide/tests. |
| `radial_explorer.py` and `.html` | **Accept together.** Multi-experiment circle views, width/seed controls and time/loss/recorded-endpoint alignment serve a different purpose from the simple sphere/array viewer. Preserve bundled D3 attribution and local operation. Alignment/interpolation must retain its documented numerical meaning. | `code/pde/radial_explorer.py` with its adjacent template, documented resource packaging, and integration tests. |
| `support_example.py`, `radial_example.py` | **Accept as bounded operational recipes.** These make all interfaces concrete; neither is a learning or approximation experiment. Remove study-path imports and output defaults. | `code/scripts/example_compression.py` and `code/scripts/example_radial_explorer.py`, with explicit fresh output directories. |
| Historical dictionary rankings, scaling and timing conclusions | **Hold.** Reports and directory existence are not a fresh producer-level reproduction. Retain adverse as well as favorable evidence in the study; no historical numerical table or ranking enters the maintained edition in this package. | No established destination until separately complete maintained inputs/producer/analysis and fresh reproduction are supplied. |

Code maintenance cost is moderate: optional Torch/TorchVision/Matplotlib,
multiple numerical initializers and two browser interfaces must be tested
without turning ordinary `import pde` into a heavy dependency import. Keep
data generation, training, plotting and campaign scheduling separate. The
existing API's physical-column inputs and these normalized-row inputs require
an explicit conversion in guides; equal seeds across different initializers
must not imply a shared random realization.

## Inputs, limitations and next gate

Actual reading comprised the project instructions and full workflow; promotion
and canonical-notation skills (including neural conventions); full current
book index/notation and Quarto navigation; book heading/keyword inventories;
targeted model/theorem passages in Chapters 7, 8 and 13, with scope snippets
and heading inventories for Chapters 9, 10, 12 and 14;
the maintained API guide and general-first-order guide; API/source inventories
and relevant finite-engine interfaces. Candidate reading comprised the compact
setup/headline/proof architecture and proof-label inventory, `RESULT.md`, the
selected mathematical statements in `older_theory.md`, complete component
guides, source interfaces/imports, and the older archive's member listing.
I did not read every compact proof line, extract every older proof, inspect
every implementation body, run tests, or reproduce empirical conclusions.
Unread proof/code bodies are explicitly deferred to the two complete reviews.

**Exposure disclosure:** the first read of permitted `older_theory.md`
accidentally displayed its embedded historical-verdict table. I reported this
immediately. The coordinator instructed continuation because Gate 1 requires
an independent selector, not blinded scientific review. Those verdicts played
no role in these decisions. I did not read original review reports, the study
README, `old_docs/`, paper sources, chats, or other studies. The archive member
names were inspected as metadata only. The coordinator later communicated
its expected placement; the comparisons and rationale above were independently
made from maintained coverage and candidate statements.

No missing source is needed to decide relevance and placement. Complete proof
dependency closure, code correctness, theorem-to-implementation boundaries,
browser behavior and standalone packaging remain unverified. In particular,
the archive contains historical reviews alongside scientific sources: construct
the next packet from explicit mathematical members and current dependencies,
excluding verdicts. Freeze the actual Quarto/module candidate with hashes;
obtain both complete adversarial reviews and edition/integration checks.
User approval applies only to the resulting concrete reviewed addition.
