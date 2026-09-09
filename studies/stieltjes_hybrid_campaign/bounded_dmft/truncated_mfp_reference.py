#!/usr/bin/env python3
"""Low-order MFP jets for a non-Gaussian symmetric readout law.
This is an isolated evaluator.  It reuses the accepted forest generation and
middle-weight Wick pairing code, but replaces *only* the moments of row/readout
variables (``Graph.c``) after row labels merge.  Column variables and the
initial middle matrix remain standard Gaussian.

The implementation is intentionally capped at order five.  It is a reference
for the bounded-DMFT calibration, not a replacement for the accepted MFP
compiler.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import functools
import json
import math
from pathlib import Path
import sys
from typing import Callable

import mpmath as mp


COMPILER = (
    Path(__file__).resolve().parents[4]
    / "mean_field_peeling"
    / "quadratic_compiler"
)
if str(COMPILER) not in sys.path:
    sys.path.insert(0, str(COMPILER))

import exact_graph_wick as eg  # noqa: E402


Moment = Callable[[int], mp.mpf]


def gaussian_moment(power: int) -> mp.mpf:
    if power & 1:
        return mp.mpf("0")
    return mp.mpf(eg.normal_moment(power))


def conditional_normal_moment_function(
    cutoff: float | mp.mpf,
    *,
    max_power: int = 24,
    dps: int = 80,
) -> tuple[Moment, dict[int, mp.mpf]]:
    """Return moments of N(0,1) conditional on ``|Z| <= cutoff``.

    The law is not variance-renormalized.  Even moments obey

        m_2k = (2k-1)m_(2k-2) - 2 A^(2k-1) phi(A) / Z_A.
    """

    if cutoff <= 0:
        raise ValueError("cutoff must be positive")
    if max_power < 0:
        raise ValueError("max_power must be nonnegative")
    mp.mp.dps = dps
    a = mp.mpf(cutoff)
    phi = mp.exp(-(a * a) / 2) / mp.sqrt(2 * mp.pi)
    mass = mp.erf(a / mp.sqrt(2))
    moments: dict[int, mp.mpf] = {0: mp.mpf(1)}
    for power in range(2, max_power + 1, 2):
        moments[power] = (
            (power - 1) * moments[power - 2]
            - 2 * a ** (power - 1) * phi / mass
        )

    def moment(power: int) -> mp.mpf:
        if power & 1:
            return mp.mpf(0)
        try:
            return moments[power]
        except KeyError as exc:
            raise ValueError(
                f"moment power {power} exceeds prepared maximum {max_power}"
            ) from exc

    return moment, moments


@dataclass
class LawEvaluator:
    """Large-width Wick evaluator with a configurable readout moment law."""

    readout_moment: Moment

    def __post_init__(self) -> None:
        # Per-law caches avoid mixing values from distinct readout laws.
        self._wick = functools.lru_cache(maxsize=400_000)(self._wick_uncached)

    def final_max_degree_and_weight(self, graph: eg.Graph) -> tuple[int, mp.mpf]:
        assert not graph.edges
        degree = len(graph.x)
        weight = mp.mpf(
            math.prod(eg.odd_double_factorial_from_half_power(a) for a in graph.x)
        )

        evens = [w for w in graph.c if not (w & 1)]
        odds = [w for w in graph.c if w & 1]
        if len(odds) & 1:
            return -1, mp.mpf(0)
        degree += len(evens) + len(odds) // 2
        for power in evens:
            weight *= self.readout_moment(power)

        @functools.lru_cache(maxsize=None)
        def pair_odds(powers: tuple[int, ...]) -> mp.mpf:
            if not powers:
                return mp.mpf(1)
            first = powers[0]
            total = mp.mpf(0)
            for j in range(1, len(powers)):
                remainder = powers[1:j] + powers[j + 1 :]
                total += self.readout_moment(first + powers[j]) * pair_odds(
                    remainder
                )
            return total

        weight *= pair_odds(tuple(sorted(odds)))
        return degree, weight

    def _wick_uncached(self, graph: eg.Graph, target_degree: int) -> mp.mpf:
        odd_c = sum(w & 1 for w in graph.c)
        if odd_c & 1:
            return mp.mpf(0)
        max_degree = len(graph.x) + len(graph.c) - odd_c // 2
        if max_degree < target_degree:
            return mp.mpf(0)
        if max_degree - 2 * (graph.edge_count // 2) > target_degree:
            return mp.mpf(0)
        if not graph.edges:
            degree, weight = self.final_max_degree_and_weight(graph)
            if degree > target_degree:
                raise ArithmeticError(
                    f"unexpected divergent Wick term: {degree} > {target_degree}"
                )
            return weight if degree == target_degree else mp.mpf(0)

        from collections import Counter

        edges = Counter({(p, i): m for p, i, m in graph.edges})
        first = min(edges, key=lambda item: (-edges[item], item))
        edges[first] -= 1
        if not edges[first]:
            del edges[first]
        total = mp.mpf(0)
        for partner, multiplicity in list(edges.items()):
            reduced = edges.copy()
            reduced[partner] -= 1
            if not reduced[partner]:
                del reduced[partner]
            stripped = eg.graph_from(list(graph.c), list(graph.x), reduced)
            contracted = eg.merge_vertices(
                stripped, first[0], partner[0], first[1], partner[1]
            )
            if contracted.edges:
                contracted = eg.canonical_graph(contracted)
            total += multiplicity * self._wick(contracted, target_degree)
        return total

    def expected_large_n(self, polynomial: dict) -> mp.mpf:
        answer = mp.mpf(0)
        for (q, _), (graph, coefficient) in polynomial.items():
            if (sum(graph.c) & 1) or (graph.edge_count & 1):
                continue
            components = eg.connected_component_graphs(graph)
            if len(components) != q:
                raise ArithmeticError(
                    f"forest invariant failed: {len(components)} != q={q}"
                )
            value = mp.mpf(1)
            for component in components:
                if (component.edge_count & 1) or (sum(component.c) & 1):
                    value = mp.mpf(0)
                    break
                value *= self._wick(
                    eg.canonical_graph(component),
                    1 + component.edge_count // 2,
                )
                if not value:
                    break
            answer += coefficient * value
        return answer


def compute_jets(
    *,
    cutoff: float | None,
    max_order: int = 5,
    dps: int = 80,
) -> dict:
    if max_order < 0 or max_order > 5:
        raise ValueError("isolated reference is capped at order five")
    mp.mp.dps = dps
    if cutoff is None:
        moment = gaussian_moment
        law = {"kind": "standard_gaussian"}
        moment_table = {2 * k: gaussian_moment(2 * k) for k in range(7)}
    else:
        moment, moment_table = conditional_normal_moment_function(
            cutoff, max_power=24, dps=dps
        )
        law = {
            "kind": "conditional_standard_gaussian",
            "cutoff": str(cutoff),
            "variance_renormalized": False,
        }

    evaluator = LawEvaluator(moment)
    polynomial = eg.initial_observable()
    derivatives: list[mp.mpf] = []
    states: list[int] = []
    for order in range(max_order + 1):
        derivatives.append(evaluator.expected_large_n(polynomial))
        states.append(len(polynomial))
        if order < max_order:
            polynomial = eg.differentiate(polynomial)

    return {
        "schema_version": 1,
        "method": "accepted forest differentiation with configurable readout moments",
        "law": law,
        "max_order": max_order,
        "derivatives": [mp.nstr(value, dps) for value in derivatives],
        "state_counts": states,
        "readout_even_moments": {
            str(power): mp.nstr(value, dps)
            for power, value in sorted(moment_table.items())
            if power <= 12
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    law = parser.add_mutually_exclusive_group(required=True)
    law.add_argument("--cutoff", type=float)
    law.add_argument("--gaussian", action="store_true")
    parser.add_argument("--order", type=int, default=5)
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = compute_jets(
        cutoff=None if args.gaussian else args.cutoff,
        max_order=args.order,
        dps=args.dps,
    )
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
