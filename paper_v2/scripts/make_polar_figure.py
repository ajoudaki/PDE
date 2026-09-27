"""Render a paper-only polar view from frozen circle predictions.

This script performs no training.  The signed network output f(theta) is shown
at radius 2 + f(theta), so the radial tick labels can still report f.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data/generated/neural_response_memory_20260922"
OUT = ROOT / "paper_v2/figures/circle_polar_center_edges.pdf"


def load(path: Path):
    with np.load(path) as data:
        return {key: np.array(data[key]) for key in data.files}


dense = load(
    DATA / "dense_reference01/quadrant_center_edges_full_level2/arrays.npz"
)
closures = {
    order: load(
        DATA
        / f"orthogonal_refined01/quadrant_center_edges_orthogonal_P{order}_level1/arrays.npz"
    )
    for order in (1, 3, 7)
}

theta = dense["endpoint_angles"]
offset = 2.0
fig, ax = plt.subplots(figsize=(7.6, 6.2), subplot_kw={"projection": "polar"})
ax.plot(theta, offset + dense["endpoint_prediction"], color="black", lw=2.5, label="dense")
colors = {1: "#2878B5", 3: "#F28E2B", 7: "#2CA02C"}
for order, record in closures.items():
    ax.plot(
        record["endpoint_angles"],
        offset + record["endpoint_prediction"],
        lw=1.7,
        color=colors[order],
        label=f"P={order}",
    )

train_theta = np.mod(np.arctan2(dense["training_inputs"][:, 1], dense["training_inputs"][:, 0]), 2 * np.pi)
ax.scatter(
    train_theta,
    offset + dense["labels"],
    marker="x",
    s=48,
    linewidths=1.8,
    color="black",
    label="training labels",
    zorder=5,
)
ax.set_theta_zero_location("E")
ax.set_theta_direction(1)
ax.set_rticks([1.0, 2.0, 3.0])
ax.set_yticklabels(["-1", "0", "+1"])
ax.set_rlim(0.55, 3.45)
ax.set_rlabel_position(135)
ax.grid(alpha=0.32)
ax.set_title(
    "Learned function around the circle\n"
    "quadrant center/edges; radius = 2 + network output",
    pad=22,
)
ax.legend(loc="center left", bbox_to_anchor=(1.03, 0.50), frameon=True)
fig.subplots_adjust(left=0.05, right=0.76, top=0.86, bottom=0.06)
OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, bbox_inches="tight")
fig.savefig(OUT.with_suffix(".png"), dpi=220, bbox_inches="tight")
