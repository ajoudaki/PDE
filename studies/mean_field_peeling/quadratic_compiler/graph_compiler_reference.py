from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache
import time
from math import prod

import networkx as nx


@dataclass
class Term:
    a: tuple[int, ...]
    x: tuple[int, ...]
    edges: tuple[tuple[int, ...], ...]
    power: int
    coef: int

    def copy_lists(self):
        return list(self.a), list(self.x), [list(r) for r in self.edges]


def graph_for(t: Term):
    g = nx.Graph()
    for p, c in enumerate(t.a):
        g.add_node(('t', p), kind='t', dec=c)
    for i, c in enumerate(t.x):
        g.add_node(('b', i), kind='b', dec=c)
    for p, row in enumerate(t.edges):
        for i, c in enumerate(row):
            if c:
                g.add_edge(('t', p), ('b', i), mult=c)
    return g


NODE_MATCH = nx.algorithms.isomorphism.categorical_node_match(['kind', 'dec'], ['', 0])
EDGE_MATCH = nx.algorithms.isomorphism.categorical_edge_match('mult', 0)


def term_hash(t: Term):
    g = graph_for(t)
    # Two rounds more than diameter is cheap for these tiny graphs.
    return (t.power, nx.weisfeiler_lehman_graph_hash(g, node_attr='kind', edge_attr='mult', iterations=20))


def iso(t: Term, u: Term):
    if t.power != u.power or len(t.a) != len(u.a) or len(t.x) != len(u.x):
        return False
    return nx.is_isomorphic(graph_for(t), graph_for(u), node_match=NODE_MATCH, edge_match=EDGE_MATCH)


def forest_key(t: Term):
    """Exact canonical key for the decorated bipartite forest carried by a term."""
    nt, nb = len(t.a), len(t.x)
    n = nt + nb
    adj = [[] for _ in range(n)]
    for p, row in enumerate(t.edges):
        for i, c in enumerate(row):
            if c:
                if c != 1:
                    raise ValueError(f"unexpected parallel edge multiplicity {c}")
                u, v = p, nt + i
                adj[u].append(v)
                adj[v].append(u)

    labels = [(0, d) for d in t.a] + [(1, d) for d in t.x]

    def rooted(v, parent):
        children = [rooted(w, v) for w in adj[v] if w != parent]
        children.sort()
        return (0, labels[v][0], labels[v][1], tuple(children))

    seen = set()
    components = []
    for start in range(n):
        if start in seen:
            continue
        stack = [start]
        comp = []
        seen.add(start)
        while stack:
            v = stack.pop()
            comp.append(v)
            for w in adj[v]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)

        # A forest component with |V| vertices has |V|-1 edges.
        if sum(len(adj[v]) for v in comp) // 2 != len(comp) - 1:
            raise ValueError("derivative graph is not a forest")

        if len(comp) == 1:
            components.append(rooted(comp[0], -1))
            continue

        degree = {v: len(adj[v]) for v in comp}
        leaves = [v for v in comp if degree[v] <= 1]
        remaining = len(comp)
        while remaining > 2:
            new_leaves = []
            remaining -= len(leaves)
            for v in leaves:
                degree[v] = 0
                for w in adj[v]:
                    if degree.get(w, 0) > 0:
                        degree[w] -= 1
                        if degree[w] == 1:
                            new_leaves.append(w)
            leaves = new_leaves
        centers = sorted(v for v in comp if degree[v] > 0)
        if not centers:  # two-vertex component after the final peel
            centers = leaves
        if len(centers) == 1:
            components.append(rooted(centers[0], -1))
        elif len(centers) == 2:
            left = rooted(centers[0], centers[1])
            right = rooted(centers[1], centers[0])
            if right < left:
                left, right = right, left
            components.append((1, left, right))
        else:
            raise ValueError(f"bad tree centers {centers}")

    components.sort()
    if len(components) != t.power:
        raise ValueError(f"component/power mismatch: {len(components)} != {t.power}")
    return (t.power, tuple(components))


def component_code(adj, labels, comp):
    """AHU canonical code for one decorated tree component."""
    def rooted(v, parent):
        children = [rooted(w, v) for w in adj[v] if w != parent]
        children.sort()
        return (0, labels[v][0], labels[v][1], tuple(children))

    if len(comp) == 1:
        return rooted(comp[0], -1)
    degree = {v: len(adj[v]) for v in comp}
    leaves = [v for v in comp if degree[v] <= 1]
    remaining = len(comp)
    while remaining > 2:
        new_leaves = []
        remaining -= len(leaves)
        for v in leaves:
            degree[v] = 0
            for w in adj[v]:
                if degree.get(w, 0) > 0:
                    degree[w] -= 1
                    if degree[w] == 1:
                        new_leaves.append(w)
        leaves = new_leaves
    centers = sorted(v for v in comp if degree[v] > 0)
    if not centers:
        centers = leaves
    if len(centers) == 1:
        return rooted(centers[0], -1)
    if len(centers) == 2:
        left = rooted(centers[0], centers[1])
        right = rooted(centers[1], centers[0])
        if right < left:
            left, right = right, left
        return (1, left, right)
    raise ValueError(f"bad tree centers {centers}")


def normalize(a, x, e, power, coef):
    return Term(tuple(a), tuple(x), tuple(tuple(r) for r in e), power, coef)


def differentiate_by_rule(t: Term):
    out = []
    # Hit an a_p.  a'_p = z_p^2.
    for p, c in enumerate(t.a):
        if not c:
            continue
        a, x, e = t.copy_lists()
        a[p] -= 1
        for _ in range(2):
            x.append(2)
            for row in e:
                row.append(0)
            e[p][-1] += 1
        out.append(('a', normalize(a, x, e, t.power, t.coef * c)))

    # Hit W_pi.  W'_pi = (2/n) a_p z_p x_i^2.
    for p, row in enumerate(t.edges):
        for i, c in enumerate(row):
            if not c:
                continue
            a, x, e = t.copy_lists()
            e[p][i] -= 1
            a[p] += 1
            x[i] += 2
            x.append(2)
            for rr in e:
                rr.append(0)
            e[p][-1] += 1
            out.append(('w', normalize(a, x, e, t.power + 1, t.coef * c * 2)))

    # Hit x_i.  x'_i = 4 x_i sum_p W_pi a_p sum_j W_pj x_j^2.
    for i, c in enumerate(t.x):
        if not c:
            continue
        a, x, e = t.copy_lists()
        # Differentiating x_i^c and replacing x'_i retains exponent c at i.
        a.append(1)
        e.append([0] * len(x))
        p = len(a) - 1
        e[p][i] += 1
        x.append(2)
        for row in e:
            row.append(0)
        e[p][-1] += 1
        out.append(('x', normalize(a, x, e, t.power, t.coef * c * 4)))
    return out


def differentiate(t: Term):
    return [u for _, u in differentiate_by_rule(t)]


def merge_terms(raw):
    merged = {}
    for t in raw:
        key = forest_key(t)
        if key in merged:
            merged[key].coef += t.coef
        else:
            merged[key] = t
    return [t for t in merged.values() if t.coef]


def canon_partition(parent):
    n = len(parent)
    p = list(parent)
    def root(i):
        while p[i] != i:
            p[i] = p[p[i]]
            i = p[i]
        return i
    roots = [root(i) for i in range(n)]
    ren = {}
    ans = []
    for r in roots:
        if r not in ren:
            ren[r] = len(ren)
        ans.append(ren[r])
    return tuple(ans)


def union_partition(part, i, j):
    p = list(part)
    ri, rj = p[i], p[j]
    if ri == rj:
        return part
    for k, r in enumerate(p):
        if r == rj:
            p[k] = ri
    # Canonicalize labels by first appearance.
    ren = {}
    ans = []
    for r in p:
        if r not in ren:
            ren[r] = len(ren)
        ans.append(ren[r])
    return tuple(ans)


def discrete_partition(n):
    return tuple(range(n))


@lru_cache(None)
def gaussian_pair_dist(counts, part):
    """Counter(component count -> number of Wick pairings)."""
    counts = tuple(counts)
    total = sum(counts)
    if total == 0:
        return ((len(set(part)), 1),)
    if total % 2:
        return tuple()
    u = next(i for i, c in enumerate(counts) if c)
    c2 = list(counts)
    c2[u] -= 1  # select one distinguished occurrence at u
    accum = Counter()
    for v, cv in enumerate(c2):
        if not cv:
            continue
        c3 = list(c2)
        c3[v] -= 1
        p3 = union_partition(part, u, v)
        for comps, mult in gaussian_pair_dist(tuple(c3), p3):
            accum[comps] += cv * mult
    return tuple(sorted(accum.items()))


@lru_cache(None)
def w_pair_partitions(edge_counts, nt, nb, pt, pb):
    """Counter((top partition,bottom partition) -> Wick pairing multiplicity)."""
    edge_counts = tuple(edge_counts)
    total = sum(edge_counts)
    if total == 0:
        return ((pt, pb, 1),)
    if total % 2:
        return tuple()
    # edge types are flattened p*nb+i
    u = next(k for k, c in enumerate(edge_counts) if c)
    p1, i1 = divmod(u, nb)
    rem = list(edge_counts)
    rem[u] -= 1
    accum = Counter()
    for v, cv in enumerate(rem):
        if not cv:
            continue
        p2, i2 = divmod(v, nb)
        rem2 = list(rem)
        rem2[v] -= 1
        pt2 = union_partition(pt, p1, p2)
        pb2 = union_partition(pb, i1, i2)
        for qt, qb, mult in w_pair_partitions(tuple(rem2), nt, nb, pt2, pb2):
            accum[(qt, qb)] += cv * mult
    return tuple((qt, qb, mult) for (qt, qb), mult in accum.items())


def odd_double_factorial(k):
    """Return k!! for odd k >= -1."""
    ans = 1
    while k > 0:
        ans *= k
        k -= 2
    return ans


@lru_cache(None)
def maximal_odd_block_pairings(degrees):
    """Leading Wick count when each odd-degree index block pairs with one peer."""
    degrees = tuple(sorted(degrees))
    if not degrees:
        return 1
    first = degrees[0]
    total = 0
    for j in range(1, len(degrees)):
        rest = degrees[1:j] + degrees[j + 1:]
        total += odd_double_factorial(first + degrees[j] - 1) * maximal_odd_block_pairings(rest)
    return total


def leading_expectation_wpair_audit(t: Term, return_audit=False):
    """Leading coefficient using only middle-weight pairings.

    Every lower preactivation exponent generated here is even.  Thus its Wick
    pairing is local inside each equality block at leading order.  For readout
    factors, the only forced additional leading equalities pair odd-degree
    weight-induced blocks two by two.  This eliminates the expensive full
    Gaussian-pairing recursion without changing the exponent-zero sector.
    """
    flat = tuple(c for row in t.edges for c in row)
    wdeg = sum(flat)
    if wdeg % 2:
        return (0, Counter()) if return_audit else 0
    nt, nb = len(t.a), len(t.x)
    wp = w_pair_partitions(flat, nt, nb, discrete_partition(nt), discrete_partition(nb))
    lead = 0
    exponent_tally = Counter()
    for pt, pb, mw in wp:
        atop = Counter()
        xbot = Counter()
        for p, degree in enumerate(t.a):
            atop[pt[p]] += degree
        for i, degree in enumerate(t.x):
            xbot[pb[i]] += degree

        odd_top = tuple(d for d in atop.values() if d % 2)
        odd_bottom = tuple(d for d in xbot.values() if d % 2)
        if len(odd_top) % 2 or len(odd_bottom) % 2:
            continue
        exponent = (
            len(atop) + len(xbot) - wdeg // 2 - t.power
            - len(odd_top) // 2 - len(odd_bottom) // 2
        )
        even_moment = 1
        for degree in atop.values():
            if degree % 2 == 0:
                even_moment *= odd_double_factorial(degree - 1)
        for degree in xbot.values():
            if degree % 2 == 0:
                even_moment *= odd_double_factorial(degree - 1)
        multiplicity = (
            mw * even_moment
            * maximal_odd_block_pairings(odd_top)
            * maximal_odd_block_pairings(odd_bottom)
        )
        exponent_tally[exponent] += multiplicity
        if exponent == 0:
            lead += multiplicity
    return (lead, exponent_tally) if return_audit else lead


def leading_expectation(t: Term, verbose=False):
    if sum(t.a) % 2 or sum(t.x) % 2:
        return 0, Counter()
    flat = tuple(c for row in t.edges for c in row)
    wdeg = sum(flat)
    if wdeg % 2:
        return 0, Counter()
    nt, nb = len(t.a), len(t.x)
    wp = w_pair_partitions(flat, nt, nb, discrete_partition(nt), discrete_partition(nb))
    exps = Counter()
    for pt, pb, mw in wp:
        ad = gaussian_pair_dist(t.a, pt)
        xd = gaussian_pair_dist(t.x, pb)
        for ca, ma in ad:
            for cb, mb in xd:
                exp = ca + cb - wdeg // 2 - t.power
                exps[exp] += mw * ma * mb
    if verbose and any(k > 0 for k in exps):
        print('DIVERGENT?', exps)
    return exps[0], exps


_component_expectation_cache = {}


def leading_component_expectation(edges, labels, code):
    """Leading Wick value of one raw decorated-tree component."""
    cached = _component_expectation_cache.get(code)
    if cached is not None:
        return cached
    E = len(edges)
    if E % 2:
        _component_expectation_cache[code] = 0
        return 0
    nv = len(labels)
    target_vertices = E // 2 + 1

    @lru_cache(None)
    def rec(remaining, part):
        if not remaining:
            classes = len(set(part))
            if classes != target_vertices:
                return 0
            ae = Counter()
            xe = Counter()
            for v, (kind, dec) in enumerate(labels):
                if kind == 0:
                    ae[part[v]] += dec
                else:
                    xe[part[v]] += dec
            ans = 1
            for dec in ae.values():
                if dec % 2:
                    return 0
                ans *= 1 if dec == 0 else prod(range(1, dec, 2))
            for dec in xe.values():
                if dec % 2:
                    return 0
                ans *= 1 if dec == 0 else prod(range(1, dec, 2))
            return ans

        # Each future paired edge can identify at most two vertex classes.
        pairs_left = len(remaining) // 2
        classes = len(set(part))
        if target_vertices > classes or target_vertices < classes - 2 * pairs_left:
            return 0

        # In a leading tree quotient every quotient edge has exactly two raw
        # preimage edges.  Vertex identifications can only merge cells, so a
        # current class-pair containing more than two raw edges can never be
        # repaired later.
        cell_counts = Counter((part[u], part[v]) for u, v in edges)
        if any(c > 2 for c in cell_counts.values()):
            return 0

        # A readout class with odd total degree must still be able to merge via
        # an endpoint of some remaining edge.
        active_vertices = set()
        for ee in remaining:
            active_vertices.update(edges[ee])
        active_classes = {part[v] for v in active_vertices}
        a_parity = Counter()
        for v, (kind, dec) in enumerate(labels):
            if kind == 0:
                a_parity[part[v]] ^= (dec & 1)
        if any(par and cls not in active_classes for cls, par in a_parity.items()):
            return 0

        e0 = remaining[0]
        u0, v0 = edges[e0]
        ans = 0
        for jj in range(1, len(remaining)):
            e1 = remaining[jj]
            u1, v1 = edges[e1]
            p2 = union_partition(part, u0, u1)
            p2 = union_partition(p2, v0, v1)
            rest = remaining[1:jj] + remaining[jj + 1:]
            ans += rec(rest, p2)
        return ans

    ans = rec(tuple(range(E)), discrete_partition(nv))
    _component_expectation_cache[code] = ans
    return ans


def leading_expectation_fast(t: Term):
    """Leading expectation, using the fact that every raw graph is a forest.

    A leading pairing cannot join distinct raw components; otherwise it loses a
    free index.  It therefore factors over components, and within each component
    the paired-edge quotient must remain a tree.
    """
    nt, nb = len(t.a), len(t.x)
    n = nt + nb
    adj = [[] for _ in range(n)]
    all_edges = []
    for p, row in enumerate(t.edges):
        for i, c in enumerate(row):
            if c:
                if c != 1:
                    raise ValueError("parallel raw edge")
                u, v = p, nt + i
                adj[u].append(v)
                adj[v].append(u)
                all_edges.append((u, v))
    labels = [(0, d) for d in t.a] + [(1, d) for d in t.x]

    seen = set()
    total = 1
    ncomp = 0
    for start in range(n):
        if start in seen:
            continue
        ncomp += 1
        stack = [start]
        seen.add(start)
        comp = []
        while stack:
            v = stack.pop()
            comp.append(v)
            for w in adj[v]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        comp_set = set(comp)
        local_index = {v: j for j, v in enumerate(comp)}
        local_edges = tuple((local_index[u], local_index[v])
                            for u, v in all_edges if u in comp_set)
        local_labels = tuple(labels[v] for v in comp)
        code = component_code(adj, labels, comp)
        val = leading_component_expectation(local_edges, local_labels, code)
        if not val:
            return 0
        total *= val
    if ncomp != t.power:
        raise ValueError("component/power mismatch in expectation")
    return total


def main(order=5, generate_only=False):
    # H=(1/n) sum_pij a_p W_pi W_pj x_i^2 x_j^2
    terms = [Term((1,), (2, 2), ((1, 1),), 1, 1)]
    for k in range(order):
        start = time.time()
        raw = [u for t in terms for u in differentiate(t)]
        print('order', k + 1, 'raw', len(raw), flush=True)
        terms = merge_terms(raw)
        print('order', k + 1, 'types', len(terms), 'merge sec', time.time() - start, flush=True)
    if generate_only:
        return terms
    total = 0
    exptally = Counter()
    lambda_tally = Counter()
    power_tally = Counter()
    surviving_types = 0
    start = time.time()
    for idx, t in enumerate(terms):
        lead = leading_expectation_fast(t)
        exps = Counter({0: lead}) if lead else Counter()
        total += t.coef * lead
        if lead:
            surviving_types += 1
            w_pairs = sum(sum(row) for row in t.edges) // 2
            lambda_tally[w_pairs] += t.coef * lead
            power_tally[t.power] += t.coef * lead
        for e, c in exps.items():
            exptally[e] += t.coef * c
        if (idx + 1) % 100 == 0:
            print('eval', idx + 1, '/', len(terms), 'sec', time.time() - start, flush=True)
    print('expectation exponent tally', sorted(exptally.items()))
    print('surviving canonical types', surviving_types, '/', len(terms))
    print('lambda polynomial', sorted(lambda_tally.items()))
    print('explicit-power decomposition', sorted(power_tally.items()))
    print('H derivative', order, '=', total)


if __name__ == '__main__':
    import sys
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 5, '--generate-only' in sys.argv)
