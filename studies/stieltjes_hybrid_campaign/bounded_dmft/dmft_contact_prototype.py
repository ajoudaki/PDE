#!/usr/bin/env python3
"""Stage-0 initialization and one-step response/contact prototype.

This file deliberately does not implement or launch a positive-time DMFT
fixed point.  It checks the bounded initialization decomposition and the
first strict-subdiagonal responses under the frozen left-contact convention.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import torch


HERE = Path(__file__).resolve().parent
PARENT_PROTOCOL = HERE.parent / "PROTOCOL.md"
PARENT_PROTOCOL_SHA256 = (
    "d1e75ad896a3572f77b9bc6ec68a7047219a075645b87d44c520d677fc3b153a"
)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_parent_protocol() -> None:
    observed = file_sha256(PARENT_PROTOCOL)
    if observed != PARENT_PROTOCOL_SHA256:
        raise RuntimeError(
            "parent protocol hash mismatch: "
            f"expected {PARENT_PROTOCOL_SHA256}, observed {observed}"
        )


def normal_cdf(value: torch.Tensor) -> torch.Tensor:
    return 0.5 * (1.0 + torch.erf(value / math.sqrt(2.0)))


def normal_icdf(probability: torch.Tensor) -> torch.Tensor:
    return math.sqrt(2.0) * torch.erfinv(2.0 * probability - 1.0)


def antithetic_sobol_uniforms(
    sample_count: int,
    dimension: int,
    seed: int,
) -> torch.Tensor:
    if sample_count <= 0 or sample_count % 2:
        raise ValueError("sample_count must be a positive even integer")
    if dimension <= 0:
        raise ValueError("dimension must be positive")
    engine = torch.quasirandom.SobolEngine(
        dimension=dimension,
        scramble=True,
        seed=seed,
    )
    base = engine.draw(sample_count // 2, dtype=torch.float64)
    values = torch.cat((base, 1.0 - base), dim=0)
    tiny = torch.finfo(torch.float64).eps
    return values.clamp(min=tiny, max=1.0 - tiny)


def gaussian_from_uniform(uniform: torch.Tensor) -> torch.Tensor:
    return normal_icdf(uniform)


def truncated_gaussian_from_uniform(
    uniform: torch.Tensor,
    cutoff: float,
) -> torch.Tensor:
    if cutoff <= 0:
        raise ValueError("cutoff must be positive")
    a = torch.tensor(float(cutoff), dtype=torch.float64)
    lower = normal_cdf(-a)
    upper = normal_cdf(a)
    return normal_icdf(lower + (upper - lower) * uniform)


def conditional_second_moment(cutoff: float) -> float:
    a = float(cutoff)
    mass = math.erf(a / math.sqrt(2.0))
    density = math.exp(-0.5 * a * a) / math.sqrt(2.0 * math.pi)
    return 1.0 - 2.0 * a * density / mass


def exact_initialization(cutoff: float) -> dict[str, float]:
    m2 = conditional_second_moment(cutoff)
    values = {
        "m2": m2,
        "kernel_a": 27.0,
        "kernel_W": 36.0 * m2,
        "kernel_u": 48.0 * m2,
    }
    values["kernel"] = (
        values["kernel_a"] + values["kernel_W"] + values["kernel_u"]
    )
    values["A10_density"] = 4.0
    values["B10_density_limit"] = 12.0 + 28.0 * m2
    return values


def top_share(values: torch.Tensor, fraction: float = 0.001) -> dict[str, float]:
    if values.ndim != 1:
        raise ValueError("tail diagnostic expects a vector")
    nonnegative = values.abs()
    total = torch.sum(nonnegative)
    count = max(1, math.ceil(fraction * nonnegative.numel()))
    largest = torch.topk(nonnegative, k=count).values
    if float(total) == 0.0:
        return {"top_fraction_share": 0.0, "largest_single_share": 0.0}
    return {
        "top_fraction_share": float(torch.sum(largest) / total),
        "largest_single_share": float(torch.max(largest) / total),
    }


def run_contact_audit(
    *,
    cutoff: float = 3.0,
    intervals: int = 64,
    horizon: float = 0.005,
    sample_count: int = 4096,
    first_seed: int = 2026081401,
    second_seed: int = 2026081402,
) -> dict:
    """Evaluate only t=0 observables and the first response contact."""

    verify_parent_protocol()
    if intervals != 64 or sample_count != 4096 or cutoff != 3.0:
        raise ValueError("Stage-0 frozen contact cell is A=3, L=64, S=4096")
    step = horizon / intervals
    exact = exact_initialization(cutoff)
    m2 = exact["m2"]

    first_uniform = antithetic_sobol_uniforms(sample_count, 2, first_seed)
    u0 = gaussian_from_uniform(first_uniform[:, 0])
    xi0 = math.sqrt(12.0 * m2) * gaussian_from_uniform(first_uniform[:, 1])
    q0 = xi0

    # Frozen left-contact first-layer step:
    # U_1 = U_0 + 2h U_0 Q_0.
    u1 = u0 + 2.0 * step * u0 * q0
    d_u1_sq_d_xi0 = 4.0 * step * u0 * u1
    response_a10_density = float(torch.mean(d_u1_sq_d_xi0) / step)

    second_uniform = antithetic_sobol_uniforms(sample_count, 2, second_seed)
    a0 = truncated_gaussian_from_uniform(second_uniform[:, 0], cutoff)
    eta0 = math.sqrt(3.0) * gaussian_from_uniform(second_uniform[:, 1])
    eta1 = eta0  # Initialization covariance Phi_1(t,s)=3 is rank one.

    # The strict subdiagonal source derivative perturbs eta_0 while holding
    # eta_1 fixed.  This off-support functional derivative is exactly the
    # response object required by the causal DMFT.
    c10 = 3.0 + response_a10_density
    readout1 = a0 + step * eta0.square()
    z1 = eta1 + 2.0 * step * c10 * a0 * eta0
    d_readout1 = 2.0 * step * eta0
    d_z1 = 2.0 * step * c10 * a0
    d_g2_1 = 2.0 * (d_readout1 * z1 + readout1 * d_z1)
    response_b10_density = float(torch.mean(d_g2_1) / step)

    # Initialization kernel components.  Independent species are never
    # paired for the middle-layer product.
    z0 = eta0
    kernel_a_samples = z0.pow(4)
    b2_samples = (a0 * z0).square()
    u4_samples = u0.pow(4)
    uq2_samples = (u0 * q0).square()
    sampled_kernel_a = float(torch.mean(kernel_a_samples))
    sampled_kernel_W = float(4.0 * torch.mean(b2_samples) * torch.mean(u4_samples))
    sampled_kernel_u = float(4.0 * torch.mean(uq2_samples))
    sampled_kernel = sampled_kernel_a + sampled_kernel_W + sampled_kernel_u

    expected_components = [
        exact["kernel_a"],
        exact["kernel_W"],
        exact["kernel_u"],
    ]
    sampled_components = [sampled_kernel_a, sampled_kernel_W, sampled_kernel_u]
    relative_components = [
        abs(observed - expected) / expected
        for observed, expected in zip(sampled_components, expected_components)
    ]
    relative_kernel = abs(sampled_kernel - exact["kernel"]) / exact["kernel"]

    exact_b_limit = exact["B10_density_limit"]
    gates = {
        "components_within_0p5_percent": max(relative_components) <= 0.005,
        "kernel_within_0p25_percent": relative_kernel <= 0.0025,
        "A_contact": abs(response_a10_density - 4.0) <= 0.02,
        "B_contact": abs(response_b10_density - exact_b_limit)
        <= 0.05 * exact_b_limit,
        "response_free_ablation_fails": exact["A10_density"] != 0.0
        and exact["B10_density_limit"] != 0.0,
    }

    return {
        "schema_version": 1,
        "status": "stage0_contact_only_no_positive_time_dmft",
        "parent_protocol_sha256": PARENT_PROTOCOL_SHA256,
        "configuration": {
            "cutoff": cutoff,
            "intervals": intervals,
            "horizon": horizon,
            "step": step,
            "sample_count": sample_count,
            "first_seed": first_seed,
            "second_seed": second_seed,
            "dtype": "float64",
            "readout_variance_renormalized": False,
        },
        "exact": exact,
        "sampled": {
            "kernel_a": sampled_kernel_a,
            "kernel_W": sampled_kernel_W,
            "kernel_u": sampled_kernel_u,
            "kernel": sampled_kernel,
            "A10_density": response_a10_density,
            "B10_density": response_b10_density,
        },
        "relative_errors": {
            "components": relative_components,
            "kernel": relative_kernel,
            "B_contact_against_h_to_zero_limit": abs(
                response_b10_density - exact_b_limit
            )
            / exact_b_limit,
        },
        "tail_diagnostics": {
            "z4": top_share(kernel_a_samples),
            "b2": top_share(b2_samples),
            "u4": top_share(u4_samples),
            "uq2": top_share(uq2_samples),
        },
        "gates": gates,
        "all_contact_and_initialization_gates_passed": all(gates.values()),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run_contact_audit()
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
