# Experiment editorial check

Read-only scoped check, 2026-10-11. Inputs were the current `paper/` README,
plotting instructions, plotting entry point, selected generation/analysis
implementations, and the portable response-memory bundle. No other study,
linked generated-data namespace, prior review, or archived manuscript was
opened. No training, figure rendering, or manuscript edit was performed.
The canonical-notation skill, neural-network reference, and paper-review
severity rubric were applied. This is an empirical editorial report, not an
independent review of the theorem or fresh experiment reproduction.

## Controlling evidence gap

The desired modern plots are **not self-contained under `paper/`**.
`paper/plot_figures.py:25` maps `storage`, `accuracy`, `trajectory`,
`fixed_budget`, `robustness`, `dense_pairs_mnist`, and other modern figure IDs
to `data/generated/paper_appendix_pilots_20261009/…`. Those inputs are outside
this assignment's read boundary. The portable bundles under `paper/figures/`
are older response-memory/radial/sphere/control experiments; the separate
`compression_validation_source.json` concerns an older Harmonic/seeded-decoder
edition. It cannot supply the new finite-panel Taylor results.

Accordingly, this check verifies modern **protocol and plotting semantics**
from code, not the claimed numerical advantage, completeness, seed counts in
the actual selected files, or current saved configurations. A modern
exported plotting package with its manifest is the minimal missing input.
Absent that package, do not present the following proposed numerical claims
as independently checked.

## Claims and the qualifications they require

| Proposed claim | Evidence and appropriate scope |
|---|---|
| Taylor beats the independent dense discrepancy at equal storage | The `accuracy` renderer compares endpoint prediction RMS against **learned scalar count**, not equal total memory. It contains a paired dense benchmark and small-dense/low-rank/frozen-feature controls. Numerical dominance remains unverified without `accuracy.json`. Specify the tested budgets and endpoint; avoid a universal superiority claim. |
| Width sweep through 16,384 with three seeds | The fixed-budget analysis explicitly requires widths 2,048/4,096/8,192/16,384 and exactly three complete pairs per displayed method. The storage renderer accepts its width grid from the missing input. These finite tests cannot identify asymptotic exponents; its log-power fits are descriptive. |
| Raw MNIST is in the main experiments | **Incorrect for the current three main plot IDs.** `storage`, `accuracy`, and `trajectory` explicitly use sklearn **8×8 Digits 1 versus 7, d=64**. Raw 28×28 MNIST has a runner implementation and a separate independent-dense-pairs figure. That figure alone supplies no Taylor/control comparison. |
| All small-dense, low-rank, and frozen-feature controls fail | Not verified numerically here. Even if the selected curves support it, say the **tested controls do not match the coupled reference to the same tolerance at these budgets**. Failure to track a reference is not failure to fit labels or a general claim about every small/low-rank/kernel model. |
| Tracking over the entire training trajectory | Modern measurements use 65 saved Euler times from 0 to 32; the main trajectory plot shows positive times only. State "recorded training times". They are not the theorem's continuous-time, all-input supremum or its infinite-time endpoint. |

For a query panel of size \(p\), the measured discrepancy at a saved time
\(t_j\) is

\[
\left(\frac1p\sum_{a=1}^{p}
  |f^{\mathrm{compressed}}(x_a,t_j)-f^{\mathrm{dense}}(x_a,t_j)|^2
\right)^{1/2}.
\]

The independent-dense comparator replaces the compressed prediction with
an independently initialized dense run. Modern width selection compares the
**maximum of each RMS curve**. A ratio of maxima at most one does not imply
pointwise domination at every time. `storage` reports the smallest **tested**
passing learned state, not an optimized minimum.

## Protocol facts established from current code

- `paper/plot_figures.py:436` and
  `paper/figures/capture_trajectory.py:13707` define the accuracy comparison:
  two panels (sphere, d=3; Digits, d=64), dense width 4,096, eight training
  inputs, 30 declared queries, endpoint t=32, and 65 saved times. The producer
  caption specifies Euler steps 1/640 (sphere) and 1/160 (Digits).
- Three-reference means and sample SDs cover the compression groups, frozen
  features, and independent dense pairs. Small-dense controls retain the
  original-reference protocol: sphere median/range, Digits mean/sample SD.
  Low-rank budget points retain original single runs. Do not describe every
  plotted control as three independently paired repetitions.
- Incomplete compression groups have no three-repetition summary. One
  missing Taylor budget is explicitly acknowledged by the plotting caption.
  The current unified renderer filters incomplete points; it must not be
  described as evidence of a completed budget grid.
- Taylor setup sees the declared query **inputs**, never their labels.
  Separate withheld-input Taylor results appear as hollow markers in the
  Digits accuracy panel; these are out-of-scope diagnostics, not the
  finite-panel guarantee. Harmonic sources use geometric nodes.
- Both practical source builders use an offline dense rollout through the
  required finite horizon (`capture_trajectory.py:9686`, `:9810`). They are
  not tests of initialization-only construction or evidence of setup speedup.
- Learned and fixed state are separate. Legendre retains its full dense
  mixer (`:685`). Two-block low-rank adaptation retains initial first and
  hidden matrices (`:893`). Frozen features use the equivalent dual Euler
  evolution, while the runner also reports primal readout/matrix storage
  (`:9707`). Query data, solver workspace, and temporary setup are separate.
- Under the actual zero-readout Gaussian initialization (`:163`), the full
  initial NTK reduces to the readout feature kernel (`:1304`). Thus the
  modern frozen-feature control is a meaningful initial-linearization
  control, but does not test every kernel or another parameterization's NTK
  limit. The low-rank control trains two factor blocks with mobilities chosen
  to match expected initial induced block velocities (`:893`).
- The raw MNIST loader (`:8844`) uses the official train/test split,
  balanced binary subsets, all 784 pixels, and unit Euclidean normalization,
  with no PCA. Labels are multiplied by configurable `label_scale` (`:8904`).
  The default is 1, but the missing selected run configurations are required
  before asserting that all displayed experiments have label scale 1. The
  toy target is normalized by its training RMS before this multiplier;
  `label_scale=1` therefore would not mean all toy labels have magnitude one.
  None of this is evidence of the theorem's growing-label regime.
- The d=784 robustness point is a **dimension-sweep panel-span variant**,
  not proof that raw MNIST was used. Its fixed projection is counted. The
  analysis records original full-coordinate candidates as infeasible
  (`:15388`). Do not conflate input dimension with dataset identity.

The fixed-width diagnostic's embedded protocol (`:15223`) specifies compact
width 512; Circle Harmonic retained rank 37, spatial degree 25, temporal
degree 8, source cap 42; Circle Taylor rank 36 at n=2,048 and 37 thereafter,
with source caps 36/42/48/79; Digits Taylor rank/cap 32 and temporal degree 8.
Circle seeds are 1701/1702/1703; Digits seeds are 1901/1902/1903. These are
code-level expected settings, not independently checked saved outcomes.
Current trajectory orders/ranks may override historical defaults; read its
actual exported configuration before reporting them.

## Directly recomputed legacy evidence

Using `/home/amir/miniconda3/bin/python` and NumPy, this check loaded only
`paper/figures/response_memory_source.npz` with `allow_pickle=False`, and
recomputed \(\sqrt{\operatorname{mean}((f-f_{\mathrm{dense}})^2)}\) from its
stored prediction arrays. The values match the bundle metadata exactly:

| Saved endpoint comparison | Prediction RMS versus dense |
|---|---:|
| MNIST 3 versus 8, Legendre order 1 | 0.003247560410434991 |
| MNIST 3 versus 8, Legendre order 2 | 0.001084434749988775 |
| MNIST 3 versus 8, Legendre order 3 | 0.001199224207446615 |
| Circle paired labels, Legendre order 3 | 0.0028176104270794295 |
| Same circle task, factor seed 20260924 | 0.3754643514759871 |
| Same circle task, factor seed 20260925 | 0.20358024445835482 |

The MNIST renderer documents 100 training images, 1,984 held-out images,
two tanh hidden layers, width 4,096, and each model's own training-MSE
0.001 endpoint. The bundle stores predictions and digit identities, not raw
image preprocessing/configuration or a three-seed Taylor comparison. The
nonmonotonic order-2/order-3 discrepancy is real in the saved arrays.
  This legacy illustration supports endpoint Legendre fidelity. It cannot be
recast as modern Taylor, raw-MNIST width scaling, or dense-pair evidence.

The legacy MNIST extraction code (`experimental_figures.py:164`) copies only
endpoint comparisons, predictions, and digit identities. Its portable
manifest and current manuscript captions do not specify raw pixels versus
PCA, input dimension, normalization, initial seed, or label multiplier.
Those legacy preprocessing facts remain unverified within `paper/`; the
current raw-MNIST loader cannot retroactively establish how the older run
was produced.

The same-rank circle comparison has correction rank bound 24 and individually
fitted endpoints; equal correction rank is not equal learned or total storage.
The bundle also contains 39 common-time checkpoints of dense and Legendre
orders 1/3/7 over 2,048 circle queries. This is saved-data reanalysis; the
training producer was not rerun.

## Best compact figure set

Use **accuracy + trajectory + storage**, in that argumentative order:

1. `accuracy`: directly tests fidelity at comparable learned budgets and
   displays the tested alternative dynamics.
2. `trajectory`: shows how coupled-reference fidelity develops at saved
   physical times, rather than relying on the endpoint alone.
3. `storage`: shows the finite-width storage tradeoff through the recorded
   grid, with descriptive fits explicitly qualified.

If limited to two figures, retain accuracy and trajectory and report the
verified width-grid facts in prose. `fixed_budget` is the strongest optional
replacement when the numerical comparison to dense variability across widths
matters more than a selected-budget storage curve: all complete compact-width
512 candidates are included regardless of passing.

After a modern exported plotting package is supplied inside this study,
the exact plotting-only command is:

```bash
/home/amir/miniconda3/bin/python -B paper/plot_figures.py \
  --data-dir data/generated/compression_literature_positioning_20261011/plot_inputs \
  --only accuracy trajectory storage \
  --out data/generated/compression_literature_positioning_20261011/experiment_figures
```

The output directory must be fresh; `plot_inputs` needs `accuracy.json`,
`trajectory.json`, `storage.json`, and the original exporter manifest with
matching checksums. To substitute the fixed-budget diagnostic, replace
`storage` by `fixed_budget` and supply `fixed_budget.json`. No figure was
redrawn in this check.

## Editorial severity

- **Major concern if asserted:** calling the main Digits panels raw MNIST,
  claiming equal *total* storage from learned-state axes, or presenting
  sampled/offline-rollout evidence as a theorem-scope/setup certificate.
- **Major concern if asserted:** all controls having the same three-reference
  protocol, or extrapolating specific control discrepancies to universal
  failure of small, low-rank, or kernel models.
- **Coverage limitation:** modern numerical advantage and selected-run
  metadata remain unverified because their actual inputs were not supplied
  within the authorized boundary. This is not evidence that they are false.
