"""Plot the existing scalar-point solutions without running training."""
import argparse
import json
import pickle
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scalar_fourier_reference import DenseReference, PopulationReference, initialize


def main():
    p=argparse.ArgumentParser()
    p.add_argument("run",type=Path)
    args=p.parse_args()
    run=args.run
    theta=np.deg2rad([10,125])
    inputs=np.column_stack([np.cos(theta),np.sin(theta)])
    test=np.array([[.5,np.sqrt(3)/2]])
    labels=np.array([1.,-1.])
    init=initialize(16,20260920)
    fig,axes=plt.subplots(1,2,figsize=(10.5,4.2))
    cases=[("dense","Dense", "#202733"),
           ("parent_P1","Population P=1", "#5374b8"),
           ("scalar_K5","Scalar K=5", "#c85432")]
    for name,label,color in cases:
        folder=run/name
        rec=json.loads((folder/"result.json").read_text())
        with (folder/"solution.pkl").open("rb") as f:
            sol=pickle.load(f)
        times=np.linspace(0,rec["fit_time"],240)
        if name.startswith("scalar"):
            with (folder/"runtime.pkl").open("rb") as f: model=pickle.load(f)
            point=lambda z:float(model.point_output(z))
            train=model.training_output
        else:
            cls=DenseReference if name=="dense" else PopulationReference
            model=cls(inputs,labels,init)
            point=lambda z:float(model.predict(z,test)[0])
            train=lambda z:model.predict(z,inputs)
        states=sol.sol(times)
        values=np.array([point(states[:,i]) for i in range(len(times))])
        errors=np.array([np.sqrt(np.mean((train(states[:,i])-labels)**2)) for i in range(len(times))])
        axes[0].plot(times,values,color=color,lw=2,label=label)
        axes[0].scatter(times[-1],values[-1],color=color,s=30,zorder=5)
        axes[1].semilogy(times,errors,color=color,lw=2)
        axes[1].scatter(times[-1],errors[-1],color=color,s=30,zorder=5)
    axes[0].set_title("Prediction at the passive 60° input",loc="left")
    axes[0].set_ylabel("Output")
    axes[0].legend(frameon=False,fontsize=9)
    axes[1].set_title("Training fit on the two active inputs",loc="left")
    axes[1].set_ylabel("Training RMS")
    axes[1].axhline(np.sqrt(.001),lw=1,color="#888888",ls="--")
    for ax in axes:
        ax.set_xlabel("Training time")
        ax.grid(alpha=.15)
        ax.spines[["top","right"]].set_visible(False)
    fig.suptitle("Single-test-input check: no Fourier representation",x=.065,ha="left",fontsize=14)
    fig.text(.065,.012,"Three tanh layers · width 16 · train at 10° and 125° · dots mark each model's fitted stopping point",fontsize=9,color="#505864")
    fig.tight_layout(rect=(0,.04,1,.94))
    fig.savefig(run/"point_comparison.png",dpi=180)
    fig.savefig(run/"point_comparison.pdf")


if __name__=="__main__": main()
