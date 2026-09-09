"""Independent distributive canonicalizer for a factored moment DAG."""

from __future__ import annotations

from fractions import Fraction

from .factored_expression import FactoredMomentExpression


Monomial = tuple[str, ...]


def expand_coefficient_map(root: FactoredMomentExpression) -> dict[Monomial, Fraction]:
    """Fully distribute a terminal DAG into its canonical atom coefficient map."""

    memo: dict[FactoredMomentExpression, dict[Monomial, Fraction]] = {}

    def visit(node: FactoredMomentExpression) -> dict[Monomial, Fraction]:
        if node in memo:
            return memo[node]
        kind = node.node[0]
        if kind == "const":
            answer = {(): node.node[1]} if node.node[1] else {}
        elif kind == "atom":
            layer, exponent = node.node[1], node.node[2]
            name = f"{layer}_{''.join(str(value) for value in exponent[:6])}"
            answer = {(name,): Fraction(1)}
        elif kind == "symbol":
            answer = {(node.node[1],): Fraction(1)}
        elif kind == "add":
            answer: dict[Monomial, Fraction] = {}
            for child in node.node[1]:
                for monomial, coefficient in visit(child).items():
                    answer[monomial] = answer.get(monomial, Fraction(0)) + coefficient
            answer = {key: value for key, value in answer.items() if value}
        elif kind == "mul":
            answer = {(): Fraction(1)}
            for child in node.node[1]:
                product: dict[Monomial, Fraction] = {}
                for left, cl in answer.items():
                    for right, cr in visit(child).items():
                        monomial = tuple(sorted(left + right))
                        product[monomial] = product.get(monomial, Fraction(0)) + cl * cr
                answer = {key: value for key, value in product.items() if value}
        else:
            raise ValueError(kind)
        memo[node] = answer
        return answer

    return visit(root)


def serializable_map(mapping: dict[Monomial, Fraction]) -> list[dict[str, object]]:
    return [
        {"atoms": list(monomial), "coefficient": str(coefficient)}
        for monomial, coefficient in sorted(mapping.items())
    ]
