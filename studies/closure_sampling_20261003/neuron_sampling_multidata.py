"""General-dimension explicit-probe adapter for the unchanged positive sampler.

U contains m unit input directions in R^d; physical inputs are sqrt(d)*U.
Only initialization, U, labels, and declared setup probes enter construction.
The runtime remains A, B, w, mu, nu, with the same weighted transpose.
"""
from __future__ import annotations

import time
import numpy as np
from neuron_sampling_setup import _matrix, build_sampler as _build_sampler


def unit_rows(value, name, dimension=None):
    value = _matrix(value, name)
    if min(value.shape) < 1 or (dimension is not None and value.shape[1] != dimension):
        raise ValueError(f'{name} must be a nonempty matrix with matching dimension')
    if not np.allclose(np.linalg.norm(value, axis=1), 1., rtol=0., atol=1e-10):
        raise ValueError(f'{name} must contain unit directions as rows')
    return value


def prepare_witness(A0, W0, U, labels, *, setup_probes):
    """Exact initial h, g, h'', g'', delta' with explicit unit probe rows.

    As in the original constructor, training rows precede setup probes. No
    evaluation query panel is accepted. Labels use unhalved mean-square loss.
    """
    begin = time.perf_counter()
    A0, W0 = _matrix(A0, 'A0'), _matrix(W0, 'W0')
    n, d = A0.shape
    if n < 1 or d < 1 or W0.shape != (n, n):
        raise ValueError('expected A0[n,d], W0[n,n] with positive n,d')
    U = unit_rows(U, 'U', d)
    setup_probes = unit_rows(setup_probes, 'setup_probes', d)
    labels = np.asarray(labels, dtype=np.float64)
    m = len(U)
    if labels.shape != (m,) or not np.isfinite(labels).all():
        raise ValueError('labels must be a finite length-m vector')
    probes = np.concatenate((U, setup_probes))
    H = np.tanh(A0 @ probes.T)
    Z = W0 @ H
    G = np.tanh(Z)
    Htrain, Gtrain = H[:, :m], G[:, :m]
    factor = 2. / m
    wdot = factor * (Gtrain @ labels)
    delta_dot = wdot[:, None] * (1. - Gtrain*Gtrain)
    reverse = W0.T @ delta_dot
    A_ddot = factor * (((1. - Htrain*Htrain)*reverse)*labels) @ U
    H_ddot = (1. - H*H)*(A_ddot @ probes.T)
    WH_ddot = W0 @ H_ddot
    Z_ddot = WH_ddot + (factor/n)*(delta_dot*labels) @ (Htrain.T @ H)
    G_ddot = (1. - G*G)*Z_ddot
    return dict(A0=A0, W0=W0, X=U, labels=labels, n=n, m=m, d=d,
        probe_count=len(setup_probes), setup_probes=setup_probes, probes=probes,
        H=H, Z=Z, G=G, delta_dot=delta_dot, reverse=reverse,
        groups1=[('A0', A0, .25), ('h0', H, 1.),
                 ('reverse_delta1', reverse, .5), ('h2', H_ddot, .3)],
        groups2=[('z0', Z, 1.), ('g0', G, 1.), ('delta1', delta_dot, .5),
                 ('g2', G_ddot, .3), ('W_h2', WH_ddot, .3)],
        setup_seconds=time.perf_counter()-begin)


def build_sampler(A0, W0, U, labels, n_selected, *, setup_probes,
                  basis_rank=None, mass_floor=.05, singular_tolerance=1e-10,
                  witness=None):
    """Reuse original selection/positive mass/mixer construction without edits."""
    setup_probes = unit_rows(setup_probes, 'setup_probes', np.asarray(A0).shape[1])
    if witness is None:
        witness = prepare_witness(A0, W0, U, labels, setup_probes=setup_probes)
    elif not np.array_equal(witness['setup_probes'], setup_probes):
        raise ValueError('witness setup probes do not match')
    result = _build_sampler(A0, W0, U, labels, n_selected,
        probe_count=len(setup_probes), basis_rank=basis_rank,
        mass_floor=mass_floor, singular_tolerance=singular_tolerance, witness=witness)
    info = result['diagnostics']
    info['input_dimension'] = witness['d']
    info['shared_data_scalar_count'] = int(witness['m']*(witness['d']+1))
    info['total_retained_scalar_count'] = (
        info['network_and_mass_scalar_count'] + info['shared_data_scalar_count'])
    info['probe_source'] = 'explicit fixed setup directions; training rows prepended'
    return result
