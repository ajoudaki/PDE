"""Post-freeze assembler for the independently derived moving-gradient passes.

The local sparse transition polynomials come from the independent analytic
route.  This module supplies a separately written depth/index assembler and
canonical comparison target.  It never imports either accepted order-five
population compiler.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from ..independent import moving_contraction
from ...order5.compiler.factored_expression import (
    FactoredMomentExpression as Expr,
    atom,
    constant,
    product,
    summation,
    symbol,
)
from .scalar_frozen_recurrence import (
    FORWARD_NAMES,
    FrozenRecurrenceResult,
    assemble_frozen_recurrence,
    substitute_symbols,
    tau,
)


def sparse_to_expr(poly) -> Expr:
    terms: list[Expr] = []
    for monomial, coefficient in poly.items():
        factors: list[Expr] = [constant(coefficient)]
        for name in monomial:
            if name.startswith("M") and len(name) == 7 and name[1:].isdigit():
                factors.append(atom("M", tuple(int(value) for value in name[1:])))
            else:
                factors.append(symbol(name))
        terms.append(product(factors))
    return summation(terms)


def moving_templates() -> dict[str, dict[str, Expr]]:
    return {
        group: {name: sparse_to_expr(poly) for name, poly in values.items()}
        for group, values in moving_contraction.transitions().items()
    }


FEATURE2_NAMES = ("q02", "q22", "qfm", "a2")
GRADIENT2_NAMES = ("r02", "r22", "rfm", "d21")
FEATURE3_NAMES = ("q13", "a30", "a32")
GRADIENT3_NAMES = ("r13", "d30", "d32")


def zero_state(names: tuple[str, ...]) -> dict[str, Expr]:
    return {name: constant(0) for name in names}


def frozen_input_seed() -> dict[str, Expr]:
    return {
        "B00": constant(1),
        "B02": constant(0),
        "B11": constant(0),
        "B13": constant(0),
        "B22": constant(0),
        "K10": constant(1),
        "K21": constant(0),
        "K30": constant(0),
        "K32": constant(0),
    }


def gradient2_seed() -> dict[str, Expr]:
    return {"r02": constant(0), "r22": constant(0), "rfm": constant(0), "d21": constant(1)}


def gradient3_seed() -> dict[str, Expr]:
    return {"r13": constant(0), "d30": constant(0), "d32": constant(1)}


def forward_at_zero() -> dict[str, Expr]:
    return {name: constant(0) for name in FORWARD_NAMES}


def local_common_replacements(
    depth: int,
    layer: int,
    frozen: FrozenRecurrenceResult,
    feature2_previous: dict[str, Expr],
    gradient2_incoming: dict[str, Expr] | None = None,
    feature3_previous: dict[str, Expr] | None = None,
    gradient3_incoming: dict[str, Expr] | None = None,
) -> dict[str, Expr]:
    previous = frozen.forward[layer - 1] if layer >= 2 else forward_at_zero()
    frozen_incoming = (
        frozen_input_seed() if layer == depth else frozen.backward[layer + 1]
    )
    replacements: dict[str, Expr] = {
        # Frozen forward contractions used by the local mixed laws.
        "u": previous["P"],
        "w": previous["V"],
        "y": previous["S"],
        "l1": tau(layer - 1),
        # Frozen reverse carrier/source input at this layer.
        "b": frozen_incoming["B00"],
        "e02": frozen_incoming["B02"],
        "e11": frozen_incoming["B11"],
        "e22": frozen_incoming["B22"],
        "c10": frozen_incoming["K10"],
        "c21": frozen_incoming["K21"],
        # Moving second-feature input.
        **feature2_previous,
        "l2": constant(1) + feature2_previous["a2"],
    }
    if gradient2_incoming is not None:
        replacements.update(gradient2_incoming)
    if feature3_previous is not None:
        replacements.update(feature3_previous)
        replacements.update(
            {
                "l30": (
                    4 * feature2_previous["q02"]
                    + 3 * previous["V"]
                    + feature3_previous["a30"]
                ),
                "l32": constant(1) + feature3_previous["a32"],
            }
        )
    if gradient3_incoming is not None:
        replacements.update(gradient3_incoming)
    return replacements


@dataclass(frozen=True)
class MovingScalarResult:
    depth: int
    frozen: FrozenRecurrenceResult
    feature2: tuple[dict[str, Expr], ...]
    gradient2: tuple[dict[str, Expr], ...]
    feature3: tuple[dict[str, Expr], ...]
    gradient3: tuple[dict[str, Expr], ...]
    B_m2: Expr
    m2_norm: Expr
    A_m3: Expr
    C: Expr


def assemble_moving_recurrence(depth: int) -> MovingScalarResult:
    if depth < 1:
        raise ValueError("depth must be positive")
    frozen = assemble_frozen_recurrence(depth)
    templates = moving_templates()

    feature2: list[dict[str, Expr]] = [{} for _ in range(depth + 1)]
    feature2[0] = zero_state(FEATURE2_NAMES)
    for layer in range(1, depth + 1):
        replacements = local_common_replacements(
            depth, layer, frozen, feature2[layer - 1]
        )
        feature2[layer] = {
            name.replace("_next", ""): substitute_symbols(value, replacements)
            for name, value in templates["feature2"].items()
        }

    gradient2: list[dict[str, Expr]] = [{} for _ in range(depth + 2)]
    gradient2[depth + 1] = gradient2_seed()
    gradient2_sources: list[dict[str, Expr]] = [{} for _ in range(depth + 1)]
    for layer in range(depth, 0, -1):
        replacements = local_common_replacements(
            depth,
            layer,
            frozen,
            feature2[layer - 1],
            gradient2[layer + 1],
        )
        values = {
            name: substitute_symbols(value, replacements)
            for name, value in templates["gradient2"].items()
        }
        gradient2[layer] = {
            "r02": values["r02_next"],
            "r22": values["r22_next"],
            "rfm": values["rfm_next"],
            "d21": values["d21_next"],
        }
        gradient2_sources[layer] = {
            "s02m": values["source02m"],
            "s22m": values["source22m"],
            "sfm": values["sourcefm"],
        }

    b_m2 = feature2[depth]["qfm"]
    m2_norm = feature2[depth]["q22"]
    for layer in range(1, depth + 1):
        source = gradient2_sources[layer]
        if layer == 1:
            b_m2 = b_m2 + source["sfm"]
            m2_norm = m2_norm + source["s22m"]
            continue
        previous = frozen.forward[layer - 1]
        frozen_source = frozen.backward[layer]
        qprev = feature2[layer - 1]
        b_m2 = (
            b_m2
            + source["sfm"]
            + frozen_source["B02"] * qprev["q02"]
            + source["s02m"] * previous["P"]
            + 4 * frozen_source["B11"] * previous["V"]
            + frozen_source["B00"] * qprev["qfm"]
        )
        m2_norm = (
            m2_norm
            + source["s22m"]
            + 2 * source["s02m"] * qprev["q02"]
            + 4 * frozen_source["B11"] * previous["V"]
            + frozen_source["B00"] * qprev["q22"]
        )

    feature3: list[dict[str, Expr]] = [{} for _ in range(depth + 1)]
    feature3[0] = zero_state(FEATURE3_NAMES)
    for layer in range(1, depth + 1):
        replacements = local_common_replacements(
            depth,
            layer,
            frozen,
            feature2[layer - 1],
            gradient2[layer + 1],
            feature3[layer - 1],
        )
        feature3[layer] = {
            name.replace("_next", ""): substitute_symbols(value, replacements)
            for name, value in templates["feature3"].items()
        }

    gradient3: list[dict[str, Expr]] = [{} for _ in range(depth + 2)]
    gradient3[depth + 1] = gradient3_seed()
    gradient3_sources: list[dict[str, Expr]] = [{} for _ in range(depth + 1)]
    for layer in range(depth, 0, -1):
        replacements = local_common_replacements(
            depth,
            layer,
            frozen,
            feature2[layer - 1],
            gradient2[layer + 1],
            feature3[layer - 1],
            gradient3[layer + 1],
        )
        values = {
            name: substitute_symbols(value, replacements)
            for name, value in templates["gradient3"].items()
        }
        gradient3[layer] = {
            "r13": values["r13_next"],
            "d30": values["d30_next"],
            "d32": values["d32_next"],
        }
        gradient3_sources[layer] = {"s13m": values["source13m"]}

    a_m3 = feature3[depth]["q13"]
    for layer in range(1, depth + 1):
        source = gradient3_sources[layer]["s13m"]
        if layer == 1:
            a_m3 = a_m3 + source
            continue
        previous = frozen.forward[layer - 1]
        frozen_source = frozen.backward[layer]
        moving2_source = gradient2_sources[layer]
        qprev = feature2[layer - 1]
        q3prev = feature3[layer - 1]
        a_m3 = (
            a_m3
            + source
            + 3 * frozen_source["B11"] * qprev["q02"]
            + 3 * moving2_source["s02m"] * previous["V"]
            + frozen_source["B00"] * q3prev["q13"]
        )

    c = (
        2 * frozen.straight5
        + 10 * frozen.gram31
        + 10 * b_m2
        + 4 * m2_norm
        + 12 * a_m3
    )
    return MovingScalarResult(
        depth,
        frozen,
        tuple(feature2),
        tuple(gradient2),
        tuple(feature3),
        tuple(gradient3),
        b_m2,
        m2_norm,
        a_m3,
        c,
    )
