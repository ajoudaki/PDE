"""Plot every completed common stage of the long network/closure comparison."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import sys
os.environ["MPLCONFIGDIR"]="/tmp/pde-long-matplotlib"
os.environ["OPENBLAS_NUM_THREADS"]="1"
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from LONG_20260914_COMMON import ROOT,STUDY,GENERATED,STAGES,sha

COLORS={1:"#d58c00",3:"#009e73",5:"#cc5078"}
DISPLAY=(("arcs30_N1","N = 1",COLORS[1],"-"),
         ("arcs30_N3","N = 3",COLORS[3],"-"),
         ("arcs30_N5","N = 5",COLORS[5],"-"),
         ("arcs30_N5_fine","N = 5, finest quadrature","#825ac3","-."))


def main(output,through=None):
    output=output.resolve()
    if output.parent!=GENERATED or not output.name.startswith("LONG_"):raise ValueError("Wrong study namespace")
    stages=[]
    for target in STAGES:
        path=output/f"stage_analysis_{target:06d}.json"
        if not path.exists() or (through is not None and target>through):break
        value=json.loads(path.read_text())
        if value["status"]!="complete" or not value["validation_pass"]:break
        stages.append((target,path,value))
    if not stages:raise ValueError("No complete common stage to plot")
    target=stages[-1][0]
    destination=output/f"figures_T{target:06d}"
    destination.mkdir(exist_ok=True)
    times=np.concatenate([np.array(v["times"])[0 if i==0 else 1:] for i,(_,_,v) in enumerate(stages)])
    products=[]
    plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False,
                        "savefig.facecolor":"white"})

    def curve(table,predicate,field="curve"):
        pieces=[]
        for i,(_,_,value) in enumerate(stages):
            rows=[r for r in value[table] if predicate(r)]
            if len(rows)!=1:raise ValueError(f"Nonunique curve in {table}: {len(rows)}")
            pieces.append(np.asarray(rows[0][field])[0 if i==0 else 1:])
        return np.concatenate(pieces)

    def save(fig,name):
        for ext in ("png","pdf"):
            p=destination/f"{name}.{ext}"
            fig.savefig(p,dpi=180,bbox_inches="tight")
            products.append(dict(path=str(p.relative_to(output)),sha256=sha(p)))
        plt.close(fig)

    def clock(ax):
        ax.set_xscale("symlog",linthresh=1,linscale=.7)
        ticks=[0,1,10,40]+[t for t in (160,640,2560,10240) if t<=target]
        if target not in ticks:ticks.append(target)
        ax.set_xticks(sorted(set(ticks)),[str(t) for t in sorted(set(ticks))])
        ax.set_xlim(0,target)
        ax.set_xlabel("Physical training time t")
        ax.grid(alpha=.2)
        ax.axvline(40,color="#959595",lw=.8,ls=":")

    fig,axes=plt.subplots(1,3,figsize=(14,4.7),constrained_layout=True)
    for width,col,style in ((8192,"#214b80","-"),(2048,"#929292",":")):
        mean=curve("loss_curves",lambda r:r["name"]==f"arcs30_n{width}_mean")
        axes[0].plot(times,mean,color=col,ls=style,lw=2,label=f"Network {width}: 3-seed mean")
        if width==8192:
            seeds=np.stack([curve("loss_curves",lambda r:r["name"]==f"arcs30_n8192_s{s}") for s in (11,29,47)])
            axes[0].fill_between(times,seeds.min(0),seeds.max(0),color=col,alpha=.18)
    for name,label,col,style in DISPLAY:
        axes[0].plot(times,curve("loss_curves",lambda r:r["name"]==name),color=col,ls=style,lw=1.7,label=label)
    axes[0].set_yscale("log");axes[0].set_ylabel("Training mean squared loss");axes[0].set_title("Loss")
    for layer in (1,2):
        ax=axes[layer]
        frozen=curve("frozen_initial_baselines",lambda r:r["name"]=="arcs30_n8192_mean" and r["layer"]==layer and r["panel"]=="data")
        ax.plot(times,frozen,color="#292929",ls="--",lw=2,label="Frozen initial Gram")
        for name,label,col,style in DISPLAY:
            e=curve("comparisons",lambda r:r["closure"]==name and r["width"]==8192 and r["layer"]==layer and r["panel"]=="data" and r["observable"]=="G")
            ax.plot(times,e,color=col,ls=style,lw=1.7)
        ax.set_title(f"Layer {layer}: Gram error");ax.set_ylabel("Matrix RMS error on training inputs")
        ax.set_ylim(bottom=0)
    for ax in axes:clock(ax)
    h,l=axes[0].get_legend_handles_labels();h2,l2=axes[1].get_legend_handles_labels()
    fig.legend(h+h2,l+l2,loc="outside lower center",ncol=4,frameon=False)
    fig.suptitle(f"±30° training arcs · longer evolution through T={target}\nVertical dotted line: previous stopping time T=40",fontsize=14)
    save(fig,"loss_and_gram_errors")

    fig,axes=plt.subplots(1,2,figsize=(12,5),constrained_layout=True)
    final=stages[-1][2]
    for r in final["runs"]:
        name=r["name"];ax=axes[0 if r["family"]=="network" else 1]
        values=curve("loss_curves",lambda q:q["name"]==name)
        if r["family"]=="network":
            config=r["configuration"]
            col=("#214b80" if config["width"]==8192 else "#7898b2")
            style={11:"-",29:"--",47:":"}[config["seed"]]
            if config["kind"]!="primary":col="#333333";style="-."
            label=f'n={config["width"]}, seed {config["seed"]}'
            if config["kind"]!="primary":label+=" "+config["kind"].replace("_"," ")
        else:
            config=r["configuration"];col=COLORS[config["order"]]
            style="-." if config["kind"]=="time_control" else ":" if config["refined"] else "-"
            label=f'N={config["order"]}, Q={config["initialization_nodes"]}'
            if config["kind"]=="time_control":label+=" half step"
        ax.plot(times,values,color=col,ls=style,lw=1.3,label=label)
    for ax,title in zip(axes,("All eight actual networks","All eight closure configurations")):
        clock(ax);ax.set_yscale("log");ax.set_ylabel("Training mean squared loss");ax.set_title(title)
        ax.legend(fontsize=8,loc="upper right",frameon=False)
    fig.suptitle(f"All configurations through T={target}",fontsize=14)
    save(fig,"all_loss_curves")

    fig,axes=plt.subplots(2,4,figsize=(15,7),constrained_layout=True)
    closure_names=[r["name"] for r in final["runs"] if r["family"]=="closure"]
    for i,observable in enumerate(("G","DeltaG")):
        for j,(layer,panel) in enumerate(((1,"data"),(2,"data"),(1,"circle"),(2,"circle"))):
            ax=axes[i,j]
            for name in closure_names:
                cfg=next(r["configuration"] for r in final["runs"] if r["name"]==name)
                col=COLORS[cfg["order"]]
                style="-." if cfg["kind"]=="time_control" else ":" if cfg["refined"] else "-"
                if "fine" in name:col="#825ac3"
                values=curve("comparisons",lambda r:r["closure"]==name and r["width"]==8192 and r["layer"]==layer and r["panel"]==panel and r["observable"]==observable)
                ax.plot(times,values,color=col,ls=style,lw=1.4,label=name.replace("arcs30_",""))
            if i==0:ax.set_title(f'Layer {layer} · {"training" if panel=="data" else "circle"}')
            if j==0:ax.set_ylabel(f"{observable} prediction error\nMatrix RMS")
            clock(ax);ax.set_ylim(bottom=0)
    h,l=axes[0,0].get_legend_handles_labels();fig.legend(h,l,loc="outside lower center",ncol=4,frameon=False,fontsize=8)
    fig.suptitle(f"All closure Gram errors against the width-8192 mean · T={target}",fontsize=14)
    save(fig,"all_gram_and_increment_errors")

    fig,axes=plt.subplots(1,3,figsize=(12,4),constrained_layout=True)
    for ax,key,label,field in zip(axes,("loss_windows","gram_windows","error_windows"),
        ("Loss variation","Actual Gram variation","Gram-error variation"),("variation","variation_bound","variation")):
        for group in ("network","closure") if key!="error_windows" else ("all closures",):
            xs=[];ys=[]
            for t,_,v in stages:
                rows=[r for r in v["settling"][key] if key=="error_windows" or r["family"]==group]
                xs.append(t);ys.append(max(r[field]/r["threshold"] for r in rows))
            ax.plot(xs,ys,"o-",label=group)
        ax.axhline(1,color="black",ls="--",label="Settling threshold")
        ax.set_xscale("log",base=2);ax.set_yscale("log")
        ax.set_xlabel("Common horizon T");ax.set_title(label);ax.grid(alpha=.2)
        ax.legend(fontsize=8,frameon=False)
    axes[0].set_ylabel("Worst window variation / allowed variation")
    fig.suptitle("Settling checks: all three panels must be at or below 1",fontsize=13)
    save(fig,"settling_checks")
    targets=[0,40,target/2,target]
    raw_hashes={}
    def read_matrix(family,name,t,layer):
        stage=40 if t<=40 else next(s for s in STAGES if s>=t)
        path=output/family/name/f"stage_{stage:06d}"/"gram.npy"
        times_path=path.with_name("observations.npz")
        with np.load(times_path) as a:k=int(np.flatnonzero(a["times"]==t)[0])
        raw_hashes[str(path.relative_to(output))]=sha(path)
        return np.load(path,mmap_mode="r")[k,layer-1,16:,16:]
    for layer in (1,2):
        actual=np.stack([sum(read_matrix("network",f"arcs30_n8192_s{s}",t,layer)/3 for s in (11,29,47)) for t in targets])
        predicted=np.stack([read_matrix("closure","arcs30_N5_fine",t,layer) for t in targets])
        err=predicted-actual
        limit=max(np.abs(actual).max(),np.abs(predicted).max())
        errlimit=max(np.abs(err).max(),1e-12)
        fig,axes=plt.subplots(3,4,figsize=(12,8.8),constrained_layout=True)
        for row,mats in enumerate((actual,predicted,err)):
            lim=errlimit if row==2 else limit
            for col,t in enumerate(targets):
                ax=axes[row,col]
                im=ax.imshow(mats[col],origin="lower",extent=(0,360,0,360),cmap="RdBu_r",vmin=-lim,vmax=lim,interpolation="nearest")
                ax.set_xticks([0,180,360]);ax.set_yticks([0,180,360])
                if row==0:ax.set_title(f"t = {t:g}")
                if col==0:ax.set_ylabel(("Actual network mean","Finest N = 5 closure","Closure − network")[row]+"\nInput angle (degrees)")
                if row==2:ax.set_xlabel("Input angle (degrees)")
            fig.colorbar(im,ax=axes[row,:],fraction=.018,pad=.015)
        fig.suptitle(f"Layer {layer} Gram evolution · passive circle · T={target}",fontsize=15)
        save(fig,f"layer{layer}_gram_evolution")
    metadata=dict(status="complete",source_sha256=sha(__file__),command=sys.argv,target=target,
        analysis_sha256={path.name:sha(path) for _,path,_ in stages},raw_gram_sha256=raw_hashes,
        products=products,matplotlib_version=matplotlib.__version__,numpy_version=np.__version__,
        reading="Loss axis is logarithmic. Gram errors use width8192 three-seed mean. Heatmap top=actual network, middle=finestN5, bottom=prediction minus network with separate error scale.")
    (destination/"figures.json").write_text(json.dumps(metadata,indent=2)+"\n")
    print(json.dumps(dict(status="complete",target=target,figure_files=len(products),directory=str(destination))))


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",required=True,type=Path)
    parser.add_argument("--through",type=int)
    args=parser.parse_args();main(args.output,args.through)
