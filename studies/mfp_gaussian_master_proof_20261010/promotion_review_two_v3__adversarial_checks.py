"""Reviewer TWO: independent rational finite-array and source-law attacks."""
from fractions import Fraction as F
from math import factorial
import json
import platform
import sys

from pde.mfp_compiler import Program, ProgramError
from pde.mfp_finite import evaluate_finite
from pde import mfp_expr as ex


class Polynomial:
    """Independent degree-three coefficient ring, no candidate derivative code."""
    def __init__(self, coeff):
        c = list(coeff)
        self.c = tuple(F(c[k]) if k < len(c) else F(0) for k in range(4))
    @staticmethod
    def of(x):
        return x if isinstance(x, Polynomial) else Polynomial([x])
    def __add__(self, other):
        other = self.of(other)
        return Polynomial(a+b for a,b in zip(self.c, other.c))
    __radd__ = __add__
    def __neg__(self):
        return Polynomial(-a for a in self.c)
    def __sub__(self, other):
        return self + -self.of(other)
    def __mul__(self, other):
        other = self.of(other)
        return Polynomial(sum(self.c[j]*other.c[k-j] for j in range(k+1)) for k in range(4))
    __rmul__ = __mul__
    def __truediv__(self, scalar):
        return self * (F(1)/scalar)
    def __pow__(self, degree):
        ans = self.of(1)
        for _ in range(degree):
            ans = ans*self
        return ans


def mv(w, x, transpose=False):
    n = len(x)
    return [sum((w[j][i] if transpose else w[i][j])*x[j] for j in range(n)) for i in range(n)]


def mean(x):
    return sum(x)/len(x)


def pair(x,y):
    return mean([a*b for a,b in zip(x,y)])


def primal(x,u,v,s,W,V,T,Q):
    y = mv(W,x)
    q = [a+b for a,b in zip(mv(V,y),v)]
    r = mv(T,q)
    back = mv(W,[a**3+s*b for a,b in zip(y,u)],True)
    z = mv(Q,x)
    return (pair(r,back)+pair(z,u))**2 + mean([a*a for a in x])*(s+mean([a**3 for a in q]))


def mixed_finite_checks(n):
    p = Program()
    a,b,c = [p.vector_type(name) for name in ('a','b','c')]
    x,u,v = p.root('x',a),p.root('u',b),p.root('v',c)
    s = p.parameter('s')
    W,V,T,Q = p.matrix('W',a,b),p.matrix('V',b,c),p.matrix('T',c,a),p.matrix('Q',a,b)
    y = W@x
    q = V@y+v
    r = T@q
    back = W.T@(y**3+s*u)
    z = Q@x
    output = (p.inner(r,back)+p.inner(z,u))**2+p.mean(x*x)*(s+p.mean(q**3))
    roots = {node:[F((i+1)*(k+1)*(-1)**(i+k),i+k+4) for i in range(n)] for k,node in enumerate((x,u,v))}
    matrices = {node:[[F((-1)**(i+j+k)*(i+2*j+k+1),i+j+k+7) for j in range(n)] for i in range(n)] for k,node in enumerate((W,V,T,Q))}
    sv = F(2,7)
    evaluate = lambda o: evaluate_finite(o,n,roots,matrices,{s:sv})
    directions = {x:x*x+1,u:-u+2,v:v*v-1,s:s+p.mean(x),W:p.rank_one(u,x,s),V:p.rank_one(v,u),T:p.rank_one(x,v,-2),Q:p.rank_one(u,x,F(3,2))}
    droot = {node:evaluate(directions[node]) for node in (x,u,v)}
    dscalar = evaluate(directions[s])
    dmatrix = {}
    for matrix in (W,V,T,Q):
        terms = [(evaluate(k),evaluate(left),evaluate(right)) for k,left,right in directions[matrix].terms]
        dmatrix[matrix] = [[sum(k*l[i]*r[j]/n for k,l,r in terms) for j in range(n)] for i in range(n)]
    pathroots = [[Polynomial([a,b]) for a,b in zip(roots[node],droot[node])] for node in (x,u,v)]
    pathmatrices = [[[Polynomial([matrices[node][i][j],dmatrix[node][i][j]]) for j in range(n)] for i in range(n)] for node in (W,V,T,Q)]
    oracle = primal(*pathroots,Polynomial([sv,dscalar]),*pathmatrices)
    actual = p.derivatives(output,directions,3)
    for k,node in enumerate(actual):
        assert evaluate(node)==factorial(k)*oracle.c[k], ('frozen mixed derivative',n,k)
    gradients = p.gradient(output,vectors=[x,u,v],matrices=[W,V,T,Q],scalars=[s])
    contraction = sum((p.inner(gradients[node],directions[node]) for node in (x,u,v)),p.coerce(0))
    contraction = contraction+gradients[s]*directions[s]
    for node in (W,V,T,Q):
        contraction = contraction+p.frobenius(gradients[node],directions[node])
    assert evaluate(contraction)==oracle.c[1], ('all-block adjoint',n)
    print('cyclic types / parallel edge / reused transpose / feedback: exact derivatives 0..3 and full adjoint at width',n,'PASS')


def source_checks():
    p=Program()
    a,b,c=[p.vector_type(name) for name in ('a','b','c')]
    W,V,T,Q=p.matrix('W',a,b),p.matrix('V',b,c),p.matrix('T',c,a),p.matrix('Q',a,b)
    e=p.one(a)
    # Three independent Gaussian matrices, followed by their actual transposes.
    # E||T V W e||^2/n = 1 exactly at every width by successive conditioning.
    cycle=T@(V@(W@e))
    assert p.compile(p.inner(cycle,cycle)).output==ex.const(1)
    assert p.compile(p.inner(W@e,Q@e)).output==ex.const(0)
    # Gram powers: the leading Wick pairings are noncrossing pairings, whose
    # root-edge split gives C[k]=sum C[j]C[k-1-j]. This is an independent oracle.
    catalan=[1]
    value=e
    for k in range(1,6):
        catalan.append(sum(catalan[j]*catalan[k-1-j] for j in range(k)))
        value=W.T@(W@value)
        assert p.compile(p.inner(e,value)).output==ex.const(catalan[k])
    # A duplicate whose opposite formal partials cancel exactly.
    z1,z2=W@e,W@e
    zero=W.T@(z1**3-z2**3)
    assert p.compile(p.inner(zero,zero)).output==ex.const(0)
    # Nonzero root means and rank-zero correlated roots.
    r1,r2=p.roots(a,['r1','r2'],[[0,0],[0,0]],[2,-3])
    assert p.compile(p.mean((r1+r2)**6)).output==ex.const(1)
    # Physical differentiation of scalar feedback must precede the limit:
    # (mean x^2)^2 has n-gradient 4*(mean x^2)*x and energy limit 16.
    x=p.root('x',a)
    out=p.mean(x*x)**2
    grad=p.gradient(out,vectors=[x])[x]
    assert p.compile(p.inner(grad,grad)).output==ex.const(16)
    print('Gaussian graph / Catalan degrees 1..5 / singular cancellation / scalar feedback: PASS')


def boundaries():
    p=Program(); a=p.vector_type('a'); x=p.root('x',a)
    failures=[lambda:p.root('bad',a,variance=F(-1,10)),
              lambda:p.roots(a,['r','q'],[[0,1],[1,1]]),
              lambda:p.roots(a,['r','q'],[[1,0],[1,1]]),
              lambda:p.root('bad',a,variance=float('inf')),
              lambda:p.matrix('W',a,a),
              lambda:p.compile(p.mean(p.phi(x*x)),preactivations=[x*x]),
              lambda:p.gradient_descent(p.mean(x*x),[x],step_size=p.mean(x*x))]
    for check in failures:
        try:
            check()
        except ValueError:
            pass
        else:
            raise AssertionError('unsupported operation was accepted')
    print('seven boundary/error attacks: PASS')


if __name__=='__main__':
    print(json.dumps({'python':sys.version,'platform':platform.platform(),'sys_path':sys.path},indent=2))
    for width in (1,2,3): mixed_finite_checks(width)
    source_checks()
    boundaries()
    print('ALL INDEPENDENT ATTACKS PASSED')
