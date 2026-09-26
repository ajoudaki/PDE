# General-dimensional p=1 and optional Torch computation

This independent first-order specialization and supplied-state backend accompany
[the complete coefficient and finite-equation proof](../docs/07-observable-closure.qmd#sec-docs-observable-p1-l1).
Use Python 3.10+ and NumPy; tensor operations additionally require PyTorch.
Ordinary `import pde` stays NumPy-only. Import the optional tensor modules
explicitly. Validation used NumPy 1.26.4 and Torch 2.9.0+cu130; other versions
may work but exact cross-version/device restart is not promised.

## Contract and first use

The order is p=1; P denotes population integration count, n denotes neural
width and d denotes input dimension. These are independent. All input rows
are U=x/sqrt(d), consumed directly with no whitening, row normalization or
extra dimension factor. Zero, repeated and nonunit finite rows are valid.
Labels are finite scalars. Data/population weights are nonnegative, have total
mass one within 2e-12 (float64) or 2e-6 (float32), and are never silently
renormalized. Zero weights are accepted. Integer dimensions/counts must be
positive, seed nonnegative; booleans are rejected. Steps are nonnegative
integers, and step size must be finite positive even at zero steps.

```python
import numpy as np
import torch
from pde.observable_torch_p1 import initialize_p1
from pde.finite_torch import NetworkEngine

U = np.array([[1.,0.,0.],[0.6,0.8,0.],[0.,0.,0.]])
y = np.array([1.,-1.,0.2])
engine, state = initialize_p1(3, 32, 17, population_rule="antithetic",
                               folded=True, device="cpu", block_size=2)
data = engine.prepare_data(U,y)
final = engine.evolve(state,data,steps=4,step_size=0.01)
observations = engine.observations(final,data,include_pairs=True)
assert observations["pairs1"].shape == (32,3,2)
network = NetworkEngine(3,32,17,device="cpu",block_size=2)
network_final = network.evolve(network.initial_state(),network.prepare_data(U,y),
                               steps=4,step_size=0.01)
print(engine.predict(final,U),network.predict(network_final,U))
```

The network is bias-free two-hidden tanh, Gaussian stored variances
(1,1/n,1/n²), output cᵀh2/n, unhalved weighted loss and physical mobilities
(n,1,n). Finite initialization comes directly from the canonical NumPy
`finite_network.initialize`, preserving draw order and the random readout.
The closure instead starts with c=0. Equal numerical seeds do not couple them.
Heun updates all three blocks simultaneously in each stage. It approximates
physical GF; it is not raw GD and a finite step need not decrease loss.

`pde.observable_p1_initialization.initialize(d,particles,seed,...)` requires
only NumPy. Its default is iid/unfolded. Scalar coefficient quadrature uses
128/256 normalized Gaussian-weighted Gauss–Legendre nodes on [-10,10], with
the larger rule supplying the working coefficients. `coefficients(...)`
exposes the constants and refinement metadata. Finer node counts at fixed
cutoff converge toward a truncated target; omitted Gaussian mass is not a
coefficient-error certificate. No accuracy/tolerance selector is supplied.

For antithetic even nominal P, P/2 independent lower joint marks and P/2
independent upper marks are drawn, with implicit or explicit negative partners.
Lower (G,R) dependence is retained; populations have no cross-index pairing.
Folded output uses only base rows and omits the invariant inactive constants.
This is not P iid draws. D has repeated initial bands; moving M stays fully
dense. The metadata records nominal/stored counts, sign status, constants,
ridge, seeds, quadrature and coefficient interpretation.

## Supplied states, data ownership and arithmetic

`ClosureEngine(b1,g,b2,D,p1=...,p2=...,device=...,dtype=...,block_size=...,
forward_mode=...,representation=...)` supports independent P1,P2,K1,K2,d.
Shapes are b1=(P1,K1), g=(P1,d), b2=(P2,K2), D=(K2,K1).
`initial_state()` returns w=g,c=0,M=D; `state(w,c,M)` accepts any matching
finite moving state. Generic supplied states default to an unfolded supplied
law, with no Gaussian or p=1 interpretation implied. A folded representation
must declare antithetic status, nominal count twice its equal stored counts,
and omitted constants; the caller declares that its base marks mean the full
odd extension. Arbitrary already-unfolded states cannot be folded blindly.

Construction copies all arrays. Prepared data copies input, label and weight
arrays. Moving states are editable and revalidated. Frozen engine tensors,
caches, and prepared data must not be edited, including through `.data`,
NumPy storage views or field replacement. Ordinary in-place tensor mutations
are detected by version checks at the next evaluation; deliberate bypass of
PyTorch version tracking violates the contract. Construct a new engine/data
object for changed marks or data; unsupported mutation cannot retain caches.
All public evaluations check shapes/dtypes/devices and boundary finiteness.
This validation may synchronize a CUDA device. Returned states and observations
own their arrays; zero-step evolution returns an independent copy.

Supported arithmetic is ordinary torch.float32/float64. TF32, float32 matmul
precision, deterministic-algorithm status, Torch version and device type are
recorded when the engine is constructed. Changing those settings requires a
new engine; the library does not change global Torch settings itself. For
reference checks disable TF32 and enable deterministic algorithms before
construction. Set CUBLAS_WORKSPACE_CONFIG=:4096:8 before starting CUDA Python.
Rounding, cancellation of 1-tanh² in saturation, underflow and intermediate
matrix overflow remain possible; nonfinite final evaluated results reject.
No extreme-range derivative or scaled-loss promise is inherited from NumPy.

`rhs(...,implementation="reference")` evaluates the displayed contractions;
`"optimized"` reuses buffers and may precontract matrices. `forward_mode` is
`"direct"`, `"folded"` (matrix association, unrelated to antithetic folding),
or `"auto"` (multiply-count choice). Reverse association uses the same cost
comparison automatically. Both retain full M/Mᵀ. Blocks partition a full
weighted sum and never update state between blocks. Associations/blocks can
change reduction rounding; no universal speed advantage is asserted.

## Observations and restart

`observations` supplies prediction, paired RMS, input rows/weights and, by
default, initial/current/cross activation Grams. `include_pairs=True` returns
`pairs1,pairs2` with last axis (initial,current), and `population_weights1,2`.
Folded observations explicitly unfold both signs with half base weights.
Multiplying population and input weights gives the finite signed joint law.
Set `include_grams=False,include_pairs=False` for bounded input-block storage.
The actual-network observation method returns the same keys, but retains a
whole panel while evaluating it. Finite panels provide no whole-domain bound.

```python
from pathlib import Path
from tempfile import TemporaryDirectory
from pde.observable_torch_p1 import ClosureEngine

with TemporaryDirectory() as directory:
    checkpoint = Path(directory)/"closure.npz"
    engine.save_restart(checkpoint,final,data,metadata={"time":0.04})
    restored, resumed, resumed_data, metadata = ClosureEngine.load_restart(checkpoint)
    continued = restored.evolve(resumed,resumed_data,steps=4,step_size=0.01)
assert metadata["time"] == 0.04
```

Archives are pickle-free NPZ, containing all frozen/current arrays, data and
required representation/arithmetic metadata. They contain no history or
initializer program. Loading requires the same recorded arithmetic policy and
device type, supplied by `device=`. Exact working continuation also requires
the same device/reduction environment, block size, association and steps; no
cross-platform bitwise claim is made. Time is caller metadata, not hidden
state. The optional network comparator exposes full current/initial arrays;
it does not add a network checkpoint schema.

`retained_bytes(state)` counts tensor entries in current/frozen arrays and
closure caches, without deduplicating transpose storage; it excludes data,
Heun stages, observations, Python metadata and allocator workspaces. See the
proof for full symbolic counts. Fixed-resolution state does not grow with
elapsed integration steps; prediction archives do.

## Comparison semantics

`pde.closure_comparison` takes explicit arrays and requires identical ordered,
unique integer/string IDs for per-image and Gram comparisons. It rejects
nonfinite/mismatched inputs. `prediction_metrics` reports absolute RMS,
relative RMS, worst absolute error, correlation and sign disagreements, plus
optional within-class metrics. Zero reference with nonzero error has null
relative error; identical zero vectors have relative error zero. Either
constant prediction vector gives null correlation. Explicit absent classes
return count zero and null real metrics. Sign(0)=0. `all_seed_pairs` retains
every candidate/reference pairing plus each candidate versus reference mean;
seed ranges are descriptive, not confidence intervals. `gram_metrics` compares
raw activation Grams without centering, normalization or calibration.

Norms scale entries before squaring; relative norms combine scale factors
without first forming a potentially overflowing or underflowing quotient.
Zero-reference and exact-zero-error decisions use the stored entries, and
constant detection uses original entries before centering. Correlations use
power-of-two scaling and subtract an anchor before centering. These calculations
handle ordinary finite float64 data near magnitudes 1e-200 and 1e200; large
representable RMS values do not require a representable unnormalized L2 norm.
Reference seed means are scaled separately for each sample and preserve exactly
constant columns, including subnormal constants.

These are floating calculations, not correctly rounded diagnostics or relative
accuracy certificates. Subnormal nonzero outputs may have large relative
rounding error. Nonzero norms/ratios/means that round to zero, nonfinite errors
or diagnostics, and unresolved nonconstant correlation variance raise ValueError
rather than being reported as exact zero. A reference seed mean also rejects
an exponent spread that erases a nonzero entry during scaling; zero correlation
with an underflowed nonzero normalized product is likewise rejected as
unresolved. Pointwise errors outside float64 range reject even if a normalized
ratio alone would fit. Conversion of a nonzero input entry to float64 zero
rejects. Correlation remains subject to ordinary dot-product cancellation,
and insignificant squared terms can underflow after norm scaling; no arbitrary
range or subnormal relative-accuracy guarantee is made.

`match_training_loss(times,losses,target)` uses only training losses. It selects
the nearest saved loss, earliest time on ties, reports actual mismatch and the
nearest lower/upper attained loss brackets. It refuses extrapolation; losses
need not be monotone. Compare predictions at both brackets to assess snapshot
sensitivity. Keep these distinct: equal physical time; independent stopping
rules; each closure matched to one fixed network reference loss; and every
system separately matched to one common attainable loss. None equates learned
maps or establishes a pure clock change. For binary data include within-class
metrics because overall correlation can mostly reflect separated labels.

## Standalone finite operation recipe

From an edition root, with explicit fresh destinations:

```sh
export PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 CUBLAS_WORKSPACE_CONFIG=:4096:8
PDE_TEST_DEVICE=cpu python -B code/tests/test_general_p1.py
python -B code/scripts/example_general_p1.py --output data/established/general_p1_a --device cpu
python -B code/scripts/example_general_p1.py --output data/established/general_p1_b --device cpu
python -B code/scripts/analyze_general_p1.py --run data/established/general_p1_a --repeat data/established/general_p1_b --output data/established/general_p1_analysis.json
```

The exported environment applies to all four commands. To run CUDA tests set
PDE_TEST_DEVICE=cuda:1; use `--device cuda:1` for the producer. CUDA examples
limit allocator use to 15% of a 24 GiB device (<4 GiB). Select an available
device explicitly. The fixed synthetic recipe uses d=3,m=9,n=P=16,seed=101,
10 Heun steps at .005, float64, one numerical thread, deterministic algorithms
and TF32 disabled. It writes source/output hashes, environment, arrays,
comparison diagnostics, timing and state-size counts. The analyzer independently
replays predictions/Grams with NumPy and checks optional repeat arrays exactly.
A supplied `--inputs input.npz` replaces synthetic data with explicit U,labels,ids;
that is a user-chosen finite run and not a predefined MNIST recipe.

The Linux producer records its 120-second work limit before input preparation
or training. It times closure initialization/transfer, network initialization/
transfer, data/working-state preparation, each integration, and observation/
analysis/checkpoint writing separately, with CUDA synchronization at phase
boundaries. `elapsed_integration_seconds` is the sum of the two integration
phases. `validation_work_seconds` includes input preparation through final
source/output hashing; it excludes interpreter/imports, device/policy setup,
and final JSON record/status writes. It is not a process end-to-end timer.
Peak RSS and CUDA allocated/reserved memory describe the whole process with
both systems retained, not isolated per-system peaks. Retained tensor counts
are separately reported. A process supervisor may record full command wall
time, including imports and final writes. None of these tiny operation timings
establishes relative speed, matched-accuracy speed, or a performance benchmark.

Tests use dense Cholesky, samplewise NumPy, independent autograd, the canonical
network oracle, nontrivial folded states, restart, float32 controls, zero/nonunit/
duplicate inputs, invalid/mutated boundaries and undefined comparison cases.
Run CPU and CUDA checks within 300/600 seconds respectively, one worker, and
retain failed output. These checks validate finite implementation and operation;
they supply no neural approximation, MNIST/PCA, timing ratio or accuracy claim.
