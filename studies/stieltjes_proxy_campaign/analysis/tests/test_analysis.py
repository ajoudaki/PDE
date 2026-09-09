from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import numpy as np

from analysis.bootstrap import (
    PointBootstrap,
    bootstrap_point,
    simultaneous_log_band,
)
from analysis.comparison import (
    BracketComparison,
    compare_proxy_hierarchy,
)
from analysis.reference_data import (
    ReferencePoint,
    estimate_curve,
    load_reference_run,
    sha256,
)
from analysis.verdict import (
    DecisionThresholds,
    decide_bracket,
    decide_protocol_bracket,
)
from analysis.width import (
    extrapolate_widths,
    width_sensitivity_summary,
)
from proxy.inventory import (
    EvaluatedFamily,
)


def synthetic_physical_point(width: int = 64, pairs: int = 12) -> ReferencePoint:
    time = np.linspace(0.0, 1.0, 81)
    base_output = 0.8 * time
    outputs = np.empty((len(time), 2 * pairs))
    kernels = np.empty_like(outputs)
    for pair in range(pairs):
        pair_shift = 0.015 * (pair - (pairs - 1) / 2) / pairs
        for member in range(2):
            anti = (1 if member == 0 else -1) * 0.003 * np.exp(-3.0 * time)
            output = base_output + pair_shift * time * (1.0 - 0.3 * time) + anti
            outputs[:, 2 * pair + member] = output
            kernels[:, 2 * pair + member] = 2.0 + 0.5 * output + 0.02 * pair_shift
    weighted = (1.0 - outputs) * kernels
    loss = np.square(1.0 - outputs)
    nodes = np.array([0.0, 0.2, 0.4, 0.6])
    mean_output = outputs.mean(axis=1)
    node_pair_output = np.empty((len(nodes), pairs))
    node_pair_weighted = np.empty_like(node_pair_output)
    node_pair_kernel = np.empty_like(node_pair_output)
    for pair in range(pairs):
        po = outputs[:, 2 * pair : 2 * pair + 2].mean(axis=1)
        pw = weighted[:, 2 * pair : 2 * pair + 2].mean(axis=1)
        pk = kernels[:, 2 * pair : 2 * pair + 2].mean(axis=1)
        node_time = np.interp(nodes, mean_output, time)
        node_pair_output[:, pair] = np.interp(node_time, time, po)
        node_pair_weighted[:, pair] = np.interp(node_time, time, pw)
        node_pair_kernel[:, pair] = np.interp(node_time, time, pk)
    arrays = {
        "output_nodes": nodes,
        "raw_time": time,
        "raw_trajectory_output": outputs,
        "raw_trajectory_kernel": kernels,
        "raw_trajectory_weighted_kernel": weighted,
        "raw_trajectory_loss": loss,
        "node_pair_output": node_pair_output,
        "node_pair_weighted_kernel": node_pair_weighted,
        "node_pair_kernel": node_pair_kernel,
    }
    return ReferencePoint(
        point_id=f"synthetic_n{width}",
        group="synthetic",
        mode="physical",
        width=width,
        antithetic_pairs=pairs,
        target=1.0,
        family_key=None,
        family_parameters=(),
        config={"monotonic_tolerance": 1e-10},
        diagnostics={"maximum_output_variance_at_nodes": 1e-4},
        arrays=arrays,
        evidence_admissible=False,
        arrays_path=Path("synthetic.npz"),
        arrays_sha256="synthetic",
    )


def test_physical_estimator_and_lineage_bootstrap_are_reproducible() -> None:
    point = synthetic_physical_point()
    central = estimate_curve(point)
    expected_numerator = np.mean(
        point.arrays["raw_trajectory_weighted_kernel"], axis=1
    )
    mean_output = np.mean(point.arrays["raw_trajectory_output"], axis=1)
    expected = np.interp(point.output_nodes, mean_output, expected_numerator) / (
        1.0 - point.output_nodes
    )
    np.testing.assert_allclose(central["kernel"], expected, rtol=2e-14, atol=2e-14)

    first = bootstrap_point(point, replicates=80, seed=123, confidence=0.9)
    second = bootstrap_point(point, replicates=80, seed=123, confidence=0.9)
    np.testing.assert_array_equal(first.samples, second.samples)
    assert first.samples.shape == (80, len(point.output_nodes))
    assert np.all(first.band.lower <= first.band.estimate)
    assert np.all(first.band.estimate <= first.band.upper)
    assert first.diagnostics["bootstrap_invalid_replicates"] == 0
    assert first.diagnostics["leakage"] == {"applicable": False}


def test_loader_verifies_npz_and_scientific_gate(tmp_path: Path) -> None:
    point = synthetic_physical_point(pairs=4)
    reference = tmp_path / "reference"
    config_dir = reference / "configs"
    run_dir = reference / "runs" / "fixture"
    config_dir.mkdir(parents=True)
    run_dir.mkdir(parents=True)
    npz = run_dir / "p.npz"
    np.savez_compressed(npz, **point.arrays)
    config = {
        "points": [{
            "id": "p",
            "mode": "physical",
            "width": 64,
            "antithetic_pairs": 4,
            "target": 1.0,
            "monotonic_tolerance": 1e-10,
            "analysis": {
                "comparison_group": "canonical",
                "family_key": "canonical",
                "family_parameters": {},
            },
        }]
    }
    config_path = config_dir / "fixture.json"
    config_path.write_text(json.dumps(config))
    summary = {
        "status": "complete_validation_only",
        "scientific_evidence_admissible": False,
        "config_name": config_path.name,
        "points": [{
            "id": "p",
            "status": "complete_validation_only",
            "arrays_file": npz.name,
            "arrays_sha256": sha256(npz),
            "diagnostics": {},
        }],
    }
    summary_path = run_dir / "summary.json"
    summary_path.write_text(json.dumps(summary))
    loaded = load_reference_run(summary_path)
    assert len(loaded.points) == 1
    assert loaded.points[0].group == "canonical"
    try:
        load_reference_run(summary_path, require_scientific=True)
    except PermissionError:
        pass
    else:  # pragma: no cover
        raise AssertionError("validation-only data passed the scientific gate")


def make_width_bootstrap(width: int, seed: int) -> PointBootstrap:
    output = np.linspace(0.0, 0.8, 9)
    infinity = 3.0 + output**2 / (1.0 + output**2)
    estimate = infinity + (2.0 + 0.2 * output) / width
    rng = np.random.default_rng(seed)
    samples = estimate[None, :] * np.exp(
        rng.normal(scale=2e-4, size=(100, len(output)))
    )
    band = simultaneous_log_band(estimate, samples, confidence=0.9)
    return PointBootstrap(
        point_id=f"n{width}",
        width=width,
        output=output,
        band=band,
        samples=samples,
        diagnostics={
            "maximum_relative_standard_error": 1e-4,
            "maximum_relative_jensen_gap": 1e-4,
        },
    )


def test_width_models_recover_known_inverse_n_limit() -> None:
    points = [make_width_bootstrap(width, width) for width in (64, 128, 256, 512)]
    estimate = extrapolate_widths(points, model="inv_n_all")
    truth = 3.0 + estimate.output**2 / (1.0 + estimate.output**2)
    np.testing.assert_allclose(estimate.band.estimate, truth, rtol=2e-14, atol=2e-14)
    sensitivity = width_sensitivity_summary((
        estimate,
        extrapolate_widths(points, model="inv_sqrt_n_all"),
        extrapolate_widths(points, model="inv_n_top3"),
        extrapolate_widths(points, model="top_width_direct"),
    ))
    assert sensitivity["maximum_pairwise_log_disagreement"] > 0.0


def test_proxy_comparison_tracks_rational_and_taylor_levels() -> None:
    output = np.linspace(0.0, 0.8, 9)
    exact = 2.0 + output**2 / (1.0 + output**2)
    samples = exact[None, :] * np.exp(
        np.linspace(-1e-5, 1e-5, 60)[:, None]
    )
    band = simultaneous_log_band(exact, samples, confidence=0.9)

    class Reference:
        pass

    reference = Reference()
    reference.output = output
    reference.band = band
    family = EvaluatedFamily(
        key="synthetic_delta",
        observable="K",
        baseline=Fraction(2),
        moments=(Fraction(1), Fraction(1), Fraction(1)),
        parameters=(),
        drives_training=True,
        training_target=Fraction(1),
        coordinate_scope="synthetic output",
        source_paths=(),
        source_sha256=(),
    )
    comparison = compare_proxy_hierarchy(reference, family, reference_model="synthetic")
    assert len(comparison.rational_levels) >= 3
    assert len(comparison.taylor_controls) == 3
    assert comparison.rational_levels[-1].sup_log_kernel_error < 1e-14
    # The exact one-atom curve lies on the lower boundary, so a nonzero
    # confidence band cannot certify strict containment; fail closed.
    assert comparison.brackets[-1].containment_status == "inconclusive"


def thresholds() -> DecisionThresholds:
    return DecisionThresholds(
        confidence=0.9,
        maximum_reference_to_bracket_width_ratio=0.25,
        maximum_width_model_log_disagreement=0.01,
        maximum_width_fit_relative_residual=0.01,
        maximum_bootstrap_invalid_fraction=0.05,
        maximum_relative_standard_error=0.01,
        maximum_relative_jensen_gap=0.01,
        maximum_transverse_leakage=None,
    )


def test_verdict_fails_closed_before_scientific_discriminator() -> None:
    bracket = BracketComparison(
        information_moments=3,
        lower_name="lower",
        upper_name="upper",
        sup_log_width=0.1,
        reference_sup_log_band_width=0.01,
        reference_to_bracket_width_ratio=0.1,
        containment_status="pass",
        definite_escape_direction="none",
        maximum_definite_escape=-1.0,
    )
    common = dict(
        thresholds=thresholds(),
        bootstrap_confidence=0.9,
        bootstrap_invalid_fraction=0.0,
        maximum_relative_standard_error=0.001,
        maximum_relative_jensen_gap=0.001,
        maximum_width_model_log_disagreement=0.001,
        maximum_width_fit_relative_residual=0.001,
        transverse_leakage=None,
    )
    assert decide_bracket(bracket, evidence_admissible=True, **common).status == "pass"
    assert decide_bracket(bracket, evidence_admissible=False, **common).status == "inconclusive"
    failed = BracketComparison(**{
        **bracket.__dict__,
        "containment_status": "fail",
        "definite_escape_direction": "above",
        "maximum_definite_escape": 0.02,
    })
    assert decide_bracket(failed, evidence_admissible=True, **common).status == "fail"
    assert decide_protocol_bracket(
        failed,
        validity_gates={"solver": True, "width": True},
        two_largest_escape_directions=("above", "above"),
    ).status == "fail"
    assert decide_protocol_bracket(
        failed,
        validity_gates={"solver": True, "width": True},
        two_largest_escape_directions=("none", "above"),
    ).status == "inconclusive"
