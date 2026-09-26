"""Study-local rational activity-bin moment closure for equalwidth2 tanh.

Inputs are rows U=x/sqrt(d), loss is mean((f-y)**2), and f=c@h2/n.
The only dense n-by-n array retained by this engine is the fixed initial W0.
Learned hidden weights and their velocities are applied through factors.
With ``lifted=True``, all RHS arithmetic is rational on rho>0, C>0, s>-1;
tanh and square root are used only for initialization/query/diagnostics.
The rho=0 boundary has the explicitly prescribed zero vector field.
"""

from dataclasses import dataclass, fields as dataclass_fields
from math import sqrt
from numbers import Integral

import numpy as np
import torch


@dataclass
class MomentState:
    w: torch.Tensor
    c: torch.Tensor
    A: torch.Tensor
    B: torch.Tensor
    C: torch.Tensor
    s: torch.Tensor
    h1: torch.Tensor | None = None
    h2: torch.Tensor | None = None
    rho: torch.Tensor | None = None

    @property
    def lifted(self):
        return self.h1 is not None

    def names(self):
        return tuple(f.name for f in dataclass_fields(self) if getattr(self, f.name) is not None)

    def tensors(self):
        return tuple(getattr(self, name) for name in self.names())

    def clone(self):
        return MomentState(**{name: getattr(self, name).clone() for name in self.names()})

    def add_scaled(self, other, scale):
        return linear_combination((1.0, scale), (self, other))


def linear_combination(coefficients, states):
    """Return sum(coefficients[i]*states[i]); no input is mutated."""
    coefficients, states = tuple(coefficients), tuple(states)
    if not states or len(coefficients) != len(states):
        raise ValueError("provide equally many nonempty coefficients and states")
    names = states[0].names()
    if any(state.names() != names for state in states):
        raise ValueError("states must have matching components")
    return MomentState(**{
        name: sum((coefficient * getattr(state, name)
                   for coefficient, state in zip(coefficients, states)),
                  torch.zeros_like(getattr(states[0], name)))
        for name in names
    })


def factor_action(left, right, values, *, transpose=False):
    """Apply left@right.T (or its transpose) without its dense product."""
    if transpose:
        left, right = right, left
    return left @ (right.T @ values)


def factor_frobenius(left, right, *, block_size=128):
    """Frobenius norm of left@right.T through blocked Gram contractions.

    Temporary Gram arrays are at most block_size squared; this never forms
    an n-by-n product. A final zero clamp handles roundoff in the Gram sum.
    """
    if left.ndim != 2 or right.ndim != 2 or left.shape[1] != right.shape[1]:
        raise ValueError("factors must be matrices with matching column counts")
    if not isinstance(block_size, Integral) or isinstance(block_size, bool) or block_size < 1:
        raise ValueError("block_size must be positive")
    total = left.new_zeros(())
    rank = left.shape[1]
    for i in range(0, rank, block_size):
        li, ri = left[:, i:i+block_size], right[:, i:i+block_size]
        for j in range(0, i+1, block_size):
            lj, rj = left[:, j:j+block_size], right[:, j:j+block_size]
            term = ((li.T @ lj) * (ri.T @ rj)).sum()
            total = total + (term if i == j else 2 * term)
    return torch.sqrt(torch.clamp(total, min=0))


class MomentEngine:
    """Owned uniform training data and canonical NumPy Gaussian initialization.

    ``inputs`` has shape (M,d) and already includes 1/sqrt(d). ``bins`` is
    the predeclared P; eta is always 1e-3/P**6. Moving state dimension is
    nd+n+2PnM+P+1, plus 2nM+1 for the rational response lift.
    """

    def __init__(self, d, width, bins, inputs, labels, *, seed=20260920,
                 device="cpu", dtype=torch.float64, lifted=False):
        for name, value in (("d", d), ("width", width), ("bins", bins)):
            if isinstance(value, bool) or not isinstance(value, Integral) or value < 1:
                raise ValueError(name + " must be a positive integer")
        if isinstance(seed, bool) or not isinstance(seed, Integral) or seed < 0:
            raise ValueError("seed must be a nonnegative integer")
        if dtype not in (torch.float32, torch.float64):
            raise ValueError("dtype must be float32 or float64")
        self.d, self.n, self.P = int(d), int(width), int(bins)
        self.device, self.dtype = torch.device(device), dtype
        self.lifted = bool(lifted)
        self.eta = 1e-3 / self.P**6
        self.inputs, self.labels = self._tensor(inputs), self._tensor(labels)
        if self.inputs.ndim != 2 or self.inputs.shape[1] != self.d or not len(self.inputs):
            raise ValueError("inputs must have shape (M,d), M positive")
        self.M = len(self.inputs)
        if self.labels.shape != (self.M,):
            raise ValueError("labels must have shape (M,)")
        self.centers = (torch.arange(self.P, dtype=dtype, device=self.device)+0.5)/self.P
        # Identical draws and order to pde.finite_network.initialize(n,2,d).
        rng = np.random.default_rng(int(seed))
        w = self._tensor(rng.standard_normal((self.n, self.d)))
        self.W0 = self._tensor(rng.standard_normal((self.n, self.n))/sqrt(self.n))
        c = self._tensor(rng.standard_normal(self.n)/self.n)
        h10 = torch.tanh(w @ self.inputs.T)
        h20 = torch.tanh(self.W0 @ h10)
        r0 = c @ h20/self.n-self.labels
        rho0 = torch.sqrt(r0.square().mean())
        self.h10 = h10.clone()
        self.q0 = (c[:, None]*(1-h20.square())*r0/rho0
                   if bool(rho0 > 0) else torch.zeros_like(h20))
        self.initial = MomentState(
            w, c, torch.zeros((self.P, self.n, self.M), dtype=dtype, device=self.device),
            self.eta*h10[None].expand(self.P, -1, -1).clone(),
            torch.full((self.P,), self.eta, dtype=dtype, device=self.device),
            torch.zeros((), dtype=dtype, device=self.device),
            h10 if lifted else None, h20 if lifted else None, rho0 if lifted else None,
        )
        self._constant_tensors = (self.inputs, self.labels, self.W0, self.centers,
                                  self.h10, self.q0, *self.initial.tensors())
        self._constant_versions = tuple((id(x), x._version) for x in self._constant_tensors)

    def _tensor(self, value):
        result = torch.as_tensor(value, dtype=self.dtype, device=self.device).detach().clone()
        if not bool(torch.isfinite(result).all()):
            raise ValueError("all input values must be finite")
        return result

    def validate_state(self, state):
        if tuple((id(x), x._version) for x in self._constant_tensors) != self._constant_versions:
            raise ValueError("engine constants or initial state were mutated")
        if not isinstance(state, MomentState) or state.lifted != self.lifted:
            raise ValueError("state lift must match engine")
        expected = {"w": (self.n, self.d), "c": (self.n,),
                    "A": (self.P, self.n, self.M), "B": (self.P, self.n, self.M),
                    "C": (self.P,), "s": ()}
        if self.lifted:
            expected.update(h1=(self.n, self.M), h2=(self.n, self.M), rho=())
        if state.names() != tuple(expected):
            raise ValueError("invalid state components")
        for name, shape in expected.items():
            value = getattr(state, name)
            if (not isinstance(value, torch.Tensor) or value.shape != shape
                    or value.dtype != self.dtype or value.device != self.device
                    or not bool(torch.isfinite(value).all())):
                raise ValueError("invalid state tensor " + name)
        if not bool((state.C > 0).all()) or not bool(state.s >= 0):
            raise ValueError("state requires positive C and nonnegative s")
        if self.lifted and not bool(state.rho >= 0):
            raise ValueError("lifted state requires nonnegative rho")
        return state

    def initial_state(self):
        return self.validate_state(self.initial).clone()

    def gates(self, s):
        v = s/(1+s)
        weights = (1+((v-self.centers)*self.P).square()).square().reciprocal()
        return weights/weights.sum()

    @staticmethod
    def _columns(value):
        # (P,n,M) -> (n,P*M), keeping matching j,a columns together.
        return value.permute(1, 0, 2).reshape(value.shape[1], -1)

    def _factors(self, state):
        return (-2/(self.M*self.n))*self._columns(state.A), self._columns(state.B/state.C[:, None, None])

    def delta_factors(self, state):
        self.validate_state(state)
        return self._factors(state)

    def _apply_delta(self, state, values, transpose=False):
        return factor_action(*self._factors(state), values, transpose=transpose)

    def apply_delta(self, state, values, *, transpose=False):
        self.validate_state(state)
        return self._apply_delta(state, values, transpose)

    def _apply_hidden(self, state, values, transpose=False):
        return (self.W0.T if transpose else self.W0) @ values + self._apply_delta(state, values, transpose)

    def apply_hidden(self, state, values, *, transpose=False):
        self.validate_state(state)
        return self._apply_hidden(state, values, transpose)

    def reconstruct_delta_for_diagnostics(self, state):
        """Explicit opt-in dense DeltaW; never called by the RHS."""
        left, right = self.delta_factors(state)
        return left @ right.T

    def _training_fields(self, state):
        if self.lifted:
            h1, h2 = state.h1, state.h2
        else:
            h1 = torch.tanh(state.w @ self.inputs.T)
            h2 = torch.tanh(self._apply_hidden(state, h1))
        f = state.c @ h2/self.n
        r = f-self.labels
        loss = r.square().mean()
        rho = state.rho if self.lifted else torch.sqrt(loss)
        delta2 = state.c[:, None]*(1-h2.square())
        delta1 = self._apply_hidden(state, delta2, transpose=True)*(1-h1.square())
        return dict(h1=h1, h2=h2, f=f, r=r, rho=rho, loss=loss,
                    delta1=delta1, delta2=delta2, gates=self.gates(state.s))

    def fields(self, state):
        """Training fields; lifted states use their dynamic h1,h2,rho."""
        self.validate_state(state)
        return self._training_fields(state)

    @torch.no_grad()
    def predict(self, state, inputs):
        """Query arbitrary already-scaled input rows using fresh tanh responses."""
        self.validate_state(state)
        inputs = self._tensor(inputs)
        if inputs.ndim != 2 or inputs.shape[1] != self.d:
            raise ValueError("query inputs must have shape (Q,d)")
        h1 = torch.tanh(state.w @ inputs.T)
        h2 = torch.tanh(self._apply_hidden(state, h1))
        return state.c @ h2/self.n

    def _derivative_factors(self, state, velocity):
        mean_b = state.B/state.C[:, None, None]
        mean_b_dot = (velocity.B-mean_b*velocity.C[:, None, None])/state.C[:, None, None]
        left = (-2/(self.M*self.n))*torch.cat((self._columns(velocity.A), self._columns(state.A)), dim=1)
        right = torch.cat((self._columns(mean_b), self._columns(mean_b_dot)), dim=1)
        return left, right

    def derivative_factors(self, state, velocity=None):
        """Return L,R such that d(DeltaW)/dt=L@R.T, rank at most 2PM."""
        self.validate_state(state)
        if velocity is None:
            velocity = self.rhs(state)
        return self._derivative_factors(state, velocity)

    @torch.no_grad()
    def rhs(self, state):
        self.validate_state(state)
        f = self._training_fields(state)
        if bool(f["rho"] == 0):
            return MomentState(**{name: torch.zeros_like(value)
                                  for name, value in zip(state.names(), state.tensors())})
        r, rho, h1, h2, g = (f[name] for name in ("r", "rho", "h1", "h2", "gates"))
        velocity = MomentState(
            (-2/self.M)*(f["delta1"]*r) @ self.inputs,
            (-2/self.M)*(h2 @ r),
            g[:, None, None]*(f["delta2"]*r)[None],
            (g*rho)[:, None, None]*h1[None],
            g*rho, rho.clone(),
        )
        if self.lifted:
            velocity.h1 = (1-h1.square())*(velocity.w @ self.inputs.T)
            z2dot = self._apply_hidden(state, velocity.h1)
            z2dot = z2dot+factor_action(*self._derivative_factors(state, velocity), h1)
            velocity.h2 = (1-h2.square())*z2dot
            fdot = (velocity.c @ h2+state.c @ velocity.h2)/self.n
            velocity.rho = (r*fdot).mean()/rho
        return velocity

    def defect_factors(self, state):
        """Factors for E=DeltaWdot+(2/(Mn))*(delta2*r)@h1.T."""
        self.validate_state(state)
        f = self._training_fields(state)
        if bool(f["rho"] == 0):
            return (state.w.new_zeros((self.n, 0)), state.w.new_zeros((self.n, 0)))
        a = state.A/state.C[:, None, None]
        b = state.B/state.C[:, None, None]
        q = f["delta2"]*f["r"]/f["rho"]
        left = (-2*f["rho"]/(self.M*self.n))*self._columns(f["gates"][:, None, None]*(q[None]-a))
        right = self._columns(b-f["h1"][None])
        return left, right

    def defect_frobenius(self, state, *, block_size=128):
        return factor_frobenius(*self.defect_factors(state), block_size=block_size)

    def lift_diagnostics(self, state):
        """Drift from the exact lifted invariant manifold, in max absolute norm."""
        self.validate_state(state)
        h1 = torch.tanh(state.w @ self.inputs.T)
        h2 = torch.tanh(self._apply_hidden(state, h1))
        r = state.c @ h2/self.n-self.labels
        result = {"recomputed_loss": r.square().mean()}
        if self.lifted:
            result.update(h1_max=(state.h1-h1).abs().max(),
                          h2_max=(state.h2-h2).abs().max(),
                          rho_abs=(state.rho-torch.sqrt(self._training_fields(state)["loss"])).abs(),
                          rho_recomputed_abs=(state.rho-torch.sqrt(r.square().mean())).abs())
        return result

    def moment_diagnostics(self, state):
        """Derivative-memory moments D1 and D2, initially identically zero."""
        f = self.fields(state)
        q = f["delta2"]*f["r"]/f["rho"] if bool(f["rho"] > 0) else torch.zeros_like(f["delta2"])
        return {"D1": state.C[:, None, None]*f["h1"][None]-state.B,
                "D2": state.C[:, None, None]*q[None]-state.A-self.eta*self.q0[None]}

    def retained_bytes(self, state):
        """Moving-state and fixed-network bytes (excludes query temporaries)."""
        self.validate_state(state)
        return {"moving": sum(x.numel()*x.element_size() for x in state.tensors()),
                "fixed_W0": self.W0.numel()*self.W0.element_size(),
                "initial_state": sum(x.numel()*x.element_size() for x in self.initial.tensors())}
