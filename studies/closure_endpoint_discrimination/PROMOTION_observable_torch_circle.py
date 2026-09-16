"""Float64 Torch backend for the maintained circle closure, orders 1, 3, 5.

Inputs are directions u=x/sqrt(2). This optional module implements finite
quadrature equations, not a broader convergence or neural accuracy theorem.
"""
from dataclasses import dataclass
import copy
import math
from numbers import Integral

import numpy as np
import torch

from pde import observable_solver as cpu
from pde.observable_arithmetic import Arithmetic

KEYS = ('b1', 'g', 'w', 'p1', 'b2', 'c', 'p2', 'M', 'D')
SUPPORTED_ORDERS = (1, 3, 5)
_DIMENSIONS = {1: (5, 3), 3: (35, 10), 5: (128, 21)}


def _integer(value, name, minimum=1):
    if isinstance(value, bool) or not isinstance(value, Integral) or value < minimum:
        raise ValueError(name + ' must be an integer >= ' + str(minimum))
    return int(value)


def _order(value):
    value = _integer(value, 'order')
    if value not in SUPPORTED_ORDERS:
        raise ValueError('supported orders are 1, 3, 5')
    return value


def _tensor(value, device):
    if isinstance(value, torch.Tensor):
        if value.is_complex() or value.dtype == torch.bool:
            raise ValueError('real numeric input required')
        return value.detach().to(device=device, dtype=torch.float64).clone()
    a = np.asarray(value)
    if a.dtype.kind not in 'fiu':
        raise ValueError('real numeric input required')
    return torch.tensor(a, dtype=torch.float64, device=device)


def _finite(value):
    return bool(torch.isfinite(value).all().item())


def _inputs(value, device):
    value = _tensor(value, device)
    if value.ndim != 2 or value.shape[0] < 1 or value.shape[1] != 2:
        raise ValueError('inputs require nonempty shape (m,2)')
    if not _finite(value) or bool((abs((value*value).sum(1)-1) > 2e-12).any()):
        raise ValueError('inputs must be finite unit directions')
    return value


@dataclass
class State:
    """Owned joint tables. Public tensors are mutable; evaluation revalidates.

    Changing a frozen mark changes the model; no derived cache is retained.
    metadata is descriptive except the checked scheme and order tags.
    """
    b1: torch.Tensor
    g: torch.Tensor
    w: torch.Tensor
    p1: torch.Tensor
    b2: torch.Tensor
    c: torch.Tensor
    p2: torch.Tensor
    M: torch.Tensor
    D: torch.Tensor
    metadata: dict

    @property
    def device(self):
        return self.w.device

    def validate(self):
        if not isinstance(self.metadata,dict):
            raise ValueError('metadata must be a dictionary')
        order = _order(self.metadata.get('hierarchy_order'))
        if self.metadata.get('dictionary_scheme') != 'tanh-chebyshev-plus-code-v1':
            raise ValueError('unsupported dictionary scheme')
        values = [getattr(self, k) for k in KEYS]
        if not all(isinstance(v, torch.Tensor) for v in values):
            raise ValueError('state requires tensors')
        if self.device.type not in ('cpu', 'cuda'):
            raise ValueError('supported devices are CPU and CUDA')
        if any(v.dtype != torch.float64 or v.device != self.device or v.requires_grad for v in values):
            raise ValueError('state requires detached float64 tensors on one device')
        if not all(_finite(v) for v in values):
            raise ValueError('nonfinite state')
        k1, k2 = _DIMENSIONS[order]
        if self.b1.ndim != 2 or self.b2.ndim != 2:
            raise ValueError('feature tables must be matrices')
        p, q = self.b1.shape[0], self.b2.shape[0]
        shapes = ((p,k1),(p,2),(p,2),(p,),(q,k2),(q,),(q,),(k2,k1),(k2,k1))
        if min(p,q) < 1 or any(tuple(v.shape) != s for v,s in zip(values,shapes)):
            raise ValueError('inconsistent state shapes')
        for weights in (self.p1,self.p2):
            if bool((weights < 0).any()) or abs(float(weights.sum())-1) > 2e-12*len(weights):
                raise ValueError('population weights require nonnegative unit mass')
        return self

    def copy(self):
        return State(*(getattr(self,k).clone() for k in KEYS),copy.deepcopy(self.metadata))

    def _moving(self,w,c,M):
        return State(self.b1,self.g,w,self.p1,self.b2,c,self.p2,M,self.D,self.metadata)


@dataclass
class DataLaw:
    """Tensor finite law; constructor factory owns its arrays."""
    inputs: torch.Tensor
    labels: torch.Tensor
    probabilities: torch.Tensor
    metadata: dict

    def validate(self, device):
        values = (self.inputs,self.labels,self.probabilities)
        if any(not isinstance(v,torch.Tensor) or v.dtype != torch.float64 or v.device != device
               or v.requires_grad or not _finite(v) for v in values):
            raise ValueError('data require finite detached float64 on the state device')
        u,y,p = values
        if u.ndim != 2 or len(u) == 0 or u.shape[1] != 2 or y.shape != (len(u),) or p.shape != y.shape:
            raise ValueError('invalid data shapes')
        if bool((abs((u*u).sum(1)-1)>2e-12).any()):
            raise ValueError('data require unit directions')
        if bool((p<0).any()) or abs(float(p.sum())-1)>2e-12*len(p):
            raise ValueError('data probabilities require nonnegative unit mass')
        return self


def data_law(inputs, labels, probabilities, *, device='cpu', metadata=None):
    device = torch.device(device)
    u,y,p = (_tensor(v,device) for v in (inputs,labels,probabilities))
    # CUDA's generic device resolves to an indexed device when allocated.
    return DataLaw(u,y,p,copy.deepcopy(metadata or {})).validate(u.device)


def from_cpu(state, *, device='cpu'):
    state.validate()
    if state.arithmetic.digits is not None or any(getattr(state,k).dtype != np.float64 for k in KEYS):
        raise ValueError('only float64 CPU states can be transferred')
    return State(*(_tensor(getattr(state,k),device) for k in KEYS),copy.deepcopy(state.metadata)).validate()


def to_cpu(state):
    state.validate()
    return cpu.State(*(getattr(state,k).detach().cpu().numpy().copy() for k in KEYS),
                     Arithmetic(),copy.deepcopy(state.metadata)).validate()


def initialize(order=1, *, initialization_nodes=2048, population_nodes=1024, device='cpu', limits=None):
    """Use the unchanged CPU initializer; preserve every feature and ridge mode."""
    return from_cpu(cpu.initialize(_order(order), initialization_nodes=initialization_nodes,
                    population_nodes=population_nodes, limits=limits),device=device)


def _fields(state,u,backward=True):
    h1 = torch.tanh(state.w @ u.T)
    a = state.b1.T @ (state.p1[:,None]*h1)
    h2 = torch.tanh(state.b2 @ (state.M @ a))
    f = state.p2 @ (state.c[:,None]*h2)
    result = dict(h1=h1,a=a,h2=h2,f=f)
    if backward:
        d = state.b2.T @ (state.p2[:,None]*state.c[:,None]*(1-h2*h2))
        result.update(d=d,q=state.b1 @ (state.M.T @ d))
    return result


@torch.no_grad()
def fields(state,inputs):
    """Full panel fields; caller chooses its size (unlike blocked prediction)."""
    state.validate()
    result = _fields(state,_inputs(inputs,state.device))
    if not all(_finite(v) for v in result.values()):
        raise ValueError('nonfinite field')
    return result


@torch.no_grad()
def predict(state,inputs,*,block_size=128):
    block_size = _integer(block_size,'block_size')
    state.validate()
    u = _inputs(inputs,state.device)
    result = torch.cat([_fields(state,u[j:j+block_size],False)['f'] for j in range(0,len(u),block_size)])
    if not _finite(result):
        raise ValueError('nonfinite prediction')
    return result


def _rhs(state,data,block_size):
    vw,vc,vM = (torch.zeros_like(v) for v in (state.w,state.c,state.M))
    for j in range(0,len(data.inputs),block_size):
        u = data.inputs[j:j+block_size]
        v = _fields(state,u)
        r = data.probabilities[j:j+block_size]*(v['f']-data.labels[j:j+block_size])
        vw -= 2*(((1-v['h1']*v['h1'])*v['q']*r) @ u)
        vc -= 2*(v['h2'] @ r)
        vM -= 2*((v['d']*r) @ v['a'].T)
    if not all(_finite(v) for v in (vw,vc,vM)):
        raise ValueError('nonfinite velocity')
    return vw,vc,vM


@torch.no_grad()
def rhs(state,data,*,block_size=128):
    block_size = _integer(block_size,'block_size')
    state.validate(); data.validate(state.device)
    return _rhs(state,data,block_size)


@torch.no_grad()
def evolve(state,data,*,steps,step_size,block_size=128):
    """Fresh simultaneous explicit-Heun state; no history or absolute clock."""
    steps = _integer(steps,'steps')
    block_size = _integer(block_size,'block_size')
    if isinstance(step_size,bool):
        raise ValueError('step_size must be finite and positive')
    h = float(step_size)
    if not math.isfinite(h) or h <= 0:
        raise ValueError('step_size must be finite and positive')
    state.validate(); data.validate(state.device)
    current = state.copy()
    for _ in range(steps):
        k = _rhs(current,data,block_size)
        stage = current._moving(current.w+h*k[0],current.c+h*k[1],current.M+h*k[2])
        stage.validate()
        v = _rhs(stage,data,block_size)
        current = current._moving(current.w+(h/2)*(k[0]+v[0]), current.c+(h/2)*(k[1]+v[1]),
                                  current.M+(h/2)*(k[2]+v[2])).validate()
    return current


@torch.no_grad()
def paired_observations(state,data,*,block_size=128,include_pairs=True):
    """Blocked paired observations; optional complete pairs are explicit output."""
    block_size = _integer(block_size,'block_size')
    state.validate(); data.validate(state.device)
    pairs = [torch.empty((len(state.b1),len(data.inputs),2),dtype=torch.float64,device=state.device),
             torch.empty((len(state.b2),len(data.inputs),2),dtype=torch.float64,device=state.device)] if include_pairs else [None,None]
    sums = torch.zeros(2,dtype=torch.float64,device=state.device)
    for j in range(0,len(data.inputs),block_size):
        u = data.inputs[j:j+block_size]
        current = _fields(state,u,False)
        first = torch.tanh(state.g @ u.T)
        second = torch.tanh(state.b2 @ (state.D @ (state.b1.T @ (state.p1[:,None]*first))))
        for layer,(initial,actual,weights) in enumerate(((first,current['h1'],state.p1),(second,current['h2'],state.p2))):
            sums[layer] += weights @ ((actual-initial)**2) @ data.probabilities[j:j+block_size]
            if include_pairs:
                pairs[layer][:,j:j+len(u),0] = initial
                pairs[layer][:,j:j+len(u),1] = actual
    result = dict(first_pairs=pairs[0],second_pairs=pairs[1],rms=torch.sqrt(sums),
                  first_weights=state.p1.clone(),second_weights=state.p2.clone(),
                  input_weights=data.probabilities.clone(),inputs=data.inputs.clone())
    if not all(v is None or _finite(v) for v in result.values()):
        raise ValueError('nonfinite paired observation')
    return result


@torch.no_grad()
def observe(state,data,*,include_pairs=False):
    """Current input Grams and same-node initial/current hidden laws and RMS.

    Grams allocate O(m²); explicit pairs allocate O((P1+P2)m).
    Initial fields are reconstructed from frozen g,D, never loaded from history.
    """
    state.validate(); data.validate(state.device)
    u = data.inputs
    # Grams require cross-block products. Retain the whole observed panel's
    # hidden fields, while predictions/RHS remain independently block bounded.
    values = _fields(state,u,False)
    initial1 = torch.tanh(state.g @ u.T)
    initial2 = torch.tanh(state.b2 @ (state.D @ (state.b1.T @ (state.p1[:,None]*initial1))))
    grams,rms,pairs = [],[],[]
    for actual,initial,weights in ((values['h1'],initial1,state.p1),(values['h2'],initial2,state.p2)):
        grams.append(actual.T @ (weights[:,None]*actual))
        rms.append(torch.sqrt(weights @ ((actual-initial)**2) @ data.probabilities))
        pairs.append(torch.stack((initial,actual),dim=-1) if include_pairs else None)
    residual = values['f']-data.labels
    result = dict(prediction=values['f'],loss=data.probabilities @ (residual*residual),
                  grams=torch.stack(grams),rms=torch.stack(rms),
                  activation_rms=torch.sqrt(torch.stack([torch.diag(G) @ data.probabilities for G in grams])),
                  first_pairs=pairs[0],second_pairs=pairs[1],
                  first_weights=state.p1.clone(),second_weights=state.p2.clone(),
                  input_weights=data.probabilities.clone(),inputs=u.clone())
    if not all(v is None or _finite(v) for v in result.values()):
        raise ValueError('nonfinite observation')
    return result


def state_bytes(state):
    state.validate()
    return sum(getattr(state,k).numel()*getattr(state,k).element_size() for k in KEYS)


def save_restart(path,state,data):
    """Existing portable float-hex format, full frozen/current arrays and law."""
    state.validate(); data.validate(state.device)
    d = cpu.DataLaw(*(v.detach().cpu().numpy().copy() for v in (data.inputs,data.labels,data.probabilities)),
                    copy.deepcopy(data.metadata))
    cpu.save_restart(path,to_cpu(state),d)


def load_restart(path,*,device='cpu'):
    state,data = cpu.load_restart(path)
    return from_cpu(state,device=device),data_law(data.inputs,data.labels,data.probabilities,
                                                 device=device,metadata=data.metadata)
