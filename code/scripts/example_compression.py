"""Tiny executable data -> model -> static/interactive visualization example."""
import argparse
import hashlib
import json
from pathlib import Path
import platform

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import torch

from pde.compression import Dense, Legendre, harmonic, taylor, rollout, storage
from pde.compression_data import toy_data
from pde.prediction_views import plot_circle, plot_sphere, write_viewer


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True,
                        help="new output directory; existing paths are refused")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(1)
    times = [0., .02, .04]
    reports = []
    for dimension, geometry in ((2, "circle"), (3, "sphere")):
        data = toy_data(dimension=dimension, train_samples=4, query_samples=96,
                        seed=47, label_scale=.1)
        inputs, labels, queries = [torch.as_tensor(v, dtype=torch.float64) for v in
                                  (data.train_inputs, data.train_labels, data.query_inputs)]
        dense = Dense(64, dimension, depth=2, seed=17)
        models = {
            "Dense": dense,
            "Legendre": Legendre(dense, inputs, labels, order=3),
            "Harmonic": harmonic(dense, inputs, labels, horizon=.04, step_size=.01,
                                  rank=1, time_degree=2, spatial_degree=2, budget=48),
            "Taylor": taylor(dense, inputs, labels, queries, source_mode="jets",
                              rank=1, budget=48),
        }
        predictions, methods = {}, {}
        for name, model in models.items():
            state, values = rollout(model, inputs, labels, times, step_size=.01,
                                    queries=queries)
            predictions[name] = values.numpy()
            methods[name] = dict(provenance=model.provenance, storage=storage(model, state))
        np.savez_compressed(args.out / (geometry + ".npz"),
                            train_inputs=data.train_inputs, train_labels=data.train_labels,
                            query_inputs=data.query_inputs, query_labels=data.query_labels,
                            times=np.asarray(times), **predictions)
        if dimension == 2:
            figure = plot_circle(data.query_inputs, predictions, reference="Dense",
                                 training_inputs=data.train_inputs, training_labels=data.train_labels)
        else:
            figure = plot_sphere(data.query_inputs, predictions, model="Legendre",
                                 reference="Dense", training_inputs=data.train_inputs)
        for extension in ("png", "pdf"):
            figure.savefig(args.out / f"{geometry}.{extension}", dpi=130, bbox_inches="tight")
        plt.close(figure)
        write_viewer(args.out / (geometry + ".html"), data.query_inputs, predictions,
                     times=times, reference="Dense", training_inputs=data.train_inputs,
                     training_labels=data.train_labels,
                     title=f"{geometry.title()}: short numerical example")
        reports.append(dict(geometry=geometry, dataset=data.provenance, methods=methods))
    sources = [Path(__file__), *[Path(__file__).resolve().parents[1] / 'pde' / name for name in
               ("compression_data.py", "prediction_views.py", "compression.py")]]
    manifest = dict(
        purpose="Operational integration example, not an approximation experiment or theorem certificate",
        comparison="Same physical times; query-panel differences from the coupled Dense run",
        settings=dict(times=times, step_size=.01, width=64, depth=2, network_seed=17,
                      dataset_seed=47, label_scale=.1, samples=4, queries=96),
        environment=dict(python=platform.python_version(), numpy=np.__version__,
                         torch=torch.__version__, matplotlib=matplotlib.__version__, device="cpu"),
        datasets=reports,
        source_sha256={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
        outputs={p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                 for p in sorted(args.out.iterdir()) if p.is_file()},
    )
    (args.out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(args.out)


if __name__ == "__main__":
    main()
