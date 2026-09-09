"""Freeze independent H=3,4 tagged and unit order-five maps."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from .depth_factored import (
    compile_depth_factored,
    emit_text,
    expand_expression,
    reachable,
    serialize_result,
)


HERE = Path(__file__).resolve().parent


def exact_write(path: Path, payload: object) -> str:
    data = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode() + b"\n"
    path.write_bytes(data)
    return hashlib.sha256(data).hexdigest()


def serial_map(mapping):
    return [
        {"atoms": list(monomial), "coefficient": str(coefficient)}
        for monomial, coefficient in sorted(mapping.items())
    ]


def main() -> None:
    manifest = {
        "format": "independent-depth-order5-freeze-manifest-v1",
        "scope": "H=3,4; B=1; Q0=1; layer-tagged and unit-Gram",
        "artifacts": {},
    }
    for depth in (3, 4):
        for unit in (False, True):
            label = f"H{depth}_{'UNIT' if unit else 'TAGGED'}"
            result = compile_depth_factored(depth, q0=1, unit_gram=unit, progress=True)
            dag_payload = serialize_result(result)
            dag_path = HERE / f"{label}_DAG.json"
            dag_hash = exact_write(dag_path, dag_payload)
            text_path = HERE / f"{label}_NORMAL_FORM.txt"
            text_path.write_text(emit_text(result))
            text_hash = hashlib.sha256(text_path.read_bytes()).hexdigest()
            expanded = {name: expand_expression(getattr(result, name)) for name in "ABC"}
            map_payload = {
                "format": "independent-depth-order5-expanded-map-v1",
                "hidden_layers": depth,
                "Q0": "1",
                "unit_gram": unit,
                "normalization": "M_200000=1" if unit else "layer-specific Lell_nu atoms",
                "A": serial_map(expanded["A"]),
                "B": serial_map(expanded["B"]),
                "C": serial_map(expanded["C"]),
            }
            map_path = HERE / f"{label}_COEFFICIENT_MAP.json"
            map_hash = exact_write(map_path, map_payload)
            manifest["artifacts"][label] = {
                "dag": {"file": dag_path.name, "sha256": dag_hash, "reachable_nodes": len(reachable((result.A, result.B, result.C)))},
                "text": {"file": text_path.name, "sha256": text_hash},
                "expanded": {
                    "file": map_path.name,
                    "sha256": map_hash,
                    "term_counts": {name: len(expanded[name]) for name in "ABC"},
                },
                "parity_zero": [result.f_coefficients[index] is result.factory.zero for index in (0, 2, 4)],
                "maximum_derivative": max(
                    (
                        derivative
                        for node in reachable((result.A, result.B, result.C))
                        if node.node[0] == "atom"
                        for derivative, count in enumerate(node.node[2])
                        if count
                    ),
                    default=0,
                ),
            }
            print(label, manifest["artifacts"][label], flush=True)
    manifest_path = HERE / "FROZEN_MANIFEST.json"
    manifest_hash = exact_write(manifest_path, manifest)
    (HERE / "FROZEN_MANIFEST_SHA256.txt").write_text(
        f"{manifest_hash}  {manifest_path.name}\n"
    )
    print("manifest", manifest_hash, flush=True)


if __name__ == "__main__":
    main()
