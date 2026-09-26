"""Direct Euclidean factor GF for W2=W0+A@B; W0 is fixed.

For unhalved probability MSE, G=dL/dW2=2*q@h1.T/(S*n),
q=c[:,None]*(1-h2**2)*(f-y). Thus A'=-G@B.T, B'=-A.T@G,
and (AB)'=-G@B.T@B-A@A.T@G. Outer mobilities are n; both
factor mobilities are one. No dense correction or dense gradient is formed.
"""
from dataclasses import dataclass
from numbers import Integral
import numpy as np
import torch
from moment_engine import factor_frobenius


@dataclass
class FactorState:
    w: torch.Tensor
    c: torch.Tensor
    A: torch.Tensor
    B: torch.Tensor

    @staticmethod
    def names():
        return ("w", "c", "A", "B")

    def tensors(self):
        return tuple(getattr(self, name) for name in self.names())

    def clone(self):
        return FactorState(*(x.clone() for x in self.tensors()))

    def add_scaled(self, velocity, step):
        return FactorState(*(x + step*y for x, y in zip(self.tensors(), velocity.tensors())))


def blend(left, right, fraction):
    return FactorState(*(a + fraction*(b-a) for a, b in zip(left.tensors(), right.tensors())))


class FactorEngine:
    def __init__(self, d, width, rank, inputs, labels, *, seed=20260920,
                 factor_seed=20260924, device="cpu", dtype=torch.float64):
        for name, value in (("d", d), ("width", width), ("rank", rank)):
            if isinstance(value, bool) or not isinstance(value, Integral) or value < 1:
                raise ValueError(name + " must be a positive integer")
        self.d, self.n, self.rank = d, width, rank
        self.device, self.dtype = torch.device(device), dtype
        self.inputs, self.labels = self.tensor(inputs), self.tensor(labels)
        self.S = len(self.inputs)
        if self.inputs.shape != (self.S, d) or not self.S or self.labels.shape != (self.S,):
            raise ValueError("expected nonempty inputs(S,d), labels(S)")
        rng = np.random.default_rng(seed)
        w = self.tensor(rng.standard_normal((width, d)))
        self.W0 = self.tensor(rng.standard_normal((width, width))/np.sqrt(width))
        c = self.tensor(rng.standard_normal(width)/width)
        # Standardized row directions have identical prefixes at every rank.
        B = self.tensor(np.random.default_rng(factor_seed).standard_normal((rank, width))/np.sqrt(rank))
        self.initial = FactorState(w, c, torch.zeros((width, rank), device=device, dtype=dtype), B)

    def tensor(self, value):
        return torch.as_tensor(value, device=self.device, dtype=self.dtype).detach().clone()

    def initial_state(self):
        return self.initial.clone()

    def validate_state(self, state):
        shapes = ((self.n, self.d), (self.n,), (self.n, self.rank), (self.rank, self.n))
        for name, value, shape in zip(state.names(), state.tensors(), shapes):
            if value.shape != shape or value.device != self.device or value.dtype != self.dtype:
                raise ValueError("invalid shape/device/dtype: " + name)
            if not bool(torch.isfinite(value).all()):
                raise ValueError("nonfinite state: " + name)

    def apply_hidden(self, state, values, *, transpose=False):
        if transpose:
            return self.W0.T @ values + state.B.T @ (state.A.T @ values)
        return self.W0 @ values + state.A @ (state.B @ values)

    def fields(self, state):
        h1 = torch.tanh(state.w @ self.inputs.T)
        h2 = torch.tanh(self.apply_hidden(state, h1))
        residual = state.c @ h2/self.n-self.labels
        q = state.c[:, None]*(1-h2.square())*residual
        return h1, h2, residual, q

    @torch.no_grad()
    def predict(self, state, inputs):
        h1 = torch.tanh(state.w @ self.tensor(inputs).T)
        return state.c @ torch.tanh(self.apply_hidden(state, h1))/self.n

    @torch.no_grad()
    def loss(self, state):
        return self.fields(state)[2].square().mean()

    @torch.no_grad()
    def rhs(self, state):
        h1, h2, residual, q = self.fields(state)
        back = self.apply_hidden(state, q, transpose=True)*(1-h1.square())
        scale = -2/(self.S*self.n)
        return FactorState((-2/self.S)*back @ self.inputs, (-2/self.S)*(h2 @ residual),
                           scale*q @ (state.B @ h1).T, scale*(state.A.T @ q) @ h1.T)


def error_ratio(current, euler, candidate, rtol, atol):
    """Raw-coordinate RMS errors plus physical ||DeltaW_Heun-DeltaW_Euler||F."""
    rms = lambda value: value.square().mean().sqrt()
    ratios = [rms(c-b)/(atol+rtol*torch.maximum(rms(a), rms(c)).clamp_min(1.))
              for a, b, c in zip(current.tensors(), euler.tensors(), candidate.tensors())]
    numerator = factor_frobenius(torch.cat((candidate.A-euler.A, euler.A), 1),
                                 torch.cat((candidate.B.T, (candidate.B-euler.B).T), 1))
    scale = torch.maximum(factor_frobenius(current.A, current.B.T),
                          factor_frobenius(candidate.A, candidate.B.T)).clamp_min(1.)
    return float(torch.stack(ratios+[numerator/(atol+rtol*scale)]).max())


@torch.no_grad()
def heun_trial(engine, state, step, rtol, atol):
    first = engine.rhs(state)
    euler = state.add_scaled(first, step)
    second = engine.rhs(euler)
    candidate = FactorState(*(x+.5*step*(a+b) for x, a, b in
                              zip(state.tensors(), first.tensors(), second.tensors())))
    return candidate, error_ratio(state, euler, candidate, rtol, atol)
