"""Independent literal parser/auditor for the frozen primary sector.

This file does not import the producer module or its expression algebra.  It
parses the frozen CSE text as a tiny arithmetic language, reconstructs its
layer sweeps, expands exact polynomials, and compares them with independently
loaded frozen references.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
from typing import Mapping

from .reference_maps import Polynomial, difference, load_reference


HERE = Path(__file__).resolve().parent
TRANSITIONS = HERE.parent / "primary/FROZEN_SECTOR_TRANSITIONS.cse.txt"
EXPECTED_SHA256 = "d5c6c081f6a953126d29b67ec953a32e26d038327f2b92bda6037098d47ce721"

FORWARD = ("P", "V", "Q", "W", "S", "J3", "J5")
BACKWARD = ("B00", "B02", "B11", "B13", "B22", "K10", "K21", "K30", "K32")
ATOM = re.compile(r"M_\{([0-9]{6})\}\Z")
NUMBER = re.compile(r"-?[0-9]+(?:/[0-9]+)?\Z")
NAME = re.compile(r"[A-Z][A-Z0-9_]*\Z|t_[0-9]{5}\Z")


def add(*polys: Mapping[tuple[str, ...], Fraction]) -> Polynomial:
    result: defaultdict[tuple[str, ...], Fraction] = defaultdict(Fraction)
    for poly in polys:
        for key, value in poly.items():
            result[key] += value
    return {key: value for key, value in sorted(result.items()) if value}


def multiply(left: Mapping[tuple[str, ...], Fraction], right: Mapping[tuple[str, ...], Fraction]) -> Polynomial:
    result: defaultdict[tuple[str, ...], Fraction] = defaultdict(Fraction)
    for lkey, lvalue in left.items():
        for rkey, rvalue in right.items():
            result[tuple(sorted(lkey + rkey))] += lvalue * rvalue
    return {key: value for key, value in sorted(result.items()) if value}


def scale(poly: Mapping[tuple[str, ...], Fraction], value: int | Fraction) -> Polynomial:
    value = Fraction(value)
    return {key: value * coefficient for key, coefficient in poly.items() if value * coefficient}


def one(value: int | Fraction = 1) -> Polynomial:
    value = Fraction(value)
    return {} if not value else {(): value}


def atom(encoded: str) -> Polynomial:
    return {(f"M_{encoded}",): Fraction(1)}


def variable(name: str) -> Polynomial:
    return {(f"X_{name}",): Fraction(1)}


def power(poly: Polynomial, exponent: int) -> Polynomial:
    result = one()
    for _ in range(exponent):
        result = multiply(result, poly)
    return result


def tau(depth: int) -> Polynomial:
    d = atom("020000")
    return add(*(power(d, exponent) for exponent in range(depth + 1)))


def parse_sections(payload: str) -> dict[str, list[tuple[str, str]]]:
    sections: dict[str, list[tuple[str, str]]] = {}
    current: str | None = None
    for line_number, raw in enumerate(payload.splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("## "):
            current = line[3:]
            if current in sections:
                raise ValueError(f"duplicate section {current}")
            sections[current] = []
            continue
        if current is None or " = " not in line:
            raise ValueError(f"line {line_number}: {raw!r}")
        target, expression = line.split(" = ", 1)
        if not NAME.fullmatch(target):
            raise ValueError(f"line {line_number}: invalid target {target!r}")
        # The deliberately tiny grammar has no parentheses, division by a
        # moment/state, exponent operator, or implicit named evaluator.
        if any(character in expression for character in "()[]/^-"):
            raise ValueError(f"line {line_number}: forbidden syntax {expression!r}")
        sections[current].append((target, expression))
    expected = {
        "FORWARD_INITIALIZATION",
        "FORWARD_TRANSITION",
        "BACKWARD_TOP",
        "BACKWARD_TRANSITION",
        "TERMINAL_CONTRACTIONS",
    }
    if set(sections) != expected:
        raise ValueError(f"section mismatch: {set(sections) ^ expected}")
    return sections


def evaluate_factor(token: str, env: Mapping[str, Polynomial]) -> Polynomial:
    token = token.strip()
    match = ATOM.fullmatch(token)
    if match:
        return atom(match.group(1))
    if NUMBER.fullmatch(token):
        return one(Fraction(token))
    if not NAME.fullmatch(token):
        raise ValueError(f"unrecognized token {token!r}")
    try:
        return env[token]
    except KeyError as error:
        raise KeyError(f"use before definition: {token}") from error


def evaluate_expression(expression: str, env: Mapping[str, Polynomial]) -> Polynomial:
    terms: list[Polynomial] = []
    for term in expression.split(" + "):
        value = one()
        for factor in term.split(" * "):
            value = multiply(value, evaluate_factor(factor, env))
        terms.append(value)
    return add(*terms)


def run_section(
    assignments: list[tuple[str, str]],
    external: Mapping[str, Polynomial],
) -> dict[str, Polynomial]:
    env = dict(external)
    outputs: dict[str, Polynomial] = {}
    for target, expression in assignments:
        value = evaluate_expression(expression, env)
        env[target] = value
        if not target.startswith("t_"):
            outputs[target] = value
    return outputs


def _strip(values: Mapping[str, Polynomial], suffix: str) -> dict[str, Polynomial]:
    answer: dict[str, Polynomial] = {}
    for name, value in values.items():
        if not name.endswith(suffix):
            raise ValueError((name, suffix))
        answer[name[: -len(suffix)]] = value
    return answer


def reconstruct(depth: int, sections: Mapping[str, list[tuple[str, str]]]) -> dict[str, Polynomial]:
    if depth < 2:
        raise ValueError("the frozen comparison panel begins at H=2")
    d = atom("020000")
    forward: list[dict[str, Polynomial]] = [{} for _ in range(depth + 1)]
    first = run_section(
        sections["FORWARD_INITIALIZATION"],
        {"BASE_B1": power(d, depth - 1)},
    )
    forward[1] = _strip(first, "_1")
    for layer in range(2, depth + 1):
        outputs = run_section(
            sections["FORWARD_TRANSITION"],
            {
                **forward[layer - 1],
                "TAU": tau(layer - 1),
                "BASE_B": power(d, depth - layer),
            },
        )
        forward[layer] = _strip(outputs, "_NEXT")

    backward: list[dict[str, Polynomial]] = [{} for _ in range(depth + 1)]
    top = run_section(
        sections["BACKWARD_TOP"],
        {**forward[depth - 1], "TAU": tau(depth - 1)},
    )
    backward[depth] = _strip(top, "_H")
    zero_forward = {name: {} for name in FORWARD}
    for layer in range(depth - 1, 0, -1):
        outputs = run_section(
            sections["BACKWARD_TRANSITION"],
            {
                **(forward[layer - 1] if layer >= 2 else zero_forward),
                **backward[layer + 1],
                "TAU": tau(layer - 1),
            },
        )
        backward[layer] = _strip(outputs, "_NEXT")

    terminal = sections["TERMINAL_CONTRACTIONS"]
    top_terminal = run_section(terminal, {**forward[depth], **backward[1]})
    straight3 = top_terminal["STRAIGHT3"]
    straight5 = top_terminal["STRAIGHT5"]

    gram11 = add(forward[depth]["V"], backward[1]["B11"])
    gram31 = add(forward[depth]["W"], backward[1]["B13"])
    gram22 = add(forward[depth]["S"], backward[1]["B22"])
    for layer in range(2, depth + 1):
        local = run_section(terminal, {**forward[layer - 1], **backward[layer]})
        gram11 = add(gram11, local["GRAM11_LAYER"])
        gram31 = add(gram31, local["GRAM31_LAYER"])
        gram22 = add(gram22, local["GRAM22_LAYER"])

    return {
        "A": tau(depth),
        "B": add(scale(straight3, 2), scale(gram11, 4)),
        "partial_C": add(
            scale(straight5, 2), scale(gram31, 22), scale(gram22, 14)
        ),
    }


def derivative_ceiling(poly: Mapping[tuple[str, ...], Fraction]) -> int:
    maximum = 0
    for monomial in poly:
        for name in monomial:
            encoded = name.split("_", 1)[1]
            for derivative, count in enumerate(map(int, encoded)):
                if count:
                    maximum = max(maximum, derivative)
    return maximum


def projection_transition_audit(
    sections: Mapping[str, list[tuple[str, str]]]
) -> dict[str, int]:
    """Compare the five Section-7.1 transition coordinates symbolically."""

    d = atom("020000")
    u = atom("040000")
    v = atom("101000")
    m = atom("121000")
    r = atom("010100")
    s = atom("002000")
    j = atom("030100")
    e = atom("022000")
    h = atom("220000")
    external = {
        name: variable(name)
        for name in (*FORWARD, *BACKWARD, "TAU", "BASE_B")
    }
    forward = run_section(sections["FORWARD_TRANSITION"], external)
    backward = run_section(sections["BACKWARD_TRANSITION"], external)
    P, V, J3 = variable("P"), variable("V"), variable("J3")
    TAU, BASE = variable("TAU"), variable("BASE_B")
    B00, B11, K10 = variable("B00"), variable("B11"), variable("K10")
    expected = {
        "V_NEXT": add(multiply(d, V), multiply(multiply(multiply(TAU, TAU), BASE), u)),
        "P_NEXT": add(
            multiply(v, V),
            multiply(multiply(multiply(TAU, TAU), BASE), m),
            multiply(add(d, v), P),
        ),
        "J3_NEXT": add(
            scale(multiply(multiply(TAU, V), r), 3),
            scale(multiply(multiply(multiply(multiply(TAU, TAU), TAU), BASE), j), 3),
            scale(multiply(multiply(TAU, P), add(r, s)), 3),
            multiply(add(J3, scale(P, 3)), d),
        ),
        "B11_NEXT": add(
            multiply(multiply(multiply(B00, V), s), one()),
            scale(multiply(multiply(multiply(multiply(TAU, TAU), B00), B00), e), 3),
            multiply(d, B11),
            multiply(multiply(K10, K10), h),
            scale(multiply(multiply(multiply(multiply(TAU, K10), B00), m), one()), 2),
        ),
        "K10_NEXT": add(
            multiply(d, B00),
            multiply(multiply(multiply(TAU, B00), add(r, s)), one()),
            multiply(K10, add(v, d)),
        ),
    }
    got = {**forward, **backward}
    return {
        name: difference(got[name], value)["discrepancy_count"]
        for name, value in expected.items()
    }


def run_audit() -> dict[str, object]:
    payload = TRANSITIONS.read_bytes()
    actual_hash = hashlib.sha256(payload).hexdigest()
    if actual_hash != EXPECTED_SHA256:
        raise RuntimeError(f"candidate hash drift: {actual_hash}")
    text = payload.decode("utf-8")
    sections = parse_sections(text)
    result: dict[str, object] = {
        "schema": "independent-literal-primary-sector-audit-v1",
        "candidate_sha256": actual_hash,
        "imports_producer_module": False,
        "grammar": "addition, multiplication, rational constants, declared scalar states, M atoms",
        "state_dimensions": {"forward": len(FORWARD), "backward": len(BACKWARD)},
        "order3_projection_transition_discrepancies": projection_transition_audit(sections),
        "depths": {},
    }
    for depth in (2, 3, 4):
        roots = reconstruct(depth, sections)
        reference = load_reference(depth)
        result["depths"][str(depth)] = {
            "A": difference(roots["A"], reference["A"]),
            "B": difference(roots["B"], reference["B"]),
            "partial_C_vs_full_C": difference(roots["partial_C"], reference["C"]),
            "partial_C_count": len(roots["partial_C"]),
            "maximum_derivative": max(derivative_ceiling(root) for root in roots.values()),
        }
    return result


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
