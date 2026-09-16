"""Full-batch tensor realization of H3.N2 in arbitrary input d.

Input rows are U=x/sqrt(d); this module never renormalizes them. Population
quadrature, dictionary initialization, and finite-network width are separate.
All retained matrix directions evolve; blocking only partitions exact sums.
Float64 is the reference. Float32 is explicit and requires numerical checks.
"""
from dataclasses import dataclass, field
import json
from pathlib import Path

import numpy as np
import torch


@dataclass
class TensorState:
    w: torch.Tensor
    c: torch.Tensor
    M: torch.Tensor

    def clone(self):
        return TensorState(self.w.clone(), self.c.clone(), self.M.clone())

    def numpy(self):
        return {k: getattr(self, k).detach().cpu().numpy().copy() for k in ("w", "c", "M")}


@dataclass
class TensorData:
    inputs: torch.Tensor
    labels: torch.Tensor
    probabilities: torch.Tensor
    _versions: tuple = field(init=False, repr=False)

    def __post_init__(self):
        self._versions = tuple((id(x), x._version) for x in (self.inputs, self.labels, self.probabilities))


class ClosureEngine:
    """Fixed marks plus stateless prediction/RHS/Heun operations.

    Constructor owns independent fixed arrays; returned TensorState owns only
    moving w,c,M. Callers must treat fixed engine tensors as immutable. Hot
    operations validate boundary shapes and finiteness (which can synchronize
    a CUDA device). Mutation of fixed tensors/caches is rejected on next use.
    """

    def __init__(self, b1, g, b2, D, *, p1=None, p2=None, device="cpu",
                 dtype=torch.float64, block_size=512, forward_mode="auto", representation=None):
        if dtype not in (torch.float32, torch.float64):
            raise ValueError("dtype must be explicit torch.float32 or torch.float64")
        if isinstance(block_size, bool) or not isinstance(block_size, int) or block_size < 1:
            raise ValueError("block_size must be a positive integer")
        if forward_mode not in ("auto", "direct", "folded"):
            raise ValueError("forward_mode must be auto, direct, or folded")
        self._representation = json.loads(json.dumps(representation or {"sign_folded": False, "population_rule": "supplied", "nominal_population_nodes": None, "omitted_inactive_constant_features": False}, allow_nan=False))
        self.forward_mode = forward_mode
        self.device, self.dtype, self.block_size = torch.device(device), dtype, block_size
        self.b1, self.g, self.b2, self.D = [self._tensor(x, copy=True) for x in (b1, g, b2, D)]
        self.device = self.b1.device
        if self.b1.ndim != 2 or self.b2.ndim != 2 or self.g.ndim != 2:
            raise ValueError("b1,b2,g must be matrices")
        if min(*self.b1.shape, *self.b2.shape, *self.g.shape) < 1:
            raise ValueError("empty population, input, or feature dimension")
        self.P1, self.K1 = self.b1.shape
        self.P2, self.K2 = self.b2.shape
        self.d = self.g.shape[1]
        if self.g.shape[0] != self.P1 or self.D.shape != (self.K2, self.K1):
            raise ValueError("inconsistent joint marks or D feature dimensions")
        self.p1 = self._probabilities(p1, self.P1)
        self.p2 = self._probabilities(p2, self.P2)
        # Multiplications by frozen quadrature weights happen once.
        self.b1_weighted_T = (self.b1.T*self.p1).contiguous()
        self.b2_T = self.b2.T.contiguous()
        if not all(bool(torch.isfinite(x).all()) for x in (self.b1, self.g, self.b2, self.D)):
            raise ValueError("nonfinite fixed marks")
        self._frozen_versions = tuple((id(x), x._version) for x in self._fixed_arrays())
        self._policy = self.arithmetic_policy()
        folded = self._representation.get("sign_folded")
        if not isinstance(folded, bool):
            raise ValueError("representation needs boolean sign_folded")
        if folded and (self._representation.get("population_rule") != "antithetic" or
                       self._representation.get("nominal_population_nodes") != 2*self.P1 or
                       self.P1 != self.P2 or
                       not self._representation.get("omitted_inactive_constant_features")):
            raise ValueError("folded representation requires equal base counts, nominal twice stored, and omitted constants")

    @property
    def representation(self):
        return json.loads(json.dumps(self._representation))

    def _fixed_arrays(self):
        return (self.b1, self.g, self.b2, self.D, self.p1, self.p2, self.b1_weighted_T, self.b2_T)

    def arithmetic_policy(self):
        return dict(tf32=bool(torch.backends.cuda.matmul.allow_tf32),
                    float32_matmul_precision=torch.get_float32_matmul_precision(),
                    deterministic_algorithms=bool(torch.are_deterministic_algorithms_enabled()),
                    torch_version=str(torch.__version__), device_type=self.device.type)

    def _check_fixed(self):
        if tuple((id(x), x._version) for x in self._fixed_arrays()) != self._frozen_versions:
            raise ValueError("frozen marks/caches mutated; construct a new engine")
        if self.arithmetic_policy() != self._policy:
            raise ValueError("arithmetic policy changed; construct a new engine")
        if isinstance(self.block_size, bool) or not isinstance(self.block_size, int) or self.block_size < 1:
            raise ValueError("block_size must be positive")
        if self.forward_mode not in ("auto", "direct", "folded"):
            raise ValueError("invalid contraction association")

    def _tensor(self, x, copy=False):
        raw = torch.as_tensor(x)
        if raw.is_complex() or raw.dtype == torch.bool:
            raise ValueError("arrays must contain real numbers, not complex/bool")
        out = torch.as_tensor(x, dtype=self.dtype, device=self.device).detach()
        return out.clone().contiguous() if copy else out.contiguous()

    def _probabilities(self, p, size):
        out = (torch.full((size,), 1/size, dtype=self.dtype, device=self.device)
               if p is None else self._tensor(p, copy=True))
        tolerance = 2e-12 if self.dtype == torch.float64 else 2e-6
        if out.shape != (size,) or not bool(torch.isfinite(out).all()):
            raise ValueError("invalid probability shape/values")
        if bool((out < 0).any()) or abs(float(out.sum())-1) > tolerance:
            raise ValueError("probabilities must be nonnegative and sum to one")
        return out

    def prepare_inputs(self, inputs):
        out = self._tensor(inputs, copy=True)
        if out.ndim != 2 or out.shape[1] != self.d or not len(out):
            raise ValueError("inputs must have nonempty shape (m,d)")
        if not bool(torch.isfinite(out).all()):
            raise ValueError("nonfinite inputs")
        return out

    def prepare_data(self, inputs, labels, probabilities=None):
        inputs = self.prepare_inputs(inputs)
        labels = self._tensor(labels, copy=True)
        if labels.shape != (len(inputs),) or not bool(torch.isfinite(labels).all()):
            raise ValueError("labels must be a finite vector matching inputs")
        return TensorData(inputs, labels, self._probabilities(probabilities, len(inputs)))

    def initial_state(self):
        return TensorState(self.g.clone(), torch.zeros(self.P2, dtype=self.dtype,
                           device=self.device), self.D.clone())

    def state(self, w, c, M):
        result = TensorState(*(self._tensor(x, copy=True) for x in (w, c, M)))
        self.validate_state(result)
        return result

    def validate_state(self, state, *, finite=True):
        self._check_fixed()
        if not isinstance(state, TensorState):
            raise ValueError("state must be TensorState")
        for name, shape in (("w", (self.P1, self.d)), ("c", (self.P2,)),
                            ("M", (self.K2, self.K1))):
            x = getattr(state, name)
            if not isinstance(x, torch.Tensor) or x.shape != shape or x.dtype != self.dtype or x.device != self.device:
                raise ValueError("state shape/dtype/device mismatch: " + name)
            if finite and not bool(torch.isfinite(x).all()):
                raise ValueError("nonfinite state: " + name)
        return state

    def _inputs(self, inputs):
        if not isinstance(inputs, torch.Tensor):
            return self.prepare_inputs(inputs)
        if (inputs.ndim != 2 or inputs.shape[1] != self.d or len(inputs) < 1
                or inputs.dtype != self.dtype or inputs.device != self.device):
            raise ValueError("prepare inputs once with this engine before evaluation")
        if not bool(torch.isfinite(inputs).all()):
            raise ValueError("nonfinite inputs")
        return inputs

    def _validate_data(self, data):
        if not isinstance(data, TensorData):
            raise ValueError("prepare data with this engine")
        if tuple((id(x), x._version) for x in (data.inputs, data.labels, data.probabilities)) != data._versions:
            raise ValueError("prepared data mutated; prepare new data")
        self._inputs(data.inputs)
        for x in (data.labels, data.probabilities):
            if x.shape != (len(data.inputs),) or x.dtype != self.dtype or x.device != self.device:
                raise ValueError("prepare data once with this engine before evolution")
            if not bool(torch.isfinite(x).all()):
                raise ValueError("nonfinite data")
        tolerance = 2e-12 if self.dtype == torch.float64 else 2e-6
        if bool((data.probabilities < 0).any()) or abs(float(data.probabilities.sum())-1) > tolerance:
            raise ValueError("invalid data probabilities")

    def _fields(self, state, inputs):
        h1 = (state.w @ inputs.T).tanh_()
        a = self.b1_weighted_T @ h1
        h2 = (self.b2 @ (state.M @ a)).tanh_()
        f = (self.p2*state.c) @ h2
        return h1, a, h2, f

    @torch.no_grad()
    def predict(self, state, inputs):
        self.validate_state(state)
        inputs = self._inputs(inputs)
        out = torch.empty(len(inputs), dtype=self.dtype, device=self.device)
        for start in range(0, len(inputs), self.block_size):
            stop = min(start+self.block_size, len(inputs))
            out[start:stop] = self._fields(state, inputs[start:stop])[3]
        if not bool(torch.isfinite(out).all()):
            raise ValueError("nonfinite prediction")
        return out

    @torch.no_grad()
    def rhs(self, state, data, *, implementation="optimized"):
        """Full weighted-batch velocity; no update takes place inside a block.

        'reference' follows the displayed contractions directly. 'optimized'
        also folds c and p2 once into the backward feature matrix and, when
        its multiplication count is smaller, forms b1@M.T once per RHS.
        Forward precontraction b2@M uses the same cost rule (forward_mode='auto');
        'direct' and 'folded' permit reproducible timing of either association.
        Both use every sample and every feature, with identical real formulas.
        """
        if implementation not in ("optimized", "reference"):
            raise ValueError("unknown implementation")
        self.validate_state(state)
        self._validate_data(data)
        vw, vc, vM = torch.zeros_like(state.w), torch.zeros_like(state.c), torch.zeros_like(state.M)
        if implementation == "optimized":
            weighted_c = self.p2*state.c
            backward_features = self.b2_T*weighted_c
            # Compare leading multiply-add counts over the entire batch.
            m = len(data.inputs)
            cost_direct = m*(self.P1*self.K1+self.K1*self.K2)
            cost_folded = self.P1*self.K1*self.K2+m*self.P1*self.K2
            reverse_left = self.b1 @ state.M.T if cost_folded < cost_direct else None
            forward_direct = m*(self.K2*self.K1+self.P2*self.K2)
            forward_folded = self.P2*self.K2*self.K1+m*self.P2*self.K1
            use_forward = self.forward_mode == "folded" or (self.forward_mode == "auto"
                                                            and forward_folded < forward_direct)
            forward_left = self.b2 @ state.M if use_forward else None
        for start in range(0, len(data.inputs), self.block_size):
            stop = min(start+self.block_size, len(data.inputs))
            u = data.inputs[start:stop]
            h1 = (state.w @ u.T).tanh_()
            a = self.b1_weighted_T @ h1
            if implementation == "optimized" and forward_left is not None:
                h2 = (forward_left @ a).tanh_()
            else:
                h2 = (self.b2 @ (state.M @ a)).tanh_()
            if implementation == "reference":
                f = self.p2 @ (state.c[:, None]*h2)
                d = self.b2_T @ (self.p2[:, None]*state.c[:, None]*(1-h2*h2))
                q = self.b1 @ (state.M.T @ d)
                r = data.probabilities[start:stop]*(f-data.labels[start:stop])
                vw.addmm_((1-h1*h1)*q*r, u, alpha=-2)
                vc.addmv_(h2, r, alpha=-2)
                vM.addmm_(d*r, a.T, alpha=-2)
            else:
                f = weighted_c @ h2
                r = data.probabilities[start:stop]*(f-data.labels[start:stop])
                vc.addmv_(h2, r, alpha=-2)
                # Forward h2 is no longer needed; reuse it for its derivative.
                h2.square_().neg_().add_(1)
                d = backward_features @ h2
                q = (reverse_left @ d if reverse_left is not None
                     else self.b1 @ (state.M.T @ d))
                h1.square_().neg_().add_(1).mul_(q).mul_(r)
                vw.addmm_(h1, u, alpha=-2)
                d.mul_(r)
                vM.addmm_(d, a.T, alpha=-2)
        return self.validate_state(TensorState(vw, vc, vM))

    @torch.no_grad()
    def heun_step(self, state, data, step_size, *, implementation="optimized"):
        if isinstance(step_size, (bool, np.bool_)):
            raise ValueError("step_size must be positive")
        h = float(step_size)
        if not np.isfinite(h) or h <= 0:
            raise ValueError("step_size must be finite and positive")
        k = self.rhs(state, data, implementation=implementation)
        stage = TensorState(state.w+h*k.w, state.c+h*k.c, state.M+h*k.M)
        ell = self.rhs(stage, data, implementation=implementation)
        return self.validate_state(TensorState(state.w+(h/2)*(k.w+ell.w), state.c+(h/2)*(k.c+ell.c),
                           state.M+(h/2)*(k.M+ell.M)))

    def evolve(self, state, data, *, steps, step_size, implementation="optimized"):
        if isinstance(steps, bool) or not isinstance(steps, int) or steps < 0:
            raise ValueError("steps must be a nonnegative integer")
        self.validate_state(state)
        self._validate_data(data)
        if isinstance(step_size, (bool, np.bool_)) or not np.isfinite(float(step_size)) or float(step_size) <= 0:
            raise ValueError("step_size must be finite positive, including for zero steps")
        current = state.clone()
        for _ in range(steps):
            current = self.heun_step(current, data, step_size, implementation=implementation)
        return self.validate_state(current)

    @torch.no_grad()
    def observations(self, state, panel, *, probabilities=None, include_grams=True,
                     include_pairs=False):
        """Same-mark initial/current activations, RMS, and panel activation Grams.

        G_l[u,v]=sum_i p_l[i] h_l(i,u)h_l(i,v). These are uncentered
        activation Grams over the fixed input panel; no whitening or scaling.
        Cross Grams order initial rows/current columns. Full panel activations
        are retained only when Gram or pair arrays are requested.
        """
        self.validate_state(state)
        if isinstance(panel, TensorData):
            self._validate_data(panel)
        inputs = self._inputs(panel.inputs if isinstance(panel, TensorData) else panel)
        weights = (panel.probabilities if isinstance(panel, TensorData)
                   else self._probabilities(probabilities, len(inputs)))
        saved = [[], [], [], []]
        squares = torch.zeros(2, dtype=self.dtype, device=self.device)
        out = torch.empty(len(inputs), dtype=self.dtype, device=self.device)
        for start in range(0, len(inputs), self.block_size):
            stop = min(start+self.block_size, len(inputs))
            u = inputs[start:stop]
            h1, _, h2, f = self._fields(state, u)
            init1 = (self.g @ u.T).tanh_()
            init2 = (self.b2 @ (self.D @ (self.b1_weighted_T @ init1))).tanh_()
            squares[0] += self.p1 @ ((h1-init1).square() @ weights[start:stop])
            squares[1] += self.p2 @ ((h2-init2).square() @ weights[start:stop])
            out[start:stop] = f
            if include_grams or include_pairs:
                for parts, values in zip(saved, (init1, h1, init2, h2)):
                    parts.append(values)
        result = {"rms1": squares[0].sqrt(), "rms2": squares[1].sqrt(), "prediction": out,
                  "input_weights": weights.clone(), "inputs": inputs.clone()}
        if include_grams or include_pairs:
            first0, first, second0, second = [torch.cat(parts, dim=1) for parts in saved]
            for number, initial, current, p in ((1, first0, first, self.p1),
                                                (2, second0, second, self.p2)):
                if include_grams:
                    result[f"gram{number}_initial"] = initial.T @ (p[:, None]*initial)
                    result[f"gram{number}_current"] = current.T @ (p[:, None]*current)
                    result[f"gram{number}_cross"] = initial.T @ (p[:, None]*current)
                if include_pairs:
                    pairs = torch.stack((initial, current), dim=-1)
                    if self._representation["sign_folded"]:
                        pairs = torch.cat((pairs, -pairs), dim=0)
                        p = torch.cat((p/2, p/2))
                    result[f"pairs{number}"] = pairs
                    result[f"population_weights{number}"] = p.clone()
        if not all(bool(torch.isfinite(v).all()) for v in result.values()):
            raise ValueError("nonfinite observations")
        return result

    @torch.no_grad()
    def loss(self, state, data):
        self._validate_data(data)
        result = data.probabilities @ (self.predict(state, data.inputs)-data.labels).square()
        if not bool(torch.isfinite(result)):
            raise ValueError("nonfinite loss")
        return result

    def retained_bytes(self, state):
        arrays = [self.b1, self.g, self.b2, self.D, self.p1, self.p2,
                  self.b1_weighted_T, self.b2_T, state.w, state.c, state.M]
        return sum(x.numel()*x.element_size() for x in arrays)

    def save_restart(self, path, state, data, *, metadata=None):
        """Pickle-free archive with all fixed marks, data, and current raw state."""
        self.validate_state(state)
        self._validate_data(data)
        record = {"format": "p1-torch-closure-v2", "dtype": str(self.dtype).split(".")[-1],
                  "block_size": self.block_size, "forward_mode": self.forward_mode, "metadata": metadata or {},
                  "representation": self.representation, "arithmetic_policy": self._policy}
        arrays = {k: getattr(self, k).detach().cpu().numpy() for k in ("b1", "g", "b2", "D", "p1", "p2")}
        arrays.update(state.numpy())
        arrays.update({k: getattr(data, k).detach().cpu().numpy() for k in ("inputs", "labels", "probabilities")})
        arrays["record"] = np.asarray(json.dumps(record, allow_nan=False))
        with Path(path).open("wb") as handle:
            np.savez(handle, **arrays)

    @classmethod
    def load_restart(cls, path, *, device="cpu"):
        with np.load(path, allow_pickle=False) as saved:
            record = json.loads(str(saved["record"]))
            if record["format"] != "p1-torch-closure-v2" or record["dtype"] not in ("float32", "float64"):
                raise ValueError("unsupported restart format or dtype")
            engine = cls(saved["b1"], saved["g"], saved["b2"], saved["D"], p1=saved["p1"], p2=saved["p2"],
                         device=device, dtype=getattr(torch, record["dtype"]), block_size=record["block_size"],
                         forward_mode=record["forward_mode"], representation=record["representation"])
            if engine.arithmetic_policy() != record["arithmetic_policy"]:
                raise ValueError("restart requires identical arithmetic policy and device type")
            state = engine.state(saved["w"], saved["c"], saved["M"])
            data = engine.prepare_data(saved["inputs"], saved["labels"], saved["probabilities"])
        return engine, state, data, record["metadata"]


def initialize_p1(d, particles, seed, *, device="cpu", dtype=torch.float64, block_size=512,
                  forward_mode="auto", **initialization_options):
    """Return (engine, initial_state); p=1 and no neural-width argument.

    NumPy initializer options include population_rule and folded. Its complete
    representation/quadrature metadata is required checkpoint data.
    """
    from pde.observable_p1_initialization import initialize
    initial = initialize(d, particles, seed, **initialization_options)
    engine = ClosureEngine(initial.b1, initial.g, initial.b2, initial.D,
        p1=initial.p1, p2=initial.p2, device=device, dtype=dtype, block_size=block_size,
        forward_mode=forward_mode, representation=initial.metadata)
    return engine, engine.initial_state()
