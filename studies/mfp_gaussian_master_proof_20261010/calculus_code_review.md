# Independent internal review of the MFP calculus implementation

Reviewer: fresh scoped code-review agent `/root/calculus_code_review`.
Review date: 2026-10-10. This is an internal study check, not a promotion review
or certification of all mathematical claims in the master theorem.

**Current status: PASS for the corrected candidate.** Both baseline contract
findings are resolved; all 53 revised tests and focused verification checks pass.
The corrected-candidate addendum records the final hashes and evidence. The
baseline verdict and findings below are retained as historical review evidence.

## Baseline verdict

**The implemented arithmetic passes the executed checks; a derivative-contract
clarification is required.** I found no incorrect finite AD, normalized gradient,
represented-matrix action, update, or Gaussian response formula in the admitted
operations I inspected and tested. All 51 supplied tests passed. Additional
independent exact probes passed, including third-order coupled vector, matrix,
and scalar gradient-flow jets. These checks are substantive but finite.

The public `freeze` operation requires an explicit qualification of “exact
Fréchet derivative”: it changes the differentiation convention while preserving
values. Its intended frozen-direction use is correct. A smaller input-contract
mismatch also exists: root covariances accept numeric strings although the public
contract describes numeric inputs. Findings and limitations follow.

## Assignment, isolation, and complete read coverage

The supervisor assigned a fresh isolated internal code review of these eight
frozen inputs only, with ownership restricted to this report and
`data/generated/mfp_gaussian_master_proof_20261010/code_review/`:

| Input | Complete lines read |
| --- | ---: |
| `master_proof.md` | 1–467 |
| `mfp_compiler.py` | 1–769 |
| `mfp_expr.py` | 1–426 |
| `mfp_finite.py` | 1–140 |
| `test_mfp_compiler.py` | 1–486 |
| `test_mfp_expr.py` | 1–189 |
| `run_calculus_examples.py` | 1–88 |
| `compiler_usage.md` | 1–241 |

The assignment specifically requested exact finite AD, normalized gradients,
moving directions and curve jets; matrix identity/reuse/orientation; frozen
expectation coefficients in Gaussian response partials; named sources at
singular covariance; causal integrands/covariances; integration-only aliases;
scalar feedback; unsupported-operation rejection; ambient gradients before
state substitution; and agreement between full-program scope and documentation.
An initially truncated combined tool output was repaired with complete individual
and chunked reads. The stated coverage excludes neither code bodies nor tests.

I also read the current root `AGENTS.md`, complete `RESEARCH_WORKFLOW.md`,
`explain-with-canonical-notation/SKILL.md` and its complete neural-response-memory
reference, and `solve-math-rigorously/SKILL.md`. I did not read the study README,
history, other reviews, other studies, book chapters, or external scientific
sources. Metadata-only Git inspection found concurrent unrelated changes and
an empty staged-path list; I made no Git-index changes.

The supervisor later specifically requested checking the `freeze` boundary;
that item was a targeted follow-up, not a wholly blind discovery. The supervisor
also relayed its own test status after my supplied-test execution. No other
reviewer's report or scientific findings were received. The status/provenance
sentences already present in the permitted master proof were read as part of
that frozen input and were not treated as correctness evidence.

Baseline HEAD was `c17cb8c2e8d486ccc1d2b80e8cd173ba551145ae`.
Hashes were taken before reading the candidate and after completing the baseline
review. All eight final hashes matched their initial hashes:

```text
55d979e9dbab1c13bc1f84a43b001efe9fefa6bd1b565d4479245ef5128a3388  master_proof.md
2ee4fc5445fed6ebe3112241d09d717e8ce69efbfdf3b6b24c27e528eae7e7f7  mfp_compiler.py
82bce3fe5f8180aa89c009fa117c1fdb6563bbb0247d20e60296fbe199f070de  mfp_expr.py
7e39ff0fd2026c6fd7fd6f3f2e6f6f2a82025a72fd83b533c38d7b4be03ed6d8  mfp_finite.py
07390c2c7833b458c6735a40b60d22b36f519bfec3860a4faf1dc05d2cc61ec1  test_mfp_compiler.py
2f782b98fcd315b0302a0a7749f4baf3b44a4ff35ef268afc1fa12bcfc3ff69e  test_mfp_expr.py
97d46462161eeccfeb50ade33e1788ebe4dd79948fd9d886e9d818705659e825  run_calculus_examples.py
77ab4a11d0730eab865c39fa721efa904c1161573f621f2b7b2a7218fea5e156  compiler_usage.md
```

The machine-readable end record is `code_review/baseline-final.sha256` in the
study's generated-data namespace.

## Findings

### C1 — Qualify the ordinary derivative claim in the presence of `freeze`

Affected baseline passages: `mfp_compiler.py:368–378` and
`compiler_usage.md:124–129,164–166`.

For a width-two root vector $x=(1,2)$, define the scalar observable
$O(x)=\operatorname{mean}(\operatorname{freeze}(x)^2)$ and direction $h=(1,1)$.
The finite interpreter evaluates the diagonal value function as
$O(x+th)=\tfrac12[(1+t)^2+(2+t)^2]$. Its ordinary directional derivative at
zero is 3. The public `directional` builder returns zero because it deliberately
stops at `freeze`. The executable probe verifies the derivative result and
values $O(x)=5/2$, $O(x+h)=13/2$.

This is consistent with a partial derivative in which each frozen seed is
independent input data, evaluated at its base-state value. It is not the ordinary
Fréchet derivative of the diagonal value function. The existing usage sentence
that `freeze` is a “derivative convention” helps, but does not qualify the earlier
universal exact-derivative statement or the method docstring.

**Requested correction:** explicitly restrict ordinary-derivative claims to
primal graphs without `freeze`, and state the independent-frozen-data partial
semantics for graphs that contain it. Explain that its intended use is freezing
direction seeds; inserting it in a primal network changes derivative semantics.
No change to the frozen-direction implementation is needed. Apply the same
qualification to gradient claims where applicable.

### C2 — Numeric covariance strings pass a numeric-only input contract

Affected baseline passage: `mfp_compiler.py:205–222`; usage numeric-input contract
at `compiler_usage.md:99–106`.

`p.root("x", kind, variance="1")` succeeds and produces variance one because
`roots` converts every entry using `Fraction(str(v))`. This accepts a string
where scalar expressions and means reject strings. The resulting covariance
has a valid mathematical value, so this is a minor interface inconsistency,
not a wrong Gaussian limit or a security finding.

**Requested correction:** either require the documented finite `int`, `float`,
or `Fraction` types before conversion, or document the broader conversion
contract. A rejection check should accompany a stricter numeric contract.

## Reconstructed semantics and component checks

- **Finite primitive graph.** Nodes preserve vector types, scalar broadcasting,
  normalized means, and named matrix identity. A represented action expands
  $cuv^\top/n$ to $cu\,\operatorname{mean}(v\odot h)$, with left/right
  factors exchanged for its transpose. The finite interpreter receives actual
  stored matrix entries and introduces no hidden matrix normalization.
- **Finite AD.** The forward rules differentiate every original dependency,
  including scalar feedback. Inserted directions are not differentiated in the
  same pass. Repeated frozen derivatives wrap all vector/scalar seeds and all
  matrix factors/coefficient seeds; moving derivatives retain their state
  dependencies. Curve coefficients are inserted simultaneously into a fresh
  auxiliary-time path and remain fixed relative to that time.
- **Reverse AD.** Vector adjoints are $n\nabla_u O$, scalar adjoints are ordinary
  gradients, and matrix contributions are sums of $bu^\top/n$. Broadcast
  adjoints and scalar operands of vector operations introduce means, so the
  normalization is consistent. Contributions accumulate through repeated and
  transpose uses. The helper differentiates the ambient loss template once and
  substitutes the current state into that gradient at each simultaneous update.
- **Contractions.** The pure-rank Frobenius rule is exactly
  $\langle uv^\top/n,ab^\top/n\rangle_F
    =\operatorname{mean}(u\odot a)\operatorname{mean}(v\odot b)$.
  It is not an unrestricted dense-tensor contraction.
- **Gaussian responses.** Each oriented matrix group keeps a list of named
  sources, with covariance from input Gram expectations. The opposite group
  supplies response derivatives. `ex.diff` fixes all other symbols, including
  expectation atoms; it neither differentiates a covariance nor substitutes
  Gaussian support identities. This preserves distinct formal slots when a
  covariance is singular.
- **DAG and aliases.** Expectation atoms store their integrands and marginal
  covariance at allocation. Inputs and coefficients are available before the
  corresponding matrix source is used. Preactivation aliases are substituted
  only when integrating; formal response derivatives use the original fields.
  The weighted duplicate-query probe independently gives limit 81 while keeping
  two response slots. Nonlinear deterministic feedback becomes a zero-dimensional
  expectation, leaving the final scalar assembly polynomial in prior atoms.
- **Normal form and scope.** The restricted form checks literal nonlinear
  arguments and centered Gaussian linear representatives; identifying original
  network preactivations remains the caller's responsibility. General nested
  nonlinearities remain integral atoms. Program sizes, coefficients, derivative
  orders, and update counts must be fixed as width grows. Neither symbolic
  compilation nor these tests establish a uniform growing-order limit, an
  infinite Taylor sum, positive-time reconstruction, or depth-linear cost.

The complete master proof was checked for consistency with those implementation
conventions. I have not separately re-proved every analytic convergence argument
or checked its cited external sources; that stronger mathematical verdict is
outside this code-review evidence.

## Executed commands and independent evidence

All commands ran from `/home/amir/Codes/PDE`. Environment: Python 3.10.12,
GCC 11.4.0, Linux 5.15.0-151-generic x86_64, glibc 2.35. No third-party packages,
random sampling, quadrature, training campaign, or network retrieval were used.
All command exit statuses were zero.

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=studies/mfp_gaussian_master_proof_20261010 \
  python -m unittest -v test_mfp_compiler test_mfp_expr \
  > data/generated/mfp_gaussian_master_proof_20261010/code_review/unittest.log 2>&1
PYTHONDONTWRITEBYTECODE=1 python studies/mfp_gaussian_master_proof_20261010/run_calculus_examples.py \
  > data/generated/mfp_gaussian_master_proof_20261010/code_review/examples.txt
PYTHONDONTWRITEBYTECODE=1 python studies/mfp_gaussian_master_proof_20261010/run_calculus_examples.py \
  --example reuse --json > data/generated/mfp_gaussian_master_proof_20261010/code_review/reuse.json
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=studies/mfp_gaussian_master_proof_20261010 \
  python data/generated/mfp_gaussian_master_proof_20261010/code_review/probes.py \
  > data/generated/mfp_gaussian_master_proof_20261010/code_review/probes.log 2>&1
```

Observed supplied-test result: **51 tests, all passed**, in 0.170 seconds.
The tests have independent substantive oracles: dense array evaluation;
raw-coordinate derivatives from an independent rational polynomial in a
perturbation parameter; dense two-step ambient updates; exact represented
matrix columns; a hand-derived second moving-flow derivative; known Gaussian
moments and Wick/Stein identities; and explicit repeated-matrix formulas.
Some compiler tests inspect the precise expression shape, which is useful for
formal-slot and coefficient contracts but does not independently establish an
asymptotic theorem. The polynomial activation oracle also exercises the generic
`phi` derivative order instead of only direct polynomial graph differentiation.

The seven example runs produced, among other formulas, reuse
$E\phi(Z)^2+(E\phi'(Z))^2$, cubic reuse 24, moving-flow second derivative 120,
frozen-direction second derivative 30, and rank-update norm limit 5. The JSON
command completed and produced a parseable representation when generated.

The additional review script, preserved verbatim below, checks:

1. Coupled vector/matrix/scalar gradient-flow observable jets of orders 0–3
   against a separate dense rational series recurrence. For
   $z=Wx$, $h=z^3$, $v=W^\top h$, $a=\operatorname{mean}(h)$, it uses
   $O=\operatorname{mean}(v^2)+a^2+sa$. The dense adjoints are
   $b_v=2v$, $b_h=Wb_v+(2a+s)\mathbf1$, $b_z=3z^2\odot b_h$,
   and velocities are
   $\dot x=-W^\top b_z$,
   $\dot W=-(b_zx^\top+hb_v^\top)/n$, $\dot s=-a$.
   The recurrence independently extracts coefficient $r$ of the velocity and
   divides by $r+1$; it does not use production AD or Gaussian reduction.
2. Nested cubic nonlinearities, two named matrices, reverse/forward reuse,
   shifted roots, and scalar feedback. An independent expression-to-polynomial
   interpreter and Gaussian covariance-pairing recurrence evaluate each DAG
   atom, and generic cubic `phi` agrees with explicitly expanded cubic graphs.
   This is an independent integration check, but the compared graphs share the
   production response compiler; it is not a separate proof of that compiler.
3. Earlier-atom-only integrands/covariances and a source-free polynomial scalar
   output on that complex graph.
4. Two identical matrix queries with linear alias $z=y_1+2y_2$: the independent
   closed expectation for $\operatorname{mean}(x\odot W^\top z^3)$ is 81.
   Both source slots survive and their formal derivatives contain no alias.
5. The two contract counterexamples above.

Every additional verification assertion passed. There was no empirical
large-width reproduction and no exhaustive graph enumeration. Structural
inspection plus these finite exact checks cannot exclude all future large-graph
or resource-limit failures.

## Exact additional probe source

The scratch script is duplicated here so this report retains the handwritten
verification source even if generated scratch is later removed.

```python
from fractions import Fraction as F
from functools import lru_cache
from math import factorial
import json, platform, sys
from mfp_compiler import Program, ProgramError
from mfp_finite import evaluate_finite
import mfp_expr as ex

print('Python:', sys.version.replace('\n', ' '))
print('Platform:', platform.platform())

# Independent fixed-order rational series, with ordinary dense matrix arithmetic.
R = 3
class Series:
    def __init__(self, c): self.c = tuple(F(c[k]) if k < len(c) else F(0) for k in range(R+1))
    @staticmethod
    def wrap(x): return x if isinstance(x, Series) else Series([x])
    def __add__(self, b):
        b=self.wrap(b); return Series([self.c[k]+b.c[k] for k in range(R+1)])
    __radd__=__add__
    def __neg__(self): return Series([-x for x in self.c])
    def __sub__(self,b): return self+-self.wrap(b)
    def __mul__(self,b):
        b=self.wrap(b); return Series([sum(self.c[j]*b.c[k-j] for j in range(k+1)) for k in range(R+1)])
    __rmul__=__mul__
    def __truediv__(self,b): return self* (F(1)/b)
    def __pow__(self,k):
        z=Series([1])
        for _ in range(k): z=z*self
        return z

def mean(a): return sum(a)/len(a)
def mv(a,x,t=False): return [sum((a[j][i] if t else a[i][j])*x[j] for j in range(len(x))) for i in range(len(x))]
def dense(x,w,s):
    n=len(x); z=mv(w,x); h=[v**3 for v in z]; v=mv(w,h,True); a=mean(h)
    o=mean([u**2 for u in v])+a**2+s*a
    bv=[2*u for u in v]
    bh=[u+2*a+s for u in mv(w,bv)]
    bz=[3*u*u*b for u,b in zip(z,bh)]
    gx=mv(w,bz,True)
    gw=[[(bz[i]*x[j]+h[i]*bv[j])/n for j in range(n)] for i in range(n)]
    return o, [-u for u in gx], [[-u for u in row] for row in gw], -a

p=Program(); lo=p.vector_type('lo'); hi=p.vector_type('hi')
x=p.root('x',lo); w=p.matrix('W',lo,hi); s=p.parameter('s')
z=w@x; h=p.phi(z); v=w.T@h; o=p.mean(v**2)+p.mean(h)**2+s*p.mean(h)
g=p.gradient(o,vectors=[x],matrices=[w],scalars=[s]); field={q:-value for q,value in g.items()}
jets=p.jets(o,field,R,moving=True)
xv=[F(1,3),F(-2,5)]; wv=[[F(1,2),F(-1,3)],[F(2,3),F(1,5)]]; sv=F(1,7)
xs=[Series([u]) for u in xv]; ws=[[Series([u]) for u in row] for row in wv]; ss=Series([sv])
for k in range(R):
    _,fx,fw,fs=dense(xs,ws,ss)
    def nextcoef(state,velocity):
        c=list(state.c); c[k+1]=velocity.c[k]/(k+1); return Series(c)
    xs=[nextcoef(a,b) for a,b in zip(xs,fx)]
    ws=[[nextcoef(a,b) for a,b in zip(ar,br)] for ar,br in zip(ws,fw)]
    ss=nextcoef(ss,fs)
reference=dense(xs,ws,ss)[0]
def cubic(k,t): return F(0) if k>3 else factorial(3)//factorial(3-k)*t**(3-k)
for k,jet in enumerate(jets):
    actual=evaluate_finite(jet,2,{x:xv},{w:wv},{s:sv},cubic)
    assert actual==reference.c[k], (k,actual,reference.c[k])
print('PASS: moving vector/matrix/scalar gradient-flow jets orders 0..3 against independent dense Taylor recurrence')

# An independent polynomial interpreter and covariance-pairing integrator for a
# returned symbolic DAG. No production expectation/differentiation operation used.
def scalar(e,env):
    if e.op=='const': return e.value
    if e.op=='symbol': return env[e]
    a=[scalar(x,env) for x in e.args]
    if e.op=='add': return sum(a,F(0))
    if e.op=='mul':
        z=F(1)
        for t in a:z*=t
        return z
    if e.op=='pow':return a[0]**e.value
    if e.op=='phi':return cubic(e.value,a[0])
    raise AssertionError(e.op)

def integrate(e,coords,K,env):
    d=len(coords); zero=(0,)*d
    def plus(a,b):
        z=dict(a)
        for k,v in b.items(): z[k]=z.get(k,F(0))+v
        return {k:v for k,v in z.items() if v}
    def times(a,b):
        z={}
        for k,u in a.items():
            for l,v in b.items():
                m=tuple(i+j for i,j in zip(k,l)); z[m]=z.get(m,F(0))+u*v
        return {k:v for k,v in z.items() if v}
    def power(a,k):
        z={zero:F(1)}
        for _ in range(k):z=times(z,a)
        return z
    def visit(n):
        if n.op=='const':return {zero:n.value}
        if n.op=='symbol':
            if n in coords:
                powers=list(zero);powers[coords.index(n)]=1;return {tuple(powers):F(1)}
            return {zero:env[n]}
        args=[visit(a) for a in n.args]
        if n.op=='add':
            z={}
            for a in args:z=plus(z,a)
            return z
        if n.op=='mul':
            z={zero:F(1)}
            for a in args:z=times(z,a)
            return z
        if n.op=='pow':return power(args[0],n.value)
        if n.op=='phi':
            if n.value>3:return {}
            return {k:factorial(3)//factorial(3-n.value)*v for k,v in power(args[0],3-n.value).items()}
        raise AssertionError(n.op)
    @lru_cache(None)
    def moment(powers):
        if not sum(powers):return F(1)
        if sum(powers)%2:return F(0)
        i=next(k for k,v in enumerate(powers) if v); rem=list(powers);rem[i]-=1
        total=F(0)
        for j,count in enumerate(rem):
            if count:
                rem[j]-=1;total+=count*K[i][j]*moment(tuple(rem));rem[j]+=1
        return total
    return sum(v*moment(k) for k,v in visit(e).items())

def dag_value(dag,params=None):
    env={} if params is None else dict(params)
    for node in dag.expectations:
        assert ex.symbols(node.integrand)-set(node.coordinates)<=env.keys(), ('noncausal integrand',node)
        for row in node.covariance:
            for entry in row:assert ex.symbols(entry)<=env.keys(),('noncausal covariance',node)
        K=tuple(tuple(scalar(e,env) for e in row) for row in node.covariance)
        env[node.symbol]=integrate(node.integrand,node.coordinates,K,env)
    assert ex.symbols(dag.output)<=env.keys()
    def no_phi(e):return e.op!='phi' and all(no_phi(a) for a in e.args)
    assert no_phi(dag.output)
    return scalar(dag.output,env)

def graph(explicit=False):
    p=Program(); a=p.vector_type('a'); b=p.vector_type('b'); c=p.vector_type('c')
    w=p.matrix('W',a,b); v=p.matrix('V',b,c)
    x=p.root('x',a,variance=F(2,3),mean=F(1,5)); one=p.one(a)
    phi=(lambda u:u**3) if explicit else p.phi
    z=w@x; h=phi(z); feedback=p.mean(phi(h))+p.mean(x)
    q=w.T@(h*feedback); y=v@phi(w@q)
    result=p.mean(phi(y+p.mean(y)))+p.inner(q,x)
    return p.compile(result)
a=graph(); b=graph(True)
assert dag_value(a)==dag_value(b)
print('PASS: general nested cubic graph, W/V forward/reverse reuse, scalar feedback, causal integrands/covariances, polynomial output; symbolic versus explicit cubic agree')

p=Program(); a=p.vector_type('a'); b=p.vector_type('b'); w=p.matrix('W',a,b); x=p.root('x',a)
y1=w@x;y2=w@x;z=y1+2*y2
for generic in (False,True):
    output=p.inner(x,w.T@(p.phi(z) if generic else z**3))
    dag=p.compile(output,preactivations=[z])
    assert dag_value(dag)==81
    if generic:
        responses=[row for row in dag.trace if row['rule']=='matrix source and response'][-1]['response']
        assert len(responses)==2
        assert all('z_' not in item['formal_derivative'] for item in responses)
print('PASS: singular named sources with weighted integration-only alias; independent limit 81; formal derivatives retain both original slots')

p=Program(); a=p.vector_type('a'); x=p.root('x',a); output=p.mean(p.freeze(x)**2)
derivative=p.directional(output,{x:p.one(a)})
base=evaluate_finite(output,2,{x:[1,2]},{}); shifted=evaluate_finite(output,2,{x:[2,3]},{}); slope=evaluate_finite(derivative,2,{x:[1,2]}, {})
assert (base,shifted,slope)==(F(5,2),F(13,2),F(0))
print('SCOPE COUNTEREXAMPLE: O(x)=mean(freeze(x)^2), x=(1,2), direction=(1,1): AD=0; ordinary derivative=3 (values 5/2 at t=0, 13/2 at t=1).')

# A front-end contract probe, reported as a minor accepted-input discrepancy.
p=Program(); a=p.vector_type('a'); x=p.root('numeric_text_covariance',a,variance='1')
assert p.compile(p.mean(x*x)).output==ex.const(1)
print('MINOR CONTRACT EDGE: a numeric string root variance is accepted via Fraction(str(v)); docs describe numeric covariance inputs.')
print('All verification assertions passed.')
```

## Corrected-candidate verification and final verdict

**Final verdict: PASS for this internal implementation review; C1 and C2 are
resolved.** This supersedes the baseline request for corrections above. The
baseline findings, hashes, and evidence remain preserved. The original review
limitations still apply: this is not promotion approval or a separate complete
analytic proof audit.

The supervisor froze a corrected candidate after the baseline review. I read
the three changed files completely: `mfp_compiler.py` lines 1–785,
`test_mfp_compiler.py` lines 1–502, and `compiler_usage.md` lines 1–254.
The other five input hashes were unchanged. I independently verified the exact
change scope by reversing only the specified edits in memory and recovering
each changed file's original SHA-256 hash. The record is
`code_review/exact_change_check.txt`; no hidden AD or Gaussian-law algorithm
change was present.

C1 is resolved by the explicit independent-seed-data semantics in the
`freeze`, `directional`, and `gradient` docstrings and in the usage guide.
The guide includes the primal counterexample and distinguishes the enlarged
parameter/seed-space partial derivative from the diagonal value function's
ordinary derivative. It also correctly retains explicit source dependence
during Gaussian response differentiation.

C2 is resolved by a numeric-type gate before covariance conversion. Tests
confirm rejection of numeric text, objects, complex numbers, and nonfinite
floats without reserving the root name. Valid integer, finite-float, and
`Fraction` covariance inputs still evaluate correctly. The two new supplied
regressions cover numeric-text rejection and the frozen-data derivative
convention.

I reran the complete test suite and all substantive baseline probes, replacing
the old numeric-string acceptance assertion with rejection assertions. Additional
checks confirm a frozen primal gradient is zero, its finite/Gaussian value is
retained, and a transpose response still differentiates the seed's source
dependence. Concretely, with standard initialized `W` and `z=W@one`,
the limit of `mean((W.T@freeze(z))**2)` remains 2.

Commands, from `/home/amir/Codes/PDE`:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=studies/mfp_gaussian_master_proof_20261010 \
  python -m unittest -v test_mfp_compiler test_mfp_expr \
  > data/generated/mfp_gaussian_master_proof_20261010/code_review/revised_unittest.log 2>&1
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=studies/mfp_gaussian_master_proof_20261010 \
  python data/generated/mfp_gaussian_master_proof_20261010/code_review/revised_probes.py \
  > data/generated/mfp_gaussian_master_proof_20261010/code_review/revised_probes.log 2>&1
```

Both commands exited zero. **All 53 supplied tests passed in 0.160 seconds**;
every focused probe assertion passed. The revised probe source consists exactly
of the preserved baseline source above up to its final minor-covariance-contract
probe, followed by this replacement suffix:

```python
# Revised numeric covariance gate and freeze boundary checks.
for invalid in ("1", object(), 1j, float("inf"), float("nan")):
    p=Program(); a=p.vector_type("a")
    try: p.root("x",a,variance=invalid)
    except ProgramError: pass
    else: raise AssertionError(("accepted invalid covariance",invalid))
    assert not p.nodes and not p.names
for variance in (1, 0.1, F(1,2)):
    p=Program(); a=p.vector_type("a"); x=p.root("x",a,variance=variance)
    assert p.compile(p.mean(x*x)).output==ex.const(variance)
p=Program(); a=p.vector_type("a"); x=p.root("x",a)
frozen=p.mean(p.freeze(x)**2)
assert evaluate_finite(p.gradient(frozen,vectors=[x])[x],2,{x:[1,2]}, {})==(0,0)
assert p.compile(frozen).output==ex.const(1)
b=p.vector_type("b"); w=p.matrix("W",a,b); z=w@p.one(a)
assert p.compile(p.mean((w.T@p.freeze(z))**2)).output==ex.const(2)
print("PASS: numeric covariance gate rejects text/objects/complex/nonfinite values without reserving names; int/float/Fraction retained")
print("PASS: frozen physical gradient is zero, finite/Gaussian values retained, Gaussian transpose response still differentiates seed source dependence")
print("All revised verification assertions passed.")
```

The revised inputs were hashed before rereading and after verification; all
eight hashes remained identical during this revision check. The records are
`code_review/revised-initial.sha256` and `code_review/revised-final.sha256`.
The three new hashes are:

```text
f6d0b2f786e9a0b676476487dff3e3c393c8fd7145261661d8b45737cae215ce  mfp_compiler.py
6ea8c4943abce850b771b9f3191e1796a99143b2391d15d8850b6c3bc84a386d  test_mfp_compiler.py
f8c7c6acc5931aeabb5efda7ebc9f24e4108c2c4aaeb7c05b48048d7403334ff  compiler_usage.md
```

The five unchanged hashes are those in the baseline table. No unresolved
correctness objection remains within the reviewed implementation scope.
