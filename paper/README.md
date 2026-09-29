# Response-memory paper draft

The working manuscript is `main.tex`, compiled to `main.pdf`:
`Compressing Global Dynamics of Deep Nonlinear Feature Learning`.
It adopts the user's alternative draft, with targeted corrections to claim
scope, the more detailed comparison derivations, and the updated figures.

Build from this directory with:

```bash
latexmk -pdf main.tex
```

The selected figure editions have been merged into `main`. The current TikZ
renderer is `scripts/tikz_figures.py`; figures and portable source bundles live
in `figures/`. The main text includes the mechanism, moment-history illustration,
shared-time evolution, four-method fitted-function comparison and deep radial overview.
Detailed rank, numerical-sensitivity and MNIST panels are in the appendices.
[FIGURE_EXPERIMENT.md](FIGURE_EXPERIMENT.md) preserves the earlier edition's
evidence and rendering record.

[NOTE_fig3_trajectory.md](NOTE_fig3_trajectory.md) documents the completed
39-checkpoint replay for Figure 3, its checks and reproduction commands.
It preserves the original task and initialization and adds genuine shared-time
predictions at two numerical resolutions. `figures/capture_trajectory.py`
performs that bounded capture; `scripts/tikz_figures.py trajectory` redraws
the figure from the bundle without training.

Figure 4 uses `figures/learning_controls_quadrant_alternating.pdf` to compare
dense, frozen NTK, rank-matched factors, and response memory. The previous
compact factor figure is retained in the appendix, followed by the full
five-task comparison split into `learning_controls_gallery_a.pdf` and
`learning_controls_gallery_b.pdf` for readability. The standalone
`learning_controls_gallery.pdf` contains all five rows together. Individual
rows, the portable data, and the bounded kernel capture are documented in
[the figure guide](scripts/README.md#four-method-comparison-across-five-circle-tasks).

`main_alternative.tex` and `main_alternative.pdf` retain the attachment as
originally compiled (28 pages, with only PDF bookmark fixes). They are a
comparison snapshot, not the current working manuscript. Git commit `bbfef82`
preserves both pre-adoption versions and their sources. The earlier rollback
checkpoint is `df473babba4849c80db75c2578995011f3450f37`.

The chosen narrative, early comparison table, low-rank corollary and fixed-width
size-at-accuracy calculation are retained. Corrections distinguish:

- prescribed finite horizons from all-time or horizon-independent order;
- restricted exact nonclosure results from universal impossibility claims;
- proved fixed-width rates from conditional population comparisons;
- evolving learned state from fixed initialization and total computational cost;
- RMS/held-out prediction measurements from uniform pointwise error.

`comparison_appendix.tex` is included for the supporting derivations.
`sphere_appendix.tex` is included for the supplementary experiment.
`comparison.tex` is retained from the previous version but is no longer included;
the chosen draft integrates the main comparison into its own narrative.

The population discussion now includes a **conditional learned-state saving**
corollary. At matched test-prediction accuracy, the explicit hypotheses are a
root-width dense error estimate and a width-uniform quadratic closure tracking
estimate, in the same time/probability norm and with uniform order thresholds.
They give width proportional to epsilon^-2, order proportional to epsilon^-1/2
(the fourth root of width), and moving-state costs epsilon^-4 versus
epsilon^-5/2. The appendix derives the factor epsilon^-3/2 saving, the optimal
error allocation, and the version with a subpolynomial history-rate correction.
All-time use requires both error hypotheses for the all-time metric; small
labels alone are not asserted to establish them. These are certified costs,
not a dense lower bound, and retain the dense fixed initialization and its cost.
The allocation and subpolynomial correction were checked independently from
the stated hypotheses, and the resulting typeset argument was inspected.
The finite-horizon branch with a superpolynomial order threshold was removed
from the working manuscript at the author's request. The earlier trial files
remain separate. The restored 41-page manuscript compiles without LaTeX
warnings; auxiliary build files are kept outside the paper folder.

Figures and reproduction tools:

- `figures/circle_deep_radial.pdf`: three hidden tanh layers, orders 1/2/3.
- `figures/circle_shallow_radial.pdf`: two hidden tanh layers, orders 1/3/7.
- `figures/sphere_orders.pdf`: supplementary four-hidden-layer ReLU case.
- `figures/experimental_figures.py`: renders the new paper figures in place
  from `figures/response_memory_source.npz`; no training is required.
- `figures/experimental_gallery.pdf`: all seven new figures in presentation form.
- `figures/order_decay.pdf` and `figures/mnist_scatter.pdf`: earlier plots,
  preserved but replaced in this experimental manuscript.
- [scripts/README.md](scripts/README.md): consolidated renderer, portable bundles,
  provenance, dependencies and reproduction commands.

Figure 3 uses the documented new checkpoint replay; the endpoint, rank, MNIST
and sphere figures reuse their saved predictions. Sphere RMS values were
checked against the saved arrays. The sphere experiment uses one
seed and float32 Euler steps of 1/128 at individually fitted endpoints. ReLU
is outside the smooth-activation theorems, and the figure supplies neither
common-time trajectory evidence nor a continuous-flow refinement certificate.
The synthetic training-stage preview is not included.

The compiled manuscript PDFs are intentionally versioned for convenient reading.
LaTeX auxiliary files are ignored by `paper/.gitignore` and were removed locally
for both manuscript variants. Before publication, two bibliography build files
were removed from the unpublished history; the checkpoint IDs above refer to
that cleaned history. The original commits remain available locally on
`codex/paper-before-aux-cleanup-20260927`.
