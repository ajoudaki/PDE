"""Experimental execution-only acceleration; frozen producers are untouched.

FastActivationTrial(engine, cuda_graph=False).trial(state, dt, rtol, atol)
returns first, second, euler, candidate, error, loss, valid. The original
combine/add_(alpha=Python_float) operations stay outside optional CUDA graphs.
Graph first/second outputs are borrowed until the next trial; consume them for
event interpolation before replaying. Euler/candidate states are fresh.
No solver decisions, fitting, event rules, or wall caps are implemented here.
"""

import copy
import math

import torch

from activation_moment_engine import ActivationDenseEngine, ActivationMomentEngine
from deep_moment_engine import combine, tensor_rms
from moment_engine import factor_action


class FastActivationMomentEngine(ActivationMomentEngine):
    """Opt-in batched fixed-matrix/vector kernel; float64 reduction order differs.

    Initialization is inherited exactly. Only training-sized products change
    kernel; other query widths retain the frozen matrix multiplication.
    """

    def _apply(self, state, layer, values, transpose=False):
        matrix = getattr(self, "W"+str(layer)+"0")
        matrix = matrix.T if transpose else matrix
        fixed = (torch.bmm(matrix.expand(self.M,-1,-1),values.T.unsqueeze(-1)).squeeze(-1).T
                 if values.shape[1] == self.M else matrix @ values)
        return fixed + factor_action(*self.delta_factors(state,layer),values,transpose=transpose)


@torch.no_grad()
def controlled_error_tensor(engine, current, euler, candidate, rtol, atol):
    """Frozen physical error arithmetic, returning its scalar on the device."""
    ratios = []
    for name in current.names():
        if name in ("W2", "W3"):
            continue
        a,b,c = (getattr(state,name) for state in (current,euler,candidate))
        scale = torch.maximum(tensor_rms(a),tensor_rms(c)).clamp_min(1)
        ratios.append(tensor_rms(c-b)/(atol+rtol*scale))
    for layer in (2,3):
        scale = torch.maximum(engine.hidden_increment_norm(current,layer),
                              engine.hidden_increment_norm(candidate,layer))/math.sqrt(engine.n)
        error = engine.hidden_difference_norm(candidate,euler,layer)/math.sqrt(engine.n)
        ratios.append(error/(atol+rtol*scale.clamp_min(1)))
    return torch.stack(ratios).max()


@torch.no_grad()
def packed_status(engine, current, euler, candidate, rtol, atol):
    error = controlled_error_tensor(engine,current,euler,candidate,rtol,atol)
    loss = (engine.predict(candidate,engine.inputs)-engine.labels).square().mean()
    checks = [torch.isfinite(value).all() for value in candidate.tensors()]
    if engine.moment:
        checks.extend(state.s >= 0 for state in (current,euler,candidate))
    state_valid = torch.stack(checks).all().to(dtype=engine.dtype)
    return torch.stack((error,loss,state_valid))


class FastActivationTrial:
    """Three optional captures and one packed device-to-host status transfer.

    The private shallow engine view shares immutable constants, replaces only
    its validation callback, and leaves all physical arithmetic inherited.
    Initialization is fully checked; shapes/dtype/device are checked at every
    public trial boundary. Dynamic finite/activity checks stay in packed_status.
    CUDA graph tolerances freeze on prepare() or the first trial.
    """

    def __init__(self, engine, *, cuda_graph=False, rtol=None, atol=None, warmup=3):
        if not isinstance(engine,(ActivationDenseEngine,ActivationMomentEngine)):
            raise TypeError("an activation dense or moment engine is required")
        if engine.dtype != torch.float64:
            raise ValueError("this experiment retains float64")
        if cuda_graph and engine.device.type != "cuda":
            raise ValueError("CUDA graphs require an explicitly selected CUDA device")
        if not isinstance(warmup,int) or isinstance(warmup,bool) or warmup < 1:
            raise ValueError("warmup must be a positive integer")
        self.engine, self.cuda_graph, self.warmup = engine, bool(cuda_graph), warmup
        self.view = copy.copy(engine)
        self.view.validate_state = lambda state, finite=True: state
        template = engine.initial_state()
        engine.validate_state(template)
        self.state_type = type(template)
        self.metadata = tuple((name,value.shape,value.dtype,value.device)
                              for name,value in zip(template.names(),template.tensors()))
        self.controls = None
        if self.cuda_graph:
            self.current_buffer = template
            self.euler_buffer = template.clone()
            self.candidate_buffer = template.clone()
        if rtol is not None or atol is not None:
            if rtol is None or atol is None:
                raise ValueError("provide both rtol and atol")
            self.prepare(rtol,atol)

    def validate_metadata(self, state):
        if type(state) is not self.state_type:
            raise ValueError("state type differs from the prepared engine")
        for name,shape,dtype,device in self.metadata:
            value = getattr(state,name)
            if value.shape != shape or value.dtype != dtype or value.device != device:
                raise ValueError("state metadata mismatch: "+name)

    @staticmethod
    def _copy_state(destination, source):
        for target,value in zip(destination.tensors(),source.tensors()):
            target.copy_(value)

    def _capture(self, operation):
        device = self.engine.device
        with torch.cuda.device(device):
            stream = torch.cuda.Stream(device=device)
            stream.wait_stream(torch.cuda.current_stream(device))
            with torch.cuda.stream(stream):
                for _ in range(self.warmup):
                    operation()
            torch.cuda.current_stream(device).wait_stream(stream)
            torch.cuda.synchronize(device)
            graph = torch.cuda.CUDAGraph()
            with torch.cuda.graph(graph,stream=stream):
                output = operation()
            torch.cuda.synchronize(device)
        return graph,output

    @torch.no_grad()
    def prepare(self, rtol, atol):
        controls = (float(rtol),float(atol))
        if not all(math.isfinite(value) and value > 0 for value in controls):
            raise ValueError("tolerances must be finite and positive")
        if self.controls == controls:
            return
        if self.cuda_graph and self.controls is not None:
            raise ValueError("captured tolerances are fixed; prepare a separate trial object")
        self.controls = controls
        if self.cuda_graph:
            self.first_graph = self._capture(lambda:self.view.rhs(self.current_buffer))
            self.second_graph = self._capture(lambda:self.view.rhs(self.euler_buffer))
            self.status_graph = self._capture(lambda:packed_status(
                self.view,self.current_buffer,self.euler_buffer,self.candidate_buffer,*controls))

    @torch.no_grad()
    def trial(self, state, dt, rtol, atol):
        self.validate_metadata(state)
        if not isinstance(dt,(int,float)) or isinstance(dt,bool) or not math.isfinite(dt) or dt <= 0:
            raise ValueError("step must be a positive finite Python scalar")
        self.prepare(rtol,atol)
        if self.cuda_graph:
            self._copy_state(self.current_buffer,state)
            self.first_graph[0].replay()
            first = self.first_graph[1]
        else:
            first = self.view.rhs(state)
        euler = combine((1.,dt),(state,first))
        if self.cuda_graph:
            self._copy_state(self.euler_buffer,euler)
            self.second_graph[0].replay()
            second = self.second_graph[1]
        else:
            second = self.view.rhs(euler)
        candidate = combine((1.,dt/2,dt/2),(state,first,second))
        if self.cuda_graph:
            self._copy_state(self.candidate_buffer,candidate)
            self.status_graph[0].replay()
            packed = self.status_graph[1]
        else:
            packed = packed_status(self.view,state,euler,candidate,*self.controls)
        error,loss,state_valid = packed.detach().cpu().tolist()
        # The frozen runner converts a failed state/activity check to inf error.
        if not state_valid:
            error = float("inf")
        valid = bool(state_valid) and math.isfinite(error) and math.isfinite(loss)
        return first,second,euler,candidate,error,loss,valid
