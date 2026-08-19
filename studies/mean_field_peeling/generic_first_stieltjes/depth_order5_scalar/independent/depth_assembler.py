"""Assemble the independent scalar contractions at arbitrary fixed depth.

The assembler performs only deterministic sparse-polynomial substitution.
All Gaussian elimination already occurred in the three contraction modules.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
import json
from math import prod
from pathlib import Path
from typing import Mapping

try:
    from . import forward_contraction as fw
    from . import reverse_contraction as rv
    from . import moving_contraction as mv
except ImportError:
    import forward_contraction as fw
    import reverse_contraction as rv
    import moving_contraction as mv


SPoly = fw.SPoly


def atom(name: str) -> SPoly:
    return fw.sv(name)


def _power(value: Mapping[fw.SMonomial, Fraction], exponent: int) -> SPoly:
    return fw.sp(value, exponent)


def substitute(
    polynomial: Mapping[fw.SMonomial, Fraction],
    values: Mapping[str, Mapping[fw.SMonomial, Fraction]],
) -> SPoly:
    """Substitute scalar polynomials for every non-M symbol exactly."""

    answer: SPoly = {}
    power_cache: dict[tuple[str, int], SPoly] = {}
    for monomial, coefficient in polynomial.items():
        counts: dict[str, int] = {}
        for name in monomial:
            counts[name] = counts.get(name, 0) + 1
        term = fw.sc(coefficient)
        for name, exponent in counts.items():
            if name.startswith("M"):
                base = atom(name)
            else:
                base = values[name]
            key = (name, exponent)
            if key not in power_cache:
                power_cache[key] = _power(base, exponent)
            term = fw.sm(term, power_cache[key])
        answer = fw.sa(answer, term)
    return answer


def _zero_state(names: tuple[str, ...]) -> dict[str, SPoly]:
    return {name: {} for name in names}


def _sum(*values: SPoly) -> SPoly:
    return fw.sa(*values)


def _mul(*values: SPoly) -> SPoly:
    return fw.sproduct(*values)


def compile_depth(hidden_layers: int) -> dict[str, SPoly]:
    if hidden_layers < 1:
        raise ValueError("hidden_layers must be positive")
    h = hidden_layers
    d = atom("M020000")
    tau = [fw.sc(1)]
    for _ in range(h):
        tau.append(_sum(fw.sc(1), _mul(d, tau[-1])))
    b = [fw.sc(0)] + [_power(d, h - layer) for layer in range(1, h + 1)]

    # Frozen forward pass.
    forward_names = ("u", "v", "w", "x", "y", "j", "k")
    forward = [_zero_state(forward_names) for _ in range(h + 1)]
    b1 = b[1]
    forward[1] = {
        "u": _mul(b1, atom("M121000")),
        "v": fw.ss(_mul(_power(b1, 2), atom("M140010")), 3),
        "w": _mul(b1, atom("M040000")),
        "x": fw.ss(_mul(_power(b1, 2), atom("M050100")), 3),
        "y": fw.ss(_mul(_power(b1, 2), atom("M042000")), 3),
        "j": fw.ss(_mul(b1, atom("M030100")), 3),
        "k": fw.ss(_mul(_power(b1, 2), atom("M050001")), 15),
    }
    frozen_transition = fw.transition()
    for layer in range(2, h + 1):
        previous = forward[layer - 1]
        values = {
            **previous,
            "b": b[layer],
            "l1": tau[layer - 1],
            "l3": _sum(previous["j"], fw.ss(previous["u"], 3)),
            "l5": _sum(previous["k"], fw.ss(previous["v"], 5)),
        }
        forward[layer] = {
            name.removesuffix("_next"): substitute(poly, values)
            for name, poly in frozen_transition.items()
        }

    # Frozen reverse pass.
    reverse_names = ("e02", "e11", "e13", "e22", "c10", "c21", "c30", "c32")
    reverse: list[dict[str, SPoly] | None] = [None] * (h + 1)
    frozen_sources: list[dict[str, SPoly] | None] = [None] * (h + 1)
    current = _zero_state(reverse_names)
    current["c10"] = fw.sc(1)
    reverse_transition = rv.transition()
    for layer in range(h, 0, -1):
        reverse[layer] = current
        previous = forward[layer - 1]
        values = {
            **previous,
            **current,
            "b": b[layer],
            "l1": tau[layer - 1],
            "l3": _sum(previous["j"], fw.ss(previous["u"], 3)),
        }
        output = {name: substitute(poly, values) for name, poly in reverse_transition.items()}
        frozen_sources[layer] = {
            name: output[name] for name in ("source00", "source02", "source11", "source13", "source22")
        }
        current = {name: output[name + "_next"] for name in reverse_names}

    # A.C and the order-three Hessian square while the frozen sources are live.
    ac = forward[h]["x"]
    hessian_square = forward[h]["w"]
    for layer in range(h, 0, -1):
        source = frozen_sources[layer]
        assert source is not None
        if layer == 1:
            ac = _sum(ac, source["source13"])
            hessian_square = _sum(hessian_square, source["source11"])
        else:
            previous = forward[layer - 1]
            ac = _sum(
                ac,
                source["source13"],
                fw.ss(_mul(source["source11"], previous["u"]), 3),
                fw.ss(_mul(source["source02"], previous["w"]), 3),
                _mul(source["source00"], previous["x"]),
            )
            hessian_square = _sum(
                hessian_square,
                source["source11"],
                _mul(source["source00"], previous["w"]),
            )

    moving = mv.transitions()

    # Moving feature derivative two.
    q2_names = ("q02", "q22", "qfm", "a2")
    q2 = [_zero_state(q2_names) for _ in range(h + 1)]
    for layer in range(1, h + 1):
        previous = forward[layer - 1]
        qprevious = q2[layer - 1]
        rcurrent = reverse[layer]
        assert rcurrent is not None
        values = {
            **previous, **qprevious, **rcurrent,
            "b": b[layer], "l1": tau[layer - 1],
            "l2": _sum(fw.sc(1), qprevious["a2"]),
        }
        q2[layer] = {
            name.removesuffix("_next"): substitute(poly, values)
            for name, poly in moving["feature2"].items()
        }

    # Moving gradient derivative two.
    r2_names = ("r02", "r22", "rfm", "d21")
    r2: list[dict[str, SPoly] | None] = [None] * (h + 1)
    moving2_sources: list[dict[str, SPoly] | None] = [None] * (h + 1)
    current = _zero_state(r2_names)
    current["d21"] = fw.sc(1)
    for layer in range(h, 0, -1):
        r2[layer] = current
        previous = forward[layer - 1]
        qprevious = q2[layer - 1]
        rcurrent = reverse[layer]
        assert rcurrent is not None
        values = {
            **previous, **qprevious, **rcurrent, **current,
            "b": b[layer], "l1": tau[layer - 1],
            "l2": _sum(fw.sc(1), qprevious["a2"]),
        }
        output = {name: substitute(poly, values) for name, poly in moving["gradient2"].items()}
        moving2_sources[layer] = {
            name: output[name] for name in ("source02m", "source22m", "sourcefm")
        }
        current = {name: output[name + "_next"] for name in r2_names}

    bm2 = q2[h]["qfm"]
    m2norm = q2[h]["q22"]
    for layer in range(h, 0, -1):
        frozen = frozen_sources[layer]
        source = moving2_sources[layer]
        assert frozen is not None and source is not None
        if layer == 1:
            bm2 = _sum(bm2, source["sourcefm"])
            m2norm = _sum(m2norm, source["source22m"])
        else:
            previous = forward[layer - 1]
            qprevious = q2[layer - 1]
            bm2 = _sum(
                bm2, source["sourcefm"],
                _mul(frozen["source02"], qprevious["q02"]),
                _mul(source["source02m"], previous["u"]),
                fw.ss(_mul(frozen["source11"], previous["w"]), 4),
                _mul(frozen["source00"], qprevious["qfm"]),
            )
            m2norm = _sum(
                m2norm, source["source22m"],
                fw.ss(_mul(source["source02m"], qprevious["q02"]), 2),
                fw.ss(_mul(frozen["source11"], previous["w"]), 4),
                _mul(frozen["source00"], qprevious["q22"]),
            )

    # Moving feature derivative three.
    q3_names = ("q13", "a30", "a32")
    q3 = [_zero_state(q3_names) for _ in range(h + 1)]
    for layer in range(1, h + 1):
        previous = forward[layer - 1]
        qprevious = q2[layer - 1]
        q3previous = q3[layer - 1]
        rcurrent = reverse[layer]
        r2current = r2[layer]
        assert rcurrent is not None and r2current is not None
        values = {
            **previous, **qprevious, **q3previous, **rcurrent, **r2current,
            "b": b[layer], "l1": tau[layer - 1],
            "l2": _sum(fw.sc(1), qprevious["a2"]),
            "l30": _sum(
                fw.ss(qprevious["q02"], 4), fw.ss(previous["w"], 3), q3previous["a30"]
            ),
            "l32": _sum(fw.sc(1), q3previous["a32"]),
        }
        q3[layer] = {
            name.removesuffix("_next"): substitute(poly, values)
            for name, poly in moving["feature3"].items()
        }

    # Moving gradient derivative three and A.m3 accumulator.
    r3_names = ("r13", "d30", "d32")
    moving3_source: list[SPoly | None] = [None] * (h + 1)
    current = _zero_state(r3_names)
    current["d32"] = fw.sc(1)
    for layer in range(h, 0, -1):
        previous = forward[layer - 1]
        qprevious = q2[layer - 1]
        q3previous = q3[layer - 1]
        rcurrent = reverse[layer]
        r2current = r2[layer]
        assert rcurrent is not None and r2current is not None
        values = {
            **previous, **qprevious, **q3previous, **rcurrent, **r2current, **current,
            "b": b[layer], "l1": tau[layer - 1],
            "l2": _sum(fw.sc(1), qprevious["a2"]),
            "l30": _sum(
                fw.ss(qprevious["q02"], 4), fw.ss(previous["w"], 3), q3previous["a30"]
            ),
            "l32": _sum(fw.sc(1), q3previous["a32"]),
        }
        output = {name: substitute(poly, values) for name, poly in moving["gradient3"].items()}
        moving3_source[layer] = output["source13m"]
        current = {name: output[name + "_next"] for name in r3_names}

    am3 = q3[h]["q13"]
    for layer in range(h, 0, -1):
        source = moving3_source[layer]
        frozen = frozen_sources[layer]
        source2 = moving2_sources[layer]
        assert source is not None and frozen is not None and source2 is not None
        if layer == 1:
            am3 = _sum(am3, source)
        else:
            previous = forward[layer - 1]
            qprevious = q2[layer - 1]
            am3 = _sum(
                am3, source,
                fw.ss(_mul(frozen["source11"], qprevious["q02"]), 3),
                fw.ss(_mul(source2["source02m"], previous["w"]), 3),
                _mul(frozen["source00"], q3[layer - 1]["q13"]),
            )

    straight3 = _sum(forward[h]["j"], fw.ss(forward[h]["u"], 3))
    straight5 = _sum(forward[h]["k"], fw.ss(forward[h]["v"], 5))
    A = tau[h]
    Bcoef = _sum(fw.ss(straight3, 2), fw.ss(hessian_square, 4))
    Ccoef = _sum(
        fw.ss(straight5, 2), fw.ss(ac, 10), fw.ss(bm2, 10),
        fw.ss(m2norm, 4), fw.ss(am3, 12),
    )
    return {
        "A": A, "B": Bcoef, "C": Ccoef,
        "S5": straight5, "AC": ac, "Bm2": bm2,
        "m2norm": m2norm, "Am3": am3,
    }


def _read_accepted(depth: int) -> dict[str, SPoly]:
    root = Path(__file__).resolve().parents[2]
    if depth == 2:
        path = root / "order5/compiler/PRIMARY_UNIT_COEFFICIENT_MAP.json"
        data = json.loads(path.read_text())["unit_gram"]
        rows = {
            name: [(row["atoms"], row["coefficient"]) for row in data[name]]
            for name in ("A", "B", "C")
        }
    elif depth in (3, 4):
        path = root / f"depth_order5/primary/H{depth}_UNIT_COEFFICIENTS.json"
        data = json.loads(path.read_text())["roots"]
        rows = {name: data[name] for name in ("A", "B", "C")}
    else:
        raise ValueError(depth)
    output: dict[str, SPoly] = {}
    for name, entries in rows.items():
        poly: SPoly = {}
        for atoms, coefficient in entries:
            monomial = tuple(sorted(value.replace("M_", "M") for value in atoms))
            poly = fw.sa(poly, {monomial: Fraction(coefficient)})
        output[name] = poly
    return output


def compare_accepted(depth: int) -> dict[str, object]:
    candidate = compile_depth(depth)
    accepted = _read_accepted(depth)
    report: dict[str, object] = {"depth": depth, "roots": {}}
    for name in ("A", "B", "C"):
        keys = set(candidate[name]) | set(accepted[name])
        discrepancies = {
            key: candidate[name].get(key, Fraction(0)) - accepted[name].get(key, Fraction(0))
            for key in keys
            if candidate[name].get(key, Fraction(0)) != accepted[name].get(key, Fraction(0))
        }
        report["roots"][name] = {
            "candidate_terms": len(candidate[name]),
            "accepted_terms": len(accepted[name]),
            "discrepancies": len(discrepancies),
        }
    return report


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("depth", type=int)
    parser.add_argument("--compare", action="store_true")
    args = parser.parse_args()
    if args.compare:
        print(json.dumps(compare_accepted(args.depth), indent=2, sort_keys=True))
    else:
        result = compile_depth(args.depth)
        print({name: len(result[name]) for name in ("A", "B", "C")})
