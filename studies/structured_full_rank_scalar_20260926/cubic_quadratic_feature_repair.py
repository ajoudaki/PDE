"""Exact initial hidden-feature Hessian in a scalar polynomial GF model.

One-time constructors may inspect weights; all returned objects contain
only scalar contractions. No training integration or experiment runs here.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import time

import numpy as np
from scipy.linalg import cho_solve

import cubic_minimal_mode_repair as minimal


RANK_RTOL = 1e-12


@dataclass
class QueryCoefficients:
    constant: np.ndarray  # (q,p)
    linear: np.ndarray  # (q,p,d)
    quadratic: np.ndarray | None  # (q,p,d,d)

    @property
    def nbytes(self):
        return sum(x.nbytes for x in (self.constant,self.linear,self.quadratic)
                   if x is not None)


@dataclass
class QuadraticFeatureModel:
    labels: np.ndarray
    readout_gram: np.ndarray
    coefficients: QueryCoefficients
    degree: int
    metadata: dict

    def __post_init__(self):
        self.labels = np.asarray(self.labels,dtype=float).copy()
        self.readout_gram = np.asarray(self.readout_gram,dtype=float).copy()
        self.m = len(self.labels)
        self.p = len(self.readout_gram)
        self.d = self.coefficients.linear.shape[-1]
        if self.degree not in (1,2):
            raise ValueError('degree must be 1 or 2')
        if (self.coefficients.constant.shape != (self.m,self.p)
                or self.coefficients.linear.shape != (self.m,self.p,self.d)
                or (self.degree == 2 and (
                    self.coefficients.quadratic is None
                    or self.coefficients.quadratic.shape != (self.m,self.p,self.d,self.d)))):
            raise ValueError('Coefficient shapes do not agree')
        self.cholesky = minimal._gram_factor(self.readout_gram)
        self.alpha = 2/self.m
        self.size = self.p+self.d
        self.blocks = (slice(0,self.p),slice(self.p,self.size))
        self.slices = self.blocks
        self.metadata = dict(self.metadata)

    @property
    def training_size(self):
        return self.size

    @property
    def coefficient_nbytes(self):
        return (self.labels.nbytes+self.readout_gram.nbytes+self.cholesky.nbytes
                +self.coefficients.nbytes)

    @property
    def model_degree(self):
        return self.degree

    def initial_state(self):
        return np.zeros(self.size)

    def unpack(self,state):
        return state[:self.p],state[self.p:]

    def solve_gram(self,rhs):
        return cho_solve((self.cholesky,True),rhs,check_finite=False)

    def _features(self,eta,coefficients):
        result = coefficients.constant+np.einsum('ail,l->ai',coefficients.linear,eta)
        if self.degree == 2:
            result = result+.5*np.einsum('ailk,l,k->ai',coefficients.quadratic,eta,eta)
        return result

    def _hidden_jacobian(self,v,eta):
        result = np.einsum('i,ail->al',v,self.coefficients.linear)
        if self.degree == 2:
            result = result+np.einsum('i,ailk,k->al',v,self.coefficients.quadratic,eta)
        return result

    def training_prediction(self,state):
        v,eta = self.unpack(state)
        return self._features(eta,self.coefficients) @ v

    def residual(self,state):
        return self.training_prediction(state)-self.labels

    def rhs(self,at,state):
        v,eta = self.unpack(state)
        features = self._features(eta,self.coefficients)
        residual = features @ v-self.labels
        hidden_jacobian = self._hidden_jacobian(v,eta)
        return np.concatenate((-self.alpha*self.solve_gram(features.T @ residual),
                               -self.alpha*hidden_jacobian.T @ residual))

    def kernel(self,state):
        v,eta = self.unpack(state)
        features = self._features(eta,self.coefficients)
        hidden_jacobian = self._hidden_jacobian(v,eta)
        return features @ self.solve_gram(features.T)+hidden_jacobian @ hidden_jacobian.T

    def readout_energy(self,state):
        v,_ = self.unpack(state)
        return float(v @ self.readout_gram @ v)

    def predict(self,state,coefficients):
        v,eta = self.unpack(state)
        if (coefficients.constant.ndim != 2
                or coefficients.constant.shape[1] != self.p
                or coefficients.linear.shape != (len(coefficients.constant),self.p,self.d)
                or (self.degree == 2 and (
                    coefficients.quadratic is None
                    or coefficients.quadratic.shape != (len(coefficients.constant),self.p,self.d,self.d)))):
            raise ValueError('Query coefficients do not match model')
        return self._features(eta,coefficients) @ v


def _workspace(w,W,inputs,labels,extra_mode):
    labels = minimal._array(labels,'labels',1)
    mode_labels = labels if extra_mode else np.zeros_like(labels)
    fields = minimal._coefficient_workspace(w,W,inputs,mode_labels)
    inputs,_,first,H,q,d,basis,gamma,beta,metadata = fields
    m,n = H.shape
    p = len(basis)
    beta_flat,gamma_flat = beta.reshape(m*p,n),gamma.reshape(m*p,n)
    S = ((beta_flat @ beta_flat.T/n).reshape(m,p,m,p)
         *(inputs @ inputs.T)[:,None,:,None]
         +(gamma_flat @ gamma_flat.T/n).reshape(m,p,m,p)
         *(first @ first.T/n)[:,None,:,None]).reshape(m*p,m*p)
    S = (S+S.T)/2
    values,vectors = np.linalg.eigh(S)
    largest = float(max(0.,values[-1]))
    if values[0] < -1e-10*max(largest,np.finfo(float).tiny):
        raise ValueError('Initial response Gram is not positive semidefinite')
    keep = values > RANK_RTOL*largest
    U = vectors[:,keep]/np.sqrt(values[keep])[None,:]
    metadata = dict(metadata)
    if not extra_mode:
        metadata.update(selection='initial_training_features',mode_status='not_requested')
    metadata.update(hidden_rank=int(np.count_nonzero(keep)),
                    hidden_candidate_dimension=m*p,
                    hidden_rank_rtol=RANK_RTOL,
                    hidden_eigenvalues=values.tolist(),
                    discarded_positive_eigenvalues=values[(~keep)&(values>0)].tolist(),
                    hidden_whitening_error=float(np.linalg.norm(U.T @ S @ U-np.eye(U.shape[1]))),
                    basis_whitening_sha256=hashlib.sha256(
                        basis.tobytes()+U.tobytes()).hexdigest())
    return inputs,labels,first,H,basis,gamma_flat,beta_flat,S,U,metadata


def _evaluate(w,W,inputs,first,basis,gamma,beta,U,queries,degree):
    queries = minimal._array(queries,'queries',2)
    if queries.shape[1] != inputs.shape[1]:
        raise ValueError('Queries and inputs must have the same dimension')
    m,n = first.shape
    p,rank = len(basis),U.shape[1]
    constants = np.empty((len(queries),p))
    linears = np.empty((len(queries),p,rank))
    hessians = np.empty((len(queries),p,rank,rank)) if degree == 2 else None
    # Only one query's derivative fields are resident at a time.
    for a,x in enumerate(queries):
        first_x = np.tanh(w @ x)
        H_x = np.tanh(W @ first_x)
        q,d = 1-first_x*first_x,1-H_x*H_x
        constants[a] = basis @ H_x/n
        dot = np.repeat(inputs @ x,p)
        t = U.T @ (beta*dot[:,None])
        dp = t*q[None,:]
        first_cross = np.repeat(first @ first_x/n,p)
        dz = dp @ W.T+(U*first_cross[:,None]).T @ gamma
        linears[a] = (basis*d[None,:]) @ dz.T/n
        if degree == 1:
            continue
        weight_second = basis*(-2*H_x*d)[None,:]
        weight_first = ((basis*d[None,:]) @ W)*(-2*first_x*q)[None,:]
        for i in range(p):
            hessians[a,i] = ((dz*weight_second[i]) @ dz.T
                              +(t*weight_first[i]) @ t.T)/n
        inner_readout = ((basis*d[None,:]) @ gamma.T/n).reshape(p,m,p)
        inner_first = first @ dp.T/n
        mixed = np.einsum('ibs,bsl,bk->ilk',inner_readout,U.reshape(m,p,rank),
                          inner_first,optimize=True)
        hessians[a] += mixed+mixed.transpose(0,2,1)
        hessians[a] = (hessians[a]+hessians[a].transpose(0,2,1))/2
    return QueryCoefficients(constants,linears,hessians)


def initialize_with_queries(w,W,inputs,labels,queries,*,extra_mode=False,degree=2):
    """Build all scalar arrays once, returning (model, query coefficients).

    extra_mode selects only the previously frozen terminal-cubic mode.
    degree=1 keeps identical basis selection and whitening but omits Hessian.
    """
    if degree not in (1,2) or isinstance(degree,bool):
        raise ValueError('degree must be 1 or 2')
    if not isinstance(extra_mode,(bool,np.bool_)):
        raise ValueError('extra_mode must be Boolean')
    started = time.monotonic()
    w,W = np.asarray(w,dtype=float),np.asarray(W,dtype=float)
    (inputs,labels,first,H,basis,gamma,beta,S,U,
     metadata) = _workspace(w,W,inputs,labels,extra_mode)
    training = _evaluate(w,W,inputs,first,basis,gamma,beta,U,inputs,degree)
    metadata['linear_contraction_error'] = float(np.max(np.abs(
        training.linear-(S @ U).reshape(len(inputs),len(basis),U.shape[1])),initial=0.))
    query = _evaluate(w,W,inputs,first,basis,gamma,beta,U,queries,degree)
    model = QuadraticFeatureModel(labels,basis @ basis.T/len(w),training,degree,metadata)
    model.metadata.update(degree=degree,extra_mode=bool(extra_mode),
                          constructor_seconds=time.monotonic()-started,
                          training_coefficient_bytes=model.coefficient_nbytes,
                          query_coefficient_bytes=query.nbytes)
    return model,query


def initialize(w,W,inputs,labels,*,extra_mode=False,degree=2):
    inputs_array = np.asarray(inputs)
    model,_ = initialize_with_queries(w,W,inputs,labels,
        np.empty((0,inputs_array.shape[1])),extra_mode=extra_mode,degree=degree)
    return model


def query_coefficients(w,W,inputs,queries,labels,*,extra_mode=False,degree=2):
    """Regenerate the fixed basis/whitening from initial data, no training."""
    _,coefficients = initialize_with_queries(w,W,inputs,labels,queries,
                                             extra_mode=extra_mode,degree=degree)
    return coefficients


def lifted_endpoint_diagnostic(w,W,inputs,labels,queries,state,*,extra_mode=False):
    """Posthoc exact-tanh evaluation at the scalar state's lifted weights.

    This explicitly uses initial width arrays, unlike all scalar evolution
    and prediction methods. No fitting, integration, or reference target
    enters. Compare its basis_whitening_sha256 with the model metadata.
    """
    w,W = np.asarray(w,dtype=float),np.asarray(W,dtype=float)
    (inputs,_,first,_,basis,gamma,beta,_,U,
     metadata) = _workspace(w,W,inputs,labels,extra_mode)
    state = minimal._array(state,'state',1)
    queries = minimal._array(queries,'queries',2)
    m,n = first.shape
    p,rank = len(basis),U.shape[1]
    if state.shape != (p+rank,) or queries.shape[1] != inputs.shape[1]:
        raise ValueError('State or query shape does not agree with construction')
    v,eta = state[:p],state[p:]
    theta = (U @ eta).reshape(m,p)
    dw = np.einsum('bi,bin,bk->nk',theta,beta.reshape(m,p,n),inputs)
    dW = np.einsum('bi,bin,bk->nk',theta,gamma.reshape(m,p,n),first)/n
    readout = v @ basis
    initial_first,initial_second,_,_ = minimal._initial_fields(w,W,queries)
    moved_first,moved_second,_,_ = minimal._initial_fields(w+dw,W+dW,queries)
    return dict(prediction=moved_second @ readout/n,
                basis_whitening_sha256=metadata['basis_whitening_sha256'],
                w_motion_rms=float(np.sqrt(np.mean(dw*dw))),
                W_motion_frobenius_over_sqrt_n=float(np.linalg.norm(dW)/np.sqrt(n)),
                readout_rms=float(np.sqrt(np.mean(readout*readout))),
                hidden_metric_norm=float(np.sqrt(np.sum(dw*dw)/n+np.sum(dW*dW))),
                first_feature_motion_rms=float(np.sqrt(np.mean((moved_first-initial_first)**2))),
                second_feature_motion_rms=float(np.sqrt(np.mean((moved_second-initial_second)**2))))
