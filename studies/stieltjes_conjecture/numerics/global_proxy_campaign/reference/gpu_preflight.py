#!/usr/bin/env python3
"""Read-only/tiny-allocation CUDA preflight; never a scientific run."""

from __future__ import annotations

import json
import platform
import sys
import time

import torch


MINIMUM_FREE_GIB = 18.0
REQUIRED_DEVICES = 2
MATRIX_SIZE = 512


def main() -> int:
    result: dict[str, object] = {
        "status": "gpu_preflight_only_not_scientific_evidence",
        "python": sys.version,
        "platform": platform.platform(),
        "torch": torch.__version__,
        "torch_cuda_build": torch.version.cuda,
        "cuda_available": torch.cuda.is_available(),
        "device_count": torch.cuda.device_count(),
        "required_devices": REQUIRED_DEVICES,
        "minimum_free_gib": MINIMUM_FREE_GIB,
        "devices": [],
    }
    passed = bool(torch.cuda.is_available() and torch.cuda.device_count() >= REQUIRED_DEVICES)
    if torch.cuda.is_available():
        for index in range(torch.cuda.device_count()):
            device = torch.device(f"cuda:{index}")
            torch.cuda.set_device(device)
            properties = torch.cuda.get_device_properties(device)
            free, total = torch.cuda.mem_get_info(device)
            started = time.monotonic()
            # The preflight allocation is deliberately tiny (~6 MiB total in
            # float64) compared with a 24-GiB RTX 3090.
            generator = torch.Generator(device=device)
            generator.manual_seed(202608130400 + index)
            x = torch.randn(
                (MATRIX_SIZE, MATRIX_SIZE),
                generator=generator,
                device=device,
                dtype=torch.float64,
            )
            y = x @ x.transpose(0, 1)
            checksum = float(torch.sum(y).item())
            torch.cuda.synchronize(device)
            elapsed = time.monotonic() - started
            finite = bool(torch.isfinite(y).all().item())
            item = {
                "index": index,
                "name": properties.name,
                "capability": [properties.major, properties.minor],
                "total_memory_gib": total / 2**30,
                "free_memory_gib": free / 2**30,
                "float64_matmul_seconds": elapsed,
                "finite": finite,
                "checksum": checksum,
                "peak_allocated_mib": torch.cuda.max_memory_allocated(device) / 2**20,
            }
            result["devices"].append(item)
            passed = passed and finite and (free / 2**30 >= MINIMUM_FREE_GIB)
            del x, y
            torch.cuda.empty_cache()
    result["passed"] = passed
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if passed else 2


if __name__ == "__main__":
    raise SystemExit(main())

