"""Finite scalar decorated-tree closure, TRUE_AGGREGATE_CONSTRUCTIVE §11.

The evolving state contains normalized scalar contractions and L only. Initial
independent Gaussian blocks may estimate integrals, then are discarded. G is
conditioned entrywise on |G| <= mark_bound; this is explicitly a bounded-G
population, not an exact unbounded Gaussian model. Reachability starts from all
feedback/output contractions and closes under every retained derivative child.
No particles, histogram masses, or initial-label coefficients evolve.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from functools import lru_cache
import json
import math
import time
import numpy as np

# A rooted encoding is (layer, sorted decorations, sorted child encodings).
# Every tree is canonicalized over all choices of root.
@lru_cache(maxsize=200000)
def flatten(tree):
    nodes, edges = [], []
    def visit(t, parent=-1):
        here=len(nodes); nodes.append((t[0], t[1]))
        if parent>=0: edges.append((parent,here))
        for child in t[2]: visit(child,here)
    visit(tree)
    return tuple(nodes),tuple(edges)

@lru_cache(maxsize=200000)
def canonical(tree):
    nodes,edges=flatten(tree)
    if len(nodes)==1: return tree
    adj=[[] for _ in nodes]
    for a,b in edges: adj[a].append(b);adj[b].append(a)
    def encode(v,p):
        return (nodes[v][0],nodes[v][1],tuple(sorted(encode(w,v) for w in adj[v] if w!=p)))
    return min(encode(v,-1) for v in range(len(nodes)))

def node(layer,decorations=(),children=()):
    return (layer,tuple(sorted(decorations)),tuple(sorted(children)))

@lru_cache(maxsize=200000)
def degree(tree):
    ns,es=flatten(tree)
    return len(es)+sum(len(d) for _,d in ns)

def graft(tree, vertex, color, replacement):
    ns,es=flatten(tree); ns=list(ns); es=list(es)
    dec=list(ns[vertex][1]);dec.remove(color)
    dec.extend(replacement[1]);ns[vertex]=(ns[vertex][0],tuple(sorted(dec)))
    def add(t,parent):
        v=len(ns);ns.append((t[0],t[1]));es.append((parent,v))
        for ch in t[2]:add(ch,v)
    for ch in replacement[2]:add(ch,vertex)
    adj=[[] for _ in ns]
    for a,b in es:adj[a].append(b);adj[b].append(a)
    def enc(v,p):return (ns[v][0],ns[v][1],tuple(sorted(enc(w,v) for w in adj[v] if w!=p)))
    return canonical(enc(0,-1))

class CompileLimit(RuntimeError): pass

class Closure:
    """Compiled scalar ODE. Runtime state is [q_T..., L]."""
    def __init__(self,u,labels,k=2,order=1,degree=9,mark_bound=3.,queries=None):
        self.u=np.asarray(u,float);self.labels=np.asarray(labels,float)
        self.queries=self.u if queries is None else np.asarray(queries,float)
        self.m=len(self.u);self.M=len(self.queries);self.k=int(k);self.order=int(order)
        self.cutoff=int(degree);self.mark_bound=float(mark_bound);self.Gscale=max(1.,mark_bound)
        if self.cutoff<9:raise ValueError('Degree at least 9 is needed for all exact feedback fields')
        if self.M<self.m or not np.allclose(self.queries[:self.m],self.u):
            raise ValueError('Queries must begin with training inputs')
        self.colors=[];self.color_ids={}
        def color(name):
            i=len(self.colors);self.colors.append(name);self.color_ids[name]=i;return i
        self.x=[color(('x',a)) for a in range(self.M)]
        self.beta={(j,b):color(('beta',j,b)) for j in range(order) for b in range(self.m)}
        self.h=[color(('h',a)) for a in range(self.M)]
        self.zeta=color(('zeta',))
        self.alpha={(j,b):color(('alpha',j,b)) for j in range(order) for b in range(self.m)}
        self.field_names=[];self.field_ids={}
        def field(name):
            i=len(self.field_names);self.field_names.append(name);self.field_ids[name]=i;return i
        self.R=[field(('R',b)) for b in range(self.m)]
        self.sig=field(('sigma',))
        self.s={(j,b,a):field(('s',j,b,a)) for j in range(order) for b in range(self.m) for a in range(self.M)}
        self.t={(j,l,b):field(('t',j,l,b)) for j in range(order) for l in range(self.m) for b in range(self.m)}
        self.D={(j,b,a):field(('D',j,b,a)) for j in range(order) for b in range(self.m) for a in range(self.M)}
        self.C={(a,b):field(('C',a,b)) for a in range(self.m,self.M) for b in range(self.m)}
        self.local={}
        # term = (numeric coefficient, (L power, sorted field IDs), rooted pattern)
        def term(c,p,fs,tr):return (float(c),(int(p),tuple(sorted(fs))),tr)
        self.local[self.zeta]=[term(-1/self.m,0,[self.R[b]],node(1,[self.h[b]])) for b in range(self.m)]+[term(-1,0,[self.sig],node(1,[self.zeta]))]
        for (j,b),col in self.beta.items():
            self.local[col]=[term(1,0,[self.sig],node(0,[self.x[b]])),term(-(j+1),0,[self.sig],node(0,[col]))]+[term(-(2*i+1),0,[self.sig],node(0,[self.beta[i,b]])) for i in range(j)]
        for (j,b),col in self.alpha.items():
            self.local[col]=[term(2/math.sqrt(self.m)*sgn,0,[self.R[b]],node(1,[self.zeta]+hs)) for sgn,hs in [(1,[]),(-1,[self.h[b]]*2)]]+[term(-(j+2),0,[self.sig],node(1,[col]))]+[term(-(2*i+1),0,[self.sig],node(1,[self.alpha[i,b]])) for i in range(j)]
        gram=self.queries@self.u.T; kg=self.k*self.Gscale
        for a in range(self.M):
            ts=[]
            for b in range(self.m):
                for sa,xa in [(1,[]),(-1,[self.x[a]]*2)]:
                    for sb,xb in [(1,[]),(-1,[self.x[b]]*2)]:
                        dec=xa+xb;fac=sa*sb*(1. if (a,b) in self.C else gram[a,b])
                        cfields=[self.C[a,b]] if (a,b) in self.C else []
                        if fac==0:continue
                        for sh,hb in [(1,[]),(-1,[self.h[b]]*2)]:
                            ts.append(term(-4/self.m*fac*sh*kg,2,[self.R[b]]+cfields,node(0,dec,[node(1,[self.zeta]+hb)])))
                        for j in range(order):
                            for l in range(self.m):
                                ts.append(term(8/(self.m*math.sqrt(self.m))*fac*(2*j+1),4,[self.R[b],self.t[j,l,b]]+cfields,node(0,dec+[self.beta[j,l]])))
            self.local[self.x[a]]=self._combine_local(ts)
        for a in range(self.M):
            ts=[]
            for sh,ha in [(1,[]),(-1,[self.h[a]]*2)]:
                # The G dot-x contribution grafts every first-gate derivative.
                for c,(p,fs),tr in self.local[self.x[a]]:
                    ts.append(term(sh*kg*c,p,fs,node(1,ha,[tr])))
                for j in range(order):
                    for l in range(self.m):
                        # dot-alpha + 2 sigma alpha cancels the normalization 2.
                        for sl,hl in [(1,[]),(-1,[self.h[l]]*2)]:
                            ts.append(term(-4/self.m*sh*sl*(2*j+1),2,[self.R[l],self.s[j,l,a]],node(1,ha+[self.zeta]+hl)))
                        if j:
                            ts.append(term(2/math.sqrt(self.m)*sh*(2*j+1)*j,2,[self.sig,self.s[j,l,a]],node(1,ha+[self.alpha[j,l]])))
                        for i in range(j):
                            ts.append(term(2/math.sqrt(self.m)*sh*(2*j+1)*(2*i+1),2,[self.sig,self.s[j,l,a]],node(1,ha+[self.alpha[i,l]])))
                        ts.append(term(-2/math.sqrt(self.m)*sh*(2*j+1),2,[self.D[j,l,a]],node(1,ha+[self.alpha[j,l]])))
            self.local[self.h[a]]=self._combine_local(ts)
        self.Ftrees=[node(1,[self.zeta,c]) for c in self.h]
        self.strees={key:node(0,[self.beta[key[:2]],self.x[key[2]]]) for key in self.s}
        self.ttrees={key:(node(1,[self.alpha[key[:2]],self.zeta]),node(1,[self.alpha[key[:2]],self.zeta,self.h[key[2]],self.h[key[2]]])) for key in self.t}
        self.Dterms={key:self.derivative(tr) for key,tr in self.strees.items()}
        self.trees=[];self.tree_ids={};self.rows=[];self.compiled=False
        self.penalty_mode="row_envelope"
        # Fixed envelope C(1+L^6), valid for every clipped low coordinate.
        bounds=np.ones(len(self.field_names));bounds[self.R]=2+np.max(np.abs(self.labels));bounds[self.sig]=2+np.max(np.abs(self.labels))
        for (a,b),fid in self.C.items():bounds[fid]=np.linalg.norm(self.queries[a])*np.linalg.norm(self.u[b])
        for fid in self.t.values():bounds[fid]=2.
        for key,terms in self.Dterms.items():
            bounds[self.D[key]]=sum(abs(c)*np.prod(bounds[list(fs)]) for c,(p,fs),tr in terms)
        self.penalty_C=max(1.,max(sum(abs(c)*np.prod(bounds[list(fs)]) for c,(p,fs),tr in ts) for ts in self.local.values()))

    @staticmethod
    def _combine_local(terms):
        out=defaultdict(float)
        for c,key,tr in terms:out[key,tr]+=c
        return [(c,key,tr) for (key,tr),c in out.items() if c!=0]

    def derivative(self,tree,max_degree=None):
        """Full exact symbolic derivative, including children beyond cutoff."""
        out=defaultdict(float)
        base_degree=degree(tree)-1
        ns,_=flatten(tree)
        for v,(_,decs) in enumerate(ns):
            for col in sorted(set(decs)):
                count=decs.count(col)
                for c,key,tr in self.local[col]:
                    if max_degree is not None and base_degree+degree(tr)>max_degree:
                        continue
                    out[key,graft(tree,v,col,tr)]+=c*count
        return [(c,key,tr) for (key,tr),c in out.items() if c!=0]

    def compile(self,max_states=100000,max_terms=1000000,seconds=60.):
        start=time.monotonic();nterms=0;dropped=0
        def add(tr):
            tr=canonical(tr)
            if tr not in self.tree_ids:
                if len(self.trees)>=max_states:raise CompileLimit('state_limit')
                self.tree_ids[tr]=len(self.trees);self.trees.append(tr)
        try:
            for tr in self.Ftrees:add(tr)
            for tr in self.strees.values():add(tr)
            for pair in self.ttrees.values():
                for tr in pair:add(tr)
            for ts in self.Dterms.values():
                for c,key,tr in ts:add(tr)
            cursor=0
            while cursor<len(self.trees):
                if time.monotonic()-start>=seconds:raise CompileLimit('time_limit')
                terms=self.derivative(self.trees[cursor],self.cutoff);row=[]
                for c,key,tr in terms:
                    if degree(tr)<=self.cutoff:
                        add(tr);row.append((c,key,self.tree_ids[tr]));nterms+=1
                        if nterms>=max_terms:raise CompileLimit('term_limit')
                    else:dropped+=1
                self.rows.append(row);cursor+=1
            self.compiled=True;reason='complete'
        except CompileLimit as e:reason=str(e)
        self.report={'status':reason,'complete':self.compiled,'states':len(self.trees),'processed_states':len(self.rows),'retained_terms':nterms,'omitted_terms':None,'omitted_terms_note':'Children beyond degree cutoff are discarded before canonicalization','seconds':time.monotonic()-start,'m':self.m,'queries':self.M,'k':self.k,'order':self.order,'degree':self.cutoff,'mark_bound':self.mark_bound,'penalty_C':self.penalty_C,'penalty_mode':self.penalty_mode,'runtime_representation':'scalar normalized decorated-tree contractions and L only','degree_counts':{d:sum(degree(t)==d for t in self.trees) for d in range(self.cutoff+1)}}
        if self.compiled:self._pack()
        return self

    def _pack(self):
        coeff_keys=[];coeff_ids={};rr=[];cc=[];tt=[];vv=[]
        def ci(key):
            if key not in coeff_ids:coeff_ids[key]=len(coeff_keys);coeff_keys.append(key)
            return coeff_ids[key]
        for row,terms in enumerate(self.rows):
            for c,key,col in terms:rr.append(row);cc.append(ci(key));tt.append(col);vv.append(c)
        self.coeff_keys=coeff_keys;self.row_index=np.asarray(rr,int);self.coeff_index=np.asarray(cc,int);self.child_index=np.asarray(tt,int);self.values=np.asarray(vv,float)
        self.degrees=np.array([degree(t) for t in self.trees],float)
        self.Fids=np.array([self.tree_ids[canonical(t)] for t in self.Ftrees])
        self.sids={key:self.tree_ids[canonical(tr)] for key,tr in self.strees.items()}
        self.tids={key:tuple(self.tree_ids[canonical(tr)] for tr in pair) for key,pair in self.ttrees.items()}
        self.Dpacked={key:[(c,ck,self.tree_ids[canonical(tr)]) for c,ck,tr in ts] for key,ts in self.Dterms.items()}

    def fields(self,q,L):
        """q must already be clipped; D uses all exact derivative contractions."""
        f=np.ones(len(self.field_names));R=2*q[self.Fids[:self.m]]-self.labels/L
        f[self.R]=R;f[self.sig]=np.sqrt(np.mean(R*R))
        for (a,b),idx in self.C.items():f[idx]=self.queries[a]@self.u[b]
        for key,idx in self.sids.items():f[self.s[key]]=q[idx]
        for key,(a,b) in self.tids.items():f[self.t[key]]=q[a]-q[b]
        for key,ts in self.Dpacked.items():
            f[self.D[key]]=sum(c*self.coefficient(ck,f,L)*q[idx] for c,ck,idx in ts)
        return f

    @staticmethod
    def coefficient(key,fields,L):
        p,fs=key
        return L**p*math.prod(fields[i] for i in fs)

    def rhs(self,time_value,state):
        if not self.compiled:raise RuntimeError('Incomplete compilation cannot evolve')
        q=np.clip(state[:-1],-1.,1.);L=float(state[-1]);fields=self.fields(q,L)
        coeff=np.array([self.coefficient(key,fields,L) for key in self.coeff_keys])
        vals=self.values*coeff[self.coeff_index]*q[self.child_index]
        out=np.empty_like(state);out[:-1]=np.bincount(self.row_index,weights=vals,minlength=len(q))
        if self.penalty_mode=="row_envelope":
            # Exact current retained-row envelope preserves |q|<=2; its
            # global majorant is C(1+L^6)deg(T) from the construction.
            envelope=np.bincount(self.row_index,weights=np.abs(self.values*coeff[self.coeff_index]),minlength=len(q))
        else:
            envelope=self.penalty_C*(1+L**6)*self.degrees
        out[:-1]-=envelope*(state[:-1]-q)
        out[-1]=fields[self.sig]*L
        return out

    def prediction(self,state):
        return 2*float(state[-1])*np.clip(state[self.Fids],-1.,1.)

    def tree_values(self,trees,coordinates,G):
        """Evaluate contractions on static blocks: result shape (trees,blocks).

        coordinates maps each color integer to a (blocks,k) array; G contains
        actual bounded mark values. This helper never belongs to the runtime.
        """
        G=np.asarray(G,float)/self.Gscale
        @lru_cache(maxsize=None)
        def message(tr):
            layer,decs,children=tr
            ans=np.ones(G.shape[:2])
            for col in decs:ans*=coordinates[col]
            for child in children:
                mat=G if layer==1 else G.transpose(0,2,1)
                ans*=np.einsum('bij,bj->bi',mat,message(child))/self.k
            return ans
        return np.asarray([np.mean(message(t),axis=1) for t in trees])

    def initialize_from_pool(self,pool,batch=128,queries=None):
        """Compute initial contractions once from supplied finite blocks.

        Uses the actual supplied c (normalized as zeta=c/2), unlike the exact
        zero-readout population initializer. Pool arrays are never stored.
        """
        if not self.compiled:raise RuntimeError('Incomplete compilation cannot initialize')
        initial_queries=self.queries if queries is None else np.asarray(queries,float)
        if initial_queries.shape!=self.queries.shape:raise ValueError('Query shape mismatch')
        started=time.monotonic();G=np.asarray(pool['G']);k=G.shape[1]
        if k!=self.k:raise ValueError('Pool block size mismatch')
        if np.max(np.abs(G))>self.mark_bound:raise ValueError('Pool violates explicit mark bound')
        c=np.asarray(pool['c']).reshape(-1,k)
        if np.max(np.abs(c))>2:raise ValueError('Readout normalization requires |c0| <= 2')
        w=np.asarray(pool['w']).reshape(-1,k,self.u.shape[1]);n=len(G)
        sums=np.zeros(len(self.trees));sums2=np.zeros(len(self.trees))
        active=[];simplified=[]
        def simplify(tr):
            layer,decs,children=tr;out=[]
            for col in decs:
                name=self.colors[col]
                if name[0]=='alpha' or (name[0]=='beta' and name[1]>0):return None
                out.append(self.x[name[2]] if name[0]=='beta' else col)
            ch=[]
            for kid in children:
                v=simplify(kid)
                if v is None:return None
                ch.append(v)
            return node(layer,out,ch)
        for i,tr in enumerate(self.trees):
            v=simplify(tr)
            if v is not None:active.append(i);simplified.append(v)
        for start in range(0,n,batch):
            sl=slice(start,min(start+batch,n));x=np.tanh(w[sl]@initial_queries.T);h=np.tanh(G[sl]@x)
            coordinates={**{col:x[:,:,a] for a,col in enumerate(self.x)},**{col:h[:,:,a] for a,col in enumerate(self.h)},self.zeta:c[sl]/2}
            vals=self.tree_values(simplified,coordinates,G[sl]);sums[active]+=vals.sum(axis=1);sums2[active]+=(vals*vals).sum(axis=1)
        values=sums/n;variance=np.maximum(0.,sums2/n-values*values)
        return np.r_[values,1.],{'method':'exact empirical initial contractions from supplied finite pool; pool discarded','initial_blocks':n,'initial_neurons':n*k,'nonzero_initial_coordinates':len(active),'seconds':time.monotonic()-started,'max_standard_error_population_estimate':float(np.max(np.sqrt(variance/n))),'finite_empirical_initialization_error':'floating point contraction evaluation only','population_initialization_error':'not certified; standard error is descriptive','initial_readout_max_abs':float(np.max(np.abs(c))),'mark_max_abs':float(np.max(np.abs(G))),'mark_bound':self.mark_bound}

    def initialize(self,samples=1024,seed=401,batch=128,confidence=.99):
        """Independent bounded-G Monte Carlo integration, discarded after use.

        Reports a simultaneous Hoeffding error bound and max standard error.
        This is not the theorem's exponentially accurate deterministic schedule.
        """
        if not self.compiled:raise RuntimeError('Incomplete compilation cannot initialize')
        started=time.monotonic();rng=np.random.default_rng(seed)
        sums=np.zeros(len(self.trees));sums2=np.zeros(len(self.trees))
        active=[];simplified=[]
        def simplify(tr):
            layer,decs,ch=tr;out=[]
            for col in decs:
                name=self.colors[col]
                if name[0] in ('zeta','alpha') or (name[0]=='beta' and name[1]>0):return None
                out.append(self.x[name[2]] if name[0]=='beta' else col)
            kids=[]
            for kid in ch:
                result=simplify(kid)
                if result is None:return None
                kids.append(result)
            return node(layer,out,kids)
        for i,tr in enumerate(self.trees):
            v=simplify(tr)
            if v is not None:active.append(i);simplified.append(v)
        for start in range(0,samples,batch):
            n=min(batch,samples-start);G=rng.standard_normal((n,self.k,self.k))/np.sqrt(self.k)
            bad=np.abs(G)>self.mark_bound
            while bad.any():
                G[bad]=rng.standard_normal(int(bad.sum()))/np.sqrt(self.k);bad=np.abs(G)>self.mark_bound
            w=rng.standard_normal((n,self.k,self.u.shape[1]));x=np.tanh(w@self.queries.T);h=np.tanh(G@x)
            coords={**{col:x[:,:,a] for a,col in enumerate(self.x)},**{col:h[:,:,a] for a,col in enumerate(self.h)}}
            vals=self.tree_values(simplified,coords,G)
            sums[active]+=vals.sum(axis=1);sums2[active]+=(vals*vals).sum(axis=1)
        q=sums/samples;var=np.maximum(0.,sums2/samples-q*q)
        bound=math.sqrt(2*math.log(2*max(1,len(active))/(1-confidence))/samples)
        metadata={'method':'independent initial integral Monte Carlo; blocks discarded','samples':samples,'seed':seed,'confidence':confidence,'simultaneous_hoeffding_absolute_bound':min(2.,bound),'max_standard_error':float(np.max(np.sqrt(var/samples))),'nonzero_initial_coordinates':len(active),'seconds':time.monotonic()-started,'target_G':'entrywise-conditioned Gaussian N(0,1/k)','initial_w':'untruncated Gaussian N(0,1)','initial_c':'exactly zero','theorem_initialization_schedule_met':False}
        return np.r_[np.clip(q,-1.,1.),1.],metadata


def compile_closure(u,labels,k=2,order=1,degree=9,mark_bound=3.,queries=None,max_states=100000,max_terms=1000000,seconds=60.):
    return Closure(u,labels,k,order,degree,mark_bound,queries).compile(max_states,max_terms,seconds)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--m',type=int,default=1);p.add_argument('--k',type=int,default=2);p.add_argument('--degree',type=int,default=9);p.add_argument('--seconds',type=float,default=60.);p.add_argument('--output');args=p.parse_args()
    angles=np.array([0.,.9])[:args.m]
    u=np.column_stack((np.cos(angles),np.sin(angles)));labels=np.cos(angles)
    model=compile_closure(u,labels,k=args.k,degree=args.degree,seconds=args.seconds)
    report=json.dumps(model.report,indent=2);print(report,flush=True)
    if args.output:
        from pathlib import Path
        dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(report+'\n')
