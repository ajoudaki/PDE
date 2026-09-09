"""Finite moving physical gradient-flow jets and held-fixed Hessians.

The raw network, residual f-y, squared loss (without one-half), and block
mobilities (n*kappa_1, kappa_2, n*kappa_3) are those of finite_network.
``flow_jet`` keeps its one-sample, two-layer, order-three contract.
``finite_flow_jets`` permits finite depth and batch through order five;
``preactivation_hessians`` differentiates only a held-fixed downstream map.
The functions accept supplied states and draw no weights. Real-arithmetic
recurrences are exact; float64 evaluations are neither exact certificates
nor population laws or finite-time flow solvers.
"""

from dataclasses import dataclass
from math import factorial
from numbers import Integral
from typing import Callable

import numpy as np

from .finite_network import (
    Parameters, _array, _evaluate, _kappas, _labels, _scaled_product,
)


DerivativeOracle = Callable[[int, np.ndarray], np.ndarray]


@dataclass(frozen=True)
class FlowJet:
    """Ordinary coefficients v[k] = (d/dt)^k v(0) / k!.

    parameter_coefficients[k] is a Parameters in the existing raw storage.
    Each of the two preactivation_coefficients and hidden_coefficients
    arrays has shape (order+1,n,1); output_coefficients is (order+1,1).
    Layer tuple positions 0,1 mean layers 1,2. The middle weight entry
    [i,j] maps first-layer neuron j to second-layer neuron i.
    All arrays are mutable and independent of inputs and callback buffers.
    """

    parameter_coefficients: tuple[Parameters, ...]
    preactivation_coefficients: tuple[np.ndarray, np.ndarray]
    hidden_coefficients: tuple[np.ndarray, np.ndarray]
    output_coefficients: np.ndarray

    @property
    def output_derivatives(self) -> np.ndarray:
        """Return a new finite array of physical-time output derivatives."""
        factors = np.array([factorial(k) for k in range(len(self.output_coefficients))])
        return _array(_scaled_product(factors[:, None], self.output_coefficients),
                      "output derivatives")


def _compose(derivatives, series, degree, shift=0):
    """Coefficient of phi(series), or phi'(series) when shift=1."""
    if degree == 0:
        return derivatives[shift]
    value = derivatives[shift + 1] * series[degree]
    if degree == 2:
        value = value + 0.5 * derivatives[shift + 2] * series[1] ** 2
    if degree == 3:
        value = (value + derivatives[shift + 2] * series[1] * series[2]
                 + derivatives[shift + 3] * series[1] ** 3 / 6.0)
    return _array(value, "activation jet coefficient")


def _convolve(left, right, degree, product):
    """Coefficient of a bilinear product, retaining every degree split."""
    value = product(left[0], right[degree])
    for index in range(1, degree + 1):
        value = value + product(left[index], right[degree - index])
    return _array(value, "jet contraction")


def flow_jet(parameters: Parameters, inputs, labels,
             activation_derivative: DerivativeOracle, *, order: int = 3,
             kappas=None) -> FlowJet:
    """Compute the moving physical GF jet at the supplied state, orders 0..3.

    Only two hidden layers and one sample are accepted. Inputs retain shape
    (d,1), labels shape (1,), and arbitrary finite inputs (including zero)
    are allowed. kappas is the finite API's positive length-three vector.
    Import this function from pde.finite_jets; no package re-export is needed.

    activation_derivative(j,z) supplies the j-th derivative of ONE shared
    scalar C3 activation, coordinatewise, with j=0 meaning its value. Only
    j=0,...,order are requested, at initial preactivations of shape (n,1).
    Real finite shape-preserving outputs are required; scalar broadcasting
    is rejected even at width one. Each invocation receives a private copy
    and its output is copied immediately. In-place callbacks and shared
    output buffers are supported. Callbacks must give consistent actual
    derivatives and must not mutate unrelated external calculation state;
    these semantic and regularity conditions are the caller's obligation.

    All weight blocks, the reused transpose, and the residual move. These
    are not frozen-direction derivatives or feature-time coefficients.
    Scalar mobility/normalization factors use the finite API's scaled
    multiplication. Raw products, sums and composition powers still use
    float64 and may overflow or underflow; nonfinite evaluated coefficients
    raise ValueError. No correct-rounding or extreme-range guarantee is made.
    Order zero validates arguments and evaluates only activation values.
    """
    if not isinstance(parameters, Parameters):
        raise TypeError("parameters must be Parameters")
    parameters.validate()
    if parameters.depth != 2:
        raise ValueError("flow_jet requires exactly two hidden layers")
    if (isinstance(order, (bool, np.bool_)) or not isinstance(order, Integral)
            or not 0 <= order <= 3):
        raise ValueError("order must be an integer between zero and three")
    order = int(order)
    if not callable(activation_derivative):
        raise TypeError("activation_derivative must be callable")
    x = _array(inputs, "inputs")
    if x.shape != (parameters.input_dimension, 1):
        raise ValueError("inputs must have shape (d,1)")
    x = x.copy()
    y = _labels(labels, 1).copy()
    rates = _kappas(kappas, 2).copy()
    n, d = parameters.width, parameters.input_dimension
    first = np.zeros((order + 1, n, d))
    middle = np.zeros((order + 1, n, n))
    readout = np.zeros((order + 1, n))
    first[0], middle[0] = parameters.weights
    readout[0] = parameters.readout
    z = tuple(np.zeros((order + 1, n, 1)) for _ in range(2))
    h = tuple(np.zeros_like(z[0]) for _ in range(2))
    # The terminal backward coefficient is unused: phi^(order+1) is not needed.
    phi_prime = tuple(np.zeros((order, n, 1)) for _ in range(2))
    delta = tuple(np.zeros_like(phi_prime[0]) for _ in range(2))
    propagated = np.zeros_like(phi_prime[0])
    residual_delta = np.zeros_like(phi_prime[0])
    output = np.zeros((order + 1, 1))
    residual = np.zeros_like(output)
    derivatives = [None, None]

    with np.errstate(over="ignore", invalid="ignore", under="ignore"):
        for k in range(order + 1):
            # Normalize only after the first raw matrix contraction.
            z[0][k] = _array((first[k] @ x) / np.sqrt(d), "first preactivation")
            for layer in range(2):
                if layer == 1:
                    z[1][k] = _convolve(middle, h[0], k, np.matmul)
                if k == 0:
                    derivatives[layer] = tuple(
                        _evaluate(lambda arg, j=j: activation_derivative(j, arg),
                                  z[layer][0], f"activation derivative {j}")
                        for j in range(order + 1)
                    )
                h[layer][k] = _compose(derivatives[layer], z[layer], k)
            output[k] = _array(_convolve(readout, h[1], k, np.matmul) / n,
                               "output coefficient")
            if k == order:
                break
            residual[k] = _array(output[k] - y if k == 0 else output[k],
                                 "residual coefficient")
            for layer in range(2):
                phi_prime[layer][k] = _compose(derivatives[layer], z[layer], k, 1)
            delta[1][k] = _convolve(readout[:, :, None], phi_prime[1], k, np.multiply)
            # The SAME moving W^(2), with indices transposed, is used here.
            propagated[k] = _convolve(middle, delta[1], k, lambda w, v: w.T @ v)
            delta[0][k] = _convolve(phi_prime[0], propagated, k, np.multiply)
            residual_delta[k] = _convolve(residual, delta[1], k, np.multiply)
            raw = (
                _array(_convolve(residual, delta[0], k, np.multiply) @ x.T,
                       "first raw contraction"),
                _convolve(residual_delta, h[0], k, lambda v, u: v @ u.T),
                _convolve(h[1], residual, k, np.matmul),
            )
            for target, contraction, rate, normalizer in zip(
                    (first, middle, readout), raw, rates, (1.0 / np.sqrt(d), 1.0 / n, 1.0)):
                target[k + 1] = _array(
                    _scaled_product(-2.0, rate, normalizer, 1.0 / (k + 1), contraction),
                    "parameter coefficient",
                )

    coefficients = tuple(Parameters((first[k], middle[k]), readout[k])
                         for k in range(order + 1))
    return FlowJet(coefficients, z, h, output)


@dataclass(frozen=True)
class FiniteFlowJet:
    """Ordinary coefficients for a supplied arbitrary finite depth and batch.

    Parameter, preactivation, hidden and output degrees are 0..order.
    Backward degrees are 0..order-1 (empty when order=0). Each layer array
    has shape (degrees,n,m), output has shape (order+1,m). Arrays are owned
    independently of the inputs and callback buffers. clock is fixed.
    """
    parameter_coefficients: tuple[Parameters, ...]
    preactivation_coefficients: tuple[np.ndarray, ...]
    hidden_coefficients: tuple[np.ndarray, ...]
    backward_coefficients: tuple[np.ndarray, ...]
    output_coefficients: np.ndarray
    clock: str = "physical_full_mean_loss"


def _general_jet_arguments(parameters, inputs, activations):
    if not isinstance(parameters, Parameters):
        raise TypeError("parameters must be Parameters")
    parameters.validate()
    x = _array(inputs, "inputs").copy()
    if x.ndim != 2 or x.shape[0] != parameters.input_dimension or x.shape[1] < 1:
        raise ValueError("inputs must have shape (d,m), m positive")
    if (not isinstance(activations, (tuple, list)) or len(activations) != parameters.depth
            or any(not callable(oracle) for oracle in activations)):
        raise ValueError("activations must contain one derivative callback per hidden layer")
    return x, tuple(activations)


def _compose_general(derivatives, series, degree, shift=0):
    if degree == 0:
        return derivatives[shift].copy()
    power = np.zeros((degree+1,)+series[0].shape)
    power[0] = 1.0
    result = np.zeros_like(series[0])
    for count in range(1, degree+1):
        new = np.zeros_like(power)
        for k in range(1, degree+1):
            for i in range(1, k+1):
                new[k] += power[k-i]*series[i]
        power = new
        result += derivatives[shift+count]*power[degree]/factorial(count)
    return _array(result, "activation coefficient")


def finite_flow_jets(parameters, inputs, labels, activations, *, order=3, kappas=None):
    """Moving full-mean-loss finite GF coefficients through order 0..5.

    Accepts every fixed finite hidden depth, common width, finite batch and
    arbitrary supplied real data. The first input factor is 1/sqrt(d), the
    readout factor 1/n, and mobilities (n*k1,k2,...,kL,n*kout) with positive
    kappas. All blocks and the actual residual and reused transposes move.
    No initialization is drawn and no time trajectory is computed.

    activations is a length-L tuple/list of callbacks oracle(j,z), each for
    one componentwise C**(order+1) activation near the supplied state (for
    order=0 only its values are needed). Derivatives 0..order are requested
    at the initial (n,m) preactivations. Consistency and regularity are caller
    obligations. Each callback receives private input, and its real finite
    shape-preserving output is copied; shared or in-place buffers are allowed.
    Numerical arithmetic is float64, not an exact rational certificate.
    Products can overflow/underflow; detected nonfinite results raise ValueError.
    No correct-rounding or extreme-range guarantee is made.
    """
    x, oracles = _general_jet_arguments(parameters, inputs, activations)
    if (isinstance(order, (bool, np.bool_)) or not isinstance(order, Integral)
            or not 0 <= order <= 5):
        raise ValueError("order must be an integer from zero through five")
    order = int(order)
    depth, n, d, m = parameters.depth, parameters.width, parameters.input_dimension, x.shape[1]
    y, rates = _labels(labels, m).copy(), _kappas(kappas, depth).copy()
    weights = [np.zeros((order+1,)+w.shape) for w in parameters.weights]
    for target, source in zip(weights, parameters.weights):
        target[0] = source
    readout = np.zeros((order+1, n))
    readout[0] = parameters.readout
    z = tuple(np.zeros((order+1, n, m)) for _ in range(depth))
    h = tuple(np.zeros_like(z[0]) for _ in range(depth))
    delta = tuple(np.zeros((order, n, m)) for _ in range(depth))
    slope = tuple(np.zeros_like(delta[0]) for _ in range(depth))
    residual_delta = tuple(np.zeros_like(delta[0]) for _ in range(depth))
    output = np.zeros((order+1, m))
    residual = np.zeros_like(output)
    derivatives = [None]*depth
    with np.errstate(over="ignore", invalid="ignore", under="ignore"):
        for k in range(order+1):
            z[0][k] = _array((weights[0][k] @ x)/np.sqrt(d), "first preactivation")
            for layer in range(depth):
                if layer:
                    z[layer][k] = _convolve(weights[layer], h[layer-1], k, np.matmul)
                if k == 0:
                    derivatives[layer] = tuple(
                        _evaluate(lambda arg, j=j, oracle=oracles[layer]: oracle(j, arg),
                                  z[layer][0], f"layer {layer+1} derivative {j}")
                        for j in range(order+1))
                h[layer][k] = _compose_general(derivatives[layer], z[layer], k)
            output[k] = _array(_convolve(readout, h[-1], k, np.matmul)/n, "output coefficient")
            if k == order:
                break
            residual[k] = _array(output[k]-y if k == 0 else output[k], "residual coefficient")
            for layer in range(depth):
                slope[layer][k] = _compose_general(derivatives[layer], z[layer], k, shift=1)
            delta[-1][k] = _convolve(readout[:, :, None], slope[-1], k, np.multiply)
            for layer in range(depth-2, -1, -1):
                # Recompute the lower-degree incoming series with the same moving transpose.
                incoming = np.stack([_convolve(weights[layer+1], delta[layer+1], j,
                                                lambda w, v: w.T @ v) for j in range(k+1)])
                delta[layer][k] = _convolve(slope[layer], incoming, k, np.multiply)
            for layer in range(depth):
                residual_delta[layer][k] = _convolve(residual, delta[layer], k, np.multiply)
                raw = (residual_delta[layer][k] @ x.T if layer == 0 else
                       _convolve(residual_delta[layer], h[layer-1], k, lambda v, u: v @ u.T))
                weights[layer][k+1] = _array(_scaled_product(
                    -2.0/m, rates[layer], 1.0/(k+1),
                    1.0/np.sqrt(d) if layer == 0 else 1.0/n, raw), "weight coefficient")
            raw_readout = _convolve(h[-1], residual, k, np.matmul)
            readout[k+1] = _array(_scaled_product(-2.0/m, rates[-1], 1.0/(k+1), raw_readout),
                                  "readout coefficient")
    parameters_out = tuple(Parameters(tuple(w[k].copy() for w in weights), readout[k].copy())
                           for k in range(order+1))
    return FiniteFlowJet(parameters_out, z, h, delta, output)


def hidden_gram_jet(jet, layer, *, kind):
    """Ordinary same-layer sample-Gram coefficients, with explicit RMS 1/n.

    layer is one-based; kind is 'activation' or 'preactivation'. Coefficients
    of X(t)^T X(t)/n are summed by every degree split. The returned array is
    freshly owned and has shape (order+1,m,m); no cross-layer pairing is made.
    """
    if not isinstance(jet, (FlowJet, FiniteFlowJet)):
        raise TypeError("jet must be FlowJet or FiniteFlowJet")
    if (isinstance(layer, (bool, np.bool_)) or not isinstance(layer, Integral)
            or not 1 <= layer <= len(jet.hidden_coefficients)):
        raise ValueError("layer must be an in-range one-based integer")
    if kind not in ("activation", "preactivation"):
        raise ValueError("kind must be activation or preactivation")
    fields = jet.hidden_coefficients if kind == "activation" else jet.preactivation_coefficients
    values = _array(fields[int(layer)-1], "jet fields")
    if values.ndim != 3 or min(values.shape) < 1:
        raise ValueError("jet fields must have shape (order+1,n,m)")
    n = values.shape[1]
    with np.errstate(over="ignore", invalid="ignore"):
        return np.stack([_array(_convolve(values, values, k, lambda v, u: v.T @ u)/n,
                                "hidden Gram coefficient") for k in range(len(values))])


@dataclass(frozen=True)
class HessianWord:
    """Held-fixed downstream preactivation-Hessian term.

    source_layer is one-based. Each factor is (role, layer, (rows,cols));
    roles D, W, WT, E mean activation slope, stored matrix, its actual
    transpose, and diag(phi''*incoming_backprop). Multiplication is left
    to right. There is no full-parameter Hessian or probabilistic meaning.
    """
    source_layer: int
    factors: tuple


def preactivation_hessian_words(layer_shapes, *, affine_flags=None):
    """Compile the exact source expansion of n_L*Hess_(z1) f.

    layer_shapes is the nonempty sequence of positive hidden widths, allowing
    unequal widths. affine_flags must declare identically affine activations,
    not merely an accidental zero second derivative at a state. Declared
    affine SOURCE terms are omitted; their slope factors in other terms remain.
    This finite typed word expansion has no closure/convergence implication.
    """
    if not isinstance(layer_shapes, (list, tuple)) or not layer_shapes:
        raise ValueError("layer_shapes must be a nonempty list or tuple")
    if any(isinstance(v, (bool, np.bool_)) or not isinstance(v, Integral) or v < 1
           for v in layer_shapes):
        raise ValueError("every hidden width must be a positive integer")
    widths = tuple(int(v) for v in layer_shapes)
    depth = len(widths)
    if affine_flags is None:
        affine_flags = (False,)*depth
    if (not isinstance(affine_flags, (list, tuple)) or len(affine_flags) != depth
            or any(type(v) is not bool for v in affine_flags)):
        raise ValueError("affine_flags must be a matching boolean list or tuple")
    terms = []
    for source in range(1, depth+1):
        if affine_flags[source-1]:
            continue
        factors = []
        for layer in range(1, source):
            factors.extend((("D", layer, (widths[layer-1], widths[layer-1])),
                            ("WT", layer+1, (widths[layer-1], widths[layer]))))
        factors.append(("E", source, (widths[source-1], widths[source-1])))
        for layer in range(source, 1, -1):
            factors.extend((("W", layer, (widths[layer-1], widths[layer-2])),
                            ("D", layer-1, (widths[layer-2], widths[layer-2]))))
        terms.append(HessianWord(source, tuple(factors)))
    return tuple(terms)


@dataclass(frozen=True)
class PreactivationHessians:
    """Finite held-fixed downstream Hessians scaled by the last width n.

    Per-layer local_sources and hessians have shape (m,n,n); preactivations,
    hidden, slopes and backward fields have shape (n,m). All arrays are owned.
    This is not the full parameter Hessian or a trained material derivative.
    """
    preactivations: tuple[np.ndarray, ...]
    hidden: tuple[np.ndarray, ...]
    slopes: tuple[np.ndarray, ...]
    backward: tuple[np.ndarray, ...]
    local_sources: tuple[np.ndarray, ...]
    hessians: tuple[np.ndarray, ...]


def preactivation_hessians(parameters, inputs, activations):
    """Evaluate typed source/Hessian recursion for the existing equal-width API.

    Every layer callback supplies values, first and second derivatives of a
    componentwise C2 activation. It receives a private (n,m) preactivation;
    finite real shape-preserving outputs are copied. All weights downstream
    of the independently varied preactivation, and the readout, are held fixed.
    No labels, loss, optimizer or initialization are presumed. Float64 products
    can overflow or underflow; nonfinite outputs raise ValueError, without a
    correct-rounding or extreme-range guarantee.
    """
    x, oracles = _general_jet_arguments(parameters, inputs, activations)
    depth, n, m = parameters.depth, parameters.width, x.shape[1]
    z, h, slope, curvature = [], [], [], []
    # Snapshot parameters too: callback buffer ownership never changes the state.
    weights = tuple(w.copy() for w in parameters.weights)
    readout = parameters.readout.copy()
    with np.errstate(over="ignore", invalid="ignore", under="ignore"):
        value = x/np.sqrt(parameters.input_dimension)
        for layer in range(depth):
            current = _array(weights[layer] @ value, "preactivation")
            derivatives = tuple(_evaluate(lambda arg, j=j, oracle=oracles[layer]: oracle(j, arg),
                                          current, f"layer {layer+1} derivative {j}") for j in range(3))
            z.append(current.copy())
            value = derivatives[0]
            h.append(value.copy())
            slope.append(derivatives[1])
            curvature.append(derivatives[2])
        delta, sources, hessians = [None]*depth, [None]*depth, [None]*depth
        for layer in range(depth-1, -1, -1):
            incoming = np.broadcast_to(readout[:, None], (n, m)) if layer == depth-1 else weights[layer+1].T @ delta[layer+1]
            delta[layer] = _array(slope[layer]*incoming, "backward field")
            source = _array(curvature[layer]*incoming, "curvature source")
            sources[layer] = np.stack([np.diag(source[:, sample]) for sample in range(m)])
            values = []
            for sample in range(m):
                result = sources[layer][sample].copy()
                if layer < depth-1:
                    J = weights[layer+1]*slope[layer][:, sample][None, :]
                    result += J.T @ hessians[layer+1][sample] @ J
                values.append(_array(result, "preactivation Hessian"))
            hessians[layer] = np.stack(values)
    return PreactivationHessians(tuple(z), tuple(h), tuple(slope), tuple(delta), tuple(sources), tuple(hessians))
