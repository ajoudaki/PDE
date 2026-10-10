# Unit-row toy tasks and binary MNIST

`pde.compression_data` is a NumPy module for circle/sphere targets and
raw binary MNIST. It returns a `Dataset` with `train_inputs`, `train_labels`,
`query_inputs`, `query_labels`, split-qualified `train_ids` / `query_ids`, and
JSON-serializable `provenance`. Input shapes are `(count,d)`, label shapes are
`(count,)`, and all four numerical arrays are float64. No experiment driver is
imported, no training is started, and no global random state is changed.

For the maintained book's physical input $x_a\in\mathbb R^d$, each returned row
is $v_a=x_a/\sqrt d$, with $\|v_a\|_2=1$. These are already the rows expected by
`pde.compression`: do not divide by another $\sqrt d$. The maintained
`code/pde` column convention instead uses `X = sqrt(d) * data.train_inputs.T`.
The module does not whiten the input Gram or change input correlations.

## Toy recipe

`toy_data(dimension=2, train_samples=8, query_samples=30, seed=47,
label_scale=1.)` uses one local `numpy.default_rng(seed)` (PCG64). It first draws
all training rows from independent standard Gaussian entries and normalizes
each row. In dimension two, query angles are
$\theta_i=2\pi i/p+0.137$, for $i=0,\ldots,p-1$ and query count $p$; in dimension
at least three, query Gaussian draws continue from the same generator after
the training draw and are normalized in the same way.

For a unit row $v$, `toy_target(v[None,:])` evaluates the raw scalar target

$$
g(v)=
\begin{cases}
\sin(3\theta)+\tfrac12\cos(5\theta),
  &d=2,\quad\theta=\operatorname{atan2}(v_2,v_1),\\
\sqrt d\,v_1+d^{3/2}v_1v_2v_3,&d\ge3.
\end{cases}
$$

Let $m$ be training count and $s=(m^{-1}\sum_{a=1}^m g(v_a)^2)^{1/2}$.
Training and query labels both equal `label_scale` times $g(v)/s$. Only the
training targets determine $s$; query labels have no effect on this scale.
The default data seed is separate from any network initialization seed.
`circle_query_inputs(count, phase=.137)` exposes the circle grid alone.
`toy_target(inputs)` takes a batch of unit rows and applies no fitted scale.
Dimension one and a zero training-target RMS are rejected.

```python
import torch
from pde.compression_data import toy_data
from pde.compression import Dense, rollout

data = toy_data(dimension=3, train_samples=4, query_samples=30,
                seed=47, label_scale=.1)
inputs = torch.from_numpy(data.train_inputs)
labels = torch.from_numpy(data.train_labels)
queries = torch.from_numpy(data.query_inputs)
dense = Dense(24, dimension=3, seed=17)
state, predictions = rollout(dense, inputs, labels, [0., .01],
                             step_size=.005, queries=queries)
```

This tiny integration example is a software check, not an accuracy experiment.
`torch.from_numpy` shares memory: keep the dataset unchanged during a run.

## Binary MNIST recipe

`load_binary_mnist(root, *, train_samples=8, query_samples=30,
digit_pair=(1,7), seed=47, label_scale=1., download=False)` imports the optional
`torchvision.datasets.MNIST` only when called. It requests `train=True` and
`train=False` separately, preserving MNIST's official training/test partition.
The root must be explicit; a missing local dataset fails unless the caller
explicitly opts into downloading. The deterministic tests use synthetic fixtures and request no downloads.

Within each official split, the first requested digit contributes
$\lceil c/2\rceil$ rows and the second $\lfloor c/2\rfloor$, where $c$ is that
split's requested count. The first digit maps to `-label_scale`, the second
to `+label_scale`. The train sampler uses `default_rng(seed)` and the test
sampler `default_rng(seed+1)`. In digit-pair order it permutes the original
indices of each class, takes the requested prefix, concatenates the selected
indices, and then permutes that concatenation. Sampling is without replacement.
Insufficient class counts fail instead of silently shrinking the dataset.

Each selected raw uint8 $28\times28$ image is flattened in C order to 784
float64 coordinates and divided by its own Euclidean norm. There is no PCA,
centering, resize, augmentation, or statistics fitted across examples.
Division by 255 would cancel in this normalization and is not performed.
Selected zero images fail. Query labels are supplied for scoring; callers
must not pass them to a source constructor that is allowed only query inputs.

```python
from pde.compression_data import load_binary_mnist

# Use an existing local cache. No download is requested.
data = load_binary_mnist(
    'data/established/mnist_cache',
    train_samples=8, query_samples=30, digit_pair=(1, 7), seed=47)
```

`binary_mnist_from_arrays(train_images, train_targets, test_images,
test_targets, *, ...)` exposes exactly the same preprocessing for local
fixtures or already loaded raw arrays. Images must have shape `(count,28,28)`
and dtype uint8; targets must be integer digits. This interface treats its
two supplied pools separately but cannot certify that they are official MNIST
or that the caller has not mixed their contents. It records its source as
`caller_supplied_arrays`; the loader records the official TorchVision source.
The package supplies no broad dataset registry, split search, sklearn digits,
arbitrary NPZ loader, resplitting, or undeclared-query sampler.

## Identity, reproducibility, and limits

IDs identify original rows: `mnist:train:123` and `mnist:test:123` name different
source records. They do not certify unique pixel content; no duplicate-image
removal occurs. Toy IDs distinguish seeded training draws from query draws or
grid nodes. The source hashes and recipe determine dataset identity, rather
than an ID string alone. Arrays and metadata are owned by the result and remain
mutable; subsequent mutation invalidates their recorded hashes.

Provenance retains recipe options, NumPy version, source implementation path
and SHA256, and hashes of all four output arrays. MNIST adds source-pool image
and target hashes, exact selected original indices, split seeds, and label
mapping. Hashes cover `dtype.str`, shape, and C-order bytes (see `_array_sha`),
not just pixel values. The loader hashes the full raw arrays; this is linear
work in the source size and uses a temporary byte copy. No downloaded bytes or
cache are read at module import. Record the local dependency environment along
with provenance for bitwise replay; cross-version floating arithmetic is not
guaranteed identical.

Counts must be positive integers, the data seed lies in $[0,2^{32}-1)$, and
`label_scale` must be finite and positive. Finite float64 arithmetic and the
explicit nonzero-norm checks are numerical contracts, not theorem certificates.
These tasks do not themselves verify small-label or Gram hypotheses.

## Deterministic checks

Run the commands in [the compression guide](COMPRESSION.md). Tests use
independent target formulas, pinned fixture IDs, pixel-normalization
oracles, official-split loader mocks, train-only scaling and seeded
replay. They do not validate downloaded MNIST files or dataset quality.
