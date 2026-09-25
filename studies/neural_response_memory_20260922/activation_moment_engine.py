"""Declared activation variants of the frozen three-layer physical/moment flow.

Initialization, transport, reconstructed matrices and physical error control
are inherited unchanged. Derivatives are selected from preactivations, including
ReLU'(0)=0 and SELU'(0)=lambda*alpha. No activation-specific gain is applied.
"""

from math import sqrt, pi
from numbers import Integral

import torch

from deep_moment_engine import (DeepDenseEngine, DeepMomentEngine, DeepDenseState,
                                DeepMomentState, combine, controlled_error, tensor_rms)


ACTIVATIONS = ("relu", "gelu", "selu", "sigmoid")
SELU_SCALE = 1.0507009873554804934193349852946
SELU_ALPHA = 1.6732632423543772848170429916717


def activation_value(name, z):
    if name == "relu":
        return torch.relu(z)
    if name == "gelu":
        return z*(.5*torch.erfc(-z/sqrt(2.)))
    if name == "selu":
        # torch.where evaluates both branches: clamp BEFORE expm1.
        negative = SELU_SCALE*SELU_ALPHA*torch.expm1(z.clamp_max(0))
        return torch.where(z > 0, SELU_SCALE*z, negative)
    if name == "sigmoid":
        return torch.sigmoid(z)
    raise ValueError("unknown activation: "+str(name))


def activation_derivative(name, z, h=None):
    if name == "relu":
        return (z > 0).to(z.dtype)
    if name == "gelu":
        return .5*torch.erfc(-z/sqrt(2.))+z*torch.exp(-.5*z.square())/sqrt(2*pi)
    if name == "selu":
        negative = SELU_SCALE*SELU_ALPHA*torch.exp(z.clamp_max(0))
        return torch.where(z > 0, torch.full_like(z, SELU_SCALE), negative)
    if name == "sigmoid":
        h = torch.sigmoid(z) if h is None else h
        return h*(1-h)
    raise ValueError("unknown activation: "+str(name))


class ActivationForward:
    def _set_activation(self, activation):
        if activation not in ACTIVATIONS:
            raise ValueError("activation must be one of "+str(ACTIVATIONS))
        self.activation = activation

    def _fields(self, state):
        z1 = state.w @ self.inputs.T
        h1 = activation_value(self.activation, z1)
        z2 = self._apply(state, 2, h1)
        h2 = activation_value(self.activation, z2)
        z3 = self._apply(state, 3, h2)
        h3 = activation_value(self.activation, z3)
        derivative1 = activation_derivative(self.activation, z1, h1)
        derivative2 = activation_derivative(self.activation, z2, h2)
        derivative3 = activation_derivative(self.activation, z3, h3)
        f = state.c @ h3/self.n
        r = f-self.labels
        loss = r.square().mean()
        delta3 = state.c[:, None]*derivative3
        delta2 = derivative2*self._apply(state, 3, delta3, transpose=True)
        delta1 = derivative1*self._apply(state, 2, delta2, transpose=True)
        return dict(z1=z1,z2=z2,z3=z3,h1=h1,h2=h2,h3=h3,
                    derivative1=derivative1,derivative2=derivative2,derivative3=derivative3,
                    f=f,r=r,loss=loss,rho=loss.sqrt(),delta1=delta1,delta2=delta2,delta3=delta3)

    @torch.no_grad()
    def predict(self, state, inputs):
        self.validate_state(state, finite=False)
        values = torch.as_tensor(inputs,dtype=self.dtype,device=self.device)
        if values.ndim != 2 or values.shape[1] != self.d:
            raise ValueError("query inputs must have shape (Q,d)")
        h1 = activation_value(self.activation,state.w @ values.T)
        h2 = activation_value(self.activation,self._apply(state,2,h1))
        h3 = activation_value(self.activation,self._apply(state,3,h2))
        return state.c @ h3/self.n


class ActivationDenseEngine(ActivationForward, DeepDenseEngine):
    def __init__(self, d, width, inputs, labels, *, activation, **kwargs):
        self._set_activation(activation)
        super().__init__(d,width,inputs,labels,**kwargs)


class ActivationMomentEngine(ActivationForward, DeepMomentEngine):
    def __init__(self, d, width, order, inputs, labels, *, activation, **kwargs):
        self._set_activation(activation)
        if isinstance(order,bool) or not isinstance(order,Integral) or order < 1:
            raise ValueError("order must be a positive integer")
        self.P = int(order)
        # Call the physical initializer directly, avoiding the old tanh B moments.
        DeepDenseEngine.__init__(self,d,width,inputs,labels,**kwargs)
        self.degrees = torch.arange(self.P,dtype=self.dtype,device=self.device)
        self.weights = 2*self.degrees+1
        h10 = activation_value(self.activation,self.initial.w @ self.inputs.T)
        h20 = activation_value(self.activation,self.W20 @ h10)
        moments = [self.initial.w.new_zeros((self.P,self.n,self.M)) for _ in range(4)]
        moments[1][0],moments[3][0] = h10,h20
        self.initial = DeepMomentState(self.initial.w,self.initial.c,*moments,
                                       self.initial.w.new_zeros(()))
