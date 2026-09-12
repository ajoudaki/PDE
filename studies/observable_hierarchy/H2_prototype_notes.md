# C-H2 executable prototype: API, numerical scope, and static checks

This study-owned implementation follows `H2_candidate_v2.md`. It has not been
promoted. Its exact mathematical inputs are the finite-population equations,
initial-word grammar, and Gaussian source/response rule stated in that candidate.
The prototype approximates the finite Gaussian integrals by deterministic tensor
Gauss–Hermite quadrature. It does not implement, sample, or initialize a dense
finite neural network, and its numerical checks do not prove the candidate theorem.

Files:

- `H2_prototype.py`: self-contained NumPy/standard-library module.
- `H2_test_prototype.py`: deterministic, static tests.
- `H2_prototype_notes.md`: this scope and API record.

The frozen independent first-route report was not changed. Only the candidate and
the complete `code/README.md` were read for this implementation task; no other
scientific source or route was fetched.

## Retained state and actual runtime equations

`State` contains the actual retained current populations, represented here by
quadrature nodes and their fixed probability weights:

| Coordinate | Storage | Role |
|---|---|---|
| First population | `first.b`, `first.g`, `first.w`, `first.probabilities` | Joint coordinates `(b,g,w)`; `b,g` are frozen marks and `w` moves at each quadrature node. |
| Second population | `second.b`, `second.c`, `second.probabilities` | Joint coordinates `(b,c)`; `b` is frozen and `c` moves at each quadrature node. |
| Current action | `M` | Finite matrix indexed by the two observable feature lists. |
| Initial action | `D` | Frozen contraction matrix, also used by frozen observations. |
| Fixed provenance | `metadata` | Hierarchy order, exact prescribed ridge, dictionaries, normalization matrices, quadrature order, and numerical source diagnostics. |

The numerical `w` and `c` arrays are not coefficient expansions in `b`. They are
the unrestricted characteristic values at the quadrature nodes. In particular,
the readout update is the candidate's unprojected update and no clipping appears.

For a columnwise batch of first-population values `V`, the only runtime forward
operation is

```text
b2 @ M @ (b1.T @ (probability1[:,None] * V)).
```

The reverse operation uses the same matrix transposed and the other probability
weights. Neither action calls the initialization compiler. `fields` exposes
`h1,a,z2,h2,delta2,d,q,f`; `rhs` returns the three velocities `w,c,M` in the
candidate's unhalved squared-loss clock. `loss` uses the supplied data probabilities.

`DataLaw` is a nonempty, finite weighted law on the unit circle with finite real
labels. Weights are nonnegative and must sum to one. This discrete data law is an
input restriction of the numerical API, not of the exact population theorem.
`fields` also evaluates arbitrary nonempty finite collections of two-dimensional
observation directions. It does not certify a supremum over the circle.

The state constructors own copies of their numeric inputs. Arrays remain mutable
for supplied-state calculations and finite differences. State coordinates and
probability weights are revalidated when evaluated; the data law is revalidated
by `loss`, `rhs`, and `save_restart`. Mutating frozen marks is a change of model,
not an evolution operation. The provided update only changes `w,c,M`.

## Initialization program and source responses

`decode_word(n)` implements the candidate's exact natural-number tree coding.
Invalid codes return `None`. `initial_dictionary(N)` adds the fixed pilot and
every valid code through `N`, keeps every bounded output in pilot-then-code order,
and retains duplicate dictionary entries. No empirical-rank decision is made.

`GaussianProgram.compile(words)` compiles a finite typed initial program containing
constants, `g1,g2`, rational scalings, additions, bounded products, `sin,cos,tanh`,
and actions on bounded operands. Identical action expressions share one named
source. The pilot has

```text
h_i = sin(g_i), z_i = A0 h_i, s_i = sin(z_i),
p_i = A0* s_i, t_i = tanh(p_i), i=1,2,
```

with constants in both populations. Each new action does the following:

1. Evaluate its bounded operand on the opposite population's current Gaussian
   rule, including all already declared response terms.
2. Form its uncentered variance and covariances with all prior operands in that
   orientation. These are quadrature approximations to the prescribed source Gram.
3. Evaluate its partial derivative with respect to **every named opposite source**.
   Each expected partial multiplies that earlier source's input field in the answer.
4. Add the new centered Gaussian source by conditional Gaussian extension, and
   retain its named derivative coordinate even if its innovation variance is zero.

The automatic derivatives hold the joint Gaussian law, source coordinates other
than the named one, and previously computed response coefficients fixed. They do
not differentiate the Gaussian square root, covariance, or a coefficient's own
expectation. This distinction is tested explicitly.

For the analytic pilot, put

```text
v = E sin(g)^2 = (1-exp(-2))/2,
alpha = E cos(z) = exp(-v/2),
s = E sin(z)^2 = (1-exp(-2v))/2.
```

Then the compiler has `p_i = R_i + alpha sin(g_i)`, with centered source variance
`s`, and

```text
E[sin(g_i) p_i] = E[z_i sin(z_i)] = alpha*v.
```

The first equality is a nonzero adjoint/Stein check that fails if the reverse
source is replaced by an independent Gaussian answer without its response.
The test also compiles `A0 tanh(p_1)` after the reverse calls and checks its new
response against the named partial `1-tanh(p_1)^2`.

`initialize` compiles the finite union of dictionary programs and all actions on
the raw first dictionary before extracting either joint mark law. It computes
the raw contraction matrix on that same upper-population rule, then applies the
two ridge normalizations. Thus `D` is formed from joint initial contractions,
not from independently sampled feature laws.

## Floating algebra and explicit resource limits

The exact ridge is `eta=2**(-N)`. `ridge_features` diagonalizes the positive matrix
`G+eta*I`, keeps every column, and retains every computed positive eigenmode.
Repeated and zero dictionary columns are supported. A nonpositive regularized
eigenvalue, unrepresentable ridge, or nonfinite numerical result raises
`NumericalInitializationError`; no adaptive rank or alternate ridge is substituted.
The floating eigensolver is not an interval certificate of the inverse square root.

The conditional Gaussian extension works with the previous source-to-independent-
Gaussian factor and a reduced QR solve. All existing independent Gaussian
directions are retained, including arbitrarily small positive ones. An exactly
zero innovation adds a named source coordinate without adding a quadrature
dimension; this represents an exactly degenerate Gaussian law rather than removal
of a dictionary feature. If a Schur complement is slightly negative within the
declared roundoff allowance, it is set to zero and the correction is explicitly
recorded. A larger negative Schur complement or unresolved covariance range is
rejected. No **positive** innovation is discarded. Near singularity can therefore
increase the cost through small positive floating innovations or cause rejection.

Default `QuadratureLimits`:

| Limit | Default | Meaning |
|---|---:|---|
| `order` | 5 | One-dimensional Gauss–Hermite order in every independent Gaussian coordinate. |
| `max_nodes` | 100000 | Maximum nodes of either population's tensor rule; checked before allocation. |
| `max_innovation_dimension` | 7 | Maximum total independent Gaussian dimension of a population, including the two initial `g` coordinates on population 1. |
| `max_named_sources` | 32 | Maximum number of action source names across both populations. |
| `roundoff_tolerance` | `2e-11` | Declared scale-adjusted covariance-range/negative-Schur floating allowance. |

`initial_dictionary` separately limits its natural-number prefix to 10000 codes
by default. The initializer rejects orders above 1074 before compilation because
their positive ridge is not representable in float64. Other, much smaller orders
can fail conditioning or source/quadrature resource limits. An oversized source
program raises `ResourceLimit` with its required dimension/node count. This is an
explicit stop, not a truncated initialization used under the original order name.
A failed program compilation may leave a partially compiled program object; do
not treat that object as the requested completed initialization.

At the default hierarchy order `N=1`, the initializer uses 6 first-population
features and 4 second-population features, with a `4 x 6` action matrix. The two
quadrature populations have 625 and 3125 nodes respectively. These node counts
are numerical integration costs, not hidden-layer widths. The default Gaussian
order is intentionally coarse. For example, its approximation to `E sin(g)^2`
is approximately `0.425679`, while the analytic value is approximately `0.432332`.
The analytic pilot checks use order 15 instead, within their declared node limit.

Source diagnostics record uncentered variances/covariances, response coefficients,
innovation variances, named-source and independent-dimension counts, range
residuals, and any negative-Schur roundoff correction. The actual numerical
`||D||` is recorded too. Quadrature errors can violate a bound known for the exact
canonical operator; the implementation neither rescales `D` nor presents such a
numerical violation as a theorem counterexample.

The module uses ordinary float64 operations. It provides no interval error bound,
validated positivity beyond its explicit checks, extreme-range arithmetic promise,
practical complexity estimate, or guarantee that increasing the Gaussian order
monotonically improves an answer. It also does not prove convergence when the
hierarchy order grows with a fixed quadrature rule. Approximation of a fixed
exact hierarchy order and convergence across hierarchy orders are separate limits.

## Observation and restart APIs

`observe(state, word)` evaluates a declared finite word using the current joint
populations. The available current seeds are `w1,w2,c`; the frozen seeds are
`g1,g2`. `frozen_z20(v)` uses the fixed `D` and the same frozen `g` coordinates.
An action node uses `M`, and a reverse action uses `M.T`. `joint_observe` returns
the coordinate matrix and probability weights of a nonempty same-population
tuple. It never couples independently sampled marginals. Bounded products and
nested action observations are supported without changing the evolving state.
The current readout's bounded type is a premise of the mathematical model; no
numerical clipping or fabricated common bound is imposed on a supplied state.

`save_restart(path,state,data)` writes the two current quadrature populations,
their frozen marks and probabilities, `M,D`, the fixed data law, and initialization
metadata to a NumPy archive. `load_restart` rejects unknown/missing fields and
loads without pickle. No source-program instance, raw dense matrix, trajectory,
time, or response history is needed to evaluate the restored RHS. The saved
initialization metadata describes the fixed model; it does not change at a restart.

`algebraic_update` performs one simultaneous map `state + step*velocity` of the
three moving blocks. It does not integrate a trajectory or promise energy
decrease for a nonzero step. Its sole Euler use in the tests is the one-step
state-map/restart check.

## Minimal API example

From the repository root, use the study folder on the import path:

```python
import sys
sys.path.insert(0, "studies/observable_hierarchy")
import H2_prototype as core

state, source_program = core.initialize(
    order=1,
    limits=core.QuadratureLimits(order=5, max_nodes=100000),
)
data = core.DataLaw(
    inputs=[[1.0, 0.0], [0.0, 1.0]],
    labels=[1.0, -1.0],
    probabilities=[0.5, 0.5],
)
initial_fields = core.fields(state, data.inputs)
velocity = core.rhs(state, data)
paired_values, paired_weights = core.joint_observe(
    state,
    [core.frozen_z20((1.0, 0.0)),
     core.action(core.unary("tanh", core.seed("w1")))],
)
# No training is needed to save and restore the current state.
core.save_restart("/tmp/h2-current-state.npz", state, data)
restored, restored_data = core.load_restart("/tmp/h2-current-state.npz")
restored_velocity = core.rhs(restored, restored_data)
```

The example shows calls only; the implementation task did not execute a training
trajectory. Its tests use study-owned temporary restart files and remove them.

## Validation performed

Run the study tests with:

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python -B studies/observable_hierarchy/H2_test_prototype.py
```

Thirteen deterministic static tests pass. They cover:

- Exact tree-code decoding, rational pairing, type rejection, and retained duplicates.
- Analytic pilot covariances, nonzero response/Stein pairing, named partials,
  and forward source reuse after a reverse call.
- Zero and singular Gaussian sources with named coordinates preserved; uncentered
  constant covariance; explicit quadrature/source resource stops.
- Singular, repeated, and zero-column dictionary ridge normalization without
  reducing feature count; ridge underflow rejection.
- Actual retained population initialization and both action directions, with
  unequal population and feature dimensions.
- Coordinate finite differences for every `M` entry and selected `w,c` coordinates,
  using the correct population-weighted gradients.
- The independent directional loss identity
  `dL/dt = -E1|w'|^2 - |M'|_F^2 - E2|c'|^2`, with all blocks nonzero.
- Same-population frozen/current tuples, readout products, and nested actions.
- One simultaneous Euler state map followed by bitwise-equal restarted fields
  and RHS, with no clock or history fields.
- Empty/invalid inputs, nonfinite states, and ownership of copied arrays.

The tests import the module by `H2_PROTOTYPE_MODULE`, defaulting to `H2_prototype`.
For a later reviewed relocation, the assembler can set
`H2_PROTOTYPE_MODULE=pde.observable_closure` without changing the scientific test
logic. `H2_TEST_SCRATCH` configures the temporary restart-file directory; its
default is the study-owned `data/generated/observable_hierarchy/H2_prototype/`.
The module imports neither maintained PDE code nor study history/data.

No convergence experiment, training integration, Monte Carlo, finite-network
comparison, theorem promotion selection, or independent-review verdict is part
of these results.
