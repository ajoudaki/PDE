"""Read only this route's pilot outputs; no training or GPU use."""
import json
from pathlib import Path
import torch

torch.set_num_threads(1)
torch.set_grad_enabled(False)
base=Path("data/generated/response_memory_frontiers_20261002/recurrence_seed4101")
data=torch.load(base/"data.pt",weights_only=False)
states={method:torch.load(base/f"{method}_t40.pt",weights_only=False)
        for method in ("dense","memory4","svd32")}
initial={method:torch.load(base/f"{method}_t0.pt",weights_only=False)
         for method in states}
hb,bb,tau=states["memory4"]["state"]
m,q,n=hb.shape
weights=(2*torch.arange(q,dtype=hb.dtype)+1)
u=(-2/(m*n*tau)*bb*weights[None,:,None]).reshape(m*q,n).T
v=hb.reshape(m*q,n).T
w=states["memory4"]["w"]
h=states["memory4"]["h"][:m]
e=h-data["y"][:m]
d=1-h*h
eye=torch.eye(n,dtype=h.dtype)
a=eye[None]-d[:,:,None]*data["w0"][None]
k=eye[None]-d[:,:,None]*w[None]
atu=torch.linalg.solve(a,d[:,:,None]*u[None])
s=torch.eye(m*q,dtype=h.dtype)[None]-v.T[None]@atu
z=torch.linalg.solve(a.transpose(-1,-2),e[:,:,None])
small=torch.linalg.solve(s.transpose(-1,-2),u.T[None]@(d[:,:,None]*z))
lam_schur=z+torch.linalg.solve(a.transpose(-1,-2),v[None]@small)
lam=states["memory4"]["lambda"][:,:,None]
summary={
    "completed_training_runs":3,
    "zero_update_failed_attempts":1,
    "same_initial_weight_bitwise":all(torch.equal(initial[x]["w"],data["w0"]) for x in initial),
    "same_initial_predictions_bitwise":all(torch.equal(initial[x]["h"],initial["dense"]["h"]) for x in initial),
    "schur_weight_reconstruction_error":float(torch.linalg.vector_norm(w-data["w0"]-u@v.T)),
    "schur_adjoint_relative_error":float(torch.linalg.vector_norm(lam_schur-lam)/torch.linalg.vector_norm(lam)),
    "schur_adjoint_relative_residual":float(torch.linalg.vector_norm(k.transpose(-1,-2)@lam_schur-e[:,:,None])/torch.linalg.vector_norm(e)),
    "dense_loss_reduction_fraction":1-states["dense"]["record"]["train_mse"]/initial["dense"]["record"]["train_mse"],
    "dense_test_loss_reduction_fraction":1-states["dense"]["record"]["test_mse"]/initial["dense"]["record"]["test_mse"],
    "dense_inverse_gain_ratio":max(states["dense"]["record"]["full_inverse_norm"])/max(initial["dense"]["record"]["full_inverse_norm"]),
    "final":{method:{key:value for key,value in checkpoint["record"].items()
                    if key not in ("increment_singular_values",)}
             for method,checkpoint in states.items()},
}
metadata=[json.loads((base/name).read_text()) for name in
          ("initial_metadata.json","memory_metadata.json","metadata_svd32.json")]
summary["total_gpu_process_seconds"]=sum(item["total_process_seconds"] for item in metadata)
summary["maximum_cuda_bytes"]=max(item["peak_cuda_bytes"] for item in metadata)
summary["gradient_check"]=json.loads((base/"gradient_check.json").read_text())
summary["moment_check"]=json.loads((base/"moment_check.json").read_text())
summary["comparisons"]={
    "memory4":json.loads((base/"comparison.json").read_text()),
    "svd32":json.loads((base/"comparison_svd32.json").read_text()),
}
(base/"summary.json").write_text(json.dumps(summary,indent=2))
print(json.dumps({key:value for key,value in summary.items() if key not in ("final","comparisons")},indent=2))
