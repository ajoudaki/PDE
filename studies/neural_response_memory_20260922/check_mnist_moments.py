"""Independent MNIST audit: raw IDX data, dense/autograd and moment oracles.

This file may reconstruct the learned dense matrix for checking only. It is
not imported by the producer and does not launch any training trajectory.
"""
from __future__ import annotations

import argparse
import contextlib
import csv
import hashlib
import io
import json
from pathlib import Path
import struct
import time

import numpy as np


HERE = Path(__file__).resolve().parent


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def array_sha256(array):
    return hashlib.sha256(np.ascontiguousarray(array).tobytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def close(actual, expected, message, *, atol=2e-12, rtol=2e-12):
    np.testing.assert_allclose(actual, expected, atol=atol, rtol=rtol,
                               err_msg=message)
    return float(np.max(np.abs(np.asarray(actual)-np.asarray(expected))))


def idx(path):
    raw = Path(path).read_bytes()
    magic = struct.unpack(">I", raw[:4])[0]
    require(magic in (2049, 2051), "expected unsigned-byte IDX labels/images")
    ndim = magic & 255
    shape = struct.unpack(">"+"I"*ndim, raw[4:4+4*ndim])
    data = np.frombuffer(raw, dtype=np.uint8, offset=4+4*ndim)
    require(data.size == np.prod(shape), "IDX payload size")
    return data.reshape(shape)


def audit_data(directory):
    provenance = json.loads((directory / "provenance.json").read_text())
    prepared = directory / "prepared.npz"
    require(sha256(prepared) == provenance["prepared_sha256"], "prepared hash")
    require(sha256(HERE / "prepare_mnist_moments.py") == provenance["source_sha256"],
            "data preparation source hash")
    for name, digest in provenance["raw_sha256"].items():
        require(sha256(directory / name) == digest, "raw hash: "+name)
    raw = directory / "raw_cache/MNIST/raw"
    for filename, digest in provenance["resources"]:
        require(hashlib.md5((raw / filename).read_bytes()).hexdigest() == digest,
                "torchvision resource MD5: "+filename)
    tr_images = idx(raw / "train-images-idx3-ubyte")
    tr_digits = idx(raw / "train-labels-idx1-ubyte")
    va_images = idx(raw / "t10k-images-idx3-ubyte")
    va_digits = idx(raw / "t10k-labels-idx1-ubyte")
    require(tr_images.shape == (60000, 28, 28), "raw training image shape")
    require(va_images.shape == (10000, 28, 28), "raw held-out image shape")
    generator = np.random.default_rng(20260924)
    expected_ids = np.concatenate([generator.choice(np.flatnonzero(tr_digits == digit),
                                                    500, replace=False)
                                   for digit in [3, 8]])
    generator.shuffle(expected_ids)
    validation_ids = np.where((va_digits == 3) | (va_digits == 8))[0]
    with np.load(prepared, allow_pickle=False) as data:
        require(np.array_equal(data["train_ids"], expected_ids), "seed-selected indices")
        require(np.unique(data["train_ids"]).size == 1000, "no repeated training index")
        require(np.array_equal(data["validation_ids"], validation_ids), "complete test subset")
        errors, hashes = {}, {}
        for split, images, digits, indices in [
                ("train", tr_images, tr_digits, expected_ids),
                ("validation", va_images, va_digits, validation_ids)]:
            pixels = images[indices].reshape(len(indices), 784).astype(np.float64)
            expected = pixels / np.sqrt((pixels*pixels).sum(axis=1))[:, None]
            errors[split] = close(data[split+"_inputs"], expected, "raw pixel normalization",
                                  atol=0, rtol=0)
            require(np.array_equal(data[split+"_digits"], digits[indices]), "digit identity")
            require(np.array_equal(data[split+"_labels"], 2*(digits[indices] == 8)-1),
                    "label signs")
            close((data[split+"_inputs"]**2).sum(axis=1), np.ones(len(indices)),
                  "unit Euclidean input norm")
        for name in data.files:
            hashes[name] = array_sha256(data[name])
        counts = {s: {str(d): int(np.sum(data[s+"_digits"] == d)) for d in (3, 8)}
                  for s in ("train", "validation")}
    # Train/test integer indices live in separate official arrays. Their numeric
    # values may overlap; such overlap is not reuse of a sample.
    train_pixel_hashes = {hashlib.sha256(a.tobytes()).digest() for a in tr_images[expected_ids]}
    exact_duplicates = sum(hashlib.sha256(a.tobytes()).digest() in train_pixel_hashes
                           for a in va_images[validation_ids])
    return dict(status="PASS", prepared_sha256=sha256(prepared), array_sha256=hashes,
                counts=counts, normalization_max_abs=errors,
                exact_pixel_duplicates_across_selected_splits=exact_duplicates,
                source_sha256=provenance["source_sha256"])


def audit_moments():
    import torch
    from orthogonal_moment_engine import OrthogonalMomentEngine

    torch.set_num_threads(1)
    rng = np.random.default_rng(9222026)
    inputs = rng.normal(size=(5, 4))
    inputs /= np.linalg.norm(inputs, axis=1)[:, None]
    labels = np.array([-1., 1., -1., 1., 1.])
    results = {}
    for order in [1, 2, 3]:
        engine = OrthogonalMomentEngine(4, 7, order, inputs, labels, seed=20260924)
        state = engine.initial_state()
        initial_rng = np.random.default_rng(20260924)
        close(state.w.numpy(), initial_rng.standard_normal((7, 4)), "initial W1", atol=0, rtol=0)
        close(engine.W0.numpy(), initial_rng.standard_normal((7, 7))/np.sqrt(7),
              "initial W2", atol=0, rtol=0)
        close(state.c.numpy(), initial_rng.standard_normal(7)/7, "initial W3", atol=0, rtol=0)
        order_errors = {}
        for kind in ["initial", "noninitial"]:
            if kind == "noninitial":
                # Reachable short history followed by an independent perturbation
                # tests identities off the special zero-history initialization.
                for _ in range(12):
                    h = 0.03
                    k1 = engine.rhs(state)
                    k2 = engine.rhs(state.add_scaled(k1, h))
                    state = state.add_scaled(k1, h/2).add_scaled(k2, h/2)
                for name in ["w", "c", "A", "B"]:
                    value = getattr(state, name)
                    value += torch.tensor(rng.normal(size=value.shape)*0.02)
            n, m = engine.n, engine.M
            A, B = state.A.numpy(), state.B.numpy()
            length = 1+float(state.s)
            weights = 2*np.arange(order)+1
            delta = sum(weights[k]*(A[k] @ B[k].T) for k in range(order))*(-2/(m*n*length))
            W = engine.W0.numpy()+delta
            h1 = np.tanh(state.w.numpy() @ inputs.T)
            h2 = np.tanh(W @ h1)
            prediction = state.c.numpy() @ h2/n
            residual = prediction-labels
            rho = float(np.sqrt(np.mean(residual**2)))
            d2 = state.c.numpy()[:, None]*(1-h2*h2)
            d1 = (W.T @ d2)*(1-h1*h1)
            velocity = engine.rhs(state)
            err = {}
            err["predictions"] = close(engine.predict(state, inputs).numpy(), prediction,
                                       "direct dense prediction")
            probe = rng.normal(size=(n, 3))
            err["forward_action"] = close(engine.apply_hidden(state, torch.tensor(probe)).numpy(),
                                          W @ probe, "noninitial forward matrix action")
            err["transpose_action"] = close(engine.apply_hidden(state, torch.tensor(probe),
                                                               transpose=True).numpy(),
                                            W.T @ probe, "noninitial transpose matrix action")
            err["w_rhs"] = close(velocity.w.numpy(), -2/m*(d1*residual) @ inputs,
                                  "canonical first-weight velocity")
            err["c_rhs"] = close(velocity.c.numpy(), -2/m*h2 @ residual,
                                  "canonical readout velocity")
            for name, source in [("A", d2*residual), ("B", rho*h1)]:
                moment = getattr(state, name).numpy()
                expected = np.empty_like(moment)
                for k in range(order):
                    lower = sum((2*j+1)*moment[j] for j in range(k))
                    expected[k] = source-rho/length*(k*moment[k]+lower)
                err[name+"_rhs"] = close(getattr(velocity, name).numpy(), expected,
                                          "noninitial Legendre moment dynamics")
            # Autograd is independent of the hand-coded chain rule and verifies
            # unhalved MSE, output 1/n, and physical mobilities (n,1,n).
            tw = state.w.detach().clone().requires_grad_()
            tW = torch.tensor(W, requires_grad=True)
            tc = state.c.detach().clone().requires_grad_()
            th1 = torch.tanh(tw @ torch.tensor(inputs).T)
            th2 = torch.tanh(tW @ th1)
            loss = ((tc @ th2/n-torch.tensor(labels))**2).mean()
            gw, gW, gc = torch.autograd.grad(loss, (tw, tW, tc))
            err["autograd_w"] = close(velocity.w.numpy(), -n*gw.detach().numpy(), "autograd W1")
            err["autograd_c"] = close(velocity.c.numpy(), -n*gc.detach().numpy(), "autograd W3")
            dense_middle_rhs = -gW.detach().numpy()
            dA, dB = velocity.A.numpy(), velocity.B.numpy()
            delta_dot = sum(weights[k]*(dA[k]@B[k].T+A[k]@dB[k].T) for k in range(order))
            delta_dot = -2/(m*n*length)*delta_dot-delta*float(velocity.s)/length
            h_projection = (weights[:, None, None]*B).sum(axis=0)/length
            u_projection = (weights[:, None, None]*A).sum(axis=0)/length
            defect = 2/(m*n)*(d2*residual-rho*u_projection) @ (h1-h_projection).T
            err["defect_identity"] = close(delta_dot-dense_middle_rhs, defect,
                                            "physical defect at noninitial state")
            left, right = engine.derivative_factors(state, velocity)
            err["matrix_derivative_factors"] = close((left@right.T).numpy(), delta_dot,
                                                       "learned matrix derivative")
            if kind == "initial":
                err["initial_middle_velocity"] = close(delta_dot, dense_middle_rhs,
                                                        "initial canonical middle velocity")
            # Central difference checks the reconstruction derivative independently.
            epsilon = 1e-5
            def reconstruction(st):
                a, b = st.A.numpy(), st.B.numpy()
                return -2/(m*n*(1+float(st.s)))*sum(weights[k]*(a[k]@b[k].T)
                                                   for k in range(order))
            numeric = (reconstruction(state.add_scaled(velocity, epsilon))-
                       reconstruction(state.add_scaled(velocity, -epsilon)))/(2*epsilon)
            err["reconstruction_finite_difference"] = close(numeric, delta_dot,
                                                           "differentiated reconstruction", atol=2e-10)
            order_errors[kind] = err
        # An integral oracle checks the transport coefficient identity itself,
        # independently of the polynomial recurrence used in the implementation.
        nodes, quadrature = np.polynomial.legendre.leggauss(48)
        def integral(length):
            tau = length*(nodes+1)/2
            history = np.exp(0.3*tau)+tau**3
            return np.array([length/2*np.sum(quadrature*history*
                                  np.polynomial.legendre.Legendre.basis(k)(nodes))
                             for k in range(order)])
        length, rho, eps = 1.7, 0.61, 1e-5
        moments = integral(length)
        expected = (integral(length+eps*rho)-integral(length-eps*rho))/(2*eps)
        # Scalar arguments explicitly float64; float32 literals would test dtype
        # conversion, not the exact transport identity.
        transport = engine.transport_moments(torch.tensor(moments[:, None, None]),
                                             torch.tensor([[rho*(np.exp(0.3*length)+length**3)]], dtype=torch.float64),
                                             torch.tensor(rho, dtype=torch.float64),
                                             torch.tensor(length, dtype=torch.float64))
        order_errors["integral_transport"] = close(transport.numpy().reshape(-1), expected,
                                                   "moving interval integral derivative", atol=2e-9)
        results[str(order)] = order_errors
    return dict(status="PASS", torch_version=torch.__version__, orders=results)


def audit_runner(scratch):
    import torch
    from mnist_moment_run import (DenseEngine, DenseState, heun_trial,
                                  locate_loss_crossing, parser, run)

    rng = np.random.default_rng(4191)
    inputs = rng.normal(size=(6, 4))/2
    labels = np.array([-1., 1., -1., 1., -1., 1.])
    engine = DenseEngine(4, 7, inputs, labels, seed=20260924)
    state = engine.initial_state()
    for name in state.names():
        getattr(state, name).add_(torch.tensor(rng.normal(size=getattr(state, name).shape)*.1))
    variables = [v.detach().clone().requires_grad_() for v in state.tensors()]
    w, W, c = variables
    prediction = c @ torch.tanh(W @ torch.tanh(w @ torch.tensor(inputs).T))/7
    loss = ((prediction-torch.tensor(labels))**2).mean()
    gradients = torch.autograd.grad(loss, variables)
    velocity = engine.rhs(state)
    errors = {name: close(v.numpy(), -mob*g.detach().numpy(), "dense autograd "+name)
              for name, v, mob, g in zip(state.names(), velocity.tensors(), [7, 1, 7], gradients)}

    class NonlinearDecay:
        inputs = torch.ones((1, 1), dtype=torch.float64)
        labels = torch.zeros(1, dtype=torch.float64)

        @staticmethod
        def rhs(value):
            return DenseState(*(-x*x for x in value.tensors()))

        @staticmethod
        def predict(value, inputs):
            return value.w.reshape(1)

    scalar_state = DenseState(*(torch.tensor(1., dtype=torch.float64) for _ in range(3)))
    step = .3
    first, second, _, candidate = heun_trial(NonlinearDecay(), scalar_state, step)
    fraction, event, event_loss = locate_loss_crossing(
        NonlinearDecay(), scalar_state, first, second, step, .9**2)
    # For y'=-y^2 at y0=1, continuous Heun output is
    # y(theta)=1-h*theta+h^2*(1-h/2)*theta^2.
    aa = step**2*(1-step/2)
    expected_fraction = (step-np.sqrt(step*step-4*aa*.1))/(2*aa)
    errors["nonlinear_crossing_fraction"] = close(fraction, expected_fraction,
                                                   "nonlinear Heun extension root", atol=2e-10)
    errors["nonlinear_crossing_loss"] = close(event_loss, .9**2,
                                               "crossing loss root", atol=2e-10)
    exact_event_time = 1/.9-1
    # The finite-step interpolant is approximate: this positive discrepancy is
    # expected, and is not confused with machine-precision event root solving.
    interpolation_time_error = abs(step*fraction-exact_event_time)

    # End-to-end isolation: change both held-out images and labels radically.
    # The tiny physical-time stop is chosen to avoid operational wall caps.
    scratch.mkdir(parents=True, exist_ok=True)
    isolated = []
    for index in range(2):
        dataset = scratch / f"isolation_data_{index}.npz"
        out = scratch / f"isolation_run_{index}"
        require(not out.exists(), "isolation scratch must be fresh")
        np.savez(dataset, train_inputs=inputs, train_labels=labels,
                 validation_inputs=inputs[:2] if index == 0 else -inputs[:2]*100,
                 validation_labels=np.array([-1., 1.]) if index == 0 else np.array([9e4, -9e4]))
        args = parser().parse_args(["--dataset", str(dataset), "--out", str(out),
                                   "--model", "moment", "--order", "3", "--width", "7",
                                   "--max-time", ".05", "--initial-step", ".025",
                                   "--target-loss", ".000001", "--rtol", ".0002"])
        args.atol = args.rtol/100
        with contextlib.redirect_stdout(io.StringIO()):
            summary = run(args)
        require(summary["status"] == "max_time", "tiny isolation run physical-time stop")
        with np.load(out / "arrays.npz", allow_pickle=False) as archive:
            isolated.append({name: archive[name].copy() for name in
                             ["w", "c", "A", "B", "C", "s", "times", "losses",
                              "accepted_steps", "local_error_ratios", "train_predictions"]})
    for name in isolated[0]:
        require(np.array_equal(isolated[0][name], isolated[1][name]),
                "validation changes altered training "+name)
    return dict(status="PASS", max_abs_errors=errors,
                nonlinear_extension_time_error_at_step_0p3=interpolation_time_error,
                validation_input_and_label_isolation="bitwise identical states and traces")


def independent_prediction(state, inputs, n, order, samples, block=256):
    w, c = state["w"], state["c"]
    if order is None:
        middle = state["W"]
    else:
        A, B = state["A"], state["B"]
        middle = state["W0"].copy()
        length = 1+float(state["s"])
        for k in range(order):
            middle -= 2*(2*k+1)/(samples*n*length)*(A[k] @ B[k].T)
    return np.concatenate([c @ np.tanh(middle @ np.tanh(w @ inputs[j:j+block].T))/n
                           for j in range(0, len(inputs), block)])


def audit_saved_runs(paths, data_path, cached_audits=()):
    dataset = np.load(data_path / "prepared.npz", allow_pickle=False)
    entries, prediction_bank = {}, {}
    cache = {}
    for cached in cached_audits:
        previous = json.loads(cached.read_text())
        require(previous["data"]["prepared_sha256"] == sha256(data_path / "prepared.npz"),
                "cached audit dataset identity")
        cache.update(previous["saved_runs"]["runs"])
    initialization_hashes = set()
    for path in paths:
        summary = json.loads((path / "summary.json").read_text())
        require(sha256(path / "arrays.npz") == summary["arrays_sha256"], "run archive hash")
        require(summary["dataset_sha256"] == sha256(data_path / "prepared.npz"), "run dataset hash")
        for name, digest in summary["source_sha256"].items():
            require(sha256(HERE / name) == digest, "run source frozen: "+name)
        require(summary["seed"] == 20260924, "run seed")
        n, d, m, order = summary["width"], summary["d"], summary["sample_count"], summary["P"]
        require(m == 1000 and d == 784, "primary input dimensions")
        require(summary["dtype"] == "float64", "primary precision")
        require(summary["rtol"] in [2e-4, 5e-5, 1.25e-5], "predeclared tolerances")
        close(summary["atol"], summary["rtol"]/100, "absolute tolerance", atol=1e-20)
        for name, expected in [("maximum_step", 2), ("max_time", 10000),
                               ("max_steps", 30000), ("wall_limit_seconds", 600),
                               ("target_loss", .001)]:
            require(summary[name] == expected, "primary control "+name)
        rng = np.random.default_rng(20260924)
        initial = dict(w=rng.standard_normal((n, d)),
                       W=rng.standard_normal((n, n))/np.sqrt(n), c=rng.standard_normal(n)/n)
        digest = hashlib.sha256()
        for name in ["w", "W", "c"]:
            digest.update(initial[name].tobytes(order="C"))
        require(digest.hexdigest() == summary["initialization_hash"], "run initialization draws")
        initialization_hashes.add(summary["initialization_hash"])
        run_id = path.name
        if run_id in cache:
            previous = cache[run_id]
            require(previous["arrays_sha256"] == summary["arrays_sha256"] and
                    previous["summary_sha256"] == sha256(path / "summary.json"),
                    "cached run unchanged")
            with np.load(path / "arrays.npz", allow_pickle=False) as archive:
                for index, (label, prediction) in enumerate(zip(archive["observation_labels"],
                                                               archive["validation_predictions"])):
                    if str(label).startswith("loss_"):
                        filename = "checkpoint_"+str(label).replace(".", "p")+".npz"
                        require(sha256(path / filename) ==
                                previous["observations"][str(label)]["checkpoint_sha256"],
                                "cached checkpoint unchanged")
                    prediction_bank[(run_id, str(label))] = prediction.copy()
                    if "training_accuracy" not in previous["observations"][str(label)]:
                        train = archive["train_predictions"][index]
                        require(np.min(np.abs(train)) >
                                previous["observations"][str(label)]["train_prediction_max_abs_error"],
                                "cached reconstruction certifies training prediction signs")
                        previous["observations"][str(label)]["training_accuracy"] = float(np.mean(
                            np.where(train >= 0, 1., -1.) == dataset["train_labels"]))
            entries[run_id] = previous
            continue
        result = dict(model=summary["model"], P=order, width=n, rtol=summary["rtol"],
                      status=summary["status"], arrays_sha256=summary["arrays_sha256"],
                      summary_sha256=sha256(path / "summary.json"), observations={})
        with np.load(path / "arrays.npz", allow_pickle=False) as archive:
            for name in ["train_labels", "validation_labels", "train_ids", "validation_ids"]:
                require(np.array_equal(archive[name], dataset[name]), "saved split labels/indices")
            require(np.all(np.diff(archive["times"]) > 0), "strictly increasing accepted times")
            require(len(archive["accepted_steps"]) == summary["accepted"], "accepted step count")
            close(np.diff(archive["times"]), archive["accepted_steps"], "saved accepted steps", atol=2e-11)
            require(np.all(archive["local_error_ratios"] <= 1), "accepted embedded-error bound")
            close(archive["times"][-1], summary["time"], "final time")
            close(archive["losses"][-1], summary["training_mse"], "final loss trace")
            for index, label in enumerate(archive["observation_labels"]):
                label = str(label)
                if label == "initial":
                    checkpoint, checkpoint_order = initial, None
                elif label == "final":
                    checkpoint, checkpoint_order = archive, order
                else:
                    filename = "checkpoint_"+label.replace(".", "p")+".npz"
                    require(filename in summary["checkpoints"], "declared checkpoint")
                    checkpoint = np.load(path / filename, allow_pickle=False)
                    checkpoint_order = order
                    close(checkpoint["physical_time"], archive["observation_times"][index],
                          "checkpoint time")
                if checkpoint_order is not None:
                    require(np.array_equal(checkpoint["W0"], initial["W"]), "retained initialized W0")
                    require(checkpoint["A"].shape == (order, n, m) and
                            checkpoint["B"].shape == (order, n, m), "moment state dimensions")
                    require(float(checkpoint["s"]) >= 0, "nonnegative accumulated activity")
                    close(checkpoint["C"], 1+float(checkpoint["s"]), "C equals interval length", atol=2e-9)
                train = independent_prediction(checkpoint, dataset["train_inputs"], n, checkpoint_order, m)
                validation = independent_prediction(checkpoint, dataset["validation_inputs"], n,
                                                     checkpoint_order, m)
                train_error = close(train, archive["train_predictions"][index],
                                    "independent saved train prediction", atol=3e-11)
                val_error = close(validation, archive["validation_predictions"][index],
                                  "independent saved held-out prediction", atol=3e-11)
                mse = float(np.mean((train-dataset["train_labels"])**2))
                close(mse, archive["observation_training_mse"][index], "recomputed training loss", atol=2e-11)
                if label.startswith("loss_"):
                    close(mse, float(label[5:]), "declared endpoint crossing", atol=2e-9)
                metrics = dict(time=float(archive["observation_times"][index]), training_mse=mse,
                               training_accuracy=float(np.mean(np.where(train >= 0, 1., -1.) ==
                                                               dataset["train_labels"])),
                               validation_mse=float(np.mean((validation-dataset["validation_labels"])**2)),
                               validation_accuracy=float(np.mean(np.where(validation >= 0, 1., -1.) ==
                                                                dataset["validation_labels"])),
                               train_prediction_max_abs_error=train_error,
                               validation_prediction_max_abs_error=val_error)
                if label not in ("initial", "final"):
                    metrics["checkpoint_sha256"] = sha256(path / filename)
                    checkpoint.close()
                result["observations"][label] = metrics
                prediction_bank[(run_id, label)] = validation
        entries[run_id] = result
    require(len(initialization_hashes) == 1, "all compared runs share initialization")
    comparisons, comparison_references = {}, {}
    # Match actual reached loss endpoints by their labels, never nearest loss/time.
    for run_id, item in entries.items():
        if item["P"] is None:
            continue
        references = [(key, value) for key, value in entries.items()
                      if value["P"] is None and value["rtol"] == item["rtol"]]
        if not references:
            require(item["rtol"] == 1.25e-5, "primary closure requires same-tolerance dense")
            references = sorted([(key, value) for key, value in entries.items()
                                 if value["P"] is None], key=lambda pair: pair[1]["rtol"])[:1]
        require(len(references) == 1, "one dense reference for each closure comparison")
        reference_id, reference = references[0]
        comparison_references[run_id] = dict(dense_run=reference_id,
                                             dense_rtol=reference["rtol"],
                                             closure_rtol=item["rtol"],
                                             equal_tolerance=reference["rtol"] == item["rtol"])
        values = {}
        for label in item["observations"].keys() & reference["observations"].keys():
            if label.startswith("loss_"):
                values[label] = float(np.sqrt(np.mean((prediction_bank[(run_id, label)]-
                                                      prediction_bank[(reference_id, label)])**2)))
        comparisons[run_id] = values
    refinements = {}
    for model in [None, 1, 2, 3]:
        matches = sorted([(key, value) for key, value in entries.items() if value["P"] == model],
                         key=lambda pair: pair[1]["rtol"], reverse=True)
        for (coarse_id, coarse), (fine_id, fine) in zip(matches[:-1], matches[1:]):
            values = {}
            for label in coarse["observations"].keys() & fine["observations"].keys():
                if label.startswith("loss_"):
                    values[label] = float(np.sqrt(np.mean((prediction_bank[(coarse_id, label)]-
                                                          prediction_bank[(fine_id, label)])**2)))
            refinements[coarse_id+"__"+fine_id] = values
    primary_entries = [value for value in entries.values() if value["rtol"] in [2e-4, 5e-5]]
    common = set.intersection(*(set(value["observations"]) for value in primary_entries))
    endpoints = [float(label[5:]) for label in common if label.startswith("loss_")]
    dataset.close()
    return dict(status="PASS", initialization_sha256=next(iter(initialization_hashes)), runs=entries,
                closure_dense_validation_rms=comparisons, tolerance_validation_rms=refinements,
                closure_dense_references=comparison_references,
                smallest_joint_endpoint=min(endpoints) if endpoints else None,
                primary_runs_in_joint_endpoint=len(primary_entries))


def audit_analysis(directory, paths, audited):
    """Check analysis formulas/selection independently, without importing it."""
    summary = json.loads((directory / "metrics_summary.json").read_text())
    require(summary["provenance"]["analysis_source_sha256"] ==
            sha256(HERE / "analyze_mnist_moments.py"), "analysis source hash")
    require(summary["primary_level"] == audited["smallest_joint_endpoint"],
            "predeclared primary endpoint selection")
    predictions, metrics = {}, {}
    for path in paths:
        entry = audited["runs"][path.name]
        model = "dense" if entry["P"] is None else "P"+str(entry["P"])
        with np.load(path / "arrays.npz", allow_pickle=False) as archive:
            for label, values in zip(archive["observation_labels"], archive["validation_predictions"]):
                key = (model, entry["rtol"], str(label))
                predictions[key] = values.copy()
                metrics[key] = entry["observations"][str(label)]

    def choices(model, label):
        return sorted(key[1] for key in predictions if key[0] == model and key[2] == label)

    def sensitivity(model, label):
        resolutions = choices(model, label)
        require(len(resolutions) >= 2, "two observed model resolutions")
        return np.linalg.norm(predictions[(model, resolutions[0], label)]-
                              predictions[(model, resolutions[1], label)])/np.sqrt(1984)

    errors = []
    expected_requests = set()
    for row in summary["comparisons"]:
        model = "P"+str(row["order"])
        label = "loss_"+format(row["level"], ".12g")
        dr, cr = choices("dense", label)[0], choices(model, label)[0]
        require(row["dense_rtol"] == dr and row["closure_rtol"] == cr,
                "finest available prediction selection")
        observed = np.linalg.norm(predictions[(model, cr, label)]-
                                  predictions[("dense", dr, label)])/np.sqrt(1984)
        errors.append(close(row["rms_difference"], observed, "reported closure-dense RMS"))
        dd, cd = sensitivity("dense", label), sensitivity(model, label)
        close(row["dense_refinement_rms"], dd, "reported dense sensitivity")
        close(row["closure_refinement_rms"], cd, "reported closure sensitivity")
        close(row["observed_refinement_margin"], dd+cd, "reported empirical margin")
        threshold = min(.005, .1*observed)
        close(row["refinement_gate_threshold"], threshold, "refinement threshold")
        passed = bool(dd <= threshold and cd <= threshold)
        require(row["numerical_gate_passed"] == passed, "reported numerical gate")
        for who, resolution, prefix in [("dense", dr, "dense"), (model, cr, "closure")]:
            close(row[prefix+"_physical_time"], metrics[(who, resolution, label)]["time"],
                  "reported endpoint time")
            close(row[prefix+"_train_mse"], metrics[(who, resolution, label)]["training_mse"],
                  "reported endpoint training MSE")
        if not passed:
            verdict = "inconclusive_numerical_refinement"
        elif observed+dd+cd < .1:
            verdict = "below_0.1_with_observed_refinement_margin"
        elif observed-dd-cd >= .1:
            verdict = "above_or_equal_0.1_with_observed_refinement_margin"
        else:
            verdict = "threshold_unresolved_by_observed_refinement"
        require(row["practical_agreement"] == verdict, "reported practical agreement verdict")
        if all((who, tol, label) in predictions for who in ("dense", model) for tol in (2e-4, 5e-5)):
            base = np.linalg.norm(predictions[(model, 5e-5, label)]-
                                  predictions[("dense", 5e-5, label)])/np.sqrt(1984)
            for who in ("dense", model):
                delta = np.linalg.norm(predictions[(who, 2e-4, label)]-
                                       predictions[(who, 5e-5, label)])/np.sqrt(1984)
                if delta > .005 or delta > .1*base:
                    expected_requests.add(who)
    require({row["model"] for row in summary["refinement_requests"]} == expected_requests,
            "conditional refinement requests over all endpoints")
    comparison_lookup = {(row["level"], row["order"]): row for row in summary["comparisons"]}
    for group in summary["order_comparisons"]:
        for row in group["comparisons"]:
            left = comparison_lookup[(group["level"], row["from_order"])]
            right = comparison_lookup[(group["level"], row["to_order"])]
            improvement = left["rms_difference"]-right["rms_difference"]
            margin = left["observed_refinement_margin"]+right["observed_refinement_margin"]
            close(row["rms_improvement"], improvement, "order comparison difference")
            close(row["observed_refinement_margin"], margin, "order comparison empirical margin")
            if not left["numerical_gate_passed"] or not right["numerical_gate_passed"]:
                verdict = "inconclusive_numerical_refinement"
            elif improvement > margin:
                verdict = "improvement_resolved_by_observed_refinement"
            elif improvement < -margin:
                verdict = "worsening_resolved_by_observed_refinement"
            else:
                verdict = "order_difference_unresolved_by_observed_refinement"
            require(row["verdict"] == verdict, "order trend verdict")
    with (directory / "label_metrics.csv").open() as stream:
        label_rows = list(csv.DictReader(stream))
    require(len(label_rows) == len(metrics), "all label metric observations reported")
    for row in label_rows:
        actual = metrics[(row["model"], float(row["rtol"]), row["label"])]
        for source, target in [("train_mse", "training_mse"),
                               ("train_accuracy", "training_accuracy"),
                               ("validation_label_mse", "validation_mse"),
                               ("validation_accuracy", "validation_accuracy")]:
            close(float(row[source]), actual[target], "reported label metric "+source)
    with np.load(directory / "validation_predictions_and_errors.npz", allow_pickle=False) as individual:
        for row in summary["comparisons"]:
            tag = format(row["level"], "g").replace(".", "p")
            label = "loss_"+format(row["level"], ".12g")
            model = row["model"]
            dp = predictions[("dense", choices("dense", label)[0], label)]
            cp = predictions[(model, choices(model, label)[0], label)]
            close(individual[f"prediction_{model}_loss_{tag}"], cp, "exported closure points", atol=0, rtol=0)
            close(individual[f"prediction_dense_loss_{tag}"], dp, "exported dense points", atol=0, rtol=0)
            close(individual[f"error_{model}_loss_{tag}"], cp-dp, "exported paired errors", atol=0, rtol=0)
    return dict(status="PASS", primary_level=summary["primary_level"],
                comparison_count=len(summary["comparisons"]), label_metric_count=len(label_rows),
                maximum_reported_rms_error=max(errors),
                refinement_requested_models=sorted(expected_requests),
                metrics_summary_sha256=sha256(directory / "metrics_summary.json"),
                analysis_source_sha256=sha256(HERE / "analyze_mnist_moments.py"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--data-only", action="store_true")
    parser.add_argument("--runs", nargs="*", type=Path, default=[])
    parser.add_argument("--cached-audits", nargs="*", type=Path, default=[])
    parser.add_argument("--analysis", type=Path)
    parser.add_argument("--skip-isolation", action="store_true")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    results = dict(data=audit_data(args.data), numpy_version=np.__version__)
    if not args.data_only:
        results["moments"] = audit_moments()
        if not args.skip_isolation:
            results["runner"] = audit_runner(args.output / ("runner_checks_"+str(time.time_ns())))
    if args.runs:
        results["saved_runs"] = audit_saved_runs(args.runs, args.data, args.cached_audits)
    if args.analysis:
        require(bool(args.runs), "analysis check requires explicitly audited runs")
        results["analysis"] = audit_analysis(args.analysis, args.runs, results["saved_runs"])
    results["source_sha256"] = {name: sha256(HERE / name) for name in [
        "check_mnist_moments.py", "MNIST_PROTOCOL.md", "MOMENT_CONSTRUCTION.md",
        "moment_engine.py", "orthogonal_moment_engine.py", "prepare_mnist_moments.py",
        "mnist_moment_run.py", "test_mnist_moment.py"]}
    results["elapsed_seconds"] = time.perf_counter()-started
    (args.output / "audit.json").write_text(json.dumps(results, indent=2)+"\n")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
