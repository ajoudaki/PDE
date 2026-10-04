"""Projected feature-overlap feedback with optional average-tanh gates."""
import numpy as np
from scipy.linalg import cho_solve


class OverlapModel:
    def __init__(self,labels,G,S,query_gram,query_diagonal,query_response,*,gated=True):
        self.labels=np.asarray(labels,dtype=float).copy()
        self.G=np.asarray(G,dtype=float).copy()
        self.S=np.asarray(S,dtype=float).copy()
        self.m=len(self.labels);self.p=len(self.G)
        self.alpha=2/self.m
        self.gated=gated
        self.chol=np.linalg.cholesky(self.G)
        self.R0=np.eye(self.p,self.m)
        self.initial_gram=self.G[:self.m,:self.m]
        self.slack=1-np.diag(self.initial_gram)
        self.query_gram=np.asarray(query_gram).copy()
        self.query_diagonal=np.asarray(query_diagonal).copy()
        self.query_response=np.asarray(query_response).copy()
        self.query_count=len(self.query_diagonal)
        self.b0=self.solve(self.query_gram.T).T
        self.query_perp=self.query_diagonal-np.einsum('qi,qi->q',self.query_gram,self.b0)
        if self.S.shape!=(self.m,self.p,self.m,self.p):
            raise ValueError('Response Gram dimensions')
        if self.query_response.shape!=(self.query_count,self.p,self.m,self.p):
            raise ValueError('Query response dimensions')
        if min(self.slack)<=0 or min(1-self.query_diagonal)<=0 or min(self.query_perp)<-1e-10:
            raise ValueError('Initial Gram/gate realizability')
        self.training_size=self.p+self.p*self.m
        self.size=self.training_size+self.query_count*self.p
        self.blocks=(slice(0,self.p),slice(self.p,self.training_size),slice(self.training_size,self.size))

    def solve(self,b):
        return cho_solve((self.chol,True),b,check_finite=False)

    def initial_state(self):
        state=np.zeros(self.size)
        state[self.blocks[1]]=self.R0.ravel()
        state[self.blocks[2]]=self.b0.ravel()
        return state

    def unpack(self,state):
        return state[self.blocks[0]],state[self.blocks[1]].reshape(self.p,self.m),state[self.blocks[2]].reshape(self.query_count,self.p)

    def fields(self,state):
        v,R,b=self.unpack(state)
        Gv=self.G@v
        K=R.T@self.G@R
        r=R.T@Gv-self.labels
        g=(1-np.diag(K))/self.slack if self.gated else np.ones(self.m)
        return v,R,b,K,r,g,Gv

    def residual(self,state):
        v,R,_=self.unpack(state)
        return R.T@(self.G@v)-self.labels

    def rhs(self,at,state):
        v,R,b,K,r,g,Gv=self.fields(state)
        T=-self.alpha*np.einsum('a,c,c,f,aecf->ea',g,r,g,v,self.S,optimize=True)
        kappa=self.query_perp+np.einsum('qe,qe->q',b@self.G,b)
        gx=(1-kappa)/(1-self.query_diagonal) if self.gated else np.ones(self.query_count)
        Tx=-self.alpha*np.einsum('q,c,c,f,qecf->qe',gx,r,g,v,self.query_response,optimize=True)
        result=np.empty_like(state)
        result[self.blocks[0]]=-self.alpha*(R@r)
        result[self.blocks[1]]=self.solve(T).ravel()
        result[self.blocks[2]]=self.solve(Tx.T).T.ravel()
        return result

    def predict(self,state):
        v,_,b=self.unpack(state)
        return b@(self.G@v)

    def diagnostics(self,state):
        v,R,b,K,r,g,Gv=self.fields(state)
        q=float(v@Gv)
        kappa=self.query_perp+np.einsum('qe,qe->q',b@self.G,b)
        N=np.einsum('a,c,e,f,aecf->ac',g,g,v,v,self.S,optimize=True)
        return dict(readout_energy=q,max_train_diagonal=float(np.max(np.diag(K))),
                    max_query_diagonal=float(np.max(kappa)),min_train_gram_eigenvalue=float(np.linalg.eigvalsh(K)[0]),
                    min_kernel_eigenvalue=float(np.linalg.eigvalsh(K+N)[0]),
                    max_query_bound_excess=float(np.max(self.predict(state)**2-q)))


def algebra_check():
    rng=np.random.default_rng(932)
    m=3;p=4
    H=rng.normal(size=(p,30))*.3
    G=H@H.T/30
    F=rng.normal(size=(m*p,20))
    S=(F@F.T/20).reshape(m,p,m,p)
    model=OverlapModel(np.array([1.,-.5,.3]),G,S,G[:m],np.diag(G)[:m],S,gated=True)
    state=model.initial_state();state[:p]=rng.normal(size=p)*.1
    v,R,b,K,r,g,Gv=model.fields(state)
    d=model.rhs(0,state);dv,dR,db=model.unpack(d)
    N=np.einsum('a,c,e,f,aecf->ac',g,g,v,v,S)
    df=dR.T@Gv+R.T@G@dv
    errors=dict(gradient=float(np.max(abs(df+model.alpha*(K+N)@r))),
                energy=float(abs(2*v@G@dv+2*model.alpha*r@(model.labels+r))),
                alias=float(np.max(abs(model.predict(state)-(model.labels+r)))),
                alias_flow=float(np.max(abs(db-dR.T))))
    assert max(errors.values())<1e-12
    return errors


if __name__=='__main__':
    print(algebra_check())
