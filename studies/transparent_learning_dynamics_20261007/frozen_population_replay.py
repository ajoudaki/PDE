"""Independent Gaussian quadrature of a saved, frozen causal coefficient history.

This diagnostic never closes or updates the population coefficients.  It freezes
C1, D2, Rh, Rdelta and write_deficit from the filtered causal run, samples the
root, eta and xi independently, and evaluates the same local scalar equations.
Fresh means therefore measure self-consistency of those saved coefficients;
this is not a new autonomous solver or a dense-network comparison.

The joint Gaussian factors are computed once before batching.  Current moments,
their changes from initialization, and per-neuron squared feature displacement
are retained per batch.  Optional full C1/C2/D2 histories are retained as two
independent half-population means.  All standard errors are conditional on the
saved coefficients and do not measure source-run uncertainty.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import sys
import time
from typing import Any

import numpy as np

from causal_panel_simulator import _activation, _flat_gram

Array = np.ndarray
STUDY = Path(__file__).resolve().parent
CURRENT_NAMES = ("c1", "c2", "d1", "d2", "f", "motion1", "motion2")


def gaussian_factor(covariance: Array, *, rank_rtol: float = 1e-12,
                    rank_atol: float = 0.) -> tuple[Array, dict[str, Any], Array]:
    """Return F with covariance approximately F F.T, without whitening samples.

    Keep eigenvalues strictly above rank_atol + rank_rtol*lambda_max.  Roundoff
    negative eigenvalues are discarded and reported.  A negative eigenvalue
    larger in magnitude than max(the rank threshold, 64*eps*q*spectral_scale)
    rejects the input instead of silently repairing a materially indefinite
    covariance.  The declared rank approximation is separate from quadrature.
    """
    covariance = np.asarray(covariance, dtype=np.float64)
    if (covariance.ndim != 2 or covariance.shape[0] != covariance.shape[1]
            or covariance.shape[0] == 0 or not np.isfinite(covariance).all()):
        raise ValueError("Covariance must be a nonempty finite square matrix")
    if (not np.isfinite(rank_rtol) or not np.isfinite(rank_atol)
            or rank_rtol < 0 or rank_atol < 0):
        raise ValueError("Rank tolerances must be finite and nonnegative")
    asymmetry = float(np.max(abs(covariance-covariance.T)))
    symmetric = .5*(covariance+covariance.T)
    eigenvalues, eigenvectors = np.linalg.eigh(symmetric)
    scale = float(np.max(abs(eigenvalues)))
    threshold = rank_atol + rank_rtol*max(0., float(eigenvalues[-1]))
    negative_tolerance = max(threshold, 64*np.finfo(float).eps*len(covariance)*scale)
    if asymmetry > max(negative_tolerance, np.finfo(float).tiny):
        raise ValueError(f"Covariance asymmetry {asymmetry} exceeds {negative_tolerance}")
    if eigenvalues[0] < -negative_tolerance:
        raise ValueError(f"Indefinite covariance: minimum eigenvalue {eigenvalues[0]}")
    keep = eigenvalues > threshold
    factor = eigenvectors[:, keep]*np.sqrt(eigenvalues[keep])[None, :]
    error = factor@factor.T-covariance
    diagnostic = dict(dimension=len(covariance), rank=int(keep.sum()),
        rank_rtol=float(rank_rtol), rank_atol=float(rank_atol),
        eigenvalue_threshold=float(threshold), negative_tolerance=float(negative_tolerance),
        minimum_eigenvalue=float(eigenvalues[0]), maximum_eigenvalue=float(eigenvalues[-1]),
        negative_eigenvalue_count=int(np.sum(eigenvalues < 0)),
        negative_eigenvalue_absolute_sum=float(-eigenvalues[eigenvalues < 0].sum()),
        discarded_positive_eigenvalue_sum=float(eigenvalues[(eigenvalues > 0) & ~keep].sum()),
        maximum_asymmetry=asymmetry, maximum_covariance_error=float(np.max(abs(error))),
        covariance_frobenius_error=float(np.linalg.norm(error)))
    return factor, diagnostic, eigenvalues


class FrozenProgram:
    """The full-model local equations with externally fixed coefficient arrays.

    C1,D2,Rh,Rdelta have shape [s,s,p,p]: evaluated time/sample precede driving
    time/sample.  write_deficit has shape [s,m], with only the first m panel rows
    training.  dt is physical time; learning_step is dt*2/m.
    """

    def __init__(self, *, vectors: Array, labels: Array, dt: float, C1: Array,
                 D2: Array, Rh: Array, Rdelta: Array, write_deficit: Array) -> None:
        self.vectors = np.asarray(vectors, dtype=np.float64)
        self.labels = np.asarray(labels, dtype=np.float64)
        if self.labels.ndim != 1 or not len(self.labels) or not np.isfinite(self.labels).all():
            raise ValueError("Labels must be a finite nonempty vector")
        self.m = len(self.labels)
        if (self.vectors.ndim != 2 or self.vectors.shape[0] < self.m
                or self.vectors.shape[1] < 1 or not np.isfinite(self.vectors).all()):
            raise ValueError("Vectors must have finite shape [p,d], p>=m, d>=1")
        if not np.allclose(np.sum(self.vectors**2, axis=1), 1., atol=1e-12, rtol=1e-12):
            raise ValueError("Input vectors must be normalized")
        if not np.isfinite(dt) or dt <= 0:
            raise ValueError("dt must be positive and finite")
        self.p, self.d = self.vectors.shape
        self.dt, self.learning_step = float(dt), float(dt)*2/self.m
        self.write = np.asarray(write_deficit, dtype=np.float64)
        if (self.write.ndim != 2 or self.write.shape[1] != self.m
                or self.write.shape[0] < 1 or not np.isfinite(self.write).all()):
            raise ValueError("write_deficit must have finite shape [s,m]")
        self.s = len(self.write)
        arrays = [np.asarray(x, dtype=np.float64) for x in (C1, D2, Rh, Rdelta)]
        expected = (self.s, self.s, self.p, self.p)
        if any(x.shape != expected or not np.isfinite(x).all() for x in arrays):
            raise ValueError(f"Coefficient arrays must have finite shape {expected}")
        self.C1, self.D2, self.Rh, self.Rdelta = arrays
        self.input_gram = self.vectors@self.vectors.T
        self.forward, self.backward = [], []
        for k in range(self.s):
            up = self.Rh[k, :k, :, :self.m].copy()
            up += self.learning_step*self.C1[k, :k, :, :self.m]*self.write[:k, None, :]
            down = self.Rdelta[k, :k+1, :, :self.m].copy()
            down[:k] += self.learning_step*self.D2[k, :k, :, :self.m]*self.write[:k, None, :]
            self.forward.append(up.transpose(0, 2, 1).reshape(k*self.m, self.p))
            self.backward.append(down.transpose(0, 2, 1).reshape((k+1)*self.m, self.p))
        passive = np.arange(self.m, self.p)
        self.passive_current = self.Rdelta[np.arange(self.s)[:, None],
            np.arange(self.s)[:, None], passive[None, :], passive[None, :]]

    @classmethod
    def from_result(cls, result: dict[str, Any]) -> "FrozenProgram":
        """Adapter for deterministic tests using the filtered simulator output."""
        cfg = result["config"]
        if not all(cfg[name] for name in ("learned_forward_memory",
                                          "learned_backward_memory", "reciprocal_correction")):
            raise ValueError("Only full-model frozen histories are supported")
        return cls(vectors=cfg["input_vectors"], labels=cfg["labels"], dt=cfg["dt"],
            C1=result["C"]["layer1"], D2=result["D"]["layer2"], Rh=result["R"]["h"],
            Rdelta=result["R"]["delta"], write_deficit=result["write_deficit"])

    def evaluate(self, root_z1: Array, eta: Array, xi: Array, *,
                 full_grams: bool = False, return_fields: bool = False) -> dict[str, Any]:
        """Evaluate supplied primitives; root_z1 is the initial [n,p] panel.

        eta and xi have shape [s,n,p].  In stochastic use root_z1 is iid N(0,I_d)
        times vectors.T and is independent of the two supplied Gaussian families.
        Observed means are never fed back into this evaluation.
        """
        root_z1 = np.asarray(root_z1, dtype=np.float64)
        eta, xi = np.asarray(eta, dtype=np.float64), np.asarray(xi, dtype=np.float64)
        if root_z1.ndim != 2 or root_z1.shape[1] != self.p or len(root_z1) < 1:
            raise ValueError("root_z1 must have shape [n,p]")
        n, s, p, m = len(root_z1), self.s, self.p, self.m
        if eta.shape != (s, n, p) or xi.shape != (s, n, p):
            raise ValueError("Primitive histories must have shape [s,n,p]")
        if not all(np.isfinite(x).all() for x in (root_z1, eta, xi)):
            raise ValueError("Primitives must be finite")
        z1, w = root_z1.copy(), np.zeros(n)
        lower_active = np.empty((n, s*m))
        upper_active = np.empty_like(lower_active)
        upper_features = np.empty_like(lower_active)
        moments = {name: np.empty((s, p, p)) for name in ("c1", "c2", "d1", "d2")}
        moments.update({name: np.empty((s, p)) for name in ("f", "motion1", "motion2")})
        history = ({name: np.empty((s, n, p)) for name in ("h1", "h2", "delta2")}
                   if full_grams or return_fields else {})
        if return_fields:
            history.update({name: np.empty((s, n, p)) for name in ("z1", "z2", "b1", "delta1")})
            history["w"] = np.empty((s, n))
        maximum_field = np.zeros(s)
        history_w_error, history_prediction_error = np.zeros(s), np.zeros(s)
        for k in range(s):
            h1, gate1, _ = _activation(z1)
            lower_active[:, k*m:(k+1)*m] = h1[:, :m]
            z2 = eta[k].copy()
            if k:
                z2 += upper_active[:, :k*m]@self.forward[k]
            h2, gate2, _ = _activation(z2)
            upper_features[:, k*m:(k+1)*m] = h2[:, :m]
            d2 = gate2*w[:, None]
            upper_active[:, k*m:(k+1)*m] = d2[:, :m]
            b1 = xi[k]+lower_active[:, :(k+1)*m]@self.backward[k]
            if p > m:
                b1[:, m:] += self.passive_current[k][None, :]*h1[:, m:]
            d1 = gate1*b1
            moments["f"][k] = np.mean(w[:, None]*h2, axis=0)
            reconstructed_w = (self.learning_step*(upper_features[:, :k*m]@self.write[:k].reshape(-1))
                               if k else np.zeros(n))
            history_w_error[k] = np.max(abs(w-reconstructed_w))
            history_prediction_error[k] = np.max(abs(moments["f"][k]
                -np.mean(reconstructed_w[:, None]*h2, axis=0)))
            for name, value in (("c1", h1), ("c2", h2), ("d1", d1), ("d2", d2)):
                moments[name][k] = value.T@value/n
            if k == 0:
                initial_h1, initial_h2 = h1.copy(), h2.copy()
            moments["motion1"][k] = np.mean((h1-initial_h1)**2, axis=0)
            moments["motion2"][k] = np.mean((h2-initial_h2)**2, axis=0)
            if history:
                for name, value in (("h1", h1), ("h2", h2), ("delta2", d2)):
                    history[name][k] = value
            if return_fields:
                for name, value in (("z1", z1), ("z2", z2), ("b1", b1), ("delta1", d1), ("w", w)):
                    history[name][k] = value
            maximum_field[k] = max(float(np.max(abs(x))) for x in (z1, z2, b1, w))
            if not np.isfinite(maximum_field[k]) or not np.isfinite(moments["f"][k]).all():
                raise FloatingPointError(f"Nonfinite frozen replay at step {k}")
            if k < s-1:
                force = self.input_gram[:, :m]*self.write[k][None, :]
                z1 += self.learning_step*(d1[:, :m]@force.T)
                w += self.learning_step*(h2[:, :m]@self.write[k])
        full = {}
        if full_grams:
            for name, field in (("C1", "h1"), ("C2", "h2"), ("D2", "delta2")):
                flat = history[field].transpose(1, 0, 2).reshape(n, s*p)
                full[name] = (flat.T@flat/n).reshape(s, p, s, p).transpose(0, 2, 1, 3)
        if return_fields:
            history.update(eta=eta, xi=xi)
        return dict(moments=moments, full=full, fields=history if return_fields else None,
                    maximum_absolute_field=maximum_field, history_w_error=history_w_error,
                    history_prediction_error=history_prediction_error)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024**2), b""):
            digest.update(block)
    return digest.hexdigest()


def _json_default(value: Any) -> Any:
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    raise TypeError(type(value).__name__)


def _source_current(source: dict[str, Array]) -> dict[str, Array]:
    index = np.arange(len(source["time"]))
    result = {name.lower(): source[name][index, index] for name in ("C1", "C2", "D1", "D2")}
    result["f"] = source["f"]
    for layer in (1, 2):
        history = source[f"C{layer}"]
        result[f"motion{layer}"] = (np.diagonal(history[index, index], axis1=1, axis2=2)
            + np.diag(history[0, 0])[None, :]-2*np.diagonal(history[:, 0], axis1=1, axis2=2))
    return result


def run(sourcepath: str | Path, n: int, batch: int, seed: int, out: str | Path, *,
        full_grams: bool = False, rank_rtol: float = 1e-12,
        rank_atol: float = 0.) -> dict[str, Any]:
    """Write one bounded diagnostic; an external caller may impose a wall timer.

    Require an even number of equal-size batches.  Conditional standard errors
    use the sample standard deviation of independent batch means divided by the
    square root of their count.  Full histories instead retain two independent
    half means (their absolute difference/2 is a noisy one-degree-of-freedom SE).
    """
    if (not isinstance(n, (int, np.integer)) or not isinstance(batch, (int, np.integer))
            or batch < 1 or n < 2*batch or n % (2*batch)):
        raise ValueError("n must be a positive multiple of 2*batch")
    sourcepath, out = Path(sourcepath).resolve(), Path(out).resolve()
    if sourcepath.is_dir():
        sourcepath = sourcepath/"trajectory.npz"
    out.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    source_names = ("frozen_population_replay.py", "causal_filtered_integrator.py",
                    "causal_panel_simulator.py", "causal_population_simulator.py")
    hashes = {name: _sha256(STUDY/name) for name in source_names}
    requested = dict(diagnostic="frozen_coefficient_independent_gaussian_quadrature",
        source=str(sourcepath), source_sha256=_sha256(sourcepath), code_sha256=hashes,
        population_size=int(n), batch_size=int(batch), batch_count=int(n//batch), seed=int(seed),
        full_grams=bool(full_grams), rank_rtol=rank_rtol, rank_atol=rank_atol,
        numpy=np.__version__, python=sys.version, command=sys.argv,
        precision="float64", cwd=str(Path.cwd()),
        gaussian_covariance_target="Saved empirical uncentered C1/D2 Grams, with declared eig truncation; not the old sampler's reconstructed factors.",
        factor_reconstruction_absolute_gate=1e-8,
        seed_streams=dict(bit_generator="PCG64", root_entropy=int(seed),
            construction="SeedSequence(seed).spawn(batch_count)[batch_index].spawn(3)",
            child_order=["root", "eta", "xi"], sample_kind="iid unwhitened standard Gaussian rows",
            independence="Distinct child streams for every batch and primitive family"),
        thread_environment={key: os.environ.get(key) for key in
                            ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
        interpretation="Conditional quadrature diagnostic; all saved coefficient and write histories are frozen.")
    source_record = sourcepath.parent/"record.json"
    if source_record.exists():
        requested["source_record_sha256"] = _sha256(source_record)
        record = json.loads(source_record.read_text())
        requested["source_config"] = record.get("config")
        requested["source_producer_sha256"] = record.get("source_sha256")
        original_diagnostics = record.get("diagnostics", {})
        requested["source_gaussian_maximum_covariance_error"] = {
            name: original_diagnostics.get(name, {}).get("maximum_covariance_error")
            for name in ("eta", "xi")}
        cfg = record.get("config", {})
        if cfg.get("kind") != "causal" or cfg.get("method") != "filtered":
            raise ValueError("Source record must identify a filtered causal full-model run")
    (out/"requested.json").write_text(json.dumps(requested, default=_json_default, indent=2)+"\n")
    try:
        with np.load(sourcepath, allow_pickle=False) as saved:
            source = {key: saved[key] for key in saved.files}
        t = source["time"]
        if len(t) < 2 or not np.allclose(np.diff(t), t[1]-t[0], atol=1e-12, rtol=1e-12):
            raise ValueError("Saved time grid must have at least two uniformly spaced points")
        program = FrozenProgram(vectors=source["vectors"], labels=source["labels"], dt=t[1]-t[0],
            C1=source["C1"], D2=source["D2"], Rh=source["Rh"], Rdelta=source["Rdelta"],
            write_deficit=source["write_deficit"])
        factors, diagnostics, eigenvalues = {}, {}, {}
        tick = time.perf_counter()
        for family, covariance in (("eta", program.C1), ("xi", program.D2)):
            factors[family], diagnostics[family], eigenvalues[family] = gaussian_factor(
                _flat_gram(covariance), rank_rtol=rank_rtol, rank_atol=rank_atol)
            if diagnostics[family]["maximum_covariance_error"] > 1e-8:
                raise FloatingPointError(f"{family} factor reconstruction exceeds the 1e-8 absolute gate")
        factor_seconds = time.perf_counter()-tick
        batch_count, half_count = n//batch, n//(2*batch)
        reference = _source_current(source)
        per_batch = {name: np.empty((batch_count,)+reference[name].shape) for name in CURRENT_NAMES}
        half_full = {name: np.zeros((2, program.s, program.s, program.p, program.p))
                     for name in ("C1", "C2", "D2")} if full_grams else {}
        maximum_field = np.empty((batch_count, program.s))
        history_w_error, history_prediction_error = np.empty_like(maximum_field), np.empty_like(maximum_field)
        batch_seconds = np.empty(batch_count)
        # Independent SeedSequence children separate all three families in every batch.
        batch_streams = np.random.SeedSequence(seed).spawn(batch_count)
        for b, sequence in enumerate(batch_streams):
            tick = time.perf_counter()
            root_rng, eta_rng, xi_rng = (np.random.default_rng(child) for child in sequence.spawn(3))
            root_z1 = root_rng.standard_normal((batch, program.d))@program.vectors.T
            primitives = {}
            for name, rng in (("eta", eta_rng), ("xi", xi_rng)):
                flat = rng.standard_normal((batch, factors[name].shape[1]))@factors[name].T
                primitives[name] = flat.reshape(batch, program.s, program.p).transpose(1, 0, 2)
            result = program.evaluate(root_z1, primitives["eta"], primitives["xi"], full_grams=full_grams)
            for name in CURRENT_NAMES:
                per_batch[name][b] = result["moments"][name]
            for name in half_full:
                half_full[name][b//half_count] += result["full"][name]/half_count
            maximum_field[b] = result["maximum_absolute_field"]
            history_w_error[b] = result["history_w_error"]
            history_prediction_error[b] = result["history_prediction_error"]
            if max(np.max(history_w_error[b]), np.max(history_prediction_error[b])) > 1e-10:
                raise FloatingPointError("Readout-history reconstruction exceeds the 1e-10 absolute gate")
            batch_seconds[b] = time.perf_counter()-tick
            print(json.dumps(dict(batch=b+1, batch_count=batch_count,
                elapsed_seconds=time.perf_counter()-started, batch_seconds=batch_seconds[b])), flush=True)
        arrays = dict(time=t, normalized_time=source.get("normalized_time", t*2/program.m),
            vectors=program.vectors, labels=program.labels, write_deficit=program.write,
            batch_seconds=batch_seconds, batch_maximum_absolute_field=maximum_field,
            batch_history_w_error=history_w_error, batch_history_prediction_error=history_prediction_error,
            eta_eigenvalues=eigenvalues["eta"], xi_eigenvalues=eigenvalues["xi"],
            batch_half=np.arange(batch_count)//half_count)
        summary = {}
        for name in CURRENT_NAMES:
            batches = per_batch[name]
            means = batches.mean(axis=0)
            se = batches.std(axis=0, ddof=1)/np.sqrt(batch_count)
            changes = batches-batches[:, :1]
            source_change = reference[name]-reference[name][:1]
            change_mean = changes.mean(axis=0)
            change_se = changes.std(axis=0, ddof=1)/np.sqrt(batch_count)
            arrays.update({name: means, "source_"+name: reference[name],
                "batch_"+name: batches, "se_"+name: se,
                "half_"+name: batches.reshape(2, half_count, *means.shape).mean(axis=1),
                "change_"+name: change_mean, "source_change_"+name: source_change,
                "se_change_"+name: change_se})
            for prefix_n in (8192, 16384, 32768):
                if prefix_n <= n and prefix_n % batch == 0:
                    arrays[f"prefix{prefix_n}_"+name] = batches[:prefix_n//batch].mean(axis=0)
            summary[name] = dict(maximum_absolute_defect=float(np.max(abs(means-reference[name]))),
                final_frobenius_defect=float(np.linalg.norm(means[-1]-reference[name][-1])),
                maximum_change_defect=float(np.max(abs(change_mean-source_change))),
                final_change_frobenius_defect=float(np.linalg.norm(change_mean[-1]-source_change[-1])),
                maximum_conditional_se=float(np.max(se)), maximum_change_conditional_se=float(np.max(change_se)))
        for name, halves in half_full.items():
            arrays[name] = halves.mean(axis=0)
            arrays["half_"+name] = halves
            arrays["half_se_"+name] = abs(halves[0]-halves[1])/2
            summary[name] = dict(maximum_absolute_defect=float(np.max(abs(arrays[name]-source[name]))),
                frobenius_defect=float(np.linalg.norm(arrays[name]-source[name])))
        arrays["raw_loss_diagnostic"] = np.mean((program.labels-arrays["f"][:, :program.m])**2, axis=1)
        arrays["source_raw_loss"] = np.mean((program.labels-source["f"][:, :program.m])**2, axis=1)
        arrays["batch_raw_loss_diagnostic"] = np.mean(
            (program.labels-per_batch["f"][:, :, :program.m])**2, axis=2)
        # A raw residual from the fresh mean is an observable only; it never drives a write.
        if hashes != {name: _sha256(STUDY/name) for name in source_names}:
            raise RuntimeError("Replay source code changed during execution")
        if requested["source_sha256"] != _sha256(sourcepath):
            raise RuntimeError("Saved coefficient source changed during execution")
        if not all(np.isfinite(value).all() for value in arrays.values()):
            raise FloatingPointError("Nonfinite saved diagnostic array")
        np.savez_compressed(out/"trajectory.npz", **arrays)
        record = dict(**requested, exit_status=0, wall_seconds=time.perf_counter()-started,
            factor_seconds=factor_seconds, gaussian_factors=diagnostics, comparison=summary,
            maximum_history_w_error=float(np.max(history_w_error)),
            maximum_history_prediction_error=float(np.max(history_prediction_error)),
            peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            se_convention="Equal independent batch means: sample sd/sqrt(batch_count); conditional on source coefficients.",
            full_history_se_convention="abs(half0-half1)/2; two independent equal halves, one variance degree of freedom.")
        (out/"record.json").write_text(json.dumps(record, default=_json_default, indent=2)+"\n")
        return record
    except Exception as exc:
        record = dict(**requested, exit_status=1, wall_seconds=time.perf_counter()-started, error=repr(exc),
                      peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        (out/"record.json").write_text(json.dumps(record, default=_json_default, indent=2)+"\n")
        raise


def self_test() -> dict[str, Any]:
    """Tiny deterministic validations only; no saved scientific run is replayed."""
    from causal_filtered_integrator import simulate_population

    vectors = np.array([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.],
                        [1., 1., 1.], [2., -1., 1.]])
    vectors /= np.linalg.norm(vectors, axis=1, keepdims=True)
    checks = {}
    for label_case, labels in (("nonzero", np.array([.3, -.2, .1])), ("zero", np.zeros(3))):
        original = simulate_population(labels, dt=.2, steps=4, population_size=23,
            seed=17, input_vectors=vectors, return_fields=True)
        program = FrozenProgram.from_result(original)
        fields = original["fields"]
        replay = program.evaluate(fields["z1"][0], fields["eta"], fields["xi"],
                                  full_grams=True, return_fields=True)
        errors = {name: float(np.max(abs(replay["fields"][name]-fields[name])))
                  for name in ("z1", "z2", "b1", "h1", "h2", "delta1", "delta2", "w")}
        errors["f"] = float(np.max(abs(replay["moments"]["f"]-original["f"])))
        assert max(errors.values()) < 1e-12, errors
        checks[label_case+"_same_primitive_field_errors"] = errors
        assert max(np.max(replay["history_w_error"]), np.max(replay["history_prediction_error"])) < 1e-12
        for name, group, layer in (("C1", "C", "layer1"), ("C2", "C", "layer2"), ("D2", "D", "layer2")):
            np.testing.assert_allclose(replay["full"][name], original[group][layer], atol=1e-12, rtol=0.)
        for layer in (1, 2):
            gram = replay["full"][f"C{layer}"]
            i = np.arange(program.s)
            motion = np.diagonal(gram[i, i], axis1=1, axis2=2)+np.diag(gram[0, 0])[None, :]
            motion -= 2*np.diagonal(gram[:, 0], axis1=1, axis2=2)
            np.testing.assert_allclose(motion, replay["moments"][f"motion{layer}"], atol=1e-12, rtol=0.)
        if label_case == "zero":
            assert not np.any(replay["moments"]["f"])
            factor, diagnostic, _ = gaussian_factor(_flat_gram(program.D2))
            assert diagnostic["rank"] == 0 and factor.shape[1] == 0
            eta_factor, _, _ = gaussian_factor(_flat_gram(program.C1))
            rng = np.random.default_rng(31)
            root = rng.normal(size=(29, program.d))@program.vectors.T
            eta = (rng.normal(size=(29, eta_factor.shape[1]))@eta_factor.T).reshape(29, program.s, program.p).transpose(1, 0, 2)
            fresh = program.evaluate(root, eta, np.zeros_like(eta))
            assert not np.any(fresh["moments"]["f"])
            assert not np.any(fresh["moments"]["motion1"])
            assert np.max(fresh["moments"]["motion2"]) < 1e-24
    base = np.array([[1., 0.], [0., 2.], [1., 2.], [0., 0.]])
    factor, diagnostic, _ = gaussian_factor(base@base.T)
    assert diagnostic["rank"] == 2
    np.testing.assert_allclose(factor@factor.T, base@base.T, atol=1e-12, rtol=0.)
    samples = np.random.default_rng(19).normal(size=(13, 2))@factor.T
    np.testing.assert_allclose(samples[:, 2], samples[:, 0]+samples[:, 1], atol=1e-12, rtol=0.)
    np.testing.assert_array_equal(samples[:, 3], np.zeros(13))
    try:
        gaussian_factor(np.diag([1., -.01]))
    except ValueError:
        checks["materially_negative_covariance_rejected"] = True
    else:
        raise AssertionError("Indefinite covariance was accepted")
    checks["singular_factor"] = diagnostic
    checks["passed"] = True
    return checks


def main() -> None:
    resource.setrlimit(resource.RLIMIT_AS, (12*1024**3, 12*1024**3))
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--source", type=Path)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--n", type=int, default=16384)
    parser.add_argument("--batch", type=int, default=512)
    parser.add_argument("--seed", type=int, default=81701)
    parser.add_argument("--full-grams", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        result = self_test()
    else:
        if args.source is None or args.out is None:
            parser.error("--source and --out are required for a scientific diagnostic")
        result = run(args.source, args.n, args.batch, args.seed, args.out, full_grams=args.full_grams)
    print(json.dumps(result, default=_json_default, indent=2))


if __name__ == "__main__":
    main()
