"""One-run Cauchy/shadow ledger for the odd Hermite neural-PDE ladder.

This diagnostic co-evolves the degree-3, degree-5, and degree-7 Galerkin
systems on literal-prefix, parity-paired quadrature.  It measures the two
terms in the projective error decomposition:

* the actual accumulated outgoing state tail;
* the propagated low-state shadow between adjacent, separately evolved
  truncations.

It also records the instantaneous low feedback commutator and the actual
output/Gram Cauchy gap.  No scientific vector field is reimplemented here.
"""

from __future__ import annotations

import argparse
import gc
import hashlib
import json
import math
from pathlib import Path
import sys
import time
from typing import Any, Iterable

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
AUDIT_SOURCE = ROOT / "pde_proof_obligation_audit" / "source"
CANONICAL_SOURCE = ROOT / "activation_linearity_smoking_gun" / "source" / "src"
for source in (ROOT, AUDIT_SOURCE, CANONICAL_SOURCE):
    if str(source) not in sys.path:
        sys.path.insert(0, str(source))

import run_study as common  # noqa: E402
from cross_p import _norm_components  # noqa: E402
from dense_pde.operator_galerkin import (  # noqa: E402
    PDESpec,
    PDEState,
    initialize,
    observe,
    vector_field,
)
from targeted_tail_commutator import (  # noqa: E402
    PROTOCOL_PATH,
    _midpoint_step,
    _odd_family,
)


LEVELS = (24, 80, 200)  # complete active odd modes through degrees 3, 5, 7
PAIRS = ((24, 80), (80, 200))


def _parse_checkpoints(value: str) -> tuple[float, ...]:
    result = tuple(float(item) for item in value.split(","))
    if (
        not result
        or result[0] <= 0.0
        or any(right <= left for left, right in zip(result, result[1:]))
    ):
        raise argparse.ArgumentTypeError(
            "checkpoints must be strictly increasing positive times"
        )
    return result


def _state_difference(
    left: PDEState,
    right: PDEState,
    quadrature: Any,
) -> dict[str, float]:
    values = _norm_components(
        PDEState(
            B=left.B - right.B,
            a=left.a - right.a,
            c=left.c - right.c,
        ),
        quadrature,
    )
    return {
        "B": values.B,
        "a": values.a,
        "c": values.c,
        "total": values.total,
    }


def _projected_state_view(state: PDEState, level: int) -> PDEState:
    return PDEState(B=state.B, a=state.a, c=state.c[..., :level])


def _projected_velocity_difference(
    high_velocity: PDEState,
    low_velocity: PDEState,
    level: int,
    quadrature: Any,
) -> dict[str, float]:
    return _state_difference(
        _projected_state_view(high_velocity, level),
        low_velocity,
        quadrature,
    )


def _tail_norm(state: PDEState, level: int, quadrature: Any) -> float:
    wb = quadrature.base_weights
    wf = quadrature.fast_weights
    tail = state.c[..., level:]
    return float(
        np.sqrt(
            max(
                float(
                    np.einsum(
                        "i,r,lirp,lirp->",
                        wb,
                        wf,
                        tail,
                        tail,
                        optimize=True,
                    )
                    / state.c.shape[0]
                ),
                0.0,
            )
        )
    )


def _observable_distance(
    left: Any,
    right: Any,
    protocol: dict[str, Any],
) -> dict[str, float]:
    f = float(np.linalg.norm(left.f - right.f)) / float(
        protocol["norms"]["S_f"]
    )
    gram = float(
        np.max(
            np.linalg.norm(
                (left.grams - right.grams).reshape(
                    left.grams.shape[0], -1
                ),
                axis=1,
            )
        )
    ) / float(protocol["norms"]["S_G"])
    return {"f": f, "gram": gram, "max": max(f, gram)}


def _feedback(
    high_state: PDEState,
    high_velocity: PDEState,
    low: int,
    family: Any,
) -> dict[str, float]:
    projected = _projected_state_view(high_state, low)
    closed_velocity, fields = vector_field(
        projected, family.spec(low), family.quadrature(low)
    )
    del fields
    result = _projected_velocity_difference(
        high_velocity,
        closed_velocity,
        low,
        family.quadrature(low),
    )
    del closed_velocity
    gc.collect()
    return result


def _record_checkpoint(
    states: dict[int, PDEState],
    family: Any,
    protocol: dict[str, Any],
) -> dict[str, Any]:
    observations: dict[int, Any] = {}
    feedback: dict[str, dict[str, float]] = {}

    # Process levels serially so high-dimensional velocity arrays never stack.
    for level in LEVELS:
        velocity, fields = vector_field(
            states[level], family.spec(level), family.quadrature(level)
        )
        observations[level] = observe(
            states[level], family.spec(level), family.quadrature(level), fields
        )
        del fields
        if level in (80, 200):
            low = 24 if level == 80 else 80
            feedback[f"{low}_{level}"] = _feedback(
                states[level], velocity, low, family
            )
        del velocity
        gc.collect()

    pairs: dict[str, Any] = {}
    for low, high in PAIRS:
        low_view = _projected_state_view(states[high], low)
        shadow = _state_difference(
            low_view, states[low], family.quadrature(low)
        )
        outgoing = _tail_norm(
            states[high], low, family.quadrature(high)
        )
        obs = _observable_distance(
            observations[low], observations[high], protocol
        )
        pairs[f"{low}_{high}"] = {
            "outgoing_state_tail": outgoing,
            "low_state_shadow": shadow,
            "feedback": feedback[f"{low}_{high}"],
            "observable_gap": obs,
        }

    levels: dict[str, Any] = {}
    for level in LEVELS:
        item = observations[level]
        levels[str(level)] = {
            "f": item.f.tolist(),
            "loss": float(item.loss),
            "grams": item.grams.tolist(),
            "theta_min": float(item.theta_min),
            "loss_dot": float(item.loss_dot),
        }
    return {"levels": levels, "pairs": pairs}


def _derived(
    checkpoints: np.ndarray,
    records: list[dict[str, Any]],
) -> dict[str, Any]:
    times = np.concatenate(([0.0], checkpoints))
    result: dict[str, Any] = {}
    for low, high in PAIRS:
        tag = f"{low}_{high}"
        r = np.asarray(
            [0.0]
            + [item["pairs"][tag]["feedback"]["total"] for item in records]
        )
        l1 = float(np.trapezoid(r, times))
        final = records[-1]["pairs"][tag]
        tail = float(final["outgoing_state_tail"])
        shadow = float(final["low_state_shadow"]["total"])
        result[tag] = {
            "feedback_L1_trapezoid": l1,
            "effective_shadow_gain": (
                float("nan") if l1 == 0.0 else shadow / l1
            ),
            "final_projective_state_error": math.hypot(tail, shadow),
            "final_observable_gap": float(final["observable_gap"]["max"]),
            "max_projective_state_error": max(
                math.hypot(
                    float(item["pairs"][tag]["outgoing_state_tail"]),
                    float(item["pairs"][tag]["low_state_shadow"]["total"]),
                )
                for item in records
            ),
            "max_observable_gap": max(
                float(item["pairs"][tag]["observable_gap"]["max"])
                for item in records
            ),
        }

    lower = result["24_80"]
    upper = result["80_200"]
    result["ratios_degree7_over_degree5"] = {
        "final_projective_state_error": (
            upper["final_projective_state_error"]
            / lower["final_projective_state_error"]
        ),
        "max_projective_state_error": (
            upper["max_projective_state_error"]
            / lower["max_projective_state_error"]
        ),
        "final_observable_gap": (
            upper["final_observable_gap"] / lower["final_observable_gap"]
        ),
        "max_observable_gap": (
            upper["max_observable_gap"] / lower["max_observable_gap"]
        ),
        "effective_shadow_gain": (
            upper["effective_shadow_gain"]
            / lower["effective_shadow_gain"]
        ),
    }
    return result


def run(args: argparse.Namespace) -> dict[str, Any]:
    protocol = json.loads(PROTOCOL_PATH.read_text())
    model = common._canonical_model(protocol)
    template = PDESpec(
        X=model["X"],
        y=model["y"],
        basis_size=LEVELS[-1],
        depth_nodes=args.N,
        base_points=args.base_order**4,
        fast_points=args.R,
        quadrature_seed=args.seed,
        sigma_w=model["sigma_w"],
        A=model["A"],
        gamma=model["gamma"],
        activation=model["activation"],
    )
    family, _ = _odd_family(
        template, max_degree=7, base_order=args.base_order
    )
    states = {
        level: initialize(family.spec(level), family.quadrature(level))
        for level in LEVELS
    }

    current = 0.0
    tolerance = 128 * np.finfo(float).eps * max(1.0, args.checkpoints[-1])
    records: list[dict[str, Any]] = []
    started = time.perf_counter()
    for checkpoint in args.checkpoints:
        while current < checkpoint - tolerance:
            step = min(args.dt, checkpoint - current)
            for level in LEVELS:
                new_state = _midpoint_step(
                    states[level],
                    step,
                    family.spec(level),
                    family.quadrature(level),
                )
                del states[level]
                states[level] = new_state
                gc.collect()
            current += step
        records.append(_record_checkpoint(states, family, protocol))

    metadata = {
        "seed": int(args.seed),
        "N": int(args.N),
        "R": int(args.R),
        "base_order": int(args.base_order),
        "M": int(args.base_order**4),
        "dt": float(args.dt),
        "integrator": "explicit midpoint",
        "checkpoints": list(args.checkpoints),
        "levels": list(LEVELS),
        "pairs": [list(pair) for pair in PAIRS],
        "wall_seconds": time.perf_counter() - started,
        "protocol_sha256": hashlib.sha256(PROTOCOL_PATH.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "claim_scope": (
            "single-seed, coupled finite-level Cauchy/shadow diagnostic; "
            "not an asymptotic convergence proof"
        ),
    }
    return {
        "metadata": metadata,
        "records": records,
        "derived": _derived(np.asarray(args.checkpoints), records),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20260723)
    parser.add_argument("--N", type=int, default=1)
    parser.add_argument("--R", type=int, default=512)
    parser.add_argument("--base-order", type=int, default=8)
    parser.add_argument("--dt", type=float, default=0.025)
    parser.add_argument(
        "--checkpoints",
        type=_parse_checkpoints,
        default=(0.125, 0.25),
    )
    parser.add_argument("--output", type=Path, required=True)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = run(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["derived"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
