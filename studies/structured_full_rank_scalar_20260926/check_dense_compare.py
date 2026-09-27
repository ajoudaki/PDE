"""Deterministic dense-core verification; no scientific training campaign.

Run directly. The JSON report records exact audited source hashes. Small
matrices and short artificial trajectories test equations and numerics only.
The maintained oracle receives X=sqrt(2)*u.T to undo its input convention.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import traceback

for _name in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "OMP_NUM_THREADS"):
    os.environ[_name] = "1"

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CORE = HERE / "dense_compare.py"
ORACLE = ROOT / "code/pde/finite_network.py"
REPORT = ROOT / "data/generated/structured_full_rank_scalar_20260926/dense_check_results.json"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


dc = load_module("checked_dense_compare", CORE)
fn = load_module("maintained_finite_network_oracle", ORACLE)


def arrays(state):
    return (state.w, state.W, state.c)


def state_norm(state):
    return float(np.sqrt(sum(np.sum(a * a) for a in arrays(state))))


def distance(left, right):
    return float(np.sqrt(sum(np.sum((a - b) ** 2)
                             for a, b in zip(arrays(left), arrays(right)))))


def assert_state_close(left, right, *, atol=3e-14, rtol=3e-12):
    for name, a, b in zip(("w", "W", "c"), arrays(left), arrays(right)):
        np.testing.assert_allclose(a, b, atol=atol, rtol=rtol,
                                   err_msg=f"state block {name}")


def add(state, velocity, h):
    return dc.State(*(a + h * b for a, b in zip(arrays(state), arrays(velocity))))


def oracle_parameters(state):
    return fn.Parameters((state.w, state.W), state.c)


def oracle_rhs(state, u, y):
    value = fn.flow_velocity(oracle_parameters(state), np.sqrt(2) * u.T, y)
    return dc.State(value.weights[0], value.weights[1], value.readout)


def loss(state, u, y):
    return float(np.mean((dc.forward(state, u).output - y) ** 2))


def problem(n=8, seed=8102, scale=0.6):
    rng = np.random.default_rng(seed)
    state = dc.State(scale * rng.standard_normal((n, 2)),
                     scale * rng.standard_normal((n, n)) / np.sqrt(n),
                     0.5 * rng.standard_normal(n))
    angles = np.array([0.13, 0.54, 1.21, 1.77, 2.61])
    u = np.column_stack((np.cos(angles), np.sin(angles)))
    y = 0.8 * np.cos(3 * angles) + 0.2 * np.sin(angles)
    return state, u, y


def test_oracle_and_directional_derivatives():
    residuals = []
    directional = []
    for n, seed, scale in ((8, 8102, 0.6), (16, 317, 0.7), (8, 450, 12.0)):
        state, u, y = problem(n, seed, scale)
        before = state.copy()
        actual = dc.rhs(state, u, y)
        expected = oracle_rhs(state, u, y)
        assert_state_close(actual, expected)
        residuals.append(distance(actual, expected))
        reference_forward = fn.forward(oracle_parameters(state), np.sqrt(2) * u.T)
        np.testing.assert_allclose(dc.forward(state, u).output,
                                   reference_forward.output, rtol=2e-13, atol=2e-15)
        assert_state_close(state, before, atol=0, rtol=0)
        if scale > 1:
            continue  # finite differences use the nonsaturated custom states
        gradient = dc.State(-actual.w / n, -actual.W, -actual.c / n)
        oracle_gradient = fn.loss_gradients(oracle_parameters(state), np.sqrt(2) * u.T, y)
        assert_state_close(gradient, dc.State(oracle_gradient.weights[0],
                           oracle_gradient.weights[1], oracle_gradient.readout))
        rng = np.random.default_rng(seed + 32)
        for block in range(3):
            directions = [np.zeros_like(a) for a in arrays(state)]
            directions[block] = rng.standard_normal(directions[block].shape)
            directions[block] /= np.linalg.norm(directions[block])
            direction = dc.State(*directions)
            analytical = float(sum(np.sum(g * v) for g, v
                                   in zip(arrays(gradient), directions)))
            errors = []
            for h in (1e-4, 1e-5, 1e-6):
                numerical = (loss(add(state, direction, h), u, y)
                             - loss(add(state, direction, -h), u, y)) / (2*h)
                errors.append(abs(numerical - analytical))
            best = min(errors)
            assert best <= 3e-9 + 3e-6 * abs(analytical), (block, best, analytical)
            directional.append({"width": n, "block": block,
                                "analytic": analytical, "best_abs_error": best})
        energy = -(np.sum(actual.w**2) / n + np.sum(actual.W**2)
                   + np.sum(actual.c**2) / n)
        h = 1e-5
        finite_energy = (loss(add(state, actual, h), u, y)
                         - loss(add(state, actual, -h), u, y)) / (2*h)
        assert abs(finite_energy - energy) <= 1e-8 + 2e-6 * abs(energy)
    return {"maximum_oracle_state_discrepancy": max(residuals),
            "finite_difference_results": directional}


def hadamard(n):
    # Independent definition through the parity of binary inner products.
    return np.array([[(-1.0) ** ((i & j).bit_count()) for j in range(n)]
                     for i in range(n)]) / np.sqrt(n)


def seeded(seed, stream):
    return np.random.default_rng(np.random.SeedSequence([seed, stream]))


def signs(rng, n):
    return 2 * rng.integers(0, 2, size=n) - 1


def test_initializers():
    diagnostics = []
    streams = {"gaussian": 101, "gaussian_control": 102, "hd": 201,
               "hdhd": 202, "fastfood": 203, "reflection4": 204, "diagonal": 205}
    for n in (8, 16, 32):
        H = hadamard(n)
        np.testing.assert_allclose(H.T @ H, np.eye(n), atol=1e-14, rtol=0)
        for seed in (0, 7, 41):
            states = {method: dc.initialize(n, seed, method) for method in dc.METHODS}
            reference = states["gaussian"]
            for method, state in states.items():
                np.testing.assert_array_equal(state.w, reference.w)
                np.testing.assert_array_equal(state.c, reference.c)
                np.testing.assert_array_equal(state.w, seeded(seed, 1).standard_normal((n, 2)))
                np.testing.assert_array_equal(state.c, seeded(seed, 2).standard_normal(n) / n)
                assert_state_close(state, dc.initialize(n, seed, method), atol=0, rtol=0)
                singular = np.linalg.svd(state.W, compute_uv=False)
                assert singular[-1] > 1e-12 * singular[0], (n, seed, method, singular[-1])
                rng = seeded(seed, streams[method])
                if method.startswith("gaussian"):
                    expected = rng.standard_normal((n, n)) / np.sqrt(n)
                elif method == "hd":
                    expected = H @ np.diag(signs(rng, n))
                elif method == "diagonal":
                    expected = np.diag(signs(rng, n))
                elif method in ("hdhd", "reflection4"):
                    d1, d3 = signs(rng, n), signs(rng, n)
                    if method == "hdhd":
                        d2 = signs(rng, n)
                    else:
                        d2 = np.ones(n)
                        d2[rng.choice(n, size=4, replace=False)] = -1
                    expected = np.diag(d1) @ H @ np.diag(d2) @ H @ np.diag(d3)
                    central = H @ np.diag(d1) @ state.W @ np.diag(d3) @ H
                    np.testing.assert_allclose(central, np.diag(d2), atol=3e-14, rtol=0)
                    if method == "reflection4":
                        assert np.count_nonzero(d2 < 0) == 4
                        perturbation = state.W - np.diag(d1 * d3)
                        assert np.linalg.matrix_rank(perturbation, tol=1e-10) == 4
                else:
                    g = rng.standard_normal(n)
                    permutation = rng.permutation(n)
                    b = signs(rng, n)
                    chi_squared = rng.chisquare(n, size=n)
                    s = np.sqrt(chi_squared) / np.linalg.norm(g)
                    Pi = np.eye(n)[permutation]
                    expected = np.diag(s) @ H @ np.diag(g) @ Pi @ H @ np.diag(b)
                    np.testing.assert_allclose(np.sum(state.W**2, axis=1),
                                               chi_squared / n, atol=2e-14, rtol=3e-13)
                    # Reverse the factor sequence for an independent transpose action.
                    v = np.linspace(-0.7, 0.8, n)
                    transpose_action = np.diag(b) @ H @ Pi.T @ np.diag(g) @ H @ np.diag(s) @ v
                    np.testing.assert_allclose(state.W.T @ v, transpose_action,
                                               atol=3e-14, rtol=3e-13)
                np.testing.assert_allclose(state.W, expected, atol=3e-14, rtol=3e-13)
                if method in ("hd", "hdhd", "reflection4", "diagonal"):
                    np.testing.assert_allclose(singular, np.ones(n), atol=3e-14, rtol=0)
                    np.testing.assert_allclose(np.sum(state.W**2), n, atol=3e-12, rtol=0)
                x, z = np.linspace(-0.4, 0.9, n), np.linspace(0.8, -0.7, n)
                np.testing.assert_allclose(z @ (state.W @ x), x @ (state.W.T @ z),
                                           atol=3e-13, rtol=3e-13)
                diagnostics.append({"width": n, "seed": seed, "method": method,
                                    "minimum_singular_value": float(singular[-1]),
                                    "mean_squared_singular_value": float(np.mean(singular**2))})
            assert not np.array_equal(states["gaussian"].W, states["gaussian_control"].W)
    return {"deterministic_draws_verified": len(diagnostics),
            "scope": "Exact factor/seed and norm-law identities; not a statistical distribution test.",
            "diagnostics": diagnostics}


def test_antipodes_and_dense_updates():
    largest = 0.0
    for method in dc.METHODS:
        state = dc.initialize(8, 517, method)
        for k in (3, 5):
            angles = np.arange(k) * np.pi / k
            u = np.column_stack((np.cos(angles), np.sin(angles)))
            y = np.cos(k * angles)
            full_u, full_y = np.vstack((u, -u)), np.concatenate((y, -y))
            v_half, v_full = dc.rhs(state, u, y), dc.rhs(state, full_u, full_y)
            assert_state_close(v_half, v_full, atol=3e-14, rtol=3e-12)
            largest = max(largest, distance(v_half, v_full))
            np.testing.assert_allclose(dc.forward(state, -u).output,
                                       -dc.forward(state, u).output, atol=1e-15, rtol=1e-14)
            assert_state_close(dc.heun_step(state, u, y, 0.03),
                               dc.heun_step(state, full_u, full_y, 0.03))
    state, u, y = problem()
    diagonal = dc.initialize(8, 517, "diagonal")
    stepped = dc.heun_step(diagonal, u, y, 0.02)
    off_diagonal = stepped.W - np.diag(np.diag(stepped.W))
    assert np.linalg.norm(off_diagonal) > 1e-10
    before = state.copy()
    velocity = oracle_rhs(state, u, y)
    predicted = add(state, velocity, 0.03)
    velocity2 = oracle_rhs(predicted, u, y)
    expected = dc.State(*(a + 0.015 * (v1 + v2) for a, v1, v2
                          in zip(arrays(state), arrays(velocity), arrays(velocity2))))
    assert_state_close(dc.heun_step(state, u, y, 0.03), expected)
    assert_state_close(state, before, atol=0, rtol=0)
    return {"maximum_folded_full_rhs_discrepancy": largest,
            "diagonal_initializer_off_diagonal_update_norm": float(np.linalg.norm(off_diagonal))}


def test_heun_order_and_stopping():
    state, u, y = problem()
    T = 0.8
    reference = dc.integrate(state, u, y, time_cap=T, dt=0.00125,
                             method="rk4", check_interval=1000).state
    errors = []
    for h in (0.08, 0.04, 0.02, 0.01):
        result = dc.integrate(state, u, y, time_cap=T, dt=h,
                              method="heun", check_interval=1000)
        assert abs(result.time - T) < 1e-14
        assert result.stop_reason == "time_cap"
        errors.append(distance(result.state, reference))
    ratios = [errors[i] / errors[i+1] for i in range(len(errors)-1)]
    assert min(ratios) > 3.5 and max(ratios) < 4.6, (errors, ratios)
    h = 0.03
    initial_loss = loss(state, u, y)
    first = dc.heun_step(state, u, y, h)
    first_loss = loss(first, u, y)
    assert first_loss < initial_loss
    threshold = (initial_loss + first_loss) / 2
    stopped = dc.integrate(state, u, y, time_cap=0.12, dt=h,
                            target_train_mse=threshold, check_interval=99,
                            stop_at_target=True)
    continued = dc.integrate(state, u, y, time_cap=0.12, dt=h,
                              target_train_mse=threshold, check_interval=99,
                              stop_at_target=False)
    frequent = dc.integrate(state, u, y, time_cap=0.12, dt=h,
                             target_train_mse=threshold, check_interval=1,
                             stop_at_target=False)
    assert stopped.first_target_step == 1 and stopped.steps == 1
    assert stopped.first_target_bracket == (0.0, h)
    assert stopped.stop_reason == "target"
    assert abs(continued.time - 0.12) < 1e-14
    assert continued.first_target_step == 1
    assert_state_close(continued.state, frequent.state, atol=0, rtol=0)
    assert_state_close(stopped.state, first, atol=0, rtol=0)
    shortened = dc.integrate(state, u, y, time_cap=0.31, dt=0.07,
                              method="heun", check_interval=99)
    manual = state.copy()
    for step in (0.07, 0.07, 0.07, 0.07, 0.03):
        manual = dc.heun_step(manual, u, y, step)
    assert_state_close(shortened.state, manual)
    assert shortened.steps == 5 and abs(shortened.time - 0.31) < 1e-14
    return {"short_time": T, "heun_steps": [0.08, 0.04, 0.02, 0.01],
            "errors_against_small_step_rk4": errors, "successive_error_ratios": ratios,
            "target_check_every_accepted_step": True,
            "history_interval_independence": True,
            "shortened_last_step_verified": True}


def main():
    paths = {"dense_compare.py": CORE, "finite_network.py": ORACLE,
             "check_dense_compare.py": Path(__file__).resolve()}
    hashes = {name: digest(path) for name, path in paths.items()}
    results = []
    for test in (test_oracle_and_directional_derivatives, test_initializers,
                 test_antipodes_and_dense_updates, test_heun_order_and_stopping):
        try:
            results.append({"name": test.__name__, "status": "PASS", "details": test()})
        except Exception:
            results.append({"name": test.__name__, "status": "FAIL", "traceback": traceback.format_exc()})
    unchanged = all(digest(path) == hashes[name] for name, path in paths.items())
    results.append({"name": "audited_sources_unchanged_during_check",
                    "status": "PASS" if unchanged else "FAIL"})
    report = {"purpose": "Deterministic correctness verification; no training campaign",
              "python": sys.version, "numpy": np.__version__,
              "source_sha256": hashes, "tests": results,
              "status": "PASS" if all(r["status"] == "PASS" for r in results) else "FAIL"}
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "report": str(REPORT),
                      "source_sha256": hashes,
                      "tests": [{"name": r["name"], "status": r["status"]} for r in results]}, indent=2))
    for result in results:
        if result["status"] == "FAIL":
            print(result.get("traceback", "Source changed during verification"))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
