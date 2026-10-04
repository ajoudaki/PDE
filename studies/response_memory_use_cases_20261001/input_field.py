"""Input-function response memories; baseline is immutable and imported locally."""
import math
import numpy as np
import torch
from baseline_compact_flow import Flow, LowRankFlow


def circle(theta):
    # Flow already consumes x/sqrt(d). Canonical raw circle inputs are
    # sqrt(2)*(cos(theta),sin(theta)), so these API rows have unit norm.
    return torch.stack((theta.cos(), theta.sin()), dim=-1)


def teacher(theta, name):
    if name == 'A': return theta.sin()+.5*(3*theta).sin()
    if name == 'B': return (3*theta).sin()+.3*(5*theta).cos()
    raise ValueError(name)


def fourier(theta, count):
    if count < 1 or count % 2 != 1: raise ValueError('positive odd count required')
    values = [torch.ones_like(theta)]
    for k in range(1, (count+1)//2):
        values.extend((math.sqrt(2)*(k*theta).cos(), math.sqrt(2)*(k*theta).sin()))
    return torch.stack(values, dim=-1)


def grid(count, device='cpu', dtype=torch.float64):
    return 2*math.pi*torch.arange(count, device=device, dtype=dtype)/count


class InputFieldFlow(Flow):
    """Moments have (time mode, neuron, input function) axes.

    `prefix_inputs` and `prefix_basis` are initialization quadrature, not state.
    Current input/label/basis arrays are replaced, never appended, on a stream.
    """
    @torch.no_grad()
    def __init__(self, inputs, labels, basis, *, prefix_inputs=None,
                 prefix_basis=None, order=3, **kwargs):
        super().__init__(inputs, labels, order=None, **kwargs)
        if self.normalization != 'none': raise ValueError('uncoupled network required')
        self.c.zero_()
        self.order = order
        self.basis = torch.as_tensor(basis, device=self.device, dtype=self.dtype).clone()
        self.C = self.basis.shape[1]
        self.degrees = torch.arange(order, device=self.device, dtype=self.dtype)[:, None, None]
        self.weights = 2*self.degrees+1
        px = self.inputs if prefix_inputs is None else torch.as_tensor(prefix_inputs, device=self.device, dtype=self.dtype)
        pp = self.basis if prefix_basis is None else torch.as_tensor(prefix_basis, device=self.device, dtype=self.dtype)
        hidden, _ = self._forward(px, None)
        self.moments = []
        for h in hidden[:-1]:
            A = h.new_zeros((order, self.n, self.C)); B = torch.zeros_like(A)
            B[0] = (h@pp)/len(px)
            self.moments.extend((A, B))
        self.s = self.w.new_zeros(())
        self.state = [self.w, self.c, *self.moments, self.s]

    def _factors(self):
        return [((-2/self.n)*self._columns(self.weights*A), self._columns(B/(1+self.s)))
                for A, B in zip(self.moments[::2], self.moments[1::2])]

    @torch.no_grad()
    def set_batch(self, inputs, labels, basis):
        self.inputs, self.labels, self.basis = inputs, labels, basis
        self.M = len(inputs)

    @torch.no_grad()
    def rhs(self):
        hidden, backward, residual, _ = self._loss_fields()
        self.loss = residual.square().mean(); rho = self.loss.sqrt()
        velocities = [(-2/self.M)*backward[0]@self.inputs,
                      (-2/self.M)*(hidden[-1]@residual)]
        for i in range(self.depth-1):
            A, B = self.moments[2*i:2*i+2]
            velocities.extend((self._transport(A, (backward[i+1]@self.basis)/self.M, rho),
                               self._transport(B, rho*(hidden[i]@self.basis)/self.M, rho)))
        return [*velocities, rho.clone()]


class ControlledFlow(Flow):
    def __init__(self, *args, control='dense', **kwargs):
        super().__init__(*args, **kwargs); self.c.zero_(); self.control = control

    @torch.no_grad()
    def rhs(self):
        velocities = super().rhs()
        if self.control == 'readout':
            for v in velocities[:-1]: v.zero_()
        elif self.control == 'frozen_internal':
            for v in velocities[1:-1]: v.zero_()
        elif self.control != 'dense': raise ValueError(self.control)
        return velocities


@torch.no_grad()
def set_batch(model, theta, labels, count=None):
    x = circle(theta)
    if isinstance(model, InputFieldFlow): model.set_batch(x, labels, fourier(theta, count or model.C))
    else:
        model.inputs, model.labels = x, labels
        model.M = len(x)


@torch.no_grad()
def internal_matrix(model):
    factors = model._factors()
    if factors is None: return model.matrices[0].clone()
    return model.matrices[0]+factors[0][0]@factors[0][1].T


@torch.no_grad()
def make_model(kind, *, n, seed, device, dtype, theta, name, count=9, order=3, prefix_nodes=256):
    kwargs = dict(width=n, depth=2, activation='tanh', seed=seed,
                  device=device, dtype=dtype, hidden_gain=1., readout_std=1.)
    x, y = circle(theta), teacher(theta, name)
    if kind == 'field':
        pt = grid(prefix_nodes, device, dtype)
        return InputFieldFlow(x, y, fourier(theta, count), prefix_inputs=circle(pt),
                              prefix_basis=fourier(pt, count), order=order, **kwargs)
    if kind == 'sample':
        model = Flow(x, y, order=order, **kwargs); model.c.zero_(); return model
    if kind == 'low_rank':
        model = LowRankFlow(x, y, rank=count*order, factor_seed=seed+10000, **kwargs)
        model.c.zero_(); return model
    return ControlledFlow(x, y, control=kind, **kwargs)
