"""Independent bounded algebra audit of the direct scalar response lift.

Frozen check: depth 2, width 5, M=2, P=1/2, K=5, seed 926719;
two passive inputs, including an exact duplicate of training input zero.
All numerical work has a 120-second CPU and wall budget. Identities pass
at 2e-10; finite differences pass at 2e-7. A short T=.2 population path
checks bound implementation, not the all-path bound theorem or accuracy.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import copy
import hashlib
import json
from pathlib import Path
import pickle
import signal
import time

import numpy as np
from scipy.integrate import solve_ivp

from scalar_direct import ScalarCompiler, FieldEvaluator
from scalar_fourier_engine import canonical, field, merge, node, nonconstant, size
from scalar_population_reference import PopulationReference, initialize


def oracle(parent, state, queries):
    """Independent finite-P formulas; never call parent RHS or reconstruction."""
    values = parent.unpack(state)
    n, m, P = parent.n, parent.M, parent.P
    w, c, L = values['w'], values['c'], float(values['L'])
    A, B = values['A2'], values['B2']
    W = parent.initialization.W0[0].copy()
    for k in range(P):
        W -= 2*(2*k+1)/(m*n*L)*(A[k] @ B[k].T)
    all_inputs = np.concatenate((parent.inputs, queries))
    h1 = np.tanh(w @ all_inputs.T)
    h2 = np.tanh(W @ h1)
    r = c @ h2[:, :m]/n-parent.labels
    rho = np.sqrt(np.dot(r, r)/m)
    delta2 = c[:, None]*(1-h2[:, :m]**2)
    delta1 = (1-h1[:, :m]**2)*(W.T @ delta2)
    dw = -2/m*((delta1*r) @ parent.inputs)
    dc = -2/m*(h2[:, :m] @ r)
    dA, dB = np.empty_like(A), np.empty_like(B)
    for k in range(P):
        dA[k] = delta2*r-rho/L*k*A[k]
        dB[k] = rho*h1[:, :m]-rho/L*k*B[k]
        for j in range(k):
            dA[k] -= rho/L*(2*j+1)*A[j]
            dB[k] -= rho/L*(2*j+1)*B[j]
    dW = np.zeros_like(W)
    for k in range(P):
        dW -= 2*(2*k+1)/(m*n*L)*(
            dA[k] @ B[k].T+A[k] @ dB[k].T-rho/L*(A[k] @ B[k].T))
    dh1 = (1-h1**2)*(dw @ all_inputs.T)
    dh2 = (1-h2**2)*(dW @ h1+W @ dh1)
    fields, dots = {field('c', 2):c}, {field('c', 2):dc}
    for layer, h, dh in ((1, h1, dh1), (2, h2, dh2)):
        for a in range(len(all_inputs)):
            fields[field('h', layer, a)] = h[:, a]
            dots[field('h', layer, a)] = dh[:, a]
    for kind, v, dv in (('A', A, dA), ('B', B, dB)):
        for k in range(P):
            for a in range(m):
                species = field(kind, 2, k*m+a)
                fields[species], dots[species] = v[k, :, a], dv[k, :, a]
    direction = parent.pack(dict(w=dw, c=dc, A2=dA, B2=dB, L=rho))
    return fields, dots, r, rho, direction, (dc @ h2+c @ dh2)/n


class IndependentTreeJets:
    """Product rule at the original root, without symbolic differentiation."""
    def __init__(self, fields, dots, weights):
        self.fields, self.dots, self.weights = fields, dots, weights
        self.n = len(next(iter(fields.values())))
        self.cache = {}

    def rooted(self, tree):
        if tree not in self.cache:
            value, dot = np.ones(self.n), np.zeros(self.n)
            factors = [(self.fields[f], self.dots[f]) for f in tree[1]]
            for child in tree[2]:
                v, d = self.rooted(child)
                W = self.weights[max(tree[0], child[0])-2]
                action = W if tree[0] > child[0] else W.T
                factors.append((action @ v, action @ d))
            for v, d in factors:
                dot = dot*v+value*d
                value = value*v
            self.cache[tree] = value, dot
        return self.cache[tree]

    def tree(self, tree):
        return tuple(float(np.mean(a)) for a in self.rooted(tree))


def substitution_terms(tree, templates):
    """Replace each decoration in place, without reroot/site-multiplicity code."""
    for i, species in enumerate(tree[1]):
        remainder = node(tree[0], tree[1][:i]+tree[1][i+1:], tree[2])
        for (root, forest, cc, ss, drive, power), coefficient in templates.rhs(species).items():
            assert cc == ss == 0
            yield merge(remainder, root), forest, drive, power, coefficient
    for i, child in enumerate(tree[2]):
        for replacement, forest, drive, power, coefficient in substitution_terms(child, templates):
            children = tree[2][:i]+(replacement,)+tree[2][i+1:]
            yield node(tree[0], tree[1], children), forest, drive, power, coefficient


def independent_split(tree, templates, evaluator, r, rho, L, K):
    full = kept = omitted = 0.
    nonzero_omitted = terms = 0
    for replacement, forest, drive, power, coefficient in substitution_terms(tree, templates):
        factors = forest+((replacement,) if nonconstant(replacement) else ())
        d = 1. if drive == -2 else rho if drive == -1 else r[drive]
        value = coefficient*d/L**power
        for factor in factors:
            value *= evaluator.tree(factor)
        full += value
        if all(size(factor) <= K for factor in factors):
            kept += value
        else:
            omitted += value
            nonzero_omitted += int(value != 0.)
        terms += 1
    return full, kept, omitted, nonzero_omitted, terms


def has_passive(tree, M):
    return any(f[0] == 'h' and f[2] >= M for f in tree[1]) or any(
        has_passive(child, M) for child in tree[2])


def rename(tree, source, target):
    species = [(kind, layer, target if kind == 'h' and a == source else a)
               for kind, layer, a in tree[1]]
    return canonical(node(tree[0], species, [rename(c, source, target) for c in tree[2]]))


def symbolic_row(compiler, row, source=None):
    out = defaultdict(float)
    for coefficient, indices, angular, drive, power in row:
        assert angular == -1
        trees = [compiler.training_patterns[i] for i in indices]
        if source is not None:
            trees = [rename(t, source, 0) for t in trees]
        out[(tuple(sorted(trees)), drive, power)] += coefficient
    return {k:v for k,v in out.items() if v != 0.}


def require_error(name, error, tolerance=2e-10):
    error = float(error)
    if not np.isfinite(error) or error > tolerance:
        raise AssertionError(f'{name}: {error} exceeds {tolerance}')
    return error


def explicit_table_rhs(runtime, z):
    q = runtime.reported(z)
    residual = q[runtime.output_indices]-runtime.labels
    rho = np.sqrt(np.dot(residual, residual)/len(residual))
    q = np.r_[q, 1.]
    drives = np.r_[1., rho, residual]
    result = np.zeros(runtime.dimension)
    table = runtime.table
    for i, coefficient in enumerate(table['coefficients']):
        value = coefficient*drives[table['drives'][i]]/z[-1]**table['powers'][i]
        for index in table['indices'][i]:
            value *= q[index]
        result[table['rows'][i]] += value
    result[-1] = rho
    return result


def run_checks():
    wall_started, cpu_started = time.monotonic(), time.process_time()
    def budget(*_):
        raise TimeoutError('120-second algebra audit budget exceeded')
    old_handler = signal.signal(signal.SIGALRM, budget)
    signal.alarm(120)
    try:
        return _run_checks(wall_started, cpu_started)
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old_handler)


def _run_checks(wall_started, cpu_started):
    inputs = np.array([[.9, .1], [-.2, .85]])
    labels = np.array([.7, -.4])
    queries = np.array([[.35, -.6], inputs[0]])
    rng = np.random.default_rng(926719)
    initial = initialize(5, seed=926719, depth=2)
    results = {}
    for order in (1, 2):
        parent = PopulationReference(inputs, labels, initial, order=order)
        compiler = ScalarCompiler(inputs, labels, queries, 5, order=order, depth=2,
                                  max_patterns=5000, max_terms=1200000,
                                  compile_seconds=45., max_memory_bytes=2*1024**3)
        runtime, bounds = compiler.initialize(parent, .2, clip=False)
        assert compiler.M == compiler.templates.M == len(labels)
        assert not compiler.angular_patterns
        state = parent.initial+.09*rng.standard_normal(parent.dimension)
        state[parent.slices['L']] = 1.4
        values, dots, residual, rho, direction, df = oracle(parent, state, queries)
        evaluator = FieldEvaluator(values, initial.W0)
        jets = IndependentTreeJets(values, dots, initial.W0)
        errors = {}
        errors['population_rhs'] = require_error('population RHS', np.max(abs(
            parent.rhs(0., state)-direction)))
        errors['primitive_templates'] = require_error('primitive templates', max(
            np.max(abs(evaluator.expression(compiler.templates.rhs(f), residual, rho, 1.4)-d))
            for f,d in dots.items()))
        all_inputs = np.concatenate((inputs, queries))
        hvelocity = parent.query_field_velocity(state, all_inputs)
        errors['population_output_chain'] = require_error('output chain', np.max(abs(hvelocity['f']-df)))
        eps = 1e-6
        fd = (parent.query_fields(state+eps*direction, all_inputs)['f']
              -parent.query_fields(state-eps*direction, all_inputs)['f'])/(2*eps)
        errors['directional_finite_difference'] = require_error('finite difference', np.max(abs(fd-df)), 2e-7)
        q = np.array([evaluator.tree(t) for t in compiler.training_patterns])
        z = np.r_[q, 1.4]
        derivative = runtime.rhs(0., z)
        errors['all_packed_rows'] = require_error('packed rows', np.max(abs(
            derivative-explicit_table_rhs(runtime, z))))
        selected = sorted(set(compiler.output_indices.tolist()+compiler.query_indices.tolist()
                              +compiler.gram_indices.ravel().tolist()
                              +np.linspace(0, compiler.ntrain-1, 12, dtype=int).tolist()))
        split_errors, nonzero_omitted, term_count = [], 0, 0
        for index in selected:
            tree = compiler.training_patterns[index]
            full, kept, omitted, count, terms = independent_split(
                tree, compiler.templates, evaluator, residual, rho, 1.4, compiler.K)
            expected = jets.tree(tree)[1]
            split_errors.extend((abs(full-expected), abs(kept-derivative[index]),
                                 abs(derivative[index]+omitted-expected)))
            nonzero_omitted += count
            term_count += terms
        errors['independent_retained_omitted_product_rules'] = require_error('independent split', max(split_errors))
        assert nonzero_omitted > 0
        initial_values = parent.query_fields(parent.initial, all_inputs)
        observations = runtime.observables(runtime.initial)
        errors['initial_outputs'] = require_error('initial outputs', np.max(abs(
            np.r_[observations['train'], observations['test']]-initial_values['f'])))
        expected_grams = np.array([h[:, :parent.M].T @ h[:, :parent.M]/parent.n
                                   for h in initial_values['h']])
        errors['initial_grams'] = require_error('initial Grams', np.max(abs(observations['grams']-expected_grams)))
        passive = np.array([has_passive(t, parent.M) for t in compiler.training_patterns])
        for i in np.flatnonzero(~passive):
            for _, indices, angular, drive, _ in compiler.training_rows[i]:
                assert angular == -1 and drive < parent.M
                assert all(not passive[j] for j in indices)
        altered = z.copy()
        altered[np.flatnonzero(passive)] += rng.standard_normal(int(passive.sum()))
        altered_dot = runtime.rhs(0., altered)
        errors['passive_feedback'] = require_error('passive feedback', max(
            np.max(abs(altered_dot[:-1][~passive]-derivative[:-1][~passive])),
            abs(altered_dot[-1]-derivative[-1])), 0.)
        zero = z.copy()
        zero[runtime.output_indices] = labels
        errors['zero_residual'] = require_error('zero residual', np.max(abs(runtime.rhs(0., zero))), 0.)
        duplicate_rows, duplicate_error = 0, 0.
        source = parent.M+1
        for i, tree in enumerate(compiler.training_patterns):
            mapped = rename(tree, source, 0)
            if mapped == tree:
                continue
            assert mapped in compiler.training_index
            j = compiler.training_index[mapped]
            left = symbolic_row(compiler, compiler.training_rows[i], source)
            right = symbolic_row(compiler, compiler.training_rows[j])
            duplicate_error = max(duplicate_error, max(
                (abs(left.get(k, 0.)-right.get(k, 0.)) for k in left.keys() | right.keys()), default=0.))
            duplicate_rows += 1
        errors['duplicate_symbolic_rows'] = require_error('duplicate rows', duplicate_error)
        errors['duplicate_output'] = require_error('duplicate output', abs(
            observations['test'][1]-observations['train'][0]), 0.)
        clipped = copy.deepcopy(runtime)
        clipped.clip = True
        clipped.caps = np.maximum(.001, np.abs(q)*.3+.002)
        stress = np.r_[np.linspace(-3., 3., len(q))*clipped.caps, 2.3]
        clipped_q = np.minimum(np.maximum(stress[:-1], -clipped.caps), clipped.caps)
        raw_copy = stress.copy()
        errors['clipped_report'] = require_error('clipped report', np.max(abs(clipped.reported(stress)-clipped_q)), 0.)
        errors['clipped_rhs'] = require_error('clipped RHS', np.max(abs(
            clipped.rhs(0., stress)-explicit_table_rhs(clipped, stress))))
        assert np.array_equal(stress, raw_copy)
        assert clipped.observables(stress)['clock'] == stress[-1]
        unbounded = copy.deepcopy(runtime)
        unbounded.clip = False
        expected_clipped_rhs = unbounded.rhs(0., np.r_[clipped_q, stress[-1]])
        errors['clip_inputs_not_derivatives'] = require_error('clipping semantics', np.max(abs(
            clipped.rhs(0., stress)-expected_clipped_rhs)), 0.)
        restored = pickle.loads(pickle.dumps(runtime))
        allowed = {'table', 'labels', 'output_indices', 'query_indices', 'gram_indices', 'caps', 'initial', 'clip'}
        assert set(vars(restored)) == allowed
        assert all(isinstance(v, np.ndarray) for v in restored.table.values())
        assert all(isinstance(getattr(restored, key), np.ndarray) for key in allowed-{'table', 'clip'})
        assert not any(getattr(restored, key).dtype.hasobject for key in allowed-{'table', 'clip'})
        errors['scalar_only_pickle_rhs'] = require_error('scalar-only restart', np.max(abs(restored.rhs(0., z)-derivative)), 0.)
        path = solve_ivp(parent.rhs, (0., .2), parent.initial, method='DOP853',
                         rtol=1e-10, atol=1e-12, t_eval=np.linspace(0., .2, 9))
        assert path.success
        maximum_ratio = 0.
        for sample in path.y.T:
            path_fields = oracle(parent, sample, queries)[0]
            ev = FieldEvaluator(path_fields, initial.W0)
            aggregate_values = np.array([ev.tree(t) for t in compiler.training_patterns])
            maximum_ratio = max(maximum_ratio, float(np.max(abs(aggregate_values)/runtime.caps)))
        assert maximum_ratio <= 1.+2e-10, maximum_ratio
        results[str(order)] = dict(errors=errors, dimension=runtime.dimension,
            retained_terms=compiler.retained_terms, independently_split_rows=len(selected),
            independent_substitution_terms=term_count, nonzero_omitted_terms=nonzero_omitted,
            duplicate_rows_checked=duplicate_rows, cap_path_max_ratio=maximum_ratio,
            cap_bounds=bounds, scalar_runtime_bytes=runtime.array_bytes())
        print(f'P={order}: PASS, dimension={runtime.dimension}, terms={compiler.retained_terms}', flush=True)
        if time.process_time()-cpu_started > 120:
            raise TimeoutError('120-second CPU budget exceeded')
    here = Path(__file__).resolve().parent
    sources = ('scalar_direct.py', 'scalar_population_reference.py', 'scalar_fourier_engine.py', 'check_scalar_direct.py')
    return dict(status='PASS', scope='deterministic algebra/implementation only; no training accuracy claim',
        config=dict(seed=926719, width=5, depth=2, orders=[1, 2], cutoff=5,
                    training_inputs=inputs.tolist(), labels=labels.tolist(), passive_inputs=queries.tolist()),
        results=results, wall_seconds=time.monotonic()-wall_started,
        cpu_seconds=time.process_time()-cpu_started,
        source_sha256={name:hashlib.sha256((here/name).read_bytes()).hexdigest() for name in sources})


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
