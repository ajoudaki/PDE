"""Post-freeze atomwise comparison of Routes S and A.

The two depth assemblers and their local transition tables were frozen before
either route inspected the other.  This checker compares not only A, B, C but
also each of the five regrouped order-five terminal sectors.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from ..audit.reference_maps import difference
from ..independent.depth_assembler import compile_depth
from ...order5.compiler.coefficient_map import expand_coefficient_map
from .moving_scalar_extension import assemble_moving_recurrence


HERE = Path(__file__).resolve().parent
ROUTE_S_FREEZE = HERE / "FULL_SCALAR_CANDIDATE_FREEZE.json"
ROUTE_A_FREEZE = HERE.parent / "independent/FROZEN_MANIFEST.json"
EXPECTED_S = "d731ec66b067b8739df305426c6aa6d06bbc309d5fd624bd16d1c283ca649728"
EXPECTED_A = "0699148b5d5fcd77a821908f333e230e36e148afad710e2421c36ab89c7441f8"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize_analytic(poly: dict[tuple[str, ...], Fraction]):
    return {
        tuple(sorted("M_" + atom[1:] if atom.startswith("M") else atom for atom in monomial)): coefficient
        for monomial, coefficient in poly.items()
        if coefficient
    }


def compare_depth(depth: int) -> dict[str, object]:
    route_s = assemble_moving_recurrence(depth)
    s_roots = {
        "A": route_s.frozen.A,
        "B": route_s.frozen.B,
        "C": route_s.C,
        "S5": route_s.frozen.straight5,
        "AC": route_s.frozen.gram31,
        "Bm2": route_s.B_m2,
        "m2norm": route_s.m2_norm,
        "Am3": route_s.A_m3,
    }
    s_maps = {name: expand_coefficient_map(root) for name, root in s_roots.items()}
    a_maps = {name: normalize_analytic(poly) for name, poly in compile_depth(depth).items()}
    comparisons = {name: difference(s_maps[name], a_maps[name]) for name in s_roots}
    if any(value["discrepancy_count"] for value in comparisons.values()):
        raise AssertionError((depth, comparisons))
    return {"depth": depth, "roots": comparisons}


def run(depths: list[int]) -> dict[str, object]:
    if sha256(ROUTE_S_FREEZE) != EXPECTED_S or sha256(ROUTE_A_FREEZE) != EXPECTED_A:
        raise RuntimeError("producer freeze hash drift")
    return {
        "schema": "post-freeze-two-route-atomwise-comparison-v1",
        "route_S_freeze_sha256": EXPECTED_S,
        "route_A_freeze_sha256": EXPECTED_A,
        "depths": {str(depth): compare_depth(depth) for depth in depths},
        "decision": "PASS: every requested root agrees atom by atom",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("depth", nargs="*", type=int, default=[1, 2, 3])
    args = parser.parse_args()
    print(json.dumps(run(args.depth), indent=2, sort_keys=True))
