"""Independent activation-campaign audit; no production RHS in saved replay.

CPU self-tests are small algebraic checks, not training runs. Saved-state
replay explicitly materializes both physical matrices and evaluates independent
activation formulas. A GPU device must be assigned separately by the lead.
"""

import argparse
import hashlib
import json
import math
from pathlib import Path
import time
import traceback
import zipfile

import numpy as np
from scipy.special import ndtr, expit


FOLDER = Path(__file__).resolve().parent
DEFAULT_OUT = FOLDER.parents[1] / "data/generated/neural_response_memory_20260922/activation_circle_audit01"
LAMBDA = 1.0507009873554804934193349852946
ALPHA = 1.6732632423543772848170429916717
ACTIVATIONS = ("relu", "gelu", "selu", "sigmoid")


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def array_hash(*arrays):
    digest = hashlib.sha256()
    for value in arrays:
        value = np.asarray(value)
        digest.update(str(value.shape).encode())
        digest.update(str(value.dtype).encode())
        digest.update(value.tobytes(order="C"))
    return digest.hexdigest()


def numpy_activation(z, name):
    z = np.asarray(z, dtype=np.float64)
    if name == "relu":
        return np.maximum(z, 0), (z > 0).astype(np.float64)
    if name == "gelu":
        with np.errstate(over="ignore", under="ignore"):
            pdf = np.exp(-0.5*z*z)/math.sqrt(2*math.pi)
        cdf = ndtr(z)
        return z*cdf, cdf + z*pdf
    if name == "selu":
        value, deriv = np.empty_like(z), np.empty_like(z)
        positive = z > 0
        value[positive], deriv[positive] = LAMBDA*z[positive], LAMBDA
        value[~positive] = LAMBDA*ALPHA*np.expm1(z[~positive])
        deriv[~positive] = LAMBDA*ALPHA*np.exp(z[~positive])
        return value, deriv
    if name == "sigmoid":
        value = expit(z)
        return value, value*(1-value)
    raise ValueError(name)


def reference_draws(config):
    n = config["width"]
    rng = np.random.default_rng(config["seed"])
    return (rng.standard_normal((n, 2)),
            rng.standard_normal((n, n))/math.sqrt(n),
            rng.standard_normal((n, n))/math.sqrt(n),
            rng.standard_normal(n)/n)


def explicit_matrices(config, state, W20, W30):
    if config["model"] == "dense":
        return state["W2"], state["W3"]
    scale = -2/(len(config["labels"])*config["width"]*(1+float(state["s"])))
    matrices = []
    for layer, initial in ((2, W20), (3, W30)):
        A, B = state["A"+str(layer)], state["B"+str(layer)]
        matrix = initial.copy()
        for degree in range(len(A)):
            matrix += scale*(2*degree+1)*(A[degree] @ B[degree].T)
        matrices.append(matrix)
    return tuple(matrices)


def torch_activation(z, name):
    import torch
    # Independent from the producer, using standard Torch primitives.
    if name == "relu":
        return torch.nn.functional.relu(z)
    if name == "gelu":
        return torch.nn.functional.gelu(z, approximate="none")
    if name == "selu":
        return torch.nn.functional.selu(z)
    if name == "sigmoid":
        return torch.sigmoid(z)
    raise ValueError(name)


def explicit_predictions(config, state, matrices, inputs, *, device="cpu", block=128):
    import torch
    tensors = [torch.as_tensor(v, dtype=torch.float64, device=device)
               for v in (state["w"], *matrices, state["c"])]
    w, W2, W3, c = tensors
    answer = []
    with torch.no_grad():
        for start in range(0, len(inputs), block):
            h = torch.as_tensor(inputs[start:start+block], dtype=torch.float64, device=device).T
            for W in (w, W2, W3):
                h = torch_activation(W @ h, config["activation"])
            answer.append((c @ h/config["width"]).cpu().numpy())
    return np.concatenate(answer)


def explicit_diagnostics(config, state, matrices, initial, *, device="cpu"):
    import torch
    w0, W20, W30, c0 = initial
    current = torch.tensor(config["inputs"],dtype=torch.float64,device=device).T
    original = current.clone()
    result = dict(w_motion_rms=rms(state["w"]-w0),c_motion_rms=rms(state["c"]-c0))
    diagnostics = {}
    for layer,(weight,initial_weight) in enumerate(zip((state["w"],*matrices),(w0,W20,W30)),1):
        z = (torch.as_tensor(weight,dtype=torch.float64,device=device) @ current).cpu().numpy()
        z0 = (torch.as_tensor(initial_weight,dtype=torch.float64,device=device) @ original).cpu().numpy()
        h,derivative = numpy_activation(z,config["activation"])
        h0,_ = numpy_activation(z0,config["activation"])
        current = torch.as_tensor(h,dtype=torch.float64,device=device)
        original = torch.as_tensor(h0,dtype=torch.float64,device=device)
        result["feature_motion_h"+str(layer)+"_rms"] = rms(h-h0)
        row = dict(activation_mean=float(h.mean()),activation_rms=rms(h),activation_min=float(h.min()),
                   activation_max=float(h.max()),preactivation_rms=rms(z),
                   nonpositive_preactivation_fraction=float(np.mean(z <= 0)),derivative_mean=float(derivative.mean()),
                   derivative_rms=rms(derivative),derivative_min=float(derivative.min()),derivative_max=float(derivative.max()),
                   small_derivative_fraction=float(np.mean(np.abs(derivative) <= 1e-3)),
                   zero_derivative_fraction=float(np.mean(derivative == 0)),negative_derivative_fraction=float(np.mean(derivative < 0)))
        if config["activation"] == "sigmoid":
            row["sigmoid_saturated_fraction"] = float(np.mean((h <= .01)|(h >= .99)))
        diagnostics["layer"+str(layer)] = row
    result["activation_diagnostics"] = diagnostics
    return result


def diagnostic_error(actual, expected):
    errors = []
    for key,value in actual.items():
        if isinstance(value,dict):
            errors.append(diagnostic_error(value,expected[key]))
        else:
            errors.append(abs(value-expected[key]))
    return max(errors,default=0.)


def integrity(run):
    run = Path(run)
    summary = json.loads((run/"summary.json").read_text())
    config = json.loads((run/"config.json").read_text())
    failures, checks = [], {}
    def check(name, value):
        checks[name] = bool(value)
        if not value:
            failures.append(name)
    check("effective_config_sha256", sha256(run/"config.json") == summary["effective_config_sha256"])
    check("arrays_sha256", sha256(run/"arrays.npz") == summary["arrays_sha256"])
    for filename, expected in summary.get("checkpoint_sha256", {}).items():
        check(filename+"_sha256", sha256(run/filename) == expected)
    for filename in ("arrays.npz", *summary.get("checkpoints", [])):
        with zipfile.ZipFile(run/filename) as archive:
            check(filename+"_crc", archive.testzip() is None)
    for filename, expected in summary["source_sha256"].items():
        check(filename+"_source_sha256", sha256(FOLDER/filename) == expected)
    x, y = np.asarray(config["inputs"]), np.asarray(config["labels"])
    check("data_sha256", array_hash(x, y) == summary["data_sha256"])
    for row in summary.get("observations", []):
        if row.get("kind") == "time":
            check(row["label"]+"_requested_time_exact", row["time"] == row["requested_time"])
            if summary["status"] == "target_loss":
                check(row["label"]+"_strictly_before_target", row["time"] < summary["time"])
    with np.load(run/"arrays.npz", allow_pickle=False) as a:
        check("query_sha256", array_hash(a["circle_inputs"]) == summary["query_sha256"])
        check("train_inputs", np.array_equal(x, a["train_inputs"]))
        check("train_labels", np.array_equal(y, a["train_labels"]))
        check("accepted_count", len(a["accepted_steps"]) == summary["accepted"])
        check("error_ratios", bool(np.isfinite(a["local_error_ratios"]).all()) and
              bool((a["local_error_ratios"] <= 1).all()))
        check("trace_times", bool((np.diff(a["times"]) > 0).all()) and
              np.allclose(np.diff(a["times"]), a["accepted_steps"], atol=1e-10, rtol=1e-12))
        check("trace_final", float(a["times"][-1]) == summary["time"] and
              float(a["losses"][-1]) == summary["training_mse"])
        check("trace_finite", bool(np.isfinite(a["losses"]).all()))
        check("observations_ordered", bool((np.diff(a["observation_times"]) >= 0).all()))
        check("observations_before_stop", bool((a["observation_times"] <= summary["time"]+1e-10).all()))
        rescored = np.mean((a["train_predictions"]-y)**2, axis=1)
        check("observed_training_mse", np.allclose(rescored, a["observation_training_mse"], atol=2e-12, rtol=2e-10))
        for label, actual in zip(a["observation_labels"], rescored):
            if str(label).startswith("loss_"):
                threshold = float(str(label)[5:])
                check(str(label)+"_within_one_percent", abs(actual-threshold) <= .01*threshold)
    return dict(run=str(run), checks=checks, failures=failures, passed=not failures)


def replay(run, *, device="cpu", labels=None):
    import torch
    torch.set_num_threads(1)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    start = time.monotonic()
    run = Path(run)
    result = integrity(run)
    config = json.loads((run/"config.json").read_text())
    summary = json.loads((run/"summary.json").read_text())
    w0, W20, W30, c0 = reference_draws(config)
    init_match = array_hash(w0, W20, W30, c0) == summary["initialization_hash"]
    result["initialization_hash"] = init_match
    if not init_match:
        result["failures"].append("initialization_hash")
    records = []
    with np.load(run/"arrays.npz", allow_pickle=False) as arrays:
        observations = list(map(str, arrays["observation_labels"]))
        sources = [("initial", None), ("final", "arrays.npz")]
        for filename in summary.get("checkpoints", []):
            label = filename.removeprefix("checkpoint_").removesuffix(".npz").replace("p", ".")
            sources.append((label, filename))
        for label, filename in sources:
            if labels is not None and label not in labels:
                continue
            if filename is None:
                state = dict(w=w0, W2=W20, W3=W30, c=c0)
                matrices = W20, W30
            else:
                with np.load(run/filename, allow_pickle=False) as checkpoint:
                    keys = ("w", "W2", "W3", "c") if config["model"] == "dense" else ("w", "c", "A2", "B2", "A3", "B3", "s")
                    state = {key:checkpoint[key] for key in keys}
                matrices = explicit_matrices(config, state, W20, W30)
            index = observations.index(label)
            circle = explicit_predictions(config, state, matrices, arrays["circle_inputs"], device=device)
            train = explicit_predictions(config, state, matrices, arrays["train_inputs"], device=device)
            circle_error = float(np.max(np.abs(circle-arrays["circle_predictions"][index])))
            train_error = float(np.max(np.abs(train-arrays["train_predictions"][index])))
            diagnostics = explicit_diagnostics(config,state,matrices,(w0,W20,W30,c0),device=device)
            diag_error = diagnostic_error(diagnostics,summary["observations"][index])
            passed = circle_error <= 2e-9 and train_error <= 2e-9 and diag_error <= 2e-9
            records.append(dict(label=label, circle_max_abs=circle_error, train_max_abs=train_error,
                                diagnostics_max_abs=diag_error,diagnostics=diagnostics,
                                training_mse=float(np.mean((train-arrays["train_labels"])**2)), passed=passed))
            if not passed:
                result["failures"].append(label+"_explicit_replay")
            del matrices, state
    result.update(replay=records, device=device, elapsed_seconds=time.monotonic()-start,
                  passed=not result["failures"])
    return result


def observations(run):
    with np.load(Path(run)/"arrays.npz", allow_pickle=False) as a:
        return {str(label):dict(time=float(t), mse=float(loss), prediction=pred.copy())
                for label,t,loss,pred in zip(a["observation_labels"],a["observation_times"],
                                           a["observation_training_mse"],a["circle_predictions"])}


def rms(value):
    return float(np.sqrt(np.mean(np.asarray(value)**2)))


def score(dense_fine, closure_fine, dense_coarse=None, closure_coarse=None):
    d, p = observations(dense_fine), observations(closure_fine)
    dc = observations(dense_coarse) if dense_coarse else {}
    pc = observations(closure_coarse) if closure_coarse else {}
    results = {}
    for label in sorted(set(d) & set(p)):
        difference = p[label]["prediction"]-d[label]["prediction"]
        error = rms(difference)
        nested = abs(error-rms(difference[::2]))
        record = dict(rms=error, nested_grid_change=nested,
                      dense_time=d[label]["time"], closure_time=p[label]["time"],
                      dense_mse=d[label]["mse"], closure_mse=p[label]["mse"])
        if label in dc and label in pc:
            ds = rms(d[label]["prediction"]-dc[label]["prediction"])
            ps = rms(p[label]["prediction"]-pc[label]["prediction"])
            milestone_valid = (not label.startswith("loss_") or all(
                abs(v[label]["mse"]-float(label[5:])) <= .01*float(label[5:]) for v in (d,p,dc,pc)))
            numerical = ds <= min(.005, .1*error) and ps <= min(.005, .1*error) and nested <= 1e-5 and milestone_valid
            record.update(dense_refinement_rms=ds, closure_refinement_rms=ps,
                          sensitivity_sum=ds+ps, milestone_valid=milestone_valid,
                          numerical_gate_pass=numerical)
        results[label] = record
    return results


def reproduction(original, repeated):
    result = dict(original=str(original), repeated=str(repeated), checks={})
    ac = json.loads((Path(original)/"config.json").read_text())
    bc = json.loads((Path(repeated)/"config.json").read_text())
    for key in ("case","activation","model","order","width","seed","inputs","labels","rtol","atol","query_count",
                "initial_step","max_step","max_time","max_steps","target_loss","milestones","observation_times"):
        result["checks"]["config_"+key] = ac[key] == bc[key]
    result["checks"]["gpu_swapped"] = {ac["device"],bc["device"]} == {"cuda:0","cuda:1"}
    asm = json.loads((Path(original)/"summary.json").read_text())
    bsm = json.loads((Path(repeated)/"summary.json").read_text())
    result["checks"]["initialization_hash"] = asm["initialization_hash"] == bsm["initialization_hash"]
    result["checks"]["source_hashes"] = asm["source_sha256"] == bsm["source_sha256"]
    with np.load(Path(original)/"arrays.npz", allow_pickle=False) as a, np.load(Path(repeated)/"arrays.npz", allow_pickle=False) as b:
        accepted = min(len(a["accepted_steps"]), len(b["accepted_steps"]))
        for key in ("accepted_steps", "local_error_ratios"):
            result["checks"][key+"_shared_prefix_exact"] = bool(np.array_equal(a[key][:accepted],b[key][:accepted]))
        for key in ("times", "losses"):
            result["checks"][key+"_shared_prefix_exact"] = bool(np.array_equal(a[key][:accepted+1],b[key][:accepted+1]))
        result["shared_accepted_steps"] = accepted
        same_endpoint = len(a["accepted_steps"]) == len(b["accepted_steps"]) and float(a["times"][-1]) == float(b["times"][-1])
        result["equal_endpoint"] = same_endpoint
        if same_endpoint:
            for key in ("w", "W2", "W3", "c", "A2", "B2", "A3", "B3", "s"):
                if key in a and key in b:
                    result["checks"][key+"_endpoint_exact"] = bool(np.array_equal(a[key],b[key]))
    oa, ob = observations(original), observations(repeated)
    for label in sorted(set(oa) & set(ob)):
        if label == "final" and not same_endpoint:
            continue
        result["checks"][label+"_time_exact"] = oa[label]["time"] == ob[label]["time"]
        result["checks"][label+"_mse_exact"] = oa[label]["mse"] == ob[label]["mse"]
        result["checks"][label+"_prediction_exact"] = bool(np.array_equal(oa[label]["prediction"],ob[label]["prediction"]))
    for filename in sorted(set(asm.get("checkpoints", [])) & set(bsm.get("checkpoints", []))):
        with np.load(Path(original)/filename,allow_pickle=False) as a, np.load(Path(repeated)/filename,allow_pickle=False) as b:
            result["checks"][filename+"_state_exact"] = set(a.files) == set(b.files) and all(np.array_equal(a[k],b[k]) for k in a.files)
    result["passed"] = all(result["checks"].values())
    return result


def selftest():
    """Independent, nonintegrating algebra tests of the production fields."""
    import torch
    import activation_moment_engine as producer
    from activation_circle_run import feature_diagnostics
    torch.set_num_threads(1)
    torch.manual_seed(719)
    checks, failures = [], []
    def close(name, actual, expected, atol=3e-12, rtol=3e-11):
        a = actual.detach().cpu().numpy() if isinstance(actual, torch.Tensor) else np.asarray(actual)
        b = expected.detach().cpu().numpy() if isinstance(expected, torch.Tensor) else np.asarray(expected)
        error = float(np.max(np.abs(a-b))) if a.size else 0.
        passed = bool(np.isfinite(a).all()) and bool(np.isfinite(b).all()) and bool(np.allclose(a,b,atol=atol,rtol=rtol))
        checks.append(dict(name=name,max_abs_error=error,passed=passed))
        if not passed:
            failures.append(name)
    theta = np.asarray([.13,.5,1.9,3.3,5.7])
    x = np.column_stack((np.cos(theta),np.sin(theta)))
    y = np.asarray([1.,-1.,1.,-1.,1.])
    n, M = 11, len(y)
    first_initialization = None
    for activation in ACTIVATIONS:
        z = torch.tensor([-12.,-3.,-.2,-1e-9,0.,1e-9,.2,3.,12.],dtype=torch.float64,requires_grad=True)
        value = torch_activation(z,activation)
        derivative = torch.autograd.grad(value.sum(),z)[0]
        close(activation+"_activation",producer.activation_value(activation,z),value)
        close(activation+"_derivative_autograd",producer.activation_derivative(activation,z),derivative)
        zext = np.asarray([-1e300,-1000.,-100.,0.,100.,1000.,1e300])
        values, derivatives = numpy_activation(zext,activation)
        tensor = torch.tensor(zext,dtype=torch.float64)
        close(activation+"_extreme_values",producer.activation_value(activation,tensor),values)
        close(activation+"_extreme_derivatives",producer.activation_derivative(activation,tensor),derivatives)
        dense = producer.ActivationDenseEngine(2,n,x,y,activation=activation,seed=271)
        initial = dense.initial_state()
        current_initialization = [v.clone() for v in (initial.w,dense.W20,dense.W30,initial.c)]
        if first_initialization is None:
            first_initialization = current_initialization
        for j,(a,b) in enumerate(zip(current_initialization,first_initialization)):
            close(activation+"_shared_initialization_"+str(j),a,b,0,0)
        expected_draws = reference_draws(dict(width=n,seed=271))
        for j,(a,b) in enumerate(zip(current_initialization,expected_draws)):
            close(activation+"_numpy_draw_"+str(j),a,b,0,0)
        state = initial.clone()
        for value in state.tensors():
            value.add_(.09*torch.randn_like(value))
        parameters = [value.detach().clone().requires_grad_(True) for value in state.tensors()]
        w,W2,W3,c = parameters
        inputs = torch.tensor(x,dtype=torch.float64)
        h1 = torch_activation(w @ inputs.T,activation)
        h2 = torch_activation(W2 @ h1,activation)
        h3 = torch_activation(W3 @ h2,activation)
        f = c @ h3/n
        loss = (f-torch.tensor(y,dtype=torch.float64)).square().mean()
        gradients = torch.autograd.grad(loss,parameters)
        rhs = dense.rhs(state)
        for name,actual,gradient,mobility in zip(state.names(),rhs.tensors(),gradients,(n,1,1,n)):
            close(activation+"_physical_gradient_"+name,actual,-mobility*gradient)
        close(activation+"_dense_predict",dense.predict(state,inputs),f)
        for order in (1,2,3):
            prefix = activation+"_P"+str(order)
            engine = producer.ActivationMomentEngine(2,n,order,x,y,activation=activation,seed=271)
            moment = engine.initial_state()
            init_fields = dense.fields(initial)
            close(prefix+"_B2_initial",moment.B2[0],init_fields["h1"],0,0)
            close(prefix+"_B3_initial",moment.B3[0],init_fields["h2"],0,0)
            initial_rhs = engine.rhs(moment)
            initial_dense_rhs = dense.rhs(initial)
            for name in ("w","c"):
                close(prefix+"_initial_velocity_"+name,getattr(initial_rhs,name),getattr(initial_dense_rhs,name))
            for layer in (2,3):
                dl,dr = engine.derivative_factors(moment,layer,initial_rhs)
                close(prefix+"_initial_velocity_W"+str(layer),dl@dr.T,getattr(initial_dense_rhs,"W"+str(layer)))
                close(prefix+"_initial_defect_W"+str(layer),engine.defect_frobenius(moment,layer),0.,3e-14,0)
            # Noninitial independent moment arrays expose sign/transpose/clock bugs.
            for name in ("w","c","A2","B2","A3","B3"):
                getattr(moment,name).add_(.15*torch.randn_like(getattr(moment,name)))
            moment.s.fill_(.7)
            values = {key:value.numpy() for key,value in zip(moment.names(),moment.tensors())}
            matrices = explicit_matrices(dict(model="moment",labels=y,width=n),values,
                                         engine.W20.numpy(),engine.W30.numpy())
            physical = producer.DeepDenseState(moment.w,torch.tensor(matrices[0]),torch.tensor(matrices[1]),moment.c)
            fields = dense.fields(physical)
            moment_fields = engine.fields(moment)
            for key in ("f","h1","h2","h3","delta1","delta2","delta3"):
                close(prefix+"_physical_fields_"+key,moment_fields[key],fields[key])
            config = dict(model="moment",activation=activation,inputs=x,labels=y,width=n)
            query_angles = np.arange(31)*2*np.pi/31
            query = np.column_stack((np.cos(query_angles),np.sin(query_angles)))
            close(prefix+"_independent_query_replay",explicit_predictions(config,values,matrices,query),engine.predict(moment,query))
            diagnostic_reference = explicit_diagnostics(config,values,matrices,expected_draws)
            observed_diagnostics = feature_diagnostics(engine,moment,moment_fields,{j:init_fields["h"+str(j)] for j in (1,2,3)})
            close(prefix+"_independent_diagnostics",diagnostic_error(diagnostic_reference,observed_diagnostics),0.,3e-12,0)
            velocity = engine.rhs(moment)
            physical_velocity = dense.rhs(physical)
            for name in ("w","c"):
                close(prefix+"_physical_velocity_"+name,getattr(velocity,name),getattr(physical_velocity,name))
            rho,length = fields["rho"],1+moment.s
            close(prefix+"_clock",velocity.s,rho)
            for layer in (2,3):
                W = torch.tensor(matrices[layer-2])
                probe = torch.randn((n,7),dtype=torch.float64)
                close(prefix+"_action_"+str(layer),engine.apply_hidden(moment,layer,probe),W@probe)
                close(prefix+"_transpose_"+str(layer),engine.apply_hidden(moment,layer,probe,transpose=True),W.T@probe)
                A,B = getattr(moment,"A"+str(layer)),getattr(moment,"B"+str(layer))
                da,db = getattr(velocity,"A"+str(layer)),getattr(velocity,"B"+str(layer))
                for T,dT,source,name in ((A,da,fields["delta"+str(layer)]*fields["r"],"A"),
                                       (B,db,rho*fields["h"+str(layer-1)],"B")):
                    for k in range(order):
                        expected = source-rho/length*(k*T[k]+sum(((2*j+1)*T[j] for j in range(k)),torch.zeros_like(T[k])))
                        close(prefix+"_transport_"+name+str(layer)+"_"+str(k),dT[k],expected)
                derivative_matrix = torch.zeros_like(W)
                for k in range(order):
                    derivative_matrix += (-2/(M*n*length))*(2*k+1)*(da[k]@B[k].T+A[k]@db[k].T-rho/length*(A[k]@B[k].T))
                explicit_defect = derivative_matrix-getattr(physical_velocity,"W"+str(layer))
                left,right = engine.defect_factors(moment,layer)
                close(prefix+"_defect_"+str(layer),left@right.T,explicit_defect)
                dl,dr = engine.derivative_factors(moment,layer,velocity)
                close(prefix+"_derivative_factors_"+str(layer),dl@dr.T,derivative_matrix)
                close(prefix+"_defect_norm_"+str(layer),engine.defect_frobenius(moment,layer),torch.linalg.vector_norm(explicit_defect))
            engine.labels = engine.predict(moment,engine.inputs).clone()
            zero = engine.rhs(moment)
            for name,value in zip(zero.names(),zero.tensors()):
                close(prefix+"_zero_residual_"+name,value,torch.zeros_like(value),0,0)
            for layer in (2,3):
                close(prefix+"_zero_defect_"+str(layer),engine.defect_frobenius(moment,layer),0.,0,0)
    return dict(checks=checks,failures=failures,passed=not failures,check_count=len(checks),
                sources={name:sha256(FOLDER/name) for name in ("activation_moment_engine.py","deep_moment_engine.py","moment_engine.py")},
                numpy=np.__version__,torch=torch.__version__,device="cpu",training_runs=0)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("selftest", "integrity", "replay", "score", "reproduction"))
    parser.add_argument("paths", nargs="*")
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--label", action="append")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        raise FileExistsError("Audit evidence is append-only: "+str(out))
    def preserve_failure(function,path,**kwargs):
        try:
            result = function(path,**kwargs)
        except Exception as error:
            result = dict(run=str(path),passed=False,failures=["audit_exception"],
                          exception=type(error).__name__,message=str(error),traceback=traceback.format_exc())
        result["auditor_sha256"] = sha256(Path(__file__))
        return result
    if args.mode == "selftest":
        result = selftest()
    elif args.mode == "integrity":
        result = [preserve_failure(integrity,path) for path in args.paths]
    elif args.mode == "replay":
        result = [preserve_failure(replay,path,device=args.device,labels=args.label) for path in args.paths]
    elif args.mode == "score":
        result = score(*args.paths)
    else:
        result = reproduction(*args.paths)
    out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(dict(output=str(out), completed=True)))


if __name__ == "__main__":
    main()
