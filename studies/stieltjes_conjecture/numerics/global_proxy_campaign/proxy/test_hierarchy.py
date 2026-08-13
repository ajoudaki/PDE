from fractions import Fraction

import numpy as np
import pytest

from proxy.hierarchy import (
    MomentConeError,
    build_kernel_brackets,
    build_kernel_hierarchy,
    quadrature_for_prefix,
    quadrature_moment_errors,
    stieltjes_s_fraction,
)
from proxy.inventory import evaluate_family


def test_canonical_endpoint_hierarchy_matches_audited_values():
    family = evaluate_family("canonical")
    levels = build_kernel_hierarchy(family.baseline, family.moments)
    values = [level.kernel(1.0) for level in levels]
    expected = [
        111.0,
        179.38665692719746,
        173.1650734255395,
        174.5966048211249,
        174.44808731147506,
        174.47893212627082,
    ]
    assert values == pytest.approx(expected, rel=2e-15, abs=2e-13)


def test_one_moment_is_added_at_every_level_and_sides_alternate():
    family = evaluate_family("canonical")
    levels = build_kernel_hierarchy(family.baseline, family.moments)
    assert [level.information_moments for level in levels] == list(range(6))
    assert [level.side for level in levels] == [
        "lower", "upper", "lower", "upper", "lower", "upper"
    ]


def test_progressive_brackets_are_nested_on_positive_grid():
    family = evaluate_family("canonical")
    brackets = build_kernel_brackets(family.baseline, family.moments)
    for y in np.linspace(0.0, 2.0, 51):
        lowers = [bracket.lower.kernel(float(y)) for bracket in brackets]
        uppers = [bracket.upper.kernel(float(y)) for bracket in brackets]
        assert lowers == pytest.approx(sorted(lowers))
        assert uppers == pytest.approx(sorted(uppers, reverse=True))
        assert all(lower <= upper for lower, upper in zip(lowers, uppers))


def test_s_fraction_fails_closed_outside_moment_cone():
    with pytest.raises(MomentConeError):
        stieltjes_s_fraction([1, -1])
    with pytest.raises(MomentConeError):
        stieltjes_s_fraction([0, 1])


def test_zero_measure_endpoint_collapses_to_ntk():
    family = evaluate_family("relative_metric_output", **{"lambda": 0})
    assert family.baseline == 27
    assert family.moments == (0, 0, 0, 0)
    hierarchy = build_kernel_hierarchy(family.baseline, family.moments)
    assert len(hierarchy) == 1
    assert hierarchy[0].kernel(7.0) == 27.0


def test_every_canonical_atomic_rule_matches_its_moment_prefix():
    moments = evaluate_family("canonical").moments
    for count in range(1, len(moments) + 1):
        rule = quadrature_for_prefix(moments[:count])
        assert max(abs(value) for value in quadrature_moment_errors(
            rule, moments[:count]
        )) < 3e-15
        assert all(node >= 0 for node in rule.nodes)
        assert all(weight >= 0 for weight in rule.weights)


def test_audited_canonical_gauss_and_radau_nodes_weights():
    moments = evaluate_family("canonical").moments
    gauss = quadrature_for_prefix(moments[:4])
    radau = quadrature_for_prefix(moments[:5])
    assert gauss.nodes == pytest.approx((0.0272629998478521, 0.5519348798369933))
    assert gauss.weights == pytest.approx((58.89534501443515, 9.491311912762315))
    assert radau.nodes == pytest.approx((0.0, 0.2133933440943994, 0.6582709413391857))
    assert radau.weights == pytest.approx((46.81094092048007, 16.5403181664963, 5.03539784022110))
