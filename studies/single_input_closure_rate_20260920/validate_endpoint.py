"""Exact arithmetic checks of ENDPOINT_ROUTE; no training or quadrature."""

from fractions import Fraction as F


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def outer(x, y):
    return tuple(a * b for a in x for b in y)


# T(1/5)^2 = 255 + 100 sqrt(5), with sqrt(5) < 9/4.
assert F(9, 4) ** 2 > 5
assert 255 + 100 * F(9, 4) < 22**2
# T(9/50)^2 = (241550 + 150000 sqrt(2))/729.
assert F(17, 12) ** 2 > 2
assert (241550 + 150000 * F(17, 12)) / 729 < 25**2


def exp_lower(x):
    """Positive series partial sum, strictly below exp(x) for x>0."""
    term = total = F(1)
    for k in range(1, 81):
        term *= x / k
        total += term
    return total


assert 22 / exp_lower(F(16)) + 25 / exp_lower(F(72, 5)) < F(17, 10**6)

# Non-idempotent positive contractions: retaining Q instead of Q^2 matters.
q2, q1 = (F(1, 2), F(1, 3)), (F(1, 4), F(2, 5))
delta, hidden = (F(1), F(2)), (F(3), F(1))
delta_u, hidden_u = (F(-1), F(1)), (F(2), F(-1))
j, ju = outer(delta, hidden), outer(delta_u, hidden_u)
filtered_j = tuple(a * z for a, z in zip(outer(q2, q1), j))
defect = tuple(a - b for a, b in zip(filtered_j, j))

# Add unchanged contributions from the other gradient blocks.
k, cross = 3 + dot(j, j), 4 + dot(ju, j)
k_filtered = 3 + dot(j, filtered_j)
cross_filtered = 4 + dot(ju, filtered_j)
ratio = cross / k
assert k_filtered > 0
lhs = cross_filtered / k_filtered - ratio
transverse = tuple(a - ratio * b for a, b in zip(ju, j))
assert lhs == dot(transverse, defect) / k_filtered
assert lhs == ((cross_filtered - cross) - ratio * (k_filtered - k)) / k_filtered
assert dot(j, filtered_j) != dot(filtered_j, filtered_j)

# Any positive common rescaling of the train/query kernel column cancels.
speed = F(7, 3)
assert speed * cross / (speed * k) == ratio
print("PASS: rational tail constants, nonprojector metric, defect identity, speed cancellation")
