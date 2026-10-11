# Compressing Global Dynamics of Deep Nonlinear Feature Learning

The current modular manuscript is [main.tex](main.tex), compiled to
[main.pdf](main.pdf). These are the renamed compact manuscript, now the sole
active edition. The obsolete long manuscript and its exclusive TeX modules
have been removed; they remain recoverable from Git history (commit `3233888`).
The unified response-compression framework presents
Legendre history compression, and a shared selected-coordinate runtime
with Harmonic (whole-sphere) and Taylor (declared finite-panel) source
builders. The approved 2026-10-11 update transfers the reviewed Chapter 9
polynomial-width and efficient-initialization results into the compact paper.
The main theorem incorporates polynomial sufficient widths for Legendre and
Taylor. The nonlinear feature-learning theorem follows it directly, then the
initialization proposition gives both supplied-dense and fresh-implicit-Gaussian
setup costs for Harmonic and Taylor. Storage, error,
label, activation, optimizer and query-domain qualifications are preserved.

The current reading order is **Introduction → Setup and main results → Related
work and discussion → proofs → references → figures**. The new framing adapts
the older manuscript's motivation and literature discussion to the current
width/setup results. It introduces no additional global notation and leaves
the theorem statements and all proof modules unchanged. The proof roadmap
closes the discussion before the technical sections begin.

The subsequent proof-only refactor reduces the compiled compact paper from
94 to 89 pages, reusing established in-paper arguments and shared finite cost
formulas. Its headline theorem and initialization proposition are unchanged,
as are the older proof modules and global notation. Two fresh mathematical
audits and a separate final integration audit passed; the
[shortening record](../studies/headline_threefold_upgrade_20261011/README.md)
contains the exact scope, preservation checks and review reports.
The later figure-only addition leaves that proof content unchanged and appends
24 pages of existing static illustrations (113 pages at that stage). The symbol
table now omits the count column while retaining every symbol and definition.
The introduction/discussion update adds two pages, for 115 pages in total.

## Reading and source structure

- `main.tex`: introduction, setup and main results, related work and
  discussion, followed by the modular proofs. Its final proof section,
  `compact_nth.tex`, gives the matching frozen-top NTH literal-storage theorem
  and complete proof from the established book's Chapter 7. This separate
  benchmark uses two identity hidden layers, 4 ≤ m ≤ √n samples (fixed m
  already gives size n^Θ(log m)), fixed label magnitude and a short time
  interval; it is not a same-family
  separation from the compression theorem. It keeps the initialized frozen
  top and the hierarchy's own residual. The half-MSE clock is explicitly
  related to the manuscript's full-MSE clock. This addition is unchanged by
  the width/setup update and entry-point rename.
- `compact_figures.tex`: the final, separately captioned collection of all
  44 top-level static figure assets, including all seven pages of
  `experimental_gallery.pdf` (50 included panels). PDF is used once per stem;
  PNG/SVG format copies and interactive-explainer thumbnails are omitted.
  Alternate assemblies are retained and identified as such. Historical RMS,
  endpoint, control, and method-name distinctions are stated in the captions;
  these earlier illustrations are not new experiments or theorem certificates.
- `compact_width.tex`: complete quantitative source, actual dense lower,
  third-order Legendre approximation and polynomial-onset proofs.
- `compact_initialization.tex`: complete supplied-dense and implicit-Gaussian
  setup proofs, including finite-order time and peak-memory ledgers.
- `compact_fitting.tex`, `compact_foundations.tex`, `compact_legendre.tex`,
  `compact_selected.tex`: shared fitting and analytic estimates, Legendre
  compression, and the Harmonic/Taylor selected-coordinate constructions.
- `feature_learning_theorem.tex`: the additional nonlinear feature-learning
  theorem. `compact_feature_learning.tex` gives its self-contained shortened
  proof. Its extra assumptions
  (nonaffine activations and no parallel or antiparallel training inputs)
  do not narrow the compression theorem. Taylor may append four predeclared
  passive witness inputs. Constants in this additional theorem depend on
  the whole fixed problem, not just activation and depth.
- `references.bib`: literature bibliography.

Retained-state constants depend only on activation and fixed depth; the
initialization proposition separately states its fixed-parameter computational
constant convention. All three
headline constructions have compression error divided by actual independent
dense-run discrepancy tending to zero in probability, on the same promised
query domain and over the entire training trajectory including its endpoint.
Harmonic and Taylor additionally attain absolute error `Y/n` at every
fixed confidence for sufficiently large width, with the displayed storage
orders unchanged. The older quantile/factor-three comparison belongs only
to the separate supplementary seeded decoder and historical experiments.
Structural parameters remain distinct. The detailed proofs retain label factors,
arbitrary confidence, full label allowance, width gates and internal setup orders.
The setup defines the persistent notation before the theorem statements.

The following distinctions are intentional:

- Legendre compresses the moving state but retains its fixed dense mixers.
- Harmonic tracks a coupled dense reference. Its explicit and implicit
  initializers have different setup costs; the latter samples a fresh latent
  reference rather than reading a supplied dense matrix cheaply.
- Taylor denotes the finite-panel, cubic-logarithmic real-coordinate
  construction. Its passive inputs, but not their labels, are available at
  setup. It tracks a coupled dense reference with the same selected nonlinear
  runtime as Harmonic. The initialization-jet compiler remains an alternative
  without an efficient work bound; the numerical initializers now have both
  near-linear and near-quadratic bounds. They compute across the required
  finite horizon, not just a short physical-time prefix. Arithmetic is exact
  real, with supplied activation envelopes and population-gap certificates;
  no finite-bit or empirical-speedup claim is made.
- The older independent-reference finite-word construction is called the
  **seeded decoder** in the historical figure captions. Its words and bits must not be
  confused with the new Taylor model's real-coordinate count.
- The dense lower bound is transient, not an endpoint result. Legendre and
  Taylor now have polynomial sufficient widths; Harmonic retains its eventual
  qualification. The sharper original dense-lower coefficient and the separate
  nonlinear-feature-learning certificates are not assigned polynomial onset.
  In the preceding long manuscript, the seeded decoder's additive and
  analytic absolute certificates have an explicit conservative gate; its purely
  multiplicative intrinsic comparison also uses the lower bound's eventual onset.

## Historical versions

Commit `3233888` contains the obsolete long manuscript under its former
`paper/main.tex` and `paper/main.pdf` names, along with its exclusive modules.
The present `main.tex` is the former `compact.tex`, unchanged by the rename.
Historical study records, generated build snapshots and frozen inputs under
`reviews/` are retained as provenance, not alternative active manuscripts.
Do not rerun historical transfer scripts over the current sources.
LaTeX reads no study files: all mathematical dependencies are statements and
proofs inside the manuscript.

## Plot the figure inventory

Run `python paper/plot_figures.py` from the repository root to render the
selected main and appendix figures from saved data, including the legacy
radial and spherical plots. No training or GPU work is launched. Use
`--list`, `--check`, or `--only storage accuracy trajectory` to inspect or
select figures. Outputs go to a fresh generated-data folder, not over the
manuscript assets. [Plotting instructions](scripts/README.md) describe
dependencies and exporting a portable data package.

## Build

From `paper/`, use a fresh study-owned output directory to keep auxiliary
files out of the manuscript folder:

```bash
paper_build_dir=$(mktemp -d ../data/generated/headline_threefold_upgrade_20261011/paper_build.XXXXXX)
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir="$paper_build_dir" main.tex
```

The current 115-page build, including the introduction and related-work
discussion, is in
`data/generated/headline_threefold_upgrade_20261011/framing_build.YVWqPV/`
and was published as `paper/compact.pdf` before the entry-point rename.
The freshly rebuilt current publication is `paper/main.pdf`, from
`data/generated/headline_threefold_upgrade_20261011/main_build.gd8fkP/`.
Its text is identical to the preceding build; figures occupy pages 92–115.
The preceding 113-page build is retained in
`data/generated/headline_threefold_upgrade_20261011/figure_appendix.833uww/`
and in rollback commit `3233888`. Its figure section occupies pages 90–113.
The preceding 89-page build, after the statement-only relocation, is retained in
`data/generated/headline_threefold_upgrade_20261011/feature_theorem_move.RsouOA/`
and is superseded only by the figure/table editorial changes. The reviewed
pre-relocation build remains
in `data/generated/headline_threefold_upgrade_20261011/short_paper_v2/build/`.
The 94-page rollback build remains at
`data/generated/headline_threefold_upgrade_20261011/paper_integration_v3/build/`;
the still earlier PDF is retained beside that build as `prior_compact.pdf`.
The static TeX sources, bibliography and included figures suffice to compile
the manuscript; regenerating the appendix is not a build prerequisite.

## Empirical validation

Earlier experiments implement Harmonic and an empirical finite-program
seeded decoder in the single script `figures/capture_trajectory.py`.
Their state/fidelity comparisons, dimension checks, embedded-digits results,
negative cases and Legendre illustrations are preserved in the final figure
collection and saved records. They are not presented as tests of the new finite-panel log-cubed
theorem. The newer concurrent suite described below is unchanged.

The new experiments measure maximum recorded-time unseen-input RMS against
an actual independent dense pair. They do not establish asymptotic exponents,
continuous-time/sphere supremum bounds, confidence rates, or a setup speedup.
Harmonic setup uses a full offline dense rollout. The empirical seeded-decoder
backend uses float64 and an ordinary counter PRNG, not the certified finite-bit
backend. Source construction and query workspace are accounted for separately.
Matched small networks sometimes do better, including on the digits task.

`figures/compression_validation_source.json` preserves every pilot,
confirmation, failure, configuration, source hash, timing and plotted curve
available at export. The three `compression_*.pdf` figures can be regenerated
from this bundle without the raw runs. Commands are in
[scripts/README.md](scripts/README.md); the protocol and outcome accounting are
in [the empirical study](../studies/compression_empirical_validation_20261007/README.md).
[FIGURE_EXPERIMENT.md](FIGURE_EXPERIMENT.md) retains the historical figure record.
Other figure exports and their renderers remain available for reproduction
and alternative layouts; they are not all included in the current manuscript.
The immutable snapshots under `reviews/` retain the inputs supporting those
historical reviews, not alternative current theorem interfaces. Their copies
are intentional and must not be deduplicated against the evolving manuscript.

### Unified width-scaling suite

The same executable now provides a self-contained two-layer tanh Legendre
closure, geometric Harmonic setup in dimensions2/3, and the latest rank-safe
finite-panel Taylor optimizer. The unified suite compares their Euler
trajectories with learned-state-matched small dense and two-block low-rank
models, plus the exact initial-NTK Euler control. Fixed matrices are charged
separately; the NTK control deliberately uses a smaller state. There is no PCA.

```bash
python paper/figures/capture_trajectory.py unified-check
python paper/figures/capture_trajectory.py compression-sweep --protocol unified \
  --plan studies/unified_compression_empirics_20261008/plan.json \
  --devices cuda:0 cuda:1 --case-seconds 900 --out /path/to/fresh/runs
python paper/figures/capture_trajectory.py unified-plot \
  --root /path/to/fresh/runs --out /path/to/figures
```

The [fixed protocol and outcome record](../studies/unified_compression_empirics_20261008/README.md)
separate two engineering pilots from twelve width-comparison cases. Eight
training inputs and thirty test inputs are used throughout. Harmonic uses
independent sphere nodes; finite-panel Taylor setup sees the test inputs,
never their labels. Both practical source builders use full-horizon offline
dense rollouts. These experiments do **not** validate initialization-only
setup, arbitrary unseen-input decoding by the finite-panel method, asymptotic
exponents, or a uniform-in-time/input theorem. Results are not automatically
inserted into the manuscript.

## Directory cleanup

Commit `306733f` preserves the complete unified-paper revision before cleanup.
The unused top-level `proof_alltime.tex`, `proof_finite_time.tex`,
`proof_tracking.tex`, `comparison_appendix.tex`, `sphere_appendix.tex`, and
`NOTES_alltime_theorem.md` were removed: none is read by the current manuscript
or its figure tools. They remain recoverable from that commit. Current proof
sources, all figure/data bundles, experiment scripts, interactive viewers and
frozen review inputs are retained. `scripts/order_decay.tex` is a standalone
figure source, not a stray manuscript fragment.

The old trial PDF, disposable review page/contact-sheet images and Python
bytecode cache were moved out of `paper/` into the framing study's
`data/generated/response_compression_framework_20261008/paper_cleanup_19UBb0/`
archive, preserving their original relative paths. No experiment was rerun
or scientific statement changed during cleanup.
