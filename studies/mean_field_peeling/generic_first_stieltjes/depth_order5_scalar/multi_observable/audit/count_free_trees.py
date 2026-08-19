"""Independent no-dependency check of the raw D^k f free-tree shape count."""

from itertools import product
from heapq import heapify, heappop, heappush


def edges_from_prufer(sequence):
    n = len(sequence) + 2
    degree = [1] * n
    for vertex in sequence:
        degree[vertex] += 1
    leaves = [vertex for vertex, value in enumerate(degree) if value == 1]
    heapify(leaves)
    edges = []
    for vertex in sequence:
        leaf = heappop(leaves)
        edges.append((leaf, vertex))
        degree[leaf] -= 1
        degree[vertex] -= 1
        if degree[vertex] == 1:
            heappush(leaves, vertex)
    edges.append((heappop(leaves), heappop(leaves)))
    return edges


def canonical_free_tree(n, edges):
    adjacency = [[] for _ in range(n)]
    for left, right in edges:
        adjacency[left].append(right)
        adjacency[right].append(left)
    degree = [len(row) for row in adjacency]
    leaves = [vertex for vertex, value in enumerate(degree) if value <= 1]
    removed = len(leaves)
    while removed < n:
        next_leaves = []
        for leaf in leaves:
            for neighbour in adjacency[leaf]:
                degree[neighbour] -= 1
                if degree[neighbour] == 1:
                    next_leaves.append(neighbour)
        if removed + len(next_leaves) >= n:
            leaves = next_leaves
            break
        removed += len(next_leaves)
        leaves = next_leaves

    def rooted_code(vertex, parent):
        children = sorted(
            rooted_code(child, vertex)
            for child in adjacency[vertex]
            if child != parent
        )
        return "(" + "".join(children) + ")"

    return min(rooted_code(center, -1) for center in leaves)


def count(n):
    return len(
        {
            canonical_free_tree(n, edges_from_prufer(sequence))
            for sequence in product(range(n), repeat=n - 2)
        }
    )


if __name__ == "__main__":
    print({n: count(n) for n in range(2, 9)})

