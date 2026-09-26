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
| `weighted_closure` | Response-adapted clock and weighted Legendre history projection, with matching initialization prefix | Any MLP; positive `order`; default `response` is the theorem's unscaled clock; `response_rms` and `residual` remain explicit alternatives |

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

Initialization uses a shared seed for matching models. The low-level `Flow`
constructor retains `hidden_gain=1, readout_std=null` for historical compatibility,
with stored readout standard deviation `1/n`. The config/CLI defaults now use
`hidden_gain="auto", readout_std=1` for practical fitting. `auto` uses gain 8
after sigmoid, and the `unit_moment` rule for other activations. The rule selects the
hidden-link gain from the preceding activation's Gaussian second moment using
128-node quadrature. `readout_std=1` supplies a width-independent stored readout
scale, with the same output and muP mobilities. These are explicit initialization
choices, not normalization layers. Historical dictionaries require the old law.

All methods share one CUDA-graph fitter. Existing methods and the
two trainable-factor methods use simultaneous Euler. Weighted history uses
Euler for network/source velocities and exact polynomial coordinate transport
for its moments and Gram matrix; see below. There is one host loss read per block.
The config/CLI default is `step=1/64, adaptive=true, block=8`, with target RMS
0.05 and a 110-second training cap. A block that increases RMS by more than 5%
or becomes nonfinite is restored and retried at half the step. Accepted decreases
regrow the step by 10%, up to the configured maximum. This reuses the existing
block loss check and one state backup; it is a fitting safeguard, not Euler
error estimation or a certificate of continuous-flow accuracy. `adaptive=false`
retains the original fixed stepping. The low-level `fit` API defaults remain fixed
for compatibility. No momentum, Adam, clipping or task-specific branch is used.
The solver records accepted steps, rejected blocks, actual physical time, capture time
and stop reason. Its wall-time cap includes capture but excludes initialization
and final test prediction. Stopping occurs at block endpoints. Float32 is the
explicit default; float64 is available; TF32 is disabled by the runner.

Use the explicit `fast_*` catalog entries for the fitting benchmark; older entries
retain their original settings. Per-run caps exclude initialization and final
query prediction, which are included in each record's `total_seconds`.
Training results and exceptions are recorded in the README validation block and
`data/generated/neural_response_memory_20260922/fast_fit01/`.

For **dense-versus-memory accuracy comparisons**, the `accuracy_*` catalog
entries also test maximum step **1/256**, applied to both models with the same
initialization and target RMS 0.05. This improved P3 on the tested depth-10/15/20
circle cases at two seeds and on six additional tasks, while shallow results
were mixed. Tightening the training target to 0.005 did not generally improve
query agreement. Keep P3 as the practical accuracy choice; low training loss
does not make P1 reliable on every task. The 82-configuration baseline sweep,
216 new bounded fits, capped cases and all parameter comparisons are recorded in
the README and `data/generated/neural_response_memory_20260922/response_accuracy01/`.
These are configuration results; the canonical implementation and its defaults
are unchanged by this accuracy sweep.

## Added methods and their clocks

`{"kind":"trainable_dictionary","basis":"dictionary_flow","order":3}` trains
the initialized bases as well as their cores. `basis` can also be
`dictionary_old`, `gaussian` or `orthogonal`; use `ranks` for random bases at
arbitrary depth. The existing frozen path computes the prediction and core
velocity. The additional basis velocity has mobility `n`; an intermediate
population basis receives both incoming and outgoing link gradients. These
are the original trainable-dictionary equations generalized link by link.
The historical frozen methods remain frozen.

Random Gaussian/orthogonal bases optionally support `rescale_core=true` (also
with trainable bases). At initialization only, each core is scaled so that its
preactivations on the supplied training inputs have RMS one. This uses no labels,
adds no normalization layer and leaves subsequent equations unchanged. It is an
explicit data-dependent initialization option, not the historical projected-core
law. Without it, rank-64 random projections nearly erase the signal across ten
layers; multiplying every core by width/rank instead can amplify it catastrophically
because intermediate bases are shared by incoming and outgoing links. Historical
dictionary formulas and their original random controls retain `rescale_core=false`.

`{"kind":"low_rank","rank":12}` retains each initialized dense matrix and
trains `A_l B_l`, with `A_l=0` and independent Gaussian `B_l` entries of standard
deviation `1/sqrt(rank)`. An integer rank applies to every hidden link; a list
specifies each link. Both factor mobilities are `1`; outer mobilities are `n`.
This preserves the original factor-control parameterization and physical time,
rather than silently rescaling it to accelerate optimization.

`{"kind":"weighted_closure","order":3,"clock":"response"}` implements the matching-prefix
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
the same weighted projection. `clock="response_rms"` instead uses the RMS of
the response derivative, removing the monitor's explicit square-root dependence
on the number of neuron/sample/link coordinates. This is a different clock
configuration, not an unchanged numerical implementation of the unscaled clock.
Both config/CLI and low-level defaults are now `response`, the theorem's
unscaled clock. Historical experiments with explicit `response_rms` retain it.
P1's physical model is clock independent; the fast P1 examples use `residual`
to avoid computing a response derivative that cannot affect their predictions.

The response derivative reuses cached forward/backward fields and propagates their
directional derivatives along the computed weight velocity. Built-in activation
curvatures use direct pointwise formulas; custom activations retain a pointwise
AD fallback. It constructs no Hessian, Jacobian or dense weight update.
The historical normalization API uses the full-traversal AD fallback. Each traversal
solves one `P x P` Gram system with all right-hand sides batched across links,
including the endpoint vector. It forms no inverse and performs no host error
check in the captured update. Moments, Gram and clock use float64; reconstructed
factors and all initialized-matrix actions use the network dtype. This protects
the small weighted projection from moment-rounding amplification. At exactly
zero residual the state is stationary. For
ReLU/SELU, derivatives follow the implementation's almost-everywhere convention;
the smooth-theory assumptions do not automatically extend across their kinks.

The weighted step transports the polynomial coordinates from `L` to `L+dt*g`
and adds the positive rank-one Gram contribution of the new history sample.
This avoids the indefinite Gram matrix that plain Euler can produce from basis
dilation alone. Each accepted update is a first-order explicit step; the optional
shared fitting guard chooses its size. There is no ridge regularizer. Checks
verify the stated ODE limit and physical clock derivative. The
response clock adds work compared with ordinary memory, and a tiny Gram can
still become ill-conditioned over a long run. No claim that the new method fits
faster or improves final RMS is made by these implementation checks. The fixed-depth
smooth-activation theorem is now given in `DEEP_ACTIVATION_ERROR_THEOREM.md`.
Run `--check-clock --out FRESH.json` for the isolated response-clock checks.

## Response-clock validation protocol (2026-09-26)

Compare the theorem's unscaled `clock="response"` with ordinary `closure`,
orders 1,2,3 and a freshly fitted dense reference. Preserve width 2048,
no normalization, seed 20260920, unit-moment hidden gain and readout std 1.
Use the existing quadrant-alternating, quadrant-pairs and outlier-alternating
circle data, 1024 full-circle queries, tanh depth 2 and GELU depth 3.
Shared maximum step 1/64, block guard, target training RMS 0.05; count
comparisons as fitted only if both models have RMS <=0.065. Main metrics:
full-circle RMS versus dense, training RMS, total seconds and moving-state bytes.
Practical success is fitting in <=120 seconds with test RMS <=0.1; retain all
failures and order reversals. This tests usefulness, not an asymptotic rate.

Before fitting, verify independent materialized-matrix reconstruction in both
orientations, response derivatives, zero residual, no internal layer, and the
step's first-order ODE limit. Run the 42-model panel with a 30-second per-fit
cap; permit one step-halved comparison for at most two groups with a numerical
failure or test RMS >0.1. Stop at 56 fits / 30 cumulative compute-minutes.
GPU execution is intended; any CPU fallback is labelled separately, without
claiming measured GPU performance. Outputs belong to
`data/generated/neural_response_memory_20260922/response_clock_validation01/`.
No test predictions enter training. Preserve initial snapshots and resolved
configs/source hashes, all capped fits, and actual device information.

### Completed response-clock comparison

All **49 GPU fits** reached training RMS <=0.05 (maximum 0.04998593):
42 main-panel models and seven models in the single GELU/quadrant step-halving
check. On two RTX 3090s with PyTorch 2.9.0+cu130 and TF32 off, new-clock total
model time was **2.07–10.05 seconds** in the main panel (median 3.77), and at
most **12.46 seconds** including refinement. Total summed model time was 177.89
seconds. Timings include initialization and queries, but exclude process startup.

Full-circle RMS versus the independently fitted dense network at maximum
step 1/64. P1–P3 are from the initial panel; P4/P5 are from the extension below,
whose fresh dense predictions and data were verified bitwise identical.

| Activation / depth | Task | Clock | P1 | P2 | P3 | P4 | P5 |
|---|---|---|---:|---:|---:|---:|---:|
| tanh / 2 | Alternating outliers | Old | 0.07250 | 0.04009 | 0.01674 | 0.00524 | 0.00123 |
| tanh / 2 | Alternating outliers | New | 0.07018 | 0.04901 | 0.01323 | 0.00786 | 0.00324 |
| tanh / 2 | Alternating quadrant | Old | 0.05417 | 0.06186 | 0.02388 | 0.00818 | 0.00658 |
| tanh / 2 | Alternating quadrant | New | 0.06552 | 0.09918 | 0.01283 | 0.00591 | 0.00346 |
| tanh / 2 | Paired quadrant | Old | 0.00566 | 0.00135 | 0.00056 | 0.00022 | 0.00007 |
| tanh / 2 | Paired quadrant | New | 0.00833 | 0.00124 | 0.00111 | 0.00032 | 0.00019 |
| gelu / 3 | Alternating outliers | Old | 0.44504 | 0.07570 | 0.00549 | 0.00207 | 0.00196 |
| gelu / 3 | Alternating outliers | New | 0.45472 | 0.11902 | 0.04500 | 0.00679 | 0.00098 |
| gelu / 3 | Alternating quadrant | Old | 2.98734 | 0.20941 | 0.11963 | 0.01469 | 0.01279 |
| gelu / 3 | Alternating quadrant | New | 3.06966 | 2.69207 | 1.24526 | 1.21472 | 0.99568 |
| gelu / 3 | Paired quadrant | Old | 0.08807 | 0.00574 | 0.00443 | 0.00149 | 0.00077 |
| gelu / 3 | Paired quadrant | New | 0.11162 | 0.00674 | 0.00157 | 0.00206 | 0.00016 |

The predeclared half-step check on GELU/alternating quadrant used a fresh dense
reference and the same data/initialization at 1/128. Including the P4/P5 extension:

| Clock | P1 | P2 | P3 | P4 | P5 |
|---|---:|---:|---:|---:|---:|
| Old | 2.99053 | 0.21233 | 0.11999 | 0.02364 | 0.02150 |
| New | 3.07505 | 2.90895 | 0.11200 | 0.22258 | 0.10313 |

Thus P3's large discrepancy is strongly step-sensitive; P1/P2 remain inaccurate
despite fitting. One refinement does not certify continuous-flow accuracy.
The new clock fits quickly and gives small P3 error on five main groups, but
does not uniformly outperform the activity clock or solve every low-order case.
The theoretical asymptotic rate is not an empirical low-order guarantee.

P3 moving state occupies 811,088 bytes at depth 2 and 1,597,520 at depth 3,
about 21x less than dense moving state. The initialized dense matrices and fixed
prefix vectors are retained separately; this is not a total-storage reduction.
Double-precision moments use more bytes than ordinary float32 history moments.

Validation: 694 CPU oracle assertions across 72 weighted cases, six width-2048
GPU capture/eager comparisons with zero state discrepancy, and runner/guard
checks. Tests cover all six built-ins, P1/P2/P3, depth 1/2/4, both matrix
orientations, exact zero residual, curvature, physical operator/clock derivatives,
and first-order step consistency. These checks do not prove a convergence rate.
The interrupted CPU pilot is retained separately and excluded from the GPU table.

Evidence: `response_clock_validation01/comparison.csv`, `summary.json`,
`check_gpu01.json`, `runner_guard01.json`, and per-run predictions/configs/hashes
under the study's generated-data directory. Each `--summarize` invocation
rechecks prediction/data hashes and recomputes RMS, timings and memory columns.
Reproduction from the repository root (fresh output paths required):

```sh
python -B studies/neural_response_memory_20260922/compact_flow.py --check-clock --gpu cuda:0 --out FRESH_CHECK.json
python -B studies/neural_response_memory_20260922/compact_flow.py --config studies/neural_response_memory_20260922/experiment_configs.json --experiment response_clock_tanh response_clock_gelu --device cuda:0 --out FRESH_RUN
python -B studies/neural_response_memory_20260922/compact_flow.py --config studies/neural_response_memory_20260922/experiment_configs.json --experiment response_clock_gelu_half_step --device cuda:0 --out FRESH_REFINEMENT
python -B studies/neural_response_memory_20260922/compact_flow.py --summarize FRESH_RUN
```

### P4/P5 extension protocol (2026-09-26)

User-requested continuation of the preceding table: run ordinary and unscaled
response-clock P4/P5 on the same six groups at 1/64 and the GELU/alternating
quadrant group at 1/128. Keep width 2048, architecture, initialization, seed,
data/query grids, guard and RMS target unchanged. Rerun one dense reference per
group and verify its predictions agree with the original reference before
combining P1–P3 and P4–P5. No solver changes or parameter search.

Budget: 35 fits, 30 seconds per fit, <=18 summed GPU-minutes. Stop after this
panel, retaining capped/nonfinite cases as failures rather than fitted comparisons.
Interpret fidelity only when both train RMS values are <=0.065; report the
strict 0.05 fit count too. Main observable remains 1024-query whole-circle RMS
versus dense, with timings and Gram condition reported. P4/P5 need not improve
monotonically. Save to `response_clock_p45_01/` under this study's generated data;
configs are `response_clock_p45_tanh`, `response_clock_p45_gelu` and
`response_clock_p45_gelu_half_step` in the same catalog. Before training, check
P4/P5 materialized-operator agreement and CUDA graph/eager consistency.

The extension completed **35/35 fits with training RMS <=0.05** (maximum
0.04997962). Total time per model was 0.94–11.49 seconds, median 2.53;
summed model time was 129.00 seconds. At P5, every main-table error is below
0.013 except the new-clock GELU/alternating quadrant case (0.99568).
Its smaller-step P5 error is 0.10313, still above the old clock's 0.02150.
Higher order generally helped, but the new clock does not dominate and has
order reversals (e.g. GELU paired quadrant at P4 and refined quadrant at P4).

All seven new dense references and all dataset/query arrays matched their
original counterparts bitwise. Eight P4/P5 operator/capture checks passed;
maximum explicit-operator discrepancy was 1.12e-16 and all GPU capture/eager
state discrepancies were zero. The canonical solver was unchanged at SHA-256
`e52fd395e26613e4a174b88cb8a9be0f742220c44b8a7d3ae419e556dc2b5a76`.
Evidence under `data/generated/neural_response_memory_20260922/response_clock_p45_01/`:
`comparison_p1_p5.csv` (70 closure comparisons), `new_runs.csv` (35 new fits),
`summary.json`, `operator_capture_check.json`, `table.md`, and per-run
prediction/config/provenance records. Source/data/prediction hashes and RMS
were checked with the canonical summarizer. These are internally checked
finite-step endpoint results, not a convergence-rate certificate.

Reproduce with the existing command and catalog, selecting
`--experiment response_clock_p45_tanh response_clock_p45_gelu response_clock_p45_gelu_half_step --device cuda:0 --out FRESH`.
Then use `--summarize FRESH` to rescore. P1–P3 remain in the preceding run
namespace; combine by activation, dataset, step, method and order after verifying
the dense-reference equality recorded in `summary.json`. The extension is complete;
no extra tuning or runs are queued.

### Broad new-clock sweep protocol (2026-09-26)

User-authorized extension to the exact 82 activation/depth/task configurations
in `response_accuracy01/sweep_table.csv`: ReLU, GELU, SELU, tanh, sigmoid and
SiLU; depths 2,3,4,6,10,15,20; six original circle tasks, deep circle cases,
high-frequency circle/sphere full/partial-support cases, and smooth spheres.
Clone their model and data configs, retain width 2048, seed 20260920, no
normalization, float32 network / float64 weighted history, TF32 off and 1024
query points. Compare a fresh dense model with new-clock P1/P2/P3; explicitly
use `clock="response"`, including for P1. Maximum step remains 1/64, with
the existing block guard and target training RMS 0.05.

Budget: 328 fits, 20 seconds per fit, 200,000 accepted steps per fit, two
GPU workers, no retries or tuning. The training cap bounds the total at
109.34 GPU-minutes plus initialization/query overhead; actual time is reported.
This shorter cap differs from several historical runs. A capped fit is not
evidence of a positive-loss floor. Stop after the declared panel.

Primary output: full-circle/full-sphere RMS of closure minus dense predictions
at their separately fitted/capped endpoints. Retain every numerical result;
flag `D` when dense train RMS exceeds 0.05 and `C` when closure train RMS
exceeds 0.05 (both flags may occur). Report actual training RMS, status and
runtime. Also retain the historical relaxed 0.065 eligibility flag for comparison,
but do not describe a relaxed pass as reaching the strict target. Rank aggregate
accuracy only on fitted pairs and disclose their counts; report poor fitted
comparisons separately from underfitting. P1/P2/P3 are not an asymptotic-rate test.

Configs are the `newclock_sweep_*` entries in the existing JSON catalog.
Generated outputs belong to `data/generated/neural_response_memory_20260922/newclock_sweep01/`.
Its schedule records the exact case-to-source mapping and GPU allocation.
The solver is unchanged from the previous verified implementation. No additional
Python engine or task-specific optimization is introduced.

Completed: all **82 cases / 328 fits** saved finite results, all 25 experiment
groups exited successfully, and the unchanged canonical summarizer recomputed
RMS from every saved prediction and verified the data/prediction hashes. Dense
reached training RMS <=0.05 in **79/82** cases; P1/P2/P3 in **70/82, 67/82,
66/82**. The other 46 fits hit the cap; 17 cases contain at least one miss.

| New-clock order | Fitted pairs / 82 | Median test RMS | 90th percentile | Maximum |
|---:|---:|---:|---:|---:|
| P1 | 70 | 0.042725 | 0.405369 | 3.661275 |
| P2 | 67 | 0.018895 | 0.179336 | 3.240721 |
| P3 | 66 | 0.006795 | 0.161205 | 1.362737 |

On the same 65 cases where all four models fit, the medians are
0.031467 / 0.013385 / 0.006579. The largest fitted P3 discrepancies are SiLU
depth3/alternating quadrant (1.362737), GELU depth3/alternating quadrant
(1.245256), and SELU depth2/alternating quadrant (0.369138). Thus good median
accuracy does not imply uniformly good low-order compression. This panel uses
the fixed shared 1/64 maximum step; the earlier GELU step-sensitivity finding
still applies, and these errors are not diagnosed as intrinsic closure floors.

Dense misses are ReLU depth10/high-frequency full circle (train RMS 0.125699),
ReLU depth10/high-frequency arc (0.117508), and SELU depth20/high-frequency arc
(0.116898). Closure misses additionally occur in sigmoid, deep nonsmooth
high-frequency cases, and two GELU depth15 sphere/order pairs. All are retained
and flagged in the [complete 82-row report](../../data/generated/neural_response_memory_20260922/newclock_sweep01/report.md).
The [wide CSV](../../data/generated/neural_response_memory_20260922/newclock_sweep01/sweep_table.csv)
contains every training/test RMS, D/C flag, stop status and runtime;
[all_runs.csv](../../data/generated/neural_response_memory_20260922/newclock_sweep01/all_runs.csv)
contains all 328 model rows, and
[summary.json](../../data/generated/neural_response_memory_20260922/newclock_sweep01/summary.json)
contains the aggregate checks and statistics. The relaxed 0.065 gate admits
only one additional model (SELU depth20/full-sphere P2, train RMS 0.051675).

Median total model time was **3.97 seconds**, range 0.18–22.35 seconds including
setup/final prediction; summed model time was 37.56 minutes over two concurrent
RTX 3090 workers (process startup excluded). PyTorch 2.9.0+cu130; solver SHA256
`e52fd395e26613e4a174b88cb8a9be0f742220c44b8a7d3ae419e556dc2b5a76`.
Root performed the checks; empirical, internally checked, no independent
promotion review. No tuning, solver changes or additional training is queued.

Reproduce the catalog entries listed in the run's `worker0_experiments.txt`
and `worker1_experiments.txt` with the canonical CLI, selecting `--device cuda:0`
or `cuda:1` and fresh output directories. Rescore each output directory with
`compact_flow.py --summarize <output/gpu0>` (likewise GPU1). Concatenate the two
`rms.csv` files; join dense/P1/P2/P3 by experiment/dataset and the frozen
`schedule.json.coverage`. D/C flags use train RMS >0.05; medians and linearly
interpolated 90th percentiles use only fitted pairs, with the common-case
summary requiring all four fits. Full resolved configs, commands, source hashes,
data and prediction arrays are preserved with each experiment.

## Saved experiment configs

`experiment_configs.json` contains editable examples for all six circle cases,
smooth sphere tasks with 16/64 samples, the four high-frequency/full/partial
support tasks, MNIST, and `additional_methods` for the three additions.
The `fast_*` entries reproduce the bounded fitting benchmark described in the
README; the older examples retain their historical settings. Select the examples
you intend to run:

```sh
python -B studies/neural_response_memory_20260922/compact_flow.py \
  --config studies/neural_response_memory_20260922/experiment_configs.json \
  --experiment fast_circle_relu \
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
  --summarize data/generated/neural_response_memory_20260922/my_run/fast_circle_relu
```

Query RMS compares final endpoints over the saved full query grid; it is not
an exact continuum integral or a same-physical-time trajectory comparison.
MNIST uses the saved official test panel, not a circle/sphere interpretation.

## Consolidation checks and historical preservation

The latest check is
[fast_fit01/final_gpu_check02.json](../../data/generated/neural_response_memory_20260922/fast_fit01/final_gpu_check02.json):
3,070 CPU assertions (2,136 existing plus 934 added), 72 weighted-history cases,
CPU/GPU guarded-step checks, 22 CUDA-graph/eager comparisons and historical
dictionary regressions, in 15.93 seconds. MNIST rows still reproduce bitwise;
all 35 catalog entries passed dataset preparation. The 266-run fitting benchmark
and its remaining eight RMS >0.065 cases are documented in the README and
[benchmark.csv](../../data/generated/neural_response_memory_20260922/fast_fit01/benchmark.csv).
The benchmark reached training RMS <=0.05 in 254/266 runs and <=0.065 in
258/266. Median total time was 1.73 seconds, the 90th percentile 17.74 seconds,
and the maximum 111.25 seconds, including setup and final prediction. Coverage
includes all six original circle tasks with six activations, selected depths
2/3/4/10/15/20, smooth sphere tasks and four 64-sample high-frequency tasks.
The eight larger misses are ordinary SELU depth-20 and weighted ReLU/SELU
depth-10 closures on the high-frequency arc. This tests representative
configurations, not a full Cartesian grid or a continuous-flow accuracy bound.
The aggregate uses exactly `circle_final`, `coverage_gpu0`, `final_gpu0` and
`final_gpu1` under `fast_fit01`, preserving all their failures. Earlier probes
remain separate. Source hashes and per-experiment counts are in
[benchmark_summary.json](../../data/generated/neural_response_memory_20260922/fast_fit01/benchmark_summary.json).

The cached-response/small-Gram optimization was compared for the same 128
fixed updates of depth-10, width-2048 ReLU weighted P3: 1.55x faster training
iterations, with zero query prediction RMS difference. See
[optimization_check.json](../../data/generated/neural_response_memory_20260922/fast_fit01/optimization_check.json).
This timing comparison is separate from changing initialization, step safeguards
or the response-clock configuration, which can change fitted trajectories.

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
