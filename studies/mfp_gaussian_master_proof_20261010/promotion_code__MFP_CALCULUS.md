# Symbolic mean-field peeling calculus

`pde.mfp_compiler` builds a finite typed program, differentiates it at finite
width, and compiles its scalar output to a Gaussian expectation graph. Import
it explicitly; its names are not added to `pde`'s top-level exports. The
[finite-program theorem](../docs/02-gaussian-reuse.qmd#sec-mfp-finite-derivative-programs)
supplies the width-limit justification under its stated assumptions. Software
tests check the implementation, not that theorem.

**Physical differentiation is exact at finite width. Gaussian compilation
returns the infinite-width limit.** For example, the identity-activation reuse
observable below has finite expectation `2 + 1/n`, whereas `compile` returns
`2`. No numerical sampling or quadrature is performed. General activation
integrals remain explicit integrals.

Use Python 3.10+ and the maintained package's NumPy dependency. These three new
modules themselves use only the standard library; importing their parent `pde`
also imports its existing NumPy finite-network API. From the edition root:

```sh
PYTHONPATH=code python -B code/scripts/example_mfp_calculus.py
PYTHONPATH=code python -B code/scripts/example_mfp_mlp_derivative.py
PYTHONPATH=code python -B code/scripts/example_mfp_kernel_jets.py --activation identity
PYTHONPATH=code python -B -m unittest discover -s code/tests -p 'test_mfp_*.py' -v
```

The scripts print text by default and accept `--json`. To regenerate all three
kernel-jet variants into a fresh, explicitly chosen directory:

```sh
PYTHONPATH=code python -B code/scripts/example_mfp_kernel_jets.py --activation all --output-dir data/established/mfp_kernel_jets_01
```

The directory must not exist. It receives complete text formulas, JSON graphs,
and a manifest with source/output hashes and Python/platform information. The
producer reads no historical output, study files or Git metadata. The default
jet order is two; larger fixed orders are permitted but can grow very expensive.

## Construct a reusable-transpose observable

A named matrix has iid Gaussian entries of variance `1/n`. Calls to `W.T` use
the same parameter as calls to `W`. Both types have width `n`.

```python
from pde.mfp_compiler import Program

p = Program()
lower, upper = p.vector_type("lower"), p.vector_type("upper")
W = p.matrix("W", lower, upper)
z = W @ p.one(lower)
v = W.T @ p.phi(z)
dag = p.compile(p.inner(v, v), preactivations=[z])
print(dag.formula())
```

For a standard Gaussian scalar `Z`, the returned limit is
`E[phi(Z)**2] + E[phi'(Z)]**2`. The second term is the response caused by
matrix reuse. With a polynomial coordinate expression such as `v = W.T @ z**3`,
all Gaussian moments reduce exactly and the output is `24`.

`p.phi(u, order=r)` is the actual derivative `phi^(r)(u)` of one named
activation. Assume `phi` is smooth and every derivative has polynomial growth.
This analytic condition is the caller's obligation, not something inferred from
a name or callback. Arbitrary admitted compositions can be compiled without
`preactivations`. Specifying that argument requests the restricted
initialization activation-moment form: each reachable `phi` argument must be
one of those literal nodes, and every designated reachable representative must
be a centered Gaussian linear expression. The compiler checks these conditions;
the caller identifies the original initialization preactivations. It does not
infer the network architecture. A shifted or nonlinear designated argument is
rejected. Linear combinations receive auxiliary integration coordinates; formal
source derivatives still use the original named sources.

## Typed operations and input conventions

| Construction | Meaning |
| --- | --- |
| `p.vector_type(name)` | A named population of width `n` |
| `p.root(name, kind, variance=1, mean=0)` | An iid Gaussian vector independent of other root declarations |
| `p.roots(kind, names, covariance, means=None)` | One jointly Gaussian tuple per neuron, allowing singular covariance |
| `p.parameter(name)` | A fixed deterministic real scalar, available to physical AD |
| `p.broadcast(s, kind)` | The constant-coordinate vector with value `s` |
| `u+v`, `u*v`, `u**r` | Addition, coordinate product and nonnegative integer power; scalars broadcast |
| `p.phi(u, r)` | A coordinatewise activation derivative |
| `p.mean(u)`, `p.inner(u,v)` | `sum(u_i)/n` and `u.T v/n`; pairings require the same type |
| `W @ u`, `W.T @ v` | Both orientations of the same named matrix |
| `p.rank_one(u,v,c)` | `c*u*v.T/n`, from the type of `v` to that of `u` |
| `W + p.rank_one(...)` | One initialized base plus a finite represented update sum |
| `p.frobenius(A,B)` | Exact Frobenius product of two pure represented matrix directions |

All vector types have equal width. Named matrices connect distinct types.
Retain the original object for shared parameters: duplicate parameter names
are rejected. Separate root declarations are independent, including separate
calls of `roots`; use a single call for correlations within one type.

Constants accept Python integers, `Fraction`, and finite floats. A float is
interpreted as the exact decimal rational `Fraction(str(value))`. All later
symbolic constant arithmetic is rational; arithmetic already evaluated by Python
before entering the builder is outside that guarantee. Root means and covariance
entries are concrete numbers. Covariance symmetry and positive semidefiniteness
are checked exactly, including singular laws and zero pivots.

The frontend does not accept symbolic covariance matrices. Symbolic fixed
geometry can instead be represented by explicit scalar coefficients multiplying
independent roots, as in the kernel example below. This distinction preserves
the shared trainable parameters and their derivatives. Arbitrary fixed real
coefficients can be scalar parameter nodes; admissibility always requires them
to remain fixed as width grows.

Build coordinate expressions from these operations. For instance,
`p.phi(u*v+s, 2)*w` is a same-type expression when `u,v,w` share a type and
`s` is scalar. Nonlinear scalar feedback can be written
`p.mean(p.phi(p.broadcast(s, kind)))`. Its limit may be a zero-dimensional
Gaussian expectation, so the final assembly remains polynomial in the returned
expectation nodes and deterministic parameters.

Cross-type products, array or text formulas, nonconstant division, negative or
fractional powers, and dense matrix directions are unsupported. There is no
coordinate selection, inverse, arbitrary parameter-tensor contraction, or
width-dependent normalization primitive. The implementation supports arbitrary
fixed finite program sizes, derivative orders and update counts in principle;
Python recursion, memory use, rational bit sizes and expression expansion can
stop much smaller practical cases. There is no uniform-in-depth or efficient
high-order guarantee. A parameter named `n` does not make a width-dependent
program admissible. Fixed-order jets do not reconstruct a positive-time
trajectory or establish convergence of an infinite Taylor series.

## Physical derivatives and frozen seed data

`p.directional(O, directions)` takes one derivative of the finite primitive
graph. Dictionary keys are vector-root nodes, scalar parameter nodes, or named
matrix parameters. Node directions must match their parameter type; matrix
directions must be pure represented rank sums. Inserted directions are held
fixed for that one derivative. Unlisted parameters have zero direction.

`p.derivatives(O, directions, order, moving=False)` returns derivatives indexed
`0,...,order`. With `moving=False`, directions are fixed across all repeated
derivatives, giving the straight path through the initial point. With
`moving=True`, repeated differentiation includes the state dependence of the
vector field. Its second derivative is `D²O[V,V] + DO[DV[V]]`.

```python
from pde.mfp_compiler import Program

p = Program()
kind = p.vector_type("neurons")
x = p.root("x", kind)
O, V = p.mean(x**2), -(x**3)
frozen = p.derivatives(O, {x: V}, order=2)
moving = p.derivatives(O, {x: V}, order=2, moving=True)
assert str(p.compile(frozen[2]).output) == "30"
assert str(p.compile(moving[2]).output) == "120"
assert str(p.compile(p.jets(O, {x: V}, 2, moving=True)[2]).output) == "60"
```

Here `x` is the evolving vector state, not a data input. For the scalar ODE
`x_dot=-x**3`, the coordinate solution is `a/sqrt(1+2*t*a**2)`, so the second
derivative of its square at zero is `8*a**6`. A standard Gaussian sixth moment
is 15. The straight path `a-t*a**3` instead gives `2*a**6`. This independently
explains the values 120 and 30. `jets` divides derivative `r` by `r!`.

`p.freeze(value)` declares an independent seed datum with the base state's
numerical value. Physical AD holds it fixed, while finite evaluation and
Gaussian compilation retain that value and its source dependence. Thus
`p.mean(p.freeze(x)**2)` has the same value as `p.mean(x**2)`, but zero physical
derivative with respect to `x` under the declared convention. This is a partial
derivative on the enlarged space of parameters and seed data, evaluated at the
specified seeds. Inserting `freeze` into a primal network changes the derivative
being requested. Gaussian source partials still differentiate the frozen
expression's explicit source dependence. Independence here concerns physical
derivative coordinates, not statistical independence of initialization values.

State substitution preserves the original seed expression: `p.at(seed, state)`
does not refresh it, and repeated gradient steps keep that same seed. For
`seed=p.freeze(x)` and `loss=p.inner(x,seed)`, vector mobility `n` gives
`x_after=x-steps*eta*seed`. To take a new snapshot of an ordinary expression
`value` at an updated state, explicitly use `p.freeze(p.at(value,state))`.
Freezing a represented matrix direction means freezing its scalar coefficient
and both vector factors; their original dependencies are preserved in the same
way. Finite evaluation still obtains seed values from the supplied initial
arrays, rather than storing a numerical copy when the symbolic node is built.

For a general finite path, `curve_jets` accepts already factorial-normalized
parameter coefficients. This complete example uses `x(t)=x+t*x**2-t**2*x`, with
both coefficients evaluated at the base state and fixed on the path:

```python
from pde.mfp_compiler import Program

p = Program()
x = p.root("x", p.vector_type("neurons"))
jet = p.curve_jets(p.mean(x**2), {x: (x**2, -x)}, order=2)
assert str(p.compile(jet[2]).output) == "1"  # E[x**4-2*x**2]
```

Matrix path coefficients must be pure rank sums. Mixed fixed-direction
derivatives can be constructed with successive `directional` calls and
explicitly frozen direction expressions.

## Gradients, ambient updates and history pullbacks

For scalar `loss`, `p.gradient(loss, vectors=[x], matrices=[W], scalars=[s])`
returns `n*grad_x(loss)`, the ordinary Frobenius gradient `grad_W(loss)`, and
ordinary scalar `grad_s(loss)`. A matrix gradient is a finite sum of normalized
outer products. Contributions from every shared forward and transpose use are
accumulated. Additional fixed block multipliers can be included explicitly in
a moving flow, such as `{x: -kx*g[x], W: -kW*g[W]}`.

`p.gradient_descent` computes the ambient gradient of the current-parameter
loss template before substituting updated states. Updates are simultaneous;
vector mobility is `n` and matrix mobility is one. Its `mobilities` dictionary
supplies extra fixed deterministic factors. `steps` is a fixed nonnegative
integer; the step size and factors are deterministic scalar expressions.
They are not allowed to depend on random coordinates or scalar averages.
The helper does not assert loss decrease or step stability.

```python
from pde.mfp_compiler import Program

p = Program()
lower, upper = p.vector_type("lower"), p.vector_type("upper")
x = p.root("x", lower)
W = p.matrix("W", lower, upper)
loss = p.mean((W @ x)**2)
state = p.gradient_descent(loss, vectors=[x], matrices=[W], steps=2, step_size=0.01)
updated_loss = p.at(loss, state)
print(p.compile(updated_loss).formula())
```

`at` substitutes all supplied states simultaneously without revisiting their
replacement expressions or changing existing frozen seed expressions.
To differentiate through training history, build
`updated_loss` first and then differentiate that entire graph. This pullback
includes the parameter dependence of the updates; it is distinct from the
ambient gradient used to take each step. Explicitly frozen independent seeds
remain fixed in that pullback as well.

The `gradient_update` calculus example uses the explicit scalar loss
`mean(z**4)/4`, where `z=W@one`, a matrix mobility of one, and fixed step `eta`.
It evaluates the updated transpose on the saved pre-update vector `z**3`.
The result is exactly lowered at finite width, and its limiting squared
normalized norm is `15+(3-15*eta)**2`. A separate `rank_update` example checks
`W+2*u*x.T/n`; `singular_queries` uses two calls `W@one` with identical inputs.
Their source covariance has rank one, but both formal source slots and both
response contributions remain present.

## A parameter derivative of a two-hidden-layer MLP

The executable [MLP example](scripts/example_mfp_mlp_derivative.py) has input
`x=1`, no biases, two hidden layers of width `n`, and stored parameters
`W1,W3` of length `n`, with `W2` an `n` by `n` matrix. Initialization entries
are independent: `W1_i,W3_i ~ N(0,1)` and `W2_ij ~ N(0,1/n)`. This explicitly
uses an order-one stored readout, not the small-readout initialization.

Its forward pass is `z1=W1`, `h1=phi(z1)`, `z2=W2@h1`, `h2=phi(z2)`, and
`f=W3.T@h2/n`. The requested first-layer observable is
`O=n*||grad_W1 f||²`, formed as the normalized squared norm of the returned
scaled vector gradient. The executable constructs the forward pass with
`Program`, then calls `gradient`, `inner`, and `compile` as above.

Let `Z1 ~ N(0,1)`, `q1=E[phi(Z1)**2]`, and `Z2 ~ N(0,q1)`. Set
`s1=E[phi'(Z1)**2]`, `s2=E[phi'(Z2)**2]`, and `q2=E[phi(Z2)**2]`.
The limiting expectation of `O` is `s1*s2`. The average first-layer derivative
has limit zero; the full parameter metric norm has limit `s1*s2+q1*s2+q2`.
The reused transpose is included: its response coefficient vanishes because
it contains the independent centered readout.

| Activation flag | First-layer derivative energy | Full metric norm |
| --- | ---: | ---: |
| `identity` | 1 | 3 |
| `cubic` | 164025 | 305775 |

The `symbolic` default returns the explicit Gaussian moments. The test suite
checks rational-array backpropagation and the norm identity independently of
the symbolic AD code, then checks both polynomial specializations.

## Geometry, labels and feature-kernel jets

The [kernel example](scripts/example_mfp_kernel_jets.py) fixes `m=d=2` and
normalized data `x1/sqrt(2)=(alpha,0)` and `x2/sqrt(2)=(beta,gamma)`.
Geometry and labels `y1,y2` remain fixed symbolic scalar parameters. The input
Gram is

```text
G11=alpha**2,  G12=alpha*beta,  G22=beta**2+gamma**2.
```

This parameterization is positive semidefinite, including singular cases.
It covers every real PSD two-by-two Gram after choosing factors; computing
factors from arbitrary symbolic covariance entries is not an API operation.

The shared first-layer matrix has independent columns `U,V ~ N(0,I_n)`.
The hidden matrix `W2` has iid `N(0,1/n)` entries, and the independent stored
readout `W3` again has iid `N(0,1)` entries. There are no biases. The finite
forward pass and loss are

```text
z1 = [alpha*U, beta*U+gamma*V]
h1[a] = phi(z1[a])
z2[a] = W2 @ h1[a]
h2[a] = phi(z2[a])
f[a] = W3.T @ h2[a] / n
r[a] = f[a]-y[a]
loss = (r[0]**2+r[1]**2)/4.
```

Physical gradient flow trains all four blocks: `U,V,W3` have mobility `n`,
and `W2` has mobility one. The loss is the **half mean squared loss**, so
its clock differs by a factor of two from the default unhalved book loss.
The observable `K12=h2[0].T@h2[1]/n` is the last-layer feature kernel, or
equivalently the readout block of the tangent kernel. It is not the sum over
parameter blocks. The script computes

```text
J_r = lim_(n→∞) E[(d**r/dt**r) K12(0)] / r!,   r=0,1,2,
```

by taking finite-width moving derivatives first. The residuals, all parameter
blocks and the reused transpose move. A finite-width first derivative need not
vanish. The limiting first coefficient does vanish in this example.

For generic activation, let `(Z1_1,Z1_2)` be centered Gaussian with covariance
`G`, define `S_ab=E[phi(Z1_a)*phi(Z1_b)]`, and let `(Z2_1,Z2_2)` have covariance
`S`. Then `J0=E[phi(Z2_1)*phi(Z2_2)]`, `J1=0`, and `J2` is homogeneous
quadratic in `y1,y2`, with coefficients given by the generated Gaussian graph.
The generic graph is intentionally emitted by the producer rather than pasted
into this guide. Its intermediate expectations may remain after final output
simplification; the graph is not claimed to be minimal.

Identity activation gives the compact independent check

```text
J0 = G12,  J1 = 0,
J2 = (9/4)*(G11*y1+G12*y2)*(G12*y1+G22*y2).
```

For the nonlinear choice `phi(z)=z**2`, put `s=G11*G22`, `c=G12`, and define

```text
A = 5815*s**2+11746*s*c**2+16702*c**4
B = 4542*s**4+14636*s**3*c**2+30788*s**2*c**4+13856*s*c**6+4704*c**8.
J0 = 9*s**2+2*(s+2*c**2)**2
J1 = 0
J2 = A*(G11**4*y1**2+G22**4*y2**2)+B*y1*y2.
```

The complete producer regenerates that polynomial with symbolic geometry and
labels. Tests compare its compact form to the generated expansion, and also
specialize every generic expectation atom to the quadratic activation and
compare with direct polynomial compilation. Those two compilation paths share
the source-rule implementation; their agreement is not an independent proof
of the full second coefficient. The finite-width AD check is independent:
rational dense backpropagation and coefficient convolution through order two
verify all moving blocks at widths two and three. The initial nonlinear kernel
is separately checked by two Gaussian fourth-moment identities. These checks
require no retained outputs.

## Returned graph, expression API and finite interpreter

`dag.expectations` is an ordered tuple of entries with fields `symbol`,
`integrand`, `coordinates`, `covariance`, and `kind`. Covariance entries and
integrands use only prior expectation values and fixed deterministic parameters.
`dag.output` is the final scalar expression. `dag.fields` exposes computed
representatives; `dag.sources` retains named source coordinates and covariances,
even for duplicate calls with perfect correlation. `dag.trace` includes the
finite builder transformations and Gaussian dependency traversal. `formula()`
renders definitions once; `to_dict()` yields a JSON-ready description. These
are inspection outputs, not a serializer for recreating an editable `Program`.

Two distinct derivative engines are exposed. `Program.directional` and
`Program.gradient` propagate through the finite typed graph, including scalar
feedback and reused parameters. `pde.mfp_expr.diff` takes named scalar-source
partials inside Gaussian evaluation, holding all other symbols, including
previous expectation coefficients, fixed. Singular covariance does not identify
formal variables before these partials are taken.

The supporting `pde.mfp_expr` factories are `const`, `symbol`, and `phi`; its
operations include `diff`, `expand`, `substitute`, `evaluate`, `render`, and
`gaussian_expectation`. Substitution is simultaneous and structural.
`evaluate(expr, values, activation)` calls `activation(order, value)` for
activation nodes; it evaluates a supplied scalar expression, not an entire
expectation DAG. `gaussian_expectation` accepts named centered coordinates,
with missing covariance entries treated as zero. Symbolic covariance symmetry
is checked structurally, while positive semidefiniteness is the caller's
obligation at this lower level. Polynomial terms reduce by Wick's rule; flat
activation products use terminating Stein reduction. Nested activation
integrals remain atoms. Rational moment checks compare the specialized reducer
with the maintained `pde.gaussian_moments.gaussian_moment` API, whose stricter
no-float input contract is unchanged.

The independent interpreter is
`pde.mfp_finite.evaluate_finite(output, width, roots, matrices, parameters=None,
activation=None)`. It evaluates actual supplied arrays and never samples the
initialization law. Pass finite Python lists/tuples and actual stored matrix
entries, with no extra matrix rescaling. All required root/matrix/parameter
leaves need values; unused supplied entries are validated too. The activation
callback must supply the actual derivative at its requested order. Integer and
`Fraction` inputs remain exact; float state entries use ordinary floating
arithmetic, unlike symbolic decimal-rational conversion. Vector outputs are
immutable tuples. Finite input checks do not guarantee that every intermediate
floating operation avoids overflow or underflow.

```python
from fractions import Fraction
from pde.mfp_compiler import Program
from pde.mfp_finite import evaluate_finite

p = Program()
x = p.root("x", p.vector_type("neurons"))
O = p.mean(x**2)
assert evaluate_finite(O, 2, {x: [Fraction(1, 2), Fraction(3, 2)]}, {}) == Fraction(5, 4)
```

No part of this API silently replaces a Gaussian integral with numerical
quadrature, supplies a covariance family with a neural interpretation, or
turns fixed finite derivatives into a positive-time population solver.
