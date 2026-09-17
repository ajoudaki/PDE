"""Study-local float64 tensor implementation of the maintained closure.

Inputs are normalized unit directions u=x/sqrt(2), shape (m,2).  Frozen
marks are produced by pde.observable_solver.initialize without alteration.
Only w,c,M evolve; step uses simultaneous explicit Heun in physical time
for the unhalved probability-weighted squared loss. No finite network is used.

Kernel block order is (w,c,M); kernel excludes data weights and loss factors.
The state metric is sum_i p1_i |dw_i|^2 + sum_i p2_i dc_i^2 + |dM|_F^2.
"""
from dataclasses import dataclass
import json
from pathlib import Path
import sys

import numpy as np
import torch

REPO = Path(__file__).resolve().parents[2]
if str(REPO / "code") not in sys.path:
    sys.path.insert(0, str(REPO / "code"))
from pde.observable_solver import initialize as maintained_initialize

ARRAYS = ("b1", "g", "w", "p1", "b2", "c", "p2", "M", "D")
FORMAT = "closure-circle-torch-float64-v1"


def _numpy(value):
    return value.detach().cpu().numpy().copy()


@dataclass(frozen=True)
class Data:
    """Once-validated device tensors; callers must not mutate these arrays."""
    inputs: torch.Tensor
    labels: torch.Tensor
    probabilities: torch.Tensor


class Closure:
    def __init__(self, arrays, metadata, device="cpu", clock=None):
        self.device = torch.device(device)
        for key in ARRAYS:
            setattr(self, key, torch.as_tensor(arrays[key], dtype=torch.float64,
                                              device=self.device).clone())
        self.device = self.w.device  # Resolve bare 'cuda' to its concrete index.
        self.metadata = json.loads(json.dumps(metadata, allow_nan=False))
        self.clock = dict(clock or {"physical_time": 0.0, "steps": 0})
        self._validate_state()
        # Algebraically identical weighted contractions with frozen marks.
        self._b1pT = (self.b1 * self.p1[:, None]).T.contiguous()
        self._b2pT = (self.b2 * self.p2[:, None]).T.contiguous()

    def _tensor(self, value):
        if isinstance(value, torch.Tensor):
            if value.dtype == torch.bool:
                raise ValueError("boolean numerical input")
        elif np.asarray(value).dtype.kind == "b":
            raise ValueError("boolean numerical input")
        return torch.as_tensor(value, dtype=torch.float64, device=self.device)

    def _inputs(self, inputs):
        u = self._tensor(inputs)
        if u.ndim != 2 or u.shape[0] < 1 or u.shape[1] != 2:
            raise ValueError("inputs must have nonempty shape (m,2)")
        if not bool(torch.isfinite(u).all()) or not bool(((u*u).sum(1)-1).abs().le(2e-12).all()):
            raise ValueError("inputs must be normalized unit-circle directions u=x/sqrt(2)")
        return u

    def _validate_state(self):
        if not all(bool(torch.isfinite(getattr(self, k)).all()) for k in ARRAYS):
            raise ValueError("nonfinite state")
        if self.b1.ndim != 2 or self.b2.ndim != 2 or min(*self.b1.shape, *self.b2.shape) < 1:
            raise ValueError("invalid feature tables")
        if self.g.shape != (len(self.b1), 2) or self.w.shape != self.g.shape:
            raise ValueError("invalid first joint population")
        if self.c.shape != (len(self.b2),) or self.p1.shape != (len(self.b1),) or self.p2.shape != self.c.shape:
            raise ValueError("invalid population shapes")
        if self.M.shape != (self.b2.shape[1], self.b1.shape[1]) or self.D.shape != self.M.shape:
            raise ValueError("invalid feature-indexed action")
        for p in (self.p1, self.p2):
            if bool((p < 0).any()) or abs(float(p.sum())-1) > 2e-12*len(p):
                raise ValueError("population weights must have unit mass")

    def prepare_data(self, inputs, labels, weights):
        u = self._inputs(inputs)
        y, p = self._tensor(labels), self._tensor(weights)
        if y.shape != (len(u),) or p.shape != y.shape:
            raise ValueError("data arrays have inconsistent shapes")
        if not bool(torch.isfinite(y).all()) or not bool(torch.isfinite(p).all()):
            raise ValueError("nonfinite labels or data weights")
        if bool((p < 0).any()) or abs(float(p.sum())-1) > 2e-12*len(p):
            raise ValueError("data weights must have unit mass")
        return Data(u.clone(), y.clone(), p.clone())

    def _data(self, data):
        if isinstance(data, Data):
            if data.inputs.device != self.device:
                raise ValueError("prepared data device differs from engine")
            return data
        if hasattr(data, "inputs"):
            return self.prepare_data(data.inputs, data.labels, data.probabilities)
        return self.prepare_data(*data)

    def _fields(self, u, w=None, c=None, M=None, backward=True):
        w = self.w if w is None else w
        c = self.c if c is None else c
        M = self.M if M is None else M
        h1 = torch.tanh(w @ u.T)
        a = self._b1pT @ h1
        h2 = torch.tanh(self.b2 @ (M @ a))
        f = (self.p2*c) @ h2
        result = dict(h1=h1, a=a, h2=h2, f=f)
        if backward:
            d = self._b2pT @ (c[:, None]*(1-h2*h2))
            result.update(d=d, q=self.b1 @ (M.T @ d))
        return result

    def fields(self, inputs, backward=True):
        return self._fields(self._inputs(inputs), backward=backward)

    def initial_fields(self, inputs):
        return self._fields(self._inputs(inputs), w=self.g, c=torch.zeros_like(self.c),
                            M=self.D, backward=False)

    def _rhs(self, data, w=None, c=None, M=None):
        v = self._fields(data.inputs, w, c, M)
        r = data.probabilities*(v["f"]-data.labels)
        vw = -2*((1-v["h1"]*v["h1"])*v["q"]*r) @ data.inputs
        vc = -2*v["h2"] @ r
        vM = -2*(v["d"]*r) @ v["a"].T
        return vw, vc, vM

    def rhs(self, data):
        return self._rhs(self._data(data))

    @torch.no_grad()
    def step_data(self, data, h):
        """Fast path for a prepare_data result; updates all blocks together."""
        if not isinstance(data, Data) or data.inputs.device != self.device:
            raise ValueError("step_data needs prepared data on the engine device")
        h = float(h)
        if not np.isfinite(h) or h <= 0:
            raise ValueError("step size must be finite and positive")
        k = self._rhs(data)
        stage = (self.w+h*k[0], self.c+h*k[1], self.M+h*k[2])
        ell = self._rhs(data, *stage)
        updated = (self.w+(h/2)*(k[0]+ell[0]), self.c+(h/2)*(k[1]+ell[1]),
                   self.M+(h/2)*(k[2]+ell[2]))
        self.w, self.c, self.M = updated
        self.clock["physical_time"] += h
        self.clock["steps"] += 1
        return self

    def step(self, inputs, labels, weights, h):
        return self.step_data(self.prepare_data(inputs, labels, weights), h)

    @torch.no_grad()
    def predict(self, panel, block_size=256):
        u = self._inputs(panel)
        if isinstance(block_size, bool) or not isinstance(block_size, int) or block_size < 1:
            raise ValueError("block_size must be a positive integer")
        result = torch.cat([self._fields(block, backward=False)["f"]
                            for block in u.split(block_size)])
        if not bool(torch.isfinite(result).all()):
            raise ValueError("nonfinite prediction")
        return _numpy(result)

    @torch.no_grad()
    def tangent_blocks(self, inputs, right_inputs=None):
        """Exact w,c,M kernel blocks, optionally rectangular; no loss factors."""
        u = self._inputs(inputs)
        v = u if right_inputs is None else self._inputs(right_inputs)
        left = self._fields(u)
        right = left if right_inputs is None else self._fields(v)
        s = (1-left["h1"]**2)*left["q"]
        t = (1-right["h1"]**2)*right["q"]
        kw = (s.T @ (self.p1[:, None]*t))*(u @ v.T)
        kc = left["h2"].T @ (self.p2[:, None]*right["h2"])
        km = (left["d"].T @ right["d"])*(left["a"].T @ right["a"])
        return _numpy(torch.stack((kw, kc, km)))

    @torch.no_grad()
    def diagnostics(self, panel, training_inputs, training_weights):
        """Population-averaged one-sided Fourier energy and paired hidden motion.

        panel must traverse an equally spaced full circle in increasing angle.
        power[k] is E_population |DFT(h)[k]/J|^2, doubled except at DC and
        even-J Nyquist, so its sum equals the panel-averaged hidden square.
        Motion powers use the same-mark field difference before Fourier transform.
        Training Grams use population weights and no data-weight factors.
        """
        u = self._inputs(panel)
        j = len(u)
        theta0 = torch.atan2(u[0, 1], u[0, 0])
        theta = theta0+2*torch.pi*torch.arange(j, dtype=torch.float64, device=self.device)/j
        expected = torch.stack((torch.cos(theta), torch.sin(theta)), 1)
        if not bool((u-expected).abs().le(2e-10).all()):
            raise ValueError("Fourier panel must be a uniform full circle in increasing angle")
        current = self._fields(u, backward=False)
        initial = self._fields(u, self.g, torch.zeros_like(self.c), self.D, False)
        data = self.prepare_data(training_inputs, np.zeros(len(training_inputs)), training_weights)
        train = self._fields(data.inputs, backward=False)
        train0 = self._fields(data.inputs, self.g, torch.zeros_like(self.c), self.D, False)
        result = {"fourier_k": np.arange(j//2+1), "prediction": _numpy(current["f"]),
                  "train_prediction": _numpy(train["f"])}
        scale = torch.full((j//2+1,), 2.0, dtype=torch.float64, device=self.device)
        scale[0] = 1
        if j % 2 == 0:
            scale[-1] = 1
        for name, values in (("current", current["a"]), ("initial", initial["a"]),
                             ("motion", current["a"]-initial["a"])):
            coeff = torch.fft.rfft(values, dim=1)/j
            result[f"a_power_{name}"] = _numpy((coeff.real**2+coeff.imag**2).sum(0)*scale)
        for layer, p in ((1, self.p1), (2, self.p2)):
            key = f"h{layer}"
            for name, values in (("current", current[key]), ("initial", initial[key]),
                                 ("motion", current[key]-initial[key])):
                coeff = torch.fft.rfft(values, dim=1)/j
                power = (p @ (coeff.real**2+coeff.imag**2))*scale
                result[f"hidden{layer}_power_{name}"] = _numpy(power)
            result[f"hidden{layer}_gram_current"] = _numpy(train[key].T @ (p[:, None]*train[key]))
            result[f"hidden{layer}_gram_initial"] = _numpy(train0[key].T @ (p[:, None]*train0[key]))
            result[f"hidden{layer}_motion_rms_training"] = float(torch.sqrt(p @ ((train[key]-train0[key])**2) @ data.probabilities))
            result[f"hidden{layer}_motion_rms_circle"] = float(torch.sqrt((p @ ((current[key]-initial[key])**2)).mean()))
        result["tangent_blocks_training"] = self.tangent_blocks(data.inputs)
        return result

    def arrays_numpy(self):
        return {key: _numpy(getattr(self, key)) for key in ARRAYS}

    def clone(self):
        """Independent dynamic and frozen arrays; no initializer rerun."""
        return Closure({k: getattr(self, k) for k in ARRAYS}, self.metadata,
                       self.device, self.clock)

    copy = clone

    def save_npz(self, path, metadata=None, data=None):
        """Full own-state restart; optional training law is saved with the state."""
        self._validate_state()
        record = dict(format=FORMAT, metadata=self.metadata, clock=self.clock,
                      extra_metadata={} if metadata is None else metadata)
        payload = self.arrays_numpy()
        if data is not None:
            data = self._data(data)
            for key in ("inputs", "labels", "probabilities"):
                payload["data_"+key] = _numpy(getattr(data, key))
        payload["record_json"] = np.asarray(json.dumps(record, sort_keys=True, allow_nan=False))
        with Path(path).open("wb") as handle:
            np.savez_compressed(handle, **payload)

    @classmethod
    def load_npz(cls, path, device="cpu"):
        return load_npz(path, device)


def initialize(order, Q, P, device="cpu"):
    reference = maintained_initialize(order, initialization_nodes=Q, population_nodes=P)
    return Closure({k: getattr(reference, k) for k in ARRAYS}, reference.metadata, device)


def load_npz(path, device="cpu"):
    with np.load(path, allow_pickle=False) as archive:
        record = json.loads(str(archive["record_json"].item()))
        if record.get("format") != FORMAT:
            raise ValueError("unsupported engine checkpoint format")
        expected = set(ARRAYS) | {"record_json"}
        data_keys = {"data_inputs", "data_labels", "data_probabilities"}
        if set(archive.files) not in (expected, expected | data_keys):
            raise ValueError("invalid engine checkpoint fields")
        engine = Closure({k: archive[k] for k in ARRAYS}, record["metadata"], device, record["clock"])
        engine.checkpoint_metadata = record["extra_metadata"]
        engine.checkpoint_data = (engine.prepare_data(archive["data_inputs"], archive["data_labels"],
                                  archive["data_probabilities"]) if data_keys <= set(archive.files) else None)
    return engine
