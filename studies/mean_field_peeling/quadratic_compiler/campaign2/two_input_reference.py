#!/usr/bin/env python3
"""Transparent exhaustive-Wick oracle for the Campaign-2 two-input jet.

This implementation deliberately favors auditability over speed.  Raw
derivative forests are expanded explicitly.  Every W factor is labelled and
every Wick pairing is enumerated.  It is therefore used only through order
three and is mathematically independent of the quotient-Wick recursion used
by the production compiler.

Internally A=f1+sigma*f2 and Dtilde=2 D_sigma are used.  The returned desired
jet is E[D_sigma**k g_sigma] = E[Dtilde**k A] / 2**(k+1).
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
import argparse
import json
import math
from typing import Iterable


Poly = tuple[int, ...]  # coefficient of theta**r


def trim(p: Iterable[int]) -> Poly:
    a = list(p)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a) if a else (0,)


def add(p: Poly, q: Poly) -> Poly:
    return trim((p[i] if i < len(p) else 0) +
                (q[i] if i < len(q) else 0)
                for i in range(max(len(p), len(q))))


def scale_shift(p: Poly, c: int, r: int = 0) -> Poly:
    if c == 0 or p == (0,):
        return (0,)
    return (0,) * r + tuple(c * x for x in p)


def mul(p: Poly, q: Poly) -> Poly:
    if p == (0,) or q == (0,):
        return (0,)
    z = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            z[i + j] += x * y
    return trim(z)


def odd_df(k: int) -> int:
    if k <= 0:
        return 1
    return math.prod(range(k, 0, -2))


def bivariate_moment(p: int, q: int) -> Poly:
    """E[X**p Y**q] for standard Gaussians with correlation theta."""
    out = [0] * (min(p, q) + 1)
    for r in range(min(p, q) + 1):
        if (p - r) % 2 or (q - r) % 2:
            continue
        out[r] += (math.comb(p, r) * math.comb(q, r) * math.factorial(r)
                   * odd_df(p - r - 1) * odd_df(q - r - 1))
    return trim(out)


@dataclass(frozen=True)
class Graph:
    a: tuple[int, ...]
    h: tuple[tuple[int, int], ...]
    edges: tuple[tuple[int, int], ...]  # simple labelled forest edges


def canonical_key(g: Graph) -> tuple:
    """Exact AHU code for a colored bipartite forest."""
    na = len(g.a)
    n = na + len(g.h)
    nb = [[] for _ in range(n)]
    for u, v in g.edges:
        nb[u].append(na + v)
        nb[na + v].append(u)

    def color(v: int):
        return (0, g.a[v]) if v < na else (1, *g.h[v - na])

    def rooted(v: int, parent: int):
        return color(v), tuple(sorted(rooted(w, v) for w in nb[v]
                                      if w != parent))

    seen: set[int] = set()
    components = []
    for seed in range(n):
        if seed in seen:
            continue
        stack = [seed]
        seen.add(seed)
        vertices = []
        while stack:
            v = stack.pop()
            vertices.append(v)
            for w in nb[v]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        if sum(len(nb[v]) for v in vertices) // 2 != len(vertices) - 1:
            raise ValueError("raw derivative graph is not a forest")
        degree = {v: len(nb[v]) for v in vertices}
        leaves = [v for v in vertices if degree[v] <= 1]
        remaining = len(vertices)
        while remaining > 2:
            remaining -= len(leaves)
            nxt = []
            for v in leaves:
                degree[v] = 0
                for w in nb[v]:
                    if degree[w] > 0:
                        degree[w] -= 1
                        if degree[w] == 1:
                            nxt.append(w)
            leaves = nxt
        centers = leaves if leaves else vertices
        components.append(min(rooted(v, -1) for v in centers))
    return tuple(sorted(components))


def add_term(dst: dict, graph: Graph, q: int, coefficient: Poly) -> None:
    if coefficient == (0,):
        return
    key = (q, canonical_key(graph))
    if key in dst:
        old, old_coefficient = dst[key]
        dst[key] = (old, add(old_coefficient, coefficient))
    else:
        dst[key] = (graph, coefficient)


def initial(sigma: int) -> dict:
    out = {}
    for alpha in (0, 1):
        h = [(0, 0), (0, 0)]
        h[0] = (2, 0) if alpha == 0 else (0, 2)
        h[1] = h[0]
        g = Graph((1,), tuple(h), ((0, 0), (0, 1)))
        add_term(out, g, 1, (1 if alpha == 0 else sigma,))
    return out


def differentiated_children(g: Graph, q: int, sigma: int):
    signs = (1, sigma)

    # Dtilde a: a_p' = sum_alpha signs[alpha] (z_p^alpha)^2.
    for u, power in enumerate(g.a):
        if not power:
            continue
        for alpha in (0, 1):
            a = list(g.a)
            a[u] -= 1
            h = list(g.h)
            e = [0, 0]
            e[alpha] = 2
            v0 = len(h)
            h.extend([tuple(e), tuple(e)])
            edges = list(g.edges) + [(u, v0), (u, v0 + 1)]
            yield Graph(tuple(a), tuple(h), tuple(edges)), q, power * signs[alpha], 0

    # Dtilde u_beta = 4 sum_alpha Q_beta,alpha signs[alpha] u_alpha (...).
    for v, exponents in enumerate(g.h):
        for beta in (0, 1):
            if not exponents[beta]:
                continue
            for alpha in (0, 1):
                a = list(g.a) + [1]
                h = list(g.h)
                here = list(h[v])
                here[beta] -= 1
                here[alpha] += 1
                h[v] = tuple(here)
                fresh = [0, 0]
                fresh[alpha] = 2
                v1 = len(h)
                h.append(tuple(fresh))
                u1 = len(a) - 1
                edges = list(g.edges) + [(u1, v), (u1, v1)]
                theta_power = int(alpha != beta)
                coefficient = 4 * exponents[beta] * signs[alpha]
                yield Graph(tuple(a), tuple(h), tuple(edges)), q, coefficient, theta_power

    # Dtilde W_pv = 2 a_p sum_alpha signs[alpha] z_p^alpha (u_v^alpha)^2 / n.
    for edge_index, (u, v) in enumerate(g.edges):
        for alpha in (0, 1):
            a = list(g.a)
            a[u] += 1
            h = list(g.h)
            here = list(h[v])
            here[alpha] += 2
            h[v] = tuple(here)
            fresh = [0, 0]
            fresh[alpha] = 2
            v1 = len(h)
            h.append(tuple(fresh))
            edges = list(g.edges)
            del edges[edge_index]
            edges.append((u, v1))
            yield Graph(tuple(a), tuple(h), tuple(edges)), q + 1, 2 * signs[alpha], 0


def differentiate(polynomial: dict, sigma: int) -> dict:
    out = {}
    for (q, _), (g, coefficient) in polynomial.items():
        for child, child_q, c, r in differentiated_children(g, q, sigma):
            add_term(out, child, child_q, scale_shift(coefficient, c, r))
    return out


class DSU:
    def __init__(self, n: int):
        self.p = list(range(n))

    def root(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, x: int, y: int) -> None:
        x, y = self.root(x), self.root(y)
        if x != y:
            self.p[y] = x


def exhaustive_wick(g: Graph, q: int) -> Poly:
    if len(g.edges) % 2:
        return (0,)
    na, nh = len(g.a), len(g.h)
    edges = list(g.edges)
    total = (0,)

    def pairings(rest: tuple[int, ...], pairs: tuple[tuple[int, int], ...]):
        nonlocal total
        if not rest:
            dsu_r, dsu_h = DSU(na), DSU(nh)
            for x, y in pairs:
                ux, vx = edges[x]
                uy, vy = edges[y]
                dsu_r.union(ux, uy)
                dsu_h.union(vx, vy)
            row_classes = defaultdict(list)
            col_classes = defaultdict(list)
            for u in range(na):
                row_classes[dsu_r.root(u)].append(u)
            for v in range(nh):
                col_classes[dsu_h.root(v)].append(v)
            # Each W covariance is 1/n.  Retain exactly the n^0 terms.
            if len(row_classes) + len(col_classes) != q + len(pairs):
                return
            value = (1,)
            for vertices in row_classes.values():
                power = sum(g.a[u] for u in vertices)
                if power % 2:
                    return
                value = scale_shift(value, odd_df(power - 1))
            for vertices in col_classes.values():
                p = sum(g.h[v][0] for v in vertices)
                r = sum(g.h[v][1] for v in vertices)
                value = mul(value, bivariate_moment(p, r))
            total = add(total, value)
            return
        x = rest[0]
        for position in range(1, len(rest)):
            y = rest[position]
            pairings(rest[1:position] + rest[position + 1:], pairs + ((x, y),))

    pairings(tuple(range(len(edges))), ())
    return total


def expectation(polynomial: dict) -> Poly:
    total = (0,)
    for (q, _), (g, coefficient) in polynomial.items():
        total = add(total, mul(coefficient, exhaustive_wick(g, q)))
    return total


def run(sigma: int, max_order: int = 3):
    polynomial = initial(sigma)
    raw = []
    desired = []
    for k in range(max_order + 1):
        value = expectation(polynomial)
        raw.append(value)
        divisor = 2 ** (k + 1)
        fractions = tuple(Fraction(x, divisor) for x in value)
        if any(x.denominator != 1 for x in fractions):
            raise ArithmeticError(f"nonintegral normalized jet at order {k}")
        desired.append(tuple(x.numerator for x in fractions))
        polynomial = differentiate(polynomial, sigma)
    return raw, desired


def theta_to_t(poly: Poly) -> tuple[int, ...]:
    if any(poly[i] for i in range(1, len(poly), 2)):
        raise ValueError("answer is not even in theta")
    return trim(poly[::2])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", type=int, default=3)
    args = parser.parse_args()
    result = {}
    for sigma, name in ((1, "plus"), (-1, "minus")):
        raw, desired = run(sigma, args.order)
        result[name] = {
            "raw_theta": [list(x) for x in raw],
            "desired_t": [list(theta_to_t(x)) for x in desired],
        }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

