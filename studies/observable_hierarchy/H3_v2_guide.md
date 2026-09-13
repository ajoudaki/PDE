# Finite numerical observable closure

The solver integrates the autonomous nonlinear two-hidden-layer tanh closure
of C.4.7.10. It uses the bias-free model, Gaussian initialization, mobilities
(n,1,n), unhalved squared loss, and physical time. Population integration
points represent joint laws. The middle matrix indexes retained features;
there is no neural width argument or neuron-by-neuron middle matrix.

The library requires Python and NumPy. The optional bounded validation
supervisor additionally uses psutil on Linux. No external data, trained
surrogate, target trajectory, Gaussian-action service, or cached experiment
is needed for initialization or evolution.

## Supported laws and initialization

`ArcLaw(p,a,b,c,d)` accepts exact rational strings, integers or `Fraction`
parameters. It represents the mixture described in C.4.7.10: normalized input
U(s)=((1-s²)/(1+s²),2s/(1+s²)), labels +1 and -1, and a 3/5,4/5 rotation
for the second arc. Required ranges are 1/3<=p<=2/3 and
-1/20<=a<=b<=1/20, -1/20<=c<=d<=1/20. Degenerate intervals are atoms.
The mathematical model uses x=sqrt(2)u; all library input arrays contain u.
The proved numerical and population convergence scope is 0<=t<=1/200.
The family and this horizon are independent of every resolution parameter.

```python
from fractions import Fraction
from pde.observable_solver import (
    initialize, ArcLaw, evolve, predict, circle_inputs,
    paired_observations, save_restart, load_restart,
)

state = initialize(order=3, initialization_nodes=2048, population_nodes=1024)
data = ArcLaw().quadrature(nodes_per_arc=8, arithmetic=state.arithmetic)
final = evolve(state, data, steps=32, step_size=Fraction(1, 6400))
directions = circle_inputs(128, final.arithmetic)
prediction = predict(final, directions)
observations = paired_observations(final, data)
print(observations['rms1'], observations['rms2'])
```

`initialize` retains b1,g,w,p1 and b2,c,p2, one evolving matrix M and its
frozen initialization D, arithmetic settings and small metadata. Initially
w=g,c=0,M=D. All joint marks needed by the declared observations are retained.
It discards the Gaussian compiler and integration coefficient tables after
forming these arrays. Q=`initialization_nodes` determines coefficient/Gram
integration; P=`population_nodes` separately discretizes each full joint
mark law. It does not sample a Gaussian coordinate independently of the
other coordinates on its population.

Orders 1,3,5 have retained feature dimensions (5,3),(35,10),(128,21), with
strictly larger exact polynomial spans and new nonzero initialized action
couplings at each transition. Order 5 includes two redundant constant tail
words in addition to its 126 first-population polynomial features; the
declared syntax rule retains them. Odd degree choices avoid relying solely
on new even directions in an odd tanh trajectory. The polynomial core uses only four
and two independent Gaussian integration dimensions. Its initialized matrix
contains the reverse-to-forward response term. Higher orders also append an
exhaustive bounded-word prefix. Once that prefix introduces new actions,
initialization dispatches to the full joint Gaussian compiler; its cost may
grow substantially. Practical computation at every order is not promised.

`InitializationLimits` from `pde.observable_initialization` controls feature,
word, integration point, estimated work and estimated memory allowances.
`CompilerLimits` from `pde.observable_compiler` additionally controls generic
source-program resources. Pass an `InitializationLimits` instance through
`initialize(limits=...)`. Exceeding a limit raises an error without changing
the dictionary. Limits may be raised explicitly; they are resource controls,
not definitions of a capped hierarchy. Estimated bytes do not replace an
operating-system resource limit.

## Evolution and observations

`evolve` uses simultaneous explicit Heun updates of w,c,M and returns a fresh
state. The state has no absolute clock or growing history. Input blocks bound
temporary storage; set `block_size` on evolution, prediction and observation
calls. For a non-node time, `interpolate_state(left,right,fraction)` interpolates
the endpoints of one step on their identical frozen joint marks. This supplies
the continuous within-step convention used by the numerical theorem.

`predict(state, inputs)` evaluates any supplied circle directions directly
from the evolving nonlinear state. Its meaning is not restricted to an output
grid. A finite circle panel is a diagnostic, not a certified supremum estimate.

`paired_observations` returns `first_pairs` and `second_pairs`, each of shape
(population_nodes,input_nodes,2), with the last coordinate ordered as
(initial,current). The upper initial field is reconstructed using g and D
on the same frozen marks. The probability of a pair entry is the product
of its returned population weight and input weight. The returned `rms1,rms2`
are the square roots of the training-averaged squared paired displacements.
Use `include_pairs=False` to compute RMS values without retaining pair arrays.
`loss` and `rhs` expose the unhalved loss and complete nonlinear vector field
for diagnostics. Both directions use M and its actual transpose.

## Own-state restart

```python
from fractions import Fraction
from tempfile import TemporaryDirectory
from pathlib import Path

half = evolve(state, data, steps=16, step_size=Fraction(1, 6400))
with TemporaryDirectory() as directory:
    checkpoint = Path(directory) / 'observable_restart.json'
    save_restart(checkpoint, half, data)
    restored, restored_data = load_restart(checkpoint)
    continued = evolve(restored, restored_data,
                       steps=16, step_size=Fraction(1, 6400))
```

The JSON checkpoint contains all frozen/current joint arrays, both matrices,
the represented finite input rule and arithmetic metadata. It contains no
source program or history. Floats use hexadecimal values; Decimal values
use exact decimal strings; rational fixed-point values use hexadecimal integer
units. Loading does not redraw initialization. Continuing with identical
steps and arithmetic reproduces the working state exactly. This is own-state
restart, with convergence to the population restart proved separately.

## Precision and convergence

The default is float64. `digits=40` selects the practical Decimal backend.
`digits=36, backend='rational'` selects a slower integer/rational fixed-point
algorithm with no fixed library precision ceiling. The latter rounds every
basic operation to a multiple of 10^-digits and evaluates elementary functions
by finite rational series. Precision is retained in checkpoints. To avoid
freezing binary-float input errors during precision refinement, declare exact
parameters with integers, rational strings or `Fraction`.

Feature normalization uses the fixed positive ridge
eta_N=1/[1024(N+1)^2] and inverse Cholesky factors. No singular direction is
deleted. The generic source compiler additionally uses `epsilon_cov>0`;
this is an approximation removed in its own limit. The core initializer
does not need this source regularizer, and marks it unused. An unresolved
positive pivot, nonfinite state, invalid probability/input or exceeded
resource allowance raises an error. Increase declared precision or resources
explicitly; no automatic tolerance selection or convergence certificate is
provided.

At each fixed order, the proved numerical refinement removes arithmetic error
first, then time step, input quadrature, population quadrature, initialization
quadrature, and finally generic source regularization. Closure order is taken
to infinity after those limits. This is an iterated limit, not permission to
choose an arbitrary diagonal. Convergence is uniform in physical time and the
whole input circle, and includes the declared joint pairs and RMS motions.
Agreement between finite runs provides operational evidence only.

`DataLaw(inputs,labels,probabilities)` also permits exploratory finite circle
laws with finite labels; validate them with the state's arithmetic. Evolution
at other horizons or on broader inputs uses the same equations, but those uses
are outside the represented-family guarantee unless separately proved. There
is no implied general Borel-integration oracle.

## Bounded validation recipe

From the repository root, run the deterministic tests and the supplied
predeclared validation plan into fresh directories:

```text
PYTHONPATH=code OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B -m unittest discover -s code/tests -p 'test_observable*.py' -v
python -B code/scripts/run_observable_validation.py --plan code/validation/observable_solver_plan.json --output-dir data/established/observable_solver_check
PYTHONPATH=code OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B code/scripts/analyze_observable_solver.py --plan code/validation/observable_solver_plan.json --runs data/established/observable_solver_check --output data/established/observable_solver_analysis --recount-state
```

The twelve configurations cover two supported laws, odd orders 1,3,5,
a time-step refinement, a joint integration/time refinement, and a small
four-backend-resolution comparison. They use deterministic joint integration
points, so no random seed is needed. Each configuration includes a disk
restart and final paired observations. The plan fixes T=1/200, a 128-direction
output panel, one numerical thread, a 4 GiB process memory allowance,
20 CPU/wall minutes per configuration and one CPU hour for all workers.
The supervisor stops budget breaches and records failures without searching
for replacement parameters. Allow ten CPU minutes for deterministic tests.

Records include source hashes, configurations, environment, initialization,
evolution and observation timings, operating-system peak memory, retained-state
bytes, and diagnostics of the retained population-point feature Grams. These
condition diagnostics describe that particular finite rule; they are not
the raw initialization Grams or a conditioning guarantee. Observation archives
are rounded to float64 for analysis; exact working values remain in the JSON
checkpoints. The analysis verifies output hashes and reports all comparable
declared pairs. It does not compare with a supplied reference trajectory.

These checks establish operation at declared resolutions. Their differences
do not bound true prediction or hidden-motion error, do not demonstrate a
monotone convergence rate, and do not select a resolution for a tolerance.
