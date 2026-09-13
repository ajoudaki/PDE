## Observable computation through physical time 40

C.4.7.10 part D extends the same `observable_solver` and initialized-word
hierarchy through physical time 40 on a separate fixed supported family. The
bias-free two-hidden-layer tanh model, stored Gaussian variances
`(1,1/n,1/n²)`, mobilities `(n,1,n)`, unhalved squared loss and actual adjoint
are unchanged. Only the law module and time-40 validation/analysis interface
are added; the initializer, compiler, arithmetic, dictionary and integrator
are unchanged.

### Exact supported laws and integration

`pde.observable_laws` supplies `supported_radius()`, `supported_law()`,
`OrthogonalArcLaw`, `DyadicRadius`, `RationalRadius`, `IntegerExpression`
and `LawLimits`. The class name refers to the two reference axes, not to
orthogonality of its current support. Directions are normalized `u=x/sqrt(2)`.
The exact family uses equal label masses and rational intervals in `[-1,1]`,
mapped by `U(rho*s)=((1-(rho*s)^2)/(1+(rho*s)^2),2*rho*s/(1+(rho*s)^2))`
and its quarter-turn. A degenerate interval is an atom. The fixed exponent is
`E0=8192, E(j+1)=2**Ej` for ten steps and `rho=2**(-E10)`.

This example constructs a supported nonatomic law and its numerical input
rule without initialization or training:

```python
from pde.observable_arithmetic import Arithmetic
from pde.observable_laws import supported_law, OrthogonalArcLaw

law = supported_law(a="-1", b="1", c="-1/2", d="1")
description = law.exact_description()
assert OrthogonalArcLaw.from_description(description).exact_description() == description
data = law.quadrature(8, Arithmetic())
assert len(data.labels) == 16
```

`supported_law(a=0,b=0,c=1,d=1)` is a nonorthogonal two-atom law.
`quadrature(m, arithmetic, limits=..., allow_collapse=...)` uses `m` equal
midpoint nodes per nondegenerate interval and one per degenerate interval.
Input integration is separate from the initialized joint-population rule.
Its exact transport error is at most `rho/m`. `data.metadata` retains the exact
descriptor, quadrature, scope, rounding errors and collapse information.

The exponent has an eleven-node exact expression. At decimal precision `p`
the law routine may replace its radius by zero if `E10>4*(p+8)+2`; float64
uses `p=17` for this decision. Each input then changes by at most
`2*rho<10**(-p-8)`. This is an explicit numerical approximation, saved in
metadata. At the declared validation precisions the supported perturbations
all collapse: these runs demonstrate operation, not resolved perturbed-law
behavior. Their positive exact law description is retained.

`LawLimits` bounds expression size/depth, literal bits, exact scalar bits and
rule nodes. Requests that cannot be represented under supplied allowances
raise `LawResourceLimit`; `allow_collapse=False` rejects an unresolved radius.
For a fixed exact law, increasing precision eventually disables collapse, but
the denominator alone then needs `E10+1` bits. The convergence theorem permits
allowances to increase to admit each requested finite computation. Default
limits do not promise practical resolution of this extremely small radius.
Direct coordinate/weight rounding and any resulting collapse are recorded
separately; operational weights are not silently normalized.

`OrthogonalArcLaw(RationalRadius("1/20"), ...)` uses the same integration and
solver interface for wider arcs. It is exploratory; the time-40 theorem
does not apply simply because a run finishes. A user-supplied scope tag is
descriptive. The supported validation worker verifies the exact radius against
`supported_radius()` before assigning its supported scope.

### Qualitative limit and storage contract

For each fixed represented law and order, remove rational arithmetic error,
time mesh, input quadrature, population replay, initializer quadrature, then
generic source regularization, in that order. Finally let closure order tend
to infinity. The source regularizer is unused on the optimized core branch.
Part D proves uniform convergence on `[0,40]` and the full input circle,
uniform-time training-averaged initial/current pair laws in `W2`, their RMS
motions and risks. Finite-precision query outputs use the supremum norm;
exact limiting predictions are continuous. The method is deterministic.
Finite-network identification is separately in probability and retains the
actual finite random initial readout. An arbitrary simultaneous refinement or
tolerance-to-resolution rule is not asserted.

The same solver evolves `w,c,M`, retaining complete joint `b1,g,w` and
`b2,c` populations, both probability vectors and fixed contraction `D`.
For populations `P1,P2`, feature dimensions `d1,d2`, and `A` input nodes,
the retained numerical state has
`P1*(d1+5)+P2*(d2+2)+2*d1*d2` scalars and the finite law has `4*A`.
Part D.5 accounts separately for initialization tables/source programs,
coefficient contractions, Heun stages, input blocks, precision, exact law
descriptions and total runtime. Neither source programs nor observations
are fed into later dynamics. Stage storage stays bounded at a fixed
resolution; step counters require only their predeclared integer width.

### Maintained bounded recipe

Run from the repository or standalone edition root, into fresh directories:

```text
mkdir -p data/established
observable_test_scratch=$(mktemp -d "$PWD/data/established/observable_tests.XXXXXX")
env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 H4_LAW_TEST_SCRATCH="$observable_test_scratch" H4_VALIDATION_TEST_SCRATCH="$observable_test_scratch" TMPDIR="$observable_test_scratch" python -B -m unittest discover -s code/tests -p 'test_observable*.py' -v
python -B code/scripts/run_observable_validation.py --plan code/validation/observable_horizon_plan.json --worker validate_observable_horizon.py --output-dir data/established/observable_horizon_check
python -B code/scripts/analyze_observable_horizon.py --plan code/validation/observable_horizon_plan.json --runs data/established/observable_horizon_check --output data/established/observable_horizon_analysis
```

The setup creates fresh scratch inside this edition and supplies both required
test scratch settings and TMPDIR. Keep the resulting directory with the check
records. Allow 600 CPU seconds for deterministic tests. The time-40 plan fixes 14
configurations before execution: supported atomic and nonatomic cases at
orders 1,3,5; separate time, initialization, population and input-law
refinements; two resolved exploratory arc rules; and a small rational
24/36-digit comparison. It fixes one worker/thread, 1200 CPU/wall seconds
per configuration, 7200 cumulative CPU seconds, and 4 GiB process memory.
No random seed is needed for the deterministic joint integration. The
supervisor records and stops exceeded limits without parameter replacement.
Its optional `--worker` selects the new producer; omitting it preserves the
H3 default worker and original plan protocol. Sampled RSS monitoring is not
an operating-system memory reservation.

Each configuration starts from its prescribed initializer and completes its
own steps to time 40. The six observation times are `0,1/200,1,10,20,40` and
the output circle has 128 directions. At off-mesh times the worker observes
an affine interpolation of adjacent states and continues from the actual
right node. At 20 it saves its own complete current state and finite law,
continues to 40, then loads the checkpoint and repeats the remaining identical
steps. It compares all nine state arrays, three data arrays, metadata,
arithmetic and final prediction by exact scalar encoding. Plan and record
retain physical time, intended step, remaining steps and block size alongside
the serializer's complete state. Exact restart assumes the same backend and
reduction environment; no new initializer is called.

Records contain exact source/configuration hashes, environment, initialization,
evolution, observation, checkpoint and restart timings, peak RSS, retained
state/data bytes, exact law-description bytes and structural stage allowances.
Phase timings need not sum to total process time. Stage allowances and current
per-scalar byte estimates are distinct from measured RSS and temporary rational
arithmetic storage. Conditioning diagnostics concern retained P-node feature
Grams, which may be singular because no redundant feature is deleted. Their
null/status values disclose unresolved/infinite estimates; they are not
normalization-Gram or conditioning certificates.

Each saved NPZ contains float64 views of both `(initial,current)` pair arrays,
their population/data weights, input and circle directions, predictions,
labels, loss and RMS. A companion JSON preserves every working value: float
hexadecimal strings, exact Decimal strings, or hexadecimal fixed-point integer
units with the saved decimal scale. The analysis verifies hashes and independently
recomputes loss, paired RMS and moments. It reports all comparable declared
configurations. Agreement in a float64 view is not exact high-precision
agreement. These fixed panels/times do not certify whole-circle or time-uniform
accuracy, monotone order convergence or a target learning threshold.

### Recorded operation

The declared 14-configuration run completed with exact own-state restart in
every case. The worker CPU sum was 506.291 seconds; maximum process peak RSS
was 56,119,296 bytes (53.520 MiB). The full deterministic observable suite
contained 67 passing tests; the inherited exact rational check of the reference
learning constants also passed. These are operational and algebraic results.

Orders 1,3,5 use dimensions `(5,3)`, `(35,10)`, `(128,21)`. The baseline
supported runs used 1024 initializer nodes, 512 population nodes, 8000 steps
and float64; supported arc rules used eight nodes per component. The recorded
maximum prediction differences over saved times and the 128-direction panel
were `1.205e-6` on doubling the step count, `0.003274` on doubling initializer
nodes, and `0.01240` on doubling population nodes at order 3. The supported
input-rule refinement differs only at rounding level because the perturbation
collapses. Resolved radius-1/20 exploratory arc rules with eight and sixteen
nodes per component differed by `0.0002252` on that panel; no supported-flow
theorem is attached to this wider radius. The 24/36-digit tiny rational runs
agree in the reported float64 view; exact working observations are retained.

The maintained producer and analyzer regenerate the full configuration tables,
losses, paired observations, timing, memory and conditioning records. Their
numbers are empirical diagnostics, separate from part D's qualitative proof
and target substantial-learning conclusions.
