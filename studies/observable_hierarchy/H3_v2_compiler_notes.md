# Generic initialized Gaussian compiler: implementation record

2026-09-13. Author implementation, not an independent review or promotion.
Owned module: `H3_v2_compiler.py`, proposed canonical import
`pde.observable_compiler`. No established file or Git index was changed.
No trajectory was executed. The implemented finite source program has no
identified generalized-AD/source-nesting gap; the convergence claim remains
conditional on the separately proved cubature consistency premise and the
established H6 finite Gaussian law.

## Interface and scope

The module imports only NumPy and the Python standard library. Arithmetic and
the joint Gaussian rule are supplied explicitly:

```python
program = GaussianCompiler(
    arithmetic, gaussian_points, integration_count=Q,
    epsilon_cov=epsilon_cov, limits=CompilerLimits(...),
)
program.compile(complete_word_union, population_nodes=P)
values = program.evaluate(word, population_count=P)
values, partials = program.evaluate(word, population_count=P, derivative=True)
```

`compile` is one-shot. An enlarged requested program requires a complete new
compilation. `partials` has one column for every named source on the word's
population, including dependent/zero limiting queries and sources unavailable
when the word was first defined; the latter derivative entries are zero.
This differentiates named source coordinates with every coefficient and
covariance frozen. It does not differentiate Gaussian innovations, matrix
factorization, quadrature generation or initialization feedback.

The combined entry point is

```python
raw = compile_raw_dictionary(
    first_words, second_words,
    arithmetic=arithmetic, gaussian_points=gaussian_points,
    initialization_nodes=Q, population_nodes=P,
    epsilon_cov=epsilon_cov, limits=CompilerLimits(...),
)
```

It returns `RawInitialization` with:

| Field | Meaning |
| --- | --- |
| `psi1, psi2` | Same-row raw feature tables on the P-point replay clouds |
| `g` | The paired two-dimensional frozen first-population seed on that same P cloud |
| `probabilities1, probabilities2` | Uniform P-point population probabilities |
| `gram1, gram2` | Raw dictionary Grams on the complete Q-point initialization clouds |
| `C` | Q-point forward contraction `E2[psi2 (A0 psi1)^T]`, shape d2-by-d1 |
| `C_reverse` | Same-program diagnostic `E1[(A0* psi2) psi1^T]`, same shape |
| `program, metadata` | Optional initialization-only program and explicit numerical provenance |

Both terminal contraction lists are compiled in the complete union before any
Gram or C is extracted. Replays use exactly those frozen source factors and
response coefficients. No coefficients or covariances are recomputed on P.
The initializer may discard `program` after building normalized b,D; the
runtime solver needs no compiled Gaussian source object.

Normalization is intentionally outside the compiler. For the chosen
inverse-Cholesky convention, let `G_l+eta I=L_l L_l^T`, `T_l=L_l^(-1)`. Then
the caller computes `b_l=psi_l @ T_l.T` and `D=T_2 @ C @ T_1.T`, and the runtime
reverse action uses `D.T` (subsequently `M.T`). The final right transpose is
essential. The compiler imposes no feature-ridge schedule and does not delete
Gram modes, clip an action norm, average C with another estimator, or replace
the reverse action independently.

At finite epsilon_cov and Q, `C_reverse` need not equal C: both source
regularization and numerical integration are approximations. The reverse
diagnostic is not substituted into the runtime action. In the iterated Q to
infinity and epsilon_cov to zero limits both converge to the same H6 adjoint
contraction. Calling either finite numerical estimate the exact canonical
Gaussian contraction would be incorrect.

## Entire grammar and structural sharing

The compiler accepts Word-like objects by `op`, `population`, `args`, and
`scalar` attributes. It does not depend on the Python class used by a caller.
The complete maintained initialized grammar is implemented:

`one`, `g1`, `g2`, rational `scale`, `add`, bounded `multiply`, `sin`, `cos`,
`tanh`, and `action` in either orientation. Population types and bounded
operand sorts are inferred and checked; a supplied envelope is not trusted to
license an unbounded product. Initialization aliases `w1,w2` map to `g1,g2`,
`c` maps to zero, and `frozen_z20(v)` expands to `A0 tanh(g·v)`.

Graph ingestion is iterative. Every instruction is canonicalized by its
operation, population, parent node numbers and exact rational scalar. Literal
identical action expressions therefore share a source even when they come
from different Word classes. Algebraically dependent but different expressions
keep separate source slots. There is no approximate symbolic simplification
or numerical rank decision. A node's scalar and inferred syntax-envelope bit
sizes are bounded by an explicit resource limit.

## Causal construction and differentiation

Before numerical arrays are allocated, the full graph determines the number
of sources in each orientation. The input `gaussian_points(Q,d,ar)` supplies
one persistent joint rule for each population. Population 1 uses two initial
seed coordinates followed by its reverse innovation coordinates; population
2 uses its forward innovation coordinates. These are separate population
measures, and no cross-population pairing of point indices is used.

At a new action, its operand v and every old same-orientation operand v_i
already have permanent values on the other population's Q cloud. The source
covariance extension is the full uncentered Gram of that list plus
`epsilon_cov I`. The old block is unchanged, since the old operands are
unchanged. A triangular solve appends only the new Cholesky row. Old source
variables, factors and node values are never recomputed during a compilation.

In exact arithmetic, the new Schur complement is strictly positive and at
least epsilon_cov. To verify this, the enlarged matrix is `V^T V/Q+epsilon I`;
its quadratic form at `(-C^(-1)a,1)` equals the Schur complement and is at least
epsilon times the squared norm of that vector, hence at least epsilon.
An unresolved nonpositive numerical pivot raises `CompilerNumericalError`.
No absolute-value repair, rank threshold, mode deletion, or zero-pivot fallback
is used. Positive but poorly resolved pivots remain a finite-precision error;
the mathematical convergence claim removes precision at fixed positive epsilon.

Every action output is its new named Gaussian source plus all earlier
opposite-orientation operands times the expected named-source input derivative,
as in H6. The new source slots are separate formal leaves even when the
zero-regularization law is singular. Reverse AD seeds the requested operand
and traverses the scalar expression backward. At an action output it records
the adjoint at that named leaf and propagates through its frozen response
links; it does not propagate through the opposite-population query edge as
though that were a scalar differentiable matrix application. Response links
point to earlier nodes on the same population, so the augmented graph remains
acyclic. Contributions from repeated parents are accumulated. Exact zero
response coefficients can be skipped as arithmetic work; all named source
coordinates remain present and no tolerance is used.

At fixed Q and epsilon, replay on P evaluates this same finite scalar program
with its learned factors and coefficients. AD on that replay still holds them
fixed. Gaussian point dimensions can grow without changing their prefix
coordinates, as the injected Halton/Box–Muller rule guarantees. The program
caches the initialization values and at most one replay point count; it does
not accumulate a history of previous P values.

## Consistency obligation and singular limits

For fixed positive epsilon, induction on finitely many source calls reduces
coefficient consistency as Q grows to cubature of continuous finite Gaussian
expressions and their source derivatives. Each has a locally uniform
polynomial envelope as prior coefficients vary in a compact neighborhood.
The Cholesky step is continuous because every limiting covariance is strictly
positive. Split an integral's error into a coefficient perturbation and a
fixed-expression cubature error; the former is dominated by a polynomial
envelope. The scope agent's contained Halton all-moment result is the proposed
dependency that justifies both terms. This compiler file itself does not
prove Halton convergence.

At Q fixed, the P limit is the ordinary joint-law cubature of the frozen
finite source expression; its full same-population W2 law is preserved. The
epsilon-to-zero passage uses full covariance-matrix square-root continuity,
including singular covariances, and frozen-source derivative expectations.
It does not use inverse or Cholesky continuity at zero covariance. The finite
regularized source law can fail exact linearity between different dependent
queries; it is an auxiliary approximation, removed before closure order.
This matches the scoped route's singular-law argument and the supplied
III.F.4–5 source conventions.

No unresolved generalized-AD/source-nesting implication has been identified.
The numerical tests below check finite algebra, not this convergence theorem,
large-order practical resource feasibility, or canonical trajectory accuracy.

## Resource gates

`CompilerLimits` exposes positive integer limits:

| Field | Default |
| --- | ---: |
| max_nodes | 4096 |
| max_sources | 256 |
| max_points | 1000000 |
| max_working_bytes | 536870912 |
| max_work_units | 2000000000 |
| max_scalar_bits | 65536 |

The graph, source, point, work and estimated-memory gates are checked before
Gaussian clouds, source factors or node-value arrays are allocated. The raw
entry point additionally counts retained feature columns, including repeated
columns. Its anticipated replay P is included before compilation. A later
standalone replay checks its own count before allocating that replay. Object
graph parsing necessarily precedes graph-size verification; the byte estimate
is a conservative numerical-workspace estimate, not an operating-system
memory guarantee or a bound on arbitrary externally supplied objects.

With L DAG nodes, S action sources and E at most `2L+S^2` scalar/response
edges, the conservative source work estimate is `Q*S*E`, plus Gram, triangular
and replay work. Numerical workspace is `O((Q+P)(L+S+d)+S^2+d^2)` with no
stored Q-by-L-by-S derivative tensor. There is no tensor Gaussian quadrature
factor and no P2-by-P1 neural matrix. A requested program exceeding a limit
raises `CompilerResourceLimit`; raising limits is an explicit caller choice.
This generic fallback does not make the first exhaustive-tail action at a
large Chebyshev degree cheap. It implements arbitrary finite grammar at
explicit finite resource cost; useful first orders use the separate fast core.

## Static verification and provenance

The assigned ceiling was 10 CPU minutes and 4 GiB; each test process enforced
those limits. Tests used one OpenBLAS/OMP thread. The passing suite used
0.755 CPU seconds and 37,368 KiB peak RSS. Its observed outcomes were:

- Full covariance-factor versus persistent-input-Gram error: `1.67e-16`.
- All named-source partials of a forward/reverse/forward/reverse graph versus
  centered finite differences of formal named coordinates: maximum `2.01e-10`.
- Earlier values in a larger complete program were bit-for-bit preserved.
- Q=257 initialization/P=131 replay preserved coefficients and same-row identities.
- Zero and scaled-dependent source operands retained all derivative slots.
- The complete original code prefix through 99, plus current/frozen aliases,
  evaluated in both populations with finite outputs and derivatives.
- Raw Grams and the forward/reverse contraction interface matched their direct
  same-cloud formulas to arithmetic roundoff.
- Every tested resource gate rejected before the injected Gaussian allocator.
- Decimal40 and rational40 matched Float64 on a tiny round-trip program.
- A constant/scaled-constant source with epsilon=`1e-100` raised the intended
  Float64 pivot error; Decimal120 resolved both positive source directions.

The first test revision incorrectly demanded bit equality for separately
assembled matrix products. NumPy's symmetric-product and generic-product
paths differed by `5.55e-17`, so that test failed. The retained second revision
uses `3e-15` for those direct floating product checks. No compiler change was
needed for that test correction. Both test revisions are retained in
`data/generated/observable_hierarchy/H3_v2_route_gaussian/`.

Passing source hashes:

| Source | SHA-256 |
| --- | --- |
| H3_v2_compiler.py | `1add30410ee2e8de05fffca225643dbbbeab7ab8d6420382014bb8c9cceca7ac` |
| H3_v2_arithmetic.py | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| H3_v2_fixed.py | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |
| code/pde/observable_closure.py | `f8dc5d16e5de1737444c44aae737ee1c9b4d664188d72f59acd0bb92f457c137` |

Scientific/process input coverage for this implementation: the preceding
route's complete allowed H1/H2, notation and maintained module/tests; the
complete tanh `H3_v2_basis_synthesis.md`, complete coordinator route, arithmetic
interface; `dependencies_v1.md` lines 1–593 (complete III.F.1–10 and A.1–4,
the source/calculus scopes relevant to this compiler); and complete
`H2_proposed_section_v3.md`. The other dependency excerpts concern trajectories
and were not reopened for this initialization-only implementation. No other
study was read. The earlier independence claim applies only to the frozen
creative route, not this coordinated implementation.

The executable passing test source follows so no unique verification recipe
exists only in generated data. Save the Python block below as a study-owned
scratch file and run, from `/home/amir/Codes/PDE`, with
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python <scratch-file>`.

<!-- STATIC_TEST_SOURCE -->

```python
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
from dataclasses import replace
from fractions import Fraction

resource.setrlimit(resource.RLIMIT_CPU, (600, 600))
resource.setrlimit(resource.RLIMIT_AS, (4*1024**3, 4*1024**3))
root = Path('/home/amir/Codes/PDE')
study = root/'studies/observable_hierarchy'
sys.path.insert(0, str(root/'code'))
from pde import observable_closure as w
import numpy as np

for name, filename in [('pde.observable_fixed', 'H3_v2_fixed.py'),
                       ('pde.observable_arithmetic', 'H3_v2_arithmetic.py'),
                       ('pde.observable_compiler', 'H3_v2_compiler.py')]:
    spec = importlib.util.spec_from_file_location(name, study/filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
from pde.observable_arithmetic import Arithmetic, gaussian_points
from pde.observable_compiler import GaussianCompiler, CompilerLimits, CompilerResourceLimit, CompilerNumericalError, compile_raw_dictionary

started = time.process_time()
checks = {}
pilot = w.pilot_words()
forward = w.action(pilot['t1'])
mixed = w.multiply(w.unary('sin', forward), w.unary('cos', pilot['z2']))
reverse = w.action(mixed)
terminal = w.multiply(w.unary('tanh', reverse), pilot['t1'])
targets = list(pilot.values())+[forward,mixed,reverse,terminal]
program = GaussianCompiler(Arithmetic(), gaussian_points, 257, 0.001).compile(targets, population_nodes=131)

# Full Gram consistency, including all nested forward and reverse operands.
gram_error = 0.0
for pop in (1,2):
    source = program.source_lists[pop]
    inputs = np.column_stack([program._values[s.operand] for s in source])
    expected = inputs.T@inputs/257+0.001*np.eye(len(source))
    actual = program.factors[pop]@program.factors[pop].T
    gram_error = max(gram_error,float(np.max(np.abs(expected-actual))))
assert gram_error < 2e-14
checks['nested_full_gram_max_error'] = gram_error

# Independently perturb formal named coordinates, holding all factors and
# response coefficients fixed. This checks AD through nested response paths.
values, normals = program._at_count(131)
gaussian = {pop: normals[pop][:,2 if pop==1 else 0:]@program.factors[pop].T for pop in (1,2)}
derivative_error = 0.0
for word in (forward,mixed,reverse,terminal):
    index = program._word(word,False)
    _, derivative = program.evaluate(word,131,True)
    for coordinate in range(derivative.shape[1]):
        outputs=[]
        for sign in (1,-1):
            perturbed={pop:g.copy() for pop,g in gaussian.items()}
            perturbed[word.population][:,coordinate] += sign*1e-6
            result=[]
            for node in range(len(program.nodes)):
                result.append(program._value(node,result,normals,perturbed))
            outputs.append(result[index])
        estimate=(outputs[0]-outputs[1])/2e-6
        derivative_error=max(derivative_error,float(np.max(np.abs(estimate-derivative[:,coordinate]))))
assert derivative_error < 3e-9
checks['all_nested_named_partials_max_error']=derivative_error

# A larger complete union preserves every old scalar expression and factor.
prefix=GaussianCompiler(Arithmetic(),gaussian_points,257,0.001).compile(pilot.values())
for word in pilot.values():
    np.testing.assert_array_equal(prefix.evaluate(word),program.evaluate(word))
checks['old_cloud_values_preserved_exactly']=True

# Replay uses unchanged coefficients and preserves same-row identities.
before=[d['response_coefficients'].copy() for d in program.diagnostics]
replayed=program.evaluate(terminal,131)
replayed_again=program.evaluate(terminal,131)
np.testing.assert_array_equal(replayed,replayed_again)
for old,d in zip(before,program.diagnostics):
    np.testing.assert_array_equal(old,d['response_coefficients'])
np.testing.assert_allclose(program.evaluate(terminal,131),np.tanh(program.evaluate(reverse,131))*program.evaluate(pilot['t1'],131),rtol=0,atol=0)
checks['frozen_coefficient_replay_and_joint_identity']=True

# Singular limiting inputs retain separate named derivative slots.
one=w.constant(1)
degenerate=[w.action(w.scale(0,one)),w.action(one),w.action(w.scale(2,one))]
singular=GaussianCompiler(Arithmetic(),gaussian_points,31,0.0001).compile(degenerate)
assert len(singular.source_lists[2])==3
_, derivatives=singular.evaluate(degenerate[2],derivative=True)
np.testing.assert_array_equal(derivatives,np.tile([0.,0.,1.],(31,1)))
assert all(d['innovation_variance']>0 for d in singular.diagnostics)
checks['singular_named_slots_retained']=True

# Whole original instruction grammar and initialization aliases.
grammar=[word for n in range(100) if (word:=w.decode_word(n)) is not None]
grammar += [w.seed('w1'),w.seed('w2'),w.seed('c'),w.frozen_z20((0.6,0.8))]
all_ops=GaussianCompiler(Arithmetic(),gaussian_points,61,0.001).compile(grammar)
for word in grammar:
    assert np.all(np.isfinite(all_ops.evaluate(word,47,True)[0]))
np.testing.assert_array_equal(all_ops.evaluate(w.seed('c')),0)
checks['full_grammar_prefix_and_aliases']=True

# Raw contraction is explicitly forward; reverse is a diagnostic from the
# same union. Different integration/replay counts do not mix Gram carriers.
first,second,_=w.initial_dictionary(1)
raw=compile_raw_dictionary(first,second,arithmetic=Arithmetic(),gaussian_points=gaussian_points,initialization_nodes=257,population_nodes=131,epsilon_cov=0.001)
assert raw.psi1.shape==(131,6) and raw.psi2.shape==(131,4)
np.testing.assert_allclose(raw.gram1,raw.program.table(first).T@raw.program.table(first)/257,rtol=0,atol=3e-15)
np.testing.assert_allclose(raw.C,raw.program.table(second).T@raw.program.table([w.action(word) for word in first])/257,rtol=0,atol=3e-15)
np.testing.assert_allclose(raw.C_reverse,raw.program.table([w.action(word) for word in second]).T@raw.program.table(first)/257,rtol=0,atol=3e-15)
checks['raw_joint_interface']=True

# Each resource gate rejects before Gaussian allocation.
for limits in (replace(CompilerLimits(),max_nodes=2),replace(CompilerLimits(),max_sources=1),replace(CompilerLimits(),max_points=4),replace(CompilerLimits(),max_working_bytes=64),replace(CompilerLimits(),max_work_units=1)):
    called=[]
    def forbidden(*args):
        called.append(True)
        raise AssertionError('allocated before resource failure')
    try:
        GaussianCompiler(Arithmetic(),forbidden,31,0.001,limits).compile(pilot.values(),population_nodes=47)
    except CompilerResourceLimit:
        pass
    else:
        raise AssertionError('resource gate did not reject')
    assert not called
checks['preallocation_resource_gates']=True

# Actual precision backends, with a tiny round-trip program.
tiny=[pilot['h1'],pilot['z1'],pilot['s1'],pilot['p1'],pilot['t1']]
base=GaussianCompiler(Arithmetic(),gaussian_points,11,0.001).compile(tiny)
for backend in ('decimal','rational'):
    precise=GaussianCompiler(Arithmetic(40,backend=backend),gaussian_points,11,'0.001').compile(tiny)
    for word in tiny:
        np.testing.assert_allclose(np.asarray(precise.evaluate(word,13),dtype=float),base.evaluate(word,13),rtol=0,atol=2e-12)
checks['decimal_and_rational_backends']=True

try:
    GaussianCompiler(Arithmetic(),gaussian_points,7,1e-100).compile(degenerate[1:])
except CompilerNumericalError:
    pass
else:
    raise AssertionError('unresolved positive float pivot was silently changed')
resolved=GaussianCompiler(Arithmetic(120),gaussian_points,7,'1e-100').compile(degenerate[1:])
assert len(resolved.sources)==2 and resolved.diagnostics[-1]['innovation_variance']>0
checks['unresolved_pivot_failure_and_precision_recovery']=True

print(json.dumps({'status':'PASS','checks':checks,'cpu_seconds':time.process_time()-started,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'source_hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [study/'H3_v2_compiler.py',study/'H3_v2_arithmetic.py',study/'H3_v2_fixed.py',root/'code/pde/observable_closure.py']}},indent=2))
```
