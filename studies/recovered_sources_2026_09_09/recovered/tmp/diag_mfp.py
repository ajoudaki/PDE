import sys
from collections import Counter

sys.path.insert(0, "/tmp")
import mfp_graph_compiler as m

terms = m.main(7, True)
decorated = set()
topological = set()
exact_edges = set()
decorated_by_size = {}
topological_by_size = {}
exact_by_size = {}
sizes = Counter()
side_sizes = Counter()
for t in terms:
    nt = len(t.a)
    n = nt + len(t.x)
    adj = [[] for _ in range(n)]
    all_edges = []
    for p, row in enumerate(t.edges):
        for i, c in enumerate(row):
            if c:
                u, v = p, nt + i
                adj[u].append(v)
                adj[v].append(u)
                all_edges.append((u, v))
    labels = [(0, d) for d in t.a] + [(1, d) for d in t.x]
    kinds = [(kind, 0) for kind, _ in labels]
    seen = set()
    for start in range(n):
        if start in seen:
            continue
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
        local = {v: j for j, v in enumerate(comp)}
        edges = tuple((local[u], local[v]) for u, v in all_edges if u in comp_set)
        dcode = m.component_code(adj, labels, comp)
        tcode = m.component_code(adj, kinds, comp)
        decorated.add(dcode)
        topological.add(tcode)
        exact_edges.add(edges)
        decorated_by_size.setdefault(len(edges), set()).add(dcode)
        topological_by_size.setdefault(len(edges), set()).add(tcode)
        exact_by_size.setdefault(len(edges), set()).add(edges)
        sizes[len(edges)] += 1
        if len(edges) == 16:
            side_sizes[(sum(1 for v in comp if labels[v][0] == 0), sum(1 for v in comp if labels[v][0] == 1))] += 1

print("component occurrences", sum(sizes.values()))
print("edge-size occurrences", sorted(sizes.items()))
print("unique decorated", len(decorated))
print("unique topology", len(topological))
print("unique exact edges", len(exact_edges))
print("unique decorated by size", [(k, len(v)) for k, v in sorted(decorated_by_size.items())])
print("unique topology by size", [(k, len(v)) for k, v in sorted(topological_by_size.items())])
print("unique exact by size", [(k, len(v)) for k, v in sorted(exact_by_size.items())])
print("E16 side sizes", sorted(side_sizes.items()))
