"""Test-only dense square-zero multijet oracle for ordered scalar derivatives.

This deliberately does not import the production high-order initializer.
For w=(i1,...,ik), compose theta <- theta+eps_j*g_ij(theta), j=k,...,1,
in the algebra eps_j**2=0, and extract the full mixed coefficient of Theta.
The full dense parameter jets are intended ONLY for small deterministic tests.
"""

from itertools import product
from math import factorial

import numpy as np

import scalar_aggregate_engine as aggregate


def _subsets(mask):
    subset = mask
    while True:
        yield subset
        if subset == 0:
            break
        subset = (subset-1) & mask


class _Jet:
    def __init__(self, coefficients):
        self.coefficients = tuple(np.asarray(value, dtype=float) for value in coefficients)
        self.degree = (len(self.coefficients)-1).bit_length()
        if len(self.coefficients) != 2**self.degree:
            raise ValueError("jet needs a power-of-two coefficient count")

    @classmethod
    def constant(cls, value, degree):
        value = np.asarray(value, dtype=float)
        return cls((value, *(np.zeros_like(value) for _ in range(2**degree-1))))

    def _other(self, other):
        return other if isinstance(other, _Jet) else _Jet.constant(other, self.degree)

    def __add__(self, other):
        other = self._other(other)
        return _Jet(tuple(a+b for a, b in zip(self.coefficients, other.coefficients)))

    __radd__ = __add__

    def __neg__(self):
        return _Jet(tuple(-a for a in self.coefficients))

    def __sub__(self, other):
        return self+-self._other(other)

    def __rsub__(self, other):
        return self._other(other)+-self

    def _product(self, other, operation):
        other = self._other(other)
        return _Jet(tuple(sum((operation(self.coefficients[subset], other.coefficients[mask ^ subset])
                               for subset in _subsets(mask)))
                          for mask in range(len(self.coefficients))))

    def __mul__(self, other):
        return self._product(other, np.multiply)

    __rmul__ = __mul__

    def __matmul__(self, other):
        return self._product(other, np.matmul)

    def __truediv__(self, scalar):
        return _Jet(tuple(a/scalar for a in self.coefficients))

    def __getitem__(self, index):
        return _Jet(tuple(a[index] for a in self.coefficients))

    @property
    def T(self):
        return _Jet(tuple(a.T for a in self.coefficients))

    def epsilon_times(self, position):
        bit = 1 << position
        return _Jet(tuple(self.coefficients[mask ^ bit] if mask & bit
                          else np.zeros_like(self.coefficients[0])
                          for mask in range(len(self.coefficients))))

    def tanh(self):
        base = np.tanh(self.coefficients[0])
        result = _Jet.constant(base, self.degree)
        increment = self-_Jet.constant(self.coefficients[0], self.degree)
        power = _Jet.constant(np.ones_like(base), self.degree)
        polynomial = np.array([0., 1.])
        for degree in range(1, self.degree+1):
            polynomial = np.polynomial.polynomial.polymul(
                [1., 0., -1.], np.polynomial.polynomial.polyder(polynomial))
            derivative = np.polynomial.polynomial.polyval(base, polynomial)
            power = power*increment
            result = result+power*(derivative/factorial(degree))
        return result


def _fields(params, inputs):
    value = _Jet.constant(inputs.T, params[0].degree)
    h = []
    for matrix in params[:-1]:
        value = (matrix @ value).tanh()
        h.append(value)
    delta = [None]*len(h)
    delta[-1] = params[-1][:, None]*(1-h[-1]*h[-1])
    for layer in range(len(h)-2, -1, -1):
        delta[layer] = (1-h[layer]*h[layer])*(params[layer+1].T @ delta[layer+1])
    return h, delta


def _direction(params, inputs, sample):
    h, delta = _fields(params, inputs)
    n = len(params[-1].coefficients[0])
    return (delta[0][:, sample, None]*inputs[sample][None, :],
            *(delta[layer][:, sample, None]*h[layer-1][:, sample][None, :]/n
              for layer in range(1, len(h))), h[-1][:, sample])


def selected_word_kernel(params, train_inputs, probe_inputs, word):
    """Exact square-free coefficient for one ordered word (small widths only)."""
    params, train_inputs = aggregate._validated_network(params, train_inputs)
    _, probe_inputs = aggregate._validated_network(params, probe_inputs)
    word = tuple(word)
    if len(word) > 4 or any(isinstance(i, bool) or not isinstance(i, (int, np.integer))
                           or not 0 <= i < len(train_inputs) for i in word):
        raise ValueError("word requires at most four valid training indices")
    jets = tuple(_Jet.constant(value, len(word)) for value in params)
    for position in range(len(word)-1, -1, -1):
        directions = _direction(jets, train_inputs, word[position])
        jets = tuple(value+direction.epsilon_times(position) for value, direction in zip(jets, directions))
    inputs = np.vstack((train_inputs, probe_inputs))
    h, delta = _fields(jets, inputs)
    m, n = len(train_inputs), len(params[-1])

    def gram(field):
        return field[:, m:].T @ field[:, :m]/n

    theta = gram(delta[0])*(probe_inputs @ train_inputs.T)+gram(h[-1])
    for layer in range(1, len(h)):
        theta = theta+gram(h[layer-1])*gram(delta[layer])
    return theta.coefficients[-1].copy()


def initialize_probe_coefficients(params, train_inputs, probe_inputs, order=6):
    if isinstance(order, bool) or not isinstance(order, int) or not 2 <= order <= 6:
        raise ValueError("order must be from 2 through 6")
    params, train_inputs = aggregate._validated_network(params, train_inputs)
    _, probe_inputs = aggregate._validated_network(params, probe_inputs)
    m, count = len(train_inputs), len(probe_inputs)
    result = {"T1": aggregate.network_fields(params, probe_inputs)["f"]}
    for degree in range(order-1):
        tensor = np.empty((count,)+(m,)*(degree+1), dtype=float)
        for word in product(range(m), repeat=degree):
            tensor[(slice(None), slice(None), *word)] = selected_word_kernel(
                params, train_inputs, probe_inputs, word)
        result["T"+str(degree+2)] = tensor
    return result


def initialize_coefficients(params, inputs, order=6):
    return initialize_probe_coefficients(params, inputs, inputs, order)
