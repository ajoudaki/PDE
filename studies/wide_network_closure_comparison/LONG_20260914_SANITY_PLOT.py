"""Linear-clock view of the completed long-run sanity check."""
import argparse
import json
import os
from pathlib import Path
import sys
os.environ["MPLCONFIGDIR"]="/tmp/pde-long-sanity-matplotlib"
os.environ["OPENBLAS_NUM_THREADS"]="1"
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from LONG_20260914_COMMON import GENERATED,STAGES,sha


def main(output,target):
    output=output.resolve()
    if output.parent!=GENERATED or target not in STAGES:raise ValueError("Invalid run/stage")
    values=[];hashes={}
    for t in STAGES:
        if t>target:break
        path=output/f"stage_analysis_{t:06d}.json"
        value=json.loads(path.read_text())
        if value["status"]!="complete" or not value["validation_pass"]:raise ValueError("Incomplete stage")
        values.append(value);hashes[path.name]=sha(path)
    times=np.concatenate([np.array(v["times"])[0 if i==0 else 1:] for i,v in enumerate(values)])
    def curve(table,**match):
        parts=[]
        for i,v in enumerate(values):
            rows=[r for r in v[table] if all(r.get(k)==x for k,x in match.items())]
            if len(rows)!=1:raise ValueError("Nonunique plotted curve")
            parts.append(np.array(rows[0]["curve"])[0 if i==0 else 1:])
        return np.concatenate(parts)
    plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
    fig,axes=plt.subplots(1,3,figsize=(14,4.6),constrained_layout=True)
    axes[0].plot(times,curve("loss_curves",name="arcs30_n8192_mean"),color="#214b80",lw=2.2,label="Actual network: width 8192, 3-seed mean")
    seed_losses=np.stack([curve("loss_curves",name=f"arcs30_n8192_s{s}") for s in (11,29,47)])
    axes[0].fill_between(times,seed_losses.min(0),seed_losses.max(0),color="#214b80",alpha=.18)
    display=(("arcs30_N1","N = 1","#d58c00","-"),("arcs30_N3","N = 3","#009e73","-"),
             ("arcs30_N5","N = 5","#cc5078","-"),("arcs30_N5_fine","N = 5, finest quadrature","#825ac3","-."))
    for name,label,color,style in display:
        axes[0].plot(times,curve("loss_curves",name=name),color=color,ls=style,lw=1.8,label=label)
        for layer in (1,2):
            axes[layer].plot(times,curve("comparisons",closure=name,width=8192,layer=layer,panel="data",observable="G"),
                             color=color,ls=style,lw=1.8)
    axes[0].set_yscale("log");axes[0].set_title("Loss (logarithmic vertical scale)")
    axes[0].set_ylabel("Training mean squared loss")
    for layer in (1,2):
        axes[layer].set_title(f"Layer {layer}: Gram prediction error")
        axes[layer].set_ylabel("Matrix RMS on 16 training inputs")
        axes[layer].set_ylim(bottom=0)
    for ax in axes:
        ax.set_xlim(0,target);ax.set_xlabel("Physical training time t (linear scale)")
        ax.set_xticks(np.linspace(0,target,5))
        ax.axvline(40,color="#858585",ls=":",lw=1)
        ax.axvspan(.75*target,target,color="#dfe8f0",alpha=.35)
        ax.grid(alpha=.18)
    h,l=axes[0].get_legend_handles_labels();fig.legend(h,l,loc="outside lower center",ncol=3,frameon=False)
    fig.suptitle(f"Longer-time sanity check through T={target}\nDotted line: original T=40 · shaded region: final quarter",fontsize=14)
    destination=output/f"figures_T{target:06d}";destination.mkdir(exist_ok=True)
    products=[]
    for ext in ("png","pdf"):
        path=destination/f"sanity_linear_time.{ext}"
        fig.savefig(path,dpi=180,bbox_inches="tight",facecolor="white")
        products.append(dict(path=path.name,sha256=sha(path)))
    plt.close(fig)
    record=dict(source_sha256=sha(__file__),command=sys.argv,target=target,analyses=hashes,products=products,
                numpy_version=np.__version__,matplotlib_version=matplotlib.__version__,
                note="All runs remain in full evidence; this display shows the actual wide-network mean and four representative closure resolutions. Frozen baseline is in the companion overview.")
    (destination/"sanity_linear_time.json").write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps(dict(status="complete",target=target)))


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--target",type=int,required=True)
    a=parser.parse_args();main(a.output,a.target)
