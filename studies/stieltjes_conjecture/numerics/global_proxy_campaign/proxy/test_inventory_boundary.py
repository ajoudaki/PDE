import pytest

from proxy.boundary_benchmark import benchmark_boundary
from proxy.hierarchy import build_kernel_hierarchy
from proxy.inventory import evaluate_family, family_inventory
from proxy.variance_boundary import (
    BOUNDARY_MOMENTS,
    boundary_feature_output,
    boundary_feature_time,
    boundary_kernel,
)


def test_inventory_has_all_completed_families_and_no_spurious_four_input_family():
    records = family_inventory()
    keys = {record["key"] for record in records}
    assert keys == {
        "canonical",
        "variance_homotopy",
        "relative_metric_output",
        "relative_metric_q2",
        "two_input_equal",
        "two_input_opposite",
        "centered_activation",
        "independent_block_metric",
        "three_input_equal",
    }
    assert all(record["moment_count"] >= 2 for record in records)


def test_inventory_domain_guards():
    with pytest.raises(ValueError):
        evaluate_family("centered_activation", c=3)
    with pytest.raises(ValueError):
        evaluate_family("three_input_equal", rho="-3/4")
    with pytest.raises(ValueError):
        evaluate_family("independent_block_metric", alpha=-1, beta=1)


def test_three_input_independence_endpoint_is_finite():
    family = evaluate_family("three_input_equal", rho=0)
    assert family.baseline == 47
    assert len(family.moments) == 2
    assert all(value > 0 for value in family.moments)


def test_variance_normalized_training_target_is_not_silently_one():
    assert evaluate_family("variance_homotopy", alpha=0).training_target is None
    assert evaluate_family("variance_homotopy", alpha="1/2").training_target == 2
    assert evaluate_family("variance_homotopy", alpha=1).training_target == 1
    assert evaluate_family("relative_metric_q2", **{"lambda": 1}).training_target is None


@pytest.mark.parametrize("key,parameters", [
    ("variance_homotopy", {"alpha": "1/2"}),
    ("relative_metric_output", {"lambda": 2}),
    ("relative_metric_q2", {"lambda": "1/2"}),
    ("two_input_equal", {"t": "1/2"}),
    ("two_input_opposite", {"t": "9/10"}),
    ("centered_activation", {"c": 2}),
    ("independent_block_metric", {"alpha": 1, "beta": 2}),
    ("three_input_equal", {"rho": "-1/2"}),
])
def test_every_family_builds_a_positive_proxy_at_a_noncanonical_point(key, parameters):
    family = evaluate_family(key, **parameters)
    hierarchy = build_kernel_hierarchy(family.baseline, family.moments)
    assert len(hierarchy) == len(family.moments) + 1
    assert all(level.kernel(0.99) > 0 for level in hierarchy)


def test_boundary_feature_inverse_and_initial_kernel():
    assert boundary_kernel(0) == 36.0
    assert boundary_feature_time(0) == 0.0
    for s in (0.001, 0.01, 0.03):
        y = boundary_feature_output(s)
        assert boundary_feature_time(y) == pytest.approx(s, rel=2e-14, abs=2e-15)


def test_boundary_benchmark_nested_order_and_taylor_control_count():
    result = benchmark_boundary(grid_points=15, y_max=0.9)
    assert len(result.rational_levels) == 6
    assert len(result.taylor_controls) == len(BOUNDARY_MOMENTS)
    assert [record.information_moments for record in result.brackets] == [1, 2, 3, 4, 5]
    widths = [record.sup_log_width for record in result.brackets]
    assert all(right <= left + 1e-15 for left, right in zip(widths, widths[1:]))
    assert max(record.maximum_reference_escape for record in result.brackets) < 2e-13


def test_boundary_grid_cap_fails_closed():
    with pytest.raises(ValueError, match="grid_points"):
        benchmark_boundary(grid_points=2)
    with pytest.raises(ValueError, match="grid_points"):
        benchmark_boundary(grid_points=2002)
