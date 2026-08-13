#!/usr/bin/env python3
"""Independent exact checks for exact_graph_wick.py.

This file deliberately does not call its recursive Wick contraction routine.
It provides:

1. a scalar n=1 recurrence on exponent triples (c,B,x), compared against the
   graph differentiation output with all labels identified;
2. a direct union-find enumeration of every B-edge pairing, used as a low-order
   independent check of the large-n Wick coefficient.
"""

from __future__ import annotations

import argparse
import functools
import math
from collections import Counter

import exact_graph_wick as eg


def scalar_step(poly: dict[tuple[int, int, int], int]) -> dict[tuple[int, int, int], int]:
    out = Counter()
    for (c, b, x), a in poly.items():
        # c'=B^2 x^2
        if c:
            out[(c - 1, b + 2, x + 2)] += a * c
        # B'=2 c B x^2 at n=1
        if b:
            out[(c + 1, b, x + 2)] += a * 2 * b
        # x'=8 c B^2 x^2
        if x:
            out[(c + 1, b + 2, x + 1)] += a * 8 * x
    return dict(out)


def scalar_expectation(poly: dict[tuple[int, int, int], int]) -> int:
    return sum(a * eg.normal_moment(c) * eg.normal_moment(b) * eg.normal_moment(2 * x)
               for (c, b, x), a in poly.items())


def graph_n1_expectation(poly: dict) -> int:
    ans = 0
    for (_, _), (g, a) in poly.items():
        ans += a * eg.normal_moment(sum(g.c)) * eg.normal_moment(g.edge_count) * eg.normal_moment(2 * sum(g.x))
    return ans


class DSU:
    def __init__(self, n: int):
        self.p = list(range(n))

    def copy(self):
        z = DSU(0)
        z.p = self.p.copy()
        return z

    def find(self, a: int) -> int:
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a

    def union(self, a: int, b: int) -> None:
        a, b = self.find(a), self.find(b)
        if a != b:
            self.p[b] = a


def final_weight_from_dsu(g: eg.Graph, pd: DSU, id_: DSU, target: int) -> int:
    pc = Counter()
    ix = Counter()
    for p, w in enumerate(g.c):
        pc[pd.find(p)] += w
    for i, w in enumerate(g.x):
        ix[id_.find(i)] += w
    evens = [w for w in pc.values() if w % 2 == 0]
    odds = sorted(w for w in pc.values() if w % 2)
    if len(odds) % 2:
        return 0
    degree = len(ix) + len(evens) + len(odds) // 2
    if degree != target:
        if degree > target:
            raise ArithmeticError((degree, target))
        return 0
    ans = math.prod(eg.normal_moment(2 * w) for w in ix.values())
    ans *= math.prod(eg.normal_moment(w) for w in evens)

    @functools.lru_cache(None)
    def rec(ws):
        if not ws:
            return 1
        total = 0
        for j in range(1, len(ws)):
            total += eg.normal_moment(ws[0] + ws[j]) * rec(ws[1:j] + ws[j + 1:])
        return total

    return ans * rec(tuple(odds))


def direct_pairing_graph(g: eg.Graph, target: int) -> int:
    edges = [(p, i) for p, i, m in g.edges for _ in range(m)]
    if len(edges) % 2:
        return 0

    def rec(rem: tuple[int, ...], pd: DSU, id_: DSU) -> int:
        if not rem:
            return final_weight_from_dsu(g, pd, id_, target)
        a = rem[0]
        total = 0
        for j in range(1, len(rem)):
            b = rem[j]
            p2, i2 = pd.copy(), id_.copy()
            p2.union(edges[a][0], edges[b][0])
            i2.union(edges[a][1], edges[b][1])
            total += rec(rem[1:j] + rem[j + 1:], p2, i2)
        return total

    return rec(tuple(range(len(edges))), DSU(len(g.c)), DSU(len(g.x)))


def direct_large_n(poly: dict) -> int:
    total = 0
    for (q, _), (g, a) in poly.items():
        total += a * direct_pairing_graph(g, q + g.edge_count // 2)
    return total


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-order", type=int, default=5)
    ap.add_argument("--direct-wick-through", type=int, default=3)
    args = ap.parse_args()

    scalar = {(1, 2, 2): 1}
    graphs = eg.initial_observable()
    for order in range(args.max_order + 1):
        s1 = scalar_expectation(scalar)
        s2 = graph_n1_expectation(graphs)
        assert s1 == s2, (order, s1, s2)
        line = {"order": order, "n1": str(s1), "graphs": len(graphs)}
        if order <= args.direct_wick_through:
            brute = direct_large_n(graphs)
            fast = eg.expected_large_n(graphs)
            assert brute == fast, (order, brute, fast)
            line["large_n_direct_pairings"] = str(brute)
        print(line, flush=True)
        scalar = scalar_step(scalar)
        graphs = eg.differentiate(graphs)


if __name__ == "__main__":
    main()
