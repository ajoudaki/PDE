"""Eliminate the redundant ``a43`` state from the frozen Route-S head.

The frozen third transition is ``a43^+ = d (1+a43)``.  Since ``a43_0=0``
and ``l1=tau_(ell-1)``, induction gives ``1+a43_(ell-1)=l1``.  This script
performs only the literal substitution ``l43 -> l1`` in the already frozen
two remaining transitions.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "FROZEN_GAMMA04_RECURRENCE.json"
SOURCE_SHA256 = "66449874726a3f424ec8cdcda27f90823c3317aa0b00fa7ebfbed9d1e88075b6"


def reduce() -> dict[str, object]:
    digest = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    if digest != SOURCE_SHA256:
        raise RuntimeError(f"source freeze changed: {digest}")
    source = json.loads(SOURCE.read_text())
    reduced: dict[str, dict[str, str]] = {}
    formatted: dict[str, str] = {}
    for name in ("gamma04_next", "a41_next"):
        output: dict[tuple[str, ...], Fraction] = {}
        for monomial, coefficient in source["transition"][name].items():
            factors = tuple(
                sorted("l1" if factor == "l43" else factor for factor in monomial.split("*"))
            )
            output[factors] = output.get(factors, Fraction(0)) + Fraction(coefficient)
        output = {key: value for key, value in output.items() if value}
        reduced[name] = {
            "*".join(key): str(value) for key, value in sorted(output.items())
        }
        terms: list[str] = []
        for factors, coefficient in sorted(output.items()):
            counts: dict[str, int] = {}
            for factor in factors:
                counts[factor] = counts.get(factor, 0) + 1
            rendered = "*".join(
                factor if power == 1 else f"{factor}^{power}"
                for factor, power in sorted(counts.items())
            )
            if coefficient == 1:
                terms.append(rendered or "1")
            elif coefficient == -1:
                terms.append("-" + (rendered or "1"))
            else:
                terms.append(f"{coefficient}*{rendered}" if rendered else str(coefficient))
        formatted[name] = " + ".join(terms).replace("+ -", "- ")
    return {
        "contract": "exact two-state projection of frozen Route S",
        "source_sha256": digest,
        "state": ["gamma04", "a41"],
        "initialization": {"gamma04": 0, "a41": 0},
        "derived_abbreviations": {
            "l41": "9*q02 + 8*w + a41",
            "l43_eliminated": "l43 = l1 = tau_(ell-1)",
        },
        "transition": reduced,
        "formatted": formatted,
        "term_counts": {name: len(value) for name, value in reduced.items()},
        "no_minimality_claim": True,
    }


if __name__ == "__main__":
    payload = reduce()
    path = HERE / "FROZEN_GAMMA04_REDUCED_RECURRENCE.json"
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    markdown = HERE / "FROZEN_GAMMA04_REDUCED_TRANSITIONS.md"
    lines = [
        "# Frozen two-state `Gamma_04` head",
        "",
        "Set `l41 = 9*q02 + 8*w + a41` and use the existing",
        "`l1 = tau_(ell-1)`. Initialize `gamma04=a41=0`.",
        "",
    ]
    for name, formula in payload["formatted"].items():
        lines.extend((f"## `{name}`", "", "```text", f"{name} = {formula}", "```", ""))
    markdown.write_text("\n".join(lines))
    print(path)
    print(hashlib.sha256(path.read_bytes()).hexdigest())
    print(markdown)
    print(hashlib.sha256(markdown.read_bytes()).hexdigest())
    print(json.dumps(payload["term_counts"], sort_keys=True))
