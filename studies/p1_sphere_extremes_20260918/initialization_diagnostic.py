"""Preregistered Gaussian-initialization diagnostic; not an error certificate."""
import json
import platform
from pathlib import Path
import numpy as np


def evaluate(order):
    roots, weights = np.polynomial.hermite.hermgauss(order)
    roots = roots * np.sqrt(2)
    weights = weights / np.sqrt(np.pi)
    h = np.tanh(roots)
    nu = weights @ (h * h)
    upper = np.tanh(np.sqrt(nu) * roots)
    tau = weights @ (upper * upper)
    alpha = 1 - tau
    k = np.tanh(np.sqrt(tau) * roots[None, :] + alpha * h[:, None])
    conditional_k = k @ weights
    second = (k * k) @ weights
    s = weights @ second
    beta = weights @ (h * conditional_k)
    gamma = 1 - s
    eta = 1 / 4096
    a = np.sqrt(nu + eta)
    b = np.sqrt(s + eta - beta**2 / (nu + eta))
    c = np.sqrt(tau + eta)
    d_h = alpha * nu / (a * c)
    d_k = (alpha * beta * eta / (nu + eta) + tau * gamma) / (b * c)
    coef_h = d_h / a - d_k * beta / ((nu + eta) * b)
    coef_k = d_k / b
    conditional_target = np.tanh(
        roots[:, None] / np.sqrt(3) + np.sqrt(2 / 3) * roots[None, :]
    ) @ weights
    effective_component = weights @ (
        (coef_h * h + coef_k * conditional_k) * conditional_target
    )
    return dict(order=order, nu=float(nu), tau=float(tau), s=float(s),
                beta=float(beta), coefficient_h=float(coef_h),
                coefficient_k=float(coef_k),
                Z0=float(np.sqrt(3) * effective_component),
                lower_radicand=float(b * b))


if __name__ == "__main__":
    output = dict(python=platform.python_version(), numpy=np.__version__,
                  results=[evaluate(n) for n in (64, 128, 256)])
    target = Path("data/generated/p1_sphere_extremes_20260918")
    target.mkdir(parents=True, exist_ok=True)
    (target / "initialization_diagnostic.json").write_text(
        json.dumps(output, indent=2) + "\n"
    )
    print(json.dumps(output, indent=2))
