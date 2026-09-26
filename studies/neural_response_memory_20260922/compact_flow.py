"""Dense gradient flow and the original residual-activity Legendre closure.

Fixed simultaneous Euler; inputs are already scaled as desired. Float32 is
explicitly the default. A custom activation is (phi, dphi), both acting on z;
a list supplies one activation per hidden layer. CUDA fit checks loss only at
block endpoints, so its stopping state is not the first fitted Euler state.
"""
import math
import time

import numpy as np
import torch


def _activation(spec, z, derivative=False):
    if not isinstance(spec, str):
        h = spec[0](z)
        return (h, spec[1](z)) if derivative else h
    if spec == "relu":
        h = z.relu()
        d = (z > 0).to(z.dtype) if derivative else None
    elif spec == "gelu":
        phi = .5*torch.erfc(-z/math.sqrt(2.))
        h = z*phi
        d = phi+z*torch.exp(-.5*z.square())/math.sqrt(2*math.pi) if derivative else None
    elif spec == "selu":
        scale, alpha = 1.0507009873554804934193349852946, 1.6732632423543772848170429916717
        h = torch.where(z > 0, scale*z, scale*alpha*torch.expm1(z.clamp_max(0)))
        d = torch.where(z > 0, torch.full_like(z, scale), scale*alpha*torch.exp(z.clamp_max(0))) if derivative else None
    elif spec == "tanh":
        h = z.tanh(); d = 1-h.square() if derivative else None
    elif spec == "sigmoid":
        h = z.sigmoid(); d = h*(1-h) if derivative else None
    elif spec == "silu":
        sigma = z.sigmoid(); h = z*sigma
        d = sigma+z*sigma*(1-sigma) if derivative else None
    else:
        raise ValueError("Unknown activation: "+spec)
    return (h, d) if derivative else h


class Flow:
    """Common-width, bias-free hidden layers and scalar c@h/n output.

    Dense state: [w, W1, ..., W(depth-1), c]. Closure state:
    [w, c, A1, B1, ..., A(depth-1), B(depth-1), s]. Closure matrices
    are immutable Gaussian initializers; s'=sqrt(MSE) and L=1+s.
    """
    @torch.no_grad()
    def __init__(self, inputs, labels, width=2048, depth=3, activation="relu",
                 order=None, seed=20260920, device="cuda:0", dtype=torch.float32,
                 normalization="none", norm_eps=1e-5, hidden_gain=1., readout_std=None):
        started = time.perf_counter()
        if any(isinstance(v, bool) or not isinstance(v, int) or v < 1 for v in (width, depth)):
            raise ValueError("width and depth must be positive integers")
        if order is not None and (isinstance(order, bool) or not isinstance(order, int) or order < 1):
            raise ValueError("order must be None or a positive integer")
        if dtype not in (torch.float32, torch.float64): raise ValueError("Use float32 or float64")
        self.n, self.depth, self.order = width, depth, order
        if normalization not in ("none", "before", "after"):
            raise ValueError("normalization must be none, before or after activation")
        if not math.isfinite(norm_eps) or norm_eps <= 0:
            raise ValueError("Positive finite LayerNorm epsilon required")
        self.normalization, self.norm_eps = normalization, norm_eps
        self.device, self.dtype = torch.device(device), dtype
        self.inputs = torch.as_tensor(inputs, dtype=dtype, device=device).detach().clone()
        self.labels = torch.as_tensor(labels, dtype=dtype, device=device).detach().clone()
        if self.inputs.ndim != 2 or min(self.inputs.shape) < 1 or self.labels.shape != (len(self.inputs),):
            raise ValueError("Expected inputs (M,d) and labels (M,)")
        if not bool(torch.isfinite(self.inputs).all() & torch.isfinite(self.labels).all()):
            raise ValueError("Training data must be finite")
        self.M = len(self.inputs)
        self.activations = list(activation) if isinstance(activation, list) else [activation]*depth
        if len(self.activations) != depth: raise ValueError("One activation per hidden layer required")
        for spec in self.activations:
            if isinstance(spec, str):
                if spec not in ("relu", "gelu", "selu", "tanh", "sigmoid", "silu"):
                    raise ValueError("Unknown activation: "+spec)
            elif not (isinstance(spec, tuple) and len(spec) == 2 and all(callable(f) for f in spec)):
                raise ValueError("Custom activation must be (value, derivative)")
        if hidden_gain == "unit_moment":
            nodes, weights = np.polynomial.hermite.hermgauss(128)
            z = torch.tensor(nodes*math.sqrt(2.), dtype=torch.float64)
            gains = []
            for spec in self.activations[:-1]:
                moment = float((_activation(spec,z).square()*torch.from_numpy(weights)).sum()/math.sqrt(math.pi))
                if not math.isfinite(moment) or moment <= 0:
                    raise ValueError("Activation needs a positive finite Gaussian second moment")
                gains.append(moment**-.5)
        else:
            gains = [float(hidden_gain)]*(depth-1)
        if any(not math.isfinite(g) or g <= 0 for g in gains):
            raise ValueError("Positive finite hidden initialization gain required")
        readout_std = 1/width if readout_std is None else float(readout_std)
        if not math.isfinite(readout_std) or readout_std <= 0:
            raise ValueError("Positive finite readout standard deviation required")
        self.hidden_gains, self.readout_std = gains, readout_std
        rng = np.random.default_rng(seed)
        tensor = lambda value: torch.tensor(value, dtype=dtype, device=device)
        self.w = tensor(rng.standard_normal((width, self.inputs.shape[1])))
        self.matrices = [tensor(rng.standard_normal((width,width))*g/math.sqrt(width)) for g in gains]
        draw = rng.standard_normal(width)
        self.c = tensor(draw/width if readout_std == 1/width else draw*readout_std)
        if order is None:
            self.state = [self.w, *self.matrices, self.c]
        else:
            self.degrees = torch.arange(order, dtype=dtype, device=device)[:,None,None]
            self.weights = 2*self.degrees+1
            self.moments = []
            h = self._layer(self.activations[0], self.w@self.inputs.T)[0]
            for i, matrix in enumerate(self.matrices):
                A = h.new_zeros((order,width,self.M)); B = torch.zeros_like(A); B[0] = h
                self.moments.extend((A,B))
                h = self._layer(self.activations[i+1], matrix@h)[0]
            self.s = self.w.new_zeros(())
            self.state = [self.w, self.c, *self.moments, self.s]
        self.setup_seconds = time.perf_counter()-started

    @staticmethod
    def _columns(value):
        return value.permute(1,0,2).reshape(value.shape[1],-1)

    def _factors(self):
        if self.order is None: return None
        return [((-2/(self.M*self.n))*self._columns(self.weights*A), self._columns(B/(1+self.s)))
                for A,B in zip(self.moments[::2],self.moments[1::2])]

    def _apply(self, index, values, factors, transpose=False):
        matrix = self.matrices[index]
        result = (matrix.T if transpose else matrix)@values
        if factors is not None:
            left,right = factors[index]
            if transpose: left,right = right,left
            result = result+left@(right.T@values)
        return result

    def _normalize(self, z):
        centered = z-z.mean(dim=0, keepdim=True)
        inverse = (centered.square().mean(dim=0, keepdim=True)+self.norm_eps).rsqrt()
        return centered*inverse, inverse

    def _layer(self, spec, z, derivatives=False):
        # LayerNorm is per sample, across neurons, with no affine parameters.
        if self.normalization == "before":
            u, inverse = self._normalize(z)
            result = _activation(spec, u, derivatives)
        else:
            result = _activation(spec, z, derivatives)
        h, d = result if derivatives else (result, None)
        if self.normalization == "after":
            h, inverse = self._normalize(h); u = h
        cache = (d, u, inverse) if derivatives and self.normalization != "none" else d
        return h, cache

    def _backward_layer(self, cache, gradient):
        if self.normalization == "none": return cache*gradient
        d, u, inverse = cache
        if self.normalization == "before": gradient = d*gradient
        gradient = inverse*(gradient-gradient.mean(dim=0, keepdim=True)
                            -u*(u*gradient).mean(dim=0, keepdim=True))
        return gradient if self.normalization == "before" else d*gradient

    def _forward(self, inputs, factors, derivatives=False):
        hidden, slopes = [], []
        z = self.w@inputs.T
        for i, spec in enumerate(self.activations):
            if i: z = self._apply(i-1, hidden[-1], factors)
            h, cache = self._layer(spec,z,derivatives)
            if derivatives: slopes.append(cache)
            hidden.append(h)
        return hidden, slopes

    @torch.no_grad()
    def predict(self, inputs):
        inputs = torch.as_tensor(inputs,dtype=self.dtype,device=self.device)
        if inputs.ndim != 2 or inputs.shape[1] != self.w.shape[1]: raise ValueError("Wrong query shape")
        hidden,_ = self._forward(inputs,self._factors())
        return self.c@hidden[-1]/self.n

    def _transport(self, moments, source, rho):
        if self.order == 1: return source[None]
        weighted = self.weights*moments
        lower = torch.cat((torch.zeros_like(weighted[:1]),weighted[:-1].cumsum(dim=0)),dim=0)
        return source[None]-(rho/(1+self.s))*(self.degrees*moments+lower)

    @torch.no_grad()
    def rhs(self):
        factors = self._factors()  # Shared by every forward/transpose use this RHS.
        hidden, slopes = self._forward(self.inputs,factors,True)
        residual = self.c@hidden[-1]/self.n-self.labels
        self.loss = residual.square().mean()
        delta = [None]*self.depth
        delta[-1] = self._backward_layer(slopes[-1],self.c[:,None])
        for i in range(self.depth-2,-1,-1):
            delta[i] = self._backward_layer(slopes[i],self._apply(i,delta[i+1],factors,True))
        dw = (-2/self.M)*(delta[0]*residual)@self.inputs
        dc = (-2/self.M)*(hidden[-1]@residual)
        if self.order is None:
            return [dw, *((-2/(self.M*self.n))*(delta[i+1]*residual)@hidden[i].T
                          for i in range(self.depth-1)), dc]
        rho = self.loss.sqrt()
        velocities = [dw,dc]
        for i in range(self.depth-1):
            A,B = self.moments[2*i:2*i+2]
            velocities.extend((self._transport(A,delta[i+1]*residual,rho),
                               self._transport(B,rho*hidden[i],rho)))
        return [*velocities,rho.clone()]

    @torch.no_grad()
    def step(self, dt):
        if not math.isfinite(dt) or dt <= 0: raise ValueError("Positive finite step required")
        velocities = self.rhs()
        for value, velocity in zip(self.state,velocities): value.add_(velocity,alpha=dt)

    @torch.no_grad()
    def fit(self, step=.0625, target_rms=.05, max_seconds=120., max_steps=20000, block=32):
        """Fixed Euler, one host loss read per block; capture time counts in budget.

        CUDA captures full updates, restoring all state after warmup/capture.
        The last partial block runs eagerly. No clipping, retries or adaptation.
        """
        if any(not math.isfinite(v) or v <= 0 for v in (step,target_rms,max_seconds)):
            raise ValueError("Step, target and seconds must be positive and finite")
        if any(isinstance(v,bool) or not isinstance(v,int) or v < 1 for v in (max_steps,block)):
            raise ValueError("max_steps and block must be positive integers")
        started = time.perf_counter(); updates = 0; capture_seconds = 0.; graph = None
        loss = lambda: (self.predict(self.inputs)-self.labels).square().mean()
        rms = float(loss().sqrt().cpu())
        length = min(block,max_steps)
        def advance(count):
            for _ in range(count): self.step(step)
            return loss()
        if self.device.type == "cuda" and math.isfinite(rms) and rms > target_rms:
            capture_start = time.perf_counter()
            backup = [value.clone() for value in self.state]
            with torch.cuda.device(self.device):
                stream = torch.cuda.Stream(device=self.device)
                stream.wait_stream(torch.cuda.current_stream(self.device))
                try:
                    with torch.cuda.stream(stream): advance(2)
                    torch.cuda.current_stream(self.device).wait_stream(stream)
                    for value, saved in zip(self.state,backup): value.copy_(saved)
                    torch.cuda.synchronize(self.device)
                    graph = torch.cuda.CUDAGraph()
                    with torch.cuda.graph(graph,stream=stream): captured_loss = advance(length)
                finally:
                    torch.cuda.synchronize(self.device)
                    for value, saved in zip(self.state,backup): value.copy_(saved)
                    torch.cuda.synchronize(self.device)
            capture_seconds = time.perf_counter()-capture_start
        loop_start = time.perf_counter()
        while True:
            if not math.isfinite(rms): status="nonfinite"; break
            if rms <= target_rms: status="target_rms"; break
            if updates >= max_steps: status="max_steps"; break
            if time.perf_counter()-started >= max_seconds: status="wall_limit"; break
            count = min(length,max_steps-updates)
            if graph is not None and count == length:
                graph.replay(); value = captured_loss
            else: value = advance(count)
            rms = float(value.sqrt().cpu()); updates += count
        return dict(rms=rms,steps=updates,seconds=time.perf_counter()-started,status=status,
                    physical_time=updates*step,step=step,block=block,dtype=str(self.dtype),
                    capture_seconds=capture_seconds,loop_seconds=time.perf_counter()-loop_start,
                    setup_seconds=self.setup_seconds)
