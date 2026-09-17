"""Independent NumPy/CPU forward replay of saved study checkpoints.

Does not import either engine, the runner, initializer, or dataset producer;
never evolves parameters. Float64 arithmetic evaluates the saved finite
weights and the input values rounded to the run's declared working dtype.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import struct
import time

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "data/generated/first_order_dimension_mnist"


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def group_path(name):
    """Resolve only one named result group inside this study."""
    if not name or Path(name).name != name or name in (".",".."):
        raise ValueError("run groups must be a single study-owned directory name")
    path = (BASE/name).resolve()
    path.relative_to(BASE.resolve())
    return path


def independent_data(config, summary):
    if config["task"] == "toy":
        rng = np.random.default_rng(20260915)
        data = {}
        for part, count in (("train",24), ("val",128), ("test",512)):
            U = rng.normal(size=(count,8))
            U /= np.linalg.norm(U,axis=1,keepdims=True)
            data[part+"_u"] = U
            data[part+"_y"] = np.tanh(2*U[:,0]-1.5*U[:,1])+0.35*np.sin(3*U[:,2])
        return data, {"method":"independent seeded regeneration of declared toy input/target"}
    if config["task"] != "mnist":
        raise ValueError("only completed toy or MNIST final checkpoints are replayed")
    path = Path(summary["data"]["path"]) / "dataset.npz"
    path.resolve().relative_to(BASE.resolve())
    expected = summary["data"]["metadata"]["dataset_sha256"]
    actual = digest(path)
    if actual != expected:
        raise ValueError("dataset hash no longer matches frozen run metadata")
    with np.load(path,allow_pickle=False) as saved:
        data = {key:saved[key].copy() for key in saved.files}
    if np.intersect1d(data["train_ids"],data["val_ids"]).size:
        raise ValueError("training/validation IDs overlap")
    return data, {"method":"hash-verified frozen official split", "sha256":actual,
                  "training_validation_ID_disjoint":True}


def fields(saved, U, model, *, initial=False):
    if model == "network":
        prefix = "initial_" if initial else ""
        w = saved[prefix+"w"]
        M = saved[prefix+"M"]
        c = saved[prefix+"c"]
        h1 = np.tanh(w @ U.T)
        h2 = np.tanh(M @ h1)
        f = np.sum(c[:,None]*h2,axis=0)/len(c)
        return h1,h2,f
    w = saved["g"] if initial else saved["w"]
    M = saved["D"] if initial else saved["M"]
    h1 = np.tanh(w @ U.T)
    a = saved["b1"].T @ (saved["p1"][:,None]*h1)
    h2 = np.tanh(saved["b2"] @ (M @ a))
    f = np.sum(saved["p2"][:,None]*saved["c"][:,None]*h2,axis=0)
    if initial:
        f = np.zeros(len(U))
    return h1,h2,f


def predict(saved, U, model, block=128):
    return np.concatenate([fields(saved,U[start:start+block],model)[2]
                           for start in range(0,len(U),block)])


def difference(actual, expected, *, tolerance):
    error = actual-expected
    result = {"max_absolute":float(np.max(np.abs(error))),
              "rms":float(np.sqrt(np.mean(error*error))),
              "tolerance_absolute":tolerance}
    result["pass"] = result["max_absolute"] <= tolerance
    if not result["pass"]:
        raise AssertionError(result)
    return result


def metrics(pred,y):
    return {"mse":float(np.mean((pred-y)**2)),
            "accuracy":float(np.mean((pred>=0)==(y>=0)))}


def independent_metrics(pred,reference):
    residual = pred-reference
    a = np.abs(residual)
    norm = np.sqrt(np.dot(reference,reference)/len(reference))
    rms = np.sqrt(np.dot(residual,residual)/len(residual))
    centered_pred = pred-np.mean(pred)
    centered_ref = reference-np.mean(reference)
    correlation = (np.dot(centered_pred,centered_ref)/np.sqrt(np.dot(centered_pred,centered_pred)*np.dot(centered_ref,centered_ref))
                   if norm>1e-15 and np.std(pred)>1e-15 else None)
    return {"rms":rms,"relative_rms":rms/max(norm,1e-30),"mae":sum(a)/len(a),
            "median_absolute":np.percentile(a,50),"p90_absolute":np.percentile(a,90),
            "p95_absolute":np.percentile(a,95),"p99_absolute":np.percentile(a,99),
            "max_absolute":max(a),"bias":sum(residual)/len(residual),
            "sign_disagreements":sum((pred>=0)!=(reference>=0)),
            "sign_agreement":np.mean((pred>=0)==(reference>=0)),
            "within_0_05":np.mean(a<=0.05),"within_0_1":np.mean(a<=0.1),
            "within_0_2":np.mean(a<=0.2),"correlation":correlation}


def audit_dataset(directory, output):
    """Regenerate every split, label, and normalized image from local IDXs."""
    directory = Path(directory).resolve()
    directory.relative_to(BASE.resolve())
    meta = json.loads((directory/"metadata.json").read_text())
    assert digest(directory/"dataset.npz") == meta["dataset_sha256"]
    raw = BASE/"mnist_raw"
    source_hashes = {}
    def idx(name):
        payload = (raw/name).read_bytes()
        assert hashlib.md5(payload).hexdigest() == meta["sources"][name]["md5"]
        source_hashes[name] = hashlib.sha256(payload).hexdigest()
        assert source_hashes[name] == meta["sources"][name]["sha256"]
        unpacked = gzip.decompress(payload)
        assert unpacked[:3] == bytes((0,0,8))
        dimensions = unpacked[3]
        shape = struct.unpack(">"+"I"*dimensions,unpacked[4:4+4*dimensions])
        values = np.frombuffer(unpacked,dtype=np.uint8,offset=4+4*dimensions)
        return values.reshape(shape)
    train_images,train_labels = idx("train-images-idx3-ubyte.gz"),idx("train-labels-idx1-ubyte.gz")
    test_images,test_labels = idx("t10k-images-idx3-ubyte.gz"),idx("t10k-labels-idx1-ubyte.gz")
    rng = np.random.default_rng(meta["split_seed"])
    train_ids,val_ids = [],[]
    for digit in meta["digits"]:
        order = rng.permutation(np.flatnonzero(train_labels==digit))
        val_ids.extend(order[:500]);train_ids.extend(order[500:])
    expected_ids = {"train":rng.permutation(train_ids),"val":np.asarray(val_ids),
                    "test":np.flatnonzero(np.isin(test_labels,meta["digits"]))}
    assert not np.intersect1d(expected_ids["train"],expected_ids["val"]).size
    result = {"status":"PASS","dataset_sha256":meta["dataset_sha256"],
              "raw_sha256":source_hashes,"checks":{},"source_sha256":digest(__file__)}
    with np.load(directory/"dataset.npz",allow_pickle=False) as saved:
        for part in ("train","val","test"):
            images,labels = (test_images,test_labels) if part=="test" else (train_images,train_labels)
            ids = expected_ids[part]
            np.testing.assert_array_equal(saved[part+"_ids"],ids)
            expected_y = np.where(labels[ids]==meta["positive_digit"],1.,-1.).astype(np.float32)
            pixels = images[ids].reshape(len(ids),-1).astype(np.float64)/255
            expected_U = (pixels/np.linalg.norm(pixels,axis=1,keepdims=True)).astype(np.float32)
            np.testing.assert_array_equal(saved[part+"_y"],expected_y)
            np.testing.assert_array_equal(saved[part+"_u"],expected_U)
            result["checks"][part] = {"count":len(ids),"ids_exact":True,"labels_exact":True,
                                      "preprocessing_exact":True,"official_source":"test" if part=="test" else "train"}
    output.mkdir(parents=True,exist_ok=True)
    (output/"dataset_audit.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"dataset_audit":"PASS","directory":str(directory)}),flush=True)
    return result


def audit_analysis(directory, output, *, run_group="main", analysis_source=None):
    """Independently recompute the primary same-time validation comparison."""
    directory = Path(directory).resolve()
    directory.relative_to(BASE.resolve())
    report = json.loads((directory/"summary.json").read_text())
    group = group_path(run_group)
    if "run_group" in report:
        assert report["run_group"] == run_group
    seeds = (1729,2718,3141)
    original = {}
    time_sets = []
    source_hashes = {}
    first_summary = json.loads((group/"network_1729/summary.json").read_text())
    dataset_path = Path(first_summary["data"]["path"])/"dataset.npz"
    dataset_path.resolve().relative_to(BASE.resolve())
    dataset_hash = digest(dataset_path)
    with np.load(dataset_path,allow_pickle=False) as data:
        ids,labels = data["val_ids"].copy(),data["val_y"].copy()
    assert len(ids) == len(set(ids.tolist())) == len(labels) == 1000
    for model in ("network","closure"):
        original[model] = []
        for seed in seeds:
            path = group/f"{model}_{seed}"
            summary = json.loads((path/"summary.json").read_text())
            if run_group in ("main","main4096","pca4096"):
                assert summary["configuration"]["width"] == (2048 if run_group=="main" else 4096)
            assert summary["configuration"]["model"] == model and summary["configuration"]["seed"] == seed
            assert summary["data"]["metadata"]["dataset_sha256"] == dataset_hash
            with np.load(path/"observations.npz",allow_pickle=False) as saved:
                np.testing.assert_array_equal(saved["val_y"],labels)
                values = {float(t):np.asarray(pred,dtype=np.float64)
                          for t,pred in zip(saved["times"],saved["val_predictions"])}
                assert all(pred.shape==(1000,) for pred in values.values())
            original[model].append(values)
            time_sets.append(set(values))
            source_hashes[f"{model}_{seed}"] = digest(path/"observations.npz")
    times = sorted(set.intersection(*time_sets))
    assert report["common_final_time"] == times[-1]
    assert report["validation_count"] == len(labels)
    with np.load(directory/"sample_predictions.npz",allow_pickle=False) as exported:
        np.testing.assert_array_equal(exported["times"],times)
        np.testing.assert_array_equal(exported["official_train_ids"],ids)
        np.testing.assert_array_equal(exported["labels"],labels)
        for model in original:
            expected = np.asarray([[values[t] for t in times] for values in original[model]])
            np.testing.assert_array_equal(exported[model],expected)
    largest_metric_error = 0.
    def compare(actual,expected):
        nonlocal largest_metric_error
        for key,value in expected.items():
            if value is None:
                assert actual[key] is None
                continue
            discrepancy = abs(actual[key]-value)
            largest_metric_error = max(largest_metric_error,float(discrepancy))
            if key=="sign_disagreements":
                assert actual[key]==value
            else:
                np.testing.assert_allclose(actual[key],value,atol=2e-7,rtol=2e-7)
    assert len(report["trajectory"]) == len(times)
    for t,row in zip(times,report["trajectory"]):
        assert row["time"] == t
        networks = [values[t] for values in original["network"]]
        closures = [values[t] for values in original["closure"]]
        netmean = sum(networks)/len(networks)
        closuremean = sum(closures)/len(closures)
        for actual,pred in zip(row["individual_closure_vs_network_mean"],closures):
            compare(actual,independent_metrics(pred,netmean))
        compare(row["closure_mean_vs_network_mean"],independent_metrics(closuremean,netmean))
        expected_pairwise = [independent_metrics(networks[i],networks[j])["rms"]
                             for i,j in ((0,1),(0,2),(1,2))]
        np.testing.assert_allclose(row["network_pairwise_rms"],expected_pairwise,atol=2e-12,rtol=2e-12)
    final = times[-1]
    networks = [x[final] for x in original["network"]]
    closures = [x[final] for x in original["closure"]]
    for i,cs in enumerate(seeds):
        for j,ns in enumerate(seeds):
            row = next(x for x in report["all_individual_seed_pairs"]
                       if x["closure_seed"]==cs and x["network_seed"]==ns)
            compare(row,independent_metrics(closures[i],networks[j]))
    netmean,closuremean = sum(networks)/3,sum(closures)/3
    extra_checks = {}
    if "within_class" in report:
        for digit,sign in ((3,1),(5,-1)):
            mask = labels==sign
            row = report["within_class"][str(digit)]
            assert row["count"] == int(mask.sum()) == 500
            np.testing.assert_allclose(row["network_mean_output_sd"],np.std(netmean[mask]),atol=2e-12,rtol=2e-12)
            for actual,pred in zip(row["individual_closure_vs_network_mean"],closures):
                compare(actual,independent_metrics(pred[mask],netmean[mask]))
        extra_checks["within_class_metrics"] = True
    if "label_only_diagnostic" in report:
        compare(report["label_only_diagnostic"],independent_metrics(labels.astype(np.float64),netmean))
        assert "true validation label" in report["label_only_diagnostic"]["description"]
        extra_checks["true_label_diagnostic_metrics"] = True
    if "provenance" in report:
        assert report["provenance"]["analysis_sha256"] == digest(analysis_source or Path(__file__).with_name("VALIDATION_ANALYSIS.py"))
        assert report["provenance"]["dataset_sha256"] == dataset_hash
        for model in original:
            for seed in seeds:
                assert report["provenance"]["run_summary_sha256"][f"{model}_{seed}"] == digest(group/f"{model}_{seed}/summary.json")
        extra_checks["analysis_dataset_run_provenance"] = True
    csv = np.loadtxt(directory/"validation_samples.csv",delimiter=",",skiprows=1)
    expected_csv = np.column_stack([ids,labels,*networks,*closures,netmean,closuremean,closuremean-netmean])
    np.testing.assert_array_equal(csv,expected_csv)
    order = np.argsort(np.abs(closuremean-netmean))[::-1]
    for expected_row,example in zip(order,report["worst_examples"]):
        assert example["validation_row"] == expected_row
        assert example["official_train_id"] == ids[expected_row]
        assert example["digit"] == (3 if labels[expected_row]>0 else 5)
        np.testing.assert_allclose(example["network_outputs"],[p[expected_row] for p in networks],atol=0,rtol=0)
        np.testing.assert_allclose(example["closure_outputs"],[p[expected_row] for p in closures],atol=0,rtol=0)
    result = {"status":"PASS","run_group":run_group,"common_final_time":final,"validation_count":len(ids),
              "shared_time_count":len(times),"individual_seed_pairs":9,
              "maximum_scalar_metric_difference":largest_metric_error,
              "all_exported_pointwise_predictions_exact":True,"csv_pointwise_predictions_exact":True,
              "worst_example_ids_confirmed":True,
              "dataset_sha256":dataset_hash,"observations_sha256":source_hashes,
              "analysis_summary_sha256":digest(directory/"summary.json"),"source_sha256":digest(__file__)}
    result.update(extra_checks)
    output.mkdir(parents=True,exist_ok=True)
    (output/"validation_analysis_audit.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result),flush=True)
    return result


def audit_control(model, output, *, run_group="main", control_group=None):
    """Compare completed half-step outputs against original equal-time rows."""
    control_group = control_group or ("controls4096" if run_group=="main4096" else "main_controls")
    main = group_path(run_group)/f"{model}_1729"
    control = group_path(control_group)/f"{model}_halfstep"
    original = json.loads((main/"summary.json").read_text())
    refined = json.loads((control/"summary.json").read_text())
    assert refined["configuration"]["step"]*2 == original["configuration"]["step"]
    for key in ("task","model","width","seed","dtype","digits","block"):
        assert refined["configuration"][key] == original["configuration"][key]
    assert refined["configuration"].get("dataset") == original["configuration"].get("dataset")
    assert refined["data"]["metadata"]["dataset_sha256"] == original["data"]["metadata"]["dataset_sha256"]
    assert refined["final_time"] == original["final_time"] > 0
    final_time = original["final_time"]
    rows = []
    with np.load(main/"observations.npz",allow_pickle=False) as a, np.load(control/"observations.npz",allow_pickle=False) as b:
        np.testing.assert_array_equal(a["val_y"],b["val_y"])
        np.testing.assert_array_equal(a["times"],b["times"])
        y = a["val_y"]
        for t in sorted(set(a["times"]).intersection(b["times"])):
            reference = a["val_predictions"][np.flatnonzero(a["times"]==t)[0]].astype(np.float64)
            actual = b["val_predictions"][np.flatnonzero(b["times"]==t)[0]].astype(np.float64)
            error = actual-reference
            rms = float(np.linalg.norm(error)/np.sqrt(len(error)))
            accuracy_delta = float(abs(np.mean((actual>=0)==(y>=0))-np.mean((reference>=0)==(y>=0))))
            rows.append({"time":float(t),"validation_rms_difference":rms,
                         "maximum_absolute_difference":float(max(abs(error))),
                         "accuracy_difference_percentage_points":100*accuracy_delta,
                         "sign_disagreements":int(np.sum((actual>=0)!=(reference>=0))),
                         "pass":rms<=0.002 and accuracy_delta<=0.002})
    result = {"model":model,"run_group":run_group,"control_group":control_group,
              "comparison_type":"refined-step numerical reproduction; not a same-configuration bitwise full rerun",
              "status":"PASS" if rows[-1]["pass"] else "FAIL",
              "full_horizon":final_time,"endpoint":rows[-1],"all_common_saved_times_pass":all(x["pass"] for x in rows),
              "maximum_saved_time_rms":max(x["validation_rms_difference"] for x in rows),
              "maximum_saved_time_absolute_difference":max(x["maximum_absolute_difference"] for x in rows),
              "maximum_saved_time_sign_disagreements":max(x["sign_disagreements"] for x in rows),
              "maximum_saved_time_accuracy_difference_percentage_points":max(x["accuracy_difference_percentage_points"] for x in rows),
              "original_selected_time":original["selected_time"],"refined_selected_time":refined["selected_time"],
              "trajectory":rows,"source_sha256":digest(__file__),
              "original_summary_sha256":digest(main/"summary.json"),"control_summary_sha256":digest(control/"summary.json")}
    output.mkdir(parents=True,exist_ok=True)
    (output/(model+"_halfstep_audit.json")).write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"model":model,"halfstep_audit":result["status"],"endpoint":rows[-1],
                      "all_common_saved_times_pass":result["all_common_saved_times_pass"]}),flush=True)
    return result


def audit_halfstep_gate(output, *, run_group="pca4096", control_group="pca_controls"):
    """Publish the two-model gate only from completed equal-horizon artifacts."""
    summaries = {}
    core = ("RUN.py","P1_ENGINE.py","NETWORK_ENGINE.py","P1_INITIALIZATION.py")
    frozen_sources = {}
    for model in ("network","closure"):
        paths = (group_path(run_group)/f"{model}_1729",group_path(control_group)/f"{model}_halfstep")
        sources = []
        for path in paths:
            summary = json.loads((path/"summary.json").read_text())
            config = summary["configuration"]
            assert config["task"]=="mnist" and config["width"]==4096 and config["seed"]==1729
            assert config["dtype"]=="float32" and config["block"]==2048
            assert config["environment"]["tf32"] == False
            assert summary["final_time"]==600 and summary["stop_reason"]=="horizon"
            assert summary["steps"]*config["step"]==600
            dataset_file = Path(summary["data"]["path"])/"dataset.npz"
            dataset_file.resolve().relative_to(BASE.resolve())
            assert digest(dataset_file)==summary["data"]["metadata"]["dataset_sha256"]
            with np.load(path/"observations.npz",allow_pickle=False) as a, np.load(dataset_file,allow_pickle=False) as data:
                np.testing.assert_array_equal(a["times"],np.arange(0,601,10))
                np.testing.assert_array_equal(a["val_y"],data["val_y"])
                assert a["val_predictions"].shape==(61,1000)
            actual = {name:digest(path/"source"/name) for name in core}
            assert all(value==config["source_sha256"][name] for name,value in actual.items())
            sources.append(actual)
        assert sources[0] == sources[1]
        frozen_sources[model] = sources[0]
        summaries[model] = audit_control(model,output,run_group=run_group,control_group=control_group)
    result = {"passed":all(r["status"]=="PASS" and r["all_common_saved_times_pass"] for r in summaries.values()),
              "run_group":run_group,"control_group":control_group,"horizon":600,"recorded_times":61,
              "gate":{"maximum_per_time_validation_rms":0.002,"maximum_per_time_accuracy_difference_percentage_points":0.2,
                      "sign_changes":"recorded at every time; not an additional zero-sign-change criterion"},
              "models":summaries,"frozen_core_source_sha256":frozen_sources,"source_sha256":digest(__file__),
              "scope":"Full-horizon refined-step numerical reproduction; not a same-configuration bitwise rerun"}
    output.mkdir(parents=True,exist_ok=True)
    path = output/"halfstep_gate.json"
    with path.open("x") as handle:
        json.dump(result,handle,indent=2)
        handle.write("\n")
    print(json.dumps({"halfstep_gate":str(path),"passed":result["passed"]}),flush=True)
    return result


def audit_reproduction(model, output, *, run_group="main", reproduction_group="reproduction"):
    """Check a fresh same-configuration rerun against every original record."""
    original_path = group_path(run_group)/f"{model}_1729"
    rerun_path = group_path(reproduction_group)/f"{model}_1729"
    original = json.loads((original_path/"summary.json").read_text())
    rerun = json.loads((rerun_path/"summary.json").read_text())
    for key in ("task","model","width","seed","digits","dtype","step","block","horizon","maximum_horizon","continue_validation"):
        assert original["configuration"][key] == rerun["configuration"][key],key
    assert original["data"]["metadata"]["dataset_sha256"] == rerun["data"]["metadata"]["dataset_sha256"]
    for key in ("selected_time","final_time","steps","stop_reason"):
        assert original[key] == rerun[key],key
    with np.load(original_path/"observations.npz",allow_pickle=False) as a, np.load(rerun_path/"observations.npz",allow_pickle=False) as b:
        np.testing.assert_array_equal(a["times"],b["times"])
        np.testing.assert_array_equal(a["val_y"],b["val_y"])
        first,last = a["val_predictions"].astype(np.float64),b["val_predictions"].astype(np.float64)
        differences = last-first
        row_rms = np.sqrt(np.mean(differences**2,axis=1))
        row_max = np.max(np.abs(differences),axis=1)
        sign_disagreements = int(np.sum((first>=0)!=(last>=0)))
        assert np.max(row_rms)<=1e-5 and np.max(row_max)<=1e-4 and sign_disagreements==0
        prediction_checks = {"recorded_times":len(a["times"]),"validation_count":first.shape[1],
                             "largest_per_time_rms":float(np.max(row_rms)),
                             "largest_absolute_difference":float(np.max(row_max)),
                             "classification_sign_changes":sign_disagreements,
                             "validation_arrays_bitwise_equal":bool(np.array_equal(a["val_predictions"],b["val_predictions"]))}
        ancillary = {}
        for key in ("train_predictions","gram1","gram2","test_predictions","test_final_predictions"):
            delta = np.asarray(a[key],dtype=np.float64)-np.asarray(b[key],dtype=np.float64)
            ancillary[key] = {"max_absolute":float(np.max(abs(delta))),"bitwise_equal":bool(np.array_equal(a[key],b[key]))}
    checkpoint_checks = {}
    for name in ("best_state.npz","final_state.npz"):
        with np.load(original_path/name,allow_pickle=False) as a, np.load(rerun_path/name,allow_pickle=False) as b:
            assert set(a.files)==set(b.files)
            checkpoint_checks[name] = {key:bool(np.array_equal(a[key],b[key])) for key in a.files}
    result = {"model":model,"run_group":run_group,"reproduction_group":reproduction_group,
              "status":"PASS","selected_time":rerun["selected_time"],"final_time":rerun["final_time"],
              "same_training_configuration":True,"same_dataset_hash":True,
              "validation":prediction_checks,"ancillary":ancillary,"checkpoint_arrays_bitwise_equal":checkpoint_checks,
              "source_sha256":digest(__file__),"original_summary_sha256":digest(original_path/"summary.json"),
              "reproduction_summary_sha256":digest(rerun_path/"summary.json")}
    output.mkdir(parents=True,exist_ok=True)
    (output/(model+"_reproduction_audit.json")).write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"model":model,"reproduction_audit":"PASS","validation":prediction_checks}),flush=True)
    return result


def audit_prefix(model, output, *, run_group="main4096", prefix_group="speed4096"):
    """Compare the saved first T100 of a full run with both earlier speed runs."""
    path = group_path(run_group)/f"{model}_1729"
    full = json.loads((path/"summary.json").read_text())
    assert full["configuration"]["width"] == 4096
    assert full["final_time"] >= 100
    with np.load(path/"observations.npz",allow_pickle=False) as a:
        full_arrays = {k:a[k].copy() for k in ("times","train_predictions","val_predictions","gram1","gram2","train_y","val_y")}
    rows = []
    for repetition in (1,2):
        prior_path = group_path(prefix_group)/f"{model}_4096_r{repetition}"
        prior = json.loads((prior_path/"summary.json").read_text())
        for key in ("task","model","width","seed","digits","dtype","step","block"):
            assert full["configuration"][key] == prior["configuration"][key],key
        assert full["configuration"]["environment"]["tf32"] == prior["configuration"]["environment"]["tf32"] == False
        assert full["data"]["metadata"]["dataset_sha256"] == prior["data"]["metadata"]["dataset_sha256"]
        assert prior["final_time"] == 100
        with np.load(prior_path/"observations.npz",allow_pickle=False) as a:
            prior_arrays = {k:a[k].copy() for k in full_arrays}
        np.testing.assert_array_equal(prior_arrays["times"],np.arange(0,101,10))
        indices = [int(np.flatnonzero(full_arrays["times"]==t)[0]) for t in prior_arrays["times"]]
        checks = {}
        for key in ("train_predictions","val_predictions","gram1","gram2"):
            first,last = prior_arrays[key],full_arrays[key][indices]
            assert first.shape == last.shape
            delta = last.astype(np.float64)-first.astype(np.float64)
            largest_rms = float(np.max(np.sqrt(np.mean(delta.reshape(len(indices),-1)**2,axis=1))))
            largest_abs = float(np.max(np.abs(delta)))
            assert largest_rms<=1e-5 and largest_abs<=1e-4
            checks[key] = {"largest_per_time_rms":largest_rms,"maximum_absolute_difference":largest_abs,
                           "bitwise_equal":bool(np.array_equal(first,last))}
            if key.endswith("predictions"):
                flips = int(np.sum((first>=0)!=(last>=0)))
                assert flips == 0
                checks[key]["classification_sign_changes"] = flips
        for key in ("train_y","val_y"):
            np.testing.assert_array_equal(full_arrays[key],prior_arrays[key])
        rows.append({"repetition":repetition,"status":"PASS","checks":checks,
                     "prefix_summary_sha256":digest(prior_path/"summary.json")})
    result = {"status":"PASS","model":model,"run_group":run_group,"prefix_group":prefix_group,
              "prefix_horizon":100,"recorded_prefix_times":11,"full_run_final_time":full["final_time"],
              "comparison_type":"same-configuration numerical prefix reproduction only; no full-horizon same-configuration rerun claim",
              "repetitions":rows,"source_sha256":digest(__file__),"full_summary_sha256":digest(path/"summary.json")}
    output.mkdir(parents=True,exist_ok=True)
    (output/(model+"_prefix_audit.json")).write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"model":model,"prefix_audit":"PASS","all_prefix_arrays_bitwise_equal":
                      all(v["bitwise_equal"] for row in rows for v in row["checks"].values())}),flush=True)
    return result


def audit_width_comparison(directory, output, *, small_analysis="analysis_generalization_check_001",
                           large_analysis="validation4096_001"):
    """Check the width table from saved outputs at the exact time intersection."""
    directory = Path(directory).resolve()
    directory.relative_to(BASE.resolve())
    report = json.loads((directory/"summary.json").read_text())
    archives = {}
    for width,name,run_group in ((2048,small_analysis,"main"),(4096,large_analysis,"main4096")):
        path = group_path(name)
        summary = json.loads((path/"summary.json").read_text())
        assert summary["width"] == width and summary["run_group"] == run_group
        assert report["provenance"][str(width)] == digest(path/"sample_predictions.npz")
        with np.load(path/"sample_predictions.npz",allow_pickle=False) as a:
            archives[width] = {key:a[key].copy() for key in a.files}
        a = archives[width]
        assert a["network"].shape == a["closure"].shape == (3,len(a["times"]),1000)
        assert len(a["times"]) == len(np.unique(a["times"]))
    for key in ("official_train_ids","labels"):
        np.testing.assert_array_equal(archives[2048][key],archives[4096][key])
    assert len(np.unique(archives[2048]["official_train_ids"])) == 1000
    times = sorted(set(archives[2048]["times"]).intersection(archives[4096]["times"]))
    np.testing.assert_array_equal([r["time"] for r in report["trajectory"]],times)
    assert report["common_final_time"] == times[-1] and report["validation_count"] == 1000
    largest_error = 0.
    def check(actual,expected):
        nonlocal largest_error
        for key,value in expected.items():
            if value is None:
                assert actual[key] is None
            else:
                largest_error = max(largest_error,float(abs(actual[key]-value)))
                np.testing.assert_allclose(actual[key],value,atol=2e-12,rtol=2e-12)
    for t,row in zip(times,report["trajectory"]):
        for width,a in archives.items():
            i = int(np.flatnonzero(a["times"]==t)[0])
            networks = np.asarray(a["network"][:,i],dtype=np.float64)
            closures = np.asarray(a["closure"][:,i],dtype=np.float64)
            reference = sum(networks)/3
            expected = [independent_metrics(p,reference) for p in closures]
            actual = row["widths"][str(width)]
            assert len(actual["individual_closures"]) == 3
            for target,value in zip(actual["individual_closures"],expected):
                check(target,value)
            check(actual["mean_closure_vs_mean_network"],independent_metrics(sum(closures)/3,reference))
            check(actual,{"mean_individual_rms":sum(r["rms"] for r in expected)/3,
                          "mean_individual_relative_rms":sum(r["relative_rms"] for r in expected)/3})
            pairs = [independent_metrics(networks[j],networks[k])["rms"] for j,k in ((0,1),(0,2),(1,2))]
            np.testing.assert_allclose(actual["network_pairwise_rms"],pairs,atol=2e-12,rtol=2e-12)
            for sign in (1,-1):
                mask = a["labels"]==sign
                assert int(mask.sum()) == 500
                for target,pred in zip(actual["within_class"][str(sign)],closures):
                    check(target,independent_metrics(pred[mask],reference[mask]))
    assert report["final"] == report["trajectory"][-1]
    first = report["final"]["widths"]["2048"]["mean_individual_rms"]
    second = report["final"]["widths"]["4096"]["mean_individual_rms"]
    check(report,{"relative_reduction_mean_individual_rms":1-second/first})
    assert report["source_sha256"] == digest(Path(__file__).with_name("WIDTH_COMPARE.py"))
    result = {"status":"PASS","common_final_time":times[-1],"shared_time_count":len(times),
              "validation_count":1000,"same_ids_and_labels":True,"each_width_uses_own_network_mean":True,
              "maximum_scalar_metric_difference":largest_error,
              "relative_reduction_mean_individual_rms":report["relative_reduction_mean_individual_rms"],
              "analysis_summary_sha256":digest(directory/"summary.json"),"source_sha256":digest(__file__),
              "scope":"Descriptive finite-width comparison at fixed p=1, not a convergence result"}
    output.mkdir(parents=True,exist_ok=True)
    (output/"width_comparison_audit.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result),flush=True)
    return result


def audit_pca_analysis(directory, output):
    """Independently check PCA scientific metrics and all pointwise exports."""
    directory = Path(directory).resolve()
    directory.relative_to(BASE.resolve())
    report = json.loads((directory/"summary.json").read_text())
    for field,name in (("analysis_source_sha256","PCA_ANALYZE.py"),("metric_source_sha256","VALIDATION_ANALYSIS.py")):
        archived = directory/"source"/name
        assert report[field] == digest(archived if archived.exists() else Path(__file__).with_name(name))
    seeds = (1729,2718,3141)
    runs, datasets = {}, {}
    for representation,group_name,data_name in (("original","main4096","data_3_5"),("pca","pca4096","data_pca98")):
        dataset_path = group_path(data_name)/"dataset.npz"
        dataset_hash = digest(dataset_path)
        with np.load(dataset_path,allow_pickle=False) as data:
            datasets[representation] = {k:data[k].copy() for k in ("train_y","val_y","val_ids","test_y")}
        runs[representation] = {}
        for model in ("network","closure"):
            records = []
            for seed in seeds:
                path = group_path(group_name)/f"{model}_{seed}"
                summary = json.loads((path/"summary.json").read_text())
                config = summary["configuration"]
                assert config["model"]==model and config["seed"]==seed and config["width"]==4096
                assert summary["final_time"]==600 and summary["data"]["metadata"]["dataset_sha256"]==dataset_hash
                source = report["run_provenance"][f"{representation}_{model}_{seed}"]
                assert source["summary_sha256"]==digest(path/"summary.json")
                assert source["observations_sha256"]==digest(path/"observations.npz")
                with np.load(path/"observations.npz",allow_pickle=False) as a:
                    record = {k:a[k].copy() for k in ("times","train_predictions","val_predictions","train_y","val_y",
                                                     "test_y","test_predictions","test_final_predictions")}
                np.testing.assert_array_equal(record["times"],np.arange(0,601,10))
                assert record["val_predictions"].shape==(61,1000)
                for key in ("train_y","val_y","test_y"):
                    np.testing.assert_array_equal(record[key],datasets[representation][key])
                residual = record["train_predictions"].astype(np.float64)-record["train_y"]
                record["loss"] = np.einsum("ij,ij->i",residual,residual)/residual.shape[1]
                record["summary"] = summary
                records.append(record)
            runs[representation][model] = records
    for key in datasets["original"]:
        np.testing.assert_array_equal(datasets["original"][key],datasets["pca"][key])
    labels,ids = datasets["original"]["val_y"],datasets["original"]["val_ids"]
    assert len(np.unique(ids))==len(labels)==1000
    largest_error,metric_count = 0.,0
    def check(actual,expected):
        nonlocal largest_error,metric_count
        for key,value in expected.items():
            if isinstance(value,dict):
                check(actual[key],value)
            elif value is None:
                assert actual[key] is None
            else:
                metric_count += 1
                largest_error = max(largest_error,float(abs(actual[key]-value)))
                np.testing.assert_allclose(actual[key],value,atol=2e-12,rtol=2e-12)
    def prediction_metrics(pred,ref):
        return {**independent_metrics(pred,ref),"within_class":{
            str(digit):independent_metrics(pred[labels==sign],ref[labels==sign])
            for digit,sign in ((3,1),(5,-1))}}
    expected_exports = {"official_train_ids":ids,"labels":labels}
    csv_names = ["official_train_id","label"]
    csv_columns = [ids,labels]
    for representation in ("original","pca"):
        for model in ("network","closure"):
            rows = report["main"][representation][model]
            assert len(rows)==3
            for row,seed,run in zip(rows,seeds,runs[representation][model]):
                summary = run["summary"]
                final = run["val_predictions"][-1].astype(np.float64)
                assert row["seed"]==seed and row["final_time"]==600 and row["selected_time"]==summary["selected_time"]
                check(row,{"final_training_mse":run["loss"][-1],"final_validation_mse":np.mean((final-labels)**2),
                           "final_validation_accuracy":np.mean((final>=0)==(labels>=0)),
                           "selected_test_accuracy":np.mean((run["test_predictions"]>=0)==(run["test_y"]>=0)),
                           "final_test_accuracy":np.mean((run["test_final_predictions"]>=0)==(run["test_y"]>=0)),
                           "integration_seconds":summary["integration_seconds"],"training_wall_seconds":summary["training_wall_seconds"],
                           "peak_allocated_MiB":summary["peak_allocated_bytes"]/2**20,
                           "moving_state_MiB":summary["moving_state_bytes"]/2**20,
                           "retained_model_MiB":summary["retained_model_bytes"]/2**20})
                key = f"{representation}_{model}_{seed}_T600"
                expected_exports[key] = final
                csv_names.append(key);csv_columns.append(final)
    definitions = {
        "original_closure_vs_original_network":("original","closure","original"),
        "pca_closure_vs_pca_network":("pca","closure","pca"),
        "pca_closure_vs_original_network":("pca","closure","original"),
        "pca_network_vs_original_network":("pca","network","original")}
    selections = {}
    for name,(candidate_rep,candidate_model,reference_rep) in definitions.items():
        actual = report["comparisons"][name]
        candidates = runs[candidate_rep][candidate_model]
        references = runs[reference_rep]["network"]
        reference_outputs = [r["val_predictions"][-1].astype(np.float64) for r in references]
        reference = sum(reference_outputs)/3
        target = sum(r["loss"][-1] for r in references)/3
        assert actual["reference_time"]==600 and "not ensemble loss" in actual["target_definition"]
        check(actual,{"target_training_mse":target})
        finals,chosen_values,times,availability = [],[],[],[]
        same_rms,matched_rms = [],[]
        assert len(actual["rows"])==3 and len(actual["all_individual_pairs"])==9
        for row,seed,run in zip(actual["rows"],seeds,candidates):
            index = int(np.argmin(np.abs(run["loss"]-target)))
            available = bool(min(run["loss"])<=target<=max(run["loss"]))
            final = run["val_predictions"][-1].astype(np.float64)
            chosen = run["val_predictions"][index].astype(np.float64)
            assert row["seed"]==seed and row["selected_time"]==run["times"][index]
            assert row["target_in_saved_loss_range"]==available
            check(row,{"selected_training_mse":run["loss"][index],"relative_loss_mismatch":run["loss"][index]/target-1})
            expected_same = prediction_metrics(final,reference)
            check(row["same_time"],expected_same);same_rms.append(expected_same["rms"])
            if available:
                expected_matched = prediction_metrics(chosen,reference)
                check(row["matched_loss"],expected_matched);matched_rms.append(expected_matched["rms"])
            else:
                assert row["matched_loss"] is None
            for ref_seed,ref in zip(seeds,reference_outputs):
                pair = next(p for p in actual["all_individual_pairs"] if p["candidate_seed"]==seed and p["reference_seed"]==ref_seed)
                check(pair["same_time"],prediction_metrics(final,ref))
                if available:check(pair["matched_loss"],prediction_metrics(chosen,ref))
                else:assert pair["matched_loss"] is None
            finals.append(final);chosen_values.append(chosen);times.append(float(run["times"][index]));availability.append(available)
            csv_names.append(f"{name}_{seed}_selected_by_train_loss");csv_columns.append(chosen)
        check(actual,{"mean_same_time_rms":sum(same_rms)/3,
                      "mean_matched_loss_rms":sum(matched_rms)/3 if all(availability) else None})
        expected_pairs = [independent_metrics(reference_outputs[i],reference_outputs[j])["rms"] for i,j in ((0,1),(0,2),(1,2))]
        np.testing.assert_allclose(actual["reference_network_pairwise_rms"],expected_pairs,atol=2e-12,rtol=2e-12)
        expected_exports.update({name+"_reference":reference,name+"_same_time":np.asarray(finals),
                                 name+"_selected":np.asarray(chosen_values),name+"_selected_times":np.asarray(times)})
        selections[name] = {"times":times,"target_in_saved_loss_range":availability,
                            "mean_same_time_rms":sum(same_rms)/3,
                            "mean_matched_loss_rms":sum(matched_rms)/3 if all(availability) else None}
    common_check = None
    if "common_training_loss" in report:
        common = report["common_training_loss"]
        target = max(r["loss"][-1] for representation in runs.values() for group in representation.values() for r in group)
        check(common,{"target_training_mse":target})
        assert "all twelve" in common["target_definition"]
        chosen,choices = {},{}
        for representation in ("original","pca"):
            chosen[representation],choices[representation] = {},{}
            for model in ("network","closure"):
                values,times = [],[]
                rows = common["choices"][representation][model]
                assert len(rows)==3
                for row,seed,run in zip(rows,seeds,runs[representation][model]):
                    assert min(run["loss"])<=target<=max(run["loss"])
                    index = int(np.argmin(np.abs(run["loss"]-target)))
                    assert row["seed"]==seed and row["time"]==run["times"][index]
                    check(row,{"training_mse":run["loss"][index],"relative_loss_mismatch":run["loss"][index]/target-1})
                    prediction = run["val_predictions"][index].astype(np.float64)
                    check(row,{"validation_accuracy":np.mean((prediction>=0)==(labels>=0)),
                               "validation_mse":np.mean((prediction-labels)**2)})
                    values.append(prediction);times.append(float(run["times"][index]))
                chosen[representation][model] = values
                choices[representation][model] = times
                key = f"common_loss_{representation}_{model}"
                expected_exports[key] = np.asarray(values)
                expected_exports[key+"_times"] = np.asarray(times)
                for seed,value in zip(seeds,values):
                    csv_names.append(f"{key}_{seed}");csv_columns.append(value)
        common_results = {}
        for name,(candidate_rep,candidate_model,reference_rep) in definitions.items():
            actual = common["comparisons"][name]
            values = chosen[candidate_rep][candidate_model]
            references = chosen[reference_rep]["network"]
            reference = sum(references)/3
            assert len(actual["individual"])==3 and len(actual["all_individual_pairs"])==9
            rms = []
            for row,seed,value in zip(actual["individual"],seeds,values):
                expected = prediction_metrics(value,reference)
                check(row,expected);rms.append(expected["rms"])
                for ref_seed,ref in zip(seeds,references):
                    pair = next(p for p in actual["all_individual_pairs"] if p["candidate_seed"]==seed and p["reference_seed"]==ref_seed)
                    check(pair,prediction_metrics(value,ref))
            check(actual,{"mean_individual_rms":sum(rms)/3})
            common_results[name] = sum(rms)/3
        common_check = {"target_training_mse":float(target),"all_twelve_selected_from_training_only":True,
                        "choices":choices,"mean_individual_rms":common_results}
    with np.load(directory/"sample_predictions.npz",allow_pickle=False) as exported:
        for key,value in expected_exports.items():
            np.testing.assert_array_equal(exported[key],value)
    csv_path = directory/"validation_samples.csv"
    with csv_path.open() as handle:
        assert handle.readline().strip()==",".join(csv_names)
    np.testing.assert_array_equal(np.loadtxt(csv_path,delimiter=",",skiprows=1),np.column_stack(csv_columns))
    result = {"status":"PASS","validation_count":1000,"comparison_count":4,"seed_pairs_per_comparison":9,
              "verified_scalar_metrics":metric_count,"maximum_scalar_metric_difference":largest_error,
              "same_ids_labels_and_data_hashes":True,"all_pointwise_NPZ_CSV_exports_exact":True,
              "matched_loss_selected_from_training_only":True,"out_of_range_targets_not_extrapolated":True,
              "comparisons":selections,"source_sha256":digest(__file__),
              "common_training_loss":common_check,
              "analysis_summary_sha256":digest(directory/"summary.json"),
              "scope":"Scientific metrics and exports only; benchmark table checked separately"}
    output.mkdir(parents=True,exist_ok=True)
    (output/"primary_analysis_audit.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result),flush=True)
    return result


def replay(directory, output):
    directory = Path(directory).resolve()
    directory.relative_to(BASE.resolve())
    config = json.loads((directory/"config.json").read_text())
    summary = json.loads((directory/"summary.json").read_text())
    data, provenance = independent_data(config,summary)
    working_dtype = np.dtype(config["dtype"])
    # Preserve the actual run's rounded inputs; only replay arithmetic changes.
    for part in ("train","val","test"):
        data[part+"_u"] = data[part+"_u"].astype(working_dtype).astype(np.float64)
    with np.load(directory/"observations.npz",allow_pickle=False) as archive:
        observations = {key:archive[key].copy() for key in archive.files}
    for part in ("train","val","test"):
        np.testing.assert_array_equal(observations[part+"_y"],data[part+"_y"])
    selected_index = int(np.flatnonzero(observations["times"] == summary["selected_time"])[0])
    val_mse = np.mean((observations["val_predictions"]-data["val_y"])**2,axis=1)
    eligible = np.ones(len(val_mse),dtype=bool)
    if config["task"] == "mnist":
        times = observations["times"]
        eligible = np.isin(times,[0,10,20,50,100,150,200]) | ((times>=300)&(np.abs(times/100-np.round(times/100))<1e-8))
    # Same strict improvement criterion gives the first eligible minimizer.
    eligible_indices = np.flatnonzero(eligible)
    assert selected_index == int(eligible_indices[np.argmin(val_mse[eligible])])
    final_index = len(observations["times"])-1
    assert observations["times"][final_index] == summary["final_time"]
    tolerance = 8e-6 if config["dtype"] == "float32" else 2e-11
    report = {"run":str(directory), "model":config["model"], "dtype_saved":config["dtype"],
              "replay_arithmetic":"NumPy float64; no engine imports", "data":provenance,
              "selected_time":summary["selected_time"], "first_eligible_validation_minimizer_confirmed":True,
              "source_sha256":digest(__file__), "checks":{}, "recomputed_metrics":{},
              "input_hashes":{name:digest(directory/name) for name in
                              ("config.json","summary.json","observations.npz","best_state.npz","final_state.npz")}}
    predictions = {}
    panel = observations["panel_u"].astype(working_dtype).astype(np.float64)
    for which, index in (("best",selected_index), ("final",final_index)):
        with np.load(directory/(which+"_state.npz"),allow_pickle=False) as archive:
            saved = {key:np.asarray(archive[key],dtype=np.float64) for key in archive.files}
        for part in ("train","val","test"):
            actual = predict(saved,data[part+"_u"],config["model"])
            key = which+"_"+part
            predictions[key] = actual
            expected = (observations["test_predictions" if which == "best" else "test_final_predictions"]
                        if part == "test" else observations[part+"_predictions"][index])
            report["checks"][key+"_prediction"] = difference(actual,expected,tolerance=tolerance)
            computed = metrics(actual,data[part+"_y"])
            report["recomputed_metrics"][key] = computed
            expected_metrics = (summary["test"]["selected" if which == "best" else "terminal"]
                                if part == "test" else summary["observations"][index]["train" if part=="train" else "validation"])
            report["checks"][key+"_mse"] = difference(np.array(computed["mse"]),np.array(expected_metrics["mse"]),
                                                        tolerance=max(tolerance,2e-11))
            # Classification may be unstable exactly near zero; record flips
            # explicitly instead of imposing an arbitrary margin convention.
            report["checks"][key+"_prediction"]["sign_disagreements"] = int(np.count_nonzero((actual>=0)!=(expected>=0)))
        h1,h2,_ = fields(saved,panel,config["model"])
        h10,h20,_ = fields(saved,panel,config["model"],initial=True)
        p1,p2 = ((saved["p1"],saved["p2"]) if config["model"]=="closure"
                 else (np.full(len(h1),1/len(h1)),np.full(len(h2),1/len(h2))))
        for number,h,h0,p in ((1,h1,h10,p1),(2,h2,h20,p2)):
            gram = h.T @ (p[:,None]*h)
            motion = np.sqrt(np.mean(p @ ((h-h0)**2)))
            report["checks"][f"{which}_gram{number}"] = difference(gram,observations[f"gram{number}"][index],tolerance=tolerance)
            report["checks"][f"{which}_motion{number}"] = difference(
                np.asarray(motion),np.asarray(summary["observations"][index][f"rms_motion{number}"]),tolerance=tolerance)
    report["status"] = "PASS"
    output.mkdir(parents=True,exist_ok=True)
    name = "__".join(directory.relative_to(BASE).parts)
    np.savez_compressed(output/(name+"_predictions.npz"),**predictions)
    (output/(name+".json")).write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    print(json.dumps({"run":str(directory),"status":"PASS",
                      "max_prediction_error":max(v["max_absolute"] for k,v in report["checks"].items() if k.endswith("prediction")),
                      "sign_disagreements":sum(v.get("sign_disagreements",0) for v in report["checks"].values())}),flush=True)
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("runs",nargs="*",type=Path)
    parser.add_argument("--audit-dataset",type=Path)
    parser.add_argument("--audit-analysis",type=Path)
    parser.add_argument("--audit-control",choices=("network","closure"))
    parser.add_argument("--audit-halfstep-gate",action="store_true")
    parser.add_argument("--audit-reproduction",choices=("network","closure"))
    parser.add_argument("--audit-prefix",choices=("network","closure"))
    parser.add_argument("--audit-width-comparison",type=Path)
    parser.add_argument("--audit-pca-analysis",type=Path)
    parser.add_argument("--run-group",default="main")
    parser.add_argument("--control-group")
    parser.add_argument("--reproduction-group",default="reproduction")
    parser.add_argument("--prefix-group",default="speed4096")
    parser.add_argument("--analysis-source",type=Path)
    parser.add_argument("--small-analysis",default="analysis_generalization_check_001")
    parser.add_argument("--large-analysis",default="validation4096_001")
    parser.add_argument("--output",type=Path,default=BASE/"replaychecks")
    args = parser.parse_args()
    if not args.runs and not any((args.audit_dataset,args.audit_analysis,args.audit_control,args.audit_halfstep_gate,args.audit_reproduction,args.audit_prefix,args.audit_width_comparison,args.audit_pca_analysis)):
        parser.error("provide completed run paths or an --audit-* option")
    start = time.perf_counter()
    rows = [replay(path,args.output) for path in args.runs]
    if args.audit_dataset is not None:
        audit_dataset(args.audit_dataset,args.output)
    if args.audit_analysis is not None:
        audit_analysis(args.audit_analysis,args.output,run_group=args.run_group,analysis_source=args.analysis_source)
    if args.audit_control is not None:
        audit_control(args.audit_control,args.output,run_group=args.run_group,control_group=args.control_group)
    if args.audit_halfstep_gate:
        audit_halfstep_gate(args.output,run_group=args.run_group,control_group=args.control_group or "pca_controls")
    if args.audit_reproduction is not None:
        audit_reproduction(args.audit_reproduction,args.output,run_group=args.run_group,reproduction_group=args.reproduction_group)
    if args.audit_prefix is not None:
        audit_prefix(args.audit_prefix,args.output,run_group=args.run_group,prefix_group=args.prefix_group)
    if args.audit_width_comparison is not None:
        audit_width_comparison(args.audit_width_comparison,args.output,small_analysis=args.small_analysis,
                               large_analysis=args.large_analysis)
    if args.audit_pca_analysis is not None:
        audit_pca_analysis(args.audit_pca_analysis,args.output)
    summary = {"runs":[r["run"] for r in rows],"status":"PASS","elapsed_seconds":time.perf_counter()-start,
               "scope":"saved finite weights, predictions, selected-state metrics, hidden Grams and RMS; no trajectory retraining"}
    if rows:
        (args.output/"summary.json").write_text(json.dumps(summary,indent=2)+"\n")


if __name__ == "__main__":
    main()
