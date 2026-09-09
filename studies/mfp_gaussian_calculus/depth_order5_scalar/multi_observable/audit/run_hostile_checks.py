#!/usr/bin/env python3
"""Frozen hostile checks for the amortized Gamma_04 observable head.

This runner intentionally compares serialized producer artifacts against the
independent Route-H program.  It does not import either producer's contraction
tables.  Expensive Monte Carlo data are hash-checked and their preregistered
decisions are inspected rather than regenerated.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / "studies").is_dir())
ROUTE_A = HERE.parent / "independent_route_a"
ROUTE_S = (
    REPO
    / "studies/mean_field_peeling/generic_first_stieltjes"
    / "depth_order5_observables/independent"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path):
    return json.loads(path.read_text())


def run_json(module: str) -> tuple[dict, str]:
    raw = subprocess.check_output(
        [sys.executable, "-m", module], cwd=REPO, text=True
    )
    return json.loads(raw), hashlib.sha256(raw.encode()).hexdigest()


def parse_term(term: str) -> tuple[tuple[str, ...], Fraction]:
    coefficient = Fraction(1)
    factors: list[str] = []
    for factor in term.strip().split("*"):
        factor = factor.strip()
        try:
            coefficient *= Fraction(factor)
            continue
        except ValueError:
            pass
        if "^" in factor:
            name, exponent = factor.split("^", 1)
            factors.extend([name] * int(exponent))
        else:
            factors.append(factor)
    return tuple(sorted(factors)), coefficient


def parse_expression(expression: str) -> dict[tuple[str, ...], Fraction]:
    result: dict[tuple[str, ...], Fraction] = {}
    for term in expression.replace(" - ", " + -").split(" + "):
        monomial, coefficient = parse_term(term)
        result[monomial] = result.get(monomial, Fraction(0)) + coefficient
    return {m: c for m, c in result.items() if c}


def serialized_map(transition: dict[str, str]) -> dict[str, dict]:
    return {name: parse_expression(expr) for name, expr in transition.items()}


def producer_map(transition: dict[str, dict[str, str]]) -> dict[str, dict]:
    output = {}
    for name, terms in transition.items():
        polynomial: dict[tuple[str, ...], Fraction] = {}
        for monomial, coefficient in terms.items():
            factors, embedded = parse_term(monomial)
            polynomial[factors] = polynomial.get(factors, Fraction(0)) + embedded * Fraction(coefficient)
        output[name] = {m: c for m, c in polynomial.items() if c}
    return output


def discrepancy_count(left: dict, right: dict) -> int:
    return sum(
        left.get(key, Fraction(0)) != right.get(key, Fraction(0))
        for key in set(left) | set(right)
    )


def transition_discrepancies(left: dict[str, dict], right: dict[str, dict]) -> dict[str, int]:
    return {
        key: discrepancy_count(left.get(key, {}), right.get(key, {}))
        for key in sorted(set(left) | set(right))
    }


def eliminate_l43(polynomial: dict[tuple[str, ...], Fraction]) -> dict[tuple[str, ...], Fraction]:
    reduced: dict[tuple[str, ...], Fraction] = {}
    for monomial, coefficient in polynomial.items():
        key = tuple(sorted("l1" if factor == "l43" else factor for factor in monomial))
        reduced[key] = reduced.get(key, Fraction(0)) + coefficient
    return {m: c for m, c in reduced.items() if c}


def maximum_atom_derivative(transition: dict[str, dict]) -> int:
    maximum = -1
    for polynomial in transition.values():
        for monomial in polynomial:
            for factor in monomial:
                match = re.fullmatch(r"M([0-9]{6})", factor)
                if match:
                    digits = match.group(1)
                    maximum = max(maximum, max(i for i, v in enumerate(digits) if v != "0"))
    return maximum


checks: dict[str, object] = {}

# The hostile contract and independent programs must still be the preregistered files.
contract_freeze = load(HERE / "AUDIT_CONTRACT_FREEZE.json")
checks["contract_hash"] = sha256(HERE / contract_freeze["artifact"]) == contract_freeze["sha256"]

v2_freeze = load(HERE / "HOSTILE_CANDIDATE_V2_FREEZE.json")
checks["hostile_v2_source_hash"] = sha256(HERE / v2_freeze["artifact"]) == v2_freeze["artifact_sha256"]
v2, v2_stdout_sha = run_json(
    "studies.mean_field_peeling.generic_first_stieltjes.depth_order5_scalar.multi_observable.audit.hostile_gamma04_derivation_v2"
)
checks["hostile_v2_stdout_hash"] = v2_stdout_sha == v2_freeze["canonical_stdout_sha256"]

v1_freeze = load(HERE / "HOSTILE_CANDIDATE_FREEZE.json")
checks["hostile_v1_source_hash"] = sha256(HERE / v1_freeze["artifact"]) == v1_freeze["artifact_sha256"]
v1, v1_stdout_sha = run_json(
    "studies.mean_field_peeling.generic_first_stieltjes.depth_order5_scalar.multi_observable.audit.hostile_gamma04_derivation"
)
checks["hostile_v1_stdout_hash"] = v1_stdout_sha == v1_freeze["canonical_stdout_sha256"]

# Verify every file named by both final producer manifests.
route_a_manifest_path = ROUTE_A / "FINAL_ROUTE_A_FREEZE.json"
route_a_manifest = load(route_a_manifest_path)
checks["route_a_manifest_hash"] = sha256(route_a_manifest_path) == "5880677b1ea2567c8d44498fb634c4fc4ab771d43d7e5d37959b0df8d9deaab6"
checks["route_a_manifest_files"] = all(
    sha256(ROUTE_A / name) == digest
    for name, digest in route_a_manifest["files"].items()
)
route_a_pre_manifest = load(ROUTE_A / "PRE_REDUCTION_ROUTE_A_FREEZE.json")
route_a_pre_core = {
    "EQUALITY_PARTITION_LEDGER.json", "F7_TREE_ROADMAP_ROUTE_A.json",
    "FROZEN_GAMMA04_RECURRENCE.json", "FROZEN_GAMMA04_TRANSITIONS.md",
    "NORMALIZED_SINE_GAMMA04_RESULT.json", "finite_width_hidden.py",
    "gamma04_contraction.py", "numeric_head.py",
}
checks["route_a_pre_manifest_core_files"] = all(
    sha256(ROUTE_A / name) == digest
    for name, digest in route_a_pre_manifest["files"].items()
    if name in route_a_pre_core
)

route_s_manifest_path = ROUTE_S / "FINAL_PRODUCER_FREEZE.json"
route_s_manifest = load(route_s_manifest_path)
checks["route_s_manifest_hash"] = sha256(route_s_manifest_path) == "3a3fd13beeeea4a0947f459d829932f4feb2770ccaac7ea951155e785614f02e"
checks["route_s_manifest_files"] = all(
    sha256(ROUTE_S / name) == digest
    for section in ("unreduced_head", "reduced_public_head", "derivation_contracts")
    for name, digest in route_s_manifest[section].items()
    if isinstance(digest, str) and (ROUTE_S / name).is_file()
)

# Independent local contractions: Route H-v2, Route A, and Route S.
route_h_raw = serialized_map(v2["transition"])
route_h_v1_raw = serialized_map(v1["transition"])
route_a_raw = producer_map(load(ROUTE_A / "FROZEN_GAMMA04_RECURRENCE.json")["transition"])
route_s_raw = producer_map(load(ROUTE_S / "FROZEN_GAMMA04_RECURRENCE.json")["transition"])
checks["raw_H_vs_A_discrepancies"] = transition_discrepancies(route_h_raw, route_a_raw)
checks["raw_H_vs_S_discrepancies"] = transition_discrepancies(route_h_raw, route_s_raw)
checks["raw_A_vs_S_discrepancies"] = transition_discrepancies(route_a_raw, route_s_raw)
checks["falsified_v1_vs_A_discrepancies"] = transition_discrepancies(route_h_v1_raw, route_a_raw)
checks["raw_term_counts"] = {name: len(poly) for name, poly in route_h_raw.items()}

# Exact a43 -> tau reduction and all three reduced map comparisons.
route_h_reduced = {
    name: eliminate_l43(polynomial)
    for name, polynomial in route_h_raw.items()
    if name != "a43_next"
}
route_a_reduced_artifact = load(ROUTE_A / "REDUCED_GAMMA04_RECURRENCE.json")
route_s_reduced_artifact = load(ROUTE_S / "FROZEN_GAMMA04_REDUCED_RECURRENCE.json")
route_a_reduced = producer_map(route_a_reduced_artifact["transition"])
route_s_reduced = producer_map(route_s_reduced_artifact["transition"])
checks["reduced_H_vs_A_discrepancies"] = transition_discrepancies(route_h_reduced, route_a_reduced)
checks["reduced_H_vs_S_discrepancies"] = transition_discrepancies(route_h_reduced, route_s_reduced)
checks["reduced_A_vs_S_discrepancies"] = transition_discrepancies(route_a_reduced, route_s_reduced)
checks["reduced_term_counts"] = {name: len(poly) for name, poly in route_h_reduced.items()}
checks["a43_tau_reduction"] = (
    route_h_raw["a43_next"] == parse_expression("M020000*l43")
    and v2["substitutions"]["l43"] == "1 + a43"
    and route_a_reduced_artifact["proof"]
    == "a43_l=d*(1+a43_(l-1)); 1+a43_l=tau_l; hence l43=l1"
)

# Complete local partition/transpose ledger and derivative ceiling.
partition = load(ROUTE_A / "EQUALITY_PARTITION_LEDGER.json")
checks["partition_degree_exhaustion"] = (
    partition["maximum_forward_innovation_degree"] == 4
    and partition["maximum_reverse_innovation_degree"] == 4
    and {key: value["pre_wick_local_monomials"] for key, value in partition["targets"].items()}
    == {"gamma04_next": 51, "a41_next": 11, "a43_next": 1}
)
checks["transpose_branches"] = set(partition["transpose_response_branches"]) == {
    "Delta0", "Delta1", "Delta2", "Delta3"
}
checks["head_derivative_ceiling"] = (
    maximum_atom_derivative(route_h_raw)
    == maximum_atom_derivative(route_a_raw)
    == maximum_atom_derivative(route_s_raw)
    == 4
)

# Full-depth response-aware comparison, controls, finite-width, and parity gates.
exact = load(ROUTE_S / "POST_FREEZE_EXACT_AUDIT.json")
checks["H2_H3_H4_population_discrepancies"] = {
    depth: value["total_discrepancies"]
    for depth, value in exact["population_atomwise_comparisons"].items()
}
checks["H1_H4_two_state_discrepancies"] = {
    depth: value["total_discrepancies"]
    for depth, value in exact["two_state_projection_comparisons"].items()
}
checks["finite_width_two_oracle"] = exact["finite_width_two_oracle_gate"]
checks["readout_reflection"] = exact["readout_reflection_gate"]
controls = exact["exact_controls"]["activations"]
checks["constant_control"] = all(
    value == "0"
    for depths in controls["constant_1"].values()
    for layer in depths.values()
    for value in layer.values()
)
checks["linear_H2_control"] = {
    layer: controls["linear_x"]["2"][layer]
    for layer in ("1", "2")
}
checks["affine_H2_control"] = {
    layer: controls["affine_3plus4x_over5"]["2"][layer]
    for layer in ("1", "2")
}
checks["linear_control_exact"] = checks["linear_H2_control"] == {
    "1": {
        "Gamma02": "2", "Gamma04": "17", "Gamma11": "1",
        "Gamma13": "4", "Gamma22": "5", "Q2": "6", "Q4": "96",
    },
    "2": {
        "Gamma02": "4", "Gamma04": "53", "Gamma11": "5",
        "Gamma13": "40", "Gamma22": "17", "Q2": "18", "Q4": "528",
    },
}
checks["affine_control_exact"] = checks["affine_H2_control"] == {
    "1": {
        "Gamma02": "512/625", "Gamma04": "1581824/390625",
        "Gamma11": "4096/15625", "Gamma13": "4784128/9765625",
        "Gamma22": "364544/390625", "Q2": "33792/15625",
        "Q4": "172045824/9765625",
    },
    "2": {
        "Gamma02": "24592/15625", "Gamma04": "103905536/9765625",
        "Gamma11": "495872/390625", "Gamma13": "230838272/48828125",
        "Gamma22": "27339008/9765625", "Q2": "2221344/390625",
        "Q4": "3705931776/48828125",
    },
}

# Smooth nonpolynomial gates.  H3 is intentionally not upgraded: three widths
# make the preregistered quadratic-curvature comparison saturated.
route_a_sine = load(ROUTE_A / "NORMALIZED_SINE_GAMMA04_RESULT.json")
route_s_sine = load(ROUTE_S / "NORMALIZED_SINE_EXPERIMENT.json")
h3_freeze = load(HERE / "H3_REGRESSION_FREEZE.json")
h3_result = load(HERE / "H3_NORMALIZED_SINE_RESULT.json")
checks["route_a_H2_sine"] = {
    "decision": route_a_sine["decision"],
    "networks": route_a_sine["replicates_per_width"] * len(route_a_sine["widths"]),
    "layer2_gamma04_z": route_a_sine["fits"]["layer2_gamma04"]["z"],
    "layer2_q4_z": route_a_sine["fits"]["layer2_q4"]["z"],
}
checks["route_s_H2_sine"] = {
    "decision": route_s_sine["decision"],
    "networks": route_s_sine["total_networks"],
    "z": route_s_sine["fit"]["z"],
}
checks["hostile_H3_sine"] = {
    "decision": h3_result["decision"],
    "reason": h3_result["decision_reason"],
    "raw_hash_ok": sha256(HERE / h3_result["raw_path"]) == h3_freeze["raw_sha256_after_runner_serialization_failure"],
    "source_hash_ok": sha256(HERE / h3_freeze["runner"]) == h3_freeze["runner_sha256"],
    "postprocessor_hash_ok": sha256(HERE / h3_freeze["deterministic_postprocessor"])
    == h3_freeze["deterministic_postprocessor_sha256"],
    "nonfinite": h3_result["nonfinite_count"],
    "z_scores": {key: value["z"] for key, value in h3_result["fits"].items()},
}
extension_freeze = load(HERE / "H3_CURVATURE_EXTENSION_FREEZE.json")
extension_result = load(HERE / "H3_NORMALIZED_SINE_CURVATURE_EXTENSION_RESULT.json")
checks["hostile_H3_curvature_extension"] = {
    "decision": extension_result["decision"],
    "freeze_hashes_ok": (
        sha256(HERE / extension_freeze["contract"]) == extension_freeze["contract_sha256"]
        and sha256(HERE / extension_freeze["runner"]) == extension_freeze["runner_sha256"]
        and sha256(HERE / extension_freeze["serialization_wrapper"])
        == extension_freeze["serialization_wrapper_sha256"]
        and sha256(HERE / extension_result["raw_path"])
        == extension_freeze["first_raw_sha256"]
    ),
    "validity_gates": extension_result["validity_gates"],
    "identity_residual": extension_result["maximum_finite_width_identity_relative_residual"],
    "old_reproduction_error": extension_result["maximum_old_reproduction_scaled_error"],
    "nonfinite": extension_result["nonfinite_count"],
    "replication_required": extension_result["replication_required"],
    "affine_z_scores": {
        key: value["affine"]["z"] for key, value in extension_result["fits"].items()
    },
    "resolved_material_curvature": {
        key: value["resolved_material_curvature"]
        for key, value in extension_result["fits"].items()
    },
}

# Roadmap evidence only; this does not promote an F^(7) compiler claim.
free_tree_raw = subprocess.check_output([sys.executable, str(HERE / "count_free_trees.py")], text=True)
checks["free_tree_enumeration_roadmap_only"] = free_tree_raw.strip()


def all_zero(mapping: dict[str, int]) -> bool:
    return all(value == 0 for value in mapping.values())


promotion_gates = {
    "frozen_artifacts": all(
        checks[key] is True
        for key in (
            "contract_hash", "hostile_v2_source_hash", "hostile_v2_stdout_hash",
            "hostile_v1_source_hash", "hostile_v1_stdout_hash",
            "route_a_manifest_hash", "route_a_manifest_files",
            "route_a_pre_manifest_core_files",
            "route_s_manifest_hash", "route_s_manifest_files",
        )
    ),
    "three_route_raw_atom_comparison": all(
        all_zero(checks[key])
        for key in ("raw_H_vs_A_discrepancies", "raw_H_vs_S_discrepancies", "raw_A_vs_S_discrepancies")
    ),
    "falsified_alias_preserved": checks["falsified_v1_vs_A_discrepancies"]
    == {"a41_next": 4, "a43_next": 0, "gamma04_next": 31},
    "two_state_reduction": (
        checks["a43_tau_reduction"] is True
        and checks["reduced_term_counts"] == {"a41_next": 17, "gamma04_next": 64}
        and all(
            all_zero(checks[key])
            for key in ("reduced_H_vs_A_discrepancies", "reduced_H_vs_S_discrepancies", "reduced_A_vs_S_discrepancies")
        )
    ),
    "partition_transpose_and_ceiling": (
        checks["partition_degree_exhaustion"] is True
        and checks["transpose_branches"] is True
        and checks["head_derivative_ceiling"] is True
    ),
    "depth_population_maps": all(value == 0 for value in checks["H2_H3_H4_population_discrepancies"].values()),
    "two_state_depth_maps": all(value == 0 for value in checks["H1_H4_two_state_discrepancies"].values()),
    "finite_width_and_parity": (
        checks["finite_width_two_oracle"]["pass"] is True
        and checks["readout_reflection"]["pass"] is True
    ),
    "constant_linear_affine_controls": (
        checks["constant_control"] is True
        and checks["linear_control_exact"] is True
        and checks["affine_control_exact"] is True
    ),
    "smooth_nonpolynomial": (
        checks["route_a_H2_sine"]["decision"] == "pass"
        and checks["route_s_H2_sine"]["decision"] == "pass"
        and checks["hostile_H3_sine"]["decision"] == "inconclusive"
        and checks["hostile_H3_curvature_extension"]["decision"] == "pass"
        and checks["hostile_H3_curvature_extension"]["freeze_hashes_ok"] is True
        and all(checks["hostile_H3_curvature_extension"]["validity_gates"].values())
        and checks["hostile_H3_curvature_extension"]["replication_required"] is False
    ),
}

result = {
    "decision": "promote_gamma04_head" if all(promotion_gates.values()) else "withhold",
    "promotion_gates": promotion_gates,
    "checks": checks,
    "claim_boundary": {
        "promoted": "algebraically audited M-only Gamma_04 normal form and conditional fixed-H annealed theorem",
        "not_promoted": [
            "minimality of the two-state head",
            "growing-depth uniformity or positive-time convergence",
            "preactivation-RMS head",
            "any F^(7) closure/state/sweep/derivative-ceiling/O(H) claim",
        ],
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
if result["decision"] != "promote_gamma04_head":
    raise SystemExit(1)
