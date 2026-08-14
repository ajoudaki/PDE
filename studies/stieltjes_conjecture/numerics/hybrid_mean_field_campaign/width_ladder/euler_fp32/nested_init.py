#!/usr/bin/env python3
"""Shape-independent nested Gaussian initialization rounded once to FP32."""

from __future__ import annotations

import hashlib
import math
import struct

import numpy as np


MASK = (1 << 64) - 1
GOLDEN = 0x9E3779B97F4A7C15
MIX1 = 0xBF58476D1CE4E5B9
MIX2 = 0x94D049BB133111EB
PAIR_SALT = 0xD2B74407B1CE6E93
SECOND_SALT = 0xCA5A826395121157
ROW_BASE = 1 << 32
TWO53 = float(1 << 53)
DOMAIN = {
    "a": 0x243F6A8885A308D3,
    "u": 0x13198A2E03707344,
    "W": 0xA4093822299F31D0,
    "monitor": 0x082EFA98EC4E6C89,
}


def u64(value: int) -> np.uint64:
    return np.uint64(value & MASK)


def splitmix(values: np.ndarray) -> np.ndarray:
    values = np.asarray(values, dtype=np.uint64)
    with np.errstate(over="ignore"):
        z = values + u64(GOLDEN)
        z = (z ^ (z >> u64(30))) * u64(MIX1)
        z = (z ^ (z >> u64(27))) * u64(MIX2)
        return z ^ (z >> u64(31))


def _base(seed: int, lineage: int, domain: str) -> int:
    return (
        int(seed)
        ^ DOMAIN[domain]
        ^ ((int(lineage) * PAIR_SALT) & MASK)
    ) & MASK


def normal(counters: np.ndarray, *, seed: int, lineage: int, domain: str) -> np.ndarray:
    counters = np.asarray(counters, dtype=np.uint64)
    base = _base(seed, lineage, domain)
    with np.errstate(over="ignore"):
        x1 = counters * u64(GOLDEN) + u64(base)
        x2 = counters * u64(MIX1) + u64(base ^ SECOND_SALT)
    b1 = splitmix(x1)
    b2 = splitmix(x2)
    u1 = ((b1 >> u64(11)).astype(np.float64) + 0.5) / TWO53
    u2 = ((b2 >> u64(11)).astype(np.float64) + 0.5) / TWO53
    return np.sqrt(-2.0 * np.log(u1)) * np.cos(2.0 * math.pi * u2)


def vector_fp32(width: int, *, seed: int, lineage: int, domain: str) -> np.ndarray:
    counters = np.arange(width, dtype=np.uint64)
    return normal(counters, seed=seed, lineage=lineage, domain=domain).astype(
        np.float32
    )


def matrix_fp32(
    width: int,
    *,
    seed: int,
    lineage: int,
    row_block: int = 128,
) -> np.ndarray:
    result = np.empty((width, width), dtype=np.float32)
    columns = np.arange(width, dtype=np.uint64)[None, :]
    for start in range(0, width, row_block):
        stop = min(width, start + row_block)
        rows = np.arange(start, stop, dtype=np.uint64)[:, None]
        counters = rows * u64(ROW_BASE) + columns
        result[start:stop] = normal(
            counters, seed=seed, lineage=lineage, domain="W"
        ).astype(np.float32)
    return result


def state_digest(seed: int, lineage: int, width: int, a, u, W) -> str:
    digest = hashlib.sha256()
    digest.update(b"nested-euler-fp32-state-v1\0")
    digest.update(struct.pack("<QQQ", int(seed), int(lineage), int(width)))
    for label, array in ((b"a", a), (b"u", u), (b"W", W)):
        digest.update(label + b"\0")
        digest.update(np.asarray(array, dtype="<f4", order="C").tobytes(order="C"))
    return digest.hexdigest()


def prefix_digest(seed: int, lineage: int, size: int, a, u, W) -> str:
    """Width-independent digest of a declared coordinate prefix."""

    if size > len(a) or size > W.shape[0] or size > W.shape[1]:
        raise ValueError("prefix exceeds generated state")
    digest = hashlib.sha256()
    digest.update(b"nested-euler-fp32-prefix-v1\0")
    digest.update(struct.pack("<QQQ", int(seed), int(lineage), int(size)))
    for label, array in (
        (b"a", a[:size]),
        (b"u", u[:size]),
        (b"W", W[:size, :size]),
    ):
        digest.update(label + b"\0")
        digest.update(np.asarray(array, dtype="<f4", order="C").tobytes(order="C"))
    return digest.hexdigest()


def generate_lineage(
    width: int,
    *,
    seed: int,
    lineage: int,
    row_block: int = 128,
    prefix_sizes: tuple[int, ...] = (),
) -> tuple[np.ndarray, np.ndarray, np.ndarray, str, dict[int, str]]:
    if width < 1 or width >= ROW_BASE:
        raise ValueError("width is outside the frozen coordinate range")
    a = vector_fp32(width, seed=seed, lineage=lineage, domain="a")
    u = vector_fp32(width, seed=seed, lineage=lineage, domain="u")
    W = matrix_fp32(
        width, seed=seed, lineage=lineage, row_block=row_block
    )
    prefixes = {
        int(size): prefix_digest(seed, lineage, int(size), a, u, W)
        for size in prefix_sizes
    }
    return a, u, W, state_digest(seed, lineage, width, a, u, W), prefixes


def monitor_coordinates(
    sample_size: int,
    *,
    seed: int,
    extent: int = 2048,
) -> tuple[np.ndarray, np.ndarray, str]:
    """Fixed top-left representative coordinates shared by every width."""

    if sample_size < 1 or sample_size > extent * extent:
        raise ValueError("invalid monitor sample size")
    selected: set[tuple[int, int]] = set()
    counter = 0
    base = _base(seed, 0, "monitor")
    while len(selected) < sample_size:
        values = np.arange(counter, counter + 2 * sample_size, dtype=np.uint64)
        mixed = splitmix(values + u64(base))
        for value in mixed.tolist():
            row = int(value & 0xFFFFFFFF) % extent
            col = int((value >> 32) & 0xFFFFFFFF) % extent
            selected.add((row, col))
            if len(selected) == sample_size:
                break
        counter += 2 * sample_size
    pairs = np.asarray(sorted(selected), dtype=np.int64)
    payload = np.asarray(pairs, dtype="<i8", order="C").tobytes(order="C")
    digest = hashlib.sha256(
        b"euler-fp32-W-monitor-v1\0"
        + struct.pack("<QQQ", int(seed), int(extent), int(sample_size))
        + payload
    ).hexdigest()
    return pairs[:, 0], pairs[:, 1], digest
