"""Small CPU algebra and implementation checks; no learning experiment."""
import json
import math

import torch

from pde.finite_torch import NetworkEngine
from new_dictionary import build, raw_features


def main():
    torch.set_num_threads(1)
    errors = {}

    def compare(name, actual, expected, tolerance=3e-12):
        error = float(torch.max(torch.abs(actual - expected)))
        scale = max(1.0, float(torch.max(torch.abs(expected))))
        errors[name] = max(errors.get(name, 0.0), error)
        if error > tolerance * scale:
            raise AssertionError(f"{name}: {error} exceeds {tolerance * scale}")

    ranks = []
    for seed in (9, 41):
        finite = NetworkEngine(2, 37, seed, device="cpu", dtype=torch.float64)
        initial = finite.initial_state()
        initial_copies = initial.clone()
        lower1, upper1, _ = raw_features(initial, 1)
        lower2, upper2, _ = raw_features(initial, 2)
        compare("level_1_2_lower_identity", lower1, lower2, tolerance=0.0)
        compare("level_1_2_upper_identity", upper1, upper2, tolerance=0.0)
        lower, upper, metadata = raw_features(initial, 3)
        assert lower.shape == (37, 6) and upper.shape == (37, 12)
        v = metadata["v"]
        # Rebuild all fields independently of the candidate's private helpers.
        h = torch.tanh(initial.w)
        H = torch.tanh(initial.M @ h)
        D = 1 - H * H
        E = -2 * H * D
        U = torch.stack([H[:, b] * D[:, a] for a in range(2) for b in range(2)], dim=1)
        L = torch.stack([(1 - h[:, a] ** 2) ** 2 * (initial.M.T @ U[:, 2 * a + b])
                         for a in range(2) for b in range(2)], dim=1)
        F = v * U + initial.M @ L
        compare("independent_lower_fields", lower, torch.cat((h, L), dim=1))
        compare("independent_base_upper", upper[:, :4], U)

        for label_values in ((1.0, 0.0), (0.0, -1.4), (0.7, -1.2), (-0.3, 2.1), (0.0, 0.0)):
            y = torch.tensor(label_values, dtype=torch.float64)
            S = H @ y
            V = torch.stack([0.5 * y[a] * sum(y[b] * L[:, 2 * a + b] for b in range(2))
                             for a in range(2)], dim=1)
            R = torch.stack([0.5 * v * y[a] * S * D[:, a] + initial.M @ V[:, a]
                             for a in range(2)], dim=1)
            R_from_F = torch.stack([0.5 * y[a] * sum(y[b] * F[:, 2 * a + b] for b in range(2))
                                    for a in range(2)], dim=1)
            compare("normalized_probe_F_coefficient", R_from_F, R)
            J = sum(y[b] * D[:, b] * R[:, b] for b in range(2))
            expected = torch.stack([y[a] * (J * D[:, a] / 3 + S * E[:, a] * R[:, a])
                                    for a in range(2)], dim=1)
            monomials = torch.tensor([y[0] ** (4 - j) * y[1] ** j for j in range(5)])
            actual = torch.stack((upper[:, 4:8] @ monomials[:4],
                                  upper[:, 8:12] @ monomials[1:]), dim=1) / 6
            compare("collected_quartic_upper_coefficients", actual, expected)
            direct_feedback = sum(torch.outer(expected[:, a], h[:, a])
                                  + torch.outer(y[a] * S * D[:, a], V[:, a]) for a in range(2))
            collected_feedback = sum(torch.outer(actual[:, a], h[:, a])
                                     + sum(0.5 * y[a] ** 2 * y[b] * y[c]
                                           * torch.outer(U[:, 2 * a + c], L[:, 2 * a + b])
                                           for b in range(2) for c in range(2)) for a in range(2))
            compare("complete_cubic_feedback_tensor", collected_feedback, direct_feedback)

        for p in (1, 2, 3):
            engine, state, info = build(initial, p, block_size=3)
            raw1, raw2, _ = raw_features(initial, p)
            n = initial.w.shape[0]
            eta = info["eta"]
            filters = []
            for raw in (raw1, raw2):
                gram = raw.T @ raw / n
                identity = torch.eye(raw.shape[1], dtype=raw.dtype, device=raw.device)
                filters.append(raw @ torch.linalg.solve(gram + eta * identity, raw.T) / n)
            expected_middle = filters[1] @ initial.M @ filters[0]
            lifted_middle = engine.b2 @ state.M @ engine.b1.T / n
            compare("direct_filtered_initial_middle", lifted_middle, expected_middle)
            compare("preserved_finite_readout", state.c, initial.c, tolerance=0.0)
            compare("preserved_finite_readin", state.w, initial.w, tolerance=0.0)
            panel = torch.tensor([[1.0, 0.0], [0.6, 0.8], [-math.sqrt(0.5), math.sqrt(0.5)], [0.0, -1.0]], dtype=torch.float64)
            expected_output = initial.c @ torch.tanh(expected_middle @ torch.tanh(initial.w @ panel.T)) / n
            compare("direct_initial_prediction", engine.predict(state, panel), expected_output)
            data = engine.prepare_data(panel, torch.tensor([0.4, -0.8, 0.1, 1.3], dtype=torch.float64))
            # Independent autograd differentiates the current nonlinear model.
            w, c, M = (x.detach().clone().requires_grad_(True) for x in (state.w, state.c, state.M))
            h_current = torch.tanh(w @ panel.T)
            a_current = engine.b1.T @ h_current / n
            H_current = torch.tanh(engine.b2 @ (M @ a_current))
            output = c @ H_current / n
            loss = torch.mean((output - data.labels) ** 2)
            gradients = torch.autograd.grad(loss, (w, c, M))
            velocity = engine.rhs(state, data)
            for name, observed, gradient, mobility in zip(("w", "c", "M"),
                    (velocity.w, velocity.c, velocity.M), gradients, (n, n, 1)):
                compare("autograd_velocity_" + name, observed, -mobility * gradient)
            for side in ("lower", "upper"):
                assert info[side]["ridge_identity_residual_frobenius"] < 2e-11
                assert info[side]["cholesky_relative_residual"] < 2e-14
                assert info[side]["triangular_relative_residual"] <= 1e-8
                assert info[side]["ridge_condition"] <= 1e10
            ranks.append({"seed": seed, "p": p, "K1": info["K1"], "K2": info["K2"],
                          "lower_rank": info["lower"]["raw_numerical_rank"],
                          "upper_rank": info["upper"]["raw_numerical_rank"]})
        for name in ("w", "c", "M"):
            compare("initial_state_unmodified_" + name, getattr(initial, name), getattr(initial_copies, name), tolerance=0.0)

    print(json.dumps({"status": "PASS", "scope": "small CPU algebra checks; no training or exact finite-jet claim",
                      "maximum_absolute_errors": errors, "ranks": ranks,
                      "v": metadata["v"], "v_128": metadata["v_128"],
                      "v_quadrature_absolute_discrepancy": metadata["v_quadrature_absolute_discrepancy"]}, indent=2))


if __name__ == "__main__":
    main()
