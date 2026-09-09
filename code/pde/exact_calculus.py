"""Small exact combinatorial and formal-series primitives.

Rational operations accept only Python int/Fraction (never float or bool).
The fixed quadratic certificate is an initialization-jet obstruction for a
specified frozen-first-block feature metric, not a training-limit theorem.
All functions are deterministic, draw no samples, and write no files.
"""

from fractions import Fraction
from math import factorial


def _integer(value, name, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return value


def _rationals(values):
    if not isinstance(values, (list, tuple)):
        raise ValueError("coefficients must be a list or tuple")
    if any(type(v) is not int and type(v) is not Fraction for v in values):
        raise ValueError("coefficients must be integers or Fractions")
    return [Fraction(v) for v in values]


def _multiply(a, b, length):
    result = [Fraction(0) for _ in range(length)]
    for i, x in enumerate(a[:length]):
        for j, y in enumerate(b[:length-i]):
            result[i+j] += x*y
    return result


def _compose(a, b, length):
    result = [Fraction(0) for _ in range(length)]
    for value in reversed(a[:length]):
        result = _multiply(result, b, length)
        if length:
            result[0] += value
    return result


def revert_series(coefficients):
    """Return b with a(b(y))=y modulo y**len(a), using ordinary coefficients.

    Requires at least the constant and nonzero linear term, with a[0]=0.
    No convergence or infinite-radius assertion is made. O(N**4) rational
    operations is a conservative bound; coefficient bit sizes are unbounded.
    """
    a = _rationals(coefficients)
    if len(a) < 2 or a[0] != 0 or a[1] == 0:
        raise ValueError("reversion needs zero constant and nonzero linear term")
    b = [Fraction(0) for _ in a]
    b[1] = 1/a[1]
    for k in range(2, len(a)):
        # b[k] is still zero; its only omitted contribution is a[1]*b[k].
        b[k] = -_compose(a, b, k+1)[k]/a[1]
    return b


def determinant(matrix):
    """Exact rational determinant; det([])=1, with no input mutation."""
    if not isinstance(matrix, (list, tuple)):
        raise ValueError("matrix must be a list or tuple of rows")
    work = [_rationals(row) for row in matrix]
    size = len(work)
    if any(len(row) != size for row in work):
        raise ValueError("matrix must be square")
    result = Fraction(1)
    for k in range(size):
        pivot = next((i for i in range(k, size) if work[i][k]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            work[k], work[pivot] = work[pivot], work[k]
            result = -result
        value = work[k][k]
        result *= value
        for i in range(k+1, size):
            ratio = work[i][k]/value
            for j in range(k+1, size):
                work[i][j] -= ratio*work[k][j]
            work[i][k] = Fraction(0)
    return result


def forest_key(colors, edges):
    """Canonical immutable key of a finite decorated bipartite simple forest.

    colors[v]=(layer, decoration), layer in {1,2}, decoration a nonnegative
    integer. Edges are pairs of distinct vertex indices in different layers;
    duplicates and cycles are rejected. Vertex and edge ordering is ignored,
    but colors and multiplicities of components are retained. Empty and
    isolated-vertex forests are allowed. No global cache is retained.
    This transparent all-roots implementation is for small forests, not a
    packed high-order coefficient generator. Recursion depth can reach the
    component size and Python's recursion limit still applies.
    """
    if not isinstance(colors, (list, tuple)) or not isinstance(edges, (list, tuple)):
        raise ValueError("colors and edges must be lists or tuples")
    labels = []
    for color in colors:
        if not isinstance(color, (list, tuple)) or len(color) != 2:
            raise ValueError("each color is (layer, decoration)")
        layer = _integer(color[0], "layer", 1)
        if layer not in (1, 2):
            raise ValueError("layer must be 1 or 2")
        labels.append((layer, _integer(color[1], "decoration")))
    size = len(labels)
    neighbors = [[] for _ in labels]
    parents = list(range(size))

    def find(v):
        while parents[v] != v:
            parents[v] = parents[parents[v]]
            v = parents[v]
        return v

    for edge in edges:
        if not isinstance(edge, (list, tuple)) or len(edge) != 2:
            raise ValueError("each edge is a pair")
        u, v = (_integer(value, "vertex") for value in edge)
        if u >= size or v >= size or u == v or labels[u][0] == labels[v][0]:
            raise ValueError("edge needs distinct in-range vertices of different layers")
        ru, rv = find(u), find(v)
        if ru == rv:
            raise ValueError("edges must form a simple forest")
        parents[ru] = rv
        neighbors[u].append(v)
        neighbors[v].append(u)
    groups = {}
    for v in range(size):
        groups.setdefault(find(v), []).append(v)

    def rooted(v, parent):
        return labels[v], tuple(sorted(rooted(w, v) for w in neighbors[v] if w != parent))

    return tuple(sorted(min(rooted(v, -1) for v in vertices)
                        for vertices in groups.values()))


def quadratic_axis_certificate():
    """Regenerate the fixed order-13/six-moment rational certificate.

    Uses X=z² partial_a+6az partial_z on a*z², with independent
    a~N(0,1), z~N(0,3). Direct coefficient reversion is used, not a
    specialized inversion formula or a retained coefficient artifact.
    The returned dict is freshly owned, contains Fractions, and writes nothing.
    """
    def moment(power, variance):
        if power % 2:
            return 0
        value = variance**(power//2)
        for k in range(1, power, 2):
            value *= k
        return value

    poly = {(1, 2): Fraction(1)}
    derivatives = []
    for order in range(14):
        derivatives.append(sum((c*moment(p, 1)*moment(q, 3)
                                for (p, q), c in poly.items()), Fraction(0)))
        if order == 13:
            break
        new = {}
        for (p, q), c in poly.items():
            if p:
                key = (p-1, q+2)
                new[key] = new.get(key, Fraction(0)) + p*c
            if q:
                key = (p+1, q)
                new[key] = new.get(key, Fraction(0)) + 6*q*c
        poly = new
    coefficients = [value/factorial(k) for k, value in enumerate(derivatives)]
    inverse = revert_series(coefficients)
    # K(y)=F'(F^{-1}(y)); length 13 supplies degrees 0,...,12.
    kernel = _compose([(k+1)*coefficients[k+1] for k in range(13)], inverse, 13)
    moments = [(-1)**j*kernel[2*j+2] for j in range(6)]
    hankel = [[moments[i+j+1] for j in range(3)] for i in range(3)]
    lead = moments[1]*moments[3]-moments[2]**2
    if lead <= 0:
        raise ArithmeticError("certificate leading block is not positive")
    witness = [(moments[2]*moments[4]-moments[3]**2)/lead,
               (moments[2]*moments[3]-moments[1]*moments[4])/lead,
               Fraction(1)]
    value = sum((witness[i]*hankel[i][j]*witness[j]
                 for i in range(3) for j in range(3)), Fraction(0))
    return {"derivatives": derivatives, "inverse": inverse,
            "kernel": kernel, "moments": moments, "witness": witness,
            "shifted_determinant": determinant(hankel), "witness_value": value}
