"""Serialization-only wrapper for the frozen H3 curvature extension.

The frozen runner completed its full calculation and wrote the raw panel, then
failed because ``numpy.bool_`` is not JSON serializable.  This wrapper was
frozen before inspecting any raw numerical value.  It reruns the unchanged
calculation while teaching the JSON encoder only how to convert NumPy scalar
types.  It also verifies that the regenerated raw hash is identical.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

from studies.mean_field_peeling.generic_first_stieltjes.depth_order5_scalar.multi_observable.audit import (
    run_h3_curvature_extension as frozen,
)


HERE = Path(__file__).resolve().parent
RAW = HERE / "H3_NORMALIZED_SINE_CURVATURE_EXTENSION_RAW.npz"
EXPECTED_RAW_SHA256 = "2d2329246d15f1884458c39cae2897e06776fd3aad24d3875c21468175797ad0"
ORIGINAL_DUMPS = json.dumps


def scalar_default(value):
    if isinstance(value, np.bool_):
        return bool(value)
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    raise TypeError(f"Object of type {type(value).__name__} is not JSON serializable")


def safe_dumps(*args, **kwargs):
    kwargs.setdefault("default", scalar_default)
    return ORIGINAL_DUMPS(*args, **kwargs)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run():
    frozen.json.dumps = safe_dumps
    result = frozen.run()
    if digest(RAW) != EXPECTED_RAW_SHA256:
        raise RuntimeError("deterministic rerun changed the pre-serialization raw panel")
    result["runner_serialization_failure"] = (
        "the frozen extension completed and wrote raw data, then failed because "
        "numpy.bool_ is not JSON serializable"
    )
    result["serialization_wrapper"] = Path(__file__).name
    result_path = HERE / "H3_NORMALIZED_SINE_CURVATURE_EXTENSION_RESULT.json"
    result_path.write_text(
        ORIGINAL_DUMPS(result, indent=2, sort_keys=True, default=scalar_default) + "\n"
    )
    return result


if __name__ == "__main__":
    print(ORIGINAL_DUMPS(run(), indent=2, sort_keys=True, default=scalar_default))
