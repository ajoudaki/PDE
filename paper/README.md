# Response-memory paper draft

The working manuscript is `main.tex`, compiled to `main.pdf`:
`Compressing Global Dynamics of Deep Nonlinear Feature Learning`.
It adopts the user's alternative draft, with targeted corrections to claim
scope, the more detailed comparison derivations, and the updated figures.

Build from this directory with:

```bash
latexmk -pdf main.tex
```

The current PDF has 34 pages and compiles without warnings or unresolved
references. The early comparison table is on page 6; the radial circle figures
are on pages 12 and 13. Appendix E (page 28 onward) gives the common error metric,
conditional population cost comparisons, NTH and DMFT derivations, and the
sharper weighted joint-clock estimate. Appendix F (page 34) contains the
supplementary sphere-order figure.

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

Figures and reproduction tools:

- `figures/circle_deep_radial.pdf`: three hidden tanh layers, orders 1/2/3.
- `figures/circle_shallow_radial.pdf`: two hidden tanh layers, orders 1/3/7.
- `figures/sphere_orders.pdf`: supplementary four-hidden-layer ReLU case.
- `figures/order_decay.pdf` and `figures/mnist_scatter.pdf`: existing results.
- [scripts/README.md](scripts/README.md): consolidated renderer, portable bundles,
  provenance, dependencies and reproduction commands.

These figures reuse saved predictions; no training was rerun. Sphere RMS
values were checked against the saved arrays. The sphere experiment uses one
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
