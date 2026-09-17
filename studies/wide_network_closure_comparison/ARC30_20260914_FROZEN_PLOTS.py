"""Add a frozen initial activation Gram baseline from finalized ARC30 arrays.

Deterministic postprocessing of the existing frozen-baseline metric; no training.
Usage: python -B ARC30_20260914_FROZEN_PLOTS.py --output <fresh output directory>
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MPLCONFIGDIR"] = "/tmp/pde-arc30-frozen-matplotlib"
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
GENERATED = ROOT / "data/generated/wide_network_closure_comparison"
SOURCE = GENERATED / "ARC30_20260914_v1"
COLORS = {1: "#d58c00", 3: "#009e73", 5: "#cc5078"}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main(output):
    output = output.resolve()
    if output.parent != GENERATED or not output.name.startswith("ARC30_") or output == SOURCE:
        raise ValueError("Use a separate ARC30 output under this study's generated directory")
    output.mkdir(exist_ok=True)
    result = json.loads((SOURCE / "arc30_comparison.json").read_text())
    verified = json.loads((SOURCE / "final_verification.json").read_text())
    assert verified["status"] == "passed"
    assert sha(SOURCE / "arc30_comparison.json") == verified["analysis_sha256"]
    paths = [SOURCE / "network" / f"arcs30_n8192_s{s}" / "gram.npy" for s in (11,29,47)]
    input_hashes = {str(p.relative_to(ROOT)): sha(p) for p in paths}
    for path in paths:
        rec = json.loads(path.with_name("record.json").read_text())
        assert rec["status"] == "complete" and rec["gram_completed_observations"] == 206
        assert sha(path) == rec["gram_sha256"]
        obs_path = path.with_name("observations.npz")
        input_hashes[str(obs_path.relative_to(ROOT))] = sha(obs_path)
        assert input_hashes[str(obs_path.relative_to(ROOT))] == rec["observations_sha256"]
    for name in ("arc30_comparison.json", "final_verification.json", "inputs.npz", "figures/figures.json"):
        input_hashes[str((SOURCE / name).relative_to(ROOT))] = sha(SOURCE / name)
    with np.load(SOURCE / "inputs.npz") as archive:
        times = archive["times"].copy()
    raw = [np.load(path, mmap_mode="r") for path in paths]
    assert all(g.shape == (206,2,144,144) for g in raw)
    curves = {}
    summaries = []
    max_crosscheck = 0.
    for panel, sl in (("data",slice(0,16)), ("circle",slice(16,144))):
        for layer in (1,2):
            mean = sum(np.asarray(g[:,layer-1,sl,sl]) for g in raw) / 3
            m = mean.shape[-1]
            frozen = np.sqrt(np.mean((mean-mean[0])**2, axis=(-2,-1)))
            old = next(r for r in result["frozen_initial_baselines"] if r["family"]=="network_seed_mean"
                       and r["width"]==8192 and r["layer"]==layer and r["panel"]==panel)
            error = float(np.max(np.abs(frozen-np.asarray(old["rms_curve"]))))
            max_crosscheck = max(max_crosscheck,error)
            assert error < 2e-15 and frozen[0] == 0
            initial_norm = float(np.linalg.norm(mean[0])/m)
            final_norm = float(np.linalg.norm(mean[-1])/m)
            closures = {}
            for name in ("arcs30_N1","arcs30_N3","arcs30_N5","arcs30_N5_fine"):
                row = next(r for r in result["seed_mean_comparisons"] if r["width"]==8192 and
                           r["layer"]==layer and r["panel"]==panel and r["observable"]=="G" and r["closure"]==name)
                curve = np.array(row["rms_curve"])
                closures[name] = curve
                wins = np.flatnonzero(curve < frozen)
                closures_summary = dict(
                    closure=name, panel=panel, layer=layer, frozen_max=float(frozen.max()),
                    frozen_terminal=float(frozen[-1]), frozen_max_time=float(times[frozen.argmax()]),
                    closure_max=float(curve.max()), closure_terminal=float(curve[-1]),
                    max_error_improvement_factor=float(frozen.max()/curve.max()),
                    terminal_error_improvement_factor=float(frozen[-1]/curve[-1]),
                    relative_terminal_movement_to_initial= float(frozen[-1]/initial_norm),
                    relative_terminal_movement_to_final=float(frozen[-1]/final_norm),
                    first_saved_time_closure_better=float(times[wins[0]]) if len(wins) else None,
                    closure_better_saved_count=int(len(wins)),
                    frozen_better_times=times[frozen < curve].tolist())
                summaries.append(closures_summary)
            curves[(panel,layer)] = dict(frozen=frozen, closures=closures)
    plt.rcParams.update({"font.size":11, "axes.spines.top":False, "axes.spines.right":False,
                         "savefig.facecolor":"white"})
    products = []

    def save(fig,name):
        for ext in ("png","pdf"):
            path = output / f"{name}.{ext}"
            fig.savefig(path,dpi=180,bbox_inches="tight")
            products.append(dict(path=path.name,sha256=sha(path)))
        plt.close(fig)

    def time_axis(ax):
        ax.set_xscale("symlog",linthresh=.5,linscale=.7)
        ax.set_xticks([0,.5,1,5,10,40],["0",".5","1","5","10","40"])
        ax.set_xlim(0,40)
        ax.set_xlabel("Training time t (early times expanded)")
        ax.grid(alpha=.18)

    def gram_panel(ax,panel,layer):
        values = curves[(panel,layer)]
        ax.plot(times,values["frozen"],color="#292929",ls="--",lw=2.5,
                label="Frozen initial Gram G(0)")
        for n in (1,3,5):
            ax.plot(times,values["closures"][f"arcs30_N{n}"],color=COLORS[n],lw=1.8,
                    label=f"Closure N = {n}")
        ax.plot(times,values["closures"]["arcs30_N5_fine"],color="#825ac3",ls="-.",lw=2,
                label="N = 5, finest quadrature")
        ax.set_ylim(0,.46)
        ax.set_title(f"Layer {layer}")
        ax.set_ylabel("Gram prediction error (matrix RMS)")
        time_axis(ax)

    for panel,m in (("data",16),("circle",128)):
        fig,axes = plt.subplots(1,2,figsize=(11,4.7),constrained_layout=True)
        for layer,ax in enumerate(axes,1):
            gram_panel(ax,panel,layer)
        handles,labels = axes[0].get_legend_handles_labels()
        fig.legend(handles,labels,loc="outside lower center",ncol=3,frameon=False)
        panel_label = "training" if panel=="data" else "passive circle"
        fig.suptitle(f"±30° training arcs · prediction versus frozen geometry\n"
                     f"{m} {panel_label} inputs; width-8192 three-seed network mean",fontsize=14)
        save(fig,f"gram_errors_with_frozen_{panel}")
    fig,axes = plt.subplots(1,3,figsize=(14,4.6),constrained_layout=True)
    with np.load(SOURCE/"network/arcs30_n8192_s11/observations.npz") as archive:
        losses = [archive["loss"].copy()]
    for seed in (29,47):
        with np.load(SOURCE/f"network/arcs30_n8192_s{seed}/observations.npz") as archive:
            losses.append(archive["loss"].copy())
    axes[0].plot(times,np.mean(losses,axis=0),color="#214b80",lw=2.2,label="Network 8192: 3-seed mean")
    axes[0].fill_between(times,np.min(losses,axis=0),np.max(losses,axis=0),color="#214b80",alpha=.18)
    for name,color,style in [(f"arcs30_N{n}",COLORS[n],"-") for n in (1,3,5)]+[("arcs30_N5_fine","#825ac3","-.")]:
        row = next(r for r in result["scalar_seed_mean_comparisons"] if r["width"]==8192 and r["observable"]=="loss" and r["closure"]==name)
        axes[0].plot(times,row["left_curve"],color=color,ls=style,lw=1.8)
    axes[0].set_yscale("log")
    axes[0].set_ylabel("Training mean squared loss")
    axes[0].set_title("Loss evolution")
    time_axis(axes[0])
    for layer in (1,2):
        gram_panel(axes[layer],"data",layer)
    h0,l0 = axes[0].get_legend_handles_labels()
    h1,l1 = axes[1].get_legend_handles_labels()
    fig.legend(h0+h1,l0+l1,loc="outside lower center",ncol=3,frameon=False)
    fig.suptitle("±30° training arcs · loss and Gram errors with frozen baseline\n"
                 "Gram comparison on 16 training inputs",fontsize=14)
    save(fig,"loss_and_gram_errors_with_frozen")
    assert all(sha(ROOT/path)==value for path,value in input_hashes.items())
    payload = dict(status="complete",created_utc=datetime.now(timezone.utc).isoformat(),
        method="Frozen prediction is the mean of the same three networks' initial activation Grams. Error = Frobenius norm / panel size. Closure errors use the same evolving mean reference. No new training.",
        interpretation="Tests freezing activation geometry, not the predictive loss of a separately trained NTK model. Ratios are ratios of maximum saved-time errors, not pointwise guarantees.",
        source_sha256=sha(__file__),source=str(Path(__file__).relative_to(ROOT)),command=sys.argv,
        input_sha256=input_hashes,all_inputs_preserved=True,max_existing_curve_crosscheck_error=max_crosscheck,
        numpy_version=np.__version__,matplotlib_version=matplotlib.__version__,times=times.tolist(),
        summaries=summaries,curves={f"{p}_layer{l}":{"frozen":v["frozen"].tolist(),
                **{k:a.tolist() for k,a in v["closures"].items()}} for (p,l),v in curves.items()},
        products=products)
    (output/"frozen_baseline.json").write_text(json.dumps(payload,indent=2)+"\n")
    print(json.dumps(dict(status="complete",output=str(output),summaries=[r for r in summaries
        if r["panel"]=="data" and r["closure"]=="arcs30_N5_fine"]),indent=2))


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    main(parser.parse_args().output)
