"""Freeze the independent layer-tagged Q0=1 coefficient map.

This is a separate artifact from the already frozen unit-Gram quotient.  It is
needed for controls such as the canonical unnormalised quadratic activation,
for which Q1=3 and Q2=27 rather than one.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from .independent_compiler import compile_layer_tagged, mpoly_to_terms


def main() -> None:
    here = Path(__file__).resolve().parent
    result = compile_layer_tagged(q0=1, progress=True)
    payload = {
        "format": "independent-H2-B1-layer-tagged-Mpoly-v1",
        "Q0": "1",
        "atom_semantics": {
            "X_nu": "E_{G~N(0,Q0)} prod_r phi^(r)(G)^nu_r",
            "Y_nu": "E_{G~N(0,Q1)} prod_r phi^(r)(G)^nu_r",
            "Q1": "X_200000",
        },
        "A": mpoly_to_terms(result.A),
        "B": mpoly_to_terms(result.B),
        "C": mpoly_to_terms(result.C),
        "parity": {
            "F0": mpoly_to_terms(result.f_coefficients[0]),
            "F2_over_2factorial": mpoly_to_terms(result.f_coefficients[2]),
            "F4_over_4factorial": mpoly_to_terms(result.f_coefficients[4]),
        },
        "term_counts": {"A": len(result.A), "B": len(result.B), "C": len(result.C)},
    }
    exact = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode() + b"\n"
    path = here / "independent_layer_tagged_coefficient_map.json"
    path.write_bytes(exact)
    digest = hashlib.sha256(exact).hexdigest()
    (here / "LAYER_TAGGED_FROZEN_SHA256.txt").write_text(
        f"{digest}  {path.name}\n"
    )
    print(digest, path)


if __name__ == "__main__":
    main()
