"""Combinatorial route-A check for the *roadmap-only* D^7 free-tree count.

Repeated ``D=grad(f).grad`` attaches one new leaf to a contraction tree at
every differentiation.  This script canonicalizes unlabelled free trees by
their center encodings and groups growth histories.  It is discovery/audit
input for the F7 roadmap, not a promoted F7 MFP closure.
"""

from __future__ import annotations

import json
from pathlib import Path


Adjacency = tuple[tuple[int, ...], ...]


def centers(adjacency: Adjacency) -> tuple[int, ...]:
    n = len(adjacency)
    if n <= 2:
        return tuple(range(n))
    degree = [len(neighbors) for neighbors in adjacency]
    leaves = [vertex for vertex, value in enumerate(degree) if value <= 1]
    remaining = n
    while remaining > 2:
        next_leaves = []
        remaining -= len(leaves)
        for leaf in leaves:
            degree[leaf] = 0
            for neighbor in adjacency[leaf]:
                if degree[neighbor] > 0:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        next_leaves.append(neighbor)
        leaves = next_leaves
    return tuple(sorted(leaves))


def rooted_encoding(adjacency: Adjacency, root: int, parent: int = -1) -> str:
    children = sorted(
        rooted_encoding(adjacency, child, root)
        for child in adjacency[root]
        if child != parent
    )
    return "(" + "".join(children) + ")"


def canonical(adjacency: Adjacency) -> str:
    center = centers(adjacency)
    if len(center) == 1:
        return rooted_encoding(adjacency, center[0])
    left, right = center
    halves = sorted(
        (
            rooted_encoding(adjacency, left, right),
            rooted_encoding(adjacency, right, left),
        )
    )
    return "[" + "".join(halves) + "]"


def attach_leaf(adjacency: Adjacency, vertex: int) -> Adjacency:
    n = len(adjacency)
    rows = [list(neighbors) for neighbors in adjacency] + [[vertex]]
    rows[vertex].append(n)
    return tuple(tuple(sorted(row)) for row in rows)


def grow(max_vertices: int = 8):
    current: dict[str, tuple[Adjacency, int]] = {"()": (((),), 1)}
    levels = {1: current}
    for vertices in range(1, max_vertices):
        next_level: dict[str, tuple[Adjacency, int]] = {}
        for _, (adjacency, coefficient) in current.items():
            for vertex in range(vertices):
                child = attach_leaf(adjacency, vertex)
                key = canonical(child)
                representative, old = next_level.get(key, (child, 0))
                next_level[key] = (representative, old + coefficient)
        current = next_level
        levels[vertices + 1] = current
    return levels


def report() -> dict[str, object]:
    levels = grow(8)
    return {
        "status": "roadmap-only; no F7 closure claim",
        "family_counts_by_D_order": {
            str(vertices - 1): len(level) for vertices, level in levels.items()
        },
        "D5_coefficients": sorted(
            coefficient for _, coefficient in levels[6].values()
        ),
        "D7_family_count_route_A": len(levels[8]),
        "D7_families": [
            {"canonical_tree": key, "growth_coefficient": coefficient}
            for key, (_, coefficient) in sorted(levels[8].items())
        ],
        "promotion_blockers": [
            "no independent tree-family canonicalization",
            "no explicit rank-labelled tensor contraction table",
            "no equality-partition/transpose-response audit",
            "no M-only F7 recurrence or fixed state count",
        ],
    }


if __name__ == "__main__":
    result = report()
    path = Path(__file__).resolve().parent / "F7_TREE_ROADMAP_ROUTE_A.json"
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
