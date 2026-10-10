# Optional numerical trajectory compression

**The selected-model numerical setup is not the theorem's certified global
initialization-only compiler.** Harmonic uses finite-horizon dense rollout.
Taylor offers either the same kind of empirical rollout or exact origin jets
through order two. The latter uses initialization alone, but does not perform
the analytic continuation or certified source approximation required by the
all-time theorem. Neither option supplies its accuracy or storage guarantee.

## Model and public interface

Let $n$ be dense width, $d$ input dimension, $L$ hidden depth and $m$
training sample count. `inputs` has shape `(m,d)`, with **normalized input
rows** $v_a=x_a/\sqrt d$; `labels` has shape `(m,)`. Queries use the same
normalization. The code never divides inputs by another $\sqrt d$, whitens
them, or rescales hidden matrices. All tensors use float64 and one explicit
device; the default is CPU. Unit input rows are a theorem assumption, rather
than an enforced numerical restriction.

The stored readout `w` is $W^{(L+1)}$ in the book. For dense state
`[W1,w,W2,...,WL]`,

$$
z_a^{(1)}=W^{(1)}v_a,\qquad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
h_a^{(\ell)}=\phi(z_a^{(\ell)}),\qquad
f_a=w^\top h_a^{(L)}/n.
$$

The loss is $\mathcal L=m^{-1}\sum_a(f_a-y_a)^2$, and physical gradient-flow
mobilities are `(n,n,1,...,1)` **in this stored state order**. Hidden matrices
are initialized with entry variance $1/n$, first weights with variance one.
The default readout is exactly zero, as in the complete-trajectory theorem. Explicit
`readout='small_gaussian'` instead gives stored readout variance $1/n^2$, as
in the book's finite small-readout convention; compressed constructors reject
that different initial condition. Draw order is first matrix, hidden matrices,
then the optional Gaussian readout, using a local seeded Torch generator.

All methods expose `initial_state`, `rhs(state,inputs,labels)` and
`predict(state,queries,inputs,labels)`. Dense and Legendre allow omission of
the last two prediction arguments. Selected methods need the training data
to reconstruct their corrected readout. Keep training data, initial arrays
and fixed model tensors unchanged during a run. Returned state lists can be
owned and edited by the caller; changing them defines a different initial
value problem.

`step(model,state,inputs,labels,h,method=...)` supports simultaneous Euler,
Heun and RK4, returns new tensors, and leaves its input unchanged. `rollout`
returns the final state and optionally predictions at requested times. It
stores no weight trajectory. Continuing a returned state requires its
`start_time` and the intended time schedule. These are numerical ODE steps;
only the dense Euler case is also ordinary simultaneous GD. There is no
arbitrary-step stability or loss-decrease promise.

```python
import torch
from pde.compression import Dense, Legendre, harmonic, taylor, rollout

U = torch.tensor([[1., 0.], [.6, .8]], dtype=torch.float64)
y = torch.tensor([.1, -.08], dtype=torch.float64)
queries = torch.tensor([[0., 1.]], dtype=torch.float64)
dense = Dense(48, 2, depth=3, seed=17)
models = {
    'dense': dense,
    'legendre': Legendre(dense, U, y, order=3),
    'harmonic': harmonic(dense, U, y, horizon=.04, step_size=.01,
                         rank=1, time_degree=2, spatial_degree=2, budget=32),
    'taylor': taylor(dense, U, y, queries, source_mode='jets',
                     rank=1, budget=32),
}
for name, model in models.items():
    state, predictions = rollout(model, U, y, [0., .02, .04],
                                 step_size=.01, queries=queries)
    print(name, predictions[-1])
```

This is a small operational example, not a problem certified to meet the
theorem's small-label and population-Gram hypotheses.

## Construction coverage

| Construction | Implemented numerical contract | Remaining theorem-to-runtime gap |
|---|---|---|
| Dense | Arbitrary positive fixed depth; all six supported activations; exact finite-flow right-hand side | Integration/roundoff error is numerical; no automatic theorem-hypothesis check |
| Legendre | Direct physical-time moments, arbitrary positive order and depth | No certified order selection, numerical error bound or fitted-limit certificate |
| Harmonic | Shared selected dynamics, time Chebyshev and real sphere-harmonic sources in dimensions 2 and 3 | Dense-rollout source setup; finite quadrature/time fits and rank truncation have no uniform certificate; no general-dimension harmonic compiler |
| Taylor, `jets` | Shared selected dynamics with exact order-two origin source jets before numerical rank truncation | No later-anchor continuation, adaptive analytic partition or uniform source bound |
| Taylor, `rollout` | Shared selected dynamics with finite-panel piecewise time-polynomial sources | Fits use a Chebyshev basis and dense rollout, not certified Taylor derivatives; no guarantee outside the declared panel |

Every runtime and both source backends support a common activation chosen
from `tanh`, `atan`, exact Gaussian-CDF `gelu`, `silu`, `softplus`, and `erf`.
All support arbitrary positive fixed depth; this uses the same direct equations throughout.
Layer-dependent activations and user-supplied derivative evaluators are not
implemented. The compact theorem assumes $L\ge2$; a one-layer numerical
instance has no hidden interface to compress.

Let $q$ be the positive integer memory order. Legendre state is `[W1,w,tau,bar_delta2,bar_h1,...,bar_deltaL,bar_h(L-1)]`.
Each moment array has shape `(q,n,m)`. The initialized hidden mixers are fixed,
and their evolving corrections are applied as low-rank factors:

$$
\widehat W^{(\ell)}=W_0^{(\ell)}-
\frac{2}{mn\tau}\sum_{a=1}^m\sum_{j=0}^{q-1}(2j+1)
\bar\delta_{a,j}^{(\ell)}\bar h_{a,j}^{(\ell-1)\top}.
$$

The same factors implement the actual transpose in backpropagation.
With residual $r_a=\widehat f_a-y_a$ and $\rho=\|r\|_2/\sqrt m$, the clock
obeys $\dot\tau=\rho$, $\tau(0)=1$. The zero-mode forward moment starts at
the initial feature, encoding the constant unit prefix; all other moments
start at zero. No right-hand side divides by a residual. At residual zero,
including zero labels at zero readout, every velocity is zero. This direct state stores moments themselves, without auxiliary lifted
features or a separately integrated residual norm.

Harmonic and Taylor use the same `Selected` runtime. For each layer, its
positive metric $M_\ell$ preserves the dense normalized inner product on
the retained source space. A selected mixer $B^{(\ell)}$ uses the adjoint

$$
B^{(\ell)*}=M_{\ell-1}^{-1}B^{(\ell)\top}M_\ell.
$$

The moving state adds the training deficit $c=y-f$. Let $V$ contain the
last-layer training features divided by $\sqrt m$, and let

$$
Q=V^\top M_LV,\qquad
\widehat w=w+VQ^{-1}\{(y-c)/\sqrt m-V^\top M_Lw\}.
$$

Prediction uses $\widehat w^\top M_Lh^{(L)}$, so training predictions equal
$y-c$, up to floating arithmetic. `rhs` implements the complete-trajectory theorem's
prescribed corrected optimizer and $\dot c=-2Kc/m$, with its metric Gram
matrix $K$. This is not claimed to be the Euclidean gradient of the
corrected predictor. `Q` uses a Cholesky solve after a scale-relative numerical
rank check: its smallest eigenvalue must exceed its largest times
`32 * max(selected_width, m) * float64_epsilon`. Every readout reconstruction
also checks the training identity against a scale-relative tolerance four
times that factor. Failure raises an error without regularization. Thus a
mathematically positive but numerically ill-conditioned Gram can be rejected;
Cholesky success alone does not establish numerical invertibility. The driver's
low-budget spectral-floor branch is outside this core's exact-Gram contract.

`budget=None` uses a sparsity-nine BSS barrier selector;
its finite arithmetic checks the source embedding's spectral interval.
An explicit `budget<n` uses seeded uniform coordinate candidates and accepts
only a measured condition number at most `condition_limit` (default 16).
It still constructs an exact source metric to numerical precision, but does
not claim the BSS factor-four bound. A budget below source rank is rejected.
`budget>=n` selects the explicit uncompressed full-retention branch. Both
selected backends retain the constant and initialized training features,
form initialized forward/reverse images **after** base-source truncation,
and discard the dense reference and source matrices after construction.

## Setup, storage and checks

`empirical_sources` evolves a disposable dense reference over the requested
finite horizon using RK4. Dyadic time intervals fit even Chebyshev nodes and
measure errors at interleaved odd nodes. Harmonic uses fixed circle or sphere
quadrature independent of scored queries; Taylor uses training and declared
passive inputs, never passive labels. Only one interval's fields and the
coefficient blocks awaiting an exact SVD are kept. Dense states are never
archived. This lowers history storage, but setup still costs a dense rollout
and coefficient factorization. It is not an efficient-preprocessing result.

`initial_jets` uses zero-readout identities: initially the hidden-weight
velocities vanish. With $H_L=[h_1^{(L)},\ldots,h_m^{(L)}]$,
$\dot w=2H_Ly/m$, and the first two source derivatives
come from differentiating the finite ODE. Its extension to arbitrary depth
and the six activations is checked against independent Torch autodifferentiation.
Numerical rank detection scales against the source before removal of its
mandatory component, so subtraction roundoff alone is not retained as a new
source direction.

Legendre has $n(d+1)+1+2(L-1)mnq$ moving tensor entries and $(L-1)n^2$
fixed entries. Selected widths $k_1,\ldots,k_L$ use
$k_1d+k_L+\sum_{\ell=2}^L k_\ell k_{\ell-1}+m$ moving entries, plus full
metrics and inverse caches. `storage` reports these and a separately retained
initial-state copy. If the current state is the initial object, count that
object once. Data, query buffers, integrator stages, Python objects and source
compiler scratch are additional; smaller selected widths do not by themselves
guarantee smaller total memory than dense.

The tests use independent autograd and maintained NumPy finite-network
oracles, moment quadrature/transport, source-jet derivatives, metric
identities and explicit continuation checks. Finite arithmetic can
overflow or saturate; no automatic precision or stability guarantee
is supplied. See the [data guide](COMPRESSION_DATA.md),
[prediction views](PREDICTION_VIEWS.md) and
[radial explorer](RADIAL_EXPLORER.md).

## Bounded reproduction

Run from the standalone edition or repository root with Python 3.10+,
NumPy and PyTorch. Static plotting additionally requires Matplotlib; Node is
optional for the executable JavaScript checks. Choose fresh output directories.
TorchVision is needed only for explicit MNIST loading.

```sh
mkdir -p data/established
optional_test_scratch=$(mktemp -d "$PWD/data/established/optional_tests.XXXXXX")
export PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
export PDE_OPTIONAL_TEST_SCRATCH="$optional_test_scratch" TMPDIR="$optional_test_scratch" MPLCONFIGDIR="$optional_test_scratch/matplotlib"
python -B -m unittest discover -s code/tests -p 'test_compression*.py' -v
python -B -m unittest discover -s code/tests -p 'test_observable_dictionaries.py' -v
python -B -m unittest discover -s code/tests -p 'test_prediction_views.py' -v
python -B -m unittest discover -s code/tests -p 'test_radial*.py' -v
python -B code/scripts/example_compression.py --out data/established/compression_example
python -B code/scripts/example_radial_explorer.py --out data/established/radial_example
```

These bounded CPU checks and examples make no fitted-endpoint, dense-fidelity,
GPU, speed, convergence-rate or theorem-certification claim. They require no
retained arrays or downloads. Keep the generated manifests and local dependency
versions for replay. Examples refuse existing output directories.
