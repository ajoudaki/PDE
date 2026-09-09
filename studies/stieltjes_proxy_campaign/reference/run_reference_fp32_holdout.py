#!/usr/bin/env python3
"""Validation-only float32 wrapper for the side-conversation width holdout."""

from pathlib import Path

import torch

import canonical_model
import reference_engine
import run_reference as runner


_ORIGINAL_DTYPE = runner._dtype


def _validation_dtype(name: str) -> torch.dtype:
    if name == "float32":
        return torch.float32
    return _ORIGINAL_DTYPE(name)


runner._dtype = _validation_dtype
runner.SOURCE_FILES = (*runner.SOURCE_FILES, Path(__file__).resolve())


_ORIGINAL_GENERATOR = canonical_model.generate_antithetic_state


def _float64_draw_then_cast(
    width: int,
    pair_count: int,
    seed_base: int,
    *,
    device: torch.device,
    dtype: torch.dtype,
    pair_offset: int = 0,
    microcanonical_readout: bool = False,
):
    """Match the historical float64 Gaussian stream before float32 evolution."""

    if dtype != torch.float32:
        return _ORIGINAL_GENERATOR(
            width,
            pair_count,
            seed_base,
            device=device,
            dtype=dtype,
            pair_offset=pair_offset,
            microcanonical_readout=microcanonical_readout,
        )
    state64, init64 = _ORIGINAL_GENERATOR(
        width,
        pair_count,
        seed_base,
        device=device,
        dtype=torch.float64,
        pair_offset=pair_offset,
        microcanonical_readout=microcanonical_readout,
    )
    state32 = canonical_model.State(
        state64.a.to(dtype=torch.float32),
        state64.W.to(dtype=torch.float32),
        state64.u.to(dtype=torch.float32),
    )
    initial32 = canonical_model.observables(state32)
    return state32, {
        "initial_output": initial32.output,
        "initial_kernel": initial32.kernel,
        "projection_relative_norm": init64["projection_relative_norm"].to(
            dtype=torch.float32
        ),
    }


reference_engine.generate_antithetic_state = _float64_draw_then_cast


if __name__ == "__main__":
    raise SystemExit(runner.main())
