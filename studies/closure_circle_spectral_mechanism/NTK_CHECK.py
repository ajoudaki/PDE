"""Reproduce the bounded deterministic baseline checks into a fresh directory."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import subprocess
import sys
import time

import numpy as np
import scipy
from scipy.linalg import expm
from scipy.special import roots_hermitenorm

from NTK import kernel, kernel_decrement, predict, sample_kernel_power


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def conditional_covariance(rho, variance, nodes=192):
    # Independent Cholesky-style parametrization of the same Gaussian pair.
    z, w = roots_hermitenorm(nodes)
    w = w / np.sqrt(2 * np.pi)
    u = np.sqrt(variance) * z[:, None]
    v = np.sqrt(variance) * (rho * z[:, None] + np.sqrt(max(0, 1-rho*rho)) * z[None, :])
    return float(w @ (np.tanh(u) * np.tanh(v)) @ w)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    study = Path(__file__).resolve().parent
    root = study.parent.parent
    generated = root / "data/generated/closure_circle_spectral_mechanism"
    if not output.is_relative_to(generated):
        raise ValueError("output must be in this study's generated namespace")
    output.mkdir(parents=True, exist_ok=False)
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    start_cpu, start_wall = time.process_time(), time.perf_counter()
    measurements, gates = {}, {}

    def gate(name, value, tolerance):
        measurements[name] = float(value)
        gates[name] = bool(np.isfinite(value) and value <= tolerance)

    separations = np.array([0, 1e-4, 1e-3, .02, .05, .2, .6, np.pi/2, np.pi-1e-4, np.pi])
    values = {n: kernel(separations, n) for n in [48, 96, 128, 192]}
    for low, high in [(48, 96), (96, 128)]:
        measurements[f"kernel_{low}_{high}_max_absolute_change"] = float(np.max(np.abs(values[low]-values[high])))
    gate("kernel_128_192_max_absolute_change", np.max(np.abs(values[128]-values[192])), 2e-10)
    tiny = separations[1:4]
    stable128, stable192 = kernel_decrement(tiny, 128), kernel_decrement(tiny, 192)
    gate("stable_decrement_128_192_max_relative_change", np.max(np.abs(stable128/stable192-1)), 2e-7)
    measurements["direct_vs_stable_decrement_relative_error"] = (
        np.abs((kernel(0, 128)-kernel(tiny, 128))/stable128-1).tolist())
    measurements["tiny_separations"] = tiny.tolist()
    measurements["tiny_stable_decrements"] = stable128.tolist()

    panel = sample_kernel_power(1024, 128)
    coefficients, modes = panel["coefficients"], panel["modes"]
    gate("kernel_fourier_imaginary_leakage", np.max(np.abs(coefficients.imag)), 2e-10)
    gate("kernel_even_fourier_leakage", np.max(np.abs(coefficients[modes % 2 == 0])), 2e-10)
    # For a stationary panel, its circulant Gram eigenvalues are M*khat_m.
    gate("kernel_normalized_circulant_negative_eigenvalue", max(0., -float(coefficients.real.min())), 2e-10)
    phi = np.linspace(-np.pi, np.pi, 129)
    gate("kernel_mirror_error", np.max(np.abs(kernel(phi)-kernel(-phi))), 2e-10)
    gate("kernel_antipodal_error", np.max(np.abs(kernel(phi)+kernel(phi+np.pi))), 2e-10)

    z, w = roots_hermitenorm(192)
    q192 = float((w/np.sqrt(2*np.pi)) @ np.tanh(z)**2)
    independent = []
    for angle in [.001, .2, .8, 1.3, 2.7]:
        inner = conditional_covariance(np.cos(angle), 1.)
        independent.append(abs(conditional_covariance(inner/q192, q192)-float(kernel(angle))))
    gate("independent_parameterization_max_discrepancy", max(independent), 2e-10)

    interpolation_errors, flow_errors = [], []
    for train, target, probability in [
        ([-.3, .3], [-1, 1], [.5, .5]),
        ([-.9, .1, 1.2], [-1, .5, 1], [.2, .3, .5]),
        ([-1.3, -.2, .5, 1.6], [-1, 1, -.5, .8], [.1, .2, .3, .4]),
    ]:
        train, target, probability = map(np.asarray, (train, target, probability))
        gram = kernel(train[:, None]-train[None, :])
        gate(f"gram_{train.size}_negative_eigenvalue", max(0., -np.linalg.eigvalsh(gram)[0]), 2e-10)
        interpolation_errors.append(np.max(np.abs(predict(train, target, train, weights=probability)-target)))
        for t in [0, .03, 1.5, 40.]:
            independent_train = target-expm(-2*t*gram @ np.diag(probability)) @ target
            flow_errors.append(np.max(np.abs(predict(train, target, train, t=t, weights=probability)-independent_train)))
    gate("training_interpolation_max_residual", max(interpolation_errors), 2e-9)
    gate("weighted_matrix_exponential_max_discrepancy", max(flow_errors), 2e-9)

    pair_formula_errors, pair_spectrum_errors, pair_odd_errors, pair_loss_errors = [], [], [], []
    for separation in [.3, 1.2, 2.7, np.pi]:
        train, target = np.array([-separation/2, separation/2]), np.array([-1., 1.])
        denominator = kernel(0)-kernel(separation)
        query = panel["angles"]
        formula = (kernel(query-separation/2)-kernel(query+separation/2))/denominator
        endpoint = predict(train, target, query)
        pair_formula_errors.append(np.max(np.abs(endpoint-formula)))
        expected_coefficients = -2j*coefficients*np.sin(modes*separation/2)/denominator
        pair_spectrum_errors.append(np.max(np.abs(np.fft.fft(endpoint)/len(query)-expected_coefficients)))
        pair_odd_errors.append(np.max(np.abs(predict(train, target, phi)+predict(train, target, -phi))))
        for t in [.3, 8.]:
            pair_formula_errors.append(np.max(np.abs(predict(train, target, query, t=t)-(-np.expm1(-denominator*t))*formula)))
            numerical_loss = np.mean((predict(train, target, train, t=t)-target)**2)
            pair_loss_errors.append(abs(numerical_loss-np.exp(-2*denominator*t)))
    gate("pair_closed_form_max_discrepancy", max(pair_formula_errors), 2e-9)
    gate("pair_fourier_formula_max_discrepancy", max(pair_spectrum_errors), 2e-9)
    gate("pair_mirror_odd_max_error", max(pair_odd_errors), 2e-10)
    gate("pair_physical_loss_formula_max_discrepancy", max(pair_loss_errors), 2e-9)
    gate("duplicate_consistent_interpolation_error", np.max(np.abs(predict([.2, .2], [1., 1.], [.2])-1)), 2e-9)
    gate("antipodal_consistent_interpolation_error", np.max(np.abs(predict([0., np.pi], [1., -1.], [0., np.pi])-[1., -1.])), 2e-9)
    try:
        predict([.2, .2], [1., -1.], [.2])
    except ValueError:
        gates["conflicting_duplicate_endpoint_rejected"] = True
    else:
        gates["conflicting_duplicate_endpoint_rejected"] = False
    gate("conflicting_duplicate_finite_time_zero", np.max(np.abs(predict([.2, .2], [1., -1.], phi, t=2.))), 2e-9)

    data_file = output / "kernel_panel.npz"
    np.savez_compressed(data_file, **panel, separations=separations,
                        kernel48=values[48], kernel96=values[96],
                        kernel128=values[128], kernel192=values[192],
                        tiny_separations=tiny, tiny_decrements128=stable128,
                        tiny_decrements192=stable192)
    measurements["first_positive_odd_complex_coefficients"] = {
        str(mode): float(coefficients[mode].real) for mode in range(1, 20, 2)}
    sources = [study/"NTK.py", study/"NTK_THEORY.md", study/"NTK_CHECK.py",
               root/"code/pde/finite_network.py", root/"docs/NOTATION.md",
               root/"code/README.md", root/"docs/global_nonlinear.md"]
    result = {
        "status": "PASS" if all(gates.values()) else "FAIL",
        "claim": "Deterministic finite-rule checks only; no interval error or nonlinear closure conclusion.",
        "gates": gates, "measurements": measurements,
        "cpu_seconds": time.process_time()-start_cpu,
        "wall_seconds": time.perf_counter()-start_wall,
        "command": [sys.executable, *sys.argv], "cwd": os.getcwd(),
        "source_sha256": {str(path.relative_to(root)): digest(path) for path in sources},
        "head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip(),
        "python": sys.version, "numpy": np.__version__, "scipy": scipy.__version__,
        "platform": platform.platform(), "processor": platform.processor(),
        "threads": {name: os.environ.get(name) for name in
                    ["OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"]},
        "precision": "float64", "random_seed": None,
        "output_sha256": {data_file.name: digest(data_file)},
        "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "limits": {"cpu_seconds": 60, "generated_output_bytes": 10*1024*1024},
    }
    result_path = output / "check.json"
    result_path.write_text(json.dumps(result, indent=2)+"\n")
    generated_bytes = sum(path.stat().st_size for path in output.iterdir())
    if generated_bytes > 10*1024*1024:
        raise RuntimeError("Generated output exceeded 10 MiB")
    print(json.dumps({"status": result["status"], "gates": gates,
                      "measurements": measurements, "cpu_seconds": result["cpu_seconds"],
                      "output": str(output), "generated_bytes": generated_bytes}, indent=2))
    return 0 if all(gates.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
