"""Plot the completed seed-zero clustered-cosine-9 width checks; no training."""
import json
import math
from pathlib import Path

import numpy as np
from reportlab.graphics import renderPDF, renderPM
from reportlab.graphics.shapes import Circle, Drawing, Line, Rect, String
from reportlab.lib.colors import HexColor


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "data/generated/structured_full_rank_scalar_20260926"
OUT = BASE / "cluster_wide_stopped8192_plot_20260926"
TASK = "cluster_triple_cos9"


def load_values():
    rows = []
    for width, folder in [
        (2048, "wide_hd_analysis_20260926"),
        (4096, "wide_hd_cluster4096_analysis_20260926"),
    ]:
        summary = json.loads((BASE / folder / "summary.json").read_text())
        row = next(r for r in summary["per_seed"] if r["task"] == TASK and r["seed"] == 0)
        assert row["all_fitted"]
        rows.append((width, row["HD_G"], row["G2_G"]))
    folder = BASE / "wide_hd_two_tasks8192_20260926"
    predictions = {}
    for method in ("gaussian", "gaussian_control", "hd"):
        stem = f"{TASK}__n8192__s00__{method}"
        metadata = json.loads((folder / (stem + ".json")).read_text())
        assert metadata["fitted"] and metadata["status"] == "ok"
        with np.load(folder / (stem + ".npz")) as saved:
            predictions[method] = saved["prediction"]
    rms = lambda method: float(np.sqrt(np.mean((predictions[method] - predictions["gaussian"]) ** 2)))
    rows.append((8192, rms("hd"), rms("gaussian_control")))
    return rows


def main():
    rows = load_values()
    OUT.mkdir(parents=True, exist_ok=True)
    drawing = Drawing(900, 650)
    drawing.add(Rect(0, 0, 900, 650, fillColor=HexColor("#ffffff"), strokeColor=None))
    drawing.add(String(55, 610, "Clustered cosine 9: fitted-function discrepancy", fontName="Helvetica-Bold", fontSize=20))
    drawing.add(String(55, 583, "Absolute circle function RMS; no amplitude normalization", fontSize=13))
    left, bottom, width, height = 115, 150, 720, 365
    xmin, xmax = math.log10(1750), math.log10(9600)
    ymin, ymax = math.log10(.0017), math.log10(.065)
    x = lambda value: left + width * (math.log10(value) - xmin) / (xmax - xmin)
    y = lambda value: bottom + height * (math.log10(value) - ymin) / (ymax - ymin)
    grid = HexColor("#e1e5e9")
    for value in [2048, 4096, 8192]:
        drawing.add(Line(x(value), bottom, x(value), bottom + height, strokeColor=grid))
        drawing.add(String(x(value), bottom - 22, str(value), textAnchor="middle", fontSize=12))
    for value in [.002, .005, .01, .02, .05]:
        drawing.add(Line(left, y(value), left + width, y(value), strokeColor=grid))
        drawing.add(String(left - 12, y(value) - 4, f"{value:g}", textAnchor="end", fontSize=12))
    drawing.add(Line(left, bottom, left + width, bottom, strokeColor=HexColor("#5b6570")))
    drawing.add(Line(left, bottom, left, bottom + height, strokeColor=HexColor("#5b6570")))
    drawing.add(String(left, bottom + height + 15, "RMS difference (log scale)", fontSize=12))
    drawing.add(String(left + width / 2, bottom - 49, "Network width n (log scale)", textAnchor="middle", fontSize=13))
    for index, color, label, legend_x in [
        (1, "#6A3D9A", "HD - Gaussian", 200),
        (2, "#0072B2", "Gaussian control - Gaussian", 460),
    ]:
        color = HexColor(color)
        points = [(x(row[0]), y(row[index])) for row in rows]
        for p, q in zip(points, points[1:]):
            drawing.add(Line(*p, *q, strokeColor=color, strokeWidth=2))
        for px, py in points:
            drawing.add(Circle(px, py, 5, fillColor=color, strokeColor=color))
        drawing.add(Line(legend_x, 553, legend_x + 27, 553, strokeColor=color, strokeWidth=3))
        drawing.add(String(legend_x + 36, 549, label, fontSize=12))
    drawing.add(String(55, 58, "One paired seed (seed 0) at each width; all models stopped at training MSE 1e-4.", fontSize=11))
    drawing.add(String(55, 38, "Lines connect observed points. The stopped n=8192 campaign completed this task only.", fontSize=11))
    renderPM.drawToFile(drawing, str(OUT / "cluster_width_errors.png"), fmt="PNG", dpi=72)
    renderPDF.drawToFile(drawing, str(OUT / "cluster_width_errors.pdf"))
    print(json.dumps({"plot": str(OUT / "cluster_width_errors.png"), "rows_n_HD_G_G2_G": rows}, indent=2))


if __name__ == "__main__":
    main()
