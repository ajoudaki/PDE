# Unified experiment suite

Use **`compact_flow.py`** for both imports and commands. This is the only active
Python file for this suite: network, all compression methods, initialization
dictionaries, datasets, config runner, RMS reporting and optional `--check`
share one implementation. The separate dictionary, runner and checker files
have been removed. They remain recoverable from checkpoint `531a329`.

Scalar compression remains separate and unchanged. Current experiment configs
use no normalization. The historical optional LayerNorm API is retained for
compatibility; it is not enabled by this runner.

## Methods and their actual scope

| Config `kind` | Meaning | Supported settings |
|---|---|---|
| `dense` | Full trainable dense hidden matrices | Any positive hidden depth, input dimension and supported activation |
| `closure` | Evolving residual-activity Legendre response memory; retains the actual initialized matrices | Same MLP settings; any positive order, including P=1,2,3 |
| `dictionary_old` | Original frozen circle polynomial/action-word dictionary | Two hidden tanh layers, 2D inputs, historical initialization; orders 1,3,5,6,7,8,9 |
| `dictionary_flow` | Frozen initialization dictionary from population gradient-flow coefficients | Same historical setting; orders 1 through 7 |
| `gaussian` | Frozen Gaussian random bases, column RMS normalized | Arbitrary MLP settings with explicit ranks |
| `orthogonal` | Frozen random QR bases, scaled by sqrt(width) | Arbitrary MLP settings; ranks cannot exceed width |
| `trainable_dictionary` | Same dictionary/core representation, with the bases also trained | Any MLP with Gaussian/orthogonal bases; historical bases retain their original scope |
| `low_rank` | Directly train factors in `W_l = W0_l + A_l B_l` | Any MLP; explicit positive `rank` per hidden link |
| `weighted_closure` | Response-adapted clock and weighted Legendre history projection, with matching initialization prefix | Any MLP; positive `order`, `clock="response"` (default) or `"residual"` |

The recovered **old circle dictionary uses Chebyshev polynomials of initialized
response coordinates and retained action words**. Calling that implementation
Hermite would be inaccurate. The separate Hermite residual-network Galerkin
construction is not substituted for this MLP method.

The old and gradient-flow dictionaries remain frozen at initialization. Their
trainable hidden links are `W_l = B_(l+1) C_l B_l.T / n`; the core coefficients,
first-layer weights and readout evolve. They do not retain an extra dense
background. Core initialization is `B_(l+1).T @ W0_l @ B_l / n`. Thus their
initial predictions generally differ from dense; response-memory closure, in
contrast, starts with the dense predictor. Neither dictionary uses training
labels or a fitted trajectory to construct its basis.

The dictionary order has a **method-specific meaning**, not a common parameter
budget. Every result records the actual basis ranks. Historical random controls
can use `order` instead of `ranks`: at depth two this reproduces the original
old-dictionary ranks and fixed maximal-draw prefix protocol through order 9.
With explicit `ranks` (one integer or a list per hidden layer), the random draw
has that declared shape; use this to match a different dictionary's rank.

Dictionary formulas are consolidated from the explicitly requested old circle
and gradient-flow dictionary sources; those source studies were not changed.
The established `code/pde/observable_initialization.py` and
`observable_words.py` still supply the polynomial-word compiler. There is no
runtime import from the old studies. Their untouched builders are used only
by the optional GPU regression test.

## One model and one trainer

The MLP is bias-free, has a common configurable width and scalar output
`f = c @ h / n`. Depth counts hidden layers. Input rows are supplied in their
intended scale; the engine does not silently rescale them. The loss is mean
squared error. Mobilities are `n` for the input weights and readout, and `1`
for each dense matrix or frozen-dictionary core.

Built-ins are `relu`, `gelu`, `selu`, `tanh`, `sigmoid`, and `silu`. A config may
supply a list of activations, one per hidden layer. The Python API additionally
accepts `(activation, derivative)` callables. Historical dictionaries enforce
their narrower derivation scope rather than inventing formulas for other MLPs.

Initialization uses a shared seed for matching models. Defaults
`hidden_gain=1, readout_std=null` preserve the old law, with stored readout
standard deviation `1/n`. Optional `hidden_gain="unit_moment"` selects the
hidden-link gain from the preceding activation's Gaussian second moment using
128-node quadrature. `readout_std=1` supplies a width-independent stored readout
scale, with the same output and muP mobilities. These are explicit initialization
choices, not normalization layers. Historical dictionaries require the old law.

All methods share the fixed-step CUDA-graph fitter. Existing methods and the
two trainable-factor methods use simultaneous Euler. Weighted history uses
Euler for network/source velocities and exact polynomial coordinate transport
for its moments and Gram matrix; see below. There is one host loss read per block.
There are no adaptive retries,
line searches, clipping, task-specific optimizer branches or hidden learning-rate
changes. The solver records the actual step count, physical time, capture time
and stop reason. Its wall-time cap includes capture but excludes initialization
and final test prediction. Stopping occurs at block endpoints. Float32 is the
explicit default; float64 is available; TF32 is disabled by the runner.

This is a fast numerical implementation, not a guarantee that one fixed step
fits every task or resolves continuous gradient flow. The earlier all-fit
stress objective remains unachieved; see `CANONICAL_UNNORMALIZED_RESULTS.md`.
Underfit and nonfinite runs are reported rather than filtered out.

## Added methods and their clocks

`{"kind":"trainable_dictionary","basis":"dictionary_flow","order":3}` trains
the initialized bases as well as their cores. `basis` can also be
`dictionary_old`, `gaussian` or `orthogonal`; use `ranks` for random bases at
arbitrary depth. The existing frozen path computes the prediction and core
velocity. The additional basis velocity has mobility `n`; an intermediate
population basis receives both incoming and outgoing link gradients. These
are the original trainable-dictionary equations generalized link by link.
The historical frozen methods remain frozen.

`{"kind":"low_rank","rank":12}` retains each initialized dense matrix and
trains `A_l B_l`, with `A_l=0` and independent Gaussian `B_l` entries of standard
deviation `1/sqrt(rank)`. An integer rank applies to every hidden link; a list
specifies each link. Both factor mobilities are `1`; outer mobilities are `n`.
This preserves the original factor-control parameterization and physical time,
rather than silently rescaling it to accelerate optimization.

`{"kind":"weighted_closure","order":3}` implements the matching-prefix
construction in [RESPONSE_CLOCK_FULL_CLOSURE.md](RESPONSE_CLOCK_FULL_CLOSURE.md).
For each link it stores moments `U,H` of the residual-normalized backward field
`u = residual * delta / rho` and forward field `h`, with weight `rho dt`, where
`rho` is training RMS. Each moment `U_p,H_p` is an `n x M` matrix. One shared
Gram matrix reconstructs each correction as
`-2/(n M) * (sum_pq (G^-1)_pq U_p H_q.T - u0 h0.T)`.
The fixed prefix subtraction ensures that
initial predictions match dense exactly. The response clock is
`g = rho + ||d(h,u)/dt||_2`, concatenating all compressed links with the source's
unscaled Euclidean convention. `clock="residual"` selects `g=rho` while keeping
the same weighted projection. P1's physical model is clock independent.

The response derivative uses one directional derivative of the shared network
traversal, along its computed weight velocity. It does not construct a Hessian,
Jacobian or dense weight update. Each traversal solves one small `P x P` Gram
system for all links; moments use the selected network dtype, while the Gram
and clock use float64. At exactly zero residual the state is stationary. For
ReLU/SELU, derivatives follow the implementation's almost-everywhere convention;
the smooth-theory assumptions do not automatically extend across their kinks.

The weighted step transports the polynomial coordinates from `L` to `L+dt*g`
and adds the positive rank-one Gram contribution of the new history sample.
This avoids the indefinite Gram matrix that plain Euler can produce from basis
dilation alone. It is a fixed, first-order explicit step with no retries, ridge
regularizer or adaptive step search; checks verify its stated ODE limit. The
response clock adds work compared with ordinary memory, and a tiny Gram can
still become ill-conditioned over a long run. No claim that the new method fits
faster or improves final RMS is made by these implementation checks. Extension
of the two-layer construction to multiple links is an implementation choice,
not an additional approximation theorem.

## Saved experiment configs

`experiment_configs.json` contains editable examples for all six circle cases,
smooth sphere tasks with 16/64 samples, the four high-frequency/full/partial
support tasks, MNIST, and `additional_methods` for the three additions.
They are starting configurations, not newly validated
fitting claims. Select the examples you intend to run:

```sh
python -B studies/neural_response_memory_20260922/compact_flow.py \
  --config studies/neural_response_memory_20260922/experiment_configs.json \
  --experiment circle_baselines \
  --out data/generated/neural_response_memory_20260922/my_run
```

A catalog contains `{"experiments": {"name": CONFIG, ...}}`. A single experiment
file can contain `CONFIG` directly. Each config separates `model`, `optimizer`,
`methods`, `datasets`, and `device`. Relative data/cache paths are resolved from
the config's directory. `--device cuda:1` may override the device. Model/data/solver
CLI overrides cannot be mixed with a JSON config. Unknown fields and unsupported
combinations fail before training. Output directories must be fresh.

Datasets:

- **Circle:** named historical `case`, literal `angles_degrees`/`labels`, or
  generated sinusoidal labels with configurable `samples`, `frequency`, `phase`,
  `span_degrees` and `start_degrees`. Queries cover the full circle.
- **Sphere:** whole-sphere or cap training (`z_min`), oscillatory or `xy`/`xyz`
  targets, configurable sample count/frequency/seed. Queries use the full
  equal-area Fibonacci sphere grid. `sampling="normal", seed=20260925`
  reproduces the earlier smooth-sphere training sets.
- **MNIST:** two configurable digits, balanced seeded training samples, official
  test split, L2 or pixel scaling. Reads official cached IDX files, compressed
  or uncompressed; it never substitutes synthetic data. `samples_per_class=500`
  reproduces the original 1,000-image panel. A fresh 50-per-class raw selection
  differs from the historical nested 100-image subset; the
  `mnist_historical100` config reads that exact saved subset instead.
- **NPZ:** arbitrary `inputs`, `labels`, `test_inputs`, optional `test_labels`
  and boolean query `region`; historical `train_*`/`validation_*` aliases work.

`--prepare-only` saves the chosen datasets without allocating models or using
CUDA. Existing `--data NPZ ... --width ... --depth ... --activation ... --step ...`
commands still work for dense/P1/P2/P3; `--orders 0 1 2 3` selects those models.

Every run saves the resolved config, command, source/data hashes, Git version,
precision/device metadata, dataset provenance, predictions and model records.
`rms.csv` reports train RMS, query RMS against dense, optional target RMS, and
inside/outside-region differences. The `fitted_pair` column requires both model
and dense to meet the declared training target. A missing dense reference gives
a null comparison. Recompute metrics and verify prediction/data hashes with:

```sh
python -B studies/neural_response_memory_20260922/compact_flow.py \
  --summarize data/generated/neural_response_memory_20260922/my_run/circle_baselines
```

Query RMS compares final endpoints over the saved full query grid; it is not
an exact continuum integral or a same-physical-time trajectory comparison.
MNIST uses the saved official test panel, not a circle/sphere interpretation.

## Consolidation checks and historical preservation

Run `python -B studies/neural_response_memory_20260922/compact_flow.py --check`.
Add `--gpu cuda:0 --out FRESH.json` to check CUDA graphs at width 2048 and all
original dictionary orders. Checks cover independent autograd gradients, all
six activations, depths up to 20, P1/P2/P3 reconstructed operators, frozen bases,
legacy velocities, dataset reproduction and saved RMS computation.

The earlier consolidation verification is in `unified_suite01/`; the single-file
checks are in `data/generated/neural_response_memory_20260922/single_file01/`.
The original CPU checks passed 2,136 assertions (maximum discrepancy 1.33e-15);
the additions passed 610 assertions, including independent autograd checks for
trainable factors, 36 weighted-history cases, reconstructed-operator and clock
derivatives, the zero-residual case, P1 clock independence and first-order step
consistency. The saved runner/RMS checks exercise every new method.

MNIST's 1,000 training and 1,984 test rows reproduced bitwise. The width-2048
CUDA captures matched eager state updates exactly in the tested 19-step runs,
including the final partial block: 22 cases, including depth-four ReLU/GELU/SELU
with three-dimensional inputs for every added method. The complete CPU/GPU
check took 16.01 seconds; its source hash and results are in
`single_file01/final_check.json`. All six config examples passed data preparation.
All supported frozen dictionary orders and
random controls matched their original builders and flow equations. This is
implementation verification, not a new fitting or scientific accuracy campaign.

65 redundant/historical study scripts were retired from the active directory.
`legacy_experiments.zip` preserves their exact source plus the three previous
canonical files, with a per-file SHA-256 manifest. The rollback checkpoint is
`87cade22a12323227d076e92f8801a1bdb7c21c0`; the archive was checked byte-for-byte
before removal. The checker imports legacy reference equations from this archive;
production code does not. The old study sources that supplied frozen dictionaries
remain in their original locations.

Shared data preparation and current endpoint reporting moved into the runner.
Old adaptive campaigns, rational-moment variants, the original direct-factor
control driver, normalization experiments, plotting scripts and detailed diagnostics
remain in the archive with their own protocols. They are not silently redefined
as the new fixed-Euler suite. Older Markdown reproduction commands refer to
those archived filenames. Existing reports, theory notes, datasets and scalar
compression files were not consolidated or rewritten; this guide is the current
entry point.
