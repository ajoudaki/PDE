"""Small exact checks for the order-rate proofs; never form huge thresholds."""

from fractions import Fraction as F
from math import factorial


# Tame-gate Bernstein margin and the actual integer exponents in inversion.
assert F(36, 1024) < F(1, 16)
assert 100 * 49 * 4 * 1616 < 2**25
assert 4 * 84 == 336
assert 25 + 336 + 40 + 26 * 400000 == 10400401
assert 10400401 + 3 + 28 * 62004 == 12136516
assert 28 * 433447 == 12136516

# Exact rational interval exponents check the abstract squaring bounds.
# These are majorants of logarithms, not fabricated evaluations of N_k.
for w in (8, 9, 16, 32):
    upper_e = F(w)
    lower_e = F(1)
    for _ in range(w):
        lower_e *= 2
        upper_e = 2 * upper_e + 2 * w + 6
    assert 2**w == lower_e
    assert upper_e <= 4 * w * 2**w
    upper_log_a = w + 2 * upper_e
    assert upper_log_a <= 9 * w * 2**w
    upper_m = 2 * upper_log_a + 6
    lower_m = 4 * lower_e
    for _ in range(4 * w):
        lower_m *= 2
        upper_m = 2 * upper_m + 8
    assert lower_m == 4 * 2 ** (5 * w)
    assert upper_m <= 20 * w * 2 ** (5 * w)
    assert 20 * w <= 2 ** (3 * w)

# Auxiliary generation constants and the Picard-integral recurrence.
s = F(5)
b = 2 + s * s / 2
ell = 2 * b + 1 + 2 * s * (b * b + b + 1)
mass = 1 + 3 * s / 2 + s**3 / 8
assert ell == F(4575, 2)
assert s * ell == F(22875, 2)
assert mass == F(193, 8)
assert 9 + 10 * s * b + s == 739
for r in range(1, 15):
    coefficient = mass * ell ** (r - 1) / factorial(r)
    next_coefficient = mass * ell**r / factorial(r + 1)
    assert next_coefficient == ell * coefficient / (r + 1)

print('PASS: Bernstein margin, order exponents, squaring majorants, Picard constants')
