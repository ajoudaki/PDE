"""Small exact combinatorial and formal-series primitives.

Rational operations accept only Python int/Fraction (never float or bool).
The fixed quadratic certificate is an initialization-jet obstruction for a
specified frozen-first-block feature metric, not a training-limit theorem.
All functions are deterministic, draw no samples, and write no files.
"""

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import comb, factorial


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


def euler_pullback_words(order, steps):
    """Return the exact order-h**order operator words for ``steps`` Euler steps.

    A tuple (k1,...,kq) denotes T_k1 ... T_kq acting right to left, where
    T_k u = D**k u[v,...,v]/k! freezes v inside this derivative. Each word
    has weight binom(steps,q). The empty word has weight one at order zero;
    positive orders with zero steps return an empty dict. Zero weights are
    omitted. Inputs must be Python nonnegative ints, excluding bool.

    This compiles finite noncommuting word coefficients, not derivatives,
    trajectories, or Gaussian expectations. The result is freshly owned and
    uses Fractions. At order m>=1 there are at most 2**(m-1) words; tuple
    construction takes O(m*2**m) operations/storage in the unrestricted case.
    Integer bit sizes and the user's requested order are not bounded here.
    """
    order = _integer(order, "order")
    steps = _integer(steps, "steps")
    if order == 0:
        return {(): Fraction(1)}
    if steps == 0:
        return {}
    result = {}
    stack = [(order, ())]
    while stack:
        remaining, prefix = stack.pop()
        if remaining == 0:
            result[prefix] = Fraction(comb(steps, len(prefix)))
        elif len(prefix) < steps:
            for k in range(remaining, 0, -1):
                stack.append((remaining-k, prefix+(k,)))
    return result


def paired_euler_weights(order):
    """Return rational coefficient rows for fine-minus-coarse Euler doubling.

    Row q-1 contains ordinary coefficients in N, in increasing degree, of
    binom(2*N,q) - 2**order * binom(N,q), for q=1,...,order. Every row has
    length order; the potential degree-order term cancels. At order zero
    the result is (). Thus order one returns ((Fraction(0),),).

    The weights multiply sums of all T-words with total order ``order``
    and length q. They do not evaluate those operators or their observable.
    The input is a nonnegative Python int, excluding bool. The immutable
    result uses exact Fractions, with O(order**2) rational operations and
    storage; rational bit sizes can grow. No cache or files are retained.
    """
    order = _integer(order, "order")
    binomial = [Fraction(1)]
    rows = []
    for q in range(1, order+1):
        # binom(N,q) = binom(N,q-1) * (N-q+1)/q.
        binomial = _multiply(binomial, [Fraction(1-q, q), Fraction(1, q)], q+1)
        rows.append(tuple((2**k-2**order)*binomial[k] if k <= q else Fraction(0)
                          for k in range(order)))
    return tuple(rows)


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


# General finite forest inputs keep the two Gaussian populations distinct.


@dataclass(frozen=True)
class GaussianForest:
    """Owned canonical simple bipartite forest for normalized Gaussian sums.

    ``colors[v]=(population, power)``, with populations 1 (a) and 2 (u).
    Each edge contributes one independent standard g entry. Normalization is
    n**(-edges/2-components), including isolates. Numerical labels in the
    defining sum are unrestricted. Construction validates and canonicalizes
    the graph, so equality and hashing ignore vertex/edge order. This is a
    small finite graph representation; recursive depth and combinatorial
    costs are not capped by this API.
    """
    colors: tuple
    edges: tuple

    def __post_init__(self):
        key = forest_key(self.colors, self.edges)
        colors, edges = [], []

        def visit(node, parent=None):
            vertex = len(colors)
            color, children = node
            colors.append(color)
            if parent is not None:
                edges.append((parent, vertex))
            for child in children:
                visit(child, vertex)

        for component in key:
            visit(component)
        object.__setattr__(self, "colors", tuple(colors))
        object.__setattr__(self, "edges", tuple(sorted(edges)))

    @property
    def components(self):
        return len(self.colors) - len(self.edges)


def _forest(value):
    if not isinstance(value, GaussianForest):
        raise ValueError("forest must be a GaussianForest")
    return value


def _partitions(items):
    """Every equality partition once, including the partition of no vertices."""
    if not items:
        yield ()
        return
    last = items[-1]
    for old in _partitions(items[:-1]):
        for index in range(len(old)):
            yield old[:index] + (old[index] + (last,),) + old[index+1:]
        yield old + ((last,),)


def _gaussian_moment(power):
    if power % 2:
        return 0
    value = 1
    for index in range(1, power, 2):
        value *= index
    return value


def forest_expectation(forest, *, width=None):
    """Exact rational Gaussian expectation at finite width, or its leading limit.

    ``width=None`` uses paired quotient trees; a positive Python integer
    width uses all equality partitions with falling-factorial multiplicity.
    No rank/mod-two pruning is used. Odd edge count has expectation zero.
    Counts reject booleans. Enumeration has Bell-number cost at caller-chosen
    finite size; no efficient high-order or trajectory claim is made.
    """
    forest = _forest(forest)
    if width is not None:
        width = _integer(width, "width", 1)
    edge_count = len(forest.edges)
    if edge_count % 2:
        return Fraction(0)
    rows = tuple(i for i, color in enumerate(forest.colors) if color[0] == 1)
    cols = tuple(i for i, color in enumerate(forest.colors) if color[0] == 2)
    exponent = edge_count // 2 + forest.components
    total = Fraction(0)
    for rp in _partitions(rows):
        ri = {v: i for i, block in enumerate(rp) for v in block}
        for cp in _partitions(cols):
            ci = {v: i for i, block in enumerate(cp) for v in block}
            cells = {}
            for u, v in forest.edges:
                if forest.colors[u][0] == 2:
                    u, v = v, u
                key = (ri[u], ci[v])
                cells[key] = cells.get(key, 0) + 1
            if width is None and (len(rp) + len(cp) != exponent
                                  or any(count != 2 for count in cells.values())):
                continue
            value = 1
            for block in rp + cp:
                value *= _gaussian_moment(sum(forest.colors[v][1] for v in block))
            for count in cells.values():
                value *= _gaussian_moment(count)
            if width is not None:
                for count in (len(rp), len(cp)):
                    for index in range(count):
                        value *= width - index
                total += Fraction(value, width**exponent)
            else:
                total += value
    return total


def _forest_product(left, right):
    offset = len(left.colors)
    return GaussianForest(left.colors + right.colors,
                          left.edges + tuple((i+offset, j+offset) for i, j in right.edges))


def _add_term(poly, forest, coefficient):
    if coefficient:
        value = poly.get(forest, Fraction(0)) + coefficient
        if value:
            poly[forest] = value
        else:
            poly.pop(forest, None)


def _forest_polynomial_product(left, right):
    result = {}
    for a, x in left.items():
        for b, y in right.items():
            _add_term(result, _forest_product(a, b), x*y)
    return result


def _quadratic_root(forest):
    forest = _forest(forest)
    if any(population == 2 and power % 2 for population, power in forest.colors):
        raise ValueError("quadratic forest roots require even column powers")
    return forest


def quadratic_forest_derivatives(forest, order, *, alpha=1, beta=1):
    """Exact finite forest polynomials for D**k S, k=0,...,order.

    Raw square, one input, two hidden layers, order-one Gaussian readout;
    FEATURE ASCENT metric in stored coordinates is (n*alpha,beta,n).
    alpha,beta are nonnegative Python int/Fraction. Dictionary coefficients
    are Fractions and keys are immutable GaussianForest objects. Different
    block hits are ordered by the derivation; they are never commuted.
    Evaluating each polynomial by forest_expectation gives its annealed
    finite-width or deterministic limiting coefficient. No time solver or
    high-order campaign is run. Each returned dictionary is independently owned.
    """
    forest = _quadratic_root(forest)
    order = _integer(order, "order")
    alpha, beta = _rationals([alpha, beta])
    if min(alpha, beta) < 0:
        raise ValueError("alpha and beta must be nonnegative")
    levels = [{forest: Fraction(1)}]
    for _ in range(order):
        new = {}
        for parent, coefficient in levels[-1].items():
            size = len(parent.colors)
            for vertex, (population, power) in enumerate(parent.colors):
                if not power:
                    continue
                colors, edges = list(parent.colors), list(parent.edges)
                if population == 1:
                    colors[vertex] = (1, power-1)
                    colors.extend(((2, 2), (2, 2)))
                    edges.extend(((vertex, size), (vertex, size+1)))
                    weight = power
                else:
                    colors.extend(((1, 1), (2, 2)))
                    edges.extend(((vertex, size), (size, size+1)))
                    weight = 4*alpha*power
                _add_term(new, GaussianForest(colors, edges), coefficient*weight)
            for index, (u, v) in enumerate(parent.edges):
                if parent.colors[u][0] == 2:
                    u, v = v, u
                colors = list(parent.colors)
                colors[u] = (1, colors[u][1]+1)
                colors[v] = (2, colors[v][1]+2)
                colors.append((2, 2))
                edges = list(parent.edges[:index] + parent.edges[index+1:])
                edges.append((u, size))
                _add_term(new, GaussianForest(colors, edges), coefficient*2*beta)
        levels.append(new)
    return tuple(levels)


def quadratic_euler_pullback(forest, step, *, loss=False, label=1):
    """One exact simultaneous raw-square pullback as a forest polynomial.

    Unit block metric, one input, two hidden layers. In feature mode step is
    a signed feature step. With loss=True it is a signed raw step for the
    FULL squared loss (f-label)**2: s=2*step*(label-f) is expanded exactly,
    including residual feedback. The activation here is precisely z**2.
    Every scalar is Python int/Fraction; loss must be bool. General normalized
    square models need their own stated c**3 scaling. New factors are never
    updated within this same step. Computation is finite and combinatorial.
    """
    forest = _quadratic_root(forest)
    step, label = _rationals([step, label])
    if type(loss) is not bool:
        raise ValueError("loss must be a boolean")
    if not loss and label != 1:
        raise ValueError("label is only used in loss mode")
    choices = [range(power+1) for _, power in forest.colors]
    choices += [range(2) for _ in forest.edges]
    by_degree = {}
    for selected in product(*choices):
        colors = list(forest.colors)
        edges = []
        degree = sum(selected)
        coefficient = Fraction(1)
        for vertex, ((population, power), count) in enumerate(zip(forest.colors, selected)):
            coefficient *= comb(power, count)
            if population == 1:
                colors[vertex] = (1, power-count)
                for _ in range(count):
                    index = len(colors)
                    colors.extend(((2, 2), (2, 2)))
                    edges.extend(((vertex, index), (vertex, index+1)))
            else:
                coefficient *= 4**count
                for _ in range(count):
                    index = len(colors)
                    colors.extend(((1, 1), (2, 2)))
                    edges.extend(((vertex, index), (index, index+1)))
        for (u, v), count in zip(forest.edges, selected[len(forest.colors):]):
            if not count:
                edges.append((u, v))
                continue
            coefficient *= 2
            if forest.colors[u][0] == 2:
                u, v = v, u
            colors[u] = (1, colors[u][1]+1)
            colors[v] = (2, colors[v][1]+2)
            index = len(colors)
            colors.append((2, 2))
            edges.append((u, index))
        bucket = by_degree.setdefault(degree, {})
        _add_term(bucket, GaussianForest(colors, edges), coefficient)
    result = {}
    if not loss:
        for degree, poly in by_degree.items():
            for term, coefficient in poly.items():
                _add_term(result, term, coefficient*step**degree)
        return result
    unit = GaussianForest((), ())
    output = GaussianForest(((1, 1), (2, 2), (2, 2)), ((0, 1), (0, 2)))
    residual_step = {}
    _add_term(residual_step, unit, 2*step*label)
    _add_term(residual_step, output, -2*step)
    power = {unit: Fraction(1)}
    for degree in range(max(by_degree, default=0)+1):
        for term, coefficient in _forest_polynomial_product(by_degree.get(degree, {}), power).items():
            _add_term(result, term, coefficient)
        power = _forest_polynomial_product(power, residual_step)
    return result


def gradient_tree_terms(order):
    """Return canonical unrooted contraction trees and exact attachment weights.

    Maps a parenthesis code to (integer weight, immutable edge tuple). Each
    tree has order+1 vertices indexed from zero. It means the contraction of
    derivative tensors of a scalar f, one per vertex, against a CONSTANT
    symmetric metric on the edges. A singleton means f. This compiles D**order
    f, not just tree shape counts; metric derivatives are not included.
    """
    order = _integer(order, "order")

    def key(edges):
        neighbors = [[] for _ in range(len(edges)+1)]
        for i, j in edges:
            neighbors[i].append(j)
            neighbors[j].append(i)

        def rooted(i, parent):
            return '(' + ''.join(sorted(rooted(j, i) for j in neighbors[i] if j != parent)) + ')'
        return min(rooted(i, -1) for i in range(len(neighbors)))

    trees = {'()': (1, ())}
    for degree in range(1, order+1):
        new = {}
        for weight, edges in trees.values():
            for vertex in range(degree):
                child = edges + ((vertex, degree),)
                code = key(child)
                old, representative = new.get(code, (0, child))
                new[code] = (old+weight, representative)
        trees = new
    return trees


def next_hankel_threshold(matrix, column):
    """Exact b^T A^+ b for a supplied rational symmetric PSD leading block A.

    Accepts singular A only when b belongs to its range. The next symmetric
    block [[A,b],[b^T,c]] is PSD exactly when c >= the returned Fraction.
    No provenance or infinite moment representation is inferred. Rejects
    indefinite/nonsymmetric blocks and out-of-range columns. Empty A,b give 0.
    """
    if not isinstance(matrix, (list, tuple)):
        raise ValueError("matrix must be a list or tuple")
    original = [_rationals(row) for row in matrix]
    rhs = _rationals(column)
    size = len(original)
    if any(len(row) != size for row in original) or len(rhs) != size:
        raise ValueError("A must be square and b have matching length")
    if any(original[i][j] != original[j][i] for i in range(size) for j in range(size)):
        raise ValueError("A must be symmetric")
    schur = [row[:] for row in original]
    for k in range(size):
        pivot = schur[k][k]
        if pivot < 0 or (pivot == 0 and any(schur[k][j] for j in range(k+1, size))):
            raise ValueError("A must be positive semidefinite")
        if pivot:
            for i in range(k+1, size):
                for j in range(k+1, size):
                    schur[i][j] -= schur[i][k]*schur[k][j]/pivot
    work = [row[:] + [value] for row, value in zip(original, rhs)]
    pivots = []
    row = 0
    for col in range(size):
        pivot = next((j for j in range(row, size) if work[j][col]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        value = work[row][col]
        work[row] = [x/value for x in work[row]]
        for j in range(size):
            if j != row:
                ratio = work[j][col]
                work[j] = [x-ratio*y for x, y in zip(work[j], work[row])]
        pivots.append(col)
        row += 1
    if any(not any(line[:-1]) and line[-1] for line in work):
        raise ValueError("b must belong to the range of A")
    solution = [Fraction(0)]*size
    for row, col in enumerate(pivots):
        solution[col] = work[row][-1]
    return sum((x*y for x, y in zip(rhs, solution)), Fraction(0))


def bernstein_coefficients(coefficients, left, right, *, degree=None):
    """Exact Bernstein coefficients on [left,right] of a rational polynomial.

    Input coefficients are ordinary increasing powers of the original x.
    degree defaults to len(coefficients)-1 and may be elevated. Every scalar
    is Python int/Fraction and left < right. Signs of the output certify this
    supplied polynomial only, without a neural coefficient-provenance claim.
    """
    values = _rationals(coefficients)
    left, right = _rationals([left, right])
    if not values or left >= right:
        raise ValueError("need nonempty coefficients and left < right")
    if degree is None:
        degree = len(values)-1
    degree = _integer(degree, "degree", len(values)-1)
    shifted = [sum((values[j]*comb(j, k)*left**(j-k)*(right-left)**k
                    for j in range(k, len(values))), Fraction(0))
               for k in range(degree+1)]
    return tuple(sum((shifted[k]*Fraction(comb(j, k), comb(degree, k))
                      for k in range(j+1)), Fraction(0)) for j in range(degree+1))


def identity_shallow_step(f, q, d, label, mobility, step):
    """Exact rational scalar raw-GD update for one-input shallow identity.

    f=a^T u/n, q=(|a|²+|u|²)/n, d=(|a|²-|u|²)/n; full squared
    loss and equal mobilities n*mobility. Inputs must be Python int/Fraction,
    mobility positive, step nonnegative, and q² >= d²+4f², q >= 0.
    Returns a new (f,q,d) tuple. No initialization or population limit is used.
    """
    f, q, d, label, mobility, step = _rationals([f, q, d, label, mobility, step])
    if q < 0 or q*q < d*d+4*f*f or mobility <= 0 or step < 0:
        raise ValueError("infeasible scalar state, mobility, or step")
    b = -2*mobility*step*(f-label)
    return ((1+b*b)*f+b*q, (1+b*b)*q+4*b*f, (1-b*b)*d)


def gaussian_hidden_head(covariance, responses, activation):
    """Exact supplied-Gaussian polynomial hidden head through derivative four.

    Coordinates are (Z,U1,U2,U3,U4,V0,V1,V2,V3). Supply the complete 9-by-9
    rational PSD covariance, with Var(Z)=1 and zero cross covariance between
    the first five and last four coordinates; singular blocks are allowed.
    ``activation`` contains nonempty ordinary polynomial coefficients.
    ``responses`` is a dict with precisely the ten keys lambda1, lambda2,
    lambda30, lambda32, lambda41, lambda43, c10, d21, d30, d32. Every scalar
    must be a Python int/Fraction, excluding bool and floats.

    The local Bell/product graph is E9 in the Gaussian calculus chapter;
    the additional response rules are supplied inputs, not inferred neural
    covariances. Partials hold all other coordinates and response constants
    fixed BEFORE expectation. Return fresh exact Fraction values gamma,
    A41, A43, gram13, gram22, and squared_rms_fourth = 2*gamma+8*gram13+
    6*gram22. This last output is a fourth derivative, not an ordinary
    Taylor coefficient. Only activation derivatives zero through four are
    formed, by exact polynomial differentiation. No symbolic atoms or
    nonpolynomial integration mode is implemented.

    Sparse polynomial size and Wick states can grow rapidly with the input
    degree; this is a finite algebra evaluator with no efficiency promise
    for large inputs. It draws no samples, writes no files, retains no cache
    and does not mutate inputs. There is no population or trajectory claim.
    """
    from .gaussian_moments import gaussian_moment

    names = ('lambda1', 'lambda2', 'lambda30', 'lambda32', 'lambda41',
             'lambda43', 'c10', 'd21', 'd30', 'd32')
    if not isinstance(responses, dict) or set(responses) != set(names):
        raise ValueError("responses must supply exactly the ten declared keys")
    rates = dict(zip(names, _rationals([responses[key] for key in names])))
    coefficients = _rationals(activation)
    if not coefficients:
        raise ValueError("activation coefficients must be nonempty")
    if not isinstance(covariance, (list, tuple)) or len(covariance) != 9:
        raise ValueError("covariance must have nine rows")
    sigma = tuple(tuple(_rationals(row)) for row in covariance)
    if any(len(row) != 9 for row in sigma):
        raise ValueError("covariance must be 9-by-9")
    gaussian_moment(sigma, (0,)*9)  # Validate the entire matrix, including PSD.
    if sigma[0][0] != 1 or any(sigma[i][j] for i in range(5) for j in range(5, 9)):
        raise ValueError("need Var(Z)=1 and independent U/Z and V blocks")

    zero = (0,)*9

    def add(*terms):
        answer = {}
        for term in terms:
            for powers, value in term.items():
                answer[powers] = answer.get(powers, Fraction(0)) + value
        return {powers: value for powers, value in answer.items() if value}

    def scale(value, term):
        return {powers: value*coefficient for powers, coefficient in term.items()
                if value*coefficient}

    def mul(*terms):
        answer = {zero: Fraction(1)}
        for term in terms:
            new = {}
            for a, x in answer.items():
                for b, y in term.items():
                    powers = tuple(i+j for i, j in zip(a, b))
                    new[powers] = new.get(powers, Fraction(0)) + x*y
            answer = {powers: value for powers, value in new.items() if value}
        return answer

    def partial(term, coordinate):
        answer = {}
        for powers, value in term.items():
            if powers[coordinate]:
                reduced = list(powers)
                reduced[coordinate] -= 1
                answer[tuple(reduced)] = value*powers[coordinate]
        return answer

    coordinates = []
    for coordinate in range(9):
        powers = [0]*9
        powers[coordinate] = 1
        coordinates.append({tuple(powers): Fraction(1)})
    _, u1, u2, u3, u4, v0, v1, v2, v3 = coordinates
    p = [{(k,)+(0,)*8: value for k, value in enumerate(coefficients) if value}]
    for _ in range(4):
        p.append(partial(p[-1], 0))
    p0, p1, p2, p3, p4 = p
    d0 = mul(p1, v0)
    z1 = add(u1, scale(rates['lambda1'], d0))
    h1 = mul(p1, z1)
    r1 = add(v1, scale(rates['c10'], p0))
    d1 = add(mul(p2, z1, v0), mul(p1, r1))
    z2 = add(u2, scale(rates['lambda2'], d1))
    h2 = add(mul(p2, z1, z1), mul(p1, z2))
    r2 = add(v2, scale(rates['d21'], h1))
    d2 = add(mul(p3, z1, z1, v0), mul(p2, z2, v0),
             scale(2, mul(p2, z1, r1)), mul(p1, r2))
    z3 = add(u3, scale(rates['lambda30'], d0), scale(rates['lambda32'], d2))
    h3 = add(mul(p3, z1, z1, z1), scale(3, mul(p2, z1, z2)), mul(p1, z3))
    r3 = add(v3, scale(rates['d30'], p0), scale(rates['d32'], h2))
    d3 = add(mul(p4, z1, z1, z1, v0), scale(3, mul(p3, z1, z2, v0)),
             mul(p2, z3, v0), scale(3, mul(p3, z1, z1, r1)),
             scale(3, mul(p2, z2, r1)), scale(3, mul(p2, z1, r2)), mul(p1, r3))
    z4 = add(u4, scale(rates['lambda41'], d1), scale(rates['lambda43'], d3))
    h4 = add(mul(p4, z1, z1, z1, z1), scale(6, mul(p3, z1, z1, z2)),
             scale(3, mul(p2, z2, z2)), scale(4, mul(p2, z1, z3)), mul(p1, z4))
    cache = {zero: Fraction(1)}

    def moment(powers):
        if sum(powers) % 2:
            return Fraction(0)
        if powers not in cache:
            i = next(i for i, count in enumerate(powers) if count)
            remainder = list(powers)
            remainder[i] -= 1
            value = Fraction(0)
            for j, count in enumerate(remainder):
                if count and sigma[i][j]:
                    paired = remainder.copy()
                    paired[j] -= 1
                    value += count*sigma[i][j]*moment(tuple(paired))
            cache[powers] = value
        return cache[powers]

    def expectation(term):
        return sum((value*moment(powers) for powers, value in term.items()), Fraction(0))

    gamma = expectation(mul(p0, h4))
    gram13, gram22 = expectation(mul(h1, h3)), expectation(mul(h2, h2))
    return {'gamma': gamma, 'A41': expectation(partial(h4, 6)),
            'A43': expectation(partial(h4, 8)), 'gram13': gram13,
            'gram22': gram22, 'squared_rms_fourth': 2*gamma+8*gram13+6*gram22}
