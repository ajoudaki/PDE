"""Post-freeze elimination of the deterministic a43 coordinate.

The three-state producer was frozen first.  Since

    a43_l = d * (1 + a43_(l-1)),  a43_0 = 0,

one has ``1+a43_(l-1)=tau_(l-1)=l1``.  This module performs only that exact
deterministic substitution and combines identical commutative monomials.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from ...independent import forward_contraction as fw
from . import gamma04_contraction as g4


def replace_l43(polynomial: fw.SPoly) -> fw.SPoly:
    output: defaultdict[fw.SMonomial, Fraction] = defaultdict(Fraction)
    for monomial, coefficient in polynomial.items():
        target = tuple(sorted("l1" if name == "l43" else name for name in monomial))
        output[target] += coefficient
    return {monomial: coefficient for monomial, coefficient in output.items() if coefficient}


def transitions() -> dict[str, fw.SPoly]:
    source = g4.transitions()
    return {
        "gamma04_next": replace_l43(source["gamma04_next"]),
        "a41_next": replace_l43(source["a41_next"]),
    }


def emit() -> dict[str, object]:
    result = transitions()
    payload = {
        "status": "post-freeze exact deterministic reduction of Route A",
        "proof": "a43_l=d*(1+a43_(l-1)); 1+a43_l=tau_l; hence l43=l1",
        "state": ["gamma04", "a41"],
        "initial_state": {"gamma04": 0, "a41": 0},
        "layer_coefficients": {
            "l41": "9*q02 + 8*w + a41",
            "l43_eliminated": "l1=tau_(ell-1)",
        },
        "transition": {name: fw.serialise(poly) for name, poly in result.items()},
        "formatted": {name: fw.format_poly(poly) for name, poly in result.items()},
        "term_counts": {name: len(poly) for name, poly in result.items()},
    }
    here = Path(__file__).resolve().parent
    path = here / "REDUCED_GAMMA04_RECURRENCE.json"
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    markdown = here / "REDUCED_GAMMA04_TRANSITIONS.md"
    lines = [
        "# Post-freeze two-state Gamma_04 recurrence",
        "",
        "Exact substitution `l43=l1` in frozen Route A.",
        "",
    ]
    for name, formula in payload["formatted"].items():
        lines.extend((f"## `{name}`", "", "```text", f"{name} = {formula}", "```", ""))
    markdown.write_text("\n".join(lines))
    manifest = {
        "json": path.name,
        "json_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "markdown": markdown.name,
        "markdown_sha256": hashlib.sha256(markdown.read_bytes()).hexdigest(),
    }
    (here / "REDUCED_GAMMA04_FREEZE.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    )
    return {**manifest, "payload": payload}


if __name__ == "__main__":
    print(json.dumps(emit(), indent=2, sort_keys=True))
