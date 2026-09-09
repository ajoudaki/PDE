"""Exact inventory of every accepted family usable by the proxy campaign.

The evaluators read the checked artifacts in place and transform their jets
with exact rational arithmetic.  They do not copy large coefficient tables,
fit trajectories, or inspect any future finite-width result.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from pathlib import Path
from typing import Callable, Mapping

from .exact_series import (
    as_fraction,
    companion_moments,
    output_kernel_moments,
)


REPO_ROOT = Path(__file__).resolve().parents[5]
COMPILER = REPO_ROOT / "studies/mean_field_peeling/quadratic_compiler"
THEORY = REPO_ROOT / "studies/stieltjes_conjecture/theory"


@dataclass(frozen=True)
class EvaluatedFamily:
    key: str
    observable: str
    baseline: Fraction
    moments: tuple[Fraction, ...]
    parameters: tuple[tuple[str, Fraction], ...]
    drives_training: bool
    training_target: Fraction | None
    coordinate_scope: str
    source_paths: tuple[str, ...]
    source_sha256: tuple[str, ...]
    caveats: tuple[str, ...] = ()

    def exact_record(self) -> dict:
        return {
            "key": self.key,
            "observable": self.observable,
            "baseline": str(self.baseline),
            "moments": [str(value) for value in self.moments],
            "parameters": {name: str(value) for name, value in self.parameters},
            "drives_training": self.drives_training,
            "training_target": (
                None if self.training_target is None else str(self.training_target)
            ),
            "coordinate_scope": self.coordinate_scope,
            "source_paths": list(self.source_paths),
            "source_sha256": list(self.source_sha256),
            "caveats": list(self.caveats),
        }


@dataclass(frozen=True)
class FamilySpec:
    key: str
    title: str
    observable: str
    parameters: tuple[str, ...]
    exact_domain: str
    moment_count: int
    drives_training: bool
    target_rule: Callable[[Mapping[str, Fraction]], Fraction | None]
    coordinate_scope: str
    source_paths: tuple[Path, ...]
    evaluator: Callable[[Mapping[str, Fraction]], tuple[Fraction, tuple[Fraction, ...], tuple[str, ...]]]

    def public_record(self) -> dict:
        return {
            "key": self.key,
            "title": self.title,
            "observable": self.observable,
            "parameters": list(self.parameters),
            "exact_domain": self.exact_domain,
            "moment_count": self.moment_count,
            "hierarchy_levels_including_ntk": self.moment_count + 1,
            "drives_training": self.drives_training,
            "training_target_rule": (
                "parameter-dependent; inspect evaluate_family"
                if self.key == "variance_homotopy"
                else "1" if self.drives_training else "use the associated output kernel"
            ),
            "coordinate_scope": self.coordinate_scope,
            "source_paths": [str(path.relative_to(REPO_ROOT)) for path in self.source_paths],
        }


@lru_cache(maxsize=None)
def _json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _poly(coefficients: list[str] | tuple[int, ...], x: Fraction) -> Fraction:
    value = Fraction(0)
    for coefficient in reversed(coefficients):
        value = value * x + as_fraction(coefficient)
    return value


def _require(parameters: Mapping[str, Fraction], names: tuple[str, ...]) -> tuple[Fraction, ...]:
    missing = set(names) - set(parameters)
    extra = set(parameters) - set(names)
    if missing or extra:
        raise ValueError(f"parameter mismatch: missing={sorted(missing)}, extra={sorted(extra)}")
    return tuple(parameters[name] for name in names)


def _canonical(_: Mapping[str, Fraction]) -> tuple[Fraction, tuple[Fraction, ...], tuple[str, ...]]:
    document = _json(THEORY / "certificates_order11.json")
    return (
        as_fraction(document["kappa_K_even_coefficients"][0]),
        tuple(as_fraction(value) for value in document["mu"]),
        (),
    )


@lru_cache(maxsize=1)
def _variance_rows() -> tuple[tuple[int, ...], ...]:
    """Read the accepted Wick-sector matrix without executing its module."""
    path = THEORY / "sector_total_nonnegativity.py"
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "C" for target in node.targets
        ):
            value = ast.literal_eval(node.value)
            return tuple(tuple(int(entry) for entry in row) for row in value)
    raise RuntimeError("accepted sector matrix C was not found")


def _variance(parameters: Mapping[str, Fraction]) -> tuple[Fraction, tuple[Fraction, ...], tuple[str, ...]]:
    (alpha,) = _require(parameters, ("alpha",))
    if alpha < 0:
        raise ValueError("variance alpha must be nonnegative")
    # C[r][p] is [alpha^(p+1)] F_alpha^(2r+1).  Dividing F by
    # alpha makes the normalized derivative sum_p C[r][p] alpha^p.
    derivatives = {
        2 * r + 1: _poly(list(row), alpha)
        for r, row in enumerate(_variance_rows())
    }
    baseline, moments = output_kernel_moments(derivatives)
    return baseline, moments, (
        "This is the normalized kernel kappa_alpha(z)=K_alpha(alpha*z)/alpha.",
        "For alpha>0, physical label one is the normalized target z*=1/alpha; at alpha=0 there is no finite physical target in this chart.",
        "At alpha=0 it is the exact singular Lambert-W calibration boundary; at alpha=1 it is canonical.",
    )


def _campaign1_jets(observable: str, lam: Fraction) -> dict[int, Fraction]:
    path = COMPILER / "campaign1/results_order9_q2_order8.json"
    records = _json(path)["observables"][observable]["jets"]
    return {
        int(record["order"]): _poly(record["lambda_coefficients"], lam)
        for record in records
    }


def _relative_metric_output(parameters: Mapping[str, Fraction]):
    (lam,) = _require(parameters, ("lambda",))
    if lam < 0:
        raise ValueError("metric lambda must be nonnegative")
    jets = _campaign1_jets("f", lam)
    return (*output_kernel_moments({k: v for k, v in jets.items() if k % 2}), ())


def _relative_metric_q2(parameters: Mapping[str, Fraction]):
    (lam,) = _require(parameters, ("lambda",))
    if lam < 0:
        raise ValueError("metric lambda must be nonnegative")
    feature = _campaign1_jets("f", lam)
    q2 = _campaign1_jets("q2", lam)
    baseline, moments = companion_moments(
        {k: v for k, v in feature.items() if k % 2},
        {k: v for k, v in q2.items() if k % 2 == 0},
    )
    return baseline, moments, (
        "This is the independent second-hidden companion N2, not a training kernel.",
        "The first-hidden Q1 curve is derived directly from the output kernel and is not an independent family.",
    )


def _two_input(channel: str, parameters: Mapping[str, Fraction]):
    (t,) = _require(parameters, ("t",))
    if not 0 <= t <= 1:
        raise ValueError("two-input t=theta^2 must lie in [0,1]")
    document = _json(COMPILER / "campaign2/certificates_order7.json")
    key = "plus" if channel == "plus" else "minus_raw"
    if channel == "minus" and t == 1:
        raise ValueError(
            "the physical opposite-label channel collapses at t=1; its normalized h extension is not a physical target-one flow"
        )
    derivatives = {
        int(order): _poly(coefficients, t)
        for order, coefficients in document["jets"][key].items()
    }
    baseline, moments = output_kernel_moments(derivatives)
    caveats = () if channel == "plus" else (
        "These are raw physical-channel moments, not the normalized h moments used to certify the singular t=1 endpoint.",
        "The admissible physical domain is 0 <= t < 1.",
    )
    return baseline, moments, caveats


def _centered(parameters: Mapping[str, Fraction]):
    (c,) = _require(parameters, ("c",))
    if not 0 <= c <= 2:
        raise ValueError("centering c must lie in [0,2]")
    t = 1 - c
    document = _json(COMPILER / "campaign3/certificates_order7.json")
    derivatives = {
        int(order): _poly(coefficients, t)
        for order, coefficients in document["jets_t"].items()
    }
    return (*output_kernel_moments(derivatives), ())


def _block_metric(parameters: Mapping[str, Fraction]):
    alpha, beta = _require(parameters, ("alpha", "beta"))
    if alpha < 0 or beta < 0:
        raise ValueError("block metrics alpha,beta must be nonnegative")
    document = _json(COMPILER / "campaign4/results_order9.json")
    derivatives: dict[int, Fraction] = {}
    for record in document["jets"]:
        order = int(record["order"])
        if order % 2 == 0:
            continue
        derivatives[order] = sum(
            as_fraction(term["value"])
            * alpha ** int(term["alpha_power"])
            * beta ** int(term["beta_power"])
            for term in record["monomials"]
        )
    return (*output_kernel_moments(derivatives), ())


def _three_input(parameters: Mapping[str, Fraction]):
    (rho,) = _require(parameters, ("rho",))
    if not Fraction(-1, 2) <= rho <= 1:
        raise ValueError("three-input equicorrelation rho must lie in [-1/2,1]")
    document = _json(
        COMPILER / "campaign5_b3/frozen/stage_b_connected_order5.json"
    )
    derivatives = {
        order: _poly(coefficients, rho) / (3 ** (order + 1))
        for order, coefficients in enumerate(document["raw_rho"])
        if order % 2 == 1
    }
    baseline, moments = output_kernel_moments(derivatives)
    return baseline, moments, (
        "Only mu_0 and mu_1 are available; no ordinary 2x2 Hankel test exists for this family.",
    )


def _specs() -> tuple[FamilySpec, ...]:
    canonical_certificate = THEORY / "certificates_order11.json"
    sector_source = THEORY / "sector_total_nonnegativity.py"
    variance_audit = THEORY / "finite_variance_hankel_audit.py"
    boundary_audit = THEORY / "variance_homotopy_boundary_audit.py"
    c1_results = COMPILER / "campaign1/results_order9_q2_order8.json"
    c1_certificate = COMPILER / "campaign1/hankel_certificates_order9_q2_order8.json"
    c2_certificate = COMPILER / "campaign2/certificates_order7.json"
    c3_certificate = COMPILER / "campaign3/certificates_order7.json"
    c4_results = COMPILER / "campaign4/results_order9.json"
    c4_certificate = COMPILER / "campaign4/certificates_order9.json"
    c5_results = COMPILER / "campaign5_b3/frozen/stage_b_connected_order5.json"
    c5_certificate = COMPILER / "campaign5_b3/certificates_lower_moments.json"
    return (
        FamilySpec(
            "canonical", "Canonical one-input kernel", "K", (), "singleton", 5,
            True, lambda _: Fraction(1), "physical output y", (canonical_certificate,), _canonical,
        ),
        FamilySpec(
            "variance_homotopy", "Normalized middle-weight variance homotopy", "kappa_alpha",
            ("alpha",), "alpha >= 0", 5, True,
            lambda p: None if p["alpha"] == 0 else 1 / p["alpha"],
            "normalized output z=y/alpha",
            (sector_source, variance_audit, boundary_audit), _variance,
        ),
        FamilySpec(
            "relative_metric_output", "Relative block-metric ray", "K_lambda",
            ("lambda",), "lambda >= 0", 4, True, lambda _: Fraction(1), "physical output y",
            (c1_results, c1_certificate), _relative_metric_output,
        ),
        FamilySpec(
            "relative_metric_q2", "Second-hidden companion on the metric ray", "N2_lambda",
            ("lambda",), "lambda >= 0", 4, False, lambda _: None, "physical output y",
            (c1_results, c1_certificate), _relative_metric_q2,
        ),
        FamilySpec(
            "two_input_equal", "Two-input equal-label channel", "K_plus",
            ("t",), "0 <= t=theta^2 <= 1", 3, True, lambda _: Fraction(1), "symmetry-channel output g_plus",
            (c2_certificate,), lambda p: _two_input("plus", p),
        ),
        FamilySpec(
            "two_input_opposite", "Two-input opposite-label physical channel", "K_minus",
            ("t",), "0 <= t=theta^2 < 1", 3, True, lambda _: Fraction(1), "symmetry-channel output g_minus",
            (c2_certificate,), lambda p: _two_input("minus", p),
        ),
        FamilySpec(
            "centered_activation", "Centered first-hidden quadratic activation", "K_c",
            ("c",), "0 <= c <= 2", 3, True, lambda _: Fraction(1), "physical output y",
            (c3_certificate,), _centered,
        ),
        FamilySpec(
            "independent_block_metric", "Independent hidden-block metric quadrant", "K_alpha_beta",
            ("alpha", "beta"), "alpha,beta >= 0", 4, True, lambda _: Fraction(1), "physical output y",
            (c4_results, c4_certificate), _block_metric,
        ),
        FamilySpec(
            "three_input_equal", "Three-input equal-label equicorrelation channel", "K_3",
            ("rho",), "-1/2 <= rho <= 1", 2, True, lambda _: Fraction(1), "symmetric output g_3",
            (c5_results, c5_certificate), _three_input,
        ),
    )


@lru_cache(maxsize=1)
def _spec_by_key() -> dict[str, FamilySpec]:
    return {spec.key: spec for spec in _specs()}


def family_inventory() -> tuple[dict, ...]:
    """Return immutable public metadata, not an exploratory parameter grid."""
    return tuple(spec.public_record() for spec in _specs())


def evaluate_family(
    key: str, **parameters: int | str | float | Fraction
) -> EvaluatedFamily:
    """Evaluate one preselected rational parameter point exactly."""
    try:
        spec = _spec_by_key()[key]
    except KeyError as exc:
        raise KeyError(f"unknown proxy family {key!r}") from exc
    rational_parameters = {name: as_fraction(value) for name, value in parameters.items()}
    baseline, moments, caveats = spec.evaluator(rational_parameters)
    if len(moments) != spec.moment_count:
        raise ArithmeticError(
            f"{key} produced {len(moments)} moments, expected {spec.moment_count}"
        )
    paths = spec.source_paths
    return EvaluatedFamily(
        key=key,
        observable=spec.observable,
        baseline=baseline,
        moments=moments,
        parameters=tuple((name, rational_parameters[name]) for name in spec.parameters),
        drives_training=spec.drives_training,
        training_target=spec.target_rule(rational_parameters),
        coordinate_scope=spec.coordinate_scope,
        source_paths=tuple(str(path.relative_to(REPO_ROOT)) for path in paths),
        source_sha256=tuple(_sha256(path) for path in paths),
        caveats=caveats,
    )
