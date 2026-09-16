"""Optional Torch reference for bias-free two-hidden tanh physical GF.

U rows are x/sqrt(d). Stored initialization variances are (1,1/n,1/n²),
output is c.T@h2/n, unhalved weighted loss, mobilities (n,1,n).
Ordinary float32/64 arithmetic, including 1-tanh²; no extreme-range promise.
"""
import numpy as np
import torch
from pde.observable_torch_p1 import TensorState, TensorData, ClosureEngine


class NetworkEngine:
    """Owned initial arrays, full dense moving network, simultaneous Heun.

    Inputs and prepared data are copied. Prepared data and the initial state
    are immutable by contract; detected in-place tensor edits are rejected.
    Moving states may be edited and are revalidated at every public call.
    """
    # Share only input/domain utilities; network contractions remain separate.
    _tensor = ClosureEngine._tensor
    _probabilities = ClosureEngine._probabilities
    prepare_inputs = ClosureEngine.prepare_inputs
    prepare_data = ClosureEngine.prepare_data
    _inputs = ClosureEngine._inputs
    _validate_data = ClosureEngine._validate_data
    arithmetic_policy = ClosureEngine.arithmetic_policy

    def __init__(self, d, width, seed, *, device="cpu", dtype=torch.float64, block_size=512):
        from pde.finite_network import initialize
        if dtype not in (torch.float32, torch.float64):
            raise ValueError("dtype must be float32 or float64")
        if isinstance(block_size, bool) or not isinstance(block_size, int) or block_size < 1:
            raise ValueError("block_size must be positive")
        initial = initialize(width, 2, d, seed=seed)
        self.d, self.n = initial.input_dimension, initial.width
        self.device, self.dtype, self.block_size = torch.device(device), dtype, block_size
        self.initial = TensorState(*(self._tensor(a, copy=True) for a in
                                     (initial.weights[0], initial.readout, initial.weights[1])))
        self.device = self.initial.w.device
        self._initial_versions = self._versions()
        self._policy = self.arithmetic_policy()

    def _versions(self):
        return tuple((id(x), x._version) for x in (self.initial.w, self.initial.c, self.initial.M))

    def validate_state(self, state):
        if self._versions() != self._initial_versions:
            raise ValueError("initial state mutated; construct a new engine")
        if self.arithmetic_policy() != self._policy:
            raise ValueError("arithmetic policy changed; construct a new engine")
        if isinstance(self.block_size, bool) or not isinstance(self.block_size, int) or self.block_size < 1:
            raise ValueError("block_size must be positive")
        if not isinstance(state, TensorState):
            raise ValueError("state must be TensorState")
        for name, shape in (("w", (self.n, self.d)), ("c", (self.n,)), ("M", (self.n, self.n))):
            value = getattr(state, name)
            if not isinstance(value, torch.Tensor) or value.shape != shape or value.dtype != self.dtype or value.device != self.device:
                raise ValueError("invalid state tensor " + name)
            if not bool(torch.isfinite(value).all()):
                raise ValueError("nonfinite state " + name)
        return state

    def initial_state(self):
        return self.validate_state(self.initial).clone()

    def state(self, w, c, M):
        return self.validate_state(TensorState(*(self._tensor(v, copy=True) for v in (w,c,M))))

    def _fields(self, state, inputs):
        h1 = torch.tanh(state.w @ inputs.T)
        h2 = torch.tanh(state.M @ h1)
        return h1, h2, state.c @ h2 / self.n

    @torch.no_grad()
    def predict(self, state, inputs):
        self.validate_state(state)
        inputs = self._inputs(inputs)
        result = torch.cat([self._fields(state, inputs[j:j+self.block_size])[2]
                            for j in range(0, len(inputs), self.block_size)])
        if not bool(torch.isfinite(result).all()):
            raise ValueError("nonfinite prediction")
        return result

    @torch.no_grad()
    def rhs(self, state, data):
        self.validate_state(state)
        self._validate_data(data)
        vw, vc, vM = (torch.zeros_like(v) for v in (state.w, state.c, state.M))
        for start in range(0, len(data.inputs), self.block_size):
            stop = start+self.block_size
            u = data.inputs[start:stop]
            h1,h2,f = self._fields(state,u)
            r = data.probabilities[start:stop]*(f-data.labels[start:stop])
            delta2 = state.c[:,None]*(1-h2*h2)
            delta1 = (state.M.T @ delta2)*(1-h1*h1)
            vw.addmm_(delta1*r,u,alpha=-2)
            vc.addmv_(h2,r,alpha=-2)
            vM.addmm_(delta2*r,h1.T,alpha=-2/self.n)
        return self.validate_state(TensorState(vw,vc,vM))

    @torch.no_grad()
    def heun_step(self, state, data, step_size):
        if isinstance(step_size, (bool,np.bool_)) or not np.isfinite(float(step_size)) or float(step_size) <= 0:
            raise ValueError("step_size must be finite positive")
        h = float(step_size)
        k = self.rhs(state,data)
        stage = TensorState(*(getattr(state,a)+h*getattr(k,a) for a in ("w","c","M")))
        ell = self.rhs(stage,data)
        return self.validate_state(TensorState(*(getattr(state,a)+(h/2)*(getattr(k,a)+getattr(ell,a))
                                                for a in ("w","c","M"))))

    def evolve(self, state, data, *, steps, step_size):
        if isinstance(steps,bool) or not isinstance(steps,int) or steps < 0:
            raise ValueError("steps must be nonnegative integer")
        if isinstance(step_size,(bool,np.bool_)) or not np.isfinite(float(step_size)) or float(step_size) <= 0:
            raise ValueError("step_size must be finite positive")
        self.validate_state(state)
        self._validate_data(data)
        current = state.clone()
        for _ in range(steps):
            current = self.heun_step(current,data,step_size)
        return current

    @torch.no_grad()
    def observations(self, state, panel, *, probabilities=None):
        self.validate_state(state)
        inputs = self._inputs(panel)
        weights = self._probabilities(probabilities,len(inputs))
        h1,h2,f = self._fields(state,inputs)
        h10,h20,_ = self._fields(self.initial,inputs)
        result = {"prediction":f,"input_weights":weights.clone(),"inputs":inputs.clone()}
        for i,h0,h in ((1,h10,h1),(2,h20,h2)):
            result[f"pairs{i}"] = torch.stack((h0,h),dim=-1)
            result[f"population_weights{i}"] = torch.full((self.n,),1/self.n,dtype=self.dtype,device=self.device)
            result[f"rms{i}"] = torch.sqrt(torch.mean((h-h0).square(),dim=0) @ weights)
            for label,left,right in (("initial",h0,h0),("current",h,h),("cross",h0,h)):
                result[f"gram{i}_{label}"] = left.T @ right / self.n
        if not all(bool(torch.isfinite(v).all()) for v in result.values()):
            raise ValueError("nonfinite observations")
        return result

    @torch.no_grad()
    def loss(self,state,data):
        self._validate_data(data)
        result = data.probabilities @ (self.predict(state,data.inputs)-data.labels).square()
        if not bool(torch.isfinite(result)):
            raise ValueError("nonfinite loss")
        return result

    def retained_bytes(self,state):
        self.validate_state(state)
        return sum(v.numel()*v.element_size() for obj in (self.initial,state)
                   for v in (obj.w,obj.c,obj.M))
