"""Post-freeze assembler and exact atomwise audit for the `Gamma_04` head."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Iterable

from ...depth_order5.independent.depth_factored import expand_expression
from ...depth_order5.primary.depth_population_jet import activation_product_moment
from ...depth_order5_scalar.primary.moving_scalar_extension import (
    MovingScalarResult,
    assemble_moving_recurrence,
    local_common_replacements,
)
from ...depth_order5_scalar.primary.scalar_frozen_recurrence import (
    FORWARD_NAMES,
    substitute_symbols,
)
from ...order5.compiler.coefficient_map import expand_coefficient_map
from ...order5.compiler.factored_expression import (
    FactoredMomentExpression as Expr,
    atom,
    constant,
    product,
    summation,
    symbol,
)
from .reference_population_head import compile_reference


HERE = Path(__file__).resolve().parent
FROZEN = HERE / "FROZEN_GAMMA04_RECURRENCE.json"
EXPECTED_FROZEN_SHA256 = (
    "66449874726a3f424ec8cdcda27f90823c3317aa0b00fa7ebfbed9d1e88075b6"
)
REDUCED = HERE / "FROZEN_GAMMA04_REDUCED_RECURRENCE.json"
EXPECTED_REDUCED_SHA256 = (
    "e97a3f6afda6ae17d1be498ac79b308b64fc71e7fd94a1f343e0e28844762122"
)


def _load_templates() -> dict[str, Expr]:
    digest = hashlib.sha256(FROZEN.read_bytes()).hexdigest()
    if digest != EXPECTED_FROZEN_SHA256:
        raise RuntimeError(f"frozen Gamma_04 map changed: {digest}")
    payload = json.loads(FROZEN.read_text())
    templates: dict[str, Expr] = {}
    for name, rows in payload["transition"].items():
        terms: list[Expr] = []
        for raw_monomial, raw_coefficient in rows.items():
            factors: list[Expr] = [constant(Fraction(raw_coefficient))]
            if raw_monomial:
                for value in raw_monomial.split("*"):
                    if value.startswith("M") and len(value) == 7 and value[1:].isdigit():
                        factors.append(atom("M", tuple(int(digit) for digit in value[1:])))
                    else:
                        factors.append(symbol(value))
            terms.append(product(tuple(factors)))
        templates[name] = summation(tuple(terms))
    return templates


def _load_reduced_templates() -> dict[str, Expr]:
    digest = hashlib.sha256(REDUCED.read_bytes()).hexdigest()
    if digest != EXPECTED_REDUCED_SHA256:
        raise RuntimeError(f"reduced Gamma_04 map changed: {digest}")
    payload = json.loads(REDUCED.read_text())
    templates: dict[str, Expr] = {}
    for name, rows in payload["transition"].items():
        terms: list[Expr] = []
        for raw_monomial, raw_coefficient in rows.items():
            factors: list[Expr] = [constant(Fraction(raw_coefficient))]
            if raw_monomial:
                for value in raw_monomial.split("*"):
                    if value.startswith("M") and len(value) == 7 and value[1:].isdigit():
                        factors.append(atom("M", tuple(int(digit) for digit in value[1:])))
                    else:
                        factors.append(symbol(value))
            terms.append(product(tuple(factors)))
        templates[name] = summation(tuple(terms))
    return templates


@dataclass(frozen=True)
class Gamma04HeadResult:
    depth: int
    backbone: MovingScalarResult
    head: tuple[dict[str, Expr], ...]


def assemble_head(depth: int) -> Gamma04HeadResult:
    if depth < 1:
        raise ValueError("depth must be positive")
    backbone = assemble_moving_recurrence(depth)
    templates = _load_templates()
    head: list[dict[str, Expr]] = [
        {"gamma04": constant(0), "a41": constant(0), "a43": constant(0)}
        for _ in range(depth + 1)
    ]
    for layer in range(1, depth + 1):
        previous_frozen = (
            backbone.frozen.forward[layer - 1]
            if layer >= 2
            else {name: constant(0) for name in FORWARD_NAMES}
        )
        replacements = local_common_replacements(
            depth,
            layer,
            backbone.frozen,
            backbone.feature2[layer - 1],
            backbone.gradient2[layer + 1],
            backbone.feature3[layer - 1],
            backbone.gradient3[layer + 1],
        )
        replacements.update(head[layer - 1])
        replacements.update(
            {
                "l41": (
                    9 * backbone.feature2[layer - 1]["q02"]
                    + 8 * previous_frozen["V"]
                    + head[layer - 1]["a41"]
                ),
                "l43": constant(1) + head[layer - 1]["a43"],
            }
        )
        values = {
            name: substitute_symbols(template, replacements)
            for name, template in templates.items()
        }
        head[layer] = {
            "gamma04": values["gamma04_next"],
            "a41": values["a41_next"],
            "a43": values["a43_next"],
        }
    return Gamma04HeadResult(depth, backbone, tuple(head))


def assemble_reduced_head(depth: int) -> Gamma04HeadResult:
    """Assemble the exact two-state projection with ``l43=l1``."""

    if depth < 1:
        raise ValueError("depth must be positive")
    backbone = assemble_moving_recurrence(depth)
    templates = _load_reduced_templates()
    head: list[dict[str, Expr]] = [
        {"gamma04": constant(0), "a41": constant(0)}
        for _ in range(depth + 1)
    ]
    for layer in range(1, depth + 1):
        previous_frozen = (
            backbone.frozen.forward[layer - 1]
            if layer >= 2
            else {name: constant(0) for name in FORWARD_NAMES}
        )
        replacements = local_common_replacements(
            depth,
            layer,
            backbone.frozen,
            backbone.feature2[layer - 1],
            backbone.gradient2[layer + 1],
            backbone.feature3[layer - 1],
            backbone.gradient3[layer + 1],
        )
        replacements.update(head[layer - 1])
        replacements["l41"] = (
            9 * backbone.feature2[layer - 1]["q02"]
            + 8 * previous_frozen["V"]
            + head[layer - 1]["a41"]
        )
        values = {
            name: substitute_symbols(template, replacements)
            for name, template in templates.items()
        }
        head[layer] = {
            "gamma04": values["gamma04_next"],
            "a41": values["a41_next"],
        }
    return Gamma04HeadResult(depth, backbone, tuple(head))


def compare_reduced_projection(depth: int) -> dict[str, object]:
    full = assemble_head(depth)
    reduced = assemble_reduced_head(depth)
    layers: dict[str, object] = {}
    total = 0
    for layer in range(1, depth + 1):
        left = expand_coefficient_map(full.head[layer]["gamma04"])
        right = expand_coefficient_map(reduced.head[layer]["gamma04"])
        discrepancy = _diff(left, right)
        total += len(discrepancy)
        layers[str(layer)] = {
            "full_terms": len(left),
            "reduced_terms": len(right),
            "discrepancies": len(discrepancy),
        }
    return {"depth": depth, "layers": layers, "total_discrepancies": total}


def _normalize_reference_map(
    mapping: dict[tuple[str, ...], Fraction]
) -> dict[tuple[str, ...], Fraction]:
    answer: dict[tuple[str, ...], Fraction] = {}
    for monomial, coefficient in mapping.items():
        normalized: list[str] = []
        for name in monomial:
            if not name.startswith("M_"):
                raise ValueError(f"non-M reference atom: {name}")
            digits = name[2:]
            if any(value != "0" for value in digits[6:]):
                raise ValueError(f"derivative ceiling exceeded: {name}")
            normalized.append("M_" + digits[:6].ljust(6, "0"))
        key = tuple(sorted(normalized))
        answer[key] = answer.get(key, Fraction(0)) + coefficient
    return {key: value for key, value in answer.items() if value}


def _diff(
    candidate: dict[tuple[str, ...], Fraction],
    reference: dict[tuple[str, ...], Fraction],
) -> dict[tuple[str, ...], Fraction]:
    return {
        key: candidate.get(key, Fraction(0)) - reference.get(key, Fraction(0))
        for key in set(candidate) | set(reference)
        if candidate.get(key, Fraction(0)) != reference.get(key, Fraction(0))
    }


def compare_reference(depth: int) -> dict[str, object]:
    if depth < 2:
        raise ValueError("the independent response-aware reference starts at H=2")
    candidate = assemble_head(depth)
    reference = compile_reference(depth)
    report: dict[str, object] = {"depth": depth, "layers": {}}
    for layer in range(1, depth + 1):
        roots = {
            "Gamma11": candidate.backbone.frozen.forward[layer]["V"],
            "Gamma02": candidate.backbone.feature2[layer]["q02"],
            "Gamma22": candidate.backbone.feature2[layer]["q22"],
            "Gamma13": candidate.backbone.feature3[layer]["q13"],
            "Gamma04": candidate.head[layer]["gamma04"],
        }
        targets = {
            "Gamma11": reference.gamma11[layer],
            "Gamma02": reference.gamma02[layer],
            "Gamma22": reference.gamma22[layer],
            "Gamma13": reference.gamma13[layer],
            "Gamma04": reference.gamma04[layer],
        }
        layer_report: dict[str, object] = {}
        for name in roots:
            # Candidate and reference use deliberately separate distributive
            # canonicalizers.
            candidate_map = expand_coefficient_map(roots[name])
            reference_map = _normalize_reference_map(expand_expression(targets[name]))
            discrepancy = _diff(candidate_map, reference_map)
            layer_report[name] = {
                "candidate_terms": len(candidate_map),
                "reference_terms": len(reference_map),
                "discrepancies": len(discrepancy),
                "first_discrepancies": [
                    {"atoms": list(key), "difference": str(value)}
                    for key, value in sorted(discrepancy.items())[:5]
                ],
            }
        report["layers"][str(layer)] = layer_report
    report["total_discrepancies"] = sum(
        record["discrepancies"]
        for layer in report["layers"].values()
        for record in layer.values()
    )
    return report


def evaluate_unit_polynomial(
    root: Expr, coefficients: Iterable[int | Fraction]
) -> Fraction:
    coefficients = tuple(Fraction(value) for value in coefficients)
    memo: dict[Expr, Fraction] = {}

    def visit(node: Expr) -> Fraction:
        if node in memo:
            return memo[node]
        kind = node.node[0]
        if kind == "const":
            value = node.node[1]
        elif kind == "atom":
            if node.node[1] != "M":
                raise KeyError(node.node[1])
            value = activation_product_moment(node.node[2], coefficients, Fraction(1))
        elif kind == "add":
            value = sum((visit(child) for child in node.node[1]), Fraction(0))
        elif kind == "mul":
            value = Fraction(1)
            for child in node.node[1]:
                value *= visit(child)
        else:
            raise ValueError(node.node)
        memo[node] = value
        return value

    return visit(root)


def exact_controls(depths: Iterable[int] = (1, 2, 3, 4)) -> dict[str, object]:
    activations = {
        "constant_1": (1,),
        "linear_x": (0, 1),
        "affine_3plus4x_over5": (Fraction(3, 5), Fraction(4, 5)),
    }
    report: dict[str, object] = {"activations": {}}
    for activation_name, coefficients in activations.items():
        depth_rows: dict[str, object] = {}
        for depth in depths:
            result = assemble_head(depth)
            layer_rows: dict[str, object] = {}
            for layer in range(1, depth + 1):
                w = evaluate_unit_polynomial(
                    result.backbone.frozen.forward[layer]["V"], coefficients
                )
                q02 = evaluate_unit_polynomial(
                    result.backbone.feature2[layer]["q02"], coefficients
                )
                q22 = evaluate_unit_polynomial(
                    result.backbone.feature2[layer]["q22"], coefficients
                )
                q13 = evaluate_unit_polynomial(
                    result.backbone.feature3[layer]["q13"], coefficients
                )
                gamma04 = evaluate_unit_polynomial(
                    result.head[layer]["gamma04"], coefficients
                )
                q2 = 2 * (w + q02)
                q4 = 2 * gamma04 + 8 * q13 + 6 * q22
                layer_rows[str(layer)] = {
                    "Gamma11": str(w),
                    "Gamma02": str(q02),
                    "Gamma22": str(q22),
                    "Gamma13": str(q13),
                    "Gamma04": str(gamma04),
                    "Q2": str(q2),
                    "Q4": str(q4),
                }
            depth_rows[str(depth)] = layer_rows
        report["activations"][activation_name] = depth_rows
    return report


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", type=int, default=2)
    parser.add_argument("--controls", action="store_true")
    args = parser.parse_args()
    print(
        json.dumps(
            exact_controls() if args.controls else compare_reference(args.depth),
            indent=2,
            sort_keys=True,
        )
    )
