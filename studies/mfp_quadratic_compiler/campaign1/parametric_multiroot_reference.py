#!/usr/bin/env python3
"""Exact low-order reference compiler for Campaign 1.

This is deliberately a transparent extension of ``exact_graph_wick.py``.  It
does two things that the accepted single-root compiler does not yet do:

1. it carries several observable roots on one canonical graph DAG; and
2. it records an exact polynomial in one relative block-metric parameter.

The network variables and graphical conventions are those of the parent
compiler:

    c_p       readout weights,
    x_i=u_i^2 first-hidden squared preactivations,
    B_pi      middle weights.

The three vector-field blocks are

    D_a: c_p' = sum_ij B_pi B_pj x_i x_j,
    D_u: x_i' = 8 x_i sum_pj B_pi B_pj c_p x_j,
    D_W: B_pi' = (2/n) sum_j c_p B_pj x_j x_i.

By default the tested one-parameter line is

    D_lambda = D_a + lambda (D_u + D_W).

The operator is parameterized only through exact nonnegative integer powers
of lambda attached to the three rewrites.  No floating-point arithmetic is
used.  This file is a low-order reference and regression implementation; it
is not a replacement for the checked high-sector C++ engine.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
from typing import Iterable


COMPILER_ROOT = Path(__file__).resolve().parents[1]
if str(COMPILER_ROOT) not in sys.path:
    sys.path.insert(0, str(COMPILER_ROOT))

import exact_graph_wick as eg  # noqa: E402


ROOTS = ("f", "q1", "q2")
Polynomial = tuple[int, ...]  # coefficient of lambda**r at position r
Amplitude = tuple[Polynomial, ...]  # one polynomial for every ROOTS entry


def trim(poly: Iterable[int]) -> Polynomial:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values) if values else (0,)


def poly_add(left: Polynomial, right: Polynomial) -> Polynomial:
    size = max(len(left), len(right))
    return trim(
        (left[i] if i < len(left) else 0)
        + (right[i] if i < len(right) else 0)
        for i in range(size)
    )


def poly_scale_shift(poly: Polynomial, scalar: int, exponent: int) -> Polynomial:
    if exponent < 0:
        raise ValueError("metric exponents must be nonnegative")
    if not scalar or poly == (0,):
        return (0,)
    return (0,) * exponent + tuple(scalar * value for value in poly)


ZERO_AMPLITUDE: Amplitude = tuple((0,) for _ in ROOTS)


def amplitude_add(left: Amplitude, right: Amplitude) -> Amplitude:
    return tuple(poly_add(a, b) for a, b in zip(left, right, strict=True))


def amplitude_scale_shift(
    amplitude: Amplitude, scalar: int, exponent: int
) -> Amplitude:
    return tuple(poly_scale_shift(poly, scalar, exponent) for poly in amplitude)


def unit_amplitude(root: str) -> Amplitude:
    if root not in ROOTS:
        raise ValueError(f"unknown root {root!r}")
    return tuple((1,) if name == root else (0,) for name in ROOTS)


def tagged_children(
    graph: eg.Graph,
    q: int,
) -> Iterable[tuple[str, eg.Graph, int, int]]:
    """Yield ``(block, child, child_q, integer_multiplier)``.

    This repeats the three formulas in ``eg.differentiate_graph`` only to
    expose their block labels.  The test suite compares the complete untagged
    child multiset against the parent implementation on every reachable graph
    through the configured regression order.
    """
    edge0 = Counter({(p, i): multiplicity for p, i, multiplicity in graph.edges})

    # D_a: differentiate a readout factor c_p**power.
    for p, power in enumerate(graph.c):
        if power == 0:
            continue
        c = list(graph.c)
        x = list(graph.x) + [1, 1]
        c[p] -= 1
        edges = edge0.copy()
        i1, i2 = len(graph.x), len(graph.x) + 1
        edges[(p, i1)] += 1
        edges[(p, i2)] += 1
        yield "a", eg.graph_from(c, x, edges), q, power

    # D_u: differentiate x_i**power, where x_i=u_i**2.
    for i, power in enumerate(graph.x):
        if power == 0:
            continue
        c = list(graph.c) + [1]
        x = list(graph.x) + [1]
        pnew, inew = len(graph.c), len(graph.x)
        edges = edge0.copy()
        edges[(pnew, i)] += 1
        edges[(pnew, inew)] += 1
        yield "u", eg.graph_from(c, x, edges), q, 8 * power

    # D_W: differentiate one B_pi occurrence.
    for p, i, multiplicity in graph.edges:
        c = list(graph.c)
        x = list(graph.x) + [1]
        c[p] += 1
        x[i] += 1
        inew = len(graph.x)
        edges = edge0.copy()
        edges[(p, i)] -= 1
        if not edges[(p, i)]:
            del edges[(p, i)]
        edges[(p, inew)] += 1
        yield "w", eg.graph_from(c, x, edges), q + 1, 2 * multiplicity


def add_term(
    destination: dict,
    graph: eg.Graph,
    q: int,
    amplitude: Amplitude,
) -> None:
    if amplitude == ZERO_AMPLITUDE:
        return
    key = (q, eg.canonical_key(graph))
    if key in destination:
        old_graph, old_amplitude = destination[key]
        merged = amplitude_add(old_amplitude, amplitude)
        if merged == ZERO_AMPLITUDE:
            del destination[key]
        else:
            destination[key] = (old_graph, merged)
    else:
        destination[key] = (graph, amplitude)


def initial_observables() -> dict:
    """Return the output, first norm, and second norm on one DAG.

    ``q`` is the explicit power of ``n^{-1}`` used by the accepted compiler.
    The roots are

      f  = n^{-1} sum_pij c_p B_pi B_pj x_i x_j,
      q1 = n^{-1} sum_i x_i,
      q2 = n^{-1} sum_pij B_pi B_pj x_i x_j.
    """
    result: dict = {}

    output = eg.Graph((1,), (1, 1), ((0, 0, 1), (0, 1, 1)))
    add_term(result, output, 1, unit_amplitude("f"))

    first_norm = eg.Graph((), (1,), ())
    add_term(result, first_norm, 1, unit_amplitude("q1"))

    second_norm = eg.Graph((0,), (1, 1), ((0, 0, 1), (0, 1, 1)))
    add_term(result, second_norm, 1, unit_amplitude("q2"))
    return result


def differentiate(
    polynomial: dict,
    metric_exponents: dict[str, int],
) -> dict:
    if set(metric_exponents) != {"a", "u", "w"}:
        raise ValueError("metric_exponents must have exactly the keys a, u, w")
    if any(value < 0 for value in metric_exponents.values()):
        raise ValueError("metric exponents must be nonnegative")

    result: dict = {}
    for (q, _), (graph, amplitude) in polynomial.items():
        for block, child, child_q, multiplier in tagged_children(graph, q):
            child_amplitude = amplitude_scale_shift(
                amplitude,
                multiplier,
                metric_exponents[block],
            )
            add_term(result, child, child_q, child_amplitude)
    return result


def expected_large_n(polynomial: dict) -> dict[str, Polynomial]:
    """Contract the DAG once and return one exact lambda polynomial per root."""
    totals = [Counter() for _ in ROOTS]
    for (q, key), (graph, amplitude) in polynomial.items():
        # Reuse the accepted leading-width contraction and all of its caches.
        base_value = eg.expected_large_n({(q, key): (graph, 1)})
        if not base_value:
            continue
        for root_index, poly in enumerate(amplitude):
            for exponent, coefficient in enumerate(poly):
                totals[root_index][exponent] += base_value * coefficient

    return {
        root: trim(totals[index].get(exponent, 0)
                   for exponent in range(max(totals[index], default=0) + 1))
        for index, root in enumerate(ROOTS)
    }


def evaluate_polynomial(poly: Polynomial, value: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def project_root_at_integer(polynomial: dict, root: str, value: int) -> dict:
    """Project a vector DAG to one scalar root after integer substitution."""
    root_index = ROOTS.index(root)
    result = {}
    for key, (graph, amplitude) in polynomial.items():
        coefficient = evaluate_polynomial(amplitude[root_index], value)
        if coefficient:
            result[key] = (graph, coefficient)
    return result


def check_parent_children(polynomial: dict) -> None:
    """Assert exact agreement with the unmodified parent rewrite engine."""
    for (q, _), (graph, _) in polynomial.items():
        tagged = Counter(
            (child_q, eg.canonical_key(child), multiplier)
            for _, child, child_q, multiplier in tagged_children(graph, q)
        )
        parent = Counter(
            (child_q, eg.canonical_key(child), multiplier)
            for child, child_q, multiplier in eg.differentiate_graph(graph, q)
        )
        if tagged != parent:
            raise AssertionError("tagged rewrite differs from parent compiler")


def component_cache_census(polynomial: dict) -> dict:
    """Measure exact connected-component cache sharing between roots.

    Whole forests from different roots need not coincide.  The connected MFP
    recurrence nevertheless reuses any canonical component with the same
    Wick target.  This census measures that lower-level, mathematically valid
    sharing without assuming that the full forest states collide.
    """
    by_root: list[set] = [set() for _ in ROOTS]
    for (_, _), (graph, amplitude) in polynomial.items():
        component_keys = {
            (1 + component.edge_count // 2, eg.canonical_key(component))
            for component in eg.connected_component_graphs(graph)
        }
        for root_index, poly in enumerate(amplitude):
            if poly != (0,):
                by_root[root_index].update(component_keys)

    union = set().union(*by_root)
    shared = sum(1 for key in union if sum(key in keys for keys in by_root) > 1)
    return {
        "per_root": [len(keys) for keys in by_root],
        "union": len(union),
        "shared_by_at_least_two_roots": shared,
        "duplicate_evaluations_avoided": sum(map(len, by_root)) - len(union),
    }


def run(
    max_order: int,
    metric_exponents: dict[str, int] | None = None,
    verify_parent_rewrites: bool = False,
) -> dict:
    if max_order < 0:
        raise ValueError("max_order must be nonnegative")
    if metric_exponents is None:
        metric_exponents = {"a": 0, "u": 1, "w": 1}

    polynomial = initial_observables()
    jets: dict[str, list[Polynomial]] = {root: [] for root in ROOTS}
    graph_counts: list[int] = []
    overlap_counts: list[int] = []
    component_census: list[dict] = []

    for order in range(max_order + 1):
        if verify_parent_rewrites and order < max_order:
            check_parent_children(polynomial)
        expected = expected_large_n(polynomial)
        for root in ROOTS:
            jets[root].append(expected[root])
        graph_counts.append(len(polynomial))
        overlap_counts.append(sum(
            1 for _, amplitude in polynomial.values()
            if sum(poly != (0,) for poly in amplitude) > 1
        ))
        component_census.append(component_cache_census(polynomial))
        if order < max_order:
            polynomial = differentiate(polynomial, metric_exponents)

    return {
        "schema_version": 1,
        "max_order": max_order,
        "metric_exponents": dict(metric_exponents),
        "metric_line": (
            "D_lambda = lambda^a D_a + lambda^u D_u + lambda^w D_W"
        ),
        "roots": list(ROOTS),
        "graph_counts": graph_counts,
        "shared_state_counts": overlap_counts,
        "component_cache_census": component_census,
        "jets": {
            root: [list(poly) for poly in values]
            for root, values in jets.items()
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-order", type=int, default=3)
    parser.add_argument("--a-exponent", type=int, default=0)
    parser.add_argument("--u-exponent", type=int, default=1)
    parser.add_argument("--w-exponent", type=int, default=1)
    parser.add_argument("--verify-parent-rewrites", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = run(
        args.max_order,
        {
            "a": args.a_exponent,
            "u": args.u_exponent,
            "w": args.w_exponent,
        },
        verify_parent_rewrites=args.verify_parent_rewrites,
    )
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
        print(f"sha256={hashlib.sha256(encoded.encode()).hexdigest()}")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
