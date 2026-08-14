from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
import pytest
import torch


TWO_INPUT = Path(__file__).resolve().parents[1]
BREADTH = TWO_INPUT.parent
sys.path.insert(0, str(TWO_INPUT))
sys.path.insert(0, str(BREADTH / "one_input"))

import one_input_engine  # noqa: E402
import two_input_engine as panel  # noqa: E402


def _random_state(*, replicas: int = 2, width: int = 5, seed: int = 1):
    generator = torch.Generator().manual_seed(seed)
    return panel.State(
        a=torch.randn(replicas, width, generator=generator, dtype=torch.float64),
        W=torch.randn(
            replicas, width, width, generator=generator, dtype=torch.float64
        ),
        u=torch.randn(
            replicas, 2, width, generator=generator, dtype=torch.float64
        ),
    )


@pytest.mark.parametrize("sigma", (-1, 1))
def test_full_average_loss_field_and_full_ntk_match_autograd(sigma):
    width = 4
    configuration = panel.Configuration("autograd", math.sqrt(0.5), sigma)
    state = _random_state(replicas=1, width=width, seed=202608151 + sigma)
    tangent, obs = panel.fused_eval(state, configuration)

    a = state.a.clone().requires_grad_(True)
    W = state.W.clone().requires_grad_(True)
    u = state.u.clone().requires_grad_(True)
    z = torch.bmm(W, u.square().transpose(1, 2)).transpose(1, 2) / math.sqrt(
        width
    )
    output = torch.mean(a[:, None, :] * z.square(), dim=2)
    labels = output.new_tensor(configuration.labels)
    loss = 0.5 * (labels[None, :] - output).square().sum()
    ga_loss, gW_loss, gu_loss = torch.autograd.grad(
        loss, (a, W, u), retain_graph=True
    )
    gram = panel.input_gram(
        configuration, dtype=u.dtype, device=u.device
    )
    expected = (
        -width * ga_loss,
        -width * gW_loss,
        -width * torch.einsum("st,rtj->rsj", gram, gu_loss),
    )
    for actual, wanted in zip(
        (tangent.a, tangent.W, tangent.u), expected
    ):
        torch.testing.assert_close(actual, wanted, rtol=3e-13, atol=3e-13)

    gradients = []
    for sample in range(2):
        gradients.append(
            torch.autograd.grad(
                output[0, sample], (a, W, u), retain_graph=True
            )
        )
    expected_a = torch.empty((1, 2, 2), dtype=a.dtype)
    expected_W = torch.empty_like(expected_a)
    expected_u = torch.empty_like(expected_a)
    for s in range(2):
        for t in range(2):
            expected_a[0, s, t] = width * torch.sum(
                gradients[s][0] * gradients[t][0]
            )
            expected_W[0, s, t] = width * torch.sum(
                gradients[s][1] * gradients[t][1]
            )
            metric_gu_t = torch.einsum(
                "ij,rjk->rik", gram, gradients[t][2]
            )
            expected_u[0, s, t] = width * torch.sum(
                gradients[s][2] * metric_gu_t
            )
    torch.testing.assert_close(obs.output, output, rtol=2e-13, atol=2e-13)
    torch.testing.assert_close(
        obs.kernel_a_matrix, expected_a, rtol=3e-13, atol=3e-13
    )
    torch.testing.assert_close(
        obs.kernel_W_matrix, expected_W, rtol=3e-13, atol=3e-13
    )
    torch.testing.assert_close(
        obs.kernel_u_matrix, expected_u, rtol=3e-13, atol=3e-13
    )


@pytest.mark.parametrize("sigma", (-1, 1))
def test_channel_equations_are_exact_directional_derivatives(sigma):
    configuration = panel.Configuration("channel", 0.37, sigma)
    state = _random_state(replicas=2, width=5, seed=202608160 + sigma)
    tangent, obs = panel.fused_eval(state, configuration)

    a = state.a.clone().requires_grad_(True)
    W = state.W.clone().requires_grad_(True)
    u = state.u.clone().requires_grad_(True)
    z = torch.bmm(W, u.square().transpose(1, 2)).transpose(1, 2) / math.sqrt(5)
    output = torch.mean(a[:, None, :] * z.square(), dim=2)
    g = 0.5 * (output[:, 0] + sigma * output[:, 1])
    delta = 0.5 * (output[:, 0] - sigma * output[:, 1])

    def directional(values):
        grads = torch.autograd.grad(values.sum(), (a, W, u), retain_graph=True)
        return sum(
            torch.sum(gradient * velocity, dim=tuple(range(1, gradient.ndim)))
            for gradient, velocity in zip(
                grads, (tangent.a, tangent.W, tangent.u)
            )
        )

    torch.testing.assert_close(
        directional(g), 2.0 * obs.effective_numerator,
        rtol=4e-13, atol=4e-13,
    )
    torch.testing.assert_close(
        directional(delta), 2.0 * obs.transverse_numerator,
        rtol=4e-13, atol=4e-13,
    )
    labels = output.new_tensor(configuration.labels)
    torch.testing.assert_close(
        obs.loss_full,
        0.5 * (labels[None, :] - output).square().sum(dim=1),
    )
    torch.testing.assert_close(
        obs.loss_full, obs.loss_projected + obs.delta.square()
    )


def test_equal_label_identical_input_endpoint_matches_one_input_exactly():
    width = 6
    generator = torch.Generator().manual_seed(202608171)
    a = torch.randn(2, width, generator=generator, dtype=torch.float64)
    W = torch.randn(2, width, width, generator=generator, dtype=torch.float64)
    u = torch.randn(2, width, generator=generator, dtype=torch.float64)
    one_state = one_input_engine.State(a, W, u)
    two_state = panel.State(a, W, torch.stack((u, u), dim=1))
    configuration = panel.Configuration("identical-plus", 1.0, 1)

    one_tangent, one = one_input_engine.fused_eval(
        one_state, one_input_engine.CANONICAL
    )
    two_tangent, two = panel.fused_eval(two_state, configuration)
    torch.testing.assert_close(two.g, one.output, rtol=2e-14, atol=2e-14)
    torch.testing.assert_close(two.kernel_g, one.kernel, rtol=2e-14, atol=2e-14)
    torch.testing.assert_close(two.delta, torch.zeros_like(two.delta))
    torch.testing.assert_close(two.cross_kernel, torch.zeros_like(two.cross_kernel))
    torch.testing.assert_close(two.kernel_delta, torch.zeros_like(two.kernel_delta))
    torch.testing.assert_close(two_tangent.a, one_tangent.a, rtol=2e-14, atol=2e-14)
    torch.testing.assert_close(two_tangent.W, one_tangent.W, rtol=2e-14, atol=2e-14)
    torch.testing.assert_close(
        two_tangent.u[:, 0], one_tangent.u, rtol=2e-14, atol=2e-14
    )
    torch.testing.assert_close(
        two_tangent.u[:, 1], one_tangent.u, rtol=2e-14, atol=2e-14
    )


def test_opposite_label_identical_input_channel_is_degenerate():
    state = _random_state(replicas=2, width=5, seed=202608181)
    state = panel.State(
        state.a,
        state.W,
        torch.stack((state.u[:, 0], state.u[:, 0]), dim=1),
    )
    _, obs = panel.fused_eval(
        state, panel.Configuration("identical-minus", 1.0, -1)
    )
    torch.testing.assert_close(obs.g, torch.zeros_like(obs.g))
    torch.testing.assert_close(
        obs.kernel_g, torch.zeros_like(obs.kernel_g), atol=1e-13, rtol=0.0
    )
    torch.testing.assert_close(
        obs.cross_kernel,
        torch.zeros_like(obs.cross_kernel),
        atol=1e-13,
        rtol=0.0,
    )
    torch.testing.assert_close(
        obs.effective_numerator,
        torch.zeros_like(obs.effective_numerator),
        atol=1e-13,
        rtol=0.0,
    )


def test_theta_sign_is_a_first_preactivation_gauge():
    theta = math.sqrt(0.5)
    state = _random_state(replicas=2, width=7, seed=202608191)
    reflected = panel.State(
        state.a,
        state.W,
        torch.stack((state.u[:, 0], -state.u[:, 1]), dim=1),
    )
    for sigma in (-1, 1):
        positive = panel.Configuration("positive", theta, sigma)
        negative = panel.Configuration("negative", -theta, sigma)
        tangent_pos, obs_pos = panel.fused_eval(state, positive)
        tangent_neg, obs_neg = panel.fused_eval(reflected, negative)
        for name in obs_pos.__dataclass_fields__:
            torch.testing.assert_close(
                getattr(obs_pos, name), getattr(obs_neg, name),
                rtol=3e-14, atol=3e-14,
            )
        torch.testing.assert_close(tangent_pos.a, tangent_neg.a)
        torch.testing.assert_close(tangent_pos.W, tangent_neg.W)
        torch.testing.assert_close(tangent_pos.u[:, 0], tangent_neg.u[:, 0])
        torch.testing.assert_close(tangent_pos.u[:, 1], -tangent_neg.u[:, 1])


def test_equal_label_input_exchange_has_expected_channel_parities():
    configuration = panel.Configuration("exchange", 0.42, 1)
    state = _random_state(replicas=2, width=5, seed=202608201)
    swapped = panel.State(state.a, state.W, state.u.flip(1))
    tangent, obs = panel.fused_eval(state, configuration)
    swapped_tangent, swapped_obs = panel.fused_eval(swapped, configuration)
    torch.testing.assert_close(swapped_obs.output, obs.output.flip(1))
    torch.testing.assert_close(swapped_obs.g, obs.g)
    torch.testing.assert_close(swapped_obs.delta, -obs.delta)
    torch.testing.assert_close(swapped_obs.kernel_g, obs.kernel_g)
    torch.testing.assert_close(swapped_obs.kernel_delta, obs.kernel_delta)
    torch.testing.assert_close(swapped_obs.cross_kernel, -obs.cross_kernel)
    torch.testing.assert_close(
        swapped_obs.effective_numerator, obs.effective_numerator
    )
    torch.testing.assert_close(swapped_tangent.a, tangent.a)
    torch.testing.assert_close(swapped_tangent.W, tangent.W)
    torch.testing.assert_close(swapped_tangent.u, tangent.u.flip(1))


@pytest.mark.parametrize("sigma", (-1, 1))
def test_channel_kernel_is_psd_and_component_sum_is_exact(sigma):
    configuration = panel.Configuration("psd", math.sqrt(0.5), sigma)
    _, obs = panel.fused_eval(
        _random_state(replicas=5, width=7, seed=202608211 + sigma),
        configuration,
    )
    assert torch.all(obs.Kg >= -1e-12)
    assert torch.all(obs.Kdelta >= -1e-12)
    assert torch.all(obs.Kg * obs.Kdelta - obs.C.square() >= -1e-11)
    torch.testing.assert_close(
        obs.Kg, obs.kernel_g_a + obs.kernel_g_W + obs.kernel_g_u
    )
    torch.testing.assert_close(
        obs.Kdelta,
        obs.kernel_delta_a + obs.kernel_delta_W + obs.kernel_delta_u,
    )
    torch.testing.assert_close(obs.C, obs.C_a + obs.C_W + obs.C_u)


def test_counter_u_stream_covariance_without_allocating_a_large_W():
    width = 200_000
    configuration = panel.CORE_EQUAL
    counters = np.arange(width, dtype=np.uint64)
    u1 = panel.audited_init.normal(
        counters, seed=314159, lineage=2, domain="u"
    )
    independent = panel.audited_init.normal(
        panel.SECOND_INPUT_COUNTER_OFFSET + counters,
        seed=314159,
        lineage=2,
        domain="u",
    )
    u2 = configuration.theta * u1 + math.sqrt(1.0 - configuration.t) * independent
    covariance = np.cov(np.stack((u1, u2)), bias=True)
    np.testing.assert_allclose(
        covariance,
        np.array(((1.0, configuration.theta), (configuration.theta, 1.0))),
        atol=1.2e-2,
        rtol=0.0,
    )


def test_small_counter_state_is_antithetic_and_digest_bound():
    state, metadata = panel.build_antithetic_state(
        panel.CORE_OPPOSITE,
        13,
        seed=271828,
        lineage=4,
        device=torch.device("cpu"),
        row_block=5,
        prefix_sizes=(7, 13),
    )
    torch.testing.assert_close(state.a[1], -state.a[0], rtol=0.0, atol=0.0)
    torch.testing.assert_close(state.W[1], state.W[0], rtol=0.0, atol=0.0)
    torch.testing.assert_close(state.u[1], state.u[0], rtol=0.0, atol=0.0)
    assert metadata["t"] == pytest.approx(0.5)
    assert metadata["sigma"] == -1
    assert len(metadata["physical_state_sha256"]) == 64
    assert metadata["physical_state_sha256"] != metadata["base_one_input_state_sha256"]
    small, small_metadata = panel.build_antithetic_state(
        panel.CORE_OPPOSITE,
        7,
        seed=271828,
        lineage=4,
        device=torch.device("cpu"),
        row_block=5,
        prefix_sizes=(7,),
    )
    assert metadata["physical_prefix_sha256"][7] == small_metadata[
        "physical_state_sha256"
    ]
    torch.testing.assert_close(state.a[:, :7], small.a, rtol=0.0, atol=0.0)
    torch.testing.assert_close(state.u[:, :, :7], small.u, rtol=0.0, atol=0.0)
    torch.testing.assert_close(state.W[:, :7, :7], small.W, rtol=0.0, atol=0.0)


@pytest.mark.parametrize(
    ("configuration", "expected"),
    (
        (panel.CORE_EQUAL, (22.0, 26.0, 32.0, 80.0, 212, 286, 472, 970)),
        (panel.CORE_OPPOSITE, (5.0, 10.0, 16.0, 31.0, 76, 98, 200, 374)),
    ),
)
def test_exact_finite_width_initial_kernel_controls(configuration, expected):
    width = 37
    record = panel.finite_width_initial_kernel_means(configuration, width)
    limits = expected[:4]
    corrections = expected[4:]
    for key, limit, correction in zip(
        ("kernel_a", "kernel_W", "kernel_u", "kernel"),
        limits,
        corrections,
        strict=True,
    ):
        assert record[key] == pytest.approx(limit + correction / width)


def test_in_place_euler_and_w_norm_diagnostics_match_direct_fp32_arithmetic():
    state = _random_state(replicas=2, width=7, seed=202608221)
    state = panel.State(
        state.a.to(torch.float32),
        state.W.to(torch.float32),
        state.u.to(torch.float32),
    )
    tangent, _ = panel.fused_eval(state, panel.CORE_EQUAL)
    direct_w_norm = torch.linalg.vector_norm(
        tangent.W.reshape(tangent.W.shape[0], -1), dim=1
    )
    torch.testing.assert_close(
        tangent.w_derivative_l2, direct_w_norm, rtol=2e-6, atol=2e-6
    )
    direct_inner = torch.sum(state.W * tangent.W, dim=(1, 2))
    torch.testing.assert_close(
        tangent.w_state_inner_derivative, direct_inner, rtol=2e-6, atol=2e-5
    )

    expected = panel.State(state.a.clone(), state.W.clone(), state.u.clone())
    expected.a.add_(tangent.a, alpha=1e-5)
    expected.W.add_(tangent.W, alpha=1e-5)
    expected.u.add_(tangent.u, alpha=1e-5)
    actual = panel.State(state.a.clone(), state.W.clone(), state.u.clone())
    returned = panel.euler_step_in_place(actual, tangent, 1e-5)
    assert returned is actual
    assert torch.equal(actual.a, expected.a)
    assert torch.equal(actual.W, expected.W)
    assert torch.equal(actual.u, expected.u)
