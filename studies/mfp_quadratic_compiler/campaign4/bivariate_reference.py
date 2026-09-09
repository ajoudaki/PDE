#!/usr/bin/env python3
"""Transparent whole-forest oracle for Campaign 4.

This route carries exact coefficients in the two independent metric
parameters but otherwise deliberately uses the accepted whole-forest
``exact_graph_wick`` contraction.  It is restricted to low order and is
independent of the connected double-graded production recurrence.
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import sys
from typing import Iterable


COMPILER = Path(__file__).resolve().parents[1]
if str(COMPILER) not in sys.path:
    sys.path.insert(0, str(COMPILER))

import exact_graph_wick as eg  # noqa: E402


Monomial = tuple[int, int]  # (alpha power, beta power)
Bivariate = dict[Monomial, int]


def add_polynomial(left: Bivariate, right: Bivariate) -> Bivariate:
    out = Counter(left)
    out.update(right)
    return {monomial: value for monomial, value in out.items() if value}


def scale_shift(poly: Bivariate, scalar: int, da: int, db: int) -> Bivariate:
    if not scalar:
        return {}
    return {
        (a + da, b + db): scalar * value
        for (a, b), value in poly.items()
        if value
    }


def evaluate(poly: Bivariate, alpha: int, beta: int) -> int:
    return sum(value * alpha**a * beta**b
               for (a, b), value in poly.items())


def add_term(destination: dict, graph: eg.Graph, q: int,
             coefficient: Bivariate) -> None:
    if not coefficient:
        return
    key = (q, eg.canonical_key(graph))
    if key in destination:
        old_graph, old = destination[key]
        destination[key] = old_graph, add_polynomial(old, coefficient)
    else:
        destination[key] = graph, coefficient


def initial() -> dict:
    graph = eg.Graph((1,), (1, 1), ((0, 0, 1), (0, 1, 1)))
    out = {}
    add_term(out, graph, 1, {(0, 0): 1})
    return out


def differentiated_children(graph: eg.Graph, q: int):
    edges0 = Counter({(u, v): multiplicity
                      for u, v, multiplicity in graph.edges})

    # Readout hit: D_a.
    for u, power in enumerate(graph.c):
        if not power:
            continue
        c = list(graph.c)
        x = list(graph.x) + [1, 1]
        c[u] -= 1
        edges = edges0.copy()
        v0 = len(graph.x)
        edges[(u, v0)] += 1
        edges[(u, v0 + 1)] += 1
        yield eg.graph_from(c, x, edges), q, power, 0, 0

    # First-hidden hit: alpha D_u.
    for v, power in enumerate(graph.x):
        if not power:
            continue
        c = list(graph.c) + [1]
        x = list(graph.x) + [1]
        u1, v1 = len(graph.c), len(graph.x)
        edges = edges0.copy()
        edges[(u1, v)] += 1
        edges[(u1, v1)] += 1
        yield eg.graph_from(c, x, edges), q, 8 * power, 1, 0

    # Middle-weight hit: beta D_W.
    for u, v, multiplicity in graph.edges:
        c = list(graph.c)
        x = list(graph.x) + [1]
        c[u] += 1
        x[v] += 1
        v1 = len(graph.x)
        edges = edges0.copy()
        edges[(u, v)] -= 1
        if not edges[(u, v)]:
            del edges[(u, v)]
        edges[(u, v1)] += 1
        yield eg.graph_from(c, x, edges), q + 1, 2 * multiplicity, 0, 1


def differentiate(polynomial: dict) -> dict:
    out = {}
    for (q, _), (graph, coefficient) in polynomial.items():
        for child, child_q, scalar, da, db in differentiated_children(graph, q):
            add_term(out, child, child_q,
                     scale_shift(coefficient, scalar, da, db))
    return out


def expectation(polynomial: dict) -> Bivariate:
    total: Bivariate = {}
    for (q, key), (graph, coefficient) in polynomial.items():
        contraction = eg.expected_large_n({(q, key): (graph, 1)})
        if contraction:
            total = add_polynomial(total,
                                   scale_shift(coefficient, contraction, 0, 0))
    return total


def records(poly: Bivariate) -> list[dict[str, str | int]]:
    return [
        {"alpha_power": a, "beta_power": b, "value": str(value)}
        for (a, b), value in sorted(poly.items())
    ]


def run(max_order: int = 5) -> dict:
    if max_order < 0 or max_order > 5:
        raise ValueError("transparent reference is capped at order five")
    polynomial = initial()
    jets = []
    states = []
    for order in range(max_order + 1):
        jets.append(records(expectation(polynomial)))
        states.append(len(polynomial))
        if order < max_order:
            polynomial = differentiate(polynomial)
    return {
        "schema_version": 1,
        "metric": "D_a + alpha D_u + beta D_W",
        "method": "whole-forest expansion with independent Wick contraction",
        "max_order": max_order,
        "jets": jets,
        "state_counts": states,
    }


def parse_records(values: Iterable[dict]) -> Bivariate:
    return {
        (int(record["alpha_power"]), int(record["beta_power"])):
        int(record["value"])
        for record in values
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", type=int, default=5)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.order)
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded)
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
