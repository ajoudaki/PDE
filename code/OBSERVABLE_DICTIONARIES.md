# Initialized observable dictionaries on finite carriers

## Model, order and retained state

There are two tanh hidden layers, input dimension $d=2$, and $n$ neurons
per layer. Training data are normalized rows $u_a=x_a/\sqrt2\in\mathbb R^2$,
labels $y_a$, and nonnegative weights $\rho_a$ summing to one. The actual
finite initializer supplies $g=W^{(1)}(0)\in\mathbb R^{n\times2}$,
$A=W^{(2)}(0)\in\mathbb R^{n\times n}$, and stored readout
$c(0)\in\mathbb R^n$, with independent Gaussian variances $1,1/n,1/n^2$.
Its small random readout is retained.

The integer **$p$ is the initialized dictionary order**, called $N$ in
parts of the maintained book. It is neither width nor the number of integration
nodes, and it is not the complete-trajectory theorem's Legendre memory order $q$.
For fixed matrices $b_1\in\mathbb R^{n\times K_1}$ and
$b_2\in\mathbb R^{n\times K_2}$, the moving state consists of
$W^{(1)}\in\mathbb R^{n\times2}$, $c\in\mathbb R^n$, and
$M\in\mathbb R^{K_2\times K_1}$. Initialize

$$
W^{(1)}(0)=g,\qquad M(0)=D=\frac{b_2^\top A b_1}{n},\qquad
W^{(2)}_{\rm dict}(t)=\frac{b_2 M(t)b_1^\top}{n}.
$$

In particular, the initial middle matrix is generally a filtered version of
$A$, and the first-layer rows and readout remain full carrier vectors.
Forward evaluation and residual-free backward responses are

$$
\begin{aligned}
h_a^{(1)}&=\tanh(W^{(1)}u_a),&
a_a&=b_1^\top h_a^{(1)}/n,\\
h_a^{(2)}&=\tanh(b_2 M a_a),&
f_a&=c^\top h_a^{(2)}/n,\\
\delta_a^{(2)}&=c\odot(1-(h_a^{(2)})^2),&
d_a&=b_2^\top\delta_a^{(2)}/n,\\
\delta_a^{(1)}&=(1-(h_a^{(1)})^2)\odot(b_1M^\top d_a),&
r_a&=f_a-y_a.
\end{aligned}
$$

Here $a_a\in\mathbb R^{K_1}$ and $d_a\in\mathbb R^{K_2}$ are evaluated
feature contractions, not extra stored state. The physical unhalved loss is
$\mathcal L=\sum_a\rho_a r_a^2$. The maintained engine evolves

$$
\dot W^{(1)}=-2\sum_a\rho_a r_a\delta_a^{(1)}u_a^\top,\qquad
\dot c=-2\sum_a\rho_a r_a h_a^{(2)},\qquad
\dot M=-2\sum_a\rho_a r_a d_a a_a^\top.
$$

These equations use the actual transpose of the same represented middle map.
They are the gradient flow in the population-weighted row/readout metric and
ordinary Frobenius coefficient metric. On this equal finite carrier their
coordinate mobilities are $n,n,1$ for $W^{(1)},c,M$, respectively.
For complete bases $b_1=b_2=\sqrt n I$, they reduce to the dense network with
physical block mobilities $n,1,n$. A general nonorthogonal dictionary changes
the middle update as well as the initial middle action.

The moving scalar count is $3n+K_1K_2$, and the frozen dictionaries require
$n(K_1+K_2)$ scalars. The engine also retains diagnostic initial copies,
probability vectors and caches; `engine.retained_bytes(state)` counts its tensor
entries, not construction scratch or all process memory. In a native population
solver the carrier row counts $P_1,P_2$ are independent quadratures; this finite
adapter deliberately sets both to the actual dense width $n$.

## Frozen dictionaries and exact counts

The observable method uses only the initialization. Define the two-column
arrays $H=\tanh(g)$, $J=\tanh(AH)$, and the bounded coordinate arrays
$X_1=[H,\tanh(A^\top J)]\in\mathbb R^{n\times4}$,
$X_2=J\in\mathbb R^{n\times2}$. Retain products
$\prod_j T_{\alpha_j}(X_{\ell,j})$ of Chebyshev polynomials with
total degree $\sum_j\alpha_j\le p$, in total-degree then descending
lexicographic exponent order. Append every bounded valid initialized-word
code through $p$ not already literally present, preserving the maintained
word definition and increasing code order. Dependencies are not automatically
retained features. Let $R_\ell$ be these raw matrices and set

$$
\eta_p=\frac1{1024(p+1)^2},\qquad
L_\ell L_\ell^\top=R_\ell^\top R_\ell/n+\eta_p I,\qquad
b_\ell=R_\ell L_\ell^{-\top}.
$$

The inverse-Cholesky transpose is essential. No feature is dropped for low
rank. For example, $p=5$ retains both lower constant words $\sin(1),\cos(1)$.
The returned matrix implements a positive ridge filter, not an orthogonal
projection. Through $p=9$, enrichment uses the same four/two initialized
coordinates; it does not explore the eventual new-action word hierarchy.

| $p$ | $K_1,K_2$ | Total columns | Middle coefficients |
|---:|---:|---:|---:|
| 1 | 5,3 | 8 | 15 |
| 2 | 15,6 | 21 | 90 |
| 3 | 35,10 | 45 | 350 |
| 4 | 71,15 | 86 | 1065 |
| 5 | 128,21 | 149 | 2688 |
| 6 | 213,28 | 241 | 5964 |
| 7 | 333,36 | 369 | 11988 |
| 8 | 499,45 | 544 | 22455 |
| 9 | 720,55 | 775 | 39600 |

The Gaussian and orthogonal controls start from the same random matrices in
each population. Gaussian columns are individually normalized to RMS one,
without whitening. Orthogonal columns are `sqrt(n)*qr(raw).Q`. Consequently
the controls share a subspace but have different frame conditioning and
different dynamics. Orthogonal controls require $n\ge\max(K_1,K_2)$.

The frozen random draw protocol is: with seed $s=7319$
and zero-based population index $j=0,1$, draw an $n\times(128,21)_j$ block
using $s+j$; append an $n\times(592,34)_j$ block using $s+100000+j$.
Requested counts take prefixes of those fixed blocks. Increasing $p$ never
changes the earlier raw random columns. Gaussian normalized prefixes agree
up to floating reduction effects; QR prefixes have the same subspaces up to
roundoff and column signs. Device and random-generator implementation remain
part of reproducibility: CPU and CUDA draws are not promised identical.

Observable raw spans are nested as sets of words;
their stored arrays need not be literal prefixes once tails move after larger
polynomial cores. Changing the ridge with $p$ also prevents claiming that the
normalized observable bases themselves are frozen prefixes.

`dictionary_metadata` retains normalized Gram eigenvalues, numerical rank at
the original relative eigenvalue cutoff $10^{-10}$, condition number on the
retained nonzero spectrum, stable/participation/entropy ranks, and observable
regularized raw-Gram condition and triangular-solve residual. These are
diagnostics, not truncation rules or symbolic rank proofs. Different finite carriers can have different numerical ranks.

## API and a small bounded use

`pde.observable_dictionaries` reuses maintained `pde` modules and optional Torch. Its `build` returns
the existing `ClosureEngine` and a `TensorState(w,c,M)`; `w` denotes first
weights, while `M` denotes dense middle weights in the supplied initial state
and dictionary coefficients in the returned state. The engine owns copies of
all frozen marks and rejects their detected mutation. Input rows are already
normalized; they are not normalized again.

Run with `PYTHONPATH=code` from the repository root:

```python
import torch
from pde.finite_torch import NetworkEngine
from pde.observable_dictionaries import build, dictionary_metadata, fit_endpoint, endpoint_errors

full = NetworkEngine(2, 40, seed=17, dtype=torch.float64, device="cpu")
initial = full.initial_state()
engine, state = build(initial, order=2, method="ours")
U = [[1., 0.], [.6, .8]]
data = engine.prepare_data(U, [1., -1.])
values = engine.predict(state, U)
velocity = engine.rhs(state, data)
short_state = engine.evolve(state, data, steps=4, step_size=.001)
diagnostics = dictionary_metadata(initial, 2, "ours", bases=(engine.b1, engine.b2))
```

`dictionaries(initial,order,method,dictionary_seed=7319)` returns the two
frozen matrices. `raw_observable_values(initial,order)` exposes the exact
unnormalized word evaluation. Supported integer orders are 1 through 9;
all even and odd orders use the same maintained word definition.
Float64 CPU and explicit CUDA devices are supported; global Torch policies are
unchanged. `ClosureEngine`'s historical module name `observable_torch_p1` does
not restrict the dimensions of supplied fixed marks.

For dimension-general first-order population initialization use
`initialize_population_p1(d,population_nodes,seed,device="cpu",...)`. This thin
adapter exposes the maintained general-d initializer with the same returned
engine operations. In its default unfolded representation $K_1=1+2d$,
$K_2=1+d$; thus $d=3$ gives `(7,4)`. It starts at readout zero and uses
independent joint population marks, with scalar coefficient quadrature;
`population_nodes` is $P$, not neural width $n$. Optional antithetic and
folded representations preserve their maintained metadata. For example:

```python
from pde.observable_dictionaries import initialize_population_p1
engine3, state3 = initialize_population_p1(3, 32, 53)
data3 = engine3.prepare_data([[1., 0., 0.], [.6, .8, 0.], [0., .6, .8]],
                             [1., -.5, .3], [.2, .3, .5])
state3 = engine3.evolve(state3, data3, steps=2, step_size=.01)
```

This makes weighted sphere triples executable without changing the circle
dictionary contract. The coefficient quadrature is numerical, and this adapter
does not establish general-d trained-network convergence.

For the native circle population initialization at orders two and three, use
the existing `pde.observable_solver` directly. Its `initialize(order,
initialization_nodes=..., population_nodes=...)`, `DataLaw`, `rhs`, `evolve`,
and `predict` already implement that model; no copied solver is needed. For
example:

```python
from pde import observable_solver as population
state = population.initialize(2, initialization_nodes=64, population_nodes=16)
data = population.DataLaw([[1., 0.], [.6, .8]], [1., -1.], [.4, .6])
data.validate(state.arithmetic)
final = population.evolve(state, data, steps=1, step_size=.001)
prediction = population.predict(final, data.inputs)
```

Its quadrature counts are deliberately small and carry no accuracy claim.
The specialized `observable_torch_circle.initialize` supports orders 1, 3,
and 5 only; order two must not be silently redirected through that interface.

`fit_endpoint(engine,state,data,step_size=...,max_steps=...,threshold=1e-3)`
returns an `Endpoint` containing copied state, time, loss, threshold, steps and
status. A missed threshold has status `step_cap`. A bracketed crossing uses
40 bisections of the accepted Heun step's parameter chord. This implements the
within-step chord convention; it is not a certificate of the earliest
crossing of the exact flow or of a nonmonotone chord. It uses a fixed Heun step size. Each full network and approximation must
be stopped independently at its own crossing.

`endpoint_errors(engine,end,full,full_end,U)` rejects unfitted or different-
threshold endpoints and returns panel L1, RMS, MSE and sampled maximum.
Endpoint metadata must describe the supplied state; callers retaining external
checkpoints should independently replay their losses. A uniform circle panel
gives sampled circle metrics; no unseen target labels enter this comparison.
Fitting, numerical consistency and approximation to the full predictor remain
separate assertions. Step size must be refined for any scientific comparison.

## Relation to population closures and selected-coordinate compression

The maintained book's polynomial observable closure is the direct mathematical
ancestor of this finite-carrier dictionary benchmark. The native population
solver `pde.observable_solver` independently integrates Gaussian coefficient
and population laws and starts at readout zero. Its initialization count $Q$
and population count $P$ are independent of dictionary order and of neural
width. Its fixed-order evaluation, `rhs`, Heun integration and restart APIs
remain available unchanged; $p=1,2,3$ have strict raw-span enrichment, with
the book explicitly distinguishing even-degree enrichment from dynamically
used directions. The dedicated `observable_torch_circle` importer supports
only $p=1,3,5$. No wrapper here broadens that importer's contract.

The earlier `pde.observable_closure` prototype has a different sine pilot,
retained dependency convention and ridge $2^{-N}$; its first-order counts
are `(6,4)`. It must not be silently substituted for the polynomial initializer
whose counts begin `(5,3)`. Maintained short-horizon population convergence
and iterated numerical limits do not constitute a theorem for the finite
carrier's long-training fitted-function benchmarks.

The complete-trajectory selected construction retains chosen neuron coordinates,
exact source metrics and metric adjoints, and has a corrected readout and
separate residual dynamics. Its Legendre model instead stores history moments
and a residual clock while retaining dense initial mixers. This older method
freezes initialized word dictionaries, keeps every first/readout carrier row,
and evolves one middle coefficient matrix. Common normalized contractions and
autonomous nonlinear evolution explain the conceptual relationship. There is
no established change of variables making these models identical, no transfer
of the complete-trajectory theorem's all-time bounds to this adapter, and no evidence here
that these small-order dictionaries satisfy that theorem's source-approximation
hypotheses. The selected-coordinate construction starts with zero readout; this finite comparison retains the actual small random finite readout.


The [general first-order guide](GENERAL_P1.md) specifies engine ownership,
arithmetic, integration and restart contracts. Its comparison section
documents `pde.closure_comparison`: saved-loss matching, parameter-chord
stopping here, and display interpolation are different operations.
The adapter retains its four basic endpoint metrics for convenience;
they use ordinary float64 squares and supply no extreme-range promise.
Diagnostic condition numbers are finite-carrier measurements.

Deterministic tests cover all retained words against a NumPy interpreter,
ridge orientation, seeded prefixes, gradient blocks, complete-basis
dense equivalence, weighted population initialization and endpoint
status. Run the commands in [the compression guide](COMPRESSION.md).
