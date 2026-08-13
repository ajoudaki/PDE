#!/usr/bin/env python3
"""Transparent labelled-Wick oracle for Campaign 5.

The implementation expands derivative forests explicitly, labels every
middle-weight edge, and enumerates every Gaussian Wick pairing.  It is used
only through order three.  Internally A=sum_alpha f_alpha and
Dtilde=B*D=n grad(A).grad are used, so the desired order-k jet is the raw
expectation divided by B**(k+1).
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
import argparse
import json
from typing import Iterable


Poly = tuple[int, ...]  # coefficient of rho**r


def trim(values: Iterable[int]) -> Poly:
    values = list(values)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values) if values else (0,)


def add(left: Poly, right: Poly) -> Poly:
    return trim(
        (left[q] if q < len(left) else 0)
        + (right[q] if q < len(right) else 0)
        for q in range(max(len(left), len(right)))
    )


def scale_shift(poly: Poly, scale: int, shift: int = 0) -> Poly:
    if scale == 0 or poly == (0,):
        return (0,)
    return (0,) * shift + tuple(scale * value for value in poly)


def multiply(left: Poly, right: Poly) -> Poly:
    if left == (0,) or right == (0,):
        return (0,)
    result = [0] * (len(left) + len(right) - 1)
    for q, x in enumerate(left):
        for r, y in enumerate(right):
            result[q + r] += x * y
    return trim(result)


def equicorrelated_moment(exponents: tuple[int, ...]) -> Poly:
    """Direct labelled Gaussian pairing for a common off-diagonal rho."""
    labels = tuple(
        color for color, power in enumerate(exponents) for _ in range(power)
    )
    if len(labels) % 2:
        return (0,)

    def pair(rest: tuple[int, ...]) -> Poly:
        if not rest:
            return (1,)
        first = rest[0]
        total = (0,)
        for position in range(1, len(rest)):
            second = rest[position]
            child = rest[1:position] + rest[position + 1 :]
            total = add(total, scale_shift(pair(child), 1, first != second))
        return total

    return pair(labels)


@dataclass(frozen=True)
class Graph:
    a: tuple[int, ...]
    h: tuple[tuple[int, ...], ...]
    edges: tuple[tuple[int, int], ...]  # labelled forest edges


def _canonical_for_color_permutation(graph: Graph, permutation: tuple[int, ...]):
    rows = len(graph.a)
    vertices = rows + len(graph.h)
    neighbors = [[] for _ in range(vertices)]
    for u, v in graph.edges:
        neighbors[u].append(rows + v)
        neighbors[rows + v].append(u)

    def color(vertex: int):
        if vertex < rows:
            return (0, graph.a[vertex])
        raw = graph.h[vertex - rows]
        return (1, *(raw[q] for q in permutation))

    def rooted(vertex: int, parent: int):
        return (
            color(vertex),
            tuple(sorted(rooted(child, vertex) for child in neighbors[vertex]
                         if child != parent)),
        )

    seen: set[int] = set()
    components = []
    for seed in range(vertices):
        if seed in seen:
            continue
        stack = [seed]
        seen.add(seed)
        component = []
        while stack:
            vertex = stack.pop()
            component.append(vertex)
            for child in neighbors[vertex]:
                if child not in seen:
                    seen.add(child)
                    stack.append(child)
        if sum(len(neighbors[v]) for v in component) // 2 != len(component) - 1:
            raise ValueError("raw derivative graph is not a forest")
        degree = {v: len(neighbors[v]) for v in component}
        leaves = [v for v in component if degree[v] <= 1]
        remaining = len(component)
        while remaining > 2:
            remaining -= len(leaves)
            following = []
            for vertex in leaves:
                degree[vertex] = 0
                for child in neighbors[vertex]:
                    if degree[child] > 0:
                        degree[child] -= 1
                        if degree[child] == 1:
                            following.append(child)
            leaves = following
        centers = leaves if leaves else component
        components.append(min(rooted(v, -1) for v in centers))
    return tuple(sorted(components))


def canonical_key(graph: Graph) -> tuple:
    # Keep color labels explicit here.  This makes the oracle structurally
    # independent of the production compiler's symmetry quotient.
    colors = len(graph.h[0]) if graph.h else 1
    return _canonical_for_color_permutation(graph, tuple(range(colors)))


def add_term(destination: dict, graph: Graph, width_power: int,
             coefficient: Poly) -> None:
    if coefficient == (0,):
        return
    key = (width_power, canonical_key(graph))
    if key in destination:
        old_graph, old_coefficient = destination[key]
        destination[key] = (old_graph, add(old_coefficient, coefficient))
    else:
        destination[key] = (graph, coefficient)


def initial(colors: int) -> dict:
    output = {}
    for alpha in range(colors):
        exponent = tuple(2 if q == alpha else 0 for q in range(colors))
        graph = Graph((1,), (exponent, exponent), ((0, 0), (0, 1)))
        add_term(output, graph, 1, (1,))
    return output


def differentiated_children(graph: Graph, width_power: int):
    colors = len(graph.h[0])

    # Dtilde a: a_p' = sum_alpha (z_p^alpha)^2.
    for u, power in enumerate(graph.a):
        if not power:
            continue
        for alpha in range(colors):
            a = list(graph.a)
            a[u] -= 1
            h = list(graph.h)
            exponent = tuple(2 if q == alpha else 0 for q in range(colors))
            v0 = len(h)
            h.extend((exponent, exponent))
            edges = list(graph.edges) + [(u, v0), (u, v0 + 1)]
            yield Graph(tuple(a), tuple(h), tuple(edges)), width_power, power, 0

    # Dtilde u_beta includes G_beta,alpha: off-diagonal terms contribute rho.
    for v, exponents in enumerate(graph.h):
        for beta in range(colors):
            if not exponents[beta]:
                continue
            for alpha in range(colors):
                a = list(graph.a) + [1]
                h = list(graph.h)
                here = list(h[v])
                here[beta] -= 1
                here[alpha] += 1
                h[v] = tuple(here)
                fresh = tuple(2 if q == alpha else 0 for q in range(colors))
                v1 = len(h)
                h.append(fresh)
                u1 = len(a) - 1
                edges = list(graph.edges) + [(u1, v), (u1, v1)]
                yield (
                    Graph(tuple(a), tuple(h), tuple(edges)),
                    width_power,
                    4 * exponents[beta],
                    int(alpha != beta),
                )

    # Dtilde W.  Removing the hit edge raises the explicit width power by one.
    for edge_index, (u, v) in enumerate(graph.edges):
        for alpha in range(colors):
            a = list(graph.a)
            a[u] += 1
            h = list(graph.h)
            here = list(h[v])
            here[alpha] += 2
            h[v] = tuple(here)
            fresh = tuple(2 if q == alpha else 0 for q in range(colors))
            v1 = len(h)
            h.append(fresh)
            edges = list(graph.edges)
            del edges[edge_index]
            edges.append((u, v1))
            yield Graph(tuple(a), tuple(h), tuple(edges)), width_power + 1, 2, 0


def differentiate(polynomial: dict) -> dict:
    output = {}
    for (width_power, _), (graph, coefficient) in polynomial.items():
        for child, child_width, scale, shift in differentiated_children(
            graph, width_power
        ):
            add_term(output, child, child_width,
                     scale_shift(coefficient, scale, shift))
    return output


class DSU:
    def __init__(self, size: int):
        self.parent = list(range(size))

    def root(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> None:
        x, y = self.root(x), self.root(y)
        if x != y:
            self.parent[y] = x


def exhaustive_wick_terms(graph: Graph, width_power: int):
    """Yield each leading labelled-W pairing and its column-class moments."""
    if len(graph.edges) % 2:
        return
    rows, columns = len(graph.a), len(graph.h)
    edges = list(graph.edges)

    def pairings(rest: tuple[int, ...], pairs: tuple[tuple[int, int], ...]):
        if not rest:
            row_dsu, column_dsu = DSU(rows), DSU(columns)
            for first, second in pairs:
                u0, v0 = edges[first]
                u1, v1 = edges[second]
                row_dsu.union(u0, u1)
                column_dsu.union(v0, v1)
            row_classes = defaultdict(list)
            column_classes = defaultdict(list)
            for u in range(rows):
                row_classes[row_dsu.root(u)].append(u)
            for v in range(columns):
                column_classes[column_dsu.root(v)].append(v)
            if len(row_classes) + len(column_classes) != width_power + len(pairs):
                return
            value = (1,)
            for vertices in row_classes.values():
                power = sum(graph.a[u] for u in vertices)
                if power % 2:
                    return
                # Direct labelled pair count for one standard Gaussian.
                row_moment = equicorrelated_moment((power,))[0]
                value = scale_shift(value, row_moment)
            column_data = []
            for vertices in column_classes.values():
                exponents = tuple(
                    sum(graph.h[v][color] for v in vertices)
                    for color in range(len(graph.h[0]))
                )
                moment = equicorrelated_moment(exponents)
                column_data.append((exponents, moment))
                value = multiply(value, moment)
            yield pairs, value, column_data
            return
        first = rest[0]
        for position in range(1, len(rest)):
            second = rest[position]
            child = rest[1:position] + rest[position + 1 :]
            yield from pairings(child, pairs + ((first, second),))

    yield from pairings(tuple(range(len(edges))), ())


def exhaustive_wick(graph: Graph, width_power: int) -> Poly:
    total = (0,)
    for _, value, _ in exhaustive_wick_terms(graph, width_power):
        total = add(total, value)
    return total


def expectation(polynomial: dict) -> Poly:
    total = (0,)
    for (width_power, _), (graph, coefficient) in polynomial.items():
        total = add(total, multiply(coefficient,
                                    exhaustive_wick(graph, width_power)))
    return total


def normalize(raw: Poly, colors: int, order: int) -> tuple[Fraction, ...]:
    return tuple(Fraction(value, colors ** (order + 1)) for value in raw)


def run(colors: int = 3, max_order: int = 3):
    if colors not in (2, 3):
        raise ValueError("reference supports only two or three colors")
    polynomial = initial(colors)
    raw = []
    desired = []
    stages = []
    for order in range(max_order + 1):
        value = expectation(polynomial)
        raw.append(value)
        desired.append(normalize(value, colors, order))
        stages.append(polynomial)
        polynomial = differentiate(polynomial)
    return raw, desired, stages


def three_color_witness(stage_three: dict) -> dict:
    """Return a concrete leading terminal contraction with an odd rho term."""
    for (width_power, _), (graph, source) in stage_three.items():
        color_totals = tuple(
            sum(column[color] for column in graph.h) for color in range(3)
        )
        if any(total == 0 for total in color_totals):
            continue
        for pairs, terminal, columns in exhaustive_wick_terms(graph, width_power):
            triangle_columns = [
                (exponents, moment) for exponents, moment in columns
                if all(power > 0 for power in exponents)
                and any(moment[q] for q in range(1, len(moment), 2))
            ]
            if not triangle_columns:
                continue
            contribution = multiply(source, terminal)
            if contribution == (0,):
                continue
            return {
                "width_power": width_power,
                "a": list(graph.a),
                "h": [list(x) for x in graph.h],
                "edges": [list(x) for x in graph.edges],
                "color_totals": list(color_totals),
                "source_polynomial": list(source),
                "weight_pairing": [list(x) for x in pairs],
                "terminal_column_classes": [
                    {"exponents": list(exponents), "moment": list(moment)}
                    for exponents, moment in columns
                ],
                "triangle_columns": [
                    {"exponents": list(exponents), "moment": list(moment)}
                    for exponents, moment in triangle_columns
                ],
                "terminal_polynomial": list(terminal),
                "contribution_polynomial": list(contribution),
            }
    raise ArithmeticError("no explicit nonzero three-color terminal sector found")


def fraction_json(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--colors", type=int, choices=(2, 3), default=3)
    parser.add_argument("--order", type=int, default=3)
    args = parser.parse_args()
    raw, desired, stages = run(args.colors, args.order)
    output = {
        "colors": args.colors,
        "raw_rho": [list(poly) for poly in raw],
        "desired_rho": [
            [fraction_json(value) for value in poly] for poly in desired
        ],
    }
    if args.colors == 3 and args.order >= 3:
        output["three_color_witness"] = three_color_witness(stages[3])
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
