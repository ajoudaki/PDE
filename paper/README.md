# Compressing Global Dynamics of Deep Nonlinear Feature Learning

The working manuscript is [main.tex](main.tex), compiled to [main.pdf](main.pdf).
The 2026-10-08 revision presents a unified response-compression framework:
Legendre history compression, and a shared selected-coordinate runtime
with Harmonic (whole-sphere) and Taylor (declared finite-panel) source
builders. It is a working paper, not promotion into the maintained Quarto book.

## Reading and source structure

- `main.tex`: canonical network setup, motivation, discussion and appendix guide.
- `results.tex`: one prescribed-size compression theorem for all three methods,
  negligible error relative to actual dense variability and the theoretical
  consequences.
- `methods.tex`: retained states, update rules and the core theoretical ideas.
- `feature_learning_theorem.tex`, `feature_learning_proof.tex`, and
  `feature_learning_initialization.tex`: the additional nonlinear
  feature-learning theorem and its self-contained early-time proof,
  shared by the main and compact manuscripts. Its extra assumptions
  (nonaffine activations and no parallel or antiparallel training inputs)
  do not narrow the compression theorem. Taylor may append four predeclared
  passive witness inputs. Constants in this additional theorem depend on
  the whole fixed problem, not just activation and depth.
- `costs.tex`: interpretation of setup, runtime and query resources;
  initialization-only information is distinct from cheap initialization.
- `integrated_appendix.tex`: complete parameter-explicit scientific statements,
  certificates and shared proofs, plus the separate supplementary seeded decoder.
- `panel_appendix.tex`: complete residual-adapted finite-panel proof,
  initialization-jet compiler, explicit counts and unified theorem assembly.
- `cost_appendix.tex`, `empirical_appendix.tex`: detailed existing costs and
  earlier experimental illustrations, preserved with their original scope.
- `references.bib`: literature bibliography.

Main-text constants depend only on activation and fixed depth. All three
headline constructions have compression error divided by actual independent
dense-run discrepancy tending to zero in probability, on the same promised
query domain and over the entire training trajectory including its endpoint.
Harmonic and Taylor additionally attain absolute error `Y/n` at every
fixed confidence for sufficiently large width, with the displayed storage
orders unchanged. The older quantile/factor-three comparison belongs only
to the separate supplementary seeded decoder and historical experiments.
Structural parameters remain distinct. The appendix retains label factors, arbitrary
confidence, full label allowance, width gates, internal setup orders, and
finite-word evaluator/access costs. Its notation correspondence and a linked
page guide precede the detailed material.

The following distinctions are intentional:

- Legendre compresses the moving state but retains its fixed dense mixers.
- Harmonic tracks a coupled dense reference. Its explicit and implicit
  initializers have different setup costs; the latter samples a fresh latent
  reference rather than reading a supplied dense matrix cheaply.
- Taylor denotes the finite-panel, cubic-logarithmic real-coordinate
  construction. Its passive inputs, but not their labels, are available at
  setup. It tracks a coupled dense reference with the same selected nonlinear
  runtime as Harmonic. The finite initialization-only compiler has no proved
  near-linear or near-quadratic work bound.
- The older independent-reference finite-word construction is called the
  **seeded decoder** in the appendices. Its words and bits must not be
  confused with the new Taylor model's real-coordinate count.
- The dense lower bound is transient, not an endpoint result. All three main
  stochastic width thresholds remain qualitative. The seeded decoder's additive and
  analytic absolute certificates have an explicit conservative gate; its purely
  multiplicative intrinsic comparison also uses the lower bound's eventual onset.

The original detailed library was converted from the owning study's
[RESULT.md](../studies/integrated_general_compression_20261004/RESULT.md).
The static appendix retains that proof chain with editorial integration
patches. **Do not regenerate it over the current file** with the old
converter: that would overwrite the current naming, scope and label-factor
corrections. The new panel proof is separately integrated from the authorized
adaptive-clock and initialization-panel sources. LaTeX reads no study files;
all mathematical dependencies are statements and proofs inside the manuscript.

The rollback version is commit 2c27cbc; its frozen checks remain in
[PAPER_REWRITE_CHECK.md](../studies/integrated_general_compression_20261004/PAPER_REWRITE_CHECK.md).
The new intrinsic-benchmark proof and scoped audit are in the owning study;
the earlier build record is
[PAPER_INTRINSIC_REVISION_CHECK.md](../studies/integrated_general_compression_20261004/PAPER_INTRINSIC_REVISION_CHECK.md).
These are editorial and bounded mathematical integration checks, not formal
verification or a new independent review of every proof.

The current unified-framing integration and its bounded checks are recorded in
[the framing study](../studies/response_compression_framework_20261008/README.md).
The new panel appendix was read against its complete flaring/adaptive sources;
the inherited proof library was not freshly re-reviewed in its entirety.

The subsequent targeted feedback revision corrects the panel propagator's
summed-exponent gate, explicitly specializes both Harmonic setup bounds to
the exact `Y/n` target, and makes label-sensitive eventual-width qualifications
prominent. It also separates `Seed` from the finite-panel Taylor model,
disambiguates proof-local radii, thresholds and quantiles, states the source
event formally, and repairs identified proof-interface and cross-reference
omissions. The headline storage orders and error conclusions are unchanged.
These are scoped checks of the supplied feedback, not a fresh independent
review of the entire manuscript. Decisions and verification are recorded in
the framing study linked above.

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
files out of the manuscript folder. The latest additional-theorem build is:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=/home/amir/Codes/PDE/data/generated/nonlinear_feature_learning_certificate_20261010/paper_build_19s6aj \
  main.tex
```

Use `compact.tex` with the same command to build the shorter proof manuscript.
The checked PDFs are copied to `paper/main.pdf` and `paper/compact.pdf` for
convenient reading; their pre-integration copies are preserved in that build
directory as `prior_main.pdf` and `prior_compact.pdf`.
The static TeX sources, bibliography and included figures suffice to compile
the manuscript; regenerating the appendix is not a build prerequisite.

## Empirical validation

Earlier experiments implement Harmonic and an empirical finite-program
seeded decoder in the single script `figures/capture_trajectory.py`.
Their state/fidelity comparisons, dimension checks, embedded-digits results,
negative cases and Legendre illustrations are preserved in the empirical
appendix. They are not presented as tests of the new finite-panel log-cubed
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
