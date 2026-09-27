# Complete feedback dependency balls and input-identification consistency

2026-09-27. Scoped same-study investigation. This note uses the exact model in
`AGGREGATE_SCALAR_CONSTRUCTION.md` sections 1–2, the gate/tree lift and normalized
bounds in `TRUE_AGGREGATE_CONSTRUCTIVE.md`, and the current scalar compiler.
No other study, population training, or external theorem was used. Required
conjecture-investigation and rigorous-math skills were read.

**Conclusion.** A complete dependency ball around *all* output and feedback
moments repairs a precise nonexhaustion defect of the output-only depth family.
For bounded G, exact or sufficiently accurate initialization, and fixed finite
queries, this family has a compact-time convergence proof by propagation in
dependency distance. The first nontrivial ball is small enough to test on the
two-input case. This is not a proof of useful low-order accuracy. Input alias
consistency is a separate issue: it requires a truncation commuting with input
identification, or explicit canonicalization of known equal inputs. The new
compiler does not claim to solve that issue.

## 1. Contract and the implementable proposal

Keep the exact block-Gaussian response-memory target, its current moving gates,
the actual G/G-transpose correlations, memory order H, and scalar predictions.
The rigorous statement below retains the existing bounded-G hypothesis; it
does not establish an efficient unbounded-Gaussian theorem or a full-circle
decoder. Runtime state consists of scalar current tree contractions and L.
Initialization uses only the allowed initial law or initial finite pool, which
is then discarded. There is no evolved population, density, cell mass, reference
forcing, history tape, or frozen activation dictionary.

Let S be the union of the following trees:

1. Every output F tree, for training and specified queries.
2. Every s tree and both constituents of every t field.
3. Every tree in every exact dot-s field, including cancellations combined by
   the exact symbolic generator.

For each tree v, draw an edge v -> w if the exact derivative of its contraction
contains the contraction w with a coefficient not identically zero. Coefficient
fields use the seed coordinates in S. Define

    R_0 = S,
    R_(J+1) = R_J union {w : v -> w for some v in R_J}.

Retain R_J, evaluate its complete retained derivative rows, and set children
outside R_J to zero. Keep the existing clipping and outward penalty. The
parameter J measures the number of dependency steps separating every seed
from the boundary. Increasing it does not change normalization or coefficients.
No target horizon enters the selected set or equations.

`next_dependency_closure.py` implements this family as

```python
from next_dependency_closure import DependencyClosure
template = DependencyClosure(u, labels, k=4, order=1,
    queries=queries, mark_bound=3., depth=1).compile(
        max_states=100000, max_terms=1000000, seconds=60.)
```

It reuses the exact additive-signature compiler filter. It fixes the existing
selection settings to output_depth=0, dependency_depth=J, augment_outputs=False,
preserve_essential=False, boundary='zero'. Extra protected Gram rows are not
needed for the convergence argument; adding finitely many of them to S would
also give a valid family, at additional cost. The wrapper initializes the
early-limit reporting field before selection so a state cap remains a reported
state cap. It does not modify any existing implementation.

The inherited cooperative compile deadline is not a hard process deadline.
Callers requiring a constructor-inclusive wall cap must retain their existing
outer timer. API compatibility was checked with FastSharedQueryClosure; the
initialization interface is unchanged.

## 2. Why output-only depth does not exhaust the feedback hierarchy

Every derivative graft preserves all existing formal vertices and edges. It
adds decorations or attaches new vertices; it never deletes an existing vertex
or edge. Starting with the F tree, which has one second-layer vertex, no number
of such derivatives can produce an edgeless first-layer tree.

The current output-depth family has a fixed additional base consisting of S,
Gram rows, and the immediate derivatives of the designated essential rows.
In that fixed base, an edgeless first-layer tree has degree at most six. This
can also be read directly from the local formulas: beta dot has degree one;
the edgeless memory term of x dot is a beta times at most four gate factors;
and the differentiated s or Gram tree supplies one other factor.

For any nonzero training input u_a and H>=1, consider the first-layer trees

    x_a^2,
    x_a^5 beta_(0,l),
    x_a^8 beta_(0,l)^2.

The normalized memory part of dot x_a contains, for training index b=a,

    [8 L^4 / (m sqrt(m))] R_a C_aa t_(0,l,a)
                      (1-x_a^2)^2 beta_(0,l).

The leading monomial differentiating x_a^2 produces x_a^5 beta_(0,l).
Differentiating its five x_a factors with the same leading monomial produces
x_a^8 beta_(0,l)^2. The latter has degree ten, is a genuine symbolic derivative
child, and is absent from the fixed first-layer base. It cannot be supplied by
any output-descendant expansion. Further repetition gives
x_a^(2+3n) beta_(0,l)^n, degree 2+4n.

The coefficient can vanish at special states, including initialization when
t=0. That does not make it an identically zero coefficient in the hierarchy.
This proves **nonexhaustion of the current output-only family**, not a lower
bound on its prediction error. It blocks a proof based on sending the boundary
away from every feedback channel. Complete feedback balls do send that boundary
away: the degree-ten example is included once its seed ancestor's derivative
is expanded.

## 3. A convergence lemma in dependency distance

Here is the precise claim. Fix bounded G, k,m,H, a finite query set, bounded
labels, the normalized gate lift of section 11 of
`TRUE_AGGREGATE_CONSTRUCTIVE.md`, and its initial law. Initialize every retained
moment exactly. Then for every T<infinity there are finite C_T,c_T>0, independent
of J, such that the complete dependency closure satisfies

    sup_(0<=t<=T) max_(v in S) |qhat_v(t)-q_v(t)|
                          + sup_(0<=t<=T) |ghat(t)-g(t)|
        <= C_T exp(-c_T J),                         (1)

where g=1/L. Predictions and training loss satisfy the same type of estimate.
The same family is used for every T. The constants can be extremely unfavorable;
no useful numerical exponent is asserted. Gaussian first weights are permitted
because the lifted gates are bounded; the static matrix mark bound remains.

### Proof

Write s=9 and r=10. Each seed has degree at most s, and each derivative edge
increases degree by at most r. Thus

    v in R_j  implies  degree(v) <= s+rj.             (2)

The exact hierarchy has the form

    dot q_v = sum_w a_vw(q_S,g) q_w.

On [0,T], the normalization bounds and the clock lower bound give finite A,B
with

    sum_w |a_vw| <= A degree(v),
    sum_w |a_vw(z)-a_vw(z')|
                    <= B degree(v) ||z-z'||_infinity. (3)

These bounds follow by expanding the finite local formulas. They are stated
and derived for the same lift in the source construction; restricting to
reachable trees does not enlarge them. The norm defining sigma is Lipschitz
even at zero residual. The current row-envelope penalty is bounded by (3)
and suffices to keep |qhat_v|<=2. The fixed degree-majorant penalty also works.
For each exact q_v in [-1,1], the penalty contributes nonpositively to the
upper derivative of |qhat_v-q_v|. Scalar clipping is nonexpansive.

For 0<=j<=J, let E_j be the maximum moment error on R_j together with clock
error. Define missing approximate children to be zero only when comparing
boundary equations. Exact and approximate values then give an error bound of
three for every moment that can enter the finite iteration. Equations (2)–(3)
give the integral inequality

    E_j(t) <= E_j(t0)
       + A(s+rj) integral_(t0)^t E_(j+1)(v) dv
       + B(s+rj) integral_(t0)^t E_0(v) dv.           (4)

At the last step, the missing true child has magnitude at most one. This is
the truncation source; it is not assumed to be small. Its influence must cross
J-j+1 dependency edges to reach R_j.

Choose tau>0 with Ar tau<=1/8. Iterating the first integral n times gives
the factor

    (A tau)^n product_(ell=0)^(n-1)(s+r(j+ell)) / n!
      = (Ar tau)^n (j+s/r)_(n) / n!,                 (5)

where (a)_(n)=a(a+1)...(a+n-1). For a fixed time slab and j at most a small
fixed fraction of the available depth M, taking n=M-j+1 makes (5)
exponentially small in M. To check this directly, replace j+s/r by its ceiling
h. Then (h)_(n)/n! is the binomial coefficient C(h+n-1,n), at most
2^(h+n-1), while (Ar tau)^n<=8^(-n). Since n is proportional to M and h
is at most a small fraction of M plus a constant, the product is <=C exp(-cM).

The sum of factors multiplying errors present at the slab's initial time is

    sum_(n>=0) (Ar tau)^n (j+s/r)_(n)/n!
          = (1-Ar tau)^(-j-s/r) <= C exp(C'j).        (6)

Differentiating this convergent series bounds the iterated kernel of the
E_0 term in (4). First set j=0; its kernel is bounded independently of M.
The integral inequality for E_0 can be solved by iterating its bounded
convolution kernel (equivalently the exponential-series proof of scalar
Gronwall). It gives C[delta+exp(-cM)], where all errors on R_M at slab start
are at most delta. Inserting this bound back into (4) gives, for sufficiently
small fixed alpha>0 and j<=alpha M,

    sup_slab E_j <= C exp(C'j) [delta+exp(-cM)].       (7)

Choose alpha<=1/4 and small enough that C'alpha<c/4. Cover [0,T] by finitely
many slabs. After each slab retain the *estimate* only on R_floor(alpha M);
the actual ODE still retains all R_J. Initially delta=0. On the next slab
the old exponentially small error is multiplied by at most exp(C'alpha M),
and the newly propagated boundary source is exponentially small in the next
available depth. Because the number of slabs is fixed and alpha>0, this
induction yields a positive exponent c_T times J at the final seed level.
Integer floors change constants only. This proves (1).

The clock satisfies g,ghat>=exp[-(2+Y)T] for Y=max|y_b|. Therefore the decoder
f_a=2q_Fa/g is Lipschitz on the relevant compact set, and bounded residuals
transfer prediction error to training-loss error. Finite-precision initial
errors can be included in delta in (7); an exponentially decreasing
initialization error with a sufficiently large fixed exponent for the desired
compact interval gives the same conclusion. This is a condition on actual
initialization accuracy, not a guarantee for the current n=1024 estimate.

### State count

Set C=M+mH+3, where M counts the finite queries including training inputs.
The decorated-tree bound in the source construction and (2) give

    |R_J| <= [64(C+1)^2]^(s+rJ+1).                  (8)

The state dimension is |R_J|+1, independent of original width and run duration.
The bound is exponential in depth. Neither (8) nor (1) asserts uniformity in
k, the mark bound, dataset size, H, or horizon. Combining them gives an
algebraic error-versus-state upper bound at fixed bounded-mark parameters,
with potentially useless exponent. Initialization and compilation remain
separate costs.

## 4. Compile-only feasibility evidence

The frozen count protocol and source hashes are in `NEXT_BOUNDARY_COUNTS.jsonl`.
It used k=4,H=1, a generic 60-degree pair with labels +1,-1, training inputs
only, zero boundary, and caps of seven seconds, 100000 moments, and 600000
retained terms per compilation. Three predetermined compilations ran, with
a 29-second process cap. No training or solver step was run.

| Family | Selected moments | Including clock | Compilation outcome |
| --- | ---: | ---: | --- |
| Current output depth 2 plus essential rows | 2246 | 2247 | Selection complete; row generation hit 7-second cap |
| Complete feedback depth 1 | 1652 | 1653 | Complete, 6.34 seconds |
| Complete feedback depth 2 | 59192 | 59193 | Selection complete; row generation hit 7-second cap |

All three selected-set counts are complete: their dependency-layer arrays
were finalized before the capped row-generation stage. Capped row counts and
term counts are partial. These timings use the original unfiltered compiler
and are not timings for the new exact signature filter. Depth one has fewer
states than output depth two but different equations and fewer output-path
layers; these counts do not establish better accuracy. Depth two grows by
35.8 times over depth one, so the convergence theorem by itself does not make
high depth practical.

`NEXT_BOUNDARY_COMPILER_CHECK.json` records a separate bounded implementation
check: the new wrapper and the existing exact compiler produce identical tree
order and rows for a 294-moment one-training/one-query model; their RHS values,
including active clipping, match bit for bit. The shared query evaluator also
matches bit for bit, and an early one-state cap returns state_limit. These
checks validate the wrapper only. No population or aggregate training occurred.

## 5. What exact input consistency requires

Let a passive input v equal training input u_b. Exact dynamics obey
x_v=x_b and h_v=h_b at every block. Let pi_b replace the passive gate colors
by their training counterparts in every tree. Exact monomial trees satisfy

    q_T = q_(pi_b T).

The exact derivative generator commutes with this substitution, together with
C_vl=C_bl, s_(j,l,v)=s_(j,l,b), and the corresponding dot-s identities.
An arbitrary selected zero boundary does not commute with it: a missing
passive tree can specialize to a retained core tree, or conversely. Initial
agreement then has no reason to remain invariant. Complete dependency balls
improve the approximation family but do not automatically fix this at each J.

There are two distinct repairs.

**Known exact aliases.** Before assigning gate colors, canonicalize exactly
equal requested inputs. Return the existing core prediction for an aliased
query. For exactly antipodal inputs, oddness gives x_-u=-x_u, h_-u=-h_u,
and f(-u)=-f(u), so a signed alias is also valid. This creates no new state
and proves equality at the recognized inputs, but it can hide a discontinuity
between the core and the neighboring passive decoder. Keep the raw passive
copy as a diagnostic when assessing a closure; do not report a canonicalized
alias as evidence that its neighboring query dynamics were repaired.

**A commuting monomial cutoff.** Erase only x/h input labels from each tree,
retaining its graph, local gate multiplicities, and all alpha/beta labels.
Choose retained gate-degree skeletons, and retain *every* coloring of each
selected skeleton by the allowed input labels. Membership then depends only
on a skeleton unchanged by pi_b, so

    T retained  iff  pi_b(T) retained.

The zero-boundary selector consequently commutes with input identification.
Use a common degree-majorant penalty, not a separately combined absolute-row
envelope: identifying colors can merge terms and change absolute coefficient
sums, so the latter penalty need not commute outside the clipping cube.
With an identical penalty coefficient for identified rows, the specialized
approximate equations are the core equations. Uniqueness of the finite
locally Lipschitz ODE then proves that all alias identities persist from
consistent initial values. This is an exact fixed-cutoff consistency lemma.

The cost is explicit. If a skeletal tree has n_v gate decorations at vertex v,
its labeled-vertex coloring count is

    product_v binomial(n_v+M-1,M-1).

Tree automorphisms can only reduce this count. It is bounded by M^d, where
d is the number of gate decorations. A single-query template can be colored
with m training colors plus one passive color and then copied for K requested
queries. No cross-query colors are needed: the exact dynamics of one passive
query depends on the core and itself only. Total state is
N_core+K(N_template-N_core)+1. This repairs consistency but may multiply the
state substantially; no count or training for this saturation was authorized
or performed here. It is a secondary route, not the delivered depth-one model.

## 6. Relation to a current-gate orthogonal polynomial basis

Replacing monomials of current x/h gates by Legendre polynomials is an
admissible aggregate representation. It stores statistics of moving gates.
It is not a frozen feature model. The exact identity

    (1-x^2) P_n'(x)
       = n(n+1)/(2n+1) [P_(n-1)(x)-P_(n+1)(x)]

keeps the activation-derivative cancellation in a short expression and retains
an O(n) coefficient envelope. Multiplication by x has a two-term recurrence
with nonnegative coefficients summing to one, so a fixed-degree local velocity
still produces a bounded degree jump and a coefficient envelope linear in
total degree. Complete feedback expansion can therefore be studied in that
basis as well, once its exact local products and normalization are implemented.

A zero boundary in this basis is mathematically different from a zero
monomial boundary. For example x^2=(1+2P_2(x))/3 retains a constant baseline
when P_2 is omitted. This can repair some cancellations lost by zeroing a high
monomial, but it does not prove positivity or moment realizability. For example

    (1-x^2)^2 = 8/15 -(16/21)P_2(x)+(8/35)P_4(x).

Zeroing the P_4 moment can give a negative answer for admissibly bounded
but unrealizable low moments with E[P_2]>7/10. A small boundary source or a
realizability argument is still needed for an accuracy claim.

Input identification requires special care in a tensor orthogonal basis:

    P_1(x_v) P_1(x_b) at v=b equals [1+2P_2(x_b)]/3.

Thus identifying labels mixes total degrees. Even a total-degree tensor
Legendre cutoff need not commute with aliases; the omitted product can
specialize to a retained constant. The monomial skeleton consistency lemma
above cannot be transferred unchanged. Canonicalize known equal inputs before
assigning orthogonal colors, or impose the resulting linear moment identities
explicitly. Introducing a separate derivative gate d=1-x^2 has the same
obligation: a truncation must preserve its algebraic relations with x, or
the augmented coordinates can develop inconsistent versions of one gate.

## 7. Claim status and next bottleneck

| Claim | Status |
| --- | --- |
| Output-only expansion never reaches certain feedback dependencies | Proved structural nonexhaustion |
| Complete feedback dependency balls are an admissible scalar family | Exact construction |
| Their bounded-mark finite-query compact-time convergence | Proved under the stated initialization and normalization conditions |
| New compiler preserves the selected equations and reports early limits | Checked on the specified bounded implementation test |
| Depth-one feedback closure improves practical fitting | Open; no training here |
| Depth-one closure preserves passive/core equality | Not claimed |
| Gate-skeleton monomial cutoff preserves input identities with compatible penalty | Proved conditional consistency lemma |
| Orthogonal gate basis improves practical boundary behavior | Plausible, untested here |
| Efficient unbounded-Gaussian, whole-circle aggregate closure | Open |

The immediate bottleneck is whether the affordable complete feedback depth-one
closure improves the known hard pair while retaining the successful easy pair.
Keep raw passive-versus-core disagreement as an independent diagnostic.
Failure would reject this affordable witness, not the complete-depth theorem
or the existence of another effective aggregate closure.
