"""Generate deterministic Route S formula and exact coefficient artifacts.

Run once per requested depth.  The coefficient JSON writer is deliberately
streaming because the H=4 tagged distributive normal form is large.
"""

from __future__ import annotations

import argparse
import gc
import hashlib
import json
from pathlib import Path
from time import perf_counter

from studies.mean_field_peeling.generic_first_stieltjes.order5.compiler.coefficient_map import (
    expand_coefficient_map,
)
from studies.mean_field_peeling.generic_first_stieltjes.order5.compiler.factored_expression import (
    emit_cse,
    walk,
)

from .depth_population_jet import (
    compile_depth,
    evaluate_polynomial_activation,
    specialize_unit_gram,
    terminal_maximum_derivative,
)


HERE = Path(__file__).resolve().parent


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_coefficient_json(path: Path, depth: int, quotient: str, roots) -> dict[str, int]:
    temporary = path.with_suffix(path.suffix + ".tmp")
    counts: dict[str, int] = {}
    with temporary.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write('{"schema":"route-s-coefficient-map-v1","depth":')
        stream.write(str(depth))
        stream.write(',"quotient":')
        stream.write(json.dumps(quotient, separators=(",", ":")))
        stream.write(',"roots":{')
        for root_index, (name, root) in enumerate(roots.items()):
            if root_index:
                stream.write(",")
            stream.write(json.dumps(name))
            stream.write(":[")
            started = perf_counter()
            mapping = expand_coefficient_map(root)
            counts[name] = len(mapping)
            for index, (monomial, coefficient) in enumerate(sorted(mapping.items())):
                if index:
                    stream.write(",")
                json.dump(
                    [list(monomial), str(coefficient)],
                    stream,
                    ensure_ascii=True,
                    separators=(",", ":"),
                )
            stream.write("]")
            print(
                f"{path.name} {name}: {len(mapping)} terms in "
                f"{perf_counter() - started:.3f}s",
                flush=True,
            )
            del mapping
            gc.collect()
        stream.write("}}\n")
    temporary.replace(path)
    return counts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", type=int, choices=(3, 4), required=True)
    args = parser.parse_args()
    depth = args.depth

    started = perf_counter()
    result = compile_depth(depth, order=5, arbitrary_q0=True, verbose=True)
    tagged = {"A": result.A, "B": result.B, "C": result.C}
    unit = {name: specialize_unit_gram(root) for name, root in tagged.items()}

    tagged_cse = HERE / f"H{depth}_LAYER_TAGGED_ABC.cse.txt"
    unit_cse = HERE / f"H{depth}_UNIT_ABC.cse.txt"
    tagged_cse.write_text(emit_cse(tagged) + "\n", encoding="utf-8")
    unit_cse.write_text(emit_cse(unit) + "\n", encoding="utf-8")

    tagged_json = HERE / f"H{depth}_LAYER_TAGGED_COEFFICIENTS.json"
    unit_json = HERE / f"H{depth}_UNIT_COEFFICIENTS.json"
    tagged_counts = write_coefficient_json(tagged_json, depth, "layer-tagged-arbitrary-Q0", tagged)
    unit_counts = write_coefficient_json(unit_json, depth, "unit-Gram-M200000=1", unit)

    controls = {}
    for name, coefficients in {
        "zero": (0,),
        "constant_2": (2,),
        "linear": (0, 1),
        "affine_1_plus_x": (1, 1),
        "quadratic_x2": (0, 0, 1),
    }.items():
        controls[name] = {
            root_name: str(
                evaluate_polynomial_activation(root, depth, coefficients, q0=1)
            )
            for root_name, root in tagged.items()
        }

    stats = {
        "schema": "route-s-depth-stats-v1",
        "depth": depth,
        "order": 5,
        "compile_and_emit_seconds": perf_counter() - started,
        "tagged_term_counts": tagged_counts,
        "unit_term_counts": unit_counts,
        "tagged_dag_node_counts": {name: len(walk(root)) for name, root in tagged.items()},
        "unit_dag_node_counts": {name: len(walk(root)) for name, root in unit.items()},
        "maximum_terminal_derivative": {
            name: terminal_maximum_derivative(root) for name, root in tagged.items()
        },
        "parity": {
            "F0_is_zero": not bool(result.derivatives[0]),
            "F2_is_zero": not bool(result.derivatives[2]),
            "F4_is_zero": not bool(result.derivatives[4]),
        },
        "registry_counts": {
            "alpha_stored": len(result.alpha),
            "beta_stored": len(result.beta),
            "H_symmetric_dictionary": len(result.H),
            "B_symmetric_dictionary": len(result.Bcov),
            "unique_states_formula": 66 * (depth - 1),
        },
        "coordinate_term_counts": dict(result.counts),
        "polynomial_controls_Q0_1": controls,
        "artifact_sha256": {
            path.name: sha256(path)
            for path in (tagged_cse, unit_cse, tagged_json, unit_json)
        },
    }
    stats_path = HERE / f"H{depth}_ARTIFACT_STATS.json"
    stats_path.write_text(json.dumps(stats, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(stats_path)
    print(json.dumps(stats["artifact_sha256"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

