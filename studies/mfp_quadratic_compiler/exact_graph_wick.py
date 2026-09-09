#!/usr/bin/env python3
"""Exact large-n Taylor/Wick enumeration for the formal Stieltjes test.

The state variables are x_i=u_i^2, c_p, and B_{pi}.  A summed monomial is
stored as a weighted bipartite multigraph.  The integer ``q`` records an
explicit factor n^{-q}.  Time differentiation is by the exact local rules

  x_i'    = 8 x_i sum_{p,j} B_{pi} B_{pj} c_p x_j,
  B_{pi}' = (2/n) sum_j c_p B_{pj} x_j x_i,
  c_p'    = sum_{i,j} B_{pi} B_{pj} x_i x_j.

At t=0, B edges are paired by Wick's rule.  Every pair merges both endpoints
and supplies n^{-1}.  The n^0 coefficient is then obtained exactly from the
Gaussian moments of c and u.  All arithmetic is over Python integers.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import math
import pickle
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


_TREE_SIG_TO_ID: dict[tuple, int] = {}
_TREE_ID_TO_SIG: list[tuple] = []


def _intern_tree(sig: tuple) -> int:
    found = _TREE_SIG_TO_ID.get(sig)
    if found is not None:
        return found
    found = len(_TREE_ID_TO_SIG)
    _TREE_SIG_TO_ID[sig] = found
    _TREE_ID_TO_SIG.append(sig)
    return found


@dataclass(frozen=True)
class Graph:
    """A summed monomial, without its scalar coefficient or n power."""

    c: tuple[int, ...]
    x: tuple[int, ...]
    # (p, i, multiplicity), sorted, multiplicities positive
    edges: tuple[tuple[int, int, int], ...]

    @property
    def edge_count(self) -> int:
        return sum(m for _, _, m in self.edges)


def odd_double_factorial_from_half_power(a: int) -> int:
    """E[u^(2a)] for u standard normal."""
    if a == 0:
        return 1
    return math.prod(range(1, 2 * a, 2))


def normal_moment(power: int) -> int:
    if power & 1:
        return 0
    return odd_double_factorial_from_half_power(power // 2)


def graph_from(c: list[int], x: list[int], edge_counter: Counter) -> Graph:
    return Graph(tuple(c), tuple(x), tuple(sorted((p, i, m) for (p, i), m in edge_counter.items() if m)))


def adjacency(g: Graph) -> list[list[int]]:
    n_p, n_i = len(g.c), len(g.x)
    a = [[0] * (n_p + n_i) for _ in range(n_p + n_i)]
    for p, i, m in g.edges:
        j = n_p + i
        a[p][j] = a[j][p] = m
    return a


def _forest_canonical_codes(g: Graph) -> tuple | None:
    """Linear-time colored-forest canonical code, or None for a nonforest.

    Every graph produced by differentiation before Wick contraction is a
    forest with simple edges.  Exploiting that fact avoids exponential generic
    graph individualization in the high (p=11,12) Wick sectors.
    """
    n_p, n_i = len(g.c), len(g.x)
    n = n_p + n_i
    if any(m != 1 for _, _, m in g.edges):
        return None
    nb = [[] for _ in range(n)]
    for p, i, _ in g.edges:
        j = n_p + i
        nb[p].append(j)
        nb[j].append(p)

    seen = set()
    components = []
    for start in range(n):
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        comp = []
        edge_twice = 0
        while stack:
            v = stack.pop()
            comp.append(v)
            edge_twice += len(nb[v])
            for w in nb[v]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        if edge_twice // 2 != len(comp) - 1:
            return None
        components.append(comp)

    def color(v):
        return (0, g.c[v]) if v < n_p else (1, g.x[v - n_p])

    def rooted(v, parent):
        children = [rooted(w, v) for w in nb[v] if w != parent]
        return _intern_tree((color(v), tuple(sorted(children))))

    def centers(comp):
        if len(comp) <= 2:
            return comp
        degree = {v: len(nb[v]) for v in comp}
        leaves = [v for v in comp if degree[v] <= 1]
        remaining = len(comp)
        while remaining > 2:
            remaining -= len(leaves)
            new = []
            for v in leaves:
                degree[v] = 0
                for w in nb[v]:
                    if degree[w] > 0:
                        degree[w] -= 1
                        if degree[w] == 1:
                            new.append(w)
            leaves = new
        return leaves

    coded_components = []
    for comp in components:
        candidates = [rooted(v, -1) for v in centers(comp)]
        coded_components.append(min(candidates))
    return tuple(sorted(coded_components))


@functools.lru_cache(maxsize=None)
def connected_component_graphs(g: Graph) -> tuple[Graph, ...]:
    """Split a raw graph into connected components, including isolates."""
    n_p, n_i = len(g.c), len(g.x)
    nbr = [[] for _ in range(n_p + n_i)]
    for p, i, _ in g.edges:
        j = n_p + i
        nbr[p].append(j)
        nbr[j].append(p)
    seen: set[int] = set()
    ans: list[Graph] = []
    for root in range(n_p + n_i):
        if root in seen:
            continue
        seen.add(root)
        stack = [root]
        verts: list[int] = []
        while stack:
            v = stack.pop()
            verts.append(v)
            for w in nbr[v]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        ps = sorted(v for v in verts if v < n_p)
        xs = sorted(v - n_p for v in verts if v >= n_p)
        pmap = {p: j for j, p in enumerate(ps)}
        xmap = {i: j for j, i in enumerate(xs)}
        e = Counter()
        for p, i, m in g.edges:
            if p in pmap and i in xmap:
                e[(pmap[p], xmap[i])] = m
        ans.append(graph_from([g.c[p] for p in ps], [g.x[i] for i in xs], e))
    return tuple(ans)


def _refine_partition(a: list[list[int]], cells: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    while True:
        where = {}
        for ci, cell in enumerate(cells):
            for v in cell:
                where[v] = ci
        changed = False
        out = []
        for cell in cells:
            buckets = defaultdict(list)
            for v in cell:
                sig = tuple(sum(a[v][w] for w in target) for target in cells)
                buckets[sig].append(v)
            if len(buckets) > 1:
                changed = True
            for sig in sorted(buckets):
                out.append(tuple(buckets[sig]))
        cells2 = tuple(out)
        if not changed:
            return cells2
        cells = cells2


@functools.lru_cache(maxsize=None)
def canonical_key(g: Graph) -> tuple:
    """Exact isomorphism key under separate p/i relabeling.

    A small individualization/refinement canonicalizer is enough here because
    derivative graphs are connected and vertex powers strongly color them.
    """
    forest_codes = _forest_canonical_codes(g)
    if forest_codes is not None:
        return ("F", forest_codes)

    a = adjacency(g)
    n_p = len(g.c)

    base = defaultdict(list)
    for p, w in enumerate(g.c):
        base[(0, w)].append(p)
    for i, w in enumerate(g.x):
        base[(1, w)].append(n_p + i)
    cells0 = tuple(tuple(base[k]) for k in sorted(base))

    best = None

    def encode(cells: tuple[tuple[int, ...], ...]) -> tuple:
        order = [cell[0] for cell in cells]
        weights = tuple((0, g.c[v]) if v < n_p else (1, g.x[v - n_p]) for v in order)
        upper = tuple(a[order[r]][order[s]] for r in range(len(order)) for s in range(r + 1, len(order)))
        return weights, upper

    def visit(cells: tuple[tuple[int, ...], ...]) -> None:
        nonlocal best
        cells = _refine_partition(a, cells)
        choices = [(len(cell), j) for j, cell in enumerate(cells) if len(cell) > 1]
        if not choices:
            code = encode(cells)
            if best is None or code < best:
                best = code
            return
        _, j = min(choices)
        cell = cells[j]
        # Vertices with identical complete adjacency rows are literal twins;
        # individualizing more than one of them repeats the same branch.
        seen_rows = set()
        for v in cell:
            row = tuple(a[v])
            if row in seen_rows:
                continue
            seen_rows.add(row)
            rest = tuple(w for w in cell if w != v)
            visit(cells[:j] + ((v,), rest) + cells[j + 1 :])

    visit(cells0)
    assert best is not None
    return best


@functools.lru_cache(maxsize=None)
def canonical_graph(g: Graph) -> Graph:
    """Return a canonically labelled representative reconstructed from its key."""
    key = canonical_key(g)
    if key[0] == "F":
        c, x, raw_edges = [], [], []

        def build(code_id, parent=None):
            (side, weight), children = _TREE_ID_TO_SIG[code_id]
            if side == 0:
                v = (0, len(c))
                c.append(weight)
            else:
                v = (1, len(x))
                x.append(weight)
            if parent is not None:
                p, i = (v[1], parent[1]) if v[0] == 0 else (parent[1], v[1])
                raw_edges.append((p, i))
            for child in children:
                build(child, v)

        for component in key[1]:
            build(component)
        return graph_from(c, x, Counter(raw_edges))

    weights, upper = key
    n = len(weights)
    a = [[0] * n for _ in range(n)]
    k = 0
    for r in range(n):
        for s in range(r + 1, n):
            a[r][s] = a[s][r] = upper[k]
            k += 1
    c = [w for side, w in weights if side == 0]
    x = [w for side, w in weights if side == 1]
    n_p = len(c)
    e = Counter()
    for p in range(n_p):
        for j in range(n_p, n):
            if a[p][j]:
                e[(p, j - n_p)] = a[p][j]
    return graph_from(c, x, e)


def add_term(dst: dict, g: Graph, q: int, coeff: int) -> None:
    if not coeff:
        return
    k = (q, canonical_key(g))
    if k in dst:
        old_g, old_c = dst[k]
        dst[k] = (old_g, old_c + coeff)
    else:
        dst[k] = (g, coeff)


def differentiate_graph(g: Graph, q: int) -> Iterable[tuple[Graph, int, int]]:
    """Yield (new_graph, new_q, integer_multiplier)."""
    edge0 = Counter({(p, i): m for p, i, m in g.edges})

    # Differentiate a c_p^a factor.
    for p, power in enumerate(g.c):
        if power == 0:
            continue
        c = list(g.c)
        x = list(g.x) + [1, 1]
        c[p] -= 1
        e = edge0.copy()
        i1, i2 = len(g.x), len(g.x) + 1
        e[(p, i1)] += 1
        e[(p, i2)] += 1
        yield graph_from(c, x, e), q, power

    # Differentiate an x_i^a factor.  The original x power is unchanged.
    for i, power in enumerate(g.x):
        if power == 0:
            continue
        c = list(g.c) + [1]
        x = list(g.x) + [1]
        pnew, inew = len(g.c), len(g.x)
        e = edge0.copy()
        e[(pnew, i)] += 1
        e[(pnew, inew)] += 1
        yield graph_from(c, x, e), q, 8 * power

    # Differentiate one occurrence of B_{pi}.
    for p, i, mult in g.edges:
        c = list(g.c)
        x = list(g.x) + [1]
        c[p] += 1
        x[i] += 1
        inew = len(g.x)
        e = edge0.copy()
        e[(p, i)] -= 1
        if not e[(p, i)]:
            del e[(p, i)]
        e[(p, inew)] += 1
        yield graph_from(c, x, e), q + 1, 2 * mult


def differentiate(poly: dict) -> dict:
    out = {}
    for (q, _), (g, coeff) in poly.items():
        for h, qh, mul in differentiate_graph(g, q):
            add_term(out, h, qh, coeff * mul)
    # Cancellations do not occur in this positive vector field, but keep clean.
    return {k: v for k, v in out.items() if v[1]}


def merge_vertices(g: Graph, p1: int, p2: int, i1: int, i2: int) -> Graph:
    """Impose p1=p2 and i1=i2 after selected edges were removed."""
    c = list(g.c)
    x = list(g.x)
    pmap = list(range(len(c)))
    imap = list(range(len(x)))
    if p1 != p2:
        keep, drop = sorted((p1, p2))
        c[keep] += c[drop]
        del c[drop]
        for j in range(len(pmap)):
            old = pmap[j]
            if old == drop:
                pmap[j] = keep
            elif old > drop:
                pmap[j] = old - 1
    if i1 != i2:
        keep, drop = sorted((i1, i2))
        x[keep] += x[drop]
        del x[drop]
        for j in range(len(imap)):
            old = imap[j]
            if old == drop:
                imap[j] = keep
            elif old > drop:
                imap[j] = old - 1
    e = Counter()
    for p, i, m in g.edges:
        e[(pmap[p], imap[i])] += m
    return graph_from(c, x, e)


def final_max_degree_and_weight(g: Graph) -> tuple[int, int]:
    """Degree in n and its leading coefficient after all B edges vanish."""
    assert not g.edges
    # i labels can all remain distinct: x_i^a has positive even Gaussian moment.
    degree = len(g.x)
    weight = math.prod(odd_double_factorial_from_half_power(a) for a in g.x)

    evens = [w for w in g.c if not (w & 1)]
    odds = [w for w in g.c if w & 1]
    if len(odds) & 1:
        return -1, 0
    degree += len(evens) + len(odds) // 2
    weight *= math.prod(normal_moment(w) for w in evens)

    @functools.lru_cache(maxsize=None)
    def pair_odds(ws: tuple[int, ...]) -> int:
        if not ws:
            return 1
        a = ws[0]
        total = 0
        for j in range(1, len(ws)):
            rest = ws[1:j] + ws[j + 1 :]
            total += normal_moment(a + ws[j]) * pair_odds(rest)
        return total

    weight *= pair_odds(tuple(sorted(odds)))
    return degree, weight


@functools.lru_cache(maxsize=400_000)
def wick_leading(g: Graph, target_degree: int) -> int:
    """Sum Wick pairings whose post-contraction n-degree is target_degree."""
    # Even if every remaining B-pair avoids all further endpoint mergers, the
    # final number of free labels cannot exceed this value.  Odd c-labelled
    # vertices must themselves be identified in pairs.  This monotone bound
    # prunes all partial pairings that have already lost a power of n.
    odd_c = sum(w & 1 for w in g.c)
    if odd_c & 1:
        return 0
    max_degree = len(g.x) + len(g.c) - odd_c // 2
    if max_degree < target_degree:
        return 0
    if max_degree - 2 * (g.edge_count // 2) > target_degree:
        return 0
    if not g.edges:
        degree, weight = final_max_degree_and_weight(g)
        if degree > target_degree:
            raise ArithmeticError(f"unexpected divergent Wick term: degree {degree} > target {target_degree}")
        return weight if degree == target_degree else 0

    e = Counter({(p, i): m for p, i, m in g.edges})
    first = min(e, key=lambda z: (-e[z], z))
    e[first] -= 1
    if not e[first]:
        del e[first]
    total = 0
    for partner, multiplicity in list(e.items()):
        e2 = e.copy()
        e2[partner] -= 1
        if not e2[partner]:
            del e2[partner]
        stripped = graph_from(list(g.c), list(g.x), e2)
        contracted = merge_vertices(stripped, first[0], partner[0], first[1], partner[1])
        if contracted.edges:
            contracted = canonical_graph(contracted)
        total += multiplicity * wick_leading(contracted, target_degree)
    return total


def expected_large_n(poly: dict) -> int:
    ans = 0
    for (q, _), (g, coeff) in poly.items():
        # A Wick contraction only identifies c-labels; it never changes their
        # total Gaussian degree.  Hence odd total c-degree vanishes before any
        # edge-pair enumeration.  This is the graph-level form of the exact
        # c -> -c, t -> -t symmetry and is essential at even derivative order.
        if sum(g.c) & 1:
            continue
        if g.edge_count & 1:
            continue
        # Raw derivative histories are forests with q components.  An n^0
        # Wick contraction cannot merge distinct raw components, so its value
        # factors over them.  Components of odd B- or c-degree vanish.
        comps = connected_component_graphs(g)
        if len(comps) != q:
            raise ArithmeticError(f"forest invariant failed: {len(comps)} != q={q}")
        value = 1
        for comp in comps:
            if (comp.edge_count & 1) or (sum(comp.c) & 1):
                value = 0
                break
            value *= wick_leading(canonical_graph(comp), 1 + comp.edge_count // 2)
            if not value:
                break
        ans += coeff * value
    return ans


def initial_observable() -> dict:
    # n^{-1} sum_{p,i,j} c_p B_{pi}B_{pj}x_i x_j
    g = Graph((1,), (1, 1), ((0, 0, 1), (0, 1, 1)))
    return {(1, canonical_key(g)): (g, 1)}


def save_checkpoint(path: Path, derivative_order: int, poly: dict, derivatives: list[int]) -> None:
    payload = {"order": derivative_order, "poly": poly, "derivatives": derivatives}
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as fh:
        pickle.dump(payload, fh, protocol=5)


def run(max_order: int, checkpoint: Path | None = None, resume: bool = False) -> dict:
    if resume and checkpoint and checkpoint.exists():
        with checkpoint.open("rb") as fh:
            state = pickle.load(fh)
        order = state["order"]
        poly = state["poly"]
        derivatives = state["derivatives"]
    else:
        order = 0
        poly = initial_observable()
        derivatives = [expected_large_n(poly)]

    while order < max_order:
        poly = differentiate(poly)
        order += 1
        value = expected_large_n(poly)
        derivatives.append(value)
        print(json.dumps({
            "order": order,
            "graphs": len(poly),
            "derivative": str(value),
            "canonical_cache": canonical_key.cache_info()._asdict(),
            "wick_cache": wick_leading.cache_info()._asdict(),
        }), flush=True)
        if checkpoint:
            save_checkpoint(checkpoint, order, poly, derivatives)
    return {"max_order": max_order, "derivatives": [str(v) for v in derivatives]}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-order", type=int, default=7)
    ap.add_argument("--checkpoint", type=Path)
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--output", type=Path)
    ap.add_argument("--differentiate-only", action="store_true")
    ap.add_argument("--evaluate-only", action="store_true")
    args = ap.parse_args()
    if args.differentiate_only:
        if not args.checkpoint or not args.resume:
            ap.error("--differentiate-only requires --checkpoint and --resume")
        with args.checkpoint.open("rb") as fh:
            state = pickle.load(fh)
        order, poly, derivatives = state["order"], state["poly"], state["derivatives"]
        while order < args.max_order:
            poly = differentiate(poly)
            order += 1
            derivatives.append(0 if order % 2 == 0 else None)
            save_checkpoint(args.checkpoint, order, poly, derivatives)
            print(json.dumps({"order": order, "graphs": len(poly), "derivative": None}), flush=True)
        return
    if args.evaluate_only:
        if not args.checkpoint:
            ap.error("--evaluate-only requires --checkpoint")
        with args.checkpoint.open("rb") as fh:
            state = pickle.load(fh)
        value = expected_large_n(state["poly"])
        print(json.dumps({"order": state["order"], "graphs": len(state["poly"]), "derivative": str(value)}))
        return
    result = run(args.max_order, args.checkpoint, args.resume)
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
        print(f"sha256={hashlib.sha256(encoded.encode()).hexdigest()}")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
