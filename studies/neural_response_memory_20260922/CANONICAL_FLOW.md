# One canonical flow implementation

`compact_flow.Flow` is the single numerical implementation for the full dense
finite-width flow and the original residual-activity Legendre population closure.
Use `run_compact_flow.py` for new experiments and RMS reports. Historical
experiment drivers are preserved in the pre-consolidation Git checkpoint
`87cade22a12323227d076e92f8801a1bdb7c21c0`; they are no longer active files.

The current setup has **no normalization layers**. No task name, input dimension,
label pattern, or dataset-specific training rule appears in the engine or runner.
Data, network configuration, and numerical integration settings are separate.

```python
from compact_flow import Flow

model = Flow(inputs, labels, width=2048, depth=depth,
             activation=activation, order=P, normalization="none",
             hidden_gain="unit_moment", readout_std=1.0,
             seed=20260920, device="cuda:0")
fit = model.fit(step=step, target_rms=0.04,
                max_seconds=60, max_steps=60000, block=8)
prediction = model.predict(test_inputs)
```

- `inputs` has shape `(samples, dimension)`; labels are scalar, shape `(samples,)`.
- `depth` is any positive number of hidden layers, subject to available memory.
- `P=None` selects dense flow; positive integer `P` selects closure order.
- Built-ins are ReLU, GELU, SELU, tanh, sigmoid, and SiLU. The Python API also
  accepts `(activation, derivative)` callables and a list with one per layer.
- Dense and closure use the same initialization seed, forward/backward operations,
  muP scaling, and fixed simultaneous Euler integrator. The closure retains the
  initialized matrices and adds its response-moment correction.
- `step`, stopping RMS, and runtime budget are explicit solver configuration.
  There is no automatic tuning, optimizer substitution, or task-dependent branch.

Initialization is also configuration, not a change to the architecture. The
default `hidden_gain=1, readout_std=None` preserves the earlier initialization,
including standard deviation `1/n` for the stored readout `c`. The optional
`unit_moment` rule chooses the Gaussian gain of a hidden link from its preceding
activation: `gain = 1/sqrt(E[activation(Z)^2])`, using 128-node Gaussian quadrature.
This rule depends on the activation, never on the task or labels. It is an
initialization rule only; it performs no normalization during forward evaluation.
For a custom activation, this option requires CPU evaluation and a positive,
finite estimated Gaussian second moment; an explicit positive gain is also valid.
`readout_std=1` gives the usual width-independent stored readout scale while
retaining output `c @ h / n` and the same muP mobilities. Both initialization
choices are recorded and applied equally to dense and closures.

The generic command-line runner reads NPZ files with `inputs`, `labels`,
`test_inputs`, and optional `test_labels`. It applies **one supplied configuration
to every file**. For example, from the repository root:

```text
python -B studies/neural_response_memory_20260922/run_compact_flow.py --data circle.npz sphere.npz --out data/generated/neural_response_memory_20260922/my_run --width 2048 --depth 10 --activation selu --hidden-gain unit_moment --readout-std 1 --step 0.0009765625 --seconds 60
```

The default order list is dense/P1/P2/P3. `--orders` selects any nonnegative
orders, where zero denotes dense. The runner records the common configuration,
source and data hashes, exact command, environment, predictions, training RMS,
and query RMS versus the matching dense endpoint when it is present.
If only closures are requested, the dense-reference score is null, not guessed.

The runner also recomputes scores from saved predictions, writes `rms.csv`,
and prints a table. The `fitted_pair` column requires both dense and closure
training RMS to meet the configured target. A missing dense reference stays
unscored; underfit comparisons stay labelled. To regenerate a report without
training, use:

```text
python -B studies/neural_response_memory_20260922/run_compact_flow.py --summarize data/generated/neural_response_memory_20260922/my_run
```

This command handles the canonical runner's output format. Historical result
formats retain their original analyzers at the checkpoint, not implicit format
conversions or different numerical protocols in the current runner.

Verification: the standalone `check_compact_flow.py` passes 3,330 CPU assertions
(maximum absolute discrepancy `2.41e-13`). It uses independent PyTorch autograd
gradients, full reconstructed matrices, explicit moment-transport matrices and
simultaneous Euler checks. It covers depths 1/4/20, all six built-ins, custom
activations, optional initialization, nonzero P1/P2/P3 states, and depth-one
dense/closure identity. It imports no historical engines. Before retirement,
the previous legacy-equivalence suite passed all 1,416 assertions (`1.33e-15`).
The numerical engine is byte-for-byte unchanged by consolidation. These are
implementation checks, not a guarantee of fitting arbitrary data or converged
continuous-time predictions at a chosen Euler step.

The current empirical check is under `canonical_unnormalized01/` in this study's
generated-data directory. It uses the same four stress datasets at width 2048.
The shared configuration does not yet fit all closures. Failed settings remain
reported; no task-specific equation or architecture patch is adopted.

## Source-file consolidation audit (2026-09-26)

Before consolidation the study contained 86 Python files, totaling 21,409 lines. The audit
parsed every file's definitions, imports and literal script references, compared
duplicate function bodies, and inspected the current runtime and representative
historical variants. This is an organization/dependency audit, not a new
mathematical verification of every historical implementation.

| Role | Files | Lines |
| --- | ---: | ---: |
| Current runtime: `compact_flow.py`, `run_compact_flow.py` | 2 | 352 |
| Current verification: `check_compact_flow.py` | 1 | 121 |
| Historical experiment drivers | 21 | 5,401 |
| Historical engines | 6 | 1,182 |
| Historical analysis and plots | 12 | 3,801 |
| Historical verification | 19 | 5,758 |
| One-off diagnostics | 5 | 691 |
| Data preparation | 2 | 167 |
| Distinct scalar-model research, including its checks/drivers | 18 | 3,936 |

There are 20 groups of identical function bodies. In particular, the 460-line
activation runner and its 470-line fast variant largely duplicate one another;
execution-backend changes did not require a second complete runner. Campaign,
resume, dataset and reporting variants accumulated as separate scripts where
configuration and a shared runner would have sufficed.

**The active dense/Legendre-closure workflow already requires only the two
runtime files above.** Keep numerical equations in `compact_flow.py`; run all
tasks through `run_compact_flow.py` using data files and explicit configuration.
The runner already saves training RMS and whole-query-set RMS against dense.
New tasks, depths, activations and step sizes do not require new drivers.
Existing frozen NPZ datasets can be consumed directly; regeneration recipes
in historical drivers remain useful provenance, not runtime dependencies.

An isolated smoke check temporarily copied only these two source files, then
checked 144 small CPU models spanning six activations, depths 1/3/20, input
dimensions 2/3, and dense/P1/P2/P3. Two CLI datasets produced eight records whose
RMS values were independently recalculated from saved predictions. All passed
in 3.4 seconds. This checks dependency separation and basic execution only;
it is not a fitting or performance experiment. The CLI still uses NumPy,
PyTorch, and Git metadata from the checkout.

The complete per-file inventory, dependency references, duplicate-body groups
and isolated-check receipt are under
`data/generated/neural_response_memory_20260922/code_consolidation_audit01/`.

## Completed consolidation

The working study now has **21 Python files**: two dense/closure runtime files,
one standalone check, and 18 unchanged files for the separate scalar-model
investigation. The 65 historical/support scripts were removed only after
verifying their bytes against the rollback commit. Their role in current
experiments is replaced by the generic data/configuration runner and its
integrated reporting. Scalar code has no imports of retired modules.

The old rational closures, direct-factor controls, adaptive integrators,
campaign controllers and historical analyzers are retired implementations,
not mathematical aliases of the current fixed-step Legendre closure. No
historical protocol has silently been changed to use the current solver.
Saved experiment data and scientific reports are untouched.

Source retrieval uses the exact original paths at checkpoint
`87cade22a12323227d076e92f8801a1bdb7c21c0`. For example:

```text
git show 87cade22a12323227d076e92f8801a1bdb7c21c0:studies/neural_response_memory_20260922/activation_circle_run.py
```

The complete pre-cleanup study can be exported to a fresh destination using
`git archive` at that commit, with path `studies/neural_response_memory_20260922`.
Historical commands and source links in older Markdown files refer to this
versioned source. Reproduction also requires the recorded inputs and matching
source hashes; the checkpoint preserves the pre-cleanup tree, not a claim that
every earlier experiment used that exact revision. Avoid restoring old files
over the shared live checkout merely to inspect them.

Consolidation evidence and the full retired-file/hash list are in
`data/generated/neural_response_memory_20260922/code_consolidation01/`.
The final isolated CPU regression took 11.7 seconds: all 3,330 equation checks
passed, eight before/after model predictions were bitwise identical, eight
reports matched independently recomputed RMS values, missing dense references
remained unscored, and mismatched configurations/corrupted predictions were
rejected. These tiny-width checks validate the refactor, not experimental fit.

## Markdown cleanup recommendation (not performed)

The 109 study Markdown documents comprise 48 theory/research notes, 26 audits,
14 results reports, 10 protocols, five execution/decision notes, two benchmark
descriptions, two overview/API guides, and two communications documents.

- Shorten README to the current scope, entry points, results index and open
  limitations. Its 1,989-line pre-cleanup body is largely chronological history;
  preserve that history once instead of repeating reports in the landing page.
- Keep this implementation guide separate from scientific theory and results.
- Combine each completed experiment's protocol, numerical decisions and results
  into one report with dated sections and original evidence links. Retain what
  was planned versus amended, stopped/failed runs and exact configurations.
- The normalized stress sweep, activation extension and failed SELU fixes can
  share a report with separate configuration sections. The unnormalized results
  must remain explicitly distinguished: they concern different models/settings.
- Keep the 26 original audit/check documents intact as versioned evidence, with
  links from the relevant report. A later synthesis must not rewrite the scope
  or verdict of the original check.
- Consolidate theory only by mathematical topic after checking complete proofs,
  assumptions and corrections. Activity clocks versus response-speed clocks,
  population closures versus scalar truncations, and smooth versus nonsmooth
  activation results cannot be merged as if they were equivalent. Their titles
  and shared notation alone do not establish redundancy.
- Keep communications/handoff material separate from scientific documentation.

This suggests a small set of reading entry points with substantive proofs and
original audits linked underneath, not a single concatenation of all documents.
No scientific Markdown files have been merged or discarded in this cleanup.
