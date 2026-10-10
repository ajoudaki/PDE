"""Reviewer TWO probes, independent of candidate tests and moment reducer.

The index-pairing oracle computes exact finite-width Gaussian expectations
of normalized matrix-word contractions by Wick pairing raw entries and
counting free typed indices. It never calls the candidate source rule.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import factorial
import json
import platform
import sys

from pde.mfp_compiler import Program, ProgramError
from pde.mfp_finite import evaluate_finite
from pde import mfp_expr as ex


def pairings(items):
    if not items:
        yield ()
        return
    first, *rest = items
    for j, second in enumerate(rest):
        for tail in pairings(rest[:j] + rest[j + 1:]):
            yield ((first, second),) + tail


def word_moment(words, matrices):
    """E[inner(word_1 @ one, word_2 @ one)], polynomial in n.

    Each word is in action order. All endpoints must have one common type.
    One endpoint index is shared because of the normalized pairing.
    """
    indices, entries = [], {}
    endpoint = None
    for word in words:
        first, trans = word[0]
        source, target = matrices[first]
        kind = target if trans else source
        previous = len(indices)
        indices.append(kind)
        for j, (name, transpose) in enumerate(word):
            source, target = matrices[name]
            assert kind == (target if transpose else source)
            kind = source if transpose else target
            if j == len(word) - 1 and endpoint is not None:
                current = endpoint
                assert indices[current] == kind
            else:
                current = len(indices)
                indices.append(kind)
            entry = (previous, current) if transpose else (current, previous)
            entries.setdefault(name, []).append(entry)
            previous = current
        endpoint = previous
    if any(len(value) % 2 for value in entries.values()):
        return {}
    total_entries = sum(map(len, entries.values()))
    result = Counter()
    for combination in product(*(tuple(pairings(value)) for value in entries.values())):
        parent = list(range(len(indices)))
        def find(i):
            while parent[i] != i:
                i = parent[i]
            return i
        def union(i, j):
            assert indices[i] == indices[j]
            parent[find(i)] = find(j)
        for matching in combination:
            for a, b in matching:
                union(a[0], b[0])
                union(a[1], b[1])
        exponent = len({find(i) for i in range(len(indices))}) - total_entries//2 - 1
        result[exponent] += 1
    return dict(sorted(result.items()))


checks = []
def check(name, actual, expected):
    assert actual == expected, (name, actual, expected)
    checks.append(dict(name=name, result=str(actual)))


def compare_words(name, descriptions, words):
    p = Program()
    kinds = {}
    for kind in sorted({kind for ends in descriptions.values() for kind in ends}):
        kinds[kind] = p.vector_type(kind)
    objects = {key: p.matrix(key, *ends) for key, ends in descriptions.items()}
    vectors = []
    for word in words:
        name0, trans = word[0]
        current = p.one(descriptions[name0][1 if trans else 0])
        for key, transpose in word:
            current = (objects[key].T if transpose else objects[key]) @ current
        vectors.append(current)
    exact = word_moment(words, descriptions)
    assert not any(k > 0 and v for k, v in exact.items())
    check(name, p.compile(p.inner(*vectors)).output, ex.const(exact.get(0, 0)))
    checks[-1]['finite_width_polynomial'] = exact


for k in range(1, 4):
    word = [('A', False), ('A', True)] * k
    compare_words(f'wishart_norm_{k}', {'A': ('a', 'b')}, (word, word))
compare_words('cyclic_types_reused_edge',
              {'A': ('a', 'b'), 'B': ('b', 'c'), 'C': ('c', 'a')},
              ([('A', False), ('B', False), ('C', False), ('A', False)],)*2)
compare_words('parallel_edges_mixed_reverse',
              {'A': ('a', 'b'), 'B': ('a', 'b')},
              ([('A', False), ('B', True), ('A', False)],
               [('B', False), ('A', True), ('B', False)]))
compare_words('parallel_same_route', {'A': ('a', 'b'), 'B': ('a', 'b')},
              ([('A', False), ('B', True)],)*2)
compare_words('mixed_cycle_and_transposes',
              {'A': ('a', 'b'), 'B': ('b', 'c'), 'C': ('c', 'a')},
              ([('A', False), ('B', False), ('C', False)],
               [('C', True), ('B', True), ('A', True)]))

# Polynomial scalar feedback and physical derivatives through its average.
p = Program(); a = p.vector_type('a'); b = p.vector_type('b')
W = p.matrix('W', a, b); e = p.one(a); x = p.root('x', a)
z = W @ e; q = p.mean(z*z); out = p.inner(W.T @ (q*z), W.T @ (q*z))
check('causal_feedback_limit', p.compile(out).output, ex.const(2))
O = p.mean(x*x)**2
direction = {x: p.one(a)}
second = p.derivatives(O, direction, 2)[2]
check('physical_average_derivative_limit', p.compile(second).output, ex.const(4))
check('physical_average_derivative_width1', evaluate_finite(second, 1, {x: [F(2)]}, {}), F(48))

# Exact cubic cancellation of formally distinct singular slots, including the
# reverse response, and freeze affecting physical AD only.
y1, y2 = W @ e, W @ e
cancel = W.T @ (y1**3-y2**3)
check('singular_cubic_reverse_cancellation', p.compile(p.inner(cancel,cancel)).output, ex.const(0))
frozen = p.freeze(z**3)
check('freeze_retains_source_response', p.compile(p.inner(W.T @ frozen, W.T @ frozen)).output, ex.const(24))
g = p.gradient(p.mean(frozen), matrices=[W])[W]
check('freeze_zero_physical_gradient', len(g.terms), 0)

# Repeated ambient updates on a vector, compared with a direct scalar formula.
eta = F(1, 7); loss = p.mean(x**4)/4
state = p.gradient_descent(loss, vectors=[x], steps=3, step_size=eta)
values = [F(-1,2), F(2,3), F(0)]
direct = values[:]
for _ in range(3):
    direct = [v-eta*v**3 for v in direct]
check('three_ambient_updates', evaluate_finite(state[x], 3, {x: values}, {}), tuple(direct))
for r in (0, 1, 2, 3):
    jet = p.jets(p.mean(x*x), {x: -x**3}, r, moving=True)[r]
    expected = F((-2)**r) * F(factorial(2*r+2), 2**(r+1)*factorial(r+1))
    check(f'cubic_flow_coefficient_{r}', p.compile(jet).output, ex.const(expected))

# Root rank loss and raw initialization law do not alter ambient derivatives.
r = Program(); t = r.vector_type('t'); u,v = r.roots(t,['u','v'],[[0,0],[0,2]],[3,-1])
check('zero_variance_nonzero_mean_root', r.compile(r.mean(u**4)).output, ex.const(81))
check('ambient_gradient_of_degenerate_root', r.compile(r.mean(r.gradient(r.mean(u*u),[u])[u])).output, ex.const(6))
check('shifted_singular_root_moment', r.compile(r.mean(u*v*v)).output, ex.const(9))

errors = [lambda: r.roots(t,['bad1','bad2'],[[0,1],[1,2]]),
          lambda: r.root('bad3',t,float('inf')),
          lambda: r.root('bad4',t,-F(1,10**100)),
          lambda: r.compile(r.mean(r.phi(u)),preactivations=[u]),
          lambda: r.gradient_descent(r.mean(u*u),[u],mobilities={u:r.mean(v)}),
          lambda: evaluate_finite(r.mean(u),1,{u:[True]},{}),
          lambda: evaluate_finite(r.mean(u),1,{u:[1]}, {},activation=3)]
for i, operation in enumerate(errors):
    try:
        operation()
    except (ProgramError, ex.UnsupportedExpression):
        checks.append(dict(name=f'boundary_rejection_{i}',result='rejected'))
    else:
        raise AssertionError(f'boundary {i} accepted')

# Matrix ambient-gradient evaluation and pullback differ by the update Jacobian.
m = Program(); lo=m.vector_type('lo'); hi=m.vector_type('hi')
A=m.matrix('A',lo,hi); one=m.one(lo); zz=A@one
ell=m.inner(zz,zz)/2; eta=F(1,5)
new=m.gradient_descent(ell,matrices=[A],step_size=eta)
ambient=m.at(m.gradient(ell,matrices=[A])[A]@one,new)
pullback=m.gradient(m.at(ell,new),matrices=[A])[A]@one
matrix_data={A:[[F(2),F(-1)],[F(3),F(4)]]}
check('matrix_current_gradient',evaluate_finite(ambient,2,{},matrix_data),(F(4,5),F(28,5)))
check('matrix_history_pullback',evaluate_finite(pullback,2,{},matrix_data),(F(16,25),F(112,25)))

# A separate analytic limit for zero geometry and affine nonlinearity phi(z)=1+z.
# First features are one; upper H=1+W one has E H^2=2. With ybar=(y1+y2)/2,
# Hdot=ybar*w, wdot=ybar*H, so K_[2]=3*ybar^2 after centered-readout cancellation.
from scripts.example_mfp_kernel_jets import compile_example
def affine(node):
    if node.op in ('const','symbol'):
        return node
    args=[affine(a) for a in node.args]
    if node.op=='phi':
        return 1+args[0] if node.value==0 else ex.const(1 if node.value==1 else 0)
    if node.op=='pow':
        return args[0]**node.value
    if node.op=='add':
        return sum(args,ex.const(0))
    result=ex.const(1)
    for a in args:
        result=result*a
    return result
def no_atom(expr):
    raise AssertionError(expr)
zero={ex.symbol('s_'+name):ex.const(0) for name in ('alpha','beta','gamma')}
expected=(ex.const(2),ex.const(0),ex.const(3)/4*(ex.symbol('s_y1')+ex.symbol('s_y2'))**2)
for j,dag in enumerate(compile_example('symbolic')):
    vals=dict(zero)
    for atom in dag.expectations:
        integrand=ex.substitute(affine(atom.integrand),vals)
        covariance={(a,b):ex.substitute(atom.covariance[i][k],vals)
                    for i,a in enumerate(atom.coordinates) for k,b in enumerate(atom.coordinates)}
        vals[atom.symbol]=ex.gaussian_expectation(integrand,atom.coordinates,covariance,no_atom)
    check(f'zero_geometry_affine_kernel_{j}',ex.expand(ex.substitute(dag.output,vals)),ex.expand(expected[j]))

print(json.dumps(dict(python=sys.version,platform=platform.platform(),checks=checks),indent=2))
