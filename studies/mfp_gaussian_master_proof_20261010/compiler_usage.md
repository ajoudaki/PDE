# Using the symbolic MFP calculus

The study now has three entry points: the [operational rules](calculus_rulebook.md),
the [complete worked calculations](worked_examples.md), and the executable
[typed compiler](mfp_compiler.py). The compiler builds the Gaussian expectation
graph from an explicitly constructed finite program. It does not parse LaTeX or
natural language, and it does not perform numerical quadrature.

**Physical derivative expansion is exact at finite width. Gaussian compilation
returns the infinite-width limit.** For example, the identity-activation reuse
observable below has finite expectation `2 + 1/n`, although the Gaussian
compiler returns `2`. The [master proof](master_proof.md) supplies the convergence
claim under its assumptions; software tests check the implementation.

## Run the examples

Python 3.10 or later suffices. There are no third-party dependencies. From the
repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python studies/mfp_gaussian_master_proof_20261010/run_calculus_examples.py
PYTHONDONTWRITEBYTECODE=1 python studies/mfp_gaussian_master_proof_20261010/run_calculus_examples.py --example reuse --json
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s studies/mfp_gaussian_master_proof_20261010 -p 'test_mfp_*.py' -v
```

The JSON contains integrands, coordinate lists, covariance matrices, the output
expression, vector/scalar representatives, named source covariances and applied
rules. Sources remain named even when their covariance is singular. The finite
trace records the builder's transformation history; the Gaussian trace records
the dependency traversal for the requested output.

## Construct a formula

Place this study on `PYTHONPATH`, or run a script in its directory:

```python
from mfp_compiler import Program

p = Program()
lower = p.vector_type("lower")
upper = p.vector_type("upper")
W = p.matrix("W", lower, upper)       # actual entries N(0, 1/n)
z = W @ p.one(lower)
v = W.T @ p.phi(z)
J = p.inner(v, v)                    # v.T v / n
dag = p.compile(J, preactivations=[z])
print(dag.formula())
```

The answer is

```text
I_1 = E[phi(g_W_F_1)^2],  g_W_F_1 ~ N(0,1)
I_2 = E[phi^(1)(g_W_F_1)], g_W_F_1 ~ N(0,1)
output = I_1 + I_2^2
```

`p.phi(u, order=r)` represents the actual derivative `phi^(r)(u)` of the same
activation. Smoothness and polynomial growth of every derivative are the
caller's mathematical contract; the program cannot infer them from a name.
Polynomial activations can instead be written directly, such as `z**3`, in
which case Gaussian polynomial integrals are evaluated exactly by Wick's rule.

`p.compile(J)` accepts the general admitted nonlinear language, including
nested activation compositions. Supplying `preactivations=[...]` requests the
restricted activation-moment form: every reachable nonlinear argument must be
one of those literal vector nodes, and each designated representative must be
a centered Gaussian linear expression. A violation raises `ProgramError`.
The caller identifies the original initialization preactivations; the compiler
checks the stated syntactic and Gaussian conditions, not an inferred network
architecture. Linear first-layer combinations receive auxiliary Gaussian
coordinates for integration only. Formal response derivatives continue to use
the original named sources.

## Input language and normalization

| Construction | Meaning |
| --- | --- |
| `p.vector_type(name)` | A population of width `n`; distinct type labels are not interchangeable |
| `p.root(name, kind, variance=1, mean=0)` | One iid Gaussian vector independent of other root declarations |
| `p.roots(kind, names, covariance, means=None)` | A jointly Gaussian tuple iid over neurons; singular covariance allowed |
| `p.parameter(name)` | A deterministic scalar parameter, fixed as width grows |
| `p.broadcast(s, kind)` | Constant-coordinate vector with scalar value `s` |
| `u+v`, `u*v`, `u**r` | Sums, coordinate products and nonnegative integer powers; scalars broadcast |
| `p.phi(u, r)` | Coordinate activation derivative, for a vector `u` |
| `p.mean(u)` | The scalar `sum(u_i)/n` |
| `p.inner(u,v)` | The scalar `u.T v/n`, requiring matching vector types |
| `W @ u`, `W.T @ v` | Forward/transpose calls to one named matrix |
| `p.rank_one(u,v,c)` | The matrix `c*u*v.T/n`, from the type of `v` to that of `u` |
| `W + p.rank_one(...)` | Initialized base plus represented updates |
| `p.frobenius(A,B)` | Exact Frobenius product of two pure represented matrix directions |

Multiple root declarations are independent. Use a **single** `roots` call to
declare correlations within one type. All types have the same width. Matrices
must connect distinct types. A second `matrix` call cannot reuse an existing
name; retain the original object for shared parameters. No operation substitutes
an independently sampled transpose.

Numbers may be integers, `fractions.Fraction`, or finite floats. Floats are
interpreted as the exact decimal rational `Fraction(str(value))`; the symbolic
engine then uses rational arithmetic. Root means and covariance entries are
concrete numeric inputs. Root covariance symmetry and positive semidefiniteness
are checked exactly, including zero pivots. Abstract fixed real coefficients
can be scalar parameter nodes. Symbolic root-covariance families are not a
front-end feature; instantiate a concrete covariance for each calculation.

An arbitrary coordinate expression is assembled from the elementary nodes.
For example, `p.phi(u*v+s, 2) * w` builds a product of an activation derivative
and a same-type vector. For a nonlinear scalar feedback value, use
`p.mean(p.phi(p.broadcast(s, kind)))`; its limit is recorded as a
zero-dimensional Gaussian expectation when appropriate. This preserves the
polynomial assembly of the final result from expectation nodes.

The public builders reject cross-type products, arrays used as symbolic
expressions, strings used as formulas, duplicate names, nonconstant division,
negative/fractional powers, dense matrix directions and unsupported covariance
data. No coordinate-selection, inverse, unrestricted tensor contraction or
width-dependent normalization primitive is provided. Fixed depth, order,
update count and coefficients remain mathematical assumptions: naming a scalar
`n` does not make a width-dependent choice admissible.

## Physical derivatives, jets and moving directions

`p.directional(O, directions)` computes one exact Fréchet derivative of an
ordinary primal graph. Explicitly frozen seed data are held fixed, as detailed
below. Its dictionary keys are vector-root nodes, deterministic scalar
parameter nodes, or named matrix parameters. Vector/scalar directions are
matching expression nodes; matrix directions are pure represented rank sums.
The directions are evaluated at the base point and held fixed for that one
derivative.

```python
neurons = p.vector_type("neurons")
x = p.root("x", neurons)
O = p.mean(x**2)
V = -(x**3)
ordinary = p.derivatives(O, {x: V}, order=2, moving=False)
flow = p.derivatives(O, {x: V}, order=2, moving=True)
print(p.compile(ordinary[2]).output)  # 30
print(p.compile(flow[2]).output)      # 120
```

`moving=False` freezes directions across repeated differentiation, giving
derivatives on the straight path `x+t*V(x)` with its initial `V(x)` held fixed.
`moving=True` repeatedly differentiates along the state-dependent field and
includes its motion. At second order it computes

\[
D^2O[V,V]+DO[DV[V]].
\]

The API returns derivatives `0,...,order`. `p.jets(...)` instead divides entry
`r` by `r!`. No infinite series is constructed or claimed to converge.
For prescribed general finite paths, use

```python
coefficients = {x: (a, b)}
jet = p.curve_jets(O, coefficients, order=2)
```

where `a,b` are matching nodes and the path is `x(t)=x+t*a+t**2*b`.
The supplied values are already factorial-normalized path coefficients and
are fixed along the auxiliary path, even if constructed from the base state.
Matrix path coefficients must be pure rank sums. Mixed fixed-direction
derivatives can be built by successive `directional` calls using explicitly
`p.freeze`d direction expressions.

`freeze` declares **independent seed data** whose numerical values are taken
from the base state. It is intended for direction conventions. Physical AD
holds those declared data fixed; finite evaluation and Gaussian compilation
retain their values and dependencies. For example, `p.mean(p.freeze(x)**2)`
has the value of `p.mean(x**2)`, but its derivative with respect to `x` is zero
under the declared frozen-data convention. It is therefore not the ordinary
derivative of the latter primal observable. Do not insert `freeze` inside a
network and claim its unmodified parameter derivative. With frozen nodes,
the exact derivative claim concerns the partial derivative on the enlarged
space of parameters and independent seed data, followed by evaluation at the
specified base-state seed values. Formal Gaussian source differentiation still
follows the seed expressions' explicit source dependence.

## Gradients and updates

For a scalar loss template `loss`,

```python
g = p.gradient(loss, vectors=[x], matrices=[W])
```

returns `g[x]=n*grad_x(loss)` and `g[W]=grad_W(loss)`. The latter is a sum
of normalized outer products. Contributions from every shared parameter use,
including transpose calls, are accumulated. Optional `scalars=[s]` returns
ordinary scalar gradients. To build a gradient-flow field with fixed block
multipliers, use `{x: -kappa_x*g[x], W: -kappa_W*g[W]}` with `moving=True`.

The finite update helper is

```python
state = p.gradient_descent(loss, vectors=[x], matrices=[W],
                           steps=2, step_size=eta)
updated_observable = p.at(O, state)
dag = p.compile(updated_observable)
```

The loss is a template in the **current ambient parameters**. Its gradient is
computed before substituting any update factors. Updates are simultaneous;
`at` inserts the supplied states without revisiting their expressions. Vector
mobility is `n`, matrix mobility is `1`, and `mobilities={parameter: kappa}`
supplies additional fixed block factors. The step size and factors must be
fixed deterministic coefficients for this optimizer helper; use explicit
program arithmetic for a different admitted update rule.

If the requested object is a derivative *through the training history*, first
construct `updated_observable` and then differentiate that graph. This computes
the history pullback. It is distinct from the current ambient gradient used
to take each training step.

## Inspect or evaluate the result

`dag.expectations` is an ordered tuple. Each entry has a named scalar symbol,
integrand, Gaussian coordinate tuple, full covariance matrix, and vector type.
Every covariance and integrand refers only to earlier expectation values and
fixed deterministic parameters. `dag.output` is the final scalar expression.
`dag.formula()` renders shared expectations once; `dag.to_dict()` produces a
JSON-ready representation. `dag.sources` preserves each named source and its
covariances, including duplicate calls with correlation one.

There are two derivative engines, intentionally separated in code:

- `Program.directional` and `Program.gradient` operate on the finite typed
  graph and propagate through means, feedback and parameter reuse.
- `mfp_expr.diff` operates on named scalar sources inside the Gaussian
  compiler. Other symbols, including expectation coefficients, remain fixed.

The scalar kernel uses exact polynomial algebra and terminating Wick/Stein
reduction for flat activation moments. General nested nonlinear integrals
remain as integrals. Integrating such an atom requires a separately chosen
quadrature or sampling method; this package does not silently choose one.

The independent [finite interpreter](mfp_finite.py) evaluates supplied arrays
at a particular width. It takes the matrices' **actual stored entries**, not
unscaled samples, and never substitutes Gaussian limiting laws. The tests use
it with rational arrays and separate polynomial/dense formulas to check exact
derivative, gradient, contraction and update identities. It is also useful for
checking a newly constructed expression at small width.

## Implementation scope

This is a study prototype implementing the theorem's primitive operations and
the explicit derivative constructions above. It is not a theorem prover or a
general computer-algebra system. Its root-covariance input is concrete, its
activation is one formally named function, and its formula output is plain
text/JSON. No depth-linear complexity guarantee is claimed: expansion and
higher derivatives can become large, and ordinary Python resource limits apply.
No Gaussian integral is replaced by an unreported numerical approximation.
