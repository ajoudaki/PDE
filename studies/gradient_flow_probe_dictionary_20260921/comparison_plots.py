#!/usr/bin/env python3
"""Render saved comparison results without training or recomputing their metrics.

The CLI accepts only this study's generated analysis and a fresh output folder.
Raw endpoint/loss arrays may additionally come from the two explicitly authorized
archival runs.  All numerical comparison metrics are copied verbatim from the
GPU analysis.  NumPy is used only to read/validate saved samples for display.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


REPO = Path(__file__).resolve().parents[2]
GENERATED = REPO / "data/generated/gradient_flow_probe_dictionary_20260921"
ARCHIVE = REPO / "data/generated/random_dictionary_learned_circle_20260920"
RAW_ROOTS = (
    GENERATED,
    ARCHIVE / "scaling_width4096_primary01",
    ARCHIVE / "scaling_width4096_refined01",
)
CASES = ("quadrant_pairs", "two_outliers_alternating")
CASE_LABELS = {
    "quadrant_pairs": "Quadrant pairs",
    "two_outliers_alternating": "Two outliers, alternating",
}
COLORS = {"new": "#1874b5", "old": "#cb6a24", "full": "#444851"}
METHOD_LABELS = {"new": "New dictionary", "old": "Old dictionary", "full": "Dense network"}
LEVELS = ("primary", "refined")
ARRAY_KEYS = (
    "endpoint_angles", "endpoint_prediction", "times", "losses",
    "training_inputs", "labels",
)
TARGET = 1e-3


def _under(path: Path, root: Path) -> bool:
    return path == root or root in path.parents


def _hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _json_value(value: Any) -> Any:
    """Represent nonfinite saved values as null for standards-compliant HTML data."""
    if isinstance(value, dict):
        return {key: _json_value(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_value(item) for item in value]
    if isinstance(value, float) and not math.isfinite(value):
        return None
    return value


def _raw_path(value: str, analysis: Path) -> Path:
    path = Path(value)
    if not path.is_absolute():
        # Saved manifests normally use repository-relative paths; analysis-local
        # relative paths are also supported, without widening the allowed roots.
        alternatives = (REPO / path, analysis / path)
        path = next((item for item in alternatives if item.exists()), alternatives[0])
    if path.name != "arrays.npz":
        path = path / "arrays.npz"
    path = path.resolve(strict=True)
    if path.name != "arrays.npz" or not any(_under(path, root.resolve()) for root in RAW_ROOTS):
        raise ValueError(f"Raw input is outside the authorized run roots: {path}")
    return path


def _load_raw(path: Path) -> dict[str, Any]:
    with np.load(path, allow_pickle=False) as bundle:
        data = {key: np.array(bundle[key], copy=True) for key in ARRAY_KEYS}
    for key in ("endpoint_angles", "endpoint_prediction", "times", "losses", "labels"):
        if data[key].ndim != 1 or not data[key].size:
            raise ValueError(f"Expected nonempty one-dimensional {key}: {path}")
    if data["endpoint_angles"].shape != data["endpoint_prediction"].shape:
        raise ValueError(f"Mismatched endpoint samples: {path}")
    if data["times"].shape != data["losses"].shape:
        raise ValueError(f"Mismatched time/loss samples: {path}")
    if data["training_inputs"].shape != (len(data["labels"]), 2):
        raise ValueError(f"Expected two-dimensional circle training inputs: {path}")
    if any(not np.isfinite(value).all() for value in data.values()):
        raise ValueError(f"Nonfinite raw display samples: {path}")
    if np.any(np.diff(data["times"]) < 0) or np.any(np.diff(data["endpoint_angles"]) < 0):
        raise ValueError(f"Saved sample order must be monotone: {path}")
    data["path"] = str(path)
    # This is the saved event endpoint, not an estimated/interpolated crossing.
    data["endpoint_time"] = float(data["times"][-1])
    data["endpoint_loss"] = float(data["losses"][-1])
    data["at_target"] = math.isclose(data["endpoint_loss"], TARGET, rel_tol=1e-5, abs_tol=1e-10)
    return data


def load_inputs(analysis: Path) -> tuple[list[dict], dict, dict, list[Path]]:
    metrics_path, selected_path = analysis / "metrics.json", analysis / "selected_levels.json"
    metrics = json.loads(metrics_path.read_text())
    selected = json.loads(selected_path.read_text())
    if not isinstance(metrics, list):
        raise ValueError("metrics.json must contain a list of saved metric rows")
    if not isinstance(selected.get("cells"), dict):
        raise ValueError("selected_levels.json must contain a cells mapping")
    row_index = {(row["case"], row["method"]): row for row in metrics}
    required = {(case, f"{family}_p{p}") for case in CASES for family in ("new", "old") for p in (1, 2, 3)}
    if set(row_index) != required or len(metrics) != len(required):
        raise ValueError("Expected exactly the two cases and six new/old methods")
    for (case, method), row in row_index.items():
        expected = (6 if row["p"] in (1, 2) else 18) if method.startswith("new_") else {1: 8, 2: 21, 3: 45}[row["p"]]
        if row["vectors"] != expected:
            raise ValueError(f"Unexpected dictionary vector count for {case}/{method}")
    curves, inputs, cache = {}, [metrics_path, selected_path], {}
    for case in CASES:
        for method in ("new_p1", "new_p2", "new_p3", "old_p1", "old_p2", "old_p3", "full"):
            key = f"{case}_{method}"
            entry = selected["cells"][key]
            curves[key] = {}
            for level in LEVELS:
                path = _raw_path(entry[level]["path"], analysis)
                if path not in cache:
                    cache[path] = _load_raw(path)
                    inputs.append(path)
                curves[key][level] = cache[path]
    return metrics, selected, curves, inputs


def _style() -> Any:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 9, "axes.spines.top": False,
        "axes.spines.right": False, "axes.titleweight": "semibold",
        "axes.labelcolor": "#39404a", "text.color": "#202834",
        "axes.edgecolor": "#b5bdc7", "grid.color": "#e5e9ee",
        "savefig.facecolor": "white", "figure.facecolor": "white",
        "svg.fonttype": "none",
    })
    return plt


def plot_rms(metrics: list[dict], out: Path) -> None:
    plt = _style()
    from matplotlib.lines import Line2D
    from matplotlib.ticker import FuncFormatter, NullFormatter
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.25), sharex=True)
    for axis, case in zip(axes, CASES):
        for family in ("new", "old"):
            rows = sorted((row for row in metrics if row["case"] == case and row["method"].startswith(family + "_")), key=lambda row: row["p"])
            for level, marker, line in (("primary", "o", "-"), ("refined", "s", "--")):
                usable = [row for row in rows if isinstance(row.get(f"{level}_rms"), (int, float)) and math.isfinite(row[f"{level}_rms"]) and row[f"{level}_rms"] > 0]
                axis.plot([row["vectors"] for row in usable], [row[f"{level}_rms"] for row in usable], color=COLORS[family], marker=marker, ls=line, lw=1.45, ms=5, alpha=.9)
                if level == "primary":
                    for row in usable:
                        label = f"p={row['p']}" + (" ?" if not row["valid"] else "")
                        offset = (7, 7) if row["p"] != 2 or family == "old" else (7, -13)
                        axis.annotate(label, (row["vectors"], row[f"{level}_rms"]), xytext=offset, textcoords="offset points", fontsize=8, color=COLORS[family])
                for row in usable:
                    if not row["valid"]:
                        axis.scatter([row["vectors"]], [row[f"{level}_rms"]], marker="x", s=45, color="#a62c40", zorder=5)
        axis.set(title=CASE_LABELS[case], xlabel="Dictionary vectors", ylabel="RMS difference from dense network")
        axis.set_yscale("log")
        axis.set_ylim(.06, 3.2)
        axis.set_yticks([.1, .2, .5, 1, 2, 3])
        axis.yaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value:g}"))
        axis.yaxis.set_minor_formatter(NullFormatter())
        axis.set_xlim(0, 50)
        axis.set_xticks([0, 6, 8, 18, 21, 30, 40, 45])
        axis.tick_params(axis="x", labelsize=8)
        axis.grid(True, which="major", linewidth=.65)
    handles = [Line2D([0], [0], color=COLORS[family], lw=2, label=METHOD_LABELS[family]) for family in ("new", "old")]
    handles += [Line2D([0], [0], color="#5e6772", ls=line, marker=marker, label=level.title()) for level, line, marker in (("primary", "-", "o"), ("refined", "--", "s"))]
    fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(.5, .08), ncol=4, frameon=False)
    fig.suptitle("Endpoint approximation versus dictionary size", fontsize=13, y=.97)
    fig.text(.5, .89, "Each method uses its own training-MSE 10⁻³ endpoint; saved GPU RMS values", ha="center", fontsize=9)
    caption = "Linear vector-count axis · logarithmic RMS axis"
    if any(not row["valid"] for row in metrics):
        caption += " · × / ? = unresolved accuracy check"
    if any(not isinstance(row.get(f"{level}_rms"), (int, float)) or not math.isfinite(row[f"{level}_rms"]) or row[f"{level}_rms"] <= 0 for row in metrics for level in LEVELS):
        caption += " · zero/nonfinite RMS omitted"
    fig.text(.5, .035, caption, ha="center", fontsize=8, color="#596471")
    fig.subplots_adjust(left=.085, right=.98, top=.8, bottom=.25, wspace=.3)
    for extension in ("png", "svg"):
        fig.savefig(out / f"rms_vs_vectors.{extension}", dpi=180)
    plt.close(fig)


def plot_losses(curves: dict, out: Path) -> None:
    plt = _style()
    from matplotlib.lines import Line2D
    handles = [Line2D([0], [0], color=COLORS[family], lw=2, label=METHOD_LABELS[family]) for family in ("new", "old", "full")]
    handles += [Line2D([0], [0], color="#5e6772", ls=line, label=level.title()) for level, line in (("primary", "-"), ("refined", "--"))]
    for orders in ((1, 2, 3), (1,), (2,), (3,)):
        combined = len(orders) == 3
        fig, axes = plt.subplots(2, len(orders), figsize=(11.6 if combined else 5.2, 7.35), squeeze=False)
        for i, case in enumerate(CASES):
            for j, p in enumerate(orders):
                axis = axes[i, j]
                for family in ("new", "old", "full"):
                    method = "full" if family == "full" else f"{family}_p{p}"
                    for level, line in (("primary", "-"), ("refined", "--")):
                        saved = curves[f"{case}_{method}"][level]
                        positive = saved["losses"] > 0
                        axis.plot(saved["times"][positive], saved["losses"][positive], color=COLORS[family], ls=line, lw=1.35, alpha=.88)
                        if saved["endpoint_loss"] > 0:
                            axis.plot(saved["endpoint_time"], saved["endpoint_loss"], marker="o" if saved["at_target"] else "x", color=COLORS[family], ms=3)
                axis.axhline(TARGET, color="#8b95a2", ls=":", lw=.8)
                axis.set_yscale("log")
                axis.set_xlim(left=0)
                axis.set(title=f"{CASE_LABELS[case]} · p={p}", xlabel="Physical time", ylabel="Own training MSE")
                axis.grid(True, which="major", linewidth=.65)
        fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(.5, .045), ncol=5 if combined else 3, frameon=False)
        fig.suptitle("Training loss along each method's physical-time trajectory" if combined else f"Training loss versus physical time · p={orders[0]}", fontsize=13, y=.98)
        footnote = "Saved accepted steps connected by straight segments · dotted threshold MSE = 10⁻³ · endpoint markers show each method's own stopping time" if combined else "Saved steps joined by straight segments · dotted MSE = 10⁻³\nMarkers show each method's own stopping time"
        fig.text(.5, .015, footnote, ha="center", fontsize=8, color="#596471")
        fig.subplots_adjust(left=.065 if combined else .15, right=.985 if combined else .97, top=.91, bottom=.15 if combined else .19, hspace=.38, wspace=.28)
        stem = "training_loss_vs_time" if combined else f"training_loss_p{orders[0]}"
        for extension in ("png", "svg"):
            fig.savefig(out / f"{stem}.{extension}", dpi=180)
        plt.close(fig)


HTML = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>New and old dictionaries — saved endpoint comparison</title>
<style>
:root{font-family:system-ui,sans-serif;color:#202834;background:#f3f6fa;color-scheme:light}*{box-sizing:border-box}body{margin:0}main{max-width:1250px;margin:auto;padding:24px}h1{font-size:24px;margin:0 0 8px}p{line-height:1.5}header p{margin:0;color:#5c6776}.controls,.card{background:white;border:1px solid #dce3ec;border-radius:12px;padding:18px}.controls{display:flex;gap:20px;flex-wrap:wrap;margin:22px 0 16px}label{display:flex;align-items:center;gap:8px;font-size:14px}select{padding:8px;background:#fff;border:1px solid #b6c1cf;border-radius:6px;font:inherit}.grid{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:16px}.card{min-width:0}h2{font-size:17px;margin:0 0 12px}canvas{display:block;width:100%;height:auto;aspect-ratio:1}.legend{display:flex;gap:14px;flex-wrap:wrap;font-size:13px}.swatch{display:inline-block;width:20px;height:3px;vertical-align:middle;margin:0 5px 3px 0}.note{font-size:12px;color:#5c6776}.table-wrap{overflow-x:auto}table{width:100%;border-collapse:collapse;font-size:12px}th,td{text-align:left;padding:10px 7px;border-bottom:1px solid #e4e9f0;vertical-align:top}th{color:#5c6776;font-weight:600}td.number{font-variant-numeric:tabular-nums;overflow-wrap:anywhere;max-width:190px}.bad{color:#a62c40;font-weight:600}.good{color:#286344}details{margin-top:18px;font-size:12px}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:11px}button{border:1px solid #b6c1cf;background:white;border-radius:6px;padding:7px 10px;color:#364357;cursor:pointer}footer{margin-top:18px}#endpoint-note{min-height:1.5em}@media(max-width:850px){main{padding:14px}.grid{grid-template-columns:1fr}.controls{gap:12px}h1{font-size:21px}}
</style></head><body><main>
<header><h1>New and old dictionary endpoints</h1><p>Saved predictions on the circle, each at its own training-MSE 10⁻³ stopping event. The dense network is the reference.</p></header>
<div class="controls"><label>Case <select id="case"><option value="quadrant_pairs">Quadrant pairs</option><option value="two_outliers_alternating">Two outliers, alternating</option></select></label><label>Order <select id="degree"><option value="1">p = 1</option><option value="2">p = 2</option><option value="3">p = 3</option></select></label><label>Run <select id="level"><option value="primary">Standard</option><option value="refined" selected>Finer accuracy</option></select></label><label>Saved points shown <select id="density"><option value="1024">1,024</option><option value="2048" selected>2,048</option></select></label><label>Curve size <input id="amplitude" type="range" min="50" max="150" step="5" value="100"><output id="amplitude-value" for="amplitude">100%</output></label></div>
<div class="grid"><section class="card"><h2>Predictions around the circle</h2><div class="legend"><span><i class="swatch" style="background:#1874b5"></i>New</span><span><i class="swatch" style="background:#cb6a24"></i>Old</span><span><i class="swatch" style="background:#444851"></i>Dense network</span></div><canvas id="radial" aria-label="Radial plot of the saved endpoint predictions"></canvas><p class="note">The gray ring means zero. Positive predictions lie outside it; negative predictions lie inside. Dashed rings mark +1 and −1. Training targets are green for +1 and red for −1.</p><p class="note">The scale stays the same across all orders and both runs within each case. Curve size changes the view only; predictions and errors remain unchanged.</p><p class="note">The plot selects evenly spaced saved points and joins them with straight segments. It adds no samples and does not smooth or change the model.</p><button id="save">Save circle plot as PNG</button></section>
<section class="card"><h2>Saved errors and stopping times</h2><p class="note" id="endpoint-note"></p><div class="table-wrap"><table><thead><tr><th>Method</th><th>Vectors</th><th>Own MSE = 10⁻³ time</th><th>RMS vs dense</th></tr></thead><tbody id="summary"></tbody></table></div><p class="note">RMS numbers are copied from the analysis without rounding or recalculation. Each method stops at its own target crossing, so the times need not agree.</p><h2 style="margin-top:24px">Accuracy check</h2><div class="table-wrap"><table><thead><tr><th>Method</th><th>Largest saved change between runs</th><th>Status</th></tr></thead><tbody id="status"></tbody></table></div><p class="note">“Unresolved” means the analysis has not confirmed the comparison's accuracy. The saved error is still shown unchanged.</p><details><summary>Saved comparison details</summary><pre id="metric-json"></pre></details><details><summary>Source files and checksums</summary><pre id="provenance"></pre></details></section></div>
<footer class="note">Standalone local file; no external scripts, fonts, requests, or runtime dependencies. Static figures: <a href="rms_vs_vectors.svg">RMS versus vectors</a> · <a href="training_loss_vs_time.svg">Training loss versus physical time</a>.</footer>
</main><script id="saved-data" type="application/json">__DATA__</script><script>
'use strict';
const data=JSON.parse(document.getElementById('saved-data').textContent);
const palette={new:'#1874b5',old:'#cb6a24',full:'#444851'};
const title={new:'New dictionary',old:'Old dictionary',full:'Dense network'};
const canvas=document.getElementById('radial');
const text=v=>v===null||v===undefined?'unresolved':String(v);
// One display bound per case, using every saved order and both accuracy levels.
// This changes canvas coordinates only; saved predictions and metrics are intact.
const caseMagnitude=Object.fromEntries([...new Set(data.metrics.map(r=>r.case))].map(c=>{let bound=1;for(const [key,levels] of Object.entries(data.curves)){if(key.startsWith(c+'_'))for(const raw of Object.values(levels))for(const value of raw.endpoint_prediction)bound=Math.max(bound,Math.abs(value));}return [c,bound];}));
function selected(){const c=document.getElementById('case').value,p=Number(document.getElementById('degree').value),l=document.getElementById('level').value,density=Number(document.getElementById('density').value),amplitude=Number(document.getElementById('amplitude').value)/100;return {c,p,l,density,amplitude,rows:data.metrics.filter(r=>r.case===c&&r.p===p),curves:['new','old','full'].map(f=>({family:f,raw:data.curves[c+'_'+(f==='full'?'full':f+'_p'+p)][l]}))};}
function cell(tr,value,cls){const td=document.createElement('td');td.textContent=value;if(cls)td.className=cls;tr.appendChild(td);}
function update(){const s=selected(),summary=document.getElementById('summary'),status=document.getElementById('status');summary.replaceChildren();status.replaceChildren();let stopped=true;
for(const item of s.curves){const f=item.family,r=s.rows.find(x=>x.method===f+'_p'+s.p),raw=item.raw,tr=document.createElement('tr');cell(tr,title[f]);cell(tr,r?text(r.vectors):'—');cell(tr,raw.at_target?text(raw.endpoint_time):'unresolved (last t = '+text(raw.endpoint_time)+')','number');cell(tr,r?text(r[s.l+'_rms']):'reference','number');summary.appendChild(tr);stopped=stopped&&raw.at_target;
if(r){const st=document.createElement('tr');cell(st,title[f]);cell(st,text(r.refinement_max),'number');cell(st,r.valid?'Passed check':'Unresolved',r.valid?'good':'bad');status.appendChild(st);}}
const fullRow=document.createElement('tr');cell(fullRow,'Dense network');cell(fullRow,text(s.rows[0].full_refinement_max),'number');cell(fullRow,'Reference check');status.appendChild(fullRow);
document.getElementById('endpoint-note').textContent=stopped?'Times below are the exact saved target-crossing times for the selected run.':'At least one saved run did not end at the target MSE; its crossing time is unresolved.';
document.getElementById('amplitude-value').textContent=Math.round(s.amplitude*100)+'%';
document.getElementById('metric-json').textContent=JSON.stringify(s.rows,null,2);draw(s);}
function draw(s){const size=Math.max(260,Math.round(canvas.getBoundingClientRect().width)),dpr=window.devicePixelRatio||1;canvas.width=Math.round(size*dpr);canvas.height=Math.round(size*dpr);const ctx=canvas.getContext('2d');ctx.setTransform(dpr,0,0,dpr,0,0);ctx.clearRect(0,0,size,size);ctx.fillStyle='#ffffff';ctx.fillRect(0,0,size,size);const center=size/2,R=size*.43,zero=R*.57,scale=R*.24*s.amplitude/caseMagnitude[s.c];ctx.font='12px system-ui';ctx.textAlign='center';ctx.textBaseline='middle';
for(const angle of [0,Math.PI/2,Math.PI,Math.PI*1.5]){ctx.strokeStyle='#eef1f5';ctx.setLineDash([]);ctx.beginPath();ctx.moveTo(center,center);ctx.lineTo(center+R*Math.cos(angle),center-R*Math.sin(angle));ctx.stroke();ctx.fillStyle='#697788';ctx.fillText(({0:'0',1:'π/2',2:'π',3:'3π/2'})[Math.round(angle/(Math.PI/2))],center+(R+14)*Math.cos(angle),center-(R+14)*Math.sin(angle));}
for(const f of [-1,0,1]){ctx.beginPath();ctx.setLineDash(f===0?[]:[4,4]);ctx.strokeStyle=f===0?'#a0aab8':'#d2d8e0';ctx.lineWidth=f===0?1.2:1;ctx.arc(center,center,zero+scale*f,0,Math.PI*2);ctx.stroke();}ctx.setLineDash([]);
for(const item of [...s.curves].reverse()){const raw=item.raw,n=Math.min(s.density,raw.endpoint_angles.length);ctx.beginPath();for(let j=0;j<n;j++){const i=Math.floor(j*raw.endpoint_angles.length/n),a=raw.endpoint_angles[i],r=zero+scale*raw.endpoint_prediction[i],x=center+r*Math.cos(a),y=center-r*Math.sin(a);if(j===0)ctx.moveTo(x,y);else ctx.lineTo(x,y);}ctx.closePath();ctx.lineWidth=item.family==='full'?1.8:1.55;ctx.strokeStyle=palette[item.family];ctx.stroke();}
const training=s.curves[2].raw;for(let i=0;i<training.labels.length;i++){const xy=training.training_inputs[i],a=Math.atan2(xy[1],xy[0]),f=training.labels[i],r=zero+scale*f;ctx.beginPath();ctx.arc(center+r*Math.cos(a),center-r*Math.sin(a),4,0,2*Math.PI);ctx.fillStyle=f>0?'#208657':'#c13c55';ctx.fill();ctx.strokeStyle='white';ctx.lineWidth=1;ctx.stroke();}
ctx.font='11px system-ui';ctx.fillStyle='#687482';ctx.textAlign='left';ctx.fillText('zero',center+zero+5,center+14);}
for(const id of ['case','degree','level','density'])document.getElementById(id).addEventListener('change',update);
document.getElementById('amplitude').addEventListener('input',update);
document.getElementById('provenance').textContent=JSON.stringify(data.provenance,null,2);
document.getElementById('save').addEventListener('click',()=>{const s=selected(),a=document.createElement('a');a.href=canvas.toDataURL('image/png');a.download=s.c+'_p'+s.p+'_'+s.l+'_radial.png';a.click();});
window.addEventListener('resize',()=>draw(selected()));update();
</script></body></html>'''


def write_html(metrics: list[dict], curves: dict, provenance: dict, out: Path) -> None:
    serial = {}
    for key, levels in curves.items():
        serial[key] = {}
        for level, saved in levels.items():
            # Losses are shown in the static time plot; avoid doubling this data
            # in a viewer whose only curve display is the radial endpoint.
            serial[key][level] = {
                name: value.tolist() if isinstance(value, np.ndarray) else value
                for name, value in saved.items() if name not in ("times", "losses")
            }
    data = _json_value({"metrics": metrics, "curves": serial, "provenance": provenance})
    embedded = json.dumps(data, separators=(",", ":"), allow_nan=False).replace("<", "\\u003c")
    (out / "radial_comparison.html").write_text(HTML.replace("__DATA__", embedded), encoding="utf-8")


def render(analysis: Path, out: Path) -> None:
    metrics, selected, curves, inputs = load_inputs(analysis)
    provenance = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "analysis": str(analysis), "output": str(out),
        "producer": {"path": str(Path(__file__).resolve()), "sha256": _hash(Path(__file__).resolve())},
        "inputs": [{"path": str(path.resolve()), "sha256": _hash(path)} for path in sorted(set(inputs))],
        "metric_policy": "metrics.json copied byte-for-byte; scientific metrics are not recomputed",
        "display_policy": "1024 or 2048 evenly selected raw saved endpoint samples (all if fewer); straight connecting segments; signed radial offset; one case-wide scale across all orders and both levels, with display-only amplitude control; no smoothing or model transformation",
        "stopping_time_policy": "saved final times at MSE 1e-3; unresolved if the saved terminal loss is not within 1e-5 relative / 1e-10 absolute of 1e-3",
    }
    # Create only after all inputs have been read and validated.
    out.mkdir(parents=True, exist_ok=False)
    shutil.copy2(analysis / "metrics.json", out / "metrics.json")
    shutil.copy2(analysis / "selected_levels.json", out / "selected_levels.json")
    plot_rms(metrics, out)
    plot_losses(curves, out)
    write_html(metrics, curves, provenance, out)
    (out / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    artifacts = [path for path in out.iterdir() if path.is_file()]
    (out / "artifacts.json").write_text(json.dumps({path.name: {"sha256": _hash(path), "bytes": path.stat().st_size} for path in sorted(artifacts)}, indent=2) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--analysis", required=True, type=Path, help="This study's generated directory containing metrics.json and selected_levels.json")
    parser.add_argument("--out", required=True, type=Path, help="Fresh output directory within this study's generated namespace")
    args = parser.parse_args()
    analysis, out = args.analysis.resolve(strict=True), args.out.resolve()
    root = GENERATED.resolve()
    if not _under(analysis, root) or not analysis.is_dir():
        parser.error(f"--analysis must be a directory inside {root}")
    if not _under(out, root) or out == root or out.exists():
        parser.error(f"--out must be a fresh directory inside {root}")
    render(analysis, out)
    print(json.dumps({"output": str(out), "viewer": str(out / "radial_comparison.html")}))


if __name__ == "__main__":
    main()
