"""Reviewer-one independent checks; only frozen edition code is imported."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json, math, platform, sys
from pde.mfp_compiler import Program, ProgramError
from pde.mfp_finite import evaluate_finite
from pde import mfp_expr as ex

EDITION=Path.cwd().resolve()
assert Path(sys.modules['pde.mfp_compiler'].__file__).resolve().is_relative_to(EDITION/'code')

# Exact finite expectation of mean(W_k ... W_1 1) by raw-entry Wick pairing.
# Vertices are summation indices; each pair identifies its row and column.
# This oracle has no Gaussian source/response recursion.
def wick_word(word):
    def pairings(rest):
        if not rest:
            yield ()
            return
        first=rest[0]
        for k in range(1,len(rest)):
            second=rest[k]
            if word[first][0] == word[second][0]:
                for tail in pairings(rest[1:k]+rest[k+1:]):
                    yield ((first,second),)+tail
    powers=Counter()
    for pairs in pairings(tuple(range(len(word)))):
        parent=list(range(len(word)+1))
        def root(i):
            while i!=parent[i]:i=parent[i]
            return i
        def merge(i,j):parent[root(i)]=root(j)
        for a,b in pairs:
            # word is in action order, edge k has input k and output k+1.
            ar,ac=(a,a+1) if word[a][1] else (a+1,a)
            br,bc=(b,b+1) if word[b][1] else (b+1,b)
            merge(ar,br);merge(ac,bc)
        exponent=len({root(i) for i in parent})-1-len(word)//2
        assert exponent<=0
        powers[exponent]+=1
    return dict(powers)

edges={'A':('a','b'),'B':('b','c'),'C':('c','a'),'D':('a','b')}
words=[]
def walk(kind,word,length):
    if len(word)==length:
        words.append(tuple(word));return
    for name,(source,target) in edges.items():
        if kind==source:walk(target,word+[(name,False)],length)
        if kind==target:walk(source,word+[(name,True)],length)
for length in (0,2,4,6):walk('a',[],length)
# Longer selected reuses, cycles and alternating parallel calls.
words += [tuple([('A',False),('A',True)]*k) for k in (4,5,6)]
words += [tuple([('A',False),('B',False),('C',False),('C',True),('B',True),('A',True)]*k) for k in (1,2)]
records=[]
for word in words:
    p=Program()
    kinds={k:p.vector_type(k) for k in ('a','b','c')}
    matrices={name:p.matrix(name,*endpoints) for name,endpoints in edges.items()}
    value=p.one('a')
    for name,transpose in word:value=(matrices[name].T if transpose else matrices[name]) @ value
    dag=p.compile(p.mean(value));terms=wick_word(word)
    assert dag.output==ex.const(terms.get(0,0)),(word,dag.output,terms)
    assert not dag.expectations
    records.append({'word':word,'finite_expectation_powers_of_n':terms,'limit':str(dag.output)})

# Independent polynomial perturbation, generic activation with nonzero fourth derivative.
class Poly:
    def __init__(self,c):self.c=tuple(F(v) for v in c)
    @staticmethod
    def of(x):return x if isinstance(x,Poly) else Poly([x])
    def __add__(self,x):
        x=self.of(x);return Poly([self[i]+x[i] for i in range(max(len(self.c),len(x.c)))])
    __radd__=__add__
    def __neg__(self):return Poly([-v for v in self.c])
    def __sub__(self,x):return self+-self.of(x)
    def __mul__(self,x):
        x=self.of(x);out=[F(0)]*(len(self.c)+len(x.c)-1)
        for i,a in enumerate(self.c):
            for j,b in enumerate(x.c):out[i+j]+=a*b
        return Poly(out)
    __rmul__=__mul__
    def __truediv__(self,x):return self*(F(1)/x)
    def __pow__(self,k):
        out=Poly([1])
        for _ in range(k):out=out*self
        return out
    def __getitem__(self,k):return self.c[k] if k<len(self.c) else F(0)

def mat(A,x,transpose=False):
    n=len(x);return [sum((A[j][i] if transpose else A[i][j])*x[j] for j in range(n)) for i in range(n)]
def mean(x):return sum(x)/len(x)
def activation(x):return 1+x+x**4

def raw(x,u,A,B,s):
    # Two named parallel edges; scalar feedback enters inside a nonlinear map.
    a=mat(A,x);coefficient=mean([v*v for v in x])+s
    h=[activation(v+coefficient*t) for v,t in zip(a,u)]
    back=mat(A,h,True)
    side=mat(B,[v*v for v in back])
    return mean([z*z+z*t for z,t in zip(side,h)])+coefficient**2

def act_derivative(order,x):
    return ((1 if order==0 else 0)+(x if order==0 else 1 if order==1 else 0)
            +(math.factorial(4)//math.factorial(4-order)*x**(4-order) if order<=4 else 0))

ad_results=[]
for n in (1,2,3):
    p=Program();a,b=p.vector_type('a'),p.vector_type('b')
    x,u=p.root('x',a),p.root('u',b);A,B=p.matrix('A',a,b),p.matrix('B',a,b);s=p.parameter('s')
    coefficient=p.mean(x*x)+s
    h=p.phi(A@x+coefficient*u)
    back=A.T@h;side=B@(back*back)
    O=p.mean(side*side+side*h)+coefficient**2
    xv=[F(i+1,7) for i in range(n)];uv=[F(1-i,5) for i in range(n)]
    av=[[F(i-j+1,9) for j in range(n)] for i in range(n)]
    bv=[[F(2*i+j-1,11) for j in range(n)] for i in range(n)];sv=F(2,9)
    evaluate=lambda v:evaluate_finite(v,n,{x:xv,u:uv},{A:av,B:bv},{s:sv},act_derivative)
    assert evaluate(O)==raw(xv,uv,av,bv,sv)
    grad=p.gradient(O,vectors=[x,u],matrices=[A,B],scalars=[s])
    expected_norm=F(0)
    for node,values in ((x,xv),(u,uv)):
        out=[]
        for i in range(n):
            altered=[Poly([v,int(j==i)]) for j,v in enumerate(values)]
            result=raw(altered if node is x else xv,altered if node is u else uv,av,bv,sv)
            out.append(n*result[1]);expected_norm+=n*result[1]**2
        assert evaluate(grad[node])==tuple(out)
    for matrix,values in ((A,av),(B,bv)):
        dense=[]
        for i in range(n):
            row=[]
            for j in range(n):
                altered=[[Poly([v,int(i==k and j==l)]) for l,v in enumerate(r)] for k,r in enumerate(values)]
                result=raw(xv,uv,altered if matrix is A else av,altered if matrix is B else bv,sv)
                row.append(result[1]);expected_norm+=result[1]**2
            dense.append(row)
        actual=[[sum(evaluate(c)*evaluate(left)[i]*evaluate(right)[j]/n for c,left,right in grad[matrix].terms) for j in range(n)] for i in range(n)]
        assert actual==dense
    gs=raw(xv,uv,av,bv,Poly([sv,1]))[1]
    assert evaluate(grad[s])==gs;expected_norm+=gs**2
    assert evaluate(p.directional(O,grad))==expected_norm
    ad_results.append({'width':n,'checked_raw_partial_count':2*n+2*n*n+1,'value':str(evaluate(O))})

# Explicit singular cancellation and roots with fixed shifts.
p=Program();a,b=p.vector_type('a'),p.vector_type('b');W=p.matrix('W',a,b)
z1,z2=W@p.one(a),W@p.one(a)
v=W.T@(z1**4-z2**4)
assert p.compile(p.inner(v,v)).output==ex.const(0)
p=Program();a=p.vector_type('a');x,y=p.roots(a,['x','y'],[[4,-6],[-6,9]],[2,-3])
assert p.compile(p.mean((3*x+2*y)**8)).output==ex.const(0)

# Python guide snippets are complete and run independently in the standalone edition.
text=(EDITION/'code/MFP_CALCULUS.md').read_text(); snippets=[]
for block in text.split('```python\n')[1:]:snippets.append(block.split('```',1)[0])
for i,code in enumerate(snippets):
    exec(compile(code,f'MFP_CALCULUS.md:snippet{i+1}','exec'),{})

out={'python':sys.version,'platform':platform.platform(),'import':sys.modules['pde.mfp_compiler'].__file__,
     'linear_wick_programs':len(records),'linear_wick_records':records,'independent_finite_AD':ad_results,
     'guide_python_snippets':len(snippets),'singular_checks':'passed','status':'PASS'}
Path('../reviewer_one/independent_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('linear_wick_records','independent_finite_AD')},indent=2))
