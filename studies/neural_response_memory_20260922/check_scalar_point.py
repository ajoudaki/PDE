"""Independent algebra checks for the passive-point scalar closure.

No fitting campaign runs here.  The physical oracle below is written directly
from the P=1 response equations, without calling the reference implementation.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import copy
import hashlib
import json
from pathlib import Path
import time

import numpy as np

from scalar_fourier_engine import (DiagramEvaluator, canonical, field, merge,
                                   node, nonconstant, size)
from scalar_point_engine import ScalarPointSystem


def oracle(W1, W20, W30, c, U, V, y, A2, B2, A3, B3, L):
    """Direct physical/moment derivatives and training/passive response lift."""
    n, M = c.size, U.shape[1]
    alpha = -2. / (M * n * L)
    W2 = W20 + alpha * (A2 @ B2.T)
    W3 = W30 + alpha * (A3 @ B3.T)
    h1 = np.tanh(W1 @ U)
    h2 = np.tanh(W2 @ h1)
    h3 = np.tanh(W3 @ h2)
    r = c @ h3 / n - y
    rho = np.linalg.norm(r) / np.sqrt(M)
    d3 = c[:, None] * (1. - h3*h3)
    d2 = (1. - h2*h2) * (W3.T @ d3)
    d1 = (1. - h1*h1) * (W2.T @ d2)
    dw = (-2. / M) * ((d1 * r) @ U.T)
    dc = (-2. / M) * (h3 @ r)
    dA2, dB2, dA3, dB3 = d2*r, rho*h1, d3*r, rho*h2
    dW2 = alpha * (dA2 @ B2.T + A2 @ dB2.T - rho/L*(A2 @ B2.T))
    dW3 = alpha * (dA3 @ B3.T + A3 @ dB3.T - rho/L*(A3 @ B3.T))
    inputs = np.column_stack((U, V))
    all1 = np.tanh(W1 @ inputs)
    all2 = np.tanh(W2 @ all1)
    all3 = np.tanh(W3 @ all2)
    dh1 = (1.-all1*all1) * (dw @ inputs)
    dh2 = (1.-all2*all2) * (dW2 @ all1 + W2 @ dh1)
    dh3 = (1.-all3*all3) * (dW3 @ all2 + W3 @ dh2)
    vals, dots = {field('c', 3): c[:, None]}, {field('c', 3): dc[:, None]}
    for layer, h, dh in ((1, all1, dh1), (2, all2, dh2), (3, all3, dh3)):
        for a in range(M+1):
            vals[field('h', layer, a)] = h[:, a, None]
            dots[field('h', layer, a)] = dh[:, a, None]
    for kind, layer, value, dot in (
        ('A', 2, A2, dA2), ('B', 2, B2, dB2),
        ('A', 3, A3, dA3), ('B', 3, B3, dB3)):
        for a in range(M):
            vals[field(kind, layer, a)] = value[:, a, None]
            dots[field(kind, layer, a)] = dot[:, a, None]
    df = (dc @ all3 + c @ dh3) / n
    return vals, dots, r, rho, df


def contains_sample(tree, sample):
    return any(f[0] == 'h' and f[2] == sample for f in tree[1]) or any(
        contains_sample(c, sample) for c in tree[2])


def rename_sample(tree, source, target):
    def rooted(t):
        fields = tuple((kind, layer, target if kind == 'h' and a == source else a)
                       for kind, layer, a in t[1])
        return node(t[0], fields, [rooted(c) for c in t[2]])
    return canonical(rooted(tree))


def row_as_patterns(system, row, rename=None):
    out = defaultdict(float)
    for coef, indices, ai, drive, lp in row:
        if ai != -1:
            raise AssertionError('Angular factor in point equation')
        trees = [system.training_patterns[i] for i in indices]
        if rename is not None:
            trees = [rename(t) for t in trees]
        out[(tuple(sorted(trees)), drive, lp)] += coef
    return {key: value for key, value in out.items() if value != 0.}


def scalar_row_value(row, scalar_values, r, rho, L):
    result = 0.
    for coef, indices, ai, drive, lp in row:
        if ai != -1:
            raise AssertionError('Angular factor in point equation')
        d = 1. if drive == -2 else rho if drive == -1 else r[drive]
        result += coef * np.prod(scalar_values[list(indices)]) * d / L**lp
    return result


def output_rule(system, ev, vals, r, rho, L, sample):
    """Rebuild output product rule and cutoff independently of row compiler."""
    total, kept, omitted, omitted_nonzero = 0., 0., 0, 0
    for species, other in ((field('c', 3), field('h', 3, sample)),
                           (field('h', 3, sample), field('c', 3))):
        for (root, forest, cc, ss, drive, lp), coef in system.templates.rhs(species).items():
            if cc or ss:
                raise AssertionError('Trigonometric bookkeeping in point template')
            joined = canonical(merge(node(3, [other]), root))
            factors = forest + ((joined,) if nonconstant(joined) else ())
            d = 1. if drive == -2 else rho if drive == -1 else r[drive]
            term = coef*d/L**lp
            for t in factors:
                term *= float(ev.tree(t)[0])
            total += term
            if all(size(t) <= system.K for t in factors):
                kept += term
            else:
                omitted += 1
                omitted_nonzero += bool(term != 0.)
    return total, kept, omitted, omitted_nonzero


def run_checks():
    started = time.process_time()
    theta = np.deg2rad([10., 125.])
    U = np.stack((np.cos(theta), np.sin(theta)))
    V = np.array([np.cos(np.pi/3), np.sin(np.pi/3)])
    y = np.array([1., -1.])
    caps = dict(max_patterns=6000, max_terms=2000000, compile_seconds=120.)
    system = ScalarPointSystem(U, y, V, 5, **caps)
    M, n = len(y), 5
    assert system.M == M and system.templates.M == M
    assert len(system.output_indices) == M
    assert system.point_sample == M
    rng = np.random.default_rng(9252026)
    W1 = .4*rng.standard_normal((n, 2))
    W20, W30 = (rng.standard_normal((n, n))/np.sqrt(n) for _ in range(2))
    c = .3*rng.standard_normal(n)
    A2, B2, A3, B3 = (.2*rng.standard_normal((n, M)) for _ in range(4))
    L = 1.7
    vals, dots, r, rho, df = oracle(W1, W20, W30, c, U, V, y,
                                   A2, B2, A3, B3, L)
    ev = DiagramEvaluator(vals, W20, W30, np.array([0.]))
    template_errors = {}
    for species, expected in dots.items():
        actual = ev.expression(system.templates.rhs(species), r, rho, L)
        template_errors[str(species)] = float(np.max(np.abs(actual-expected)))
    assert max(template_errors.values()) < 2e-11
    q = np.array([float(ev.tree(t)[0]) for t in system.training_patterns])
    z = np.r_[q, L]
    actual = system.rhs(0., z)
    expected = np.array([scalar_row_value(row, q, r, rho, L)
                         for row in system.training_rows] + [rho])
    scalar_error = float(np.max(np.abs(actual-expected)))
    assert scalar_error < 2e-11
    output_checks = {}
    for sample, index in list(enumerate(system.output_indices)) + [(M, system.point_index)]:
        full, retained, omitted, nonzero = output_rule(system, ev, vals, r, rho, L, sample)
        output_checks[str(sample)] = dict(full_rule_error=abs(full-df[sample]),
                                          retained_rule_error=abs(retained-actual[index]),
                                          omitted_terms=omitted,
                                          nonzero_omitted_terms=nonzero)
        assert abs(full-df[sample]) < 2e-11
        assert abs(retained-actual[index]) < 2e-11
    passive = np.array([contains_sample(t, M) for t in system.training_patterns])
    for row in np.flatnonzero(~passive):
        for _, indices, _, drive, _ in system.training_rows[row]:
            assert all(not passive[i] for i in indices)
            assert drive < M
    perturbed = z.copy()
    perturbed[np.flatnonzero(passive)] += rng.standard_normal(passive.sum())
    perturbed_rhs = system.rhs(0., perturbed)
    train_independence = float(np.max(np.abs(actual[:-1][~passive]
                                             - perturbed_rhs[:-1][~passive])))
    assert train_independence == 0. and actual[-1] == perturbed_rhs[-1]
    no_residual = z.copy()
    no_residual[system.output_indices] = y
    stationary_error = float(np.max(np.abs(system.rhs(0., no_residual))))
    assert stationary_error == 0.
    stripped = copy.copy(system)
    for attr in ('templates', 'U', 'test_U', 'training_patterns', 'training_index',
                 'training_rows', 'angular_patterns', 'angular_index', 'angular_rows',
                 '_pending'):
        if hasattr(stripped, attr):
            delattr(stripped, attr)
    autonomy_error = float(np.max(np.abs(stripped.rhs(0., z)-actual)))
    assert autonomy_error == 0.
    initial = system.initialize(W1, W20, W30, c)
    expected_init = c @ np.tanh(W30 @ np.tanh(W20 @ np.tanh(W1 @ V))) / n
    initialization_error = abs(float(system.point_output(initial))-float(expected_init))
    assert initialization_error < 2e-13
    assert time.process_time()-started < 90., 'Leave 30 CPU seconds for duplicate control'

    duplicate = ScalarPointSystem(U, y, U[:, 0], 5, **caps)
    duplicate_error, checked_rows = 0., 0
    rename = lambda t: rename_sample(t, M, 0)
    for i, t in enumerate(duplicate.training_patterns):
        if not contains_sample(t, M):
            continue
        mapped = rename(t)
        assert mapped in duplicate.training_index
        j = duplicate.training_index[mapped]
        left = row_as_patterns(duplicate, duplicate.training_rows[i], rename)
        right = row_as_patterns(duplicate, duplicate.training_rows[j])
        error = max((abs(left.get(k, 0.)-right.get(k, 0.))
                     for k in left.keys() | right.keys()), default=0.)
        duplicate_error = max(duplicate_error, error)
        checked_rows += 1
    assert duplicate_error < 2e-12
    duplicate_initial = duplicate.initialize(W1, W20, W30, c)
    duplicate_initial_error = abs(float(duplicate.point_output(duplicate_initial))
                                  - duplicate.training_output(duplicate_initial)[0])
    assert duplicate_initial_error == 0.
    elapsed = time.process_time()-started
    assert elapsed < 120., 'Algebra CPU budget exceeded'
    files = ('scalar_fourier_engine.py', 'scalar_point_engine.py', 'check_scalar_point.py')
    here = Path(__file__).resolve().parent
    return dict(status='PASS', cpu_seconds=elapsed,
                primitive_template_max_error=max(template_errors.values()),
                primitive_template_errors=template_errors,
                compiled_scalar_rows_max_error=scalar_error,
                output_rule_checks=output_checks,
                train_cone_independence_error=train_independence,
                stationary_error=stationary_error, runtime_autonomy_error=autonomy_error,
                initialization_error=initialization_error,
                duplicate_rows_checked=checked_rows,
                duplicate_row_relabeling_max_error=duplicate_error,
                duplicate_initial_error=duplicate_initial_error,
                point_statistics=system.statistics(), duplicate_statistics=duplicate.statistics(),
                source_sha256={name: hashlib.sha256((here/name).read_bytes()).hexdigest()
                               for name in files})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.output and args.output.exists():
        raise FileExistsError(args.output)
    result = run_checks()
    text = json.dumps(result, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open('x') as stream:
            stream.write(text+'\n')
    print(text)


if __name__ == '__main__':
    main()
