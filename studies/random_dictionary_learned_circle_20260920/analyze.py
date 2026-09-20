"""Recompute endpoint metrics on GPU from retained, unfitted-to-test outputs."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import numpy as np
import torch
from benchmark import setup, CASES, save_json

MODELS = [f"{method}_p{p}" for p in (1, 3) for method in ("ours", "gaussian", "orthogonal")]


def tensor(x, device):
    return torch.as_tensor(x.copy(), device=device, dtype=torch.float64)


@torch.no_grad()
def evaluate_saved(saved, device):
    w, c, M = [tensor(saved[k][-1], device) for k in ("w", "c", "M")]
    u = tensor(saved["endpoint_inputs"], device)
    result = []
    if "b1" in saved:
        b1, b2 = [tensor(saved[k], device) for k in ("b1", "b2")]
    for batch in u.split(256):
        h1 = (w @ batch.T).tanh()
        z2 = b2 @ (M @ (b1.T @ h1 / len(w))) if "b1" in saved else M @ h1
        result.append(c @ z2.tanh() / len(c))
    return torch.cat(result)


def markdown_table(rows, field):
    header = "| Training configuration | " + " | ".join(MODELS) + " |\n"
    header += "|---|" + "---:|" * len(MODELS) + "\n"
    for case in CASES:
        cells = []
        for model in MODELS:
            r = next(row for row in rows if row["case"] == case and row["model"] == model)
            cells.append(f'{r[field]:.5f}' if r["eligible"] else f'not fitted (loss {r["loss"]:.3g})')
        header += "| " + case + " | " + " | ".join(cells) + " |\n"
    return header


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--refined", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    device = setup()
    args.out.mkdir(parents=True, exist_ok=False)
    primary = json.loads((args.primary / "results.json").read_text())
    refined = json.loads((args.refined / "results.json").read_text())
    rows, validation, error_arrays = [], {}, {}
    loaded = {}
    for case in CASES:
        for model in ["full"] + MODELS:
            key = case + "_" + model
            pa = np.load(args.primary / key / "arrays.npz", allow_pickle=False)
            ra = np.load(args.refined / key / "arrays.npz", allow_pickle=False)
            f = tensor(pa["endpoint_prediction"], device)
            fr = tensor(ra["endpoint_prediction"], device)
            replay = evaluate_saved(pa, device)
            replay_error = float((f - replay).abs().max())
            assert replay_error < 1e-10, (key, replay_error)
            validation[key] = {
                "checkpoint_replay_max": replay_error,
                "step_refinement_endpoint_max": float((f-fr).abs().max()),
                "primary_fit": primary[key]["status"], "refined_fit": refined[key]["status"],
                "refined_loss": refined[key]["loss"], "refined_time": refined[key]["time"],
            }
            loaded[key] = (pa, f, fr)
        ref, full, full_refined = loaded[case + "_full"]
        error_arrays[case + "_angles"] = ref["endpoint_angles"]
        for model in MODELS:
            key = case + "_" + model
            saved, f, fr = loaded[key]
            error, er = f - full, fr - full_refined
            eabs = error.abs()
            summary = primary[key]
            eligible = (summary["status"] == "fitted" and primary[case + "_full"]["status"] == "fitted")
            stable = all(validation[k]["step_refinement_endpoint_max"] <= .01 and
                         validation[k]["refined_fit"] == "fitted" for k in (key, case + "_full"))
            row = dict(case=case, model=model, eligible=eligible, numerically_stable=stable,
                       l1=float(eabs.mean()), l2=float(error.square().mean().sqrt()),
                       mse=float(error.square().mean()), max_abs=float(eabs.max()),
                       refined_l2=float(er.square().mean().sqrt()), refined_max_abs=float(er.abs().max()),
                       grid_max_change=float(eabs.max()-eabs[::2].max()),
                       grid_l2_change=float((error.square().mean().sqrt()-error[::2].square().mean().sqrt()).abs()),
                       loss=summary["loss"], time=summary["time"], seconds=summary["seconds"],
                       rms1=summary["rms_hidden1"], rms2=summary["rms_hidden2"])
            rows.append(row)
            error_arrays[key + "_signed_error"] = error.cpu().numpy()
            error_arrays[key + "_absolute_error"] = eabs.cpu().numpy()
    save_json(args.out / "metrics.json", rows)
    save_json(args.out / "validation.json", validation)
    np.savez(args.out / "circle_errors.npz", **error_arrays)
    with (args.out / "metrics.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    report = "# Endpoint approximation at training MSE 1e-3\n\n"
    report += "Each predictor is evaluated at its own threshold crossing. Reference: the same uncompressed width-512 network.\n\n"
    report += "## Circle RMS error\n\n" + markdown_table(rows, "l2")
    report += "\n## Maximum absolute error on 8192 circle angles\n\n" + markdown_table(rows, "max_abs")
    report += "\nL1, MSE, training losses/times, hidden motion, refined-step errors and nested-grid checks are in metrics.csv.\n"
    report += "Continuous-circle suprema are not certified. These are one-seed finite-carrier dictionary comparisons; no population-limit or universal superiority claim.\n"
    report += f"\nLargest endpoint step-refinement discrepancy: {max(v['step_refinement_endpoint_max'] for v in validation.values()):.6g}.\n"
    report += f"All 12 endpoint comparisons pass fit and numerical gates: {all(r['eligible'] and r['numerically_stable'] for r in rows)}.\n"
    (args.out / "tables.md").write_text(report)

    # Rendering is CPU-only; all simulation and metric calculations above are CUDA.
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    colors = {"ours": "#1261a0", "gaussian": "#ce6c1b", "orthogonal": "#7d4196"}
    for case in CASES:
        fig, axes = plt.subplots(2, 2, figsize=(12, 7), sharex=True)
        ref, fref, _ = loaded[case + "_full"]
        angle = ref["endpoint_angles"] * 180 / np.pi
        for col, p in enumerate((1, 3)):
            axes[0, col].plot(angle, fref.cpu().numpy(), color="black", label="Full network", lw=2)
            axes[0, col].scatter(*CASES[case], color="black", marker="x", zorder=5, label="Training samples")
            for method in ("ours", "gaussian", "orthogonal"):
                key = f"{case}_{method}_p{p}"
                _, f, _ = loaded[key]
                axes[0, col].plot(angle, f.cpu().numpy(), color=colors[method], label=method, lw=1.2)
                axes[1, col].plot(angle, (f-fref).abs().cpu().numpy(), color=colors[method], label=method, lw=1.2)
            axes[0, col].set_title(f"{case} inputs; p={p} feature budget")
            axes[0, col].set_ylabel("Learned prediction")
            axes[1, col].set_ylabel("Absolute prediction error")
            axes[1, col].set_xlabel("Circle angle (degrees)")
            axes[0, col].legend(fontsize=8)
            for ax in axes[:, col]:
                ax.grid(alpha=.2)
                ax.set_xlim(0, 360)
        fig.tight_layout()
        fig.savefig(args.out / f"{case}_circle.png", dpi=160)
        plt.close(fig)
    files = sorted(p for folder in (args.primary, args.refined, args.out) for p in folder.rglob("*") if p.is_file())
    save_json(args.out / "artifact_hashes.json", {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in files})
    print(report)


if __name__ == "__main__":
    main()
