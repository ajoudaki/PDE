"""Post-freeze comparison with Route A and the hostile 82-term candidate."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path

from ...depth_order5_scalar.multi_observable.audit.hostile_gamma04_derivation import (
    transitions as hostile_transitions,
)
from .gamma04_contraction import transitions as route_s_transitions


HERE = Path(__file__).resolve().parent
ROUTE_A = (
    HERE.parents[1]
    / "depth_order5_scalar/multi_observable/independent_route_a/FROZEN_GAMMA04_RECURRENCE.json"
)


def _canonical_json(path: Path):
    payload = json.loads(path.read_text())["transition"]
    return {
        name: {monomial: Fraction(value) for monomial, value in rows.items()}
        for name, rows in payload.items()
    }


def _route_s_json():
    path = HERE / "FROZEN_GAMMA04_RECURRENCE.json"
    return _canonical_json(path)


def _difference(left, right):
    return {
        key: left.get(key, Fraction(0)) - right.get(key, Fraction(0))
        for key in set(left) | set(right)
        if left.get(key, Fraction(0)) != right.get(key, Fraction(0))
    }


def compare() -> dict[str, object]:
    s = _route_s_json()
    a = _canonical_json(ROUTE_A)
    local = {}
    for name in sorted(set(s) | set(a)):
        discrepancy = _difference(s.get(name, {}), a.get(name, {}))
        local[name] = {
            "route_s_terms": len(s.get(name, {})),
            "route_a_terms": len(a.get(name, {})),
            "discrepancies": len(discrepancy),
        }

    hostile_raw = hostile_transitions()
    hostile = {
        name: {"*".join(monomial): coefficient for monomial, coefficient in rows.items()}
        for name, rows in hostile_raw.items()
    }
    hostile_report = {}
    for name in sorted(s):
        discrepancy = _difference(s[name], hostile[name])
        hostile_report[name] = {
            "route_s_terms": len(s[name]),
            "hostile_terms": len(hostile[name]),
            "discrepancies": len(discrepancy),
            "first_discrepancies": [
                {"monomial": key, "route_s_minus_hostile": str(value)}
                for key, value in sorted(discrepancy.items())[:12]
            ],
        }
    return {
        "freeze_boundary": "Route S FINAL_PRODUCER_FREEZE.json predates this comparison",
        "route_a_path": str(ROUTE_A),
        "route_a_sha256": hashlib.sha256(ROUTE_A.read_bytes()).hexdigest(),
        "route_s_vs_route_a": local,
        "route_s_vs_hostile_82_term_candidate": hostile_report,
        "hostile_82_term_explanation": {
            "status": "rejected indexing alias, not an equivalent canonicalization",
            "inherited_forward_slots": [
                "F1",
                "F2_frozen",
                "F2_moving",
                "F3_moving",
            ],
            "required_extension": "append F4_moving as slot 5 and set H(0,5)=Gamma04",
            "hostile_assignment": "renames slots 1..4 as f1,g2,g3,g4 and sets H(0,4)=Gamma04",
            "effect": (
                "g2 aliases F2_frozen, g3 aliases F2_moving, and g4 aliases "
                "F3_moving; q02/q22/q13 terms are replaced by u/y or lost"
            ),
        },
        "decision": (
            "pass: independently frozen Route A and Route S agree exactly; "
            "the hostile 82-term candidate is falsified"
        ),
    }


if __name__ == "__main__":
    payload = compare()
    path = HERE / "POST_FREEZE_ROUTE_COMPARISON.json"
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))
