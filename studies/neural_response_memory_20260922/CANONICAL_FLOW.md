# One canonical flow implementation

`compact_flow.Flow` is the single numerical implementation for the full dense
finite-width flow and the original residual-activity Legendre population closure.
Use `run_compact_flow.py` for new experiments. Historical experiment drivers
are retained for provenance; they do not define separate flow equations.

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

Verification: `check_compact_flow.py` passed 1,416 assertions (maximum absolute
discrepancy `1.33e-15`). Checks include legacy equation equivalence, independent
autograd gradients, depths 1/4/20 with all six built-ins and the optional
initialization, and explicit reconstruction of nonzero P1/P2/P3 moment states.
Custom activations and the depth-one dense/closure identity are also checked.
These are implementation checks, not a guarantee of fitting arbitrary data or
of converged continuous-time predictions at a chosen Euler step.

The current empirical check is under `canonical_unnormalized01/` in this study's
generated-data directory. It uses the same four stress datasets at width 2048.
The shared configuration does not yet fit all closures. Failed settings remain
reported; no task-specific equation or architecture patch is adopted.

## Source-file consolidation audit (2026-09-26)

The study currently contains 86 Python files, totaling 21,409 lines. The audit
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

Keep `check_compact_flow.py` as a separate development check: its legacy
equivalence section currently imports three historical engine modules.
Tests therefore have more dependencies than the two-file runtime. Old rational
closures, direct-factor controls and the scalar hierarchy models also represent
distinct mathematics; folding them into the current engine would not be a
behavior-preserving deduplication. Scalar work includes concurrent changes.

No source files were moved or deleted in this audit. Before physically retiring
historical scripts, preserve their exact source and reproduction commands and
resolve incoming checker/script references. Do not concatenate them into a
large two-file monolith or silently replace historical protocols with the
current fixed-step solver. Future dense/closure experiments use the two-file
interface above, with one separate development check.

The complete per-file inventory, dependency references, duplicate-body groups
and isolated-check receipt are under
`data/generated/neural_response_memory_20260922/code_consolidation_audit01/`.
