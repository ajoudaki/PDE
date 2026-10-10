# Retained responses, trainability, and compression

## What this study contains

One assembled candidate for later promotion, centered on the current compact
paper. The user explicitly authorized combining that paper, its core
implementation, the established book, and the previously selected older
studies on 2026-10-10. This supersedes this folder’s earlier coordination-only
scope. The older findings are retained where they add a distinct result or
mechanism, with their different model assumptions stated explicitly.

Start with [RESULT.md](RESULT.md): it gives the common scientific question,
exact compact-paper scope, the older results’ roles, and proposed book homes.
It does not replace the complete proofs.

| Material | Entry point |
|---|---|
| Compact paper, including its complete four proof components | [compact.tex](compact.tex) and its local `compact_*.tex` inputs |
| Earlier landscape, initialized-feature geometry, trainability, protected-flow fitting, and reached plateau | [older_theory.md](older_theory.md); complete selected proof sources in `older_theory_sources.tar.gz` |
| Dense reference, Legendre moments, and the common Harmonic/Taylor selected-coordinate evolution | [CODE.md](CODE.md), [compression_core.py](compression_core.py) |
| Earlier observable, Gaussian, and orthogonal dictionaries; bounded closure evolution and endpoint comparison | [DICTIONARIES.md](DICTIONARIES.md), [dictionary_core.py](dictionary_core.py) |
| Reproducible toy tasks and official-split binary MNIST preparation | [DATA.md](DATA.md), [data_core.py](data_core.py) |
| Reusable radial/spherical figures and offline interactive prediction comparison | [VISUALS.md](VISUALS.md), [visual_core.py](visual_core.py) |
| Original multi-experiment radial HTML interface: local data loading, width/seed selection, time/loss alignment and playback | [RADIAL.md](RADIAL.md), [radial_explorer.py](radial_explorer.py), [radial_explorer.html](radial_explorer.html) |
| Small end-to-end example using the assembled data, methods, and viewers | [support_example.py](support_example.py) |
| Exact source identity and historical provenance | `sources.json`, `older_sources.json`, `core_sources.json`, `dictionary_sources.json` |

The two numerical modules form one study-owned implementation collection.
They share normalized input rows, float64 arithmetic, the unhalved square
loss, and explicit matrix reuse. Their distinct states remain explicit; a
wrapper that hides those differences is unnecessary. They import neither the
large paper experiment driver nor historical study archives at runtime.
Maintained `code/` supplies the existing closure engine, dictionary words, and
general-dimensional first-order population initialization. The latter also
makes the weighted sphere-triple model executable with its own initialization
and probability weights.

## Scope and source boundary

The main theorem is exactly the five frozen local compact-paper files. They
were copied byte-for-byte from `paper/`, with hashes recorded before further
concurrent manuscript changes. No longer-manuscript theory or experiment
campaign is included by implication. The paper’s originating provenance is
`studies/compact_paper_20261009/`; its version-specific historical reviews do
not automatically approve this assembled candidate.

The selected older sources are:

- `fixed_p_population_landscape_20260919`: strongest circle landscape result;
- `p1_stochastic_escape_20260918`: complementary order-one sphere landscape;
- `fixed_p_predictor_uniqueness_20260919`: necessary canonical-feature result,
  without the deferred noisy optimizers or projected selector;
- `p1_three_input_geometry_20260918`: lower-layer trainability despite upper
  feature collapse;
- `closure_lyapunov_p1_20260916`: reflected/antipodal and small-label pair fitting;
- `p1_sphere_extremes_20260918`: cyclic triples and initialized architectural
  plateau;
- `random_dictionary_learned_circle_20260920`: matched dictionary controls and
  qualified historical evidence, including unfavorable comparisons.

Their selected complete proof chains, corrections, and historical checking
status are identified in the older-theory manifest and archive. The dictionary
manifest identifies code and evidence sources; its guide distinguishes
reported campaign findings from the small implementation checks run here.
These sources are authorized inputs for this assembly only. Other studies
must not acquire its unpromoted findings as established dependencies.

This is the narrower previously selected priority set. Weighted slow-onset,
C-X extensions, modified noisy optimizers, projected predictor selection, and
attention are not silently added. No new research campaign was run.

The user subsequently authorized a small supporting layer: reusable task-data
generation, binary-MNIST preparation, radial/spherical plotting, and selected
interactive examples. These extract or adapt the paper implementation's
reusable behavior. They do not import the paper driver, its bundled datasets,
or one-off campaign/figure scripts at runtime. Source provenance is recorded
in the two supporting guides and `sources.json`. No dataset download is made
implicitly, and no historical experimental conclusion is promoted by adding
these utilities.

## Implementation scope and the remaining gap

All three compact-paper evolution methods have executable numerical cores.
Dense and Legendre support arbitrary fixed hidden depth with the documented
smooth activation implementations. Harmonic and Taylor share the same exact
source-metric and corrected-readout evolution; their source construction and
coordinate selection choices are recorded explicitly.

The practical Harmonic source builder and optional empirical Taylor builder
use a finite dense rollout. The Taylor origin-jet option uses initialization
only, through order two. **Neither is the theorem’s arbitrary-accuracy,
globally certified initialization-only source compiler.** That compiler remains
an implementation gap; it is not replaced by a claim that a practical setup
inherits the theorem. Numerical source rank, time step, and conditioning are
likewise not finite-run error certificates. See CODE.md for supported contracts.

The older population theorems remain exact Gaussian-law statements. Their
finite-carrier implementation and finite-step endpoints are numerical
approximations, not proofs of those theorems or a transfer to dense-network
all-time limits. Historical dictionary comparisons are not rerun or upgraded.

## Validation and reproduction

From the repository root, use the installed Torch Python (here
`/home/amir/miniconda3/bin/python`), or another environment with NumPy and Torch:

```bash
python studies/book_promotion_20261010/check_sources.py
PYTHONPATH=code:studies/book_promotion_20261010 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 /home/amir/miniconda3/bin/python -m unittest discover -s studies/book_promotion_20261010 -p 'test_*_core.py' -v
```

The checks exercise actual differential equations and their normalizations,
projection and source-metric identities, nonzero-residual dynamics, and the
dictionary/replay contracts. They use small synthetic CPU fixtures, not saved
campaign outputs. The completed run is recorded under
`data/generated/book_promotion_20261010/validation/`.

The combined run passed **23 tests** (15 compression and 8 dictionary/closure
checks; 1.332 seconds of test execution). Separate one-step smoke checks of
the maintained native population solver passed at orders two and three.
Frozen-source, archive-membership, and compact-reference checks also passed.

To exercise the supporting layer with all three compression methods and the
dense reference, run the bounded example below. It uses width 64, four toy
training inputs, 96 queries, and short RK4 trajectories through time 0.04 for
each circle/sphere example. It produces prediction arrays, PNG/PDF views, offline HTML viewers,
and a manifest containing settings, source hashes, and output hashes. The
output directory must be new. This checks interoperability, not fitting or a
scientific approximation claim.

```bash
PYTHONPATH=code:studies/book_promotion_20261010 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MPLCONFIGDIR=data/generated/book_promotion_20261010/mplconfig /home/amir/miniconda3/bin/python -B studies/book_promotion_20261010/support_example.py --out data/generated/book_promotion_20261010/my_support_example
```

The `test_*_core.py` command also discovers the dataset and visualization
checks. Those include synthetic MNIST fixtures and execution of the embedded
viewer JavaScript with Node; Node is needed for the interaction check.
Matplotlib is needed for static views, while TorchVision is optional and used
only by the explicit MNIST loader. The HTML viewers require no online assets.

The compact snapshot has 136 unique labels and 141 non-comment reference uses, with no
unresolved local reference or missing included proof file. Source archives
and manifests preserve the exact inputs; generated scratch belongs only under
`data/generated/book_promotion_20261010/`.

The expanded combined suite passed **41 tests** (15 compression, 8
dictionary/closure, 11 data, and 7 visualization checks; 1.663 seconds of test
execution). The actual viewer JavaScript ran under Node for both geometries.
Toy and synthetic MNIST arrays matched the extracted paper producers
bit-for-bit. No real MNIST download or real-data training was performed.
Both end-to-end examples ran successfully and their PNGs were inspected;
sphere colorbar labels received a reusable compact-tick/alignment fix and
were rechecked from the saved arrays, without rerunning training.

Evidence and examples:

- [Combined validation](../../data/generated/book_promotion_20261010/support_validation01/validation.json)
- [Final surgical visualization recheck](../../data/generated/book_promotion_20261010/support_visual_final01/validation.json)
- [Data parity against the paper producer](../../data/generated/book_promotion_20261010/data_support/source_parity.json)
- [Example settings and provenance](../../data/generated/book_promotion_20261010/support_example01/manifest.json)
- [Offline circle viewer](../../data/generated/book_promotion_20261010/support_example01/circle.html)
- [Offline sphere viewer](../../data/generated/book_promotion_20261010/support_example01/sphere.html)
- [Rechecked sphere figure](../../data/generated/book_promotion_20261010/support_visual_final01/sphere.png)

The user's clarification of “radial” adds the original multi-experiment HTML
explorer, adapted to supplied JSON bundles with its campaign payload removed.
It retains time/loss/endpoint alignment, width/seed choices, playback and hover.
Ten additional checks cover its data adapter and actual JavaScript controls.
A two-experiment example connects it to the assembled numerical cores:

- [Multi-experiment radial explorer](../../data/generated/book_promotion_20261010/radial_example01/explorer.html)
- [Empty explorer for loading experiment JSON](../../data/generated/book_promotion_20261010/radial_example01/empty_explorer.html)
- [Radial validation](../../data/generated/book_promotion_20261010/radial_validation01/validation.json)

Use `-p 'test_*.py'` in the test command to include these checks. See RADIAL.md
for the source contract, reproduction command and browser-testing limitation.

## Status and next step

**Promoted and verified.** The
exact reviewed v5 edition is now in `docs/` and `code/`. The promotion record
below retains its selection, independent reviews, approval and correspondence.

The promotion proposal below uses this single collection, with natural book
placements: quantitative compression in Part II and the older finite-closure
learning geometry in Part III. Follow `RESEARCH_WORKFLOW.md` Part 2 for
independent selection, complete fresh scientific reviews, Quarto/code
integration review, and approval of the concrete addition. Existing reviews
should inform provenance without being passed to fresh isolated reviewers.
The resulting book material must use `docs/notation.qmd`, proper Quarto
mathematical environments, and stable references. Assembly itself did not
authorize live integration.

Owner: the book-refactor/promotion task
`01a0bfab-7ccd-7ee3-94e4-11a3ef88fd90`. Shared working-tree changes outside this
study belong to their current tasks and were preserved.

## Promotion attempt (2026-10-10)

The user initially authorized passing the promotion gates for this assembled
study. The review history below records preparation before live integration;
the approval and application record follows it.
Independent selector `/root/promotion_screen` screens the exact scope and
placement. `/root/draft_compression_chapter` drafts the full compact proof in
Quarto; `/root/draft_older_chapters` drafts the selected older additions. The
coordinator owns packaging, the current record, frozen packets and validation.
The starting maintained inputs are retained in `promotion_base.tar.gz`, with
per-file identity in `promotion_base.json`; these are document/library inputs,
not a checkout or a worktree. Unrelated working-tree changes are preserved.

Independent relevance/placement screening completed in
[promotion_selection.md](promotion_selection.md). The complete candidate adds
one Part II chapter, `docs/08b-trajectory-compression.qmd`, and integrates the
selected older results into the existing trainability, correlated-pair,
three-sample and predictor-selection chapters. Stable filenames/identifiers are
preserved; visible chapter ordinals advance after the insertion.

The code overlay contains optional `pde.compression`,
`pde.observable_dictionaries`, `pde.compression_data`, `pde.prediction_views`,
and `pde.radial_explorer` with its original interactive HTML interface,
six test modules, two bounded examples and five guides. Ordinary `import pde`
stays NumPy-only. Historical dictionary rankings remain study evidence and
are excluded from new empirical claims. Practical numerical source builders
are explicitly distinguished from the theorem's certified global compiler.

The complete first reviews are retained unchanged:
[review A v1](promotion_scientific_a_v1.md) and
[review B v1](promotion_scientific_b_v1.md). Both required correction. They
identified a misnamed Taylor-series coefficient; B also found that Cholesky
success could accept a singular training Gram. These are corrected, with
scale-relative rank/identity checks and regression cases. Candidate section
links now name their targets because the edition has unnumbered sections.
The original packet remains immutable.

The corrected candidate is frozen in `promotion_packet_v2.tar.gz`, with exact
inputs in [promotion_review_inputs_v2.json](promotion_review_inputs_v2.json).
Its standalone edition is
`data/generated/book_promotion_20261010/promotion_edition_v5/`.
Fresh complete scientific reviews both PASS this exact packet:
[review A v2](promotion_scientific_a_v2.md) and
[review B v2](promotion_scientific_b_v2.md). Both verified all 114 input hashes,
completed their full assigned reading, passed all 54 proposed tests, and ran
independent boundary checks plus both tiny examples. The coordinator read both
reports completely and checked their provenance. B discloses an initial
temporary-directory setting deviation; no manifest input changed, and the
checks were repeated with the required scratch settings.

The initial complete candidate rendered to HTML, PDF and editable LaTeX.
[Integration review v2](promotion_integration_v2.md) passed source placement,
notation, preservation and runtime checks but required two HTML delivery fixes:
global LaTeX preamble text leaked into HTML, and six exported links to code
files lacked packaged resources. Its original report and packet are retained.

The subsequent candidate is frozen in `promotion_packet_v3.tar.gz`, with exact files
in [promotion_review_inputs_v3.json](promotion_review_inputs_v3.json), assembled
under `data/generated/book_promotion_20261010/promotion_edition_v7/`.
Relative to the scientifically reviewed v2, only `docs/_quarto.yml` changes,
and `docs/package_code_links.py` is added. Every mathematical passage,
numerical module, test and guide is byte-identical, so the scientific PASSes
retain their complete scientific scope. The complete new presentation helper
and configuration are in the fresh integration review scope. It scopes TeX
headers to PDF/LaTeX and packages linked code resources into HTML output.

[Integration review v3](promotion_integration_v3.md) passed the complete source,
runtime, HTML and sampled print-layout checks, but found that the six code
resources also needed packaging for PDF and editable LaTeX. That report and
packet remain unchanged. A print-only link filter now places those URLs inside
each export directory, and the shared packaging helper copies the referenced
source files beside each print artifact.

[Integration review v4](promotion_integration_v4.md) verified all direct export
links, but following links inside the copied guides exposed missing component
guides and book-source backlinks. The helper now packages the source `docs/`
and `code/` trees together, preserving their relative layout and excluding
render outputs/caches. This covers supporting navigation without a growing
list of special cases. The previous report and packet remain unchanged.

The current candidate is `promotion_packet_v5.tar.gz`, with exact files in
[promotion_review_inputs_v5.json](promotion_review_inputs_v5.json), assembled
under `data/generated/book_promotion_20261010/promotion_edition_v9/`.
Relative to scientific v2, only Quarto configuration changes and two presentation
helpers are added; every mathematical addition, numerical module, test and
guide remains byte-identical. The scientific PASSes therefore retain their
complete scope. Renders/evidence are under
`data/generated/book_promotion_20261010/promotion_render_v9/`. The fresh complete
[integration review v5](promotion_integration_v5.md) **PASSes**, with no required
correction. It verifies all 105 assembled inputs, all 54 tests, both examples,
full HTML/PDF/editable-LaTeX builds, native references and the 26 local links
within the bundled Markdown guides. All 103 book/code source resources in each
export bundle match the frozen sources byte for byte. The coordinator read the
complete report and verified packet/source identity; all 83 live baseline files
remain unchanged. Earlier adverse reports are retained above.

**Technical promotion gates passed; user approved the exact v5 package.**
The approved packet is v5, SHA256
`a8882cd38656089f9a29aa7c23f7f119d0ea809ca5ff289fcbb6102e863be15a`.
The user explicitly confirmed, “I approve the promotion.” After rechecking all
83 baseline inputs and preserving concurrent paper/study changes, the coordinator
applied exactly the 33 changed/new maintained paths. All 103 resulting book/code
files match the approved packet. [promotion_applied.json](promotion_applied.json)
records the approval, before/after hashes and candidate-to-live mapping.
Final live-path checks PASS: all 103 files match, all 54 tests pass without skips,
both examples succeed, and the source/reference validator reports no errors.
[Live-check evidence](../../data/generated/book_promotion_20261010/live_promotion_check/check_results.json).
The promotion commit is `e184cd790c8c9f751aed153bb55584c2e3fc62e6`; it is also recorded in the application receipt. The unchanged
edition's complete render and independent review evidence above remains valid;
no scientific source was modified during application.

The main compression result retains fixed data/depth/activation, a positive
initialized population feature Gram gap, an explicit small-label condition,
zero initial readout, and its stated width/probability/exact-arithmetic scope.
The practical source builders are not the theorem's certified global compiler.
Historical dictionary rankings are excluded from promoted empirical claims;
there was no new data campaign or real-MNIST download/run. Browser controls were
executed through the Node-backed tests; full graphical-browser interaction and
page-by-page PDF inspection were outside the bounded integration checks.

Nonblocking follow-up from review A: explain the radial viewer's dash for a
relative query RMS with a near-zero reference norm. The dash is not a false
error measurement; this presentation refinement is deferred and is not an
unreviewed edit to the accepted scientific packet.
Integration reviewers also record a nonblocking PDF line break inside one
function application in equation (2047). The source formula is intact; this
layout refinement is deferred without changing the reviewed sources.
