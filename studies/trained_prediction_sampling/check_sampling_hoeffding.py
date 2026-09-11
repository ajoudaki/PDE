#!/usr/bin/env python3
"""Exact finite verification of the Hilbert Hoeffding identities.

Purpose: check the decomposition, orthogonality, double-replacement identity,
higher-order bound, and exact sampling-remainder identity independently by
enumerating all Bernoulli outcomes. This is a deterministic rational-arithmetic
check, not a simulation or a training experiment.

Fixed inputs: m=4, Bernoulli p=2/5, and a prescribed symmetric R^3 statistic
specified by five unrelated vector values according to the count of ones.
All Hoeffding orders 1 through 4 must be nonzero, and the second-difference
bound must have strict positive slack, to make the fixture nondegenerate.

Success: every exact equality and inequality holds. Any failed assertion gives
a nonzero exit status. Resource bound: 16 base states, 6 replacement pairs,
and 64 original/replacement configurations per pair; no random draws or seeds.

Run from the repository root:
  python3 studies/trained_prediction_sampling/check_sampling_hoeffding.py

The command creates a fresh timestamped directory in the assigned generated
namespace and writes a JSON report including the source hash and Python version.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
from itertools import combinations, product
import json
from pathlib import Path
import platform


M = 4
P = F(2, 5)
DIMENSION = 3
TABLE = (
    (2, -1, 3),
    (-3, 4, 0),
    (5, 2, -2),
    (1, -5, 7),
    (-2, 6, 1),
)
TARGET = (F(1), F(2), F(-3))
INFLUENCE_DIRECTION = (F(3), F(-2), F(5))
ZERO = (F(0),) * DIMENSION


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(c, a):
    return tuple(c * x for x in a)


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def norm2(a):
    return dot(a, a)


def sum_vectors(items):
    total = ZERO
    for item in items:
        total = add(total, item)
    return total


def stat(state):
    return tuple(F(x) for x in TABLE[sum(state)])


def bit_weight(bit):
    return P if bit else 1 - P


def state_weight(state):
    result = F(1)
    for bit in state:
        result *= bit_weight(bit)
    return result


def replace(state, index, value):
    result = list(state)
    result[index] = value
    return tuple(result)


def encode(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {str(key): encode(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(item) for item in value]
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()

    source_path = Path(__file__).resolve()
    repository = source_path.parents[2]
    namespace = (
        repository
        / "data/generated/trained_prediction_sampling/statistical_checks"
    ).resolve()
    started = datetime.now(timezone.utc)
    default_name = "exact_hoeffding_" + started.strftime("%Y%m%dT%H%M%S_%fZ")
    output_dir = (args.output_dir or namespace / default_name).resolve()
    if namespace not in output_dir.parents:
        raise ValueError("The output directory must be a child of the assigned namespace.")
    output_dir.mkdir(parents=True, exist_ok=False)

    checks = Counter()

    def check(condition, category, detail):
        if not condition:
            raise AssertionError(f"{category}: {detail}")
        checks[category] += 1

    states = list(product((0, 1), repeat=M))
    weights = {state: state_weight(state) for state in states}

    def expect_scalar(fn):
        return sum((weights[state] * fn(state) for state in states), F(0))

    def expect_vector(fn):
        return sum_vectors(scale(weights[state], fn(state)) for state in states)

    check(sum(weights.values(), F(0)) == 1, "probability", "base weights sum to one")
    mean = expect_vector(stat)

    conditional = {}
    for mask in range(1 << M):
        for state in states:
            matching = [
                other
                for other in states
                if all(
                    other[index] == state[index]
                    for index in range(M)
                    if mask & (1 << index)
                )
            ]
            mass = sum((weights[other] for other in matching), F(0))
            conditional[mask, state] = scale(
                1 / mass,
                sum_vectors(scale(weights[other], stat(other)) for other in matching),
            )

    components = {}
    for mask in range(1 << M):
        subsets = [submask for submask in range(1 << M) if submask & mask == submask]
        for state in states:
            components[mask, state] = sum_vectors(
                scale(
                    F((-1) ** (mask.bit_count() - submask.bit_count())),
                    conditional[submask, state],
                )
                for submask in subsets
            )

    for state in states:
        check(
            sum_vectors(components[mask, state] for mask in range(1 << M)) == stat(state),
            "decomposition",
            repr(state),
        )
        check(components[0, state] == mean, "constant_component", repr(state))

    for mask in range(1, 1 << M):
        for index in range(M):
            if mask & (1 << index):
                for state in states:
                    conditional_zero = sum_vectors(
                        scale(bit_weight(bit), components[mask, replace(state, index, bit)])
                        for bit in (0, 1)
                    )
                    check(
                        conditional_zero == ZERO,
                        "coordinate_centering",
                        f"mask={mask}, index={index}, state={state}",
                    )

    energies = {
        mask: expect_scalar(lambda state, mask=mask: norm2(components[mask, state]))
        for mask in range(1 << M)
    }
    for left, right in combinations(range(1 << M), 2):
        inner_product = expect_scalar(
            lambda state: dot(components[left, state], components[right, state])
        )
        check(inner_product == 0, "orthogonality", f"masks={left},{right}")

    order_energies = {
        order: sum(
            (energies[mask] for mask in energies if mask.bit_count() == order), F(0)
        )
        for order in range(1, M + 1)
    }
    for order, energy in order_energies.items():
        check(energy > 0, "fixture_nondegeneracy", f"order={order}")

    higher = {
        state: sum_vectors(
            components[mask, state]
            for mask in range(1 << M)
            if mask.bit_count() >= 2
        )
        for state in states
    }
    higher_energy = expect_scalar(lambda state: norm2(higher[state]))
    check(
        higher_energy == sum((order_energies[order] for order in range(2, M + 1)), F(0)),
        "higher_order_energy",
        "direct residual equals sum of component energies",
    )

    replacement_results = {}
    for first, second in combinations(range(M), 2):
        direct = F(0)
        for state in states:
            for first_prime, second_prime in product((0, 1), repeat=2):
                replaced_first = replace(state, first, first_prime)
                replaced_second = replace(state, second, second_prime)
                replaced_both = replace(replaced_first, second, second_prime)
                difference = add(
                    sub(sub(stat(state), stat(replaced_first)), stat(replaced_second)),
                    stat(replaced_both),
                )
                direct += (
                    weights[state]
                    * bit_weight(first_prime)
                    * bit_weight(second_prime)
                    * norm2(difference)
                )
        pair_mask = (1 << first) | (1 << second)
        component_formula = 4 * sum(
            (energies[mask] for mask in energies if mask & pair_mask == pair_mask), F(0)
        )
        check(
            direct == component_formula,
            "replacement_identity",
            f"pair={first},{second}",
        )
        replacement_results[f"{first},{second}"] = {
            "enumerated_second_moment": direct,
            "four_times_containing_components": component_formula,
        }

    bound = sum(
        (result["enumerated_second_moment"] for result in replacement_results.values()),
        F(0),
    ) / 4
    check(higher_energy <= bound, "hoeffding_bound", "higher residual at most pair sum / 4")
    check(bound > higher_energy, "fixture_nondegeneracy", "bound has strict positive slack")
    weighted_order_sum = sum(
        (F(order * (order - 1), 2) * energy for order, energy in order_energies.items()),
        F(0),
    )
    check(bound == weighted_order_sum, "pair_sum_identity", "each order counted choose(order, 2)")

    h = {}
    for bit in (0, 1):
        candidates = [
            scale(F(M), components[1, state]) for state in states if state[0] == bit
        ]
        h[bit] = candidates[0]
        check(all(candidate == h[bit] for candidate in candidates), "first_projection", f"bit={bit}")
    for index in range(M):
        for state in states:
            check(
                scale(F(M), components[1 << index, state]) == h[state[index]],
                "first_projection_symmetry",
                f"index={index}, state={state}",
            )

    influence = {bit: scale(F(bit) - P, INFLUENCE_DIRECTION) for bit in (0, 1)}
    check(
        sum_vectors(scale(bit_weight(bit), influence[bit]) for bit in (0, 1)) == ZERO,
        "influence_centering",
        "chosen comparison influence is centered",
    )
    bias = sub(mean, TARGET)
    remainder_lhs = M * expect_scalar(
        lambda state: norm2(
            sub(
                sub(stat(state), TARGET),
                scale(F(1, M), sum_vectors(influence[bit] for bit in state)),
            )
        )
    )
    projection_difference = sum(
        (bit_weight(bit) * norm2(sub(h[bit], influence[bit])) for bit in (0, 1)), F(0)
    )
    remainder_terms = {
        "m_times_bias_squared": M * norm2(bias),
        "m_times_higher_order_second_moment": M * higher_energy,
        "first_projection_difference_L2_squared": projection_difference,
    }
    remainder_rhs = sum(remainder_terms.values(), F(0))
    check(remainder_lhs == remainder_rhs, "exact_remainder_identity", "three orthogonal terms")
    check(all(term > 0 for term in remainder_terms.values()), "fixture_nondegeneracy", "all three remainder terms are nonzero")

    report = {
        "status": "PASS",
        "started_utc": started.isoformat(),
        "completed_utc": datetime.now(timezone.utc).isoformat(),
        "method": "complete enumeration with fractions.Fraction; no floating point or random sampling",
        "source_path": str(source_path),
        "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
        "python_version": platform.python_version(),
        "working_directory": str(Path.cwd().resolve()),
        "inputs": {
            "sample_size": M,
            "bernoulli_probability": P,
            "hilbert_space": "R^3 with Euclidean inner product",
            "statistic_table_by_count": TABLE,
            "target_vector": TARGET,
            "comparison_influence": "(z-p) times influence_direction",
            "influence_direction": INFLUENCE_DIRECTION,
        },
        "enumeration": {
            "base_states": len(states),
            "replacement_pairs": len(replacement_results),
            "states_per_replacement_pair": len(states) * 4,
        },
        "checks_passed_by_category": dict(sorted(checks.items())),
        "total_checks_passed": sum(checks.values()),
        "expected_statistic": mean,
        "component_energies_by_mask": energies,
        "component_energies_by_order": order_energies,
        "replacement_results": replacement_results,
        "hoeffding_bound": {
            "higher_order_second_moment": higher_energy,
            "one_quarter_pair_second_moment_sum": bound,
            "strict_slack": bound - higher_energy,
        },
        "scaled_first_projection_by_observation": h,
        "exact_remainder_identity": {
            "direct_m_times_second_moment": remainder_lhs,
            "sum_of_three_terms": remainder_rhs,
            "terms": remainder_terms,
        },
        "limitations": "Finite exact verification of algebraic identities; not a proof of neural dynamics or asymptotic assumptions.",
    }
    report_path = output_dir / "report.json"
    report_path.write_text(json.dumps(encode(report), indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "checks": sum(checks.values()), "report": str(report_path)}))


if __name__ == "__main__":
    main()
