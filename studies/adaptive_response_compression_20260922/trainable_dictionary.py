"""Study-only gradient flow with trainable dictionary population vectors."""
from dataclasses import dataclass
import torch

NAMES = ("w", "c", "M", "b1", "b2")


@dataclass
class State:
    w: torch.Tensor
    c: torch.Tensor
    M: torch.Tensor
    b1: torch.Tensor
    b2: torch.Tensor

    def clone(self):
        return State(*(getattr(self, k).clone() for k in NAMES))

    def numpy(self):
        return {k: getattr(self, k).detach().cpu().numpy().copy() for k in NAMES}


def validate(state):
    n = state.w.shape[0]
    if state.w.shape != (n, 2) or state.c.shape != (n,):
        raise ValueError("bad read-in/readout shapes")
    if state.b1.shape[0] != n or state.b2.shape[0] != n:
        raise ValueError("bad population shapes")
    if state.M.shape != (state.b2.shape[1], state.b1.shape[1]):
        raise ValueError("bad middle shape")
    if any(not bool(torch.isfinite(getattr(state, k)).all()) for k in NAMES):
        raise ValueError("nonfinite state")


def forward(state, inputs):
    n = len(state.c)
    h = torch.tanh(state.w @ inputs.T)
    a = state.b1.T @ h / n
    v = state.M @ a
    H = torch.tanh(state.b2 @ v)
    f = state.c @ H / n
    return {"h": h, "a": a, "v": v, "H": H, "f": f}


def predict(state, inputs, block_size=256):
    return torch.cat([forward(state, block)["f"] for block in inputs.split(block_size)])


def loss(state, inputs, labels, probabilities=None):
    residual = forward(state, inputs)["f"] - labels
    return residual.square().mean() if probabilities is None else probabilities @ residual.square()


def rhs(state, inputs, labels, probabilities=None, *, train_basis=True):
    n = len(state.c)
    f = forward(state, inputs)
    h, a, v, H = (f[k] for k in ("h", "a", "v", "H"))
    weighted_r = f["f"] - labels
    weighted_r = weighted_r / len(labels) if probabilities is None else weighted_r * probabilities
    delta = state.c[:, None] * (1 - H.square())
    d = state.b2.T @ delta / n
    s = state.M.T @ d
    q = state.b1 @ s
    dw = -2 * (((1 - h.square()) * q) * weighted_r) @ inputs
    dc = -2 * (H @ weighted_r)
    dM = -2 * (d * weighted_r) @ a.T
    db1 = -2 * (h * weighted_r) @ s.T if train_basis else torch.zeros_like(state.b1)
    db2 = -2 * (delta * weighted_r) @ v.T if train_basis else torch.zeros_like(state.b2)
    return State(dw, dc, dM, db1, db2)


def add(state, velocity, scale):
    return State(*(getattr(state, k) + scale * getattr(velocity, k) for k in NAMES))


def blend(left, right, fraction):
    return State(*(getattr(left, k) + fraction * (getattr(right, k) - getattr(left, k))
                   for k in NAMES))


@torch.no_grad()
def heun_trial(state, inputs, labels, step, initial_M, rtol, atol, *, train_basis=True):
    k = rhs(state, inputs, labels, train_basis=train_basis)
    euler = add(state, k, step)
    ell = rhs(euler, inputs, labels, train_basis=train_basis)
    candidate = State(*(getattr(state, name) + .5 * step *
                        (getattr(k, name) + getattr(ell, name)) for name in NAMES))
    validate(candidate)
    ratios = []
    for name in ("w", "c"):
        x, y, z = (getattr(s, name) for s in (state, euler, candidate))
        scale = atol + rtol * torch.maximum(x.square().mean().sqrt(), z.square().mean().sqrt())
        ratios.append((z - y).square().mean().sqrt() / scale)
    middle_scale = atol + rtol * torch.maximum(
        (state.M - initial_M).norm(), (candidate.M - initial_M).norm()).clamp_min(1)
    ratios.append((candidate.M - euler.M).norm() / middle_scale)
    if train_basis:
        for name in ("b1", "b2"):
            x, y, z = (getattr(s, name) for s in (state, euler, candidate))
            scale = atol + rtol * torch.maximum(x.square().mean(0).sqrt(), z.square().mean(0).sqrt())
            ratios.append(((z - y).square().mean(0).sqrt() / scale).max())
    return candidate, float(torch.stack(ratios).max())
