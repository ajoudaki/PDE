"""Exact arbitrary-depth leading-width diagrams for the deep-linear control.

The algorithm never instantiates a numerical width.  It grows the copies of
the unnormalised path polynomial created by repeated
``(grad P).grad``, records derivative-coordinate identifications with a
union-find partition, performs every Gaussian Wick pairing, and counts the
remaining free neuron-index classes.  The resulting integer polynomial in
``n`` gives both the large-width coefficient and all finite-width collision
corrections.
"""

from __future__ import annotations

from collections import defaultdict
from functools import lru_cache
from math import factorial


Occurrence = tuple[int, int]  # (path-copy, parameter block)
Partition = tuple[int, ...]
State = tuple[tuple[Occurrence, ...], Partition]


def _canonical_partition(labels: list[int]) -> Partition:
    replacement: dict[int, int] = {}
    answer = []
    for label in labels:
        if label not in replacement:
            replacement[label] = len(replacement)
        answer.append(replacement[label])
    return tuple(answer)


def _union(partition: Partition, pairs: list[tuple[int, int]]) -> Partition:
    parent = list(range(len(partition)))

    def find(value: int) -> int:
        while parent[value] != value:
            parent[value] = parent[parent[value]]
            value = parent[value]
        return value

    # Restore the equivalence classes represented by the canonical labels.
    first: dict[int, int] = {}
    for node, label in enumerate(partition):
        if label in first:
            parent[find(node)] = find(first[label])
        else:
            first[label] = node
    for left, right in pairs:
        left_root, right_root = find(left), find(right)
        if left_root != right_root:
            parent[right_root] = left_root
    labels = [find(node) for node in range(len(parent))]
    return _canonical_partition(labels)


def _extend(partition: Partition, count: int) -> Partition:
    next_label = max(partition, default=-1) + 1
    return partition + tuple(range(next_label, next_label + count))


def _node(copy: int, layer_index: int, hidden_depth: int) -> int:
    return copy * hidden_depth + layer_index


def _block_nodes(copy: int, block: int, hidden_depth: int) -> tuple[int, ...]:
    """Neuron-index components of one parameter coordinate on a path."""

    if block == 0:  # first-layer active coordinate r_i1
        return (_node(copy, 0, hidden_depth),)
    if block == hidden_depth:  # readout a_iH
        return (_node(copy, hidden_depth - 1, hidden_depth),)
    # W^(block+1) has row i_(block+1), column i_block.
    return (
        _node(copy, block - 1, hidden_depth),
        _node(copy, block, hidden_depth),
    )


@lru_cache(maxsize=None)
def _perfect_pairings(items: tuple[int, ...]) -> tuple[tuple[tuple[int, int], ...], ...]:
    if not items:
        return ((),)
    if len(items) % 2:
        return ()
    first = items[0]
    answer = []
    for index in range(1, len(items)):
        second = items[index]
        rest = items[1:index] + items[index + 1 :]
        for suffix in _perfect_pairings(rest):
            answer.append(((first, second),) + suffix)
    return tuple(answer)


def derivative_history_states(hidden_depth: int, order: int) -> dict[State, int]:
    """Aggregate all product-rule histories before the terminal Wick step."""

    if hidden_depth < 1 or order < 0:
        raise ValueError("depth must be positive and order nonnegative")
    block_count = hidden_depth + 1
    initial_occurrences = tuple((0, block) for block in range(block_count))
    initial_partition = tuple(range(hidden_depth))
    states: dict[State, int] = {(initial_occurrences, initial_partition): 1}

    for new_copy in range(1, order + 1):
        next_states: dict[State, int] = defaultdict(int)
        for (occurrences, partition), multiplicity in states.items():
            extended = _extend(partition, hidden_depth)
            for target_index, (target_copy, block) in enumerate(occurrences):
                remaining = list(occurrences)
                remaining.pop(target_index)
                remaining.extend(
                    (new_copy, candidate)
                    for candidate in range(block_count)
                    if candidate != block
                )
                target_nodes = _block_nodes(target_copy, block, hidden_depth)
                new_nodes = _block_nodes(new_copy, block, hidden_depth)
                constrained = _union(extended, list(zip(target_nodes, new_nodes)))
                state = (tuple(sorted(remaining)), constrained)
                next_states[state] += multiplicity
        states = dict(next_states)
    return states


@lru_cache(maxsize=None)
def unnormalised_expectation_polynomial(
    hidden_depth: int, order: int, *, progress: bool = False
) -> dict[int, int]:
    """Return ``{free_index_classes: integer multiplicity}`` for E[O^k P]."""

    states = derivative_history_states(hidden_depth, order)
    if progress:
        print(
            f"H={hidden_depth} k={order}: {len(states)} aggregated derivative histories",
            flush=True,
        )
    block_count = hidden_depth + 1
    polynomial: dict[int, int] = defaultdict(int)
    for state_index, ((occurrences, partition), history_multiplicity) in enumerate(states.items()):
        wick_states: dict[Partition, int] = {partition: history_multiplicity}
        for block in range(block_count):
            copies = tuple(copy for copy, candidate in occurrences if candidate == block)
            pairings = _perfect_pairings(copies)
            if not pairings:
                wick_states = {}
                break
            next_wick: dict[Partition, int] = defaultdict(int)
            for current_partition, current_multiplicity in wick_states.items():
                for pairing in pairings:
                    constraints: list[tuple[int, int]] = []
                    for left_copy, right_copy in pairing:
                        constraints.extend(
                            zip(
                                _block_nodes(left_copy, block, hidden_depth),
                                _block_nodes(right_copy, block, hidden_depth),
                            )
                        )
                    next_wick[_union(current_partition, constraints)] += current_multiplicity
            wick_states = dict(next_wick)
        for final_partition, multiplicity in wick_states.items():
            polynomial[len(set(final_partition))] += multiplicity
        if progress and state_index and state_index % 10000 == 0:
            print(f"  Wick-processed {state_index}/{len(states)} states", flush=True)
    return dict(sorted(polynomial.items(), reverse=True))


def deep_linear_limits(hidden_depth: int, *, progress: bool = False) -> tuple[int, int, int]:
    """Return exact large-width ``(A_H,B_H,C_H)`` at Q0=1."""

    answer = []
    block_count = hidden_depth + 1
    for order in (1, 3, 5):
        polynomial = unnormalised_expectation_polynomial(
            hidden_depth, order, progress=progress
        )
        target_twice = (order + 1) * block_count - 2 * order
        if target_twice % 2:
            raise AssertionError("odd derivative has half-integral width valuation")
        target = target_twice // 2
        if any(power > target and coefficient for power, coefficient in polynomial.items()):
            raise AssertionError(
                f"uncancelled divergent sector H={hidden_depth} k={order}: {polynomial}"
            )
        answer.append(polynomial.get(target, 0))
    return tuple(answer)  # type: ignore[return-value]


def finite_width_value(hidden_depth: int, order: int, width: int) -> int | float:
    """Evaluate the exact diagram polynomial with the model normalization."""

    polynomial = unnormalised_expectation_polynomial(hidden_depth, order)
    block_count = hidden_depth + 1
    exponent_twice = 2 * order - (order + 1) * block_count
    if exponent_twice % 2:
        raise ValueError("requested parity has a half-integral normalization")
    exponent = exponent_twice // 2
    numerator = sum(coefficient * width**power for power, coefficient in polynomial.items())
    return numerator * width**exponent if exponent >= 0 else numerator / width ** (-exponent)


if __name__ == "__main__":
    for depth in range(1, 5):
        print(depth, deep_linear_limits(depth, progress=True))
