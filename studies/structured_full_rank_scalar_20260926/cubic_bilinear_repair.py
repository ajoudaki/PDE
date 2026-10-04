"""Aggregate bilinear feedback candidate; importing never trains.

The residual is derived from v and Theta. Training state count is m*m+m.
The full query decoder appends m**3 passive integrals.
"""
from dataclasses import dataclass
import numpy as np
from scipy.linalg import cho_solve


@dataclass
class BilinearQueryCoefficients:
    cross_gram: np.ndarray
    A: np.ndarray
    B: np.ndarray


@dataclass
class BilinearModel:
    labels: np.ndarray
    initial_gram: np.ndarray
    response_gram: np.ndarray

    def __post_init__(self):
        self.labels=np.asarray(self.labels,dtype=float).copy()
        self.initial_gram=np.asarray(self.initial_gram,dtype=float).copy()
        self.response_gram=np.asarray(self.response_gram,dtype=float).copy()
        self.m=len(self.labels)
        m=self.m
        if self.initial_gram.shape!=(m,m) or self.response_gram.shape!=(m,m,m,m):
            raise ValueError('Coefficient dimensions do not match labels')
        ev=np.linalg.eigvalsh(self.initial_gram)
        self.condition=float(ev[-1]/ev[0])
        if ev[0]<=0 or self.condition>1e12:
            raise ValueError('Initial Gram fails original conditioning gate')
        self.cholesky=np.linalg.cholesky(self.initial_gram)
        self.alpha=2/m
        self.slices=(slice(0,m),slice(m,m+m*m),slice(m+m*m,m+m*m+m**3))
        self.blocks=self.slices
        self.size=m+m*m+m**3
        self.training_size=m+m*m
        self.intrinsic_training_size=m+m*m

    def initial_state(self):
        return np.zeros(self.size)

    def unpack(self,state):
        return (state[self.slices[0]],state[self.slices[1]].reshape(self.m,self.m),
                state[self.slices[2]].reshape(self.m,self.m,self.m))

    def solve_gram(self,rhs):
        return cho_solve((self.cholesky,True),rhs,check_finite=False)

    def moving_cross(self,Theta):
        m=self.m
        return (self.response_gram.reshape(m*m,m*m)@Theta.ravel()).reshape(m,m).T

    def kernel(self,v,Theta):
        m=self.m
        M=self.moving_cross(Theta)
        N=np.einsum('qiac,i,c->qa',self.response_gram,v,v)
        transformed=self.cholesky.T@(np.eye(m)+self.solve_gram(M))
        return transformed.T@transformed+N,M,N

    def rhs(self,at,state):
        v,Theta,_=self.unpack(state)
        M=self.moving_cross(Theta)
        r=(self.initial_gram+M.T)@v-self.labels
        result=np.empty_like(state)
        result[self.slices[0]]=-self.alpha*(r+self.solve_gram(M@r))
        result[self.slices[1]]=(-self.alpha*np.outer(r,v)).ravel()
        result[self.slices[2]]=(r[:,None,None]*Theta[None,:,:]).ravel()
        return result

    def direct_training_prediction(self,state):
        v,Theta,_=self.unpack(state)
        M=self.moving_cross(Theta)
        return (self.initial_gram+M.T)@v

    def residual(self,state):
        return self.direct_training_prediction(state)-self.labels

    def predict(self,state,coefficients,query_A=None,query_B=None):
        if query_A is not None:
            coefficients=BilinearQueryCoefficients(coefficients,query_A,query_B)
        v,Theta,T=self.unpack(state)
        b=np.einsum('xibc,bc->xi',coefficients.B,Theta)
        direct=(coefficients.cross_gram+b)@v
        d=np.einsum('abc,aibc->i',T,self.response_gram)
        orthogonal=(np.einsum('xabc,abc->x',coefficients.A,T)
                    -coefficients.cross_gram@self.solve_gram(d))
        return direct-self.alpha*orthogonal


def algebra_check():
    """No ODE integration: differentiate exact model and check cubic terms."""
    rng=np.random.default_rng(8091)
    m=3
    L=rng.normal(size=(m,m))
    K0=L@L.T+np.eye(m)
    F=rng.normal(size=(m*m,m*m))
    S=(F@F.T).reshape(m,m,m,m)
    model=BilinearModel(rng.normal(size=m),K0,S)
    state=model.initial_state()
    state[model.slices[0]]=rng.normal(size=m)*.1
    state[model.slices[1]]=rng.normal(size=m*m)*.01
    state[model.slices[2]]=rng.normal(size=m**3)*.01
    v,Theta,T=model.unpack(state)
    r=model.residual(state)
    derivative=model.rhs(0,state)
    dv,dTheta,_=model.unpack(derivative)
    K,M,_=model.kernel(v,Theta)
    dM=np.einsum('bc,aqbc->qa',dTheta,S)
    df=(K0+M.T)@dv+dM.T@v
    gradient_gap=float(np.max(abs(df+model.alpha*K@r)))
    assert gradient_gap<1e-12
    train=BilinearQueryCoefficients(K0,S.transpose(1,0,2,3),S)
    alias_gap=float(np.max(abs(model.predict(state,train)-model.direct_training_prediction(state))))
    assert alias_gap<1e-12
    assert np.linalg.eigvalsh(K)[0]>0
    zero_model=BilinearModel(model.direct_training_prediction(state),K0,S)
    assert np.max(abs(zero_model.rhs(0,state)))==0
    # Cubic query formula with the next-order product explicitly removed.
    z=rng.normal(size=m)*.1
    J=.5*np.outer(z,z)
    skew=rng.normal(size=(m,m))*.01
    J+=(skew-skew.T)/2
    # Shuffle-consistent third integral for a two-segment path, constructed
    # by exact polynomial integration rather than arbitrary P.
    a=rng.normal(size=m)*.1;b=rng.normal(size=m)*.1
    z=a+b
    J=.5*np.outer(a,a)+np.outer(b,a)+.5*np.outer(b,b)
    P=(np.einsum('a,b,c->abc',a,a,a)/6
       +np.einsum('a,bc->abc',b,.5*np.outer(a,a))
       +.5*np.einsum('a,b,c->abc',b,b,a)
       +np.einsum('a,b,c->abc',b,b,b)/6)
    k=rng.normal(size=(4,m));A=rng.normal(size=(4,m,m,m));B=rng.normal(size=(4,m,m,m))
    coeff=BilinearQueryCoefficients(k,A,B)
    d=np.einsum('abc,aibc->i',P,S)
    v3=-model.alpha**3*model.solve_gram(d)
    check=model.initial_state()
    check[model.slices[0]]=-model.alpha*z+v3
    check[model.slices[1]]=(model.alpha**2*J).ravel()
    check[model.slices[2]]=(model.alpha**2*P).ravel()
    C=A+B+B.transpose(0,2,1,3)+B.transpose(0,2,3,1)
    cubic=-model.alpha*(k@z+model.alpha**2*np.einsum('xabc,abc->x',C,P))
    next_product=model.alpha**2*np.einsum('xibc,bc->xi',B,J)@v3
    cubic_gap=float(np.max(abs(model.predict(check,coeff)-next_product-cubic)))
    assert cubic_gap<1e-12
    return dict(gradient_identity_max_abs=gradient_gap,training_alias_max_abs=alias_gap,
                cubic_identity_max_abs=cubic_gap,minimum_kernel_eigenvalue=float(np.linalg.eigvalsh(K)[0]),
                training_runs=0)


if __name__=='__main__':
    import json
    print(json.dumps(algebra_check(),indent=2))
