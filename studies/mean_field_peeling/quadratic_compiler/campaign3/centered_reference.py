#!/usr/bin/env python3
"""Transparent labelled-Wick oracle for Campaign 3.

The first hidden activation is

    phi_c(u) = u**2-c = X+t,   X=u**2-1,   t=1-c.

Raw derivative forests are expanded explicitly and every labelled Wick
pairing of the middle weights is enumerated.  Consequently this file is an
independent low-order oracle (used through order three), not the production
engine.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import argparse
import json
import math
from typing import Iterable


Poly = tuple[int, ...]  # coefficient of t**r


def trim(values: Iterable[int]) -> Poly:
    out = list(values)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out) if out else (0,)


def add(left: Poly, right: Poly) -> Poly:
    return trim(
        (left[i] if i < len(left) else 0)
        + (right[i] if i < len(right) else 0)
        for i in range(max(len(left), len(right)))
    )


def scale_shift(poly: Poly, scalar: int, shift: int = 0) -> Poly:
    if not scalar or poly == (0,):
        return (0,)
    return (0,) * shift + tuple(scalar * value for value in poly)


def multiply(left: Poly, right: Poly) -> Poly:
    if left == (0,) or right == (0,):
        return (0,)
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return trim(out)


def odd_double_factorial(k: int) -> int:
    if k <= 0:
        return 1
    return math.prod(range(k, 0, -2))


_centered_moments = [1, 0]


def centered_moment(power: int) -> int:
    """E[(U**2-1)**power], U standard Gaussian.

    The requested recurrence is C_0=1, C_1=0 and
    C_{p+1}=2p(C_p+C_{p-1}).
    """
    while len(_centered_moments) <= power:
        p = len(_centered_moments) - 1
        _centered_moments.append(
            2 * p * (_centered_moments[p] + _centered_moments[p - 1])
        )
    return _centered_moments[power]


@dataclass(frozen=True)
class Graph:
    a: tuple[int, ...]
    x: tuple[int, ...]
    edges: tuple[tuple[int, int], ...]  # labelled simple forest edges


def canonical_key(graph: Graph) -> tuple:
    rows = len(graph.a)
    count = rows + len(graph.x)
    neighbors = [[] for _ in range(count)]
    for u, v in graph.edges:
        neighbors[u].append(rows + v)
        neighbors[rows + v].append(u)

    def color(vertex: int):
        return (0, graph.a[vertex]) if vertex < rows else (1, graph.x[vertex-rows])

    def rooted(vertex: int, parent: int):
        return color(vertex), tuple(sorted(
            rooted(w, vertex) for w in neighbors[vertex] if w != parent
        ))

    seen: set[int] = set()
    components = []
    for seed in range(count):
        if seed in seen:
            continue
        vertices = [seed]
        seen.add(seed)
        for vertex in vertices:
            for w in neighbors[vertex]:
                if w not in seen:
                    seen.add(w)
                    vertices.append(w)
        if sum(len(neighbors[v]) for v in vertices) // 2 != len(vertices)-1:
            raise ValueError("derivative graph is not a forest")
        degree = {v: len(neighbors[v]) for v in vertices}
        leaves = [v for v in vertices if degree[v] <= 1]
        remaining = len(vertices)
        while remaining > 2:
            remaining -= len(leaves)
            following = []
            for v in leaves:
                degree[v] = 0
                for w in neighbors[v]:
                    if degree[w] > 0:
                        degree[w] -= 1
                        if degree[w] == 1:
                            following.append(w)
            leaves = following
        centers = leaves if leaves else vertices
        components.append(min(rooted(v, -1) for v in centers))
    return tuple(sorted(components))


def add_term(destination: dict, graph: Graph, q: int, coefficient: Poly) -> None:
    if coefficient == (0,):
        return
    key = (q, canonical_key(graph))
    if key in destination:
        old_graph, old = destination[key]
        destination[key] = old_graph, add(old, coefficient)
    else:
        destination[key] = graph, coefficient


def initial() -> dict:
    """Expand a W_i W_j (X_i+t)(X_j+t) exactly."""
    out = {}
    for left in (0, 1):       # 1 means X, 0 means the constant t
        for right in (0, 1):
            graph = Graph((1,), (left, right), ((0, 0), (0, 1)))
            add_term(out, graph, 1, (0,) * (2-left-right) + (1,))
    return out


def differentiated_children(graph: Graph, q: int):
    # D a_u^p = p a_u^(p-1) z_u^2.  Each z activation is X+t.
    for u, power in enumerate(graph.a):
        if not power:
            continue
        for left in (0, 1):
            for right in (0, 1):
                a = list(graph.a)
                a[u] -= 1
                x = list(graph.x)
                v0 = len(x)
                x.extend((left, right))
                edges = list(graph.edges) + [(u, v0), (u, v0+1)]
                shift = 2-left-right
                yield Graph(tuple(a), tuple(x), tuple(edges)), q, power, shift

    # D X_v^p = 8p X_v^(p-1)(X_v+1) a_new W_new,v z_new.
    for v, power in enumerate(graph.x):
        if not power:
            continue
        for same_increment in (0, 1):  # exponent p-1 or p
            for fresh in (0, 1):       # fresh z activation X+t
                a = list(graph.a) + [1]
                x = list(graph.x)
                x[v] = power - 1 + same_increment
                v1 = len(x)
                x.append(fresh)
                u1 = len(a)-1
                edges = list(graph.edges) + [(u1, v), (u1, v1)]
                yield Graph(tuple(a), tuple(x), tuple(edges)), q, 8*power, 1-fresh

    # D W_uv = 2 a_u z_u (X_v+t).  Remove the hit edge.  Expand both
    # affine activation factors, including the possibility of exponent zero.
    for edge_index, (u, v) in enumerate(graph.edges):
        for old_increment in (0, 1):
            for fresh in (0, 1):
                a = list(graph.a)
                a[u] += 1
                x = list(graph.x)
                x[v] += old_increment
                v1 = len(x)
                x.append(fresh)
                edges = list(graph.edges)
                del edges[edge_index]
                edges.append((u, v1))
                shift = (1-old_increment) + (1-fresh)
                yield Graph(tuple(a), tuple(x), tuple(edges)), q+1, 2, shift


def differentiate(polynomial: dict) -> dict:
    out = {}
    for (q, _), (graph, coefficient) in polynomial.items():
        for child, child_q, scalar, shift in differentiated_children(graph, q):
            add_term(out, child, child_q, scale_shift(coefficient, scalar, shift))
    return out


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def root(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> None:
        x, y = self.root(x), self.root(y)
        if x != y:
            self.parent[y] = x


def exhaustive_wick(graph: Graph, q: int) -> int:
    """Enumerate labelled pairings and retain precisely leading width."""
    if len(graph.edges) % 2:
        return 0
    edges = graph.edges
    rows, cols = len(graph.a), len(graph.x)
    total = 0

    def pairings(rest: tuple[int, ...], pairs: tuple[tuple[int, int], ...]):
        nonlocal total
        if not rest:
            row_dsu, col_dsu = DSU(rows), DSU(cols)
            for first, second in pairs:
                u0, v0 = edges[first]
                u1, v1 = edges[second]
                row_dsu.union(u0, u1)
                col_dsu.union(v0, v1)
            row_classes: dict[int, list[int]] = defaultdict(list)
            col_classes: dict[int, list[int]] = defaultdict(list)
            for u in range(rows):
                row_classes[row_dsu.root(u)].append(u)
            for v in range(cols):
                col_classes[col_dsu.root(v)].append(v)
            if len(row_classes) + len(col_classes) != q + len(pairs):
                return
            value = 1
            for vertices in row_classes.values():
                power = sum(graph.a[u] for u in vertices)
                if power % 2:
                    return
                value *= odd_double_factorial(power-1)
            for vertices in col_classes.values():
                power = sum(graph.x[v] for v in vertices)
                value *= centered_moment(power)
                if not value:
                    return
            total += value
            return
        first = rest[0]
        for position in range(1, len(rest)):
            second = rest[position]
            pairings(rest[1:position] + rest[position+1:], pairs+((first, second),))

    pairings(tuple(range(len(edges))), ())
    return total


def expectation(polynomial: dict) -> Poly:
    total = (0,)
    for (q, _), (graph, coefficient) in polynomial.items():
        total = add(total, scale_shift(coefficient, exhaustive_wick(graph, q)))
    return total


def run(max_order: int = 3) -> dict:
    polynomial = initial()
    jets = []
    state_counts = []
    for order in range(max_order+1):
        jets.append(list(expectation(polynomial)))
        state_counts.append(len(polynomial))
        if order < max_order:
            polynomial = differentiate(polynomial)
    return {
        "schema_version": 1,
        "parameter": "t=1-c; phi_c(u)=X+t; X=u^2-1",
        "method": "transparent labelled-Wick forest expansion",
        "max_order": max_order,
        "jets_t": jets,
        "state_counts": state_counts,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", type=int, default=3)
    args = parser.parse_args()
    print(json.dumps(run(args.order), indent=2))


if __name__ == "__main__":
    main()
