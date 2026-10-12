"""Independent finite-network derivatives; no manuscript/compiler imports."""
import json
import numpy as np

rng = np.random.default_rng(170319)
gram = np.eye(2)
y = np.ones(2)
records = []
for n, repeats in [(64, 1000), (128, 600), (256, 300), (512, 120)]:
    values = []
    for _ in range(repeats):
        v = rng.standard_normal((n, 2))
        W = rng.standard_normal((n, n)) / np.sqrt(n)
        w = rng.standard_normal(n)
        z = W @ v
        delta = y - w @ z / n
        s = v @ delta / 2
        lam = gram @ delta / 2
        vdot = (W.T @ w)[:, None] * lam
        Wdot = np.outer(w, s) / n
        wdot = W @ s
        zdot = Wdot @ v + W @ vdot
        deltadot = -(wdot @ z + w @ zdot) / n
        sdot = (vdot @ delta + v @ deltadot) / 2
        lamdot = gram @ deltadot / 2
        vddot = ((Wdot.T @ w + W.T @ wdot)[:, None] * lam
                 + (W.T @ w)[:, None] * lamdot)
        Wddot = (np.outer(wdot, s) + np.outer(w, sdot)) / n
        zddot = Wddot @ v + 2 * Wdot @ vdot + W @ vddot
        kernel_jet = (zdot.T @ zdot
                      + (zddot.T @ z + z.T @ zddot) / 2) / n
        values.append(float(kernel_jet[0, 1]))
    records.append({"n": n, "repeats": repeats, "mean_J2": np.mean(values),
                    "standard_error": np.std(values, ddof=1) / np.sqrt(repeats)})
print(json.dumps({"gram": gram.tolist(), "labels": y.tolist(),
                  "full_response_limit_J2": 2.25,
                  "printed_P4_limit_J2": 1.0,
                  "results": records}, indent=2))
