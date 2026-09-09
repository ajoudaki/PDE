#!/usr/bin/env python3
"""Stateless, coordinate-indexed Gaussian initialization for the width ladder.

The generator is intentionally independent of tensor shape.  A matrix entry is
addressed by its ordered coordinate pair, not by a row-major stride involving
the requested width.  Therefore every smaller-width draw is a bitwise prefix of
every larger-width draw for the same campaign seed and lineage.

This is a reproducible counter-based pseudorandom construction, not a source of
cryptographic randomness.  SplitMix64 is used as a bijective bit mixer and two
independently salted outputs are mapped to one normal with Box--Muller.
"""

from __future__ import annotations

import math
import hashlib
import struct
from dataclasses import dataclass

import numpy as np
import torch


_MASK_INT = (1 << 64) - 1
_GOLDEN = 0x9E3779B97F4A7C15
_MIX1 = 0xBF58476D1CE4E5B9
_MIX2 = 0x94D049BB133111EB
_PAIR_SALT = 0xD2B74407B1CE6E93
_SECOND_SALT = 0xCA5A826395121157
_ROW_BASE = 1 << 32
_TWO53 = float(1 << 53)

_DOMAIN_SALTS = {
    "a": 0x243F6A8885A308D3,
    "u": 0x13198A2E03707344,
    "W": 0xA4093822299F31D0,
}


def _as_u64(value: int) -> np.uint64:
    return np.uint64(value & _MASK_INT)


def _splitmix64(values: np.ndarray) -> np.ndarray:
    """Vectorized SplitMix64 with intentional unsigned wraparound."""

    values = np.asarray(values, dtype=np.uint64)
    with np.errstate(over="ignore"):
        z = values + _as_u64(_GOLDEN)
        z = (z ^ (z >> _as_u64(30))) * _as_u64(_MIX1)
        z = (z ^ (z >> _as_u64(27))) * _as_u64(_MIX2)
        return z ^ (z >> _as_u64(31))


def _uniform_open(bits: np.ndarray) -> np.ndarray:
    """Map the high 53 bits to the open interval (0, 1)."""

    mantissa = (bits >> _as_u64(11)).astype(np.float64)
    return (mantissa + 0.5) / _TWO53


def _base_key(seed: int, lineage: int, domain: str) -> int:
    if domain not in _DOMAIN_SALTS:
        raise ValueError(f"unknown RNG domain {domain!r}")
    if lineage < 0:
        raise ValueError("lineage must be nonnegative")
    return (
        int(seed)
        ^ _DOMAIN_SALTS[domain]
        ^ ((int(lineage) * _PAIR_SALT) & _MASK_INT)
    ) & _MASK_INT


def normal_from_counters(
    counters: np.ndarray,
    *,
    seed: int,
    lineage: int,
    domain: str,
) -> np.ndarray:
    """Return deterministic standard normals for arbitrary uint64 counters."""

    c = np.asarray(counters, dtype=np.uint64)
    base = _base_key(seed, lineage, domain)
    with np.errstate(over="ignore"):
        x1 = c * _as_u64(_GOLDEN) + _as_u64(base)
        x2 = c * _as_u64(_MIX1) + _as_u64(base ^ _SECOND_SALT)
    u1 = _uniform_open(_splitmix64(x1))
    u2 = _uniform_open(_splitmix64(x2))
    return np.sqrt(-2.0 * np.log(u1)) * np.cos(2.0 * math.pi * u2)


def vector_normal(
    width: int,
    *,
    seed: int,
    lineage: int,
    domain: str,
) -> np.ndarray:
    if width < 1:
        raise ValueError("width must be positive")
    if width >= _ROW_BASE:
        raise ValueError("width exceeds the frozen 32-bit coordinate range")
    counters = np.arange(width, dtype=np.uint64)
    return normal_from_counters(
        counters, seed=seed, lineage=lineage, domain=domain
    )


def matrix_normal(
    width: int,
    *,
    seed: int,
    lineage: int,
    row_block: int = 256,
) -> np.ndarray:
    """Create a nested ``width x width`` matrix in bounded row blocks."""

    if width < 1:
        raise ValueError("width must be positive")
    if width >= _ROW_BASE:
        raise ValueError("width exceeds the frozen 32-bit coordinate range")
    if row_block < 1:
        raise ValueError("row_block must be positive")
    result = np.empty((width, width), dtype=np.float64)
    columns = np.arange(width, dtype=np.uint64)[None, :]
    for start in range(0, width, row_block):
        stop = min(width, start + row_block)
        rows = np.arange(start, stop, dtype=np.uint64)[:, None]
        counters = rows * _as_u64(_ROW_BASE) + columns
        result[start:stop] = normal_from_counters(
            counters, seed=seed, lineage=lineage, domain="W"
        )
    return result


@dataclass(frozen=True)
class InitialControls:
    lineage_ids: np.ndarray
    total: np.ndarray
    components: np.ndarray


def generate_nested_antithetic_state(
    width: int,
    lineage_ids: list[int] | np.ndarray,
    seed: int,
    *,
    device: torch.device,
    dtype: torch.dtype = torch.float64,
    row_block: int = 256,
    return_digests: bool = False,
):
    """Build ordinary Gaussian states followed by adjacent readout antithetics.

    The return type is the canonical model's ``State`` class, imported lazily to
    keep the RNG module independently testable.
    """

    if dtype != torch.float64:
        raise ValueError("the frozen width ladder requires float64")
    ids = np.asarray(lineage_ids, dtype=np.int64)
    if ids.ndim != 1 or ids.size < 1:
        raise ValueError("lineage_ids must be a nonempty vector")
    if np.any(ids < 0) or len(np.unique(ids)) != len(ids):
        raise ValueError("lineage_ids must be distinct and nonnegative")

    # Local import avoids making this low-level module depend on a mutable
    # sys.path at import time.
    from width_engine import canonical_model

    base_a = []
    base_u = []
    base_W = []
    digests: list[str] = []
    for lineage in ids.tolist():
        a_np = vector_normal(width, seed=seed, lineage=lineage, domain="a")
        u_np = vector_normal(width, seed=seed, lineage=lineage, domain="u")
        W_np = matrix_normal(
            width, seed=seed, lineage=lineage, row_block=row_block
        )
        digest = hashlib.sha256()
        digest.update(b"nested-width-initial-state-v1\0")
        digest.update(struct.pack("<QQQ", int(seed), int(lineage), int(width)))
        for label, array in ((b"a", a_np), (b"u", u_np), (b"W", W_np)):
            digest.update(label + b"\0")
            digest.update(np.asarray(array, dtype="<f8", order="C").tobytes(order="C"))
        digests.append(digest.hexdigest())
        base_a.append(torch.from_numpy(a_np).to(device=device, dtype=dtype))
        base_u.append(torch.from_numpy(u_np).to(device=device, dtype=dtype))
        base_W.append(torch.from_numpy(W_np).to(device=device, dtype=dtype))

    a0 = torch.stack(base_a)
    u0 = torch.stack(base_u)
    W0 = torch.stack(base_W)
    a = torch.stack((a0, -a0), dim=1).reshape(2 * len(ids), width)
    u = torch.stack((u0, u0), dim=1).reshape(2 * len(ids), width)
    W = torch.stack((W0, W0), dim=1).reshape(2 * len(ids), width, width)
    state = canonical_model.State(a=a, W=W, u=u)
    if return_digests:
        return state, np.asarray(digests, dtype="S64")
    return state


def exact_initial_component_means(width: int) -> np.ndarray:
    if width < 1:
        raise ValueError("width must be positive")
    inv_n = 1.0 / float(width)
    return np.array(
        [27.0 + 288.0 * inv_n, 36.0 + 384.0 * inv_n, 48.0 + 672.0 * inv_n],
        dtype=np.float64,
    )


def exact_initial_total_mean(width: int) -> float:
    if width < 1:
        raise ValueError("width must be positive")
    return 111.0 + 1344.0 / float(width)
