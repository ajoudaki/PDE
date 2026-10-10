"""Small paper-compatible unit-row toy and binary-MNIST datasets; see DATA.md.

NumPy is the sole eager dependency. TorchVision is imported only by the explicit
MNIST loader, whose download flag defaults to False. No training is performed.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import math
from numbers import Integral, Real
from pathlib import Path

import numpy as np


PAPER_SOURCE = {
    'path': 'paper/figures/capture_trajectory.py',
    'sha256': '199a05d6ceba1ada532dd2db13774c9529424525cffdf3655e5aefa67639b0e3',
    'scopes': ['validation_data', '_experiment_data', 'EXPERIMENT_DEFAULTS.dataset'],
}


@dataclass
class Dataset:
    """Owned float64 rows, scalar labels, split-qualified IDs and provenance.

    Arrays and metadata remain mutable. Changing them invalidates the recorded
    hashes. IDs refer to source rows/draws, not to unique image content.
    """

    train_inputs: np.ndarray
    train_labels: np.ndarray
    query_inputs: np.ndarray
    query_labels: np.ndarray
    train_ids: np.ndarray
    query_ids: np.ndarray
    provenance: dict


def _integer(value, name, minimum=1):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, Integral) or value < minimum:
        raise ValueError(f'{name} must be an integer >= {minimum}')
    return int(value)


def _options(train_samples, query_samples, seed, label_scale):
    counts = (_integer(train_samples, 'train_samples'), _integer(query_samples, 'query_samples'))
    seed = _integer(seed, 'seed', 0)
    if seed >= 2**32-1:
        raise ValueError('seed must be less than 2**32-1 (the paper data-seed contract)')
    if (isinstance(label_scale, (bool, np.bool_)) or not isinstance(label_scale, Real)
            or not math.isfinite(label_scale) or label_scale <= 0):
        raise ValueError('label_scale must be finite and positive')
    return *counts, seed, float(label_scale)


def _array_sha(value):
    value = np.ascontiguousarray(value)
    digest = hashlib.sha256()
    digest.update(f'{value.dtype.str}:{value.shape}:'.encode('ascii'))
    digest.update(value.tobytes(order='C'))
    return digest.hexdigest()


def _unit_rows(value):
    value = np.array(value, dtype=np.float64, copy=True)
    norms = np.linalg.norm(value, axis=1, keepdims=True)
    if not np.isfinite(norms).all() or np.any(norms == 0):
        raise ValueError('Every selected input must have a finite, nonzero norm')
    return value/norms


def _dataset(train, labels, query, truth, train_ids, query_ids, provenance):
    arrays = dict(train_inputs=train, train_labels=labels, query_inputs=query, query_labels=truth)
    if not all(np.isfinite(v).all() for v in arrays.values()):
        raise ValueError('Data contain nonfinite values after preprocessing')
    provenance = dict(provenance, numpy_version=np.__version__, input_convention='unit Euclidean rows v=x/sqrt(d)',
                      source_implementation=dict(PAPER_SOURCE, scopes=list(PAPER_SOURCE['scopes'])),
                      array_sha256={name: _array_sha(v) for name, v in arrays.items()})
    return Dataset(**arrays, train_ids=np.asarray(train_ids, dtype=str),
                   query_ids=np.asarray(query_ids, dtype=str), provenance=provenance)


def circle_query_inputs(count, phase=.137):
    """Equally spaced unit directions, in increasing angle, without a duplicate endpoint."""
    count = _integer(count, 'count')
    if isinstance(phase, (bool, np.bool_)) or not isinstance(phase, Real) or not math.isfinite(phase):
        raise ValueError('phase must be finite and real')
    angle = np.linspace(0, 2*np.pi, count, endpoint=False) + float(phase)
    return np.column_stack((np.cos(angle), np.sin(angle)))


def toy_target(inputs):
    """Unscaled paper target on unit rows, with d=2 or d>=3; no label fitting.

    At d=2, g(v)=sin(3 theta)+0.5 cos(5 theta), theta=atan2(v[1],v[0]).
    At d>=3, g(v)=sqrt(d)*v[0]+d**1.5*v[0]*v[1]*v[2].
    """
    raw = np.asarray(inputs)
    if raw.dtype.kind not in 'fiu' or raw.ndim != 2 or raw.shape[1] < 2:
        raise ValueError('inputs must be real rows of dimension at least two')
    values = np.asarray(raw, dtype=np.float64)
    if (not np.isfinite(values).all()
            or not np.allclose(np.linalg.norm(values, axis=1), 1., rtol=1e-12, atol=1e-12)):
        raise ValueError('toy_target requires finite unit input rows')
    dimension = values.shape[1]
    if dimension == 2:
        angle = np.arctan2(values[:, 1], values[:, 0])
        return np.sin(3*angle) + .5*np.cos(5*angle)
    return np.sqrt(dimension)*values[:, 0] + dimension**1.5*values[:, 0]*values[:, 1]*values[:, 2]


def toy_data(dimension=2, train_samples=8, query_samples=30, seed=47, label_scale=1.):
    """Paper toy recipe: Gaussian training directions; grid/random test directions.

    The train RMS of the raw target scales BOTH splits. In d=2 queries use the
    phase-.137 grid; in d>=3 the same local RNG continues after the training draw.
    """
    dimension = _integer(dimension, 'dimension', 2)
    train_samples, query_samples, seed, label_scale = _options(train_samples, query_samples, seed, label_scale)
    rng = np.random.default_rng(seed)
    train = _unit_rows(rng.normal(size=(train_samples, dimension)))
    query = (circle_query_inputs(query_samples) if dimension == 2
             else _unit_rows(rng.normal(size=(query_samples, dimension))))
    labels, truth = toy_target(train), toy_target(query)
    scale = float(np.sqrt(np.mean(labels**2)))
    if not math.isfinite(scale) or scale == 0:
        raise ValueError('Training target RMS must be finite and positive')
    labels, truth = (labels/scale)*label_scale, (truth/scale)*label_scale
    prefix = f'toy:d{dimension}:seed{seed}:m{train_samples}'
    provenance = dict(dataset='toy', dimension=dimension, train_samples=train_samples,
                      query_samples=query_samples, seed=seed, generator='numpy.default_rng/PCG64',
                      label_scale=label_scale, target_train_rms=scale,
                      query_rule='equispaced_circle_phase_0.137' if dimension == 2 else 'continued_gaussian_directions',
                      normalization_fit='training target labels only')
    return _dataset(train, labels, query, truth,
                    [f'{prefix}:train:{i}' for i in range(train_samples)],
                    [f'{prefix}:q{query_samples}:query:{i}' for i in range(query_samples)], provenance)


def _digit_pair(value):
    try:
        value = tuple(value)
    except TypeError as error:
        raise ValueError('digit_pair must contain two distinct digits') from error
    if (len(value) != 2 or any(isinstance(v, (bool, np.bool_)) or not isinstance(v, Integral)
                              or not 0 <= v <= 9 for v in value) or value[0] == value[1]):
        raise ValueError('digit_pair must contain two distinct integer digits from 0 through 9')
    return tuple(map(int, value))


def _mnist_source(images, targets, split):
    images, targets = np.asarray(images), np.asarray(targets)
    if images.dtype != np.uint8 or images.ndim != 3 or images.shape[1:] != (28, 28):
        raise ValueError(f'{split} images must be raw uint8 arrays of shape (count,28,28)')
    if (targets.dtype.kind not in 'iu' or targets.shape != (len(images),)
            or np.any(targets > 9) or np.any(targets < 0)):
        raise ValueError(f'{split} targets must be one integer digit from 0 through 9 per image')
    return images, targets


def binary_mnist_from_arrays(train_images, train_targets, test_images, test_targets, *,
                             train_samples=8, query_samples=30, digit_pair=(1, 7), seed=47,
                             label_scale=1.):
    """Prepare binary subsets without ever mixing the supplied train/test pools.

    This array interface cannot certify that the caller supplied official MNIST.
    The loader below obtains the official partitions. IDs retain original row
    indices, qualified by split. Inputs are raw uint8 28x28 images, not transforms.
    """
    train_samples, query_samples, seed, label_scale = _options(train_samples, query_samples, seed, label_scale)
    digit_pair = _digit_pair(digit_pair)
    arrays, identifiers, sources = [], [], {}
    for split, count, images, targets in (
            ('train', train_samples, train_images, train_targets),
            ('test', query_samples, test_images, test_targets)):
        images, targets = _mnist_source(images, targets, split)
        rng = np.random.default_rng(seed + (split == 'test'))
        selected = []
        for digit, wanted in zip(digit_pair, ((count+1)//2, count//2)):
            candidates = np.flatnonzero(targets == digit)
            if len(candidates) < wanted:
                raise ValueError(f'{split} split has too few examples of digit {digit}')
            selected.extend(rng.permutation(candidates)[:wanted])
        rows = rng.permutation(np.asarray(selected, dtype=int))
        values = _unit_rows(images[rows].reshape(count, 784))
        labels = np.where(targets[rows] == digit_pair[0], -1., 1.)*label_scale
        arrays.extend((values, labels))
        identifiers.append([f'mnist:{split}:{row}' for row in rows])
        sources[split] = dict(count=len(images), selected_indices=rows.tolist(),
                              images_sha256=_array_sha(images), targets_sha256=_array_sha(targets))
    provenance = dict(dataset='binary_mnist', source='caller_supplied_arrays', dimension=784,
                      train_samples=train_samples, query_samples=query_samples, digit_pair=list(digit_pair),
                      seed=seed, split_seeds={'train': seed, 'test': seed+1},
                      generator='numpy.default_rng/PCG64', label_scale=label_scale,
                      class_labels={str(digit_pair[0]): -label_scale, str(digit_pair[1]): label_scale},
                      balancing='first digit gets ceil(count/2), second gets floor(count/2)',
                      preprocessing='flatten raw pixels in C order, divide each row by its Euclidean norm',
                      source_splits=sources, normalization_fit='none; per-image normalization only')
    return _dataset(*arrays, *identifiers, provenance)


def load_binary_mnist(root, *, train_samples=8, query_samples=30, digit_pair=(1, 7), seed=47,
                      label_scale=1., download=False):
    """Load official train/test splits through optional TorchVision, then preprocess.

    Downloads require download=True. No PCA, centering, resizing, augmentation,
    pooling, transformed Dataset access, or train/test resplitting is performed.
    """
    _options(train_samples, query_samples, seed, label_scale)
    digit_pair = _digit_pair(digit_pair)
    if not isinstance(download, bool):
        raise ValueError('download must be explicitly True or False')
    if not isinstance(root, (str, Path)) or not str(root).strip():
        raise ValueError('root must be an explicit nonempty cache path')
    try:
        from torchvision.datasets import MNIST
    except (ImportError, RuntimeError) as error:
        raise ImportError('load_binary_mnist needs a working optional torchvision installation') from error
    root = str(Path(root).expanduser())
    train = MNIST(root=root, train=True, download=download)
    test = MNIST(root=root, train=False, download=download)
    result = binary_mnist_from_arrays(train.data, train.targets, test.data, test.targets,
                                     train_samples=train_samples, query_samples=query_samples,
                                     digit_pair=digit_pair, seed=seed, label_scale=label_scale)
    result.provenance.update(source='torchvision.datasets.MNIST official train/test splits',
                             cache=root, download_requested=download)
    return result
