"""Exact initial contractions with shared query-free tree messages.

This changes setup work only. Gates, rooted multiplication order, block batch
size and summation order follow Closure.initialize_from_pool. No initial block
or message array is retained after initialization.
"""
from functools import lru_cache
import time

import numpy as np

from true_aggregate_ode import node


def initialization_plan(model):
    template = model.template
    passive_colors = {i for i, name in enumerate(template.colors)
                      if name[0] in ('x', 'h') and name[1] >= template.m}

    @lru_cache(maxsize=None)
    def simplify(tree):
        layer, decorations, children = tree
        new_decorations = []
        for color in decorations:
            name = template.colors[color]
            if name[0] == 'alpha' or (name[0] == 'beta' and name[1] > 0):
                return None
            new_decorations.append(template.x[name[2]] if name[0] == 'beta' else color)
        new_children = []
        for child in children:
            simplified = simplify(child)
            if simplified is None:
                return None
            new_children.append(simplified)
        return node(layer, new_decorations, new_children)

    @lru_cache(maxsize=None)
    def is_passive(tree):
        return (any(color in passive_colors for color in tree[1])
                or any(is_passive(child) for child in tree[2]))

    def group(indices):
        active, roots = [], []
        for local_id, global_id in enumerate(indices):
            tree = simplify(template.trees[global_id])
            if tree is not None:
                active.append(local_id)
                roots.append(tree)
                is_passive(tree)
        return np.asarray(active, dtype=int), tuple(roots)

    core_ids, core_roots = group(model.core_ids)
    passive_ids, passive_roots = group(model.passive_ids)
    all_roots = core_roots+passive_roots
    dependencies = {}
    def visit(tree):
        if tree not in dependencies:
            dependencies[tree] = is_passive(tree)
            for child in tree[2]:
                visit(child)
    for tree in all_roots:
        visit(tree)
    return {'core_active': core_ids, 'core_roots': core_roots,
            'passive_active': passive_ids, 'passive_roots': passive_roots,
            'passive_dependencies': dependencies,
            'distinct_message_trees': len(dependencies)}


def initialize_shared_fast(model, pool, batch=128):
    started = time.monotonic()
    template = model.template
    if not template.compiled:
        raise ValueError('Initialization requires a complete template')
    G = np.asarray(pool['G'])
    k, count = G.shape[1], len(G)
    if k != template.k or np.max(np.abs(G)) > template.mark_bound:
        raise ValueError('Pool does not satisfy the fixed block/mark configuration')
    readout = np.asarray(pool['c']).reshape(-1, k)
    if np.max(np.abs(readout)) > 2.:
        raise ValueError('Readout normalization requires |c0| <= 2')
    weights = np.asarray(pool['w']).reshape(-1, k, template.u.shape[1])
    plan = initialization_plan(model)
    plan_seconds = time.monotonic()-started
    result = np.zeros(model.size)
    second = np.zeros(model.size)
    core, passive, _ = model.unpack(result)
    core_second, passive_second, _ = model.unpack(second)
    core_ids, passive_ids = plan['core_active'], plan['passive_active']
    shared_message_evaluations = 0
    passive_message_evaluations = 0
    for start in range(0, count, batch):
        sl = slice(start, min(start+batch, count))
        normalized_G = G[sl]/template.Gscale
        shared_messages = {}
        for lane, query_model in enumerate(model.models):
            # Match the original m+1-column matrix products, including the
            # training columns, before reusing their identical messages.
            x = np.tanh(weights[sl] @ query_model.queries.T)
            h = np.tanh(G[sl] @ x)
            coordinates = {**{color: x[:, :, a] for a, color in enumerate(template.x)},
                           **{color: h[:, :, a] for a, color in enumerate(template.h)},
                           template.zeta: readout[sl]/2}
            passive_messages = {}
            def message(tree):
                nonlocal shared_message_evaluations, passive_message_evaluations
                dependent = plan['passive_dependencies'][tree]
                cache = passive_messages if dependent else shared_messages
                if tree in cache:
                    return cache[tree]
                layer, decorations, children = tree
                value = np.ones(normalized_G.shape[:2])
                for color in decorations:
                    value *= coordinates[color]
                for child in children:
                    matrix = normalized_G if layer == 1 else normalized_G.transpose(0, 2, 1)
                    value *= np.einsum('bij,bj->bi', matrix, message(child))/template.k
                cache[tree] = value
                if dependent:
                    passive_message_evaluations += 1
                else:
                    shared_message_evaluations += 1
                return value
            if lane == 0 and len(core_ids):
                values = np.asarray([np.mean(message(tree), axis=1) for tree in plan['core_roots']])
                core[core_ids] += values.sum(axis=1)
                core_second[core_ids] += (values*values).sum(axis=1)
            if len(passive_ids):
                values = np.asarray([np.mean(message(tree), axis=1) for tree in plan['passive_roots']])
                passive[lane, passive_ids] += values.sum(axis=1)
                passive_second[lane, passive_ids] += (values*values).sum(axis=1)
    result /= count
    second /= count
    variance = np.maximum(0., second[:-1]-result[:-1]**2)
    result[-1] = 1.
    return result, {'method': 'same empirical initial contractions; cached symbolic plan and shared core messages',
        'seconds': time.monotonic()-started, 'plan_seconds': plan_seconds,
        'initial_blocks': count, 'initial_neurons': count*k, 'batch': batch,
        'active_core_coordinates': len(core_ids), 'active_passive_coordinates_per_query': len(passive_ids),
        'distinct_message_trees': plan['distinct_message_trees'],
        'shared_message_evaluations': shared_message_evaluations,
        'passive_message_evaluations': passive_message_evaluations,
        'max_standard_error_population_estimate': float(np.max(np.sqrt(variance/count))),
        'initial_readout_max_abs': float(np.max(np.abs(readout))),
        'mark_max_abs': float(np.max(np.abs(G))), 'mark_bound': template.mark_bound,
        'finite_empirical_initialization_error': 'floating point contraction evaluation only',
        'population_initialization_error': 'not certified; standard error is descriptive',
        'runtime_initial_pool_retained': False, 'mathematical_initialization_changed': False}
