"""Tanh polynomial-core initialization for the finite observable closure.

All runtime dependencies use canonical module names or injected callables.
There are no imports from studies, no neural-width parameter, and no trajectory
solver. Positive source regularization belongs only to the generic compiler.
"""
from dataclasses import dataclass
from fractions import Fraction
import math
from typing import Any

import numpy as np

from pde.observable_words import (
    action, add, constant, decode_word, multiply, scale, seed, unary,
)


class InitializationResourceLimit(ValueError):
    """A finite requested initializer exceeds a caller-adjustable budget."""


def _integer(value, name, minimum=1):
    if isinstance(value, bool) or not isinstance(value, (int, np.integer)):
        raise ValueError(f"{name} must be an integer")
    value = int(value)
    if value < minimum:
        raise ValueError(f"{name} must be at least {minimum}")
    return value


@dataclass(frozen=True)
class InitializationLimits:
    max_features_per_population: int = 4096
    max_dictionary_nodes: int = 65536
    max_codes: int = 100000
    max_points: int = 1000000
    max_working_bytes: int = 536870912
    max_work_units: int = 2000000000
    compiler_limits: Any = None

    def __post_init__(self):
        for name in ("max_features_per_population", "max_dictionary_nodes",
                     "max_codes", "max_points", "max_working_bytes", "max_work_units"):
            _integer(getattr(self, name), name)


@dataclass(frozen=True)
class Dictionary:
    order: int
    first_words: tuple
    second_words: tuple
    first_exponents: tuple
    second_exponents: tuple
    first_tail: tuple
    second_tail: tuple
    core_actions: tuple
    fast_core: bool
    node_count: int
    tail_codes: tuple


@dataclass
class InitializedFeatures:
    b1: np.ndarray
    g: np.ndarray
    p1: np.ndarray
    b2: np.ndarray
    p2: np.ndarray
    D: np.ndarray
    metadata: dict


def _exponents(total, dimension):
    if dimension == 1:
        yield (total,)
        return
    for first in range(total, -1, -1):
        for rest in _exponents(total - first, dimension - 1):
            yield (first,) + rest


def _all_exponents(order, dimension):
    return tuple(a for total in range(order + 1) for a in _exponents(total, dimension))


def _polynomial_words(coordinates, exponents, order):
    one = constant(coordinates[0].population)
    univariate = []
    for x in coordinates:
        terms = [one, x]
        for degree in range(1, order):
            terms.append(add(scale(2, multiply(x, terms[-1])), scale(-1, terms[-2])))
        univariate.append(terms)
    result = []
    for powers in exponents:
        factors = [univariate[j][a] for j, a in enumerate(powers) if a]
        word = one if not factors else factors[0]
        for factor in factors[1:]:
            word = multiply(word, factor)
        result.append(word)
    return result


def build_dictionary(order, *, limits=None):
    """Nested bounded outputs; dependencies are compiled, never auto-retained.

    Resource limits reject a request without changing its dictionary. They can
    be increased by the caller and do not define a mathematical maximum order.
    """
    order = _integer(order, "order")
    limits = limits or InitializationLimits()
    if order + 1 > limits.max_codes:
        raise InitializationResourceLimit("explicit exhaustive prefix exceeds max_codes")
    core_counts = (math.comb(order + 4, 4), math.comb(order + 2, 2))
    if max(core_counts) > limits.max_features_per_population:
        raise InitializationResourceLimit("polynomial feature count exceeds its declared limit")
    g = (seed("g1"), seed("g2"))
    h = tuple(unary("tanh", x) for x in g)
    xi = tuple(action(x) for x in h)
    upper = tuple(unary("tanh", x) for x in xi)
    reverse = tuple(action(x) for x in upper)
    lower_coordinates = h + tuple(unary("tanh", x) for x in reverse)
    exponents = (_all_exponents(order, 4), _all_exponents(order, 2))
    lists = [_polynomial_words(lower_coordinates, exponents[0], order),
             _polynomial_words(upper, exponents[1], order)]
    seen_outputs = [set(words) for words in lists]
    tails, retained_codes = [[], []], []
    for code in range(order + 1):
        word = decode_word(code)
        if word is None or not word.bounded:
            continue
        population = word.population - 1
        if word not in seen_outputs[population]:
            lists[population].append(word)
            tails[population].append(word)
            seen_outputs[population].add(word)
            retained_codes.append(code)
    if max(map(len, lists)) > limits.max_features_per_population:
        raise InitializationResourceLimit("retained feature count exceeds its declared limit")
    core_actions = xi + reverse
    known_actions = set(core_actions)
    nodes, stack, fast_core = set(), [*lists[0], *lists[1]], True
    while stack:
        word = stack.pop()
        if word in nodes:
            continue
        nodes.add(word)
        if len(nodes) > limits.max_dictionary_nodes:
            raise InitializationResourceLimit("dictionary DAG exceeds max_dictionary_nodes")
        if word.op == "action" and word not in known_actions:
            fast_core = False
        stack.extend(word.args)
    return Dictionary(order, tuple(lists[0]), tuple(lists[1]),
                      exponents[0], exponents[1], tuple(tails[0]), tuple(tails[1]),
                      core_actions, fast_core, len(nodes), tuple(retained_codes))


def _checked_cloud(rule, count, dimension, ar):
    cloud = ar.array(rule(count, dimension, ar))
    if cloud.shape != (count, dimension) or not ar.finite(cloud):
        raise ValueError("Gaussian rule returned the wrong finite cloud shape")
    return cloud


def _chebyshev_values(x, exponents, order, active_coordinates, ar):
    """Polynomial values and derivatives with respect to selected x entries."""
    count, dimension = x.shape
    one, two = ar.real(1), ar.real(2)
    terms, derivatives = [], []
    for coordinate in range(dimension):
        t = ar.zeros((count, order + 1))
        dt = ar.zeros(t.shape)
        t[:, 0], t[:, 1], dt[:, 1] = one, x[:, coordinate], one
        for degree in range(1, order):
            t[:, degree + 1] = two*x[:, coordinate]*t[:, degree]-t[:, degree-1]
            dt[:, degree + 1] = two*t[:, degree]+two*x[:, coordinate]*dt[:, degree]-dt[:, degree-1]
        terms.append(t)
        derivatives.append(dt)
    values = ar.zeros((count, len(exponents)))
    gradient = ar.zeros((count, len(exponents), len(active_coordinates)))
    for column, powers in enumerate(exponents):
        values[:, column] = one
        for coordinate, degree in enumerate(powers):
            values[:, column] *= terms[coordinate][:, degree]
        for derivative_column, differentiated in enumerate(active_coordinates):
            gradient[:, column, derivative_column] = derivatives[differentiated][:, powers[differentiated]]
            for coordinate, degree in enumerate(powers):
                if coordinate != differentiated:
                    gradient[:, column, derivative_column] *= terms[coordinate][:, degree]
    return values, gradient


def _tail_values(words, population, g, xi, reverse, core_actions, ar):
    """Evaluate the small no-new-source tail on the complete core tuple."""
    count = len(g) if population == 1 else len(xi)
    zero = ar.zeros((count, 2))
    one = ar.real(1)
    known = dict(zip(core_actions, (xi[:, 0], xi[:, 1], reverse[:, 0], reverse[:, 1])))
    known_indices = dict(zip(core_actions, (0, 1, 0, 1)))
    cache = {}

    def visit(word):
        if word in cache:
            return cache[word]
        if word.population != population:
            raise ValueError("fast tail cannot evaluate a foreign population operand")
        if word in known:
            derivative = zero.copy()
            derivative[:, known_indices[word]] = one
            value = known[word]
        elif word.op == "one":
            value, derivative = np.full(count, one, dtype=ar.dtype), zero.copy()
        elif word.op in ("g1", "g2"):
            value, derivative = g[:, int(word.op[1])-1], zero.copy()
        elif word.op in ("sin", "cos", "tanh"):
            v, dv = visit(word.args[0])
            if word.op == "tanh":
                value = ar.tanh(v)
                derivative = (one-value*value)[:, None]*dv
            elif word.op == "sin":
                value, derivative = ar.trig(v), ar.trig(v, cosine=True)[:, None]*dv
            else:
                value, derivative = ar.trig(v, cosine=True), -ar.trig(v)[:, None]*dv
        elif word.op == "scale":
            v, dv = visit(word.args[0])
            coefficient = ar.real(word.scalar)
            value, derivative = coefficient*v, coefficient*dv
        elif word.op in ("add", "multiply"):
            v, dv = visit(word.args[0])
            w, dw = visit(word.args[1])
            if word.op == "add":
                value, derivative = v+w, dv+dw
            else:
                value, derivative = v*w, dv*w[:, None]+dw*v[:, None]
        else:
            raise ValueError("fast core encountered an undeclared initialized action")
        cache[word] = value, derivative
        return cache[word]

    if not words:
        return ar.zeros((count, 0)), ar.zeros((count, 0, 2))
    evaluated = [visit(word) for word in words]
    return np.column_stack([pair[0] for pair in evaluated]), np.stack([pair[1] for pair in evaluated], axis=1)


def _core_tables(dictionary, cloud1, cloud2, v, alpha, tau_core, ar):
    one = ar.real(1)
    g = cloud1[:, :2]
    h = ar.tanh(g)
    reverse = ar.sqrt(tau_core)*cloud1[:, 2:4]+alpha*h
    bounded_reverse = ar.tanh(reverse)
    xi = ar.sqrt(v)*cloud2
    upper = ar.tanh(xi)
    x1 = np.concatenate((h, bounded_reverse), axis=1)
    raw1, derivative1 = _chebyshev_values(x1, dictionary.first_exponents,
                                        dictionary.order, (2, 3), ar)
    raw2, derivative2 = _chebyshev_values(upper, dictionary.second_exponents,
                                        dictionary.order, (0, 1), ar)
    derivative1 *= (one-bounded_reverse*bounded_reverse)[:, None, :]
    derivative2 *= (one-upper*upper)[:, None, :]
    tail1, tail_derivative1 = _tail_values(dictionary.first_tail, 1, g, xi, reverse,
                                         dictionary.core_actions, ar)
    tail2, tail_derivative2 = _tail_values(dictionary.second_tail, 2, g, xi, reverse,
                                         dictionary.core_actions, ar)
    return (np.concatenate((raw1, tail1), axis=1),
            np.concatenate((raw2, tail2), axis=1),
            np.concatenate((derivative1, tail_derivative1), axis=1),
            np.concatenate((derivative2, tail_derivative2), axis=1), g, h, upper)


def _mean(values, ar):
    return np.sum(values, axis=0)/ar.real(len(values))


def _resource_plan(dictionary, initialization_nodes, population_nodes, ar, limits):
    q = _integer(initialization_nodes, "initialization_nodes")
    p = _integer(population_nodes, "population_nodes")
    if max(q, p) > limits.max_points:
        raise InitializationResourceLimit("Gaussian point count exceeds max_points")
    d1, d2, degree = len(dictionary.first_words), len(dictionary.second_words), dictionary.order
    # Conservative simultaneous array and algebra bounds for the fast branch.
    # The generic compiler additionally checks its source/DAG work separately.
    scalars = q*(4*(d1+d2)+16*(degree+1)+100)+p*(4*(d1+d2)+16*(degree+1)+100)
    scalars += 8*(d1*d1+d2*d2+d1*d2)
    scalar_bytes = 8 if ar.digits is None else 192+ar.digits
    estimated_bytes = scalars*scalar_bytes
    work = q*(4*(d1*d1+d2*d2+d1*d2)+32*(degree+1)*(d1+d2))
    work += p*32*(degree+1)*(d1+d2)
    if estimated_bytes > limits.max_working_bytes:
        raise InitializationResourceLimit("initializer array estimate exceeds max_working_bytes")
    if work > limits.max_work_units:
        raise InitializationResourceLimit("initializer algebra estimate exceeds max_work_units")
    return q, p, dict(estimated_working_scalars=scalars,
                     estimated_working_bytes=estimated_bytes, estimated_work_units=work)


def _normalize(raw1, raw2, gram1, gram2, contraction, ar, eta):
    t1 = ar.inverse_lower(ar.cholesky(gram1+eta*ar.eye(len(gram1))))
    t2 = ar.inverse_lower(ar.cholesky(gram2+eta*ar.eye(len(gram2))))
    # Cholesky transforms are nonsymmetric: all three transposes are essential.
    return raw1 @ t1.T, raw2 @ t2.T, t2 @ contraction @ t1.T


def initialize_features(order, *, arithmetic, initialization_nodes, population_nodes,
                        epsilon_cov, limits=None, gaussian_points=None, raw_compiler=None):
    """Build finite joint mark tables and one action matrix.

    Q=initialization_nodes fixes Gaussian coefficient/Gram quadrature;
    P=population_nodes independently discretizes the resulting joint mark law.
    A tail using only the known core sources uses the exact contraction
    reduction (numerically integrated). Any new non-core action in the
    exhaustive tail dispatches to the complete
    source compiler. Returned metadata contains no source tape or dense arrays.
    """
    limits = limits or InitializationLimits()
    dictionary = build_dictionary(order, limits=limits)
    ar = arithmetic
    q, p, resource_metadata = _resource_plan(dictionary, initialization_nodes,
                                          population_nodes, ar, limits)
    if gaussian_points is None:
        from pde.observable_arithmetic import gaussian_points
    with ar.context():
        epsilon_cov = ar.real(epsilon_cov)
        if epsilon_cov <= 0:
            raise ValueError("epsilon_cov must be positive for the complete initializer")
        eta = ar.real(Fraction(1, 1024*(dictionary.order+1)**2))
        constants = {}
        if dictionary.fast_core:
            cloud1 = _checked_cloud(gaussian_points, q, 4, ar)
            cloud2 = _checked_cloud(gaussian_points, q, 2, ar)
            v = _mean(ar.tanh(cloud1[:, 0])**2, ar)
            if v <= 0:
                raise ValueError("core forward variance is unresolved by this Gaussian rule")
            scalar_upper = ar.tanh(ar.sqrt(v)*cloud2[:, 0])
            tau_core = _mean(scalar_upper*scalar_upper, ar)
            alpha = _mean(ar.real(1)-scalar_upper*scalar_upper, ar)
            if tau_core <= 0 or alpha <= 0:
                raise ValueError("core reverse variance or response is unresolved")
            raw1, raw2, derivative1, derivative2, _, h, upper = _core_tables(
                dictionary, cloud1, cloud2, v, alpha, tau_core, ar)
            gram1, gram2 = raw1.T @ raw1/ar.real(q), raw2.T @ raw2/ar.real(q)
            beta = raw1.T @ h/ar.real(q)
            gamma = _mean(derivative1, ar)
            upper_derivative = _mean(derivative2, ar)
            upper_pairing = raw2.T @ upper/ar.real(q)
            contraction = upper_derivative @ beta.T+upper_pairing @ gamma.T
            # Release coefficient-rule tables before independent population replay.
            del raw1, raw2, derivative1, derivative2, cloud1, cloud2, h, upper
            cloud1 = _checked_cloud(gaussian_points, p, 4, ar)
            cloud2 = _checked_cloud(gaussian_points, p, 2, ar)
            raw1, raw2, derivative1, derivative2, g, _, _ = _core_tables(
                dictionary, cloud1, cloud2, v, alpha, tau_core, ar)
            g = g.copy()
            del derivative1, derivative2, cloud1, cloud2
            p1 = np.full(p, ar.real(1)/ar.real(p), dtype=ar.dtype)
            p2 = p1.copy()
            constants = dict(v=str(v), alpha=str(alpha), tau_core=str(tau_core))
            strategy = "tanh-core-bounded-contractions"
        else:
            if raw_compiler is None:
                from pde.observable_compiler import compile_raw_dictionary as raw_compiler
            compiled = raw_compiler(dictionary.first_words, dictionary.second_words,
                                    arithmetic=ar, gaussian_points=gaussian_points,
                                    initialization_nodes=q, population_nodes=p,
                                    epsilon_cov=epsilon_cov, limits=limits.compiler_limits)
            raw1, raw2, g = compiled.psi1, compiled.psi2, compiled.g
            p1, p2 = compiled.probabilities1, compiled.probabilities2
            gram1, gram2, contraction = compiled.gram1, compiled.gram2, compiled.C
            strategy = "complete-gaussian-program"
        b1, b2, D = _normalize(raw1, raw2, gram1, gram2, contraction, ar, eta)
        expected = ((p, len(dictionary.first_words)), (p, len(dictionary.second_words)))
        if b1.shape != expected[0] or b2.shape != expected[1] or g.shape != (p, 2):
            raise ValueError("initializer returned inconsistent joint population shapes")
        if p1.shape != (p,) or p2.shape != (p,) or D.shape != (expected[1][1], expected[0][1]):
            raise ValueError("initializer returned inconsistent weights or action shape")
        if not all(ar.finite(a) for a in (b1, b2, g, p1, p2, D)):
            raise ValueError("nonfinite initialized feature or action entry")
        d1, d2 = expected[0][1], expected[1][1]
        metadata = dict(
            dictionary_scheme="tanh-chebyshev-plus-code-v1", hierarchy_order=dictionary.order,
            polynomial_ordering="total-degree-then-descending-lexicographic",
            feature_dimensions=[d1, d2], polynomial_dimensions=[len(dictionary.first_exponents),
                                                               len(dictionary.second_exponents)],
            retained_tail_codes=list(dictionary.tail_codes), dictionary_nodes=dictionary.node_count,
            initialization_strategy=strategy, initialization_nodes=q, population_nodes=p,
            gaussian_rule=getattr(gaussian_points, "__qualname__", type(gaussian_points).__name__),
            arithmetic_digits=ar.digits, ridge=str(eta), epsilon_cov=str(epsilon_cov),
            arithmetic_backend="float64" if ar.digits is None else getattr(ar, "backend", "decimal"),
            ridge_numerator=1, ridge_denominator=1024*(dictionary.order+1)**2,
            epsilon_cov_used=not dictionary.fast_core, exact_initialized_law=False,
            normalization="inverse-lower-Cholesky", core_constants=constants,
            initializer_output_scalars=p*(d1+d2+4)+d1*d2,
            closure_state_scalars_without_data=p*(d1+4)+p*(d2+1)+2*d1*d2+2*p,
            **resource_metadata,
        )
        return InitializedFeatures(b1, g, p1, b2, p2, D, metadata)
