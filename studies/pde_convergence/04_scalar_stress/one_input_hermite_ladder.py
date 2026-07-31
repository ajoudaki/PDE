"""Minimal one-input stress test for the neural-PDE Hermite hierarchy.

The experiment deliberately reduces both the sample count and ambient input
dimension to one.  The immutable neuron label is then

    theta = (B(0), a(0)/A) in R^2.

For an odd activation and the exact global sign symmetry, only odd Hermite
degrees are active.  The complete active mode counts through degrees
1, 3, 5, 7, 9, 11, 13 are only 2, 6, 12, 20, 30, 42, 56.

This file is a diagnostic wrapper around the existing audited PDE and dense
vector fields.  It adds one theory-selected activation at runtime,

    phi(z) = sin(2.5 z) / 2.5,

without modifying the frozen source tree.  The activation is smooth, odd,
bounded, and 1-Lipschitz, but has much more non-linear Hermite energy than
the canonical tanh at the initialization preactivation variance.
"""

from __future__ import annotations

import argparse
import dataclasses
import gc
import hashlib
import json
import math
from pathlib import Path
import sys
import time
from types import MappingProxyType
from typing import Any, Iterable, Sequence

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_SOURCE = ROOT / "activation_linearity_smoking_gun" / "source" / "src"
AUDIT_SOURCE = ROOT / "pde_proof_obligation_audit" / "source"
for source in (CANONICAL_SOURCE, AUDIT_SOURCE):
    if str(source) not in sys.path:
        sys.path.insert(0, str(source))

import activations as activation_registry  # noqa: E402
from activations import Activation  # noqa: E402


OMEGA = 2.5
SINE_NAME = "sine_2p5"


def _sine_value(z: np.ndarray) -> np.ndarray:
    return np.sin(OMEGA * z) / OMEGA


def _sine_derivative(z: np.ndarray) -> np.ndarray:
    return np.cos(OMEGA * z)


def _register_sine() -> None:
    """Extend only this process's closed activation registry."""

    if SINE_NAME in activation_registry.ACTIVATIONS:
        return
    records = dict(activation_registry.ACTIVATIONS)
    records[SINE_NAME] = Activation(
        SINE_NAME,
        _sine_value,
        _sine_derivative,
    )
    activation_registry.ACTIVATIONS = MappingProxyType(records)
    activation_registry.ACTIVATION_NAMES = tuple(records)


_register_sine()

from cross_p import (  # noqa: E402
    NestedQuadratureFamily,
    _block_orthonormalize,
    _norm_components,
    _quadrature_record,
)
from dense_pde.operator_galerkin import (  # noqa: E402
    PDESpec,
    PDEState,
    _eval_hermite_basis,
    _multi_indices,
    _normal_hermite_tensor,
    _normal_sobol,
    initialize,
    observe,
    vector_field,
)
from dense_reference import (  # noqa: E402
    ModelSpec,
    forward_adjoint,
    initialize as initialize_dense,
    rk4_param_step,
)


ODD_DEGREES = (1, 3, 5, 7, 9, 11, 13)


def _canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _parse_degrees(value: str) -> tuple[int, ...]:
    degrees = tuple(int(item) for item in value.split(","))
    if (
        not degrees
        or tuple(sorted(set(degrees))) != degrees
        or any(item not in ODD_DEGREES for item in degrees)
    ):
        raise argparse.ArgumentTypeError(
            f"degrees must be an increasing subset of {ODD_DEGREES}"
        )
    return degrees


def _parse_activations(value: str) -> tuple[str, ...]:
    activations = tuple(item.strip() for item in value.split(","))
    allowed = ("tanh", SINE_NAME)
    if (
        not activations
        or len(set(activations)) != len(activations)
        or any(item not in allowed for item in activations)
    ):
        raise argparse.ArgumentTypeError(
            f"activations must be a comma-separated subset of {allowed}"
        )
    return activations


def _odd_schedule(
    latent_dim: int,
    master_degree: int,
) -> tuple[
    tuple[tuple[int, ...], ...],
    tuple[int, ...],
    dict[int, int],
]:
    if master_degree not in ODD_DEGREES:
        raise ValueError(f"master_degree must be one of {ODD_DEGREES}")
    full_count = math.comb(master_degree + latent_dim, latent_dim)
    full = _multi_indices(latent_dim, full_count)
    odd = tuple(index for index in full if sum(index) % 2 == 1)
    degrees = tuple(item for item in ODD_DEGREES if item <= master_degree)
    ends = tuple(
        sum(sum(index) <= degree for index in odd)
        for degree in degrees
    )
    if not ends or ends[-1] != len(odd):
        raise AssertionError("odd Hermite schedule is inconsistent")
    return odd, ends, dict(zip(degrees, ends, strict=True))


def _odd_family(
    template: PDESpec,
    *,
    master_degree: int,
    base_order: int,
) -> tuple[NestedQuadratureFamily, dict[int, int]]:
    latent_dim = template.X.shape[0] + 1
    indices, levels, degree_to_level = _odd_schedule(
        latent_dim,
        master_degree,
    )
    maximum = levels[-1]
    if template.fast_points % 2:
        raise ValueError("parity-paired fast cubature requires even R")
    if template.fast_points // 2 < maximum:
        raise ValueError(
            f"R/2 must be at least the {maximum} active master modes"
        )

    base_latent, base_weights = _normal_hermite_tensor(
        base_order,
        latent_dim,
    )
    raw_phi = _eval_hermite_basis(base_latent, indices)
    phi = _block_orthonormalize(
        raw_phi,
        base_weights,
        levels,
        center=False,
    )

    half = _normal_sobol(
        template.fast_points // 2,
        maximum,
        template.quadrature_seed + 104729,
    )
    raw_epsilon = np.concatenate((half, -half), axis=0)
    fast_weights = np.full(
        template.fast_points,
        1.0 / template.fast_points,
        dtype=float,
    )
    epsilon = _block_orthonormalize(
        raw_epsilon,
        fast_weights,
        levels,
        center=True,
    )

    specs: dict[int, PDESpec] = {}
    quadratures: dict[int, Any] = {}
    for level in levels:
        spec = dataclasses.replace(
            template,
            basis_size=level,
            base_points=base_latent.shape[0],
        )
        spec.validate()
        specs[level] = spec
        quadratures[level] = _quadrature_record(
            base_latent=base_latent,
            base_weights=base_weights,
            raw_phi=raw_phi[:, :level],
            phi=phi[:, :level],
            raw_epsilon=raw_epsilon[:, :level],
            epsilon=epsilon[:, :level],
            fast_weights=fast_weights,
            multi_indices=indices[:level],
        )
    family = NestedQuadratureFamily(
        levels=levels,
        master_levels=levels,
        specs=specs,
        quadratures=quadratures,
        raw_epsilon=raw_epsilon,
        base_order=base_order,
    )
    return family, degree_to_level


def _add_scaled(
    state: PDEState,
    direction: PDEState,
    scale: float,
) -> PDEState:
    return PDEState(
        B=state.B + scale * direction.B,
        a=state.a + scale * direction.a,
        c=state.c + scale * direction.c,
    )


def _midpoint_step(
    state: PDEState,
    dt: float,
    spec: PDESpec,
    quadrature: Any,
) -> PDEState:
    first, fields = vector_field(state, spec, quadrature)
    del fields
    midpoint = _add_scaled(state, first, 0.5 * dt)
    del first
    second, fields = vector_field(midpoint, spec, quadrature)
    del fields, midpoint
    result = _add_scaled(state, second, dt)
    del second
    return result


def _record_observation(
    state: PDEState,
    spec: PDESpec,
    quadrature: Any,
) -> tuple[float, float, np.ndarray]:
    fields = None
    item = observe(state, spec, quadrature, fields)
    return float(item.f[0]), float(item.loss), item.grams[:, 0, 0].copy()


def _evolve_ladder(
    family: NestedQuadratureFamily,
    degree_to_level: dict[int, int],
    degrees: Sequence[int],
    *,
    duration: float,
    dt: float,
    sample_dt: float,
    label: str,
) -> tuple[dict[str, np.ndarray], dict[int, PDEState], float]:
    levels = {degree: degree_to_level[degree] for degree in degrees}
    states = {
        degree: initialize(
            family.spec(level),
            family.quadrature(level),
        )
        for degree, level in levels.items()
    }
    steps = int(round(duration / dt))
    stride = int(round(sample_dt / dt))
    if (
        not np.isclose(steps * dt, duration)
        or not np.isclose(stride * dt, sample_dt)
        or stride < 1
    ):
        raise ValueError("duration and sample_dt must be multiples of dt")

    samples = steps // stride + 1
    times = np.arange(samples, dtype=float) * sample_dt
    f = {degree: np.empty(samples) for degree in degrees}
    loss = {degree: np.empty(samples) for degree in degrees}
    grams = {
        degree: np.empty((samples, family.spec(levels[degree]).depth_nodes + 1))
        for degree in degrees
    }

    def save(sample: int) -> None:
        for degree in degrees:
            level = levels[degree]
            value_f, value_loss, value_grams = _record_observation(
                states[degree],
                family.spec(level),
                family.quadrature(level),
            )
            f[degree][sample] = value_f
            loss[degree][sample] = value_loss
            grams[degree][sample] = value_grams

    save(0)
    sample = 1
    started = time.perf_counter()
    for step in range(1, steps + 1):
        for degree in degrees:
            level = levels[degree]
            states[degree] = _midpoint_step(
                states[degree],
                dt,
                family.spec(level),
                family.quadrature(level),
            )
            gc.collect()
        if step % stride == 0:
            save(sample)
            sample += 1
        if step % max(1, steps // 4) == 0:
            print(
                f"{label}: completed {step}/{steps} time steps",
                flush=True,
            )
    wall_seconds = time.perf_counter() - started

    arrays: dict[str, np.ndarray] = {"times": times}
    for degree in degrees:
        arrays[f"d{degree}_f"] = f[degree]
        arrays[f"d{degree}_loss"] = loss[degree]
        arrays[f"d{degree}_grams"] = grams[degree]
    return arrays, states, wall_seconds


def _evolve_single(
    spec: PDESpec,
    quadrature: Any,
    *,
    duration: float,
    dt: float,
    sample_dt: float,
) -> tuple[dict[str, np.ndarray], float]:
    state = initialize(spec, quadrature)
    steps = int(round(duration / dt))
    stride = int(round(sample_dt / dt))
    samples = steps // stride + 1
    times = np.arange(samples, dtype=float) * sample_dt
    f = np.empty(samples)
    loss = np.empty(samples)
    grams = np.empty((samples, spec.depth_nodes + 1))

    def save(sample: int) -> None:
        value_f, value_loss, value_grams = _record_observation(
            state,
            spec,
            quadrature,
        )
        f[sample] = value_f
        loss[sample] = value_loss
        grams[sample] = value_grams

    save(0)
    sample = 1
    started = time.perf_counter()
    for step in range(1, steps + 1):
        state = _midpoint_step(state, dt, spec, quadrature)
        gc.collect()
        if step % stride == 0:
            save(sample)
            sample += 1
    return {
        "times": times,
        "f": f,
        "loss": loss,
        "grams": grams,
    }, time.perf_counter() - started


def _dense_ensemble(
    *,
    activation: str,
    gamma: float,
    y: float,
    seeds: int,
    seed_start: int,
    n: int,
    depth: int,
    duration: float,
    dt: float,
    sample_dt: float,
    pde_depth_nodes: int,
) -> tuple[dict[str, np.ndarray], float]:
    if depth % pde_depth_nodes:
        raise ValueError("dense depth must be divisible by PDE depth nodes")
    indices = np.arange(
        0,
        depth + 1,
        depth // pde_depth_nodes,
        dtype=int,
    )
    steps = int(round(duration / dt))
    stride = int(round(sample_dt / dt))
    samples = steps // stride + 1
    times = np.arange(samples, dtype=float) * sample_dt
    all_f = np.empty((seeds, samples))
    all_grams = np.empty((seeds, samples, pde_depth_nodes + 1))
    started = time.perf_counter()

    for seed_offset in range(seeds):
        spec = ModelSpec(
            n=n,
            depth=depth,
            X=np.array([[1.0]]),
            y=np.array([y]),
            seed=seed_start + seed_offset,
            sigma_w=0.65,
            A=1.0,
            gamma=gamma,
            activation=activation,
        )
        state = initialize_dense(spec)
        sample = 0
        for step in range(steps + 1):
            if step % stride == 0:
                fields = forward_adjoint(state, spec)
                all_f[seed_offset, sample] = (
                    state.a @ fields.H[-1, :, 0] / n
                )
                all_grams[seed_offset, sample] = np.mean(
                    fields.H[indices, :, 0] ** 2,
                    axis=1,
                )
                sample += 1
            if step < steps:
                state = rk4_param_step(state, dt, spec)
        print(
            f"dense {activation}: completed seed "
            f"{seed_offset + 1}/{seeds}",
            flush=True,
        )
    loss = 0.5 * (all_f - y) ** 2
    return {
        "times": times,
        "f": all_f,
        "loss": loss,
        "grams": all_grams,
        "mean_f": np.mean(all_f, axis=0),
        "mean_loss": 0.5 * (np.mean(all_f, axis=0) - y) ** 2,
        "mean_grams": np.mean(all_grams, axis=0),
        "depth_indices": indices,
    }, time.perf_counter() - started


def _increments(values: np.ndarray) -> np.ndarray:
    return values - values[0:1]


def _scales(curves: Sequence[dict[str, np.ndarray]], y: float) -> dict[str, float]:
    return {
        "gram": max(
            0.05,
            *(
                float(np.max(np.abs(_increments(curve["grams"]))))
                for curve in curves
            ),
        ),
        "output": max(
            0.05,
            abs(y),
            *(
                float(np.max(np.abs(_increments(curve["f"]))))
                for curve in curves
            ),
        ),
        "loss": max(
            0.05,
            *(
                float(np.max(curve["loss"]))
                for curve in curves
            ),
        ),
    }


def _curve_distance(
    left: dict[str, np.ndarray],
    right: dict[str, np.ndarray],
    scales: dict[str, float],
) -> dict[str, float]:
    return {
        "gram": float(
            np.max(
                np.abs(
                    _increments(left["grams"])
                    - _increments(right["grams"])
                )
            )
            / scales["gram"]
        ),
        "output": float(
            np.max(
                np.abs(
                    _increments(left["f"])
                    - _increments(right["f"])
                )
            )
            / scales["output"]
        ),
        "loss": float(
            np.max(np.abs(left["loss"] - right["loss"]))
            / scales["loss"]
        ),
    }


def _trajectory_view(
    arrays: dict[str, np.ndarray],
    degree: int,
) -> dict[str, np.ndarray]:
    return {
        "times": arrays["times"],
        "f": arrays[f"d{degree}_f"],
        "loss": arrays[f"d{degree}_loss"],
        "grams": arrays[f"d{degree}_grams"],
    }


def _state_pair_error(
    low_state: PDEState,
    high_state: PDEState,
    low_quadrature: Any,
    high_quadrature: Any,
) -> dict[str, float]:
    low = low_state.c.shape[-1]
    difference = PDEState(
        B=high_state.B - low_state.B,
        a=high_state.a - low_state.a,
        c=high_state.c[..., :low] - low_state.c,
    )
    shadow = _norm_components(difference, low_quadrature)
    tail = high_state.c[..., low:]
    tail_norm = float(
        np.sqrt(
            max(
                float(
                    np.einsum(
                        "i,r,lirp,lirp->",
                        high_quadrature.base_weights,
                        high_quadrature.fast_weights,
                        tail,
                        tail,
                        optimize=True,
                    )
                    / high_state.c.shape[0]
                ),
                0.0,
            )
        )
    )
    return {
        "shadow_B": shadow.B,
        "shadow_a": shadow.a,
        "shadow_c": shadow.c,
        "shadow_total": shadow.total,
        "outgoing_tail": tail_norm,
        "projective_total": math.hypot(shadow.total, tail_norm),
    }


def _shell_summary(
    state: PDEState,
    spec: PDESpec,
    quadrature: Any,
) -> dict[str, Any]:
    velocity, fields = vector_field(state, spec, quadrature)
    degrees = np.asarray(
        [sum(index) for index in quadrature.multi_indices],
        dtype=int,
    )
    wb = quadrature.base_weights
    wf = quadrature.fast_weights
    pcoef = np.einsum(
        "ip,i,lim->lpm",
        quadrature.phi,
        wb,
        fields.p,
        optimize=True,
    )
    output: dict[str, Any] = {}
    for degree in sorted(set(degrees.tolist())):
        mask = degrees == degree
        count = int(np.sum(mask))
        c2 = float(
            np.einsum(
                "i,r,lirp,lirp->",
                wb,
                wf,
                state.c[..., mask],
                state.c[..., mask],
                optimize=True,
            )
            / state.c.shape[0]
        )
        cdot2 = float(
            np.einsum(
                "i,r,lirp,lirp->",
                wb,
                wf,
                velocity.c[..., mask],
                velocity.c[..., mask],
                optimize=True,
            )
            / state.c.shape[0]
        )
        h2 = float(np.mean(np.sum(fields.hcoef[:, mask, :] ** 2, axis=(1, 2))))
        p2 = float(np.mean(np.sum(pcoef[:, mask, :] ** 2, axis=(1, 2))))
        output[str(degree)] = {
            "mode_count": count,
            "c_norm": math.sqrt(max(c2, 0.0)),
            "cdot_norm": math.sqrt(max(cdot2, 0.0)),
            "hcoef_norm": math.sqrt(max(h2, 0.0)),
            "pcoef_norm": math.sqrt(max(p2, 0.0)),
            "c_rms_per_mode": math.sqrt(max(c2, 0.0) / count),
            "cdot_rms_per_mode": math.sqrt(max(cdot2, 0.0) / count),
            "hcoef_rms_per_mode": math.sqrt(max(h2, 0.0) / count),
            "pcoef_rms_per_mode": math.sqrt(max(p2, 0.0) / count),
        }
    return output


def _analyze_ladder(
    arrays: dict[str, np.ndarray],
    states: dict[int, PDEState],
    family: NestedQuadratureFamily,
    degree_to_level: dict[int, int],
    degrees: Sequence[int],
    *,
    y: float,
) -> dict[str, Any]:
    curves = [_trajectory_view(arrays, degree) for degree in degrees]
    scales = _scales(curves, y)
    reference_degree = degrees[-1]
    reference = _trajectory_view(arrays, reference_degree)
    to_reference = {
        str(degree): _curve_distance(
            _trajectory_view(arrays, degree),
            reference,
            scales,
        )
        for degree in degrees[:-1]
    }
    adjacent: dict[str, Any] = {}
    for low_degree, high_degree in zip(degrees, degrees[1:]):
        low_level = degree_to_level[low_degree]
        high_level = degree_to_level[high_degree]
        adjacent[f"{low_degree}_{high_degree}"] = {
            "observable": _curve_distance(
                _trajectory_view(arrays, low_degree),
                _trajectory_view(arrays, high_degree),
                scales,
            ),
            "final_state": _state_pair_error(
                states[low_degree],
                states[high_degree],
                family.quadrature(low_level),
                family.quadrature(high_level),
            ),
        }
    high_level = degree_to_level[reference_degree]
    return {
        "scales": scales,
        "reference_degree": reference_degree,
        "errors_to_reference": to_reference,
        "adjacent": adjacent,
        "reference_shells_final": _shell_summary(
            states[reference_degree],
            family.spec(high_level),
            family.quadrature(high_level),
        ),
        "reference_endpoint": {
            "f": float(reference["f"][-1]),
            "loss": float(reference["loss"][-1]),
            "gram_motion": float(
                np.max(np.abs(_increments(reference["grams"])))
            ),
        },
    }


def _dense_curve(
    arrays: dict[str, np.ndarray],
) -> dict[str, np.ndarray]:
    return {
        "times": arrays["times"],
        "f": arrays["mean_f"],
        "loss": arrays["mean_loss"],
        "grams": arrays["mean_grams"],
    }


def _per_seed_distance(
    left: dict[str, np.ndarray],
    right: dict[str, np.ndarray],
    scales: dict[str, float],
    y: float,
) -> dict[str, Any]:
    records = []
    for index in range(left["f"].shape[0]):
        lcurve = {
            "times": left["times"],
            "f": left["f"][index],
            "loss": 0.5 * (left["f"][index] - y) ** 2,
            "grams": left["grams"][index],
        }
        rcurve = {
            "times": right["times"],
            "f": right["f"][index],
            "loss": 0.5 * (right["f"][index] - y) ** 2,
            "grams": right["grams"][index],
        }
        records.append(_curve_distance(lcurve, rcurve, scales))
    result: dict[str, Any] = {}
    for name in ("gram", "output", "loss"):
        values = np.asarray([record[name] for record in records])
        result[name] = {
            "mean": float(np.mean(values)),
            "standard_error": float(
                np.std(values, ddof=1) / np.sqrt(values.size)
            ) if values.size > 1 else 0.0,
            "minimum": float(np.min(values)),
            "maximum": float(np.max(values)),
        }
    return result


def run(args: argparse.Namespace) -> tuple[dict[str, Any], dict[str, np.ndarray]]:
    if args.master_degree < args.degrees[-1]:
        raise ValueError("master_degree must cover every evolved degree")
    X = np.array([[1.0]])
    y_array = np.array([args.y])
    base_points = args.base_order ** 2
    template = PDESpec(
        X=X,
        y=y_array,
        basis_size=2,
        depth_nodes=args.N,
        base_points=base_points,
        fast_points=args.R,
        quadrature_seed=args.seed,
        sigma_w=0.65,
        A=1.0,
        gamma=1.0,
        activation="tanh",
    )

    all_arrays: dict[str, np.ndarray] = {}
    analyses: dict[str, Any] = {}
    wall: dict[str, float] = {}
    families: dict[str, NestedQuadratureFamily] = {}
    mappings: dict[str, dict[int, int]] = {}
    final_states: dict[str, dict[int, PDEState]] = {}

    for activation in args.activations:
        case_template = dataclasses.replace(template, activation=activation)
        family, degree_to_level = _odd_family(
            case_template,
            master_degree=args.master_degree,
            base_order=args.base_order,
        )
        print(
            f"starting {activation} odd ladder {args.degrees}",
            flush=True,
        )
        arrays, states, elapsed = _evolve_ladder(
            family,
            degree_to_level,
            args.degrees,
            duration=args.duration,
            dt=args.dt,
            sample_dt=args.sample_dt,
            label=activation,
        )
        families[activation] = family
        mappings[activation] = degree_to_level
        final_states[activation] = states
        wall[f"pde_{activation}"] = elapsed
        analyses[activation] = _analyze_ladder(
            arrays,
            states,
            family,
            degree_to_level,
            args.degrees,
            y=args.y,
        )
        for name, value in arrays.items():
            all_arrays[f"{activation}_{name}"] = value

    reference_degree = args.degrees[-1]
    kappa_init = None
    sine_arrays = None
    sine_reference = None
    baseline_curves: dict[str, dict[str, np.ndarray]] = {}
    if SINE_NAME in families and not args.skip_baselines:
        sine_family = families[SINE_NAME]
        sine_mapping = mappings[SINE_NAME]
        reference_level = sine_mapping[reference_degree]
        reference_spec = sine_family.spec(reference_level)
        reference_quadrature = sine_family.quadrature(reference_level)
        q = 0.65**2
        kappa_init = math.exp(-0.5 * OMEGA**2 * q)
        activation_energy = (
            1.0 - math.exp(-2.0 * OMEGA**2 * q)
        ) / (2.0 * OMEGA**2)
        kappa_rms = math.sqrt(activation_energy / q)
        for name, kappa in (
            ("linear_init_gain", kappa_init),
            ("linear_rms_gain", kappa_rms),
        ):
            spec = dataclasses.replace(
                reference_spec,
                activation="identity",
                gamma=kappa,
            )
            print(f"starting {name} kappa={kappa:.9f}", flush=True)
            curve, elapsed = _evolve_single(
                spec,
                reference_quadrature,
                duration=args.duration,
                dt=args.dt,
                sample_dt=args.sample_dt,
            )
            baseline_curves[name] = curve
            wall[f"pde_{name}"] = elapsed
            for key, value in curve.items():
                all_arrays[f"{name}_{key}"] = value

        sine_arrays = {
            name[len(f"{SINE_NAME}_"):]: value
            for name, value in all_arrays.items()
            if name.startswith(f"{SINE_NAME}_")
        }
        sine_reference = _trajectory_view(sine_arrays, reference_degree)
        baseline_scales = _scales(
            [sine_reference, *baseline_curves.values()],
            args.y,
        )
        analyses["gain_baselines"] = {
            "kappa_init": kappa_init,
            "kappa_rms": kappa_rms,
            "activation_energy": activation_energy,
            "linear_projection_energy": kappa_init**2 * q,
            "nonlinear_energy_fraction": (
                activation_energy - kappa_init**2 * q
            ) / activation_energy,
            "scales": baseline_scales,
            "distances_to_sine_reference": {
                name: _curve_distance(curve, sine_reference, baseline_scales)
                for name, curve in baseline_curves.items()
            },
        }

    if args.dense_seeds and sine_reference is not None and kappa_init is not None:
        dense_sine, elapsed = _dense_ensemble(
            activation=SINE_NAME,
            gamma=1.0,
            y=args.y,
            seeds=args.dense_seeds,
            seed_start=args.dense_seed_start,
            n=args.dense_width,
            depth=args.dense_depth,
            duration=args.duration,
            dt=args.dt,
            sample_dt=args.sample_dt,
            pde_depth_nodes=args.N,
        )
        wall["dense_sine"] = elapsed
        dense_linear, elapsed = _dense_ensemble(
            activation="identity",
            gamma=kappa_init,
            y=args.y,
            seeds=args.dense_seeds,
            seed_start=args.dense_seed_start,
            n=args.dense_width,
            depth=args.dense_depth,
            duration=args.duration,
            dt=args.dt,
            sample_dt=args.sample_dt,
            pde_depth_nodes=args.N,
        )
        wall["dense_linear_init_gain"] = elapsed
        for prefix, arrays in (
            ("dense_sine", dense_sine),
            ("dense_linear_init_gain", dense_linear),
        ):
            for name, value in arrays.items():
                all_arrays[f"{prefix}_{name}"] = value

        dense_sine_curve = _dense_curve(dense_sine)
        dense_linear_curve = _dense_curve(dense_linear)
        dense_scales = _scales(
            [
                dense_sine_curve,
                dense_linear_curve,
                sine_reference,
                *(
                    _trajectory_view(sine_arrays, degree)
                    for degree in args.degrees
                ),
            ],
            args.y,
        )
        analyses["dense_validation"] = {
            "config": {
                "seeds": args.dense_seeds,
                "seed_start": args.dense_seed_start,
                "width": args.dense_width,
                "depth": args.dense_depth,
            },
            "scales": dense_scales,
            "dense_linear_vs_sine_ensemble_mean": _curve_distance(
                dense_linear_curve,
                dense_sine_curve,
                dense_scales,
            ),
            "dense_linear_vs_sine_per_seed": _per_seed_distance(
                dense_linear,
                dense_sine,
                dense_scales,
                args.y,
            ),
            "pde_reference_vs_dense_sine": _curve_distance(
                sine_reference,
                dense_sine_curve,
                dense_scales,
            ),
            "pde_degree_vs_dense_sine": {
                str(degree): _curve_distance(
                    _trajectory_view(sine_arrays, degree),
                    dense_sine_curve,
                    dense_scales,
                )
                for degree in args.degrees
            },
        }

    script_path = Path(__file__).resolve()
    first_activation = args.activations[0]
    metadata = {
        "claim_scope": (
            "minimal scalar diagnostic; not a proof of the full "
            "four-label dense-limit conjecture"
        ),
        "model": {
            "X": X.tolist(),
            "y": y_array.tolist(),
            "sigma_w": 0.65,
            "A": 1.0,
            "gamma": 1.0,
        },
        "pde": {
            "degrees": list(args.degrees),
            "active_mode_counts": {
                str(degree): mappings[first_activation][degree]
                for degree in args.degrees
            },
            "master_degree": args.master_degree,
            "master_active_modes": mappings[first_activation][args.master_degree],
            "activations": list(args.activations),
            "N": args.N,
            "R": args.R,
            "base_order": args.base_order,
            "M": base_points,
            "seed": args.seed,
            "dt": args.dt,
            "sample_dt": args.sample_dt,
            "duration": args.duration,
            "integrator": "explicit midpoint",
            "parity_reduced": True,
        },
        "stress_activation": {
            "name": SINE_NAME,
            "formula": "sin(2.5 z)/2.5",
            "smooth": True,
            "odd": True,
            "bounded": True,
            "lipschitz_constant": 1.0,
        },
        "wall_seconds": wall,
        "script_sha256": _sha256(script_path),
        "canonical_solver_sha256": _sha256(
            CANONICAL_SOURCE / "dense_pde" / "operator_galerkin.py"
        ),
        "canonical_dense_sha256": _sha256(
            CANONICAL_SOURCE / "dense_reference" / "core.py"
        ),
    }
    summary = {
        "metadata": metadata,
        "analyses": analyses,
    }
    all_arrays["metadata_json"] = np.asarray(_canonical_json(metadata))
    return summary, all_arrays


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--degrees",
        type=_parse_degrees,
        default=(1, 3, 5, 7, 9, 11),
    )
    parser.add_argument(
        "--master-degree",
        type=int,
        choices=ODD_DEGREES,
        default=13,
    )
    parser.add_argument(
        "--activations",
        type=_parse_activations,
        default=("tanh", SINE_NAME),
    )
    parser.add_argument("--skip-baselines", action="store_true")
    parser.add_argument("--y", type=float, default=2.0)
    parser.add_argument("--N", type=int, default=4)
    parser.add_argument("--R", type=int, default=128)
    parser.add_argument("--base-order", type=int, default=14)
    parser.add_argument("--seed", type=int, default=20260725)
    parser.add_argument("--duration", type=float, default=2.0)
    parser.add_argument("--dt", type=float, default=0.025)
    parser.add_argument("--sample-dt", type=float, default=0.05)
    parser.add_argument("--dense-seeds", type=int, default=8)
    parser.add_argument("--dense-seed-start", type=int, default=71000)
    parser.add_argument("--dense-width", type=int, default=128)
    parser.add_argument("--dense-depth", type=int, default=16)
    parser.add_argument("--output", type=Path, required=True)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    summary, arrays = run(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    npz_path = args.output.with_suffix(".npz")
    np.savez_compressed(npz_path, **arrays)
    print(
        json.dumps(
            {
                "output": str(args.output),
                "npz": str(npz_path),
                "wall_seconds": summary["metadata"]["wall_seconds"],
                "key_results": {
                    "tanh_adjacent": summary["analyses"].get(
                        "tanh", {}
                    ).get("adjacent"),
                    "sine_errors_to_reference": summary["analyses"].get(
                        SINE_NAME, {}
                    ).get("errors_to_reference"),
                    "gain_baselines": summary["analyses"].get(
                        "gain_baselines", {}
                    ).get("distances_to_sine_reference"),
                    "dense_validation": summary["analyses"].get(
                        "dense_validation"
                    ),
                },
            },
            indent=2,
            sort_keys=True,
        ),
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
