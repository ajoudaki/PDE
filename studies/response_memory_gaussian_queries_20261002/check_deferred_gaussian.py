"""Algebraic and distribution diagnostics, not a proof of adaptive exactness."""
import argparse
import hashlib
import json
from pathlib import Path
import torch
from deferred_gaussian import DeferredGaussian


def one(tolerance, seed=1717):
    n = 48
    gen = torch.Generator().manual_seed(seed + 1)
    oracle = DeferredGaussian(n, tolerance=tolerance, seed=seed,
                              record_queries=True)
    x = torch.randn((3, n), generator=gen, dtype=torch.float64)
    for j in range(12):
        z = oracle.action(x)
        d = torch.tanh(z) * (1 + j / 20)
        back = oracle.action(d, transpose=True)
        x = torch.tanh(x + .1 * back)
    W = oracle.complete(seed=seed+2)
    operator_norm = float(torch.linalg.matrix_norm(W, ord=2))
    absolute, normalized_bound_excess = 0.0, 0.0
    for query, ans, residual, trans in oracle.records:
        exact = query @ (W if trans else W.T)
        error = torch.linalg.vector_norm(exact-ans, dim=1) / n**.5
        bound = operator_norm * torch.linalg.vector_norm(residual, dim=1) / n**.5
        absolute = max(absolute, float(error.max()))
        normalized_bound_excess = max(normalized_bound_excess,
                                      float((error-bound).max()))
    U, V = oracle.U[:, :oracle.r], oracle.V[:, :oracle.s]
    Y, Z = oracle.Y[:, :oracle.r], oracle.Z[:, :oracle.s]
    constraints = max(float((W@U-Y).abs().max()), float((W.T@V-Z).abs().max()))
    a = torch.randn((1,n), generator=gen, dtype=torch.float64)
    b = torch.randn((1,n), generator=gen, dtype=torch.float64)
    adjoint = float(abs((oracle.mean_action(a)*b).sum()
                        -(a*oracle.mean_action(b, transpose=True)).sum()))
    assert constraints < 1e-11
    assert adjoint < 1e-11
    assert normalized_bound_excess < 1e-11
    if tolerance == 0:
        assert absolute < 1e-10
    return {**oracle.statistics(), "completion_constraint_error": constraints,
            "adjoint_error": adjoint, "max_action_rms_error": absolute,
            "bound_excess": normalized_bound_excess, "W_operator_norm":operator_norm}


def distribution():
    # An adaptive nonlinear query followed by a completion should still have
    # standard Gaussian marginal entries. This is only a gross scaling check.
    norms, means = [], []
    for seed in range(160):
        n=12
        oracle=DeferredGaussian(n,tolerance=.03,seed=10000+seed)
        x=torch.arange(1,n+1,dtype=torch.float64).reshape(1,n)/n
        for j in range(3):
            z=oracle.action(x)
            x=torch.tanh(oracle.action(torch.tanh(z),transpose=True))
        W=oracle.complete(seed=20000+seed)
        means.append(float(W.mean()))
        norms.append(float(W.square().mean())*n)
    mean=sum(means)/len(means)
    variance=sum(norms)/len(norms)
    assert abs(mean)<.015 and abs(variance-1)<.05
    return dict(repetitions=160, mean_entry=mean, second_moment_times_n=variance)


if __name__ == "__main__":
    p=argparse.ArgumentParser();p.add_argument("--out",required=True)
    args=p.parse_args()
    out=Path(args.out);out.mkdir(parents=True,exist_ok=False)
    torch.set_num_threads(1)
    result={"exact":one(0),"approximate":one(.02),"distribution":distribution(),
            "torch":torch.__version__,"dtype":"float64","device":"cpu"}
    result["source_sha256"]={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                              for name in ["deferred_gaussian.py","check_deferred_gaussian.py"]}
    (out/"checks.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
