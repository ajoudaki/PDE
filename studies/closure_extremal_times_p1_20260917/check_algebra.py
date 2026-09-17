"""Exact finite arithmetic checks; no training or research experiment."""
from fractions import Fraction
from math import comb, factorial


def main():
    for order in range(1, 17):
        offsets = [Fraction(2 * j - order, 2) for j in range(order + 1)]
        probabilities = [Fraction(comb(order, j), 2**order)
                         for j in range(order + 1)]
        signed = [(-1)**j * p for j, p in enumerate(probabilities)]
        assert sum(probabilities) == 1
        assert sum(probabilities[::2]) == Fraction(1, 2)
        assert sum(probabilities[1::2]) == Fraction(1, 2)
        for degree in range(order):
            assert sum(a * x**degree for a, x in zip(signed, offsets)) == 0
        leading = sum(a * x**order for a, x in zip(signed, offsets))
        assert leading == Fraction((-1)**order * factorial(order), 2**order)
        normalized = leading / factorial(order)
        assert 4 * normalized**2 == Fraction(4, 4**order)

    # Differentiate the normalized-readout expressions algebraically at exact
    # rational points. K is independent; q_s=2F and F_s=K are the inputs.
    for f in [Fraction(1, 5), Fraction(1, 2), Fraction(3, 2)]:
        for q in [Fraction(1, 7), Fraction(2, 3), Fraction(5)]:
            for k in [Fraction(1, 11), Fraction(2), Fraction(7)]:
                for c0 in [Fraction(1, 13), Fraction(1, 3)]:
                    direct = 2*f / f**2 - 2*q*k / f**3
                    assert direct == -2*(q*k-f*f) / f**3
                    direct_w = c0*(2*f*(c0+f*f)-2*f*k*(1+q))/(c0+f*f)**2
                    claimed_w = -2*c0*f*((q*k-f*f)+(k-c0))/(c0+f*f)**2
                    assert direct_w == claimed_w
    print("PASS: balanced binomial moments and slope factors, orders 1--16;")
    print("PASS: both normalized-readout derivative identities at 54 rational points.")
    print("Finite arithmetic only; long-time and population arguments require the proofs.")


if __name__ == "__main__":
    main()
