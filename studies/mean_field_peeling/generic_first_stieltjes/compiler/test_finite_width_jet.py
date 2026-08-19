import importlib.util
from pathlib import Path

import numpy as np

from .finite_width_jet import feature_jet


def polynomial_oracle(coefficients):
    coefficients = tuple(float(value) for value in coefficients)

    def derivative(order, x):
        values = list(coefficients)
        for _ in range(order):
            values = [k * values[k] for k in range(1, len(values))]
        out = np.zeros_like(x, dtype=np.float64)
        for coefficient in reversed(values):
            out = out * x + coefficient
        return out

    return derivative


def _load_quadratic_reference():
    path = (
        Path(__file__).resolve().parents[2]
        / "quadratic_compiler"
        / "finite_width_jet_reference.py"
    )
    spec = importlib.util.spec_from_file_location("quadratic_jet_reference", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_constant_activation_is_exactly_linear_in_feature_time() -> None:
    result = feature_jet(7, 1.0, polynomial_oracle([2.0]), 19)
    assert np.allclose(result.derivatives[2:], 0.0, atol=0.0, rtol=0.0)
    assert result.derivatives[1] == 4.0


def test_generic_oracle_matches_quadratic_reference_seedwise() -> None:
    reference = _load_quadratic_reference()
    for width in (2, 5):
        for seed in (0, 7):
            generic = feature_jet(
                width, 1.0, polynomial_oracle([0.0, 0.0, 1.0]), seed
            ).ordinary_coefficients
            accepted = reference.feature_jet(width, 3, 1.0, seed)
            assert np.allclose(generic, accepted, atol=1.0e-10, rtol=1.0e-12)


def test_linear_exact_expectation_target_is_48() -> None:
    # The exact finite-width annealed identity is E[D_n^3 f_n]=48+60/n.
    # This small deterministic seed panel is only a smoke test of the oracle;
    # exactness of the target is proved algebraically in README.md.
    width = 32
    values = np.asarray(
        [
            feature_jet(width, 1.0, polynomial_oracle([0.0, 1.0]), seed).derivatives[3]
            for seed in range(128)
        ]
    )
    target = 48.0 + 60.0 / width
    assert abs(float(values.mean()) - target) < 3.0
