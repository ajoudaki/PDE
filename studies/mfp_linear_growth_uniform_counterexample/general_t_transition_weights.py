"""Exact Euler elementary-differential weights for the general paired horizon."""

from __future__ import annotations

from fractions import Fraction
from math import comb


F = Fraction


def state_and_output_weights(number_of_steps: int):
    """Return the six [h^5] output weights after N Euler steps.

    Basis:
      E1=V[g^5], E2=U[Hg,g^3], E3=T[T[g,g],g,g],
      E4=T[H^2g,g,g], E5=T[Hg,Hg,g], E6=||H^2g||^2.
    """

    # State coefficients through order four.  x3=(c3,b3) in the bases
    # H^2g,T[g,g]; x4=(a4,b4,c4,d4) in the bases
    # H^3g,H T[g,g],T[g,Hg],U[g,g,g].
    c3 = b3 = F(0)
    a4 = b4 = c4 = d4 = F(0)
    x2 = F(0)

    # p dot x5, already reduced to the six scalar families.
    px5 = [F(0) for _ in range(6)]

    for step in range(number_of_steps):
        r = F(step)

        # Increment x5 using the state at the start of this Euler step.
        px5[0] += r**4 / 24
        px5[1] += d4 + r**2 * x2 / 2
        px5[2] += r * b3
        px5[3] += b4 + r * c3
        px5[4] += c4 + x2**2 / 2
        px5[5] += a4

        # Increment x4, x3, and x2 in descending order so every right-hand
        # side uses the old state.
        a4 += c3
        b4 += b3
        c4 += r * x2
        d4 += r**3 / 6
        c3 += x2
        b3 += r**2 / 2
        x2 += r

    n = F(number_of_steps)

    # Taylor-expand the terminal observable f(x+delta_N).
    answer = px5[:]
    answer[0] += n**5 / 120
    answer[1] += n * d4 + n**3 * x2 / 6
    answer[2] += n**2 * b3 / 2
    answer[3] += n * b4 + x2 * b3 + n**2 * c3 / 2
    answer[4] += n * c4 + n * x2**2 / 2
    answer[5] += n * a4 + x2 * c3
    return tuple(answer)


def cubic_output_weights(number_of_steps: int):
    """Return weights of T[g,g,g] and ||Hg||^2 in [h^3]F_N."""

    n = F(number_of_steps)
    x2 = F(comb(number_of_steps, 2))
    # x3 coefficients accumulated by Euler: H^2g and T[g,g].
    c3 = F(comb(number_of_steps, 3))
    b3 = sum((F(r) ** 2 / 2 for r in range(number_of_steps)), F(0))
    # p.x3 + H[x1,x2] + T[x1^3]/6.
    t_weight = b3 + n**3 / 6
    h_weight = c3 + n * x2
    return t_weight, h_weight


def finite_differences(values):
    current = list(values)
    answer = []
    while current:
        answer.append(current[0])
        current = [right - left for left, right in zip(current, current[1:])]
    return tuple(answer)


def poly_add(left, right):
    size = max(len(left), len(right))
    out = [F(0)] * size
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    while out and out[-1] == 0:
        out.pop()
    return tuple(out)


def poly_scale(polynomial, scalar):
    return tuple(F(scalar) * value for value in polynomial)


def poly_mul(left, right):
    out = [F(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return tuple(out)


def binomial_polynomial(scale: int, order: int):
    out = (F(1),)
    for shift in range(order):
        out = poly_mul(out, (F(-shift), F(scale)))
    denominator = 1
    for value in range(1, order + 1):
        denominator *= value
    return poly_scale(out, F(1, denominator))


def paired_polynomial(newton_coefficients, order_scale: int):
    out = ()
    for order, coefficient in enumerate(newton_coefficients):
        if not coefficient:
            continue
        difference = poly_add(
            binomial_polynomial(2, order),
            poly_scale(binomial_polynomial(1, order), -order_scale),
        )
        out = poly_add(out, poly_scale(difference, coefficient))
    return out


def polynomial_string(polynomial, variable="t"):
    pieces = []
    for power in range(len(polynomial) - 1, -1, -1):
        value = polynomial[power]
        if not value:
            continue
        sign = "+" if value > 0 else "-"
        magnitude = abs(value)
        if power == 0:
            body = str(magnitude)
        else:
            coefficient = "" if magnitude == 1 else f"{magnitude}*"
            body = coefficient + variable + ("" if power == 1 else f"^{power}")
        pieces.append((sign, body))
    if not pieces:
        return "0"
    first_sign, first_body = pieces[0]
    text = ("-" if first_sign == "-" else "") + first_body
    for sign, body in pieces[1:]:
        text += f" {sign} {body}"
    return text


def exact_results():
    fifth_values = [state_and_output_weights(n) for n in range(6)]
    fifth_newton = [
        finite_differences([row[index] for row in fifth_values])
        for index in range(6)
    ]
    fifth_paired = [paired_polynomial(theta, 32) for theta in fifth_newton]

    cubic_values = [cubic_output_weights(n) for n in range(4)]
    cubic_newton = [
        finite_differences([row[index] for row in cubic_values])
        for index in range(2)
    ]
    cubic_paired = [paired_polynomial(theta, 8) for theta in cubic_newton]

    # Integrated single-node quadratic transition symbols.
    fifth_symbol = poly_add(
        poly_add(poly_scale(fifth_paired[0], 5), poly_scale(fifth_paired[1], -1)),
        fifth_paired[2],
    )
    cubic_symbol = poly_add(cubic_paired[1], poly_scale(cubic_paired[0], -3))
    return fifth_values, fifth_newton, fifth_paired, cubic_values, cubic_newton, cubic_paired, fifth_symbol, cubic_symbol


def main():
    results = exact_results()
    fifth_values, fifth_newton, fifth_paired, cubic_values, cubic_newton, cubic_paired, fifth_symbol, cubic_symbol = results
    assert fifth_values[1][0] == F(1, 120)
    assert tuple(sum(poly, F(0)) for poly in fifth_paired) == (
        F(1, 24), F(5, 3), F(1), F(1, 2), F(1), F(0)
    )
    assert tuple(sum(poly, F(0)) for poly in cubic_paired) == (F(1, 2), F(2))
    assert fifth_symbol == (F(0), F(-1, 8), F(0), F(0), F(-1, 3))
    assert cubic_symbol == (F(0), F(-1, 2), F(1))
    assert tuple(row[5] for row in fifth_newton) == (
        F(2), F(22), F(14), F(30), F(36), F(16)
    )
    assert tuple(row[3] for row in cubic_newton) == (F(2), F(4))

    print("fifth q_N, N=0,...,5")
    for n, row in enumerate(fifth_values):
        print(n, row)
    print("fifth Newton coefficients by elementary differential")
    for index, row in enumerate(fifth_newton, 1):
        print("E", index, row)
    print("paired fifth weights")
    for index, polynomial in enumerate(fifth_paired, 1):
        print("E", index, polynomial_string(polynomial))
    print("single-node fifth symbol", polynomial_string(fifth_symbol))

    print("cubic q_N, N=0,...,3", cubic_values)
    print("cubic Newton", cubic_newton)
    print("paired cubic weights")
    print("T", polynomial_string(cubic_paired[0]))
    print("H", polynomial_string(cubic_paired[1]))
    print("single-node cubic symbol", polynomial_string(cubic_symbol))


if __name__ == "__main__":
    main()
