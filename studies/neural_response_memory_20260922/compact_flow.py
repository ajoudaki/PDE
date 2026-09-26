"""One-file dense and compressed learning suite.

Run --config experiment_configs.json --experiment NAME --out FRESH.
Run --check [--gpu cuda:0] [--out FRESH.json] for bounded regression checks.
Scalar compression is a separate exploratory study branch.
"""
import argparse
import csv
from functools import lru_cache
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import shlex
import struct
import subprocess
import sys
import tempfile
import time
from types import SimpleNamespace
import zipfile
os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
import numpy as np
import torch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT/'code'))
from pde.observable_initialization import build_dictionary

MODEL = dict(width=2048, depth=3, activation='relu', seed=20260920,
             hidden_gain=1., readout_std=None, dtype='float32')
OPTIMIZER = dict(step=.0625, target_rms=.05, max_seconds=60., max_steps=60000, block=8)
KINDS = ('dense', 'closure', 'dictionary_old', 'dictionary_flow', 'gaussian', 'orthogonal',
         'trainable_dictionary', 'low_rank', 'weighted_closure')
OLD_RANKS = {1: (5, 3), 3: (35, 10), 5: (128, 21), 6: (213, 28),
             7: (333, 36), 8: (499, 45), 9: (720, 55)}


# Shared network and fixed-step trainer.

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

    def _forward(self, inputs, factors, derivatives=False, w=None, apply=None):
        hidden, slopes = [], []
        z = (self.w if w is None else w)@inputs.T
        for i, spec in enumerate(self.activations):
            if i: z = self._apply(i-1, hidden[-1], factors) if apply is None else apply(i-1, hidden[-1])
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
    def _fields(self, w=None, c=None, factors=None, apply=None):
        factors = self._factors() if factors is None else factors
        c = self.c if c is None else c
        hidden, slopes = self._forward(self.inputs,factors,True,w,apply)
        residual = c@hidden[-1]/self.n-self.labels
        delta = [None]*self.depth
        delta[-1] = self._backward_layer(slopes[-1],c[:,None])
        for i in range(self.depth-2,-1,-1):
            back = self._apply(i,delta[i+1],factors,True) if apply is None else apply(i,delta[i+1],True)
            delta[i] = self._backward_layer(slopes[i],back)
        return hidden, delta, residual

    @torch.no_grad()
    def rhs(self):
        hidden, delta, residual = self._fields()
        self.loss = residual.square().mean()
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


class FrozenFlow(Flow):
    """Fixed population bases with trainable cores; no retained dense background.

    W_l = B_(l+1) C_l B_l.T / n. Outer mobilities are n; core mobility
    is 1, exactly as in the historical fixed-dictionary ClosureEngine.
    The same forward/backward routines, Euler update and CUDA graph fitter
    serve dense, response-memory and frozen-dictionary models.
    """
    @torch.no_grad()
    def __init__(self, inputs, labels, *, kind, order=1, ranks=None, basis_seed=7319,
                 train_basis=False, **kwargs):
        started = time.perf_counter()
        if kind in ('dictionary_old', 'dictionary_flow'):
            if (kwargs.get('depth', 3) != 2 or len(np.shape(inputs)) != 2 or np.shape(inputs)[1] != 2
                    or kwargs.get('activation', 'relu') != 'tanh'
                    or kwargs.get('normalization', 'none') != 'none'
                    or kwargs.get('hidden_gain', 1.) != 1.
                    or kwargs.get('readout_std') not in (None, 1/kwargs.get('width', 2048))):
                raise ValueError('Historical dictionaries require 2D, depth=2, tanh, no normalization, hidden_gain=1 and readout_std=1/width')
        super().__init__(inputs, labels, order=None, **kwargs)
        self.kind, self.train_basis = kind, train_basis
        self.bases = frozen_bases(self.w, self.matrices, self.c, kind, order, ranks, basis_seed)
        self.matrices = [self.bases[i+1].T @ (matrix @ self.bases[i])/self.n
                         for i, matrix in enumerate(self.matrices)]
        self.state = [self.w, *self.matrices, self.c, *(self.bases if train_basis else [])]
        self.setup_seconds = time.perf_counter()-started

    def _apply(self, index, values, factors, transpose=False):
        left, right = self.bases[index+1], self.bases[index]
        core = self.matrices[index]
        if transpose: left, right, core = right, left, core.T
        return left @ (core @ (right.T @ values/self.n))

    @torch.no_grad()
    def rhs(self):
        hidden, delta, residual = self._fields()
        self.loss = residual.square().mean()
        dw = (-2/self.M)*(delta[0]*residual) @ self.inputs
        dc = (-2/self.M)*(hidden[-1] @ residual)
        cores = [(-2/self.M)*((self.bases[i+1].T @ delta[i+1]/self.n)*residual)
                 @ (self.bases[i].T @ hidden[i]/self.n).T for i in range(self.depth-1)]
        velocities = [dw, *cores, dc]
        if self.train_basis:
            # A population basis is shared by its incoming and outgoing link.
            db = [torch.zeros_like(b) for b in self.bases]
            for i, core in enumerate(self.matrices):
                a = self.bases[i].T @ hidden[i]/self.n
                d = self.bases[i+1].T @ delta[i+1]/self.n
                db[i].add_((-2/self.M)*(hidden[i]*residual) @ (core.T@d).T)
                db[i+1].add_((-2/self.M)*(delta[i+1]*residual) @ (core@a).T)
            velocities.extend(db)
        return velocities


class LowRankFlow(Flow):
    """W=W0+A B; factors have mobility one, outer weights mobility n."""
    @torch.no_grad()
    def __init__(self, inputs, labels, *, rank, factor_seed=20260924, **kwargs):
        started = time.perf_counter()
        super().__init__(inputs, labels, order=None, **kwargs)
        ranks = [rank]*(self.depth-1) if isinstance(rank, int) else rank
        if isinstance(rank,bool) or not isinstance(ranks,(list,tuple)) or len(ranks) != self.depth-1 or any(isinstance(r,bool) or not isinstance(r,int) or r < 1 for r in ranks):
            raise ValueError('Use one positive rank per hidden-to-hidden link')
        rng = np.random.default_rng(factor_seed)
        self.factors = [(self.w.new_zeros((self.n,r)), torch.tensor(
            rng.standard_normal((r,self.n))/math.sqrt(r),device=self.device,dtype=self.dtype)) for r in ranks]
        self.state = [self.w,self.c,*[v for pair in self.factors for v in pair]]
        self.setup_seconds = time.perf_counter()-started

    def _factors(self):
        return [(a,b.T) for a,b in self.factors]

    @torch.no_grad()
    def rhs(self):
        hidden,delta,residual = self._fields()
        self.loss = residual.square().mean()
        velocities = [(-2/self.M)*(delta[0]*residual)@self.inputs,
                      (-2/self.M)*(hidden[-1]@residual)]
        for i,(a,b) in enumerate(self.factors):
            q = delta[i+1]*residual
            scale = -2/(self.M*self.n)
            velocities.extend((scale*q@(b@hidden[i]).T,scale*(a.T@q)@hidden[i].T))
        return velocities


class WeightedFlow(Flow):
    """Matching-prefix weighted history moments and a response-speed clock.

    Implements RESPONSE_CLOCK_FULL_CLOSURE, layer by layer. One clock/Gram
    serves all links. No dense update, Hessian, numerical ridge or clock solve.
    The tiny Gram and clock use float64 even with float32 network tensors.
    """
    @torch.no_grad()
    def __init__(self, inputs, labels, *, order=1, clock='response', **kwargs):
        started = time.perf_counter()
        if clock not in ('response','residual'): raise ValueError('Unknown history clock')
        super().__init__(inputs, labels, order=order, **kwargs)
        self.clock = clock
        self.G = torch.diag(1/(2*torch.arange(order,device=self.device,dtype=torch.float64)+1))
        self.s = self.G.new_zeros(())
        self.prefix = [(a[0].clone(),b[0].clone()) for a,b in zip(self.moments[::2],self.moments[1::2])]
        hidden,delta,residual = self._fields()
        rho = residual.square().mean().sqrt()
        safe = torch.where(rho>0,rho,torch.ones_like(rho))
        for i,(a,b) in enumerate(zip(self.moments[::2],self.moments[1::2])):
            a[0].copy_(delta[i+1]*(residual/safe))
        self.prefix = [(a[0].clone(),b[0].clone()) for a,b in zip(self.moments[::2],self.moments[1::2])]
        self.state = [self.w,self.c,*self.moments,self.G,self.s]
        k = torch.arange(order,device=self.device,dtype=torch.float64)
        self.T = torch.diag(k)+torch.tril((2*k+1).expand(order,-1),diagonal=-1)
        # Exact polynomial coordinate transport, evaluated at Gauss nodes.
        nodes,_ = np.polynomial.legendre.leggauss(order)
        self.nodes = torch.tensor((nodes+1)/2,device=self.device,dtype=torch.float64)
        self.inverse_vander = torch.tensor(np.linalg.inv(np.polynomial.legendre.legvander(nodes,order-1).T),device=self.device)
        self.setup_seconds = time.perf_counter()-started

    def _factors(self):
        # One small solve, shared by all links and both action orientations.
        columns = [a.reshape(self.order,-1).double() for a in self.moments[::2]]
        rhs = torch.cat([*columns,self.G.new_ones((self.order,1))],1)
        solved = torch.linalg.solve_ex(self.G,rhs,check_errors=False).result
        self._q = solved[:,-1].to(self.dtype)[:,None,None]
        factors=[]; offset=0; size=self.n*self.M; scale=-2/(self.n*self.M)
        for (a,b),(u0,h0) in zip(zip(self.moments[::2],self.moments[1::2]),self.prefix):
            u = solved[:,offset:offset+size].to(self.dtype).reshape_as(a);offset+=size
            factors.append((scale*torch.cat((self._columns(u),-u0),1),torch.cat((self._columns(b),h0),1)))
        return factors

    def _weighted_terms(self):
        factors = self._factors()
        hidden,delta,residual = self._fields(factors=factors)
        self.loss = residual.square().mean();rho = self.loss.sqrt()
        dw=(-2/self.M)*(delta[0]*residual)@self.inputs
        dc=(-2/self.M)*(hidden[-1]@residual)
        source=[];velocity=[]
        for i,(u,h) in enumerate(zip(self.moments[::2],self.moments[1::2])):
            hs,us=(h*self._q).sum(0),(u*self._q).sum(0)
            rd=delta[i+1]*residual
            source.extend((rd,rho*hidden[i]))
            velocity.append((-2/(self.n*self.M)*torch.cat((rd,rho*us),1),
                             torch.cat((hs,hidden[i]-hs),1)))
        g=rho
        if self.clock=='response' and self.depth>1:
            # One scalar forward-mode directional derivative of the existing
            # network traversal. Weight velocities do not depend on this clock.
            def responses(eps):
                def apply(i,values,transpose=False):
                    left,right=velocity[i]
                    if transpose:left,right=right,left
                    return self._apply(i,values,factors,transpose)+eps*(left@(right.T@values))
                h,d,r=self._fields(w=self.w+eps*dw,c=self.c+eps*dc,factors=factors,apply=apply)
                norm=r.square().mean().sqrt()
                safe=torch.where(norm>0,norm,torch.ones_like(norm))
                return torch.cat([v.reshape(-1) for i in range(self.depth-1) for v in (h[i],d[i+1]*(r/safe))])
            zero=self.w.new_zeros(())
            _,speed=torch.func.jvp(responses,(zero,),(torch.ones_like(zero),))
            g=rho+torch.where(rho>0,speed.square().sum().sqrt(),torch.zeros_like(rho))
        return dw,dc,source,rho,g.double(),velocity

    @torch.no_grad()
    def rhs(self):
        dw,dc,source,rho,g,_=self._weighted_terms()
        moments=[v[None]-(g/(1+self.s))*(self.T.to(self.dtype)@m.reshape(self.order,-1)).reshape_as(m)
                 for m,v in zip(self.moments,source)]
        gram=rho-(g/(1+self.s))*(self.T@self.G+self.G@self.T.T)
        return [dw,dc,*moments,gram,g]

    @torch.no_grad()
    def step(self,dt):
        """First-order step with exact coordinate transport and positive Gram insertion.

        This avoids Euler making G indefinite solely through basis dilation.
        Network/source velocities remain explicit; there is no retry or tuning.
        """
        if not math.isfinite(dt) or dt<=0:raise ValueError('Positive finite step required')
        dw,dc,source,rho,g,_=self._weighted_terms()
        ratio=(1+self.s)/(1+self.s+dt*g)
        z=2*ratio*self.nodes-1
        polys=[torch.ones_like(z)]
        if self.order>1:polys.append(z)
        for k in range(1,self.order-1):polys.append(((2*k+1)*z*polys[-1]-k*polys[-2])/(k+1))
        change=torch.stack(polys)@self.inverse_vander
        endpoint=change.sum(1)
        for m,v in zip(self.moments,source):
            moved=(change.to(self.dtype)@m.reshape(self.order,-1)).reshape_as(m)
            m.copy_(moved+dt*endpoint.to(self.dtype)[:,None,None]*v)
        gram=change@self.G@change.T+dt*rho*endpoint[:,None]*endpoint[None,:]
        self.G.copy_((gram+gram.T)/2)
        self.s.add_(dt*g);self.w.add_(dw,alpha=dt);self.c.add_(dc,alpha=dt)

# Frozen initialization formulas (unchanged retained dictionaries).

def old_raw_features(initial, order):
    """Original Chebyshev/action-word dictionary, including redundant tails."""
    if order not in OLD_RANKS:
        raise ValueError('Old dictionary orders: 1,3,5,6,7,8,9')
    definition = build_dictionary(order)
    lower = initial.w.tanh()
    upper = (initial.M @ lower).tanh()
    reverse = (initial.M.T @ upper).tanh()
    cache = {}
    def word(value):
        if value not in cache:
            op = value.op
            if op == 'one': result = torch.ones_like(initial.c)
            elif op in ('g1', 'g2'): result = initial.w[:, int(op[-1])-1]
            elif op == 'action': result = (initial.M if value.population == 2 else initial.M.T) @ word(value.args[0])
            elif op in ('sin', 'cos', 'tanh'): result = getattr(torch, op)(word(value.args[0]))
            elif op == 'scale': result = float(value.scalar)*word(value.args[0])
            elif op == 'add': result = word(value.args[0])+word(value.args[1])
            elif op == 'multiply': result = word(value.args[0])*word(value.args[1])
            else: raise ValueError('Unsupported initialized word: '+op)
            cache[value] = result
        return cache[value]
    result = []
    for coordinates, exponents, tail in zip((torch.cat((lower, reverse), 1), upper),
            (definition.first_exponents, definition.second_exponents),
            (definition.first_tail, definition.second_tail)):
        terms = [torch.ones_like(coordinates), coordinates]
        for _ in range(1, order): terms.append(2*coordinates*terms[-1]-terms[-2])
        columns = []
        for powers in exponents:
            column = torch.ones_like(initial.c)
            for j, degree in enumerate(powers): column = column*terms[degree][:, j]
            columns.append(column)
        result.append(torch.stack(columns+[word(w) for w in tail], 1))
    return result


@torch.no_grad()
def frozen_bases(w, matrices, c, kind, order=1, ranks=None, seed=7319):
    """Build once in float64, then cast to the declared training precision.

    Default random ranks/draws reproduce scaling_dictionary's p<=9 protocol.
    Explicit ranks allow random baselines at arbitrary depth/input dimension.
    """
    n, depth, dtype = len(w), len(matrices)+1, w.dtype
    if isinstance(order, bool) or not isinstance(order, int) or order < 1:
        raise ValueError('Positive integer dictionary order required')
    if isinstance(seed, bool) or not isinstance(seed, int) or not 0 <= seed <= 2**64-2-100000:
        raise ValueError('Dictionary seed and appended seeds must fit uint64')
    if kind in ('dictionary_old', 'dictionary_flow'):
        if ranks is not None: raise ValueError('Historical dictionary ranks are fixed by order')
        if depth != 2 or w.shape[1] != 2:
            raise ValueError('Historical dictionaries require depth=2 and input dimension=2')
        initial = SimpleNamespace(w=w.double(), M=matrices[0].double(), c=c.double())
        if kind == 'dictionary_old': raw = old_raw_features(initial, order)
        else:
            if order not in range(1, 8): raise ValueError('Gradient-flow dictionary orders: 1..7')
            builder = d_raw_features if order <= 3 else d45_raw_features if order <= 5 else d7_raw_features
            *raw, _ = builder(initial, order)
        bases = []
        ridge = 1/(1024*(order+1)**2)
        for values in raw:
            gram = values.T @ values/n
            # Preserve the derivative builder's explicit symmetrization.
            if kind == 'dictionary_flow': gram = (gram+gram.T)/2
            chol = torch.linalg.cholesky(gram+ridge*torch.eye(values.shape[1], dtype=values.dtype, device=w.device))
            bases.append(torch.linalg.solve_triangular(chol, values.T, upper=False).T.contiguous())
    elif kind in ('gaussian', 'orthogonal'):
        legacy = ranks is None
        if legacy:
            if depth != 2 or order not in OLD_RANKS:
                raise ValueError('Supply ranks for random baselines outside the historical two-layer orders')
            ranks = OLD_RANKS[order]
        elif isinstance(ranks, int): ranks = [ranks]*depth
        if len(ranks) != depth or any(isinstance(k, bool) or not isinstance(k, int) or k < 1 for k in ranks):
            raise ValueError('Use one positive rank per hidden layer')
        bases = []
        for i, rank in enumerate(ranks):
            if kind == 'orthogonal' and rank > n: raise ValueError('Orthogonal rank cannot exceed width')
            generator = torch.Generator(device=w.device).manual_seed(seed+i)
            raw = torch.randn((n, (128, 21)[i] if legacy else rank), generator=generator, device=w.device, dtype=torch.float64)
            if legacy and rank > raw.shape[1]:
                generator.manual_seed(seed+100000+i)
                extra = torch.randn((n, (592, 34)[i]), generator=generator, device=w.device, dtype=torch.float64)
                raw = torch.cat((raw, extra), 1)
            raw = raw[:, :rank]
            bases.append(raw/raw.square().mean(0).sqrt() if kind == 'gaussian'
                         else math.sqrt(n)*torch.linalg.qr(raw, mode='reduced')[0])
    else: raise ValueError('Unknown frozen dictionary: '+kind)
    return [b.to(dtype).contiguous() for b in bases]


def g_mul(a, b):
    rows = max(a.shape[0], b.shape[0])
    if a.shape[0] not in (1, rows) or b.shape[0] not in (1, rows):
        raise ValueError('incompatible polynomial row counts')
    shape = (rows, a.shape[1] + b.shape[1] - 1)
    out = a.new_zeros(shape) if isinstance(a, torch.Tensor) else np.zeros(shape)
    for i in range(a.shape[1]):
        for j in range(b.shape[1]):
            out[:, i + j] += a[:, i] * b[:, j]
    return out


def g_ytimes(a, axis):
    shape = (a.shape[0], a.shape[1] + 1)
    out = a.new_zeros(shape) if isinstance(a, torch.Tensor) else np.zeros(shape)
    out[:, axis:axis + a.shape[1]] = a
    return out


def g_gaussian_rule(order):
    (z, w) = np.polynomial.hermite.hermgauss(order)
    return (np.sqrt(2) * z, w / np.sqrt(np.pi))


@lru_cache(maxsize=3)
def g_population_contractions(order=256):
    """All scalars needed by the label-leading W(t) coefficient through t8.

    UK[a,b,c,j] = <U_ab,[y1^(3-j)y2^j] K3_c>.
    hT[i,a,j] = <h_i,[y1^(4-j)y2^j] T_a>.
    VV[a,b,j] = [y1^(4-j)y2^j] <V_a,V_b>.
    beta[a,j] = [y1^(3-j)y2^j] beta_a.
    """
    (fixed_z, fixed_w) = np.polynomial.hermite.hermgauss(256)
    v = float(fixed_w @ np.tanh(np.sqrt(2) * fixed_z) ** 2 / np.sqrt(np.pi))
    (z, w) = g_gaussian_rule(order)
    grid = np.array(np.meshgrid(z, z, indexing='ij')).reshape(2, -1).T
    weights = np.outer(w, w).ravel()
    n = len(weights)

    def avg(x):
        return np.einsum('n,n...->...', weights, x)
    h = np.tanh(grid)
    ell = 1 - h * h
    lower_second = -2 * h * ell
    Y = np.sqrt(v) * grid
    H = np.tanh(Y)
    d = 1 - H * H
    e = -2 * H * d
    U = (d[:, :, None] * H[:, None, :]).reshape(n, 4)
    pairs = [(a, b) for a in range(2) for b in range(2)]
    DU = np.zeros((n, 4, 2))
    for (i, (a, b)) in enumerate(pairs):
        DU[:, i, b] += d[:, a] * d[:, b]
        DU[:, i, a] += e[:, a] * H[:, b]
    A = avg(DU)
    C = avg(U[:, :, None] * U[:, None, :])
    mu = h @ A.T
    gates = np.stack([ell[:, a] ** 2 for (a, b) in pairs], 1)
    Lmean = gates * mu
    LL = avg(gates[:, :, None] * gates[:, None, :] * (C[None] + mu[:, :, None] * mu[:, None, :]))
    P = avg(Lmean[:, :, None] * h[:, None, :])
    kappa = float(w @ (1 - np.tanh(z) ** 2) ** 2)
    ximean = Y @ P.T / v
    Fmean = ximean + (v + kappa) * U
    S = H
    R = [g_ytimes(Fmean[:, 2 * a:2 * a + 2], a) / 2 for a in range(2)]
    J = sum((g_ytimes(d[:, b:b + 1] * R[b], b) for b in range(2)))
    K = [d[:, a:a + 1] * J / 3 + e[:, a:a + 1] * g_mul(S, R[a]) for a in range(2)]
    KR = np.zeros((2, 4, n, 4))
    for (i, (c, b)) in enumerate(pairs):
        Ri = [np.zeros((n, 3)), np.zeros((n, 3))]
        Ri[c][:, c + b] = 0.5
        Ji = sum((g_ytimes(d[:, a:a + 1] * Ri[a], a) for a in range(2)))
        for a in range(2):
            KR[a, i] = d[:, a:a + 1] * Ji / 3 + e[:, a:a + 1] * g_mul(S, Ri[a])
    KY = np.zeros((2, 2, n, 4))
    upper_third = (6 * H * H - 2) * d
    for j in range(2):
        Rj = [g_ytimes((v + kappa) * DU[:, 2 * a:2 * a + 2, j], a) / 2 for a in range(2)]
        Jj = sum((g_ytimes(d[:, b:b + 1] * Rj[b] + (e[:, b:b + 1] * R[b] if j == b else 0), b) for b in range(2)))
        Sj = np.zeros_like(S)
        Sj[:, j] = d[:, j]
        for a in range(2):
            KY[a, j] = (d[:, a:a + 1] * Jj + (e[:, a:a + 1] * J if a == j else 0)) / 3
            KY[a, j] += e[:, a:a + 1] * (g_mul(Sj, R[a]) + g_mul(S, Rj[a]))
            if a == j:
                KY[a, j] += upper_third[:, a:a + 1] * g_mul(S, R[a])
    UK = np.empty((2, 2, 2, 4))
    for (i, (a, b)) in enumerate(pairs):
        for c in range(2):
            UK[a, b, c] = avg(U[:, i:i + 1] * K[c])
    beta = np.array([avg(H[:, a:a + 1] * J / 3 + g_mul(S, d[:, a:a + 1] * R[a])) for a in range(2)])
    VV = np.zeros((2, 2, 5))
    hT = np.zeros((2, 2, 5))
    hV = np.zeros((2, 2, 3))
    adjoint_response_error = 0.0
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for k in range(2):
                    (ia, ib) = (2 * a + c, 2 * b + k)
                    VV[a, b, a + b + c + k] += avg(gates[:, ia] * gates[:, ib] * (C[ia, ib] + mu[:, ia] * mu[:, ib])) / 4
        for i in range(2):
            for b in range(2):
                hV[i, a, a + b] += avg(h[:, i] * Lmean[:, 2 * a + b]) / 2
            f = h[:, i] * ell[:, a] ** 2
            fY = avg(f[:, None] * h)
            fxi = avg(f[:, None] * Lmean)
            conditional_cov = fxi - fY @ P.T / v
            fmean = Y @ fY / v
            fK = avg(fmean[:, None] * K[a])
            for j in range(4):
                fK += conditional_cov[j] * avg(KR[a, j])
            reverse_fK = np.zeros(4)
            for j in range(2):
                reverse_fK += fY[j] * avg(KY[a, j])
            for j in range(4):
                reverse_fK += fxi[j] * avg(KR[a, j])
            adjoint_response_error = max(adjoint_response_error, float(np.max(np.abs(reverse_fK - fK))))
            hT[i, a, a:a + 4] += fK / 4
            for b in range(2):
                lower = avg(f * h[:, b]) / 8
                for c in range(2):
                    for k in range(2):
                        hT[i, a, a + b + c + k] += lower * C[2 * b + c, 2 * a + k]
            for b in range(2):
                for c in range(2):
                    (i1, i2) = (2 * a + b, 2 * a + c)
                    value = avg(h[:, i] * lower_second[:, a] * ell[:, a] ** 2 * (C[i1, i2] + mu[:, i1] * mu[:, i2])) / 4
                    hT[i, a, 2 * a + b + c] += value
    joint = np.block([[v * np.eye(2), P.T], [P, LL]])
    return dict(order=order, v=v, tau=float(w @ np.tanh(np.sqrt(v) * z) ** 2), kappa=kappa, A=A, C=C, P=P, LL=LL, UK=UK, hT=hT, VV=VV, hV=hV, beta=beta, adjoint_response_error=adjoint_response_error, source_covariance_minimum_eigenvalue=float(np.linalg.eigvalsh(joint).min()))


@lru_cache(maxsize=1)
def d__variance_rules():
    values = []
    for order in (128, 256):
        (nodes, weights) = np.polynomial.hermite.hermgauss(order)
        values.append(float(weights @ np.tanh(np.sqrt(2.0) * nodes) ** 2 / np.sqrt(np.pi)))
    return tuple(values)


def d__quadrature_metadata():
    (coarse, fine) = d__variance_rules()
    return {'v': fine, 'v_128': coarse, 'v_256': fine, 'v_quadrature_absolute_discrepancy': abs(fine - coarse), 'v_quadrature': 'Gauss-Hermite 128/256; 256-node working value', 'v_target': 'E[tanh(G)^2], G standard normal', 'v_discrepancy_is_error_bound': False}


def d__validate_initial(initial, p):
    if isinstance(p, bool) or not isinstance(p, int) or p not in (1, 2, 3):
        raise ValueError('new dictionary level must be 1, 2, or 3')
    if initial.w.ndim != 2 or initial.w.shape[1] != 2:
        raise ValueError('initial.w must have shape (n,2)')
    n = initial.w.shape[0]
    if n < 1 or initial.M.shape != (n, n) or initial.c.shape != (n,):
        raise ValueError('inconsistent equal-width finite initial state')
    if initial.w.dtype not in (torch.float32, torch.float64):
        raise ValueError('initial state must use float32 or float64')
    for value in (initial.w, initial.c, initial.M):
        if value.dtype != initial.w.dtype or value.device != initial.w.device:
            raise ValueError('initial state dtype/device mismatch')
        if not bool(torch.isfinite(value).all()):
            raise ValueError('nonfinite initial state')


def d__initialized_fields(initial, p):
    h = torch.tanh(initial.w)
    H = torch.tanh(initial.M @ h)
    D = 1 - H.square()
    U = D[:, :, None] * H[:, None, :]
    fields = {'h': h, 'H': H, 'U': U}
    if p == 3:
        Q = (initial.M.T @ U.flatten(1)).reshape(-1, 2, 2)
        lower_gate_squared = (1 - h.square()).square()
        L = lower_gate_squared[:, :, None] * Q
        F = d__variance_rules()[1] * U + (initial.M @ L.flatten(1)).reshape(-1, 2, 2)
        fields.update(L=L, F=F)
    return fields


def d__collected_upper(H, F):
    (D, E) = (1 - H.square(), -2 * H * (1 - H.square()))

    def A(a, b, c):
        return D[:, a] * D[:, b] * F[:, b, c]

    def B(a, b, c):
        return H[:, c] * E[:, a] * F[:, a, b]
    return torch.stack((A(0, 0, 0) + 3 * B(0, 0, 0), A(0, 0, 1) + 3 * (B(0, 0, 1) + B(0, 1, 0)), A(0, 1, 0) + 3 * B(0, 1, 1), A(0, 1, 1), A(1, 0, 0), A(1, 0, 1) + 3 * B(1, 0, 0), A(1, 1, 0) + 3 * (B(1, 0, 1) + B(1, 1, 0)), A(1, 1, 1) + 3 * B(1, 1, 1)), dim=1)


@torch.no_grad()
def d_raw_features(initial, p):
    """Return (lower table, upper table, JSON-safe metadata), without ridge.

    Column order is lower h1,h2,[L11,L12,L21,L22], and upper
    U11,U12,U21,U22,[C1,...,C8]. Both first levels have identical tables.
    C1...C4 multiply y1^4,y1^3*y2,y1^2*y2^2,y1*y2^3 in the h1
    coefficient; C5...C8 multiply y1^3*y2,...,y2^4 in h2. The actual
    feedback coefficient has an additional common factor 1/6.
    """
    d__validate_initial(initial, p)
    fields = d__initialized_fields(initial, p)
    (lower, upper) = (fields['h'], fields['U'].flatten(1))
    if p == 3:
        lower = torch.cat((lower, fields['L'].flatten(1)), dim=1)
        upper = torch.cat((upper, d__collected_upper(fields['H'], fields['F'])), dim=1)
    if not bool(torch.isfinite(lower).all() and torch.isfinite(upper).all()):
        raise ValueError('nonfinite derivative dictionary')
    metadata = {'dictionary': 'derivative_collected_increment', 'p': p, 'maximum_weight_taylor_power': p + 1, 'normalized_probes': [[1.0, 0.0], [0.0, 1.0]], 'physical_probe_scale': float(np.sqrt(2.0)), 'K1': lower.shape[1], 'K2': upper.shape[1], 'lower_column_order': ['h1', 'h2'] + (['L11', 'L12', 'L21', 'L22'] if p == 3 else []), 'upper_column_order': ['U11', 'U12', 'U21', 'U22'] + ([f'C{i}' for i in range(1, 9)] if p == 3 else []), 'F_coefficient': 'v*U + W0*L', 'raw_column_rescaling': 'none', 'finite_jet_matching_claim': False, **d__quadrature_metadata()}
    return (lower.contiguous(), upper.contiguous(), metadata)






@lru_cache(maxsize=1)
def d45_population_moments():
    records = []
    v = d__variance_rules()[1]
    for order in (128, 256):
        (z, weights) = np.polynomial.hermite.hermgauss(order)
        weights = weights / np.sqrt(np.pi)
        h = np.tanh(np.sqrt(2.0) * z)
        H = np.tanh(np.sqrt(2.0 * v) * z)
        (p, d) = (1 - h * h, 1 - H * H)
        tau = float(weights @ (H * H))
        (d1, d2) = (float(weights @ d), float(weights @ (d * d)))
        H2d = float(weights @ (H * H * d))
        H2d2 = float(weights @ (H * H * d * d))
        lam_diag = float(weights @ (h * h * p * p)) * (d2 - 2 * H2d)
        lam_off = v * float(weights @ (p * p)) * d1 * d1
        lam = [[lam_diag, lam_off], [lam_off, lam_diag]]
        g = [[[H2d2 if a == b == k else tau * d2 if a == b else H2d * d1 for k in range(2)] for b in range(2)] for a in range(2)]
        records.append(dict(order=order, v=v, tau=tau, mean_d=d1, mean_d2=d2, mean_H2d=H2d, mean_H2d2=H2d2, lam=lam, g=g))
    (left, right) = records
    discrepancy = max((abs(left[k] - right[k]) for k in ('tau', 'mean_d', 'mean_d2', 'mean_H2d', 'mean_H2d2')))
    discrepancy = max(discrepancy, float(np.max(np.abs(np.array(left['lam']) - np.array(right['lam'])))))
    discrepancy = max(discrepancy, float(np.max(np.abs(np.array(left['g']) - np.array(right['g'])))))
    if discrepancy > 1e-09:
        raise ValueError('population moment quadrature gate failed')
    return dict(working=right, coarse=left, maximum_discrepancy=discrepancy, discrepancy_is_error_bound=False, method='one-dimensional Gauss-Hermite 128/256, working 256')


@torch.no_grad()
def d45_raw_features(initial, p):
    if isinstance(p, bool) or not isinstance(p, int) or p not in (4, 5):
        raise ValueError('extension order must be 4 or 5')
    (lower, upper, metadata) = d_raw_features(initial, 3)
    metadata.update(p=p, maximum_weight_taylor_power=p + 1, dictionary='derivative_collected_increment_extension', inherited_builder='new_dictionary.py', p4_span_equals_p3=True, population_moments=d45_population_moments())
    if p == 5:
        n = len(initial.w)
        (h, L) = (lower[:, :2], lower[:, 2:].reshape(n, 2, 2))
        H = torch.tanh(initial.M @ h)
        lower_gate = 1 - h.square()
        lower_second = -2 * h * lower_gate
        d = 1 - H.square()
        e = -2 * H * d
        third = (6 * H.square() - 2) * d
        U = upper[:, :4].reshape(n, 2, 2)
        Q = (initial.M.T @ U.flatten(1)).reshape(n, 2, 2)
        F = d__variance_rules()[1] * U + (initial.M @ L.flatten(1)).reshape(n, 2, 2)
        S = H
        R = [g_ytimes(F[:, a, :], a) / 2 for a in range(2)]
        q = [g_ytimes(lower_gate[:, a:a + 1] * Q[:, a, :], a) / 2 for a in range(2)]
        J = sum((g_ytimes(d[:, b:b + 1] * R[b], b) for b in range(2)))
        K3 = [d[:, a:a + 1] * J / 3 + e[:, a:a + 1] * g_mul(S, R[a]) for a in range(2)]
        collection_error = max((float((6 * K3[a] - upper[:, 4 + 4 * a:8 + 4 * a]).abs().max()) for a in range(2)))
        moments = d45_population_moments()['working']
        (T, E) = ([], [])
        for a in range(2):
            B2adj = initial.w.new_zeros((n, 4))
            for b in range(2):
                gram = initial.w.new_zeros((n, 3))
                (gram[:, 0], gram[:, 2]) = moments['g'][a][b]
                B2adj += g_ytimes(h[:, b:b + 1] * gram, b) / 2
            value = g_ytimes(lower_gate[:, a:a + 1].square() * (initial.M.T @ K3[a]), a) / 4 + g_ytimes(lower_gate[:, a:a + 1].square() * B2adj, a) / 4 + lower_second[:, a:a + 1] * g_mul(q[a], q[a])
            T.append(value)
        for a in range(2):
            contraction = initial.w.new_zeros((n, 4))
            for b in range(2):
                contraction += moments['lam'][a][b] * g_ytimes(g_ytimes(U[:, b, :], b), b)
            E.append(initial.M @ T[a] + d__variance_rules()[1] * g_ytimes(K3[a], a) / 4 + 3 * g_ytimes(contraction, a) / 8)
        K = sum((g_ytimes(d[:, b:b + 1] * E[b] + e[:, b:b + 1] * g_mul(R[b], R[b]) / 2, b) for b in range(2)))
        K5 = [d[:, a:a + 1] * K / 5 + e[:, a:a + 1] * g_mul(J, R[a]) / 3 + e[:, a:a + 1] * g_mul(S, E[a]) + third[:, a:a + 1] * g_mul(S, g_mul(R[a], R[a])) / 2 for a in range(2)]
        zero_error = max(float(T[0][:, 4].abs().max()), float(T[1][:, 0].abs().max()))
        if zero_error != 0:
            raise ValueError('symbolic polynomial divisibility failed')
        scale = max(1.0, float(upper.abs().max()))
        if collection_error > 1e-12 * scale:
            raise ValueError('inherited coefficient collection mismatch')
        lower = torch.cat((lower, 24 * T[0][:, :4], 24 * T[1][:, 1:]), dim=1)
        upper = torch.cat((upper, 120 * K5[0], 120 * K5[1]), dim=1)
        metadata.update(lower_column_order=metadata['lower_column_order'] + [f'24*T{a + 1}_y1^{4 - j}y2^{j}' for a in range(2) for j in range(a, a + 4)], upper_column_order=metadata['upper_column_order'] + [f'120*K5_{a + 1}_y1^{5 - j}y2^{j}' for a in range(2) for j in range(6)], added_lower_raw_scale=24, added_upper_raw_scale=120, raw_column_rescaling='inherited columns unchanged; new derivative coefficients times 4! and 5!', inherited_collection_absolute_error=collection_error, polynomial_divisibility_absolute_error=zero_error, scalar_contractions='population Gaussian moments, not empirical task contractions')
    if not bool(torch.isfinite(lower).all() and torch.isfinite(upper).all()):
        raise ValueError('nonfinite higher-order dictionary')
    metadata.update(K1=lower.shape[1], K2=upper.shape[1])
    return (lower.contiguous(), upper.contiguous(), metadata)






@lru_cache(maxsize=1)
def d7_moment_metadata():
    (coarse, fine) = (g_population_contractions(192), g_population_contractions(256))
    keys = ('v', 'tau', 'kappa', 'A', 'C', 'P', 'LL', 'UK', 'hT', 'VV', 'hV', 'beta')
    errors = {key: float(np.max(np.abs(np.asarray(coarse[key]) - np.asarray(fine[key])))) for key in keys}
    maximum = max(errors.values())
    parity = max(abs(fine['beta'][0, 1]), abs(fine['beta'][0, 3]), abs(fine['beta'][1, 0]), abs(fine['beta'][1, 2]), float(np.max(np.abs(fine['beta'][0] - fine['beta'][1, ::-1]))))
    if maximum > 1e-09 or parity > 2e-13 or fine['adjoint_response_error'] > 2e-13:
        raise ValueError('p7 population moment validation failed')
    return dict(method='two-dimensional Gauss-Hermite after analytic Gaussian innovation integration', resolution_orders=[192, 256], working_order=256, resolution_discrepancies=errors, maximum_discrepancy=maximum, discrepancy_is_error_bound=False, beta_parity_error=parity, beta_parity_projection='average the two equal diagonal/off-diagonal entries; set forbidden monomials to exact zero', beta_diagonal=float((fine['beta'][0, 0] + fine['beta'][1, 3]) / 2), beta_off_diagonal=float((fine['beta'][0, 2] + fine['beta'][1, 1]) / 2), adjoint_response_error=float(fine['adjoint_response_error']), source_covariance_minimum_eigenvalue=float(fine['source_covariance_minimum_eigenvalue']), contractions='initial Gaussian population UK,hT,VV,hV,C,beta; never empirical task contractions')


def d7__graph(initial, lower, upper, *, through_p7):
    """Ordinary homogeneous coefficient fields; exposed for scoped checks."""
    metadata = d7_moment_metadata()
    moments = g_population_contractions(256)
    to_tensor = lambda a: torch.as_tensor(a, dtype=initial.w.dtype, device=initial.w.device)
    n = len(initial.w)
    h = lower[:, :2]
    ell = 1 - h.square()
    m = -2 * h * ell
    lower_third = (6 * h.square() - 2) * ell
    H = torch.tanh(initial.M @ h)
    d = 1 - H.square()
    e = -2 * H * d
    f = (6 * H.square() - 2) * d
    fourth = 8 * H * d * (2 - 3 * H.square())
    U = upper[:, :4].reshape(n, 2, 2)
    L = lower[:, 2:6].reshape(n, 2, 2)
    F = d__variance_rules()[1] * U + (initial.M @ L.flatten(1)).reshape(n, 2, 2)
    Q = (initial.M.T @ U.flatten(1)).reshape(n, 2, 2)
    S = H
    sd = [S * d[:, a:a + 1] for a in range(2)]
    q = [g_ytimes(ell[:, a:a + 1] * Q[:, a, :], a) / 2 for a in range(2)]
    V = [g_ytimes(L[:, a, :], a) / 2 for a in range(2)]
    R = [g_ytimes(F[:, a, :], a) / 2 for a in range(2)]
    J = sum((g_ytimes(d[:, a:a + 1] * R[a], a) for a in range(2)))
    K3 = [upper[:, 4 + 4 * a:8 + 4 * a] / 6 for a in range(2)]
    T = [initial.w.new_zeros((n, 5)) for _ in range(2)]
    (T[0][:, :4], T[1][:, 1:]) = (lower[:, 6:10] / 24, lower[:, 10:14] / 24)
    K5 = [upper[:, 12 + 6 * a:18 + 6 * a] / 120 for a in range(2)]
    beta = [initial.w.new_zeros((1, 4)) for _ in range(2)]
    beta[0][0, 0] = beta[1][0, 3] = metadata['beta_diagonal']
    beta[0][0, 2] = beta[1][0, 1] = metadata['beta_off_diagonal']
    B = sum((g_mul(H[:, a:a + 1], beta[a]) for a in range(2)))
    (Z, Zplus) = ([], [])
    for a in range(2):
        bz = sum((g_mul(F[:, a, b:b + 1], beta[b]) for b in range(2)))
        sy = F[:, a, :]
        Z.append(-g_ytimes(bz, a) / 20 - g_mul(sy, beta[a]) / 5)
        Zplus.append(g_ytimes(bz, a) / 10 + 3 * g_mul(sy, beta[a]) / 8)
    common_M = sum((g_ytimes(d[:, b:b + 1] * Z[b], b) - g_mul(d[:, b:b + 1] * R[b], beta[b]) for b in range(2)))
    common_P = sum((g_ytimes(d[:, b:b + 1] * (Zplus[b] - Z[b]), b) + 11 * g_mul(d[:, b:b + 1] * R[b], beta[b]) / 4 for b in range(2)))
    M = [d[:, a:a + 1] * common_M / 6 - e[:, a:a + 1] * g_mul(B, R[a]) / 4 + e[:, a:a + 1] * g_mul(S, Z[a]) for a in range(2)]
    P = [d[:, a:a + 1] * common_P / 7 + 3 * e[:, a:a + 1] * g_mul(B, R[a]) / 5 + e[:, a:a + 1] * g_mul(S, Zplus[a] - Z[a] / 2) for a in range(2)]
    graph = dict(h=h, H=H, U=U, L=L, F=F, q=q, V=V, R=R, J=J, K3=K3, T=T, K5=K5, beta=beta, B=B, Z=Z, Zplus=Zplus, M=M, P=P)
    if not through_p7:
        return graph
    (C, UK) = (to_tensor(moments['C']), to_tensor(moments['UK']))
    (hT, VV, hV) = (to_tensor(moments[key]) for key in ('hT', 'VV', 'hV'))

    def pair_sd_sd(a, b):
        out = initial.w.new_zeros((1, 3))
        for c in range(2):
            for k in range(2):
                out[0, c + k] += C[2 * a + c, 2 * b + k]
        return out

    def pair_sd_K3(a, b):
        return sum((g_ytimes(UK[a, c, b][None, :], c) for c in range(2)))
    B2adj_sd = [sum((g_ytimes(g_mul(h[:, b:b + 1], pair_sd_sd(b, a)), b) / 2 for b in range(2))) for a in range(2)]
    J3 = [g_ytimes(initial.M.T @ K3[a] + B2adj_sd[a], a) for a in range(2)]
    P4 = [ell[:, a:a + 1] * J3[a] / 4 + m[:, a:a + 1] * g_mul(q[a], g_ytimes(initial.M.T @ sd[a], a)) / 4 for a in range(2)]
    T_recomputed = [ell[:, a:a + 1] * P4[a] + m[:, a:a + 1] * g_mul(q[a], q[a]) / 2 for a in range(2)]
    composition_error = max((float((T_recomputed[a] - T[a]).abs().max()) for a in range(2)))
    E = []
    for a in range(2):
        B2V = sum((g_ytimes(g_mul(sd[b], hV[b, a][None, :]), b) / 2 for b in range(2)))
        Fh = sum((g_ytimes((moments['v'] * K3[b] if a == b else torch.zeros_like(K3[b])) + g_mul(sd[b], hV[a, b][None, :]), b) / 4 for b in range(2)))
        E.append(initial.M @ T[a] + B2V + Fh)
    N = sum((g_ytimes(d[:, b:b + 1] * E[b] + e[:, b:b + 1] * g_mul(R[b], R[b]) / 2, b) for b in range(2)))
    T6 = []
    for a in range(2):
        B2adj_K3 = sum((g_ytimes(g_ytimes(g_mul(h[:, b:b + 1], pair_sd_K3(b, a)), a), b) / 2 for b in range(2)))
        Fadj_sd = sum((g_ytimes(g_ytimes(g_mul(h[:, b:b + 1], pair_sd_K3(a, b)) + g_mul(V[b], pair_sd_sd(b, a)), a), b) for b in range(2)))
        value = ell[:, a:a + 1].square() * (g_ytimes(initial.M.T @ K5[a], a) + B2adj_K3 + Fadj_sd / 4) / 6 + ell[:, a:a + 1] * m[:, a:a + 1] * g_mul(q[a], J3[a]) / 6 + 4 * m[:, a:a + 1] * g_mul(q[a], P4[a]) / 3 + lower_third[:, a:a + 1] * g_mul(q[a], g_mul(q[a], q[a])) / 3
        T6.append(value)
    E6 = []
    for a in range(2):
        B2T = sum((g_ytimes(g_mul(sd[b], hT[b, a][None, :]), b) / 2 for b in range(2)))
        FV = sum((g_ytimes(g_mul(K3[b], hV[b, a][None, :]) + g_mul(sd[b], VV[b, a][None, :]), b) / 4 for b in range(2)))
        Gh = sum((g_ytimes((moments['v'] * K5[b] if a == b else torch.zeros_like(K5[b])) + g_mul(K3[b], hV[a, b][None, :]) + g_mul(sd[b], hT[a, b][None, :]), b) / 6 for b in range(2)))
        E6.append(initial.M @ T6[a] + B2T + FV + Gh)
    O = sum((g_ytimes(d[:, a:a + 1] * E6[a] + e[:, a:a + 1] * g_mul(R[a], E[a]) + f[:, a:a + 1] * g_mul(R[a], g_mul(R[a], R[a])) / 6, a) for a in range(2)))
    K7 = [d[:, a:a + 1] * O / 7 + e[:, a:a + 1] * g_mul(N, R[a]) / 5 + g_mul(J, e[:, a:a + 1] * E[a] + f[:, a:a + 1] * g_mul(R[a], R[a]) / 2) / 3 + g_mul(S, e[:, a:a + 1] * E6[a] + f[:, a:a + 1] * g_mul(R[a], E[a]) + fourth[:, a:a + 1] * g_mul(R[a], g_mul(R[a], R[a])) / 6) for a in range(2)]
    zero_error = max(float(T6[0][:, 6].abs().max()), float(T6[1][:, 0].abs().max()))
    if zero_error != 0:
        raise ValueError('p7 symbolic y_a divisibility failed')
    scale = max(1.0, max((float(x.abs().max()) for x in T)))
    if composition_error > 1e-09 * scale:
        raise ValueError('p7 inherited lower composition mismatch')
    graph.update(P4=P4, E=E, N=N, T6=T6, E6=E6, O=O, K7=K7, composition_absolute_error=composition_error, divisibility_absolute_error=zero_error)
    return graph


@torch.no_grad()
def d7_raw_features(initial, p):
    if isinstance(p, bool) or not isinstance(p, int) or p not in (6, 7):
        raise ValueError('full-time extension order must be 6 or 7')
    (lower, upper, metadata) = d45_raw_features(initial, 5)
    graph = d7__graph(initial, lower, upper, through_p7=p == 7)
    m_columns = torch.stack((graph['M'][0][:, 1], graph['M'][0][:, 2], graph['M'][1][:, 3], graph['M'][1][:, 4]), dim=1)
    upper = torch.cat((upper, 720 * m_columns), dim=1)
    upper_names = metadata['upper_column_order'] + ['720*M1_y1^4y2', '720*M1_y1^3y2^2', '720*M2_y1^2y2^3', '720*M2_y1y2^4']
    lower_names = metadata['lower_column_order']
    if p == 7:
        tau = g_population_contractions(256)['tau']
        p_columns = torch.stack((graph['P'][0][:, 1], graph['P'][1][:, 4]), dim=1)
        lower = torch.cat((lower, 720 * graph['T6'][0][:, :6], 720 * graph['T6'][1][:, 1:]), dim=1)
        upper = torch.cat((upper, 5040 * tau * p_columns, 5040 * graph['K7'][0], 5040 * graph['K7'][1]), dim=1)
        lower_names = lower_names + [f'720*T6_{a + 1}_y1^{6 - j}y2^{j}' for a in range(2) for j in range(a, a + 6)]
        upper_names += ['5040*tau*P1_y1^4y2', '5040*tau*P2_y1y2^4'] + [f'5040*K7_{a + 1}_y1^{7 - j}y2^{j}' for a in range(2) for j in range(8)]
    if not bool(torch.isfinite(lower).all() and torch.isfinite(upper).all()):
        raise ValueError('nonfinite p7 derivative dictionary')
    metadata.update(dictionary='derivative_collected_full_time_increment_extension', inherited_builder='new_dictionary_p45.py', p=p, maximum_weight_taylor_power=p + 1, K1=lower.shape[1], K2=upper.shape[1], lower_column_order=lower_names, upper_column_order=upper_names, p6_span_equals_p5_claim=False, minimal_population_dimension_claim=False, full_lower_label_degrees_retained=True, p7_population_moments=d7_moment_metadata(), raw_column_rescaling='p5 prefix unchanged; M time6 times6!; T6 time6 times6!; tauP and K7 time7 times7!', added_M_raw_scale=720, added_T6_raw_scale=720 if p == 7 else None, added_P_raw_scale='5040*tau' if p == 7 else None, added_K7_raw_scale=5040 if p == 7 else None, new_dense_adjoint_query_count=12 if p == 7 else 0, new_dense_forward_query_count=12 if p == 7 else 0, inherited_p5_raw_prefix_exact=True, scalar_contractions='Gaussian population moments, never empirical task contractions')
    if p == 7:
        metadata.update(lower_composition_absolute_error=graph['composition_absolute_error'], polynomial_divisibility_absolute_error=graph['divisibility_absolute_error'])
    return (lower.contiguous(), upper.contiguous(), metadata)

# Dataset/configuration interface and endpoint reporting.

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rms(value):
    value = float(np.sqrt(np.mean(np.asarray(value, dtype=np.float64)**2)))
    return value if np.isfinite(value) else None


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')


def data_path(value, base):
    path = Path(value)
    return path if path.is_absolute() else base/path


def load_npz(path):
    with np.load(path, allow_pickle=False) as d: arrays = {k: d[k].copy() for k in d.files}
    for old, new in [('train_inputs', 'inputs'), ('train_labels', 'labels'),
                     ('validation_inputs', 'test_inputs'), ('validation_labels', 'test_labels')]:
        if new not in arrays and old in arrays: arrays[new] = arrays.pop(old)
    return arrays


def mnist_data(spec, base):
    """Official cached IDX files; balanced seeded train selection, separate test split."""
    root = data_path(spec['cache'], base)
    arrays, hashes = [], {}
    for filename, magic in [('train-images-idx3-ubyte', 2051), ('train-labels-idx1-ubyte', 2049),
                            ('t10k-images-idx3-ubyte', 2051), ('t10k-labels-idx1-ubyte', 2049)]:
        paths = [folder/(filename+suffix) for folder in (root, root/'MNIST/raw', root/'raw') for suffix in ('', '.gz')]
        path = next((p for p in paths if p.is_file()), None)
        if path is None: raise FileNotFoundError(f'MNIST cache lacks {filename}: {root}')
        payload = gzip.open(path, 'rb').read() if path.suffix == '.gz' else path.read_bytes()
        got, count = struct.unpack('>II', payload[:8])
        if got != magic: raise ValueError(f'Incorrect IDX format: {path}')
        shape = (count, *struct.unpack('>II', payload[8:16])) if magic == 2051 else (count,)
        arrays.append(np.frombuffer(payload, dtype=np.uint8, offset=16 if magic == 2051 else 8).reshape(shape))
        hashes[str(path.resolve())] = sha(path)
    train, train_digits, test, test_digits = arrays
    digits = spec.get('digits', [3, 8])
    if len(digits) != 2 or len(set(digits)) != 2 or any(d not in range(10) for d in digits):
        raise ValueError('Scalar-output MNIST uses two distinct digits')
    rng = np.random.default_rng(spec.get('seed', 20260924))
    count = spec.get('samples_per_class', 50)
    if not isinstance(count, int) or count < 1: raise ValueError('Positive samples_per_class required')
    ids = np.concatenate([rng.choice(np.flatnonzero(train_digits == d), count, replace=False) for d in digits])
    rng.shuffle(ids)
    test_ids = np.flatnonzero(np.isin(test_digits, digits))
    if 'test_per_class' in spec:
        count_test = spec['test_per_class']
        if not isinstance(count_test, int) or count_test < 1: raise ValueError('Positive test_per_class required')
        test_ids = np.concatenate([rng.choice(np.flatnonzero(test_digits == d), count_test, replace=False) for d in digits])
    def scale(images, indices):
        x = images[indices].reshape(len(indices), -1).astype(np.float64)
        if spec.get('normalization', 'l2') == 'l2':
            norms = np.linalg.norm(x, axis=1, keepdims=True)
            if np.any(norms == 0): raise ValueError('Cannot normalize zero image')
            return x/norms
        if spec['normalization'] == 'pixels': return x/255.
        raise ValueError('MNIST normalization must be l2 or pixels')
    return dict(inputs=scale(train, ids), labels=np.where(train_digits[ids] == digits[0], -1., 1.),
                test_inputs=scale(test, test_ids), test_labels=np.where(test_digits[test_ids] == digits[0], -1., 1.),
                train_ids=ids, test_ids=test_ids), hashes


def dataset(spec, base=HERE):
    kind = spec['kind']; hashes = {}
    fields = dict(npz={'path'}, mnist={'cache', 'digits', 'seed', 'samples_per_class', 'test_per_class', 'normalization'},
                  circle={'queries', 'query_offset', 'case', 'span_degrees', 'start_degrees', 'angles_degrees', 'labels', 'samples', 'frequency', 'phase', 'region_span_degrees'},
                  sphere={'samples', 'queries', 'seed', 'z_min', 'sampling', 'target', 'frequency', 'region_z_min'})
    if kind not in fields or set(spec)-fields[kind]-{'kind', 'name'}: raise ValueError('Unknown dataset kind/setting')
    if kind == 'npz':
        path = data_path(spec['path'], base); data = load_npz(path); hashes[str(path.resolve())] = sha(path)
    elif kind == 'mnist': data, hashes = mnist_data(spec, base)
    elif kind == 'circle':
        q = spec.get('queries', 8192)
        if not isinstance(q, int) or q < 1: raise ValueError('Positive queries required')
        query_angle = (np.arange(q)+spec.get('query_offset', .5))*2*np.pi/q
        if 'case' in spec and any(k in spec for k in ('angles_degrees', 'labels', 'samples', 'frequency', 'phase', 'span_degrees', 'start_degrees')):
            raise ValueError('A named circle case supplies its own training points and labels')
        if 'angles_degrees' in spec and 'samples' in spec: raise ValueError('Use literal angles or a sample count')
        literal = spec
        if 'case' in spec:
            cases = {}
            for filename in ('activation_circle_cases.json', 'compact_extra_circle_cases.json'):
                path = HERE/filename; hashes[str(path)] = sha(path)
                for key, value in json.loads(path.read_text()).items():
                    name = key.split('__')[-1]
                    selected = {k: value[k] for k in ('angles_degrees', 'labels')}
                    if name in cases and cases[name] != selected: raise ValueError('Ambiguous legacy circle case')
                    cases[name] = selected
            literal = cases[spec['case']]
        span = np.deg2rad(spec.get('span_degrees', 360.)); start = np.deg2rad(spec.get('start_degrees', 0.))
        if not 0 < span <= 2*np.pi: raise ValueError('Circle span must lie in (0,360]')
        if 'angles_degrees' in literal: angle = np.deg2rad(literal['angles_degrees'])
        else:
            m = spec.get('samples', 64)
            if not isinstance(m, int) or m < 1: raise ValueError('Positive samples required')
            angle = start+(np.arange(m)+.5)*span/m
        points = lambda a: np.column_stack((np.cos(a), np.sin(a)))
        target = lambda a: np.sqrt(2)*np.sin(spec.get('frequency', 24)*a+spec.get('phase', 0.))
        data = dict(inputs=points(angle), labels=np.asarray(literal['labels'], dtype=float) if 'labels' in literal else target(angle),
                    test_inputs=points(query_angle), region=(query_angle-start) % (2*np.pi) < np.deg2rad(spec.get('region_span_degrees', 90.)))
        if 'labels' not in literal: data['test_labels'] = target(query_angle)
    elif kind == 'sphere':
        m, q = spec.get('samples', 64), spec.get('queries', 8192)
        if any(not isinstance(v, int) or v < 1 for v in (m, q)): raise ValueError('Positive sample/query counts required')
        rng = np.random.default_rng(spec.get('seed', 20260926)); z_min = spec.get('z_min', -1.)
        if not -1 <= z_min < 1: raise ValueError('Sphere z_min must lie in [-1,1)')
        make = lambda z, a: np.column_stack((np.sqrt(1-z*z)*np.cos(a), np.sqrt(1-z*z)*np.sin(a), z))
        sampling = spec.get('sampling', 'uniform_z')
        if sampling not in ('normal', 'uniform_z'): raise ValueError('Unknown sphere sampling')
        if sampling == 'normal':
            if z_min != -1: raise ValueError('Normal-direction sampling uses the whole sphere')
            x = rng.standard_normal((m, 3)); x /= np.linalg.norm(x, axis=1, keepdims=True)
        else:
            u, v = rng.random((2, m)); x = make(z_min+(1-z_min)*u, 2*np.pi*v)
        i = np.arange(q); query = make(1-2*(i+.5)/q, i*np.pi*(3-np.sqrt(5)))
        name = spec.get('target', 'oscillatory')
        if name == 'xy': target = lambda a: np.sqrt(15)*a[:, 0]*a[:, 1]
        elif name == 'xyz': target = lambda a: np.sqrt(105)*np.prod(a, axis=1)
        elif name == 'oscillatory': target = lambda a: np.sin(spec.get('frequency', 6)*np.pi*a[:, 0])*np.sin(spec.get('frequency', 6)*np.pi*a[:, 1])
        else: raise ValueError('Unknown sphere target: '+name)
        truth, y = target(query), target(x)
        if name == 'oscillatory':
            scale = np.sqrt(np.mean(truth**2))
            if scale == 0: raise ValueError('Zero sphere target scale')
            truth, y = truth/scale, y/scale
        data = dict(inputs=x, labels=y, test_inputs=query, test_labels=truth, region=query[:, 2] >= spec.get('region_z_min', .5))
    else: raise ValueError('Unknown dataset kind: '+kind)
    x, y, query = (data[k] for k in ('inputs', 'labels', 'test_inputs'))
    if x.ndim != 2 or min(x.shape) < 1 or y.shape != (len(x),) or query.ndim != 2 or len(query) < 1 or query.shape[1] != x.shape[1]:
        raise ValueError('Expected nonempty inputs (M,d), labels (M,), test_inputs (Q,d)')
    if not all(np.isfinite(a).all() for a in (x, y, query)): raise ValueError('Nonfinite dataset')
    if 'test_labels' in data and (data['test_labels'].shape != (len(query),) or not np.isfinite(data['test_labels']).all()):
        raise ValueError('Invalid test labels')
    if 'region' in data and (data['region'].shape != (len(query),) or data['region'].dtype != bool): raise ValueError('Invalid query region mask')
    return data, hashes


def resolve(raw):
    unknown = set(raw)-{'model', 'optimizer', 'methods', 'datasets', 'device'}
    if unknown: raise ValueError('Unknown experiment fields: '+str(sorted(unknown)))
    for key, defaults in [('model', MODEL), ('optimizer', OPTIMIZER)]:
        if set(raw.get(key, {}))-set(defaults): raise ValueError('Unknown '+key+' setting')
    config = dict(model={**MODEL, **raw.get('model', {})}, optimizer={**OPTIMIZER, **raw.get('optimizer', {})},
                  methods=raw.get('methods', [{'kind': 'dense'}, *[dict(kind='closure', order=p) for p in (1, 2, 3)]]),
                  datasets=raw['datasets'], device=raw.get('device', 'cuda:0'))
    names = []
    for method in config['methods']:
        kind = method['kind']
        if kind not in KINDS: raise ValueError('Unknown method: '+kind)
        allowed={'dense':set(), 'closure':{'order'}, 'weighted_closure':{'order','clock'},
                 'dictionary_old':{'order'}, 'dictionary_flow':{'order'},
                 'gaussian':{'order','ranks','basis_seed'}, 'orthogonal':{'order','ranks','basis_seed'},
                 'trainable_dictionary':{'basis','order','ranks','basis_seed'}, 'low_rank':{'rank','factor_seed'}}
        if set(method)-allowed[kind]-{'kind','id'}: raise ValueError('Unknown setting for '+kind)
        base=method.get('basis','dictionary_flow') if kind=='trainable_dictionary' else kind
        if kind=='trainable_dictionary' and base not in ('dictionary_old','dictionary_flow','gaussian','orthogonal'):raise ValueError('Unknown dictionary basis')
        if base in ('dictionary_old','dictionary_flow') and ('ranks' in method or 'basis_seed' in method):raise ValueError('Historical dictionary is determined by order')
        if kind=='weighted_closure' and method.get('clock','response') not in ('response','residual'):raise ValueError('Unknown clock')
        if kind=='low_rank':
            rank=method.get('rank')
            ranks=[rank]*(config['model']['depth']-1) if isinstance(rank,int) else rank
            if isinstance(rank,bool) or not isinstance(ranks,(list,tuple)) or len(ranks)!=config['model']['depth']-1 or any(isinstance(r,bool) or not isinstance(r,int) or r<1 for r in ranks):raise ValueError('Positive rank per hidden link required')
            seed=method.get('factor_seed',20260924)
            if isinstance(seed,bool) or not isinstance(seed,int) or seed<0:raise ValueError('Invalid factor_seed')
        order = method.get('order', 1)
        if isinstance(order, bool) or not isinstance(order, int) or order < 1: raise ValueError('Positive integer order required')
        if base == 'dictionary_old' and order not in OLD_RANKS: raise ValueError('Old dictionary orders: '+str(list(OLD_RANKS)))
        if base == 'dictionary_flow' and order > 7: raise ValueError('Gradient-flow dictionary orders: 1..7')
        if base in ('gaussian', 'orthogonal'):
            seed = method.get('basis_seed', 7319)
            if isinstance(seed, bool) or not isinstance(seed, int) or not 0 <= seed <= 2**64-2-100000: raise ValueError('Invalid basis_seed')
            if 'ranks' in method:
                if 'order' in method: raise ValueError('Random bases use ranks or historical order, not both')
                ranks = [method['ranks']]*config['model']['depth'] if isinstance(method['ranks'], int) else method['ranks']
                if len(ranks) != config['model']['depth'] or any(isinstance(r, bool) or not isinstance(r, int) or r < 1 for r in ranks): raise ValueError('One positive rank per hidden layer required')
                if base == 'orthogonal' and max(ranks) > config['model']['width']: raise ValueError('Orthogonal rank exceeds width')
            elif config['model']['depth'] != 2 or order not in OLD_RANKS: raise ValueError('Supply random ranks outside historical depth-two orders')
            elif base == 'orthogonal' and max(OLD_RANKS[order]) > config['model']['width']: raise ValueError('Orthogonal rank exceeds width')
        names.append(method_name(method))
    if not names or len(set(names)) != len(names): raise ValueError('Use distinct nonempty method IDs')
    if sum(m['kind'] == 'dense' for m in config['methods']) > 1: raise ValueError('Use one dense reference per experiment')
    data_names = [s['name'] for s in config['datasets']]
    if not data_names or len(set(data_names)) != len(data_names): raise ValueError('Use distinct nonempty dataset names')
    for name in [*names, *data_names]:
        if not isinstance(name, str) or not name or Path(name).name != name or name in ('.', '..'): raise ValueError('Names must be simple path components')
    if config['model']['dtype'] not in ('float32', 'float64'): raise ValueError('dtype must be float32 or float64')
    m, o = config['model'], config['optimizer']
    if isinstance(m['seed'], bool) or not isinstance(m['seed'], int) or m['seed'] < 0: raise ValueError('Use a nonnegative integer model seed')
    for key, value in [('width', m['width']), ('depth', m['depth']), ('max_steps', o['max_steps']), ('block', o['block'])]:
        if isinstance(value, bool) or not isinstance(value, int) or value < 1: raise ValueError('Positive integer '+key+' required')
    for key in ('step', 'target_rms', 'max_seconds'):
        if not math.isfinite(o[key]) or o[key] <= 0: raise ValueError('Positive finite '+key+' required')
    activations = m['activation'] if isinstance(m['activation'], list) else [m['activation']]*m['depth']
    if len(activations) != m['depth'] or any(v not in ('relu', 'gelu', 'selu', 'tanh', 'sigmoid', 'silu') for v in activations): raise ValueError('Use a supported activation or one per hidden layer')
    if m['hidden_gain'] != 'unit_moment' and (not math.isfinite(m['hidden_gain']) or m['hidden_gain'] <= 0): raise ValueError('Invalid hidden_gain')
    if m['readout_std'] is not None and (not math.isfinite(m['readout_std']) or m['readout_std'] <= 0): raise ValueError('Invalid readout_std')
    return config


def construct(config, method, data):
    model = dict(config['model']); model['dtype'] = getattr(torch, model['dtype'])
    kind = method['kind']; order = method.get('order', 1)
    args = (data['inputs'], data['labels'])
    if kind in ('dense', 'closure'):
        return Flow(*args, **model, order=None if kind == 'dense' else order, device=config['device'], normalization='none')
    if kind=='low_rank':return LowRankFlow(*args,**model,rank=method['rank'],factor_seed=method.get('factor_seed',20260924),device=config['device'])
    if kind=='weighted_closure':return WeightedFlow(*args,**model,order=order,clock=method.get('clock','response'),device=config['device'])
    return FrozenFlow(*args, **model, kind=method.get('basis','dictionary_flow') if kind=='trainable_dictionary' else kind,
                      train_basis=kind=='trainable_dictionary', order=order, ranks=method.get('ranks'),
                      basis_seed=method.get('basis_seed', 7319), device=config['device'], normalization='none')


def method_name(method):
    kind=method['kind']
    default=kind if kind in ('dense','low_rank') else f"{kind}_P{method.get('order',1)}"
    return method.get('id',default)


def summarize(root):
    rows = []
    for folder in sorted(p.parent for p in root.glob('*/data.npz')):
        data = load_npz(folder/'data.npz'); records = []
        for path in sorted(folder.glob('*.json')):
            if path.name == 'provenance.json': continue
            r = json.loads(path.read_text()); file = folder/(r['model']+'.npz')
            if sha(file) != r['predictions_sha256'] or sha(folder/'data.npz') != r['data_sha256']: raise ValueError('Changed prediction/data archive')
            with np.load(file) as d: records.append((r, d['prediction'].copy(), d['test_prediction'].copy()))
        reference = next((v for v in records if v[0]['method']['kind'] == 'dense'), None)
        for r, train, query in records:
            if reference is not None and r['config'] != reference[0]['config']: raise ValueError('Mismatched dense configuration')
            train_rms = rms(train-data['labels']); dense_rms = rms(reference[1]-data['labels']) if reference else None
            rows.append(dict(dataset=folder.name, model=r['model'], train_rms=train_rms, dense_train_rms=dense_rms,
                             test_rms_vs_dense=rms(query-reference[2]) if reference else None,
                             test_rms_vs_target=rms(query-data['test_labels']) if 'test_labels' in data else None,
                             fitted_pair=all(v is not None and v <= r['config']['optimizer']['target_rms'] for v in (train_rms, dense_rms)),
                             status=r['fit']['status'], seconds=r['total_seconds']))
            for label, mask in [('region', data.get('region')), ('outside', ~data['region'] if 'region' in data else None)]:
                rows[-1][label+'_rms_vs_dense'] = rms((query-reference[2])[mask]) if reference and mask is not None and mask.any() else None
    if not rows: raise ValueError('No model records to summarize')
    with (root/'rms.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)
    print('| Dataset | Model | Train RMS | Test RMS vs dense | Both fitted |')
    print('|---|---|---:|---:|---|')
    fmt = lambda v: '—' if v is None else f'{v:.6f}'
    for r in rows: print(f"| {r['dataset']} | {r['model']} | {fmt(r['train_rms'])} | {fmt(r['test_rms_vs_dense'])} | {r['fitted_pair']} |")
    return rows


def run(config, out, base, prepare_only=False):
    torch.set_num_threads(1); torch.backends.cuda.matmul.allow_tf32 = False
    if torch.device(config['device']).type == 'cuda' and not prepare_only: torch.cuda.set_device(config['device'])
    prepared = [(spec, *dataset(spec, base)) for spec in config['datasets']]
    # Reject unsupported historical formulas before spending time on any model.
    for spec, data, _ in prepared:
        for method in config['methods']:
            basis=method.get('basis','dictionary_flow') if method['kind']=='trainable_dictionary' else method['kind']
            if basis in ('dictionary_old', 'dictionary_flow'):
                m = config['model']
                if (m['depth'] != 2 or data['inputs'].shape[1] != 2 or m['activation'] != 'tanh'
                        or m['hidden_gain'] != 1 or m['readout_std'] not in (None, 1/m['width'])):
                    raise ValueError(f"{method['kind']} requires 2D/two hidden tanh layers and historical initialization; dataset {spec['name']}")
    out.mkdir(parents=True, exist_ok=False)
    source_paths = [HERE/'compact_flow.py']
    source_paths += [ROOT/'code/pde'/n for n in ('observable_initialization.py', 'observable_words.py')]
    head = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, capture_output=True, text=True)
    write_json(out/'config.json', dict(config=config, command=shlex.join([sys.executable, *sys.argv]),
               git_head=head.stdout.strip() if head.returncode == 0 else None, cwd=os.getcwd(),
               source_sha256={str(p): sha(p) for p in source_paths}, torch=torch.__version__, numpy=np.__version__,
               gpu=torch.cuda.get_device_name(config['device']) if not prepare_only and torch.device(config['device']).type == 'cuda' else None,
               threads=torch.get_num_threads(), tf32=False))
    for spec, data, hashes in prepared:
        folder = out/spec['name']; folder.mkdir(); np.savez(folder/'data.npz', **data)
        write_json(folder/'provenance.json', dict(dataset=spec, source_sha256=hashes))
        if prepare_only: continue
        dense = None
        for method in sorted(config['methods'], key=lambda m: m['kind'] != 'dense'):
            started = time.perf_counter(); kind = method['kind']; order = method.get('order', 1)
            name = method_name(method)
            model = construct(config, method, data); fit = model.fit(**config['optimizer'])
            if not np.isfinite(fit['rms']): fit['rms'] = None
            prediction = model.predict(data['inputs']).cpu().numpy().astype(np.float64)
            query = data['test_inputs']
            curve = np.concatenate([model.predict(query[i:i+512]).cpu().numpy() for i in range(0, len(query), 512)]).astype(np.float64)
            if kind == 'dense': dense = curve.copy()
            file = folder/(name+'.npz'); np.savez(file, prediction=prediction, test_prediction=curve)
            record = dict(model=name, method=method, config=config, fit=fit, train_rms=rms(prediction-data['labels']),
                          test_rms_vs_dense=rms(curve-dense) if dense is not None else None,
                          test_rms_vs_target=rms(curve-data['test_labels']) if 'test_labels' in data else None,
                          basis_ranks=[b.shape[1] for b in model.bases] if isinstance(model, FrozenFlow) else None,
                          correction_ranks=[a.shape[1] for a,b in model.factors] if isinstance(model,LowRankFlow) else None,
                          integrator='Euler with exact history-coordinate transport' if isinstance(model,WeightedFlow) else 'simultaneous Euler',
                          data_sha256=sha(folder/'data.npz'), predictions_sha256=sha(file), total_seconds=time.perf_counter()-started)
            write_json(folder/(name+'.json'), record)
            print(json.dumps(dict(dataset=spec['name'], model=name, train_rms=record['train_rms'], seconds=record['total_seconds'])), flush=True)
            del model
    if not prepare_only: summarize(out)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--config', type=Path); p.add_argument('--experiment', nargs='+')
    p.add_argument('--out', type=Path); p.add_argument('--device'); p.add_argument('--prepare-only', action='store_true')
    p.add_argument('--summarize', type=Path); p.add_argument('--data', type=Path, nargs='+')
    for name, kind in [('width', int), ('depth', int), ('activation', str), ('seed', int), ('hidden-gain', str), ('readout-std', float)]:
        p.add_argument('--'+name, type=kind)
    for name, kind in [('step', float), ('target-rms', float), ('seconds', float), ('max-steps', int)]: p.add_argument('--'+name, type=kind)
    p.add_argument('--orders', type=int, nargs='+')
    p.add_argument('--check',action='store_true');p.add_argument('--gpu')
    a = p.parse_args()
    if a.check:
        self_check(a.gpu,a.out);return
    if a.gpu:p.error('--gpu is only for --check; use --device for experiments')
    if a.summarize is not None: summarize(a.summarize); return
    if a.out is None: p.error('--out is required')
    if a.config:
        if a.data or a.orders or any(getattr(a, k) is not None for k in ('width', 'depth', 'activation', 'seed', 'hidden_gain', 'readout_std', 'step', 'target_rms', 'seconds', 'max_steps')):
            p.error('With --config, put model/solver/data settings in the config')
        raw = json.loads(a.config.read_text()); base = a.config.resolve().parent
        if 'experiments' in raw:
            if set(raw) != {'experiments'}: p.error('Unknown catalog fields')
            if not a.experiment: p.error('Select catalog entries explicitly with --experiment NAME ...')
            selected = a.experiment
            if len(set(selected)) != len(selected) or any(not n or Path(n).name != n or n in ('.', '..') for n in selected): p.error('Use distinct simple experiment names')
            jobs = [(a.out/name, raw['experiments'][name]) for name in selected]
        else:
            if a.experiment: p.error('--experiment requires an experiments catalog')
            jobs = [(a.out, raw)]
    else:
        if a.experiment: p.error('--experiment requires --config')
        if not a.data: p.error('Supply --config or --data')
        model = {k: getattr(a, k) for k in MODEL if hasattr(a, k) and getattr(a, k) is not None}
        if 'hidden_gain' in model and model['hidden_gain'] != 'unit_moment': model['hidden_gain'] = float(model['hidden_gain'])
        optimizer = {k: getattr(a, k) for k in ('step', 'target_rms', 'max_steps') if getattr(a, k) is not None}
        if a.seconds is not None: optimizer['max_seconds'] = a.seconds
        methods = [dict(kind='dense') if k == 0 else dict(kind='closure', order=k, id=f'P{k}') for k in (a.orders or [0, 1, 2, 3])]
        jobs = [(a.out, dict(model=model, optimizer=optimizer, methods=methods,
                 datasets=[dict(name=v.stem, kind='npz', path=str(v.resolve())) for v in a.data]))]; base = Path.cwd()
    configs = [(out, resolve(raw)) for out, raw in jobs]
    for out, config in configs:
        if a.device: config['device'] = a.device
        run(config, out, base, a.prepare_only)

# Optional regression checks; production never imports archived engines.

def check_equations():
    from activation_moment_engine import ActivationDenseEngine, ActivationMomentEngine
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float32)
    generator = torch.Generator().manual_seed(741)
    inputs = torch.randn((8, 2), generator=generator, dtype=torch.float64)
    labels = torch.tensor([1., -1.] * 4, dtype=torch.float64)
    checks, maximum = 0, 0.

    def close(actual, expected):
        nonlocal checks, maximum
        torch.testing.assert_close(actual, expected, atol=3e-12, rtol=3e-12)
        assert bool(torch.isfinite(actual).all())
        maximum = max(maximum, float((actual - expected).abs().max()))
        checks += 1

    def make(depth, activation, order=None):
        return Flow(inputs, labels, width=7, depth=depth, activation=activation,
                    order=order, seed=773, device='cpu', dtype=torch.float64)

    # Same initialization and evolving physical/moment coordinates as the
    # established three-layer implementation, with three simultaneous steps.
    for activation in ('relu', 'gelu', 'selu'):
        for order in (None, 1, 2, 3):
            new = make(3, activation, order)
            arguments = (2, 7, inputs, labels) if order is None else (2, 7, order, inputs, labels)
            kind = ActivationDenseEngine if order is None else ActivationMomentEngine
            old = kind(*arguments, activation=activation, seed=773, device='cpu', dtype=torch.float64)
            state = old.initial_state()
            assert len(new.state) == len(state.tensors())
            for index in range(4):
                for actual, expected in zip(new.state, state.tensors()):
                    assert actual.dtype == torch.float64 and actual.device.type == 'cpu'
                    close(actual, expected)
                close(new.predict(inputs), old.predict(state, inputs))
                before = [value.clone() for value in new.state]
                velocity, reference = new.rhs(), old.rhs(state)
                for actual, expected in zip(velocity, reference.tensors()):
                    close(actual, expected)
                for actual, expected in zip(new.state, before):
                    close(actual, expected)
                if index < 3:
                    new.step(.0003)
                    state = state.add_scaled(reference, .0003)

    custom = (lambda z: torch.tanh(z) + .05 * z,
              lambda z: 1 - torch.tanh(z).square() + .05)
    # Autograd is independent of the implementation's manual backward pass.
    for depth in (1, 2, 4):
        for activation in ('tanh', custom):
            model = make(depth, activation)
            phi = torch.tanh if activation == 'tanh' else custom[0]
            for _ in range(3):
                parameters = [value.detach().clone().requires_grad_(True) for value in model.state]
                hidden = phi(parameters[0] @ inputs.T)
                for matrix in parameters[1:-1]:
                    hidden = phi(matrix @ hidden)
                prediction = parameters[-1] @ hidden / model.n
                loss = (prediction - labels).square().mean()
                gradients = torch.autograd.grad(loss, parameters)
                close(model.predict(inputs), prediction.detach())
                mobilities = [model.n] + [1] * (depth - 1) + [model.n]
                for actual, gradient, mobility in zip(model.rhs(), gradients, mobilities):
                    close(actual, -mobility * gradient)
                model.step(.0003)

    # With no hidden-to-hidden link, moments cannot alter depth-one dynamics.
    for activation in ('relu', 'gelu', 'selu', custom):
        for order in (1, 3):
            dense, closure = make(1, activation), make(1, activation, order)
            for _ in range(3):
                close(dense.predict(inputs), closure.predict(inputs))
                d, c = dense.rhs(), closure.rhs()
                close(d[0], c[0])
                close(d[1], c[1])
                close(c[-1], (closure.predict(inputs) - labels).square().mean().sqrt())
                dense.step(.0003)
                closure.step(.0003)
    # Configured initialization must preserve the same muP gradient equations.
    # Independent PyTorch activations cover deep models and arbitrary input dimension.
    phis={'relu':torch.relu,'gelu':torch.nn.functional.gelu,
          'selu':torch.nn.functional.selu,'tanh':torch.tanh,
          'sigmoid':torch.sigmoid,'silu':torch.nn.functional.silu}
    x3=torch.randn((8,3),generator=generator,dtype=torch.float64)
    for depth in (1,4,20):
        for activation,phi in phis.items():
            model=Flow(x3,labels,width=7,depth=depth,activation=activation,
                       hidden_gain='unit_moment',readout_std=1.,seed=773,
                       device='cpu',dtype=torch.float64)
            parameters=[v.detach().clone().requires_grad_(True) for v in model.state]
            h=phi(parameters[0]@x3.T)
            for matrix in parameters[1:-1]:h=phi(matrix@h)
            pred=parameters[-1]@h/model.n
            gradients=torch.autograd.grad((pred-labels).square().mean(),parameters)
            close(model.predict(x3),pred.detach())
            for actual,g,mobility in zip(model.rhs(),gradients,[model.n]+[1]*(depth-1)+[model.n]):
                close(actual,-mobility*g)
            for order in (1,2,3):
                closure=Flow(x3,labels,width=7,depth=depth,activation=activation,
                             order=order,hidden_gain='unit_moment',readout_std=1.,seed=773,
                             device='cpu',dtype=torch.float64)
                close(closure.predict(x3),model.predict(x3))
                for _ in range(2):closure.step(.00001)
                h=phi(closure.w@x3.T)
                for i,matrix in enumerate(closure.matrices):
                    A,B=closure.moments[2*i:2*i+2]
                    correction=sum((2*k+1)*(A[k]@B[k].T) for k in range(order))
                    W=matrix-2*correction/(closure.M*closure.n*(1+closure.s))
                    h=phi(W@h)
                close(closure.predict(x3),closure.c@h/closure.n)
    # Frozen coefficients use the Euclidean core gradient and muP outer gradients.
    for kind in ('gaussian', 'orthogonal'):
        for depth in (1, 2, 4):
            for activation, phi in phis.items():
                model = FrozenFlow(x3, labels, kind=kind, ranks=3, width=7, depth=depth,
                                   activation=activation, device='cpu', dtype=torch.float64)
                bases = [b.clone() for b in model.bases]
                for _ in range(3):
                    parameters = [v.clone().requires_grad_(True) for v in model.state]
                    h = phi(parameters[0]@x3.T)
                    for i, core in enumerate(parameters[1:-1]):
                        matrix = bases[i+1]@core@bases[i].T/model.n
                        h = phi(matrix@h)
                    pred = parameters[-1]@h/model.n
                    gradients = torch.autograd.grad((pred-labels).square().mean(), parameters)
                    close(model.predict(x3), pred.detach())
                    for actual, g, mobility in zip(model.rhs(), gradients, [model.n]+[1]*(depth-1)+[model.n]): close(actual, -mobility*g)
                    model.step(.0003)
                    for before, after in zip(bases, model.bases): close(after, before)
    print(f'PASS: {checks} CPU assertions; max absolute discrepancy {maximum:.3g}')
    return dict(assertions=checks, maximum_absolute_error=maximum)


def check_data():
    from quick_normalized_stress import data as old_stress
    from quick_sphere_flow import sphere_data
    maximum = 0.
    for kind in ('circle', 'sphere'):
        for support in ('full', 'patch'):
            spec = dict(kind=kind, name=kind+'_'+support)
            spec.update(dict(span_degrees=90 if support == 'patch' else 360) if kind == 'circle' else dict(z_min=.5 if support == 'patch' else -1.))
            new, _ = dataset(spec); old = old_stress(spec['name'])
            for k, value in zip(('inputs','labels','test_inputs','test_labels','region'), old):
                np.testing.assert_allclose(new[k], value, atol=2e-14, rtol=2e-14)
                if value.dtype != bool: maximum = max(maximum, float(np.max(np.abs(new[k]-value))))
    for target in ('xy', 'xyz'):
        new, _ = dataset(dict(kind='sphere', name=target, sampling='normal', seed=20260925, target=target, samples=16))
        for k, value in zip(('inputs','labels','test_inputs','test_labels'), sphere_data(target,16)):
            np.testing.assert_array_equal(new[k], value)
    # Reproduce the original frozen MNIST panel from its official raw files.
    cache = HERE.parents[1]/'data/generated/neural_response_memory_20260922/mnist_data01'
    mnist = 'unavailable'
    if (cache/'prepared.npz').exists():
        new, _ = dataset(dict(kind='mnist', name='mnist', cache=str(cache/'raw_cache'), samples_per_class=500))
        old = load_npz(cache/'prepared.npz')
        for k in ('inputs','labels','test_inputs','test_labels','train_ids'): np.testing.assert_array_equal(new[k],old[k])
        np.testing.assert_array_equal(new['test_ids'],old['validation_ids'])
        mnist = '1000 training and 1984 test rows: bitwise identical'
    print('PASS: dataset reproduction;', mnist)
    return dict(maximum_toy_difference=maximum, mnist=mnist)


def check_runner():
    import contextlib
    import io
    raw = dict(device='cpu', model=dict(width=12, depth=2, activation='tanh',dtype='float64'),
               optimizer=dict(step=.01,max_steps=3,block=2,max_seconds=10),
               methods=[dict(kind='dense')]+[dict(kind='closure',order=p) for p in (1,2,3)]
                       +[dict(kind=k,order=1) for k in ('dictionary_old','dictionary_flow','gaussian','orthogonal','trainable_dictionary')]
                       +[dict(kind='low_rank',rank=3)]
                       +[dict(kind='weighted_closure',order=p) for p in (1,2,3)],
               datasets=[dict(kind='circle',name='circle',case='quadrant_pairs',queries=32)])
    config = resolve(raw)
    with tempfile.TemporaryDirectory() as tmp, contextlib.redirect_stdout(io.StringIO()):
        root = Path(tmp)/'results'; run(config,root,HERE)
        rows = summarize(root); assert len(rows) == len(raw['methods'])
        dense = np.load(root/'circle/dense.npz')['test_prediction']
        for row in rows:
            query = np.load(root/'circle'/(row['model']+'.npz'))['test_prediction']
            np.testing.assert_allclose(row['test_rms_vs_dense'],np.sqrt(np.mean((query-dense)**2)),rtol=1e-14)
        no_dense = {**raw, 'methods':[dict(kind='closure',order=1)]}
        run(resolve(no_dense),Path(tmp)/'no_dense',HERE)
        assert summarize(Path(tmp)/'no_dense')[0]['test_rms_vs_dense'] is None
        changed = root/'circle/dense.npz'; changed.write_bytes(changed.read_bytes()+b'changed')
        try: summarize(root)
        except ValueError: pass
        else: raise AssertionError('Changed predictions accepted')
        for override in (dict(model={'width':0}),dict(optimizer={'step':0}),dict(methods=[dict(kind='dictionary_old',order=2)]),dict(methods=[dict(kind='dense'),dict(kind='dense',id='duplicate')]),
                         dict(methods=[dict(kind='low_rank',rank=0)]),dict(methods=[dict(kind='trainable_dictionary',basis='invalid')]),dict(methods=[dict(kind='weighted_closure',clock='invalid')])):
            try: resolve({**raw,**override})
            except ValueError: pass
            else: raise AssertionError('Invalid configuration accepted')
        try: dataset(dict(kind='circle',name='bad',frequncy=7))
        except ValueError: pass
        else: raise AssertionError('Dataset typo accepted')
    print('PASS: runner, saved metrics, missing dense, corruption and config validation')


def check_gpu(device):
    # Compare captured Euler to eager updates, including a final partial block.
    torch.cuda.set_device(device); torch.backends.cuda.matmul.allow_tf32=False
    records=[]; x=np.array([[1.,0.],[0.,1.],[-1.,0.],[0.,-1.]]);y=np.array([1.,-1.,-1.,1.])
    cases=[dict(kind='dense')]+[dict(kind='closure',order=p) for p in (1,2,3)]
    cases += [dict(kind=k,order=3) for k in ('dictionary_old','dictionary_flow','gaussian','orthogonal')]
    cases += [dict(kind='trainable_dictionary',order=3),dict(kind='low_rank',rank=12)]
    cases += [dict(kind='weighted_closure',order=p) for p in (1,2,3)]
    cases=[(method,2,'tanh') for method in cases]
    cases += [(method,4,activation) for activation in ('relu','gelu','selu') for method in
              (dict(kind='trainable_dictionary',basis='gaussian',ranks=12),dict(kind='low_rank',rank=12),dict(kind='weighted_closure',order=3))]
    for method,depth,activation in cases:
        config=resolve(dict(device=device,model=dict(width=2048,depth=depth,activation=activation),methods=[method],datasets=[dict(name='circle',kind='circle')]))
        data=dict(inputs=x if depth==2 else np.column_stack((x,np.full(len(x),.5))),labels=y)
        model=construct(config,method,data); reference=construct(config,method,data)
        before=[b.clone() for b in model.bases] if isinstance(model,FrozenFlow) and not model.train_basis else []
        dt=1/1024 if isinstance(model,WeightedFlow) else 1/64
        fit=model.fit(step=dt,target_rms=1e-20,max_seconds=30,max_steps=19,block=8)
        assert fit['steps']==19
        for _ in range(19): reference.step(dt)
        maximum=0.
        for a,b in zip(model.state,reference.state):
            torch.testing.assert_close(a,b,atol=2e-6,rtol=2e-6)
            maximum=max(maximum,float((a-b).abs().max()))
        for a,b in zip(before,getattr(model,'bases',[])): assert torch.equal(a,b)
        records.append(dict(method=method,depth=depth,activation=activation,fit=fit,maximum_state_difference=maximum))
        print('PASS GPU',method,'depth',depth,activation,'fit seconds',round(fit['seconds'],3),'difference',maximum,flush=True)
        del model,reference
    # Original builders use CUDA: compare every supported dictionary order.
    root=HERE.parents[1]
    sys.path.insert(0,str(root/'studies/random_dictionary_learned_circle_20260920'))
    sys.path.insert(0,str(root/'studies/gradient_flow_probe_dictionary_20260921'))
    import scaling_dictionary, new_dictionary, new_dictionary_p45, new_dictionary_p7
    from pde.observable_torch_p1 import TensorState, ClosureEngine
    dense=Flow(x,y,width=2048,depth=2,activation='tanh',device=device,dtype=torch.float64)
    initial=TensorState(dense.w,dense.c,dense.matrices[0])
    legacy_checks=[]
    for kind,orders in [('dictionary_old',list(OLD_RANKS)),('dictionary_flow',list(range(1,8))),('gaussian',list(OLD_RANKS)),('orthogonal',list(OLD_RANKS))]:
        for order in orders:
            actual=frozen_bases(dense.w,dense.matrices,dense.c,kind,order)
            if kind=='dictionary_flow':
                builder=new_dictionary if order<=3 else new_dictionary_p45 if order<=5 else new_dictionary_p7
                engine,state,_=builder.build(initial,order)
                expected=[engine.b1,engine.b2]
            else: expected=scaling_dictionary.dictionaries(initial,order,'ours' if kind=='dictionary_old' else kind)
            for a,b in zip(actual,expected): torch.testing.assert_close(a,b,atol=2e-10,rtol=2e-10)
            discrepancy=max(float((a-b).abs().max()) for a,b in zip(actual,expected))
            # Legacy core flow equivalence from the actual original producer.
            core=expected[1].T@(initial.M@expected[0])/dense.n
            old=ClosureEngine(expected[0],initial.w,expected[1],core,device=device,dtype=torch.float64)
            state=old.state(initial.w,initial.c,core)
            data=old.prepare_data(x,y)
            model=FrozenFlow(x,y,kind=kind,order=order,width=2048,depth=2,activation='tanh',device=device,dtype=torch.float64)
            for _ in range(2):
                reference=old.rhs(state,data)
                for a,b in zip(model.rhs(),(reference.w,reference.M,reference.c)): torch.testing.assert_close(a,b,atol=2e-10,rtol=2e-10)
                model.step(.001)
                state=TensorState(state.w+.001*reference.w,state.c+.001*reference.c,state.M+.001*reference.M)
            del model,old
            legacy_checks.append(dict(kind=kind,order=order,maximum_basis_difference=discrepancy))
        print('PASS original bases and equations:',kind,'orders',orders,flush=True)
    return dict(cuda_graph=records,legacy_dictionaries=legacy_checks,gpu=torch.cuda.get_device_name(device))


def check_added_methods():
    """Independent autograd, materialized-operator and original-producer oracles."""
    torch.set_num_threads(1)
    rng=np.random.default_rng(925);x=rng.normal(size=(4,3));y=np.array([1.,-1.,1.,-1.])
    phis={'tanh':torch.tanh,'relu':torch.relu,'gelu':torch.nn.functional.gelu,
          'selu':torch.nn.functional.selu,'sigmoid':torch.sigmoid,'silu':torch.nn.functional.silu}
    checks=0;maximum=0.
    def close(a,b,atol=3e-11,rtol=3e-11):
        nonlocal checks,maximum
        torch.testing.assert_close(a,b,atol=atol,rtol=rtol)
        assert bool(torch.isfinite(a).all())
        checks+=1;maximum=max(maximum,float((a-b).abs().max()))
    args=dict(width=7,device='cpu',dtype=torch.float64,readout_std=1.,seed=625)
    for depth in (1,2,4):
        for activation,phi in phis.items():
            for kind in ('trainable','low_rank'):
                model=(FrozenFlow(x,y,kind='gaussian',ranks=3,train_basis=True,depth=depth,activation=activation,**args)
                       if kind=='trainable' else LowRankFlow(x,y,rank=3,depth=depth,activation=activation,**args))
                # Move away from zero factors; check incoming+outgoing basis gradients.
                model.step(.001)
                p=[v.clone().requires_grad_(True) for v in model.state]
                if kind=='trainable':
                    w,c=p[0],p[depth];bases=p[depth+1:]
                    matrices=[bases[i+1]@core@bases[i].T/model.n for i,core in enumerate(p[1:depth])]
                    mobilities=[model.n]+[1]*(depth-1)+[model.n]*(depth+1)
                else:
                    w,c=p[:2];matrices=[W+a@b for W,a,b in zip(model.matrices,p[2::2],p[3::2])]
                    mobilities=[model.n,model.n]+[1]*(2*(depth-1))
                h=phi(w@model.inputs.T)
                for W in matrices:h=phi(W@h)
                pred=c@h/model.n
                # Depth-one trainable bases are unused and have zero velocity.
                gradients=torch.autograd.grad((pred-model.labels).square().mean(),p,allow_unused=True)
                close(model.predict(x),pred.detach())
                for actual,g,mobility,param in zip(model.rhs(),gradients,mobilities,p):close(actual,torch.zeros_like(param) if g is None else -mobility*g)

    def explicit(model,state):
        # Dense reconstruction and autograd adjoints; independent of fast factors/JVP.
        with torch.enable_grad():
            w,c=[v.detach().clone().requires_grad_(True) for v in state[:2]]
            moments=state[2:-2];G=state[-2];matrices=[]
            for W,u,h,(u0,h0) in zip(model.matrices,moments[::2],moments[1::2],model.prefix):
                S=torch.einsum('pna,pq,qma->nm',u,torch.linalg.inv(G),h)
                matrices.append(W-2/(model.n*model.M)*(S-u0@h0.T))
            hs=[];zs=[];z=w@model.inputs.T
            for i,spec in enumerate(model.activations):
                if i:z=matrices[i-1]@hs[-1]
                zs.append(z);hs.append(phis[spec](z))
            pred=c@hs[-1]/model.n;r=pred-model.labels
            ds=torch.autograd.grad(pred.sum(),zs)
            norm=r.square().mean().sqrt();safe=torch.where(norm>0,norm,torch.ones_like(norm))
            response=torch.cat([v.flatten() for i in range(model.depth-1) for v in (hs[i],model.n*ds[i+1]*(r/safe))])
            return [v.detach() for v in matrices],pred.detach(),response.detach()
    weighted_cases=0
    for depth in (2,4):
        for activation in phis:
            for order in (1,2,3):
                model=WeightedFlow(x,y,depth=depth,activation=activation,order=order,**args)
                dense=Flow(x,y,depth=depth,activation=activation,**args)
                close(model.predict(x),dense.predict(x))
                for _ in range(2):model.step(.0001)
                matrices,pred,_=explicit(model,model.state);close(model.predict(x),pred)
                identity=torch.eye(model.n,dtype=torch.float64)
                factors=model._factors()
                for i,W in enumerate(matrices):
                    close(model._apply(i,identity,factors),W)
                    close(model._apply(i,identity,factors,True),W.T)
                velocity=model.rhs();eps=1e-6
                plus=explicit(model,[a+eps*b for a,b in zip(model.state,velocity)])
                minus=explicit(model,[a-eps*b for a,b in zip(model.state,velocity)])
                terms=model._weighted_terms()
                for Wp,Wm,(left,right) in zip(plus[0],minus[0],terms[-1]):close((Wp-Wm)/(2*eps),left@right.T,atol=3e-7,rtol=3e-6)
                expected=(pred-model.labels).square().mean().sqrt()+((plus[2]-minus[2])/(2*eps)).norm()
                close(velocity[-1],expected,atol=3e-6,rtol=3e-6)
                assert float(torch.linalg.eigvalsh(model.G).min())>0
                weighted_cases+=1
    # P1 physical flow is clock independent, including the discrete update.
    response=WeightedFlow(x,y,depth=2,activation='tanh',order=1,**args)
    residual=WeightedFlow(x,y,depth=2,activation='tanh',order=1,clock='residual',**args)
    for _ in range(5):
        response.step(.01);residual.step(.01)
        for a,b in zip(response.state[:-1],residual.state[:-1]):close(a,b)
    # Zero residual is stationary, without division-by-zero gradients.
    dense=Flow(x,y,depth=2,activation='tanh',**args)
    zero=WeightedFlow(x,dense.predict(x),depth=2,activation='tanh',order=3,**args)
    for v in zero.rhs():close(v,torch.zeros_like(v))
    before=[v.clone() for v in zero.state];zero.step(.1)
    for a,b in zip(zero.state,before):close(a,b)
    # Transport step has the documented ODE as its first-order limit.
    model=WeightedFlow(x,y,depth=2,activation='tanh',order=3,**args)
    before=[v.clone() for v in model.state];rhs=model.rhs();errors=[]
    for dt in (2e-4,1e-4,5e-5):
        for a,b in zip(model.state,before):a.copy_(b)
        model.step(dt)
        errors.append(max(float(((a-b)/dt-v).abs().max()) for a,b,v in zip(model.state,before,rhs)))
    assert 1.8<errors[0]/errors[1]<2.2 and 1.8<errors[1]/errors[2]<2.2,errors
    # Compare the existing two-hidden-layer factor implementations directly.
    from factor_control_engine import FactorEngine
    sys.path.insert(0,str(ROOT/'studies/adaptive_response_compression_20260922'))
    import trainable_dictionary as original
    x2=x[:,:2]
    old=FactorEngine(2,7,3,x2,y,seed=625,device='cpu',dtype=torch.float64)
    old_state=old.initial_state()
    new=LowRankFlow(x2,y,rank=3,width=7,depth=2,activation='tanh',seed=625,device='cpu',dtype=torch.float64)
    for _ in range(3):
        reference=old.rhs(old_state)
        for a,b in zip(new.rhs(),reference.tensors()):close(a,b)
        new.step(.001);old_state=old_state.add_scaled(reference,.001)
    new=FrozenFlow(x2,y,kind='dictionary_flow',order=3,train_basis=True,width=7,depth=2,activation='tanh',seed=625,device='cpu',dtype=torch.float64)
    old_state=original.State(new.w.clone(),new.c.clone(),new.matrices[0].clone(),*[v.clone() for v in new.bases])
    for _ in range(3):
        reference=original.rhs(old_state,new.inputs,new.labels)
        for a,b in zip(new.rhs(),(reference.w,reference.M,reference.c,reference.b1,reference.b2)):close(a,b)
        new.step(.001);old_state=original.add(old_state,reference,.001)
    print('PASS added methods:',checks,'assertions;',weighted_cases,'weighted cases; step errors',errors,flush=True)
    return dict(assertions=checks,weighted_cases=weighted_cases,maximum_error=maximum,step_consistency_errors=errors)


def self_check(gpu=None,out=None):
    started=time.perf_counter()
    sys.modules.setdefault('compact_flow',sys.modules[__name__])
    sys.path.append(str(HERE/'legacy_experiments.zip'))
    result=dict(existing=check_equations(),added=check_added_methods(),datasets=check_data())
    check_runner()
    if gpu:result['gpu']=check_gpu(gpu)
    result.update(seconds=time.perf_counter()-started,source_sha256={Path(__file__).name:sha(__file__)},
                  torch=torch.__version__,numpy=np.__version__)
    if out:
        out.parent.mkdir(parents=True,exist_ok=True)
        with out.open('x') as f:json.dump(result,f,indent=2)
    print('PASS complete check in',round(result['seconds'],2),'seconds',flush=True)

if __name__ == "__main__": main()
