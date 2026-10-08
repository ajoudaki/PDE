# Finite-panel rollout implementation check

2026-10-08. Scoped internal implementation audit by the `rollout_source_audit`
subagent. This report concerns the empirical rollout compiler and the shared
autonomous runtime in `paper/figures/capture_trajectory.py`. It is not a
promotion review, a proof of the finite-panel theorem, or a reproduction of
the digit experiment. **PASS for the scoped implementation properties below:**
the three original findings and the two follow-on defects were repaired and
rechecked. No unresolved blocker remains within this audit's stated scope.

## Scope, provenance, and read coverage

The supervisor authorized only the implementation file and this study's
`RESULT.md`, `PANEL_SOURCE.md`, and `PANEL_RUNTIME.md` as scientific inputs,
plus tiny independent CPU checks. All three mathematical files were read
completely. In the implementation, the complete relevant definitions read
were `dense_fields`, `dense_rhs`, `Dense`, `integrate`, `validation_data`,
`trajectory_rms`, `_harmonic_source_basis`, `_harmonic_bss_metric`,
`_panel_coordinate_metric`, `Harmonic`, `harmonic_small_checks`,
`integrate_euler`, `finite_panel_rollout_sources`, `finite_panel_initial_jets`,
`FinitePanelCompression`, the finite-panel small checks, and both finite-panel
CLI drivers. Imports and dispatch were also inspected. Unrelated legacy,
LoRA, logarithmic, plot, and experiment implementations were not audited.

Required instructions read were the canonical-notation skill and its neural
response-memory reference, the conjecture-investigation skill and its
adversarial-audit and decisive-experiments references, `AGENTS.md`, and Part 1
of `RESEARCH_WORKFLOW.md`. The scoped assignment replaced ordinary author
startup reading. No study README, other study, linked outside dependency,
old-book passage, empirical result, or another reviewer's report was read.
The audit made no GPU call and loaded no digit dataset.

This is **not an isolated promotion review**: it was an implementation
subtask, the code owner received findings and repaired the live candidate,
and this same reviewer rechecked those repairs. The three supplied theory
files state inherited interfaces whose complete dependencies were outside
the assignment. Their truth was not freshly established here. Exposure to
the supervisor's bounded assignment and repair messages is disclosed; no
blindness claim is made.

Input SHA256 values:

| Input/version | SHA256 |
| --- | --- |
| Original audited implementation | `98e63465d4cce569b0a6df6a5fe4455dace96d9b90d6863b4a3cda5fac9e7e77` |
| First repair candidate | `53a12571644b303825eba28c411daa874be3a00af5ba8e9f9f5f0f624ff97be9` |
| Final pre-precision implementation | `d505c8c8df4d176afba2dda8a0366209f9635536b1b1f6872c4cf39aee4422ab` |
| Precision-option implementation, both checks passed | `3ad9b8bfe43c42fccca1e752c2aa0759ee2c98c3b1ec2a4313dc4c491e526eff` |
| `RESULT.md` | `38ca06a2e812d8e2b45c6b7350c0437d710433b11a00b89aa66487a9229b028b` |
| `PANEL_SOURCE.md` | `ca1066cf168829bea642db013a4fbc24166b224df0731783a51b4c85e4fdbaed` |
| `PANEL_RUNTIME.md` | `514d9e06cfd1cf23c496df0ece976812a39ea33f70112334c84326cfa0f0cd9f` |

The final tested implementation hash is given with the executed results.
Before the sole report edit, metadata-only checks gave HEAD
`99f6930d9b72c3e4fc4609aab897eed36894e7ab`, a modified implementation file,
no existing report at this path, and an empty staged-file list. This reviewer
does not own or stage the implementation. Only this report was written;
the supervisor remains the Git writer.

## Checked construction and claim boundary

The code uses two hidden tanh layers. In domain notation its moving state is
the selected first weights, selected hidden mixer, raw readout, and training
deficit. Only the training labels drive the ODE, with denominator equal to
the number of training examples. Passive inputs are available at compilation
and query evaluation but have no labels or residual coordinates in the
compiler or runtime. The driver loads its panel before creating the Gaussian
reference. The class's predeclaration diagnostic depends on this caller
contract; the constructor itself cannot establish when its inputs were chosen.

For each geometrically growing time interval, even Chebyshev nodes determine
the degree-limited coefficient blocks. Odd nodes appear only in interpolation
diagnostics; the SVD and coordinate trials do not select on those diagnostics.
A data-free perturbation check below directly tests this separation. The
source teacher itself is a numerical RK4 solve. Its time grid includes both
fit and audit nodes, so the audit is about excluded field values, not an
independently generated teacher trajectory.

Residualization respects the paired-image requirement. First-layer features
are projected only against initial training features, whose initialized
forward images are mandatory in layer two. Top-layer features may be
projected against the complete mandatory top-layer space because no further
forward image is required. First-layer responses may similarly use their
mandatory layer-one space because no lower hidden reverse image is required.
Top-layer responses are not projected against initial top-layer features:
their reverse images need not be mandatory. The initialized forward and
reverse images of retained vectors are then included before forming the
selected mixer. This preserves both orientations from one initialized map.

The randomized SVD uses a fixed seed per family, an oversampling allowance of
16, and two power iterations. Its residual diagnostics concern the retained
subspace and sampled fields, not an optimal-rank certificate. The corrected
rank filter is assessed below, including exactly zero backward sources.

The uniform coordinate selector tries four seeded candidate restrictions in
rollout mode and picks the smallest source-Gram condition number. With
source basis normalized in the dense neuron inner product, rescaling the
uniform diagonal metric makes the selected Gram eigenvalues lie in
`[1, kappa]`. The full correction gives exact source isometry in exact
arithmetic and a positive metric satisfying `D/kappa <= M <= D`. The inverse
formula is consistent with that correction. Thus reported `embedding_max`
is the Gram condition `kappa`, not the condition of the rectangular selected
basis. The empirical acceptance gate `kappa <= 16` is not the theorem's
factor-four hypothesis. The separate `bss_factor_four_satisfied` flag and
`certified_source_setup=False` preserve that distinction.

The corrected-readout and deficit equations agree with the supplied runtime
contract. A noninitial restart needs only the current four state arrays,
two metrics, the incoming metric inverse, training data, and evaluator.
The explicit test restores those tensors into an otherwise empty object and
compares both derivatives and passive predictions. No dense model, source
array, panel history, selected indices, or future predictions are needed.

`total_model_words` is the sum of deployable current-state tensors and fixed
metrics/inverse. Common inputs and training labels are reported separately.
It is not the all-retained bound in the theory: the benchmark also keeps
an initial-state copy, solver scratch, diagnostics, observations, and other
process objects. Dense trajectory samples and source bases are temporary
compilation objects and are absent from the deployable model. A process peak
is explicitly not an isolated model-memory measurement. Both storage and
setup cost must retain these qualifications in empirical comparisons.

## Original findings and repair history

1. **Interval-coverage reporting.** The original source diagnostic called its
   source the full physical interval regardless of the actual evaluation
   horizon. Source horizon and runtime horizon were independent; their
   defaults permitted an evaluation past the source endpoint. The first
   repair derives coverage from the loaded checkpoint's actual source
   diagnostics, rejects an explicit requested horizon beyond it, and records
   a warning if loss-stopped training passes it. The first repair still
   omitted this check from the aggregate summary; that follow-on was sent
   to the owner. Final disposition is recorded below. Autonomy does not fail
   when continuing beyond the source horizon; the unsupported claim is
   coverage by the compiled interval.

2. **Compiler provenance.** The original checkpoint did not store the
   compiler-source hash. A restored run's CLI configuration could suggest
   a different source mode, rank, or budget. The first repair stores the
   compiler hash/configuration in newly compiled checkpoints and reports
   effective source configuration from saved diagnostics. Old checkpoints
   produce explicit null compiler provenance rather than being assigned the
   current runtime source hash. This is an appropriate distinction; the
   missing historical hash remains missing.

3. **Null singular directions.** The original code retained a fixed number
   of left singular vectors without testing the singular values of the
   source matrix. On an exactly zero-label tiny example, both identically
   zero backward sources became rank-three orthonormal matrices. The later
   shared compiler saw their unit singular values and retained arbitrary
   directions. The first repair filters the original randomized-SVD
   singular values and reports the numerical rank within that subspace.
   Its source-only zero-label check correctly returned backward ranks zero.
   End-to-end compilation then exposed an empty-array `max()` in the shared
   truncation diagnostic. That follow-on was sent to the owner; final
   disposition is recorded below.

The first and second findings concerned coverage/provenance, not incorrect
ODE algebra. The third is a degenerate-input robustness issue, not evidence
against finite-panel compressibility or the studied nondegenerate task.

## Executed checks and reproducible command

All checks use CPU, one PyTorch thread, float64, fixed seeds, no data files,
and bytecode writes disabled. The verification contract is an algebra and
information-flow check, not a scientific performance experiment: changing
only held-out values must leave fitted subspaces unchanged; a noninitial
restart must reproduce derivatives and predictions; exactly zero backward
sources must retain zero directions and compile successfully. Tolerances
are stated in the assertions. No empirical accuracy hypothesis is inferred.

Original-version checks exited zero. Perturbing odd observations changed
held-out errors from roughly `1e-4` to `0.3--0.7`, while all four projector
differences were exactly zero. A genuine short rollout had initialized
forward/reverse pairing errors below `2.8e-16`; restarting at `t=0.1`
reproduced derivatives and query outputs exactly. The two realized metric
conditions were `1.7417630774867685` and `1.7360721566619364`, with positive
minimum eigenvalues. The original zero-label source-only check exited zero
and exposed spurious backward rank three.

At the first-repair hash, the zero-label source-only ranks were
`h1=1, h2=1, delta1=0, delta2=0`. The end-to-end extension exited one with
`RuntimeError: max(): Expected reduction dim to be specified for
input.numel() == 0` at the shared `max_coefficient_error` calculation.
This adverse outcome is retained rather than folded into the final pass.

Working directory: `/home/amir/Codes/PDE`. The exact final verification
command extracts and executes the following embedded program without
creating another file:

```bash
sed -n '/^# BEGIN AUDIT PROGRAM$/,/^# END AUDIT PROGRAM$/p' studies/finite_panel_absolute_compression_20261005/ROLLOUT_IMPLEMENTATION_CHECK.md | PYTHONDONTWRITEBYTECODE=1 /home/amir/Codes/sber-swap/.venv/bin/python -
```

```python
# BEGIN AUDIT PROGRAM
import hashlib, importlib.util, json, platform
import numpy as np
import torch

path = 'paper/figures/capture_trajectory.py'
with open(path, 'rb') as stream:
    before = hashlib.sha256(stream.read()).hexdigest()
spec = importlib.util.spec_from_file_location('capture_audit', path)
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)
inputs = torch.tensor([[1., 0.], [.6, .8], [-.8, .6]])
labels = torch.tensor([.3, -.2, .1])
queries = torch.tensor([[0., 1.], [-.6, -.8]])
panel = torch.cat((inputs, queries))
dense = c.Dense(72, 2, 913, 'cpu')

original_integrate = c.integrate
alter_odd = False
def artificial_integrate(model, inputs, labels, queries, times, step,
                         seconds, observer=None):
    for j, t in enumerate(times):
        state = [x.clone() for x in model.initial_state]
        state[0] += float(t*t)*.1
        state[1] += float(t)*.2
        state[2] += float(t)*.001
        if alter_odd and j % 2:
            state[0] += .35
            state[1] += .25
        observer(float(t), state)
    return state, np.zeros((len(times), len(queries))), dict(steps=0)

c.integrate = artificial_integrate
first, first_info = c.finite_panel_rollout_sources(
    dense, inputs, labels, panel, horizon=1., degree=3,
    source_rank=4, seconds=20)
alter_odd = True
second, second_info = c.finite_panel_rollout_sources(
    dense, inputs, labels, panel, horizon=1., degree=3,
    source_rank=4, seconds=20)
separation = {k: float((first[k]@first[k].T-second[k]@second[k].T)
                       .abs().max()) for k in first}
assert max(separation.values()) < 1e-12, separation
before_errors = {k: v['heldout_temporal_max_abs']
                 for k, v in first_info['source_checks'].items()}
after_errors = {k: v['heldout_temporal_max_abs']
                for k, v in second_info['source_checks'].items()}
assert any(after_errors[k] > before_errors[k]+.01 for k in first)
c.integrate = original_integrate

model = c.FinitePanelCompression(
    dense, inputs, labels, queries, budget=60, source_rank=3,
    source_mode='rollout', source_horizon=.2, source_step=.01,
    time_degree=3)
state, _, _ = c.integrate_euler(
    model, inputs, labels, queries, .002, 20, horizon=.1,
    observation_every=25)
restored = c.FinitePanelCompression.__new__(c.FinitePanelCompression)
restored.metrics = [x.clone() for x in model.metrics]
restored.metric_inverses = [x.clone() for x in model.metric_inverses]
restored.initial_state = [x.clone() for x in state]
restored.fixed_scalars = model.fixed_scalars
restart_rhs = max(float((x-y).abs().max()) for x, y in zip(
    model.rhs(state, inputs, labels),
    restored.rhs(restored.initial_state, inputs, labels)))
restart_query = float((model.predict(state, queries, inputs, labels)
    - restored.predict(restored.initial_state, queries, inputs, labels))
    .abs().max())
assert max(restart_rhs, restart_query) < 1e-12
assert not any(hasattr(model, k) for k in ('dense', 'sources', 'panel', 'queries'))
paired = {k: model.diagnostics[k] for k in (
    'initialized_gram_error', 'paired_forward_action_error',
    'paired_reverse_action_error')}
assert max(paired.values()) < 1e-11
metric_checks = []
for metric in model.metrics:
    values = torch.linalg.eigvalsh(metric)
    metric_checks.append(dict(min=float(values[0]),
        condition=float(values[-1]/values[0]), constant_norm=float(metric.sum())))
assert min(item['min'] for item in metric_checks) > 0
assert max(abs(item['constant_norm']-1) for item in metric_checks) < 1e-11

zero_dense = c.Dense(48, 2, 914, 'cpu')
zero_labels = torch.zeros(3)
zero_queries = torch.tensor([[0., 1.]])
zero_sources, zero_info = c.finite_panel_rollout_sources(
    zero_dense, inputs, zero_labels, torch.cat((inputs, zero_queries)),
    horizon=.1, step=.01, degree=2, source_rank=3, seconds=10)
assert zero_sources['delta1'].shape[1] == zero_sources['delta2'].shape[1] == 0
zero_model = c.FinitePanelCompression(
    zero_dense, inputs, zero_labels, zero_queries, budget=40, source_rank=3,
    source_mode='rollout', source_horizon=.1, source_step=.01, time_degree=2)
zero_rhs = max(float(x.abs().max()) for x in zero_model.rhs(
    zero_model.initial_state, inputs, zero_labels))
zero_prediction = float(zero_model.predict(
    zero_model.initial_state, zero_queries, inputs, zero_labels).abs().max())
assert zero_rhs == zero_prediction == 0
with open(path, 'rb') as stream:
    after = hashlib.sha256(stream.read()).hexdigest()
assert before == after, 'Implementation changed during verification'
print(json.dumps(dict(source_sha256=before, python=platform.python_version(),
    torch=torch.__version__, numpy=np.__version__, device='cpu', threads=1,
    heldout_projector_errors=separation, heldout_before=before_errors,
    heldout_after=after_errors, restart_rhs=restart_rhs,
    restart_prediction=restart_query, paired_errors=paired,
    metric_checks=metric_checks, zero_source_ranks={k: v['retained_rank']
        for k, v in zero_info['source_checks'].items()},
    zero_rhs=zero_rhs, zero_prediction=zero_prediction), indent=2))
# END AUDIT PROGRAM
```

The exact command above exited **zero** in approximately 1.59 seconds on
the final hash `d505c8c8df4d176afba2dda8a0366209f9635536b1b1f6872c4cf39aee4422ab`.
The program checked that the implementation hash was unchanged during its
execution. Environment: Python `3.10.12`, PyTorch `2.6.0+cu124`, NumPy
`1.26.4`; despite the CUDA-capable build, every tensor was on CPU.

Observed final output, with the already-recorded environment/hash omitted:

```json
{
  "heldout_projector_errors": {
    "h1": 0.0, "h2": 0.0, "delta1": 0.0, "delta2": 0.0
  },
  "heldout_before": {
    "h1": 0.00012183792272152383,
    "h2": 0.0007320284240691088,
    "delta1": 0.0003129597858127775,
    "delta2": 0.000384405176629507
  },
  "heldout_after": {
    "h1": 0.48040303479084373,
    "h2": 0.7434091082776852,
    "delta1": 0.430509314912295,
    "delta2": 0.30590804936938176
  },
  "restart_rhs": 0.0,
  "restart_prediction": 0.0,
  "paired_errors": {
    "initialized_gram_error": 2.0816681711721685e-16,
    "paired_forward_action_error": 2.393918396847994e-16,
    "paired_reverse_action_error": 2.7755575615628914e-16
  },
  "metric_checks": [
    {
      "min": 0.013888888888888883,
      "condition": 1.7417630774867685,
      "constant_norm": 1.0000000000000013
    },
    {
      "min": 0.013888888888888876,
      "condition": 1.7360721566619364,
      "constant_norm": 1.0000000000000007
    }
  ],
  "zero_source_ranks": {"h1": 1, "h2": 1, "delta1": 0, "delta2": 0},
  "zero_rhs": 0.0,
  "zero_prediction": 0.0
}
```

Static reinspection of that same hash confirms the shared compiler guards
the empty truncation-error maximum with `error.numel()`. The aggregate
summary checks both fine and coarse panel reports: if the saved source
method is the rollout compiler, it rejects `actual_horizon` greater than
that report's saved `source.horizon` (up to `1e-10`). This uses checkpoint
source facts, not the current command's source-horizon default. The driver
keeps the earlier explicit-horizon rejection and the warning for a
loss-stopped extrapolation. Therefore a warning remains available for such
an individual run, and the full-interval aggregate refuses to accept it.

New checkpoints store `compiler_source_sha256` and `compiler_config`;
restored runs expose both via `payload.get` and separately expose the
effective source diagnostics, requested compiled budget, actual selected
widths, and selector. Explicit nulls for older checkpoints correctly retain
the historical provenance limitation. The runtime implementation hash is
kept separate. These observations close the original scoped findings and
their follow-ons without changing the empirical/theoretical claim boundary.

## Limitations that remain regardless of test outcome

This check establishes implementation properties on inspected code and tiny
test cases, not empirical digit performance. It does not inspect or reproduce
any saved experiment. CUDA numerical behavior, large-source memory peaks,
and large training-Gram conditioning were not tested. The checkpoint's disk
serialization path was inspected; the restart test directly clones tensors
without a disk round trip. Coverage and compiler-provenance driver changes
are inspected statically rather than by running the data-loading CLI.

Temporal holdouts measure interpolation against the numerical teacher at
sampled times. They do not isolate teacher discretization error or prove a
continuous-time maximum error. Sampled source projection errors and runtime
query RMS are not the theorem's coordinate-uniform/all-time source bound.
The source integrates the dense teacher over its stated interval, so setup
cost and dense information used during compilation must remain explicit.
Autonomy after discarding that teacher does not make compilation inexpensive.

The mathematical source files supply a certified initialization-only
construction as a conditional theoretical interface. This measured rollout
compiler, rank truncation, and uniform selection are explicitly empirical
substitutions. None of the tests gives the logarithmic storage/accuracy
certificate or verifies its small-label and eventual-width hypotheses.
No finding here rules out the broader existence claim; no passing test
promotes the implementation to the established book or code.

## Addendum: disposable-teacher precision option

The supervisor subsequently requested a narrow check of `rollout_dtype`
(`source_dtype` in the constructor and `--source-dtype` in the driver).
Only that change and its plumbing were inspected; no empirical result was
read. The implementation at the start of this recheck had SHA256
`3ad9b8bfe43c42fccca1e752c2aa0759ee2c98c3b1ec2a4313dc4c491e526eff`.
Metadata-only checks before this addendum found HEAD
`0bcf8367e92c3c83bfd03ea1268b09688a748107`, a clean report path, and no
staged files. This reviewer still writes only this report and makes no
Git-index change.

The precision cast creates a disposable `Dense` teacher and matching copies
or views of the source inputs, labels, and panel. If no conversion is needed,
`Tensor.to` may alias the original initialization; this is safe here because
`integrate` clones its initial state before evolving it. When conversion is
needed, the original float64 tensors remain separate. The observer evaluates
both forward and backward source fields in the teacher precision. Before
Chebyshev coefficient assembly, each sampled family is converted back to the
original dense-initialization dtype. Mandatory features, mandatory weights,
initialized images, selected metrics and the compact initialization all
continue to use that original dtype. The CLI establishes it as float64;
the lower-level function preserves the caller's original dtype rather than
unconditionally forcing float64. Source diagnostics record both rollout and
assembly dtypes, and checkpoint compiler configuration records the option.

The test below fixes two teacher precisions on the same tiny float64
initialization. It verifies the actual teacher dtype, checks bitwise
preservation of original initialization and data, compares raw sampled fields
on identical observation times, and verifies float64 output/compact tensors
and initialized pairing after the float32 teacher. Raw field discrepancy
must be below `1e-4` in this tiny diagnostic; this threshold is a corruption
check, not a scientific float32 accuracy certificate. No requirement that
the rank-truncated bases be identical is imposed: casting the teacher can
change small singular directions.

Exact command, from `/home/amir/Codes/PDE`:

```bash
sed -n '/^# BEGIN PRECISION AUDIT$/,/^# END PRECISION AUDIT$/p' studies/finite_panel_absolute_compression_20261005/ROLLOUT_IMPLEMENTATION_CHECK.md | PYTHONDONTWRITEBYTECODE=1 /home/amir/Codes/sber-swap/.venv/bin/python -
```

```python
# BEGIN PRECISION AUDIT
import hashlib, importlib.util, json
import torch
path = 'paper/figures/capture_trajectory.py'
with open(path, 'rb') as stream:
    before = hashlib.sha256(stream.read()).hexdigest()
spec = importlib.util.spec_from_file_location('capture_precision_audit', path)
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)
inputs = torch.tensor([[1., 0.], [.6, .8], [-.8, .6]])
labels = torch.tensor([.3, -.2, .1])
queries = torch.tensor([[0., 1.], [-.6, -.8]])
panel = torch.cat((inputs, queries))
dense = c.Dense(72, 2, 915, 'cpu')
originals = [x.clone() for x in dense.initial_state]
data_before = [x.clone() for x in (inputs, labels, panel)]
actual_integrate = c.integrate
observations = {}
current_dtype = None
def capture_integrate(teacher, source_inputs, source_labels, source_queries,
                      times, step, seconds, observer=None):
    assert all(x.dtype == current_dtype for x in teacher.initial_state)
    assert all(x.dtype == current_dtype for x in
               (source_inputs, source_labels, source_queries))
    def capture(t, state):
        h1, h2, _ = c.dense_fields(state, panel.to(dtype=current_dtype))
        d2 = state[1][:, None]*(1-h2[:, :len(labels)].square())
        d1 = (state[2].T@d2)*(1-h1[:, :len(labels)].square())
        observations[current_dtype].append(
            (t, [v.to(torch.float64).clone() for v in (h1, h2, d1, d2)]))
        observer(t, state)
    return actual_integrate(teacher, source_inputs, source_labels,
        source_queries, times, step, seconds, observer=capture)
c.integrate = capture_integrate
metadata = {}
for current_dtype in (torch.float64, torch.float32):
    observations[current_dtype] = []
    sources, info = c.finite_panel_rollout_sources(
        dense, inputs, labels, panel, horizon=.5, step=.025,
        degree=3, source_rank=3, seconds=20, rollout_dtype=current_dtype)
    assert all(value.dtype == torch.float64 for value in sources.values())
    assert info['rollout_dtype'] == str(current_dtype)
    assert info['assembly_dtype'] == 'torch.float64'
    assert all(torch.equal(a, b) for a, b in zip(originals, dense.initial_state))
    assert all(torch.equal(a, b) for a, b in zip(data_before, (inputs, labels, panel)))
    metadata[str(current_dtype)] = {k: info[k] for k in
        ('rollout_dtype', 'assembly_dtype', 'source_observation_count')}
c.integrate = actual_integrate
differences = dict.fromkeys(('h1', 'h2', 'delta1', 'delta2'), 0.)
for left, right in zip(observations[torch.float64], observations[torch.float32]):
    assert left[0] == right[0]
    for name, a, b in zip(differences, left[1], right[1]):
        differences[name] = max(differences[name], float((a-b).abs().max()))
assert max(differences.values()) < 1e-4, differences
model = c.FinitePanelCompression(
    dense, inputs, labels, queries, budget=60, source_rank=3,
    source_mode='rollout', source_horizon=.5, source_step=.025,
    time_degree=3, source_dtype=torch.float32)
assert all(x.dtype == torch.float64 for x in
           model.initial_state+model.metrics+model.metric_inverses)
assert all(torch.equal(a, b) for a, b in zip(originals, dense.initial_state))
errors = {k: model.diagnostics[k] for k in (
    'initialized_gram_error', 'paired_forward_action_error',
    'paired_reverse_action_error')}
assert max(errors.values()) < 1e-11, errors
with open(path, 'rb') as stream:
    after = hashlib.sha256(stream.read()).hexdigest()
assert before == after, 'Implementation changed during verification'
print(json.dumps(dict(source_sha256=before, metadata=metadata,
    raw_field_float32_vs_float64_max_abs=differences,
    original_initialization_and_data_bitwise_unchanged=True,
    assembled_and_compact_dtype='torch.float64', paired_errors=errors), indent=2))
# END PRECISION AUDIT
```

The precision command exited **zero** in approximately 1.57 seconds at
`3ad9b8bfe43c42fccca1e752c2aa0759ee2c98c3b1ec2a4313dc4c491e526eff`.
The original embedded audit was also rerun by this reviewer on that hash;
it exited zero in approximately 1.56 seconds with the same numerical
results recorded above. Both commands independently checked that the
source hash stayed unchanged during execution. The environment and CPU
settings remained those recorded for the preceding check.

Observed precision-check results:

```json
{
  "source_sha256": "3ad9b8bfe43c42fccca1e752c2aa0759ee2c98c3b1ec2a4313dc4c491e526eff",
  "metadata": {
    "torch.float64": {
      "rollout_dtype": "torch.float64",
      "assembly_dtype": "torch.float64",
      "source_observation_count": 7
    },
    "torch.float32": {
      "rollout_dtype": "torch.float32",
      "assembly_dtype": "torch.float64",
      "source_observation_count": 7
    }
  },
  "raw_field_float32_vs_float64_max_abs": {
    "h1": 2.2030892266045043e-07,
    "h2": 4.918023416844441e-07,
    "delta1": 2.1629063699790674e-08,
    "delta2": 1.2856848020242895e-08
  },
  "original_initialization_and_data_bitwise_unchanged": true,
  "assembled_and_compact_dtype": "torch.float64",
  "paired_errors": {
    "initialized_gram_error": 8.326672684688674e-17,
    "paired_forward_action_error": 3.885780586188048e-16,
    "paired_reverse_action_error": 4.163336342344337e-16
  }
}
```

**PASS for the narrow precision change.** The tested original dense weights
and source data are bitwise unchanged; source assembly and compact tensors
remain float64 while the disposable solve actually uses the requested
precision. The float32 teacher rounds its copies of the float64 initial
weights and data, so its source error includes that rounding and subsequent
finite-precision integration. Converting sampled fields back to float64
does not recover the lost accuracy. The small observed difference here
does not certify full-horizon float32 source accuracy or GPU behavior.
That numerical claim remains separate from this mutation/dtype audit.
