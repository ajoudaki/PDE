from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
import pytest
import torch


HERE = Path(__file__).resolve().parents[1]
EULER = HERE.parents[1] / "width_ladder" / "euler_fp32"
PROXY_PARENT = HERE.parents[2] / "global_proxy_campaign"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(EULER))
sys.path.insert(0, str(PROXY_PARENT))

import euler_engine as audited_euler  # noqa: E402
import nested_init as audited_init  # noqa: E402
import one_input_engine as panel  # noqa: E402
from proxy.inventory import evaluate_family  # noqa: E402


@pytest.mark.parametrize("configuration", panel.CONFIGURATIONS)
def test_fused_field_and_metric_kernel_match_autograd(configuration):
    generator = torch.Generator().manual_seed(202608141)
    batch, width = 3, 5
    state = panel.State(
        torch.randn(batch, width, generator=generator, dtype=torch.float64),
        torch.randn(batch, width, width, generator=generator, dtype=torch.float64),
        torch.randn(batch, width, generator=generator, dtype=torch.float64),
    )
    tangent, obs = panel.fused_eval(state, configuration, target=1.0)

    a = state.a.clone().requires_grad_(True)
    W = state.W.clone().requires_grad_(True)
    u = state.u.clone().requires_grad_(True)
    hidden = u.square() - configuration.centering
    z = torch.bmm(W, hidden.unsqueeze(-1)).squeeze(-1) / math.sqrt(width)
    output = torch.mean(a * z.square(), dim=1)
    ga, gW, gu = torch.autograd.grad(output.sum(), (a, W, u))
    residual_factor = 2.0 * (1.0 - output)
    metric = configuration.hidden_metric
    expected_tangents = (
        width * ga * residual_factor[:, None],
        width * metric * gW * residual_factor[:, None, None],
        width * metric * gu * residual_factor[:, None],
    )
    for actual, expected in zip(
        (tangent.a, tangent.W, tangent.u), expected_tangents
    ):
        torch.testing.assert_close(actual, expected, rtol=2e-13, atol=2e-13)

    expected_a = width * ga.square().sum(dim=1)
    expected_W = width * metric * gW.square().sum(dim=(1, 2))
    expected_u = width * metric * gu.square().sum(dim=1)
    torch.testing.assert_close(obs.output, output, rtol=2e-13, atol=2e-13)
    torch.testing.assert_close(obs.kernel_a, expected_a, rtol=2e-13, atol=2e-13)
    torch.testing.assert_close(obs.kernel_W, expected_W, rtol=2e-13, atol=2e-13)
    torch.testing.assert_close(obs.kernel_u, expected_u, rtol=2e-13, atol=2e-13)
    torch.testing.assert_close(
        obs.kernel, expected_a + expected_W + expected_u, rtol=2e-13, atol=2e-13
    )
    torch.testing.assert_close(
        obs.weighted_kernel, (1.0 - output) * obs.kernel, rtol=2e-13, atol=2e-13
    )
    torch.testing.assert_close(
        obs.loss, (1.0 - output).square(), rtol=2e-13, atol=2e-13
    )
    torch.testing.assert_close(obs.q1, u.square().mean(dim=1), rtol=0.0, atol=0.0)
    torch.testing.assert_close(
        obs.q2, z.square().mean(dim=1), rtol=2e-13, atol=2e-13
    )


def test_canonical_is_exact_regression_to_audited_euler_engine():
    generator = torch.Generator().manual_seed(202608142)
    state = panel.State(
        torch.randn(2, 7, generator=generator, dtype=torch.float64),
        torch.randn(2, 7, 7, generator=generator, dtype=torch.float64),
        torch.randn(2, 7, generator=generator, dtype=torch.float64),
    )
    actual_tangent, actual = panel.fused_eval(state, panel.CANONICAL)
    expected_tangent, expected = audited_euler.fused_eval(state)
    for left, right in (
        (actual_tangent.a, expected_tangent.a),
        (actual_tangent.W, expected_tangent.W),
        (actual_tangent.u, expected_tangent.u),
        (actual_tangent.w_derivative_l2, expected_tangent.w_derivative_l2),
        (
            actual_tangent.w_state_inner_derivative,
            expected_tangent.w_state_inner_derivative,
        ),
        (actual.output, expected.output),
        (actual.kernel, expected.kernel),
        (actual.kernel_a, expected.kernel_a),
        (actual.kernel_W, expected.kernel_W),
        (actual.kernel_u, expected.kernel_u),
    ):
        torch.testing.assert_close(left, right, rtol=2e-15, atol=2e-15)


def test_relative_metric_enters_updates_and_kernel_linearly():
    generator = torch.Generator().manual_seed(202608143)
    state = panel.State(
        torch.randn(2, 6, generator=generator, dtype=torch.float64),
        torch.randn(2, 6, 6, generator=generator, dtype=torch.float64),
        torch.randn(2, 6, generator=generator, dtype=torch.float64),
    )
    base_tangent, base = panel.fused_eval(state, panel.CANONICAL)
    metric_tangent, metric = panel.fused_eval(state, panel.RELATIVE_METRIC_L2)
    torch.testing.assert_close(metric_tangent.a, base_tangent.a)
    torch.testing.assert_close(metric_tangent.W, 2.0 * base_tangent.W)
    torch.testing.assert_close(metric_tangent.u, 2.0 * base_tangent.u)
    torch.testing.assert_close(metric.kernel_a, base.kernel_a)
    torch.testing.assert_close(metric.kernel_W, 2.0 * base.kernel_W)
    torch.testing.assert_close(metric.kernel_u, 2.0 * base.kernel_u)
    torch.testing.assert_close(
        metric.kernel, base.kernel_a + 2.0 * (base.kernel_W + base.kernel_u)
    )


def test_variance_initialization_uses_sqrt_v_and_keeps_antithetic_pair():
    width, seed, lineage = 11, 171, 3
    base = audited_init.generate_lineage(
        width, seed=seed, lineage=lineage, row_block=4, prefix_sizes=(5, 11)
    )
    state, metadata = panel.build_antithetic_state(
        panel.VARIANCE_VHALF,
        width,
        seed=seed,
        lineage=lineage,
        device=torch.device("cpu"),
        row_block=4,
        prefix_sizes=(5, 11),
    )
    expected_W = np.multiply(
        base[2], np.float32(math.sqrt(0.5)), dtype=np.float32
    )
    np.testing.assert_array_equal(state.W[0].numpy(), expected_W)
    np.testing.assert_array_equal(state.W[1].numpy(), expected_W)
    np.testing.assert_array_equal(state.u[0].numpy(), base[1])
    np.testing.assert_array_equal(state.u[1].numpy(), base[1])
    np.testing.assert_array_equal(state.a[0].numpy(), base[0])
    np.testing.assert_array_equal(state.a[1].numpy(), -base[0])
    assert metadata["base_state_sha256"] == base[3]
    assert metadata["physical_state_sha256"] != base[3]
    assert metadata["middle_weight_variance"] == 0.5


def test_physical_prefix_digests_bind_scaled_bytes_and_are_width_nested():
    common = dict(seed=172, lineage=4, device=torch.device("cpu"), row_block=4)
    small, small_metadata = panel.build_antithetic_state(
        panel.VARIANCE_VHALF, 7, prefix_sizes=(5, 7), **common
    )
    large, large_metadata = panel.build_antithetic_state(
        panel.VARIANCE_VHALF, 11, prefix_sizes=(5, 11), **common
    )
    assert (
        small_metadata["physical_prefix_sha256"][5]
        == large_metadata["physical_prefix_sha256"][5]
    )
    assert (
        small_metadata["base_prefix_sha256"][5]
        == large_metadata["base_prefix_sha256"][5]
    )
    assert (
        small_metadata["physical_prefix_sha256"][5]
        != small_metadata["base_prefix_sha256"][5]
    )
    independent = panel.physical_prefix_digest(
        172,
        4,
        5,
        panel.VARIANCE_VHALF,
        small.a[0].numpy(),
        small.u[0].numpy(),
        small.W[0].numpy(),
    )
    assert independent == small_metadata["physical_prefix_sha256"][5]
    np.testing.assert_array_equal(small.W[0, :5, :5], large.W[0, :5, :5])


def test_variance_proxy_chart_has_correct_output_kernel_target_and_time():
    values = torch.tensor([2.0, 3.0], dtype=torch.float64)
    obs = panel.Observables(
        output=values,
        kernel=5.0 * values,
        kernel_a=values,
        kernel_W=2.0 * values,
        kernel_u=2.0 * values,
        weighted_kernel=7.0 * values,
        loss=11.0 * values,
        q1=13.0 * values,
        q2=17.0 * values,
    )
    proxy = panel.to_proxy_coordinates(obs, panel.VARIANCE_VHALF)
    assert proxy.target == 2.0
    assert proxy.time_scale == 0.5
    torch.testing.assert_close(proxy.output, 2.0 * obs.output)
    torch.testing.assert_close(proxy.kernel, 2.0 * obs.kernel)
    torch.testing.assert_close(proxy.kernel_a, 2.0 * obs.kernel_a)
    torch.testing.assert_close(proxy.kernel_W, 2.0 * obs.kernel_W)
    torch.testing.assert_close(proxy.kernel_u, 2.0 * obs.kernel_u)
    torch.testing.assert_close(proxy.weighted_kernel, 4.0 * obs.weighted_kernel)
    torch.testing.assert_close(proxy.loss, 4.0 * obs.loss)
    torch.testing.assert_close(proxy.q1, obs.q1)
    torch.testing.assert_close(proxy.q2, 2.0 * obs.q2)


def test_variance_fused_physical_observables_map_end_to_end_to_normalized_chart():
    state, _ = panel.build_antithetic_state(
        panel.VARIANCE_VHALF,
        9,
        seed=173,
        lineage=2,
        device=torch.device("cpu"),
        row_block=3,
        prefix_sizes=(5, 9),
    )
    _, physical = panel.fused_eval(state, panel.VARIANCE_VHALF)
    normalized = panel.to_proxy_coordinates(physical, panel.VARIANCE_VHALF)
    v = panel.VARIANCE_VHALF.middle_weight_variance
    torch.testing.assert_close(v * normalized.output, physical.output)
    torch.testing.assert_close(v * normalized.kernel, physical.kernel)
    torch.testing.assert_close(
        v * v * normalized.weighted_kernel, physical.weighted_kernel
    )
    torch.testing.assert_close(v * v * normalized.loss, physical.loss)
    torch.testing.assert_close(v * normalized.q2, physical.q2)
    assert normalized.target * v == 1.0


def test_proxy_family_bindings_are_the_existing_exact_inventory_points():
    assert (panel.CANONICAL.proxy_family, panel.CANONICAL.proxy_parameters) == (
        "canonical",
        (),
    )
    assert panel.CENTERED_C1.proxy_parameters == (("c", "1"),)
    assert panel.RELATIVE_METRIC_L2.proxy_parameters == (("lambda", "2"),)
    assert panel.VARIANCE_VHALF.proxy_parameters == (("alpha", "1/2"),)


def test_analytic_infinite_width_initialization_gates():
    expected = {
        "canonical": (3.0, 27.0, 36.0, 48.0, 111.0),
        "centered_c1": (2.0, 12.0, 16.0, 32.0, 60.0),
        "relative_metric_l2": (3.0, 27.0, 72.0, 96.0, 195.0),
        "variance_vhalf": (1.5, 6.75, 18.0, 12.0, 36.75),
    }
    for configuration in panel.CONFIGURATIONS:
        values = panel.initial_mean_field_values(configuration)
        assert values["output"] == 0.0
        assert values["q1"] == 1.0
        assert (
            values["q2"],
            values["kernel_a"],
            values["kernel_W"],
            values["kernel_u"],
            values["kernel"],
        ) == expected[configuration.key]
    variance = panel.initial_mean_field_values(panel.VARIANCE_VHALF)
    assert variance["kernel"] / 0.5 == 73.5
    assert variance["q2"] / 0.5 == 3.0


def test_exact_finite_width_initial_kernel_means_use_m2_m4_and_r():
    width = 8
    expected = {
        "canonical": (27 + 288 / width, 36 + 384 / width, 48 + 672 / width),
        "centered_c1": (12 + 168 / width, 16 + 224 / width, 32 + 448 / width),
        "relative_metric_l2": (
            27 + 288 / width,
            72 + 768 / width,
            96 + 1344 / width,
        ),
        "variance_vhalf": (
            6.75 + 72 / width,
            18 + 192 / width,
            12 + 168 / width,
        ),
    }
    for configuration in panel.CONFIGURATIONS:
        finite = panel.initial_finite_width_means(configuration, width)
        assert (
            finite["kernel_a"],
            finite["kernel_W"],
            finite["kernel_u"],
        ) == expected[configuration.key]
        assert finite["kernel"] == sum(expected[configuration.key])
        limiting = panel.initial_mean_field_values(configuration)
        huge = panel.initial_finite_width_means(configuration, 10**12)
        for key in ("kernel_a", "kernel_W", "kernel_u", "kernel", "q1", "q2"):
            assert huge[key] == pytest.approx(limiting[key], rel=2e-10)
    assert panel.centered_gaussian_moments(panel.CANONICAL) == {
        "m2": 3.0,
        "m4": 105.0,
        "r": 15.0,
    }
    assert panel.centered_gaussian_moments(panel.CENTERED_C1) == {
        "m2": 2.0,
        "m4": 60.0,
        "r": 10.0,
    }


def test_invalid_finite_width_is_rejected():
    with pytest.raises(ValueError, match="positive integer"):
        panel.initial_finite_width_means(panel.CANONICAL, 0)


def test_initial_gates_match_the_existing_exact_proxy_inventory():
    for configuration in panel.CONFIGURATIONS:
        parameters = dict(configuration.proxy_parameters)
        exact = evaluate_family(configuration.proxy_family, **parameters)
        physical = panel.initial_mean_field_values(configuration)
        expected_proxy_baseline = (
            physical["kernel"] / configuration.middle_weight_variance
        )
        assert float(exact.baseline) == expected_proxy_baseline
    q2 = evaluate_family("relative_metric_q2", **{"lambda": "2"})
    assert float(q2.baseline) == 3.0
