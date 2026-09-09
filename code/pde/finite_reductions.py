"""Finite two-hidden-layer reductions for x=1 and unit block multipliers.

Stored parameters are (u[:, None], B), a; B acts without another width
factor. The metric is ||du||²/n + ||dB||_F² + ||da||²/n. These routines
evaluate output-ascent and full-squared-loss physical vector fields at one
state. They neither integrate a trajectory nor assert a width limit.

All returned arrays are fresh float64 arrays. Evaluated nonfinite values are
rejected. Intermediate overflow/underflow and rounding are still ordinary
float64 limitations; this is not exact rational arithmetic or a range-proof
implementation. Gaussian initialization is not performed or assumed.
"""

from dataclasses import dataclass
from numbers import Real

import numpy as np

from .finite_network import Parameters


@dataclass(frozen=True)
class ReductionEvaluation:
    """Current-state finite output, fields and vector fields.

    ``kernel_blocks`` has shape (3,) in first/middle/readout order.
    ``ascent`` is the metric gradient of the output; ``velocity`` is
    -2*(output-label)*ascent. ``field_ascent`` uses the same unit ascent.
    ``row_balance_ascent`` and ``column_balance_ascent`` give the derivative
    of n*sum(B²)-2*a² and n*sum(B²)-u²/2; they are present for QQ and RMS,
    and None for the other mixed models. Multiply them by -2*residual for
    physical derivatives. Dictionaries and their arrays are caller-owned.
    """

    output: float
    residual: float
    loss: float
    kernel: float
    kernel_blocks: np.ndarray
    output_velocity: float
    loss_velocity: float
    ascent: Parameters
    velocity: Parameters
    fields: dict[str, np.ndarray | float]
    field_ascent: dict[str, np.ndarray | float]
    row_balance_ascent: np.ndarray | None
    column_balance_ascent: np.ndarray | None


@dataclass(frozen=True)
class LaxEvaluation:
    """Ordinary Euclidean isometric block matrices for QI or IQ.

    ``operator = signature @ gram``; ``ascent = [operator,generator]``.
    For IQ the generator already includes the factor two. QI's ``factor``
    is [a/sqrt(n), B], while IQ's is [B; h.T/sqrt(n)]. The Gram is factor.T
    @ factor for QI and factor @ factor.T for IQ. These matrices have size
    n+1 and retain orientation. ``ascent`` is a feature vector field, not
    the derivative for an unspecified physical label.
    """

    factor: np.ndarray
    factor_ascent: np.ndarray
    gram: np.ndarray
    signature: np.ndarray
    operator: np.ndarray
    generator: np.ndarray
    ascent: np.ndarray


def _scalar(value, name, *, positive=False):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, Real):
        raise ValueError(f"{name} must be a finite real scalar")
    try:
        result = float(value)
    except (ValueError, OverflowError) as error:
        raise ValueError(f"{name} must be a finite real scalar") from error
    if not np.isfinite(result) or (positive and result <= 0):
        raise ValueError(f"{name} must be finite" + (" and positive" if positive else ""))
    return result


def _state(parameters):
    if not isinstance(parameters, Parameters):
        raise TypeError("parameters must be Parameters")
    parameters.validate()
    if parameters.depth != 2 or parameters.input_dimension != 1:
        raise ValueError("the reduction requires two hidden layers and x=1 in dimension one")
    return (parameters.weights[0][:, 0].copy(), parameters.weights[1].copy(),
            parameters.readout.copy())


def _finite(value, name):
    if not np.all(np.isfinite(value)):
        raise ValueError(f"{name} is not representable as finite float64")
    return value


def _field_copies(fields):
    return {name: (float(_finite(value, name)) if np.ndim(value) == 0
                   else np.array(_finite(value, name), dtype=np.float64, copy=True))
            for name, value in fields.items()}


def _evaluation(a, v, label, ascent, fields, derivatives, row=None, column=None):
    n = a.size
    output = float(_finite(a @ v / n, "output"))
    residual = float(_finite(output - label, "residual"))
    blocks = np.array([np.sum(ascent.weights[0] ** 2) / n,
                       np.sum(ascent.weights[1] ** 2),
                       np.sum(ascent.readout ** 2) / n])
    _finite(blocks, "kernel blocks")
    kernel = float(_finite(blocks.sum(), "kernel"))
    multiplier = -2.0 * residual
    velocity = Parameters(tuple(multiplier * w for w in ascent.weights),
                          multiplier * ascent.readout)
    loss = float(_finite(residual * residual, "loss"))
    output_velocity = float(_finite(multiplier * kernel, "output velocity"))
    loss_velocity = float(_finite(-4.0 * loss * kernel, "loss velocity"))
    return ReductionEvaluation(
        output, residual, loss, kernel, blocks, output_velocity, loss_velocity,
        ascent, velocity, _field_copies(fields), _field_copies(derivatives),
        None if row is None else np.array(_finite(row, "row balance"), copy=True),
        None if column is None else np.array(_finite(column, "column balance"), copy=True),
    )


def mixed_quadratic(parameters: Parameters, label, *, model="QQ") -> ReductionEvaluation:
    """Evaluate QI, IQ or QQ, with raw coordinatewise square Q and identity I.

    ``fields`` contains h (first feature), z (second preactivation), v
    (second feature), b (a for QI, a*z otherwise), q=B.T@b.
    ``field_ascent`` contains h,z,v. Input is fixed to x=1; label is scalar;
    all three mobility multipliers are one. Supplied parameters are unchanged.
    """
    if not isinstance(model, str) or model not in ("QI", "IQ", "QQ"):
        raise ValueError("model must be QI, IQ or QQ")
    u, matrix, a = _state(parameters)
    label = _scalar(label, "label")
    n = u.size
    try:
        with np.errstate(over="raise", invalid="raise", divide="raise", under="ignore"):
            h = u * u if model[0] == "Q" else u.copy()
            z = matrix @ h
            v = z * z if model[1] == "Q" else z.copy()
            b = a * z if model[1] == "Q" else a.copy()
            q = matrix.T @ b
            multiplier = 2.0 if model[1] == "Q" else 1.0
            du = multiplier * q
            if model[0] == "Q":
                du = 2.0 * u * du
            dmatrix = multiplier * np.outer(b, h) / n
            dh = 2.0 * u * du if model[0] == "Q" else du.copy()
            dz = dmatrix @ h + matrix @ dh
            dv = 2.0 * z * dz if model[1] == "Q" else dz.copy()
            ascent = Parameters((du[:, None], dmatrix), v.copy())
            balances = np.zeros(n) if model == "QQ" else None
            return _evaluation(a, v, label, ascent,
                               {"h": h, "z": z, "v": v, "b": b, "q": q},
                               {"h": dh, "z": dz, "v": dv}, balances, balances)
    except FloatingPointError as error:
        raise ValueError("mixed reduction encountered a nonfinite float64 intermediate") from error


def mixed_lax(parameters: Parameters, *, model) -> LaxEvaluation:
    """Evaluate the QI/IQ Lax factorization and its unit-ascent derivative.

    Only finite raw-image states are accepted. No eigenvalue-only dynamics
    or generic independent block-matrix initial state is provided.
    """
    if not isinstance(model, str) or model not in ("QI", "IQ"):
        raise ValueError("a Lax reduction is provided only for QI or IQ")
    u, matrix, a = _state(parameters)
    n, scale = u.size, np.sqrt(u.size)
    try:
        with np.errstate(over="raise", invalid="raise", divide="raise", under="ignore"):
            generator = np.zeros((n + 1, n + 1))
            signature = np.eye(n + 1)
            if model == "QI":
                h = u * u
                factor = np.column_stack((a / scale, matrix))
                generator[0, 1:] = h / scale
                generator[1:, 0] = h / scale
                factor_ascent = factor @ generator
                gram = factor.T @ factor
                signature[0, 0] = -1.0
            else:
                b = a * (matrix @ u)
                factor = np.vstack((matrix, u / scale))
                generator[:-1, -1] = 2.0 * b / scale
                generator[-1, :-1] = 2.0 * b / scale
                factor_ascent = generator @ factor
                gram = factor @ factor.T
                signature[-1, -1] = -1.0
            operator = signature @ gram
            ascent = operator @ generator - generator @ operator
            values = (factor, factor_ascent, gram, signature, operator, generator, ascent)
            for value in values:
                _finite(value, "Lax matrix")
            return LaxEvaluation(*(value.copy() for value in values))
    except FloatingPointError as error:
        raise ValueError("Lax reduction encountered a nonfinite float64 intermediate") from error


def rms_quadratic(parameters: Parameters, label, *, epsilon) -> ReductionEvaluation:
    """Evaluate the square network with both RMS denominators differentiated.

    epsilon must be strictly positive. Fields are p=u², alpha, h=p/alpha,
    z=B@h, w=z², beta, v=w/beta, c=a-output*v, b=2*z*c/beta,
    q=B.T@b, q_tilde=q-h*(h@q/n). ``field_ascent`` supplies p,alpha,h,z,w,beta,v.
    The full RMS architecture is not a scalar Activation callback.
    """
    u, matrix, a = _state(parameters)
    label = _scalar(label, "label")
    epsilon = _scalar(epsilon, "epsilon", positive=True)
    n = u.size
    try:
        with np.errstate(over="raise", invalid="raise", divide="raise", under="ignore"):
            p = u * u
            alpha = np.sqrt(p @ p / n + epsilon)
            h = p / alpha
            z = matrix @ h
            w = z * z
            beta = np.sqrt(w @ w / n + epsilon)
            v = w / beta
            output = a @ v / n
            c = a - output * v
            b = 2.0 * z * c / beta
            q = matrix.T @ b
            q_tilde = q - h * (h @ q / n)
            du = 2.0 * u * q_tilde / alpha
            dmatrix = np.outer(b, h) / n
            dp = 2.0 * u * du
            dalpha = h @ dp / n
            dh = (dp - h * (h @ dp / n)) / alpha
            dz = dmatrix @ h + matrix @ dh
            dw = 2.0 * z * dz
            dbeta = v @ dw / n
            dv = (dw - v * (v @ dw / n)) / beta
            ascent = Parameters((du[:, None], dmatrix), v.copy())
            return _evaluation(
                a, v, label, ascent,
                {"p": p, "alpha": alpha, "h": h, "z": z, "w": w, "beta": beta,
                 "v": v, "c": c, "b": b, "q": q, "q_tilde": q_tilde},
                {"p": dp, "alpha": dalpha, "h": dh, "z": dz, "w": dw,
                 "beta": dbeta, "v": dv},
                -4.0 * output * v * v,
                4.0 * epsilon * output * h * h / (beta * beta),
            )
    except FloatingPointError as error:
        raise ValueError("RMS reduction encountered a nonfinite float64 intermediate") from error
