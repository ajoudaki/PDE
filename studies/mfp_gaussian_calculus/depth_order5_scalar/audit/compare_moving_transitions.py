"""Literal exact comparison of the two frozen moving-transition encodings."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
PRIMARY = HERE.parent / "primary/MOVING_SECTOR_TRANSITIONS.cse.txt"
INDEPENDENT = HERE.parent / "independent/FROZEN_MOVING_RECURRENCE.json"
PRIMARY_SHA = "d394fff8e50d0b6a357f5712ba00f2ba961a2c8a7997de3ff22631c561988fe8"
INDEPENDENT_SHA = "aa530c6a2ff323398412df9e52b864ca955acf9296e5f1303af83090a10a7865"

Monomial = tuple[str, ...]
Poly = dict[Monomial, Fraction]
ATOM = re.compile(r"M_\{([0-9]{6})\}\Z")
NUMBER = re.compile(r"[0-9]+(?:/[0-9]+)?\Z")
NAME = re.compile(r"[A-Za-z][A-Za-z0-9_]*\Z|t_[0-9]{5}\Z")


def one(value: int | Fraction = 1) -> Poly:
    value = Fraction(value)
    return {} if not value else {(): value}


def add(*values: Poly) -> Poly:
    answer: defaultdict[Monomial, Fraction] = defaultdict(Fraction)
    for value in values:
        for monomial, coefficient in value.items():
            answer[monomial] += coefficient
    return {key: value for key, value in sorted(answer.items()) if value}


def multiply(left: Poly, right: Poly) -> Poly:
    answer: defaultdict[Monomial, Fraction] = defaultdict(Fraction)
    for lm, lc in left.items():
        for rm, rc in right.items():
            answer[tuple(sorted(lm + rm))] += lc * rc
    return {key: value for key, value in sorted(answer.items()) if value}


def factor(token: str, environment: dict[str, Poly]) -> Poly:
    match = ATOM.fullmatch(token)
    if match:
        return {("M" + match.group(1),): Fraction(1)}
    if NUMBER.fullmatch(token):
        return one(Fraction(token))
    if token in environment:
        return environment[token]
    if NAME.fullmatch(token):
        return {(token,): Fraction(1)}
    raise ValueError(token)


def expression(text: str, environment: dict[str, Poly]) -> Poly:
    terms: list[Poly] = []
    for raw_term in text.split(" + "):
        term = one()
        for raw_factor in raw_term.split(" * "):
            term = multiply(term, factor(raw_factor, environment))
        terms.append(term)
    return add(*terms)


def load_primary() -> dict[str, Poly]:
    payload = PRIMARY.read_bytes()
    if hashlib.sha256(payload).hexdigest() != PRIMARY_SHA:
        raise RuntimeError("primary transition hash drift")
    environment: dict[str, Poly] = {}
    roots: dict[str, Poly] = {}
    for line_number, raw in enumerate(payload.decode().splitlines(), 1):
        if not raw.strip():
            continue
        if " = " not in raw:
            raise ValueError((line_number, raw))
        target, text = raw.split(" = ", 1)
        if not NAME.fullmatch(target):
            raise ValueError((line_number, target))
        value = expression(text, environment)
        environment[target] = value
        if not target.startswith("t_"):
            roots[target.replace("__", "/")] = value
    return roots


def load_independent() -> dict[str, Poly]:
    payload = INDEPENDENT.read_bytes()
    if hashlib.sha256(payload).hexdigest() != INDEPENDENT_SHA:
        raise RuntimeError("independent transition hash drift")
    raw = json.loads(payload)["transition"]
    result: dict[str, Poly] = {}
    for group, roots in raw.items():
        for name, entries in roots.items():
            poly: defaultdict[Monomial, Fraction] = defaultdict(Fraction)
            for encoded, coefficient in entries.items():
                monomial = tuple(sorted(encoded.split("*"))) if encoded else ()
                poly[monomial] += Fraction(coefficient)
            result[f"{group}/{name}"] = {
                key: value for key, value in sorted(poly.items()) if value
            }
    return result


def compare() -> dict[str, object]:
    primary = load_primary()
    independent = load_independent()
    if set(primary) != set(independent):
        raise AssertionError({
            "primary_only": sorted(set(primary) - set(independent)),
            "independent_only": sorted(set(independent) - set(primary)),
        })
    roots: dict[str, object] = {}
    total = 0
    for name in sorted(primary):
        keys = set(primary[name]) | set(independent[name])
        discrepancy = sum(
            primary[name].get(key, 0) != independent[name].get(key, 0)
            for key in keys
        )
        roots[name] = {
            "primary_terms": len(primary[name]),
            "independent_terms": len(independent[name]),
            "discrepancies": discrepancy,
        }
        total += discrepancy
    return {
        "schema": "literal-moving-transition-comparison-v1",
        "primary_sha256": PRIMARY_SHA,
        "independent_sha256": INDEPENDENT_SHA,
        "root_count": len(roots),
        "total_discrepancies": total,
        "roots": roots,
        "provenance_caveat": "Both encodings descend from the same moving local contraction; this checks serialization/CSE, not an independent Wick derivation.",
    }


if __name__ == "__main__":
    print(json.dumps(compare(), indent=2, sort_keys=True))
