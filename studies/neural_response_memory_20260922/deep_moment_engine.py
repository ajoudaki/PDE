"""Three hidden tanh layers with dense or orthogonal response-history flow.

Inputs are the actual first-layer rows (unit-circle rows need no sqrt(2)).
The loss is mean((f-y)**2), f=c@h3/n, with mobilities (n,1,1,n).
Direct tanh coordinates are used: the continuous moment model is unchanged,
but activations and residual RMS are recomputed rather than integrated.
No learned dense matrix is constructed in the moment RHS or error controller.
"""

from dataclasses import dataclass, fields as dataclass_fields
from math import sqrt
from numbers import Integral

import numpy as np
import torch

from moment_engine import factor_action, factor_frobenius


class StateAlgebra:
    def names(self):
        return tuple(field.name for field in dataclass_fields(self))

    def tensors(self):
        return tuple(getattr(self, name) for name in self.names())

    def clone(self):
        return type(self)(*(value.clone() for value in self.tensors()))

    def add_scaled(self, other, scale):
        return combine((1., scale), (self, other))


@dataclass
class DeepDenseState(StateAlgebra):
    w: torch.Tensor
    W2: torch.Tensor
    W3: torch.Tensor
    c: torch.Tensor


@dataclass
class DeepMomentState(StateAlgebra):
    w: torch.Tensor
    c: torch.Tensor
    A2: torch.Tensor
    B2: torch.Tensor
    A3: torch.Tensor
    B3: torch.Tensor
    s: torch.Tensor


def combine(coefficients, states):
    coefficients, states = tuple(coefficients), tuple(states)
    if not states or len(coefficients) != len(states):
        raise ValueError("nonempty equally sized coefficients and states required")
    if any(type(state) is not type(states[0]) for state in states):
        raise ValueError("matching state types required")
    # Avoid zero-filled dense accumulator allocations.
    components = []
    for values in zip(*(state.tensors() for state in states)):
        result = coefficients[0]*values[0]
        for coefficient, value in zip(coefficients[1:], values[1:]):
            result.add_(value, alpha=coefficient)
        components.append(result)
    return type(states[0])(*components)


def tensor_rms(value):
    return value.square().mean().sqrt()


class DeepDenseEngine:
    """Canonical three-hidden-layer physical gradient flow."""

    moment = False

    def __init__(self, d, width, inputs, labels, *, seed=20260920,
                 device="cpu", dtype=torch.float64):
        for name, value in (("d", d), ("width", width)):
            if isinstance(value, bool) or not isinstance(value, Integral) or value < 1:
                raise ValueError(name+" must be a positive integer")
        if isinstance(seed, bool) or not isinstance(seed, Integral) or seed < 0:
            raise ValueError("seed must be a nonnegative integer")
        if dtype not in (torch.float32, torch.float64):
            raise ValueError("dtype must be float32 or float64")
        self.d, self.n, self.seed = int(d), int(width), int(seed)
        self.device, self.dtype = torch.device(device), dtype
        self.inputs, self.labels = self._tensor(inputs), self._tensor(labels)
        if self.inputs.ndim != 2 or self.inputs.shape[1] != d or len(self.inputs) < 1:
            raise ValueError("inputs must have shape (M,d), M positive")
        self.M = len(self.inputs)
        if self.labels.shape != (self.M,):
            raise ValueError("labels must have shape (M,)")
        # Keep this draw order explicit, including stored c standard deviation 1/n.
        rng = np.random.default_rng(self.seed)
        w = self._tensor(rng.standard_normal((self.n, self.d)))
        self.W20 = self._tensor(rng.standard_normal((self.n, self.n))/sqrt(self.n))
        self.W30 = self._tensor(rng.standard_normal((self.n, self.n))/sqrt(self.n))
        c = self._tensor(rng.standard_normal(self.n)/self.n)
        self.initial = DeepDenseState(w, self.W20, self.W30, c)

    def _tensor(self, value):
        result = torch.as_tensor(value, dtype=self.dtype, device=self.device).detach().clone()
        if not bool(torch.isfinite(result).all()):
            raise ValueError("nonfinite tensor")
        return result

    def initial_state(self):
        return self.initial.clone()

    def validate_state(self, state, *, finite=True):
        expected = {"w": (self.n, self.d), "W2": (self.n, self.n),
                    "W3": (self.n, self.n), "c": (self.n,)}
        if self.moment:
            expected = {"w": (self.n, self.d), "c": (self.n,),
                        **{key: (self.P, self.n, self.M) for key in ("A2", "B2", "A3", "B3")},
                        "s": ()}
        if not isinstance(state, DeepMomentState if self.moment else DeepDenseState):
            raise ValueError("incorrect state type")
        for name, shape in expected.items():
            value = getattr(state, name)
            if value.shape != shape or value.dtype != self.dtype or value.device != self.device:
                raise ValueError("invalid state tensor "+name)
            if finite and not bool(torch.isfinite(value).all()):
                raise ValueError("nonfinite state tensor "+name)
        if self.moment and not bool(state.s >= 0):
            raise ValueError("activity must be nonnegative")
        return state

    def _apply(self, state, layer, values, transpose=False):
        matrix = getattr(state, "W"+str(layer))
        return (matrix.T if transpose else matrix) @ values

    def apply_hidden(self, state, layer, values, *, transpose=False):
        if layer not in (2, 3):
            raise ValueError("hidden layer must be 2 or 3")
        self.validate_state(state, finite=False)
        return self._apply(state, layer, values, transpose)

    def _fields(self, state):
        h1 = torch.tanh(state.w @ self.inputs.T)
        h2 = torch.tanh(self._apply(state, 2, h1))
        h3 = torch.tanh(self._apply(state, 3, h2))
        f = state.c @ h3/self.n
        r = f-self.labels
        loss = r.square().mean()
        delta3 = state.c[:, None]*(1-h3.square())
        delta2 = (1-h2.square())*self._apply(state, 3, delta3, transpose=True)
        delta1 = (1-h1.square())*self._apply(state, 2, delta2, transpose=True)
        return dict(h1=h1, h2=h2, h3=h3, f=f, r=r, loss=loss,
                    rho=loss.sqrt(), delta1=delta1, delta2=delta2, delta3=delta3)

    @torch.no_grad()
    def fields(self, state):
        self.validate_state(state, finite=False)
        return self._fields(state)

    @torch.no_grad()
    def predict(self, state, inputs):
        self.validate_state(state, finite=False)
        values = torch.as_tensor(inputs, dtype=self.dtype, device=self.device)
        if values.ndim != 2 or values.shape[1] != self.d:
            raise ValueError("query inputs must have shape (Q,d)")
        h1 = torch.tanh(state.w @ values.T)
        h2 = torch.tanh(self._apply(state, 2, h1))
        h3 = torch.tanh(self._apply(state, 3, h2))
        return state.c @ h3/self.n

    @torch.no_grad()
    def rhs(self, state):
        self.validate_state(state, finite=False)
        f = self._fields(state)
        return DeepDenseState(
            (-2/self.M)*(f["delta1"]*f["r"]) @ self.inputs,
            (-2/(self.M*self.n))*(f["delta2"]*f["r"]) @ f["h1"].T,
            (-2/(self.M*self.n))*(f["delta3"]*f["r"]) @ f["h2"].T,
            (-2/self.M)*(f["h3"] @ f["r"]),
        )

    def hidden_increment_norm(self, state, layer):
        return torch.linalg.vector_norm(getattr(state, "W"+str(layer))-getattr(self, "W"+str(layer)+"0"))

    def hidden_difference_norm(self, left, right, layer):
        return torch.linalg.vector_norm(getattr(left, "W"+str(layer))-getattr(right, "W"+str(layer)))

    def storage(self, state):
        moving = sum(value.numel()*value.element_size() for value in state.tensors())
        initial = sum(value.numel()*value.element_size() for value in self.initial.tensors())
        return dict(moving_state_bytes=moving, initial_state_bytes=initial,
                    fixed_hidden_bytes=0, fixed_hidden_bytes_retained_for_initialization_and_error_control=
                    self.W20.numel()*self.W20.element_size()+self.W30.numel()*self.W30.element_size(),
                    data_bytes=sum(value.numel()*value.element_size() for value in (self.inputs,self.labels)))


class DeepMomentEngine(DeepDenseEngine):
    """Independent P-mode moments on both hidden links; shared L=1+s."""

    moment = True

    def __init__(self, d, width, order, inputs, labels, **kwargs):
        if isinstance(order, bool) or not isinstance(order, Integral) or order < 1:
            raise ValueError("order must be a positive integer")
        self.P = int(order)
        super().__init__(d, width, inputs, labels, **kwargs)
        self.degrees = torch.arange(self.P, dtype=self.dtype, device=self.device)
        self.weights = 2*self.degrees+1
        h10 = torch.tanh(self.initial.w @ self.inputs.T)
        h20 = torch.tanh(self.W20 @ h10)
        moments = [self.initial.w.new_zeros((self.P,self.n,self.M)) for _ in range(4)]
        moments[1][0] = h10
        moments[3][0] = h20
        self.initial = DeepMomentState(self.initial.w, self.initial.c, *moments,
                                       self.initial.w.new_zeros(()))

    @staticmethod
    def _columns(values):
        return values.permute(1,0,2).reshape(values.shape[1],-1)

    def delta_factors(self, state, layer):
        if layer not in (2,3):
            raise ValueError("layer must be 2 or 3")
        A, B = getattr(state,"A"+str(layer)), getattr(state,"B"+str(layer))
        return (-2/(self.M*self.n))*self._columns(self.weights[:,None,None]*A), self._columns(B/(1+state.s))

    def _apply(self, state, layer, values, transpose=False):
        matrix = getattr(self, "W"+str(layer)+"0")
        return (matrix.T if transpose else matrix) @ values + factor_action(
            *self.delta_factors(state,layer), values, transpose=transpose)

    def reconstruct_delta_for_diagnostics(self, state, layer):
        left,right = self.delta_factors(state,layer)
        return left @ right.T

    def transport_moments(self, moments, source, rho, length):
        weighted = self.weights[:,None,None]*moments
        lower = torch.cat((torch.zeros_like(weighted[:1]),weighted[:-1].cumsum(dim=0)),dim=0)
        return source[None]-(rho/length)*(self.degrees[:,None,None]*moments+lower)

    @torch.no_grad()
    def rhs(self, state):
        self.validate_state(state, finite=False)
        f = self._fields(state)
        velocities = []
        for layer in (2,3):
            velocities.extend((
                self.transport_moments(getattr(state,"A"+str(layer)),f["delta"+str(layer)]*f["r"],f["rho"],1+state.s),
                self.transport_moments(getattr(state,"B"+str(layer)),f["rho"]*f["h"+str(layer-1)],f["rho"],1+state.s),
            ))
        return DeepMomentState((-2/self.M)*(f["delta1"]*f["r"]) @ self.inputs,
                               (-2/self.M)*(f["h3"] @ f["r"]), *velocities, f["rho"].clone())

    def derivative_factors(self, state, layer, velocity=None):
        velocity = self.rhs(state) if velocity is None else velocity
        A,B = getattr(state,"A"+str(layer)),getattr(state,"B"+str(layer))
        dA,dB = getattr(velocity,"A"+str(layer)),getattr(velocity,"B"+str(layer))
        length,weights = 1+state.s,self.weights[:,None,None]
        return ((-2/(self.M*self.n))*torch.cat((self._columns(weights*dA),self._columns(weights*A)),dim=1),
                torch.cat((self._columns(B/length),self._columns((dB-B*velocity.s/length)/length)),dim=1))

    def endpoint_projections(self, state, layer):
        weights = self.weights[:,None,None]/(1+state.s)
        return ((weights*getattr(state,"A"+str(layer))).sum(dim=0),
                (weights*getattr(state,"B"+str(layer))).sum(dim=0))

    def defect_factors(self, state, layer, fields=None):
        f = self.fields(state) if fields is None else fields
        up,hp = self.endpoint_projections(state,layer)
        # Division-free formula also gives zero on the absorbing rho=0 boundary.
        return ((2/(self.M*self.n))*(f["r"]*f["delta"+str(layer)]-f["rho"]*up),
                f["h"+str(layer-1)]-hp)

    def defect_frobenius(self, state, layer, fields=None):
        return factor_frobenius(*self.defect_factors(state,layer,fields))

    def difference_factors(self, left, right, layer):
        """Stable exact factors for DeltaW(left)-DeltaW(right)."""
        a,b = getattr(left,"A"+str(layer)),getattr(left,"B"+str(layer))
        ar,br = getattr(right,"A"+str(layer)),getattr(right,"B"+str(layer))
        weights = self.weights[:,None,None]
        return ((-2/(self.M*self.n))*torch.cat((self._columns(weights*(a-ar)),self._columns(weights*ar)),dim=1),
                torch.cat((self._columns(b/(1+left.s)),self._columns(b/(1+left.s)-br/(1+right.s))),dim=1))

    def hidden_increment_norm(self, state, layer):
        return factor_frobenius(*self.delta_factors(state,layer))

    def hidden_difference_norm(self, left, right, layer):
        return factor_frobenius(*self.difference_factors(left,right,layer))

    def storage(self, state):
        result = super().storage(state)
        result["fixed_hidden_bytes"] = result.pop("fixed_hidden_bytes_retained_for_initialization_and_error_control")
        result.update(history_scalars=4*self.P*self.n*self.M,
                      history_rank_bound_per_link=min(self.n,self.P*self.M),
                      history_factor_columns_per_link=self.P*self.M)
        return result


@torch.no_grad()
def controlled_error(engine, current, euler, candidate, rtol, atol):
    """Euler/Heun difference: max block error plus both physical matrix errors.

    Vector/moment blocks use RMS with scale max(1,RMS(current),RMS(candidate)).
    Both models use hidden Frobenius/sqrt(n), scaled by their learned increment
    norms with the same unit floor. This avoids entrywise 1/n dilution.
    """
    ratios = []
    for name in current.names():
        if name in ("W2","W3"):
            continue
        a,b,c = (getattr(state,name) for state in (current,euler,candidate))
        scale = torch.maximum(tensor_rms(a),tensor_rms(c)).clamp_min(1)
        ratios.append(tensor_rms(c-b)/(atol+rtol*scale))
    for layer in (2,3):
        scale = torch.maximum(engine.hidden_increment_norm(current,layer),
                              engine.hidden_increment_norm(candidate,layer))/sqrt(engine.n)
        error = engine.hidden_difference_norm(candidate,euler,layer)/sqrt(engine.n)
        ratios.append(error/(atol+rtol*scale.clamp_min(1)))
    return float(torch.stack(ratios).max().cpu())
