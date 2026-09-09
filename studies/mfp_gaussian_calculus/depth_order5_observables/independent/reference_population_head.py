"""Post-freeze independent population reference for hidden feature Grams.

This is intentionally not a scalar-head producer.  It reruns the complete
response-aware arbitrary-depth population jet, retains the moving activation
coordinates, and contracts ``24 E[h_0 h_4]`` directly.  It was added only
after ``FROZEN_ROUTE_S_MANIFEST.json`` fixed the candidate three-state map.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import factorial

from ...depth_order5.primary.depth_population_jet import (
    CoordinatePolynomial,
    Layout,
    Peeler,
    activation_coefficient,
    cp_a,
    cp_constant,
    cp_f,
    cp_r,
    specialize_unit_gram,
)
from ...order5.compiler.factored_expression import (
    FactoredMomentExpression as Expr,
    constant,
)


@dataclass(frozen=True)
class PopulationHeadReference:
    depth: int
    gamma04: tuple[Expr, ...]
    gamma02: tuple[Expr, ...]
    gamma11: tuple[Expr, ...]
    gamma22: tuple[Expr, ...]
    gamma13: tuple[Expr, ...]


def compile_reference(depth: int) -> PopulationHeadReference:
    """Compile all hidden-layer Gram atoms through total derivative four."""

    if depth < 1:
        raise ValueError("depth must be positive")
    order = 4
    layout = Layout(depth)
    peeler = Peeler(layout)

    u = {
        layer: [CoordinatePolynomial.zero() for _ in range(order + 1)]
        for layer in range(1, depth + 1)
    }
    h = {
        layer: [CoordinatePolynomial.zero() for _ in range(order + 1)]
        for layer in range(1, depth + 1)
    }
    hp = {
        layer: [CoordinatePolynomial.zero() for _ in range(order + 1)]
        for layer in range(1, depth + 1)
    }
    b = {
        layer: [CoordinatePolynomial.zero() for _ in range(order)]
        for layer in range(1, depth + 1)
    }
    r = {
        layer: [CoordinatePolynomial.zero() for _ in range(order)]
        for layer in range(2, depth + 1)
    }
    a = [CoordinatePolynomial.zero() for _ in range(order + 1)]
    a[0] = cp_a(layout)

    for degree in range(order + 1):
        h[1][degree] = activation_coefficient(layout, 1, u[1], degree)
        if degree < order:
            hp[1][degree] = activation_coefficient(
                layout, 1, u[1], degree, 1
            )

        for layer in range(2, depth + 1):
            for ell in range(degree + 1):
                peeler.set_h(
                    layer,
                    degree,
                    ell,
                    peeler.expect(h[layer - 1][degree] * h[layer - 1][ell]),
                )
            if degree > 0:
                uk = cp_f(layout, layer, degree)
                for response_order in range(degree):
                    alpha = peeler.expect(
                        h[layer - 1][degree].derivative_r(
                            layout, layer, response_order
                        )
                    )
                    uk = uk + b[layer][response_order].scale(layout, alpha)
                for partition_degree in range(1, degree + 1):
                    for back_order in range(partition_degree):
                        q = partition_degree - 1 - back_order
                        inner = peeler.expect(
                            h[layer - 1][q]
                            * h[layer - 1][degree - partition_degree]
                        )
                        uk = uk + b[layer][back_order].scale(
                            layout,
                            Fraction(1, partition_degree) * inner,
                        )
                u[layer][degree] = uk
            h[layer][degree] = activation_coefficient(
                layout, layer, u[layer], degree
            )
            if degree < order:
                hp[layer][degree] = activation_coefficient(
                    layout, layer, u[layer], degree, 1
                )

        if degree == order:
            break

        a[degree + 1] = h[depth][degree].divide(layout, degree + 1)
        top = CoordinatePolynomial.zero()
        for left in range(degree + 1):
            top = top + a[left] * hp[depth][degree - left]
        b[depth][degree] = top

        for layer in range(depth, 1, -1):
            for ell in range(degree + 1):
                peeler.set_b(
                    layer,
                    degree,
                    ell,
                    peeler.expect(b[layer][degree] * b[layer][ell]),
                )
            beta = {
                response_order: peeler.expect(
                    b[layer][degree].derivative_f(
                        layout, layer, response_order
                    )
                )
                for response_order in range(degree + 1)
            }
            rk = cp_r(layout, layer, degree)
            for response_order in range(degree + 1):
                rk = rk + h[layer - 1][response_order].scale(
                    layout, beta[response_order]
                )
            for partition_degree in range(1, degree + 1):
                for back_order in range(partition_degree):
                    q = partition_degree - 1 - back_order
                    inner = peeler.expect(
                        b[layer][back_order]
                        * b[layer][degree - partition_degree]
                    )
                    rk = rk + h[layer - 1][q].scale(
                        layout,
                        Fraction(1, partition_degree) * inner,
                    )
            r[layer][degree] = rk
            lower = CoordinatePolynomial.zero()
            for left in range(degree + 1):
                lower = (
                    lower
                    + hp[layer - 1][left]
                    * r[layer][degree - left]
                )
            b[layer - 1][degree] = lower

        u[1][degree + 1] = b[1][degree].divide(layout, degree + 1)

    def gram(layer: int, left: int, right: int) -> Expr:
        return specialize_unit_gram(
            factorial(left)
            * factorial(right)
            * peeler.expect(h[layer][left] * h[layer][right])
        )

    zero = constant(0)
    gamma04 = [zero]
    gamma02 = [zero]
    gamma11 = [zero]
    gamma22 = [zero]
    gamma13 = [zero]
    for layer in range(1, depth + 1):
        gamma04.append(gram(layer, 0, 4))
        gamma02.append(gram(layer, 0, 2))
        gamma11.append(gram(layer, 1, 1))
        gamma22.append(gram(layer, 2, 2))
        gamma13.append(gram(layer, 1, 3))
    return PopulationHeadReference(
        depth,
        tuple(gamma04),
        tuple(gamma02),
        tuple(gamma11),
        tuple(gamma22),
        tuple(gamma13),
    )
